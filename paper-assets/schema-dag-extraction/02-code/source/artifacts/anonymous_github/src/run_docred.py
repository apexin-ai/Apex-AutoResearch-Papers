"""DocRED confusability pilot (exp_docred_confusability).

Adapts FewRel BCS pipeline to DocRED document-level RE.
- 96 relation types
- Closed-set classification: given (document, head, tail) → predict relation
- Count curve: count={4, 16, 64}, 3 random batches per count
- Greedy decoding, constrained JSON output

Two-stage execution:
    python3 src/run_docred.py --stage all
    python3 src/run_docred.py --stage all --dry_run
    python3 src/run_docred.py --stage preprocess  # CPU only
    python3 src/run_docred.py --stage extract     # GPU only
"""
import argparse
import json
import logging
import random
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

logger = logging.getLogger(__name__)

BASE_DIR = Path(".")
DATA_DIR = BASE_DIR / "data" / "docred"
OUTPUT_DIR = BASE_DIR / "artifacts" / "exp_docred_confusability"

COUNTS = [4, 16, 64]
N_RANDOM_PER_COUNT = 3
DEFAULT_N_SAMPLES = 500
SEED = 42


# === Data Loading ===

def load_docred_dev(data_path=None):
    """Load DocRED dev set and convert to RE samples."""
    if data_path is None:
        data_path = DATA_DIR / "dev.json"
    with open(data_path) as f:
        docs = json.load(f)

    rel_info_path = DATA_DIR / "rel_info.json"
    with open(rel_info_path) as f:
        rel_info = json.load(f)

    samples = []
    for doc in docs:
        text = " ".join(" ".join(sent) for sent in doc["sents"])
        vertex_set = doc["vertexSet"]

        for label in doc["labels"]:
            h_idx, t_idx, rel_pid = label["h"], label["t"], label["r"]
            head_name = vertex_set[h_idx][0]["name"]
            tail_name = vertex_set[t_idx][0]["name"]
            rel_name = rel_info.get(rel_pid, rel_pid)

            samples.append({
                "text": text,
                "head_entity": head_name,
                "tail_entity": tail_name,
                "relation_type": rel_name,
                "relation_pid": rel_pid,
                "doc_title": doc["title"],
            })

    return samples, rel_info


def sample_balanced(samples, n_per_relation, seed=42):
    """Sample n_per_relation per relation type."""
    rng = random.Random(seed)
    by_rel = defaultdict(list)
    for s in samples:
        by_rel[s["relation_type"]].append(s)

    sampled = []
    for rel in sorted(by_rel.keys()):
        pool = by_rel[rel]
        k = min(n_per_relation, len(pool))
        sampled.extend(rng.sample(pool, k))
    return sampled


# === SCS Matrix ===

def compute_scs_matrix(rel_info):
    """Compute SCS matrix for DocRED relation types using all-MiniLM-L6-v2."""
    from sentence_transformers import SentenceTransformer

    local_path = "~/.cache/huggingface/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/c9745ed1d9f207416be6d2e6f8de32d1f16199bf"
    if Path(local_path).exists():
        model = SentenceTransformer(local_path, device="cpu")
    else:
        model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

    type_names = sorted(rel_info.values())
    texts = [f"Relation type: {name}" for name in type_names]
    embeddings = model.encode(texts, show_progress_bar=False)

    vecs = torch.tensor(embeddings).float()
    vecs = F.normalize(vecs, dim=1)
    sim_matrix = vecs @ vecs.T

    type_to_idx = {name: i for i, name in enumerate(type_names)}
    return sim_matrix, type_names, type_to_idx


def compute_bcs(type_subset, sim_matrix, type_to_idx):
    """BCS = mean pairwise cosine similarity in subset."""
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


# === Batch Selection ===

def select_random_batches(n, num_batches, type_names, sim_matrix, type_to_idx, seed=42):
    """Random batches of n types with BCS."""
    rng = random.Random(seed)
    results = []
    for _ in range(num_batches):
        chosen = rng.sample(type_names, n)
        bcs = compute_bcs(chosen, sim_matrix, type_to_idx)
        results.append({"types": chosen, "bcs": bcs})
    return results


def build_batch_config(sim_matrix, type_names, type_to_idx, counts, n_random, seed):
    """Build batch config: n_random random batches per count."""
    config = {}
    for count in counts:
        effective = min(count, len(type_names))
        batches = select_random_batches(
            effective, n_random, type_names, sim_matrix, type_to_idx,
            seed + count
        )
        config[f"count_{effective}"] = {"random": batches}
    return config


# === Prompt & Schema ===

def build_prompt_docred(text, head, tail, relation_types):
    """Build RE prompt for DocRED document-level classification."""
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
    """Constrained JSON schema for RE output."""
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


# === Extraction ===

