from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from typing import Any

from .adapters.sweperf import PatchContractError, validate_unified_diff


_DIFF_FENCE = re.compile(
    r"\s*```(?:diff|patch)?\s*\n(.*?)```\s*", re.DOTALL | re.IGNORECASE
)


class ContractCompatibilityError(ValueError):
    """A public artifact cannot be safely adapted to its strict codec."""

    def __init__(self, message: str, *, reason_code: str) -> None:
        super().__init__(message)
        self.reason_code = reason_code


@dataclass(frozen=True)
class ContractCapabilityCard:
    schema_version: int
    policy_id: str
    artifact_kind: str
    response_boundary: str
    literal_template: str
    safe_normalizations: tuple[str, ...]
    forbidden_transformations: tuple[str, ...]
    public_failure_stages: tuple[str, ...]

    def public_payload(self) -> dict[str, Any]:
        return asdict(self)

    def skill_sha256(self) -> str:
        """Return a stable identity for this public benchmark contract skill."""

        encoded = json.dumps(
            self.public_payload(), ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()


@dataclass(frozen=True)
class CompatibilityNormalization:
    text: str
    trace: dict[str, Any]


SWEBENCH_VERIFIED_CAPABILITY = ContractCapabilityCard(
    schema_version=1,
    policy_id="swebench-verified-official-diff-compat-v1",
    artifact_kind="swebench_verified_unified_diff",
    response_boundary="one complete Git unified diff and no prose",
    literal_template=(
        "diff --git a/<path> b/<path>\n"
        "[optional: index <old-hex>..<new-hex> 100644]\n"
        "--- a/<path>\n+++ b/<path>\n"
        "@@ -<old-start>,<old-count> +<new-start>,<new-count> @@\n"
        " <context>\n-<deleted>\n+<added>"
    ),
    safe_normalizations=(
        "strip_one_outer_diff_fence",
        "append_one_terminal_lf",
        "insert_deterministic_nonsemantic_index_for_regular_file",
    ),
    forbidden_transformations=(
        "change_repository_path",
        "change_hunk_header",
        "change_context_or_added_or_deleted_line",
        "add_remove_or_reorder_diff_section",
        "repair_patch_application_or_test_semantics",
    ),
    public_failure_stages=(
        "response_boundary",
        "unsafe_path",
        "invalid_index_metadata",
        "malformed_hunk",
        "patch_apply_failed",
        "evaluator_correctness",
    ),
)


def lcbench_capability(instance_id: str) -> ContractCapabilityCard:
    return ContractCapabilityCard(
        schema_version=1,
        policy_id="yahpo-lcbench-query-batch-v1",
        artifact_kind="yahpo_lcbench_query_batch",
        response_boundary="one bare strict JSON object and no prose",
        literal_template=(
            '{"schema_version":1,"instance_id":"'
            + instance_id
            + '","queries":[16 distinct objects, each with exactly '
            "batch_size,learning_rate,max_dropout,max_units,momentum,"
            "num_layers,weight_decay]}"
        ),
        safe_normalizations=("strip_one_outer_json_fence", "canonicalize_json"),
        forbidden_transformations=(
            "change_instance_id",
            "add_remove_or_alias_top_level_field",
            "add_remove_or_alias_query_field",
            "repair_out_of_range_or_duplicate_query",
        ),
        public_failure_stages=(
            "response_boundary",
            "json_schema",
            "task_binding",
            "query_policy",
            "evaluator_correctness",
        ),
    )


def compilergym_capability(benchmark_uri: str) -> ContractCapabilityCard:
    return ContractCapabilityCard(
        schema_version=1,
        policy_id="compilergym-action-sequence-v1",
        artifact_kind="compilergym_action_sequence",
        response_boundary="one bare strict JSON object and no prose",
        literal_template=(
            '{"schema_version":1,"benchmark_uri":"'
            + benchmark_uri
            + '","actions":[1 to 64 allowlisted LLVM pass strings]}'
        ),
        safe_normalizations=("strip_one_outer_json_fence", "canonicalize_json"),
        forbidden_transformations=(
            "change_benchmark_uri",
            "add_remove_or_alias_top_level_field",
            "invent_or_rewrite_action",
            "repair_empty_or_oversized_action_sequence",
        ),
        public_failure_stages=(
            "response_boundary",
            "json_schema",
            "task_binding",
            "action_allowlist",
            "fresh_replay",
            "semantic_validator",
        ),
    )


def edgebench_capability(required_submit_path: str = "solution.py") -> ContractCapabilityCard:
    """Return the public output skill for one EdgeBench file bundle."""

    return ContractCapabilityCard(
        schema_version=1,
        policy_id="edgebench-file-bundle-v1",
        artifact_kind="edgebench_file_bundle_v1",
        response_boundary="one complete JSON object and no prose",
        literal_template=(
            '{"schema_version":1,"files":[{"path":"'
            + required_submit_path
            + '","type":"file","content":"<text>"}]}'
        ),
        safe_normalizations=("canonicalize_json", "normalize_crlf_to_lf"),
        forbidden_transformations=(
            "markdown_fence",
            "extra_prose",
            "missing_required_submit_path",
            "unsafe_or_duplicate_path",
            "change_evaluator_semantics",
        ),
        public_failure_stages=(
            "response_boundary",
            "json_schema",
            "path_policy",
            "size_policy",
            "evaluator_correctness",
        ),
    )


def alebench_capability() -> ContractCapabilityCard:
    """Return the public output skill for one ALE-Bench source response."""

    return ContractCapabilityCard(
        schema_version=1,
        policy_id="alebench-fenced-source-v1",
        artifact_kind="alebench_source_file",
        response_boundary="one complete fenced source file and no prose",
        literal_template=(
            "```<supported language label>\n"
            "<complete source file>\n"
            "```"
        ),
        safe_normalizations=("normalize_crlf_to_lf", "append_terminal_lf"),
        forbidden_transformations=(
            "extra_prose",
            "extra_code_fence",
            "unsupported_language_label",
            "empty_source",
            "change_evaluator_semantics",
        ),
        public_failure_stages=(
            "response_boundary",
            "language_label",
            "source_size",
            "evaluator_correctness",
        ),
    )


def patch_contract_reason_code(message: str) -> str:
    lowered = message.lower()
    if "path" in lowered or "rename" in lowered or "cop" in lowered:
        return "unsafe_path"
    if "index" in lowered or "mode" in lowered:
        return "invalid_index_metadata"
    if "hunk" in lowered or "unified-diff prefix" in lowered:
        return "malformed_hunk"
    if "whole response" in lowered or "must start" in lowered or "empty" in lowered:
        return "response_boundary"
    if "utf-8" in lowered or "lf ending" in lowered or "nul" in lowered:
        return "text_encoding"
    if "too many" in lowered or "byte limit" in lowered:
        return "artifact_limit"
    return "solution_contract_rejected"


def _extract_diff(raw_response: str) -> str:
    if not isinstance(raw_response, str) or not raw_response.strip():
        raise ContractCompatibilityError(
            "SWE-bench response cannot be empty", reason_code="response_boundary"
        )
    fenced = _DIFF_FENCE.fullmatch(raw_response)
    if fenced:
        patch = fenced.group(1)
    elif raw_response.startswith("diff --git "):
        patch = raw_response
    else:
        raise ContractCompatibilityError(
            "SWE-bench unified diff must occupy the whole response",
            reason_code="response_boundary",
        )
    return patch.rstrip("\n") + "\n"


def normalize_swebench_verified_response(
    raw_response: str,
) -> CompatibilityNormalization:
    """Normalize only non-semantic metadata omitted by official SWE patches.

    Every byte other than an inserted ``index`` line is preserved.  The existing
    strict unified-diff validator remains the final authority for paths, hunks,
    file kinds, bounds, and semantic changes.
    """

    source = _extract_diff(raw_response)
    source_sha = hashlib.sha256(source.encode("utf-8")).hexdigest()
    lines = source[:-1].split("\n")
    normalized: list[str] = []
    inserted = 0
    section_index = 0
    index = 0
    while index < len(lines):
        line = lines[index]
        normalized.append(line)
        index += 1
        if not line.startswith("diff --git "):
            continue
        fields = line.split()
        if (
            len(fields) != 4
            or not fields[2].startswith("a/")
            or not fields[3].startswith("b/")
            or fields[2][2:] != fields[3][2:]
        ):
            section_index += 1
            continue
        path = fields[2][2:]
        change_kind = "modify"
        mode = "100644"
        if index < len(lines) and lines[index].startswith("new file mode "):
            change_kind = "new"
            mode = lines[index].removeprefix("new file mode ")
            normalized.append(lines[index])
            index += 1
        elif index < len(lines) and lines[index].startswith("deleted file mode "):
            change_kind = "delete"
            mode = lines[index].removeprefix("deleted file mode ")
            normalized.append(lines[index])
            index += 1
        expected_old_header = (
            "--- /dev/null" if change_kind == "new" else f"--- {fields[2]}"
        )
        if (
            index < len(lines)
            and not lines[index].startswith("index ")
            and lines[index] == expected_old_header
            and mode in {"100644", "100755"}
        ):
            old_object = hashlib.sha1(
                f"compat-index-old:{section_index}:{path}:{source_sha}".encode()
            ).hexdigest()
            new_object = hashlib.sha1(
                f"compat-index-new:{section_index}:{path}:{source_sha}".encode()
            ).hexdigest()
            if change_kind == "new":
                old_object = "0" * 40
            elif change_kind == "delete":
                new_object = "0" * 40
            if old_object == new_object:  # pragma: no cover - cryptographic guard.
                raise RuntimeError("compatibility index metadata collided")
            normalized.append(f"index {old_object}..{new_object} {mode}")
            inserted += 1
        section_index += 1
    text = "\n".join(normalized) + "\n"
    try:
        validate_unified_diff(text)
    except PatchContractError as exc:
        raise ContractCompatibilityError(
            str(exc), reason_code=patch_contract_reason_code(str(exc))
        ) from exc
    normalized_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return CompatibilityNormalization(
        text=text,
        trace={
            "schema_version": 1,
            "policy_id": SWEBENCH_VERIFIED_CAPABILITY.policy_id,
            "original_response_sha256": hashlib.sha256(
                raw_response.encode("utf-8")
            ).hexdigest(),
            "extracted_diff_sha256": source_sha,
            "normalized_diff_sha256": normalized_sha,
            "inserted_index_lines": inserted,
            "semantic_content_changed": False,
        },
    )


def codec_capability_payload(codec: object) -> dict[str, Any]:
    card = getattr(codec, "capability_card", None)
    if isinstance(card, ContractCapabilityCard):
        payload = card.public_payload()
        payload["skill_sha256"] = card.skill_sha256()
        return payload
    output_mode = getattr(codec, "output_mode", "unknown")
    return {
        "schema_version": 1,
        "policy_id": "strict-codec-no-safe-normalization-v1",
        "artifact_kind": type(codec).__name__,
        "response_boundary": str(output_mode),
        "literal_template": "provider task card is authoritative",
        "safe_normalizations": [],
        "forbidden_transformations": ["all_unregistered_transformations"],
        "public_failure_stages": ["solution_contract_rejected"],
    }


__all__ = [
    "CompatibilityNormalization",
    "ContractCapabilityCard",
    "ContractCompatibilityError",
    "SWEBENCH_VERIFIED_CAPABILITY",
    "alebench_capability",
    "codec_capability_payload",
    "compilergym_capability",
    "edgebench_capability",
    "lcbench_capability",
    "normalize_swebench_verified_response",
    "patch_contract_reason_code",
]
