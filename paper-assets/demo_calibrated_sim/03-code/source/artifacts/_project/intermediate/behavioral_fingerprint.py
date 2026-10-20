"""Behavioral fingerprint extraction from τ-Bench conversation traces.

Detects question rate and politeness marker rate in user turns,
used for calibrating LLM user simulators against real user behavior
(cf. Seshadri et al. on AAVE user simulation gaps).

Input:  list[dict] with keys {role: "user"|"agent", content: str}
Output: FingerprintResult dataclass with per-turn annotations and aggregate rates.
"""

from __future__ import annotations

import re
import statistics
from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# Question detection
# ---------------------------------------------------------------------------

_QUESTION_WORD_RE = re.compile(
    r"(?:^|(?<=\.\s)|(?<=!\s)|(?<=\?\s))"  # sentence boundary
    r"((?:what|where|when|why|how|which|who|whom|whose"
    r"|is|are|was|were|do|does|did"
    r"|can|could|would|should|will|shall"
    r"|have|has|had)\b[^.!?]*\?)",
    re.IGNORECASE,
)

_QUESTION_MARK_RE = re.compile(r"[^.!?]*\?")

_TAG_QUESTION_RE = re.compile(
    r",\s*(?:right|isn't it|aren't they|wasn't it|weren't they"
    r"|doesn't it|don't they|didn't it|won't it|wouldn't it"
    r"|shouldn't it|couldn't it|hasn't it|haven't they"
    r"|ok|okay|yeah|no|huh)\s*\?",
    re.IGNORECASE,
)


class QuestionDetector:
    """Detect questions in a single user message via rule combination."""

    def detect(self, text: str) -> tuple[bool, list[str]]:
        """Return (has_question, list_of_detected_questions)."""
        if not text or not text.strip():
            return False, []

        questions: list[str] = []
        seen: set[str] = set()

        # 1) Sentences ending with '?'
        for m in _QUESTION_MARK_RE.finditer(text):
            q = m.group(0).strip()
            if q and q not in seen:
                questions.append(q)
                seen.add(q)

        # 2) Tag questions (subset of above, but ensure they're captured)
        for m in _TAG_QUESTION_RE.finditer(text):
            q = m.group(0).strip()
            if q and q not in seen:
                questions.append(q)
                seen.add(q)

        return (len(questions) > 0, questions)


# ---------------------------------------------------------------------------
# Politeness detection
# ---------------------------------------------------------------------------

_POLITENESS_PHRASES = [
    "could you please",
    "would you mind",
    "if you don't mind",
    "i'd appreciate",
    "i appreciate",
    "thank you",
    "thanks",
    "excuse me",
    "please",
    "sorry",
    "pardon",
    "grateful",
]

_POLITENESS_RES = [
    (phrase, re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE))
    for phrase in _POLITENESS_PHRASES
]


class PolitenessDetector:
    """Detect politeness markers in a single user message."""

    def detect(self, text: str) -> tuple[bool, list[str]]:
        """Return (has_politeness, list_of_detected_markers)."""
        if not text or not text.strip():
            return False, []

        markers: list[str] = []
        consumed: set[int] = set()  # character positions already claimed

        for phrase, pattern in _POLITENESS_RES:
            for m in pattern.finditer(text):
                span = set(range(m.start(), m.end()))
                if span & consumed:
                    continue  # skip overlapping shorter match
                consumed |= span
                markers.append(phrase)

        return (len(markers) > 0, markers)


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------


@dataclass
class TurnDetail:
    turn_index: int
    has_question: bool
    questions: list[str]
    has_politeness: bool
    politeness_markers: list[str]
    char_length: int
    word_count: int


@dataclass
class FingerprintResult:
    question_rate: float
    politeness_rate: float
    avg_turn_length: float
    avg_word_count: float
    turn_details: list[TurnDetail]
    total_user_turns: int
    total_turns: int


@dataclass
class BatchResult:
    mean_question_rate: float
    std_question_rate: float
    mean_politeness_rate: float
    std_politeness_rate: float
    num_traces: int


# ---------------------------------------------------------------------------
# Fingerprint extraction
# ---------------------------------------------------------------------------


class BehavioralFingerprint:
    """Extract behavioral fingerprint from a conversation trace."""

    def __init__(self) -> None:
        self._q_detector = QuestionDetector()
        self._p_detector = PolitenessDetector()

    def extract(self, trace: list[dict]) -> FingerprintResult:
        """Analyze a single conversation trace."""
        total_turns = len(trace)
        details: list[TurnDetail] = []

        for i, turn in enumerate(trace):
            if turn.get("role") != "user":
                continue
            content = turn.get("content", "")
            has_q, qs = self._q_detector.detect(content)
            has_p, ps = self._p_detector.detect(content)
            words = content.split()
            details.append(TurnDetail(
                turn_index=i,
                has_question=has_q,
                questions=qs,
                has_politeness=has_p,
                politeness_markers=ps,
                char_length=len(content),
                word_count=len(words),
            ))

        n = len(details)
        if n == 0:
            return FingerprintResult(
                question_rate=0.0,
                politeness_rate=0.0,
                avg_turn_length=0.0,
                avg_word_count=0.0,
                turn_details=details,
                total_user_turns=0,
                total_turns=total_turns,
            )

        return FingerprintResult(
            question_rate=sum(1 for d in details if d.has_question) / n,
            politeness_rate=sum(1 for d in details if d.has_politeness) / n,
            avg_turn_length=sum(d.char_length for d in details) / n,
            avg_word_count=sum(d.word_count for d in details) / n,
            turn_details=details,
            total_user_turns=n,
            total_turns=total_turns,
        )


# ---------------------------------------------------------------------------
# Batch analysis
# ---------------------------------------------------------------------------


def analyze_traces(traces: list[list[dict]]) -> BatchResult:
    """Compute aggregate statistics across multiple conversation traces."""
    fp = BehavioralFingerprint()
    results = [fp.extract(t) for t in traces]

    q_rates = [r.question_rate for r in results]
    p_rates = [r.politeness_rate for r in results]

    n = len(results)
    if n == 0:
        return BatchResult(
            mean_question_rate=0.0,
            std_question_rate=0.0,
            mean_politeness_rate=0.0,
            std_politeness_rate=0.0,
            num_traces=0,
        )

    return BatchResult(
        mean_question_rate=statistics.mean(q_rates),
        std_question_rate=statistics.pstdev(q_rates) if n > 1 else 0.0,
        mean_politeness_rate=statistics.mean(p_rates),
        std_politeness_rate=statistics.pstdev(p_rates) if n > 1 else 0.0,
        num_traces=n,
    )
