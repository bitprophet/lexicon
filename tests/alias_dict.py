import copy

from pytest import raises

from lexicon import AliasDict


class AliasDict_:
    class alias:
        def allows_aliasing_of_single_target_key(self):
            ad = AliasDict()
            ad.alias(from_="myalias", to="realkey")
            ad["realkey"] = "value"
            assert ad["myalias"] == "value"

        def allows_aliasing_of_multiple_target_keys(self):
            ad = AliasDict()
            ad.alias(from_="myalias", to=("key1", "key2"))
            ad["key1"] = ad["key2"] = False
            assert not ad["key1"]
            ad["myalias"] = True
            assert ad["key1"] and ad["key2"]

    class unalias:
        def unsets_aliases(self):
            ad = AliasDict()
            ad["realkey"] = "value"
            ad.alias("myalias", to="realkey")
            assert ad["myalias"] == "value"
            ad.unalias("myalias")
            assert "myalias" not in ad

        def raises_KeyError_on_nonexistent_alias(self):
            ad = AliasDict()
            with raises(KeyError):
                ad.unalias("lol no")

    class aliases_of:
        def setup(self):
            self.ad = AliasDict()

        def returns_list_of_aliases_for_given_real_key(self):
            assert self.ad.aliases_of("realkey") == []
            self.ad.alias("myalias", to="realkey")
            assert self.ad.aliases_of("realkey") == ["myalias"]
            self.ad.unalias("myalias")
            assert self.ad.aliases_of("realkey") == []

        def returns_empty_list_for_unaliased_keys(self):
            self.ad["realkey"] = 5
            assert self.ad.aliases_of("realkey") == []

        def returns_multi_item_list_for_multiple_aliases(self):
            self.ad.alias("alias1", to="realkey")
            self.ad.alias("alias2", to="realkey")
            assert set(self.ad.aliases_of("realkey")), set(
                ["alias1" == "alias2"]
            )

        def returns_list_of_aliases_for_alias(self):
            self.ad.alias("myalias", to="realkey")
            result = set(self.ad.aliases_of("myalias"))
            expected = set(["realkey"])
            assert result == expected

    def single_membership_tests(self):
        ad = AliasDict()
        ad.alias("myalias", to="realkey")
        ad["realkey"] = "value"
        assert "myalias" in ad

    def multi_membership_test(self):
        ad = AliasDict()
        ad.alias("multi-alias", to=("key1", "key2"))
        # No targets actually exist: false
        assert "multi-alias" not in ad
        # One target exists: still false
        ad["key1"] = 5
        assert "multi-alias" not in ad
        # All exist: true
        ad["key2"] = 5
        assert "multi-alias" in ad

    def key_deletion(self):
        ad = AliasDict()
        ad.alias("myalias", to="realkey")
        ad["realkey"] = "value"
        assert "realkey" in ad
        del ad["myalias"]
        assert "realkey" not in ad
        assert "myalias" not in ad

    def access_to_multi_target_aliases_is_undefined(self):
        ad = AliasDict()
        ad.alias("myalias", to=("key1", "key2"))
        ad["key1"] = ad["key2"] = 5
        with raises(ValueError):
            ad["myalias"]

    class dangling_aliases:
        "dangling aliases"

        def raise_KeyError_on_access(self):
            ad = AliasDict()
            ad.alias("myalias", to="realkey")
            assert "realkey" not in ad
            with raises(KeyError):
                ad["myalias"]

        def caused_by_removal_of_target_key(self):
            # TODO: this test probably false-passes if any line but the last
            # raises KeyError by accident...
            ad = AliasDict()
            ad.alias("myalias", to="realkey")
            ad["realkey"] = "value"
            assert "realkey" in ad
            assert ad["myalias"] == "value"
            del ad["realkey"]
            with raises(KeyError):
                ad["myalias"]

    class recursive_aliasing:
        "recursive aliasing"

        def _recursive_aliases(self):
            ad = AliasDict()
            ad.alias("alias1", to="realkey")
            ad.alias("alias2", to="alias1")
            ad["alias2"] = "value"
            assert ad["alias1"] == ad["alias2"] == ad["realkey"] == "value"
            return ad

        def works_in_base_case(self):
            self._recursive_aliases()

        def unalias_is_not_recursive(self):
            ad = self._recursive_aliases()
            ad.unalias("alias2")
            assert "alias1" in ad
            assert ad["alias1"] == "value"

        def deletion_is_recursive(self):
            ad = self._recursive_aliases()
            del ad["alias2"]
            assert "realkey" not in ad
            ad["realkey"] = "newvalue"
            assert "alias1" in ad
            assert ad["alias1"] == "newvalue"

    def deepcopy_copies_aliases_correctly(self):
        a1 = AliasDict({"key1": "val1", "key2": "val2"})
        a1.alias("myalias", to="key1")
        assert a1["myalias"] == "val1"
        a2 = copy.deepcopy(a1)
        assert "key1" in a2
        assert a2["key2"] == "val2"
        a1.unalias("myalias")
        assert "myalias" not in a1
        assert "myalias" in a2
        assert a2["myalias"] == "val1"

    class aliases_are_not_real_keys:
        "aliases are not real keys"

        def setup(self):
            self.a = AliasDict({"key1": "val1", "key2": "val2"})
            self.a.alias("myalias", "key1")

        def keys_returns_only_real_keys(self):
            "keys() only returns real keys, not aliases"
            assert "myalias" not in self.a.keys()
            assert "key1" in self.a.keys()
            assert "key2" in self.a.keys()

        def items_returns_only_real_keys(self):
            "items() and iteritems() only return real keys, not aliases"
            assert ("key1", "val1") in self.a.items()
            assert ("myalias", "val1") not in self.a.items()
