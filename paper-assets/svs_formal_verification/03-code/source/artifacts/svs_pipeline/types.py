"""Shared data types for the SVS pipeline.

All modules import from here to ensure consistent data structures
across chain sampling, formalization, verification, and evaluation.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Problem:
    """A logical reasoning problem (ProofWriter / FOLIO)."""
    id: str
    premises: list[str]
    hypothesis: str
    label: str  # "True" / "False" / "Unknown"
    dataset: str  # "proofwriter" / "folio"
    raw: dict = field(default_factory=dict)


@dataclass
class Chain:
    """A single CoT reasoning chain sampled for a problem."""
    problem_id: str
    chain_id: int
    answer: str       # extracted final answer: "True" / "False" / "Unknown"
    reasoning: str    # full CoT text
    logprobs: Optional[list[float]] = None  # per-token log probabilities


@dataclass
class AtomicClaim:
    """An atomic claim decomposed from a reasoning chain."""
    chain_id: int
    problem_id: str
    claim_index: int
    text: str                          # natural language claim
    fol: Optional[str] = None          # FOL formula string
    z3_parseable: bool = False         # whether Z3 can parse the FOL
    fol_error: Optional[str] = None    # parse/type error message if any


@dataclass
class ChainVerification:
    """Verification result for a single chain."""
    problem_id: str
    chain_id: int
    answer: str
    total_claims: int
    formalized_claims: int
    ic_score: float        # internal consistency: |MCS| / |total formalized|
    fc_score: float        # formalization confidence
    ic_sat: bool           # whether full conjunction is SAT
    mcs_size: int          # size of maximal consistent subset


@dataclass
class GroupVerification:
    """Verification result for an answer group (all chains with same answer)."""
    problem_id: str
    answer: str
    chain_verifications: list[ChainVerification]
    cclc_score: float      # cross-chain logical coherence score
    cclc_sat: bool         # whether merged FOL across chains is SAT
    group_score: float     # final composite group score
    cclc_diagnostics: dict = field(default_factory=dict)


@dataclass
class SVSResult:
    """Final SVS result for a single problem."""
    problem_id: str
    gold_label: str
    selected_answer: str
    sc_answer: str          # majority vote answer
    group_scores: dict[str, float]  # answer -> group_score
    correct_svs: bool
    correct_sc: bool
    chain_verifications: list[ChainVerification] = field(default_factory=list)
