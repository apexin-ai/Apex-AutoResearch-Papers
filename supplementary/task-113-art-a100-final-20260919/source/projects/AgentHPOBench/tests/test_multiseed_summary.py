import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "summarize_multiseed", ROOT / "analysis" / "summarize_multiseed.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class MultiseedSummaryTests(unittest.TestCase):
    def test_score_respects_direction_and_bounds(self):
        higher = MODULE.score(
            12.0, {"baseline": 10.0, "anchor": 11.0, "direction": "higher"}
        )
        lower = MODULE.score(
            8.0, {"baseline": 10.0, "anchor": 9.0, "direction": "lower"}
        )
        self.assertEqual(higher["bounded_normalized_score"], 1.0)
        self.assertEqual(lower["bounded_normalized_score"], 1.0)
        self.assertEqual(higher["baseline_win"], 1)
        self.assertEqual(lower["baseline_win"], 1)

    def test_score_treats_serialization_noise_as_a_tie(self):
        reference = {
            "baseline": 70.7127354666,
            "anchor": 3.55,
            "direction": "lower",
        }
        scored = MODULE.score(70.71273546655729, reference)
        self.assertGreater(scored["bounded_normalized_score"], 0.0)
        self.assertEqual(scored["baseline_win"], 0)

    def test_trace_items_requires_baseline_plus_five_interventions(self):
        trace = [{"kind": "baseline"}] + [
            {"kind": f"intervention_{index}"} for index in range(1, 6)
        ]
        items, schema = MODULE.trace_items({"history": trace})
        self.assertEqual(len(items), 6)
        self.assertEqual(schema, "explicit_history")
        with self.assertRaises(ValueError):
            MODULE.trace_items({"history": trace[:-1]})

    def test_fallback_audit_reads_decision_metadata(self):
        payload = {
            "decisions": [
                {"metadata": {"fallback": False}},
                {"metadata": {"fallback": True}},
            ]
        }
        self.assertEqual(MODULE.fallback_count(payload), 1)

    def test_empty_repair_csv_replaces_stale_contents_with_header(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "repair.csv"
            path.write_text("stale\n")
            MODULE.write_csv(path, [], fieldnames=["method", "seed", "task"])
            self.assertEqual(path.read_text(), "method,seed,task\n")

    def test_paper_aggregate_scores_each_seed_before_averaging(self):
        method = {
            "id": "toy",
            "display_name": "Toy",
            "type": "test",
        }
        reference = {
            "category": "Test",
            "direction": "lower",
            "baseline": 10.0,
            "anchor": 5.0,
        }
        rows = []
        for seed, final in zip([0, 1, 42], [20.0, 5.0, 5.0]):
            rows.append(
                {
                    "method": "toy",
                    "display_name": "Toy",
                    "method_type": "test",
                    "seed": seed,
                    "task": "toy_task",
                    **reference,
                    "final": final,
                    "valid": True,
                    "error": "",
                    "result_path": "",
                    **MODULE.score(final, reference),
                }
            )

        summary, task_rows, category_rows = MODULE.aggregate_method(
            method,
            rows,
            [0, 1, 42],
            ["toy_task"],
        )

        paper = summary["paper_aggregate"]
        diagnostic = summary["raw_mean_then_score_diagnostic"]
        self.assertAlmostEqual(paper["mbns"], 1.0 / 3.0)
        self.assertAlmostEqual(paper["bwr_percent"], 200.0 / 3.0)
        self.assertAlmostEqual(paper["maa_percent"], 75.0)
        self.assertAlmostEqual(diagnostic["mbns"], 0.0)
        self.assertAlmostEqual(diagnostic["bwr_percent"], 0.0)
        self.assertAlmostEqual(diagnostic["maa_percent"], 50.0)
        self.assertAlmostEqual(task_rows[0]["seed_bns_mean"], 1.0 / 3.0)
        self.assertAlmostEqual(category_rows[0]["mbns"], 1.0 / 3.0)

    def test_paper_table_excludes_ablation_rows(self):
        summaries = []
        category_rows = []
        for method, method_type in (
            ("main", "open_weight"),
            ("ablation", "ablation"),
        ):
            summaries.append(
                {
                    "method": method,
                    "display_name": method.title(),
                    "method_type": method_type,
                    "protocol_valid": True,
                    "across_seed_summary": {
                        "mbns": {"mean": 0.1, "sd": 0.01},
                        "bwr_percent": {"mean": 50.0, "sd": 1.0},
                        "maa_percent": {"mean": 60.0, "sd": 2.0},
                    },
                }
            )
            for category in MODULE.CATEGORY_ORDER:
                category_rows.append(
                    {
                        "method": method,
                        "category": category,
                        "seed_mbns_mean": 0.1,
                        "seed_mbns_sd": 0.01,
                    }
                )

        rows = MODULE.build_paper_table_rows(summaries, category_rows)

        self.assertEqual([row["method"] for row in rows], ["main"])

    def test_extract_run_applies_local_model_integrity(self):
        with tempfile.TemporaryDirectory() as directory:
            raw_root = Path(directory)
            source = "source"
            task = "agent_lightning_room_selector"
            task_dir = raw_root / source / task
            task_dir.mkdir(parents=True)
            result_path = task_dir / f"{task}_QwenLocal_results.json"
            payload = {
                "history": [
                    {"kind": "baseline", "metrics": {"accuracy": 0.1}},
                    *[
                        {
                            "kind": f"intervention_{index}",
                            "metrics": {"accuracy": 0.1 + index / 100},
                        }
                        for index in range(1, 6)
                    ],
                ],
                "decisions": [
                    {"metadata": {"raw_text": f"output {index}", "fallback": False}}
                    for index in range(5)
                ],
                "fallback_decision_count": 0,
                "replicate_seed": 1,
                "model_path": "/models/Qwen3-8B",
                "success": True,
            }
            result_path.write_text(__import__("json").dumps(payload))
            method = {
                "id": "qwen3_8b",
                "display_name": "Qwen3-8B",
                "type": "open_weight",
                "expected_model": "Qwen3-8B",
                "runs": {"1": [source]},
            }
            reference = {
                "category": "RL",
                "direction": "higher",
                "baseline": 0.1,
                "anchor": 0.5,
            }

            row = MODULE.extract_run(
                method=method,
                seed=1,
                task=task,
                reference=reference,
                raw_root=raw_root,
            )
            self.assertTrue(row["valid"])

            payload["success"] = False
            result_path.write_text(__import__("json").dumps(payload))
            row = MODULE.extract_run(
                method=method,
                seed=1,
                task=task,
                reference=reference,
                raw_root=raw_root,
            )
            self.assertFalse(row["valid"])
            self.assertIn("success=false", row["error"])

            payload["success"] = True
            payload.pop("replicate_seed")
            payload["decisions"][0]["metadata"].pop("raw_text")
            result_path.write_text(__import__("json").dumps(payload))
            compatible_row = MODULE.extract_run(
                method=method,
                seed=1,
                task=task,
                reference=reference,
                raw_root=raw_root,
            )
            self.assertTrue(compatible_row["valid"])

            (result_path.parent / "qwen_error_1.txt").write_text("stale error")
            compatible_row = MODULE.extract_run(
                method=method,
                seed=1,
                task=task,
                reference=reference,
                raw_root=raw_root,
            )
            self.assertTrue(compatible_row["valid"])

            strict_row = MODULE.extract_run(
                method=method,
                seed=1,
                task=task,
                reference=reference,
                raw_root=raw_root,
                require_local_artifacts=True,
            )
            self.assertFalse(strict_row["valid"])
            self.assertIn("missing or invalid replicate_seed", strict_row["error"])
            self.assertIn(
                "expected 5 nonempty raw responses, got 4", strict_row["error"]
            )
            self.assertIn("nonempty model-error files: 1", strict_row["error"])


if __name__ == "__main__":
    unittest.main()
