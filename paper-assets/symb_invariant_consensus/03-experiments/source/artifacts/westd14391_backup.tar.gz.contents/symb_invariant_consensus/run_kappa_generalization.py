"""
exp-077: κ generalization — verify independence bottleneck across aggregation methods.

Tests whether high Fleiss' κ (low independence) is a general property of
same-model aggregation, not specific to SC+SICA. Measures κ and Effective K
for three aggregation methods on Mistral-7B / FOLIO-204:
  (a) Standard SC — reuses exp-033 traces
  (b) LLM-Debate — 4 debates × 3 rounds = 12 answer points per question
  (c) Diverse-Prompt — 4 prompt styles × 3 samples = 12 answer points

Input:  data/folio_full.json + exp-033 intermediates
Output: results/exp077_kappa_generalization/results.json
Deps:   openai, numpy, sica.pipeline (normalize_logic_answer)
"""
from __future__ import annotations

import argparse
import asyncio
import glob
import json
import logging
import os
import re
import sys
import time
from collections import Counter

import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Answer normalization (inlined from sica.pipeline)
# ---------------------------------------------------------------------------

_LOGIC_CANONICAL = {
    "true": "True", "yes": "True", "1": "True",
    "false": "False", "no": "False", "0": "False",
    "unknown": "Unknown", "uncertain": "Unknown", "undetermined": "Unknown",
}


def normalize_logic_answer(ans: str) -> str:
    s = ans.strip()
    if s.startswith('\\text{'):
        s = s[len('\\text{'):]
        if s.endswith('}'):
            s = s[:-1]
        s = s.strip()
    return _LOGIC_CANONICAL.get(s.lower(), s)


# ---------------------------------------------------------------------------
# Answer extraction from free-form text
# ---------------------------------------------------------------------------

_ANSWER_PATTERNS = [
    re.compile(r'(?:the\s+)?(?:final\s+)?answer\s+is[:\s]*\b(true|false|unknown|uncertain)\b', re.I),
    re.compile(r'(?:conclusion|therefore|thus|hence)[:\s]*.*?\b(true|false|unknown|uncertain)\b', re.I),
]


def _strip_thinking(text: str) -> str:
    idx = text.find('</think>')
    if idx != -1:
        return text[idx + len('</think>'):].strip()
    idx = text.find('<think>')
    if idx != -1:
        return ''
    return text


def extract_answer(text: str) -> str:
    clean = _strip_thinking(text)
    if not clean:
        clean = text
    boxed = re.findall(r'\\boxed\{([^}]*)\}', clean)
    if boxed:
        return normalize_logic_answer(boxed[-1])
    for pattern in _ANSWER_PATTERNS:
        matches = pattern.findall(clean)
        if matches:
            return normalize_logic_answer(matches[-1])
    last_chunk = clean[-300:].lower()
    for label in ["true", "false", "unknown", "uncertain"]:
        if label in last_chunk:
            return normalize_logic_answer(label)
    return ""


# ---------------------------------------------------------------------------
# Fleiss' kappa
# ---------------------------------------------------------------------------

def fleiss_kappa(ratings: list[dict[str, int]]) -> float:
    if not ratings:
        return float('nan')
    categories = sorted(set(cat for d in ratings for cat in d.keys()))
    cat_idx = {c: i for i, c in enumerate(categories)}
    k = len(categories)
    n = len(ratings)
    M = np.zeros((n, k))
    N_per = np.zeros(n)
    for i, d in enumerate(ratings):
        for cat, count in d.items():
            M[i, cat_idx[cat]] = count
        N_per[i] = sum(d.values())
    valid = N_per > 1
    if valid.sum() == 0:
        return float('nan')
    P_i = np.zeros(n)
    for i in range(n):
        if N_per[i] > 1:
            P_i[i] = (np.sum(M[i]**2) - N_per[i]) / (N_per[i] * (N_per[i] - 1))
    P_bar = P_i[valid].mean()
    total = N_per[valid].sum()
    p_j = M[valid].sum(axis=0) / total
    P_e = np.sum(p_j**2)
    if P_e >= 1.0:
        return 1.0
    return float((P_bar - P_e) / (1 - P_e))


