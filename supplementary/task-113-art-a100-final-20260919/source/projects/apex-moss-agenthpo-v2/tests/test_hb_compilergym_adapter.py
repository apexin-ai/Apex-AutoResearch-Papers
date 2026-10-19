from __future__ import annotations

import hashlib
import json
import stat
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

from optimization_lab.harness_builder.adapters.compilergym import (
    ADVERSARIAL_CANARY_IDS,
    CBENCH_BENCHMARK_URIS,
    CBENCH_ORDINARY_VALIDATOR_INDICES,
    CBENCH_VALIDATOR_SOURCE_SHA256,
    COMPILER_GYM_EVALUATOR_ID,
    COMPILER_GYM_RELEASE_COMMIT,
    COMPILER_GYM_VERSION,
    LLVM_ACTION_FLAGS,
    LLVM_ENV_ID,
    MAX_ACTIONS,
    OBSERVATION_SPACE,
    REWARD_SPACE,
    ActionSequenceCandidate,
    CandidatePolicyError,
    CompilerGymCbenchAdapter,
    build_preflight_command_plan,
    frozen_contract,
    semantic_validator_allowlist_sha256,
    semantic_validator_ids,
)


BENCHMARK_URI = "benchmark://cbench-v1/qsort"


class FakeActionSpace:
    def __init__(self, flags: tuple[str, ...] = LLVM_ACTION_FLAGS):
        self.flags = list(flags)

    def __getitem__(self, action: str) -> int:
        return self.flags.index(action)


class FakeObservation:
    def __init__(self, env: "FakeCompilerGymEnv"):
        self.env = env

    def __getitem__(self, name: str) -> int:
        assert name == OBSERVATION_SPACE
        return self.env.instruction_count


@dataclass
class FakeValidation:
    benchmark_uri: str
    succeeds: bool = True
    reward_validated: bool = True
    benchmark_semantics_validated: bool = True

    @property
    def state(self) -> SimpleNamespace:
        return SimpleNamespace(benchmark=self.benchmark_uri)

    @property
    def error_details(self) -> str:
        return "wrong output" if not self.succeeds else ""

    def okay(self) -> bool:
        return self.succeeds


class FakeCompilerGymEnv:
    def __init__(
        self,
        benchmark_uri: str,
        *,
        final_adjustment: int = 0,
        reward_adjustment: float = 0,
        validation_succeeds: bool = True,
        reward_validated: bool = True,
        semantics_validated: bool = True,
        action_flags: tuple[str, ...] = LLVM_ACTION_FLAGS,
    ):
        self.expected_benchmark_uri = benchmark_uri
        self.final_adjustment = final_adjustment
        self.reward_adjustment = reward_adjustment
        self.validation_succeeds = validation_succeeds
        self.validation_reward_validated = reward_validated
        self.validation_semantics_validated = semantics_validated
        self.action_space = FakeActionSpace(action_flags)
        self.reward_space = SimpleNamespace(name=REWARD_SPACE)
        self.observation = FakeObservation(self)
        self.stdout = json.dumps(
            {"status": "valid", "normalized_score": 999999}, sort_keys=True
        )
        self.reset_calls: list[str] = []
        self.step_calls: list[int] = []
        self.validate_calls = 0
        self.closed = False
        self.benchmark = ""
        self.instruction_count = 100
        self.episode_reward = 0.0

    def reset(self, *, benchmark: str) -> None:
        assert benchmark == self.expected_benchmark_uri
        self.reset_calls.append(benchmark)
        self.benchmark = benchmark
        self.instruction_count = 100
        self.episode_reward = 0.0

    def step(self, action: int) -> tuple[None, float, bool, dict[str, Any]]:
        self.step_calls.append(action)
        old_count = self.instruction_count
        # Every allowlisted action produces a deterministic reduction in this
        # offline fake; real effectiveness is not assumed by the adapter.
        self.instruction_count -= action % 3 + 1
        if len(self.step_calls) == 3:
            self.instruction_count += self.final_adjustment
        reward = float(old_count - self.instruction_count)
        if len(self.step_calls) == 3:
            reward += self.reward_adjustment
        self.episode_reward += reward
        return None, reward, False, {"candidate_stdout": self.stdout}

    def validate(self) -> FakeValidation:
        self.validate_calls += 1
        return FakeValidation(
            benchmark_uri=self.benchmark,
            succeeds=self.validation_succeeds,
            reward_validated=self.validation_reward_validated,
            benchmark_semantics_validated=self.validation_semantics_validated,
        )

    def close(self) -> None:
        self.closed = True


