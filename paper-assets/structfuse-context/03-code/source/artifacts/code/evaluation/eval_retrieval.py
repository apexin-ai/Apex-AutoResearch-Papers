import os
os.environ["CUDA_VISIBLE_DEVICES"] = "4"

"""
StructFuse Retrieval Evaluation Script

Evaluates the StructFuse contrastive retriever on file-level and function-level
retrieval tasks across SWE-bench Lite, RepoBench-R, and custom held-out sets.

Input:
  - Trained StructFuse checkpoint(s)
  - Test file (JSON Lines): each line has {query, gold_files, gold_functions, repo_path}
  - (Optional) CodeQL data-flow output directory

Output:
  - JSON file with per-instance predictions and aggregate metrics:
    Recall@1/5/10, MRR, Structural Precision

Dependencies: transformers, torch, rank_bm25, faiss-cpu, numpy
"""

import argparse
import json
import os
import glob
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import jsonlines
import numpy as np
import torch
import torch.nn.functional as F
from tqdm import tqdm
from transformers import AutoTokenizer
from rank_bm25 import BM25Okapi

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "training"))
from contrastive_model import StructFuseEncoder


@dataclass
class RetrievalInstance:
    query: str
    gold_files: list[str]
    gold_functions: list[str] = field(default_factory=list)
    repo_path: str = ""
    instance_id: str = ""
    metadata: dict = field(default_factory=dict)


@dataclass
class RetrievalResult:
    instance_id: str
    query: str
    gold_files: list[str]
    predicted_files: list[str]
    scores: list[float]
    hits: dict[str, bool] = field(default_factory=dict)


def load_test_data(test_file: str, dataset: str) -> list[RetrievalInstance]:
    """Load test instances from JSON Lines file, adapting format per dataset."""
    instances = []
    with jsonlines.open(test_file) as reader:
        for i, item in enumerate(reader):
            if dataset == "swebench_lite":
                inst = RetrievalInstance(
                    query=item.get("problem_statement", item.get("query", "")),
                    gold_files=item.get("gold_files", []),
                    gold_functions=item.get("gold_functions", []),
                    repo_path=item.get("repo_path", item.get("repo", "")),
                    instance_id=item.get("instance_id", f"swebench_{i}"),
                )
            elif dataset == "repobench":
                inst = RetrievalInstance(
                    query=item.get("query", ""),
                    gold_files=item.get("gold_files", []),
                    gold_functions=item.get("gold_functions", []),
                    repo_path=item.get("repo_path", ""),
                    instance_id=item.get("instance_id", f"repobench_{i}"),
                )
            else:
                inst = RetrievalInstance(
                    query=item["query"],
                    gold_files=item["gold_files"],
                    gold_functions=item.get("gold_functions", []),
                    repo_path=item.get("repo_path", ""),
                    instance_id=item.get("instance_id", f"custom_{i}"),
                    metadata=item.get("metadata", {}),
                )
            instances.append(inst)
    return instances


def collect_candidate_files(repo_path: str, extensions: tuple[str, ...] = (".py",)) -> list[dict]:
    """Walk repo and collect candidate source files with their content."""
    candidates = []
    repo = Path(repo_path)
    if not repo.exists():
        return candidates
    for ext in extensions:
        for fpath in repo.rglob(f"*{ext}"):
            rel = str(fpath.relative_to(repo))
            if any(part.startswith(".") for part in fpath.parts):
                continue
            if "__pycache__" in rel:
                continue
            fname = fpath.name
            if (fname.startswith("test_") and fname.endswith(".py")) or fname.endswith("_test.py"):
                continue
            try:
                content = fpath.read_text(errors="replace")
            except Exception:
                continue
            candidates.append({"path": rel, "content": content})
    return candidates