def run_extraction(model_path, samples, batch_config, max_model_len=4096,
                   gpu_memory_utilization=0.90):
    """Run RE extraction with vLLM offline (constrained JSON)."""
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

    for count_key, strategies in batch_config.items():
        batches_to_run = []
        for ri, rb in enumerate(strategies.get("random", [])):
            batches_to_run.append((f"random_{ri}", rb["types"], rb["bcs"]))

        for batch_id, batch_types, batch_bcs in batches_to_run:
            full_batch_id = f"{count_key}_{batch_id}"
            type_set = set(batch_types)

            # Filter samples with gold relation in this batch
            batch_samples = [s for s in samples if s["relation_type"] in type_set]
            if not batch_samples:
                logger.warning("No samples for batch %s", full_batch_id)
                continue

            schema = build_json_schema_re(batch_types)
            structured = StructuredOutputsParams(json=schema)  #
            sampling_params = SamplingParams(
                temperature=0, max_tokens=64, seed=SEED,
                structured_outputs=structured,
            )

            prompts = []
            sample_indices = []
            for si, s in enumerate(batch_samples):
                prompt = build_prompt_docred(
                    s["text"], s["head_entity"], s["tail_entity"], batch_types
                )
                prompts.append(prompt)
                sample_indices.append(si)

            logger.info("Batch %s: %d types, BCS=%.4f, %d samples",
                        full_batch_id, len(batch_types), batch_bcs, len(prompts))

            t0 = time.time()
            outputs = llm.generate(prompts, sampling_params)
            elapsed = time.time() - t0

            for oi, output in enumerate(outputs):
                si = sample_indices[oi]
                s = batch_samples[si]
                generated_text = output.outputs[0].text

                try:
                    pred_obj = json.loads(generated_text)
                    prediction = pred_obj.get("relation", "PARSE_ERROR")
                except json.JSONDecodeError:
                    prediction = "PARSE_ERROR"

                all_results.append({
                    "batch_id": full_batch_id,
                    "count_key": count_key,
                    "batch_types": batch_types,
                    "batch_bcs": batch_bcs,
                    "ground_truth": s["relation_type"],
                    "prediction": prediction,
                    "head_entity": s["head_entity"],
                    "tail_entity": s["tail_entity"],
                    "doc_title": s["doc_title"],
                })

            correct = sum(1 for r in all_results[-len(prompts):]
                          if r["prediction"] == r["ground_truth"])
            logger.info("  -> acc=%.4f (%d/%d) in %.1fs",
                        correct / len(prompts), correct, len(prompts), elapsed)

    return all_results


# === Evaluation ===

def evaluate(results):
    """Per-batch accuracy."""
    batch_stats = defaultdict(lambda: {"correct": 0, "total": 0, "bcs": 0.0,
                                       "count_key": "", "batch_types": []})
    for r in results:
        bid = r["batch_id"]
        s = batch_stats[bid]
        s["total"] += 1
        s["bcs"] = r["batch_bcs"]
        s["count_key"] = r["count_key"]
        s["batch_types"] = r["batch_types"]
        if r["prediction"] == r["ground_truth"]:
            s["correct"] += 1

    out = {}
    for bid, s in batch_stats.items():
        out[bid] = {
            "accuracy": s["correct"] / s["total"] if s["total"] else 0.0,
            "correct": s["correct"],
            "total": s["total"],
            "bcs": s["bcs"],
            "count_key": s["count_key"],
            "num_types": len(s["batch_types"]),
        }
    return out


# === Stages ===

