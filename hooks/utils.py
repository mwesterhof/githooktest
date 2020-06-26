from git import Repo

repo = Repo('.')


class only_on_branch:
    def __init__(self, names):
        if type(names) == str:
            names = (names,)
        else:
            names = tuple(names)

        self._valid_branch = repo.active_branch.name in names

    def __call__(self, f):
        def _wrapped(*args, **kwargs):
            if self._valid_branch:
                return f(*args, **kwargs)
        return _wrapped
