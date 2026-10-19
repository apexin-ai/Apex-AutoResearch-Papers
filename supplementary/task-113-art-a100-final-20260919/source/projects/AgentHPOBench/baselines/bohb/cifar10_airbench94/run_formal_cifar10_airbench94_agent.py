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
FORMAL_DIR = ROOT / "baselines/bohb/cifar10_airbench94"
EVAL_SCRIPT = FORMAL_DIR / "eval_cifar10_airbench94.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "cifar10_airbench94"
RUN_ID = os.environ.get("RUN_ID") or f"cifar10_airbench94_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "cifar10_airbench94_QwenLocal_results.json"

PAPER_ANCHOR_ACC = 94.01
FIXED_BUDGET = {
    "epochs": float(os.environ.get("AIRBENCH_EPOCHS", "3.0")),
    "eval_batch_size": int(os.environ.get("AIRBENCH_EVAL_BATCH_SIZE", "2000")),
}
BASE_CONFIG = {
    "learning_rate": 11.5,
    "weight_decay": 0.0153,
    "momentum": 0.85,
    "label_smoothing": 0.2,
    "batch_size": 1024,
    "translate": 2,
    "tta_level": 2,
}
SEARCH_SPACE = {
    "learning_rate": {"choices": [8.0, 11.5, 14.0, 17.0]},
    "weight_decay": {"choices": [0.006, 0.01, 0.0153, 0.025]},
    "momentum": {"choices": [0.8, 0.85, 0.9]},
    "label_smoothing": {"choices": [0.0, 0.1, 0.2]},
    "batch_size": {"choices": [512, 1024]},
    "translate": {"choices": [1, 2, 3]},
    "tta_level": {"choices": [0, 1, 2]},
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def nearest(value: Any, choices: list[Any]) -> Any:
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "lr": "learning_rate",
        "learningrate": "learning_rate",
        "wd": "weight_decay",
        "weight_decay_rate": "weight_decay",
        "smoothing": "label_smoothing",
        "label_smooth": "label_smoothing",
        "bs": "batch_size",
        "train_batch_size": "batch_size",
        "translation": "translate",
        "tta": "tta_level",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "learning_rate": float(nearest(merged["learning_rate"], SEARCH_SPACE["learning_rate"]["choices"])),
        "weight_decay": float(nearest(merged["weight_decay"], SEARCH_SPACE["weight_decay"]["choices"])),
        "momentum": float(nearest(merged["momentum"], SEARCH_SPACE["momentum"]["choices"])),
        "label_smoothing": float(nearest(merged["label_smoothing"], SEARCH_SPACE["label_smoothing"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
        "translate": int(nearest(merged["translate"], SEARCH_SPACE["translate"]["choices"])),
        "tta_level": int(nearest(merged["tta_level"], SEARCH_SPACE["tta_level"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return (
        f"lr{cfg['learning_rate']}_wd{cfg['weight_decay']}_m{cfg['momentum']}"
        f"_ls{cfg['label_smoothing']}_bs{cfg['batch_size']}_tr{cfg['translate']}_tta{cfg['tta_level']}"
    ).replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("AIRBENCH_CUDA_VISIBLE_DEVICES", "1")
        env["PYTHONPATH"] = f"{ROOT}:{ROOT / '.python_deps'}:{ROOT / 'repositories/cifar10-airbench'}:{env.get('PYTHONPATH', '')}"
        env.setdefault("TOKENIZERS_PARALLELISM", "false")
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--epochs {FIXED_BUDGET['epochs']} "
            f"--batch-size {cfg['batch_size']} "
            f"--eval-batch-size {FIXED_BUDGET['eval_batch_size']} "
            f"--learning-rate {cfg['learning_rate']} "
            f"--weight-decay {cfg['weight_decay']} "
            f"--momentum {cfg['momentum']} "
            f"--label-smoothing {cfg['label_smoothing']} "
            f"--translate {cfg['translate']} "
            f"--tta-level {cfg['tta_level']} "
            "--seed 42 "
            "--verbose",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"Airbench eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def training_log(history: list[dict[str, Any]], current: dict[str, Any], baseline: float) -> str:
    lines = [
        "Task: CIFAR-10 Airbench 94% fast training.",
        "Metric: CIFAR-10 test accuracy percent with Airbench TTA, higher is better.",
        f"Paper anchor: {PAPER_ANCHOR_ACC} mean accuracy from cifar10-airbench README/paper 94% recipe.",
        f"Budget protocol: fixed epochs={FIXED_BUDGET['epochs']}; do not change epochs or data.",
        f"Budget baseline accuracy={baseline:.4f}, config={BASE_CONFIG}.",
        "Short-budget hint: early accuracy is sensitive to LR, label smoothing, and weight decay.",
        f"Current config: {current}",
        "Tune only learning_rate, weight_decay, momentum, label_smoothing, batch_size, translate, and tta_level.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"accuracy_percent={m['accuracy_percent']:.4f} "
            f"no_tta={m['no_tta_accuracy_percent']:.4f} seconds={m['seconds']}"
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
    sys.path.insert(0, str(ROOT))
    deps = ROOT / ".python_deps"
    if deps.exists():
        sys.path.insert(0, str(deps))
    from agenthpobench.agents.open_source.qwen_agent import QwenAgent
    from agenthpobench.core.agent_base import DecisionContext

    payload = {
        "training_log": training_log(history, current, baseline),
        "current_config": current,
        "metrics_history": [
            (item["trial"], item["metrics"]["accuracy_percent"], item["config"], item["kind"]) for item in history
        ],
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
        raw_config = dict(decision.new_config)
        out = {
            "new_config": clamp_config({**current, **raw_config}),
            "raw_new_config": raw_config,
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
        return out
    except Exception as exc:  # noqa: BLE001
        fallback = {
            "learning_rate": 14.0,
            "weight_decay": 0.01,
            "momentum": 0.85,
            "label_smoothing": 0.1,
            "batch_size": 1024,
            "translate": 2,
            "tta_level": 2,
        }
        return {
            "new_config": clamp_config(fallback),
            "raw_new_config": fallback,
            "reasoning": f"Qwen decision failed; using short-budget Airbench fallback. Error: {exc!r}",
            "confidence": 0.0,
            "metadata": {"fallback": True, "error": repr(exc)},
        }


def normalized_score(value: float, baseline: float) -> float:
    denom = PAPER_ANCHOR_ACC - baseline
    if abs(denom) < 1e-9:
        return 0.0
    return (value - baseline) / denom


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    history: list[dict[str, Any]] = []
    baseline_trial = run_eval("baseline", 0, BASE_CONFIG)
    history.append(baseline_trial)
    budget_baseline = float(baseline_trial["metrics"]["accuracy_percent"])

    decision = decide_with_qwen(history, BASE_CONFIG, budget_baseline)
    final_config = clamp_config(decision["new_config"])
    final_trial = run_eval("final", 1, final_config)
    history.append(final_trial)
    final_acc = float(final_trial["metrics"]["accuracy_percent"])

    score = normalized_score(final_acc, budget_baseline)
    summary = {
        "agent": os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal"),
        "benchmark_name": "cifar10_airbench94",
        "repo": "cifar10-airbench",
        "task": "CIFAR-10 Airbench 94% short-budget training",
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "run_dir": str(OUT_DIR),
        "paper_anchor": PAPER_ANCHOR_ACC,
        "budget": {
            "epochs": FIXED_BUDGET["epochs"],
            "metric": "accuracy_percent",
            "baseline_config": BASE_CONFIG,
        },
        "baseline_metrics": baseline_trial["metrics"],
        "final_metrics": final_trial["metrics"],
        "final_config": final_config,
        "decisions": [
            {
                "decision_number": 0,
                "old_config": BASE_CONFIG,
                "new_config": final_config,
                "raw_new_config": decision.get("raw_new_config"),
                "reasoning": decision.get("reasoning"),
                "confidence": decision.get("confidence"),
                "metadata": decision.get("metadata"),
            }
        ],
        "decisions_made": 1,
        "history": history,
        "search_space": SEARCH_SPACE,
        "success": True,
        "score": {
            "direction": "higher_is_better",
            "official_budget_baseline": budget_baseline,
            "paper_anchor": PAPER_ANCHOR_ACC,
            "normalized_score": score,
            "scoring_eligible": True,
        },
        "normalized_score": score,
    }
    (OUT_DIR / "summary.json").write_text(json.dumps(summary, indent=2))
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(summary, indent=2))
    print("RESULT_JSON " + json.dumps(summary, sort_keys=True), flush=True)
    print(str(RESULT_FILE), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
