from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import math
import numbers
import os
import stat
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol, Sequence


COMPILER_GYM_VERSION = "0.2.5"
COMPILER_GYM_RELEASE_COMMIT = "64bdd6cd39967d3d2fe5e6c72deb15e830b838bb"
COMPILER_GYM_EVALUATOR_ID = "compilergym-llvm-ic"
CBENCH_VALIDATOR_SOURCE_SHA256 = (
    "e6337c70f9a3e83abc8f54d9b4193e7ba51fe853a555fa78e472b2fc87920d88"
)
LLVM_ENV_ID = "llvm-v0"
REWARD_SPACE = "IrInstructionCount"
OBSERVATION_SPACE = "IrInstructionCount"
CANDIDATE_SCHEMA_VERSION = 1
SUPERVISOR_SCHEMA_VERSION = 1
MIN_ACTIONS = 1
MAX_ACTIONS = 64
MAX_CANDIDATE_BYTES = 16 * 1024
ADVERSARIAL_CANARY_IDS = (
    "empty-actions",
    "unknown-action",
    "no-effect",
    "forged-stdout",
)

# These are the eight cBench instances frozen by HB-GEN-1. A candidate is bound
# to one URI by the trusted adapter constructor and cannot redirect evaluation
# to another (possibly easier) member of the suite.
CBENCH_BENCHMARK_URIS = (
    "benchmark://cbench-v1/qsort",
    "benchmark://cbench-v1/bitcount",
    "benchmark://cbench-v1/bzip2",
    "benchmark://cbench-v1/crc32",
    "benchmark://cbench-v1/dijkstra",
    "benchmark://cbench-v1/stringsearch2",
    "benchmark://cbench-v1/blowfish",
    "benchmark://cbench-v1/susan",
)

# CompilerGym v0.2.5 registers one ordinary callback followed by four
# sanitizer callbacks for most cBench datasets. The aggregate ``env.validate``
# path runs all callbacks; on the pinned host its sanitizer callbacks fail even
# for the reference program. HB-GEN-1 therefore executes this exact, audited
# ordinary-callback allowlist and fails closed if source bytes, callback count,
# order, or sanitizer classification drift. The indices are registration
# indices in ``compiler_gym.envs.llvm.datasets.cbench.VALIDATORS``.
_TWENTY_ORDINARY_INDICES = tuple(range(0, 100, 5))
CBENCH_VALIDATOR_REGISTRY_LENGTHS: Mapping[str, int] = {
    "benchmark://cbench-v1/qsort": 100,
    "benchmark://cbench-v1/bitcount": 10,
    "benchmark://cbench-v1/bzip2": 100,
    "benchmark://cbench-v1/crc32": 100,
    "benchmark://cbench-v1/dijkstra": 100,
    "benchmark://cbench-v1/stringsearch2": 4,
    "benchmark://cbench-v1/blowfish": 100,
    "benchmark://cbench-v1/susan": 100,
}
CBENCH_ORDINARY_VALIDATOR_INDICES: Mapping[str, tuple[int, ...]] = {
    "benchmark://cbench-v1/qsort": _TWENTY_ORDINARY_INDICES,
    "benchmark://cbench-v1/bitcount": (0, 5),
    "benchmark://cbench-v1/bzip2": _TWENTY_ORDINARY_INDICES,
    "benchmark://cbench-v1/crc32": _TWENTY_ORDINARY_INDICES,
    "benchmark://cbench-v1/dijkstra": _TWENTY_ORDINARY_INDICES,
    "benchmark://cbench-v1/stringsearch2": (0,),
    "benchmark://cbench-v1/blowfish": _TWENTY_ORDINARY_INDICES,
    "benchmark://cbench-v1/susan": _TWENTY_ORDINARY_INDICES,
}

