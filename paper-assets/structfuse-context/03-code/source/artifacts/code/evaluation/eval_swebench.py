import os
os.environ["CUDA_VISIBLE_DEVICES"] = "4"

"""
StructFuse SWE-bench End-to-End Evaluation Script

Pipeline: issue description -> StructFuse context retrieval -> Qwen3.6-27B patch
generation (via vLLM) -> SWE-bench harness evaluation.

Input:
  - Trained StructFuse checkpoint
  - vLLM serving endpoint with Qwen3.6-27B loaded
  - SWE-bench dataset split (lite/verified/pro)

Output:
  - Per-instance results: retrieved files, generated patch, test outcomes
  - Summary: Pass@1, avg tokens used, avg retrieval recall

Dependencies: transformers, torch, datasets, requests, rank_bm25
"""

import argparse
import json
import os
import subprocess
import tempfile
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import requests
from datasets import load_dataset
from tqdm import tqdm

from eval_retrieval import (
    StructFuseRetriever,
    FusionRanker,
    bm25_retrieve,
    collect_candidate_files,
    load_dataflow_reachability,
)


@dataclass
class SWEBenchInstance:
    instance_id: str
    repo: str
    base_commit: str
    problem_statement: str
    patch: str  # gold patch for reference
    test_patch: str
    gold_files: list[str] = field(default_factory=list)


@dataclass
class EvalResult:
    instance_id: str
    status: str  # "pass", "fail", "error", "timeout", "skipped"
    retrieved_files: list[str] = field(default_factory=list)
    retrieval_recall: float = 0.0
    generated_patch: str = ""
    tokens_used: int = 0
    error_message: str = ""
    duration_seconds: float = 0.0


def load_swebench_instances(split: str) -> list[SWEBenchInstance]:
    """Load SWE-bench instances from HuggingFace datasets."""
    split_map = {
        "lite": "princeton-nlp/SWE-bench_Lite",
        "verified": "princeton-nlp/SWE-bench_Verified",
        "pro": "princeton-nlp/SWE-bench",
    }
    dataset_name = split_map.get(split, split_map["lite"])
    ds = load_dataset(dataset_name, split="test")

    instances = []
    for item in ds:
        gold_files = extract_gold_files_from_patch(item.get("patch", ""))
        instances.append(SWEBenchInstance(
            instance_id=item["instance_id"],
            repo=item["repo"],
            base_commit=item["base_commit"],
            problem_statement=item["problem_statement"],
            patch=item.get("patch", ""),
            test_patch=item.get("test_patch", ""),
            gold_files=gold_files,
        ))
    return instances


def extract_gold_files_from_patch(patch: str) -> list[str]:
    """Extract modified file paths from a unified diff patch."""
    files = []
    for line in patch.split("\n"):
        if line.startswith("--- a/") or line.startswith("+++ b/"):
            fpath = line.split("/", 1)[1] if "/" in line else ""
            if fpath and fpath != "/dev/null" and fpath not in files:
                files.append(fpath)
    return files


def setup_repo(repo: str, base_commit: str, workspace: str) -> str:
    """Clone and checkout the target repo at the base commit."""
    repo_url = f"https://github.com/{repo}.git"
    repo_dir = os.path.join(workspace, repo.replace("/", "__"))

    if not os.path.exists(repo_dir):
        subprocess.run(
            ["git", "clone", "--depth", "200", repo_url, repo_dir],
            capture_output=True, timeout=120,
        )
    subprocess.run(
        ["git", "checkout", base_commit],
        cwd=repo_dir, capture_output=True, timeout=30,
    )
    return repo_dir


