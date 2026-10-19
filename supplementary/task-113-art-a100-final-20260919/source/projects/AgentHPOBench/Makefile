PYTHON ?= python3

.PHONY: check test

check:
	$(PYTHON) scripts/validate_release.py
	$(PYTHON) analysis/validate_tasks.py
	$(PYTHON) -m compileall -q agenthpobench analysis scripts tasks/main tasks/ablations/no_feedback baselines runners
	find runners baselines tasks -type f -name '*.sh' -exec bash -n {} +
	for method in random tpe bohb; do AUTOREP_DRY_RUN=1 bash runners/hpo/run_hpo_seed_phase.sh $$method 0 0 nonray; AUTOREP_DRY_RUN=1 bash runners/hpo/run_hpo_seed_phase.sh $$method 0 0 ray; done

test:
	$(PYTHON) -m unittest discover -s tests -v
