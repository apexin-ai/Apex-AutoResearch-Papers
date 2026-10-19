#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(os.environ.get("AUTOREP_ROOT", "."))
FORMAL_DIR = ROOT / "tasks/ablations/no_feedback/var_imagenet256"
EVAL_SCRIPT = FORMAL_DIR / "eval_var_imagenet_subset.py"
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/main/qwen3_8b_seed0_final30"))) / "var_imagenet256"
RUN_ID = os.environ.get("RUN_ID") or f"var_imagenet256_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE_AGENT_NAME = os.environ.get("RESULT_FILE_AGENT_NAME", "QwenLocal")
RESULT_FILE = RESULT_ROOT / f"var_imagenet256_{RESULT_FILE_AGENT_NAME}_results.json"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", str(ROOT / "models/Qwen/Qwen3-8B")))
AGENT_LABEL = os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal")

PAPER_ANCHOR_FID = 3.55
BASE_CONFIG = {"cfg": 1.5, "top_k": 900, "top_p": 0.96, "more_smooth": False}
SEARCH_SPACE = {
    "cfg": [1.0, 1.5, 2.0, 3.0, 5.0],
    "top_k": [300, 600, 900],
    "top_p": [0.90, 0.95, 0.96, 0.98],
    "more_smooth": [False, True],
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "var_imagenet256", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)

