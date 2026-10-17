"""SDGD experiment runner: compare SDGD decomposition vs baselines.

Modes:
  sdgd_zero:    SDGD graph-coloring decomposition (adaptive threshold, embedding similarity)
  sdgd_cal:     SDGD with empirical confusion-based decomposition (calibration run)
  single_pass:  All types in one batch (baseline)
  per_type:     One batch per type (upper bound on decomposition)
  random_batch: Random grouping into N batches (ablation)
"""
import argparse
import json
import logging
import random
import sys
import time
from pathlib import Path

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from few_nerd_utils import load_few_nerd, load_type_definitions
from sdgd.decompose import sdgd_decompose, sdgd_extract, sdgd_cal_extract
from sdgd.similarity import cosine_similarity_matrix, adaptive_threshold, load_type_embeddings, load_sim_matrix
from sdgd.graph import build_threshold_graph, color_graph, group_by_color, get_graph_stats
from sdgd.merge import merge_all_samples
from sdgd.evaluate import compute_f1, compare_with_baseline


def run_single_pass(model_path, samples, type_definitions, all_types, prompt_version, max_model_len, task):
    """Baseline: all types in one batch."""
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    if task == "re":
        from run_extraction import build_json_schema_re, build_prompt_v2_re
        schema_fn = build_json_schema_re
        prompt_fn = None
    elif task == "event":
        from run_extraction import build_json_schema_v2
        schema_fn = build_json_schema_v2
        if prompt_version == "v2":
            from run_extraction import build_prompt_v2_event
            prompt_fn = build_prompt_v2_event
        else:
            from run_extraction import build_prompt_v1_event
            prompt_fn = build_prompt_v1_event
    else:
        if prompt_version == "v2":
            from run_extraction import build_json_schema_v2, build_prompt_v2
            schema_fn = build_json_schema_v2
            prompt_fn = build_prompt_v2
        else:
            from run_extraction import build_json_schema_v1, build_prompt_v1
            schema_fn = build_json_schema_v1
            prompt_fn = build_prompt_v1

    llm = LLM(
        model=model_path, dtype="bfloat16", gpu_memory_utilization=0.95,
        enforce_eager=True, max_model_len=max_model_len,
        trust_remote_code=True, disable_log_stats=True,
    )

    batch_schema = schema_fn(all_types)
    structured_params = StructuredOutputsParams(json=batch_schema)
    sampling_params = SamplingParams(max_tokens=1024, temperature=0.0, structured_outputs=structured_params)

    if task == "re":
        prompts = [build_prompt_v2_re(s["text"], s["head_entity"], s["tail_entity"],
                                      type_definitions, all_types) for s in samples]
    else:
        prompts = [prompt_fn(s["text"], type_definitions, all_types) for s in samples]
    t0 = time.time()
    outputs = llm.generate(prompts, sampling_params)
    elapsed = time.time() - t0

    predictions = []
    for output in outputs:
        try:
            preds = json.loads(output.outputs[0].text)
        except json.JSONDecodeError:
            preds = []
        predictions.append(preds)

    return predictions, {"mode": "single_pass", "n_types": len(all_types), "latency_s": elapsed}


def run_per_type(model_path, samples, type_definitions, all_types, prompt_version, max_model_len, task):
    """Each type extracted individually, then merged."""
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    if task == "re":
        from run_extraction import build_json_schema_re, build_prompt_v2_re
        schema_fn = build_json_schema_re
        prompt_fn = None
    elif task == "event":
        from run_extraction import build_json_schema_v2
        schema_fn = build_json_schema_v2
        if prompt_version == "v2":
            from run_extraction import build_prompt_v2_event
            prompt_fn = build_prompt_v2_event
        else:
            from run_extraction import build_prompt_v1_event
            prompt_fn = build_prompt_v1_event
    else:
        if prompt_version == "v2":
            from run_extraction import build_json_schema_v2, build_prompt_v2
            schema_fn = build_json_schema_v2
            prompt_fn = build_prompt_v2
        else:
            from run_extraction import build_json_schema_v1, build_prompt_v1
            schema_fn = build_json_schema_v1
            prompt_fn = build_prompt_v1

    llm = LLM(
        model=model_path, dtype="bfloat16", gpu_memory_utilization=0.95,
        enforce_eager=True, max_model_len=max_model_len,
        trust_remote_code=True, disable_log_stats=True,
    )

    all_results = []
    t0 = time.time()
    for ti, type_name in enumerate(sorted(all_types)):
        batch_types = [type_name]
        batch_schema = schema_fn(batch_types)
        structured_params = StructuredOutputsParams(json=batch_schema)
        sampling_params = SamplingParams(max_tokens=1024, temperature=0.0, structured_outputs=structured_params)

        if task == "re":
            prompts = [build_prompt_v2_re(s["text"], s["head_entity"], s["tail_entity"],
                                          type_definitions, batch_types) for s in samples]
        else:
            prompts = [prompt_fn(s["text"], type_definitions, batch_types) for s in samples]
        outputs = llm.generate(prompts, sampling_params)

        for si, output in enumerate(outputs):
            try:
                preds = json.loads(output.outputs[0].text)
            except json.JSONDecodeError:
                preds = []
            all_results.append({"sample_id": si, "batch_id": f"type_{ti}", "predictions": preds})

        logger.info("  Type %d/%d: %s", ti + 1, len(all_types), type_name)

    elapsed = time.time() - t0
    merged = merge_all_samples(all_results, len(samples))
    return merged, {"mode": "per_type", "n_types": len(all_types), "n_batches": len(all_types), "latency_s": elapsed}


