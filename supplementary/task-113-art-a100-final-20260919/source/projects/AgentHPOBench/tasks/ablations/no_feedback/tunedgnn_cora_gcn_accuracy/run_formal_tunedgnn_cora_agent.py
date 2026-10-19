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
FORMAL_DIR = ROOT / "tasks/ablations/no_feedback/tunedgnn_cora_gcn_accuracy"
EVAL_SCRIPT = FORMAL_DIR / "eval_tunedgnn_cora.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", str(ROOT / "models/Qwen/Qwen3-8B")))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/main/qwen3_8b_seed0_final30"))) / "tunedgnn_cora_gcn_accuracy"
RUN_ID = os.environ.get("RUN_ID") or f"tunedgnn_cora_gcn_accuracy_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE_AGENT_NAME = os.environ.get("RESULT_FILE_AGENT_NAME", "QwenLocal")
RESULT_FILE = RESULT_ROOT / f"tunedgnn_cora_gcn_accuracy_{RESULT_FILE_AGENT_NAME}_results.json"

PAPER_ANCHOR_ACC = 85.10
FIXED_BUDGET = {
    "epochs": int(os.environ.get("TUNEDGNN_EPOCHS", "50")),
    "seed": int(os.environ.get("TUNEDGNN_SEED", "123")),
    "label_num_per_class": int(os.environ.get("TUNEDGNN_LABEL_NUM_PER_CLASS", "20")),
    "valid_num": int(os.environ.get("TUNEDGNN_VALID_NUM", "500")),
    "test_num": int(os.environ.get("TUNEDGNN_TEST_NUM", "1000")),
}
INTERVENTIONS = int(os.environ.get("AUTOREP_INTERVENTIONS", "5"))
BASE_CONFIG = {
    "lr": 0.001,
    "hidden_channels": 512,
    "local_layers": 3,
    "dropout": 0.7,
    "weight_decay": 5e-4,
    "layer_norm": False,
    "residual": False,
}
SEARCH_SPACE = {
    "lr": {"choices": [0.0005, 0.001, 0.002, 0.005]},
    "hidden_channels": {"choices": [128, 256, 512]},
    "local_layers": {"choices": [2, 3, 4]},
    "dropout": {"choices": [0.3, 0.5, 0.7]},
    "weight_decay": {"choices": [0.0, 0.0005, 0.001]},
    "layer_norm": {"choices": [False, True]},
    "residual": {"choices": [False, True]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "tunedgnn_cora_gcn_accuracy", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)

AGENT_SEARCH_SPACE = {
    **SEARCH_SPACE,
    "learning_rate": SEARCH_SPACE["lr"],
    "eta": SEARCH_SPACE["lr"],
    "hidden": SEARCH_SPACE["hidden_channels"],
    "hidden_dim": SEARCH_SPACE["hidden_channels"],
    "hidden_size": SEARCH_SPACE["hidden_channels"],
    "layers": SEARCH_SPACE["local_layers"],
    "num_layers": SEARCH_SPACE["local_layers"],
    "n_layers": SEARCH_SPACE["local_layers"],
    "dropout_rate": SEARCH_SPACE["dropout"],
    "wd": SEARCH_SPACE["weight_decay"],
    "weight_decay_rate": SEARCH_SPACE["weight_decay"],
    "ln": SEARCH_SPACE["layer_norm"],
    "use_layer_norm": SEARCH_SPACE["layer_norm"],
    "res": SEARCH_SPACE["residual"],
    "use_residual": SEARCH_SPACE["residual"],
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


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
        "eta": "lr",
        "hidden": "hidden_channels",
        "hidden_dim": "hidden_channels",
        "hidden_size": "hidden_channels",
        "layers": "local_layers",
        "num_layers": "local_layers",
        "n_layers": "local_layers",
        "dropout_rate": "dropout",
        "wd": "weight_decay",
        "weight_decay_rate": "weight_decay",
        "ln": "layer_norm",
        "use_layer_norm": "layer_norm",
        "res": "residual",
        "use_residual": "residual",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "lr": float(nearest(merged["lr"], SEARCH_SPACE["lr"]["choices"])),
        "hidden_channels": int(nearest(merged["hidden_channels"], SEARCH_SPACE["hidden_channels"]["choices"])),
        "local_layers": int(nearest(merged["local_layers"], SEARCH_SPACE["local_layers"]["choices"])),
        "dropout": float(nearest(merged["dropout"], SEARCH_SPACE["dropout"]["choices"])),
        "weight_decay": float(nearest(merged["weight_decay"], SEARCH_SPACE["weight_decay"]["choices"])),
        "layer_norm": bool(nearest(merged["layer_norm"], SEARCH_SPACE["layer_norm"]["choices"])),
        "residual": bool(nearest(merged["residual"], SEARCH_SPACE["residual"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return (
        f"lr{cfg['lr']}_h{cfg['hidden_channels']}_l{cfg['local_layers']}"
        f"_do{cfg['dropout']}_wd{cfg['weight_decay']}_ln{int(cfg['layer_norm'])}_res{int(cfg['residual'])}"
    ).replace(".", "p")


def metric_value(metrics: dict[str, Any]) -> float:
    return float(metrics["test_accuracy_percent_at_best_val"])


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("TUNEDGNN_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "0"))
        env["PYTHONPATH"] = f"{ROOT}:{ROOT / '.python_deps'}:{ROOT / 'repositories/tunedGNN'}:{env.get('PYTHONPATH', '')}"
        env.setdefault("TOKENIZERS_PARALLELISM", "false")
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--epochs {FIXED_BUDGET['epochs']} "
            f"--seed {FIXED_BUDGET['seed']} "
            f"--label-num-per-class {FIXED_BUDGET['label_num_per_class']} "
            f"--valid-num {FIXED_BUDGET['valid_num']} "
            f"--test-num {FIXED_BUDGET['test_num']} "
            f"--lr {cfg['lr']} "
            f"--hidden-channels {cfg['hidden_channels']} "
            f"--local-layers {cfg['local_layers']} "
            f"--dropout {cfg['dropout']} "
            f"--weight-decay {cfg['weight_decay']} "
            "--device cuda:0 "
            + ("--layer-norm " if cfg["layer_norm"] else "")
            + ("--residual " if cfg["residual"] else ""),
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"tunedGNN Cora eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def training_log(history: list[dict[str, Any]], current: dict[str, Any], baseline: float, decision_idx: int) -> str:
    history = history[:1]  # No-feedback: expose only the baseline observation.
    best = max(history, key=lambda item: metric_value(item["metrics"]))
    lines = [
        "Task: tunedGNN Cora node classification with a GCN.",
        "Metric: Cora test accuracy percent at best validation epoch, higher is better.",
        "Paper anchor: 85.10 +/- 0.67 from tunedGNN NeurIPS 2024 medium_graph README for Cora GCN.",
        f"Budget protocol: fixed epochs={FIXED_BUDGET['epochs']} (1/10 of the paper default 500), seed={FIXED_BUDGET['seed']}; do not change dataset, split, or epoch budget.",
        f"Budget baseline accuracy={baseline:.4f}, official config={BASE_CONFIG}.",
        "Tune only lr, hidden_channels, local_layers, dropout, weight_decay, layer_norm, and residual.",
        f"Current config before decision {decision_idx}: {current}",
        f"Best observed config so far: {best['config']} with accuracy={metric_value(best['metrics']):.4f}.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"test_accuracy_percent_at_best_val={m['test_accuracy_percent_at_best_val']:.4f} "
            f"best_val_accuracy_percent={m['best_val_accuracy_percent']:.4f} "
            f"best_epoch={m['best_epoch']} seconds={m['seconds']}"
        )
    return "\n".join(lines)


def fallback_config(decision_idx: int, current: dict[str, Any]) -> dict[str, Any]:
    candidates = [
        {"lr": 0.002, "hidden_channels": 512, "local_layers": 3, "dropout": 0.5, "weight_decay": 0.0005, "layer_norm": False, "residual": False},
        {"lr": 0.001, "hidden_channels": 512, "local_layers": 4, "dropout": 0.5, "weight_decay": 0.0005, "layer_norm": True, "residual": True},
        {"lr": 0.0005, "hidden_channels": 256, "local_layers": 3, "dropout": 0.7, "weight_decay": 0.001, "layer_norm": True, "residual": False},
        {"lr": 0.005, "hidden_channels": 256, "local_layers": 2, "dropout": 0.3, "weight_decay": 0.0, "layer_norm": False, "residual": True},
        {"lr": 0.001, "hidden_channels": 128, "local_layers": 4, "dropout": 0.5, "weight_decay": 0.0005, "layer_norm": True, "residual": True},
    ]
    return clamp_config({**current, **candidates[decision_idx % len(candidates)]})


def decide_with_qwen(history: list[dict[str, Any]], current: dict[str, Any], baseline: float, decision_idx: int) -> dict[str, Any]:

    history = history[:1]  # No-feedback: expose only the baseline observation.
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
        from agenthpobench.agents.open_source.qwen_agent import QwenAgent
        from agenthpobench.core.agent_base import DecisionContext

        os.environ["CUDA_VISIBLE_DEVICES"] = os.environ.get("QWEN_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "0"))
        use_chat_template = os.environ.get("AUTOREP_USE_CHAT_TEMPLATE", "0").lower() in {"1", "true", "yes"}
        agent = QwenAgent(
            model_path=str(AGENT_MODEL),
            temperature=0.0,
            max_new_tokens=int(os.environ.get("AUTOREP_AGENT_MAX_NEW_TOKENS", "384")),
            device_map="auto",
            torch_dtype=os.environ.get("AUTOREP_AGENT_TORCH_DTYPE", "bfloat16"),
            use_chat_template=use_chat_template,
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
    except Exception as exc:  # noqa: BLE001
        fallback = fallback_config(decision_idx, current)
        return {
            "new_config": fallback,
            "raw_new_config": fallback,
            "reasoning": f"Agent decision failed; using deterministic tunedGNN fallback candidate. Error: {exc!r}",
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
        "benchmark_name": "tunedgnn_cora_gcn_accuracy",
        "repo": "tunedGNN",
        "repo_url": "https://github.com/LUOyk1999/tunedGNN",
        "task": "Cora GCN node classification",
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "run_dir": str(OUT_DIR),
        "paper_anchor": PAPER_ANCHOR_ACC,
        "budget": {
            **FIXED_BUDGET,
            "metric": "test_accuracy_percent_at_best_val",
            "paper_default_epochs": 500,
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
        "metric": "test_accuracy_percent_at_best_val",
        "higher_is_better": True,
        "direction": "higher_is_better",
        "agent_budget_result": best_acc,
        "final_agent_budget_result": final_acc,
        "official_budget_baseline": budget_baseline,
        "paper_anchor_source": "tunedGNN medium_graph README: Cora GCN 85.10 +/- 0.67; run_gnn.sh official Cora config.",
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
