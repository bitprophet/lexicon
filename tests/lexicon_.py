import copy

from lexicon import Lexicon


class Lexicon_:
    def attributes_work(self):
        lex = Lexicon()
        lex.foo = "bar"
        assert lex["foo"] == lex.foo

    def aliases_work(self):
        lex = Lexicon()
        lex.alias("foo", to="bar")
        lex["bar"] = "value"
        assert lex["foo"] == lex["bar"] == "value"

    def aliases_appear_in_attributes(self):
        lex = Lexicon()
        lex.alias("foo", to="bar")
        lex.foo = "value"
        assert lex.foo == lex.bar == lex["foo"] == lex["bar"] == "value"

    def aliased_real_attributes_do_not_override_real_attributes(self):
        lex = Lexicon()
        lex.alias("get", to="notget")
        lex.notget = "value"
        assert callable(lex.get)
        assert lex.get != "value"

    def ensure_deepcopy_works(self):
        lex = Lexicon()
        lex["foo"] = "bar"
        assert lex.foo == "bar"
        lex2 = copy.deepcopy(lex)
        lex2.foo = "biz"
        assert lex2.foo != lex.foo

    def dir_only_shows_real_keys(self):
        "dir() only shows real keys-as-attrs, not aliases"
        a = Lexicon({"key1": "val1", "key2": "val2"})
        a.alias("myalias", "key1")
        assert "key1" in dir(a)
        assert "key2" in dir(a)
        assert "myalias" not in dir(a)