# Exact LLVM 10 command-line action space shipped by CompilerGym v0.2.5.
# Source: compiler_gym/envs/llvm/service/passes/10.0.0/flags.txt at the pinned
# release commit above. Do not derive this list from candidate-controlled text.
LLVM_ACTION_FLAGS = (
    "-add-discriminators",
    "-adce",
    "-aggressive-instcombine",
    "-alignment-from-assumptions",
    "-always-inline",
    "-argpromotion",
    "-attributor",
    "-barrier",
    "-bdce",
    "-break-crit-edges",
    "-simplifycfg",
    "-callsite-splitting",
    "-called-value-propagation",
    "-canonicalize-aliases",
    "-consthoist",
    "-constmerge",
    "-constprop",
    "-coro-cleanup",
    "-coro-early",
    "-coro-elide",
    "-coro-split",
    "-correlated-propagation",
    "-cross-dso-cfi",
    "-deadargelim",
    "-dce",
    "-die",
    "-dse",
    "-reg2mem",
    "-div-rem-pairs",
    "-early-cse-memssa",
    "-early-cse",
    "-elim-avail-extern",
    "-ee-instrument",
    "-flattencfg",
    "-float2int",
    "-forceattrs",
    "-inline",
    "-insert-gcov-profiling",
    "-gvn-hoist",
    "-gvn",
    "-globaldce",
    "-globalopt",
    "-globalsplit",
    "-guard-widening",
    "-hotcoldsplit",
    "-ipconstprop",
    "-ipsccp",
    "-indvars",
    "-irce",
    "-infer-address-spaces",
    "-inferattrs",
    "-inject-tli-mappings",
    "-instsimplify",
    "-instcombine",
    "-instnamer",
    "-jump-threading",
    "-lcssa",
    "-licm",
    "-libcalls-shrinkwrap",
    "-load-store-vectorizer",
    "-loop-data-prefetch",
    "-loop-deletion",
    "-loop-distribute",
    "-loop-fusion",
    "-loop-guard-widening",
    "-loop-idiom",
    "-loop-instsimplify",
    "-loop-interchange",
    "-loop-load-elim",
    "-loop-predication",
    "-loop-reroll",
    "-loop-rotate",
    "-loop-simplifycfg",
    "-loop-simplify",
    "-loop-sink",
    "-loop-reduce",
    "-loop-unroll-and-jam",
    "-loop-unroll",
    "-loop-unswitch",
    "-loop-vectorize",
    "-loop-versioning-licm",
    "-loop-versioning",
    "-loweratomic",
    "-lower-constant-intrinsics",
    "-lower-expect",
    "-lower-guard-intrinsic",
    "-lowerinvoke",
    "-lower-matrix-intrinsics",
    "-lowerswitch",
    "-lower-widenable-condition",
    "-memcpyopt",
    "-mergefunc",
    "-mergeicmps",
    "-mldst-motion",
    "-sancov",
    "-name-anon-globals",
    "-nary-reassociate",
    "-newgvn",
    "-pgo-memop-opt",
    "-partial-inliner",
    "-partially-inline-libcalls",
    "-post-inline-ee-instrument",
    "-functionattrs",
    "-mem2reg",
    "-prune-eh",
    "-reassociate",
    "-redundant-dbg-inst-elim",
    "-rpo-functionattrs",
    "-rewrite-statepoints-for-gc",
    "-sccp",
    "-slp-vectorizer",
    "-sroa",
    "-scalarizer",
    "-separate-const-offset-from-gep",
    "-simple-loop-unswitch",
    "-sink",
    "-speculative-execution",
    "-slsr",
    "-strip-dead-prototypes",
    "-strip-debug-declare",
    "-strip-nondebug",
    "-strip",
    "-tailcallelim",
    "-mergereturn",
)
LLVM_ACTION_ALLOWLIST = frozenset(LLVM_ACTION_FLAGS)

_CANDIDATE_KEYS = frozenset({"schema_version", "benchmark_uri", "actions"})
_VALID_STATUS = "valid"
_POLICY_REJECTED_STATUS = "policy_rejected"
_INCORRECT_STATUS = "incorrect"
_NO_EFFECT_STATUS = "no_effect"
_ENVIRONMENT_INVALID_STATUS = "environment_invalid"


class CandidatePolicyError(ValueError):
    """The candidate artifact violates the frozen public contract."""


class EvaluatorContractError(RuntimeError):
    """The trusted evaluator does not implement the pinned runtime contract."""


class CandidateValidationError(RuntimeError):
    """Fresh replay or cBench semantic validation rejected the candidate."""


class CompilerGymEnv(Protocol):
    action_space: Any
    reward_space: Any
    observation: Any
    episode_reward: Any
    benchmark: Any

    def reset(self, *, benchmark: str) -> Any: ...

    def step(self, action: int) -> tuple[Any, Any, bool, Mapping[str, Any]]: ...

    def validate(self) -> Any: ...

    def close(self) -> None: ...


EnvFactory = Callable[..., CompilerGymEnv]
VersionGetter = Callable[[], str]
SemanticValidatorLoader = Callable[
    [str], tuple[tuple[str, Callable[[CompilerGymEnv], Any]], ...]
]


def _reject_json_constant(value: str) -> None:
    raise CandidatePolicyError(f"non-finite JSON constant is forbidden: {value}")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CandidatePolicyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _strict_json_object(raw: bytes) -> dict[str, Any]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CandidatePolicyError("candidate JSON must be UTF-8") from exc
    try:
        payload = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_json_constant,
        )
    except CandidatePolicyError:
        raise
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        raise CandidatePolicyError(
            "candidate must contain one valid JSON value"
        ) from exc
    if type(payload) is not dict:
        raise CandidatePolicyError("candidate JSON must be an object")
    return payload


