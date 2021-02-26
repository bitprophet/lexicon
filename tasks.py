from invoke import Collection
from invocations.checks import blacken
from invocations.packaging import release
from invocations.pytest import test, coverage


ns = Collection(test, coverage, release, blacken)
ns.configure({"packaging": {"sign": True}})
