#!/usr/bin/env python3
"""SDGD Stage 2: GPU extraction. Loads vLLM FIRST to avoid fork deadlock.

Usage:
    python3 sdgd_extract_gpu.py \
        --decompositions decomp_a.json decomp_b.json \
        --model_path /path/to/model \
        --types_file configs/few_nerd_types.json \
        --output_dir artifacts/exp008
"""
import argparse
import json
import os
import sys
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--decompositions', nargs='+', required=True,
                        help='One or more decomposition JSONs from Stage 1')
    parser.add_argument('--model_path', required=True)
    parser.add_argument('--types_file', required=True)
    parser.add_argument('--dataset', default='fewnerd',
                        choices=['fewnerd', 'maven', 'fewrel'])
    parser.add_argument('--data_path', default=None)
    parser.add_argument('--prompt_version', default='v2', choices=['v1', 'v2'])
    parser.add_argument('--max_samples', type=int, default=None)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--max_model_len', type=int, default=4096)
    parser.add_argument('--task', default='ner', choices=['ner', 'event', 're'])
    parser.add_argument('--merge_strategy', default='confidence',
                        choices=['union', 'confidence'],
                        help='Merge strategy: union (v1) or confidence (v2)')
    parser.add_argument('--confidence_threshold', type=float, default=-1.0,
                        help='Min normalized logprob to keep a prediction (default: -1.0)')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    # ========== vLLM MUST be initialized FIRST ==========
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    print(f"[gpu] Loading vLLM model from {args.model_path} ...")
    t_load = time.time()
    llm = LLM(
        model=args.model_path,
        dtype="bfloat16",
        gpu_memory_utilization=0.95,
        enforce_eager=True,
        max_model_len=args.max_model_len,
        trust_remote_code=True,
        disable_log_stats=True,
    )
    print(f"[gpu] vLLM ready in {time.time() - t_load:.1f}s")

    # ========== Now safe to import everything else ==========
    import logging
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    logger = logging.getLogger(__name__)

    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))

    if args.task == "re":
        from run_extraction import build_json_schema_re, build_prompt_v2_re
        schema_fn = build_json_schema_re
        prompt_fn = None
    elif args.task == "event":
        from run_extraction import build_json_schema_v2
        schema_fn = build_json_schema_v2
        if args.prompt_version == "v2":
            from run_extraction import build_prompt_v2_event
            prompt_fn = build_prompt_v2_event
        else:
            from run_extraction import build_prompt_v1_event
            prompt_fn = build_prompt_v1_event
    else:
        if args.prompt_version == "v2":
            from run_extraction import build_json_schema_v2, build_prompt_v2
            schema_fn = build_json_schema_v2
            prompt_fn = build_prompt_v2
        else:
            from run_extraction import build_json_schema_v1, build_prompt_v1
            schema_fn = build_json_schema_v1
            prompt_fn = build_prompt_v1

    from sdgd.merge import merge_all_samples, merge_with_confidence
    from sdgd.evaluate import compute_f1

    with open(args.types_file) as f:
        type_definitions = json.load(f)

    if args.dataset == "fewnerd":
        from few_nerd_utils import load_few_nerd
        data_dir = (str(Path(args.data_path).parent)
                    if args.data_path
                    else "./data/parquet")
        samples = load_few_nerd(split="test", max_samples=args.max_samples,
                                data_dir=data_dir)
    elif args.dataset == "maven":
        from maven_utils import load_maven
        data_path = (args.data_path
                     or "./data/maven_parquet/valid.parquet")
        samples = load_maven(data_path=data_path, max_samples=args.max_samples)
    elif args.dataset == "fewrel":
        from fewrel_utils import load_fewrel
        data_path = (args.data_path
                     or "./data/fewrel_parquet/val.parquet")
        samples = load_fewrel(data_path=data_path, max_samples=args.max_samples)

    logger.info("Loaded %d samples (%s)", len(samples), args.dataset)
    logger.info("Merge strategy: %s (threshold=%.2f)", args.merge_strategy, args.confidence_threshold)

    # ========== Process each decomposition ==========
    for decomp_path in args.decompositions:
        with open(decomp_path) as f:
            decomp = json.load(f)

        mode = decomp['mode']
        batches = decomp['batches']
        logger.info("========== Mode: %s | %d batches ==========", mode, len(batches))

        all_results = []
        t_start = time.time()

        for bi, batch_types in enumerate(batches):
            batch_id = f"batch_{bi}"
            logger.info("  Batch %d/%d: %d types", bi + 1, len(batches),
                        len(batch_types))

            batch_schema = schema_fn(batch_types)
            structured_params = StructuredOutputsParams(json=batch_schema)
            sampling_params = SamplingParams(
                max_tokens=1024, temperature=0.0,
                structured_outputs=structured_params,
                logprobs=1 if args.merge_strategy == 'confidence' else None,
            )

            if args.task == "re":
                prompts = [
                    build_prompt_v2_re(
                        s["text"], s["head_entity"], s["tail_entity"],
                        type_definitions, batch_types)
                    for s in samples
                ]
            else:
                prompts = [
                    prompt_fn(s["text"], type_definitions, batch_types)
                    for s in samples
                ]

            t0 = time.time()
            outputs = llm.generate(prompts, sampling_params)
            elapsed = time.time() - t0

            for si, output in enumerate(outputs):
                gen_output = output.outputs[0]
                try:
                    preds = json.loads(gen_output.text)
                except json.JSONDecodeError:
                    preds = []

                # Compute sequence-level confidence (normalized logprob)
                confidence = 0.0
                if args.merge_strategy == 'confidence':
                    n_tokens = len(gen_output.token_ids)
                    if n_tokens > 0 and gen_output.cumulative_logprob is not None:
                        confidence = gen_output.cumulative_logprob / n_tokens

                # Attach confidence to each entity prediction
                if args.merge_strategy == 'confidence' and isinstance(preds, list):
                    for ent in preds:
                        if isinstance(ent, dict):
                            ent["confidence"] = confidence

                all_results.append({
                    "sample_id": si,
                    "batch_id": batch_id,
                    "batch_types": batch_types,
                    "predictions": preds,
                    "prompt_tokens": len(output.prompt_token_ids),
                    "gen_tokens": len(gen_output.token_ids),
                    "latency_s": elapsed / len(prompts),
                    "confidence": confidence,
                })

            logger.info("    %.1fs, %d outputs", elapsed, len(outputs))

        t_total = time.time() - t_start

        # Merge predictions across batches
        if args.merge_strategy == 'confidence':
            merged = merge_with_confidence(
                all_results, len(samples),
                confidence_threshold=args.confidence_threshold,
            )
        else:
            merged = merge_all_samples(all_results, len(samples))

        # Evaluate
        if args.dataset == "fewrel":
            gold = [{"relation": s["relation_type"]} for s in samples]
            metrics = {"f1": 0.0, "precision": 0.0, "recall": 0.0,
                       "note": "RE eval not implemented"}
        else:
            gold = [s["entities"] for s in samples]
            metrics = compute_f1(merged, gold)

        logger.info("%s F1=%.4f P=%.4f R=%.4f (%.1fs)",
                    mode, metrics["f1"], metrics["precision"],
                    metrics["recall"], t_total)

        # Save results
        meta = {
            "mode": mode,
            "n_batches": len(batches),
            "batch_sizes": [len(b) for b in batches],
            "latency_s": t_total,
            "metrics": metrics,
            "n_samples": len(samples),
            "prompt_version": args.prompt_version,
            "task": args.task,
            "dataset": args.dataset,
            "merge_strategy": args.merge_strategy,
            "confidence_threshold": args.confidence_threshold,
        }
        for key in ("tau", "k", "graph_stats", "seed", "min_batch_size",
                     "graph_stats_before_merge"):
            if key in decomp and decomp[key] is not None:
                meta[key] = decomp[key]

        out = args.output_dir
        with open(os.path.join(out, f"{mode}_results.json"), 'w') as f:
            json.dump(meta, f, indent=2)
        with open(os.path.join(out, f"{mode}_predictions.json"), 'w') as f:
            json.dump(merged, f, ensure_ascii=False, indent=2)

        logger.info("Saved %s results to %s", mode, out)

    print("[gpu] All modes complete.")


if __name__ == '__main__':
    main()
