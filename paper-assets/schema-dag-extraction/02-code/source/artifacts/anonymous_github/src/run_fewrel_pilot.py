"""FewRel RE pilot experiment (D007).

Validates BCS-confusion hypothesis on relation extraction:
- 200 samples from val set (16 relations, balanced)
- Controlled batches at count={4,8,16}: low/high BCS + random
- Qwen3-32B-FP8 RE inference via vLLM
- Accuracy comparison: high-BCS vs low-BCS

Usage:
    python3 src/run_fewrel_pilot.py --help
    python3 src/run_fewrel_pilot.py --dry-run
    python3 src/run_fewrel_pilot.py --model_path ~/.cache/models/Qwen3-32B-FP8
"""
import argparse
import json
import logging
import random
import time
from collections import defaultdict
from pathlib import Path

logger = logging.getLogger(__name__)

BASE_DIR = Path(".")


def compute_relation_embeddings_st(pid2name: dict) -> dict:
    """Compute relation embeddings using sentence-transformers (CPU).

    Args:
        pid2name: {pid: relation_name} from fewrel_relation_types.json.

    Returns:
        {relation_name: tensor} embeddings.
    """
    from sentence_transformers import SentenceTransformer
    import torch

    local_path = "~/.cache/huggingface/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/c9745ed1d9f207416be6d2e6f8de32d1f16199bf"
    from pathlib import Path
    if Path(local_path).exists():
        model = SentenceTransformer(local_path, device="cpu")
    else:
        model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

    names = []
    texts = []
    for pid, name in pid2name.items():
        names.append(name)
        texts.append(f"Relation type: {name}")

    embeddings_np = model.encode(texts, show_progress_bar=False)
    return {name: torch.tensor(emb) for name, emb in zip(names, embeddings_np)}


def build_batch_config(sim_matrix, type_names, type_to_idx, counts,
                       num_random=3, seed=42):
    """Build controlled batch configuration with low/high BCS + random."""
    import sys
    sys.path.insert(0, str(BASE_DIR / "src"))
    from compute_bcs import compute_bcs
    from select_type_batches import (select_high_bcs, select_low_bcs,
                                     select_random_batches)

    batch_config = {}
    for count in counts:
        effective = min(count, len(type_names))
        low = select_low_bcs(effective, sim_matrix, type_names, type_to_idx)
        high = select_high_bcs(effective, sim_matrix, type_names, type_to_idx)
        rand = select_random_batches(effective, num_random, type_names,
                                     sim_matrix, type_to_idx, seed + count)
        batch_config[f"count_{effective}"] = {
            "low_bcs": {"types": low, "bcs": compute_bcs(low, sim_matrix, type_to_idx)},
            "high_bcs": {"types": high, "bcs": compute_bcs(high, sim_matrix, type_to_idx)},
            "random": rand,
        }
    return batch_config


