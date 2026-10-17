#!/usr/bin/env python3
"""DocRED Phase 2: Full count curve + BCS-controlled experiment + bootstrap CI.

Phase 2a: Count curve — counts=[1,4,8,16,32,64,96], 5 random batches each
Phase 2b: BCS-controlled — count=16,32: 25 random + 5 low-BCS + 5 high-BCS
Phase 2c: Bootstrap CI — regression + quartile + Spearman on BCS-controlled data

Stages:
    python3 src/run_docred_phase2.py --stage preprocess
    python3 src/run_docred_phase2.py --stage infer
    python3 src/run_docred_phase2.py --stage analyze
    python3 src/run_docred_phase2.py --stage all
"""
import argparse
import json
import logging
import random
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

logger = logging.getLogger(__name__)

BASE_DIR = Path("/root/schema-dag-extraction")
DATA_DIR = BASE_DIR / "data" / "docred"
OUTPUT_DIR = BASE_DIR / "artifacts" / "exp_docred_confusability"

COUNTS_CURVE = [1, 4, 8, 16, 32, 64, 96]
N_RANDOM_CURVE = 5
BCS_CONTROLLED_COUNTS = [16, 32]
N_RANDOM_BCS = 25
N_EXTREME_BCS = 5
N_SAMPLES = 500
SEED = 42
MODEL_PATH = "/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/"


# ── Data Loading ──────────────────────────────────────────────────────────────

def load_docred_dev():
    with open(DATA_DIR / "dev.json") as f:
        docs = json.load(f)
    with open(DATA_DIR / "rel_info.json") as f:
        rel_info = json.load(f)

    samples = []
    for doc in docs:
        text = " ".join(" ".join(sent) for sent in doc["sents"])
        vertex_set = doc["vertexSet"]
        for label in doc["labels"]:
            h_idx, t_idx, rel_pid = label["h"], label["t"], label["r"]
            samples.append({
                "text": text,
                "head_entity": vertex_set[h_idx][0]["name"],
                "tail_entity": vertex_set[t_idx][0]["name"],
                "relation_type": rel_info.get(rel_pid, rel_pid),
                "relation_pid": rel_pid,
                "doc_title": doc["title"],
            })
    return samples, rel_info


def sample_balanced(samples, n_per_relation, seed=42):
    rng = random.Random(seed)
    by_rel = defaultdict(list)
    for s in samples:
        by_rel[s["relation_type"]].append(s)
    sampled = []
    for rel in sorted(by_rel.keys()):
        pool = by_rel[rel]
        sampled.extend(rng.sample(pool, min(n_per_relation, len(pool))))
    return sampled


# ── SCS / BCS ─────────────────────────────────────────────────────────────────

def load_scs_matrix():
    data = torch.load(OUTPUT_DIR / "scs_matrix.pt", map_location="cpu",
                      weights_only=False)
    return data["sim_matrix"], data["type_names"], data["type_to_idx"]


def compute_bcs_mean(type_subset, sim_matrix, type_to_idx):
    if len(type_subset) < 2:
        return 0.0
    indices = [type_to_idx[t] for t in type_subset]
    total, count = 0.0, 0
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            total += sim_matrix[indices[i], indices[j]].item()
            count += 1
    return total / count


def compute_bcs_max(type_subset, sim_matrix, type_to_idx):
    if len(type_subset) < 2:
        return 0.0
    indices = [type_to_idx[t] for t in type_subset]
    mx = float("-inf")
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            v = sim_matrix[indices[i], indices[j]].item()
            if v > mx:
                mx = v
    return mx


# ── Batch Construction ────────────────────────────────────────────────────────

def select_random_batches(n, num_batches, type_names, sim_matrix, type_to_idx,
                          seed=42):
    rng = random.Random(seed)
    results = []
    for _ in range(num_batches):
        chosen = rng.sample(type_names, n)
        results.append({
            "types": chosen,
            "bcs": compute_bcs_mean(chosen, sim_matrix, type_to_idx),
            "bcs_max": compute_bcs_max(chosen, sim_matrix, type_to_idx),
        })
    return results