def _canonical_json(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def semantic_validator_ids(benchmark_uri: str) -> tuple[str, ...]:
    """Return the immutable IDs of the callbacks authorized for one task."""

    if benchmark_uri not in CBENCH_ORDINARY_VALIDATOR_INDICES:
        raise ValueError("benchmark URI has no frozen semantic validator set")
    task = benchmark_uri.rsplit("/", 1)[-1]
    return tuple(
        f"cg025:{task}:ordinary:{index:03d}"
        for index in CBENCH_ORDINARY_VALIDATOR_INDICES[benchmark_uri]
    )


def semantic_validator_allowlist_sha256(benchmark_uri: str) -> str:
    payload = {
        "compiler_gym_release_commit": COMPILER_GYM_RELEASE_COMMIT,
        "validator_source_sha256": CBENCH_VALIDATOR_SOURCE_SHA256,
        "benchmark_uri": benchmark_uri,
        "registry_length": CBENCH_VALIDATOR_REGISTRY_LENGTHS[benchmark_uri],
        "validator_ids": list(semantic_validator_ids(benchmark_uri)),
    }
    return _sha256_bytes(_canonical_json(payload))


def _find_closure_value(
    callback: Callable[..., Any],
    name: str,
    *,
    seen: set[int] | None = None,
) -> tuple[bool, Any]:
    """Find a named value through CompilerGym's nested callback wrappers."""

    seen = seen or set()
    if id(callback) in seen:
        return False, None
    seen.add(id(callback))
    try:
        nonlocals = inspect.getclosurevars(callback).nonlocals
    except (TypeError, ValueError):
        return False, None
    if name in nonlocals:
        return True, nonlocals[name]
    for value in nonlocals.values():
        if callable(value):
            found, result = _find_closure_value(value, name, seen=seen)
            if found:
                return True, result
    return False, None


def _load_frozen_ordinary_validators(
    benchmark_uri: str,
) -> tuple[tuple[str, Callable[[CompilerGymEnv], Any]], ...]:
    """Load and mechanically re-derive the pinned ordinary callback set."""

    try:
        from compiler_gym.envs.llvm.datasets import cbench  # type: ignore[import-not-found]
    except ImportError as exc:
        raise EvaluatorContractError("CompilerGym cBench validators are unavailable") from exc

    source_path = Path(cbench.__file__).resolve(strict=True)
    if _sha256_bytes(source_path.read_bytes()) != CBENCH_VALIDATOR_SOURCE_SHA256:
        raise EvaluatorContractError("CompilerGym cBench validator source hash changed")
    callbacks = tuple(cbench.VALIDATORS.get(benchmark_uri, ()))
    expected_length = CBENCH_VALIDATOR_REGISTRY_LENGTHS[benchmark_uri]
    if len(callbacks) != expected_length:
        raise EvaluatorContractError("CompilerGym validator registry length changed")

    ordinary_indices: list[int] = []
    for index, callback in enumerate(callbacks):
        found, sanitizer = _find_closure_value(callback, "sanitizer")
        if not found:
            raise EvaluatorContractError(
                f"CompilerGym validator {index} has no auditable sanitizer binding"
            )
        if sanitizer is None:
            ordinary_indices.append(index)
    expected_indices = CBENCH_ORDINARY_VALIDATOR_INDICES[benchmark_uri]
    if tuple(ordinary_indices) != expected_indices:
        raise EvaluatorContractError("CompilerGym ordinary validator order changed")

    return tuple(
        (validator_id, callbacks[index])
        for validator_id, index in zip(
            semantic_validator_ids(benchmark_uri), expected_indices, strict=True
        )
    )


def _read_candidate_file(path: Path) -> bytes:
    """Read one bounded regular file without following a candidate symlink."""

    try:
        metadata = path.lstat()
    except OSError as exc:
        raise CandidatePolicyError("candidate path is unavailable") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise CandidatePolicyError("candidate path must be a regular file")
    try:
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as source:
            opened_metadata = os.fstat(source.fileno())
            if not stat.S_ISREG(opened_metadata.st_mode):
                raise CandidatePolicyError("candidate path must be a regular file")
            raw = source.read(MAX_CANDIDATE_BYTES + 1)
    except CandidatePolicyError:
        raise
    except OSError as exc:
        raise CandidatePolicyError("candidate path could not be read safely") from exc
    if len(raw) > MAX_CANDIDATE_BYTES:
        raise CandidatePolicyError(
            f"candidate JSON exceeds {MAX_CANDIDATE_BYTES} bytes"
        )
    return raw


@dataclass(frozen=True)
class ActionSequenceCandidate:
    schema_version: int
    benchmark_uri: str
    actions: tuple[str, ...]

    @classmethod
    def from_dict(
        cls,
        payload: Mapping[str, Any],
        *,
        expected_benchmark_uri: str,
    ) -> "ActionSequenceCandidate":
        if type(payload) is not dict:
            raise CandidatePolicyError("candidate payload must be a plain object")
        actual_keys = frozenset(payload)
        if actual_keys != _CANDIDATE_KEYS:
            missing = sorted(_CANDIDATE_KEYS - actual_keys)
            extra = sorted(actual_keys - _CANDIDATE_KEYS)
            raise CandidatePolicyError(
                f"candidate keys differ: missing={missing}, extra={extra}"
            )
        if type(payload["schema_version"]) is not int:
            raise CandidatePolicyError("schema_version must be an integer")
        if payload["schema_version"] != CANDIDATE_SCHEMA_VERSION:
            raise CandidatePolicyError("unsupported candidate schema_version")
        if type(payload["benchmark_uri"]) is not str:
            raise CandidatePolicyError("benchmark_uri must be a string")
        if payload["benchmark_uri"] not in CBENCH_BENCHMARK_URIS:
            raise CandidatePolicyError("benchmark_uri is not in the frozen cBench set")
        if payload["benchmark_uri"] != expected_benchmark_uri:
            raise CandidatePolicyError(
                "candidate benchmark_uri does not match this lane"
            )
        if type(payload["actions"]) is not list:
            raise CandidatePolicyError("actions must be a JSON array")
        actions = tuple(payload["actions"])
        if not MIN_ACTIONS <= len(actions) <= MAX_ACTIONS:
            raise CandidatePolicyError(
                f"actions length must be between {MIN_ACTIONS} and {MAX_ACTIONS}"
            )
        for index, action in enumerate(actions):
            if type(action) is not str:
                raise CandidatePolicyError(f"actions[{index}] must be a string")
            if action not in LLVM_ACTION_ALLOWLIST:
                raise CandidatePolicyError(
                    f"actions[{index}] is not in the CompilerGym v0.2.5 allowlist"
                )
        return cls(
            schema_version=CANDIDATE_SCHEMA_VERSION,
            benchmark_uri=expected_benchmark_uri,
            actions=actions,
        )

    @classmethod
    def from_bytes(
        cls,
        raw: bytes,
        *,
        expected_benchmark_uri: str,
    ) -> "ActionSequenceCandidate":
        if len(raw) > MAX_CANDIDATE_BYTES:
            raise CandidatePolicyError(
                f"candidate JSON exceeds {MAX_CANDIDATE_BYTES} bytes"
            )
        return cls.from_dict(
            _strict_json_object(raw),
            expected_benchmark_uri=expected_benchmark_uri,
        )

    @classmethod
    def from_json(
        cls,
        path: Path,
        *,
        expected_benchmark_uri: str,
    ) -> "ActionSequenceCandidate":
        path = Path(path)
        return cls.from_bytes(
            _read_candidate_file(path), expected_benchmark_uri=expected_benchmark_uri
        )

    @property
    def action_sequence_sha256(self) -> str:
        return _sha256_bytes(_canonical_json(list(self.actions)))

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "benchmark_uri": self.benchmark_uri,
            "actions": list(self.actions),
        }


