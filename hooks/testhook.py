from utils import only_for_branch, skip_for_branch


@only_for_branch('master')
def test_hook():
    print("running test_hook(runs first, only for master)")


@skip_for_branch('wip', r'wip\/.*')
def test_hook_2():
    print("running test_hook_2(runs second, not for wip)")


test_hook()
test_hook_2()
