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
FORMAL_DIR = ROOT / "tasks/main/tabmini_molecular_biology_promoters_auc"
EVAL_SCRIPT = FORMAL_DIR / "eval_tabmini_molecular_biology_promoters_auc.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b"))) / "tabmini_molecular_biology_promoters_auc"
RUN_ID = os.environ.get("RUN_ID") or f"tabmini_molecular_biology_promoters_auc_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "tabmini_molecular_biology_promoters_auc_QwenLocal_results.json"

PAPER_ANCHOR_AUC = 0.93
BASE_CONFIG = {
    "model_family": "logreg",
    "scaler": "minmax",
    "C": 0.5,
    "max_depth": None,
    "min_samples_leaf": 1,
    "criterion": "gini",
    "class_weight": "none",
    "n_estimators": 100,
    "max_features": "sqrt",
}
SEARCH_SPACE = {
    "model_family": {"choices": ["logreg", "tree", "forest", "extra_trees"]},
    "scaler": {"choices": ["minmax", "standard", "none"]},
    "C": {"choices": [0.01, 0.1, 0.5, 1.0, 10.0]},
    "max_depth": {"choices": [1, 2, 3, 4, None]},
    "min_samples_leaf": {"choices": [1, 2, 4]},
    "criterion": {"choices": ["gini", "entropy"]},
    "class_weight": {"choices": ["none", "balanced"]},
    "n_estimators": {"choices": [50, 100, 200]},
    "max_features": {"choices": ["sqrt", "log2", "none"]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "tabmini_molecular_biology_promoters_auc", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
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
    aliases = {"model": "model_family", "family": "model_family", "classifier": "model_family", "regularization_C": "C", "c": "C", "depth": "max_depth", "leaf": "min_samples_leaf", "min_leaf": "min_samples_leaf", "trees": "n_estimators", "num_trees": "n_estimators"}
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "model_family": str(nearest(merged["model_family"], SEARCH_SPACE["model_family"]["choices"])),
        "scaler": str(nearest(merged["scaler"], SEARCH_SPACE["scaler"]["choices"])),
        "C": float(nearest(merged["C"], SEARCH_SPACE["C"]["choices"])),
        "max_depth": nearest(merged["max_depth"], SEARCH_SPACE["max_depth"]["choices"]),
        "min_samples_leaf": int(nearest(merged["min_samples_leaf"], SEARCH_SPACE["min_samples_leaf"]["choices"])),
        "criterion": str(nearest(merged["criterion"], SEARCH_SPACE["criterion"]["choices"])),
        "class_weight": str(nearest(merged["class_weight"], SEARCH_SPACE["class_weight"]["choices"])),
        "n_estimators": int(nearest(merged["n_estimators"], SEARCH_SPACE["n_estimators"]["choices"])),
        "max_features": str(nearest(merged["max_features"], SEARCH_SPACE["max_features"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    depth = "none" if cfg["max_depth"] is None else cfg["max_depth"]
    return (f"{cfg['model_family']}_sc{cfg['scaler']}_C{cfg['C']}_d{depth}_leaf{cfg['min_samples_leaf']}_crit{cfg['criterion']}_cw{cfg['class_weight']}_n{cfg['n_estimators']}_mf{cfg['max_features']}").replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["PYTHONPATH"] = f"{ROOT}:{ROOT / '.python_deps'}:{ROOT / 'repositories/TabMini'}:{env.get('PYTHONPATH', '')}"
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} --results-dir {trial_dir} --model-family {cfg['model_family']} --scaler {cfg['scaler']} "
            f"--C {cfg['C']} --max-depth {'none' if cfg['max_depth'] is None else cfg['max_depth']} "
            f"--min-samples-leaf {cfg['min_samples_leaf']} --criterion {cfg['criterion']} --class-weight {cfg['class_weight']} "
            f"--n-estimators {cfg['n_estimators']} --max-features {cfg['max_features']} --cv 2 --seed {42 + int(os.environ.get('AUTOREP_REPLICATE_SEED', '0'))}",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"TabMini eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


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
        "training_log": f"Task: TabMini molecular_biology_promoters binary classification. Metric: 2-fold ROC AUC, higher is better. Paper/repo anchor: TabMini 3600s AutoGluon ROC AUC 0.93. Budget baseline AUC={baseline:.4f}, config={current}.",
        "current_config": current,
        "metrics_history": [(item["trial"], item["metrics"]["test_auc"], item["config"], item["kind"]) for item in history],
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
        agent = QwenAgent(model_path=str(AGENT_MODEL), temperature=0.0, max_new_tokens=384, device_map="auto", torch_dtype="bfloat16", use_chat_template=False)
        decision = agent.decide(DecisionContext(**payload))
        raw_config = dict(decision.new_config)
        out = {"new_config": clamp_config({**current, **raw_config}), "raw_new_config": raw_config, "reasoning": decision.reasoning, "confidence": decision.confidence, "metadata": decision.metadata}
        del agent
        try:
            import torch
            torch.cuda.empty_cache()
        except Exception:
            pass
        return out
    except Exception as exc:
        fallback = {"model_family": "forest", "n_estimators": 100, "max_depth": None}
        return {"new_config": clamp_config({**current, **fallback}), "raw_new_config": fallback, "reasoning": f"Qwen decision failed; using forest fallback. Error: {exc!r}", "confidence": 0.0, "metadata": {"fallback": True, "error": repr(exc)}}


def normalized_score(value: float, baseline: float) -> float:
    denom = PAPER_ANCHOR_AUC - baseline
    if abs(denom) < 1e-12:
        return 0.0
    return (value - baseline) / denom


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    history = []
    baseline_trial = run_eval("baseline", 0, BASE_CONFIG)
    history.append(baseline_trial)
    budget_baseline = float(baseline_trial["metrics"]["test_auc"])
    decision = decide_with_qwen(history, BASE_CONFIG, budget_baseline)
    final_config = clamp_config(decision["new_config"])
    final_trial = run_eval("final", 1, final_config)
    history.append(final_trial)
    final_auc = float(final_trial["metrics"]["test_auc"])
    score = normalized_score(final_auc, budget_baseline)
    summary = {
        "agent": os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal"),
        "benchmark_name": "tabmini_molecular_biology_promoters_auc",
        "repo": "TabMini",
        "task": "molecular_biology_promoters low-data tabular classification",
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "run_dir": str(OUT_DIR),
        "paper_anchor": PAPER_ANCHOR_AUC,
        "budget": {"metric": "roc_auc", "dataset": "molecular_biology_promoters", "seed": 42, "baseline_config": BASE_CONFIG},
        "baseline_metrics": baseline_trial["metrics"],
        "final_metrics": final_trial["metrics"],
        "final_config": final_config,
        "decisions": [{"decision_number": 0, "old_config": BASE_CONFIG, "new_config": final_config, "raw_new_config": decision.get("raw_new_config"), "reasoning": decision.get("reasoning"), "confidence": decision.get("confidence"), "metadata": decision.get("metadata")}],
        "decisions_made": 1,
        "history": history,
        "metric": "roc_auc",
        "higher_is_better": True,
        "direction": "higher_is_better",
        "agent_budget_result": final_auc,
        "official_budget_baseline": budget_baseline,
        "paper_anchor_source": "TabMini plotting/results/test_scores_wide_3600.csv AutoGluon column.",
        "score": {"normalized_score": score, "official_budget_baseline": budget_baseline, "paper_anchor": PAPER_ANCHOR_AUC, "direction": "higher_is_better"},
        "success": True,
    }
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(summary, indent=2))
    (OUT_DIR / "summary.json").write_text(json.dumps(summary, indent=2))
    print("FINAL_RESULT " + json.dumps(summary, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
