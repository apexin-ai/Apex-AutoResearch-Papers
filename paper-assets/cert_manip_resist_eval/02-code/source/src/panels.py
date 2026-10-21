# Panel logic: homo/hetero panel generation, majority voting, panel ASR measurement.

from typing import Any, Dict, List, Optional

import numpy as np

from src.config import HETERO_PANELS, HOMO_PANELS, MODEL_REGISTRY
from src.utils import setup_logging

logger = setup_logging("panels")


class Panel:
    """A panel of judges that aggregates via majority vote."""

    def __init__(self, judge_ids: List[str], panel_type: str = "unknown"):
        self.judge_ids = judge_ids
        self.panel_type = panel_type  # "homo" or "hetero"
        self.k = len(judge_ids)
        self.families = [MODEL_REGISTRY[jid][2] for jid in judge_ids]
        self.n_unique_families = len(set(self.families))

    def aggregate(
        self,
        scores: Dict[str, List[Dict[str, Any]]],
        method: str = "majority_vote",
    ) -> List[str]:
        """Aggregate judge scores into panel verdicts.
        Returns list of winners ('A', 'B', or 'tie') per sample."""
        n_samples = len(next(iter(scores.values())))
        verdicts = []

        for idx in range(n_samples):
            votes = []
            for jid in self.judge_ids:
                winner = scores[jid][idx].get("winner", "tie")
                votes.append(winner)

            if method == "majority_vote":
                verdict = self._majority_vote(votes)
            else:
                verdict = self._majority_vote(votes)
            verdicts.append(verdict)

        return verdicts

    @staticmethod
    def _majority_vote(votes: List[str]) -> str:
        counts = {"A": 0, "B": 0, "tie": 0}
        for v in votes:
            counts[v] = counts.get(v, 0) + 1
        max_count = max(counts.values())
        winners = [k for k, c in counts.items() if c == max_count]
        if len(winners) == 1:
            return winners[0]
        # Tie-breaking: prefer non-tie verdict, else "tie"
        for w in winners:
            if w != "tie":
                return w
        return "tie"

    def __repr__(self) -> str:
        return f"Panel({self.judge_ids}, type={self.panel_type}, K={self.k})"


def generate_homo_panels() -> List[Panel]:
    """Generate same-family (Qwen) panels from config."""
    panels = []
    for judge_ids in HOMO_PANELS:
        panels.append(Panel(judge_ids, panel_type="homo"))
    return panels


def generate_hetero_panels() -> List[Panel]:
    """Generate cross-family panels from config."""
    panels = []
    for judge_ids in HETERO_PANELS:
        panels.append(Panel(judge_ids, panel_type="hetero"))
    return panels


def generate_all_panels() -> Dict[str, List[Panel]]:
    return {
        "homo": generate_homo_panels(),
        "hetero": generate_hetero_panels(),
    }


def measure_panel_asr(
    panel: Panel,
    clean_scores: Dict[str, List[Dict[str, Any]]],
    attacked_scores: Dict[str, List[Dict[str, Any]]],
    pairs: List[Dict[str, str]],
) -> float:
    """Measure ASR at the panel level (after majority voting)."""
    clean_verdicts = panel.aggregate(clean_scores)
    attacked_verdicts = panel.aggregate(attacked_scores)

    n_flips = 0
    n_total = 0

    for clean_v, attacked_v, pair in zip(clean_verdicts, attacked_verdicts, pairs):
        gt_winner = pair["ground_truth_winner"]
        if clean_v == gt_winner:
            n_total += 1
            if attacked_v != gt_winner:
                n_flips += 1

    asr = n_flips / max(n_total, 1)
    logger.info(f"Panel {panel}: ASR = {asr:.3f} ({n_flips}/{n_total})")
    return asr


def measure_all_panels_asr(
    panels: Dict[str, List[Panel]],
    clean_scores: Dict[str, List[Dict[str, Any]]],
    attacked_scores: Dict[str, List[Dict[str, Any]]],
    pairs: List[Dict[str, str]],
) -> Dict[str, List[Dict[str, Any]]]:
    """Measure ASR for all panels."""
    results: Dict[str, List[Dict[str, Any]]] = {"homo": [], "hetero": []}

    for ptype, panel_list in panels.items():
        for panel in panel_list:
            asr = measure_panel_asr(panel, clean_scores, attacked_scores, pairs)
            results[ptype].append({
                "judge_ids": panel.judge_ids,
                "panel_type": ptype,
                "k": panel.k,
                "n_unique_families": panel.n_unique_families,
                "asr": asr,
            })

    return results