def build_prompt(problem_statement: str, retrieved_context: list[dict], max_tokens: int) -> str:
    """Construct the LLM prompt with issue description and retrieved code context."""
    header = (
        "You are an expert software engineer. Given the following GitHub issue and "
        "relevant code context, generate a minimal unified diff patch that resolves the issue.\n\n"
        f"## Issue\n{problem_statement}\n\n"
        "## Relevant Code\n"
    )

    # Budget token estimation: ~4 chars per token
    budget = (max_tokens - len(header) // 4) * 4
    context_parts = []
    used = 0

    for item in retrieved_context:
        entry = f"\n### {item['path']}\n```python\n{item['content']}\n```\n"
        entry_len = len(entry)
        if used + entry_len > budget:
            remaining = budget - used
            if remaining > 200:
                truncated_content = item["content"][: remaining - 100]
                entry = f"\n### {item['path']} (truncated)\n```python\n{truncated_content}\n```\n"
                context_parts.append(entry)
            break
        context_parts.append(entry)
        used += entry_len

    footer = (
        "\n## Instructions\n"
        "Generate a unified diff patch (```diff ... ```) that fixes the issue. "
        "Only modify the files shown above. Be minimal and precise.\n"
    )

    return header + "".join(context_parts) + footer


def call_vllm(
    prompt: str,
    endpoint: str,
    model: str,
    max_tokens: int,
    temperature: float = 0.0,
) -> tuple[str, int]:
    """Call vLLM OpenAI-compatible API and return (response_text, tokens_used)."""
    url = f"{endpoint}/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stop": ["```\n\n"],
    }
    resp = requests.post(url, json=payload, timeout=300)
    resp.raise_for_status()
    data = resp.json()

    text = data["choices"][0]["message"]["content"]
    tokens = data.get("usage", {}).get("total_tokens", 0)
    return text, tokens


def extract_patch_from_response(response: str) -> str:
    """Extract unified diff patch from LLM response."""
    lines = response.split("\n")
    in_diff = False
    patch_lines = []

    for line in lines:
        if line.strip().startswith("```diff"):
            in_diff = True
            continue
        if in_diff and line.strip() == "```":
            break
        if in_diff:
            patch_lines.append(line)

    if not patch_lines:
        # Fallback: look for diff-like content directly
        for i, line in enumerate(lines):
            if line.startswith("---") or line.startswith("diff --git"):
                patch_lines = lines[i:]
                break

    return "\n".join(patch_lines)


def apply_patch(repo_dir: str, patch: str) -> bool:
    """Apply a unified diff patch to the repo. Returns True on success."""
    if not patch.strip():
        return False
    try:
        result = subprocess.run(
            ["git", "apply", "--check", "-"],
            input=patch, text=True, capture_output=True,
            cwd=repo_dir, timeout=10,
        )
        if result.returncode != 0:
            return False
        subprocess.run(
            ["git", "apply", "-"],
            input=patch, text=True, capture_output=True,
            cwd=repo_dir, timeout=10,
        )
        return True
    except Exception:
        return False


def compute_retrieval_recall(retrieved_files: list[str], gold_files: list[str], k: int = 10) -> float:
    if not gold_files:
        return 0.0
    retrieved_set = set(retrieved_files[:k])
    hits = len(retrieved_set & set(gold_files))
    return hits / len(gold_files)


def load_completed_instances(output_dir: str) -> set[str]:
    """Load instance IDs that have already been evaluated (for resume support)."""
    results_file = os.path.join(output_dir, "results.jsonl")
    completed = set()
    if os.path.exists(results_file):
        with open(results_file) as f:
            for line in f:
                try:
                    data = json.loads(line)
                    completed.add(data["instance_id"])
                except (json.JSONDecodeError, KeyError):
                    continue
    return completed


def save_instance_result(output_dir: str, result: EvalResult):
    """Append a single instance result to the results file."""
    results_file = os.path.join(output_dir, "results.jsonl")
    with open(results_file, "a") as f:
        f.write(json.dumps({
            "instance_id": result.instance_id,
            "status": result.status,
            "retrieved_files": result.retrieved_files[:20],
            "retrieval_recall": result.retrieval_recall,
            "generated_patch": result.generated_patch,
            "tokens_used": result.tokens_used,
            "error_message": result.error_message,
            "duration_seconds": result.duration_seconds,
        }, ensure_ascii=False) + "\n")


