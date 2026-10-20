"""CIRCUS-core x CSS cross-tabulation.
Generates 2x2 table to quantify off-diagonal edges (method-specific vs cross-method-unstable).
Off-diagonal % is the MVP gate metric.
"""

from typing import Dict, Set
from dataclasses import dataclass


@dataclass
class CrossTable:
    """2x2 cross-tabulation of CIRCUS tiers vs CSS consensus."""
    stable_core: Set[str]       # CIRCUS-core AND CSS-high: robust consensus
    method_specific: Set[str]   # CIRCUS-core BUT CSS-low: stable within method, not across
    cross_unstable: Set[str]    # NOT CIRCUS-core BUT CSS-high: cross-method but config-unstable
    noise: Set[str]             # NOT CIRCUS-core AND CSS-low: discard

    @property
    def total(self) -> int:
        return len(self.stable_core) + len(self.method_specific) + \
               len(self.cross_unstable) + len(self.noise)

    @property
    def core_total(self) -> int:
        return len(self.stable_core) + len(self.method_specific)

    @property
    def core_off_diagonal_pct(self) -> float:
        """MVP gate metric: fraction of CIRCUS-core edges NOT confirmed by CSS."""
        if self.core_total == 0:
            return 0.0
        return len(self.method_specific) / self.core_total

    def summary(self) -> Dict[str, object]:
        return {
            "stable_core": len(self.stable_core),
            "method_specific": len(self.method_specific),
            "cross_unstable": len(self.cross_unstable),
            "noise": len(self.noise),
            "total": self.total,
            "core_total": self.core_total,
            "core_off_diagonal_pct": round(self.core_off_diagonal_pct, 4),
        }


def cross_tabulate(
    circus_tiers: Dict[str, str],
    css_scores: Dict[str, float],
    css_threshold: float = 0.67,
) -> CrossTable:
    """Generate 2x2 CIRCUS-core x CSS cross-tabulation.

    Args:
        circus_tiers: edge_name -> "core"|"contingent"|"noise" from CIRCUS
        css_scores: edge_name -> CSS score from cross-method voting
        css_threshold: CSS cutoff for "high consensus"

    Returns:
        CrossTable with four edge sets
    """
    all_edges = set(circus_tiers.keys()) | set(css_scores.keys())

    stable_core = set()
    method_specific = set()
    cross_unstable = set()
    noise = set()

    for edge in all_edges:
        is_circus_core = circus_tiers.get(edge) == "core"
        css_high = css_scores.get(edge, 0.0) >= css_threshold

        if is_circus_core and css_high:
            stable_core.add(edge)
        elif is_circus_core and not css_high:
            method_specific.add(edge)
        elif not is_circus_core and css_high:
            cross_unstable.add(edge)
        else:
            noise.add(edge)

    return CrossTable(
        stable_core=stable_core,
        method_specific=method_specific,
        cross_unstable=cross_unstable,
        noise=noise,
    )


def compute_off_diagonal(table: CrossTable) -> float:
    """Return core off-diagonal percentage — the MVP gate metric.

    Measures what fraction of CIRCUS-core edges are method-specific (not confirmed
    by cross-method CSS). High % = methods disagree on stable edges → StructFuse justified.
    """
    return table.core_off_diagonal_pct


def print_cross_table(table: CrossTable) -> None:
    """Pretty-print the 2x2 cross-tabulation."""
    s = table.summary()
    print(f"\n{'='*50}")
    print(f"CIRCUS-core x CSS Cross-Tabulation")
    print(f"{'='*50}")
    print(f"                  | CSS >= thr  | CSS < thr   |")
    print(f"  CIRCUS-core     | {s['stable_core']:>5} edges | {s['method_specific']:>5} edges |")
    print(f"  CIRCUS-other    | {s['cross_unstable']:>5} edges | {s['noise']:>5} edges |")
    print(f"{'='*50}")
    print(f"  Total edges: {s['total']}  |  CIRCUS-core: {s['core_total']}")
    print(f"  Core off-diagonal %: {s['core_off_diagonal_pct']*100:.1f}% (method_specific / core_total)")
    print(f"{'='*50}\n")
