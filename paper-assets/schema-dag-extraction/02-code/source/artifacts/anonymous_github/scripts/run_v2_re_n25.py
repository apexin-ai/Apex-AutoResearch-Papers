#!/usr/bin/env python3
"""FewRel v2 RE extreme-batch experiment: n=25 per group.

Uses stochastic greedy generation to produce diverse extreme-BCS batches,
rather than random sampling (which concentrates near the mean).
"""
import argparse
import json
import logging
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch

logger = logging.getLogger(__name__)

BASE_DIR = Path(".")
OUTPUT_DIR = BASE_DIR / "artifacts" / "exp_v2_re_n25"
SIM_MATRIX_PATH = BASE_DIR / "artifacts" / "fewrel_formal_full" / "relation_sim_matrix.pt"
BATCH_SIZE = 8
N_LOW = 25
N_HIGH = 25
DEFAULT_N_SAMPLES = 1000


def compute_bcs(type_subset, sim_matrix, type_to_idx):
    if len(type_subset) < 2:
        return 0.0
    indices = [type_to_idx[t] for t in type_subset]
    total = 0.0
    count = 0
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            total += sim_matrix[indices[i], indices[j]].item()
            count += 1
    return total / count


def stochastic_greedy_low(type_names, sim_matrix, n=8, n_candidates=100,
                          top_k_start=20, rng=None):
    """Generate diverse low-BCS batches via randomized greedy."""
    if rng is None:
        rng = random.Random(42)
    num_types = len(type_names)
    sim_np = sim_matrix.numpy()

    # Precompute all pairwise similarities
    pairs = []
    for i in range(num_types):
        for j in range(i + 1, num_types):
            pairs.append((sim_np[i, j], i, j))
    pairs.sort()

    results = []
    seen = set()
    for _ in range(n_candidates * 3):
        if len(results) >= n_candidates:
            break
        # Pick random starting pair from bottom-K most dissimilar
        k = min(top_k_start, len(pairs))
        _, si, sj = rng.choice(pairs[:k])
        selected = [si, sj]

        while len(selected) < n:
            # For each candidate, compute max similarity to any selected type
            candidates = []
            for c in range(num_types):
                if c in selected:
                    continue
                # Use mean similarity to selected (matches BCS definition)
                mean_sim = np.mean([sim_np[c, s] for s in selected])
                candidates.append((mean_sim, c))
            candidates.sort()
            # Pick from bottom-5 with some randomness
            pick_from = min(5, len(candidates))
            _, chosen = rng.choice(candidates[:pick_from])
            selected.append(chosen)

        batch = tuple(sorted(selected))
        if batch in seen:
            continue
        seen.add(batch)
        types = [type_names[i] for i in batch]
        bcs = compute_bcs(types, sim_matrix, {t: idx for idx, t in enumerate(type_names)})
        results.append({"types": types, "bcs": bcs})

    results.sort(key=lambda x: x["bcs"])
    return results


def stochastic_greedy_high(type_names, sim_matrix, n=8, n_candidates=100,
                           top_k_start=20, rng=None):
    """Generate diverse high-BCS batches via randomized greedy."""
    if rng is None:
        rng = random.Random(42)
    num_types = len(type_names)
    sim_np = sim_matrix.numpy()

    pairs = []
    for i in range(num_types):
        for j in range(i + 1, num_types):
            pairs.append((sim_np[i, j], i, j))
    pairs.sort(reverse=True)

    results = []
    seen = set()
    for _ in range(n_candidates * 3):
        if len(results) >= n_candidates:
            break
        k = min(top_k_start, len(pairs))
        _, si, sj = rng.choice(pairs[:k])
        selected = [si, sj]

        while len(selected) < n:
            candidates = []
            for c in range(num_types):
                if c in selected:
                    continue
                mean_sim = np.mean([sim_np[c, s] for s in selected])
                candidates.append((mean_sim, c))
            candidates.sort(reverse=True)
            pick_from = min(5, len(candidates))
            _, chosen = rng.choice(candidates[:pick_from])
            selected.append(chosen)

        batch = tuple(sorted(selected))
        if batch in seen:
            continue
        seen.add(batch)
        types = [type_names[i] for i in batch]
        bcs = compute_bcs(types, sim_matrix, {t: idx for idx, t in enumerate(type_names)})
        results.append({"types": types, "bcs": bcs})

    results.sort(key=lambda x: x["bcs"])
    return results