def run_re_extraction(model_path, samples, batch_config, relation_defs,
                      max_model_len=4096):
    """Run RE extraction using vLLM with constrained JSON decoding."""
    import sys
    sys.path.insert(0, str(BASE_DIR / "src"))
    from run_extraction import build_json_schema_re, build_prompt_v2_re

    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    llm = LLM(model=model_path, max_model_len=max_model_len,
              trust_remote_code=True, dtype="bfloat16", gpu_memory_utilization=0.95, enforce_eager=True, disable_log_stats=True)

    all_results = []

    for count_key, batches in batch_config.items():
        for batch_label, batch_data in batches.items():
            if batch_label == "random":
                batch_list = batch_data
            else:
                batch_list = [batch_data]

            for bi, entry in enumerate(batch_list):
                batch_types = entry["types"]
                batch_bcs = entry["bcs"]
                bid = (f"{count_key}_{batch_label}_{bi}"
                       if batch_label == "random"
                       else f"{count_key}_{batch_label}")

                batch_samples = [s for s in samples
                                 if s["relation_type"] in batch_types]
                if not batch_samples:
                    logger.warning("No samples for batch %s", bid)
                    continue

                logger.info("Batch %s: BCS=%.4f, %d types, %d samples",
                            bid, batch_bcs, len(batch_types), len(batch_samples))

                schema = build_json_schema_re(batch_types)
                structured = StructuredOutputsParams(json=schema)
                params = SamplingParams(max_tokens=128, temperature=0.0,
                                        structured_outputs=structured)

                prompts = [
                    build_prompt_v2_re(s["text"], s["head_entity"],
                                      s["tail_entity"], relation_defs,
                                      batch_types)
                    for s in batch_samples
                ]

                t0 = time.time()
                outputs = llm.generate(prompts, params)
                elapsed = time.time() - t0

                for oi, output in enumerate(outputs):
                    gen_text = output.outputs[0].text
                    try:
                        pred = json.loads(gen_text)
                    except json.JSONDecodeError:
                        pred = {"relation": "PARSE_ERROR"}

                    all_results.append({
                        "batch_id": bid,
                        "count_key": count_key,
                        "batch_types": batch_types,
                        "batch_bcs": batch_bcs,
                        "ground_truth": batch_samples[oi]["relation_type"],
                        "prediction": pred.get("relation", "MISSING"),
                        "head_entity": batch_samples[oi]["head_entity"],
                        "tail_entity": batch_samples[oi]["tail_entity"],
                        "text": batch_samples[oi]["text"][:200],
                        "prompt_tokens": len(output.prompt_token_ids),
                        "gen_tokens": len(output.outputs[0].token_ids),
                        "latency_s": elapsed / len(prompts),
                    })

                logger.info("  Done: %.1fs total", elapsed)

    return all_results


def evaluate_re(results):
    """Compute per-batch accuracy."""
    stats = defaultdict(lambda: {"correct": 0, "total": 0, "bcs": 0.0,
                                 "count_key": "", "num_types": 0})
    for r in results:
        bid = r["batch_id"]
        stats[bid]["total"] += 1
        stats[bid]["bcs"] = r["batch_bcs"]
        stats[bid]["count_key"] = r["count_key"]
        stats[bid]["num_types"] = len(r["batch_types"])
        if r["prediction"] == r["ground_truth"]:
            stats[bid]["correct"] += 1

    return {
        bid: {
            "accuracy": s["correct"] / s["total"] if s["total"] else 0.0,
            "correct": s["correct"],
            "total": s["total"],
            "bcs": s["bcs"],
            "count_key": s["count_key"],
            "num_types": s["num_types"],
        }
        for bid, s in stats.items()
    }