def bm25_retrieve(query: str, candidates: list[dict], top_k: int = 30) -> list[dict]:
    """BM25 coarse retrieval over candidate file contents."""
    if not candidates:
        return []
    corpus = [c["content"].split() for c in candidates]
    bm25 = BM25Okapi(corpus)
    query_tokens = query.split()
    scores = bm25.get_scores(query_tokens)
    top_indices = np.argsort(scores)[::-1][:top_k]
    results = []
    for idx in top_indices:
        results.append({**candidates[idx], "bm25_score": float(scores[idx])})
    return results


def load_dataflow_reachability(dataflow_dir: str, instance_id: str) -> set[str]:
    """Load data-flow reachable files from CodeQL output for an instance."""
    reachable = set()
    df_file = os.path.join(dataflow_dir, f"{instance_id}.json")
    if not os.path.exists(df_file):
        df_file = os.path.join(dataflow_dir, f"{instance_id}.csv")
    if not os.path.exists(df_file):
        return reachable

    if df_file.endswith(".json"):
        with open(df_file) as f:
            data = json.load(f)
        for edge in data if isinstance(data, list) else data.get("edges", []):
            if "source_file" in edge:
                reachable.add(edge["source_file"])
            if "sink_file" in edge:
                reachable.add(edge["sink_file"])
    elif df_file.endswith(".csv"):
        with open(df_file) as f:
            for line in f:
                parts = line.strip().split(",")
                for p in parts:
                    if p.endswith(".py"):
                        reachable.add(p)
    return reachable


