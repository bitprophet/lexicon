class AliasDict(dict):
    def __init__(self, *args, **kwargs):
        super(AliasDict, self).__init__(*args, **kwargs)
        self.aliases = {}

    def alias(self, from_, to):
        self.aliases[from_] = to

    def unalias(self, from_):
        del self.aliases[from_]

    def _single(self, key):
        return isinstance(key, basestring)

    def __setitem__(self, key, value):
        # Attribute existence test required to not blow up when deepcopy'd
        if hasattr(self, 'aliases') and key in self.aliases:
            target = self.aliases[key]
            # Single-string targets => direct update
            if self._single(target):
                self[target] = value
            # Multi-string targets => update all
            else:
                for subkey in self.aliases[key]:
                    self[subkey] = value
        else:
            return super(AliasDict, self).__setitem__(key, value)

    def __getitem__(self, key):
        if hasattr(self, 'aliases') and key in self.aliases:
            target = self.aliases[key]
            # Single-string targets => go ahead
            if self._single(target):
                return self[target]
            # Multi-string targets => invalid/undefined
            else:
                raise ValueError("Multi-target aliases have no well-defined value and can't be read.")
        else:
            return super(AliasDict, self).__getitem__(key)

    def __contains__(self, key):
        if hasattr(self, 'aliases') and key in self.aliases:
            target = self.aliases[key]
            # Single-string targets => return whether target exists
            if self._single(target):
                return target in self
            # Multi-string targets => return whether all targets exist
            else:
                return all(subkey in self for subkey in self.aliases[key])
        else:
            return super(AliasDict, self).__contains__(key)

    def __delitem__(self, key):
        if hasattr(self, 'aliases') and key in self.aliases:
            target = self.aliases[key]
            # Single-string targets => direct update
            if self._single(target):
                del self[target]
            # Multi-string targets => update all
            else:
                for subkey in self.aliases[key]:
                    del self[subkey]
        else:
            return super(AliasDict, self).__delitem__(key)
