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
FORMAL_DIR = ROOT / "baselines/tpe/ablkit_hwf_reasoning_accuracy"
EVAL_SCRIPT = FORMAL_DIR / "eval_ablkit_hwf.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", str(ROOT / "models/Qwen/Qwen3-8B")))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/main/qwen3_8b_seed0_final30"))) / "ablkit_hwf_reasoning_accuracy"
RUN_ID = os.environ.get("RUN_ID") or f"ablkit_hwf_reasoning_accuracy_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE_AGENT_NAME = os.environ.get("RESULT_FILE_AGENT_NAME", "QwenLocal")
RESULT_FILE = RESULT_ROOT / f"ablkit_hwf_reasoning_accuracy_{RESULT_FILE_AGENT_NAME}_results.json"

PAPER_ANCHOR_ACC = 99.2
INTERVENTIONS = int(os.environ.get("AUTOREP_INTERVENTIONS", "5"))
FIXED_BUDGET = {
    "loops": int(os.environ.get("ABLKIT_HWF_LOOPS", "1")),
    "epochs": int(os.environ.get("ABLKIT_HWF_EPOCHS", "1")),
    "train_limit": int(os.environ.get("ABLKIT_HWF_TRAIN_LIMIT", "0")),
    "test_limit": int(os.environ.get("ABLKIT_HWF_TEST_LIMIT", "0")),
    "seed": int(os.environ.get("ABLKIT_HWF_SEED", "1")),
}
BASE_CONFIG = {
    "lr": 0.001,
    "label_smoothing": 0.2,
    "batch_size": 128,
    "segment_size": 1000,
    "max_revision": -1,
    "ground": False,
}
SEARCH_SPACE = {
    "lr": {"choices": [0.0003, 0.0006, 0.001, 0.002]},
    "label_smoothing": {"choices": [0.0, 0.1, 0.2]},
    "batch_size": {"choices": [64, 128, 256]},
    "segment_size": {"choices": [500, 1000, 2000]},
    "max_revision": {"choices": [-1, 1, 2]},
    "ground": {"choices": [False, True]},
}
AGENT_SEARCH_SPACE = {
    **SEARCH_SPACE,
    "learning_rate": SEARCH_SPACE["lr"],
    "label_smooth": SEARCH_SPACE["label_smoothing"],
    "smoothing": SEARCH_SPACE["label_smoothing"],
    "batch": SEARCH_SPACE["batch_size"],
    "bs": SEARCH_SPACE["batch_size"],
    "segment": SEARCH_SPACE["segment_size"],
    "revision": SEARCH_SPACE["max_revision"],
    "use_ground": SEARCH_SPACE["ground"],
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on", "ground"}


def nearest(value: Any, choices: list[Any]) -> Any:
    if all(isinstance(item, bool) for item in choices):
        return as_bool(value)
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        text = str(value).lower()
        for item in choices:
            if str(item).lower() == text:
                return item
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "learning_rate": "lr",
        "label_smooth": "label_smoothing",
        "smoothing": "label_smoothing",
        "batch": "batch_size",
        "bs": "batch_size",
        "segment": "segment_size",
        "revision": "max_revision",
        "use_ground": "ground",
    }
    merged = dict(BASE_CONFIG)
    for key, value in (config or {}).items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "lr": float(nearest(merged["lr"], SEARCH_SPACE["lr"]["choices"])),
        "label_smoothing": float(nearest(merged["label_smoothing"], SEARCH_SPACE["label_smoothing"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
        "segment_size": int(nearest(merged["segment_size"], SEARCH_SPACE["segment_size"]["choices"])),
        "max_revision": int(nearest(merged["max_revision"], SEARCH_SPACE["max_revision"]["choices"])),
        "ground": bool(nearest(merged["ground"], SEARCH_SPACE["ground"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return (
        f"lr{cfg['lr']}_ls{cfg['label_smoothing']}_bs{cfg['batch_size']}"
        f"_seg{cfg['segment_size']}_rev{cfg['max_revision']}_g{int(cfg['ground'])}"
    ).replace(".", "p").replace("-", "m")


def metric_value(metrics: dict[str, Any]) -> float:
    return float(metrics["reasoning_accuracy_percent"])


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("ABLKIT_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "0"))
        env["PYTHONPATH"] = (
            f"{ROOT / 'baselines/tpe/ablkit_mnist_add_reasoning_accuracy/stubs'}:"
            f"{ROOT / 'repositories/ABLkit'}:{ROOT / 'repositories/ABLkit/examples/hwf'}:"
            f"{ROOT}:{ROOT / '.python_deps'}:{env.get('PYTHONPATH', '')}"
        )
        ground = "--ground" if cfg["ground"] else ""
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--lr {cfg['lr']} "
            f"--label-smoothing {cfg['label_smoothing']} "
            f"--batch-size {cfg['batch_size']} "
            f"--segment-size {cfg['segment_size']} "
            f"--loops {FIXED_BUDGET['loops']} "
            f"--epochs {FIXED_BUDGET['epochs']} "
            f"--max-revision {cfg['max_revision']} "
            f"--train-limit {FIXED_BUDGET['train_limit']} "
            f"--test-limit {FIXED_BUDGET['test_limit']} "
            f"--seed {FIXED_BUDGET['seed']} "
            "--device cuda:0 "
            f"{ground}",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT / "repositories/ABLkit/examples/hwf"), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text[-8000:], flush=True)
            raise RuntimeError(f"ABLkit HWF eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def training_log(history: list[dict[str, Any]], current: dict[str, Any], baseline: float, decision_idx: int) -> str:
    best = max(history, key=lambda item: metric_value(item["metrics"]))
    lines = [
        "Task: ABLkit handwritten formula (HWF) abductive reasoning.",
        "Metric: reasoning_accuracy_percent on the official HWF test expressions, higher is better.",
        "Paper/README anchor: ABLkit examples/hwf README reports ABL HWF reasoning accuracy 99.2 for all formula lengths.",
        f"Budget protocol: fixed loops={FIXED_BUDGET['loops']}, epochs_per_loop={FIXED_BUDGET['epochs']}, full official train/test lists unless limits are explicitly set; do not change loops, epochs, dataset, or metric.",
        f"Budget baseline reasoning_accuracy_percent={baseline:.4f}, config={BASE_CONFIG}.",
        "Tune only lr, label_smoothing, batch_size, segment_size, max_revision, and ground.",
        f"Current config before decision {decision_idx}: {current}",
        f"Best observed config so far: {best['config']} with reasoning_accuracy_percent={metric_value(best['metrics']):.4f}.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"reasoning_accuracy_percent={m['reasoning_accuracy_percent']:.4f} "
            f"symbol_accuracy_percent={m['symbol_accuracy_percent']:.4f} seconds={m.get('seconds')}"
        )
    return "\n".join(lines)


def fallback_config(decision_idx: int, current: dict[str, Any]) -> dict[str, Any]:
    candidates = [
        {"lr": 0.0006, "label_smoothing": 0.1, "batch_size": 128, "segment_size": 1000, "max_revision": -1, "ground": False},
        {"lr": 0.001, "label_smoothing": 0.0, "batch_size": 256, "segment_size": 1000, "max_revision": -1, "ground": False},
        {"lr": 0.002, "label_smoothing": 0.1, "batch_size": 128, "segment_size": 2000, "max_revision": 1, "ground": False},
        {"lr": 0.0003, "label_smoothing": 0.2, "batch_size": 64, "segment_size": 500, "max_revision": 2, "ground": True},
        {"lr": 0.001, "label_smoothing": 0.1, "batch_size": 64, "segment_size": 2000, "max_revision": -1, "ground": True},
    ]
    return clamp_config({**current, **candidates[decision_idx % len(candidates)]})


def decide_with_qwen(history: list[dict[str, Any]], current: dict[str, Any], baseline: float, decision_idx: int) -> dict[str, Any]:

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
    payload = {
        "training_log": training_log(history, current, baseline, decision_idx),
        "current_config": current,
        "metrics_history": [
            (item["trial"], metric_value(item["metrics"]), item["config"], item["kind"]) for item in history
        ],
        "budget_remaining": max(0, INTERVENTIONS - decision_idx - 1),
        "total_budget": INTERVENTIONS,
        "search_space": AGENT_SEARCH_SPACE,
        "epoch": decision_idx + 1,
        "decision_number": decision_idx,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"qwen_context_{decision_idx}.json").write_text(json.dumps(payload, indent=2))
    try:
        if os.environ.get("AUTOREP_DISABLE_AGENT", "0") == "1":
            raise RuntimeError("AUTOREP_DISABLE_AGENT=1")
        from agenthpobench.agents.open_source.qwen_agent import QwenAgent
        from agenthpobench.core.agent_base import DecisionContext

        os.environ["CUDA_VISIBLE_DEVICES"] = os.environ.get("QWEN_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "0"))
        agent = QwenAgent(
            model_path=str(AGENT_MODEL),
            temperature=0.0,
            max_new_tokens=int(os.environ.get("AUTOREP_AGENT_MAX_NEW_TOKENS", "384")),
            device_map="auto",
            torch_dtype=os.environ.get("AUTOREP_AGENT_TORCH_DTYPE", "bfloat16"),
            use_chat_template=os.environ.get("AUTOREP_USE_CHAT_TEMPLATE", "0").lower() in {"1", "true", "yes"},
        )
        decision = agent.decide(DecisionContext(**payload))
        if decision.metadata.get("fallback"):
            raise RuntimeError(f"QwenAgent internal fallback: {decision.metadata.get('error')}")
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
    except Exception as exc:
        fallback = fallback_config(decision_idx, current)
        return {
            "new_config": fallback,
            "raw_new_config": fallback,
            "reasoning": f"Agent decision failed; using deterministic ABLkit HWF fallback candidate. Error: {exc!r}",
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
    decisions: list[dict[str, Any]] = []

    baseline_trial = run_eval("baseline", 0, BASE_CONFIG)
    history.append(baseline_trial)
    budget_baseline = metric_value(baseline_trial["metrics"])
    current_config = dict(BASE_CONFIG)

    for decision_idx in range(INTERVENTIONS):
        decision = decide_with_qwen(history, current_config, budget_baseline, decision_idx)
        next_config = clamp_config(decision["new_config"])
        trial = run_eval("intervention", decision_idx + 1, next_config)
        history.append(trial)
        decisions.append(
            {
                "decision_number": decision_idx,
                "old_config": current_config,
                "new_config": next_config,
                "raw_new_config": decision.get("raw_new_config"),
                "reasoning": decision.get("reasoning"),
                "confidence": decision.get("confidence"),
                "metadata": decision.get("metadata"),
                "trial_metric": metric_value(trial["metrics"]),
            }
        )
        current_config = next_config

    best_trial = max(history, key=lambda item: metric_value(item["metrics"]))
    final_trial = history[-1]
    best_acc = metric_value(best_trial["metrics"])
    final_acc = metric_value(final_trial["metrics"])
    summary = {
        "agent": os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal"),
        "benchmark_name": "ablkit_hwf_reasoning_accuracy",
        "repo": "ABLkit",
        "repo_url": "https://github.com/AbductiveLearning/ABLkit",
        "task": "Handwritten formula abductive reasoning",
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "run_dir": str(OUT_DIR),
        "paper_anchor": PAPER_ANCHOR_ACC,
        "budget": {
            **FIXED_BUDGET,
            "metric": "reasoning_accuracy_percent",
            "baseline_config": BASE_CONFIG,
            "interventions": INTERVENTIONS,
        },
        "baseline_metrics": baseline_trial["metrics"],
        "final_metrics": final_trial["metrics"],
        "best_metrics": best_trial["metrics"],
        "final_config": final_trial["config"],
        "best_config": best_trial["config"],
        "decisions": decisions,
        "decisions_made": len(decisions),
        "history": history,
        "metric": "reasoning_accuracy_percent",
        "higher_is_better": True,
        "direction": "higher_is_better",
        "agent_budget_result": best_acc,
        "final_agent_budget_result": final_acc,
        "official_budget_baseline": budget_baseline,
        "paper_anchor_source": "ABLkit examples/hwf README: ABL HWF reasoning accuracy 99.2 for all formula lengths.",
        "score": {
            "normalized_score": normalized_score(best_acc, budget_baseline),
            "delta_vs_budget_baseline": best_acc - budget_baseline,
            "delta_vs_paper_anchor": best_acc - PAPER_ANCHOR_ACC,
            "final_delta_vs_budget_baseline": final_acc - budget_baseline,
            "final_delta_vs_paper_anchor": final_acc - PAPER_ANCHOR_ACC,
            "official_budget_baseline": budget_baseline,
            "paper_anchor": PAPER_ANCHOR_ACC,
            "direction": "higher_is_better",
        },
        "success": True,
    }
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(summary, indent=2))
    (OUT_DIR / "summary.json").write_text(json.dumps(summary, indent=2))
    print("FINAL_RESULT " + json.dumps(summary, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