def effective_k(K: int, kappa: float) -> float:
    if np.isnan(kappa):
        return float('nan')
    denom = 1 + (K - 1) * kappa
    if denom <= 0:
        return float(K)
    return K / denom


# ---------------------------------------------------------------------------
# (a) SC traces from exp-033
# ---------------------------------------------------------------------------

def load_sc_traces(sc_dir: str, limit: int | None = None) -> list[dict]:
    pattern = os.path.join(sc_dir, "intermediates", "folio_*.json")
    files = sorted(glob.glob(pattern))
    if not files:
        pattern = os.path.join(sc_dir, "folio_*.json")
        files = sorted(glob.glob(pattern))
    if not files:
        logger.error("No SC trace files found in %s", sc_dir)
        return []
    results = []
    for f in files:
        pid = os.path.splitext(os.path.basename(f))[0]
        with open(f) as fh:
            data = json.load(fh)
        sica_result = data.get("sica_result", data)
        answer_counts = sica_result.get("answer_counts", {})
        traces = sica_result.get("traces", [])
        answers = []
        for t in traces:
            a = t.get("answer", "")
            if a:
                answers.append(normalize_logic_answer(a))
        if not answer_counts and answers:
            answer_counts = dict(Counter(answers))
        if answer_counts:
            results.append({
                "problem_id": pid,
                "answer_counts": answer_counts,
                "n_raters": sum(answer_counts.values()),
                "answers": answers,
            })
        if limit and len(results) >= limit:
            break
    return results


# ---------------------------------------------------------------------------
# vLLM client (async-safe: creates fresh httpx session per event loop)
# ---------------------------------------------------------------------------

class VLLMClient:
    def __init__(self, base_url: str, model: str = "auto", temperature: float = 0.7, max_tokens: int = 4096):
        import openai
        self.base_url = base_url
        self.temperature = temperature
        self.max_tokens = max_tokens
        self._openai = openai
        sync_client = openai.OpenAI(base_url=base_url, api_key="[REDACTED]")
        if model == "auto" or not model:
            models = sync_client.models.list()
            self.model = models.data[0].id
            logger.info("Auto-detected model: %s", self.model)
        else:
            self.model = model
        sync_client.close()
        self._async_client = None

    def _get_async_client(self):
        if self._async_client is None:
            self._async_client = self._openai.AsyncOpenAI(
                base_url=self.base_url, api_key="[REDACTED]"
            )
        return self._async_client

    async def generate_async(self, prompt: str, temperature: float | None = None) -> str:
        client = self._get_async_client()
        resp = await client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature if temperature is not None else self.temperature,
            max_tokens=self.max_tokens,
        )
        return resp.choices[0].message.content or ""

    async def close(self):
        if self._async_client is not None:
            await self._async_client.close()
            self._async_client = None


# ---------------------------------------------------------------------------
# (b) LLM-Debate
# ---------------------------------------------------------------------------

DEBATE_PROPOSER = """\
Problem: {problem}

Provide your answer with detailed logical reasoning. Explain step by step.
At the end, clearly state your final answer as \\boxed{{True}}, \\boxed{{False}}, or \\boxed{{Unknown}}."""

DEBATE_CRITIC = """\
Problem: {problem}

Another reasoner gave this answer and reasoning:
{proposer_response}

You MUST disagree. Find flaws in this reasoning and argue for a DIFFERENT answer. Be specific about logical errors.
At the end, clearly state your final answer as \\boxed{{True}}, \\boxed{{False}}, or \\boxed{{Unknown}}."""

DEBATE_DEFENSE = """\
Problem: {problem}

Your original reasoning: {proposer_response}
Critic's objection: {critic_response}

Respond to the criticism. Either defend your original answer with stronger arguments, or revise your answer if the criticism is valid.
At the end, clearly state your final answer as \\boxed{{True}}, \\boxed{{False}}, or \\boxed{{Unknown}}."""