def bootstrap_delta_ci(low_accs, high_accs, n_bootstrap=10000, seed=42):
    rng = np.random.RandomState(seed)
    low_accs = np.array(low_accs)
    high_accs = np.array(high_accs)
    observed_delta = low_accs.mean() - high_accs.mean()

    deltas = []
    for _ in range(n_bootstrap):
        low_sample = rng.choice(low_accs, size=len(low_accs), replace=True)
        high_sample = rng.choice(high_accs, size=len(high_accs), replace=True)
        deltas.append(low_sample.mean() - high_sample.mean())

    deltas = np.array(deltas)
    return {
        "delta_pp": round(observed_delta * 100, 2),
        "ci_lower_pp": round(float(np.percentile(deltas, 2.5)) * 100, 2),
        "ci_upper_pp": round(float(np.percentile(deltas, 97.5)) * 100, 2),
        "low_mean_acc": round(float(low_accs.mean()), 4),
        "high_mean_acc": round(float(high_accs.mean()), 4),
        "n_bootstrap": n_bootstrap,
    }


def permutation_test(low_accs, high_accs, n_perm=10000, seed=42):
    rng = np.random.RandomState(seed)
    low_accs = np.array(low_accs)
    high_accs = np.array(high_accs)
    observed = low_accs.mean() - high_accs.mean()
    combined = np.concatenate([low_accs, high_accs])
    n_low = len(low_accs)
    count = 0
    for _ in range(n_perm):
        rng.shuffle(combined)
        perm_delta = combined[:n_low].mean() - combined[n_low:].mean()
        if perm_delta >= observed:
            count += 1
    return count / n_perm


def pearson_r(bcs_values, acc_values):
    bcs = np.array(bcs_values)
    acc = np.array(acc_values)
    if len(bcs) < 3:
        return float("nan"), float("nan")
    r = np.corrcoef(bcs, acc)[0, 1]
    n = len(bcs)
    if abs(r) >= 1.0:
        p = 0.0
    else:
        from scipy import stats
        t_stat = r * np.sqrt((n - 2) / (1 - r**2))
        p = 2 * stats.t.sf(abs(t_stat), df=n - 2)
    return float(r), float(p)


