from invoke import Collection
from invocations.testing import test
from invocations.packaging import release

ns = Collection(release, test)
ns.configure({
    'packaging': {
        'sign': True,
        'wheel': True,
    },
})
