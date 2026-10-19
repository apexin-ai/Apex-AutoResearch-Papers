#!/usr/bin/env python3
from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(os.environ.get("AUTOREP_ROOT", "."))
FORMAL_DIR = ROOT / "tasks/main/align_anything_ragen_bandit"
EVAL_SCRIPT = FORMAL_DIR / "eval_align_anything_ragen_bandit.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/main/qwen3_32b"))) / "align_anything_ragen_bandit"
RUN_ID = os.environ.get("RUN_ID") or f"align_anything_ragen_bandit_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "align_anything_ragen_bandit_QwenLocal_results.json"

PAPER_ANCHOR = 1.0
BASE_CONFIG = {
    "learning_rate": 0.01,
    "batch_size": 16,
    "entropy_coef": 0.0,
    "temperature": 1.6,
    "reward_baseline": "none",
    "optimizer": "sgd",
}
SEARCH_SPACE = {
    "learning_rate": {"choices": [0.01, 0.03, 0.1, 0.3]},
    "batch_size": {"choices": [16, 32, 64]},
    "entropy_coef": {"choices": [0.0, 0.01, 0.03, 0.06]},
    "temperature": {"choices": [0.6, 0.8, 1.0, 1.3, 1.6]},
    "reward_baseline": {"choices": ["none", "mean", "ema"]},
    "optimizer": {"choices": ["adam", "sgd"]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "align_anything_ragen_bandit", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
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
        numeric_choices = [x for x in choices if isinstance(x, (int, float))]
        if numeric_choices:
            return min(numeric_choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        pass
    text = str(value).lower()
    for item in choices:
        if str(item).lower() == text:
            return item
    return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {"lr": "learning_rate", "entropy": "entropy_coef", "baseline": "reward_baseline"}
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "learning_rate": float(nearest(merged["learning_rate"], SEARCH_SPACE["learning_rate"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
        "entropy_coef": float(nearest(merged["entropy_coef"], SEARCH_SPACE["entropy_coef"]["choices"])),
        "temperature": float(nearest(merged["temperature"], SEARCH_SPACE["temperature"]["choices"])),
        "reward_baseline": str(nearest(merged["reward_baseline"], SEARCH_SPACE["reward_baseline"]["choices"])),
        "optimizer": str(nearest(merged["optimizer"], SEARCH_SPACE["optimizer"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return (
        f"lr{cfg['learning_rate']}_bs{cfg['batch_size']}_ent{cfg['entropy_coef']}"
        f"_temp{cfg['temperature']}_{cfg['reward_baseline']}_{cfg['optimizer']}"
    ).replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        cmd = [
            sys.executable,
            str(EVAL_SCRIPT),
            "--results-dir",
            str(trial_dir),
            "--learning-rate",
            str(cfg["learning_rate"]),
            "--batch-size",
            str(cfg["batch_size"]),
            "--entropy-coef",
            str(cfg["entropy_coef"]),
            "--temperature",
            str(cfg["temperature"]),
            "--reward-baseline",
            cfg["reward_baseline"],
            "--optimizer",
            cfg["optimizer"],
            "--steps",
            str(int(os.environ.get("ALIGN_RAGEN_STEPS", "20"))),
            "--seed",
            str(42 + int(os.environ.get('AUTOREP_REPLICATE_SEED', '0'))),
        ]
        proc = subprocess.run(cmd, cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (trial_dir / "eval.log").write_bytes(proc.stdout)
        if proc.returncode != 0:
            print(proc.stdout.decode("utf-8", errors="replace"), flush=True)
            raise RuntimeError(f"align-anything RAGEN bandit eval failed rc={proc.returncode}")
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": load_json(metrics_path), "output_dir": str(trial_dir)}


def training_log(history: list[dict[str, Any]], current: dict[str, Any], baseline: float) -> str:
    lines = [
        "Task: align-anything RAGEN Bandit policy optimization.",
        "Metric: success_rate, 1.0 iff the learned policy selects the optimal arm after the budget. Higher is better.",
        "Official anchor: align-anything technical report says the RAGEN Bandit task achieved 100% success rate within 200 training steps.",
        "AgentHPOBench budget: 20 policy-gradient steps, i.e. 1/10 of the reported training-step budget.",
        f"Budget baseline success_rate={baseline:.4f}, config={BASE_CONFIG}.",
        f"Current config: {current}",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"success_rate={m['success_rate']:.4f} optimal_prob={m['optimal_arm_probability']:.4f} "
            f"expected_reward={m['expected_reward']:.4f}"
        )
    return "\n".join(lines)


def extract_config(response: str) -> tuple[dict[str, Any], float, str]:
    anchor = response.rfind("NEW_CONFIG:")
    start = response.find("{", anchor if anchor >= 0 else 0)
    if start < 0:
        raise ValueError("missing config object")
    depth = 0
    end = -1
    for idx, ch in enumerate(response[start:], start=start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = idx + 1
                break
    if end < 0:
        raise ValueError("unterminated config object")
    block = response[start:end]
    try:
        parsed = json.loads(block)
    except json.JSONDecodeError:
        parsed = ast.literal_eval(block)
    confidence = 0.7
    match = re.search(r"CONFIDENCE:\s*([0-9]*\.?[0-9]+)", response)
    if match:
        confidence = max(0.0, min(1.0, float(match.group(1))))
    return clamp_config(parsed), confidence, response


def decide_with_qwen(history: list[dict[str, Any]], current: dict[str, Any], baseline: float, decision_number: int) -> dict[str, Any]:

    import os as _tpe_os
    if _tpe_os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower() in {"tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
        import sys as _tpe_sys
        from pathlib import Path as _TpePath
        _tpe_sys.path.insert(0, str(_TpePath(__file__).resolve().parents[1]))
        from tpe_backend import tpe_decision_from_call
        return tpe_decision_from_call(globals().get("TASK_ID", _TpePath(__file__).resolve().parent.name), locals(), globals())
    backend = os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower()
    if backend in {"random", "random_search"}:
        import random

        seed = os.environ.get("AUTOREP_RANDOM_SEED", "0")
        state = json.dumps({"history": history, "current": current, "decision_number": decision_number}, sort_keys=True, default=str)
        rng = random.Random(f"{seed}:align_anything_ragen_bandit:{len(history)}:{state}")
        raw = {key: rng.choice(list(spec["choices"])) for key, spec in SEARCH_SPACE.items()}
        new_config = clamp_config(raw)
        raw_response = json.dumps({
            "backend": "random_search",
            "seed": seed,
            "raw_new_config": raw,
            "new_config": new_config,
        }, sort_keys=True)
        return {"old_config": current, "new_config": new_config, "confidence": 0.0, "raw_response": raw_response}

    sys.path.insert(0, str(ROOT))
    deps = ROOT / ".python_deps"
    if deps.exists():
        sys.path.insert(0, str(deps))
    from qwen_agent_multiseed_v2 import QwenAgent

    prompt = f"""You are tuning an RL bandit policy-gradient experiment from align-anything/RAGEN.

Target metric: maximize success_rate. Higher is better.

Context:
{training_log(history, current, baseline)}

Search space:
{json.dumps(SEARCH_SPACE, indent=2)}

Return exactly these three lines. Use strict JSON with lowercase strings.
REASONING: short explanation
NEW_CONFIG: {{"learning_rate": 0.1, "batch_size": 64, "entropy_coef": 0.01, "temperature": 0.8, "reward_baseline": "ema", "optimizer": "adam"}}
CONFIDENCE: 0.8
"""
    agent = QwenAgent(
        model_path=str(AGENT_MODEL),
        temperature=float(os.environ.get("AUTOREP_AGENT_TEMPERATURE", "0.0")),
        max_new_tokens=int(os.environ.get("AUTOREP_AGENT_MAX_NEW_TOKENS", "384")),
        torch_dtype=os.environ.get("AUTOREP_AGENT_TORCH_DTYPE", "bfloat16"),
        trust_remote_code=True,
        device_map=os.environ.get("AUTOREP_AGENT_DEVICE_MAP", "auto"),
        use_chat_template=os.environ.get("AUTOREP_USE_CHAT_TEMPLATE", "1").lower() in {"1", "true", "yes", "on"},
    )
    response = agent._generate(prompt)
    (OUT_DIR / f"qwen_response_{decision_number}.txt").write_text(response)
    try:
        new_config, confidence, raw = extract_config(response)
    except Exception as exc:
        new_config = {"learning_rate": 0.1, "batch_size": 64, "entropy_coef": 0.01, "temperature": 0.8, "reward_baseline": "ema", "optimizer": "adam"}
        confidence = 0.25
        raw = f"fallback after parse error: {exc}\n{response}"
    return {"old_config": current, "new_config": new_config, "confidence": confidence, "raw_response": raw}


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    baseline = run_eval("baseline", 0, BASE_CONFIG)
    baseline_score = float(baseline["metrics"]["success_rate"])
    history = [baseline]
    current = BASE_CONFIG
    decisions = []
    interventions = max(1, int(os.environ.get("AUTOREP_INTERVENTIONS", "1")))
    for i in range(interventions):
        decision = decide_with_qwen(history, current, baseline_score, i)
        decisions.append(decision)
        current = decision["new_config"]
        history.append(run_eval(f"intervention_{i+1}", i + 1, current))

    best = max(history, key=lambda item: float(item["metrics"]["success_rate"]))
    final = history[-1]
    best_score = float(best["metrics"]["success_rate"])
    summary = {
        "agent": os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal"),
        "benchmark_name": "align_anything_ragen_bandit",
        "repo": "align-anything",
        "repo_url": "https://github.com/PKU-Alignment/align-anything",
        "repo_year": 2024,
        "domain": "rl_agent",
        "task": "RAGEN Bandit policy optimization",
        "dataset": "Bandit task",
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "run_dir": str(OUT_DIR),
        "metric": "success_rate",
        "higher_is_better": True,
        "paper_anchor": PAPER_ANCHOR,
        "paper_anchor_source": "align-anything technical_report.md: Bandit Task achieved 100% success rate within 200 training steps.",
        "official_budget_baseline": baseline_score,
        "baseline_metrics": baseline["metrics"],
        "final_metrics": final["metrics"],
        "best_metrics": best["metrics"],
        "final_config": final["config"],
        "best_config": best["config"],
        "decisions": decisions,
        "decisions_made": len(decisions),
        "history": history,
        "agent_budget_result": best_score,
        "final_agent_budget_result": float(final["metrics"]["success_rate"]),
        "score": {
            "normalized_score": 0.0 if abs(PAPER_ANCHOR - baseline_score) < 1e-12 else (best_score - baseline_score) / (PAPER_ANCHOR - baseline_score),
            "delta_vs_budget_baseline": best_score - baseline_score,
            "delta_vs_paper_anchor": best_score - PAPER_ANCHOR,
            "official_budget_baseline": baseline_score,
            "paper_anchor": PAPER_ANCHOR,
            "direction": "higher_is_better",
            "scoring_eligible": True,
        },
        "budget": {
            "reported_steps": 200,
            "standard_steps": int(os.environ.get("ALIGN_RAGEN_STEPS", "20")),
            "search_space": SEARCH_SPACE,
            "baseline_config": BASE_CONFIG,
        },
        "success": True,
    }
    RESULT_FILE.parent.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    (OUT_DIR / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print("RESULT_JSON " + json.dumps(summary, sort_keys=True))
    print(RESULT_FILE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