class FakeEnvFactory:
    def __init__(self, envs: list[FakeCompilerGymEnv]):
        self.pending = list(envs)
        self.calls: list[tuple[str, dict[str, Any]]] = []

    def __call__(self, env_id: str, **kwargs: Any) -> FakeCompilerGymEnv:
        self.calls.append((env_id, kwargs))
        return self.pending.pop(0)


def _candidate_payload(
    *, actions: list[Any] | None = None, benchmark_uri: str = BENCHMARK_URI
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "benchmark_uri": benchmark_uri,
        "actions": (
            actions if actions is not None else ["-mem2reg", "-instcombine", "-dce"]
        ),
    }


def _write_candidate(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_contract_pins_release_benchmark_reward_and_action_space() -> None:
    contract = frozen_contract(BENCHMARK_URI)

    assert COMPILER_GYM_VERSION == "0.2.5"
    assert COMPILER_GYM_RELEASE_COMMIT == (
        "64bdd6cd39967d3d2fe5e6c72deb15e830b838bb"
    )
    assert LLVM_ENV_ID == "llvm-v0"
    assert COMPILER_GYM_EVALUATOR_ID == "compilergym-llvm-ic"
    assert REWARD_SPACE == OBSERVATION_SPACE == "IrInstructionCount"
    assert contract["evaluator_id"] == COMPILER_GYM_EVALUATOR_ID
    assert contract["benchmark_uri"] == BENCHMARK_URI
    assert contract["reward_equation"] == (
        "sum(step_rewards) == initial_ir - final_ir"
    )
    assert len(CBENCH_BENCHMARK_URIS) == 8
    assert "benchmark://cbench-v1/stringsearch2" in CBENCH_BENCHMARK_URIS
    assert "benchmark://cbench-v1/rijndael" not in CBENCH_BENCHMARK_URIS
    assert "benchmark://cbench-v1/blowfish" in CBENCH_BENCHMARK_URIS
    assert "benchmark://cbench-v1/sha" not in CBENCH_BENCHMARK_URIS
    assert contract["semantic_validation"] == "all_frozen_ordinary_callbacks"
    assert contract["semantic_validator_source_sha256"] == (
        CBENCH_VALIDATOR_SOURCE_SHA256
    )
    assert contract["semantic_validator_ids"] == list(
        semantic_validator_ids(BENCHMARK_URI)
    )
    assert contract["semantic_validator_allowlist_sha256"] == (
        semantic_validator_allowlist_sha256(BENCHMARK_URI)
    )
    assert len(CBENCH_ORDINARY_VALIDATOR_INDICES[BENCHMARK_URI]) == 20
    assert len(LLVM_ACTION_FLAGS) == 124
    assert len(set(LLVM_ACTION_FLAGS)) == len(LLVM_ACTION_FLAGS)


@pytest.mark.parametrize(
    ("mutate", "message"),
    [
        (lambda value: {**value, "schema_version": True}, "schema_version"),
        (lambda value: {**value, "schema_version": 2}, "schema_version"),
        (lambda value: {**value, "reward_space": REWARD_SPACE}, "keys differ"),
        (lambda value: {**value, "benchmark_uri": CBENCH_BENCHMARK_URIS[1]}, "lane"),
        (lambda value: {**value, "actions": "-dce"}, "JSON array"),
        (lambda value: {**value, "actions": []}, "length"),
        (lambda value: {**value, "actions": ["-dce"] * (MAX_ACTIONS + 1)}, "length"),
        (lambda value: {**value, "actions": ["-DCE"]}, "allowlist"),
        (lambda value: {**value, "actions": [" -dce"]}, "allowlist"),
        (lambda value: {**value, "actions": [1]}, "must be a string"),
    ],
)
def test_candidate_schema_is_exact_allowlisted_and_bounded(
    mutate: Any, message: str
) -> None:
    payload = mutate(_candidate_payload())

    with pytest.raises(CandidatePolicyError, match=message):
        ActionSequenceCandidate.from_dict(
            payload, expected_benchmark_uri=BENCHMARK_URI
        )


def test_candidate_json_rejects_duplicate_keys_and_nonfinite_numbers() -> None:
    duplicate = (
        b'{"schema_version":1,"schema_version":1,'
        b'"benchmark_uri":"benchmark://cbench-v1/qsort","actions":["-dce"]}'
    )
    nonfinite = (
        b'{"schema_version":NaN,'
        b'"benchmark_uri":"benchmark://cbench-v1/qsort","actions":["-dce"]}'
    )

    with pytest.raises(CandidatePolicyError, match="duplicate"):
        ActionSequenceCandidate.from_bytes(
            duplicate, expected_benchmark_uri=BENCHMARK_URI
        )
    with pytest.raises(CandidatePolicyError, match="non-finite"):
        ActionSequenceCandidate.from_bytes(
            nonfinite, expected_benchmark_uri=BENCHMARK_URI
        )


def test_evaluator_replays_in_two_fresh_envs_and_writes_trusted_json(
    tmp_path: Path,
) -> None:
    candidate_path = tmp_path / "candidate" / "candidate.json"
    candidate_path.parent.mkdir()
    _write_candidate(candidate_path, _candidate_payload())
    first = FakeCompilerGymEnv(BENCHMARK_URI)
    fresh = FakeCompilerGymEnv(BENCHMARK_URI)
    factory = FakeEnvFactory([first, fresh])
    trusted_path = tmp_path / "private" / "supervisor.json"
    adapter = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI,
        env_factory=factory,
        version_getter=lambda: COMPILER_GYM_VERSION,
    )

    result = adapter.evaluate(candidate_path, trusted_path)

    assert result.status == "valid"
    assert result.correct is True
    assert result.replay_verified is True
    assert result.initial_ir_instruction_count == 100
    assert result.final_ir_instruction_count == 94
    assert result.cumulative_reward == 6
    assert result.normalized_score == pytest.approx(100 / 94)
    assert len(factory.calls) == 2
    assert factory.calls == [
        (
            LLVM_ENV_ID,
            {"benchmark": BENCHMARK_URI, "reward_space": REWARD_SPACE},
        ),
        (
            LLVM_ENV_ID,
            {"benchmark": BENCHMARK_URI, "reward_space": REWARD_SPACE},
        ),
    ]
    assert first is not fresh
    assert first.closed and fresh.closed
    assert first.validate_calls == 0
    assert fresh.validate_calls == 1
    assert first.step_calls == fresh.step_calls

    supervisor = json.loads(trusted_path.read_text(encoding="utf-8"))
    assert supervisor == result.to_dict()
    assert supervisor["candidate_sha256"] == hashlib.sha256(
        candidate_path.read_bytes()
    ).hexdigest()
    assert supervisor["normalized_score"] != 999999
    assert "candidate_stdout" not in json.dumps(supervisor)
    assert stat.S_IMODE(trusted_path.stat().st_mode) == 0o600