class StructFuseRetriever:
    """Bi-encoder retriever using a trained StructFuse checkpoint."""

    def __init__(self, model_path: str, max_seq_length: int = 2048, device: str = "cuda"):
        self.device = torch.device(device if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

        config_path = os.path.join(model_path, "training_config.json")
        with open(config_path) as f:
            train_cfg = json.load(f)

        self.model = StructFuseEncoder(
            model_name=train_cfg.get("model_name", "Qwen/Qwen2.5-Coder-3B"),
            proj_dim=train_cfg.get("proj_dim", 256),
            use_projection=True,
            use_lora=train_cfg.get("use_lora", False),
            lora_r=train_cfg.get("lora_r", 16),
            lora_alpha=train_cfg.get("lora_r", 16) * 2,
            use_fusion_head=train_cfg.get("use_fusion_head", False),
        )
        state_dict = torch.load(
            os.path.join(model_path, "model.pt"), map_location="cpu", weights_only=True,
        )
        self.model.load_state_dict(state_dict)
        self.model.to(self.device)
        self.model.eval()
        self.max_seq_length = max_seq_length

    @torch.no_grad()
    def encode(self, texts: list[str], batch_size: int = 32) -> np.ndarray:
        all_embeddings = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            encoded = self.tokenizer(
                batch,
                padding=True,
                truncation=True,
                max_length=self.max_seq_length,
                return_tensors="pt",
            ).to(self.device)
            embeddings = self.model.encode(encoded["input_ids"], encoded["attention_mask"])
            all_embeddings.append(embeddings.cpu().numpy())
        return np.concatenate(all_embeddings, axis=0)

    def rank(self, query: str, candidates: list[dict], batch_size: int = 32) -> list[dict]:
        if not candidates:
            return []
        query_emb = self.encode([query], batch_size=1)
        doc_texts = [c.get("content", c.get("path", "")) for c in candidates]
        doc_embs = self.encode(doc_texts, batch_size=batch_size)
        scores = (query_emb @ doc_embs.T).squeeze(0)
        ranked_indices = np.argsort(scores)[::-1]
        results = []
        for idx in ranked_indices:
            results.append({**candidates[idx], "structfuse_score": float(scores[idx])})
        return results


class FusionRanker:
    """Re-ranks by combining BM25 score, data-flow signal, and StructFuse score."""

    def __init__(self, bm25_weight: float = 0.2, df_weight: float = 0.3, sf_weight: float = 0.5):
        self.bm25_weight = bm25_weight
        self.df_weight = df_weight
        self.sf_weight = sf_weight

    def rerank(self, candidates: list[dict], reachable_files: set[str]) -> list[dict]:
        if not candidates:
            return []
        bm25_scores = np.array([c.get("bm25_score", 0.0) for c in candidates])
        sf_scores = np.array([c.get("structfuse_score", 0.0) for c in candidates])

        # Normalize to [0, 1]
        if bm25_scores.max() > bm25_scores.min():
            bm25_norm = (bm25_scores - bm25_scores.min()) / (bm25_scores.max() - bm25_scores.min())
        else:
            bm25_norm = np.zeros_like(bm25_scores)

        if sf_scores.max() > sf_scores.min():
            sf_norm = (sf_scores - sf_scores.min()) / (sf_scores.max() - sf_scores.min())
        else:
            sf_norm = np.zeros_like(sf_scores)

        df_signal = np.array([1.0 if c["path"] in reachable_files else 0.0 for c in candidates])

        fused = self.bm25_weight * bm25_norm + self.df_weight * df_signal + self.sf_weight * sf_norm
        ranked_indices = np.argsort(fused)[::-1]
        results = []
        for idx in ranked_indices:
            results.append({**candidates[idx], "fused_score": float(fused[idx])})
        return results


def compute_metrics(results: list[RetrievalResult], k_values: list[int]) -> dict:
    """Compute Recall@k, MRR, and Structural Precision."""
    metrics: dict = {}
    n = len(results)
    if n == 0:
        return metrics

    for k in k_values:
        hits = 0
        for r in results:
            pred_set = set(r.predicted_files[:k])
            if pred_set & set(r.gold_files):
                hits += 1
        metrics[f"recall@{k}"] = hits / n

    # MRR
    mrr_sum = 0.0
    for r in results:
        gold_set = set(r.gold_files)
        for rank, pred in enumerate(r.predicted_files, 1):
            if pred in gold_set:
                mrr_sum += 1.0 / rank
                break
    metrics["mrr"] = mrr_sum / n

    return metrics


def compute_structural_precision(results: list[RetrievalResult], reachable_map: dict[str, set[str]]) -> float:
    """Fraction of retrieved files that are data-flow reachable from the query context."""
    total = 0
    reachable_count = 0
    for r in results:
        reachable = reachable_map.get(r.instance_id, set())
        if not reachable:
            continue
        for f in r.predicted_files[:10]:
            total += 1
            if f in reachable:
                reachable_count += 1
    return reachable_count / total if total > 0 else 0.0


def evaluate_single_model(
    model_path: str,
    instances: list[RetrievalInstance],
    args: argparse.Namespace,
    k_values: list[int],
) -> dict:
    """Run full evaluation pipeline for one model checkpoint."""
    bm25_only = args.bm25_only
    use_dataflow = args.use_dataflow_filter and args.dataflow_dir
    use_fusion = args.use_fusion

    retriever = None
    if not bm25_only:
        print(f"Loading StructFuse model from {model_path}")
        retriever = StructFuseRetriever(model_path, max_seq_length=args.max_seq_length)

    fusion = FusionRanker() if use_fusion else None
    reachable_map: dict[str, set[str]] = {}
    results: list[RetrievalResult] = []

    for inst in tqdm(instances, desc=f"Evaluating {os.path.basename(model_path)}"):
        candidates = collect_candidate_files(inst.repo_path)
        if not candidates:
            results.append(RetrievalResult(
                instance_id=inst.instance_id,
                query=inst.query,
                gold_files=inst.gold_files,
                predicted_files=[],
                scores=[],
            ))
            continue

        # Stage 1: BM25 coarse retrieval
        bm25_results = bm25_retrieve(inst.query, candidates, top_k=30)

        # Stage 2: Data-flow filter
        reachable = set()
        if use_dataflow:
            reachable = load_dataflow_reachability(args.dataflow_dir, inst.instance_id)
            reachable_map[inst.instance_id] = reachable
            if reachable:
                filtered = [c for c in bm25_results if c["path"] in reachable]
                # Keep BM25 results as fallback if filter is too aggressive
                if len(filtered) >= 3:
                    bm25_results = filtered

        if bm25_only:
            ranked = bm25_results
        else:
            # Stage 3: StructFuse bi-encoder re-ranking
            ranked = retriever.rank(inst.query, bm25_results, batch_size=args.batch_size)

            # Stage 4: Fusion re-ranking
            if use_fusion and fusion:
                for i, r in enumerate(ranked):
                    for b in bm25_results:
                        if b["path"] == r["path"]:
                            ranked[i]["bm25_score"] = b.get("bm25_score", 0.0)
                            break
                ranked = fusion.rerank(ranked, reachable)

        predicted_files = [r["path"] for r in ranked]
        score_key = "fused_score" if use_fusion else ("structfuse_score" if not bm25_only else "bm25_score")
        scores = [r.get(score_key, 0.0) for r in ranked]

        results.append(RetrievalResult(
            instance_id=inst.instance_id,
            query=inst.query[:200],
            gold_files=inst.gold_files,
            predicted_files=predicted_files,
            scores=scores,
        ))

    metrics = compute_metrics(results, k_values)
    if reachable_map:
        metrics["structural_precision"] = compute_structural_precision(results, reachable_map)

    return {
        "model": model_path,
        "num_instances": len(instances),
        "metrics": metrics,
        "per_instance": [
            {
                "instance_id": r.instance_id,
                "gold_files": r.gold_files,
                "predicted_top10": r.predicted_files[:10],
                "scores_top10": r.scores[:10],
            }
            for r in results
        ],
    }


def main():
    parser = argparse.ArgumentParser(description="StructFuse Retrieval Evaluation")
    parser.add_argument("--model-path", type=str, required=True,
                        help="Checkpoint path(s), comma-separated for multi-model comparison")
    parser.add_argument("--test-file", type=str, required=True,
                        help="JSON Lines test file")
    parser.add_argument("--dataflow-dir", type=str, default=None,
                        help="CodeQL data-flow output directory")
    parser.add_argument("--output-file", type=str, default="retrieval_results.json",
                        help="Output JSON file")
    parser.add_argument("--top-k", type=str, default="1,5,10",
                        help="Comma-separated k values for Recall@k")
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--use-fusion", action="store_true",
                        help="Enable fusion head re-ranking")
    parser.add_argument("--use-dataflow-filter", action="store_true",
                        help="Filter candidates by data-flow reachability")
    parser.add_argument("--max-seq-length", type=int, default=2048)
    parser.add_argument("--dataset", type=str, default="custom",
                        choices=["swebench_lite", "repobench", "custom"])
    parser.add_argument("--bm25-only", action="store_true",
                        help="BM25 baseline mode (no model)")
    args = parser.parse_args()

    k_values = [int(k) for k in args.top_k.split(",")]
    model_paths = [p.strip() for p in args.model_path.split(",")]

    print(f"Dataset: {args.dataset}")
    print(f"Test file: {args.test_file}")
    print(f"K values: {k_values}")

    instances = load_test_data(args.test_file, args.dataset)
    print(f"Loaded {len(instances)} test instances")

    all_results = []
    for mp in model_paths:
        result = evaluate_single_model(mp, instances, args, k_values)
        all_results.append(result)
        print(f"\n{'='*60}")
        print(f"Model: {mp}")
        for metric_name, value in result["metrics"].items():
            print(f"  {metric_name}: {value:.4f}")

    output = {
        "config": {
            "dataset": args.dataset,
            "test_file": args.test_file,
            "k_values": k_values,
            "use_fusion": args.use_fusion,
            "use_dataflow_filter": args.use_dataflow_filter,
            "bm25_only": args.bm25_only,
        },
        "results": all_results,
    }

    os.makedirs(os.path.dirname(os.path.abspath(args.output_file)), exist_ok=True)
    with open(args.output_file, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {args.output_file}")


if __name__ == "__main__":
    main()
