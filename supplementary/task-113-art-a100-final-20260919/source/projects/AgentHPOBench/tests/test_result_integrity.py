import tempfile
import unittest
from pathlib import Path

from agenthpobench.evaluation.result_integrity import (
    artifact_integrity_issues,
    embedded_raw_responses,
    fallback_count,
    local_model_integrity_issues,
    model_provenance_matches,
    raw_response_count,
)


class ResultIntegrityTests(unittest.TestCase):
    def test_uses_nested_decision_metadata_when_top_level_is_zero(self):
        payload = {
            "fallback_decision_count": 0,
            "decisions": [
                {"metadata": {"fallback": False}},
                {"metadata": {"fallback": True}},
            ],
        }
        self.assertEqual(fallback_count(payload), 1)

    def test_accepts_numeric_string_explicit_count(self):
        self.assertEqual(fallback_count({"fallback_decision_count": "3"}), 3)

    def test_counts_one_marker_per_mapping(self):
        payload = {
            "decision_history": [
                {"metadata": {"fallback": True, "fallback_used": True}}
            ]
        }
        self.assertEqual(fallback_count(payload), 1)

    def test_does_not_double_count_duplicate_decision_containers(self):
        decision = {"metadata": {"fallback": True}}
        payload = {"decisions": [decision], "decision_history": [decision]}
        self.assertEqual(fallback_count(payload), 1)

    def test_artifact_audit_checks_only_the_selected_run(self):
        with tempfile.TemporaryDirectory() as directory:
            task_dir = Path(directory)
            selected = task_dir / "runs" / "selected"
            stale = task_dir / "runs" / "stale"
            selected.mkdir(parents=True)
            stale.mkdir(parents=True)
            result_path = task_dir / "task_QwenLocal_results.json"
            result_path.write_text("{}")
            (stale / "qwen_error_1.txt").write_text("old error")
            self.assertEqual(
                artifact_integrity_issues(
                    result_path, {"run_id": "selected"}
                ),
                [],
            )
            (selected / "qwen_error_1.txt").write_text("parse failed")
            self.assertEqual(
                artifact_integrity_issues(
                    result_path, {"run_id": "selected"}
                ),
                ["nonempty model-error files: 1"],
            )

    def test_embedded_raw_responses_support_agent_lightning_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            result_path = Path(directory) / "task_QwenLocal_results.json"
            result_path.write_text("{}")
            payload = {
                "decisions": [
                    {
                        "reasoning": "derived explanation",
                        "metadata": {"raw_text": f"raw model output {index}"},
                    }
                    for index in range(5)
                ]
            }
            self.assertEqual(len(embedded_raw_responses(payload)), 5)
            self.assertEqual(raw_response_count(result_path, payload), 5)

            stale = result_path.parent / "runs" / "stale"
            stale.mkdir(parents=True)
            for index in range(5):
                (stale / f"qwen_raw_{index}.txt").write_text("stale output")
            self.assertEqual(raw_response_count(result_path, payload), 5)

    def test_result_dir_scopes_artifact_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            task_dir = Path(directory)
            selected = task_dir / "runs" / "selected"
            stale = task_dir / "runs" / "stale"
            selected.mkdir(parents=True)
            stale.mkdir(parents=True)
            result_path = task_dir / "task_QwenLocal_results.json"
            result_path.write_text("{}")
            (stale / "qwen_error_1.txt").write_text("old error")
            self.assertEqual(
                artifact_integrity_issues(
                    result_path, {"result_dir": str(selected)}
                ),
                [],
            )

    def test_explicit_model_metadata_takes_precedence_over_result_path(self):
        with tempfile.TemporaryDirectory() as directory:
            result_path = (
                Path(directory)
                / "qwen3_32b_seed1"
                / "task_QwenLocal_results.json"
            )
            result_path.parent.mkdir(parents=True)
            result_path.write_text("{}")
            self.assertFalse(
                model_provenance_matches(
                    result_path,
                    {"model_path": "/models/Llama-3.1-8B-Instruct"},
                    "qwen3_32b",
                )
            )
            self.assertTrue(
                model_provenance_matches(
                    result_path,
                    {"model_path": "/models/DeepSeek-R1-Distill-Qwen-14B"},
                    "deepseek_r1_qwen_14b",
                )
            )

    def test_direct_prompt_reasoning_is_an_explicit_legacy_raw_response(self):
        with tempfile.TemporaryDirectory() as directory:
            result_path = Path(directory) / "task_QwenLocal_results.json"
            result_path.write_text("{}")
            payload = {
                "decisions": [
                    {
                        "reasoning": f"decoded model output {index}",
                        "metadata": {"direct_prompt": True},
                    }
                    for index in range(5)
                ]
            }
            self.assertEqual(raw_response_count(result_path, payload), 5)

    def test_strict_local_result_requires_exact_protocol_and_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            task_dir = Path(directory)
            run_id = "qwen3_32b_seed1_task"
            run_dir = task_dir / "runs" / run_id
            run_dir.mkdir(parents=True)
            result_path = task_dir / "task_QwenLocal_results.json"
            result_path.write_text("{}")
            for index in range(1, 6):
                (run_dir / f"qwen_raw_{index}.txt").write_text(
                    f"NEW_CONFIG: {{\"choice\": {index}}}"
                )
            payload = {
                "history": [{"kind": "baseline"}]
                + [
                    {"kind": f"intervention_{index}"}
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
            self.assertEqual(
                local_model_integrity_issues(
                    result_path,
                    payload,
                    expected_seed=1,
                    expected_model="Qwen3-32B",
                ),
                [],
            )

    def test_strict_local_result_reports_fallback_errors_and_missing_raw(self):
        with tempfile.TemporaryDirectory() as directory:
            task_dir = Path(directory)
            run_dir = task_dir / "runs" / "llama_seed42_task"
            run_dir.mkdir(parents=True)
            result_path = task_dir / "task_QwenLocal_results.json"
            result_path.write_text("{}")
            for index in range(1, 5):
                (run_dir / f"model_raw_{index}.txt").write_text("NEW_CONFIG: {}")
            payload = {
                "history": [{} for _ in range(6)],
                "decisions": [
                    {"metadata": {"fallback": index == 4}}
                    for index in range(5)
                ],
                "fallback_decision_count": 0,
                "replicate_seed": 0,
                "run_id": "llama_seed42_task",
                "execution_error": "worker exited",
            }
            issues = local_model_integrity_issues(
                result_path,
                payload,
                expected_seed=42,
                expected_model="Qwen3-32B",
            )
            self.assertIn("fallback decisions: 1", issues)
            self.assertIn("nonempty task-level execution_error", issues)
            self.assertIn("expected 5 nonempty raw responses, got 4", issues)
            self.assertIn("replicate seed mismatch: expected 42, got 0", issues)
            self.assertIn("configured model provenance not found: Qwen3-32B", issues)


if __name__ == "__main__":
    unittest.main()