def stage_preprocess(args):
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced

    logger.info("Loading FewRel data...")
    all_samples = []
    for dp in [BASE_DIR / "data/fewrel_parquet/train.parquet",
               BASE_DIR / "data/fewrel_parquet/val.parquet"]:
        all_samples.extend(load_fewrel(data_path=str(dp)))
    all_relations = get_all_relation_types(all_samples)
    logger.info("%d samples, %d relations", len(all_samples), len(all_relations))

    n_per_rel = args.n_samples // len(all_relations)
    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)
    logger.info("Balanced sample: %d (%d/rel)", len(samples), n_per_rel)

    with open(BASE_DIR / "configs/fewrel_relation_types.json") as f:
        pid2name = json.load(f)
    relation_defs = {name: name for name in pid2name.values()}

    logger.info("Loading sim_matrix from %s", SIM_MATRIX_PATH)
    sm_data = torch.load(SIM_MATRIX_PATH, map_location="cpu", weights_only=True)
    sim_matrix = sm_data["sim_matrix"]
    type_names = sm_data["type_names"]
    type_to_idx = sm_data["type_to_idx"]

    rng = random.Random(args.seed)

    logger.info("Generating low-BCS candidates via stochastic greedy...")
    low_candidates = stochastic_greedy_low(type_names, sim_matrix,
                                            n=BATCH_SIZE, n_candidates=100,
                                            top_k_start=30, rng=rng)
    logger.info("Generated %d low-BCS candidates, BCS range [%.4f, %.4f]",
                len(low_candidates), low_candidates[0]["bcs"],
                low_candidates[-1]["bcs"])

    logger.info("Generating high-BCS candidates via stochastic greedy...")
    high_candidates = stochastic_greedy_high(type_names, sim_matrix,
                                              n=BATCH_SIZE, n_candidates=100,
                                              top_k_start=30, rng=rng)
    logger.info("Generated %d high-BCS candidates, BCS range [%.4f, %.4f]",
                len(high_candidates), high_candidates[0]["bcs"],
                high_candidates[-1]["bcs"])

    low_group = low_candidates[:N_LOW]
    high_group = high_candidates[-N_HIGH:]

    logger.info("LOW group (n=%d): BCS [%.4f, %.4f], mean=%.4f",
                len(low_group), low_group[0]["bcs"], low_group[-1]["bcs"],
                np.mean([b["bcs"] for b in low_group]))
    logger.info("HIGH group (n=%d): BCS [%.4f, %.4f], mean=%.4f",
                len(high_group), high_group[0]["bcs"], high_group[-1]["bcs"],
                np.mean([b["bcs"] for b in high_group]))

    batch_list = []
    for i, b in enumerate(low_group):
        batch_list.append({
            "batch_id": f"low_{i}",
            "types": b["types"],
            "bcs": b["bcs"],
            "group": "low",
        })
    for i, b in enumerate(high_group):
        batch_list.append({
            "batch_id": f"high_{i}",
            "types": b["types"],
            "bcs": b["bcs"],
            "group": "high",
        })

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    preprocess_config = {
        "samples": samples,
        "batch_list": batch_list,
        "relation_defs": relation_defs,
        "model_path": args.model_path,
        "max_model_len": args.max_model_len,
        "gpu_memory_utilization": args.gpu_memory_utilization,
    }
    preprocess_path = OUTPUT_DIR / "preprocess.json"
    with open(preprocess_path, "w") as f:
        json.dump(preprocess_config, f, ensure_ascii=False)

    batch_groups_path = OUTPUT_DIR / "batch_groups.json"
    with open(batch_groups_path, "w") as f:
        json.dump({"low": low_group, "high": high_group}, f, indent=2)

    logger.info("Preprocess saved to %s", preprocess_path)
    return str(preprocess_path)


def stage_extract(args):
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    sys.path.insert(0, str(BASE_DIR / "src"))
    from run_extraction import build_prompt_v2_re, build_json_schema_re

    preprocess_path = args.preprocess_path or str(OUTPUT_DIR / "preprocess.json")
    with open(preprocess_path) as f:
        config = json.load(f)

    samples = config["samples"]
    batch_list = config["batch_list"]
    relation_defs = config["relation_defs"]
    model_path = config.get("model_path", args.model_path)
    max_model_len = config.get("max_model_len", args.max_model_len)
    gpu_mem = config.get("gpu_memory_utilization", args.gpu_memory_utilization)

    results_path = OUTPUT_DIR / "results_incremental.jsonl"
    existing_results = []
    done_batches = set()

    if args.resume and results_path.exists():
        with open(results_path) as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    existing_results.append(r)
                    done_batches.add(r["batch_id"])
        logger.info("Resumed: %d existing results, %d batches done",
                    len(existing_results), len(done_batches))

    remaining = [b for b in batch_list if b["batch_id"] not in done_batches]
    if not remaining:
        logger.info("All batches done. Running analysis...")
        run_analysis(existing_results, args.n_bootstrap, args.seed)
        return

    logger.info("Loading vLLM model: %s", model_path)
    llm = LLM(
        model=model_path,
        dtype="bfloat16",
        gpu_memory_utilization=gpu_mem,
        enforce_eager=True,
        max_model_len=max_model_len,
        trust_remote_code=True,
        disable_log_stats=True,
    )

    all_results = list(existing_results)

    for bi, batch in enumerate(remaining):
        batch_id = batch["batch_id"]
        batch_types = batch["types"]
        batch_bcs = batch["bcs"]
        group = batch["group"]
        type_set = set(batch_types)

        batch_samples = [s for s in samples if s["relation_type"] in type_set]
        if not batch_samples:
            logger.warning("No samples for batch %s — skipping", batch_id)
            continue

        logger.info("[%d/%d] %s (%s): %d types, BCS=%.4f, %d samples",
                    bi + 1, len(remaining), batch_id, group,
                    len(batch_types), batch_bcs, len(batch_samples))

        schema = build_json_schema_re(batch_types)
        structured = StructuredOutputsParams(json=schema)
        sampling_params = SamplingParams(
            max_tokens=64, temperature=0.0, seed=42,
            structured_outputs=structured,
        )

        prompts = []
        sample_refs = []
        for s in batch_samples:
            p = build_prompt_v2_re(
                s["text"], s["head_entity"], s["tail_entity"],
                relation_defs, batch_types,
            )
            prompts.append(p)
            sample_refs.append(s)

        t0 = time.time()
        outputs = llm.generate(prompts, sampling_params)
        elapsed = time.time() - t0

        batch_results = []
        for oi, output in enumerate(outputs):
            s = sample_refs[oi]
            gen_text = output.outputs[0].text
            try:
                parsed = json.loads(gen_text)
                pred_rel = parsed.get("relation", "none")
            except json.JSONDecodeError:
                logger.warning("JSON parse failed for %s sample %d: %s",
                               batch_id, oi, gen_text[:100])
                pred_rel = "none"

            r = {
                "batch_id": batch_id,
                "group": group,
                "batch_types": batch_types,
                "batch_bcs": batch_bcs,
                "prediction": pred_rel,
                "ground_truth": s["relation_type"],
                "head_entity": s["head_entity"],
                "tail_entity": s["tail_entity"],
                "prompt_tokens": len(output.prompt_token_ids),
                "gen_tokens": len(output.outputs[0].token_ids),
            }
            batch_results.append(r)
            all_results.append(r)

        with open(results_path, "a") as f:
            for r in batch_results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

        correct = sum(1 for r in batch_results if r["prediction"] == r["ground_truth"])
        acc = correct / len(batch_results) if batch_results else 0
        logger.info("  acc=%.4f (%d/%d), %.1fs",
                    acc, correct, len(batch_results), elapsed)

    run_analysis(all_results, args.n_bootstrap, args.seed)


