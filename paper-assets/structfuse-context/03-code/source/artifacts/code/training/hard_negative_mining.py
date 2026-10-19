"""Data-flow-aware hard negative mining for StructFuse.

Three strategies:
  1. random         — baseline, random non-positive from same repo
  2. embedding_distance — CoCoHaNeRe-style nearest-neighbour non-positives
  3. dataflow_aware — lexically similar but data-flow disconnected (our contribution)
"""

from __future__ import annotations

import random as stdlib_random
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Set, Tuple

import numpy as np


class HardNegativeMiner(ABC):
    """Base class for hard-negative mining strategies."""

    def __init__(
        self,
        dataflow_graph: Dict[str, Set[str]] | None = None,
        embeddings: Dict[str, np.ndarray] | None = None,
        bm25_index: object | None = None,
    ):
        self.dataflow_graph = dataflow_graph or {}
        self.embeddings = embeddings or {}
        self.bm25_index = bm25_index

    @abstractmethod
    def mine(
        self,
        query: str,
        positives: List[str],
        candidates: List[str],
        num_negatives: int,
    ) -> List[Tuple[str, float]]:
        """Return list of (candidate_id, hardness_score) tuples."""
        ...

    # ── shared helpers ──────────────────────────────────────────────

    @staticmethod
    def _exclude(candidates: List[str], exclude: Set[str]) -> List[str]:
        return [c for c in candidates if c not in exclude]

    @staticmethod
    def load_embeddings(path: str | Path) -> Dict[str, np.ndarray]:
        """Load pre-computed embeddings from a .npz file (keys=file ids)."""
        data = np.load(path, allow_pickle=True)
        return {str(k): data[k] for k in data.files}

    @staticmethod
    def save_embeddings(embs: Dict[str, np.ndarray], path: str | Path) -> None:
        np.savez(path, **embs)


class RandomMiner(HardNegativeMiner):
    """Uniformly random negatives from same-repo non-positives."""

    def mine(self, query, positives, candidates, num_negatives):
        pool = self._exclude(candidates, {query, *positives})
        sampled = stdlib_random.sample(pool, min(num_negatives, len(pool)))
        return [(s, 0.0) for s in sampled]


class EmbeddingDistanceMiner(HardNegativeMiner):
    """Nearest-neighbour negatives by cosine similarity (CoCoHaNeRe baseline)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._matrix: np.ndarray | None = None
        self._keys: List[str] | None = None

    def _build_matrix(self):
        if self._matrix is not None:
            return
        self._keys = sorted(self.embeddings.keys())
        vecs = np.stack([self.embeddings[k] for k in self._keys]).astype(np.float32)
        norms = np.linalg.norm(vecs, axis=1, keepdims=True).clip(min=1e-8)
        self._matrix = vecs / norms

    def mine(self, query, positives, candidates, num_negatives):
        self._build_matrix()
        if query not in self.embeddings:
            return RandomMiner().mine(query, positives, candidates, num_negatives)

        exclude = {query, *positives}
        q_vec = self.embeddings[query].astype(np.float32)
        q_vec = q_vec / max(np.linalg.norm(q_vec), 1e-8)

        # cosine similarity against all candidates
        cand_set = set(self._exclude(candidates, exclude))
        indices = [i for i, k in enumerate(self._keys) if k in cand_set]
        if not indices:
            return []

        sims = self._matrix[indices] @ q_vec  # (N_cand,)
        top_k = min(num_negatives, len(indices))
        top_idx = np.argpartition(-sims, top_k)[:top_k]
        top_idx = top_idx[np.argsort(-sims[top_idx])]

        return [(self._keys[indices[i]], float(sims[i])) for i in top_idx]


class DataFlowAwareMiner(HardNegativeMiner):
    """Select lexically/embedding-similar but data-flow-disconnected files.

    Core insight: a file that *looks* related (high BM25 or embedding sim) but
    has no data-flow path to the query provides the strongest contrastive signal.
    """

    def __init__(self, top_k_similar: int = 50, **kwargs):
        super().__init__(**kwargs)
        self.top_k_similar = top_k_similar
        self._emb_miner = EmbeddingDistanceMiner(
            embeddings=self.embeddings,
            dataflow_graph=self.dataflow_graph,
        )

    def _is_reachable(self, src: str, dst: str) -> bool:
        return dst in self.dataflow_graph.get(src, set())

    def mine(self, query, positives, candidates, num_negatives):
        exclude = {query, *positives}

        # Step 1: get top-K similar candidates (by embedding distance)
        similar = self._emb_miner.mine(
            query, positives, candidates, self.top_k_similar
        )

        # Step 2: filter to those NOT reachable via data-flow
        disconnected = [
            (fid, score)
            for fid, score in similar
            if fid not in exclude and not self._is_reachable(query, fid)
        ]

        # Step 3: if BM25 index available, re-rank by BM25 similarity
        if self.bm25_index is not None and hasattr(self.bm25_index, "get_scores"):
            disconnected = self._rerank_bm25(query, disconnected)

        selected = disconnected[:num_negatives]

        # fallback: pad with random if not enough disconnected candidates
        if len(selected) < num_negatives:
            used = {fid for fid, _ in selected} | exclude
            pool = [c for c in candidates if c not in used]
            extra = stdlib_random.sample(pool, min(num_negatives - len(selected), len(pool)))
            selected.extend([(e, 0.0) for e in extra])

        return selected

    def _rerank_bm25(
        self, query: str, candidates: List[Tuple[str, float]]
    ) -> List[Tuple[str, float]]:
        """Re-rank disconnected candidates by BM25 score (descending)."""
        from rank_bm25 import BM25Okapi

        if not isinstance(self.bm25_index, BM25Okapi):
            return candidates

        # BM25 scores expect a tokenized query — use simple whitespace split
        scores = self.bm25_index.get_scores(query.split())
        id_to_bm25: Dict[str, float] = {}
        if hasattr(self.bm25_index, "_doc_ids"):
            for idx, doc_id in enumerate(self.bm25_index._doc_ids):
                id_to_bm25[doc_id] = float(scores[idx])

        reranked = sorted(
            candidates,
            key=lambda t: id_to_bm25.get(t[0], 0.0),
            reverse=True,
        )
        return reranked


# ── batch mining helper ─────────────────────────────────────────────

def mine_batch(
    miner: HardNegativeMiner,
    queries: List[str],
    positives_map: Dict[str, List[str]],
    all_candidates: List[str],
    num_negatives: int,
) -> Dict[str, List[Tuple[str, float]]]:
    """Mine negatives for a batch of queries. Suitable for epoch-level pre-mining."""
    results = {}
    for q in queries:
        pos = positives_map.get(q, [])
        results[q] = miner.mine(q, pos, all_candidates, num_negatives)
    return results


def build_miner(
    strategy: str,
    dataflow_graph: Dict[str, Set[str]] | None = None,
    embeddings: Dict[str, np.ndarray] | None = None,
    bm25_index: object | None = None,
    **kwargs,
) -> HardNegativeMiner:
    """Factory for miner instantiation."""
    cls_map = {
        "random": RandomMiner,
        "embedding_distance": EmbeddingDistanceMiner,
        "dataflow_aware": DataFlowAwareMiner,
    }
    if strategy not in cls_map:
        raise ValueError(f"Unknown strategy '{strategy}', choose from {list(cls_map)}")
    return cls_map[strategy](
        dataflow_graph=dataflow_graph,
        embeddings=embeddings,
        bm25_index=bm25_index,
        **kwargs,
    )