def select_extreme_batches(n, num_batches, type_names, sim_matrix, type_to_idx,
                           mode="low", seed=42):
    """Greedy extreme batch selection.
    low  → minimize mean pairwise sim (maximally dissimilar types)
    high → maximize mean pairwise sim (maximally similar types)
    """
    rng = random.Random(seed)
    n_types = len(type_names)
    sim_np = sim_matrix.numpy()

    results = []
    for _ in range(num_batches):
        start = rng.randint(0, n_types - 1)
        selected = [start]
        remaining = set(range(n_types)) - {start}

        while len(selected) < n and remaining:
            best_idx, best_score = None, float("inf") if mode == "low" else float("-inf")
            for cand in remaining:
                score = np.mean([sim_np[cand, s] for s in selected])
                if (mode == "low" and score < best_score) or \
                   (mode == "high" and score > best_score):
                    best_score = score
                    best_idx = cand
            selected.append(best_idx)
            remaining.remove(best_idx)

        chosen = [type_names[i] for i in selected]
        results.append({
            "types": chosen,
            "bcs": compute_bcs_mean(chosen, sim_matrix, type_to_idx),
            "bcs_max": compute_bcs_max(chosen, sim_matrix, type_to_idx),
        })
    return results


def build_phase2_batch_config(sim_matrix, type_names, type_to_idx):
    config = {}

    # Phase 2a: count curve
    for count in COUNTS_CURVE:
        effective = min(count, len(type_names))
        key = f"curve_count_{effective}"
        config[key] = {
            "random": select_random_batches(
                effective, N_RANDOM_CURVE, type_names, sim_matrix, type_to_idx,
                seed=SEED + count)
        }

    # Phase 2b: BCS-controlled
    for count in BCS_CONTROLLED_COUNTS:
        key = f"bcs_count_{count}"
        config[key] = {
            "random": select_random_batches(
                count, N_RANDOM_BCS, type_names, sim_matrix, type_to_idx,
                seed=SEED + 1000 + count),
            "low_bcs": select_extreme_batches(
                count, N_EXTREME_BCS, type_names, sim_matrix, type_to_idx,
                mode="low", seed=SEED + 2000 + count),
            "high_bcs": select_extreme_batches(
                count, N_EXTREME_BCS, type_names, sim_matrix, type_to_idx,
                mode="high", seed=SEED + 3000 + count),
        }

    return config


# ── Prompt & Schema ───────────────────────────────────────────────────────────

def build_prompt_docred(text, head, tail, relation_types):
    candidates = ", ".join(sorted(relation_types))
    return (
        "Given the following document and two entities, "
        "classify the relation between them.\n\n"
        f'Document: "{text}"\n'
        f'Head entity: "{head}"\n'
        f'Tail entity: "{tail}"\n\n'
        f"Candidate relations: {candidates}\n\n"
        'Output a single JSON object: {"relation": "<relation_type>"}\n'
        'If none of the candidate relations apply, output: {"relation": "none"}'
    )


def build_json_schema_re(relation_types):
    return {
        "type": "object",
        "properties": {
            "relation": {
                "type": "string",
                "enum": sorted(relation_types) + ["none"],
            },
        },
        "required": ["relation"],
    }


# ── Inference ─────────────────────────────────────────────────────────────────

