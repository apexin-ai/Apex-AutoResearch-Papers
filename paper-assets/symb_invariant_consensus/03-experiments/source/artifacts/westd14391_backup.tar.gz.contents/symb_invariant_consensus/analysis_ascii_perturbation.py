"""
Wild 2: ASCII Perturbation Experiment
Tests whether random ASCII padding in FOLIO prompts degrades inter-trace agreement (Fleiss' kappa).

Groups:
  A - standard prompt, K=4
  B - fixed ASCII padding (100 chars, same across all traces), K=4
  C - variable ASCII padding (100 chars, different per trace), K=4

Reference: 2603.06612 "Consensus is Not Verification"
"""
import asyncio
import json
import os
import random
import re
import string
import sys
import time
import logging
from collections import Counter

import numpy as np
import openai

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)

VLLM_BASE_URL = "http://localhost:8020/v1"
VLLM_API_KEY = "[REDACTED]"
K = 4
TEMPERATURE = 0.7
TOP_P = 0.95
MAX_TOKENS = 4096
DATA_PATH = "/root/symb_invariant_consensus/data/folio_full.json"
RESULTS_DIR = "/root/symb_invariant_consensus/results/wild2_ascii_perturbation"

SOLVE_PROMPT = """Solve the following math problem step by step. Show all your reasoning.
At the end, put your final answer in \\boxed{{}}.

Problem: {problem}"""


def random_ascii(n=100):
    return ''.join(random.choices(string.printable[:94], k=n))


def extract_boxed_answer(text):
    matches = re.findall(r'\\boxed\{([^}]*(?:\{[^}]*\}[^}]*)*)\}', text)
    return matches[-1].strip() if matches else ""


def extract_folio_answer(text):
    boxed = extract_boxed_answer(text)
    if boxed:
        bl = boxed.lower().strip()
        if "true" in bl and "false" not in bl:
            return "True"
        if "false" in bl:
            return "False"
        if "unknown" in bl or "uncertain" in bl:
            return "Unknown"

    text_lower = text.lower()
    for pattern in [
        r'the (?:final )?answer is[:\s]*(true|false|unknown|uncertain)',
        r'conclusion is[:\s]*(true|false|unknown|uncertain)',
        r'(?:therefore|thus|hence)[,\s].*?(true|false|unknown|uncertain)',
    ]:
        m = re.search(pattern, text_lower)
        if m:
            ans = m.group(1)
            if ans == "uncertain":
                return "Unknown"
            return ans.capitalize()

    last_lines = text.strip().split('\n')[-5:]
    for line in reversed(last_lines):
        ll = line.lower().strip()
        for label in ["true", "false", "unknown", "uncertain"]:
            if label in ll:
                if label == "uncertain":
                    return "Unknown"
                return label.capitalize()
    return ""


def fleiss_kappa(ratings_matrix):
    n, k_cat = ratings_matrix.shape
    N_per = ratings_matrix.sum(axis=1)
    valid = N_per > 1
    if valid.sum() == 0:
        return float('nan')
    P_i = np.zeros(n)
    for i in range(n):
        if N_per[i] > 1:
            P_i[i] = (np.sum(ratings_matrix[i] ** 2) - N_per[i]) / (N_per[i] * (N_per[i] - 1))
    P_bar = P_i[valid].mean()
    total = N_per[valid].sum()
    p_j = ratings_matrix[valid].sum(axis=0) / total
    P_e = np.sum(p_j ** 2)
    if P_e >= 1.0:
        return 1.0
    return float((P_bar - P_e) / (1 - P_e))


async def generate_single(client, model, prompt, trace_idx):
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE,
        top_p=TOP_P,
        max_tokens=MAX_TOKENS,
    )
    text = response.choices[0].message.content or ""
    answer = extract_folio_answer(text)
    return {"trace": text, "answer": answer, "trace_idx": trace_idx}


async def generate_group(client, model, problem_text, k, padding_mode="none", fixed_padding=None):
    tasks = []
    for i in range(k):
        if padding_mode == "none":
            prompt = SOLVE_PROMPT.format(problem=problem_text)
        elif padding_mode == "fixed":
            prompt = SOLVE_PROMPT.format(problem=problem_text) + "\n\n" + fixed_padding
        elif padding_mode == "variable":
            prompt = SOLVE_PROMPT.format(problem=problem_text) + "\n\n" + random_ascii(100)
        else:
            raise ValueError(f"Unknown padding_mode: {padding_mode}")
        tasks.append(generate_single(client, model, prompt, i))
    return await asyncio.gather(*tasks)


