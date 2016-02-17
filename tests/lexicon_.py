import copy

from spec import Spec, eq_

from lexicon import Lexicon


class Lexicon_(Spec):
    def attributes_work(self):
        l = Lexicon()
        l.foo = 'bar'
        eq_(l['foo'], l.foo)

    def aliases_work(self):
        l = Lexicon()
        l.alias('foo', to='bar')
        l['bar'] = 'value'
        assert l['foo'] == l['bar'] == 'value'

    def aliases_appear_in_attributes(self):
        l = Lexicon()
        l.alias('foo', to='bar')
        l.foo = 'value'
        assert l.foo == l.bar == l['foo'] == l['bar'] == 'value'

    def aliased_real_attributes_do_not_override_real_attributes(self):
        l = Lexicon()
        l.alias('get', to='notget')
        l.notget = 'value'
        assert callable(l.get)
        assert l.get != 'value'

    def ensure_deepcopy_works(self):
        l = Lexicon()
        l['foo'] = 'bar'
        eq_(l.foo, 'bar')
        l2 = copy.deepcopy(l)
        l2.foo = 'biz'
        assert l2.foo != l.foo

    def dir_only_shows_real_keys(self):
        "dir() only shows real keys-as-attrs, not aliases"
        a = Lexicon({'key1': 'val1', 'key2': 'val2'})
        a.alias('myalias', 'key1')
        assert 'key1' in dir(a)
        assert 'key2' in dir(a)
        assert 'myalias' not in dir(a)