def run_phase2_inference(batch_config, samples, model_path,
                         max_model_len=4096, gpu_memory_utilization=0.90):
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    llm = LLM(
        model=model_path,
        dtype="bfloat16",
        gpu_memory_utilization=gpu_memory_utilization,
        enforce_eager=True,
        max_model_len=max_model_len,
        trust_remote_code=True,
        disable_log_stats=True,
    )

    all_results = []
    total_batches = sum(len(bs) for strats in batch_config.values()
                        for bs in strats.values())
    batch_num = 0

    for config_key in sorted(batch_config.keys()):
        strategies = batch_config[config_key]
        for strategy_name in sorted(strategies.keys()):
            batches = strategies[strategy_name]
            for bi, batch_info in enumerate(batches):
                batch_num += 1
                batch_types = batch_info["types"]
                batch_bcs = batch_info["bcs"]
                batch_id = f"{config_key}_{strategy_name}_{bi}"
                type_set = set(batch_types)

                batch_samples = [s for s in samples
                                 if s["relation_type"] in type_set]
                if not batch_samples:
                    logger.warning("No samples for %s", batch_id)
                    continue

                schema = build_json_schema_re(batch_types)
                structured = StructuredOutputsParams(json=schema)
                sampling_params = SamplingParams(
                    temperature=0, max_tokens=64, seed=SEED,
                    structured_outputs=structured,
                )

                prompts = [
                    build_prompt_docred(s["text"], s["head_entity"],
                                        s["tail_entity"], batch_types)
                    for s in batch_samples
                ]

                logger.info("[%d/%d] %s: %d types, BCS=%.4f, %d samples",
                            batch_num, total_batches, batch_id,
                            len(batch_types), batch_bcs, len(prompts))

                t0 = time.time()
                outputs = llm.generate(prompts, sampling_params)
                elapsed = time.time() - t0

                correct = 0
                for oi, output in enumerate(outputs):
                    s = batch_samples[oi]
                    try:
                        pred = json.loads(output.outputs[0].text).get(
                            "relation", "PARSE_ERROR")
                    except json.JSONDecodeError:
                        pred = "PARSE_ERROR"

                    if pred == s["relation_type"]:
                        correct += 1

                    all_results.append({
                        "batch_id": batch_id,
                        "config_key": config_key,
                        "strategy": strategy_name,
                        "batch_idx": bi,
                        "batch_types": batch_types,
                        "batch_bcs": batch_bcs,
                        "batch_bcs_max": batch_info.get("bcs_max"),
                        "ground_truth": s["relation_type"],
                        "prediction": pred,
                        "head_entity": s["head_entity"],
                        "tail_entity": s["tail_entity"],
                        "doc_title": s["doc_title"],
                    })

                logger.info("  -> acc=%.4f (%d/%d) in %.1fs",
                            correct / len(prompts), correct, len(prompts),
                            elapsed)

    return all_results


# ── Evaluation ────────────────────────────────────────────────────────────────

def evaluate_predictions(predictions):
    batch_stats = defaultdict(lambda: {
        "correct": 0, "total": 0, "bcs": 0.0, "bcs_max": 0.0,
        "config_key": "", "strategy": "", "batch_idx": 0, "num_types": 0,
    })
    for r in predictions:
        bid = r["batch_id"]
        batch_stats[bid]["total"] += 1
        if r["prediction"] == r["ground_truth"]:
            batch_stats[bid]["correct"] += 1
        batch_stats[bid]["bcs"] = r["batch_bcs"]
        batch_stats[bid]["bcs_max"] = r.get("batch_bcs_max", 0)
        batch_stats[bid]["config_key"] = r["config_key"]
        batch_stats[bid]["strategy"] = r["strategy"]
        batch_stats[bid]["batch_idx"] = r["batch_idx"]
        batch_stats[bid]["num_types"] = len(r["batch_types"])

    return {
        bid: {
            "accuracy": s["correct"] / s["total"] if s["total"] else 0,
            "correct": s["correct"],
            "total": s["total"],
            "bcs": s["bcs"],
            "bcs_max": s["bcs_max"],
            "config_key": s["config_key"],
            "strategy": s["strategy"],
            "batch_idx": s["batch_idx"],
            "num_types": s["num_types"],
        }
        for bid, s in batch_stats.items()
    }


# ── Bootstrap Analysis ────────────────────────────────────────────────────────

