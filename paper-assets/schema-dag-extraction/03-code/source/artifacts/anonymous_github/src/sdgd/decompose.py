"""SDGD main orchestrator: similarity -> graph coloring -> per-batch extraction -> merge.

Input: Type definitions, embeddings/sim_matrix, test samples, vLLM model
Output: Merged predictions + decomposition metadata
Dependencies: torch, networkx, vllm (only at extraction time)
"""
import json
import logging
import time
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import torch

from .similarity import (
    adaptive_threshold,
    cosine_similarity_matrix,
    load_sim_matrix,
    load_type_embeddings,
)
from .graph import build_threshold_graph, color_graph, get_graph_stats, group_by_color
from .merge import merge_all_samples
from .calibrate import build_confusion_matrix, confusion_to_similarity, run_calibration

logger = logging.getLogger(__name__)


def sdgd_decompose(
    types: Dict[str, str],
    embeddings_path: Optional[str] = None,
    sim_matrix_path: Optional[str] = None,
    k: float = 1.0,
    tau: Optional[float] = None,
    confusion_matrix_path: Optional[str] = None,
) -> Dict:
    """Run SDGD steps 1-3 (similarity -> graph -> coloring). No GPU needed.

    Args:
        types: type_name -> description
        embeddings_path: path to type_embeddings.pt
        sim_matrix_path: path to precomputed sim_matrix.pt (preferred if available)
        k: adaptive threshold parameter (ignored if tau is set)
        tau: fixed threshold (overrides adaptive)
        confusion_matrix_path: empirical confusion matrix for SDGD-cal (optional)

    Returns:
        Dict with batches, tau, sim_matrix, type_names, graph_stats
    """
    # Step 1: get similarity matrix
    if confusion_matrix_path and Path(confusion_matrix_path).exists():
        logger.info("Loading confusion-based sim_matrix from %s", confusion_matrix_path)
        data = dict(np.load(confusion_matrix_path, allow_pickle=True))
        sim_np = data.get("similarity_matrix", data.get("sim_matrix"))
        type_names = list(data.get("type_names", sorted(types.keys())))
        sim_matrix = torch.from_numpy(sim_np.astype("float32"))
    elif sim_matrix_path and Path(sim_matrix_path).exists():
        logger.info("Loading precomputed sim_matrix from %s", sim_matrix_path)
        sim_matrix, type_names = load_sim_matrix(sim_matrix_path)
    elif embeddings_path:
        logger.info("Computing sim_matrix from embeddings %s", embeddings_path)
        embeddings, type_names = load_type_embeddings(embeddings_path)
        sim_matrix = cosine_similarity_matrix(embeddings)
    else:
        raise ValueError("Must provide sim_matrix_path, embeddings_path, or confusion_matrix_path")

    # Step 2: compute threshold
    if tau is None:
        tau = adaptive_threshold(sim_matrix, k=k)
    else:
        logger.info("Using fixed threshold tau=%.4f", tau)

    # Step 3: build graph + coloring
    G = build_threshold_graph(sim_matrix, tau, type_names)
    coloring = color_graph(G)
    batches = group_by_color(coloring)
    stats = get_graph_stats(G, batches)

    return {
        "batches": batches,
        "tau": tau,
        "k": k,
        "sim_matrix": sim_matrix,
        "type_names": type_names,
        "graph_stats": stats,
    }


