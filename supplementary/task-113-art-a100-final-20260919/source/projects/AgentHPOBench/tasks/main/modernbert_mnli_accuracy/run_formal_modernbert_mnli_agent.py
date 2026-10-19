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
FORMAL_DIR = ROOT / "tasks/main/modernbert_mnli_accuracy"
EVAL_SCRIPT = FORMAL_DIR / "eval_modernbert_mnli.py"
MODEL_DIR = ROOT / "models/modernbert/ModernBERT-base"
DATA_DIR = ROOT / "data/paper_exact/modernbert_mnli/glue_mnli"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", str(ROOT / "models/Qwen/Qwen3-8B")))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/main/qwen3_8b_seed0_final30"))) / "modernbert_mnli_accuracy"
RUN_ID = os.environ.get("RUN_ID") or f"modernbert_mnli_accuracy_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE_AGENT_NAME = os.environ.get("RESULT_FILE_AGENT_NAME", "QwenLocal")
RESULT_FILE = RESULT_ROOT / f"modernbert_mnli_accuracy_{RESULT_FILE_AGENT_NAME}_results.json"

PAPER_ANCHOR_ACC = 90.4
INTERVENTIONS = int(os.environ.get("AUTOREP_INTERVENTIONS", "5"))
FIXED_BUDGET = {
    "max_steps": int(os.environ.get("MODERNBERT_MAX_STEPS", "120")),
    "train_samples": int(os.environ.get("MODERNBERT_TRAIN_SAMPLES", "4096")),
    "eval_samples": int(os.environ.get("MODERNBERT_EVAL_SAMPLES", "0")),
    "eval_split": os.environ.get("MODERNBERT_MNLI_EVAL_SPLIT", "validation_matched"),
    "eval_batch_size": int(os.environ.get("MODERNBERT_EVAL_BATCH_SIZE", "32")),
    "seed": int(os.environ.get("MODERNBERT_SEED", "42")),
}
BASE_CONFIG = {
    "learning_rate": 2e-5,
    "weight_decay": 0.01,
    "warmup_ratio": 0.1,
    "batch_size": 8,
    "max_length": 64,
}
SEARCH_SPACE = {
    "learning_rate": {"choices": [1e-5, 2e-5, 5e-5, 8e-5]},
    "weight_decay": {"choices": [1e-5, 1e-4, 1e-3, 1e-2]},
    "warmup_ratio": {"choices": [0.0, 0.06, 0.1]},
    "batch_size": {"choices": [8, 16, 32]},
    "max_length": {"choices": [64, 128, 256]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "modernbert_mnli_accuracy", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)

AGENT_SEARCH_SPACE = {
    **SEARCH_SPACE,
    "lr": SEARCH_SPACE["learning_rate"],
    "wd": SEARCH_SPACE["weight_decay"],
    "weight_decay_rate": SEARCH_SPACE["weight_decay"],
    "warmup": SEARCH_SPACE["warmup_ratio"],
    "bs": SEARCH_SPACE["batch_size"],
    "train_batch_size": SEARCH_SPACE["batch_size"],
    "seq_len": SEARCH_SPACE["max_length"],
    "sequence_length": SEARCH_SPACE["max_length"],
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
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        text = str(value).strip().lower()
        for item in choices:
            if str(item).lower() == text:
                return item
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "lr": "learning_rate",
        "learningrate": "learning_rate",
        "wd": "weight_decay",
        "weight_decay_rate": "weight_decay",
        "warmup": "warmup_ratio",
        "bs": "batch_size",
        "train_batch_size": "batch_size",
        "seq_len": "max_length",
        "sequence_length": "max_length",
    }
    merged = dict(BASE_CONFIG)
    for key, value in (config or {}).items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "learning_rate": float(nearest(merged["learning_rate"], SEARCH_SPACE["learning_rate"]["choices"])),
        "weight_decay": float(nearest(merged["weight_decay"], SEARCH_SPACE["weight_decay"]["choices"])),
        "warmup_ratio": float(nearest(merged["warmup_ratio"], SEARCH_SPACE["warmup_ratio"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
        "max_length": int(nearest(merged["max_length"], SEARCH_SPACE["max_length"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return (
        f"lr{cfg['learning_rate']}_wd{cfg['weight_decay']}_warm{cfg['warmup_ratio']}"
        f"_bs{cfg['batch_size']}_len{cfg['max_length']}"
    ).replace(".", "p")


def metric_value(metrics: dict[str, Any]) -> float:
    return float(metrics["accuracy_percent"])


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("MODERNBERT_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "0"))
        env["HF_DATASETS_OFFLINE"] = "1"
        env["TRANSFORMERS_OFFLINE"] = "1"
        env["TOKENIZERS_PARALLELISM"] = "false"
        env["PYTHONPATH"] = f"{ROOT}:{ROOT / '.python_deps'}:{env.get('PYTHONPATH', '')}"
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--model-dir {MODEL_DIR} "
            f"--data-dir {DATA_DIR} "
            f"--cache-dir {ROOT / 'cache'} "
            f"--results-dir {trial_dir} "
            f"--eval-split {FIXED_BUDGET['eval_split']} "
            f"--learning-rate {cfg['learning_rate']} "
            f"--weight-decay {cfg['weight_decay']} "
            f"--warmup-ratio {cfg['warmup_ratio']} "
            f"--batch-size {cfg['batch_size']} "
            f"--eval-batch-size {FIXED_BUDGET['eval_batch_size']} "
            f"--max-length {cfg['max_length']} "
            f"--max-steps {FIXED_BUDGET['max_steps']} "
            f"--train-samples {FIXED_BUDGET['train_samples']} "
            f"--eval-samples {FIXED_BUDGET['eval_samples']} "
            f"--seed {FIXED_BUDGET['seed']} "
            "--bf16",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text[-8000:], flush=True)
            raise RuntimeError(f"ModernBERT MNLI eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def training_log(history: list[dict[str, Any]], current: dict[str, Any], baseline: float, decision_idx: int) -> str:
    best = max(history, key=lambda item: metric_value(item["metrics"]))
    lines = [
        "Task: ModernBERT-base fine-tuning on GLUE MNLI validation_matched.",
        "Metric: validation_matched accuracy percent, higher is better.",
        "Paper anchor: ModernBERT paper Table 5 reports ModernBERT-base MNLI-m dev accuracy 90.4.",
        f"Budget protocol: fixed max_steps={FIXED_BUDGET['max_steps']}, train_samples={FIXED_BUDGET['train_samples']}, eval_split={FIXED_BUDGET['eval_split']}; do not change data, model family, or budget fields.",
        f"Budget baseline accuracy={baseline:.4f}, baseline config={BASE_CONFIG}.",
        "Tune only learning_rate, weight_decay, warmup_ratio, batch_size, and max_length.",
        f"Current config before decision {decision_idx}: {current}",
        f"Best observed config so far: {best['config']} with accuracy={metric_value(best['metrics']):.4f}.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"accuracy_percent={m['accuracy_percent']:.4f} eval_loss={m['eval_loss']:.6f} "
            f"train_loss_final={m.get('train_loss_final')} seconds={m.get('seconds')}"
        )
    return "\n".join(lines)


def fallback_config(decision_idx: int, current: dict[str, Any]) -> dict[str, Any]:
    candidates = [
        {"learning_rate": 5e-5, "weight_decay": 0.001, "warmup_ratio": 0.06, "batch_size": 16, "max_length": 128},
        {"learning_rate": 8e-5, "weight_decay": 1e-5, "warmup_ratio": 0.06, "batch_size": 16, "max_length": 128},
        {"learning_rate": 2e-5, "weight_decay": 0.0001, "warmup_ratio": 0.1, "batch_size": 32, "max_length": 128},
        {"learning_rate": 1e-5, "weight_decay": 0.01, "warmup_ratio": 0.0, "batch_size": 32, "max_length": 256},
        {"learning_rate": 5e-5, "weight_decay": 1e-5, "warmup_ratio": 0.0, "batch_size": 8, "max_length": 256},
    ]
    return clamp_config({**current, **candidates[decision_idx % len(candidates)]})


def decide_with_qwen(history: list[dict[str, Any]], current: dict[str, Any], baseline: float, decision_idx: int) -> dict[str, Any]:

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
        from qwen_agent_multiseed_v2 import QwenAgent
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
            "reasoning": f"Agent decision failed; using deterministic ModernBERT fallback candidate. Error: {exc!r}",
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
        "benchmark_name": "modernbert_mnli_accuracy",
        "repo": "ModernBERT",
        "repo_url": "https://github.com/AnswerDotAI/ModernBERT",
        "task": "GLUE MNLI fine-tuning",
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "run_dir": str(OUT_DIR),
        "paper_anchor": PAPER_ANCHOR_ACC,
        "budget": {
            **FIXED_BUDGET,
            "metric": "accuracy_percent",
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
        "metric": "accuracy_percent",
        "higher_is_better": True,
        "direction": "higher_is_better",
        "agent_budget_result": best_acc,
        "final_agent_budget_result": final_acc,
        "official_budget_baseline": budget_baseline,
        "paper_anchor_source": "ModernBERT paper Table 5: ModernBERT-base MNLI-m dev accuracy 90.4.",
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