def bootstrap_analysis(eval_results, n_bootstrap=10000, seed=42):
    from scipy import stats as sp_stats

    rng = np.random.RandomState(seed)
    analysis = {}

    for count in BCS_CONTROLLED_COUNTS:
        bcs_key = f"bcs_count_{count}"
        batch_data = [
            {"bcs": m["bcs"], "accuracy": m["accuracy"], "strategy": m["strategy"],
             "n_samples": m["total"]}
            for m in eval_results.values()
            if m["config_key"] == bcs_key
        ]
        if len(batch_data) < 5:
            logger.warning("Too few batches for count=%d", count)
            continue

        bcs_arr = np.array([d["bcs"] for d in batch_data])
        acc_arr = np.array([d["accuracy"] for d in batch_data])
        n = len(batch_data)

        # Spearman
        spearman_r, spearman_p = sp_stats.spearmanr(bcs_arr, acc_arr)

        # OLS regression
        slope, intercept, r_val, p_val, _ = sp_stats.linregress(bcs_arr, acc_arr)

        # Bootstrap slope CI
        boot_slopes = []
        for _ in range(n_bootstrap):
            idx = rng.choice(n, size=n, replace=True)
            b_bcs, b_acc = bcs_arr[idx], acc_arr[idx]
            if np.std(b_bcs) < 1e-10:
                continue
            s, _, _, _, _ = sp_stats.linregress(b_bcs, b_acc)
            boot_slopes.append(s)
        boot_slopes = np.array(boot_slopes)
        slope_ci = [float(np.percentile(boot_slopes, 2.5)),
                     float(np.percentile(boot_slopes, 97.5))]

        # Quartile analysis
        q25, q75 = np.percentile(bcs_arr, 25), np.percentile(bcs_arr, 75)
        low_q = acc_arr[bcs_arr <= q25]
        high_q = acc_arr[bcs_arr >= q75]
        gap = float(np.mean(low_q) - np.mean(high_q)) if len(low_q) and len(high_q) else 0.0

        # Bootstrap quartile gap CI
        boot_gaps = []
        for _ in range(n_bootstrap):
            idx = rng.choice(n, size=n, replace=True)
            b_bcs, b_acc = bcs_arr[idx], acc_arr[idx]
            bq25, bq75 = np.percentile(b_bcs, 25), np.percentile(b_bcs, 75)
            bl, bh = b_acc[b_bcs <= bq25], b_acc[b_bcs >= bq75]
            if len(bl) and len(bh):
                boot_gaps.append(float(np.mean(bl) - np.mean(bh)))
        boot_gaps = np.array(boot_gaps)
        gap_ci = [float(np.percentile(boot_gaps, 2.5)),
                   float(np.percentile(boot_gaps, 97.5))]

        # Strategy breakdown
        strat_accs = defaultdict(list)
        for d in batch_data:
            strat_accs[d["strategy"]].append(d["accuracy"])
        strat_stats = {
            k: {"mean": float(np.mean(v)), "std": float(np.std(v)), "n": len(v)}
            for k, v in strat_accs.items()
        }

        analysis[f"count_{count}"] = {
            "n_batches": n,
            "bcs_range": [float(bcs_arr.min()), float(bcs_arr.max())],
            "acc_range": [float(acc_arr.min()), float(acc_arr.max())],
            "spearman_r": float(spearman_r),
            "spearman_p": float(spearman_p),
            "regression": {
                "slope": float(slope),
                "intercept": float(intercept),
                "r_squared": float(r_val ** 2),
                "p_value": float(p_val),
                "slope_95ci": slope_ci,
            },
            "quartile_analysis": {
                "q25_threshold": float(q25),
                "q75_threshold": float(q75),
                "low_bcs_quartile_mean_acc": float(np.mean(low_q)) if len(low_q) else None,
                "high_bcs_quartile_mean_acc": float(np.mean(high_q)) if len(high_q) else None,
                "gap": gap,
                "gap_95ci": gap_ci,
                "n_low": int(len(low_q)),
                "n_high": int(len(high_q)),
            },
            "strategy_breakdown": strat_stats,
        }

    return analysis


