"""vLLM offline inference runner for the G-theory variance study.

Loads a model once via ``vllm.LLM`` and supports batched generation
with explicit seed control at three levels:
  1. ``LLM(seed=...)``           — engine-level RNG
  2. ``torch.cuda.manual_seed``  — CUDA kernel RNG
  3. ``SamplingParams(seed=...)`` — per-request sampling RNG

CUDA_VISIBLE_DEVICES is set from ``gpu_id`` *before* any CUDA call.

Input:  model name + generation parameters.
Output: list of ``InferenceResult`` dataclass instances (JSON-serialisable).
"""

import argparse
import json
import os
import time
from dataclasses import asdict, dataclass
from typing import Optional

import torch
from vllm import LLM, SamplingParams


@dataclass
class InferenceResult:
    prompt: str
    generated_text: str
    finish_reason: str
    model: str
    dtype: str
    temperature: float
    top_p: Optional[float]
    seed: int
    gpu_id: int
    latency_ms: float
    answer_logprob: Optional[float] = None
    top_logprobs: Optional[dict] = None


class VLLMRunner:
    """Manages a single vLLM model instance for batched inference.

    Create one runner per (model, dtype, gpu_id) combination to avoid
    model reloads.  Different temperatures / seeds reuse the same runner.
    """

    def __init__(
        self,
        model_name: str,
        gpu_id: int = 0,
        dtype: str = "bfloat16",
        seed: int = 42,
        tensor_parallel_size: int = 1,
    ):
        if "CUDA_VISIBLE_DEVICES" not in os.environ and tensor_parallel_size == 1:
            os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed(seed)
            torch.cuda.manual_seed_all(seed)

        self.model_name = model_name
        self.gpu_id = gpu_id
        self.dtype = dtype
        self.seed = seed
        self.tensor_parallel_size = tensor_parallel_size

        os.environ["VLLM_USE_V1"] = "0"

        self.llm = LLM(
            model=model_name,
            dtype=dtype,
            seed=seed,
            tensor_parallel_size=tensor_parallel_size,
            gpu_memory_utilization=0.90,
            trust_remote_code=True,
            max_model_len=4096,
            enforce_eager=True,
        )

    def generate(
        self,
        prompts: list[str],
        temperature: float = 0.0,
        top_p: Optional[float] = None,
        seed: Optional[int] = None,
        logprobs: Optional[int] = None,
        max_tokens: int = 16,
        stop: list[str] | None = None,
    ) -> list[InferenceResult]:
        """Run batched inference.

        Args:
            prompts: Prompt strings.
            temperature: 0 for greedy, >0 for stochastic sampling.
            top_p: Nucleus sampling threshold (ignored when temperature=0).
            seed: Per-request RNG seed.  Falls back to constructor seed.
            logprobs: Number of top log-probabilities to return per token.

        Returns:
            One ``InferenceResult`` per prompt, in the same order.
        """
        effective_seed = seed if seed is not None else self.seed

        if torch.cuda.is_available():
            torch.cuda.manual_seed(effective_seed)

        params = SamplingParams(
            temperature=temperature,
            top_p=top_p if (top_p is not None and temperature > 0) else 1.0,
            max_tokens=max_tokens,
            seed=effective_seed,
            logprobs=logprobs,
            stop=stop or [],
        )

        t0 = time.perf_counter()
        outputs = self.llm.generate(prompts, params)
        elapsed_ms = (time.perf_counter() - t0) * 1000
        per_prompt_ms = elapsed_ms / max(len(prompts), 1)

        results: list[InferenceResult] = []
        for output in outputs:
            answer_logprob = None
            top_lps = None
            if logprobs and output.outputs[0].logprobs:
                first_token_lps = output.outputs[0].logprobs[0]
                chosen_token_id = next(iter(first_token_lps))
                answer_logprob = first_token_lps[chosen_token_id].logprob
                top_lps = {
                    lp.decoded_token: lp.logprob
                    for lp in first_token_lps.values()
                }

            results.append(
                InferenceResult(
                    prompt=output.prompt,
                    generated_text=output.outputs[0].text.strip(),
                    finish_reason=output.outputs[0].finish_reason,
                    model=self.model_name,
                    dtype=self.dtype,
                    temperature=temperature,
                    top_p=top_p,
                    seed=effective_seed,
                    gpu_id=self.gpu_id,
                    latency_ms=round(per_prompt_ms, 2),
                    answer_logprob=answer_logprob,
                    top_logprobs=top_lps,
                )
            )
        return results


def run_single(
    model_name: str,
    gpu_id: int,
    dtype: str,
    temperature: float,
    top_p: Optional[float],
    seed: int,
    prompt: str,
) -> dict:
    """One-shot inference for a single prompt (CLI entry point)."""
    runner = VLLMRunner(model_name, gpu_id, dtype, seed)
    results = runner.generate([prompt], temperature, top_p, seed)
    return asdict(results[0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="vLLM single-prompt inference")
    parser.add_argument("--model", required=True)
    parser.add_argument("--gpu-id", type=int, default=0)
    parser.add_argument(
        "--dtype",
        choices=["float32", "bfloat16", "float16"],
        default="bfloat16",
    )
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=None)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--prompt", required=True)
    args = parser.parse_args()

    result = run_single(
        args.model, args.gpu_id, args.dtype,
        args.temperature, args.top_p, args.seed, args.prompt,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
