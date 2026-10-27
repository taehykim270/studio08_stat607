PYTHON ?= python3
SEED ?= 20261015

.PHONY: all simulate analyze figures test clean

all:
	$(MAKE) simulate
	$(MAKE) analyze
# 	$(MAKE) figures

simulate: 
	$(PYTHON) run_simulation.py --seed $(SEED)

results/raw/simulation_results.pkl: simulate

analyze: results/raw/simulation_results.pkl
	$(PYTHON) analyze_results.py --stage analyze

figures: analyze

test:
	$(PYTHON) -m pytest -q

clean:
	rm -rf results .pytest_cache
