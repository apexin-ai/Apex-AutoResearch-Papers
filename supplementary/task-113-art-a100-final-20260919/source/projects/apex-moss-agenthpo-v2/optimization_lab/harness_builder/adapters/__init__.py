"""Trusted evaluator contracts for the HB-GEN-1 benchmark suites."""

from .kernel_candidate_invocation import TrustedKernelInvocationRunner
from .kernel_candidate_policy import (
    RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
    RestrictedKernelCandidatePolicy,
)

from .sweperf_docker import (
    ProductionSWEPerfDockerExecutor,
    SWEPerfDockerExecutor,
    SecurityLimits as SWEPerfDockerSecurityLimits,
    WrapperImageIdentity as SWEPerfWrapperImageIdentity,
)

__all__ = [
    "RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256",
    "RestrictedKernelCandidatePolicy",
    "TrustedKernelInvocationRunner",
    "ProductionSWEPerfDockerExecutor",
    "SWEPerfDockerExecutor",
    "SWEPerfDockerSecurityLimits",
    "SWEPerfWrapperImageIdentity",
]
