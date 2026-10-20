"""Wild 3 — Problem Perturbation Analysis.

Tests whether trace correlation (high κ) stems from surface form (variable names,
premise order) vs. genuine model bias.  For 30 FOLIO problems, generate semantically
equivalent perturbations (rename entities, shuffle premises, minor syntactic rewrites),
then compare Fleiss' κ: original-only vs perturbed-only vs mixed.

Usage:
  # 1. Start vLLM on cuda:2
  CUDA_VISIBLE_DEVICES=2 python -m vllm.entrypoints.openai.api_server \
      --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 \
      --max-model-len 8192 --gpu-memory-utilization 0.90 \
      --port 8022 --dtype auto --trust-remote-code --enforce-eager &
  # 2. Run analysis
  python analysis_problem_perturbation.py --api-base http://localhost:8022/v1
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import random
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

# ── Name replacement pools ──────────────────────────────────────────────
REPLACEMENT_NAMES = [
    "Xavier", "Yara", "Zane", "Priya", "Dmitri",
    "Fatima", "Henrik", "Lena", "Omar", "Sakura",
    "Rafael", "Ingrid", "Kwame", "Mei", "Tobias",
    "Nadia", "Soren", "Amara", "Felix", "Juno",
]

# Common proper names found in FOLIO premises
KNOWN_NAMES = {
    "Bonnie", "James", "Mary", "John", "Susan", "Tom", "Alice", "Bob",
    "Charlie", "David", "Emily", "Frank", "Grace", "Harry", "Ivy",
    "Jack", "Karen", "Leo", "Mike", "Nancy", "Oliver", "Paul",
    "Quinn", "Rachel", "Sam", "Tim", "Wendy", "Adam", "Beth",
    "Carol", "Dan", "Eve", "Gary", "Helen", "Ian", "Joe",
    "Kate", "Larry", "Megan", "Nick", "Peter", "Rose", "Steve",
    "Victor", "Zoe", "Alex", "Ben", "Chris", "Diana", "Eric",
    "Fiona", "George", "Hank", "Linda", "Mark", "Nina", "Oscar",
    "Pam", "Rita", "Sean", "Tina", "Vera", "Walter", "Bill",
    "Miroslav", "Geoff", "Wyatt", "Yang", "Bao", "Celeste",
}


def extract_names(problem_text: str) -> list[str]:
    """Extract proper names from problem text."""
    found = []
    for name in KNOWN_NAMES:
        pattern = r'\b' + re.escape(name) + r'\b'
        if re.search(pattern, problem_text):
            found.append(name)
    if not found:
        words = re.findall(r'\b([A-Z][a-z]{2,})\b', problem_text)
        stop = {
            "Given", "Determine", "True", "False", "Unknown", "Uncertain",
            "All", "Some", "Every", "Everyone", "Each", "People", "Person",
            "The", "That", "This", "They", "Their", "Then", "There", "Those",
            "Not", "And", "But", "Either", "Neither", "Both", "None",
            "Employees", "Students", "Managers", "Members", "Children",
            "Americans", "Europeans", "New", "San", "Los",
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday", "January", "February", "March",
            "April", "May", "June", "July", "August", "September",
            "October", "November", "December",
        }
        for w in words:
            if w not in stop and w not in found:
                if not any(w.lower() == s.lower() for s in stop):
                    found.append(w)
    return found


def rename_entities(text: str, name_map: dict[str, str]) -> str:
    """Globally rename entities in text."""
    for old, new in sorted(name_map.items(), key=lambda x: -len(x[0])):
        text = re.sub(r'\b' + re.escape(old) + r'\b', new, text)
        text = re.sub(r'\b' + re.escape(old.lower()) + r'\b', new.lower(), text)
    return text


def shuffle_premises(problem_text: str, rng: random.Random) -> str:
    """Shuffle premise order while keeping the structure intact."""
    parts = problem_text.split("\\n\\n")
    if len(parts) < 2:
        parts = problem_text.split("\n\n")
    if len(parts) < 2:
        return problem_text

    header_match = re.match(r'(Given the following premises:\s*\n?)', parts[0])
    if not header_match:
        return problem_text

    header = header_match.group(1)
    premise_block = parts[0][len(header):]
    conclusion_block = "\n\n".join(parts[1:])

    premises = [p.strip() for p in premise_block.split('.') if p.strip()]
    if len(premises) < 2:
        premises = [p.strip() for p in premise_block.split('\n') if p.strip()]

    rng.shuffle(premises)
    new_premise_block = '. '.join(premises)
    if not new_premise_block.endswith('.'):
        new_premise_block += '.'
    return header + new_premise_block + "\n\n" + conclusion_block


def syntactic_rewrite(text: str, rng: random.Random) -> str:
    """Minor syntactic rewrites preserving semantics."""
    rewrites = []

    def rewrite_if_then(m):
        cond = m.group(1).strip()
        cons = m.group(2).strip()
        if cons.endswith('.'):
            cons = cons[:-1]
        return f"{cons} if {cond}."

    if rng.random() < 0.5:
        text = re.sub(
            r'If ([^,]+), then ([^.]+\.)',
            rewrite_if_then,
            text,
            count=1
        )
    return text


def perturb_problem(problem: dict, rng: random.Random, replacement_pool: list[str]) -> dict:
    """Generate a semantically equivalent perturbed version of a FOLIO problem."""
    text = problem["problem"]
    names = extract_names(text)

    name_map = {}
    available = [n for n in replacement_pool if n not in names]
    rng.shuffle(available)
    for i, name in enumerate(names):
        if i < len(available):
            name_map[name] = available[i]

    perturbed_text = text
    if name_map:
        perturbed_text = rename_entities(perturbed_text, name_map)
    perturbed_text = shuffle_premises(perturbed_text, rng)
    perturbed_text = syntactic_rewrite(perturbed_text, rng)

    return {
        "id": problem["id"] + "_perturbed",
        "problem": perturbed_text,
        "answer": problem["answer"],
        "original_id": problem["id"],
        "perturbation": {
            "name_map": name_map,
            "premise_shuffled": True,
            "syntactic_rewrite": True,
        },
    }


def select_perturbable_problems(data: list[dict], n: int = 30, seed: int = 42) -> list[dict]:
    """Select n problems with named entities suitable for perturbation."""
    candidates = []
    for p in data:
        names = extract_names(p["problem"])
        if names:
            candidates.append((p, len(names)))

    candidates.sort(key=lambda x: -x[1])
    rng = random.Random(seed)

    if len(candidates) > n:
        selected = candidates[:n]
    else:
        selected = candidates

    return [c[0] for c in selected]


# ── Trace generation ────────────────────────────────────────────────────

SOLVE_PROMPT = """Solve the following logic problem step by step. Show all your reasoning.
At the end, put your final answer in \\boxed{{}}, using exactly one of: True, False, or Unknown.

