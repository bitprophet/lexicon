class AliasDict(dict):
    def __init__(self, *args, **kwargs):
        super(AliasDict, self).__init__(*args, **kwargs)
        self.aliases = {}

    def alias(self, from_, to):
        self.aliases[from_] = to

    def unalias(self, from_):
        del self.aliases[from_]

    def _handle(self, key, value, single, multi, unaliased):
        # Attribute existence test required to not blow up when deepcopy'd
        if hasattr(self, 'aliases') and key in self.aliases:
            target = self.aliases[key]
            # Single-string targets
            if isinstance(target, basestring):
                return single(self, target, value)
            # Multi-string targets
            else:
                return multi(self, target, value)
        else:
            return unaliased(self, key, value)

    def _single(self, target):
        return isinstance(target, basestring)

    def __setitem__(self, key, value):
        def single(d, target, value): d[target] = value

        def multi(d, target, value):
            for subkey in target:
                d[subkey] = value

        def unaliased(d, key, value): super(AliasDict, d).__setitem__(key, value)

        return self._handle(key, value, single, multi, unaliased)

    def __getitem__(self, key):
        def single(d, target, value): return d[target]

        def multi(d, target, value):
            msg = "Multi-target aliases have no well-defined value and can't be read."
            raise ValueError(msg)

        def unaliased(d, key, value): return super(AliasDict, d).__getitem__(key)

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

        def multi(d, target, value):
            for subkey in self.aliases[key]:
                del self[subkey]

        def unaliased(d, key, value):
            return super(AliasDict, d).__delitem__(key)

        return self._handle(key, None, single, multi, unaliased)