def stage_preprocess(args):
    """CPU stage: load data, compute SCS, build batches, save config."""
    random.seed(args.seed)

    logger.info("Loading DocRED dev set...")
    all_samples, rel_info = load_docred_dev()
    logger.info("Loaded %d triples from %d relation types",
                len(all_samples), len(set(s["relation_type"] for s in all_samples)))

    # Sample balanced
    n_rels = len(rel_info)
    n_per_rel = max(1, args.n_samples // n_rels)
    samples = sample_balanced(all_samples, n_per_rel, seed=args.seed)
    logger.info("Sampled %d (target %d/rel)", len(samples), n_per_rel)

    # Compute SCS matrix
    logger.info("Computing SCS matrix (96 relations, all-MiniLM-L6-v2)...")
    sim_matrix, type_names, type_to_idx = compute_scs_matrix(rel_info)
    logger.info("SCS matrix: %s, range [%.4f, %.4f] (off-diag)",
                sim_matrix.shape,
                sim_matrix[~torch.eye(96, dtype=bool)].min().item(),
                sim_matrix[~torch.eye(96, dtype=bool)].max().item())

    # Save SCS matrix
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    scs_path = OUTPUT_DIR / "scs_matrix.npy"
    np.save(scs_path, sim_matrix.numpy())
    torch.save({"sim_matrix": sim_matrix, "type_names": type_names,
                "type_to_idx": type_to_idx}, OUTPUT_DIR / "scs_matrix.pt")
    logger.info("Saved SCS matrix to %s", scs_path)

    # Build batch config
    counts = [int(c) for c in args.counts.split(",")]
    batch_config = build_batch_config(
        sim_matrix, type_names, type_to_idx, counts,
        args.n_random, args.seed
    )

    # Print summary
    logger.info("=" * 60)
    logger.info("BATCH CONFIGURATION")
    logger.info("=" * 60)
    total_inferences = 0
    for ck, strategies in sorted(batch_config.items()):
        for rb in strategies["random"]:
            n = sum(1 for s in samples if s["relation_type"] in set(rb["types"]))
            total_inferences += n
        bcs_vals = [b["bcs"] for b in strategies["random"]]
        logger.info("  %s: %d batches, BCS range [%.4f, %.4f]",
                    ck, len(strategies["random"]), min(bcs_vals), max(bcs_vals))
    logger.info("Total inferences: %d", total_inferences)

    # Save preprocess config
    preprocess_config = {
        "samples": samples,
        "batch_config": batch_config,
        "model_path": args.model_path,
        "max_model_len": args.max_model_len,
        "gpu_memory_utilization": args.gpu_memory_utilization,
        "output_dir": str(OUTPUT_DIR),
        "n_relation_types": len(type_names),
        "scs_matrix_shape": list(sim_matrix.shape),
    }
    preprocess_path = OUTPUT_DIR / "preprocess_config.json"
    with open(preprocess_path, "w") as f:
        json.dump(preprocess_config, f, ensure_ascii=False, indent=2)
    logger.info("Saved preprocess config: %s", preprocess_path)

    if args.dry_run:
        logger.info("DRY RUN COMPLETE")
        return None

    return str(preprocess_path)


def stage_extract(args):
    """GPU stage: run vLLM extraction."""
    preprocess_path = args.preprocess_path or str(OUTPUT_DIR / "preprocess_config.json")
    with open(preprocess_path) as f:
        config = json.load(f)

    results = run_extraction(
        config["model_path"],
        config["samples"],
        config["batch_config"],
        config["max_model_len"],
        config["gpu_memory_utilization"],
    )

    # Save results
    output_dir = Path(config["output_dir"])
    with open(output_dir / "predictions.json", "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info("Saved %d predictions", len(results))

    # Evaluate
    eval_results = evaluate(results)
    with open(output_dir / "eval_results.json", "w") as f:
        json.dump(eval_results, f, indent=2)

    # Build pilot_results.json
    pilot = defaultdict(lambda: {"batches": [], "n_samples": []})
    bcs_all = []
    for bid, m in eval_results.items():
        ck = m["count_key"]
        pilot[ck]["batches"].append(m["accuracy"])
        pilot[ck]["n_samples"].append(m["total"])
        bcs_all.append(m["bcs"])

    pilot_results = {}
    for ck in sorted(pilot.keys()):
        accs = pilot[ck]["batches"]
        pilot_results[ck] = {
            "batches": [round(a, 4) for a in accs],
            "mean": round(np.mean(accs), 4),
            "n_samples_per_batch": pilot[ck]["n_samples"],
        }

    pilot_results["n_relation_types"] = config["n_relation_types"]
    pilot_results["n_eval_samples"] = len(results)
    pilot_results["scs_matrix_shape"] = config["scs_matrix_shape"]
    pilot_results["bcs_range"] = [round(min(bcs_all), 4), round(max(bcs_all), 4)]
    pilot_results["pipeline_status"] = "OK"
    pilot_results["notes"] = "DocRED pilot: closed-set RE classification, Qwen3-32B-FP8, greedy decoding"

    with open(output_dir / "pilot_results.json", "w") as f:
        json.dump(pilot_results, f, indent=2)

    logger.info("=" * 60)
    logger.info("PILOT RESULTS")
    logger.info("=" * 60)
    for bid, m in sorted(eval_results.items()):
        logger.info("  %-30s acc=%.4f (%3d/%3d) BCS=%.4f",
                    bid, m["accuracy"], m["correct"], m["total"], m["bcs"])
    logger.info("-" * 60)
    for ck in sorted(pilot.keys()):
        logger.info("  %s: mean_acc=%.4f", ck, np.mean(pilot[ck]["batches"]))


def main():
    parser = argparse.ArgumentParser(description="DocRED Confusability Pilot")
    parser.add_argument("--model_path",
                        default="~/.cache/huggingface/qwen3-32b-fp8/")
    parser.add_argument("--n_samples", type=int, default=DEFAULT_N_SAMPLES)
    parser.add_argument("--counts", default="4,16,64")
    parser.add_argument("--n_random", type=int, default=N_RANDOM_PER_COUNT)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--max_model_len", type=int, default=4096)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.90)
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--stage", choices=["preprocess", "extract", "all"],
                        default="all")
    parser.add_argument("--preprocess_path", default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")

    if args.stage == "preprocess":
        stage_preprocess(args)
    elif args.stage == "extract":
        stage_extract(args)
    elif args.stage == "all":
        preprocess_path = stage_preprocess(args)
        if preprocess_path is None:
            return

        logger.info("=== Launching extract subprocess (vLLM-first) ===")
        cmd = [sys.executable, str(Path(__file__).resolve()),
               "--stage", "extract",
               "--preprocess_path", preprocess_path]
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