def evaluate_instance(
    instance: SWEBenchInstance,
    retriever: StructFuseRetriever | None,
    args: argparse.Namespace,
    workspace: str,
) -> EvalResult:
    """Evaluate a single SWE-bench instance end-to-end."""
    start = time.time()

    try:
        # Step 1: Setup repo
        repo_dir = setup_repo(instance.repo, instance.base_commit, workspace)

        # Step 2: StructFuse retrieval
        candidates = collect_candidate_files(repo_dir)
        bm25_results = bm25_retrieve(instance.problem_statement, candidates, top_k=30)

        reachable = set()
        if args.dataflow_dir:
            reachable = load_dataflow_reachability(args.dataflow_dir, instance.instance_id)
            if reachable:
                filtered = [c for c in bm25_results if c["path"] in reachable]
                if len(filtered) >= 3:
                    bm25_results = filtered

        if retriever:
            ranked = retriever.rank(instance.problem_statement, bm25_results, batch_size=16)
        else:
            ranked = bm25_results

        if args.use_fusion and reachable:
            fusion = FusionRanker()
            for i, r in enumerate(ranked):
                for b in bm25_results:
                    if b["path"] == r["path"]:
                        ranked[i]["bm25_score"] = b.get("bm25_score", 0.0)
                        break
            ranked = fusion.rerank(ranked, reachable)

        retrieved_files = [r["path"] for r in ranked[:10]]
        recall = compute_retrieval_recall(retrieved_files, instance.gold_files)

        # Step 3: Build prompt and generate patch
        prompt = build_prompt(instance.problem_statement, ranked[:10], args.max_context_tokens)
        response, tokens = call_vllm(
            prompt, args.llm_endpoint, args.llm_model, args.max_generation_tokens
        )
        patch = extract_patch_from_response(response)

        # Step 4: Apply and test
        applied = apply_patch(repo_dir, patch)
        if not applied:
            return EvalResult(
                instance_id=instance.instance_id,
                status="fail",
                retrieved_files=retrieved_files,
                retrieval_recall=recall,
                generated_patch=patch,
                tokens_used=tokens,
                error_message="patch_apply_failed",
                duration_seconds=time.time() - start,
            )

        # Step 5: Run tests (framework — actual SWE-bench harness integration TBD)
        # The SWE-bench harness runs instance-specific tests. This is a placeholder
        # that will be replaced with the actual harness invocation.
        status = run_swebench_tests(repo_dir, instance)

        return EvalResult(
            instance_id=instance.instance_id,
            status=status,
            retrieved_files=retrieved_files,
            retrieval_recall=recall,
            generated_patch=patch,
            tokens_used=tokens,
            duration_seconds=time.time() - start,
        )

    except requests.exceptions.Timeout:
        return EvalResult(
            instance_id=instance.instance_id,
            status="timeout",
            error_message="vllm_timeout",
            duration_seconds=time.time() - start,
        )
    except Exception as e:
        return EvalResult(
            instance_id=instance.instance_id,
            status="error",
            error_message=f"{type(e).__name__}: {e}",
            duration_seconds=time.time() - start,
        )


def run_swebench_tests(repo_dir: str, instance: SWEBenchInstance) -> str:
    """
    Run SWE-bench evaluation harness for a single instance.

    This is a framework placeholder. In production, this will invoke the SWE-bench
    harness (`swebench.harness.run_evaluation`) or apply the test patch and run
    pytest on the target test files. Returns "pass" or "fail".
    """
    # TODO: integrate with swebench.harness.run_evaluation or direct pytest invocation
    # For now, check if the test patch can at least be applied
    if instance.test_patch:
        result = subprocess.run(
            ["git", "apply", "--check", "-"],
            input=instance.test_patch, text=True, capture_output=True,
            cwd=repo_dir, timeout=10,
        )
        if result.returncode == 0:
            subprocess.run(
                ["git", "apply", "-"],
                input=instance.test_patch, text=True, capture_output=True,
                cwd=repo_dir, timeout=10,
            )
    # Placeholder: actual test execution TBD
    return "pending"


