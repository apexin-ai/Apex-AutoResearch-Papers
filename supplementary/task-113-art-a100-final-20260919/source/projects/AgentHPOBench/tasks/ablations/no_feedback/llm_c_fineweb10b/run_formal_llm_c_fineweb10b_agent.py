#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import time
from pathlib import Path
from typing import Any

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _budget_agent_common import (
    AGENT_LABEL,
    MODEL_PATH,
    RESULT_FILE_AGENT_NAME,
    ROOT,
    copy_result_alias,
    decide_config,
    dump_json,
    load_manifest_record,
    maybe_dry_run,
    result_root,
    run_cmd,
    utc_now,
)


TASK_ID = "llm_c_fineweb10b"
RESULT_DIRNAME = "llm_c_fineweb10b"
REPO_DIR = ROOT / "repositories/llm.c"
BASE_CONFIG = {"learning_rate": 0.0006, "weight_decay": 0.1}
SEARCH_SPACE = {
    "learning_rate": [0.0004, 0.0006, 0.0008, 0.0009, 0.0010],
    "weight_decay": [0.05, 0.1, 0.2],
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "llm_c_fineweb10b", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)

ALIASES = {"lr": "learning_rate", "learning_rate_max": "learning_rate", "wd": "weight_decay"}


def parse_targets() -> list[int]:
    text = os.environ.get("LLMC_CHUNK_TARGETS", "250,500,750,1000")
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def parse_llmc_metrics(log_path: Path, target_step: int | None = None) -> dict[str, Any]:
    text = log_path.read_text(errors="replace") if log_path.exists() else ""
    val_matches = [(int(m.group(1)), float(m.group(2))) for m in re.finditer(r"s:(\d+)\s+tel:([0-9.]+)", text)]
    train_matches = [
        (int(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)))
        for m in re.finditer(r"s:(\d+)\s+trl:([0-9.]+)\s+lr:([0-9.eE+-]+)\s+norm:([0-9.]+)", text)
    ]
    eval_matches = [(int(m.group(1)), float(m.group(2))) for m in re.finditer(r"s:(\d+)\s+eval:([0-9.]+)", text)]
    if target_step is not None:
        vals = [x for x in val_matches if x[0] <= target_step]
        trains = [x for x in train_matches if x[0] <= target_step]
        evals = [x for x in eval_matches if x[0] <= target_step]
    else:
        vals, trains, evals = val_matches, train_matches, eval_matches
    step = vals[-1][0] if vals else (trains[-1][0] if trains else target_step)
    metrics: dict[str, Any] = {"step": step}
    if vals:
        metrics["val_loss"] = vals[-1][1]
    if trains:
        metrics["train_loss"] = trains[-1][1]
        metrics["lr"] = trains[-1][2]
        metrics["grad_norm"] = trains[-1][3]
    if evals:
        metrics["hellaswag_accuracy"] = evals[-1][1]
    if "val_loss" in metrics:
        official = 4.344427
        paper = 3.424958
        metrics["score"] = (official - metrics["val_loss"]) / max(official - paper, 1e-12)
    return metrics


def ensure_binary(env: dict[str, str], log_path: Path) -> None:
    if (REPO_DIR / "train_gpt2cu").exists():
        return
    run_cmd(["make", "train_gpt2cu", "USE_CUDNN=1"], cwd=REPO_DIR, env=env, log_path=log_path)


def run_chunk(out_dir: Path, target: int, config: dict[str, Any], env: dict[str, str], log_path: Path) -> dict[str, Any]:
    cmd_prefix = []
    if os.environ.get("LLMC_USE_MPIRUN", "1") == "1":
        cmd_prefix = ["mpirun", "-np", os.environ.get("LLMC_NPROC", "1")]
    cmd = cmd_prefix + [
        "./train_gpt2cu",
        "-i", "dev/data/fineweb10B/fineweb_train_*.bin",
        "-j", "dev/data/fineweb10B/fineweb_val_*.bin",
        "-o", str(out_dir),
        "-v", os.environ.get("LLMC_VAL_EVERY", "250"),
        "-s", str(target),
        "-g", "144",
        "-h", "1",
        "-b", os.environ.get("LLMC_BATCH_SIZE", "64"),
        "-t", "1024",
        "-d", os.environ.get("LLMC_TOTAL_BATCH_SIZE", "524288"),
        "-r", "0",
        "-z", "1",
        "-c", str(config["weight_decay"]),
        "-l", str(config["learning_rate"]),
        "-q", "0.0",
        "-u", os.environ.get("LLMC_WARMUP_ITERS", "700"),
        "-n", str(target),
        "-x", str(target),
        "-y", os.environ.get("LLMC_WRITE_CHECKPOINTS", "0"),
        "-e", "d12",
    ]
    seconds = run_cmd(cmd, cwd=REPO_DIR, env=env, log_path=log_path, append=True)
    metrics = parse_llmc_metrics(out_dir / "main.log", target)
    return {"target_step": target, "config": dict(config), "metrics": metrics, "seconds": seconds}


