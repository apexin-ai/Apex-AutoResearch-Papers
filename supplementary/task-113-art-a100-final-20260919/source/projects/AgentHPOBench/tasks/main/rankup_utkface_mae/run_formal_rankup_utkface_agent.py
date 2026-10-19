#!/usr/bin/env python3
from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(".")
FORMAL_DIR = ROOT / "tasks/main/rankup_utkface_mae"
EVAL_SCRIPT = FORMAL_DIR / "eval_rankup_utkface.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b"))) / "rankup_utkface_mae"
RUN_ID = os.environ.get("RUN_ID") or f"rankup_utkface_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "rankup_utkface_mae_QwenLocal_results.json"

PAPER_ANCHOR = 4.851
BASE_CONFIG = {"lr": 0.01, "weight_decay": 0.001, "batch_size": 32, "augment": True}
SEARCH_SPACE = {
    "lr": {"choices": [0.003, 0.01, 0.03]},
    "weight_decay": {"choices": [0.0001, 0.001, 0.003]},
    "batch_size": {"choices": [32, 64, 128]},
    "augment": {"choices": [True, False]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "rankup_utkface_mae", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)

FALLBACK_CONFIGS = [
    {"lr": 0.03, "weight_decay": 0.001, "batch_size": 64, "augment": True},
    {"lr": 0.01, "weight_decay": 0.0001, "batch_size": 64, "augment": False},
    {"lr": 0.003, "weight_decay": 0.001, "batch_size": 32, "augment": True},
    {"lr": 0.03, "weight_decay": 0.003, "batch_size": 32, "augment": False},
    {"lr": 0.01, "weight_decay": 0.003, "batch_size": 128, "augment": True},
]



def _apply_experiment_seed() -> None:
    raw_seed = os.environ.get("AUTOREP_PROCESS_SEED")
    if raw_seed is None:
        return
    seed = int(raw_seed)
    import random
    random.seed(seed)
    try:
        import numpy as np
        np.random.seed(seed % (2**32 - 1))
    except Exception:
        pass
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except Exception:
        pass


_apply_experiment_seed()

def cleanup_torch() -> None:
    try:
        import gc

        gc.collect()
        import torch

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            try:
                torch.cuda.ipc_collect()
            except Exception:
                pass
        gc.collect()
    except Exception:
        pass


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def nearest(value: Any, choices: list[Any]) -> Any:
    if choices and isinstance(choices[0], bool):
        if isinstance(value, bool):
            return value
        return str(value).lower() in {"1", "true", "yes", "y"}
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {"learning_rate": "lr", "wd": "weight_decay", "batch": "batch_size", "use_augment": "augment"}
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "lr": float(nearest(merged["lr"], SEARCH_SPACE["lr"]["choices"])),
        "weight_decay": float(nearest(merged["weight_decay"], SEARCH_SPACE["weight_decay"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
        "augment": bool(nearest(merged["augment"], SEARCH_SPACE["augment"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return f"lr{cfg['lr']}_wd{cfg['weight_decay']}_bs{cfg['batch_size']}_aug{int(cfg['augment'])}".replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("RANKUP_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "1"))
        env["PYTHONPATH"] = f"{ROOT / 'repositories/semi-supervised-regression'}:{ROOT / '.python_deps'}:{ROOT}:{env.get('PYTHONPATH', '')}"
        no_aug = "--no-augment" if not cfg["augment"] else ""
        train_steps = os.environ.get("RANKUP_TRAIN_STEPS", "400")
        eval_examples = os.environ.get("RANKUP_EVAL_EXAMPLES", "0")
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--lr {cfg['lr']} --weight-decay {cfg['weight_decay']} --batch-size {cfg['batch_size']} "
            f"--train-steps {train_steps} --eval-examples {eval_examples} {no_aug} --seed {int(os.environ.get('AUTOREP_REPLICATE_SEED', '0'))}",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"RankUp UTKFace eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def parse_config(text: str) -> dict[str, Any]:
    for pattern in [r"NEW_CONFIG\s*[:=]\s*(\{.*?\})", r"```json\s*(\{.*?\})\s*```", r"(\{[^{}]*(?:lr|weight_decay|batch_size|augment)[^{}]*\})"]:
        match = re.search(pattern, text, flags=re.S | re.I)
        if not match:
            continue
        block = match.group(1)
        try:
            return json.loads(block)
        except Exception:
            try:
                return ast.literal_eval(block)
            except Exception:
                continue
    raise ValueError(f"could not parse config: {text[:500]}")


def training_log(history: list[dict[str, Any]], baseline: float) -> str:
    lines = [
        "Task: RankUp NeurIPS 2024 UTKFace age regression using official split and WRN-28-2.",
        "Metric: MAE, lower is better.",
        "Official anchor: classic_cv_average_log.csv reports fullysupervised_utkface min_MAE=4.851.",
        f"Budget baseline MAE={baseline:.4f}, config={BASE_CONFIG}.",
        "Fixed budget: train_steps is controlled externally; do not change it.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"MAE={m['MAE']:.4f} MSE={m['MSE']:.4f} loss={m['train_loss_last']:.4f} seconds={m['seconds']}"
        )
    return "\n".join(lines)


def decide_with_qwen(history: list[dict[str, Any]], baseline: float, trial_idx: int) -> dict[str, Any]:

    import os as _tpe_os
    if _tpe_os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower() in {"tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
        import sys as _tpe_sys
        from pathlib import Path as _TpePath
        _tpe_sys.path.insert(0, str(_TpePath(__file__).resolve().parents[1]))
        from tpe_backend import tpe_decision_from_call
        return tpe_decision_from_call(globals().get("TASK_ID", _TpePath(__file__).resolve().parent.name), locals(), globals())
    deps = ROOT / ".python_deps"
    if deps.exists():
        sys.path.insert(0, str(deps))
    sys.path.insert(0, str(ROOT))
    prompt = f"""You are choosing one hyperparameter configuration for UTKFace age regression.

{training_log(history, baseline)}

Search space:
{json.dumps(SEARCH_SPACE, indent=2)}

Return exactly one line:
NEW_CONFIG: {{"lr": 0.01, "weight_decay": 0.001, "batch_size": 32, "augment": true}}
"""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"qwen_prompt_{trial_idx}.txt").write_text(prompt)
    agent = None
    try:
        from qwen_agent_multiseed_v2 import QwenAgent

        os.environ["CUDA_VISIBLE_DEVICES"] = os.environ.get("QWEN_CUDA_VISIBLE_DEVICES", "0")
        agent = QwenAgent(model_path=str(AGENT_MODEL), temperature=0.0, max_new_tokens=384, device_map="auto", torch_dtype="bfloat16", use_chat_template=False)
        response = agent._generate(prompt)
        (OUT_DIR / f"qwen_raw_{trial_idx}.txt").write_text(response)
        raw = parse_config(response)
        return clamp_config(raw)
    except Exception as exc:  # noqa: BLE001
        (OUT_DIR / f"qwen_error_{trial_idx}.txt").write_text(repr(exc))
        return clamp_config(FALLBACK_CONFIGS[min(trial_idx - 1, len(FALLBACK_CONFIGS) - 1)])
    finally:
        if agent is not None:
            del agent
        cleanup_torch()


def score(value: float, baseline: float) -> float:
    denom = baseline - PAPER_ANCHOR
    if abs(denom) < 1e-12:
        return 0.0
    return float((baseline - value) / denom)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    history: list[dict[str, Any]] = []
    baseline = run_eval("baseline", 0, BASE_CONFIG)
    baseline_mae = float(baseline["metrics"]["MAE"])
    history.append(baseline)
    interventions = int(os.environ.get("AUTOREP_INTERVENTIONS", "5"))
    current = dict(BASE_CONFIG)
    for trial_idx in range(1, interventions + 1):
        current = decide_with_qwen(history, baseline_mae, trial_idx)
        history.append(run_eval("agent", trial_idx, current))
    best = min(history, key=lambda item: float(item["metrics"]["MAE"]))
    final = history[-1]
    payload = {
        "task": "rankup_utkface_mae",
        "paper_anchor_MAE": PAPER_ANCHOR,
        "baseline_config": BASE_CONFIG,
        "baseline_metric": baseline_mae,
        "best_metric": float(best["metrics"]["MAE"]),
        "final_metric": float(final["metrics"]["MAE"]),
        "best_score_vs_budget_baseline": score(float(best["metrics"]["MAE"]), baseline_mae),
        "final_score_vs_budget_baseline": score(float(final["metrics"]["MAE"]), baseline_mae),
        "best_trial": best,
        "final_trial": final,
        "history": history,
        "run_id": RUN_ID,
    }
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(payload, indent=2))
    print("RESULT_JSON " + json.dumps(payload, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
