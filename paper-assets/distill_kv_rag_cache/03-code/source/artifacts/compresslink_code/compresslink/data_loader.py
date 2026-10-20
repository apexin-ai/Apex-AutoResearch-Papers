"""NaturalQuestions data loading and prompt formatting for RAG evaluation."""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class NQDataLoader:
    """Load NaturalQuestions data from pre-processed JSONL (output of prepare_nq_data.py).

    Each record: {id, question, context, answers, context_tokens, question_tokens}
    """

    def __init__(
        self,
        data_path: str,
        num_queries: int = 500,
        max_context_length: int = 4096,
        seed: int = 42,
    ):
        self.data_path = Path(data_path)
        self.num_queries = num_queries
        self.max_context_length = max_context_length
        self.seed = seed

    def load(self) -> List[Dict]:
        """Load and filter records from JSONL file.

        Returns:
            List of dicts with keys:
              id, question, context, answers, context_tokens, question_tokens
        """
        records: List[Dict] = []
        with open(self.data_path) as f:
            for line in f:
                rec = json.loads(line)
                if rec.get("context_tokens", 0) > self.max_context_length:
                    rec["context_tokens"] = self.max_context_length
                records.append(rec)
                if len(records) >= self.num_queries:
                    break
        return records

    # ------------------------------------------------------------------
    # Prompt formatting
    # ------------------------------------------------------------------

    PROMPT_TEMPLATE = (
        "Answer the question based on the context below.\n\n"
        "Context:\n{context}\n\n"
        "Question: {question}\n"
        "Answer:"
    )

    def format_prompt(
        self, question: str, context: str, tokenizer
    ) -> Dict:
        """Format question + context into model inputs.

        Returns dict with:
          input_ids        – full token ids
          context_end_pos  – token index where context ends
          chunk_boundaries – list of chunk start positions (if chunked)
        """
        prompt = self.PROMPT_TEMPLATE.format(context=context, question=question)
        encoded = tokenizer(prompt, return_tensors="pt", truncation=False)
        input_ids = encoded["input_ids"][0]

        context_prefix = "Answer the question based on the context below.\n\nContext:\n"
        prefix_len = len(tokenizer.encode(context_prefix, add_special_tokens=False))

        context_ids = tokenizer.encode(context, add_special_tokens=False)
        if len(context_ids) > self.max_context_length:
            context_ids = context_ids[: self.max_context_length]
        context_end_pos = prefix_len + len(context_ids)

        chunks, boundaries = self.chunk_context(context_ids)
        boundaries = [b + prefix_len for b in boundaries]

        return {
            "input_ids": input_ids,
            "context_end_pos": context_end_pos,
            "chunk_boundaries": boundaries,
        }

    # ------------------------------------------------------------------
    # Chunk splitting
    # ------------------------------------------------------------------

    @staticmethod
    def chunk_context(
        context_ids: List[int], chunk_size: int = 512
    ) -> Tuple[List[List[int]], List[int]]:
        """Split context token ids into fixed-size chunks.

        Returns:
            chunks          – list of token-id lists
            chunk_boundaries – start position of each chunk
        """
        chunks: List[List[int]] = []
        boundaries: List[int] = []
        for start in range(0, len(context_ids), chunk_size):
            boundaries.append(start)
            chunks.append(context_ids[start : start + chunk_size])
        return chunks, boundaries
