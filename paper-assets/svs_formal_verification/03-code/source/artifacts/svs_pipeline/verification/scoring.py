"""Composite scoring and answer selection for SVS.

Combines internal consistency (IC), formalization confidence (FC), and
cross-chain logical coherence (CCLC) into a single group score per answer,
then selects the highest-scoring answer.
"""

import logging
import random
from collections import Counter, defaultdict

from ..types import AtomicClaim, Chain, ChainVerification, GroupVerification, SVSResult
from ..config import VerificationConfig
from .z3_checker import Z3Checker
from .cross_chain import CrossChainChecker

logger = logging.getLogger(__name__)


class SVSScorer:

    def __init__(self, config: VerificationConfig):
        self.config = config

    def score_chain(self, ic_score: float, fc_score: float) -> float:
        return self.config.ic_weight * ic_score + self.config.fc_weight * fc_score

    def score_group(self, chain_scores: list[float], cclc_score: float) -> float:
        if not chain_scores:
            return 0.0
        mean_chain = sum(chain_scores) / len(chain_scores)
        return mean_chain + self.config.cclc_lambda * cclc_score

    def select_answer(
        self,
        chains: list[Chain],
        chain_claims: dict[int, list[AtomicClaim]],
        vocab: dict,
        z3_checker: Z3Checker,
        cross_checker: CrossChainChecker,
        premise_fols: list[str] | None = None,
    ) -> SVSResult:
        """Run full SVS scoring pipeline and select the best answer.

        Args:
            chains: all sampled chains for a problem
            chain_claims: chain_id -> list of AtomicClaim
            vocab: vocabulary dict for Z3 context
            z3_checker: Z3Checker instance
            cross_checker: CrossChainChecker instance

        Returns:
            SVSResult with selected_answer, group_scores, and SC baseline.
            gold_label is left empty for the caller to fill.
        """
        problem_id = chains[0].problem_id if chains else ""

        answer_groups: dict[str, list[Chain]] = defaultdict(list)
        for chain in chains:
            answer_groups[chain.answer].append(chain)

        group_scores: dict[str, float] = {}
        group_verifications: dict[str, GroupVerification] = {}
        all_chain_verifications: list[ChainVerification] = []

        for answer, group_chains in answer_groups.items():
            chain_verifications = []
            chain_scores_list = []

            for chain in group_chains:
                claims = chain_claims.get(chain.chain_id, [])
                total = len(claims)
                formalized = [c for c in claims if c.z3_parseable and c.fol]
                formalized_count = len(formalized)

                fc_score = formalized_count / total if total > 0 else 0.0

                ic_sat, ic_score, mcs_size = z3_checker.check_internal_consistency(
                    claims, vocab, total_claims=total, premise_fols=premise_fols
                )

                cs = self.score_chain(ic_score, fc_score)
                chain_scores_list.append(cs)

                chain_verifications.append(
                    ChainVerification(
                        problem_id=problem_id,
                        chain_id=chain.chain_id,
                        answer=answer,
                        total_claims=total,
                        formalized_claims=formalized_count,
                        ic_score=ic_score,
                        fc_score=fc_score,
                        ic_sat=ic_sat,
                        mcs_size=mcs_size,
                    )
                )

            group_chain_claims = {
                chain.chain_id: chain_claims.get(chain.chain_id, [])
                for chain in group_chains
            }
            cclc_sat, cclc_score, cclc_diagnostics = cross_checker.check_cross_chain_compatibility(
                group_chain_claims, vocab
            )

            gs = self.score_group(chain_scores_list, cclc_score)
            group_scores[answer] = gs

            all_chain_verifications.extend(chain_verifications)

            group_verifications[answer] = GroupVerification(
                problem_id=problem_id,
                answer=answer,
                chain_verifications=chain_verifications,
                cclc_score=cclc_score,
                cclc_sat=cclc_sat,
                group_score=gs,
                cclc_diagnostics=cclc_diagnostics,
            )

            logger.info(
                "Answer '%s': %d chains, group_score=%.4f (cclc=%.3f, cclc_sat=%s)",
                answer, len(group_chains), gs, cclc_score, cclc_sat,
            )

        selected_answer = max(group_scores, key=group_scores.get)
        sc_answer = self.majority_vote(chains)

        logger.info(
            "Problem %s: SVS='%s' (%.4f), SC='%s'",
            problem_id, selected_answer, group_scores[selected_answer], sc_answer,
        )

        return SVSResult(
            problem_id=problem_id,
            gold_label="",
            selected_answer=selected_answer,
            sc_answer=sc_answer,
            group_scores=group_scores,
            correct_svs=False,
            correct_sc=False,
            chain_verifications=all_chain_verifications,
        )

    def majority_vote(self, chains: list[Chain]) -> str:
        """Self-consistency baseline: majority vote over chain answers."""
        if not chains:
            return ""
        counts = Counter(chain.answer for chain in chains)
        max_count = counts.most_common(1)[0][1]
        top_answers = [a for a, c in counts.items() if c == max_count]
        return random.choice(top_answers)