def generate_summary(output_dir: str) -> dict:
    """Generate summary statistics from all instance results."""
    results_file = os.path.join(output_dir, "results.jsonl")
    if not os.path.exists(results_file):
        return {}

    results = []
    with open(results_file) as f:
        for line in f:
            try:
                results.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    total = len(results)
    if total == 0:
        return {}

    status_counts = {}
    for r in results:
        s = r["status"]
        status_counts[s] = status_counts.get(s, 0) + 1

    pass_count = status_counts.get("pass", 0)
    recalls = [r.get("retrieval_recall", 0.0) for r in results]
    tokens = [r.get("tokens_used", 0) for r in results if r.get("tokens_used", 0) > 0]
    durations = [r.get("duration_seconds", 0.0) for r in results if r.get("duration_seconds", 0) > 0]

    summary = {
        "total_instances": total,
        "status_counts": status_counts,
        "pass_at_1": pass_count / total if total > 0 else 0.0,
        "avg_retrieval_recall": float(np.mean(recalls)) if recalls else 0.0,
        "avg_tokens_used": float(np.mean(tokens)) if tokens else 0.0,
        "avg_duration_seconds": float(np.mean(durations)) if durations else 0.0,
        "median_duration_seconds": float(np.median(durations)) if durations else 0.0,
    }
    return summary


def main():
    parser = argparse.ArgumentParser(description="StructFuse SWE-bench End-to-End Evaluation")
    parser.add_argument("--model-path", type=str, required=True,
                        help="StructFuse checkpoint path")
    parser.add_argument("--llm-endpoint", type=str, default="http://localhost:8000/v1",
                        help="vLLM serving endpoint URL")
    parser.add_argument("--llm-model", type=str, default="Qwen/Qwen3.6-27B",
                        help="LLM model name for vLLM")
    parser.add_argument("--swebench-split", type=str, default="lite",
                        choices=["lite", "verified", "pro"])
    parser.add_argument("--output-dir", type=str, default="swebench_results",
                        help="Output directory for results")
    parser.add_argument("--max-context-tokens", type=int, default=16000)
    parser.add_argument("--max-generation-tokens", type=int, default=4096)
    parser.add_argument("--num-workers", type=int, default=4,
                        help="Parallel evaluation workers")
    parser.add_argument("--timeout-per-instance", type=int, default=600)
    parser.add_argument("--dataflow-dir", type=str, default=None)
    parser.add_argument("--use-fusion", action="store_true")
    parser.add_argument("--agent-turns", type=int, default=50,
                        help="Max agent interaction turns (reserved for future agentic mode)")
    parser.add_argument("--bm25-only", action="store_true",
                        help="Use BM25 retrieval only (no StructFuse model)")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    workspace = os.path.join(args.output_dir, "repos")
    os.makedirs(workspace, exist_ok=True)

    print(f"Split: {args.swebench_split}")
    print(f"LLM endpoint: {args.llm_endpoint}")
    print(f"LLM model: {args.llm_model}")

    # Load instances
    print("Loading SWE-bench instances...")
    instances = load_swebench_instances(args.swebench_split)
    print(f"Loaded {len(instances)} instances")

    # Resume support
    completed = load_completed_instances(args.output_dir)
    remaining = [inst for inst in instances if inst.instance_id not in completed]
    if completed:
        print(f"Resuming: {len(completed)} done, {len(remaining)} remaining")

    # Load retriever
    retriever = None
    if not args.bm25_only:
        print(f"Loading StructFuse model from {args.model_path}")
        retriever = StructFuseRetriever(args.model_path, max_seq_length=2048)

    # Evaluate
    # Note: ThreadPoolExecutor for I/O-bound work (git clone, vLLM calls).
    # GPU inference in the retriever is sequential due to single-GPU constraint.
    for inst in tqdm(remaining, desc="SWE-bench evaluation"):
        result = evaluate_instance(inst, retriever, args, workspace)
        save_instance_result(args.output_dir, result)

    # Summary
    summary = generate_summary(args.output_dir)
    summary_file = os.path.join(args.output_dir, "summary.json")
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'='*60}")
    print("Summary:")
    print(f"  Total instances: {summary.get('total_instances', 0)}")
    print(f"  Pass@1: {summary.get('pass_at_1', 0.0):.4f}")
    print(f"  Avg retrieval recall: {summary.get('avg_retrieval_recall', 0.0):.4f}")
    print(f"  Avg tokens used: {summary.get('avg_tokens_used', 0.0):.0f}")
    print(f"  Status: {summary.get('status_counts', {})}")
    print(f"\nResults saved to {args.output_dir}/")


if __name__ == "__main__":
    main()