async def run_single_debate(client: VLLMClient, problem_text: str) -> dict:
    proposer_text = await client.generate_async(
        DEBATE_PROPOSER.format(problem=problem_text)
    )
    proposer_answer = extract_answer(proposer_text)

    critic_text = await client.generate_async(
        DEBATE_CRITIC.format(problem=problem_text, proposer_response=proposer_text[:2000])
    )
    critic_answer = extract_answer(critic_text)

    defense_text = await client.generate_async(
        DEBATE_DEFENSE.format(
            problem=problem_text,
            proposer_response=proposer_text[:2000],
            critic_response=critic_text[:2000],
        )
    )
    defense_answer = extract_answer(defense_text)

    return {
        "proposer_answer": proposer_answer,
        "critic_answer": critic_answer,
        "defense_answer": defense_answer,
        "proposer_response": proposer_text,
        "critic_response": critic_text,
        "defense_response": defense_text,
    }


async def run_debates_for_problem(client: VLLMClient, problem_text: str, n_debates: int) -> tuple[list[str], list[dict]]:
    all_answers = []
    debates_data = []
    for _ in range(n_debates):
        debate = await run_single_debate(client, problem_text)
        debates_data.append(debate)
        for key in ["proposer_answer", "critic_answer", "defense_answer"]:
            a = debate[key]
            if a:
                all_answers.append(a)
    return all_answers, debates_data


# ---------------------------------------------------------------------------
# (c) Diverse-Prompt
# ---------------------------------------------------------------------------

DIVERSE_PROMPTS = [
    # Style 1: Chain-of-thought
    """\
Problem: {problem}

Let's think step by step. Break down the premises, identify logical relationships, and derive the conclusion.
At the end, clearly state your final answer as \\boxed{{True}}, \\boxed{{False}}, or \\boxed{{Unknown}}.""",

    # Style 2: Direct / concise
    """\
Problem: {problem}

Analyze the logical structure directly. State which premises are relevant, what they entail, and give your answer.
Be concise. At the end, state your final answer as \\boxed{{True}}, \\boxed{{False}}, or \\boxed{{Unknown}}.""",

    # Style 3: Socratic / question-driven
    """\
Problem: {problem}

Approach this by asking yourself key questions:
- What does each premise tell us?
- Are there any contradictions?
- What can we definitively conclude?
Answer each question, then give your final determination.
At the end, state your final answer as \\boxed{{True}}, \\boxed{{False}}, or \\boxed{{Unknown}}.""",

    # Style 4: Proof-by-cases
    """\
Problem: {problem}

Solve this by systematic case analysis:
1. List all possible truth assignments for the key propositions.
2. Check which cases are consistent with ALL premises.
3. In the consistent cases, check whether the conclusion holds.
At the end, state your final answer as \\boxed{{True}}, \\boxed{{False}}, or \\boxed{{Unknown}}.""",
]


async def run_diverse_prompt_for_problem(
    client: VLLMClient, problem_text: str, n_prompts: int, n_samples: int
) -> tuple[list[str], list[dict]]:
    all_answers = []
    traces_data = []
    prompts_to_use = DIVERSE_PROMPTS[:n_prompts]
    for p_idx, prompt_template in enumerate(prompts_to_use):
        prompt = prompt_template.format(problem=problem_text)
        tasks = [client.generate_async(prompt) for _ in range(n_samples)]
        responses = await asyncio.gather(*tasks)
        for s_idx, resp in enumerate(responses):
            answer = extract_answer(resp)
            traces_data.append({
                "prompt_idx": p_idx,
                "sample_idx": s_idx,
                "response": resp,
                "answer": answer,
            })
            if answer:
                all_answers.append(answer)
    return all_answers, traces_data


# ---------------------------------------------------------------------------
# Async main loop
# ---------------------------------------------------------------------------