# ── Stages ────────────────────────────────────────────────────────────────────

def stage_preprocess(args):
    logger.info("Loading DocRED dev set...")
    all_samples, rel_info = load_docred_dev()
    n_rels = len(rel_info)
    n_per_rel = max(1, args.n_samples // n_rels)
    samples = sample_balanced(all_samples, n_per_rel, seed=SEED)
    logger.info("%d samples (%d/rel) from %d types", len(samples), n_per_rel, n_rels)

    logger.info("Loading SCS matrix...")
    sim_matrix, type_names, type_to_idx = load_scs_matrix()

    logger.info("Building batch config...")
    batch_config = build_phase2_batch_config(sim_matrix, type_names, type_to_idx)

    total_inferences = 0
    for ck in sorted(batch_config.keys()):
        for sn, batches in sorted(batch_config[ck].items()):
            n_inf = 0
            for b in batches:
                n_inf += sum(1 for s in samples
                             if s["relation_type"] in set(b["types"]))
            total_inferences += n_inf
            bcs_vals = [b["bcs"] for b in batches]
            logger.info("  %s/%s: %d batches, BCS=[%.4f,%.4f], ~%d inferences",
                        ck, sn, len(batches), min(bcs_vals), max(bcs_vals), n_inf)
    logger.info("Total inferences: %d", total_inferences)

    config = {
        "samples": samples,
        "batch_config": batch_config,
        "model_path": args.model_path,
        "max_model_len": args.max_model_len,
        "gpu_memory_utilization": args.gpu_memory_utilization,
        "output_dir": str(OUTPUT_DIR),
        "n_relation_types": len(type_names),
        "scs_matrix_shape": list(sim_matrix.shape),
        "phase": "phase2",
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    config_path = OUTPUT_DIR / "phase2_preprocess_config.json"
    with open(config_path, "w") as f:
        json.dump(config, f, ensure_ascii=False)
    logger.info("Saved: %s (%.1f MB)", config_path,
                config_path.stat().st_size / 1e6)

    if args.dry_run:
        logger.info("DRY RUN COMPLETE")
        return None
    return str(config_path)


def stage_infer(args):
    config_path = args.preprocess_path or str(
        OUTPUT_DIR / "phase2_preprocess_config.json")
    with open(config_path) as f:
        config = json.load(f)

    predictions = run_phase2_inference(
        config["batch_config"], config["samples"], config["model_path"],
        config["max_model_len"], config["gpu_memory_utilization"],
    )

    pred_dir = OUTPUT_DIR / "all_predictions"
    pred_dir.mkdir(parents=True, exist_ok=True)
    with open(pred_dir / "phase2_predictions.json", "w") as f:
        json.dump(predictions, f, ensure_ascii=False, indent=2)
    logger.info("Saved %d predictions", len(predictions))

    eval_results = evaluate_predictions(predictions)
    with open(OUTPUT_DIR / "phase2_eval_results.json", "w") as f:
        json.dump(eval_results, f, indent=2)

    # Count curve summary
    curve = defaultdict(lambda: {"acc": [], "bcs": [], "n": []})
    for m in eval_results.values():
        if m["config_key"].startswith("curve_"):
            curve[m["config_key"]]["acc"].append(m["accuracy"])
            curve[m["config_key"]]["bcs"].append(m["bcs"])
            curve[m["config_key"]]["n"].append(m["total"])
    count_curve = {
        ck: {
            "batches": d["acc"],
            "mean_acc": float(np.mean(d["acc"])),
            "std_acc": float(np.std(d["acc"])),
            "bcs_values": d["bcs"],
            "mean_bcs": float(np.mean(d["bcs"])),
            "n_samples": d["n"],
        }
        for ck, d in sorted(curve.items())
    }
    with open(OUTPUT_DIR / "count_curve_results.json", "w") as f:
        json.dump(count_curve, f, indent=2)

    # BCS-controlled summary
    bcs_ctrl = defaultdict(lambda: {"acc": [], "bcs": [], "n": []})
    for m in eval_results.values():
        if m["config_key"].startswith("bcs_"):
            key = f"{m['config_key']}_{m['strategy']}"
            bcs_ctrl[key]["acc"].append(m["accuracy"])
            bcs_ctrl[key]["bcs"].append(m["bcs"])
            bcs_ctrl[key]["n"].append(m["total"])
    bcs_controlled = {
        k: {
            "batches": d["acc"],
            "mean_acc": float(np.mean(d["acc"])),
            "std_acc": float(np.std(d["acc"])),
            "bcs_values": d["bcs"],
            "mean_bcs": float(np.mean(d["bcs"])),
            "n_samples": d["n"],
        }
        for k, d in sorted(bcs_ctrl.items())
    }
    with open(OUTPUT_DIR / "bcs_controlled_results.json", "w") as f:
        json.dump(bcs_controlled, f, indent=2)

    logger.info("=" * 60)
    logger.info("COUNT CURVE")
    for ck, d in sorted(count_curve.items()):
        logger.info("  %s: acc=%.4f±%.4f  BCS=%.4f", ck,
                     d["mean_acc"], d["std_acc"], d["mean_bcs"])
    logger.info("BCS-CONTROLLED")
    for k, d in sorted(bcs_controlled.items()):
        logger.info("  %s: acc=%.4f±%.4f  BCS=%.4f", k,
                     d["mean_acc"], d["std_acc"], d["mean_bcs"])
    logger.info("=" * 60)


def stage_analyze(args):
    with open(OUTPUT_DIR / "phase2_eval_results.json") as f:
        eval_results = json.load(f)

    analysis = bootstrap_analysis(eval_results, n_bootstrap=10000, seed=SEED)

    with open(OUTPUT_DIR / "bootstrap_analysis.json", "w") as f:
        json.dump(analysis, f, indent=2)

    logger.info("=" * 60)
    logger.info("BOOTSTRAP ANALYSIS")
    for ck, a in sorted(analysis.items()):
        logger.info("  %s:", ck)
        logger.info("    Spearman r=%.4f (p=%.6f)", a["spearman_r"],
                     a["spearman_p"])
        reg = a["regression"]
        logger.info("    Slope=%.4f [%.4f, %.4f] R²=%.4f p=%.6f",
                     reg["slope"], reg["slope_95ci"][0], reg["slope_95ci"][1],
                     reg["r_squared"], reg["p_value"])
        qa = a["quartile_analysis"]
        logger.info("    Quartile gap=%.4f [%.4f, %.4f] (low_n=%d, high_n=%d)",
                     qa["gap"], qa["gap_95ci"][0], qa["gap_95ci"][1],
                     qa["n_low"], qa["n_high"])
        for strat, st in sorted(a["strategy_breakdown"].items()):
            logger.info("      %s: acc=%.4f±%.4f (n=%d)",
                         strat, st["mean"], st["std"], st["n"])
    logger.info("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="DocRED Phase 2")
    parser.add_argument("--stage",
                        choices=["preprocess", "infer", "analyze", "all"],
                        default="all")
    parser.add_argument("--model_path", default=MODEL_PATH)
    parser.add_argument("--n_samples", type=int, default=N_SAMPLES)
    parser.add_argument("--max_model_len", type=int, default=4096)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.90)
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--preprocess_path", default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")

    if args.stage == "preprocess":
        stage_preprocess(args)
    elif args.stage == "infer":
        stage_infer(args)
    elif args.stage == "analyze":
        stage_analyze(args)
    elif args.stage == "all":
        config_path = stage_preprocess(args)
        if config_path is None:
            return
        args.preprocess_path = config_path
        logger.info("=== Launching infer subprocess (vLLM-first) ===")
        cmd = [sys.executable, str(Path(__file__).resolve()),
               "--stage", "infer",
               "--preprocess_path", config_path]
        subprocess.run(cmd, check=True)
        stage_analyze(args)


if __name__ == "__main__":
    main()
