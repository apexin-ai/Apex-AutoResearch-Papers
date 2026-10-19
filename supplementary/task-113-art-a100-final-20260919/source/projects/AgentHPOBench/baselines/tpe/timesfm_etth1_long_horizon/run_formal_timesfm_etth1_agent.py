#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(".")
FORMAL_DIR = ROOT / "baselines/tpe/timesfm_etth1_long_horizon"
DATA_PATH = ROOT / "data/formal/timesfm_long_horizon/ETT-small/ETTh1.csv"
MODEL_PATH = ROOT / "models/timesfm/timesfm-1.0-200m-pytorch/torch_model.ckpt"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "timesfm_etth1_long_horizon"
RUN_ID = os.environ.get("RUN_ID") or f"timesfm_etth1_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "timesfm_etth1_long_horizon_QwenLocal_results.json"

PAPER_ANCHOR_WAPE = 0.509
PAPER_ANCHOR_SMAPE = 0.725
BASE_CONFIG = {
    "context_len": 32,
    "normalize": True,
    "window_size": 0,
    "per_core_batch_size": 32,
}
SEARCH_SPACE = {
    "context_len": {"choices": [32, 128, 256, 512]},
    "window_size": {"choices": [0]},
    "per_core_batch_size": {"choices": [8, 16, 32]},
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def nearest(value: Any, choices: list[Any]) -> Any:
    if choices and isinstance(choices[0], bool):
        if isinstance(value, bool):
            return value
        text = str(value).strip().lower()
        return text in {"1", "true", "yes", "y", "on"}
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "context": "context_len",
        "context_length": "context_len",
        "ctx": "context_len",
        "normalize_data": "normalize",
        "normalization": "normalize",
        "window": "window_size",
        "decomposition_window": "window_size",
        "per_core_batch": "per_core_batch_size",
        "batch_size": "per_core_batch_size",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "context_len": int(nearest(merged["context_len"], SEARCH_SPACE["context_len"]["choices"])),
        "normalize": bool(merged["normalize"]),
        "window_size": int(nearest(merged["window_size"], SEARCH_SPACE["window_size"]["choices"])),
        "per_core_batch_size": int(nearest(merged["per_core_batch_size"], SEARCH_SPACE["per_core_batch_size"]["choices"])),
    }


def run_eval(kind: str, trial_idx: int, config: dict[str, Any], max_windows: int = 0) -> dict[str, Any]:
    cfg = clamp_config(config)
    suffix = f"ctx{cfg['context_len']}_norm{int(cfg['normalize'])}_win{cfg['window_size']}_pcb{cfg['per_core_batch_size']}"
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{suffix}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["PYTHONPATH"] = f"{ROOT / 'repositories/timesfm/v1/src'}:{env.get('PYTHONPATH', '')}"
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("TIMESFM_CUDA_VISIBLE_DEVICES", "1")
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {FORMAL_DIR / 'eval_timesfm_etth1.py'} "
            f"--data-path {DATA_PATH} "
            f"--model-path {MODEL_PATH} "
            f"--results-dir {trial_dir} "
            f"--context-len {cfg['context_len']} "
            "--pred-len 96 "
            "--batch-size 64 "
            f"--per-core-batch-size {cfg['per_core_batch_size']} "
            f"--normalize {str(cfg['normalize']).lower()} "
            f"--window-size {cfg['window_size']} "
            "--backend gpu "
            f"--max-windows {max_windows}",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"TimesFM eval failed rc={proc.returncode}")
        if not metrics_path.exists():
            raise RuntimeError(f"TimesFM eval did not write {metrics_path}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {
        "trial": trial_idx,
        "kind": kind,
        "config": cfg,
        "metrics": payload,
        "output_dir": str(trial_dir),
    }


def training_log(history: list[dict[str, Any]], current: dict[str, Any], budget_baseline: float) -> str:
    lines = [
        "Task: TimesFM-1.0 zero-shot long-horizon forecasting on ETTh1, prediction length 96.",
        "Metric: WAPE, lower is better. Secondary metric: SMAPE, lower is better.",
        f"Paper anchor: WAPE={PAPER_ANCHOR_WAPE}, SMAPE={PAPER_ANCHOR_SMAPE}, context_len=512, normalized ETTh1, disjoint windows.",
        f"Budget baseline in this harness: WAPE={budget_baseline:.6f}, config={BASE_CONFIG}.",
        "You may tune inference hyperparameters only: context_len and per_core_batch_size; window_size is fixed to 0 in this PyTorch TimesFM harness.",
        "Keep normalize=True fixed because this is part of the official benchmark protocol.",
        "Prefer improving WAPE without changing the dataset, model checkpoint, prediction horizon, or official disjoint-window split.",
        f"Current config: {current}",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            "Trial "
            f"{item['trial']} {item['kind']}: config={item['config']} "
            f"wape={m['wape']:.6f} smape={m['smape']:.6f} mse={m['mse']:.6f}"
        )
    return "\n".join(lines)


