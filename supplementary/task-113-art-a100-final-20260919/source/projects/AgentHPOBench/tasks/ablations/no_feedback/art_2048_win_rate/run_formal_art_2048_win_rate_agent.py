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
FORMAL_DIR = ROOT / "tasks/ablations/no_feedback/art_2048_win_rate"
EVAL_SCRIPT = FORMAL_DIR / "eval_art_2048_win_rate.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/no_feedback/qwen3_32b"))) / "art_2048_win_rate"
RUN_ID = os.environ.get("RUN_ID") or f"art_2048_win_rate_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "art_2048_win_rate_QwenLocal_results.json"

PAPER_ANCHOR = 0.60
BASE_CONFIG = {
    "lookahead_depth": 2,
    "empty_weight": 2.0,
    "merge_weight": 1.0,
    "max_tile_weight": 2.0,
    "corner_weight": 2.0,
    "smoothness_weight": 0.2,
    "move_order": "up_left_right_down",
}
SEARCH_SPACE = {
    "lookahead_depth": {"choices": [1, 2, 3]},
    "empty_weight": {"choices": [0.5, 1.0, 2.0, 3.0]},
    "merge_weight": {"choices": [0.0, 0.5, 1.0, 2.0]},
    "max_tile_weight": {"choices": [0.5, 1.0, 2.0, 4.0]},
    "corner_weight": {"choices": [0.0, 1.0, 2.0, 4.0]},
    "smoothness_weight": {"choices": [0.0, 0.2, 0.5, 1.0]},
    "move_order": {"choices": ["left_up_right_down", "up_left_right_down", "right_up_left_down", "down_left_right_up"]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "art_2048_win_rate", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)



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
    aliases = {"depth": "lookahead_depth", "smoothness": "smoothness_weight", "corner": "corner_weight"}
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "lookahead_depth": int(nearest(merged["lookahead_depth"], SEARCH_SPACE["lookahead_depth"]["choices"])),
        "empty_weight": float(nearest(merged["empty_weight"], SEARCH_SPACE["empty_weight"]["choices"])),
        "merge_weight": float(nearest(merged["merge_weight"], SEARCH_SPACE["merge_weight"]["choices"])),
        "max_tile_weight": float(nearest(merged["max_tile_weight"], SEARCH_SPACE["max_tile_weight"]["choices"])),
        "corner_weight": float(nearest(merged["corner_weight"], SEARCH_SPACE["corner_weight"]["choices"])),
        "smoothness_weight": float(nearest(merged["smoothness_weight"], SEARCH_SPACE["smoothness_weight"]["choices"])),
        "move_order": str(nearest(merged["move_order"], SEARCH_SPACE["move_order"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return (
        f"d{cfg['lookahead_depth']}_empty{cfg['empty_weight']}_merge{cfg['merge_weight']}"
        f"_max{cfg['max_tile_weight']}_corner{cfg['corner_weight']}_smooth{cfg['smoothness_weight']}_{cfg['move_order']}"
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
            "--lookahead-depth",
            str(cfg["lookahead_depth"]),
            "--empty-weight",
            str(cfg["empty_weight"]),
            "--merge-weight",
            str(cfg["merge_weight"]),
            "--max-tile-weight",
            str(cfg["max_tile_weight"]),
            "--corner-weight",
            str(cfg["corner_weight"]),
            "--smoothness-weight",
            str(cfg["smoothness_weight"]),
            "--move-order",
            cfg["move_order"],
            "--games",
            str(int(os.environ.get("ART_2048_GAMES", "25"))),
            "--max-moves",
            str(int(os.environ.get("ART_2048_MAX_MOVES", "70"))),
            "--seed",
            "42",
        ]
        proc = subprocess.run(cmd, cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (trial_dir / "eval.log").write_bytes(proc.stdout)
        if proc.returncode != 0:
            print(proc.stdout.decode("utf-8", errors="replace"), flush=True)
            raise RuntimeError(f"ART 2048 eval failed rc={proc.returncode}")
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": load_json(metrics_path), "output_dir": str(trial_dir)}


def training_log(history: list[dict[str, Any]], current: dict[str, Any], baseline: float) -> str:
    history = history[:1]  # No-feedback: expose only the baseline observation.
    lines = [
        "Task: ART 2048 game policy benchmark.",
        "Metric: win_rate over fixed-seed games. Higher is better. A win means the game reaches the repo's WINNING_VALUE=128.",
        "Official anchor: ART assets/benchmarks/2048/accuracy-comparison.svg reports the RL agent at 60% games won.",
        "AgentHPOBench budget: 25 fixed-seed games, max 70 moves per game.",
        f"Budget baseline win_rate={baseline:.4f}, config={BASE_CONFIG}.",
        f"Current config: {current}",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"win_rate={m['win_rate']:.4f} avg_max_tile={m['avg_max_tile']:.2f} avg_moves={m['avg_moves']:.2f}"
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

    history = history[:1]  # No-feedback: expose only the baseline observation.
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
        state = json.dumps(history, sort_keys=True, default=str)
        rng = random.Random(f"{seed}:art_2048_win_rate:{decision_number}:{state}")
        raw = {key: rng.choice(list(spec["choices"])) for key, spec in SEARCH_SPACE.items()}
        new_config = clamp_config(raw)
        return {
            "old_config": current,
            "new_config": new_config,
            "confidence": 0.0,
            "raw_response": "Uniform random sample from the constrained ART search space.",
            "metadata": {"backend": "random_search", "seed": seed, "search_space_keys": sorted(SEARCH_SPACE)},
        }

    sys.path.insert(0, str(ROOT))
    deps = ROOT / ".python_deps"
    if deps.exists():
        sys.path.insert(0, str(deps))
    from agenthpobench.agents.open_source.qwen_agent import QwenAgent

    prompt = f"""You are tuning a heuristic policy for the ART 2048 benchmark.

Target metric: maximize win_rate. Higher is better.

Context:
{training_log(history, current, baseline)}

Search space:
{json.dumps(SEARCH_SPACE, indent=2)}

Return exactly these three lines. Use strict JSON with lowercase strings.
REASONING: short explanation
NEW_CONFIG: {{"lookahead_depth": 1, "empty_weight": 1.0, "merge_weight": 0.5, "max_tile_weight": 1.0, "corner_weight": 0.0, "smoothness_weight": 0.0, "move_order": "left_up_right_down"}}
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
        new_config = {
            "lookahead_depth": 1,
            "empty_weight": 1.0,
            "merge_weight": 0.5,
            "max_tile_weight": 1.0,
            "corner_weight": 0.0,
            "smoothness_weight": 0.0,
            "move_order": "left_up_right_down",
        }
        confidence = 0.25
        raw = f"fallback after parse error: {exc}\n{response}"
    return {"old_config": current, "new_config": new_config, "confidence": confidence, "raw_response": raw}


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    baseline = run_eval("baseline", 0, BASE_CONFIG)
    baseline_score = float(baseline["metrics"]["win_rate"])
    history = [baseline]
    current = BASE_CONFIG
    decisions = []
    interventions = max(1, int(os.environ.get("AUTOREP_INTERVENTIONS", "1")))
    for i in range(interventions):
        decision = decide_with_qwen(history, current, baseline_score, i)
        decisions.append(decision)
        current = decision["new_config"]
        history.append(run_eval(f"intervention_{i+1}", i + 1, current))

    best = max(history, key=lambda item: float(item["metrics"]["win_rate"]))
    final = history[-1]
    best_score = float(best["metrics"]["win_rate"])
    summary = {
        "agent": os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal"),
        "benchmark_name": "art_2048_win_rate",
        "repo": "ART",
        "repo_url": "https://github.com/OpenPipe/ART",
        "repo_year": 2025,
        "domain": "rl_agent",
        "task": "ART 2048 game policy benchmark",
        "dataset": "2048 game rollouts",
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "run_dir": str(OUT_DIR),
        "metric": "win_rate",
        "higher_is_better": True,
        "paper_anchor": PAPER_ANCHOR,
        "paper_anchor_source": "ART assets/benchmarks/2048/accuracy-comparison.svg: RL 60% games won.",
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
        "final_agent_budget_result": float(final["metrics"]["win_rate"]),
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
            "standard_games": int(os.environ.get("ART_2048_GAMES", "25")),
            "max_moves": int(os.environ.get("ART_2048_MAX_MOVES", "70")),
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
