from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_results", ROOT / "analysis" / "validate_results.py"
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ValidateResultsTests(unittest.TestCase):
    def build_result(self, task_dir: Path) -> tuple[Path, dict]:
        run_id = "qwen3_32b_seed1_example"
        run_dir = task_dir / "runs" / run_id
        run_dir.mkdir(parents=True)
        result_path = task_dir / "example_QwenLocal_results.json"
        result_path.write_text("{}")
        for index in range(1, 6):
            (run_dir / f"qwen_raw_{index}.txt").write_text(
                f"NEW_CONFIG: {{\"choice\": {index}}}"
            )
        payload = {
            "history": [{"kind": "baseline", "metrics": {"accuracy": 0.5}}]
            + [
                {
                    "kind": f"intervention_{index}",
                    "metrics": {"accuracy": 0.5 + index / 100},
                }
                for index in range(1, 6)
            ],
            "decision_history": [
                {"metadata": {"fallback": False}} for _ in range(5)
            ],
            "fallback_decision_count": 0,
            "replicate_seed": 1,
            "run_id": run_id,
            "success": True,
        }
        return result_path, payload

    def test_valid_result_passes_all_strict_checks(self):
        with tempfile.TemporaryDirectory() as directory:
            result_path, payload = self.build_result(Path(directory))
            issues, trace_length, raw_count = MODULE.validate_result(
                "agent_lightning_room_selector",
                result_path,
                payload,
                expected_interventions=5,
                expected_seed=1,
                expected_model="qwen3_32b",
            )
            self.assertEqual(issues, [])
            self.assertEqual(trace_length, 6)
            self.assertEqual(raw_count, 5)

    def test_success_flag_cannot_hide_missing_metric_or_execution_error(self):
        with tempfile.TemporaryDirectory() as directory:
            result_path, payload = self.build_result(Path(directory))
            for item in payload["history"]:
                item.pop("metrics")
            payload["task_error"] = "evaluation failed"
            issues, _, _ = MODULE.validate_result(
                "agent_lightning_room_selector",
                result_path,
                payload,
                expected_interventions=5,
                expected_seed=1,
                expected_model="qwen3_32b",
            )
            self.assertIn("nonempty task-level task_error", issues)
            self.assertIn("final intervention metric missing", issues)


if __name__ == "__main__":
    unittest.main()
