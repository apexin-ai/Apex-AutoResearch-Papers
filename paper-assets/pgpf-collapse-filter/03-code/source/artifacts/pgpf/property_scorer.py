"""Property scoring: lexical conformity, semantic novelty, quality (PPL), confidence.

Each scorer operates on text samples and returns float scores.
Batch interface aggregates all four properties into a list of score dicts.
GPU-intensive operations (embedding, perplexity) are batched for efficiency.
"""

import random
from typing import Optional

import numpy as np

try:
    import torch
    from torch.nn import functional as F
except ImportError:
    torch = None
    F = None


def _lazy_import_sacrebleu():
    import sacrebleu
    return sacrebleu


class PropertyScorer:
    """Compute all four properties for a batch of samples."""

    def __init__(
        self,
        embedding_model_name: str = "dunzhang/stella_en_1.5B_v5",
        corpus_k: int = 50,
        device: Optional[str] = None,
    ):
        self.embedding_model_name = embedding_model_name
        self.corpus_k = corpus_k
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")

        self._embed_model = None
        self._corpus_centroid: Optional[np.ndarray] = None
        self._corpus_texts: Optional[list[str]] = None

    def _get_embed_model(self):
        if self._embed_model is None:
            from sentence_transformers import SentenceTransformer
            self._embed_model = SentenceTransformer(self.embedding_model_name, device=self.device)
        return self._embed_model

    def set_reference_corpus(self, texts: list[str]) -> None:
        """Set gen-0 corpus for semantic novelty (centroid) and lexical conformity."""
        self._corpus_texts = texts
        model = self._get_embed_model()
        embeddings = model.encode(texts, batch_size=64, show_progress_bar=True, convert_to_numpy=True)
        self._corpus_centroid = embeddings.mean(axis=0)

    def lexical_conformity(self, sample: str, corpus_subset: Optional[list[str]] = None, k: int = 50) -> float:
        """Average BLEU-4 of sample against k random reference samples."""
        sacrebleu = _lazy_import_sacrebleu()
        if corpus_subset is None:
            if self._corpus_texts is None:
                raise ValueError("Call set_reference_corpus() first or pass corpus_subset")
            corpus_subset = self._corpus_texts

        refs = random.sample(corpus_subset, min(k, len(corpus_subset)))
        bleu_scores = []
        for ref in refs:
            bleu = sacrebleu.sentence_bleu(sample, [ref])
            bleu_scores.append(bleu.score / 100.0)
        return float(np.mean(bleu_scores))

    def semantic_novelty(self, sample_embedding: np.ndarray, corpus_centroid: Optional[np.ndarray] = None) -> float:
        """Cosine distance between sample embedding and corpus centroid."""
        if corpus_centroid is None:
            if self._corpus_centroid is None:
                raise ValueError("Call set_reference_corpus() first or pass corpus_centroid")
            corpus_centroid = self._corpus_centroid

        cos_sim = np.dot(sample_embedding, corpus_centroid) / (
            np.linalg.norm(sample_embedding) * np.linalg.norm(corpus_centroid) + 1e-8
        )
        return float(1.0 - cos_sim)

    @staticmethod
    def quality_score(sample: str, model, tokenizer, max_length: int = 2048) -> float:
        """Perplexity of sample under the given model (lower = higher quality)."""
        with torch.no_grad():
            encodings = tokenizer(sample, return_tensors="pt", truncation=True, max_length=max_length)
            input_ids = encodings.input_ids.to(model.device)
            outputs = model(input_ids, labels=input_ids)
            return float(torch.exp(outputs.loss).item())

    @staticmethod
    def confidence_score(sample: str, model, tokenizer, max_length: int = 2048) -> float:
        """Average token-level log-probability under the generating model."""
        with torch.no_grad():
            encodings = tokenizer(sample, return_tensors="pt", truncation=True, max_length=max_length)
            input_ids = encodings.input_ids.to(model.device)
            outputs = model(input_ids)
            logits = outputs.logits[:, :-1, :]
            targets = input_ids[:, 1:]
            log_probs = F.log_softmax(logits, dim=-1)
            token_log_probs = log_probs.gather(2, targets.unsqueeze(-1)).squeeze(-1)
            return float(token_log_probs.mean().item())

    def embed_texts(self, texts: list[str], batch_size: int = 64) -> np.ndarray:
        model = self._get_embed_model()
        return model.encode(texts, batch_size=batch_size, show_progress_bar=True, convert_to_numpy=True)

    def score_batch(
        self,
        samples: list[str],
        model=None,
        tokenizer=None,
        base_model=None,
        base_tokenizer=None,
        compute_lexical: bool = True,
        compute_semantic: bool = True,
        compute_quality: bool = True,
        compute_confidence: bool = True,
    ) -> list[dict[str, float]]:
        """Score a batch of samples on all four properties.

        Args:
            samples: list of text samples
            model: the generating model (for confidence)
            tokenizer: tokenizer for the generating model
            base_model: the gen-0 base model (for quality/PPL)
            base_tokenizer: tokenizer for the base model
            compute_*: toggle individual properties

        Returns:
            list of {"lexical_conformity", "semantic_novelty", "quality", "confidence"} dicts
        """
        n = len(samples)
        results: list[dict[str, float]] = [{}  for _ in range(n)]

        if compute_semantic:
            embeddings = self.embed_texts(samples)
            for i in range(n):
                results[i]["semantic_novelty"] = self.semantic_novelty(embeddings[i])

        if compute_lexical:
            for i, s in enumerate(samples):
                results[i]["lexical_conformity"] = self.lexical_conformity(s)

        if compute_quality and base_model is not None and base_tokenizer is not None:
            for i, s in enumerate(samples):
                results[i]["quality"] = self.quality_score(s, base_model, base_tokenizer)

        if compute_confidence and model is not None and tokenizer is not None:
            for i, s in enumerate(samples):
                results[i]["confidence"] = self.confidence_score(s, model, tokenizer)

        return results