def run_random_batch(model_path, samples, type_definitions, all_types, n_batches, prompt_version, max_model_len, task, seed=42):
    """Random grouping into n_batches batches."""
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    if task == "re":
        from run_extraction import build_json_schema_re, build_prompt_v2_re
        schema_fn = build_json_schema_re
        prompt_fn = None
    elif task == "event":
        from run_extraction import build_json_schema_v2
        schema_fn = build_json_schema_v2
        if prompt_version == "v2":
            from run_extraction import build_prompt_v2_event
            prompt_fn = build_prompt_v2_event
        else:
            from run_extraction import build_prompt_v1_event
            prompt_fn = build_prompt_v1_event
    else:
        if prompt_version == "v2":
            from run_extraction import build_json_schema_v2, build_prompt_v2
            schema_fn = build_json_schema_v2
            prompt_fn = build_prompt_v2
        else:
            from run_extraction import build_json_schema_v1, build_prompt_v1
            schema_fn = build_json_schema_v1
            prompt_fn = build_prompt_v1

    rng = random.Random(seed)
    shuffled = sorted(all_types)
    rng.shuffle(shuffled)
    batches = {}
    for i, t in enumerate(shuffled):
        batches.setdefault(i % n_batches, []).append(t)

    llm = LLM(
        model=model_path, dtype="bfloat16", gpu_memory_utilization=0.95,
        enforce_eager=True, max_model_len=max_model_len,
        trust_remote_code=True, disable_log_stats=True,
    )

    all_results = []
    t0 = time.time()
    for batch_id, batch_types in sorted(batches.items()):
        batch_schema = schema_fn(batch_types)
        structured_params = StructuredOutputsParams(json=batch_schema)
        sampling_params = SamplingParams(max_tokens=1024, temperature=0.0, structured_outputs=structured_params)

        if task == "re":
            prompts = [build_prompt_v2_re(s["text"], s["head_entity"], s["tail_entity"],
                                          type_definitions, batch_types) for s in samples]
        else:
            prompts = [prompt_fn(s["text"], type_definitions, batch_types) for s in samples]
        outputs = llm.generate(prompts, sampling_params)

        for si, output in enumerate(outputs):
            try:
                preds = json.loads(output.outputs[0].text)
            except json.JSONDecodeError:
                preds = []
            all_results.append({"sample_id": si, "batch_id": f"random_{batch_id}", "predictions": preds})

        logger.info("  Random batch %d/%d: %d types", batch_id + 1, n_batches, len(batch_types))

    elapsed = time.time() - t0
    merged = merge_all_samples(all_results, len(samples))
    batch_sizes = sorted([len(b) for b in batches.values()], reverse=True)
    return merged, {"mode": "random_batch", "n_batches": n_batches, "batch_sizes": batch_sizes, "latency_s": elapsed, "seed": seed}


