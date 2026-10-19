from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from ._safe_artifacts import (
    lexical_absolute,
    read_safe_regular_file,
    safe_regular_file_exists,
    write_once_safe_regular_file,
)
from .operators import CompiledHarness
from .schema import HarnessDecision


_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_AXES = (
    "role_graph",
    "memory_views",
    "tools",
    "parent_strategy",
    "workflow",
    "scheduler_mode",
    "recovery_mode",
)


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _safe(value: str, label: str) -> str:
    if not isinstance(value, str) or not _SAFE_ID.fullmatch(value):
        raise ValueError(f"unsafe compile receipt {label}")
    return value


def _sha(value: str, label: str) -> str:
    if not isinstance(value, str) or not _SHA256.fullmatch(value):
        raise ValueError(f"invalid compile receipt {label}")
    return value


@dataclass(frozen=True)
class HarnessCompileReceipt:
    cell_id: str
    suite: str
    instance_id: str
    variant_id: str
    version: str
    adaptation_policy: str
    previous_receipt_sha256: str
    previous_decision_sha256: str
    context_binding_sha256: str
    decision_sha256: str
    operational_fingerprint: str
    lineage_operational_fingerprints: tuple[str, ...]
    lineage_prefix_sha256: str
    change_map: dict[str, bool]
    rule_registry_sha256: str
    component_catalog_sha256: str
    component_instances: tuple[dict[str, Any], ...]
    axis_effect_sha256s: dict[str, str]
    axis_configuration_sha256s: dict[str, str]
    selected_parent_ids: tuple[str, ...]
    memory_sha256: str
    tool_outputs_sha256: str
    workflow_sha256: str
    scheduler_sha256: str
    solution_prompt_sha256: str
    builder_meta_prior_sha256: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.cell_id, "cell id"),
            (self.suite, "suite"),
            (self.instance_id, "instance id"),
            (self.variant_id, "variant id"),
            (self.version, "version"),
        ):
            _safe(value, label)
        if re.fullmatch(r"v\d{3}", self.version) is None or not 1 <= int(
            self.version[1:]
        ) <= 8:
            raise ValueError("compile receipt version differs")
        if self.adaptation_policy not in {
            "conditional_any_v1",
            "targeted_any_change_v1",
            "wide_all_fields_recompile_v1",
        }:
            raise ValueError("invalid compile receipt adaptation policy")
        for value, label in (
            (self.previous_receipt_sha256, "previous receipt sha256"),
            (self.previous_decision_sha256, "previous decision sha256"),
            (self.context_binding_sha256, "context binding sha256"),
            (self.decision_sha256, "decision sha256"),
            (self.operational_fingerprint, "operational fingerprint"),
            (self.lineage_prefix_sha256, "lineage prefix sha256"),
            (self.rule_registry_sha256, "Rule Registry sha256"),
            (self.component_catalog_sha256, "component catalog sha256"),
            (self.memory_sha256, "memory sha256"),
            (self.tool_outputs_sha256, "tool outputs sha256"),
            (self.workflow_sha256, "workflow sha256"),
            (self.scheduler_sha256, "scheduler sha256"),
            (self.solution_prompt_sha256, "solution prompt sha256"),
            (self.builder_meta_prior_sha256, "Builder meta-prior sha256"),
        ):
            _sha(value, label)
        if (
            not isinstance(self.lineage_operational_fingerprints, (tuple, list))
            or not self.lineage_operational_fingerprints
            or len(self.lineage_operational_fingerprints) > int(self.version[1:])
            or tuple(self.lineage_operational_fingerprints)[-1]
            != self.operational_fingerprint
        ):
            raise ValueError("compile receipt lineage fingerprint prefix differs")
        if (
            self.adaptation_policy == "wide_all_fields_recompile_v1"
            and len(set(self.lineage_operational_fingerprints))
            != len(self.lineage_operational_fingerprints)
        ):
            raise ValueError("wide compile receipt reuses a lineage fingerprint")
        for value in self.lineage_operational_fingerprints:
            _sha(value, "lineage operational fingerprint")
        expected_lineage_prefix_sha = hashlib.sha256(
            json.dumps(
                list(self.lineage_operational_fingerprints),
                sort_keys=True,
                separators=(",", ":"),
            ).encode()
        ).hexdigest()
        if self.lineage_prefix_sha256 != expected_lineage_prefix_sha:
            raise ValueError("compile receipt lineage prefix hash differs")
        if set(self.change_map) != set(_AXES) or any(
            type(value) is not bool for value in self.change_map.values()
        ):
            raise ValueError("compile receipt change map differs")
        if self.adaptation_policy == "wide_all_fields_recompile_v1" and not all(
            self.change_map.values()
        ):
            raise ValueError("wide compile receipt lacks a seven-axis change")
        if (
            self.adaptation_policy == "targeted_any_change_v1"
            and int(self.version[1:]) > 1
            and not any(self.change_map.values())
        ):
            raise ValueError("targeted compile receipt lacks a material axis change")
        if set(self.axis_effect_sha256s) != set(_AXES):
            raise ValueError("compile receipt axis effect coverage differs")
        for axis, effect_sha in self.axis_effect_sha256s.items():
            _sha(effect_sha, f"{axis} effect sha256")
        if set(self.axis_configuration_sha256s) != set(_AXES):
            raise ValueError("compile receipt axis configuration coverage differs")
        for axis, configuration_sha in self.axis_configuration_sha256s.items():
            _sha(configuration_sha, f"{axis} configuration sha256")
        if not isinstance(self.component_instances, (tuple, list)):
            raise ValueError("compile receipt component instances must be a list")
        expected_component_fields = {
            "axis",
            "component_id",
            "ordinal",
            "implementation_ref",
            "instance_nonce_sha256",
            "config_sha256",
        }
        instances = tuple(self.component_instances)
        if not instances or len(instances) > 256:
            raise ValueError("compile receipt component count differs")
        seen: set[tuple[str, int]] = set()
        axes: set[str] = set()
        ordinals_by_axis: dict[str, list[int]] = {axis: [] for axis in _AXES}
        for instance in instances:
            if not isinstance(instance, dict) or set(instance) != expected_component_fields:
                raise ValueError("compile receipt component fields differ")
            axis = instance["axis"]
            component_id = instance["component_id"]
            ordinal = instance["ordinal"]
            implementation_ref = instance["implementation_ref"]
            if axis not in _AXES:
                raise ValueError("compile receipt component axis differs")
            _safe(component_id, "component id")
            _safe(implementation_ref, "component implementation")
            if implementation_ref != f"moss.harness.{axis}.{component_id}.v1":
                raise ValueError("compile receipt component implementation differs")
            if type(ordinal) is not int or ordinal < 0:
                raise ValueError("compile receipt component ordinal differs")
            config_sha = _sha(instance["config_sha256"], "component config sha256")
            instance_nonce_sha = _sha(
                instance["instance_nonce_sha256"], "component instance nonce sha256"
            )
            expected_instance_nonce_sha = hashlib.sha256(
                json.dumps(
                    {
                        "axis": axis,
                        "component_id": component_id,
                        "catalog_sha256": self.component_catalog_sha256,
                        "instance_id": self.instance_id,
                        "round_index": int(self.version[1:]),
                        "decision_sha256": self.decision_sha256,
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode()
            ).hexdigest()
            if instance_nonce_sha != expected_instance_nonce_sha:
                raise ValueError("compile receipt component instance binding differs")
            expected_config_sha = hashlib.sha256(
                json.dumps(
                    {
                        "axis": axis,
                        "component_id": component_id,
                        "ordinal": ordinal,
                        "implementation_ref": implementation_ref,
                        "catalog_sha256": self.component_catalog_sha256,
                        "instance_id": self.instance_id,
                        "round_index": int(self.version[1:]),
                        "decision_sha256": self.decision_sha256,
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode()
            ).hexdigest()
            if config_sha != expected_config_sha:
                raise ValueError("compile receipt component config binding differs")
            key = (axis, ordinal)
            if key in seen:
                raise ValueError("compile receipt component ordinal is duplicated")
            seen.add(key)
            axes.add(axis)
            ordinals_by_axis[axis].append(ordinal)
        if axes != set(_AXES) or any(
            sorted(ordinals) != list(range(len(ordinals)))
            for ordinals in ordinals_by_axis.values()
        ):
            raise ValueError("compile receipt component coverage differs")
        if not isinstance(self.selected_parent_ids, (tuple, list)) or not self.selected_parent_ids:
            raise ValueError("compile receipt selected parents differ")
        for parent_id in self.selected_parent_ids:
            _safe(parent_id, "selected parent id")

    @classmethod
    def create(
        cls,
        *,
        cell_id: str,
        suite: str,
        instance_id: str,
        variant_id: str,
        version: str,
        adaptation_policy: str,
        previous_receipt_sha256: str,
        previous_decision_sha256: str,
        compiled: CompiledHarness,
        decision: HarnessDecision,
        previous_decision: HarnessDecision | None = None,
        prior_operational_fingerprints: tuple[str, ...] = (),
    ) -> "HarnessCompileReceipt":
        if (
            decision.sha256 != compiled.decision_sha256
            or decision.operational_fingerprint != compiled.operational_fingerprint
        ):
            raise ValueError("compile receipt decision differs from compilation")
        if adaptation_policy != compiled.adaptation_policy:
            raise ValueError("compile receipt adaptation policy differs from compilation")
        if set(compiled.change_map) != set(_AXES) or not all(
            isinstance(value, bool) for value in compiled.change_map.values()
        ):
            raise ValueError("compile receipt change map differs")
        if adaptation_policy == "wide_all_fields_recompile_v1" and not all(
            compiled.change_map.values()
        ):
            raise ValueError("wide compile receipt lacks a seven-axis change")
        if (
            adaptation_policy == "targeted_any_change_v1"
            and int(version[1:]) > 1
            and not any(compiled.change_map.values())
        ):
            raise ValueError("targeted compile receipt lacks a material axis change")
        if adaptation_policy == "wide_all_fields_recompile_v1":
            if (
                not isinstance(prior_operational_fingerprints, tuple)
                or len(prior_operational_fingerprints) > int(version[1:]) - 1
                or len(set(prior_operational_fingerprints))
                != len(prior_operational_fingerprints)
                or any(_SHA256.fullmatch(value) is None for value in prior_operational_fingerprints)
                or (
                    previous_decision is not None
                    and (
                        not prior_operational_fingerprints
                        or prior_operational_fingerprints[-1]
                        != previous_decision.operational_fingerprint
                    )
                )
                or decision.operational_fingerprint in prior_operational_fingerprints
            ):
                raise ValueError("wide compile receipt lineage prefix differs")
            if int(version[1:]) > 1 and previous_decision is None:
                raise ValueError("wide compile receipt lacks its previous decision")
            if previous_decision is not None:
                if previous_decision.sha256 != previous_decision_sha256:
                    raise ValueError("wide compile receipt previous decision binding differs")
                if compiled.change_map != decision.operational_change_map_from(
                    previous_decision
                ):
                    raise ValueError("wide compile receipt change map is not decision-derived")
        elif adaptation_policy == "targeted_any_change_v1":
            if int(version[1:]) > 1 and previous_decision is None:
                raise ValueError("targeted compile receipt lacks its previous decision")
            if previous_decision is not None:
                if previous_decision.sha256 != previous_decision_sha256:
                    raise ValueError(
                        "targeted compile receipt previous decision binding differs"
                    )
                if compiled.change_map != decision.operational_change_map_from(
                    previous_decision
                ):
                    raise ValueError(
                        "targeted compile receipt change map is not decision-derived"
                    )
        elif previous_decision is not None:
            if previous_decision.sha256 != previous_decision_sha256:
                raise ValueError("compile receipt previous decision binding differs")
            if compiled.change_map != decision.operational_change_map_from(
                previous_decision
            ):
                raise ValueError("compile receipt change map is not decision-derived")
        lineage = (
            (*prior_operational_fingerprints, decision.operational_fingerprint)
            if adaptation_policy == "wide_all_fields_recompile_v1"
            else (decision.operational_fingerprint,)
        )
        instances = tuple(asdict(value) for value in compiled.component_instances)
        if not instances or {value["axis"] for value in instances} != set(_AXES):
            raise ValueError("compile receipt component coverage differs")

        def digest(value: Any) -> str:
            return hashlib.sha256(
                json.dumps(
                    value,
                    ensure_ascii=False,
                    allow_nan=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode()
            ).hexdigest()

        rule_registry_sha = str(
            compiled.rule_decision_trace.get("rule_registry_sha256", "")
        )
        return cls(
            cell_id=_safe(cell_id, "cell id"),
            suite=_safe(suite, "suite"),
            instance_id=_safe(instance_id, "instance id"),
            variant_id=_safe(variant_id, "variant id"),
            version=_safe(version, "version"),
            adaptation_policy=adaptation_policy,
            previous_receipt_sha256=_sha(
                previous_receipt_sha256, "previous receipt sha256"
            ),
            previous_decision_sha256=_sha(
                previous_decision_sha256, "previous decision sha256"
            ),
            context_binding_sha256=_sha(
                compiled.context_binding_sha256, "context binding sha256"
            ),
            decision_sha256=_sha(compiled.decision_sha256, "decision sha256"),
            operational_fingerprint=_sha(
                compiled.operational_fingerprint, "operational fingerprint"
            ),
            lineage_operational_fingerprints=lineage,
            lineage_prefix_sha256=digest(list(lineage)),
            change_map=dict(compiled.change_map),
            rule_registry_sha256=_sha(rule_registry_sha, "Rule Registry sha256"),
            component_catalog_sha256=_sha(
                compiled.component_catalog_sha256, "component catalog sha256"
            ),
            component_instances=instances,
            axis_effect_sha256s=dict(compiled.axis_effect_sha256s),
            axis_configuration_sha256s=dict(
                compiled.axis_configuration_sha256s
            ),
            selected_parent_ids=tuple(compiled.selected_parent_ids),
            memory_sha256=digest(compiled.memory),
            tool_outputs_sha256=digest(compiled.tool_outputs),
            workflow_sha256=digest([asdict(step) for step in compiled.execution_steps]),
            scheduler_sha256=digest(compiled.scheduler_phase),
            solution_prompt_sha256=hashlib.sha256(
                compiled.solution_prompt.encode("utf-8")
            ).hexdigest(),
            builder_meta_prior_sha256=_sha(
                compiled.builder_meta_prior_sha256, "Builder meta-prior sha256"
            ),
        )

    def core_payload(self) -> dict[str, Any]:
        # v2 adds the public task/context binding.  No v1 receipt was ever
        # produced by an authorized formal campaign, so accepting a v1 payload
        # here would only make it possible to erase that new binding.
        return {"schema_version": 2, **asdict(self)}

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.core_payload())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def from_bytes(cls, encoded: bytes, *, expected_sha256: str) -> "HarnessCompileReceipt":
        _sha(expected_sha256, "expected sha256")
        try:
            payload = json.loads(encoded)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("compile receipt JSON is invalid") from exc
        fields = {field.name for field in cls.__dataclass_fields__.values()}
        if not isinstance(payload, dict) or set(payload) != fields | {"schema_version"}:
            raise ValueError("compile receipt fields differ")
        if payload.pop("schema_version") != 2:
            raise ValueError("compile receipt schema differs")
        payload["component_instances"] = tuple(payload["component_instances"])
        payload["lineage_operational_fingerprints"] = tuple(
            payload["lineage_operational_fingerprints"]
        )
        payload["selected_parent_ids"] = tuple(payload["selected_parent_ids"])
        receipt = cls(**payload)
        if receipt.canonical_bytes != encoded:
            raise ValueError("compile receipt is not canonical")
        if receipt.sha256 != expected_sha256:
            raise ValueError("compile receipt hash differs")
        return receipt


class CompileReceiptArchive:
    def __init__(self, root: Path) -> None:
        self.root = lexical_absolute(root)

    def store(self, receipt: HarnessCompileReceipt) -> Path:
        path = self.root / "receipts" / f"{receipt.sha256}.json"
        try:
            return write_once_safe_regular_file(
                path,
                receipt.canonical_bytes,
                label="compile receipt",
                temporary_suffix=".compile-receipt.tmp",
            )
        except ValueError as exc:
            if "refusing to overwrite" in str(exc):
                raise ValueError("compile receipt content-address collision") from exc
            raise

    def verify_against_compilation(
        self,
        *,
        receipt: HarnessCompileReceipt,
        decision: HarnessDecision,
        compiled: CompiledHarness,
        previous_decision: HarnessDecision | None,
        prior_operational_fingerprints: tuple[str, ...],
    ) -> None:
        """Recompute a receipt from trusted runtime output and compare every byte."""

        expected = HarnessCompileReceipt.create(
            cell_id=receipt.cell_id,
            suite=receipt.suite,
            instance_id=receipt.instance_id,
            variant_id=receipt.variant_id,
            version=receipt.version,
            adaptation_policy=receipt.adaptation_policy,
            previous_receipt_sha256=receipt.previous_receipt_sha256,
            previous_decision_sha256=receipt.previous_decision_sha256,
            compiled=compiled,
            decision=decision,
            previous_decision=previous_decision,
            prior_operational_fingerprints=prior_operational_fingerprints,
        )
        if decision.sha256 != receipt.decision_sha256 or expected != receipt:
            raise ValueError("compile receipt differs from trusted recompilation")

    def store_version(
        self,
        *,
        receipt: HarnessCompileReceipt,
        decision: HarnessDecision,
        fixture_only: bool = False,
    ) -> Path:
        """Store fixture-only archival evidence without compiler provenance.

        This helper deliberately cannot be used implicitly by a runtime.  A
        caller that is only exercising archive mechanics must opt in with
        ``fixture_only=True``.  Formal and production paths must instead use
        :meth:`store_trusted_version`, which replays the trusted compilation
        before any receipt or index bytes are written.
        """

        if fixture_only is not True:
            raise ValueError(
                "generic compile version store is fixture-only; trusted "
                "recompilation is required"
            )
        return self._store_verified_version(receipt=receipt, decision=decision)

    def store_trusted_version(
        self,
        *,
        receipt: HarnessCompileReceipt,
        decision: HarnessDecision,
        compiled: CompiledHarness,
        previous_decision: HarnessDecision | None,
        prior_operational_fingerprints: tuple[str, ...],
    ) -> Path:
        """Recompile-equivalent, fail-closed seal used before solver execution.

        The complete receipt is reconstructed from the caller's trusted
        ``CompiledHarness`` and compared before this method performs any
        filesystem write.  Parent-chain validation remains a second,
        independent gate.
        """

        self.verify_against_compilation(
            receipt=receipt,
            decision=decision,
            compiled=compiled,
            previous_decision=previous_decision,
            prior_operational_fingerprints=prior_operational_fingerprints,
        )
        return self._store_verified_version(receipt=receipt, decision=decision)

    def _store_verified_version(
        self,
        *,
        receipt: HarnessCompileReceipt,
        decision: HarnessDecision,
    ) -> Path:
        """Persist a receipt only after the caller's provenance gate passed."""

        if decision.sha256 != receipt.decision_sha256:
            raise ValueError("compile index decision binding differs")
        self._verify_parent_chain(receipt, decision)
        self.store(receipt)
        payload = {
            "schema_version": 1,
            "cell_id": receipt.cell_id,
            "suite": receipt.suite,
            "instance_id": receipt.instance_id,
            "variant_id": receipt.variant_id,
            "version": receipt.version,
            "receipt_sha256": receipt.sha256,
            "decision_sha256": decision.sha256,
            "decision": asdict(decision),
        }
        encoded = _canonical_bytes(payload)
        path = self.root / "index" / f"{receipt.version}.json"
        try:
            return write_once_safe_regular_file(
                path,
                encoded,
                label="compile version index",
                temporary_suffix=".compile-index.tmp",
            )
        except ValueError as exc:
            if "refusing to overwrite" in str(exc):
                raise ValueError("compile version index binding differs") from exc
            raise

    def _verify_parent_chain(
        self, receipt: HarnessCompileReceipt, decision: HarnessDecision
    ) -> None:
        """Bind a wide lineage to the latest earlier sealed receipt, not a caller tuple."""

        if receipt.operational_fingerprint != decision.operational_fingerprint:
            raise ValueError(
                "compile receipt operational fingerprint is not decision-derived"
            )

        # A legacy conditional campaign may legitimately have no accepted
        # compile receipt before a physical v002 (for example, after an
        # abandoned v001 planner call).  Complete accepted-lineage chaining is
        # a new invariant of the explicitly preregistered wide policy only.
        if receipt.adaptation_policy == "conditional_any_v1":
            return
        round_index = int(receipt.version[1:])
        zero = "0" * 64
        if round_index == 1:
            if (
                receipt.previous_receipt_sha256 != zero
                or receipt.previous_decision_sha256 != zero
                or (
                    receipt.adaptation_policy == "wide_all_fields_recompile_v1"
                    and receipt.lineage_operational_fingerprints
                    != (receipt.operational_fingerprint,)
                )
            ):
                raise ValueError("initial compile receipt parent chain differs")
            return
        prior_binding: tuple[HarnessCompileReceipt, HarnessDecision] | None = None
        for prior_index in range(round_index - 1, 0, -1):
            prior_version = f"v{prior_index:03d}"
            if not safe_regular_file_exists(
                self.root / "index" / f"{prior_version}.json",
                label="compile version index",
            ):
                continue
            prior_binding = self.load_version(
                prior_version,
                cell_id=receipt.cell_id,
                suite=receipt.suite,
                instance_id=receipt.instance_id,
                variant_id=receipt.variant_id,
                adaptation_policy=receipt.adaptation_policy,
            )
            break
        if prior_binding is None:
            raise ValueError("compile receipt previous version is missing")
        previous_receipt, previous_decision = prior_binding
        if (
            receipt.previous_receipt_sha256 != previous_receipt.sha256
            or receipt.previous_decision_sha256 != previous_decision.sha256
        ):
            raise ValueError("compile receipt parent chain differs")
        if receipt.adaptation_policy == "wide_all_fields_recompile_v1" and (
            receipt.lineage_operational_fingerprints
            != (
                *previous_receipt.lineage_operational_fingerprints,
                receipt.operational_fingerprint,
            )
        ):
            raise ValueError("wide compile receipt lineage truncates its parent prefix")
        if (
            receipt.adaptation_policy == "targeted_any_change_v1"
            and receipt.change_map
            != decision.operational_change_map_from(previous_decision)
        ):
            raise ValueError(
                "targeted compile receipt change map is not decision-derived"
            )
        if (
            receipt.adaptation_policy == "targeted_any_change_v1"
            and not any(receipt.change_map.values())
        ):
            raise ValueError("targeted compile receipt lacks a material axis change")
        if receipt.adaptation_policy == "wide_all_fields_recompile_v1":
            decision_change_map = decision.operational_change_map_from(
                previous_decision
            )
            if receipt.change_map != decision_change_map:
                raise ValueError(
                    "wide compile receipt change map is not decision-derived"
                )
            unchanged_decision_axes = [
                axis for axis, changed in decision_change_map.items() if not changed
            ]
            if unchanged_decision_axes:
                raise ValueError(
                    "wide compile receipt lacks a decision-derived seven-axis change: "
                    + ",".join(unchanged_decision_axes)
                )
            unchanged_configurations = [
                axis
                for axis in _AXES
                if receipt.axis_configuration_sha256s[axis]
                == previous_receipt.axis_configuration_sha256s[axis]
            ]
            if unchanged_configurations:
                raise ValueError(
                    "wide compile receipt left axis configurations unchanged: "
                    + ",".join(unchanged_configurations)
                )

    def verified_prefix_before(
        self,
        version: str,
        *,
        cell_id: str,
        suite: str,
        instance_id: str,
        variant_id: str,
        adaptation_policy: str,
    ) -> tuple[str, ...]:
        """Return only a prefix proven by the previous content-addressed receipt."""

        _safe(version, "version")
        round_index = int(version[1:])
        if round_index <= 1:
            return ()
        for prior_index in range(round_index - 1, 0, -1):
            prior_version = f"v{prior_index:03d}"
            if not safe_regular_file_exists(
                self.root / "index" / f"{prior_version}.json",
                label="compile version index",
            ):
                continue
            receipt, _decision = self.load_version(
                prior_version,
                cell_id=cell_id,
                suite=suite,
                instance_id=instance_id,
                variant_id=variant_id,
                adaptation_policy=adaptation_policy,
            )
            return tuple(receipt.lineage_operational_fingerprints)
        return ()

    def load(self, sha256: str) -> HarnessCompileReceipt:
        _sha(sha256, "archive sha256")
        path = self.root / "receipts" / f"{sha256}.json"
        if not safe_regular_file_exists(path, label="compile receipt"):
            raise ValueError("compile receipt is missing")
        return HarnessCompileReceipt.from_bytes(
            read_safe_regular_file(path, label="compile receipt"),
            expected_sha256=sha256,
        )

    def load_version(
        self,
        version: str,
        *,
        cell_id: str,
        suite: str,
        instance_id: str,
        variant_id: str,
        adaptation_policy: str | None = None,
        verify_parent_chain: bool = True,
    ) -> tuple[HarnessCompileReceipt, HarnessDecision]:
        _safe(version, "version")
        path = self.root / "index" / f"{version}.json"
        if not safe_regular_file_exists(path, label="compile version index"):
            raise ValueError("compile version index is missing")
        encoded = read_safe_regular_file(path, label="compile version index")
        try:
            payload = json.loads(encoded)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("compile version index JSON is invalid") from exc
        expected = {
            "schema_version",
            "cell_id",
            "suite",
            "instance_id",
            "variant_id",
            "version",
            "receipt_sha256",
            "decision_sha256",
            "decision",
        }
        if (
            not isinstance(payload, dict)
            or set(payload) != expected
            or _canonical_bytes(payload) != encoded
            or payload["schema_version"] != 1
            or payload["cell_id"] != cell_id
            or payload["suite"] != suite
            or payload["instance_id"] != instance_id
            or payload["variant_id"] != variant_id
            or payload["version"] != version
        ):
            raise ValueError("compile version index binding differs")
        receipt = self.load(str(payload["receipt_sha256"]))
        decision_payload = payload["decision"]
        if not isinstance(decision_payload, dict):
            raise ValueError("compile version decision is invalid")
        decision = HarnessDecision.from_dict(decision_payload)
        if (
            decision.sha256 != payload["decision_sha256"]
            or decision.sha256 != receipt.decision_sha256
            or decision.operational_fingerprint != receipt.operational_fingerprint
            or receipt.cell_id != cell_id
            or receipt.suite != suite
            or receipt.instance_id != instance_id
            or receipt.variant_id != variant_id
            or receipt.version != version
            or (
                adaptation_policy is not None
                and receipt.adaptation_policy != adaptation_policy
            )
        ):
            raise ValueError("compile version receipt binding differs")
        selected = {
            "role_graph": tuple(sorted(decision.role_graph)),
            "memory_views": tuple(sorted(decision.memory_views)),
            "tools": tuple(sorted(decision.tools)),
            "parent_strategy": (decision.parent_strategy,),
            "workflow": decision.workflow,
            "scheduler_mode": (decision.scheduler_mode,),
            "recovery_mode": (decision.recovery_mode,),
        }
        resolved = {
            axis: tuple(
                str(item["component_id"])
                for item in sorted(
                    (
                        component
                        for component in receipt.component_instances
                        if component["axis"] == axis
                    ),
                    key=lambda component: int(component["ordinal"]),
                )
            )
            for axis in _AXES
        }
        if resolved != selected:
            raise ValueError("compile receipt component selection differs from decision")
        if verify_parent_chain:
            self._verify_parent_chain(receipt, decision)
        return receipt, decision