def test_candidate_cannot_forge_or_overwrite_supervisor_json(tmp_path: Path) -> None:
    candidate_path = tmp_path / "candidate.json"
    payload = {
        **_candidate_payload(),
        "stdout": json.dumps({"status": "valid", "correct": True}),
    }
    _write_candidate(candidate_path, payload)
    trusted_path = tmp_path / "private" / "supervisor.json"
    factory = FakeEnvFactory(
        [FakeCompilerGymEnv(BENCHMARK_URI), FakeCompilerGymEnv(BENCHMARK_URI)]
    )
    adapter = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI, env_factory=factory
    )

    result = adapter.evaluate(candidate_path, trusted_path)

    assert result.status == "policy_rejected"
    assert factory.calls == []
    assert json.loads(trusted_path.read_text())["status"] == "policy_rejected"
    with pytest.raises(FileExistsError):
        adapter.evaluate(candidate_path, trusted_path)
    assert json.loads(trusted_path.read_text())["status"] == "policy_rejected"


def test_candidate_symlink_is_rejected_before_environment_creation(
    tmp_path: Path,
) -> None:
    target = tmp_path / "target.json"
    _write_candidate(target, _candidate_payload())
    candidate_path = tmp_path / "candidate-link.json"
    candidate_path.symlink_to(target)
    factory = FakeEnvFactory(
        [FakeCompilerGymEnv(BENCHMARK_URI), FakeCompilerGymEnv(BENCHMARK_URI)]
    )

    result = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI, env_factory=factory
    ).evaluate(candidate_path, tmp_path / "trusted.json")

    assert result.status == "policy_rejected"
    assert "regular file" in result.error_summary
    assert factory.calls == []


