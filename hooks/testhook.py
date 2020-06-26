from hooks.utils import only_on_branch


@only_on_branch('master')
def test_hook():
    print("running test_hook")


test_hook()
