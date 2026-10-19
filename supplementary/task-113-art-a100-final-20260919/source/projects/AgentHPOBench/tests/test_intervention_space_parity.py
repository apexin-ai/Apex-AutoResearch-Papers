from __future__ import annotations

import importlib.util
import os
import unittest
from pathlib import Path
from unittest.mock import patch

from analysis.audit_intervention_space_parity import ROOT, audit


TIMEMIXER_RUNNERS = (
    "tasks/main/timemixer_ettm2_96_mse/run_formal_timemixer_ettm2_agent.py",
    "baselines/tpe/timemixer_ettm2_96_mse/run_formal_timemixer_ettm2_agent.py",
    "baselines/bohb/timemixer_ettm2_96_mse/run_formal_timemixer_ettm2_agent.py",
)


def load_runner(relative_path: str):
    path = ROOT / relative_path
    module_name = "space_parity_" + "_".join(path.parts[-4:]).replace(".", "_")
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class InterventionSpaceParityTests(unittest.TestCase):
    def test_literal_spaces_match_across_agents_tpe_and_bohb(self) -> None:
        report = audit()
        self.assertTrue(report["passed"], report)
        self.assertEqual(report["task_count"], 30)
        self.assertEqual(report["literal_space_task_count"], 29)

    def test_random_search_can_sample_each_timemixer_window(self) -> None:
        for relative_path in TIMEMIXER_RUNNERS:
            module = load_runner(relative_path)
            sampled: set[int] = set()
            for seed in range(128):
                with patch.dict(
                    os.environ,
                    {
                        "AUTOREP_AGENT_BACKEND": "random",
                        "AUTOREP_RANDOM_SEED": str(seed),
                    },
                    clear=False,
                ):
                    decision = module.decide_with_qwen([], 0.1779)
                sampled.add(decision["new_config"]["down_sampling_window"])
            self.assertEqual(sampled, {2, 3}, relative_path)


if __name__ == "__main__":
    unittest.main()