def test_fresh_replay_and_semantic_validation_fail_closed(tmp_path: Path) -> None:
    candidate_path = tmp_path / "candidate.json"
    _write_candidate(candidate_path, _candidate_payload())

    mismatch_factory = FakeEnvFactory(
        [
            FakeCompilerGymEnv(BENCHMARK_URI),
            FakeCompilerGymEnv(BENCHMARK_URI, final_adjustment=1),
        ]
    )
    mismatch = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI, env_factory=mismatch_factory
    ).evaluate(candidate_path, tmp_path / "mismatch.json")

    invalid_factory = FakeEnvFactory(
        [
            FakeCompilerGymEnv(BENCHMARK_URI),
            FakeCompilerGymEnv(BENCHMARK_URI, validation_succeeds=False),
        ]
    )
    invalid = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI, env_factory=invalid_factory
    ).evaluate(candidate_path, tmp_path / "invalid.json")

    assert mismatch.status == "incorrect"
    assert "fresh replay" in mismatch.error_summary
    assert invalid.status == "incorrect"
    assert "semantic validation" in invalid.error_summary


def test_explicit_semantic_validator_allowlist_is_executed_in_order(
    tmp_path: Path,
) -> None:
    candidate_path = tmp_path / "candidate.json"
    _write_candidate(candidate_path, _candidate_payload())
    first = FakeCompilerGymEnv(BENCHMARK_URI)
    fresh = FakeCompilerGymEnv(BENCHMARK_URI)
    calls: list[str] = []

    def loader(uri: str) -> tuple[tuple[str, Any], ...]:
        assert uri == BENCHMARK_URI

        def callback_factory(validator_id: str) -> Any:
            def callback(env: FakeCompilerGymEnv) -> tuple[()]:
                assert env is fresh
                calls.append(validator_id)
                return ()

            return callback

        return tuple(
            (validator_id, callback_factory(validator_id))
            for validator_id in semantic_validator_ids(uri)
        )

    result = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI,
        env_factory=FakeEnvFactory([first, fresh]),
        semantic_validator_loader=loader,
    ).evaluate(candidate_path, tmp_path / "allowlisted.json")

    assert result.status == "valid"
    assert calls == list(semantic_validator_ids(BENCHMARK_URI))
    assert fresh.validate_calls == 0


def test_semantic_validator_allowlist_drift_is_environment_invalid(
    tmp_path: Path,
) -> None:
    candidate_path = tmp_path / "candidate.json"
    _write_candidate(candidate_path, _candidate_payload())

    result = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI,
        env_factory=FakeEnvFactory(
            [FakeCompilerGymEnv(BENCHMARK_URI), FakeCompilerGymEnv(BENCHMARK_URI)]
        ),
        semantic_validator_loader=lambda _uri: (("unexpected", lambda _env: ()),),
    ).evaluate(candidate_path, tmp_path / "drift.json")

    assert result.status == "environment_invalid"
    assert "different allowlist" in result.error_summary


def test_action_execution_failure_is_attributed_to_the_candidate(
    tmp_path: Path,
) -> None:
    candidate_path = tmp_path / "candidate.json"
    _write_candidate(candidate_path, _candidate_payload())

    class RejectingEnv(FakeCompilerGymEnv):
        def step(self, action: int) -> tuple[None, float, bool, dict[str, Any]]:
            raise RuntimeError("LLVM rejected this pass ordering")

    factory = FakeEnvFactory(
        [RejectingEnv(BENCHMARK_URI), FakeCompilerGymEnv(BENCHMARK_URI)]
    )
    result = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI, env_factory=factory
    ).evaluate(candidate_path, tmp_path / "rejected.json")

    assert result.status == "incorrect"
    assert "rejected action" in result.error_summary
    assert factory.pending  # Failure occurs before a second environment is needed.


def test_reward_or_version_drift_is_environment_invalid(tmp_path: Path) -> None:
    candidate_path = tmp_path / "candidate.json"
    _write_candidate(candidate_path, _candidate_payload())
    reward_factory = FakeEnvFactory(
        [
            FakeCompilerGymEnv(BENCHMARK_URI, reward_adjustment=1),
            FakeCompilerGymEnv(BENCHMARK_URI),
        ]
    )
    reward_result = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI, env_factory=reward_factory
    ).evaluate(candidate_path, tmp_path / "reward.json")

    version_factory = FakeEnvFactory(
        [FakeCompilerGymEnv(BENCHMARK_URI), FakeCompilerGymEnv(BENCHMARK_URI)]
    )
    version_result = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI,
        env_factory=version_factory,
        version_getter=lambda: "0.2.4",
    ).evaluate(candidate_path, tmp_path / "version.json")

    assert reward_result.status == "environment_invalid"
    assert "reward equation" in reward_result.error_summary
    assert version_result.status == "environment_invalid"
    assert "version mismatch" in version_result.error_summary
    assert version_factory.calls == []