Problem: {problem}"""


def normalize_logic_answer(ans: str) -> str:
    _map = {
        "true": "True", "yes": "True", "1": "True",
        "false": "False", "no": "False", "0": "False",
        "unknown": "Unknown", "uncertain": "Unknown", "undetermined": "Unknown",
    }
    s = ans.strip()
    if s.startswith('\\text{'):
        s = s[len('\\text{'):]
        if s.endswith('}'):
            s = s[:-1]
        s = s.strip()
    return _map.get(s.lower(), s)


def extract_boxed_answer(text: str) -> str:
    matches = re.findall(r'\\boxed\{([^}]*(?:\{[^}]*\}[^}]*)*)\}', text)
    return matches[-1].strip() if matches else ""


def extract_freeform_answer(text: str) -> str:
    """Fallback: extract True/False/Unknown from last few lines."""
    for line in reversed(text.strip().split('\n')[-5:]):
        ll = line.lower().strip()
        for keyword in ["true", "false", "unknown", "uncertain"]:
            if keyword in ll:
                return normalize_logic_answer(keyword)
    return ""


def generate_traces_vllm(
    problems: list[dict],
    k: int,
    api_base: str,
    temperature: float = 0.7,
    max_tokens: int = 4096,
) -> dict[str, list[dict]]:
    """Generate K traces per problem using vLLM OpenAI API."""
    import openai
    import asyncio

    client = openai.AsyncOpenAI(base_url=api_base, api_key="[REDACTED]")
    sync_client = openai.OpenAI(base_url=api_base, api_key="[REDACTED]")
    models = sync_client.models.list()
    model = models.data[0].id
    logger.info("Using model: %s", model)

    async def gen_single(problem_text: str, trace_idx: int) -> dict:
        prompt = SOLVE_PROMPT.format(problem=problem_text)
        resp = await client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            top_p=0.95,
            max_tokens=max_tokens,
        )
        text = resp.choices[0].message.content or ""
        answer = extract_boxed_answer(text)
        if not answer:
            answer = extract_freeform_answer(text)
        answer = normalize_logic_answer(answer) if answer else ""
        return {"trace": text, "answer": answer, "trace_idx": trace_idx}

    async def gen_for_problem(pid: str, problem_text: str) -> tuple[str, list[dict]]:
        tasks = [gen_single(problem_text, i) for i in range(k)]
        traces = await asyncio.gather(*tasks)
        return pid, list(traces)

    async def gen_all():
        results = {}
        batch_size = 8
        for i in range(0, len(problems), batch_size):
            batch = problems[i:i + batch_size]
            batch_tasks = [gen_for_problem(p["id"], p["problem"]) for p in batch]
            batch_results = await asyncio.gather(*batch_tasks)
            for pid, traces in batch_results:
                results[pid] = traces
            logger.info("Generated traces for %d/%d problems", min(i + batch_size, len(problems)), len(problems))
        return results

    return asyncio.run(gen_all())


# ── Fleiss' kappa ───────────────────────────────────────────────────────

def fleiss_kappa(ratings_per_problem: list[dict[str, int]]) -> float:
    """Compute Fleiss' kappa from per-problem answer counts."""
    if not ratings_per_problem:
        return float('nan')

    categories = sorted(set(cat for d in ratings_per_problem for cat in d.keys()))
    cat_idx = {c: i for i, c in enumerate(categories)}
    n_cat = len(categories)
    n_subj = len(ratings_per_problem)

    M = np.zeros((n_subj, n_cat))
    N_per = np.zeros(n_subj)
    for i, d in enumerate(ratings_per_problem):
        for cat, count in d.items():
            M[i, cat_idx[cat]] = count
        N_per[i] = sum(d.values())

    valid = N_per > 1
    if valid.sum() == 0:
        return float('nan')

    P_i = np.zeros(n_subj)
    for i in range(n_subj):
        if N_per[i] > 1:
            P_i[i] = (np.sum(M[i] ** 2) - N_per[i]) / (N_per[i] * (N_per[i] - 1))

    P_bar = P_i[valid].mean()
    total = N_per[valid].sum()
    p_j = M[valid].sum(axis=0) / total
    P_e = np.sum(p_j ** 2)

    if P_e >= 1.0:
        return 1.0
    return float((P_bar - P_e) / (1 - P_e))


