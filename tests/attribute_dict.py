import copy

from lexicon import AttributeDict


class AttributeDict_:
    def allows_attribute_reads(self):
        ad = AttributeDict()
        ad["foo"] = "bar"
        assert ad["foo"] == ad.foo

    def allows_attribute_writes(self):
        ad = AttributeDict()
        ad["foo"] = "bar"
        assert ad["foo"] == "bar"
        ad.foo = "notbar"
        assert ad["foo"] == "notbar"

    def honors_attribute_deletion(self):
        ad = AttributeDict()
        ad["foo"] = "bar"
        assert ad.foo == "bar"
        del ad.foo
        assert "foo" not in ad

    def ensures_real_attributes_win(self):
        ad = AttributeDict()
        ad["get"] = "not-a-method"
        assert callable(ad.get)
        assert not isinstance(ad.get, str)

    def ensure_deepcopy_works(self):
        ad = AttributeDict()
        ad["foo"] = "bar"
        assert ad.foo == "bar"
        ad2 = copy.deepcopy(ad)
        ad2.foo = "biz"
        assert ad2.foo != ad.foo

    def dir_shows_keys(self):
        ad = AttributeDict()
        ad["foo"] = "bar"
        assert "foo" in dir(ad)