def run_analysis(results, n_bootstrap=10000, seed=42):
    batch_stats = defaultdict(lambda: {"correct": 0, "total": 0, "bcs": 0.0,
                                       "group": "", "batch_types": []})
    for r in results:
        bid = r["batch_id"]
        s = batch_stats[bid]
        s["total"] += 1
        s["bcs"] = r["batch_bcs"]
        s["group"] = r.get("group", "")
        s["batch_types"] = r["batch_types"]
        if r["prediction"] == r["ground_truth"]:
            s["correct"] += 1

    eval_results = {}
    for bid, s in batch_stats.items():
        eval_results[bid] = {
            "accuracy": s["correct"] / s["total"] if s["total"] else 0.0,
            "correct": s["correct"],
            "total": s["total"],
            "bcs": s["bcs"],
            "group": s["group"],
        }

    low_accs, high_accs = [], []
    low_bcs_vals, high_bcs_vals = [], []
    all_bcs, all_accs = [], []

    for bid, m in sorted(eval_results.items()):
        all_bcs.append(m["bcs"])
        all_accs.append(m["accuracy"])
        if bid.startswith("low_"):
            low_accs.append(m["accuracy"])
            low_bcs_vals.append(m["bcs"])
        elif bid.startswith("high_"):
            high_accs.append(m["accuracy"])
            high_bcs_vals.append(m["bcs"])

    ci = bootstrap_delta_ci(low_accs, high_accs, n_bootstrap, seed)
    perm_p = permutation_test(low_accs, high_accs, n_perm=n_bootstrap, seed=seed)
    r_val, r_p = pearson_r(all_bcs, all_accs)

    summary = {
        "n_low": len(low_accs),
        "n_high": len(high_accs),
        "n_total_batches": len(eval_results),
        "low_mean_acc": ci["low_mean_acc"],
        "high_mean_acc": ci["high_mean_acc"],
        "delta_pp": ci["delta_pp"],
        "ci_lower_pp": ci["ci_lower_pp"],
        "ci_upper_pp": ci["ci_upper_pp"],
        "permutation_p": round(perm_p, 4),
        "pearson_r": round(r_val, 4),
        "pearson_r_p": round(r_p, 6),
        "low_bcs_range": [round(min(low_bcs_vals), 4), round(max(low_bcs_vals), 4)],
        "high_bcs_range": [round(min(high_bcs_vals), 4), round(max(high_bcs_vals), 4)],
        "low_accs": [round(a, 4) for a in low_accs],
        "high_accs": [round(a, 4) for a in high_accs],
        "low_bcs_values": [round(v, 4) for v in low_bcs_vals],
        "high_bcs_values": [round(v, 4) for v in high_bcs_vals],
        "n_bootstrap": n_bootstrap,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / "results.json", "w") as f:
        json.dump(summary, f, indent=2)
    with open(OUTPUT_DIR / "eval_results.json", "w") as f:
        json.dump(eval_results, f, indent=2)

    with open(OUTPUT_DIR / "per_batch_results.csv", "w") as f:
        f.write("batch_id,group,bcs,accuracy,correct,total\n")
        for bid, m in sorted(eval_results.items()):
            f.write(f"{bid},{m['group']},{m['bcs']:.4f},{m['accuracy']:.4f},{m['correct']},{m['total']}\n")

    logger.info("=" * 70)
    logger.info("RESULTS: FewRel v2 RE Extreme-Batch n=25")
    logger.info("=" * 70)
    for bid, m in sorted(eval_results.items()):
        logger.info("  %-12s acc=%.4f (%3d/%3d) BCS=%.4f [%s]",
                    bid, m["accuracy"], m["correct"], m["total"],
                    m["bcs"], m["group"])
    logger.info("-" * 70)
    logger.info("Low  BCS (n=%d): mean_acc=%.4f  BCS range=[%.4f, %.4f]",
                len(low_accs), ci["low_mean_acc"],
                min(low_bcs_vals), max(low_bcs_vals))
    logger.info("High BCS (n=%d): mean_acc=%.4f  BCS range=[%.4f, %.4f]",
                len(high_accs), ci["high_mean_acc"],
                min(high_bcs_vals), max(high_bcs_vals))
    logger.info("Delta(low-high) = %+.2fpp  95%% CI [%+.2f, %+.2f]pp",
                ci["delta_pp"], ci["ci_lower_pp"], ci["ci_upper_pp"])
    logger.info("Permutation p-value = %.4f", perm_p)
    logger.info("Pearson r(BCS, acc) = %.4f (p=%.6f)", r_val, r_p)

    if ci["delta_pp"] > 0 and ci["ci_lower_pp"] > 0:
        logger.info("CONFIRMED: low BCS > high BCS (CI excludes 0)")
    elif ci["delta_pp"] > 0:
        logger.info("TREND: low BCS > high BCS but CI includes 0")
    else:
        logger.info("NOT CONFIRMED: delta <= 0")

    return summary


