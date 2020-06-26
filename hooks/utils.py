from re import match

from git import Repo

repo = Repo('.')


class FilteredRunner:
    _valid_branch = True

    def __call__(self, f):
        def _wrapped(*args, **kwargs):
            if self._valid_branch:
                return f(*args, **kwargs)
        return _wrapped


class skip_for_branch(FilteredRunner):
    def __init__(self, *names):
        if type(names) == str:
            names = (names,)
        else:
            names = tuple(names)

        self._valid_branch = True
        for name in names:
            if match(name, repo.active_branch.name):
                self._valid_branch = False
                break


class only_for_branch(FilteredRunner):
    def __init__(self, *names):
        if type(names) == str:
            names = (names,)
        else:
            names = tuple(names)

        self._valid_branch = False
        for name in names:
            if match(name, repo.active_branch.name):
                self._valid_branch = True
                break
