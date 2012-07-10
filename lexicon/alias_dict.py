class AliasDict(dict):
    def __init__(self, *args, **kwargs):
        super(AliasDict, self).__init__(*args, **kwargs)
        self.aliases = {}

    def alias(self, from_, to):
        self.aliases[from_] = to

    def unalias(self, from_):
        del self.aliases[from_]

    def aliases_of(self, to):
        return [key for key, value in self.aliases.iteritems() if value == to]

    def _handle(self, key, value, single, multi, unaliased):
        # Attribute existence test required to not blow up when deepcopy'd
        if key in getattr(self, 'aliases', {}):
            target = self.aliases[key]
            # Single-string targets
            if isinstance(target, basestring):
                return single(self, target, value)
            # Multi-string targets
            else:
                if multi:
                    return multi(self, target, value)
                else:
                    for subkey in target:
                        single(self, subkey, value)
        else:
            return unaliased(self, key, value)

    def _single(self, target):
        return isinstance(target, basestring)

    def __setitem__(self, key, value):
        def single(d, target, value): d[target] = value
        def unaliased(d, key, value): super(AliasDict, d).__setitem__(key, value)
        return self._handle(key, value, single, None, unaliased)

    def __getitem__(self, key):
        def single(d, target, value): return d[target]
        def unaliased(d, key, value): return super(AliasDict, d).__getitem__(key)

        def multi(d, target, value):
            msg = "Multi-target aliases have no well-defined value and can't be read."
            raise ValueError(msg)

        return self._handle(key, None, single, multi, unaliased)

    def __contains__(self, key):
        def single(d, target, value): return target in d

        def multi(d, target, value):
            return all(subkey in self for subkey in self.aliases[key])

        def unaliased(d, key, value):
            return super(AliasDict, d).__contains__(key)

        return self._handle(key, None, single, multi, unaliased)

    def __delitem__(self, key):
        def single(d, target, value): del d[target]

        def unaliased(d, key, value):
            return super(AliasDict, d).__delitem__(key)

        return self._handle(key, None, single, None, unaliased)