def main():
    parser = argparse.ArgumentParser(description="FewRel v2 RE n=25 extreme-batch")
    parser.add_argument("--model_path",
                        default="~/.cache/huggingface/qwen3-32b-fp8/")
    parser.add_argument("--n_samples", type=int, default=DEFAULT_N_SAMPLES)
    parser.add_argument("--n_bootstrap", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.90)
    parser.add_argument("--max_model_len", type=int, default=4096)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--analysis_only", action="store_true")
    parser.add_argument("--stage", choices=["preprocess", "extract", "all"],
                        default="all")
    parser.add_argument("--preprocess_path", default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")

    if args.analysis_only:
        results = []
        with open(OUTPUT_DIR / "results_incremental.jsonl") as f:
            for line in f:
                if line.strip():
                    results.append(json.loads(line))
        logger.info("Loaded %d results for analysis", len(results))
        run_analysis(results, args.n_bootstrap, args.seed)
        return

    if args.stage == "preprocess":
        stage_preprocess(args)
    elif args.stage == "extract":
        stage_extract(args)
    elif args.stage == "all":
        preprocess_path = stage_preprocess(args)
        if preprocess_path is None:
            return
        import subprocess
        logger.info("=== Launching extract subprocess ===")
        cmd = [sys.executable, str(Path(__file__).resolve()),
               "--stage", "extract",
               "--n_bootstrap", str(args.n_bootstrap),
               "--seed", str(args.seed)]
        if args.resume:
            cmd.append("--resume")
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