def test_live_action_and_reward_contract_drift_fail_closed(tmp_path: Path) -> None:
    candidate_path = tmp_path / "candidate.json"
    _write_candidate(candidate_path, _candidate_payload())
    action_factory = FakeEnvFactory(
        [
            FakeCompilerGymEnv(
                BENCHMARK_URI, action_flags=tuple(reversed(LLVM_ACTION_FLAGS))
            ),
            FakeCompilerGymEnv(BENCHMARK_URI),
        ]
    )
    action_result = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI, env_factory=action_factory
    ).evaluate(candidate_path, tmp_path / "actions.json")

    wrong_reward = FakeCompilerGymEnv(BENCHMARK_URI)
    wrong_reward.reward_space = SimpleNamespace(name="IrInstructionCountNorm")
    reward_factory = FakeEnvFactory(
        [wrong_reward, FakeCompilerGymEnv(BENCHMARK_URI)]
    )
    reward_result = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI, env_factory=reward_factory
    ).evaluate(candidate_path, tmp_path / "reward-space.json")

    assert action_result.status == "environment_invalid"
    assert "action space differs" in action_result.error_summary
    assert reward_result.status == "environment_invalid"
    assert "reward space" in reward_result.error_summary


def test_no_effect_sequence_does_not_pass_the_negative_canary(tmp_path: Path) -> None:
    candidate_path = tmp_path / "candidate.json"
    _write_candidate(candidate_path, _candidate_payload(actions=["-barrier"]))

    class NoEffectEnv(FakeCompilerGymEnv):
        def step(self, action: int) -> tuple[None, float, bool, dict[str, Any]]:
            self.step_calls.append(action)
            return None, 0.0, False, {}

    result = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI,
        env_factory=FakeEnvFactory(
            [NoEffectEnv(BENCHMARK_URI), NoEffectEnv(BENCHMARK_URI)]
        ),
    ).evaluate(candidate_path, tmp_path / "no-effect.json")

    assert result.status == "no_effect"
    assert result.correct is True
    assert result.normalized_score == 1.0


def test_preflight_plan_separates_reference_and_adversarial_outputs(
    tmp_path: Path,
) -> None:
    candidate_dir = tmp_path / "candidate-visible"
    trusted_dir = tmp_path / "trusted-private"

    adapter = CompilerGymCbenchAdapter(
        benchmark_uri=BENCHMARK_URI,
        env_factory=FakeEnvFactory(
            [FakeCompilerGymEnv(BENCHMARK_URI), FakeCompilerGymEnv(BENCHMARK_URI)]
        ),
    )
    plan = adapter.build_preflight_command_plan(
        candidate_dir=candidate_dir,
        trusted_result_dir=trusted_dir,
        python_executable="python-pinned",
    )

    assert [item.name for item in plan] == [
        "reference",
        "empty-actions",
        "unknown-action",
        "no-effect",
        "forged-stdout",
    ]
    assert plan[0].kind == "reference"
    assert plan[0].expected_status == "valid"
    assert all(item.kind == "adversarial" for item in plan[1:])
    assert tuple(item.name for item in plan[1:]) == ADVERSARIAL_CANARY_IDS
    assert [item.expected_status for item in plan[1:]] == [
        "policy_rejected",
        "policy_rejected",
        "no_effect",
        "policy_rejected",
    ]
    assert all(item.argv[0] == "python-pinned" for item in plan)
    assert all("compilergym" in " ".join(item.argv) for item in plan)
    assert all(
        Path(item.candidate_path).parent == candidate_dir
        and Path(item.supervisor_json_path).parent == trusted_dir
        for item in plan
    )
    assert "stdout" in plan[-1].candidate_payload
    assert len({item.supervisor_json_path for item in plan}) == len(plan)

    with pytest.raises(ValueError, match="must not overlap"):
        build_preflight_command_plan(
            candidate_dir=candidate_dir, trusted_result_dir=candidate_dir
        )
    with pytest.raises(ValueError, match="must not overlap"):
        build_preflight_command_plan(
            candidate_dir=candidate_dir,
            trusted_result_dir=candidate_dir / "candidate-controlled-child",
        )
