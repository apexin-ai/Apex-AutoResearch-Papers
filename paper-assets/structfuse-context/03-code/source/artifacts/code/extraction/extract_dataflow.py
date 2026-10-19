"""
StructFuse Stage 1: Data-flow extraction pipeline.

For each repo, runs CodeQL 2-phase analysis (call graph + bounded data-flow),
falls back to Beniget for intra-file def-use when CodeQL times out or has
insufficient coverage. Outputs JSON Lines with per-instance features.

Input:  JSON file with list of {repo_path, buggy_file, buggy_function}
Output: JSONL files in output_dir, one per repo, plus merged all.jsonl

Dependencies: codeql CLI on PATH, beniget (pip install beniget)
"""

import argparse
import json
import logging
import os
import subprocess
import tempfile
import time
from multiprocessing import Pool
from pathlib import Path
from typing import Any

import ast

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger("extract_dataflow")

SCRIPT_DIR = Path(__file__).resolve().parent
CALL_GRAPH_QL = SCRIPT_DIR / "codeql_queries" / "call_graph.ql"
DATAFLOW_QL = SCRIPT_DIR / "codeql_queries" / "bounded_dataflow.ql"


# ---------------------------------------------------------------------------
# CodeQL helpers
# ---------------------------------------------------------------------------

def create_codeql_database(repo_path: str, db_path: str, timeout: int) -> bool:
    """Create a CodeQL database for a Python repo. Returns True on success."""
    cmd = [
        "codeql", "database", "create", db_path,
        "--language=python",
        "--source-root", repo_path,
        "--overwrite",
        "--threads=0",  # use all available cores
    ]
    try:
        subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout, check=True
        )
        return True
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
        log.warning("CodeQL database creation failed for %s: %s", repo_path, e)
        return False


def run_codeql_query(
    db_path: str,
    query_path: str,
    output_csv: str,
    buggy_function: str,
    buggy_file: str,
    timeout: int,
    ram: int,
) -> bool:
    """Run a CodeQL query with external predicates. Returns True on success."""
    output_bqrs = output_csv + ".bqrs"
    tmpdir = os.path.dirname(output_csv)
    func_csv = os.path.join(tmpdir, "ext_func.csv")
    file_csv = os.path.join(tmpdir, "ext_file.csv")
    with open(func_csv, "w") as f:
        f.write(f'"{buggy_function}"\n')
    with open(file_csv, "w") as f:
        f.write(f'"{buggy_file}"\n')
    run_cmd = [
        "codeql", "query", "run",
        "--database", db_path,
        "--output", output_bqrs,
        f"--ram={ram}",
        f"--timeout={timeout}",
        f"--external=buggyFunctionName={func_csv}",
        f"--external=buggyFileName={file_csv}",
        "--threads=0",
        query_path,
    ]
    decode_cmd = [
        "codeql", "bqrs", "decode",
        "--format=csv",
        "--output", output_csv,
        output_bqrs,
    ]
    try:
        subprocess.run(
            run_cmd, capture_output=True, text=True, timeout=timeout + 60, check=True
        )
        subprocess.run(
            decode_cmd, capture_output=True, text=True, timeout=60, check=True
        )
        return True
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
        log.warning("CodeQL query failed (%s): %s", query_path, e)
        return False


