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
FORMAL_DIR = ROOT / "tasks/main/noisygl_cora_uniform30_gcn"
EVAL_SCRIPT = FORMAL_DIR / "eval_noisygl_cora_gcn.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "noisygl_cora_uniform30_gcn"
RUN_ID = os.environ.get("RUN_ID") or f"noisygl_cora_uniform30_gcn_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "noisygl_cora_uniform30_gcn_QwenLocal_results.json"

PAPER_ANCHOR_ACC = 71.06
FIXED_BUDGET = {
    "epochs": int(os.environ.get("NOISYGL_EPOCHS", "80")),
    "noise_rate": float(os.environ.get("NOISYGL_NOISE_RATE", "0.3")),
    "seed": int(os.environ.get("NOISYGL_SEED", "3000")),
    "noise_seed": int(os.environ.get("NOISYGL_NOISE_SEED", "3000")),
}
BASE_CONFIG = {
    "lr": 0.01,
    "weight_decay": 5e-4,
    "dropout": 0.5,
    "hidden_dim": 64,
}
SEARCH_SPACE = {
    "lr": {"choices": [0.003, 0.005, 0.01, 0.02]},
    "weight_decay": {"choices": [0.0, 5e-4, 1e-3, 5e-3]},
    "dropout": {"choices": [0.3, 0.5, 0.7]},
    "hidden_dim": {"choices": [32, 64, 128]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "noisygl_cora_uniform30_gcn", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)




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
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "learning_rate": "lr",
        "eta": "lr",
        "wd": "weight_decay",
        "weight_decay_rate": "weight_decay",
        "dropout_rate": "dropout",
        "hidden": "hidden_dim",
        "n_hidden": "hidden_dim",
        "hidden_channels": "hidden_dim",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "lr": float(nearest(merged["lr"], SEARCH_SPACE["lr"]["choices"])),
        "weight_decay": float(nearest(merged["weight_decay"], SEARCH_SPACE["weight_decay"]["choices"])),
        "dropout": float(nearest(merged["dropout"], SEARCH_SPACE["dropout"]["choices"])),
        "hidden_dim": int(nearest(merged["hidden_dim"], SEARCH_SPACE["hidden_dim"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return f"lr{cfg['lr']}_wd{cfg['weight_decay']}_do{cfg['dropout']}_h{cfg['hidden_dim']}".replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("NOISYGL_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "1"))
        env["PYTHONPATH"] = f"{ROOT}:{ROOT / '.python_deps'}:{ROOT / 'repositories/NoisyGL'}:{env.get('PYTHONPATH', '')}"
        env.setdefault("TOKENIZERS_PARALLELISM", "false")
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--epochs {FIXED_BUDGET['epochs']} "
            f"--noise-rate {FIXED_BUDGET['noise_rate']} "
            f"--noise-seed {FIXED_BUDGET['noise_seed']} "
            f"--seed {FIXED_BUDGET['seed']} "
            f"--hidden-dim {cfg['hidden_dim']} "
            f"--dropout {cfg['dropout']} "
            f"--lr {cfg['lr']} "
            f"--weight-decay {cfg['weight_decay']} "
            "--log-every 20",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"NoisyGL Cora GCN eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def training_log(history: list[dict[str, Any]], current: dict[str, Any], baseline: float) -> str:
    lines = [
        "Task: NoisyGL Cora node classification with GCN under 30% uniform label noise.",
        "Metric: clean Cora test accuracy percent, higher is better.",
        "Paper anchor: 71.06 test accuracy for GCN on Cora under 30% uniform noise from NoisyGL NeurIPS 2024 Table A1.",
        f"Budget protocol: fixed epochs={FIXED_BUDGET['epochs']}; do not change epochs, split, noise type, or data.",
        f"Budget baseline accuracy={baseline:.4f}, config={BASE_CONFIG}.",
        "Tune only lr, weight_decay, dropout, and hidden_dim.",
        f"Current config: {current}",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"test_accuracy_percent={m['test_accuracy_percent']:.4f} "
            f"val_accuracy_percent={m['best_val_accuracy_percent']:.4f} "
            f"best_epoch={m['best_epoch']} seconds={m['seconds']}"
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
    from qwen_agent_multiseed_v2 import QwenAgent
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
    except Exception as exc:  # noqa: BLE001
        fallback = {"lr": 0.005, "weight_decay": 0.001, "dropout": 0.5, "hidden_dim": 64}
        return {
            "new_config": clamp_config(fallback),
            "raw_new_config": fallback,
            "reasoning": f"Qwen decision failed; using conservative NoisyGL fallback. Error: {exc!r}",
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
        "benchmark_name": "noisygl_cora_uniform30_gcn",
        "repo": "NoisyGL",
        "task": "Cora GCN node classification under 30% uniform label noise",
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "run_dir": str(OUT_DIR),
        "paper_anchor": PAPER_ANCHOR_ACC,
        "budget": {
            "epochs": FIXED_BUDGET["epochs"],
            "noise_rate": FIXED_BUDGET["noise_rate"],
            "metric": "test_accuracy_percent",
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
