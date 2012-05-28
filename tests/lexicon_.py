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
        lex = Lexicon()
        lex['foo'] = 'bar'
        eq_(lex.foo, 'bar')
        lex2 = copy.deepcopy(lex)
        lex2.foo = 'biz'
        assert lex2.foo != lex.foo