ALIASES = {"topk": "top_k", "topp": "top_p", "guidance_scale": "cfg", "smooth": "more_smooth"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def dump_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def nearest(value: Any, choices: list[Any]) -> Any:
    if isinstance(choices[0], bool):
        if isinstance(value, str):
            return value.strip().lower() in {"1", "true", "yes", "on"}
        return bool(value)
    try:
        number = float(value)
        return min(choices, key=lambda item: abs(float(item) - number))
    except Exception:
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    merged = dict(BASE_CONFIG)
    for key, value in (config or {}).items():
        mapped = ALIASES.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "cfg": float(nearest(merged["cfg"], SEARCH_SPACE["cfg"])),
        "top_k": int(nearest(merged["top_k"], SEARCH_SPACE["top_k"])),
        "top_p": float(nearest(merged["top_p"], SEARCH_SPACE["top_p"])),
        "more_smooth": bool(nearest(merged["more_smooth"], SEARCH_SPACE["more_smooth"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return f"cfg{cfg['cfg']}_topk{cfg['top_k']}_topp{cfg['top_p']}_smooth{int(cfg['more_smooth'])}".replace(".", "p")


def run_eval(kind: str, trial: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial}_{slug(cfg)}"
    if not (trial_dir / "results.json").exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["PYTHONPATH"] = f"{ROOT / 'repositories/VAR'}:{ROOT}:{ROOT / '.python_deps'}:{env.get('PYTHONPATH', '')}"
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("VAR_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "0"))
        max_items = os.environ.get("VAR_FORMAL_MAX_ITEMS", "32")
        num_classes = os.environ.get("VAR_FORMAL_NUM_CLASSES", "16")
        samples_per_class = os.environ.get("VAR_FORMAL_SAMPLES_PER_CLASS", "2")
        use_cached = os.environ.get("VAR_USE_CACHED_FOR_AGENT", "0").strip().lower() in {"1", "true", "yes", "on"}
        generate_flag = "" if use_cached else "--generate"
        more_smooth_flag = "--more-smooth" if cfg["more_smooth"] else ""
        cmd = (
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-var && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--max-items {max_items} "
            f"--num-classes {num_classes} "
            f"--samples-per-class {samples_per_class} "
            f"--cfg {cfg['cfg']} --top-k {cfg['top_k']} --top-p {cfg['top_p']} "
            f"{more_smooth_flag} {generate_flag}"
        )
        log_path = trial_dir / "run.log"
        started = time.time()
        with log_path.open("wb") as log:
            proc = subprocess.run(["bash", "-lc", cmd], cwd=str(ROOT), env=env, stdout=log, stderr=subprocess.STDOUT)
        if proc.returncode != 0:
            print(log_path.read_text(errors="replace")[-8000:], flush=True)
            raise RuntimeError(f"VAR eval failed rc={proc.returncode}")
        seconds_outer = round(time.time() - started, 3)
        payload = load_json(trial_dir / "results.json")
        payload["seconds_outer"] = seconds_outer
        dump_json(trial_dir / "results.json", payload)
    payload = load_json(trial_dir / "results.json")
    return {"trial": trial, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def extract_config(text: str) -> dict[str, Any]:
    match = re.search(r"NEW_CONFIG:\s*(\{.*?\})", text, flags=re.S)
    if not match:
        match = re.search(r"(\{[^{}]*\})", text, flags=re.S)
    if not match:
        return {}
    block = match.group(1)
    block = re.sub(r"\bTrue\b", "true", block)
    block = re.sub(r"\bFalse\b", "false", block)
    try:
        return json.loads(block)
    except Exception:
        return {}


def decide(history: list[dict[str, Any]], current_config: dict[str, Any], decision_number: int) -> dict[str, Any]:
    history = history[:1]  # No-feedback: expose only the baseline observation.
    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(ROOT / ".python_deps"))
    sys.path.insert(0, str(ROOT / "tasks/ablations/no_feedback"))
    from _budget_agent_common import decide_config

    lines = [
        "You tune sampling hyperparameters for VAR-d16 ImageNet-256 generation.",
        "Metric: negative_subset_diag_fid, higher is better; this is just -subset_diag_fid. Do not change model, checkpoint, dataset, number of samples, or metric.",
        f"Paper anchor: VAR-d16 ImageNet-256 FID={PAPER_ANCHOR_FID}.",
        f"Current config: {json.dumps(current_config, sort_keys=True)}",
        f"Search space: {json.dumps(SEARCH_SPACE, sort_keys=True)}",
        "History:",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"{item['kind']} trial={item['trial']} config={item['config']} "
            f"subset_diag_fid={m['subset_fid']:.6f} negative_subset_diag_fid={-float(m['subset_fid']):.6f}"
        )
    decision = decide_config(
        task_name="var_imagenet256",
        current_config=current_config,
        search_space=SEARCH_SPACE,
        aliases=ALIASES,
        training_log="\n".join(lines),
        metrics_history=[
            (item["trial"], {"accuracy": -float(item["metrics"]["subset_fid"]), "subset_fid": float(item["metrics"]["subset_fid"])})
            for item in history
        ],
        budget_remaining=max(0, int(os.environ.get("AUTOREP_INTERVENTIONS", "5")) - decision_number),
        total_budget=int(os.environ.get("AUTOREP_INTERVENTIONS", "5")) + 1,
        decision_number=decision_number,
    )
    return {
        "decision_number": decision_number,
        "old_config": dict(current_config),
        "new_config": clamp_config(decision["new_config"]),
        "raw_new_config": decision.get("raw_new_config", {}),
        "reasoning": decision.get("reasoning"),
        "confidence": decision.get("confidence"),
        "metadata": decision.get("metadata"),
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if os.environ.get("AUTOREP_DRY_RUN", "0") == "1":
        print(json.dumps({"task_id": "var_imagenet256", "result_file": str(RESULT_FILE), "run_dir": str(OUT_DIR)}, indent=2))
        return 0

    history: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []
    started = time.time()
    config = dict(BASE_CONFIG)
    baseline = run_eval("baseline", 0, config)
    history.append(baseline)
    best = baseline
    interventions = int(os.environ.get("AUTOREP_INTERVENTIONS", "5"))
    for i in range(interventions):
        decision = decide(history, config, i)
        decisions.append(decision)
        config = dict(decision["new_config"])
        trial = run_eval("intervention", i + 1, config)
        history.append(trial)
        if trial["metrics"]["subset_fid"] < best["metrics"]["subset_fid"]:
            best = trial

    final = history[-1]
    payload = {
        "agent": AGENT_LABEL,
        "benchmark_name": "var_imagenet256",
        "repo": "VAR",
        "repo_url": "https://github.com/FoundationVision/VAR",
        "task": "Class-conditional ImageNet-256 autoregressive generation",
        "dataset": "ImageNet-1K 256x256 FID reference",
        "metric": "subset_diag_fid",
        "direction": "lower_is_better",
        "higher_is_better": False,
        "paper_anchor": PAPER_ANCHOR_FID,
        "paper_anchor_source": "repositories/VAR/README.md table: VAR-d16 ImageNet 256 FID 3.55.",
        "official_budget_baseline": baseline["metrics"]["subset_fid"],
        "agent_budget_result": best["metrics"]["subset_fid"],
        "final_agent_budget_result": final["metrics"]["subset_fid"],
        "baseline_metrics": baseline["metrics"],
        "best_metrics": best["metrics"],
        "final_metrics": final["metrics"],
        "best_config": best["config"],
        "final_config": final["config"],
        "decisions_made": len(decisions),
        "decisions": decisions,
        "history": history,
        "budget": {
            "interventions": interventions,
            "max_items": int(os.environ.get("VAR_FORMAL_MAX_ITEMS", "32")),
            "num_classes": int(os.environ.get("VAR_FORMAL_NUM_CLASSES", "16")),
            "samples_per_class": int(os.environ.get("VAR_FORMAL_SAMPLES_PER_CLASS", "2")),
            "metric": "subset_diag_fid",
        },
        "success": True,
        "run_dir": str(OUT_DIR),
        "run_id": RUN_ID,
        "model_path": str(AGENT_MODEL),
        "total_seconds": round(time.time() - started, 3),
        "score": {
            "direction": "lower_is_better",
            "official_budget_baseline": baseline["metrics"]["subset_fid"],
            "paper_anchor": PAPER_ANCHOR_FID,
            "delta_vs_budget_baseline": baseline["metrics"]["subset_fid"] - best["metrics"]["subset_fid"],
            "final_delta_vs_budget_baseline": baseline["metrics"]["subset_fid"] - final["metrics"]["subset_fid"],
            "delta_vs_paper_anchor": PAPER_ANCHOR_FID - best["metrics"]["subset_fid"],
            "final_delta_vs_paper_anchor": PAPER_ANCHOR_FID - final["metrics"]["subset_fid"],
        },
    }
    dump_json(RESULT_FILE, payload)
    print("FINAL_RESULT " + json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
