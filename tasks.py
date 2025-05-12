from invoke import Collection
from invocations import docs
from invocations.checks import blacken
from invocations.packaging import release
from invocations.pytest import test, coverage


ns = Collection(test, coverage, release, blacken, docs)
ns.configure(
    {
        "packaging": {"sign": False, "changelog_file": "docs/changelog.rst"},
        # TODO: add general opts override and use --extend-exclude, more
        # ergonomic
        "blacken": {"find_opts": r"-and -not -path '*.cci_pycache*'"},
    },
)
