"""Evaluate a checkpoint with full STA (Solver Trace Ablation) metrics.

Supports both FOL (Prover9) and Prolog (swipl) logic types.

Loads a fine-tuned model, generates formalizations on a test set,
runs solver + STA ablation to compute ISR, and outputs a JSON report.

Inputs:
  --model_path   Path to HF checkpoint directory
  --data_path    JSONL file
  --logic_type   "fol" or "prolog"
  --output_path  Where to write the JSON report

Output JSON keys:
  summary.prove_rate, summary.mean_isr, summary.isr_std, summary.median_isr,
  summary.isr_pr_ratio (mean_isr / prove_rate), per-sample details in results[].
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.solvers.factory import get_solver
from src.sta.reward import sta_reward
from src.sta.prolog_reward import prolog_sta_reward

# GPU safety check: abort if target GPU has active processes (prevents OOM from GPU contention)
# Usage: wrap your command with scripts/gpu_guard.sh <gpu_id> before running eval


# --- FOL prompts ---

FOL_SYSTEM_PROMPT = (
    "You are a first-order logic (FOL) expert. "
    "Given natural language premises and a conclusion, formalize them into FOL.\n\n"
    "Output format:\n"
    "Premises:\n"
    "1. <FOL formula>\n"
    "2. <FOL formula>\n"
    "...\n"
    "Conclusion: <FOL formula>\n\n"
    "Use standard FOL notation with predicate-argument syntax: "
    "all x (P(x) -> Q(x)), exists x P(x), P(a) & Q(a), -P(a), P(a) | Q(a), P(a) -> Q(a)."
)

FOL_USER_TEMPLATE = (
    "Formalize the following in first-order logic.\n\n"
    "Context:\n{context}\n\n"
    "Statement to formalize:\n{question}"
)

# --- Prolog prompts ---

PROLOG_SYSTEM_PROMPT = (
    "You are a Prolog logic programming expert. "
    "Given natural language premises and a conclusion, formalize them into Prolog.\n\n"
    "Output format:\n"
    "Facts/Rules:\n"
    "<fact_or_rule>.\n"
    "...\n\n"
    "Query: <goal>\n\n"
    "Use standard Prolog syntax: facts (predicate(args).), rules (head :- body.), "
    "variables start with uppercase, atoms/predicates start with lowercase."
)

PROLOG_USER_TEMPLATE = (
    "Formalize the following in Prolog.\n\n"
    "Context:\n{context}\n\n"
    "Statement to formalize:\n{question}"
)


# --- Prompt config per logic type ---

LOGIC_CONFIG = {
    "fol": {
        "system_prompt": FOL_SYSTEM_PROMPT,
        "user_template": FOL_USER_TEMPLATE,
        "default_solver": "prover9",
        "reward_fn": sta_reward,
    },
    "prolog": {
        "system_prompt": PROLOG_SYSTEM_PROMPT,
        "user_template": PROLOG_USER_TEMPLATE,
        "default_solver": "prolog",
        "reward_fn": prolog_sta_reward,
    },
}


def load_data(path: str) -> list[dict]:
    data = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


def load_model(model_path: str):
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype="auto",
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()
    return model, tokenizer


def generate_formalization(
    model, tokenizer, context: str, question: str,
    system_prompt: str, user_template: str,
    max_new_tokens: int = 512,
    do_sample: bool = False, temperature: float = 1.0,
) -> str:
    import torch

    user_msg = user_template.format(context=context, question=question)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_msg},
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    inputs = tokenizer([text], return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=do_sample,
            temperature=temperature,
            pad_token_id=tokenizer.pad_token_id,
        )

    generated = outputs[0][inputs["input_ids"].shape[1]:]
    result = tokenizer.decode(generated, skip_special_tokens=True).strip()
    result = re.sub(r"<think>.*?</think>\s*", "", result, flags=re.DOTALL).strip()
    return result


def main():
    parser = argparse.ArgumentParser(description="Full STA evaluation of a checkpoint")
    parser.add_argument("--model_path", type=str, required=True)
    parser.add_argument("--data_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    parser.add_argument("--logic_type", type=str, default="fol", choices=["fol", "prolog"],
                        help="Logic type: fol (Prover9) or prolog (swipl)")
    parser.add_argument("--solver", type=str, default=None,
                        help="Solver name (default: auto based on logic_type)")
    parser.add_argument("--max_new_tokens", type=int, default=512)
    parser.add_argument("--timeout", type=int, default=5)
    parser.add_argument("--max_samples", type=int, default=None,
                        help="Max number of samples to evaluate (default: all)")
    parser.add_argument("--do_sample", action="store_true", help="Use sampling instead of greedy decoding")
    parser.add_argument("--temperature", type=float, default=1.0, help="Sampling temperature")
    args = parser.parse_args()

    cfg = LOGIC_CONFIG[args.logic_type]
    reward_fn = cfg["reward_fn"]
    solver_name = args.solver or cfg["default_solver"]
    system_prompt = cfg["system_prompt"]
    user_template = cfg["user_template"]

    data_path = args.data_path
    if not Path(data_path).exists():
        print(f"ERROR: data path {data_path} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Loading data from {data_path}...")
    data = load_data(data_path)
    if args.max_samples is not None:
        data = data[:args.max_samples]
    print(f"  {len(data)} problems loaded.")

    print(f"Loading model from {args.model_path}...")
    model, tokenizer = load_model(args.model_path)
    print("  Model loaded.")

    solver = get_solver(solver_name)
    print(f"  Solver: {type(solver).__name__}")
    print(f"  Logic type: {args.logic_type}")

    results = []
    isr_scores = []
    t_start = time.time()

    for i, problem in enumerate(data):
        context = problem.get("context", "")
        question = problem.get("question", "")
        answer = problem.get("answer", "")

        print(f"[{i+1}/{len(data)}] id={problem.get('id', i)} ...", end=" ", flush=True)

        t_sample = time.time()
        formalization = generate_formalization(
            model, tokenizer, context, question,
            system_prompt, user_template,
            args.max_new_tokens,
            do_sample=args.do_sample, temperature=args.temperature,
        )
        gen_time = time.time() - t_sample

        t_eval = time.time()
        reward = reward_fn(problem, formalization, solver, timeout=args.timeout)
        eval_time = time.time() - t_eval

        record = {
            "index": i,
            "id": problem.get("id", ""),
            "context": context,
            "question": question,
            "answer": answer,
            "formalization": formalization,
            "gen_time": round(gen_time, 2),
            "eval_time": round(eval_time, 2),
            **reward,
        }
        results.append(record)

        isr_val = reward["sta_reward"]
        isr_scores.append(isr_val)
        status = "proved" if reward["execution_reward"] > 0 else "FAILED"
        print(f"{status}  ISR={isr_val:.3f}  gen={gen_time:.1f}s  eval={eval_time:.1f}s")

    elapsed = time.time() - t_start

    n = len(isr_scores)
    proved_count = sum(1 for r in results if r["execution_reward"] > 0)
    prove_rate = proved_count / n if n else 0.0
    mean_isr = statistics.mean(isr_scores) if isr_scores else 0.0
    std_isr = statistics.stdev(isr_scores) if len(isr_scores) > 1 else 0.0
    median_isr = statistics.median(isr_scores) if isr_scores else 0.0
    isr_pr_ratio = mean_isr / prove_rate if prove_rate > 0 else 0.0

    # Proved-only ISR stats
    proved_isrs = [r["sta_reward"] for r in results if r["execution_reward"] > 0]
    proved_mean_isr = statistics.mean(proved_isrs) if proved_isrs else 0.0

    by_answer = {}
    for r in results:
        a = r["answer"]
        if a not in by_answer:
            by_answer[a] = {"isr_scores": [], "proved": 0, "total": 0}
        by_answer[a]["isr_scores"].append(r["sta_reward"])
        by_answer[a]["total"] += 1
        if r["execution_reward"] > 0:
            by_answer[a]["proved"] += 1

    answer_stats = {}
    for a, stats in by_answer.items():
        answer_stats[a] = {
            "count": stats["total"],
            "proved": stats["proved"],
            "prove_rate": stats["proved"] / stats["total"] if stats["total"] else 0.0,
            "mean_isr": statistics.mean(stats["isr_scores"]) if stats["isr_scores"] else 0.0,
        }

    summary = {
        "n_problems": n,
        "n_proved": proved_count,
        "prove_rate": round(prove_rate, 4),
        "mean_isr": round(mean_isr, 4),
        "isr_std": round(std_isr, 4),
        "median_isr": round(median_isr, 4),
        "isr_pr_ratio": round(isr_pr_ratio, 4),
        "proved_only_mean_isr": round(proved_mean_isr, 4),
        "min_isr": round(min(isr_scores), 4) if isr_scores else 0.0,
        "max_isr": round(max(isr_scores), 4) if isr_scores else 0.0,
        "by_answer_type": answer_stats,
        "elapsed_seconds": round(elapsed, 1),
        "avg_time_per_sample": round(elapsed / n, 1) if n else 0.0,
        "solver": type(solver).__name__,
        "logic_type": args.logic_type,
        "model_path": args.model_path,
    }

    output = {"summary": summary, "results": results}

    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"Results saved to {args.output_path}")
    print(f"  Logic type:   {args.logic_type}")
    print(f"  Problems:     {n}")
    print(f"  Proved:       {proved_count}/{n} ({prove_rate:.1%})")
    print(f"  Mean ISR:     {mean_isr:.4f} +/- {std_isr:.4f}")
    print(f"  Median ISR:   {median_isr:.4f}")
    print(f"  ISR/PR ratio: {isr_pr_ratio:.4f}")
    print(f"  Proved-only ISR: {proved_mean_isr:.4f}")
    print(f"  By answer type:")
    for a, s in answer_stats.items():
        print(f"    {a}: n={s['count']}, proved={s['proved']}, ISR={s['mean_isr']:.4f}")
    print(f"  Time: {elapsed:.1f}s ({summary['avg_time_per_sample']:.1f}s/sample)")


if __name__ == "__main__":
    main()
