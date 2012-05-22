from attribute_dict import AttributeDict
from alias_dict import AliasDict


__version__ = "0.1.0"


class Lexicon(AttributeDict, AliasDict):
    def __init__(self, *args, **kwargs):
        # Need to avoid combining AliasDict's initial attribute write on
        # self.aliases, with AttributeDict's __setattr__. Doing so results in
        # an infinite loop. Instead, just skip straight to dict() for both
        # explicitly (i.e. we override AliasDict.__init__ instead of extending
        # it.)
        # NOTE: could tickle AttributeDict.__init__ instead, in case it ever
        # grows one.
        dict.__init__(self, *args, **kwargs)
        dict.__setattr__(self, 'aliases', {})
