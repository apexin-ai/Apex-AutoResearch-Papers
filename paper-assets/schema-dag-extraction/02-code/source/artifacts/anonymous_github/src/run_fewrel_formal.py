"""FewRel formal study: BCS-confusion hypothesis on relation extraction.

exp1 (Count curve): count={1,4,8,16,32,64,80}, 5 random batches per count,
    count_1 = 80 solo batches (one per relation type).
    1000 samples balanced across active relations.

exp2 (BCS controlled): count={8,16}, 1 low-BCS + 1 high-BCS + 25 random = 27 per count.
    Same 1000 samples.

Metric: accuracy (RE is single-label classification per sample).

Usage:
    # Auto two-stage (recommended — avoids vLLM fork deadlock):
    python3 src/run_fewrel_formal.py --mode exp1 --use_all

    # Manual two-stage:
    python3 src/run_fewrel_formal.py --stage preprocess --mode exp1 --use_all
    python3 src/run_fewrel_formal.py --stage extract --mode exp1

    # Dry run:
    python3 src/run_fewrel_formal.py --mode exp1 --use_all --dry_run
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

logger = logging.getLogger(__name__)

BASE_DIR = Path(".")

EXP1_COUNTS = [1, 4, 8, 16, 32, 64, 80]
EXP2_COUNTS = [8, 16]
EXP1_RANDOM_PER_COUNT = 5
EXP2_RANDOM_PER_COUNT = 25
DEFAULT_N_SAMPLES = 1000


def evaluate_re(results):
    """Per-batch accuracy and per-type accuracy breakdown."""
    batch_stats = defaultdict(lambda: {"correct": 0, "total": 0, "bcs": 0.0,
                                       "count_key": "", "num_types": 0,
                                       "batch_types": [], "per_type": defaultdict(lambda: {"correct": 0, "total": 0})})
    for r in results:
        bid = r["batch_id"]
        s = batch_stats[bid]
        s["total"] += 1
        s["bcs"] = r["batch_bcs"]
        s["count_key"] = r["count_key"]
        s["num_types"] = len(r["batch_types"])
        s["batch_types"] = r["batch_types"]
        gold = r["ground_truth"]
        pred = r["prediction"]
        s["per_type"][gold]["total"] += 1
        if pred == gold:
            s["correct"] += 1
            s["per_type"][gold]["correct"] += 1

    out = {}
    for bid, s in batch_stats.items():
        per_type_acc = {}
        for t, ts in s["per_type"].items():
            per_type_acc[t] = {
                "accuracy": ts["correct"] / ts["total"] if ts["total"] else 0.0,
                "correct": ts["correct"], "total": ts["total"],
            }
        out[bid] = {
            "accuracy": s["correct"] / s["total"] if s["total"] else 0.0,
            "correct": s["correct"], "total": s["total"], "bcs": s["bcs"],
            "count_key": s["count_key"], "num_types": s["num_types"],
            "batch_types": s["batch_types"], "per_type_accuracy": per_type_acc,
        }
    return out


def run_re_extraction(model_path, samples, batch_config, relation_defs, max_model_len=4096, gpu_memory_utilization=0.95):
    """Run RE extraction using vLLM with constrained JSON decoding."""
    sys.path.insert(0, str(BASE_DIR / "src"))
    from run_extraction import build_json_schema_re, build_prompt_v2_re
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    llm = LLM(model=model_path, max_model_len=max_model_len,
              trust_remote_code=True, dtype="bfloat16",
              gpu_memory_utilization=gpu_memory_utilization, enforce_eager=True, disable_log_stats=True)

    tokenizer = llm.get_tokenizer()
    _model_id = getattr(tokenizer, 'name_or_path', '') or model_path
    _needs_chat_template = any(kw in _model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])
    if _needs_chat_template:
        logger.info("Chat template enabled for model: %s", _model_id)

    all_results = []
    sample_id_map = {id(s): i for i, s in enumerate(samples)}

    for count_key, strategies in batch_config.items():
        batches_to_run = []
        if "low_bcs" in strategies:
            batches_to_run.append(("low_bcs", strategies["low_bcs"]["types"], strategies["low_bcs"]["bcs"]))
        if "high_bcs" in strategies:
            batches_to_run.append(("high_bcs", strategies["high_bcs"]["types"], strategies["high_bcs"]["bcs"]))
        if "random" in strategies:
            for ri, rb in enumerate(strategies["random"]):
                batches_to_run.append((f"random_{ri}", rb["types"], rb["bcs"]))

        for batch_id, batch_types, batch_bcs in batches_to_run:
            full_bid = f"{count_key}_{batch_id}"
            type_set = set(batch_types)
            batch_samples = [s for s in samples if s["relation_type"] in type_set]
            if not batch_samples:
                logger.warning("No samples for batch %s", full_bid)
                continue

            logger.info("Batch %s: %d types, BCS=%.4f, %d samples",
                        full_bid, len(batch_types), batch_bcs, len(batch_samples))
            schema = build_json_schema_re(batch_types)
            structured = StructuredOutputsParams(json=schema)
            sampling_params = SamplingParams(max_tokens=64, temperature=0.0, structured_outputs=structured)

            prompts = []
            sample_refs = []
            for s in batch_samples:
                p = build_prompt_v2_re(s["text"], s["head_entity"], s["tail_entity"], relation_defs, batch_types)
                prompts.append(p)
                sample_refs.append(s)

            if _needs_chat_template:
                prompts = [
                    tokenizer.apply_chat_template(
                        [{"role": "user", "content": p}],
                        tokenize=False,
                        add_generation_prompt=True,
                    )
                    for p in prompts
                ]

            t0 = time.time()
            outputs = llm.generate(prompts, sampling_params)
            elapsed = time.time() - t0

            for oi, output in enumerate(outputs):
                s = sample_refs[oi]
                gen_text = output.outputs[0].text
                try:
                    parsed = json.loads(gen_text)
                    pred_rel = parsed.get("relation", "none")
                except json.JSONDecodeError:
                    pred_rel = "none"

                all_results.append({
                    "sample_id": sample_id_map[id(s)], "batch_id": full_bid,
                    "count_key": count_key, "batch_types": batch_types, "batch_bcs": batch_bcs,
                    "prediction": pred_rel, "ground_truth": s["relation_type"],
                    "head_entity": s["head_entity"], "tail_entity": s["tail_entity"],
                    "prompt_tokens": len(output.prompt_token_ids),
                    "gen_tokens": len(output.outputs[0].token_ids),
                    "latency_s": elapsed / len(prompts),
                })
            logger.info("  Done: %.1fs (%.2fs/sample)", elapsed, elapsed / len(batch_samples))

    return all_results


def stage_preprocess(args):
    """CPU stage: load data, compute BCS, build batch config, save JSON."""
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import load_fewrel, get_all_relation_types, sample_balanced
    from compute_bcs import load_embeddings, compute_similarity_matrix, compute_bcs
    from select_type_batches import select_low_bcs, select_high_bcs, select_random_batches

    logger.info("Loading FewRel data...")
    data_paths = [args.data_path]
    if args.use_all:
        data_paths = [str(BASE_DIR / "data/fewrel_parquet/train.parquet"),
                      str(BASE_DIR / "data/fewrel_parquet/val.parquet")]
    elif args.data_path_extra:
        data_paths.extend(args.data_path_extra)

    all_samples = []
    for dp in data_paths:
        all_samples.extend(load_fewrel(data_path=dp))
    all_relations = get_all_relation_types(all_samples)
    logger.info("%d samples, %d relation types from %d file(s)",
                len(all_samples), len(all_relations), len(data_paths))

    n_per_rel = args.n_samples // len(all_relations)
    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)
    logger.info("Sampled %d (%d per relation, %d relations)",
                len(samples), n_per_rel, len(all_relations))

    with open(args.types_file) as f:
        pid2name = json.load(f)
    relation_defs = {name: name for name in pid2name.values()}

    if args.embeddings_path:
        logger.info("Loading pre-computed embeddings from %s", args.embeddings_path)
        embeddings = load_embeddings(args.embeddings_path)
        sample_keys = list(embeddings.keys())[:3]
        if sample_keys and all(k in pid2name for k in sample_keys):
            embeddings = {pid2name[k]: v for k, v in embeddings.items() if k in pid2name}
            logger.info("Remapped %d PID-keyed embeddings to relation names", len(embeddings))
    else:
        logger.info("No --embeddings_path; computing MiniLM embeddings (CPU fallback)")
        from run_fewrel_pilot import compute_relation_embeddings_st
        embeddings = compute_relation_embeddings_st(pid2name)

    import torch
    sim_matrix, type_names, type_to_idx = compute_similarity_matrix(embeddings)
    logger.info("Similarity matrix: %d types", len(type_names))

    active_types = [t for t in type_names if t in set(all_relations)]
    active_idx = {t: type_to_idx[t] for t in active_types}
    n_active = len(active_types)
    logger.info("Active types (in both embeddings and data): %d", n_active)

    mode = args.mode if args.mode != "dry_run" else "exp1"
    batch_config = {}
    seen_counts = set()

    if mode == "exp1":
        for count in EXP1_COUNTS:
            count = min(count, n_active)
            if count in seen_counts:
                continue
            seen_counts.add(count)
            if count == 1:
                solo_batches = [{"types": [t], "bcs": 0.0} for t in active_types]
                batch_config["count_1"] = {"random": solo_batches}
            else:
                rand = select_random_batches(count, EXP1_RANDOM_PER_COUNT, active_types,
                                             sim_matrix, active_idx, args.seed + count)
                batch_config[f"count_{count}"] = {"random": rand}

    elif mode == "exp2":
        for count in EXP2_COUNTS:
            count = min(count, n_active)
            if count in seen_counts:
                continue
            seen_counts.add(count)
            low = select_low_bcs(count, sim_matrix, active_types, active_idx)
            high = select_high_bcs(count, sim_matrix, active_types, active_idx)
            rand = select_random_batches(count, EXP2_RANDOM_PER_COUNT, active_types,
                                         sim_matrix, active_idx, args.seed + count)
            batch_config[f"count_{count}"] = {
                "low_bcs": {"types": low, "bcs": compute_bcs(low, sim_matrix, type_to_idx)},
                "high_bcs": {"types": high, "bcs": compute_bcs(high, sim_matrix, type_to_idx)},
                "random": rand,
            }

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / f"batch_config_{args.mode}.json", "w") as f:
        json.dump(batch_config, f, indent=2)

    torch.save({"sim_matrix": sim_matrix, "type_names": type_names, "type_to_idx": type_to_idx},
               output_dir / "relation_sim_matrix.pt")

    preprocess_output = {
        "batch_config": batch_config,
        "samples": samples,
        "relation_defs": relation_defs,
        "model_path": args.model_path,
        "max_model_len": args.max_model_len,
        "mode": mode,
        "output_dir": args.output_dir,
        "gpu_memory_utilization": args.gpu_memory_utilization,
    }
    preprocess_path = output_dir / f"preprocess_{mode}.json"
    with open(preprocess_path, "w") as f:
        json.dump(preprocess_output, f, ensure_ascii=False)
    logger.info("Saved preprocess config to %s", preprocess_path)

    total_batches = 0
    total_inferences = 0
    sample_type_counts = defaultdict(int)
    for s in samples:
        sample_type_counts[s["relation_type"]] += 1

    logger.info("=" * 60)
    logger.info("BATCH CONFIGURATION (%s)", args.mode)
    logger.info("=" * 60)
    for ck, strategies in sorted(batch_config.items()):
        logger.info("  %s:", ck)
        for label, data in strategies.items():
            if label == "random":
                bcs_vals = [b["bcs"] for b in data]
                n_inf = sum(sum(sample_type_counts.get(t, 0) for t in b["types"]) for b in data)
                total_batches += len(data)
                total_inferences += n_inf
                logger.info("    random (%d): BCS [%.4f, %.4f], ~%d inferences",
                            len(data), min(bcs_vals), max(bcs_vals), n_inf)
            else:
                n_inf = sum(sample_type_counts.get(t, 0) for t in data["types"])
                total_batches += 1
                total_inferences += n_inf
                logger.info("    %s: BCS=%.4f, %d types, ~%d inferences",
                            label, data["bcs"], len(data["types"]), n_inf)

    logger.info("-" * 60)
    logger.info("Samples: %d (%d/rel)", len(samples), n_per_rel)
    logger.info("Relations: %d active", n_active)
    logger.info("Total batches: %d", total_batches)
    logger.info("Total inferences: %d", total_inferences)
    est_sec = 1.5
    logger.info("Est. GPU time: ~%.0f min (@%.1fs/sample)", total_inferences * est_sec / 60, est_sec)

    return str(preprocess_path)


def stage_extract(args):
    """GPU stage: vLLM imported first inside run_re_extraction, read preprocess config."""
    preprocess_path = args.preprocess_path or str(
        Path(args.output_dir) / f"preprocess_{args.mode}.json"
    )
    with open(preprocess_path) as f:
        config = json.load(f)

    results = run_re_extraction(
        config["model_path"], config["samples"], config["batch_config"],
        config["relation_defs"], config["max_model_len"],
        config.get("gpu_memory_utilization", 0.95),
    )

    output_dir = Path(config["output_dir"])
    mode = config["mode"]

    pred_path = output_dir / f"predictions_{mode}.json"
    with open(pred_path, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info("Saved %d predictions to %s", len(results), pred_path)

    eval_results = evaluate_re(results)
    eval_path = output_dir / f"eval_{mode}.json"
    with open(eval_path, "w") as f:
        json.dump(eval_results, f, indent=2)

    logger.info("=" * 60)
    logger.info("RESULTS (%s)", mode)
    logger.info("=" * 60)
    for bid, m in sorted(eval_results.items()):
        logger.info("  %-40s acc=%.4f (%3d/%3d) BCS=%.4f",
                    bid, m["accuracy"], m["correct"], m["total"], m["bcs"])


def main():
    parser = argparse.ArgumentParser(description="FewRel Formal Study")
    parser.add_argument("--model_path", default="~/.cache/huggingface/qwen3-32b-fp8/")
    parser.add_argument("--data_path", default=str(BASE_DIR / "data/fewrel_parquet/val.parquet"),
                        help="Primary data parquet (val split)")
    parser.add_argument("--data_path_extra", nargs="*", default=None,
                        help="Additional parquet files (e.g. train split for full 80 relations)")
    parser.add_argument("--use_all", action="store_true",
                        help="Load both train+val splits (all 80 relations)")
    parser.add_argument("--types_file", default=str(BASE_DIR / "configs/fewrel_relation_types.json"))
    parser.add_argument("--embeddings_path", default=None, help="Pre-computed embeddings .pt (Qwen3 or MiniLM)")
    parser.add_argument("--output_dir", default=str(BASE_DIR / "artifacts/fewrel_formal"))
    parser.add_argument("--mode", choices=["exp1", "exp2", "dry_run"], required=True)
    parser.add_argument("--n_samples", type=int, default=DEFAULT_N_SAMPLES)
    parser.add_argument("--max_model_len", type=int, default=4096)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.95)
    parser.add_argument("--dry_run", action="store_true", help="Build batches + print summary, no GPU")
    parser.add_argument("--stage", choices=["preprocess", "extract", "all"], default="all",
                        help="preprocess=CPU only, extract=GPU only, all=subprocess both")
    parser.add_argument("--preprocess_path", default=None,
                        help="Path to preprocess JSON (for --stage extract)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    random.seed(args.seed)

    if args.stage == "preprocess":
        stage_preprocess(args)
    elif args.stage == "extract":
        stage_extract(args)
    elif args.stage == "all":
        preprocess_path = stage_preprocess(args)

        if args.dry_run or args.mode == "dry_run":
            logger.info("DRY RUN - stopping before GPU extraction.")
            return

        logger.info("=== Launching extract subprocess (vLLM-first) ===")
        cmd = [sys.executable, str(Path(__file__).resolve()),
               "--stage", "extract",
               "--mode", args.mode,
               "--output_dir", args.output_dir,
               "--preprocess_path", preprocess_path]
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
