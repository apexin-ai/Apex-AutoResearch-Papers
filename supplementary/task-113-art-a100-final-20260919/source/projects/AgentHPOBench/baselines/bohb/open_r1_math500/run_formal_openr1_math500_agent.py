#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import shlex
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


AUTOREP_ROOT = Path(".")
FORMAL_DIR = AUTOREP_ROOT / "baselines/bohb/open_r1_math500"
EVAL_SCRIPT = FORMAL_DIR / "openr1_math500_eval.py"
DATA_FILE = AUTOREP_ROOT / "data/paper_exact/open_r1_math500/math_500/test.jsonl"
EVAL_MODEL = AUTOREP_ROOT / "models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
AGENT_MODEL = os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B")
BUDGET_BASELINES = (
    AUTOREP_ROOT
    / "results/formal_baselines/budget_protocol/scoreable_benchmark_manifest_20260505.json"
)

RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(AUTOREP_ROOT / "results/formal_agent/qwen3_32b"))) / "open_r1_math500"
RUN_ID = os.environ.get("RUN_ID") or f"open_r1_math500_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "open_r1_math500_QwenLocal_results.json"

PAPER_ANCHOR = 83.1
BASE_CONFIG = {
    "max_new_tokens": 512,
    "temperature": 0.0,
    "top_p": 1.0,
}
SEARCH_SPACE = {
    "max_new_tokens": {"choices": [512, 1024, 2048]},
    "temperature": {"choices": [0.0, 0.3, 0.6]},
    "top_p": {"choices": [0.8, 0.95, 1.0]},
}
PROXY_LIMIT = int(os.environ.get("OPENR1_PROXY_LIMIT", "64"))
PROXY_TRIALS = int(os.environ.get("OPENR1_PROXY_TRIALS", "2"))
FINAL_LIMIT = int(os.environ.get("OPENR1_FINAL_LIMIT", "0"))
DECIDE_CONDA_ENV = os.environ.get("OPENR1_DECIDE_CONDA_ENV", "autorep-vlm2vec")


def setup_imports() -> None:
    sys.path.insert(0, str(AUTOREP_ROOT))
    deps = AUTOREP_ROOT / ".python_deps"
    if deps.exists():
        sys.path.insert(0, str(deps))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def budget_record() -> dict[str, Any] | None:
    if not BUDGET_BASELINES.exists():
        return None
    doc = load_json(BUDGET_BASELINES)
    for record in doc.get("scoreable_records", doc.get("records", [])):
        if record.get("id") == "open_r1_math500_qwen1p5b":
            return record
    return None


def nearest(value: Any, choices: list[Any]) -> Any:
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "max_tokens": "max_new_tokens",
        "max_output_tokens": "max_new_tokens",
        "tokens": "max_new_tokens",
        "temp": "temperature",
        "top_p_value": "top_p",
    }
    out = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in out:
            out[mapped] = value
    return {
        "max_new_tokens": int(nearest(out["max_new_tokens"], SEARCH_SPACE["max_new_tokens"]["choices"])),
        "temperature": float(nearest(out["temperature"], SEARCH_SPACE["temperature"]["choices"])),
        "top_p": float(nearest(out["top_p"], SEARCH_SPACE["top_p"]["choices"])),
    }


def config_slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    temp = str(cfg["temperature"]).replace(".", "p")
    top_p = str(cfg["top_p"]).replace(".", "p")
    return f"tok{cfg['max_new_tokens']}_temp{temp}_topp{top_p}"


def run_subprocess(cmd: list[str], env: dict[str, str], log_path: Path) -> str:
    started = time.time()
    print("COMMAND:", " ".join(cmd), flush=True)
    proc = subprocess.run(
        cmd,
        cwd=str(AUTOREP_ROOT),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    text = proc.stdout.decode("utf-8", errors="replace")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(text)
    print(text, flush=True)
    print(f"COMMAND_RC={proc.returncode} seconds={time.time() - started:.1f}", flush=True)
    if proc.returncode != 0:
        raise RuntimeError(f"command failed rc={proc.returncode}: {' '.join(cmd)}")
    return text


def run_eval(kind: str, trial_idx: int, config: dict[str, Any], limit: int) -> dict[str, Any]:
    config = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{config_slug(config)}"
    result_path = trial_dir / "metrics.json"
    if not result_path.exists():
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("OPENR1_CUDA_VISIBLE_DEVICES", "1")
        env.setdefault("TOKENIZERS_PARALLELISM", "false")
        env["PATH"] = (
            f"{env.get('CONDA_ROOT', '/opt/miniconda3')}/envs/autorep-open-r1/bin:"
            f"{env.get('PATH', '')}"
        )
        env.setdefault("VLLM_USE_V1", "0")
        env.setdefault("VLLM_WORKER_MULTIPROC_METHOD", "spawn")
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-open-r1 && "
            f"python {EVAL_SCRIPT} "
            f"--model {EVAL_MODEL} "
            f"--data {DATA_FILE} "
            f"--output {result_path} "
            f"--predictions {trial_dir / 'predictions.jsonl'} "
            f"--limit {limit} "
            f"--max-new-tokens {config['max_new_tokens']} "
            f"--temperature {config['temperature']} "
            f"--top-p {config['top_p']} "
            "--max-model-len 4096 "
            f"--gpu-memory-utilization {os.environ.get('OPENR1_GPU_MEMORY_UTILIZATION', '0.20')} "
            "--dtype bfloat16",
        ]
        run_subprocess(cmd, env, OUT_DIR / "logs" / f"{kind}_trial{trial_idx}.log")
    metrics = load_json(result_path)
    return {
        "trial": trial_idx,
        "kind": kind,
        "config": config,
        "metrics": metrics,
        "output_dir": str(trial_dir),
    }