def main():
    parser = argparse.ArgumentParser(description="SDGD Experiment Runner")
    parser.add_argument("--mode", required=True, choices=["sdgd_zero", "sdgd_cal", "single_pass", "per_type", "random_batch"],
                        help="Experiment mode")
    parser.add_argument("--dataset", default="fewnerd", choices=["fewnerd", "maven", "fewrel"])
    parser.add_argument("--data_path", default=None, help="Custom data path")
    parser.add_argument("--types_file", required=True, help="Type definitions JSON")
    parser.add_argument("--embeddings_path", default=None, help="Type embeddings .pt")
    parser.add_argument("--sim_matrix_path", default=None, help="Precomputed sim matrix .pt")
    parser.add_argument("--model_path", default=None, help="vLLM model path (not needed for decompose-only)")
    parser.add_argument("--k", type=float, default=1.0, help="Adaptive threshold k")
    parser.add_argument("--tau", type=float, default=None, help="Fixed threshold (overrides adaptive)")
    parser.add_argument("--max_samples", type=int, default=None, help="Max test samples")
    parser.add_argument("--max_model_len", type=int, default=4096)
    parser.add_argument("--prompt_version", default="v2", choices=["v1", "v2"])
    parser.add_argument("--task", default="ner", choices=["ner", "event", "re"])
    parser.add_argument("--output_dir", required=True, help="Output directory")
    parser.add_argument("--n_random_batches", type=int, default=None,
                        help="Number of batches for random_batch mode (default: match SDGD)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--cal_samples", type=int, default=100,
                        help="Number of calibration samples for sdgd_cal mode")
    parser.add_argument("--confusion_matrix_path", default=None,
                        help="Precomputed confusion matrix .npz for sdgd_cal (skip calibration)")
    parser.add_argument("--decompose_only", action="store_true",
                        help="Only run decomposition (no GPU inference)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    type_definitions = load_type_definitions(args.types_file)
    all_types = sorted(type_definitions.keys())
    logger.info("Loaded %d types from %s", len(all_types), args.types_file)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.mode == "sdgd_zero":
        if not args.embeddings_path and not args.sim_matrix_path:
            parser.error("sdgd_zero requires --embeddings_path or --sim_matrix_path")

        decomp = sdgd_decompose(
            types=type_definitions,
            embeddings_path=args.embeddings_path,
            sim_matrix_path=args.sim_matrix_path,
            k=args.k,
            tau=args.tau,
        )

        decomp_info = {
            "tau": decomp["tau"],
            "k": decomp["k"],
            "graph_stats": decomp["graph_stats"],
            "batches": {str(k): v for k, v in decomp["batches"].items()},
        }
        with open(output_dir / "decomposition.json", "w") as f:
            json.dump(decomp_info, f, indent=2)

        logger.info("Decomposition: tau=%.4f, n_batches=%d, sizes=%s",
                     decomp["tau"], decomp["graph_stats"]["n_colors"],
                     decomp["graph_stats"]["batch_sizes"])

        if args.decompose_only:
            print(json.dumps(decomp_info, indent=2))
            return

        if not args.model_path:
            parser.error("sdgd_zero requires --model_path for extraction")

        if args.dataset == "fewnerd":
            data_dir = str(Path(args.data_path).parent) if args.data_path else "./data/parquet"
            samples = load_few_nerd(split="test", max_samples=args.max_samples, data_dir=data_dir)
        elif args.dataset == "maven":
            from maven_utils import load_maven
            data_path = args.data_path or "./data/maven_parquet/valid.parquet"
            samples = load_maven(data_path=data_path, max_samples=args.max_samples)
        elif args.dataset == "fewrel":
            from fewrel_utils import load_fewrel
            data_path = args.data_path or "./data/fewrel_parquet/val.parquet"
            samples = load_fewrel(data_path=data_path, max_samples=args.max_samples)
        logger.info("Loaded %d test samples", len(samples))

        result = sdgd_extract(
            types=type_definitions,
            embeddings_path=args.embeddings_path,
            sim_matrix_path=args.sim_matrix_path,
            model_path=args.model_path,
            samples=samples,
            k=args.k,
            tau=args.tau,
            task=args.task,
            prompt_version=args.prompt_version,
            max_model_len=args.max_model_len,
            dataset=args.dataset,
        )

        if args.dataset == "fewrel":
            # TODO: RE evaluation needs accuracy metric, not span F1
            gold = [{"relation": s["relation_type"]} for s in samples]
            metrics = {"f1": 0.0, "precision": 0.0, "recall": 0.0, "note": "RE eval not implemented"}
        else:
            gold = [s["entities"] for s in samples]
            metrics = compute_f1(result["predictions"], gold)
        result["metadata"]["metrics"] = metrics
        logger.info("SDGD F1=%.4f P=%.4f R=%.4f", metrics["f1"], metrics["precision"], metrics["recall"])

        with open(output_dir / "sdgd_results.json", "w") as f:
            json.dump({"metadata": result["metadata"], "metrics": metrics}, f, indent=2)
        with open(output_dir / "sdgd_predictions.json", "w") as f:
            json.dump(result["predictions"], f, ensure_ascii=False, indent=2)


    elif args.mode == "sdgd_cal":
        if not args.model_path and not args.confusion_matrix_path:
            parser.error("sdgd_cal requires --model_path or --confusion_matrix_path")

        if args.dataset == "fewnerd":
            data_dir = str(Path(args.data_path).parent) if args.data_path else "./data/parquet"
            samples = load_few_nerd(split="test", max_samples=args.max_samples, data_dir=data_dir)
        elif args.dataset == "maven":
            from maven_utils import load_maven
            data_path = args.data_path or "./data/maven_parquet/valid.parquet"
            samples = load_maven(data_path=data_path, max_samples=args.max_samples)
        elif args.dataset == "fewrel":
            from fewrel_utils import load_fewrel
            data_path = args.data_path or "./data/fewrel_parquet/val.parquet"
            samples = load_fewrel(data_path=data_path, max_samples=args.max_samples)
        logger.info("Loaded %d test samples", len(samples))

        if args.decompose_only and args.confusion_matrix_path:
            import numpy as np_
            decomp = sdgd_decompose(
                types=type_definitions,
                confusion_matrix_path=args.confusion_matrix_path,
                k=args.k,
                tau=args.tau,
            )
            decomp_info = {
                "method": "sdgd_cal",
                "tau": decomp["tau"],
                "k": decomp["k"],
                "n_cal_samples": args.cal_samples,
                "graph_stats": decomp["graph_stats"],
                "batches": {str(k): v for k, v in decomp["batches"].items()},
            }
            with open(output_dir / "decomposition_cal.json", "w") as f:
                json.dump(decomp_info, f, indent=2)
            print(json.dumps(decomp_info, indent=2))
            return

        result = sdgd_cal_extract(
            types=type_definitions,
            model_path=args.model_path,
            samples=samples,
            n_cal_samples=args.cal_samples,
            k=args.k,
            tau=args.tau,
            task=args.task,
            prompt_version=args.prompt_version,
            max_model_len=args.max_model_len,
            dataset=args.dataset,
            confusion_matrix_path=args.confusion_matrix_path,
            output_dir=str(output_dir),
        )

        if args.dataset == "fewrel":
            gold = [{"relation": s["relation_type"]} for s in samples]
            metrics = {"f1": 0.0, "precision": 0.0, "recall": 0.0, "note": "RE eval not implemented"}
        else:
            gold = [s["entities"] for s in samples]
            metrics = compute_f1(result["predictions"], gold)
        result["metadata"]["metrics"] = metrics
        logger.info("SDGD-cal F1=%.4f P=%.4f R=%.4f", metrics["f1"], metrics["precision"], metrics["recall"])

        with open(output_dir / "sdgd_cal_results.json", "w") as f:
            json.dump({"metadata": result["metadata"], "metrics": metrics}, f, indent=2)
        with open(output_dir / "sdgd_cal_predictions.json", "w") as f:
            json.dump(result["predictions"], f, ensure_ascii=False, indent=2)

    elif args.mode in ("single_pass", "per_type", "random_batch"):
        if not args.model_path:
            parser.error(f"{args.mode} requires --model_path")

        if args.dataset == "fewnerd":
            data_dir = str(Path(args.data_path).parent) if args.data_path else "./data/parquet"
            samples = load_few_nerd(split="test", max_samples=args.max_samples, data_dir=data_dir)
        elif args.dataset == "maven":
            from maven_utils import load_maven
            data_path = args.data_path or "./data/maven_parquet/valid.parquet"
            samples = load_maven(data_path=data_path, max_samples=args.max_samples)
        elif args.dataset == "fewrel":
            from fewrel_utils import load_fewrel
            data_path = args.data_path or "./data/fewrel_parquet/val.parquet"
            samples = load_fewrel(data_path=data_path, max_samples=args.max_samples)
        logger.info("Loaded %d test samples", len(samples))

        if args.mode == "single_pass":
            predictions, meta = run_single_pass(
                args.model_path, samples, type_definitions, all_types,
                args.prompt_version, args.max_model_len, args.task)
        elif args.mode == "per_type":
            predictions, meta = run_per_type(
                args.model_path, samples, type_definitions, all_types,
                args.prompt_version, args.max_model_len, args.task)
        else:
            n_batches = args.n_random_batches or 10
            predictions, meta = run_random_batch(
                args.model_path, samples, type_definitions, all_types, n_batches,
                args.prompt_version, args.max_model_len, args.task, seed=args.seed)

        if args.dataset == "fewrel":
            gold = [{"relation": s["relation_type"]} for s in samples]
            metrics = {"f1": 0.0, "precision": 0.0, "recall": 0.0, "note": "RE eval not implemented"}
        else:
            gold = [s["entities"] for s in samples]
            metrics = compute_f1(predictions, gold)
        meta["metrics"] = metrics
        logger.info("%s F1=%.4f P=%.4f R=%.4f", args.mode, metrics["f1"], metrics["precision"], metrics["recall"])

        with open(output_dir / f"{args.mode}_results.json", "w") as f:
            json.dump(meta, f, indent=2)
        with open(output_dir / f"{args.mode}_predictions.json", "w") as f:
            json.dump(predictions, f, ensure_ascii=False, indent=2)

    logger.info("Results saved to %s", output_dir)


if __name__ == "__main__":
    main()