async def process_all(args, problems, sc_pid_map, client):
    per_question = []
    sc_ratings = []
    debate_ratings = []
    diverse_ratings = []
    total_start = time.time()

    for idx, problem in enumerate(problems):
        pid = problem.get("id", f"folio_{idx}")
        problem_text = problem["problem"]
        gt = normalize_logic_answer(problem.get("answer", ""))
        t0 = time.time()
        logger.info("[%d/%d] %s (gt=%s)", idx + 1, len(problems), pid, gt)

        entry = {
            "problem_idx": idx,
            "problem_id": pid,
            "ground_truth": gt,
        }

        # (a) SC
        sc_info = sc_pid_map.get(pid, {})
        sc_ac = sc_info.get("answer_counts", {})
        if sc_ac:
            sc_ratings.append(sc_ac)
            entry["sc_answer_counts"] = sc_ac
            entry["sc_n_raters"] = sum(sc_ac.values())
        else:
            logger.warning("  No SC data for %s", pid)
            entry["sc_answer_counts"] = {}
            entry["sc_n_raters"] = 0

        debates_data = []
        diverse_traces = []

        # (b) Debate
        if client:
            debate_answers, debates_data = await run_debates_for_problem(
                client, problem_text, args.n_debates
            )
            debate_ac = dict(Counter(debate_answers))
            debate_ratings.append(debate_ac)
            entry["debate_answer_counts"] = debate_ac
            entry["debate_n_raters"] = len(debate_answers)
            entry["debate_answers"] = debate_answers

        # (c) Diverse-Prompt
        if client:
            diverse_answers, diverse_traces = await run_diverse_prompt_for_problem(
                client, problem_text, args.n_prompts, args.n_samples_per_prompt
            )
            diverse_ac = dict(Counter(diverse_answers))
            diverse_ratings.append(diverse_ac)
            entry["diverse_answer_counts"] = diverse_ac
            entry["diverse_n_raters"] = len(diverse_answers)
            entry["diverse_answers"] = diverse_answers

        elapsed = time.time() - t0
        entry["wall_time_s"] = round(elapsed, 2)
        per_question.append(entry)

        # Save intermediates
        if args.save_intermediates:
            intermed_dir = os.path.join(os.path.dirname(args.output) or ".", "intermediates")
            os.makedirs(intermed_dir, exist_ok=True)
            intermed = {
                "problem": problem,
                "sc_answer_counts": sc_ac,
                "debates": debates_data,
                "diverse_traces": diverse_traces,
                "debate_answers": entry.get("debate_answers", []),
                "diverse_answers": entry.get("diverse_answers", []),
            }
            with open(os.path.join(intermed_dir, f"{pid}.json"), "w") as f:
                json.dump(intermed, f, indent=2, default=str)

        logger.info(
            "  SC=%s  Debate=%s  Diverse=%s  (%.1fs)",
            entry.get("sc_answer_counts", {}),
            entry.get("debate_answer_counts", {}),
            entry.get("diverse_answer_counts", {}),
            elapsed,
        )

    return per_question, sc_ratings, debate_ratings, diverse_ratings, time.time() - total_start


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="exp-077: κ generalization across aggregation methods")
    p.add_argument("--mode", choices=["vllm", "mock"], default="vllm")
    p.add_argument("--api-base", default="http://localhost:8002/v1")
    p.add_argument("--model", default="auto")
    p.add_argument("--data", default="data/folio_full.json")
    p.add_argument("--sc-traces-dir", default="results/exp033_mistral_7b_folio204",
                   help="Directory with exp-033 intermediates")
    p.add_argument("--n-debates", type=int, default=4)
    p.add_argument("--debate-rounds", type=int, default=3)
    p.add_argument("--n-prompts", type=int, default=4)
    p.add_argument("--n-samples-per-prompt", type=int, default=3)
    p.add_argument("--temperature", type=float, default=0.7)
    p.add_argument("--max-tokens", type=int, default=4096)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output", default="results/exp077_kappa_generalization/results.json")
    p.add_argument("--save-intermediates", action="store_true")
    p.add_argument("--limit", type=int, default=None, help="Limit number of problems (for dry-run)")
    return p.parse_args()


