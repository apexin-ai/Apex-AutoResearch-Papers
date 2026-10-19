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
FORMAL_DIR = ROOT / "baselines/bohb/binary_diffusion_adult_rf"
EVAL_SCRIPT = FORMAL_DIR / "eval_binary_diffusion_adult_rf.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b"))) / "binary_diffusion_adult_rf"
RUN_ID = os.environ.get("RUN_ID") or f"binary_diffusion_adult_rf_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "binary_diffusion_adult_rf_QwenLocal_results.json"

PAPER_ANCHOR_ACC = 85.74
BASE_CONFIG = {
    "model_family": "rf",
    "n_estimators": 100,
    "max_depth": None,
    "min_samples_leaf": 1,
    "criterion": "gini",
    "max_features": "sqrt",
    "class_weight": "none",
    "learning_rate": 0.1,
    "C": 1.0,
}
SEARCH_SPACE = {
    "model_family": {"choices": ["rf", "extra_trees", "tree", "gb", "lr"]},
    "n_estimators": {"choices": [50, 100, 200, 400]},
    "max_depth": {"choices": [3, 4, 5, 8, None]},
    "min_samples_leaf": {"choices": [1, 2, 4, 8]},
    "criterion": {"choices": ["gini", "entropy"]},
    "max_features": {"choices": ["sqrt", "log2", "none"]},
    "class_weight": {"choices": ["none", "balanced"]},
    "learning_rate": {"choices": [0.03, 0.05, 0.1, 0.2]},
    "C": {"choices": [0.1, 1.0, 10.0]},
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def nearest(value: Any, choices: list[Any]) -> Any:
    if value is None and None in choices:
        return None
    try:
        numeric = float(value)
        numeric_choices = [item for item in choices if item is not None]
        return min(numeric_choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        text = str(value).lower()
        for item in choices:
            if str(item).lower() == text:
                return item
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "model": "model_family",
        "classifier": "model_family",
        "family": "model_family",
        "num_trees": "n_estimators",
        "trees": "n_estimators",
        "depth": "max_depth",
        "leaf": "min_samples_leaf",
        "min_leaf": "min_samples_leaf",
        "lr": "learning_rate",
        "regularization_C": "C",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "model_family": str(nearest(merged["model_family"], SEARCH_SPACE["model_family"]["choices"])),
        "n_estimators": int(nearest(merged["n_estimators"], SEARCH_SPACE["n_estimators"]["choices"])),
        "max_depth": nearest(merged["max_depth"], SEARCH_SPACE["max_depth"]["choices"]),
        "min_samples_leaf": int(nearest(merged["min_samples_leaf"], SEARCH_SPACE["min_samples_leaf"]["choices"])),
        "criterion": str(nearest(merged["criterion"], SEARCH_SPACE["criterion"]["choices"])),
        "max_features": str(nearest(merged["max_features"], SEARCH_SPACE["max_features"]["choices"])),
        "class_weight": str(nearest(merged["class_weight"], SEARCH_SPACE["class_weight"]["choices"])),
        "learning_rate": float(nearest(merged["learning_rate"], SEARCH_SPACE["learning_rate"]["choices"])),
        "C": float(nearest(merged["C"], SEARCH_SPACE["C"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    depth = "none" if cfg["max_depth"] is None else cfg["max_depth"]
    return (
        f"{cfg['model_family']}_n{cfg['n_estimators']}_d{depth}_leaf{cfg['min_samples_leaf']}"
        f"_crit{cfg['criterion']}_mf{cfg['max_features']}_cw{cfg['class_weight']}"
        f"_lr{cfg['learning_rate']}_C{cfg['C']}"
    ).replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["PYTHONPATH"] = f"{ROOT}:{ROOT / '.python_deps'}:{ROOT / 'repositories/binary-diffusion-tabular'}:{env.get('PYTHONPATH', '')}"
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--model-family {cfg['model_family']} "
            f"--n-estimators {cfg['n_estimators']} "
            f"--max-depth {'none' if cfg['max_depth'] is None else cfg['max_depth']} "
            f"--min-samples-leaf {cfg['min_samples_leaf']} "
            f"--criterion {cfg['criterion']} "
            f"--max-features {cfg['max_features']} "
            f"--class-weight {cfg['class_weight']} "
            f"--learning-rate {cfg['learning_rate']} "
            f"--C {cfg['C']} "
            "--seed 42",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"binary_diffusion_adult_rf eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def training_log(history: list[dict[str, Any]], current: dict[str, Any], baseline: float) -> str:
    lines = [
        "Task: Binary Diffusion Adult Income tabular classification downstream model tuning.",
        "Metric: held-out Adult Income test accuracy percent, higher is better.",
        "Paper anchor: Binary Diffusion README reports Adult Income RF accuracy 85.74.",
        "Budget protocol: fixed official train/test split and seed=42; tune only sklearn classifier hyperparameters.",
        f"Budget baseline accuracy={baseline:.4f}, config={BASE_CONFIG}.",
        f"Current config: {current}",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"test_accuracy_percent={m['test_accuracy_percent']:.4f} "
            f"train_accuracy_percent={m['train_accuracy_percent']:.4f} seconds={m['seconds']}"
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
            (item["trial"], item["metrics"]["test_accuracy_percent"], item["config"], item["kind"]) for item in history
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
    except Exception as exc:
        fallback = {"model_family": "rf", "n_estimators": 200, "max_depth": None, "min_samples_leaf": 1}
        return {
            "new_config": clamp_config({**current, **fallback}),
            "raw_new_config": fallback,
            "reasoning": f"Qwen decision failed; using RF fallback. Error: {exc!r}",
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
    budget_baseline = float(baseline_trial["metrics"]["test_accuracy_percent"])
    decision = decide_with_qwen(history, BASE_CONFIG, budget_baseline)
    final_config = clamp_config(decision["new_config"])
    final_trial = run_eval("final", 1, final_config)
    history.append(final_trial)
    final_acc = float(final_trial["metrics"]["test_accuracy_percent"])
    score = normalized_score(final_acc, budget_baseline)
    summary = {
        "agent": os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal"),
        "benchmark_name": "binary_diffusion_adult_rf",
        "repo": "binary-diffusion-tabular",
        "task": "Adult Income downstream classifier tuning on official Binary Diffusion split",
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "run_dir": str(OUT_DIR),
        "paper_anchor": PAPER_ANCHOR_ACC,
        "budget": {"metric": "test_accuracy_percent", "dataset": "Adult Income", "seed": 42, "baseline_config": BASE_CONFIG},
        "baseline_metrics": baseline_trial["metrics"],
        "final_metrics": final_trial["metrics"],
        "final_config": final_config,
        "decisions": [{
            "decision_number": 0,
            "old_config": BASE_CONFIG,
            "new_config": final_config,
            "raw_new_config": decision.get("raw_new_config"),
            "reasoning": decision.get("reasoning"),
            "confidence": decision.get("confidence"),
            "metadata": decision.get("metadata"),
        }],
        "decisions_made": 1,
        "history": history,
        "metric": "test_accuracy_percent",
        "higher_is_better": True,
        "direction": "higher_is_better",
        "agent_budget_result": final_acc,
        "official_budget_baseline": budget_baseline,
        "paper_anchor_source": "binary-diffusion-tabular README downstream results table.",
        "score": {
            "normalized_score": score,
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
