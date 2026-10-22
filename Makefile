PYTHON ?= python3
SEED ?= 20261015

.PHONY: all simulate analyze figures test clean

all:
	$(MAKE) simulate
	$(MAKE) analyze
	$(MAKE) figures

simulate:
	$(PYTHON) simulate.py --seed $(SEED)

analyze:
	$(PYTHON) analyze.py --stage analyze

figures:
	$(PYTHON) analyze.py --stage figures

test:
	$(PYTHON) -m pytest -q

clean:
	rm -rf results .pytest_cache
