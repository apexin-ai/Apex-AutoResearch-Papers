from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import asdict
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from optimization_lab.generation import FakeGenerator
from optimization_lab.harness_builder.builder_harness import BuilderHarness
from optimization_lab.harness_builder.dual_harness import (
    HarnessWorkspace,
    TaskHarnessArtifact,
    TaskHarnessRuntime,
)
from optimization_lab.harness_builder.dual_runtime import (
    DualHarnessRuntime,
    EvaluationResult,
    PublicEvaluation,
)


def initial_artifact() -> TaskHarnessArtifact:
    return TaskHarnessArtifact.from_dict(
        {
            "schema_version": 1,
            "version": 1,
            "parent_sha256": None,
            "spec": {
                "schema_version": 1,
                "nodes": [
                    {
                        "id": "solve",
                        "kind": "model_call",
                        "role": "solver",
                        "prompt": "Solve this public task: {task}",
                    },
                    {
                        "id": "verify",
                        "kind": "tool_call",
                        "tool": "verify",
                        "input_key": "latest_output",
                    },
                    {"id": "emit", "kind": "emit", "input_key": "latest_output"},
                ],
            },
        }
    )


def evolved_proposal(current: TaskHarnessArtifact) -> str:
    spec = current.spec.to_dict()
    spec["nodes"][0]["prompt"] = (
        f"Revision {current.version + 1}: solve and check edge cases for: {{task}}"
    )
    return json.dumps(
        {
            "schema_version": 1,
            "base_sha256": current.sha256,
            "reason": "make the solving step explicitly inspect edge cases",
            "expected_effect": "reduce avoidable contract failures",
            "artifact": spec,
        }
    )


def run_fixture(artifact_root: Path) -> dict[str, object]:
    workspace = HarnessWorkspace(artifact_root)
    if workspace.current_path.exists():
        current = workspace.current()
    else:
        current = workspace.commit(initial_artifact())
    runtime = DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=FakeGenerator("fixture candidate")),
        builder=BuilderHarness(
            workspace=workspace,
            generator=FakeGenerator(evolved_proposal(current)),
            model="gpt-5.6-sol",
        ),
        solver_model="gpt-5.6-sol",
    )
    result = runtime.run_round(
        run_id=f"round-{current.version}",
        execution_contract_sha256=hashlib.sha256(
            json.dumps(
                {
                    "tools": ["verify:v1"],
                    "evaluator_public_projection": "fixture-score-feedback-v1",
                    "probe": "none",
                },
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest(),
        task="Return a valid public fixture candidate.",
        tools={"verify": lambda value: {"passed": value == "fixture candidate"}},
        evaluator=lambda value: EvaluationResult(
            public=PublicEvaluation(
                1.0 if value == "fixture candidate" else 0.0,
                "public fixture accepted"
                if value == "fixture candidate"
                else "public fixture rejected",
            )
        ),
    )
    return asdict(result)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact-root",
        type=Path,
        default=Path("results/dual-harness-fixture"),
    )
    args = parser.parse_args()
    print(json.dumps(run_fixture(args.artifact_root), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
