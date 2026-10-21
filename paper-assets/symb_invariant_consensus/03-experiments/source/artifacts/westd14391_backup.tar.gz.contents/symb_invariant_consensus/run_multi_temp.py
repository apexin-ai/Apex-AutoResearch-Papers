"""
Multi-temperature SICA pipeline.
Generates traces at multiple temperatures per problem for increased diversity,
then runs the standard extraction + MAX-SAT pipeline.

Relationship to run_full_mvp.py:
  - Reuses: load_all_problems, load_checkpoint, build_extractor, compute_summary, print_summary
  - Replaces: single-temperature trace generation with multi-temperature generation
  - Output format: identical, with additional "temperature" field per trace in intermediates

Usage:
  python run_multi_temp.py --mode vllm --temperatures 0.3,0.7,1.2 --k-per-temp 4,4,4
  python run_multi_temp.py --mode vllm --temperatures 0.3,0.7,1.2 --k-per-temp 4,4,4 --resume
"""
from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import sys
import time

from sica.constraint_extractor import ConstraintExtractor, MockLLM, APIBasedLLM, VLLMBackend
from sica.trace_generator import (
    TraceGenerator, SOLVE_PROMPT, COMMONSENSE_SOLVE_PROMPT, MULTICHOICE_SOLVE_PROMPT,
    extract_boxed_answer, extract_yesno_answer, extract_choice_answer, MockGenerator,
)
from sica.pipeline import SICAPipeline
from baselines.self_consistency import SelfConsistency
from utils.math_equiv import is_equiv
from run_full_mvp import (
    load_all_problems, load_checkpoint, build_extractor,
    compute_summary, print_summary,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


class MultiTempVLLMGenerator(TraceGenerator):
    """Generates traces at multiple temperatures using vLLM async API.

    All temperature groups are dispatched concurrently.
    Each returned trace dict includes a 'temperature' field.
    """

    def __init__(self, base_url: str, api_key: [REDACTED], model: str | None,
                 temp_k_pairs: list[tuple[float, int]],
                 top_p: float = 0.95, max_tokens: int = 4096):
        import openai
        self.async_client = openai.AsyncOpenAI(base_url=base_url, api_key=[REDACTED]
        self.top_p = top_p
        self.max_tokens = max_tokens
        self.temp_k_pairs = temp_k_pairs
        if model:
            self.model = model
        else:
            client = openai.OpenAI(base_url=base_url, api_key=[REDACTED]
            models = client.models.list()
            self.model = models.data[0].id
            logger.info("Auto-detected model: %s", self.model)

    def _build_prompt(self, problem: str) -> str:
        if self.domain == "commonsense":
            return COMMONSENSE_SOLVE_PROMPT.format(problem=problem)
        elif self.domain == "multichoice":
            return MULTICHOICE_SOLVE_PROMPT.format(problem=problem)
        return SOLVE_PROMPT.format(problem=problem)

    async def _generate_single(self, prompt: str, trace_idx: int, temperature: float) -> dict:
        response = await self.async_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            top_p=self.top_p,
            max_tokens=self.max_tokens,
        )
        text = response.choices[0].message.content or ""
        answer = extract_boxed_answer(text)
        if not answer and self.domain == "commonsense":
            answer = extract_yesno_answer(text)
        elif not answer and self.domain == "multichoice":
            answer = extract_choice_answer(text)
        return {"trace": text, "answer": answer, "trace_idx": trace_idx, "temperature": temperature}

    def generate(self, problem: str, k: int = 12) -> list[dict]:
        """Generate traces across multiple temperatures. k is ignored; uses temp_k_pairs."""
        prompt = self._build_prompt(problem)

        async def _run():
            tasks = []
            idx = 0
            for temp, k_t in self.temp_k_pairs:
                for _ in range(k_t):
                    tasks.append(self._generate_single(prompt, idx, temp))
                    idx += 1
            return await asyncio.gather(*tasks)

        try:
            loop = asyncio.get_running_loop()
            import nest_asyncio
            nest_asyncio.apply()
            return list(loop.run_until_complete(_run()))
        except RuntimeError:
            return list(asyncio.run(_run()))


class MultiTempAPIGenerator(TraceGenerator):
    """Generates traces at multiple temperatures using generic OpenAI-compatible API (sequential)."""

    def __init__(self, base_url: str, api_key: [REDACTED], model: str,
                 temp_k_pairs: list[tuple[float, int]],
                 top_p: float = 0.95, max_tokens: int = 4096):
        import openai
        self.client = openai.OpenAI(base_url=base_url, api_key=[REDACTED]
        self.model = model
        self.top_p = top_p
        self.max_tokens = max_tokens
        self.temp_k_pairs = temp_k_pairs

    def _build_prompt(self, problem: str) -> str:
        if self.domain == "commonsense":
            return COMMONSENSE_SOLVE_PROMPT.format(problem=problem)
        elif self.domain == "multichoice":
            return MULTICHOICE_SOLVE_PROMPT.format(problem=problem)
        return SOLVE_PROMPT.format(problem=problem)

    def generate(self, problem: str, k: int = 12) -> list[dict]:
        """Generate traces sequentially across multiple temperatures."""
        prompt = self._build_prompt(problem)
        results = []
        idx = 0
        for temp, k_t in self.temp_k_pairs:
            for _ in range(k_t):
                resp = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temp,
                    top_p=self.top_p,
                    max_tokens=self.max_tokens,
                )
                text = resp.choices[0].message.content or ""
                answer = extract_boxed_answer(text)
                if not answer and self.domain == "commonsense":
                    answer = extract_yesno_answer(text)
                elif not answer and self.domain == "multichoice":
                    answer = extract_choice_answer(text)
                results.append({"trace": text, "answer": answer, "trace_idx": idx, "temperature": temp})
                idx += 1
        return results


def parse_temp_k_pairs(temperatures_str: str, k_per_temp_str: str) -> list[tuple[float, int]]:
    """Parse comma-separated temperature and k-per-temp strings into paired list."""
    temps = [float(t.strip()) for t in temperatures_str.split(",")]
    ks = [int(k.strip()) for k in k_per_temp_str.split(",")]
    if len(temps) != len(ks):
        raise ValueError(
            f"--temperatures has {len(temps)} values but --k-per-temp has {len(ks)}; they must match"
        )
    return list(zip(temps, ks))


def build_multi_temp_generator(args, temp_k_pairs):
    """Build a multi-temperature trace generator based on mode."""
    if args.mode == "mock":
        return MockGenerator()
    elif args.mode == "vllm":
        return MultiTempVLLMGenerator(
            base_url=args.api_base,
            api_key=[REDACTED],
            model=args.model if args.model != "auto" else None,
            temp_k_pairs=temp_k_pairs,
            max_tokens=args.max_tokens,
        )
    elif args.mode == "api":
        return MultiTempAPIGenerator(
            base_url=args.api_base,
            api_key=[REDACTED],
            model=args.model,
            temp_k_pairs=temp_k_pairs,
            max_tokens=args.max_tokens,
        )
    raise ValueError(f"Unknown mode: {args.mode}")


def main():
    parser = argparse.ArgumentParser(description="SICA Multi-Temperature Experiment")
    parser.add_argument("--mode", choices=["mock", "vllm", "api"], default="vllm")
    parser.add_argument("--temperatures", type=str, default="0.3,0.7,1.2",
                        help="Comma-separated sampling temperatures (e.g. 0.3,0.7,1.2)")
    parser.add_argument("--k-per-temp", type=str, default="4,4,4", dest="k_per_temp",
                        help="Comma-separated trace counts per temperature (must match --temperatures length)")
    parser.add_argument("--model", type=str, default="auto")
    parser.add_argument("--api-base", type=str, default="http://localhost:8000/v1")
    parser.add_argument("--api-key", type=str, default="EMPTY")
    parser.add_argument("--math-data", type=str, default="data/math500_subset.json")
    parser.add_argument("--pw-data", type=str, default="data/proofwriter_subset.json")
    parser.add_argument("--output", type=str, default="results/multi_temp_results.json")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--max-tokens", type=int, default=4096, dest="max_tokens")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--folio-data", type=str, default=None, dest="folio_data")
    parser.add_argument("--strategyqa-data", type=str, default=None, dest="strategyqa_data")
    parser.add_argument("--save-intermediates", action="store_true", dest="save_intermediates")
    args = parser.parse_args()

    temp_k_pairs = parse_temp_k_pairs(args.temperatures, args.k_per_temp)
    total_k = sum(k for _, k in temp_k_pairs)

    if args.seed is not None:
        import random
        random.seed(args.seed)

    temp_desc = " + ".join(f"T={t}x{k}" for t, k in temp_k_pairs)
    logger.info("SICA Multi-Temp | mode=%s K=%d (%s) resume=%s",
                args.mode, total_k, temp_desc, args.resume)

    problems = load_all_problems(args.math_data, args.pw_data,
                                 folio_path=args.folio_data,
                                 strategyqa_path=args.strategyqa_data)

    completed_ids = set()
    completed_results = []
    if args.resume:
        checkpoint = load_checkpoint(args.output)
        if checkpoint and "results" in checkpoint:
            completed_results = checkpoint["results"]
            completed_ids = {r["problem_id"] for r in completed_results if "problem_id" in r}
            logger.info("Resuming: %d problems already completed", len(completed_ids))

    generator = build_multi_temp_generator(args, temp_k_pairs)
    extractor = build_extractor(args)
    pipeline = SICAPipeline(trace_generator=generator, constraint_extractor=extractor, k=total_k)
    sc_baseline = SelfConsistency()

    all_results = list(completed_results)
    elapsed_times = []
    total_start = time.time()

    remaining = [(i, p) for i, p in enumerate(problems) if p["id"] not in completed_ids]
    logger.info("Running %d remaining problems (skipped %d)", len(remaining), len(completed_ids))

    for progress_idx, (i, prob) in enumerate(remaining):
        t0 = time.time()
        prob_id = prob["id"]
        dataset = prob.get("dataset", "math")
        level = prob.get("level", "unknown")

        print(f"\n--- [{progress_idx+1}/{len(remaining)}] (overall {i+1}/{len(problems)}) ---")
        print(f"ID: {prob_id} | Dataset: {dataset} | Level: {level}")
        print(f"Q: {prob['problem'][:120]}...")
        print(f"GT: {prob['answer']}")
        sys.stdout.flush()

        if dataset in ("proofwriter", "folio"):
            extractor.domain = "logic"
            pipeline.trace_generator.domain = "math"
        elif dataset == "strategyqa":
            extractor.domain = "commonsense"
            pipeline.trace_generator.domain = "commonsense"
        elif dataset == "logiqa":
            extractor.domain = "logic"
            pipeline.trace_generator.domain = "multichoice"
        else:
            extractor.domain = "math"
            pipeline.trace_generator.domain = "math"

        try:
            sica_result = pipeline.run_single(prob)
            sica_answer = sica_result.get("answer", "")
            sica_correct = is_equiv(sica_answer, prob["answer"])

            cs = sica_result.get("constraints_stats", {})
            ms = sica_result.get("maxsat_stats", {})
            timing = sica_result.get("timing", {})

            print(f"SICA: {sica_answer} ({'V' if sica_correct else 'X'})")
            print(f"  Constraints: {cs.get('total_extracted',0)} extracted -> {cs.get('unique_after_dedup',0)} unique")
            print(f"  MaxSAT: {ms.get('satisfied',0)} sat, {ms.get('excluded',0)} excl, solve={ms.get('solve_time_ms',0)}ms")
            print(f"  Timing: trace={timing.get('trace_gen_s',0):.1f}s extract={timing.get('extraction_s',0):.1f}s total={timing.get('total_s',0):.1f}s")
        except Exception as e:
            logger.error("SICA error on %s: %s", prob_id, e)
            import traceback; traceback.print_exc()
            sica_result = {"answer": "", "traces": [], "scores": {},
                           "constraints_stats": {"total_extracted": 0, "traces_with_constraints": 0, "unique_after_dedup": 0},
                           "maxsat_stats": {"satisfied": 0, "excluded": 0, "total_weight": 0, "solve_time_ms": 0},
                           "timing": {}}
            sica_answer = ""
            sica_correct = False

        try:
            traces = sica_result.get("traces", [])
            answers = [t.get("answer", "") for t in traces]
            sc_result = sc_baseline.run(prob, traces=[t.get("trace","") for t in traces], answers=answers)
            sc_answer = sc_result.get("answer", "")
            sc_correct = is_equiv(sc_answer, prob["answer"])
            print(f"SC:   {sc_answer} ({'V' if sc_correct else 'X'}) -- votes: {sc_result.get('vote_count','?')}/{len(traces)}")
        except Exception as e:
            logger.error("SC error on %s: %s", prob_id, e)
            sc_answer = ""
            sc_correct = False
            sc_result = {"vote_count": 0, "vote_distribution": {}}

        elapsed = time.time() - t0
        elapsed_times.append(elapsed)
        print(f"Time: {elapsed:.1f}s")

        avg_time = sum(elapsed_times) / len(elapsed_times)
        remaining_count = len(remaining) - (progress_idx + 1)
        eta_s = avg_time * remaining_count
        if remaining_count > 0:
            eta_min = eta_s / 60
            print(f"ETA: {eta_min:.1f} min ({remaining_count} remaining, avg {avg_time:.1f}s/prob)")

        sys.stdout.flush()

        result_entry = {
            "problem_idx": i,
            "problem_id": prob_id,
            "problem": prob["problem"],
            "dataset": dataset,
            "level": level,
            "ground_truth": prob["answer"],
            "sica_answer": sica_answer,
            "sica_scores": sica_result.get("scores", {}),
            "sica_correct": sica_correct,
            "sc_answer": sc_answer,
            "sc_vote_count": sc_result.get("vote_count", 0),
            "sc_vote_distribution": sc_result.get("vote_distribution", {}),
            "sc_correct": sc_correct,
            "constraints_stats": sica_result.get("constraints_stats", {}),
            "maxsat_stats": sica_result.get("maxsat_stats", {}),
            "timing": sica_result.get("timing", {}),
            "wall_time_s": round(elapsed, 2),
        }
        all_results.append(result_entry)

        if args.save_intermediates:
            intermed_dir = os.path.join(os.path.dirname(args.output) or ".", "intermediates")
            os.makedirs(intermed_dir, exist_ok=True)
            intermed_data = {
                "problem": prob,
                "sica_result": sica_result,
            }
            with open(os.path.join(intermed_dir, f"{prob_id}.json"), "w") as f:
                json.dump(intermed_data, f, indent=2, default=str)

            ptc_dir = os.path.join(os.path.dirname(args.output) or ".", "per_trace_constraints")
            os.makedirs(ptc_dir, exist_ok=True)
            traces = sica_result.get("traces", [])
            ptc_list = sica_result.get("per_trace_constraints", [])
            per_trace_out = []
            for t_idx, t in enumerate(traces):
                per_trace_out.append({
                    "trace_idx": t.get("trace_idx", t_idx),
                    "answer": t.get("answer", ""),
                    "temperature": t.get("temperature"),
                    "constraints": ptc_list[t_idx] if t_idx < len(ptc_list) else [],
                })
            ptc_data = {"pid": prob_id, "gt": prob.get("answer", ""), "per_trace": per_trace_out}
            with open(os.path.join(ptc_dir, f"{prob_id}.json"), "w") as f:
                json.dump(ptc_data, f, indent=2, default=str)

        summary = compute_summary(all_results, extractor.stats)
        summary["k"] = total_k
        summary["mode"] = args.mode
        summary["temperatures"] = args.temperatures
        summary["k_per_temp"] = args.k_per_temp
        summary["total_wall_time_s"] = round(time.time() - total_start, 1)
        output = {"summary": summary, "results": all_results}
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2, default=str)

    total_wall = time.time() - total_start
    summary = compute_summary(all_results, extractor.stats)
    summary["k"] = total_k
    summary["mode"] = args.mode
    summary["temperatures"] = args.temperatures
    summary["k_per_temp"] = args.k_per_temp
    summary["total_wall_time_s"] = round(total_wall, 1)

    output = {"summary": summary, "results": all_results}
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print_summary(summary)
    temp_desc = " + ".join(f"T={t}x{k}" for t, k in temp_k_pairs)
    print(f"\nTemperature config: {temp_desc}")
    print(f"Total wall time: {total_wall/60:.1f} min")
    print(f"Results saved to {args.output}")
    print("MULTI_TEMP_DONE")


if __name__ == "__main__":
    main()