async def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    with open(DATA_PATH) as f:
        folio_data = json.load(f)
    logger.info("Loaded %d FOLIO problems", len(folio_data))

    client = openai.AsyncOpenAI(base_url=VLLM_BASE_URL, api_key=[REDACTED]
    sync_client = openai.OpenAI(base_url=VLLM_BASE_URL, api_key=[REDACTED]
    models = sync_client.models.list()
    model = models.data[0].id
    logger.info("Using model: %s", model)

    checkpoint_path = os.path.join(RESULTS_DIR, "checkpoint.json")
    completed_ids = set()
    all_results = []
    if os.path.exists(checkpoint_path):
        with open(checkpoint_path) as f:
            ckpt = json.load(f)
        all_results = ckpt.get("per_problem", [])
        completed_ids = {r["id"] for r in all_results}
        logger.info("Resuming from checkpoint: %d problems done", len(completed_ids))

    fixed_pad = random_ascii(100)
    logger.info("Fixed padding (first 50 chars): %s", repr(fixed_pad[:50]))

    categories = ["True", "False", "Unknown", ""]
    cat_idx = {c: i for i, c in enumerate(categories)}

    t_start = time.time()
    remaining = [(i, p) for i, p in enumerate(folio_data) if p["id"] not in completed_ids]
    logger.info("Running %d remaining problems", len(remaining))

    for prog_idx, (orig_idx, prob) in enumerate(remaining):
        prob_id = prob["id"]
        problem_text = prob["problem"]
        gt_answer = prob["answer"]

        t0 = time.time()

        # Generate all 3 groups concurrently (12 API calls total)
        results_a, results_b, results_c = await asyncio.gather(
            generate_group(client, model, problem_text, K, padding_mode="none"),
            generate_group(client, model, problem_text, K, padding_mode="fixed", fixed_padding=fixed_pad),
            generate_group(client, model, problem_text, K, padding_mode="variable"),
        )

        answers_a = [t["answer"] for t in results_a]
        answers_b = [t["answer"] for t in results_b]
        answers_c = [t["answer"] for t in results_c]

        prob_result = {
            "id": prob_id,
            "gt_answer": gt_answer,
            "groups": {
                "A": {"answers": answers_a, "traces": [t["trace"] for t in results_a]},
                "B": {"answers": answers_b, "traces": [t["trace"] for t in results_b]},
                "C": {"answers": answers_c, "traces": [t["trace"] for t in results_c]},
            }
        }
        all_results.append(prob_result)

        dt = time.time() - t0
        elapsed = time.time() - t_start
        eta = elapsed / (prog_idx + 1) * (len(remaining) - prog_idx - 1)

        logger.info("[%d/%d] %s (GT=%s) A=%s B=%s C=%s (%.1fs, ETA %.0fs)",
                     prog_idx + 1, len(remaining), prob_id, gt_answer,
                     answers_a, answers_b, answers_c, dt, eta)

        # Checkpoint every 25 problems
        if (prog_idx + 1) % 25 == 0:
            with open(checkpoint_path, "w") as f:
                json.dump({"per_problem": all_results}, f)
            logger.info("Checkpoint saved (%d problems)", len(all_results))

    # Compute per-group kappa
    summary = {}
    desc_map = {"A": "Standard prompt", "B": "Fixed ASCII padding", "C": "Variable ASCII padding"}

    for group in ["A", "B", "C"]:
        n = len(all_results)
        matrix = np.zeros((n, len(categories)))
        for i, r in enumerate(all_results):
            for a in r["groups"][group]["answers"]:
                ci = cat_idx.get(a, cat_idx[""])
                matrix[i, ci] += 1

        kap = fleiss_kappa(matrix)
        denom = 1 + (K - 1) * kap
        eff_k = K / denom if not np.isnan(kap) and denom != 0 else float('nan')

        correct = 0
        total_valid = 0
        for r in all_results:
            gt = r["gt_answer"]
            answers = [a for a in r["groups"][group]["answers"] if a]
            if answers:
                majority = Counter(answers).most_common(1)[0][0]
                total_valid += 1
                if majority.lower() == gt.lower():
                    correct += 1

        sc_acc = correct / total_valid * 100 if total_valid > 0 else 0.0

        summary[group] = {
            "description": desc_map[group],
            "K": K,
            "kappa": round(kap, 4) if not np.isnan(kap) else None,
            "eff_k": round(eff_k, 2) if not np.isnan(eff_k) else None,
            "sc_acc": round(sc_acc, 2),
            "n_problems": n,
            "n_valid": total_valid,
        }

    output = {
        "experiment": "wild2_ascii_perturbation",
        "model": model,
        "K": K,
        "temperature": TEMPERATURE,
        "fixed_padding": fixed_pad,
        "n_problems": len(all_results),
        "summary": summary,
        "per_problem": all_results,
    }

    output_path = os.path.join(RESULTS_DIR, "results.json")
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    logger.info("Results saved to %s", output_path)

    print("\n" + "=" * 80)
    print("Wild 2: ASCII Perturbation Results")
    print("=" * 80)
    print(f"| {'Group':^7} | {'Description':^25} | {'K':^3} | {'kappa':^8} | {'Eff-K':^7} | {'SC Acc':^8} |")
    print(f"|{'-'*9}|{'-'*27}|{'-'*5}|{'-'*10}|{'-'*9}|{'-'*10}|")
    for g in ["A", "B", "C"]:
        s = summary[g]
        k_str = f"{s['kappa']:.4f}" if s['kappa'] is not None else "NaN"
        e_str = f"{s['eff_k']:.2f}" if s['eff_k'] is not None else "NaN"
        print(f"| {g:^7} | {s['description']:^25} | {s['K']:^3} | {k_str:^8} | {e_str:^7} | {s['sc_acc']:>6.2f}% |")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
