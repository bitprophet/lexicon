from invoke import Collection
from invocations import docs
from invocations.checks import blacken
from invocations.packaging import release
from invocations.pytest import test, coverage


ns = Collection(test, coverage, release, blacken, docs)
ns.configure({"packaging": {"sign": True}})
