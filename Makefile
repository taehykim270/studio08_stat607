PYTHON ?= python3
SEED ?= 20261015

.PHONY: all simulate analyze figures test clean

all:
	$(MAKE) simulate
	$(MAKE) analyze
# 	$(MAKE) figures

simulate:
	$(PYTHON) run_simulation.py --seed $(SEED)

results/raw/simulation_results.pkl: run_simulation.py scenarios.py $(wildcard src/*.py)
	$(PYTHON) run_simulation.py --seed $(SEED)

analyze: results/raw/simulation_results.pkl
	$(PYTHON) analyze_results.py

figures: analyze

test:
	$(PYTHON) -m pytest -q

clean:
	rm -rf results .pytest_cache
