#!/usr/bin/env python3
"""StructFuse RepoBench-R Retrieval Evaluation.

Evaluates a trained StructFuse bi-encoder on RepoBench-R, a closed-pool
cross-file code retrieval benchmark.  Each instance contains a query
(import_statement + code context) and a candidate pool (context list);
the task is to rank candidates so the gold snippet appears near the top.

Dataset: tianyang/repobench-r (gzip-pickled, loaded via huggingface_hub)
Subsets: python_cff, python_cfr, java_cff, java_cfr
Splits:  train_easy, train_hard, test_easy, test_hard

Outputs (in --output-dir):
  per_instance_results.jsonl   one JSON object per instance
  summary.json                 aggregate Recall@1/5/10, MRR, config

Usage:
  # Dry-run (no GPU, validates pipeline end-to-end)
  python eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun --limit 20

  # Full eval with trained checkpoint
  python eval_repobench.py \
      --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
      --output-dir /root/autodl-tmp/structfuse/eval_results/repobench_qwen \
      --subset python_cff --split test_easy

Dependencies: torch, transformers, numpy, tqdm, huggingface_hub
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import pickle
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

import numpy as np
from tqdm import tqdm


# ── Data structures ─────────────────────────────────────────────────

@dataclass
class RepoBenchInstance:
    instance_id: str
    repo_name: str
    file_path: str
    import_statement: str
    code: str
    next_line: str
    context: list[str]
    gold_snippet_index: int


@dataclass
class InstanceResult:
    instance_id: str
    repo_name: str
    gold_index: int
    pool_size: int
    predicted_ranking: list[int]       # indices into context, ranked by score
    predicted_scores: list[float]      # corresponding scores
    recall: dict[str, float]           # {"@1": 0/1, "@5": ..., "@10": ...}
    reciprocal_rank: float
    error: str = ""


# ── Data loading ────────────────────────────────────────────────────

_URLS = {
    "java_cff":   "data/java_cff.gz",
    "java_cfr":   "data/java_cfr.gz",
    "python_cff": "data/python_cff.gz",
    "python_cfr": "data/python_cfr.gz",
}


def load_repobench(
    subset: str,
    split: str,
    cache_dir: str = "",
) -> list[RepoBenchInstance]:
    """Download and parse RepoBench-R data via huggingface_hub."""
    from huggingface_hub import hf_hub_download

    if subset not in _URLS:
        raise ValueError(f"Unknown subset '{subset}', choose from {list(_URLS.keys())}")

    parts = split.split("_")
    if len(parts) != 2 or parts[0] not in ("train", "test") or parts[1] not in ("easy", "hard"):
        raise ValueError(f"Invalid split '{split}', use train_easy/train_hard/test_easy/test_hard")

    kwargs = {}
    if cache_dir:
        kwargs["cache_dir"] = cache_dir

    print(f"Downloading tianyang/repobench-r/{_URLS[subset]} ...")
    gz_path = hf_hub_download(
        "tianyang/repobench-r", _URLS[subset], repo_type="dataset", **kwargs
    )

    print(f"Loading pickle from {gz_path} ...")
    with gzip.open(gz_path, "rb") as f:
        data = pickle.load(f)

    subset_key, level = parts[0], parts[1]
    raw = data[subset_key][level]
    print(f"  {subset}/{split}: {len(raw)} examples")

    instances = []
    for i, ex in enumerate(raw):
        instances.append(RepoBenchInstance(
            instance_id=f"{subset}_{split}_{i:05d}",
            repo_name=ex["repo_name"],
            file_path=ex["file_path"],
            import_statement=ex["import_statement"],
            code=ex["code"],
            next_line=ex["next_line"],
            context=ex["context"],
            gold_snippet_index=ex["golden_snippet_index"],
        ))
    return instances


def _mock_repobench(num_instances: int, pool_size: int = 10) -> list[RepoBenchInstance]:
    """Generate synthetic instances for dry-run testing."""
    rng = np.random.default_rng(42)
    instances = []
    for i in range(num_instances):
        gold_idx = int(rng.integers(0, pool_size))
        context = [
            f"def helper_{i}_{j}():\n    return {j}\n" for j in range(pool_size)
        ]
        instances.append(RepoBenchInstance(
            instance_id=f"mock_{i:05d}",
            repo_name=f"mock/repo_{i % 3}",
            file_path=f"src/module_{i}.py",
            import_statement=f"from helpers import helper_{i}_{gold_idx}",
            code=f"def main():\n    result = helper_{i}_{gold_idx}()\n",
            next_line=f"    print(result)",
            context=context,
            gold_snippet_index=gold_idx,
        ))
    return instances


# ── Retrievers ──────────────────────────────────────────────────────

class MockRetriever:
    """Random-score retriever for dry-run validation."""

    def rank(
        self, query: str, candidates: list[str], batch_size: int = 32
    ) -> tuple[list[int], list[float]]:
        """Return (ranked_indices, scores) with deterministic random scores."""
        if not candidates:
            return [], []
        rng = np.random.default_rng(hash(query) % (2**31))
        scores = rng.random(len(candidates)).astype(float)
        idx = np.argsort(scores)[::-1]
        return idx.tolist(), [float(scores[i]) for i in idx]


class StructFuseRetriever:
    """Bi-encoder retriever using a trained StructFuse checkpoint."""

    def __init__(
        self,
        checkpoint_path: str,
        model_name: str | None = None,
        max_seq_length: int = 2048,
        device: str = "cuda",
    ):
        import torch
        from transformers import AutoTokenizer

        train_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "..", "training"
        )
        # Also try sibling directory layout
        alt_train_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "training"
        )
        for d in [train_dir, alt_train_dir]:
            if d not in sys.path and os.path.isdir(d):
                sys.path.insert(0, d)
        from contrastive_model import StructFuseEncoder

        self._torch = torch
        self.device = torch.device(device if torch.cuda.is_available() else "cpu")
        self.max_seq_length = max_seq_length

        with open(os.path.join(checkpoint_path, "training_config.json")) as f:
            cfg = json.load(f)

        base_model = model_name or cfg.get("model_name", "Qwen/Qwen2.5-Coder-3B")
        self.tokenizer = AutoTokenizer.from_pretrained(
            checkpoint_path, trust_remote_code=True
        )
        self.model = StructFuseEncoder(
            model_name=base_model,
            proj_dim=cfg.get("proj_dim", 256),
            use_projection=True,
            use_lora=cfg.get("use_lora", False),
            lora_r=cfg.get("lora_r", 16),
            lora_alpha=cfg.get("lora_alpha", 32),
            use_fusion_head=cfg.get("use_fusion_head", False),
        )
        sd = torch.load(
            os.path.join(checkpoint_path, "model.pt"),
            map_location="cpu",
            weights_only=True,
        )
        self.model.load_state_dict(sd)
        self.model.to(self.device).eval()
        print(f"Loaded StructFuse from {checkpoint_path} on {self.device}")

    def _encode(self, texts: list[str], batch_size: int) -> np.ndarray:
        torch = self._torch
        parts: list[np.ndarray] = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            enc = self.tokenizer(
                batch,
                padding=True,
                truncation=True,
                max_length=self.max_seq_length,
                return_tensors="pt",
            ).to(self.device)
            with torch.no_grad():
                emb = self.model.encode(enc["input_ids"], enc["attention_mask"])
            parts.append(emb.cpu().numpy())
        return np.concatenate(parts, axis=0)

    def rank(
        self, query: str, candidates: list[str], batch_size: int = 32
    ) -> tuple[list[int], list[float]]:
        """Rank candidates by cosine similarity to query. Returns (indices, scores)."""
        if not candidates:
            return [], []
        q = self._encode([query], batch_size=1)
        # Truncate very long snippets for encoding
        docs = [c[:12000] for c in candidates]
        d = self._encode(docs, batch_size=batch_size)
        scores = (q @ d.T).squeeze(0)
        idx = np.argsort(scores)[::-1]
        return idx.tolist(), [float(scores[i]) for i in idx]


# ── Metrics ─────────────────────────────────────────────────────────

def recall_at_k(predicted_indices: list[int], gold_index: int, k: int) -> float:
    return 1.0 if gold_index in predicted_indices[:k] else 0.0


def reciprocal_rank(predicted_indices: list[int], gold_index: int) -> float:
    for rank, idx in enumerate(predicted_indices, start=1):
        if idx == gold_index:
            return 1.0 / rank
    return 0.0


# ── Resume helpers ──────────────────────────────────────────────────

def load_completed(output_dir: str) -> set[str]:
    path = os.path.join(output_dir, "per_instance_results.jsonl")
    done = set()
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                if line.strip():
                    try:
                        obj = json.loads(line)
                        done.add(obj["instance_id"])
                    except (json.JSONDecodeError, KeyError):
                        pass
    return done


def append_result(output_dir: str, result: InstanceResult):
    path = os.path.join(output_dir, "per_instance_results.jsonl")
    with open(path, "a") as f:
        f.write(json.dumps(asdict(result), ensure_ascii=False) + "\n")


# ── Query construction ──────────────────────────────────────────────

def build_query(inst: RepoBenchInstance) -> str:
    """Build the query text from import_statement + code context."""
    parts = []
    if inst.import_statement.strip():
        parts.append(inst.import_statement.strip())
    if inst.code.strip():
        parts.append(inst.code.strip())
    return "\n".join(parts)


# ── Main evaluation ─────────────────────────────────────────────────

def evaluate(args):
    k_values = [int(k) for k in args.top_k.split(",")]
    os.makedirs(args.output_dir, exist_ok=True)

    # 1. Load data
    if args.dry_run:
        limit = args.limit if args.limit > 0 else 50
        try:
            instances = load_repobench(args.subset, args.split, cache_dir=args.cache_dir)
            if limit > 0:
                instances = instances[:limit]
            print(f"Dry-run: loaded {len(instances)} real instances")
        except Exception as e:
            print(f"Could not load HF dataset ({e}), using mock data")
            instances = _mock_repobench(limit)
    else:
        instances = load_repobench(args.subset, args.split, cache_dir=args.cache_dir)
        if args.limit > 0:
            instances = instances[:args.limit]

    print(f"Evaluating {len(instances)} instances, subset={args.subset}, split={args.split}")
    pool_sizes = [len(inst.context) for inst in instances]
    print(f"Pool sizes: min={min(pool_sizes)}, max={max(pool_sizes)}, "
          f"mean={np.mean(pool_sizes):.1f}")

    # 2. Initialize retriever
    if args.dry_run:
        retriever = MockRetriever()
    else:
        retriever = StructFuseRetriever(
            checkpoint_path=args.checkpoint_path,
            model_name=args.model_name,
            max_seq_length=args.max_seq_length,
            device=args.device,
        )

    # 3. Resume support
    completed = load_completed(args.output_dir)
    if completed:
        print(f"Resuming: {len(completed)} already done, "
              f"{len(instances) - len(completed)} remaining")

    # 4. Evaluate each instance
    for inst in tqdm(instances, desc="RepoBench-R eval"):
        if inst.instance_id in completed:
            continue

        try:
            query = build_query(inst)
            ranked_indices, scores = retriever.rank(
                query, inst.context, batch_size=args.batch_size
            )

            rec = {}
            for k in k_values:
                rec[f"@{k}"] = recall_at_k(ranked_indices, inst.gold_snippet_index, k)
            rr = reciprocal_rank(ranked_indices, inst.gold_snippet_index)

            result = InstanceResult(
                instance_id=inst.instance_id,
                repo_name=inst.repo_name,
                gold_index=inst.gold_snippet_index,
                pool_size=len(inst.context),
                predicted_ranking=ranked_indices[:20],
                predicted_scores=scores[:20],
                recall=rec,
                reciprocal_rank=round(rr, 6),
            )
        except Exception as e:
            result = InstanceResult(
                instance_id=inst.instance_id,
                repo_name=inst.repo_name,
                gold_index=inst.gold_snippet_index,
                pool_size=len(inst.context),
                predicted_ranking=[],
                predicted_scores=[],
                recall={f"@{k}": 0.0 for k in k_values},
                reciprocal_rank=0.0,
                error=str(e),
            )

        append_result(args.output_dir, result)

    # 5. Write summary
    _write_summary(args, k_values)


def _write_summary(args, k_values: list[int]):
    """Recompute aggregate metrics from all per-instance results."""
    all_results = []
    rpath = os.path.join(args.output_dir, "per_instance_results.jsonl")
    if os.path.exists(rpath):
        with open(rpath) as f:
            for line in f:
                if line.strip():
                    try:
                        all_results.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass

    valid = [r for r in all_results if not r.get("error")]
    summary: dict = {
        "config": {
            "checkpoint_path": args.checkpoint_path,
            "subset": args.subset,
            "split": args.split,
            "top_k": k_values,
            "dry_run": args.dry_run,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "total_instances": len(all_results),
        "valid_instances": len(valid),
        "errors": len(all_results) - len(valid),
    }

    # Pool size stats
    pool_sizes = [r.get("pool_size", 0) for r in valid]
    if pool_sizes:
        summary["pool_size_mean"] = round(float(np.mean(pool_sizes)), 1)
        summary["pool_size_min"] = min(pool_sizes)
        summary["pool_size_max"] = max(pool_sizes)
        # Theoretical chance level
        summary["chance_recall_at_1"] = round(1.0 / np.mean(pool_sizes), 4)

    for k in k_values:
        vals = [r["recall"].get(f"@{k}", 0.0) for r in valid]
        summary[f"recall@{k}"] = round(float(np.mean(vals)), 4) if vals else 0.0

    mrr_vals = [r.get("reciprocal_rank", 0.0) for r in valid]
    summary["mrr"] = round(float(np.mean(mrr_vals)), 4) if mrr_vals else 0.0

    with open(os.path.join(args.output_dir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"Instances: {len(all_results)} total, {len(valid)} valid, "
          f"{len(all_results) - len(valid)} errors")
    if pool_sizes:
        print(f"  Pool size: mean={summary['pool_size_mean']}, "
              f"min={summary['pool_size_min']}, max={summary['pool_size_max']}")
        print(f"  Chance Recall@1: {summary['chance_recall_at_1']:.4f}")
    for k in k_values:
        print(f"  Recall@{k:>2d}: {summary[f'recall@{k}']:.4f}")
    print(f"  MRR:       {summary['mrr']:.4f}")
    print(f"\nResults: {args.output_dir}/")


# ── CLI ─────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(
        description="StructFuse RepoBench-R retrieval evaluation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--checkpoint-path", default="mock",
        help='Checkpoint dir (model.pt + training_config.json), or "mock" for dry-run',
    )
    p.add_argument("--model-name", default=None,
                    help="Override base model name (default: from training_config.json)")
    p.add_argument("--subset", default="python_cff",
                    choices=list(_URLS.keys()),
                    help="RepoBench-R subset (default: python_cff)")
    p.add_argument("--split", default="test_easy",
                    help="Split to evaluate: train_easy/train_hard/test_easy/test_hard")
    p.add_argument("--output-dir", default="repobench_eval_results")
    p.add_argument("--top-k", default="1,5,10",
                    help="Comma-separated k values for Recall@k (default: 1,5,10)")
    p.add_argument("--batch-size", type=int, default=32)
    p.add_argument("--max-seq-length", type=int, default=2048)
    p.add_argument("--device", default="cuda")
    p.add_argument("--limit", type=int, default=0,
                    help="Max instances to evaluate, 0 = all")
    p.add_argument("--dry-run", action="store_true",
                    help="Mock retriever (random scores), no GPU needed")
    p.add_argument("--cache-dir", default="",
                    help="HuggingFace cache dir for dataset downloads")
    args = p.parse_args()
    evaluate(args)


if __name__ == "__main__":
    main()
