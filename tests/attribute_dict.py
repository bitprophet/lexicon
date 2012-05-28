import copy

from spec import Spec, eq_, ok_

from lexicon import AttributeDict


class AttributeDict_(Spec):
    def allows_attribute_reads(self):
        ad = AttributeDict()
        ad['foo'] = 'bar'
        eq_(ad['foo'], ad.foo)

    def allows_attribute_writes(self):
        ad = AttributeDict()
        ad['foo'] = 'bar'
        eq_(ad['foo'], 'bar')
        ad.foo = 'notbar'
        eq_(ad['foo'], 'notbar')

    def honors_attribute_deletion(self):
        ad = AttributeDict()
        ad['foo'] = 'bar'
        eq_(ad.foo, 'bar')
        del ad.foo
        assert 'foo' not in ad

    def ensures_real_attributes_win(self):
        ad = AttributeDict()
        ad['get'] = 'not-a-method'
        assert callable(ad.get)
        assert not isinstance(ad.get, basestring)

    def ensure_deepcopy_works(self):
        ad = AttributeDict()
        ad['foo'] = 'bar'
        eq_(ad.foo, 'bar')
        ad2 = copy.deepcopy(ad)
        ad2.foo = 'biz'
        assert ad2.foo != ad.foo
