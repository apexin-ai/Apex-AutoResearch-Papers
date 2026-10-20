"""Filter strategies for selecting synthetic samples each generation.

All filters implement the same interface: filter(samples, scores) -> filtered_samples.
retention_rate controls what fraction of samples to keep (critical control variable).
"""

import random
from abc import ABC, abstractmethod
from typing import Optional

import numpy as np


class BaseFilter(ABC):
    def __init__(self, retention_rate: float = 0.5):
        assert 0.0 < retention_rate <= 1.0
        self.retention_rate = retention_rate

    @abstractmethod
    def filter(
        self, samples: list[dict], scores: list[dict[str, float]]
    ) -> list[dict]:
        ...

    def _target_count(self, n: int) -> int:
        return max(1, int(n * self.retention_rate))


class NoFilter(BaseFilter):
    def __init__(self, retention_rate: float = 1.0):
        super().__init__(retention_rate=1.0)

    def filter(self, samples: list[dict], scores: list[dict[str, float]]) -> list[dict]:
        return list(samples)


class RandomFilter(BaseFilter):
    def filter(self, samples: list[dict], scores: list[dict[str, float]]) -> list[dict]:
        k = self._target_count(len(samples))
        return random.sample(samples, k)


class ConfidenceFilter(BaseFilter):
    """Keep top-k samples ranked by confidence (average log-prob)."""

    def filter(self, samples: list[dict], scores: list[dict[str, float]]) -> list[dict]:
        k = self._target_count(len(samples))
        paired = list(zip(samples, scores))
        paired.sort(key=lambda x: x[1].get("confidence", float("-inf")), reverse=True)
        return [s for s, _ in paired[:k]]


class PGPFStaticFilter(BaseFilter):
    """Property-guided filtering: keep samples passing ALL three property thresholds.

    Thresholds are percentile-based, computed from the score distribution.
    If fewer samples pass than retention_rate allows, return all passing samples.
    If more pass, randomly subsample to retention_rate.

    For lexical_conformity: higher = more conforming → keep above threshold.
    For quality (PPL): lower is better → keep below threshold.
    For semantic_novelty: higher means more novel → keep above threshold.
    """

    def __init__(
        self,
        retention_rate: float = 0.5,
        lexical_conformity_percentile: float = 50.0,
        semantic_novelty_percentile: float = 50.0,
        quality_percentile: float = 50.0,
    ):
        super().__init__(retention_rate)
        self.lc_pct = lexical_conformity_percentile
        self.sn_pct = semantic_novelty_percentile
        self.q_pct = quality_percentile

    def filter(self, samples: list[dict], scores: list[dict[str, float]]) -> list[dict]:
        n = len(samples)
        k = self._target_count(n)

        lc_vals = np.array([s.get("lexical_conformity", 0.0) for s in scores])
        sn_vals = np.array([s.get("semantic_novelty", 0.0) for s in scores])
        q_vals = np.array([s.get("quality", float("inf")) for s in scores])

        lc_thresh = np.percentile(lc_vals, self.lc_pct)
        sn_thresh = np.percentile(sn_vals, self.sn_pct)
        q_thresh = np.percentile(q_vals, self.q_pct)

        passing_indices = []
        for i in range(n):
            if lc_vals[i] >= lc_thresh and sn_vals[i] >= sn_thresh and q_vals[i] <= q_thresh:
                passing_indices.append(i)

        if len(passing_indices) > k:
            passing_indices = random.sample(passing_indices, k)

        return [samples[i] for i in passing_indices]


class LexicalOnlyFilter(BaseFilter):
    """Keep samples with lexical conformity above the percentile threshold."""

    def __init__(self, retention_rate: float = 0.5, threshold_percentile: float = 50.0):
        super().__init__(retention_rate)
        self.threshold_percentile = threshold_percentile

    def filter(self, samples: list[dict], scores: list[dict[str, float]]) -> list[dict]:
        n = len(samples)
        k = self._target_count(n)

        lc_vals = np.array([s.get("lexical_conformity", 0.0) for s in scores])
        thresh = np.percentile(lc_vals, self.threshold_percentile)

        passing = [i for i in range(n) if lc_vals[i] >= thresh]
        if len(passing) > k:
            passing = random.sample(passing, k)

        return [samples[i] for i in passing]


FILTER_REGISTRY: dict[str, type[BaseFilter]] = {
    "no_filter": NoFilter,
    "random": RandomFilter,
    "confidence": ConfidenceFilter,
    "pgpf_static": PGPFStaticFilter,
    "lexical_only": LexicalOnlyFilter,
}


def build_filter(config) -> BaseFilter:
    """Instantiate a filter from a PGPFConfig."""
    method = config.filter_method
    cls = FILTER_REGISTRY[method]
    if method == "pgpf_static":
        return cls(
            retention_rate=config.retention_rate,
            lexical_conformity_percentile=config.lexical_conformity_percentile,
            semantic_novelty_percentile=config.semantic_novelty_percentile,
            quality_percentile=config.quality_percentile,
        )
    if method == "lexical_only":
        return cls(
            retention_rate=config.retention_rate,
            threshold_percentile=config.lexical_conformity_percentile,
        )
    if method == "no_filter":
        return cls()
    return cls(retention_rate=config.retention_rate)
