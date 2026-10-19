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
FORMAL_DIR = ROOT / "tasks/main/xlstm_parity"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "xlstm_parity"
RUN_ID = os.environ.get("XLSTM_RUN_ID") or os.environ.get("RUN_ID") or f"xlstm_parity_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "xlstm_parity_QwenLocal_results.json"

PAPER_ANCHOR = 1.0
BASE_CONFIG = {
    "learning_rate": 1e-4,
    "weight_decay": 0.1,
    "warmup_ratio": 0.1,
    "batch_size": 128,
    "slstm_pattern": "last",
}
SEARCH_SPACE = {
    "learning_rate": {"choices": [1e-4, 1e-3, 1e-2]},
    "weight_decay": {"choices": [0.0, 0.01, 0.1]},
    "warmup_ratio": {"choices": [0.0, 0.05, 0.1]},
    "batch_size": {"choices": [64, 128, 256]},
    "slstm_pattern": {"choices": ["last", "all"]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "xlstm_parity", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)

FIXED = {
    "train_steps": int(os.environ.get("XLSTM_TRAIN_STEPS", "120")),
    "train_count": int(os.environ.get("XLSTM_TRAIN_COUNT", "8192")),
    "eval_count": int(os.environ.get("XLSTM_EVAL_COUNT", "2048")),
    "context_length": 256,
}



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

def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def nearest(value: Any, choices: list[Any]) -> Any:
    if isinstance(choices[0], str):
        text = str(value).strip().lower()
        return text if text in choices else choices[0]
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "lr": "learning_rate",
        "wd": "weight_decay",
        "warmup": "warmup_ratio",
        "batch": "batch_size",
        "architecture": "slstm_pattern",
        "slstm_at": "slstm_pattern",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "learning_rate": float(nearest(merged["learning_rate"], SEARCH_SPACE["learning_rate"]["choices"])),
        "weight_decay": float(nearest(merged["weight_decay"], SEARCH_SPACE["weight_decay"]["choices"])),
        "warmup_ratio": float(nearest(merged["warmup_ratio"], SEARCH_SPACE["warmup_ratio"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
        "slstm_pattern": str(nearest(merged["slstm_pattern"], SEARCH_SPACE["slstm_pattern"]["choices"])),
    }


def config_from_metrics(payload: dict[str, Any]) -> dict[str, Any]:
    config = {key: payload[key] for key in BASE_CONFIG if key in payload}
    return clamp_config({**BASE_CONFIG, **config})


def existing_trial_metrics_path(kind: str, trial_idx: int) -> Path | None:
    parent = OUT_DIR / kind
    if not parent.exists():
        return None
    matches = [path for path in parent.glob(f"trial{trial_idx}_*/results.json") if path.is_file()]
    if not matches:
        return None
    return sorted(matches, key=lambda path: path.stat().st_mtime)[-1]


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    existing = existing_trial_metrics_path(kind, trial_idx)
    if existing is not None:
        payload = load_json(existing)
        resumed_cfg = config_from_metrics(payload)
        return {
            "trial": trial_idx,
            "kind": kind,
            "config": resumed_cfg,
            "metrics": payload,
            "output_dir": str(existing.parent),
            "resumed_existing": True,
        }
    cfg = clamp_config(config)
    suffix = (
        f"lr{cfg['learning_rate']}_wd{cfg['weight_decay']}_warm{cfg['warmup_ratio']}"
        f"_bs{cfg['batch_size']}_slstm{cfg['slstm_pattern']}"
    ).replace(".", "p")
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{suffix}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("XLSTM_CUDA_VISIBLE_DEVICES", "1")
        env["PYTHONPATH"] = f"{ROOT / 'repositories/xlstm'}:{env.get('PYTHONPATH', '')}"
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {FORMAL_DIR / 'eval_xlstm_parity.py'} "
            f"--results-dir {trial_dir} "
            f"--context-length {FIXED['context_length']} "
            f"--train-count {FIXED['train_count']} "
            f"--eval-count {FIXED['eval_count']} "
            f"--train-steps {FIXED['train_steps']} "
            f"--learning-rate {cfg['learning_rate']} "
            f"--weight-decay {cfg['weight_decay']} "
            f"--warmup-ratio {cfg['warmup_ratio']} "
            f"--batch-size {cfg['batch_size']} "
            "--eval-batch-size 256 "
            "--embedding-dim 64 "
            f"--slstm-pattern {cfg['slstm_pattern']} "
            "--dropout 0.0 "
            "--grad-clip 1.0 "
            "--use-amp",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"xLSTM parity eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def training_log(history: list[dict[str, Any]], current: dict[str, Any], baseline: float) -> str:
    lines = [
        "Task: xLSTM NeurIPS 2024 formal-language Parity extrapolation.",
        "Metric: scaled validation sequence accuracy, higher is better. Random baseline is 0.5 raw accuracy; paper reports scaled accuracy.",
        "Paper anchor: xLSTM reaches scaled accuracy 1.0 on Parity in the paper formal-language benchmark.",
        f"Budget: train_steps={FIXED['train_steps']}, context_length=256, validation sequences length 40..256.",
        "The official CUDA sLSTM kernel fails to compile in this environment; use the same sLSTM architecture with vanilla backend.",
        f"Budget baseline scaled_accuracy={baseline:.6f}, config={BASE_CONFIG}.",
        f"Current config: {current}",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"scaled_accuracy={m['scaled_accuracy']:.6f} raw_accuracy={m['sequence_accuracy']:.6f} "
            f"loss={m['eval_loss']:.6f} train_loss={m['train_loss_final']:.6f}"
        )
    return "\n".join(lines)


def decide_with_qwen(history: list[dict[str, Any]], current: dict[str, Any], baseline: float) -> dict[str, Any]:

    import os as _tpe_os
    if _tpe_os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower() in {"tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
        import sys as _tpe_sys
        from pathlib import Path as _TpePath
        _tpe_sys.path.insert(0, str(_TpePath(__file__).resolve().parents[1]))
        from tpe_backend import tpe_decision_from_call
        return tpe_decision_from_call(globals().get("TASK_ID", _TpePath(__file__).resolve().parent.name), locals(), globals())
    decision_idx = max(0, len(history) - 1)
    next_trial_idx = decision_idx + 1
    existing = existing_trial_metrics_path(f"intervention_{next_trial_idx}", next_trial_idx)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if existing is not None:
        payload = load_json(existing)
        resumed_cfg = config_from_metrics(payload)
        raw = {
            "new_config": resumed_cfg,
            "raw_new_config": resumed_cfg,
            "reasoning": f"Reused existing completed xLSTM intervention {next_trial_idx} from {existing}.",
            "confidence": 1.0,
            "metadata": {"resumed_existing": True, "metrics_path": str(existing)},
        }
        (OUT_DIR / f"qwen_decision_{decision_idx}.json").write_text(json.dumps(raw, indent=2))
        return raw
    target_interventions = int(os.environ.get("AUTOREP_INTERVENTIONS", os.environ.get("AUTOREP_SERIAL_INTERVENTIONS", "5")))
    sys.path.insert(0, str(ROOT))
    deps = ROOT / ".python_deps"
    if deps.exists():
        sys.path.insert(0, str(deps))
    from qwen_agent_multiseed_v2 import QwenAgent
    from agenthpobench.core.agent_base import DecisionContext

    payload = {
        "training_log": training_log(history, current, baseline),
        "current_config": current,
        "metrics_history": [(item["trial"], item["metrics"]["scaled_accuracy"], item["config"], item["kind"]) for item in history],
        "budget_remaining": max(1, target_interventions - decision_idx),
        "total_budget": target_interventions,
        "search_space": SEARCH_SPACE,
        "epoch": decision_idx + 1,
        "decision_number": decision_idx,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"qwen_context_{decision_idx}.json").write_text(json.dumps(payload, indent=2))
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
            "new_config": {"learning_rate": 1e-3, "weight_decay": 0.1, "warmup_ratio": 0.1, "batch_size": 128, "slstm_pattern": "last"},
            "raw_new_config": {"learning_rate": 1e-3, "weight_decay": 0.1, "warmup_ratio": 0.1, "batch_size": 128, "slstm_pattern": "last"},
            "reasoning": f"Fallback after Qwen failure: {exc}. Use the paper default lr=1e-3.",
            "confidence": 0.5,
            "metadata": {"fallback": True, "error": str(exc)},
        }
    (OUT_DIR / f"qwen_decision_{decision_idx}.json").write_text(json.dumps(raw, indent=2))
    return raw


def normalized_score(value: float, baseline: float) -> float:
    denom = PAPER_ANCHOR - baseline
    if denom <= 0:
        return 0.0
    return (value - baseline) / denom


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    history = [run_eval("proxy", 0, BASE_CONFIG)]
    baseline = float(history[0]["metrics"]["scaled_accuracy"])
    decision = decide_with_qwen(history, BASE_CONFIG, baseline)
    history.append(run_eval("agent", 1, decision["new_config"]))
    final = history[-1]
    final_score = float(final["metrics"]["scaled_accuracy"])
    result = {
        "task_id": "xlstm_parity_scaled_accuracy",
        "repo": "NX-AI/xlstm",
        "scoreable": True,
        "dataset": "xLSTM formal-language Parity",
        "metric": "validation_scaled_sequence_accuracy",
        "higher_is_better": True,
        "paper_anchor": PAPER_ANCHOR,
        "paper_anchor_source": "xLSTM NeurIPS 2024 paper, formal-language benchmark Figure 9.",
        "budget_protocol": FIXED,
        "budget_baseline": baseline,
        "budget_baseline_config": BASE_CONFIG,
        "agent_final": final_score,
        "agent_config": final["config"],
        "normalized_score": normalized_score(final_score, baseline),
        "history": history,
        "decision": decision,
        "run_id": RUN_ID,
        "output_dir": str(OUT_DIR),
        "result_file": str(RESULT_FILE),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(result, indent=2))
    (OUT_DIR / "summary.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