def compute_sc_accuracy(traces_by_pid: dict[str, list[dict]], gold: dict[str, str]) -> float:
    """Self-consistency accuracy: majority vote."""
    correct = 0
    total = 0
    for pid, traces in traces_by_pid.items():
        answers = [t["answer"] for t in traces if t["answer"]]
        if not answers:
            continue
        counts = Counter(answers)
        majority = counts.most_common(1)[0][0]
        total += 1
        if majority == gold.get(pid, ""):
            correct += 1
    return correct / total * 100 if total > 0 else 0.0


def compute_kappa_and_stats(
    traces_by_pid: dict[str, list[dict]],
    gold: dict[str, str],
    label: str,
) -> dict:
    """Compute κ, Eff-K, and SC accuracy for a trace set."""
    ratings = []
    k_values = []
    for pid, traces in sorted(traces_by_pid.items()):
        answers = [t["answer"] for t in traces if t["answer"]]
        if len(answers) < 2:
            continue
        counts = Counter(answers)
        ratings.append(dict(counts))
        k_values.append(len(answers))

    kappa = fleiss_kappa(ratings)
    avg_k = np.mean(k_values) if k_values else 0
    eff_k = avg_k / (1 + (avg_k - 1) * kappa) if kappa != 1.0 and avg_k > 1 else avg_k
    sc_acc = compute_sc_accuracy(traces_by_pid, gold)

    result = {
        "label": label,
        "kappa": round(kappa, 4),
        "avg_K": round(avg_k, 1),
        "eff_K": round(eff_k, 2),
        "sc_acc": round(sc_acc, 2),
        "n_problems": len(ratings),
    }
    logger.info("%s: κ=%.4f, Eff-K=%.2f, SC_Acc=%.2f%%, n=%d",
                label, kappa, eff_k, sc_acc, len(ratings))
    return result