def parse_call_graph_csv(csv_path: str) -> list[dict]:
    """Parse call_graph.ql CSV output into list of function records."""
    results = []
    if not os.path.exists(csv_path):
        return results
    with open(csv_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("target_func"):
                continue
            parts = [p.strip().strip('"') for p in line.split(",")]
            if len(parts) >= 6:
                results.append({
                    "target_func": parts[0],
                    "hop_distance": int(parts[1]),
                    "direction": parts[2],
                    "file_path": parts[3],
                    "start_line": int(parts[4]),
                    "end_line": int(parts[5]),
                })
    return results


def parse_dataflow_csv(csv_path: str) -> list[dict]:
    """Parse bounded_dataflow.ql CSV output into list of flow records."""
    results = []
    if not os.path.exists(csv_path):
        return results
    with open(csv_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("source_file"):
                continue
            parts = [p.strip().strip('"') for p in line.split(",")]
            if len(parts) >= 7:
                results.append({
                    "source_file": parts[0],
                    "source_func": parts[1],
                    "source_line": int(parts[2]) if parts[2].isdigit() else 0,
                    "sink_file": parts[3],
                    "sink_func": parts[4],
                    "sink_line": int(parts[5]) if parts[5].isdigit() else 0,
                    "path_length": int(parts[6]) if parts[6].isdigit() else 1,
                })
    return results


# ---------------------------------------------------------------------------
# Path normalization
# ---------------------------------------------------------------------------

def resolve_file_in_repo(repo_path: str, target_file: str) -> str | None:
    """Resolve a file path against a repo, handling src/ prefix mismatches."""
    candidate = os.path.join(repo_path, target_file)
    if os.path.exists(candidate):
        return target_file

    basename = os.path.basename(target_file)
    best_match = None
    best_suffix_len = 0
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
        for f in files:
            if f == basename:
                rel = os.path.relpath(os.path.join(root, f), repo_path)
                if rel.endswith(target_file):
                    return rel
                suffix_len = _common_suffix_length(rel, target_file)
                if suffix_len > best_suffix_len:
                    best_suffix_len = suffix_len
                    best_match = rel
    return best_match


def _common_suffix_length(a: str, b: str) -> int:
    a_parts = a.split("/")
    b_parts = b.split("/")
    count = 0
    for ap, bp in zip(reversed(a_parts), reversed(b_parts)):
        if ap == bp:
            count += 1
        else:
            break
    return count


def normalize_path(path: str, all_py_files: list[str]) -> str:
    """Map a path to its canonical form in all_py_files via suffix matching."""
    if path in all_py_files:
        return path
    for f in all_py_files:
        if f.endswith("/" + path) or path.endswith("/" + f):
            return f
    basename = os.path.basename(path)
    candidates = [f for f in all_py_files if os.path.basename(f) == basename]
    if len(candidates) == 1:
        return candidates[0]
    path_parts = path.split("/")
    best, best_score = path, 0
    for f in candidates:
        score = _common_suffix_length(f, path)
        if score > best_score:
            best_score = score
            best = f
    return best if best_score > 0 else path


# ---------------------------------------------------------------------------
# Beniget fallback
# ---------------------------------------------------------------------------

def beniget_extract(repo_path: str, buggy_file: str, buggy_function: str) -> dict:
    """
    Intra-file def-use chain extraction via beniget.
    Returns a dict with call_graph (empty) and dataflow_paths (intra-file only).
    """
    try:
        import beniget
    except ImportError:
        log.error("beniget not installed; pip install beniget")
        return {"call_graph": [], "dataflow_paths": []}

    resolved = resolve_file_in_repo(repo_path, buggy_file)
    if resolved:
        buggy_file = resolved
    target_path = os.path.join(repo_path, buggy_file)
    if not os.path.exists(target_path):
        log.warning("Buggy file not found: %s", target_path)
        return {"call_graph": [], "dataflow_paths": []}

    try:
        with open(target_path) as f:
            source = f.read()
        tree = ast.parse(source, filename=buggy_file)
    except SyntaxError:
        log.warning("SyntaxError parsing %s", target_path)
        return {"call_graph": [], "dataflow_paths": []}

    duc = beniget.DefUseChains()
    duc.visit(tree)

    # Build def-use edges within the buggy file
    dataflow_paths = []
    buggy_func_node = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name == buggy_function:
                buggy_func_node = node
                break

    if buggy_func_node is None:
        log.warning("Function %s not found in %s", buggy_function, buggy_file)
        return {"call_graph": [], "dataflow_paths": []}

    # Collect all names defined in the buggy function and trace their uses
    for node in ast.walk(buggy_func_node):
        if isinstance(node, ast.Name):
            try:
                chain = duc.chains[node]
            except KeyError:
                continue
            for user in chain.users():
                user_node = user.node
                dataflow_paths.append({
                    "source_file": buggy_file,
                    "source_func": buggy_function,
                    "source_line": getattr(node, "lineno", 0),
                    "sink_file": buggy_file,
                    "sink_func": _enclosing_function_name(tree, user_node),
                    "sink_line": getattr(user_node, "lineno", 0),
                    "path_length": 1,
                })

    # Deduplicate
    seen = set()
    unique = []
    for p in dataflow_paths:
        key = (p["source_func"], p["source_line"], p["sink_func"], p["sink_line"])
        if key not in seen:
            seen.add(key)
            unique.append(p)

    return {"call_graph": [], "dataflow_paths": unique}


def _enclosing_function_name(tree: ast.AST, node: ast.AST) -> str:
    """Find the name of the function enclosing `node`, or '<module>'."""
    # Build parent map
    parent_map: dict[ast.AST, ast.AST] = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            parent_map[child] = parent
    current = node
    while current in parent_map:
        current = parent_map[current]
        if isinstance(current, (ast.FunctionDef, ast.AsyncFunctionDef)):
            return current.name
    return "<module>"


# ---------------------------------------------------------------------------
# Per-repo processing
# ---------------------------------------------------------------------------

def process_repo(args_tuple: tuple) -> dict[str, Any] | None:
    """
    Process a single repo: CodeQL extraction with Beniget fallback.
    Called by multiprocessing pool.
    """
    instance, codeql_timeout, codeql_ram, min_reachable_files = args_tuple
    repo_path = instance["repo_path"]
    buggy_file = instance["buggy_file"]
    buggy_function = instance["buggy_function"]
    instance_id = instance.get("instance_id", os.path.basename(repo_path))

    log.info("Processing %s: %s in %s", instance_id, buggy_function, buggy_file)
    start = time.time()

    result = {
        "instance_id": instance_id,
        "repo_path": repo_path,
        "buggy_file": buggy_file,
        "buggy_function": buggy_function,
        "inter_procedural": False,
        "extraction_method": "none",
        "call_graph": [],
        "dataflow_paths": [],
        "extraction_time_s": 0.0,
        "error": None,
    }

    with tempfile.TemporaryDirectory(prefix="structfuse_") as tmpdir:
        db_path = os.path.join(tmpdir, "codeql_db")
        cg_csv = os.path.join(tmpdir, "call_graph.csv")
        df_csv = os.path.join(tmpdir, "dataflow.csv")

        # Phase 1a: CodeQL database + call graph
        codeql_ok = False
        if create_codeql_database(repo_path, db_path, timeout=codeql_timeout):
            if run_codeql_query(
                db_path, str(CALL_GRAPH_QL), cg_csv,
                buggy_function, buggy_file, codeql_timeout, codeql_ram,
            ):
                call_graph = parse_call_graph_csv(cg_csv)
                reachable_files = len({r["file_path"] for r in call_graph})

                if reachable_files >= min_reachable_files:
                    # Phase 1b: bounded data-flow
                    if run_codeql_query(
                        db_path, str(DATAFLOW_QL), df_csv,
                        buggy_function, buggy_file, codeql_timeout, codeql_ram,
                    ):
                        dataflow_paths = parse_dataflow_csv(df_csv)
                        result["call_graph"] = call_graph
                        result["dataflow_paths"] = dataflow_paths
                        result["inter_procedural"] = True
                        result["extraction_method"] = "codeql"
                        codeql_ok = True
                    else:
                        log.warning(
                            "%s: data-flow query failed/timed out, falling back",
                            instance_id,
                        )
                else:
                    log.info(
                        "%s: only %d reachable files (min %d), falling back",
                        instance_id, reachable_files, min_reachable_files,
                    )

        # Beniget fallback
        if not codeql_ok:
            log.info("%s: using Beniget fallback", instance_id)
            beniget_result = beniget_extract(repo_path, buggy_file, buggy_function)
            result["call_graph"] = beniget_result["call_graph"]
            result["dataflow_paths"] = beniget_result["dataflow_paths"]
            result["inter_procedural"] = False
            result["extraction_method"] = "beniget"

    result["extraction_time_s"] = round(time.time() - start, 2)
    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="StructFuse Stage 1: extract data-flow features per repo"
    )
    parser.add_argument("--repos-file", required=True, help="JSON list of instances")
    parser.add_argument("--output-dir", required=True, help="Output directory for JSONL")
    parser.add_argument("--num-workers", type=int, default=4)
    parser.add_argument("--codeql-timeout", type=int, default=300, help="Seconds")
    parser.add_argument("--codeql-ram", type=int, default=8192, help="MB")
    parser.add_argument("--min-reachable-files", type=int, default=5)
    args = parser.parse_args()

    with open(args.repos_file) as f:
        instances = json.load(f)
    log.info("Loaded %d instances", len(instances))

    os.makedirs(args.output_dir, exist_ok=True)

    task_args = [
        (inst, args.codeql_timeout, args.codeql_ram, args.min_reachable_files)
        for inst in instances
    ]

    results: list[dict] = []
    if args.num_workers <= 1:
        for ta in task_args:
            r = process_repo(ta)
            if r:
                results.append(r)
    else:
        with Pool(processes=args.num_workers) as pool:
            for r in pool.imap_unordered(process_repo, task_args):
                if r:
                    results.append(r)

    # Write per-instance JSONL
    merged_path = os.path.join(args.output_dir, "all.jsonl")
    with open(merged_path, "w") as fout:
        for r in results:
            fout.write(json.dumps(r, ensure_ascii=False) + "\n")

    # Statistics
    total = len(results)
    codeql_count = sum(1 for r in results if r["extraction_method"] == "codeql")
    beniget_count = sum(1 for r in results if r["extraction_method"] == "beniget")
    failed_count = sum(1 for r in results if r["extraction_method"] == "none")
    avg_time = sum(r["extraction_time_s"] for r in results) / max(total, 1)
    inter_proc = sum(1 for r in results if r["inter_procedural"])

    log.info("=" * 60)
    log.info("Extraction complete: %d instances", total)
    log.info("  CodeQL success:  %d (%.1f%%)", codeql_count, 100 * codeql_count / max(total, 1))
    log.info("  Beniget fallback:%d (%.1f%%)", beniget_count, 100 * beniget_count / max(total, 1))
    log.info("  Failed:          %d (%.1f%%)", failed_count, 100 * failed_count / max(total, 1))
    log.info("  Inter-procedural:%d (%.1f%%)", inter_proc, 100 * inter_proc / max(total, 1))
    log.info("  Avg time/repo:   %.1fs", avg_time)
    log.info("  Output: %s", merged_path)


if __name__ == "__main__":
    main()
