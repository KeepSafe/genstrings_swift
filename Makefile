# Some simple testing tasks (sorry, UNIX only).

PYTHON=venv/bin/python
PIP=venv/bin/pip
FLAKE=venv/bin/flake8
FLAGS=


update:
	$(PYTHON) ./setup.py install

install:
	virtualenv venv
	$(PYTHON) ./setup.py install

dev:
	$(PIP) install flake8 nose coverage
	$(PIP) install -r requirements.txt
	$(PYTHON) ./setup.py develop

flake:
	$(FLAKE) --exclude=./venv ./
