from __future__ import annotations

import ast
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNERS = (
    "runners/open_weight/run_model_seed.sh",
    "runners/qwen32/run_qwen32_seed.sh",
    "runners/no_feedback/run_qwen32_no_feedback_seed.sh",
    "runners/hpo/run_hpo_seed_phase.sh",
)


def default_task_list(script: str, variable: str) -> list[str]:
    match = re.search(
        rf'^{variable}="\$\{{AUTOREP_{variable}:-([^}}]+)\}}"$',
        script,
        flags=re.MULTILINE,
    )
    if match is None:
        raise AssertionError(f"cannot find default {variable}")
    return match.group(1).split(",")


def python_task_list(path: Path) -> list[str]:
    tree = ast.parse(path.read_text())
    for node in tree.body:
        if (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == "TASKS"
        ):
            return [task for _, task in ast.literal_eval(node.value)]
    raise AssertionError(f"cannot find TASKS in {path}")


class RunnerTaskSetTests(unittest.TestCase):
    def test_every_public_runner_matches_the_task_manifest_exactly(self):
        tasks = json.loads((ROOT / "configs" / "tasks.json").read_text())["tasks"]
        expected_nonray = [item["id"] for item in tasks if not item["ray"]]
        expected_ray = [item["id"] for item in tasks if item["ray"]]

        for relative in RUNNERS:
            with self.subTest(runner=relative):
                script = (ROOT / relative).read_text()
                nonray = default_task_list(script, "NONRAY_TASKS")
                ray = default_task_list(script, "RAY_TASKS")
                self.assertEqual(nonray, expected_nonray)
                self.assertEqual(ray, expected_ray)
                self.assertEqual(len(set(nonray + ray)), len(tasks))

    def test_agent_lightning_records_template_fallback(self):
        script = (ROOT / "tasks/main/run_strict_space_agent.py").read_text()
        self.assertIn('"fallback": used_fallback', script)

    def test_core_python_runner_matches_the_task_manifest(self):
        tasks = json.loads((ROOT / "configs" / "tasks.json").read_text())["tasks"]
        expected = [item["id"] for item in tasks]
        actual = python_task_list(ROOT / "tasks/main/run_strict_space_agent.py")
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
