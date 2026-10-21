"""Main experiment orchestrator.

v2 changes (2026-05-14): Added --prompt_version and --eval_mode support.

Modes:
  dry_run: 100 test samples, count=6, low/high/1 random — pipeline verification
  exp1: Count Baseline — solo baseline (count=1) + random batches at 2/6/12/22/44/66 types, 5 random each
  exp2: Confusability Controlled — count=6,12, low/high BCS + 25 random each
Dependencies: all src/ modules, vllm
"""
import argparse
import json
import logging
import random
import sys
import time
from pathlib import Path

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Schema-DAG Extraction MVP Experiment")
    parser.add_argument("--model_path", required=True, help="Path to model directory")
    parser.add_argument("--model_name", default=None,
                        help="Short model name for output files (default: derived from model_path)")
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.95,
                        help="vLLM GPU memory utilization (default: 0.95)")
    parser.add_argument("--data_dir", default="./data", help="Data directory")
    parser.add_argument("--output_dir", default="./artifacts", help="Output directory")
    parser.add_argument("--dataset", choices=["fewnerd", "maven", "fewrel"], default="fewnerd",
                        help="Dataset: fewnerd (NER), maven (event detection), or fewrel (RE)")
    parser.add_argument("--data_path", default=None, help="Custom data path (parquet for maven)")
    parser.add_argument("--types_file", required=True, help="Type definitions JSON path")
    parser.add_argument("--embeddings_path", default=None, help="Pre-computed embeddings .pt (required)")
    parser.add_argument("--sim_matrix_path", default=None, help="Pre-computed sim matrix .pt (optional)")
    parser.add_argument("--mode", choices=["dry_run", "exp1", "exp2"], required=True, help="Experiment mode")
    parser.add_argument("--max_samples", type=int, default=None, help="Max test samples (dry_run forces 100)")
    parser.add_argument("--max_model_len", type=int, default=4096, help="vLLM max model len")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--prompt_version", choices=["v1", "v2"], default="v1",
                        help="Prompt version: v1 (with offsets) or v2 (text+type only)")
    parser.add_argument("--eval_mode", choices=["exact", "relaxed", "text_match", "all"],
                        default="all", help="Evaluation mode")
    args = parser.parse_args()

    if args.model_name is None:
        args.model_name = Path(args.model_path).name.lower().replace(' ', '-')

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    random.seed(args.seed)

    sys.path.insert(0, str(Path(__file__).parent))

    import os as _os
    _orig_cuda = _os.environ.get('CUDA_VISIBLE_DEVICES')
    _os.environ['CUDA_VISIBLE_DEVICES'] = ''

    from few_nerd_utils import load_type_definitions, get_all_types as fewnerd_get_all_types
    from compute_bcs import load_embeddings, compute_similarity_matrix, compute_bcs
    from select_type_batches import select_low_bcs, select_high_bcs, select_random_batches
    from run_extraction import run_extraction
    from evaluate import evaluate_all

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Step 1: Load data ---
    if args.mode == "dry_run":
        max_samples = 100
        logger.info("Dry run mode: using 100 samples")
    else:
        max_samples = args.max_samples

    if args.dataset == "maven":
        from maven_utils import load_maven, get_all_types as maven_get_all_types
        data_path = args.data_path or "./data/maven_parquet/valid.parquet"
        logger.info("Loading MAVEN data from %s...", data_path)
        samples = load_maven(data_path=data_path, max_samples=max_samples)
        all_types = maven_get_all_types(samples)
        task = "event_detection"
    elif args.dataset == "fewrel":
        from fewrel_utils import load_fewrel, get_all_relation_types
        data_path = args.data_path or "./data/fewrel_parquet/val.parquet"
        logger.info("Loading FewRel data from %s...", data_path)
        samples = load_fewrel(data_path=data_path, max_samples=max_samples)
        all_types = get_all_relation_types(samples)
        task = "re"
    else:
        from few_nerd_utils import load_few_nerd
        logger.info("Loading Few-NERD test data...")
        samples = load_few_nerd(split="test", max_samples=max_samples)
        all_types = fewnerd_get_all_types(samples)
        task = "ner"

    type_definitions = load_type_definitions(args.types_file)
    logger.info("Data loaded: %d samples, %d active types", len(samples), len(all_types))

    # --- Step 2: Load embeddings and similarity matrix ---
    embeddings_path = args.embeddings_path
    if embeddings_path is None:
        embeddings_path = str(output_dir / "type_embeddings.pt")

    if not Path(embeddings_path).exists():
        logger.error("Embeddings file not found: %s", embeddings_path)
        logger.error("Run compute_type_embeddings.py first to avoid loading two models simultaneously.")
        sys.exit(1)

    logger.info("Loading embeddings from %s", embeddings_path)
    embeddings = load_embeddings(embeddings_path)

    import torch
    sim_matrix_file = Path(args.sim_matrix_path) if args.sim_matrix_path else output_dir / "sim_matrix.pt"
    if sim_matrix_file.exists():
        logger.info("Loading similarity matrix from %s", sim_matrix_file)
        sim_data = torch.load(str(sim_matrix_file), map_location="cpu", weights_only=True)
        sim_matrix = sim_data.get("sim_matrix", sim_data.get("similarity_matrix"))
        type_names = sim_data["type_names"]
        type_to_idx = sim_data.get("type_to_idx", {n: i for i, n in enumerate(type_names)})
    else:
        logger.info("Computing similarity matrix...")
        sim_matrix, type_names, type_to_idx = compute_similarity_matrix(embeddings)
        torch.save({"sim_matrix": sim_matrix, "type_names": type_names, "type_to_idx": type_to_idx},
                    str(output_dir / "sim_matrix.pt"))

    # Only use types that appear in both embeddings and data
    active_types = [t for t in type_names if t in set(all_types)]
    active_idx = {t: type_to_idx[t] for t in active_types}
    logger.info("Active types (in both embeddings and data): %d", len(active_types))

    # --- Step 3: Build batch configs based on mode ---
    # Dataset-specific count levels
    if args.dataset == "maven":
        exp1_counts = [1, 6, 12, 24, 42, 84, min(168, len(active_types))]
        exp2_counts = [12, 24]
    else:
        exp1_counts = [1, 2, 6, 12, 22, 44, min(66, len(active_types))]
        exp2_counts = [6, 12]

    batch_config = {}

    if args.mode == "dry_run":
        low = select_low_bcs(6, sim_matrix, active_types, active_idx)
        high = select_high_bcs(6, sim_matrix, active_types, active_idx)
        rand = select_random_batches(6, 1, active_types, sim_matrix, active_idx, args.seed)
        batch_config["count_6"] = {
            "low_bcs": {"types": low, "bcs": compute_bcs(low, sim_matrix, type_to_idx)},
            "high_bcs": {"types": high, "bcs": compute_bcs(high, sim_matrix, type_to_idx)},
            "random": rand,
        }

    elif args.mode == "exp1":
        for count in exp1_counts:
            if count > len(active_types):
                count = len(active_types)
            if count == 1:
                # Solo baseline: one batch per active type for per-type solo F1
                solo_batches = [{"types": [t], "bcs": 0.0} for t in active_types]
                batch_config["count_1"] = {"random": solo_batches}
            else:
                rand = select_random_batches(count, 5, active_types, sim_matrix, active_idx, args.seed + count)
                batch_config[f"count_{count}"] = {"random": rand}

    elif args.mode == "exp2":
        for count in exp2_counts:
            low = select_low_bcs(count, sim_matrix, active_types, active_idx)
            high = select_high_bcs(count, sim_matrix, active_types, active_idx)
            rand = select_random_batches(count, 25, active_types, sim_matrix, active_idx, args.seed + count)
            batch_config[f"count_{count}"] = {
                "low_bcs": {"types": low, "bcs": compute_bcs(low, sim_matrix, type_to_idx)},
                "high_bcs": {"types": high, "bcs": compute_bcs(high, sim_matrix, type_to_idx)},
                "random": rand,
            }

    # Save batch config
    batch_config_path = output_dir / f"batch_config_{args.dataset}_{args.mode}_{args.model_name}.json"
    with open(batch_config_path, "w") as f:
        json.dump(batch_config, f, indent=2)
    logger.info("Saved batch config to %s", batch_config_path)

    # --- Step 4: Run extraction ---
    if _orig_cuda is not None:
        _os.environ["CUDA_VISIBLE_DEVICES"] = _orig_cuda
    elif "CUDA_VISIBLE_DEVICES" in _os.environ:
        del _os.environ["CUDA_VISIBLE_DEVICES"]

    logger.info("Starting extraction...")
    t0 = time.time()
    results = run_extraction(
        model_path=args.model_path,
        samples=samples,
        batch_config=batch_config,
        type_definitions=type_definitions,
        max_model_len=args.max_model_len,
        prompt_version=args.prompt_version,
        task=task,
        gpu_memory_utilization=args.gpu_memory_utilization,
    )
    extraction_time = time.time() - t0
    logger.info("Extraction done in %.1fs, %d result entries", extraction_time, len(results))

    predictions_path = output_dir / f"predictions_{args.dataset}_{args.mode}_{args.model_name}.json"
    with open(predictions_path, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # --- Step 5: Evaluate ---
    logger.info("Evaluating...")
    eval_results = evaluate_all(results, samples, eval_mode=args.eval_mode)

    eval_path = output_dir / f"eval_{args.dataset}_{args.mode}_{args.model_name}.json"
    with open(eval_path, "w") as f:
        json.dump(eval_results, f, indent=2)

    # --- Step 6: Summary ---
    logger.info("=" * 60)
    logger.info("EXPERIMENT SUMMARY (%s)", args.mode)
    logger.info("=" * 60)
    for bid, metrics in sorted(eval_results.items()):
        parts = [f"  {bid:<30s}"]
        if "exact" in metrics:
            parts.append(f"exact_F1={metrics['exact']['f1']:.4f}")
        if "relaxed" in metrics:
            parts.append(f"relaxed_F1={metrics['relaxed']['f1']:.4f}")
        if "text_match" in metrics:
            parts.append(f"text_match_F1={metrics['text_match']['f1']:.4f}")
        parts.append(f"BCS={metrics['bcs']:.4f}")
        logger.info("  ".join(parts))
    logger.info("Total extraction time: %.1fs", extraction_time)
    logger.info("Results saved to: %s", output_dir)


if __name__ == "__main__":
    main()