def format_training_log(history: list[dict[str, Any]], current_config: dict[str, Any]) -> str:
    record = budget_record()
    official = None if record is None else record.get("official_budget_baseline")
    lines = [
        "Task: open-r1 MATH-500 evaluation for DeepSeek-R1-Distill-Qwen-1.5B.",
        "Metric: MATH-500 exact-match accuracy_percent, higher is better.",
        f"Paper anchor: {PAPER_ANCHOR} from open-r1 README LightEval reproduction table.",
        f"Official budget baseline: {official}. Base config: {BASE_CONFIG}.",
        "You may tune decoding only. Higher max_new_tokens can improve reasoning but costs more and may overrun the budget.",
        f"Current config: {current_config}",
    ]
    for item in history[-6:]:
        metrics = item["metrics"]
        lines.append(
            "Trial {trial}: kind={kind}, config={config}, accuracy={acc:.3f}, correct={correct}/{total}".format(
                trial=item["trial"],
                kind=item["kind"],
                config=item["config"],
                acc=float(metrics["accuracy_percent"]),
                correct=int(metrics["num_correct"]),
                total=int(metrics["num_total"]),
            )
        )
    return "\n".join(lines)


def decide_with_qwen(history: list[dict[str, Any]], config: dict[str, Any], budget_remaining: int, decision_number: int) -> dict[str, Any]:

    import os as _tpe_os
    if _tpe_os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower() in {"tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
        import sys as _tpe_sys
        from pathlib import Path as _TpePath
        _tpe_sys.path.insert(0, str(_TpePath(__file__).resolve().parents[1]))
        from tpe_backend import tpe_decision_from_call
        return tpe_decision_from_call(globals().get("TASK_ID", _TpePath(__file__).resolve().parent.name), locals(), globals())
    payload = {
        "training_log": format_training_log(history, config),
        "current_config": config,
        "metrics_history": [
            (item["trial"], item["metrics"], item["config"], item["kind"]) for item in history
        ],
        "budget_remaining": budget_remaining,
        "total_budget": PROXY_TRIALS + 1,
        "search_space": SEARCH_SPACE,
        "epoch": decision_number + 1,
        "decision_number": decision_number,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    context_path = OUT_DIR / f"qwen_context_{decision_number}.json"
    context_path.write_text(json.dumps(payload, indent=2, sort_keys=True))
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = os.environ.get("QWEN_CUDA_VISIBLE_DEVICES", "1")
    env.setdefault("TRANSFORMERS_OFFLINE", "1")
    env.setdefault("HF_HUB_OFFLINE", "1")
    env.setdefault("TOKENIZERS_PARALLELISM", "false")
    env["PYTHONPATH"] = f"{AUTOREP_ROOT}:{AUTOREP_ROOT / '.python_deps'}:{env.get('PYTHONPATH', '')}"
    cmd = [
        "bash",
        "-lc",
        "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
        f"conda activate {shlex.quote(DECIDE_CONDA_ENV)} && "
        f"python {Path(__file__).resolve()} --decide {context_path}",
    ]
    text = run_subprocess(cmd, env, OUT_DIR / "logs" / f"qwen_decision_{decision_number}.log")
    marker = "AUTOREP_DECISION_JSON="
    for line in reversed(text.splitlines()):
        if line.startswith(marker):
            return json.loads(line[len(marker) :])
    raise RuntimeError("Qwen decision marker not found")


def run_decide_mode(context_path: Path) -> int:
    setup_imports()
    from agenthpobench.agents.open_source.qwen_agent import QwenAgent
    from agenthpobench.core.agent_base import DecisionContext

    payload = load_json(context_path)
    agent = QwenAgent(
        model_path=AGENT_MODEL,
        temperature=0.0,
        max_new_tokens=int(os.environ.get("OPENR1_QWEN_DECIDE_MAX_NEW_TOKENS", os.environ.get("AUTOREP_AGENT_MAX_NEW_TOKENS", "768"))),
        device_map="auto",
        torch_dtype="bfloat16",
        use_chat_template=False,
    )
    context = DecisionContext(**payload)
    agent.total_decisions += 1
    decision = agent.decide(context)
    merged = clamp_config({**payload["current_config"], **decision.new_config})
    result = {
        "new_config": merged,
        "raw_new_config": decision.new_config,
        "reasoning": decision.reasoning,
        "confidence": decision.confidence,
        "metadata": decision.metadata,
    }
    print("AUTOREP_DECISION_JSON=" + json.dumps(result, sort_keys=True), flush=True)
    return 0


def fallback_decision(history: list[dict[str, Any]], current: dict[str, Any], decision_number: int) -> dict[str, Any]:
    if decision_number == 0:
        new_config = {**current, "max_new_tokens": 1024}
        reasoning = "Fallback: increase max_new_tokens to give the reasoning model more budget."
    else:
        best = max(history, key=lambda item: float(item["metrics"]["accuracy_percent"]))
        new_config = best["config"]
        reasoning = "Fallback: choose the proxy setting with the highest accuracy."
    return {
        "new_config": clamp_config(new_config),
        "raw_new_config": new_config,
        "reasoning": reasoning,
        "confidence": 0.2,
        "metadata": {"fallback": True},
    }


def normalized_score(agent_metric: float, official: float | None) -> float | None:
    if official is None or PAPER_ANCHOR == official:
        return None
    return (agent_metric - official) / (PAPER_ANCHOR - official)


def run_orchestrator() -> int:
    if not DATA_FILE.exists():
        raise FileNotFoundError(DATA_FILE)
    if not (EVAL_MODEL / "model.safetensors").exists():
        raise FileNotFoundError(EVAL_MODEL / "model.safetensors")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    started = time.time()
    print(f"RUN_ID={RUN_ID}", flush=True)
    print(f"OUT_DIR={OUT_DIR}", flush=True)

    config = dict(BASE_CONFIG)
    history = [run_eval("proxy", 0, config, PROXY_LIMIT)]
    decisions: list[dict[str, Any]] = []
    for decision_number in range(PROXY_TRIALS):
        try:
            decision = decide_with_qwen(history, config, PROXY_TRIALS - decision_number, decision_number)
        except Exception as exc:  # noqa: BLE001
            print(f"QWEN_DECISION_FAILED decision={decision_number} error={exc!r}", flush=True)
            decision = fallback_decision(history, config, decision_number)
        new_config = clamp_config(decision["new_config"])
        decisions.append(
            {
                "decision_number": decision_number,
                "old_config": dict(config),
                "new_config": new_config,
                "reasoning": decision.get("reasoning"),
                "confidence": decision.get("confidence"),
                "metadata": decision.get("metadata", {}),
            }
        )
        config = new_config
        if decision_number < PROXY_TRIALS - 1:
            history.append(run_eval("proxy", decision_number + 1, config, PROXY_LIMIT))

    final_config = clamp_config(config)
    final_trial = run_eval("final", PROXY_TRIALS, final_config, FINAL_LIMIT)
    history.append(final_trial)
    final_metric = float(final_trial["metrics"]["accuracy_percent"])
    record = budget_record()
    official = None if record is None else record.get("official_budget_baseline")
    full_final = int(final_trial["metrics"]["num_total"]) >= 500
    result = {
        "run_id": RUN_ID,
        "repo": "open-r1",
        "task": "MATH-500 evaluation for DeepSeek-R1-Distill-Qwen-1.5B",
        "agent": os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal"),
        "model_path": AGENT_MODEL,
        "eval_model": str(EVAL_MODEL),
        "run_dir": str(OUT_DIR),
        "budget": {
            "proxy_trials": PROXY_TRIALS,
            "proxy_limit": PROXY_LIMIT,
            "final_limit": FINAL_LIMIT,
            "metric": "accuracy_percent",
        },
        "paper_anchor": PAPER_ANCHOR,
        "search_space": SEARCH_SPACE,
        "history": history,
        "decisions": decisions,
        "final_config": final_config,
        "final_metrics": final_trial["metrics"],
        "score": {
            "scoring_eligible": full_final and official is not None,
            "normalized_score": normalized_score(final_metric, official) if full_final else None,
            "official_budget_baseline": official,
            "paper_anchor": PAPER_ANCHOR,
            "direction": "higher_is_better",
            "note": None if full_final else "Final run did not cover the full 500-example MATH-500 set.",
        },
        "success": True,
        "decisions_made": len(decisions),
        "elapsed_sec": time.time() - started,
    }
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    (OUT_DIR / "result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("RESULT_JSON", json.dumps(result, sort_keys=True), flush=True)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--decide", type=Path)
    args = parser.parse_args()
    if args.decide is not None:
        return run_decide_mode(args.decide)
    return run_orchestrator()


if __name__ == "__main__":
    raise SystemExit(main())
