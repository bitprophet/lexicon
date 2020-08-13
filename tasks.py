from invoke import Collection
from invocations.checks import blacken
from invocations.packaging import release
from invocations.testing import test


ns = Collection(test, release, blacken)
ns.configure({"packaging": {"sign": True}})