def training_log(history: list[dict[str, Any]], manifest: dict[str, Any]) -> str:
    history = history[:1]  # No-feedback: expose only the baseline observation.
    lines = [
        "Task: GPT-2 124M reproduction on FineWeb 10B with llm.c.",
        "Metric: fineweb10B_validation_loss, lower is better.",
        f"Official shortened budget baseline: {manifest.get('official_budget_baseline', 4.344427)} validation loss at 1000 steps.",
        f"Paper anchor: {manifest.get('paper_anchor', 3.424958)} validation loss at 18865 steps.",
        f"Current fixed-budget chunks: {parse_targets()}.",
    ]
    for item in history:
        lines.append(
            f"step={item['target_step']} config={item['config']} "
            f"metrics={item['metrics']}"
        )
    return "\n".join(lines)


def main() -> int:
    if not REPO_DIR.exists():
        raise FileNotFoundError(REPO_DIR)
    manifest = load_manifest_record(TASK_ID)
    targets = parse_targets()
    run_id = os.environ.get("RUN_ID") or f"{TASK_ID}_{AGENT_LABEL.lower().replace('-', '_')}_{targets[-1]}steps_{utc_now().replace(':', '').replace('+', '_')}"
    result_dir = result_root(RESULT_DIRNAME)
    out_dir = REPO_DIR / f"log_gpt2_124M_autorep_agent_{run_id}"
    run_dir = result_dir / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    result_file = result_dir / f"{TASK_ID}_{RESULT_FILE_AGENT_NAME}_results.json"
    maybe_dry_run({"task_id": TASK_ID, "run_id": run_id, "targets": targets, "result_file": str(result_file)})

    env = os.environ.copy()
    env.update(
        {
            "CUDA_VISIBLE_DEVICES": os.environ.get("LLMC_CUDA_VISIBLE_DEVICES", env.get("CUDA_VISIBLE_DEVICES", "1")),
            "OMPI_ALLOW_RUN_AS_ROOT": "1",
            "OMPI_ALLOW_RUN_AS_ROOT_CONFIRM": "1",
        }
    )
    ensure_binary(env, run_dir / "build.log")
    config = dict(BASE_CONFIG)
    history: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []
    started = time.time()
    for index, target in enumerate(targets):
        summary = run_chunk(out_dir, target, config, env, run_dir / f"chunk_{target}.log")
        history.append(summary)
        if index == len(targets) - 1:
            break
        decision = decide_config(
            task_name=TASK_ID,
            current_config=config,
            search_space=SEARCH_SPACE,
            aliases=ALIASES,
            training_log=training_log(history, manifest),
            metrics_history=[(item["target_step"], item["metrics"]) for item in history],
            budget_remaining=len(targets) - index - 1,
            total_budget=len(targets),
            decision_number=index,
        )
        decisions.append({"after_step": target, "old_config": config, **decision})
        config = dict(decision["new_config"])

    final = history[-1]
    final_metrics = final["metrics"]
    payload = {
        "experiment_name": f"{TASK_ID}_{RESULT_FILE_AGENT_NAME}",
        "benchmark_name": TASK_ID,
        "agent_name": AGENT_LABEL,
        "agent_model": str(MODEL_PATH),
        "created_at": utc_now(),
        "success": True,
        "agent_success": True,
        "direction": "lower_is_better",
        "metric": "fineweb10B_validation_loss",
        "agent_budget_result": final_metrics.get("val_loss"),
        "agent_final_config": dict(final["config"]),
        "agent_decisions_made": len(decisions),
        "agent_internal_baseline": None,
        "official_budget_baseline": manifest.get("official_budget_baseline", 4.344427),
        "paper_anchor": manifest.get("paper_anchor", 3.424958),
        "chunk_targets": targets,
        "chunk_summaries": history,
        "decision_history": decisions,
        "final_config": dict(final["config"]),
        "final_metrics": final_metrics,
        "total_steps": targets[-1],
        "total_time": round(time.time() - started, 3),
        "output_dir": str(out_dir),
        "run_dir": str(run_dir),
        "run_id": run_id,
    }
    dump_json(result_file, payload)
    print(result_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