def frozen_contract(benchmark_uri: str) -> dict[str, Any]:
    if benchmark_uri not in CBENCH_BENCHMARK_URIS:
        raise ValueError("benchmark URI is not in the HB-GEN-1 cBench set")
    return {
        "evaluator_id": COMPILER_GYM_EVALUATOR_ID,
        "compiler_gym_version": COMPILER_GYM_VERSION,
        "compiler_gym_release_commit": COMPILER_GYM_RELEASE_COMMIT,
        "environment_id": LLVM_ENV_ID,
        "benchmark_uri": benchmark_uri,
        "reward_space": REWARD_SPACE,
        "observation_space": OBSERVATION_SPACE,
        "reward_equation": "sum(step_rewards) == initial_ir - final_ir",
        "minimum_actions": MIN_ACTIONS,
        "maximum_actions": MAX_ACTIONS,
        "action_allowlist_sha256": _sha256_bytes(
            _canonical_json(list(LLVM_ACTION_FLAGS))
        ),
        "semantic_validation": "all_frozen_ordinary_callbacks",
        "semantic_validator_source_sha256": CBENCH_VALIDATOR_SOURCE_SHA256,
        "semantic_validator_ids": list(semantic_validator_ids(benchmark_uri)),
        "semantic_validator_allowlist_sha256": (
            semantic_validator_allowlist_sha256(benchmark_uri)
        ),
    }


@dataclass(frozen=True)
class SupervisorResult:
    schema_version: int
    status: str
    contract: dict[str, Any]
    contract_sha256: str
    candidate_sha256: str
    action_sequence_sha256: str | None
    action_count: int
    correct: bool
    replay_verified: bool
    reward_validated: bool
    semantics_validated: bool
    initial_ir_instruction_count: int | None
    final_ir_instruction_count: int | None
    cumulative_reward: float | None
    normalized_score: float | None
    error_type: str
    error_summary: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class _ReplayEvidence:
    initial_count: int
    final_count: int
    reward: float