# ── Main ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Wild 3: Problem Perturbation Analysis")
    parser.add_argument("--data", default="data/folio_full.json")
    parser.add_argument("--api-base", default="http://localhost:8022/v1")
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--n-problems", type=int, default=30)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output-dir", default="results/wild3_perturbation")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    random.seed(args.seed)
    rng = random.Random(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)
    intermediates_dir = os.path.join(args.output_dir, "intermediates")
    os.makedirs(intermediates_dir, exist_ok=True)

    # Load data
    with open(args.data) as f:
        all_data = json.load(f)
    logger.info("Loaded %d FOLIO problems", len(all_data))

    # Select problems with named entities
    selected = select_perturbable_problems(all_data, n=args.n_problems, seed=args.seed)
    logger.info("Selected %d perturbable problems", len(selected))

    # Generate perturbed versions
    perturbed = []
    for p in selected:
        pp = perturb_problem(p, rng, REPLACEMENT_NAMES)
        perturbed.append(pp)

    # Save selected + perturbed data for inspection
    perturbation_data = {
        "selected_ids": [p["id"] for p in selected],
        "perturbations": [
            {
                "original_id": pp["original_id"],
                "perturbed_id": pp["id"],
                "name_map": pp["perturbation"]["name_map"],
                "original_problem": next(p["problem"] for p in selected if p["id"] == pp["original_id"]),
                "perturbed_problem": pp["problem"],
            }
            for pp in perturbed
        ],
    }
    with open(os.path.join(args.output_dir, "perturbation_data.json"), "w") as f:
        json.dump(perturbation_data, f, indent=2)
    logger.info("Saved perturbation data")

    if args.dry_run:
        logger.info("DRY RUN — showing first 3 perturbations:")
        for pp in perturbed[:3]:
            orig = next(p for p in selected if p["id"] == pp["original_id"])
            logger.info("\n=== %s → %s ===", pp["original_id"], pp["id"])
            logger.info("Name map: %s", pp["perturbation"]["name_map"])
            logger.info("ORIGINAL (first 200): %s...", orig["problem"][:200])
            logger.info("PERTURBED (first 200): %s...", pp["problem"][:200])
        logger.info("Dry run complete. %d problems selected.", len(selected))
        return

    # Generate traces
    gold = {p["id"]: p["answer"] for p in selected}
    gold.update({pp["id"]: pp["answer"] for pp in perturbed})

    all_problems = selected + perturbed
    logger.info("Generating traces for %d problems (K=%d)...", len(all_problems), args.k)
    all_traces = generate_traces_vllm(
        all_problems, k=args.k, api_base=args.api_base,
        temperature=args.temperature,
    )

    # Save intermediates
    for pid, traces in all_traces.items():
        with open(os.path.join(intermediates_dir, f"{pid}.json"), "w") as f:
            json.dump({"id": pid, "traces": traces, "gold": gold.get(pid, "")}, f, indent=2)

    # Split traces by group
    orig_ids = {p["id"] for p in selected}
    pert_ids = {pp["id"] for pp in perturbed}
    orig_to_pert = {pp["original_id"]: pp["id"] for pp in perturbed}

    orig_traces = {pid: traces for pid, traces in all_traces.items() if pid in orig_ids}
    pert_traces = {pid: traces for pid, traces in all_traces.items() if pid in pert_ids}

    # Mixed: for each problem, combine original + perturbed traces under original ID
    mixed_traces = {}
    for orig_id in orig_ids:
        pert_id = orig_to_pert.get(orig_id, "")
        combined = list(all_traces.get(orig_id, []))
        combined.extend(all_traces.get(pert_id, []))
        if combined:
            mixed_traces[orig_id] = combined

    # Compute kappa for each group
    results = {}
    results["original"] = compute_kappa_and_stats(orig_traces, gold, "Original-only")
    results["perturbed"] = compute_kappa_and_stats(pert_traces, gold, "Perturbed-only")
    results["mixed"] = compute_kappa_and_stats(mixed_traces, gold, "Mixed (Orig+Pert)")

    # Per-problem detail
    per_problem = []
    for orig_p in selected:
        oid = orig_p["id"]
        pid = orig_to_pert.get(oid, "")

        o_traces = all_traces.get(oid, [])
        p_traces = all_traces.get(pid, [])
        m_traces = o_traces + p_traces

        o_answers = [t["answer"] for t in o_traces if t["answer"]]
        p_answers = [t["answer"] for t in p_traces if t["answer"]]
        m_answers = [t["answer"] for t in m_traces if t["answer"]]

        def _kappa_single(answers):
            if len(answers) < 2:
                return float('nan')
            counts = dict(Counter(answers))
            return fleiss_kappa([counts])

        per_problem.append({
            "problem_id": oid,
            "gold": orig_p["answer"],
            "original_answers": dict(Counter(o_answers)),
            "perturbed_answers": dict(Counter(p_answers)),
            "mixed_answers": dict(Counter(m_answers)),
            "original_majority": Counter(o_answers).most_common(1)[0][0] if o_answers else "",
            "perturbed_majority": Counter(p_answers).most_common(1)[0][0] if p_answers else "",
            "mixed_majority": Counter(m_answers).most_common(1)[0][0] if m_answers else "",
            "answers_changed": (
                Counter(o_answers).most_common(1)[0][0] != Counter(p_answers).most_common(1)[0][0]
                if o_answers and p_answers else None
            ),
        })

    results["per_problem"] = per_problem
    results["config"] = {
        "k": args.k,
        "n_problems": len(selected),
        "temperature": args.temperature,
        "seed": args.seed,
        "model": "Mistral-7B-Instruct-v0.3",
    }

    # Summary stats
    n_changed = sum(1 for p in per_problem if p["answers_changed"] is True)
    n_total = sum(1 for p in per_problem if p["answers_changed"] is not None)
    results["summary"] = {
        "kappa_original": results["original"]["kappa"],
        "kappa_perturbed": results["perturbed"]["kappa"],
        "kappa_mixed": results["mixed"]["kappa"],
        "kappa_delta": round(results["mixed"]["kappa"] - results["original"]["kappa"], 4),
        "majority_changed_pct": round(n_changed / n_total * 100, 1) if n_total > 0 else 0,
        "interpretation": (
            "Surface form contributes to correlation"
            if results["mixed"]["kappa"] < results["original"]["kappa"] - 0.05
            else "Correlation mainly from model bias"
        ),
    }

    # Save
    output_path = os.path.join(args.output_dir, "results.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Results saved to %s", output_path)

    # Print summary table
    print("\n" + "=" * 70)
    print("Wild 3 — Problem Perturbation Results")
    print("=" * 70)
    print(f"{'Group':<25} {'K':>4} {'κ':>8} {'Eff-K':>8} {'SC Acc':>8}")
    print("-" * 70)
    for key in ["original", "perturbed", "mixed"]:
        r = results[key]
        print(f"{r['label']:<25} {r['avg_K']:>4.0f} {r['kappa']:>8.4f} {r['eff_K']:>8.2f} {r['sc_acc']:>7.2f}%")
    print("-" * 70)
    print(f"κ(mixed) - κ(original) = {results['summary']['kappa_delta']:+.4f}")
    print(f"Majority answer changed: {results['summary']['majority_changed_pct']:.1f}%")
    print(f"Interpretation: {results['summary']['interpretation']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
