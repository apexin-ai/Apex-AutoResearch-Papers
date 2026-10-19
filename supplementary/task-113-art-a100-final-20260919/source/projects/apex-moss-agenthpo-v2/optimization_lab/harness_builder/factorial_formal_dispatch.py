"""Trusted, zero-call v001 compilation for the exact factorial matrix.

This module closes only the compiler-provenance part of the shared-v001
contract.  It rederives the pinned task authority, replays the exact zero-call
plan, loads the checked-in Rule Registry v3, constructs all four complete
runtime variants internally, and compiles one typed decision four times.  It
does not expose or accept a model, provider, evaluator, transport, budget
governor, subprocess, or execution callback.

The result is compile evidence, not permission to produce or score a solution.
Execution authority and every entitlement remain permanently zero here.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from pathlib import Path
import re
from types import MappingProxyType
from typing import Any, Mapping

from ._safe_artifacts import read_safe_regular_file
from .compile_receipts import HarnessCompileReceipt
from .factorial_contract import (
    DEFAULT_FACTORIAL_MANIFEST,
    factorial_main_arm_variant_projections,
    factorial_main_arm_variant_sha256s,
    verify_factorial_contract,
)
from .factorial_policies import (
    A_FIXED_FEEDBACK,
    ARM_IDS,
    B_FROZEN_WIDE,
    B_TARGETED,
    S_REFLECTION_SKILL,
)
from .factorial_precheck import FactorialFormalZeroCallPlan
from .factorial_task_authority import (
    ExactTaskSeedAuthorityBundle,
    FactorialTaskArtifactAuthority,
)
from .factorial_trunk import (
    ZERO_SHA256,
    TaskSeedKey,
    V001CanonicalCompileContract,
    V001CompileEquivalenceReceipt,
)
from .operators import TrustedOperatorRegistry
from .schema import BuilderVariant, HarnessDecision, RuleRegistry


DEFAULT_RULE_REGISTRY_V3 = (
    Path(__file__).with_name("data") / "rule_registry_v3.json"
)
RULE_REGISTRY_V3_SHA256 = (
    "dc3cd72887cdb5d28a7b273d64047f6f3eda45dc0a51dee4157a8a3d91e091b3"
)
FORMAL_COMPILE_AUTHORITY = "NOT_GRANTED"
_SHA256 = re.compile(r"[0-9a-f]{64}")
_ENTITLEMENT = MappingProxyType(
    {
        "cpu_evaluator_seconds": 0,
        "evaluator_transactions": 0,
        "gpu_exclusive_seconds": 0,
        "model_calls": 0,
    }
)
_ADAPTATION_POLICIES = MappingProxyType(
    {
        A_FIXED_FEEDBACK: "conditional_any_v1",
        S_REFLECTION_SKILL: "conditional_any_v1",
        B_TARGETED: "targeted_any_change_v1",
        B_FROZEN_WIDE: "wide_all_fields_recompile_v1",
    }
)
_ARCHITECTURE_FROZEN = frozenset({A_FIXED_FEEDBACK, S_REFLECTION_SKILL})
_RULE_REGISTRY_V3_EXECUTABLE_RULE_IDS = (
    "contract_compatibility",
    "discipline",
    "dream",
    "law_inversion",
    "recombination",
    "correctness_recovery",
)


def _canonical_bytes(payload: object) -> bytes:
    try:
        return (
            json.dumps(
                payload,
                allow_nan=False,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeError) as exc:
        raise ValueError("formal v001 compile payload is not canonical JSON") from exc


def _digest(payload: object) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _sha(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"invalid formal v001 {label}")
    return value


def _variant_payload(variant: BuilderVariant) -> dict[str, Any]:
    payload = asdict(variant)
    for name in ("allowed_rule_ids", "experience_sources", "excluded_task_ids"):
        payload[name] = list(payload[name])
    return payload


@dataclass(frozen=True)
class FactorialV001RuntimeContract:
    """Complete internally constructed compiler inputs for all four arms."""

    factorial_contract_sha256: str
    rule_registry_sha256: str
    component_catalog_sha256: str
    manifest_arm_variant_sha256s: tuple[tuple[str, str], ...]
    builder_variants: tuple[BuilderVariant, ...]
    schema_version: int = 1
    contract_kind: str = "moss_factorial_v001_runtime_contract_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.contract_kind != (
            "moss_factorial_v001_runtime_contract_v1"
        ):
            raise ValueError("unsupported formal v001 runtime contract")
        for value, label in (
            (self.factorial_contract_sha256, "factorial contract sha256"),
            (self.rule_registry_sha256, "Rule Registry sha256"),
            (self.component_catalog_sha256, "component catalog sha256"),
        ):
            _sha(value, label)
        if tuple(arm for arm, _ in self.manifest_arm_variant_sha256s) != ARM_IDS:
            raise ValueError("formal v001 manifest arm coverage or order differs")
        for _arm, value in self.manifest_arm_variant_sha256s:
            _sha(value, "manifest arm variant sha256")
        if (
            not isinstance(self.builder_variants, tuple)
            or tuple(item.variant_id for item in self.builder_variants) != ARM_IDS
            or any(type(item) is not BuilderVariant for item in self.builder_variants)
        ):
            raise ValueError("formal v001 runtime Builder variants differ")
        if any(
            item.rule_registry_sha256 != self.rule_registry_sha256
            or item.adaptation_policy != _ADAPTATION_POLICIES[item.variant_id]
            or item.freeze_after_initial
            != (item.variant_id in _ARCHITECTURE_FROZEN)
            or item.continual_update
            or item.description
            != "Exact factorial v001 runtime for " + item.variant_id
            or item.allowed_rule_ids != _RULE_REGISTRY_V3_EXECUTABLE_RULE_IDS
            or item.experience_sources
            or item.excluded_task_ids
            for item in self.builder_variants
        ):
            raise ValueError("formal v001 runtime Builder semantics differ")
        manifest = verify_factorial_contract(DEFAULT_FACTORIAL_MANIFEST)
        if (
            self.factorial_contract_sha256 != manifest["contract_digest"]
            or self.rule_registry_sha256 != RULE_REGISTRY_V3_SHA256
            or self.manifest_arm_variant_sha256s
            != tuple(factorial_main_arm_variant_sha256s(manifest).items())
        ):
            raise ValueError("formal v001 runtime source contract differs")

    def to_dict(self) -> dict[str, Any]:
        return {
            "builder_variant_sha256s": {
                item.variant_id: _digest(_variant_payload(item))
                for item in self.builder_variants
            },
            "builder_variants": [
                _variant_payload(item) for item in self.builder_variants
            ],
            "component_catalog_sha256": self.component_catalog_sha256,
            "contract_kind": self.contract_kind,
            "factorial_contract_sha256": self.factorial_contract_sha256,
            "manifest_arm_variant_sha256s": dict(
                self.manifest_arm_variant_sha256s
            ),
            "rule_registry_sha256": self.rule_registry_sha256,
            "schema_version": self.schema_version,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class FactorialV001TrustedCompileReceipt:
    """Zero-authority binding of one trusted four-arm v001 recompilation."""

    formal_plan_sha256: str
    task_authority_bundle_sha256: str
    task_seed_key_sha256: str
    source_locked_task_artifact_sha256: str
    context_binding_sha256: str
    decision_sha256: str
    runtime_contract_sha256: str
    canonical_compile_contract_sha256: str
    compile_equivalence_receipt_sha256: str
    arm_compile_receipt_sha256s: tuple[tuple[str, str], ...]
    execution_authority: str = FORMAL_COMPILE_AUTHORITY
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    gpu_exclusive_second_entitlement: int = 0
    cpu_evaluator_second_entitlement: int = 0
    schema_version: int = 1
    receipt_kind: str = "moss_factorial_v001_trusted_compile_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "moss_factorial_v001_trusted_compile_receipt_v1"
        ):
            raise ValueError("unsupported formal v001 trusted compile receipt")
        if self.execution_authority != FORMAL_COMPILE_AUTHORITY:
            raise ValueError("formal v001 compilation cannot grant execution")
        if any(
            type(value) is not int or value != 0
            for value in (
                self.model_call_entitlement,
                self.evaluator_transaction_entitlement,
                self.gpu_exclusive_second_entitlement,
                self.cpu_evaluator_second_entitlement,
            )
        ):
            raise ValueError("formal v001 compile entitlement must remain zero")
        for value, label in (
            (self.formal_plan_sha256, "formal plan sha256"),
            (self.task_authority_bundle_sha256, "authority bundle sha256"),
            (self.task_seed_key_sha256, "task/seed key sha256"),
            (
                self.source_locked_task_artifact_sha256,
                "source-locked task artifact sha256",
            ),
            (self.context_binding_sha256, "context binding sha256"),
            (self.decision_sha256, "decision sha256"),
            (self.runtime_contract_sha256, "runtime contract sha256"),
            (
                self.canonical_compile_contract_sha256,
                "canonical compile contract sha256",
            ),
            (
                self.compile_equivalence_receipt_sha256,
                "compile equivalence receipt sha256",
            ),
        ):
            _sha(value, label)
        if tuple(arm for arm, _ in self.arm_compile_receipt_sha256s) != ARM_IDS:
            raise ValueError("formal v001 arm compile receipt coverage differs")
        for _arm, value in self.arm_compile_receipt_sha256s:
            _sha(value, "arm compile receipt sha256")
        if len({value for _, value in self.arm_compile_receipt_sha256s}) != len(
            ARM_IDS
        ):
            raise ValueError("formal v001 arm compile receipts are not distinct")

    @property
    def execution_entitlement(self) -> dict[str, int]:
        return dict(_ENTITLEMENT)

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_compile_receipt_sha256s": dict(
                self.arm_compile_receipt_sha256s
            ),
            "canonical_compile_contract_sha256": (
                self.canonical_compile_contract_sha256
            ),
            "compile_equivalence_receipt_sha256": (
                self.compile_equivalence_receipt_sha256
            ),
            "context_binding_sha256": self.context_binding_sha256,
            "decision_sha256": self.decision_sha256,
            "execution_authority": self.execution_authority,
            "execution_entitlement": self.execution_entitlement,
            "formal_plan_sha256": self.formal_plan_sha256,
            "receipt_kind": self.receipt_kind,
            "runtime_contract_sha256": self.runtime_contract_sha256,
            "schema_version": self.schema_version,
            "source_locked_task_artifact_sha256": (
                self.source_locked_task_artifact_sha256
            ),
            "task_authority_bundle_sha256": self.task_authority_bundle_sha256,
            "task_seed_key_sha256": self.task_seed_key_sha256,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class FactorialV001TrustedCompileResult:
    """Structurally bound artifacts from one compilation dispatch.

    Construction proves only internal consistency.  Provenance is established
    by ``FactorialV001FormalCompileOrchestrator.verify_trusted_result()``, which
    replays the pinned sources, Registry and compiler and must be called at
    every persistence or downstream-consumption trust boundary.
    """

    receipt: FactorialV001TrustedCompileReceipt
    runtime_contract: FactorialV001RuntimeContract
    canonical_compile_contract: V001CanonicalCompileContract
    compile_equivalence_receipt: V001CompileEquivalenceReceipt
    arm_compile_receipts: tuple[tuple[str, HarnessCompileReceipt], ...]

    def __post_init__(self) -> None:
        if (
            type(self.receipt) is not FactorialV001TrustedCompileReceipt
            or type(self.runtime_contract) is not FactorialV001RuntimeContract
            or type(self.canonical_compile_contract)
            is not V001CanonicalCompileContract
            or type(self.compile_equivalence_receipt)
            is not V001CompileEquivalenceReceipt
            or tuple(arm for arm, _ in self.arm_compile_receipts) != ARM_IDS
            or any(
                type(item) is not HarnessCompileReceipt
                for _, item in self.arm_compile_receipts
            )
        ):
            raise ValueError("formal v001 trusted compile result types differ")
        if (
            self.receipt.runtime_contract_sha256 != self.runtime_contract.sha256
            or self.receipt.canonical_compile_contract_sha256
            != self.canonical_compile_contract.sha256
            or self.receipt.compile_equivalence_receipt_sha256
            != self.compile_equivalence_receipt.sha256
            or self.receipt.arm_compile_receipt_sha256s
            != tuple((arm, item.sha256) for arm, item in self.arm_compile_receipts)
        ):
            raise ValueError("formal v001 trusted compile result binding differs")
        arm_receipts = dict(self.arm_compile_receipts)
        canonical = self.canonical_compile_contract
        equivalence = self.compile_equivalence_receipt
        if (
            self.receipt.task_seed_key_sha256
            != canonical.task_seed_key_sha256
            or self.receipt.task_seed_key_sha256
            != equivalence.task_seed_key_sha256
            or self.receipt.context_binding_sha256
            != canonical.context_binding_sha256
            or self.receipt.decision_sha256 != canonical.decision_sha256
            or self.receipt.canonical_compile_contract_sha256
            != equivalence.canonical_compile_contract_sha256
            or self.runtime_contract.component_catalog_sha256
            != canonical.component_catalog_sha256
            or any(
                receipt.context_binding_sha256
                != self.receipt.context_binding_sha256
                or receipt.decision_sha256 != self.receipt.decision_sha256
                or receipt.component_catalog_sha256
                != self.runtime_contract.component_catalog_sha256
                for receipt in arm_receipts.values()
            )
            or dict(equivalence.arm_compile_receipt_sha256s)
            != {arm: receipt.sha256 for arm, receipt in arm_receipts.items()}
        ):
            raise ValueError(
                "formal v001 trusted compile result structural binding differs"
            )


class FactorialV001FormalCompileOrchestrator:
    """Recompile one exact-matrix v001 decision without execution authority."""

    def __init__(
        self,
        *,
        task_authority: FactorialTaskArtifactAuthority,
        task_authority_bundle: ExactTaskSeedAuthorityBundle,
        plan: FactorialFormalZeroCallPlan,
    ) -> None:
        if type(task_authority) is not FactorialTaskArtifactAuthority:
            raise ValueError("formal v001 compiler requires the source authority")
        if type(task_authority_bundle) is not ExactTaskSeedAuthorityBundle:
            raise ValueError("formal v001 compiler requires the exact authority bundle")
        if type(plan) is not FactorialFormalZeroCallPlan:
            raise ValueError("formal v001 compiler requires the exact zero-call plan")
        self.task_authority = task_authority
        self.task_authority_bundle = task_authority.verify_exact_bundle(
            task_authority_bundle
        )
        self.plan = FactorialFormalZeroCallPlan.from_bytes(
            plan.canonical_bytes,
            task_authority=task_authority,
            task_authority_bundle=self.task_authority_bundle,
            expected_sha256=plan.sha256,
        )
        self.rule_registry, self.operator_registry = self._load_registry()
        self.runtime_contract, self.variants = self._build_runtime_contract()

    @staticmethod
    def _load_registry() -> tuple[RuleRegistry, TrustedOperatorRegistry]:
        before = read_safe_regular_file(
            DEFAULT_RULE_REGISTRY_V3, label="formal Rule Registry v3"
        )
        if hashlib.sha256(before).hexdigest() != RULE_REGISTRY_V3_SHA256:
            raise ValueError("formal Rule Registry v3 bytes drifted")
        registry = RuleRegistry.from_json(DEFAULT_RULE_REGISTRY_V3)
        after = read_safe_regular_file(
            DEFAULT_RULE_REGISTRY_V3, label="formal Rule Registry v3"
        )
        if before != after or registry.source_sha256 != RULE_REGISTRY_V3_SHA256:
            raise ValueError("formal Rule Registry v3 replay drifted")
        operator = TrustedOperatorRegistry(
            rule_registry_sha256=registry.source_sha256,
            rule_registry=registry,
        )
        return registry, operator

    def _build_runtime_contract(
        self,
        *,
        rule_registry: RuleRegistry | None = None,
        operator_registry: TrustedOperatorRegistry | None = None,
    ) -> tuple[FactorialV001RuntimeContract, Mapping[str, BuilderVariant]]:
        rule_registry = self.rule_registry if rule_registry is None else rule_registry
        operator_registry = (
            self.operator_registry
            if operator_registry is None
            else operator_registry
        )
        manifest = verify_factorial_contract(DEFAULT_FACTORIAL_MANIFEST)
        manifest_hashes = factorial_main_arm_variant_sha256s(manifest)
        if (
            manifest["contract_digest"] != self.plan.factorial_contract_sha256
            or tuple(manifest_hashes.items()) != self.plan.arm_variant_sha256s
        ):
            raise ValueError("formal v001 manifest/plan arm binding differs")
        declarations = {
            item["arm_id"]: item
            for item in factorial_main_arm_variant_projections(manifest)
        }
        variants: list[BuilderVariant] = []
        for arm_id in ARM_IDS:
            declaration = declarations[arm_id]
            if (
                declaration["runtime_adaptation_policy"]
                != _ADAPTATION_POLICIES[arm_id]
                or (declaration["architecture_axes"] == "FROZEN")
                != (arm_id in _ARCHITECTURE_FROZEN)
                or declaration["cross_task_state"] != "NONE"
            ):
                raise ValueError("formal v001 arm declaration/runtime semantics differ")
            variants.append(
                BuilderVariant(
                    variant_id=arm_id,
                    description=(
                        "Exact factorial v001 runtime for " + arm_id
                    ),
                    freeze_after_initial=arm_id in _ARCHITECTURE_FROZEN,
                    continual_update=False,
                    rule_registry_sha256=rule_registry.source_sha256,
                    allowed_rule_ids=rule_registry.executable_rule_ids,
                    experience_sources=(),
                    excluded_task_ids=(),
                    adaptation_policy=_ADAPTATION_POLICIES[arm_id],
                )
            )
        contract = FactorialV001RuntimeContract(
            factorial_contract_sha256=self.plan.factorial_contract_sha256,
            rule_registry_sha256=rule_registry.source_sha256,
            component_catalog_sha256=operator_registry.component_catalog_sha256,
            manifest_arm_variant_sha256s=tuple(manifest_hashes.items()),
            builder_variants=tuple(variants),
        )
        return contract, MappingProxyType(
            {item.variant_id: item for item in variants}
        )

    def _replay_authority_and_plan(
        self,
    ) -> tuple[
        ExactTaskSeedAuthorityBundle,
        FactorialV001RuntimeContract,
        Mapping[str, BuilderVariant],
        TrustedOperatorRegistry,
    ]:
        bundle = self.task_authority.verify_exact_bundle(
            self.task_authority_bundle
        )
        plan = FactorialFormalZeroCallPlan.from_bytes(
            self.plan.canonical_bytes,
            task_authority=self.task_authority,
            task_authority_bundle=bundle,
            expected_sha256=self.plan.sha256,
        )
        if plan != self.plan or bundle.sha256 != plan.task_authority_bundle_sha256:
            raise ValueError("formal v001 authority/plan replay differs")
        rule_registry, operator_registry = self._load_registry()
        if (
            rule_registry.source_sha256 != self.rule_registry.source_sha256
            or operator_registry.component_catalog_sha256
            != self.operator_registry.component_catalog_sha256
        ):
            raise ValueError("formal v001 trusted runtime replay differs")
        runtime_contract, variants = self._build_runtime_contract(
            rule_registry=rule_registry,
            operator_registry=operator_registry,
        )
        if (
            runtime_contract != self.runtime_contract
            or runtime_contract.sha256 != self.runtime_contract.sha256
            or dict(variants) != dict(self.variants)
        ):
            raise ValueError("formal v001 runtime contract replay differs")
        return bundle, runtime_contract, variants, operator_registry

    @staticmethod
    def _canonical_decision(decision: HarnessDecision) -> HarnessDecision:
        if type(decision) is not HarnessDecision:
            raise ValueError("formal v001 compilation requires an exact decision")
        canonical = HarnessDecision.from_dict(asdict(decision))
        if canonical != decision:
            raise ValueError("formal v001 decision differs from canonical validation")
        return canonical

    def compile_shared_v001(
        self,
        *,
        key: TaskSeedKey,
        decision: HarnessDecision,
    ) -> FactorialV001TrustedCompileResult:
        """Compile one shared v001 four ways without calling an external system."""

        if type(key) is not TaskSeedKey:
            raise ValueError("formal v001 compilation requires exact typed inputs")
        decision = self._canonical_decision(decision)
        if decision.rule_id != "contract_compatibility":
            raise ValueError("formal v001 decision must use contract compatibility")
        return self._compile_expected(key=key, decision=decision)

    def _compile_expected(
        self,
        *,
        key: TaskSeedKey,
        decision: HarnessDecision,
    ) -> FactorialV001TrustedCompileResult:
        """Recompile from current trust roots; caller has canonicalized inputs."""

        bundle, runtime_contract, variants, operator_registry = (
            self._replay_authority_and_plan()
        )
        schedule = self.plan.schedule_for(key)
        if schedule.key != key:
            raise ValueError("formal v001 task/seed key replay differs")
        verified_key = next(
            (item for item in bundle.task_seed_keys if item.sha256 == key.sha256),
            None,
        )
        if verified_key != key:
            raise ValueError("formal v001 key is outside the source authority")
        contexts = self.task_authority.derived_contexts()
        context = contexts[(key.suite, key.instance_id)]
        artifact = next(
            item
            for item in bundle.task_artifacts
            if item.suite == key.suite and item.instance_id == key.instance_id
        )
        artifact.verify_context(context)
        key.verify_against_context(
            context=context,
            seed=key.seed,
            task_binding_sha256=artifact.sha256,
            factorial_contract_sha256=self.plan.factorial_contract_sha256,
        )

        arm_compiled = {
            arm_id: operator_registry.compile(
                decision,
                variant=variants[arm_id],
                context=context,
            )
            for arm_id in ARM_IDS
        }
        capability = context.public_observations["artifact_contract"]
        if any(
            compiled.tool_outputs.get("task_semantics", {}).get(
                "artifact_contract"
            )
            != capability
            for compiled in arm_compiled.values()
        ):
            raise ValueError(
                "formal v001 artifact contract did not reach the solver prompt"
            )
        canonical_compiled = arm_compiled[A_FIXED_FEEDBACK]
        canonical_contract = V001CanonicalCompileContract.create(
            key, decision, canonical_compiled
        )
        arm_receipts = {
            arm_id: HarnessCompileReceipt.create(
                cell_id=key.arm_cell_id(arm_id),
                suite=key.suite,
                instance_id=key.instance_id,
                variant_id=arm_id,
                version="v001",
                adaptation_policy=variants[arm_id].adaptation_policy,
                previous_receipt_sha256=ZERO_SHA256,
                previous_decision_sha256=ZERO_SHA256,
                compiled=arm_compiled[arm_id],
                decision=decision,
            )
            for arm_id in ARM_IDS
        }
        equivalence = V001CompileEquivalenceReceipt.create(
            key=key,
            decision=decision,
            canonical_compiled=canonical_compiled,
            arm_compiled=arm_compiled,
            arm_compile_receipts=arm_receipts,
        )
        receipt = FactorialV001TrustedCompileReceipt(
            formal_plan_sha256=self.plan.sha256,
            task_authority_bundle_sha256=bundle.sha256,
            task_seed_key_sha256=key.sha256,
            source_locked_task_artifact_sha256=artifact.sha256,
            context_binding_sha256=key.context_binding_sha256,
            decision_sha256=decision.sha256,
            runtime_contract_sha256=runtime_contract.sha256,
            canonical_compile_contract_sha256=canonical_contract.sha256,
            compile_equivalence_receipt_sha256=equivalence.sha256,
            arm_compile_receipt_sha256s=tuple(
                (arm_id, arm_receipts[arm_id].sha256) for arm_id in ARM_IDS
            ),
        )
        return FactorialV001TrustedCompileResult(
            receipt=receipt,
            runtime_contract=runtime_contract,
            canonical_compile_contract=canonical_contract,
            compile_equivalence_receipt=equivalence,
            arm_compile_receipts=tuple(
                (arm_id, arm_receipts[arm_id]) for arm_id in ARM_IDS
            ),
        )

    def verify_trusted_result(
        self,
        *,
        key: TaskSeedKey,
        decision: HarnessDecision,
        candidate: FactorialV001TrustedCompileResult,
    ) -> FactorialV001TrustedCompileResult:
        """Replay all trust roots and require byte-identical compile evidence."""

        if type(key) is not TaskSeedKey or type(candidate) is not (
            FactorialV001TrustedCompileResult
        ):
            raise ValueError("formal v001 trusted result requires exact typed inputs")
        canonical_decision = self._canonical_decision(decision)
        expected = self._compile_expected(
            key=key,
            decision=canonical_decision,
        )
        candidate_bytes = (
            candidate.receipt.canonical_bytes,
            candidate.runtime_contract.canonical_bytes,
            candidate.canonical_compile_contract.canonical_bytes,
            candidate.compile_equivalence_receipt.canonical_bytes,
            tuple(
                (arm, receipt.canonical_bytes)
                for arm, receipt in candidate.arm_compile_receipts
            ),
        )
        expected_bytes = (
            expected.receipt.canonical_bytes,
            expected.runtime_contract.canonical_bytes,
            expected.canonical_compile_contract.canonical_bytes,
            expected.compile_equivalence_receipt.canonical_bytes,
            tuple(
                (arm, receipt.canonical_bytes)
                for arm, receipt in expected.arm_compile_receipts
            ),
        )
        if candidate != expected or candidate_bytes != expected_bytes:
            raise ValueError(
                "formal v001 candidate differs from trusted recompilation"
            )
        return expected


__all__ = [
    "FactorialV001FormalCompileOrchestrator",
    "FactorialV001RuntimeContract",
    "FactorialV001TrustedCompileReceipt",
    "FactorialV001TrustedCompileResult",
]