def main():
    args = parse_args()
    np.random.seed(args.seed)

    # Load FOLIO data
    with open(args.data) as f:
        problems = json.load(f)
    if args.limit:
        problems = problems[:args.limit]
    logger.info("Loaded %d problems from %s", len(problems), args.data)

    # Output dir
    out_dir = os.path.dirname(args.output) or "."
    os.makedirs(out_dir, exist_ok=True)

    # (a) SC traces
    logger.info("=== Phase (a): Loading SC traces from %s ===", args.sc_traces_dir)
    sc_data = load_sc_traces(args.sc_traces_dir, limit=args.limit)
    sc_pid_map = {d["problem_id"]: d for d in sc_data}
    logger.info("Loaded SC data for %d problems", len(sc_data))

    # vLLM client
    client = None
    if args.mode == "vllm":
        client = VLLMClient(
            base_url=args.api_base,
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
        )

    # Run async processing loop
    per_question, sc_ratings, debate_ratings, diverse_ratings, total_wall = asyncio.run(
        process_all(args, problems, sc_pid_map, client)
    )

    # --- Compute statistics ---
    n_sc = len(sc_ratings)
    sc_K = int(np.mean([sum(d.values()) for d in sc_ratings])) if sc_ratings else 12
    sc_kappa = fleiss_kappa(sc_ratings)
    sc_eff_k = effective_k(sc_K, sc_kappa)

    n_debate = len(debate_ratings)
    debate_K = int(np.mean([sum(d.values()) for d in debate_ratings])) if debate_ratings else 12
    debate_kappa = fleiss_kappa(debate_ratings)
    debate_eff_k = effective_k(debate_K, debate_kappa)

    n_diverse = len(diverse_ratings)
    diverse_K = int(np.mean([sum(d.values()) for d in diverse_ratings])) if diverse_ratings else 12
    diverse_kappa = fleiss_kappa(diverse_ratings)
    diverse_eff_k = effective_k(diverse_K, diverse_kappa)

    results = {
        "method": "kappa_generalization",
        "experiment": "exp-077",
        "results": {
            "sc": {
                "kappa": round(sc_kappa, 4) if not np.isnan(sc_kappa) else None,
                "eff_k": round(sc_eff_k, 2) if not np.isnan(sc_eff_k) else None,
                "K": sc_K,
                "n_questions": n_sc,
            },
            "debate": {
                "kappa": round(debate_kappa, 4) if not np.isnan(debate_kappa) else None,
                "eff_k": round(debate_eff_k, 2) if not np.isnan(debate_eff_k) else None,
                "K": debate_K,
                "n_questions": n_debate,
            },
            "diverse_prompt": {
                "kappa": round(diverse_kappa, 4) if not np.isnan(diverse_kappa) else None,
                "eff_k": round(diverse_eff_k, 2) if not np.isnan(diverse_eff_k) else None,
                "K": diverse_K,
                "n_questions": n_diverse,
            },
        },
        "config": {
            "model": client.model if client else "mock",
            "n_debates": args.n_debates,
            "debate_rounds": args.debate_rounds,
            "n_prompts": args.n_prompts,
            "n_samples_per_prompt": args.n_samples_per_prompt,
            "temperature": args.temperature,
            "seed": args.seed,
            "sc_traces_dir": args.sc_traces_dir,
            "data": args.data,
            "limit": args.limit,
        },
        "total_wall_time_s": round(total_wall, 1),
        "per_question": per_question,
    }

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2, default=str)

    # Print summary
    print(f"\n{'='*60}")
    print(f"exp-077 κ GENERALIZATION RESULTS ({len(per_question)} problems)")
    print(f"{'='*60}")
    for method, label in [("sc", "SC (exp-033)"), ("debate", "LLM-Debate"), ("diverse_prompt", "Diverse-Prompt")]:
        r = results["results"][method]
        kap = r["kappa"] if r["kappa"] is not None else float('nan')
        ek = r["eff_k"] if r["eff_k"] is not None else float('nan')
        print(f"  {label:20s}  κ={kap:.4f}  Eff-K={ek:.2f}  (K={r['K']}, n={r['n_questions']})")
    print(f"\n  All κ > 0.4? {all(results['results'][m]['kappa'] is not None and results['results'][m]['kappa'] > 0.4 for m in ['sc','debate','diverse_prompt'])}")
    print(f"  Wall time: {total_wall/60:.1f} min")
    print(f"  Results saved to {args.output}")
    print("KAPPA_GENERALIZATION_DONE")


if __name__ == "__main__":
    main()