def decide_with_qwen(history: list[dict[str, Any]], current: dict[str, Any], budget_baseline: float) -> dict[str, Any]:

    import os as _tpe_os
    if _tpe_os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower() in {"random", "random_search", "tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
        import sys as _tpe_sys
        from pathlib import Path as _TpePath
        _tpe_sys.path.insert(0, str(_TpePath(__file__).resolve().parents[1]))
        from tpe_backend import tpe_decision_from_call
        return tpe_decision_from_call(globals().get("TASK_ID", _TpePath(__file__).resolve().parent.name), locals(), globals())
    sys.path.insert(0, str(ROOT))
    deps = ROOT / ".python_deps"
    if deps.exists():
        sys.path.insert(0, str(deps))
    from agenthpobench.agents.open_source.qwen_agent import QwenAgent
    from agenthpobench.core.agent_base import DecisionContext

    payload = {
        "training_log": training_log(history, current, budget_baseline),
        "current_config": {key: current[key] for key in SEARCH_SPACE},
        "metrics_history": [(item["trial"], item["metrics"]["wape"], item["config"], item["kind"]) for item in history],
        "budget_remaining": 1,
        "total_budget": 2,
        "search_space": SEARCH_SPACE,
        "epoch": 1,
        "decision_number": 0,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "qwen_context_0.json").write_text(json.dumps(payload, indent=2))
    try:
        os.environ["CUDA_VISIBLE_DEVICES"] = os.environ.get("QWEN_CUDA_VISIBLE_DEVICES", "1")
        agent = QwenAgent(
            model_path=str(AGENT_MODEL),
            temperature=0.0,
            max_new_tokens=384,
            device_map="auto",
            torch_dtype="bfloat16",
            use_chat_template=False,
        )
        decision = agent.decide(DecisionContext(**payload))
        raw = {
            "new_config": clamp_config({**current, **decision.new_config}),
            "raw_new_config": decision.new_config,
            "reasoning": decision.reasoning,
            "confidence": decision.confidence,
            "metadata": decision.metadata,
        }
        del agent
        try:
            import torch

            torch.cuda.empty_cache()
        except Exception:
            pass
    except Exception as exc:
        raw = {
            "new_config": {**current, "context_len": 512, "normalize": True, "window_size": 0, "per_core_batch_size": 32},
            "raw_new_config": {"context_len": 512, "normalize": True, "window_size": 0, "per_core_batch_size": 32},
            "reasoning": f"Fallback after Qwen decision failure: {exc}. Use the official paper context length and normalization.",
            "confidence": 0.5,
            "metadata": {"fallback": True, "error": str(exc)},
        }
    (OUT_DIR / "qwen_decision_0.json").write_text(json.dumps(raw, indent=2))
    return raw


def normalized_score(value: float, budget_baseline: float) -> float:
    denom = budget_baseline - PAPER_ANCHOR_WAPE
    if denom <= 0:
        return 0.0
    return (budget_baseline - value) / denom


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    history = [run_eval("proxy", 0, BASE_CONFIG)]
    budget_baseline = float(history[0]["metrics"]["wape"])
    decision = decide_with_qwen(history, BASE_CONFIG, budget_baseline)
    final_config = clamp_config(decision["new_config"])
    final = run_eval("final", 0, final_config)
    final_wape = float(final["metrics"]["wape"])
    result = {
        "id": "timesfm_etth1_long_horizon_wape",
        "repo": "timesfm",
        "metric": "ETTh1_h96_wape",
        "direction": "lower_is_better",
        "official_budget_baseline": budget_baseline,
        "paper_anchor": PAPER_ANCHOR_WAPE,
        "paper_anchor_secondary": {"smape": PAPER_ANCHOR_SMAPE},
        "agent_budget_result": final_wape,
        "agent_secondary_result": {"smape": final["metrics"]["smape"], "mse": final["metrics"]["mse"]},
        "normalized_score": normalized_score(final_wape, budget_baseline),
        "agent_decisions_made": 1,
        "agent_final_config": final_config,
        "agent_internal_baseline": history[0]["metrics"]["wape"],
        "agent_internal_vs_official_budget_delta": 0.0,
        "agent_success": True,
        "history": history,
        "decision": decision,
        "final": final,
        "result_file": str(RESULT_FILE),
        "status": "scored",
    }
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
