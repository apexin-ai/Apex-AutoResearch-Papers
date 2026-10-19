from __future__ import annotations

import importlib.util
import json
import os
import re
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load_json(relative_path: str) -> dict:
    return json.loads((ROOT / relative_path).read_text())


class ManifestTests(unittest.TestCase):
    def test_task_manifest_defines_the_protocol(self) -> None:
        payload = load_json("configs/tasks.json")
        tasks = payload["tasks"]

        self.assertEqual(
            payload["protocol"],
            {
                "baseline_runs": 1,
                "interventions": 5,
                "limited_budget": True,
            },
        )
        self.assertEqual(len(tasks), 30)
        self.assertEqual([task["index"] for task in tasks], list(range(1, 31)))
        self.assertEqual(len({task["id"] for task in tasks}), 30)
        self.assertEqual(sum(task["ray"] for task in tasks), 4)

    def test_all_tasks_have_repository_and_overlay_entries(self) -> None:
        tasks = load_json("configs/tasks.json")["tasks"]
        task_ids = {task["id"] for task in tasks}
        repositories = load_json("configs/repositories.json")["repositories"]

        self.assertEqual({repository["task"] for repository in repositories}, task_ids)
        self.assertEqual(len(repositories), len(task_ids))
        for repository in repositories:
            self.assertRegex(repository["revision"], re.compile(r"^[0-9a-f]{40}$"))
            patch = repository.get("patch")
            if patch:
                patch_path = (ROOT / patch).resolve()
                self.assertTrue(patch_path.is_relative_to(ROOT.resolve()))
                self.assertTrue(patch_path.is_file())

        for task_id in task_ids:
            for overlay in ("tasks/main", "tasks/ablations/no_feedback"):
                task_dir = ROOT / overlay / task_id
                self.assertTrue(task_dir.is_dir())
                self.assertTrue((task_dir / "baseline.json").is_file())

    def test_no_feedback_driver_truncates_observation_history(self) -> None:
        driver = (ROOT / "runners/no_feedback/run_strict_no_feedback.py").read_text()

        self.assertIn("history[:1]", driver)
        self.assertIn("Baseline observation:", driver)

    def test_random_search_backend_is_deterministic_and_labeled(self) -> None:
        path = ROOT / "baselines/tpe/tpe_backend.py"
        spec = importlib.util.spec_from_file_location("random_search_backend", path)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        call = {
            "history": [],
            "current": {"width": 64},
            "decision_number": 2,
            "search_space": {"width": [64, 128], "depth": [2, 4]},
        }
        with patch.dict(os.environ, {"AUTOREP_AGENT_BACKEND": "random", "AUTOREP_RANDOM_SEED": "42"}):
            first = module.tpe_decision_from_call("unit_task", call, {})
            second = module.tpe_decision_from_call("unit_task", call, {})
        self.assertEqual(first["new_config"], second["new_config"])
        self.assertEqual(first["metadata"]["backend"], "random_search")

    def test_public_runners_accept_all_reported_seeds(self) -> None:
        for relative in (
            "runners/qwen32/run_qwen32_seed.sh",
            "runners/open_weight/run_model_seed.sh",
            "runners/no_feedback/run_qwen32_no_feedback_seed.sh",
            "runners/hpo/run_hpo_seed_phase.sh",
        ):
            self.assertIn("0|1|42", (ROOT / relative).read_text())

    def test_open_weight_multiseed_methods_reference_configured_models(self) -> None:
        methods = load_json("configs/multiseed_runs.json")["methods"]
        models = load_json("configs/models.json")["agent_models"]
        for method in methods:
            if method["type"] not in {"open_weight", "ablation"}:
                continue
            self.assertIn("model_id", method)
            self.assertIn(method["model_id"], models)

    def test_no_feedback_drivers_finalize_seed_and_fallback_metadata(self) -> None:
        for relative in (
            "runners/no_feedback/run_strict_no_feedback.py",
            "tasks/ablations/no_feedback/run_strict_space_agent.py",
        ):
            driver = (ROOT / relative).read_text()
            self.assertIn('payload["replicate_seed"]', driver)
            self.assertIn('payload["fallback_decision_count"]', driver)
            self.assertIn('payload["final_intervention_record"]', driver)
