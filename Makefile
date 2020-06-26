lint:
	@python hooks/testhook.py

update_githooks:
	@python -m python_githooks

install:
	pip install -r requirements.txt
