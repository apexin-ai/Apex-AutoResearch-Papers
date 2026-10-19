"""Offline build contracts for the HB-GEN-1 SWE-Perf wrapper images.

The eight upstream SWE-Perf image digests are dependency images, not trusted
HB-GEN-1 evaluators.  This package prepares deterministic, network-free build
contexts that add the root-owned stage supervisor and bind it to one frozen
task manifest.  The current supervisor is intentionally fail closed because
the upstream in-process pytest report is unattestable.  This package never
talks to Docker and never pulls or builds an image.
"""

from .contract import (
    IMAGE_RESOURCE_LIMITS_SHA256_LABEL,
    IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL,
    IMAGE_TASK_MANIFEST_SHA256_LABEL,
    IMAGE_UPSTREAM_REF_SHA256_LABEL,
    PreparedWrapperContext,
    WrapperSourceLock,
    WrapperTaskManifest,
    prepare_wrapper_build_contexts,
)
from . import source_lock_prepare
from .source_lock_prepare import (
    BlockedSourceLockPrepare,
    PUBLIC_DATASET_COLUMNS,
    prepare_sweperf_source_lock,
)
from .trusted_result import (
    RESULT_CHANNEL_REASON_CODE,
    ResultChannelCapabilityVerdict,
    UnattestableCandidateOutcome,
    result_channel_capability_verdict,
)

__all__ = [
    "IMAGE_RESOURCE_LIMITS_SHA256_LABEL",
    "IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL",
    "IMAGE_TASK_MANIFEST_SHA256_LABEL",
    "IMAGE_UPSTREAM_REF_SHA256_LABEL",
    "PreparedWrapperContext",
    "WrapperSourceLock",
    "WrapperTaskManifest",
    "prepare_wrapper_build_contexts",
    "BlockedSourceLockPrepare",
    "PUBLIC_DATASET_COLUMNS",
    "prepare_sweperf_source_lock",
    "source_lock_prepare",
    "RESULT_CHANNEL_REASON_CODE",
    "ResultChannelCapabilityVerdict",
    "UnattestableCandidateOutcome",
    "result_channel_capability_verdict",
]