def sdgd_extract(
    types: Dict[str, str],
    embeddings_path: str,
    sim_matrix_path: str,
    model_path: str,
    samples: List[Dict],
    k: float = 1.0,
    tau: Optional[float] = None,
    confusion_matrix_path: Optional[str] = None,
    task: str = "ner",
    prompt_version: str = "v2",
    max_model_len: int = 4096,
    dataset: str = "fewnerd",
) -> Dict:
    """Main SDGD extraction pipeline.

    Steps 1-3: similarity -> graph -> coloring (CPU)
    Step 4: per-batch extraction via vLLM (GPU)
    Step 5: merge predictions

    Returns:
        {"predictions": per-sample merged predictions,
         "raw_results": all per-batch results,
         "metadata": {tau, n_batches, batch_sizes, k, graph_stats, timings}}
    """
    t_start = time.time()

    # Steps 1-3: decompose
    decomp = sdgd_decompose(
        types=types,
        embeddings_path=embeddings_path,
        sim_matrix_path=sim_matrix_path,
        k=k,
        tau=tau,
        confusion_matrix_path=confusion_matrix_path,
    )
    batches = decomp["batches"]
    t_decompose = time.time() - t_start

    # Step 4: per-batch extraction
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

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

    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    logger.info("Loading vLLM model from %s", model_path)
    llm = LLM(
        model=model_path,
        dtype="bfloat16",
        gpu_memory_utilization=0.95,
        enforce_eager=True,
        max_model_len=max_model_len,
        trust_remote_code=True,
        disable_log_stats=True,
    )

    all_results = []
    t_extract_start = time.time()

    for color_id, batch_types in sorted(batches.items()):
        batch_id = f"color_{color_id}"
        logger.info("Extracting batch %s: %d types %s", batch_id, len(batch_types), batch_types)

        batch_schema = schema_fn(batch_types)
        structured_params = StructuredOutputsParams(json=batch_schema)
        sampling_params = SamplingParams(
            max_tokens=1024,
            temperature=0.0,
            structured_outputs=structured_params,
        )

        prompts = []
        for sample in samples:
            if task == "re":
                prompts.append(build_prompt_v2_re(
                    sample["text"], sample["head_entity"],
                    sample["tail_entity"], types, batch_types))
            else:
                prompts.append(prompt_fn(sample["text"], types, batch_types))

        t0 = time.time()
        outputs = llm.generate(prompts, sampling_params)
        elapsed = time.time() - t0

        for si, output in enumerate(outputs):
            generated_text = output.outputs[0].text
            try:
                predictions = json.loads(generated_text)
            except json.JSONDecodeError:
                logger.warning("JSON parse failed for sample %d batch %s", si, batch_id)
                predictions = []

            all_results.append({
                "sample_id": si,
                "batch_id": batch_id,
                "batch_types": batch_types,
                "predictions": predictions,
                "prompt_tokens": len(output.prompt_token_ids),
                "gen_tokens": len(output.outputs[0].token_ids),
                "latency_s": elapsed / len(prompts),
            })

        logger.info("  Batch %s: %.1fs, %d outputs", batch_id, elapsed, len(outputs))

    t_extract = time.time() - t_extract_start

    # Step 5: merge
    merged = merge_all_samples(all_results, len(samples))
    t_total = time.time() - t_start

    metadata = {
        "tau": decomp["tau"],
        "k": decomp["k"],
        "n_batches": len(batches),
        "batch_sizes": [len(b) for b in batches.values()],
        "graph_stats": decomp["graph_stats"],
        "timings": {
            "decompose_s": t_decompose,
            "extract_s": t_extract,
            "total_s": t_total,
        },
        "n_samples": len(samples),
        "prompt_version": prompt_version,
        "task": task,
        "dataset": dataset,
    }

    return {
        "predictions": merged,
        "raw_results": all_results,
        "metadata": metadata,
    }


