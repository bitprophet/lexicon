=========
Changelog
=========

- :release:`2.0.0 <2021-07-XX>`
- :support:`-` Dropped support for Python <3.6
- :support:`-` Added a ``_version`` submodule and imported its
  dunder-attributes into the top level module
- :support:`-` Migrated CI to CircleCI (from Travis)
- :support:`-` Migrated tests to pytest(-relaxed)
- :support:`-` Moved changelog to stub Sphinx project for Releases plugin
- :support:`-` Changed README to ReStructured Text (from Markdown)
- :release:`1.0.0 <2016-02-17>`
- :feature:`9` Updated ``AttributeDict`` (and by extension, ``Lexicon``) so it
  displays keys in the output of ``dir()`` (since they're also attributes).
  Thanks to Hugo Oliveira for the initial patch.
- :support:`-` Bumped to 1.0 because clearly this software is pretty stable!
- :release:`0.2.0 <2013-03-07>`
- :bug:`8 major` Python 3 fixes, thanks to Donald Stufft.
- :release:`0.1.2 <2012-07-10>`
- :feature:`- backported` Added ``AliasDict.aliases_of(realkey)`` for reverse
  lookup of what, if any, aliases a given real key has.