@dataclass(frozen=True)
class PreflightCommand:
    name: str
    kind: str
    candidate_path: str
    supervisor_json_path: str
    argv: tuple[str, ...]
    candidate_payload: dict[str, Any]
    expected_status: str
    expected_exit_code: int

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["argv"] = list(self.argv)
        return payload


def _installed_compiler_gym_version() -> str:
    try:
        import compiler_gym  # type: ignore[import-not-found]
    except ImportError as exc:
        raise EvaluatorContractError("CompilerGym is not installed") from exc
    version = getattr(compiler_gym, "__version__", None)
    if type(version) is not str:
        raise EvaluatorContractError("CompilerGym does not expose __version__")
    return version


def _default_env_factory(env_id: str, **kwargs: Any) -> CompilerGymEnv:
    try:
        import compiler_gym  # type: ignore[import-not-found]
    except ImportError as exc:
        raise EvaluatorContractError("CompilerGym is not installed") from exc
    return compiler_gym.make(env_id, **kwargs)


class CompilerGymCbenchAdapter:
    """Trusted HB-GEN-1 evaluator for a bounded LLVM action sequence.

    The candidate is data, not a process. In particular, candidate stdout is
    never opened or parsed. The only authoritative JSON is constructed from
    trusted environment observations and written to ``supervisor_json_path``
    with exclusive-create semantics.
    """

    def __init__(
        self,
        *,
        benchmark_uri: str,
        env_factory: EnvFactory | None = None,
        version_getter: VersionGetter | None = None,
        semantic_validator_loader: SemanticValidatorLoader | None = None,
    ):
        if benchmark_uri not in CBENCH_BENCHMARK_URIS:
            raise ValueError("benchmark URI is not in the HB-GEN-1 cBench set")
        self.benchmark_uri = benchmark_uri
        self._env_factory = env_factory or _default_env_factory
        # Dependency-injected environments are used by offline tests. Their
        # factory is trusted test infrastructure, while production always
        # queries the installed package version itself.
        self._version_getter = version_getter or (
            _installed_compiler_gym_version
            if env_factory is None
            else lambda: COMPILER_GYM_VERSION
        )
        # Production always uses the audited callback allowlist. An injected
        # environment without an injected loader is an offline unit-test
        # fixture and retains its tiny synthetic validate() contract.
        self._semantic_validator_loader = semantic_validator_loader or (
            _load_frozen_ordinary_validators if env_factory is None else None
        )

    @property
    def contract(self) -> dict[str, Any]:
        return frozen_contract(self.benchmark_uri)

    def build_preflight_command_plan(
        self,
        *,
        candidate_dir: Path,
        trusted_result_dir: Path,
        python_executable: str = sys.executable,
    ) -> tuple[PreflightCommand, ...]:
        return build_preflight_command_plan(
            candidate_dir=candidate_dir,
            trusted_result_dir=trusted_result_dir,
            benchmark_uri=self.benchmark_uri,
            python_executable=python_executable,
        )

    def evaluate(
        self,
        candidate_path: Path,
        supervisor_json_path: Path,
    ) -> SupervisorResult:
        candidate_path = Path(candidate_path)
        supervisor_json_path = Path(supervisor_json_path)
        self._require_separate_paths(candidate_path, supervisor_json_path)
        self._require_new_supervisor_path(supervisor_json_path)

        candidate_sha256 = "0" * 64
        candidate: ActionSequenceCandidate | None = None
        try:
            candidate_bytes = _read_candidate_file(candidate_path)
            candidate_sha256 = _sha256_bytes(candidate_bytes)
            candidate = ActionSequenceCandidate.from_bytes(
                candidate_bytes,
                expected_benchmark_uri=self.benchmark_uri,
            )
        except CandidatePolicyError as exc:
            result = self._result(
                status=_POLICY_REJECTED_STATUS,
                candidate_sha256=candidate_sha256,
                candidate=None,
                error=exc,
            )
            self._write_supervisor_json(supervisor_json_path, result)
            return result

        try:
            self._check_package_version()
            evidence = self._evaluate_with_fresh_replay(candidate)
        except CandidateValidationError as exc:
            result = self._result(
                status=_INCORRECT_STATUS,
                candidate_sha256=candidate_sha256,
                candidate=candidate,
                error=exc,
            )
        except Exception as exc:
            result = self._result(
                status=_ENVIRONMENT_INVALID_STATUS,
                candidate_sha256=candidate_sha256,
                candidate=candidate,
                error=exc,
            )
        else:
            no_effect = evidence.final_count == evidence.initial_count
            result = self._result(
                status=_NO_EFFECT_STATUS if no_effect else _VALID_STATUS,
                candidate_sha256=candidate_sha256,
                candidate=candidate,
                evidence=evidence,
                error=(
                    CandidateValidationError(
                        "action sequence made no measurable instruction-count change"
                    )
                    if no_effect
                    else None
                ),
            )

        self._write_supervisor_json(supervisor_json_path, result)
        return result

    def _check_package_version(self) -> None:
        actual = self._version_getter()
        if actual != COMPILER_GYM_VERSION:
            raise EvaluatorContractError(
                f"CompilerGym version mismatch: actual={actual!r}, "
                f"expected={COMPILER_GYM_VERSION!r}"
            )

    def _evaluate_with_fresh_replay(
        self, candidate: ActionSequenceCandidate
    ) -> _ReplayEvidence:
        discovery_env = self._make_env()
        try:
            discovery = self._run_actions(discovery_env, candidate.actions)
        finally:
            discovery_env.close()

        replay_env = self._make_env()
        if replay_env is discovery_env:
            try:
                replay_env.close()
            finally:
                raise EvaluatorContractError(
                    "env_factory reused an environment; fresh replay is required"
                )
        try:
            replay = self._run_actions(replay_env, candidate.actions)
            if replay != discovery:
                raise CandidateValidationError(
                    "fresh replay did not reproduce instruction counts and reward"
                )
            self._validate_fresh_state(replay_env)
        finally:
            replay_env.close()
        return replay

    def _make_env(self) -> CompilerGymEnv:
        env = self._env_factory(
            LLVM_ENV_ID,
            benchmark=self.benchmark_uri,
            reward_space=REWARD_SPACE,
        )
        if env is None:
            raise EvaluatorContractError("env_factory returned no environment")
        return env

    def _run_actions(
        self, env: CompilerGymEnv, actions: Sequence[str]
    ) -> _ReplayEvidence:
        env.reset(benchmark=self.benchmark_uri)
        self._check_live_environment_contract(env)
        initial_count = self._instruction_count(env)
        rewards: list[float] = []
        for index, action in enumerate(actions):
            try:
                action_id = env.action_space[action]
            except Exception as exc:
                raise EvaluatorContractError(
                    f"pinned action is unavailable at index {index}: {action}"
                ) from exc
            try:
                transition = env.step(action_id)
            except Exception as exc:
                raise CandidateValidationError(
                    f"environment rejected action at index {index}: {action}"
                ) from exc
            if not isinstance(transition, tuple) or len(transition) != 4:
                raise EvaluatorContractError("CompilerGym step() contract changed")
            _, reward, done, _ = transition
            if type(done) is not bool:
                raise EvaluatorContractError("CompilerGym done flag must be boolean")
            if done:
                raise CandidateValidationError(
                    f"environment terminated while replaying action {index}"
                )
            if isinstance(reward, bool) or not isinstance(reward, numbers.Real):
                raise EvaluatorContractError(
                    "IrInstructionCount reward must be numeric"
                )
            reward_float = float(reward)
            if not math.isfinite(reward_float):
                raise EvaluatorContractError("IrInstructionCount reward must be finite")
            rewards.append(reward_float)

        final_count = self._instruction_count(env)
        cumulative_reward = math.fsum(rewards)
        expected_reward = float(initial_count - final_count)
        if not math.isclose(
            cumulative_reward, expected_reward, rel_tol=1e-12, abs_tol=1e-9
        ):
            raise EvaluatorContractError(
                "IrInstructionCount reward equation was not satisfied"
            )
        episode_reward = getattr(env, "episode_reward", None)
        if isinstance(episode_reward, bool) or not isinstance(
            episode_reward, numbers.Real
        ):
            raise EvaluatorContractError("episode_reward must be numeric")
        if not math.isclose(
            float(episode_reward), cumulative_reward, rel_tol=1e-12, abs_tol=1e-9
        ):
            raise EvaluatorContractError("episode_reward differs from step reward sum")
        return _ReplayEvidence(
            initial_count=initial_count,
            final_count=final_count,
            reward=cumulative_reward,
        )

    def _check_live_environment_contract(self, env: CompilerGymEnv) -> None:
        live_flags = getattr(getattr(env, "action_space", None), "flags", None)
        if tuple(live_flags or ()) != LLVM_ACTION_FLAGS:
            raise EvaluatorContractError(
                "live LLVM action space differs from CompilerGym v0.2.5"
            )
        live_reward = getattr(env, "reward_space", None)
        live_reward_name = getattr(live_reward, "name", live_reward)
        if live_reward_name != REWARD_SPACE:
            raise EvaluatorContractError("live reward space is not IrInstructionCount")
        if str(getattr(env, "benchmark", "")) != self.benchmark_uri:
            raise EvaluatorContractError("environment reset to an unexpected benchmark")

    @staticmethod
    def _instruction_count(env: CompilerGymEnv) -> int:
        try:
            value = env.observation[OBSERVATION_SPACE]
        except Exception as exc:
            raise EvaluatorContractError(
                "IrInstructionCount observation is unavailable"
            ) from exc
        if isinstance(value, bool) or not isinstance(value, numbers.Integral):
            raise EvaluatorContractError(
                "IrInstructionCount observation must be an integer"
            )
        count = int(value)
        if count <= 0:
            raise EvaluatorContractError(
                "IrInstructionCount observation must be positive"
            )
        return count

    def _validate_fresh_state(self, env: CompilerGymEnv) -> None:
        if self._semantic_validator_loader is not None:
            validators = self._semantic_validator_loader(self.benchmark_uri)
            expected_ids = semantic_validator_ids(self.benchmark_uri)
            if tuple(validator_id for validator_id, _ in validators) != expected_ids:
                raise EvaluatorContractError(
                    "semantic validator loader returned a different allowlist"
                )
            for validator_id, callback in validators:
                try:
                    outcome = callback(env)
                    errors = tuple(outcome)
                except CandidateValidationError:
                    raise
                except Exception as exc:
                    raise EvaluatorContractError(
                        f"semantic validator {validator_id} could not run"
                    ) from exc
                if errors:
                    error_type = str(getattr(errors[0], "type", "semantic failure"))
                    raise CandidateValidationError(
                        f"fresh cBench semantic validation failed at "
                        f"{validator_id}: {error_type[:120]}"
                    )
            return

        # Offline injected fakes use a compact aggregate object. This branch
        # cannot be reached by the production constructor.
        validation = env.validate()
        okay = getattr(validation, "okay", None)
        if not callable(okay):
            raise EvaluatorContractError("validation result has no okay() method")
        if not bool(getattr(validation, "reward_validated", False)):
            raise EvaluatorContractError(
                "CompilerGym did not validate the deterministic reward"
            )
        if not bool(getattr(validation, "benchmark_semantics_validated", False)):
            raise EvaluatorContractError(
                "cBench benchmark semantics were not exercised by validation"
            )
        if not okay():
            error_details = str(getattr(validation, "error_details", ""))
            raise CandidateValidationError(
                "fresh cBench semantic validation failed"
                + (f": {error_details[:300]}" if error_details else "")
            )
        state = getattr(validation, "state", None)
        if state is None or str(getattr(state, "benchmark", "")) != self.benchmark_uri:
            raise EvaluatorContractError(
                "validation result is not bound to the expected benchmark"
            )

    def _result(
        self,
        *,
        status: str,
        candidate_sha256: str,
        candidate: ActionSequenceCandidate | None,
        evidence: _ReplayEvidence | None = None,
        error: BaseException | None = None,
    ) -> SupervisorResult:
        contract = self.contract
        contract_sha256 = _sha256_bytes(_canonical_json(contract))
        correct = status in {_VALID_STATUS, _NO_EFFECT_STATUS}
        final_count = evidence.final_count if evidence else None
        initial_count = evidence.initial_count if evidence else None
        score = (
            float(initial_count) / float(final_count)
            if initial_count is not None and final_count is not None
            else None
        )
        summary = ""
        if error is not None:
            summary = " ".join(str(error).split())[:500]
        return SupervisorResult(
            schema_version=SUPERVISOR_SCHEMA_VERSION,
            status=status,
            contract=contract,
            contract_sha256=contract_sha256,
            candidate_sha256=candidate_sha256,
            action_sequence_sha256=(
                candidate.action_sequence_sha256 if candidate else None
            ),
            action_count=len(candidate.actions) if candidate else 0,
            correct=correct,
            replay_verified=evidence is not None,
            reward_validated=evidence is not None,
            semantics_validated=evidence is not None,
            initial_ir_instruction_count=initial_count,
            final_ir_instruction_count=final_count,
            cumulative_reward=evidence.reward if evidence else None,
            normalized_score=score,
            error_type=type(error).__name__ if error is not None else "",
            error_summary=summary,
        )

    @staticmethod
    def _require_separate_paths(candidate_path: Path, result_path: Path) -> None:
        candidate_resolved = candidate_path.resolve(strict=False)
        result_resolved = result_path.resolve(strict=False)
        if candidate_resolved == result_resolved:
            raise ValueError("candidate and trusted supervisor JSON paths must differ")

    @staticmethod
    def _require_new_supervisor_path(path: Path) -> None:
        try:
            path.lstat()
        except FileNotFoundError:
            return
        except OSError as exc:
            raise EvaluatorContractError(
                "trusted supervisor JSON path cannot be inspected"
            ) from exc
        raise FileExistsError(f"trusted supervisor JSON already exists: {path}")

    @staticmethod
    def _write_supervisor_json(path: Path, result: SupervisorResult) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        fd = os.open(path, flags, 0o600)
        try:
            payload = _canonical_json(result.to_dict())
            with os.fdopen(fd, "wb", closefd=True) as output:
                fd = -1
                output.write(payload)
                output.flush()
                os.fsync(output.fileno())
        finally:
            if fd >= 0:
                os.close(fd)
        mode = stat.S_IMODE(path.stat().st_mode)
        if mode != 0o600:
            raise EvaluatorContractError(
                f"trusted supervisor JSON mode is {oct(mode)}, expected 0o600"
            )