def sdgd_cal_extract(
    types: Dict[str, str],
    model_path: str,
    samples: List[Dict],
    cal_samples: Optional[List[Dict]] = None,
    n_cal_samples: int = 100,
    k: float = 1.0,
    tau: Optional[float] = None,
    task: str = "ner",
    prompt_version: str = "v2",
    max_model_len: int = 4096,
    dataset: str = "fewnerd",
    confusion_matrix_path: Optional[str] = None,
    output_dir: Optional[str] = None,
) -> Dict:
    """SDGD-cal: empirical confusion -> graph coloring -> batched extraction."""
    t_start = time.time()
    type_list = sorted(types.keys())

    # Step 0: get confusion-based similarity matrix
    if confusion_matrix_path and Path(confusion_matrix_path).exists():
        logger.info("Loading precomputed confusion matrix from %s", confusion_matrix_path)
        data = dict(np.load(confusion_matrix_path, allow_pickle=True))
        sim_np = data["similarity_matrix"]
        sim_matrix = torch.from_numpy(sim_np.astype("float32"))
    else:
        cal_data = cal_samples if cal_samples is not None else samples
        C, sim_np = run_calibration(
            data_samples=cal_data,
            type_list=type_list,
            type_definitions=types,
            model_path=model_path,
            task=task,
            n_samples=n_cal_samples,
            prompt_version=prompt_version,
            max_model_len=max_model_len,
            dataset=dataset,
        )
        sim_matrix = torch.from_numpy(sim_np.astype("float32"))
        if output_dir:
            out_path = Path(output_dir) / "confusion_cal.npz"
            np.savez(out_path, confusion_matrix=C, similarity_matrix=sim_np,
                     type_names=np.array(type_list))
            logger.info("Saved confusion matrix to %s", out_path)

    t_cal = time.time() - t_start

    # Steps 1-3: threshold + graph + coloring
    if tau is None:
        tau = adaptive_threshold(sim_matrix, k=k)
    else:
        logger.info("Using fixed threshold tau=%.4f", tau)

    G = build_threshold_graph(sim_matrix, tau, type_list)
    coloring = color_graph(G)
    batches = group_by_color(coloring)
    stats = get_graph_stats(G, batches)
    t_decompose = time.time() - t_start

    # Step 4: per-batch extraction via vLLM
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

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

    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    logger.info("Loading vLLM model from %s", model_path)
    llm = LLM(
        model=model_path,
        dtype="bfloat16",
        gpu_memory_utilization=0.95,
        enforce_eager=True,
        max_model_len=max_model_len,
        trust_remote_code=True,
        disable_log_stats=True,
    )

    all_results = []
    t_extract_start = time.time()

    for color_id, batch_types in sorted(batches.items()):
        batch_id = f"color_{color_id}"
        logger.info("Extracting batch %s: %d types %s", batch_id, len(batch_types), batch_types)

        batch_schema = schema_fn(batch_types)
        structured_params = StructuredOutputsParams(json=batch_schema)
        sampling_params = SamplingParams(
            max_tokens=1024, temperature=0.0, structured_outputs=structured_params,
        )

        prompts = []
        for sample in samples:
            if task == "re":
                prompts.append(build_prompt_v2_re(
                    sample["text"], sample["head_entity"],
                    sample["tail_entity"], types, batch_types))
            else:
                prompts.append(prompt_fn(sample["text"], types, batch_types))

        t0 = time.time()
        outputs = llm.generate(prompts, sampling_params)
        elapsed = time.time() - t0

        for si, output in enumerate(outputs):
            generated_text = output.outputs[0].text
            try:
                predictions = json.loads(generated_text)
            except json.JSONDecodeError:
                logger.warning("JSON parse failed for sample %d batch %s", si, batch_id)
                predictions = []

            all_results.append({
                "sample_id": si,
                "batch_id": batch_id,
                "batch_types": batch_types,
                "predictions": predictions,
                "prompt_tokens": len(output.prompt_token_ids),
                "gen_tokens": len(output.outputs[0].token_ids),
                "latency_s": elapsed / len(prompts),
            })

        logger.info("  Batch %s: %.1fs, %d outputs", batch_id, elapsed, len(outputs))

    t_extract = time.time() - t_extract_start

    # Step 5: merge
    merged = merge_all_samples(all_results, len(samples))
    t_total = time.time() - t_start

    metadata = {
        "method": "sdgd_cal",
        "tau": tau if isinstance(tau, float) else float(tau),
        "k": k,
        "n_cal_samples": n_cal_samples,
        "n_batches": len(batches),
        "batch_sizes": [len(b) for b in batches.values()],
        "graph_stats": stats,
        "timings": {
            "calibration_s": t_cal,
            "decompose_s": t_decompose,
            "extract_s": t_extract,
            "total_s": t_total,
        },
        "n_samples": len(samples),
        "prompt_version": prompt_version,
        "task": task,
        "dataset": dataset,
    }

    return {
        "predictions": merged,
        "raw_results": all_results,
        "metadata": metadata,
    }
