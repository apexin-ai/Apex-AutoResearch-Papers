# vLLM-based judge model service.
# Loads INT4 (AWQ) models, provides pairwise comparison and Likert scoring.

import json
import re
from typing import Any, Dict, List, Optional

from src.config import (
    MODEL_REGISTRY,
    VLLM_GPU_MEMORY_UTILIZATION,
    VLLM_MAX_MODEL_LEN,
    VLLM_MAX_TOKENS,
    VLLM_TEMPERATURE,
)

PAIRWISE_SYSTEM_PROMPT = """You are an impartial judge evaluating two responses to a question.
Compare Response A and Response B based on accuracy, completeness, and reasoning quality.
You MUST output a JSON object with exactly these fields:
{"winner": "A" or "B" or "tie", "score_a": <int 1-5>, "score_b": <int 1-5>, "reasoning": "<brief explanation>"}
Output ONLY the JSON object, nothing else."""

PAIRWISE_USER_TEMPLATE = """Question: {question}

Response A:
{response_a}

Response B:
{response_b}

Judge the two responses. Output JSON only."""

LIKERT_SYSTEM_PROMPT = """You are an impartial judge. Rate the following response on a scale of 1-5.
1=completely wrong, 2=mostly wrong, 3=partially correct, 4=mostly correct, 5=fully correct.
Output ONLY a JSON object: {"score": <int 1-5>, "reasoning": "<brief explanation>"}"""

LIKERT_USER_TEMPLATE = """Question: {question}

Response:
{response}

Rate this response. Output JSON only."""


def _parse_judge_output(text: str) -> Dict[str, Any]:
    """Extract JSON from judge model output, tolerating markdown fences."""
    text = text.strip()
    # Strip markdown code fences
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if match:
        text = match.group(1)
    else:
        # Try to find raw JSON object
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            text = match.group(0)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"error": "parse_failed", "raw": text}


class JudgeService:
    """Wraps a single vLLM model for judge scoring."""

    def __init__(self, model_id: str, model_path: Optional[str] = None, gpu_id: Optional[int] = None):
        self.model_id = model_id
        if model_path is None or gpu_id is None:
            reg = MODEL_REGISTRY[model_id]
            model_path = model_path or reg[0]
            gpu_id = gpu_id if gpu_id is not None else reg[1]
        self.model_path = model_path
        self.gpu_id = gpu_id
        self.family = MODEL_REGISTRY[model_id][2]
        self.llm = None

    def load(self) -> "JudgeService":
        import os
        from vllm import LLM, SamplingParams  # noqa: F401

        os.environ["CUDA_VISIBLE_DEVICES"] = str(self.gpu_id)

        self.llm = LLM(
            model=self.model_path,
            tensor_parallel_size=1,
            gpu_memory_utilization=VLLM_GPU_MEMORY_UTILIZATION,
            max_model_len=VLLM_MAX_MODEL_LEN,
            quantization="awq",
            trust_remote_code=True,
        )
        self._sampling_params = SamplingParams(
            temperature=VLLM_TEMPERATURE,
            max_tokens=VLLM_MAX_TOKENS,
        )
        return self

    def unload(self) -> "JudgeService":
        """Release GPU memory so another model can use the same GPU."""
        if self.llm is not None:
            del self.llm
            self.llm = None
            self._sampling_params = None
            import gc
            import torch
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        return self

    def _build_pairwise_prompt(self, question: str, response_a: str, response_b: str) -> str:
        return PAIRWISE_USER_TEMPLATE.format(
            question=question, response_a=response_a, response_b=response_b
        )

    def score(self, question: str, response_a: str, response_b: str) -> Dict[str, Any]:
        """Score a single response pair (pairwise comparison)."""
        assert self.llm is not None, "Call .load() first"
        from vllm import SamplingParams  # noqa: F811

        prompt = self._apply_chat_template(
            system=PAIRWISE_SYSTEM_PROMPT,
            user=self._build_pairwise_prompt(question, response_a, response_b),
        )
        outputs = self.llm.generate([prompt], self._sampling_params)
        raw_text = outputs[0].outputs[0].text
        result = _parse_judge_output(raw_text)
        result["judge_id"] = self.model_id
        return result

    def score_likert(self, question: str, response: str) -> Dict[str, Any]:
        """Score a single response on 1-5 Likert scale."""
        assert self.llm is not None, "Call .load() first"

        prompt = self._apply_chat_template(
            system=LIKERT_SYSTEM_PROMPT,
            user=LIKERT_USER_TEMPLATE.format(question=question, response=response),
        )
        outputs = self.llm.generate([prompt], self._sampling_params)
        raw_text = outputs[0].outputs[0].text
        result = _parse_judge_output(raw_text)
        result["judge_id"] = self.model_id
        return result

    def batch_score(self, items: List[Dict[str, str]], mode: str = "pairwise") -> List[Dict[str, Any]]:
        """Batch scoring. Each item: {question, response_a, response_b} or {question, response}."""
        assert self.llm is not None, "Call .load() first"

        if mode == "pairwise":
            prompts = [
                self._apply_chat_template(
                    system=PAIRWISE_SYSTEM_PROMPT,
                    user=self._build_pairwise_prompt(it["question"], it["response_a"], it["response_b"]),
                )
                for it in items
            ]
        else:
            prompts = [
                self._apply_chat_template(
                    system=LIKERT_SYSTEM_PROMPT,
                    user=LIKERT_USER_TEMPLATE.format(question=it["question"], response=it["response"]),
                )
                for it in items
            ]

        outputs = self.llm.generate(prompts, self._sampling_params)
        results = []
        for out in outputs:
            parsed = _parse_judge_output(out.outputs[0].text)
            parsed["judge_id"] = self.model_id
            results.append(parsed)
        return results

    def _apply_chat_template(self, system: str, user: str) -> str:
        """Build a chat-formatted prompt. Uses tokenizer's chat template if available."""
        if self.llm is not None and hasattr(self.llm, "get_tokenizer"):
            tokenizer = self.llm.get_tokenizer()
            if hasattr(tokenizer, "apply_chat_template"):
                messages = [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ]
                return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        # Fallback: simple concatenation
        return f"<|system|>\n{system}\n<|user|>\n{user}\n<|assistant|>\n"
