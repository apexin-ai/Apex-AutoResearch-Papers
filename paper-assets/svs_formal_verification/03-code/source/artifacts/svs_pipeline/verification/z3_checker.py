"""Z3-based internal consistency checker for single reasoning chains.

All Z3 operations are delegated to z3_sandbox (subprocess isolation)
to survive C-level crashes (SIGABRT from Z3's C++ layer).
"""

import logging

from ..types import AtomicClaim
from ..config import VerificationConfig
from ..z3_sandbox import get_sandbox

logger = logging.getLogger(__name__)


class Z3Checker:

    def __init__(self, config: VerificationConfig):
        self.config = config

    def check_internal_consistency(
        self, claims: list[AtomicClaim], vocab: dict, total_claims: int = 0,
        premise_fols: list[str] | None = None,
    ) -> tuple[bool, float, int]:
        """Check whether formalized claims in a chain are internally consistent.

        Runs entirely in Z3 subprocess sandbox.

        Returns:
            (is_sat, ic_score, mcs_size)
        """
        formalized = [c for c in claims if c.z3_parseable and c.fol]

        if not formalized:
            return (True, 0.0, 0)

        fol_strs = [c.fol for c in formalized]
        denom = total_claims if total_claims > 0 else len(formalized)

        sandbox = get_sandbox()
        is_sat, ic_score, mcs_size = sandbox.check_ic(
            fol_strs, vocab, denom,
            premise_fols=premise_fols,
            z3_timeout_ms=self.config.z3_timeout_ms,
        )

        if is_sat:
            logger.info("Chain internally consistent: %d claims all SAT", len(fol_strs))
        else:
            logger.info("Chain inconsistent: MCS=%d/%d", mcs_size, len(fol_strs))

        return (is_sat, ic_score, mcs_size)

    def check_entailment(
        self, claims: list[AtomicClaim], vocab: dict,
        premise_fols: list[str], conclusion_fol: str,
    ) -> tuple[bool, str]:
        """Check if premises ∧ chain_claims ⊨ conclusion.

        Returns:
            (entails, status): status in {"entails", "not_entails", "unknown",
            "parse_error", "subprocess_error"}
        """
        claim_fol_strs = [c.fol for c in claims if c.z3_parseable and c.fol]

        sandbox = get_sandbox()
        entails, status = sandbox.check_entailment(
            claim_fol_strs, vocab, premise_fols, conclusion_fol,
            z3_timeout_ms=self.config.z3_timeout_ms,
        )
        return (entails, status)
