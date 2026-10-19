#!/usr/bin/env python3
from __future__ import annotations

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
REPO_DIR = ROOT / "repositories/uni2ts"
MODEL_DIR = ROOT / "models/uni2ts/moirai-1.0-R-small"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "uni2ts_lsf_etth1"
RUN_ID = os.environ.get("RUN_ID") or f"uni2ts_lsf_etth1_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "uni2ts_lsf_etth1_QwenLocal_results.json"

PAPER_ANCHOR = 0.375
OFFICIAL_BUDGET_BASELINE = 1.155
BASE_CONFIG = {
    "num_samples": 1,
    "patch_size": 64,
    "context_length": 5000,
    "batch_size": 512,
}
SEARCH_SPACE = {
    "num_samples": {"choices": [1, 20, 100]},
    "patch_size": {"choices": [32, 64, 128]},
    "context_length": {"choices": [1000, 3000, 5000]},
    "batch_size": {"choices": [128, 256, 512]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "uni2ts_lsf_etth1", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)



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
        "samples": "num_samples",
        "n_samples": "num_samples",
        "sample_count": "num_samples",
        "context": "context_length",
        "ctx": "context_length",
        "patch": "patch_size",
        "bs": "batch_size",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "num_samples": int(nearest(merged["num_samples"], SEARCH_SPACE["num_samples"]["choices"])),
        "patch_size": int(nearest(merged["patch_size"], SEARCH_SPACE["patch_size"]["choices"])),
        "context_length": int(nearest(merged["context_length"], SEARCH_SPACE["context_length"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
    }


def parse_metrics(text: str) -> dict[str, float]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    header_idx = None
    for idx, line in enumerate(lines):
        if "MSE[mean]" in line and "MSE[0.5]" in line and "MAE[0.5]" in line:
            header_idx = idx
    if header_idx is None or header_idx + 1 >= len(lines):
        raise RuntimeError("could not locate Uni2TS metrics table in log")
    headers = lines[header_idx].split()
    values = lines[header_idx + 1].split()
    if values and values[0] == "None":
        values = values[1:]
    return {key: float(value) for key, value in zip(headers, values)}


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_ns{cfg['num_samples']}_p{cfg['patch_size']}_ctx{cfg['context_length']}_b{cfg['batch_size']}"
    log_path = trial_dir / "eval.log"
    metrics_path = trial_dir / "metrics.json"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["LSF_PATH"] = str(ROOT / "data/formal/uni2ts_lsf")
        env["PYTHONPATH"] = f"{REPO_DIR / 'src'}:{env.get('PYTHONPATH', '')}"
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("UNI2TS_CUDA_VISIBLE_DEVICES", "0")
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            "python -m cli.eval "
            "run_name=autorep_agent_moirai_small_pl96 "
            "model=moirai_1.0_R_small "
            f"model.module.pretrained_model_name_or_path={MODEL_DIR} "
            f"model.patch_size={cfg['patch_size']} "
            f"model.context_length={cfg['context_length']} "
            f"model.num_samples={cfg['num_samples']} "
            "data=lsf_test data.dataset_name=ETTh1 data.mode=M data.prediction_length=96 "
            f"batch_size={cfg['batch_size']} device=cuda",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(REPO_DIR), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"Uni2TS eval failed rc={proc.returncode}")
        metrics = parse_metrics(text)
        metrics_path.write_text(json.dumps({"metrics": metrics, "seconds": round(time.time() - started, 3), "config": cfg}, indent=2))
    return {
        "trial": trial_idx,
        "kind": kind,
        "config": cfg,
        **load_json(metrics_path),
        "output_dir": str(trial_dir),
    }


def training_log(history: list[dict[str, Any]], current: dict[str, Any]) -> str:
    history = history[:1]  # No-feedback: expose only the baseline observation.
    lines = [
        "Task: Uni2TS MOIRAI-small zero-shot time-series forecasting on LSF ETTh1, prediction length 96, multivariate mode.",
        "Metric: MSE[0.5], lower is better.",
        f"Paper anchor: {PAPER_ANCHOR} using num_samples=100, patch_size=64, context_length=5000.",
        f"Budget baseline: {OFFICIAL_BUDGET_BASELINE} using num_samples=1, patch_size=64, context_length=5000.",
        "You may tune inference hyperparameters only. More samples usually improves median forecast quality but costs more memory/time.",
        f"Current config: {current}",
    ]
    for item in history:
        lines.append(f"Trial {item['trial']} {item['kind']}: config={item['config']} MSE[0.5]={item['metrics']['MSE[0.5]']:.3f} MAE[0.5]={item['metrics']['MAE[0.5]']:.3f}")
    return "\n".join(lines)


def decide_with_qwen(history: list[dict[str, Any]], current: dict[str, Any]) -> dict[str, Any]:

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
    from agenthpobench.agents.open_source.qwen_agent import QwenAgent
    from agenthpobench.core.agent_base import DecisionContext

    payload = {
        "training_log": training_log(history, current),
        "current_config": current,
        "metrics_history": [(item["trial"], item["metrics"]["MSE[0.5]"], item["config"], item["kind"]) for item in history],
        "budget_remaining": 1,
        "total_budget": 2,
        "search_space": SEARCH_SPACE,
        "epoch": 1,
        "decision_number": 0,
    }
    (OUT_DIR / "logs").mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "qwen_context_0.json").write_text(json.dumps(payload, indent=2))
    try:
        os.environ["CUDA_VISIBLE_DEVICES"] = os.environ.get("QWEN_CUDA_VISIBLE_DEVICES", "0")
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
            "new_config": {**current, "num_samples": 100, "batch_size": 256},
            "raw_new_config": {"num_samples": 100, "batch_size": 256},
            "reasoning": f"Fallback after Qwen decision failure: {exc}. Increase num_samples to the official paper setting.",
            "confidence": 0.5,
            "metadata": {"fallback": True, "error": str(exc)},
        }
    (OUT_DIR / "qwen_decision_0.json").write_text(json.dumps(raw, indent=2))
    return raw


def normalized_score(value: float) -> float:
    return (OFFICIAL_BUDGET_BASELINE - value) / (OFFICIAL_BUDGET_BASELINE - PAPER_ANCHOR)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    history = [run_eval("proxy", 0, BASE_CONFIG)]
    decision = decide_with_qwen(history, BASE_CONFIG)
    final_config = clamp_config(decision["new_config"])
    final = run_eval("final", 0, final_config)
    result = {
        "id": "uni2ts_lsf_etth1_moirai_small",
        "repo": "uni2ts",
        "metric": "MSE[0.5]",
        "direction": "lower_is_better",
        "official_budget_baseline": OFFICIAL_BUDGET_BASELINE,
        "paper_anchor": PAPER_ANCHOR,
        "agent_budget_result": final["metrics"]["MSE[0.5]"],
        "normalized_score": normalized_score(final["metrics"]["MSE[0.5]"]),
        "agent_decisions_made": 1,
        "agent_final_config": final_config,
        "agent_internal_baseline": history[0]["metrics"]["MSE[0.5]"],
        "agent_internal_vs_official_budget_delta": history[0]["metrics"]["MSE[0.5]"] - OFFICIAL_BUDGET_BASELINE,
        "agent_success": True,
        "decision": decision,
        "history": history,
        "final": final,
        "status": "scored",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
