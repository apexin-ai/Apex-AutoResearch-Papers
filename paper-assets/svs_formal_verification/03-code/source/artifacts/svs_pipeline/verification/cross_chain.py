"""Cross-chain logical coherence (CCLC) checker.

Merges formalized claims across chains sharing the same answer and checks
whether the combined set is satisfiable. Provides both full-group and
pairwise compatibility diagnostics.
"""

import logging
import re
from itertools import combinations

from ..types import AtomicClaim
from ..config import VerificationConfig
from .z3_checker import Z3Checker

logger = logging.getLogger(__name__)

_PREDICATE_RE = re.compile(r'[A-Z][a-zA-Z]*(?=\()')
_CONSTANT_RE = re.compile(r'\b[a-z][a-z_]*\b')
_QUANTIFIER_VARS = frozenset({"x", "y", "z", "w"})
_Z3_KEYWORDS = frozenset({
    "and", "or", "not", "implies", "if", "else", "true", "false",
    "forall", "exists", "int", "bool",
})


def _extract_predicates(fol: str) -> set[str]:
    return set(_PREDICATE_RE.findall(fol))


def _extract_constants(fol: str) -> set[str]:
    raw = set(_CONSTANT_RE.findall(fol))
    return raw - _QUANTIFIER_VARS - _Z3_KEYWORDS


class CrossChainChecker:

    def __init__(self, config: VerificationConfig):
        self.config = config
        self.z3_checker = Z3Checker(config)

    def check_cross_chain_compatibility(
        self, chain_claims: dict[int, list[AtomicClaim]], vocab: dict
    ) -> tuple[bool, float, dict]:
        """Check cross-chain logical coherence for an answer group.

        Args:
            chain_claims: mapping chain_id -> list of AtomicClaim (same answer)
            vocab: vocabulary dict for building Z3 context

        Returns:
            (is_sat, cclc_score, diagnostics)
        """
        merged = []
        per_chain_formalized: dict[int, list[AtomicClaim]] = {}
        for chain_id, claims in chain_claims.items():
            fc = [c for c in claims if c.z3_parseable and c.fol]
            per_chain_formalized[chain_id] = fc
            merged.extend(fc)

        per_chain_predicates: dict[int, set[str]] = {}
        per_chain_constants: dict[int, set[str]] = {}
        for chain_id, fc in per_chain_formalized.items():
            preds: set[str] = set()
            consts: set[str] = set()
            for c in fc:
                preds |= _extract_predicates(c.fol)
                consts |= _extract_constants(c.fol)
            per_chain_predicates[chain_id] = preds
            per_chain_constants[chain_id] = consts

        all_pred_sets = [s for s in per_chain_predicates.values() if s]
        all_const_sets = [s for s in per_chain_constants.values() if s]

        if len(all_pred_sets) >= 2:
            pred_union = set().union(*all_pred_sets)
            pred_intersect = all_pred_sets[0].copy()
            for s in all_pred_sets[1:]:
                pred_intersect &= s
            predicate_overlap = len(pred_intersect) / len(pred_union) if pred_union else 0.0
        else:
            predicate_overlap = 1.0

        if len(all_const_sets) >= 2:
            const_union = set().union(*all_const_sets)
            const_intersect = all_const_sets[0].copy()
            for s in all_const_sets[1:]:
                const_intersect &= s
            constant_overlap = len(const_intersect) / len(const_union) if const_union else 0.0
        else:
            constant_overlap = 1.0

        diagnostics: dict = {
            "total_merged_claims": len(merged),
            "predicate_overlap": predicate_overlap,
            "constant_overlap": constant_overlap,
            "trivially_sat": False,
            "per_chain_predicates": {
                cid: sorted(preds) for cid, preds in per_chain_predicates.items()
            },
        }

        if not merged:
            diagnostics["trivially_sat"] = True
            return (True, 1.0, diagnostics)

        is_sat, ic_score, mcs_size = self.z3_checker.check_internal_consistency(
            merged, vocab
        )

        if is_sat:
            trivially_sat = predicate_overlap == 0.0 and len(all_pred_sets) >= 2
            diagnostics["trivially_sat"] = trivially_sat
            if trivially_sat:
                logger.warning(
                    "Cross-chain trivially SAT: %d merged claims have zero predicate "
                    "overlap — vocab normalization may have failed",
                    len(merged),
                )
            else:
                logger.info("Cross-chain SAT: %d merged claims consistent", len(merged))
            return (True, 1.0, diagnostics)

        formalized_count = len(merged)
        cclc_score = mcs_size / formalized_count if formalized_count > 0 else 1.0
        logger.info(
            "Cross-chain UNSAT: MCS=%d/%d, cclc=%.3f",
            mcs_size, formalized_count, cclc_score,
        )
        return (False, cclc_score, diagnostics)

    def pairwise_compatibility(
        self, chain_claims: dict[int, list[AtomicClaim]], vocab: dict
    ) -> dict[tuple[int, int], bool]:
        """Check pairwise compatibility between every pair of chains.

        Returns:
            dict mapping (chain_i, chain_j) -> is_compatible
        """
        chain_ids = sorted(chain_claims.keys())
        results = {}

        for ci, cj in combinations(chain_ids, 2):
            pair_claims = {ci: chain_claims[ci], cj: chain_claims[cj]}
            is_sat, _, _ = self.check_cross_chain_compatibility(pair_claims, vocab)
            results[(ci, cj)] = is_sat
            logger.debug("Pair (%d, %d): %s", ci, cj, "SAT" if is_sat else "UNSAT")

        return results