def main():
    parser = argparse.ArgumentParser(
        description="FewRel RE Pilot Experiment (D007)")
    parser.add_argument("--model_path",
                        default="~/.cache/models/Qwen3-32B-FP8",
                        help="Path to Qwen3 model")
    parser.add_argument("--data_path",
                        default=str(BASE_DIR / "data/fewrel_parquet/val.parquet"),
                        help="FewRel val parquet path")
    parser.add_argument("--types_file",
                        default=str(BASE_DIR / "configs/fewrel_relation_types.json"),
                        help="Relation types JSON (pid -> name)")
    parser.add_argument("--output_dir",
                        default=str(BASE_DIR / "artifacts/fewrel_pilot"),
                        help="Output directory")
    parser.add_argument("--n_samples", type=int, default=200,
                        help="Total samples (balanced across relations)")
    parser.add_argument("--counts", default="4,8,16",
                        help="Comma-separated relation counts per batch")
    parser.add_argument("--num_random", type=int, default=3,
                        help="Random batches per count level")
    parser.add_argument("--max_model_len", type=int, default=4096,
                        help="vLLM max model len")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry-run", action="store_true",
                        help="Compute embeddings + build batches only, no GPU")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    random.seed(args.seed)

    import sys
    sys.path.insert(0, str(BASE_DIR / "src"))
    from fewrel_utils import (get_all_relation_types, load_fewrel,
                              sample_balanced)

    # --- Load data ---
    logger.info("Loading FewRel val data...")
    all_samples = load_fewrel(data_path=args.data_path)
    all_relations = get_all_relation_types(all_samples)
    logger.info("%d samples, %d relations", len(all_samples), len(all_relations))

    n_per_rel = args.n_samples // len(all_relations)
    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)
    logger.info("Sampled %d (%d per relation)", len(samples), n_per_rel)

    # --- Relation definitions ---
    with open(args.types_file) as f:
        pid2name = json.load(f)
    relation_defs = {name: name for name in pid2name.values()}

    # --- Compute relation embeddings (CPU) ---
    logger.info("Computing relation embeddings (sentence-transformers, CPU)...")
    embeddings = compute_relation_embeddings_st(pid2name)
    dim = next(iter(embeddings.values())).shape[0]
    logger.info("Embeddings: %d relations, dim=%d", len(embeddings), dim)

    # --- Similarity matrix ---
    from compute_bcs import compute_similarity_matrix
    sim_matrix, type_names, type_to_idx = compute_similarity_matrix(embeddings)

    # --- Batch config ---
    counts = [int(c.strip()) for c in args.counts.split(",")]
    batch_config = build_batch_config(sim_matrix, type_names, type_to_idx,
                                      counts, args.num_random, args.seed)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / "batch_config.json", "w") as f:
        json.dump(batch_config, f, indent=2)

    import torch
    torch.save({"sim_matrix": sim_matrix, "type_names": type_names,
                "type_to_idx": type_to_idx},
               output_dir / "relation_sim_matrix.pt")

    # --- Print summary ---
    logger.info("=" * 60)
    logger.info("BATCH CONFIGURATION")
    logger.info("=" * 60)
    total_batches = 0
    total_inferences = 0
    for ck, batches in sorted(batch_config.items()):
        logger.info("  %s:", ck)
        for label, data in batches.items():
            if label == "random":
                bcs_vals = [b["bcs"] for b in data]
                for b in data:
                    n = sum(1 for s in samples
                            if s["relation_type"] in b["types"])
                    total_inferences += n
                total_batches += len(data)
                logger.info("    random (%d): BCS [%.4f, %.4f]",
                            len(data), min(bcs_vals), max(bcs_vals))
            else:
                n = sum(1 for s in samples
                        if s["relation_type"] in data["types"])
                total_inferences += n
                total_batches += 1
                logger.info("    %s: BCS=%.4f, types=%s", label, data["bcs"],
                            data["types"][:4])

    if args.dry_run:
        logger.info("=" * 60)
        logger.info("DRY RUN COMPLETE")
        logger.info("  Samples: %d (%d/rel)", len(samples), n_per_rel)
        logger.info("  Relations: %d", len(all_relations))
        logger.info("  Batch counts: %s", counts)
        logger.info("  Total batches: %d", total_batches)
        logger.info("  Total inferences: %d", total_inferences)
        est_sec_per_sample = 1.5
        logger.info("  Est. GPU time: ~%.0f min (@%.1fs/sample, Qwen3-32B-FP8)",
                    total_inferences * est_sec_per_sample / 60,
                    est_sec_per_sample)
        logger.info("  Output: %s", output_dir)
        return

    # --- Run extraction ---
    results = run_re_extraction(args.model_path, samples, batch_config,
                                relation_defs, args.max_model_len)

    with open(output_dir / "predictions.json", "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info("Saved %d predictions", len(results))

    # --- Evaluate ---
    eval_results = evaluate_re(results)
    with open(output_dir / "eval_results.json", "w") as f:
        json.dump(eval_results, f, indent=2)

    logger.info("=" * 60)
    logger.info("RESULTS")
    logger.info("=" * 60)
    for bid, m in sorted(eval_results.items()):
        logger.info("  %-35s acc=%.4f (%3d/%3d) BCS=%.4f",
                    bid, m["accuracy"], m["correct"], m["total"], m["bcs"])


if __name__ == "__main__":
    main()