# Short alias for callers that do not need the suite qualifier.
CompilerGymAdapter = CompilerGymCbenchAdapter


def build_preflight_command_plan(
    *,
    candidate_dir: Path,
    trusted_result_dir: Path,
    benchmark_uri: str = CBENCH_BENCHMARK_URIS[0],
    python_executable: str = sys.executable,
) -> tuple[PreflightCommand, ...]:
    """Return the frozen reference and adversarial Gate-1 command plan.

    The caller materializes each ``candidate_payload`` at ``candidate_path``
    and executes ``argv``. Trusted results live under a separate root and are
    exclusive-created by the supervisor. The forged-stdout case demonstrates
    that candidate-authored status text is rejected as an extra schema field.
    """

    if benchmark_uri not in CBENCH_BENCHMARK_URIS:
        raise ValueError("benchmark URI is not in the HB-GEN-1 cBench set")
    candidate_dir = Path(candidate_dir).resolve(strict=False)
    trusted_result_dir = Path(trusted_result_dir).resolve(strict=False)
    if (
        candidate_dir == trusted_result_dir
        or candidate_dir.is_relative_to(trusted_result_dir)
        or trusted_result_dir.is_relative_to(candidate_dir)
    ):
        raise ValueError("candidate and trusted result roots must not overlap")

    reference = {
        "schema_version": CANDIDATE_SCHEMA_VERSION,
        "benchmark_uri": benchmark_uri,
        "actions": [
            "-mem2reg",
            "-instcombine",
            "-simplifycfg",
            "-reassociate",
            "-gvn",
            "-dce",
        ],
    }
    cases: tuple[tuple[str, str, dict[str, Any], str], ...] = (
        ("reference", "reference", reference, _VALID_STATUS),
        (
            "empty-actions",
            "adversarial",
            {**reference, "actions": []},
            _POLICY_REJECTED_STATUS,
        ),
        (
            "unknown-action",
            "adversarial",
            {**reference, "actions": ["-not-a-compiler-gym-action"]},
            _POLICY_REJECTED_STATUS,
        ),
        (
            "no-effect",
            "adversarial",
            {**reference, "actions": ["-barrier"]},
            _NO_EFFECT_STATUS,
        ),
        (
            "forged-stdout",
            "adversarial",
            {
                **reference,
                "stdout": json.dumps(
                    {
                        "status": _VALID_STATUS,
                        "correct": True,
                        "normalized_score": 999999.0,
                    },
                    sort_keys=True,
                ),
            },
            _POLICY_REJECTED_STATUS,
        ),
    )

    commands: list[PreflightCommand] = []
    for name, kind, payload, expected_status in cases:
        candidate_path = candidate_dir / f"{name}.json"
        supervisor_path = trusted_result_dir / f"{name}.supervisor.json"
        commands.append(
            PreflightCommand(
                name=name,
                kind=kind,
                candidate_path=str(candidate_path),
                supervisor_json_path=str(supervisor_path),
                argv=(
                    python_executable,
                    "-m",
                    "optimization_lab.harness_builder.adapters.compilergym",
                    "evaluate",
                    "--benchmark-uri",
                    benchmark_uri,
                    "--candidate",
                    str(candidate_path),
                    "--supervisor-json",
                    str(supervisor_path),
                ),
                candidate_payload=payload,
                expected_status=expected_status,
                expected_exit_code=0 if expected_status == _VALID_STATUS else 2,
            )
        )
    return tuple(commands)


def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Trusted HB-GEN-1 CompilerGym cBench evaluator"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    evaluate = subparsers.add_parser("evaluate")
    evaluate.add_argument(
        "--benchmark-uri", choices=CBENCH_BENCHMARK_URIS, required=True
    )
    evaluate.add_argument("--candidate", type=Path, required=True)
    evaluate.add_argument("--supervisor-json", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    if args.command != "evaluate":  # pragma: no cover - argparse enforces this.
        raise AssertionError("unreachable command")
    result = CompilerGymCbenchAdapter(
        benchmark_uri=args.benchmark_uri
    ).evaluate(args.candidate, args.supervisor_json)
    # The authoritative record is the private file, not stdout.
    return 0 if result.status == _VALID_STATUS else 2


if __name__ == "__main__":  # pragma: no cover - exercised by the command plan.
    raise SystemExit(main())
