"""Mechanical capability verdict for the frozen SWE-Perf result channel.

The upstream workload executes arbitrary candidate Python in the same pytest
process that owns the JSON report and process exit status.  Moving that report
to a root-owned directory after the process exits does not attest its contents.
This module records that topology as a deterministic, content-addressable
verdict and provides the fail-closed gate used by the image supervisor.

This is deliberately not a heuristic detector.  HB-GEN-1 may be unlocked only
by a new, separately frozen evaluator in which a trusted process can derive
both the per-test outcome and per-test call duration without consuming a signal
controlled by the candidate process.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Any


RESULT_CHANNEL_REASON_CODE = "in_process_candidate_outcome_unattestable"


def _canonical_bytes(value: dict[str, Any]) -> bytes:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("ascii")


class UnattestableCandidateOutcome(RuntimeError):
    """The frozen worker topology cannot produce trusted score evidence."""


@dataclass(frozen=True)
class ResultChannelCapabilityVerdict:
    """Frozen proof obligation and observed trust topology."""

    schema_version: int = 1
    artifact_kind: str = "hb-gen1-sweperf-result-channel-capability"
    status: str = "blocked"
    reason_code: str = RESULT_CHANNEL_REASON_CODE

    def to_dict(self) -> dict[str, Any]:
        core: dict[str, Any] = {
            "schema_version": self.schema_version,
            "artifact_kind": self.artifact_kind,
            "status": self.status,
            "reason_code": self.reason_code,
            "frozen_topology": {
                "candidate_principal": "uid_65534",
                "candidate_and_pytest_reporter_share_process": True,
                "report_bytes_authored_by": "candidate_trust_domain",
                "process_exit_status_controlled_by": "candidate_trust_domain",
                "pytest_call_duration_controlled_by": "candidate_trust_domain",
            },
            "trusted_root_observations": [
                "outer_process_wall_clock",
                "process_liveness",
                "post_command_quiescence",
            ],
            "required_frozen_score_signals": [
                "per_test_outcome",
                "per_test_call_duration",
            ],
            "signals_not_derivable_by_trusted_root": [
                "per_test_outcome",
                "per_test_call_duration",
            ],
            "rejected_repairs": {
                "root_owned_result_file": "changes final ownership, not the authoring trust domain",
                "private_fd_or_hmac": "candidate shares the process and can access the capability",
                "external_process_monitor": "observes only worker-controlled exit and outer time",
                "root_wall_clock_scoring": "changes the frozen pytest call-duration semantics",
            },
            "required_redesign": (
                "task-specific out-of-process oracle or equivalent evaluator "
                "whose trusted process derives outcomes and call durations"
            ),
            "semantics_preserving_channel_implemented": False,
        }
        return {
            **core,
            "content_id": hashlib.sha256(_canonical_bytes(core)).hexdigest(),
        }


def result_channel_capability_verdict() -> ResultChannelCapabilityVerdict:
    return ResultChannelCapabilityVerdict()


def require_trusted_result_channel() -> None:
    """Always fail closed for the currently frozen in-process pytest topology."""

    raise UnattestableCandidateOutcome(
        "candidate code and the pytest reporter share the same trust domain; "
        "no trusted SWE-Perf result channel is implemented"
    )


__all__ = [
    "RESULT_CHANNEL_REASON_CODE",
    "ResultChannelCapabilityVerdict",
    "UnattestableCandidateOutcome",
    "require_trusted_result_channel",
    "result_channel_capability_verdict",
]
