#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
import ast
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(".")
FORMAL_DIR = ROOT / "baselines/tpe/forest_diffusion_iris_f1fake"
EVAL_SCRIPT = FORMAL_DIR / "eval_forest_diffusion_iris.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "forest_diffusion_iris_f1fake"
RUN_ID = os.environ.get("RUN_ID") or f"forest_diffusion_iris_f1fake_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "forest_diffusion_iris_f1fake_QwenLocal_results.json"

PAPER_ANCHOR_F1 = 0.970038
BASE_CONFIG = {
    "n_t": 10,
    "n_t_sampling": 10,
    "duplicate_k": 5,
    "max_depth": 7,
    "n_estimators": 50,
    "eta": 0.3,
    "diffusion_type": "flow",
    "ycond": False,
    "n_batch": 1,
    "n_jobs": 8,
}
SEARCH_SPACE = {
    "n_t": {"choices": [5, 10, 25, 50]},
    "n_t_sampling": {"choices": [5, 10, 25, 50]},
    "duplicate_k": {"choices": [1, 5, 10, 25, 100]},
    "max_depth": {"choices": [3, 5, 7]},
    "n_estimators": {"choices": [25, 50, 100]},
    "eta": {"choices": [0.1, 0.3, 0.5]},
    "diffusion_type": {"choices": ["flow", "vp"]},
    "ycond": {"choices": [False, True]},
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def nearest(value: Any, choices: list[Any]) -> Any:
    if isinstance(value, bool):
        return bool(value) if bool(value) in choices else choices[0]
    if isinstance(value, str) and value.lower() in {"true", "false"} and any(isinstance(x, bool) for x in choices):
        return value.lower() == "true"
    try:
        numeric = float(value)
        numeric_choices = [item for item in choices if not isinstance(item, str) and not isinstance(item, bool)]
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
    aliases = {
        "nt": "n_t",
        "n_steps": "n_t",
        "steps": "n_t",
        "sampling_steps": "n_t_sampling",
        "duplicate_K": "duplicate_k",
        "duplicate": "duplicate_k",
        "depth": "max_depth",
        "trees": "n_estimators",
        "num_trees": "n_estimators",
        "learning_rate": "eta",
        "lr": "eta",
        "diffusion": "diffusion_type",
        "condition_on_y": "ycond",
        "label_y": "ycond",
        "y_conditioned": "ycond",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    cfg = {
        "n_t": int(nearest(merged["n_t"], SEARCH_SPACE["n_t"]["choices"])),
        "n_t_sampling": int(nearest(merged["n_t_sampling"], SEARCH_SPACE["n_t_sampling"]["choices"])),
        "duplicate_k": int(nearest(merged["duplicate_k"], SEARCH_SPACE["duplicate_k"]["choices"])),
        "max_depth": int(nearest(merged["max_depth"], SEARCH_SPACE["max_depth"]["choices"])),
        "n_estimators": int(nearest(merged["n_estimators"], SEARCH_SPACE["n_estimators"]["choices"])),
        "eta": float(nearest(merged["eta"], SEARCH_SPACE["eta"]["choices"])),
        "diffusion_type": str(nearest(merged["diffusion_type"], SEARCH_SPACE["diffusion_type"]["choices"])),
        "ycond": bool(nearest(merged["ycond"], SEARCH_SPACE["ycond"]["choices"])),
        "n_batch": 1,
        "n_jobs": 8,
    }
    cfg["n_t_sampling"] = min(cfg["n_t_sampling"], cfg["n_t"])
    return cfg


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return (
        f"nt{cfg['n_t']}_nts{cfg['n_t_sampling']}_dup{cfg['duplicate_k']}_d{cfg['max_depth']}"
        f"_trees{cfg['n_estimators']}_eta{cfg['eta']}_{cfg['diffusion_type']}_y{int(cfg['ycond'])}"
    ).replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["PYTHONPATH"] = f"{ROOT}:{ROOT / 'repositories/ForestDiffusion'}:{ROOT / 'repositories/ForestDiffusion/Python-Package/base-ForestDiffusion'}:{env.get('PYTHONPATH', '')}"
        # Keep ForestDiffusion/XGBoost eval on CPU; the agent may use multi-GPU,
        # but XGBoost can mis-detect inherited CUDA array-interface state.
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("FOREST_EVAL_CUDA_VISIBLE_DEVICES", "")
        cmd = [
            sys.executable,
            str(EVAL_SCRIPT),
            "--results-dir",
            str(trial_dir),
            "--n-t",
            str(cfg["n_t"]),
            "--n-t-sampling",
            str(cfg["n_t_sampling"]),
            "--duplicate-k",
            str(cfg["duplicate_k"]),
            "--max-depth",
            str(cfg["max_depth"]),
            "--n-estimators",
            str(cfg["n_estimators"]),
            "--eta",
            str(cfg["eta"]),
            "--diffusion-type",
            cfg["diffusion_type"],
            "--ycond",
            str(cfg["ycond"]),
            "--n-batch",
            "1",
            "--n-jobs",
            "8",
            "--nexp",
            "1",
            "--ngen",
            "2",
            "--n-tries",
            "2",
            "--seed",
            "0",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"ForestDiffusion eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def training_log(history: list[dict[str, Any]], current: dict[str, Any], baseline: float) -> str:
    lines = [
        "Task: ForestDiffusion Iris tabular generation.",
        "Metric: F1_fake from the official generation evaluation: train downstream classifiers on generated Iris samples and evaluate macro-F1 on real held-out Iris data. Higher is better.",
        "Paper/repo anchor: official ForestDiffusion ablation_iris result for xgboost flow ycond=True reports F1_fake=0.970038.",
        "Budget protocol: baseline plus five sequential agent interventions by default; each intervention uses the prior config and observed history. One train/test split, two generated batches, two classifier seeds. Tune only ForestDiffusion hyperparameters in the search space.",
        f"Budget baseline F1_fake={baseline:.4f}, config={BASE_CONFIG}.",
        "Short-budget hint: the official ablation shows y-conditioned xgboost flow with duplicate_K=100 and n_t=50 performs best on Iris; tiny duplicate_K or no y conditioning usually hurts fake-data utility.",
        f"Current config: {current}",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"f1_fake={m['f1_fake']:.4f} f1_real={m['f1_real']:.4f} seconds={m['seconds']}"
        )
    return "\n".join(lines)


def decide_with_qwen(history: list[dict[str, Any]], current: dict[str, Any], baseline: float, decision_number: int, total_interventions: int) -> dict[str, Any]:

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
        "training_log": training_log(history, current, baseline),
        "current_config": current,
        "metrics_history": [(item["trial"], item["metrics"]["f1_fake"], item["config"], item["kind"]) for item in history],
        "budget_remaining": max(0, total_interventions - decision_number),
        "total_budget": total_interventions + 1,
        "search_space": SEARCH_SPACE,
        "epoch": decision_number + 1,
        "decision_number": decision_number,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"qwen_context_{decision_number}.json").write_text(json.dumps(payload, indent=2))
    prompt = f"""You are tuning a ForestDiffusion tabular generation experiment.

Target metric: maximize F1_fake. Higher is better.
Decision: {decision_number + 1} of {total_interventions}. Use the full history below and propose the next sequential candidate.

Context:
{payload["training_log"]}

Current config:
{json.dumps(current, indent=2)}

Search space:
{json.dumps(SEARCH_SPACE, indent=2)}

Return exactly these three lines. Use strict JSON with lowercase true/false.
REASONING: short explanation
NEW_CONFIG: {{"n_t": 50, "n_t_sampling": 50, "duplicate_k": 100, "max_depth": 7, "n_estimators": 100, "eta": 0.3, "diffusion_type": "flow", "ycond": true}}
CONFIDENCE: 0.8
"""

    def extract_config(response: str) -> tuple[dict[str, Any], float, str]:
        start = response.find("{")
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
        if not isinstance(parsed, dict):
            raise ValueError("config object is not a dict")
        confidence = 0.7
        match = re.search(r"CONFIDENCE:\s*([0-9]*\.?[0-9]+)", response)
        if match:
            confidence = max(0.0, min(1.0, float(match.group(1))))
        reasoning = response[:start].replace("REASONING:", "").strip()
        if not reasoning:
            reasoning = "Direct Qwen ForestDiffusion decision"
        return parsed, confidence, reasoning

    try:
        from agenthpobench.agents.api_decision_client import api_backend_enabled, call_decision_api
        if api_backend_enabled():
            response = call_decision_api(prompt, temperature=0.0, max_tokens=int(os.environ.get("AUTOREP_API_MAX_TOKENS", "384")))
            response_text = response.text
            (OUT_DIR / f"qwen_raw_{decision_number}.txt").write_text(response_text)
            try:
                raw_config, confidence, reasoning = extract_config(response_text)
            except ValueError as exc:
                fallback = {
                    "n_t": 50,
                    "n_t_sampling": 50,
                    "duplicate_k": 100,
                    "max_depth": 7,
                    "n_estimators": 100,
                    "eta": 0.3,
                    "diffusion_type": "flow",
                    "ycond": True,
                }
                return {
                    "new_config": clamp_config({**current, **fallback}),
                    "raw_new_config": fallback,
                    "reasoning": f"API response did not contain a parseable config; using official-ablation fallback. Error: {exc!r}",
                    "confidence": 0.0,
                    "metadata": {"api_backend": True, "api_parse_fallback": True, "api": response.metadata, "raw_text": response_text[:1000]},
                }
            return {
                "new_config": clamp_config({**current, **raw_config}),
                "raw_new_config": raw_config,
                "reasoning": reasoning,
                "confidence": confidence,
                "metadata": {"api_backend": True, "api": response.metadata, "model_path": str(AGENT_MODEL)},
            }
    except Exception:
        if os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower() in {"api", "openai", "openai-compatible", "anthropic", "glm", "claude_code", "claude-code", "codex", "codex_cli", "codex-cli"}:
            raise

    try:
        from agenthpobench.agents.open_source.qwen_agent import QwenAgent
        os.environ["CUDA_VISIBLE_DEVICES"] = os.environ.get("QWEN_CUDA_VISIBLE_DEVICES", "1")
        agent = QwenAgent(
            model_path=str(AGENT_MODEL),
            temperature=0.0,
            max_new_tokens=384,
            device_map="auto",
            torch_dtype="bfloat16",
            use_chat_template=False,
        )
        response_text = agent._generate(prompt)
        (OUT_DIR / f"qwen_raw_{decision_number}.txt").write_text(response_text)
        raw_config, confidence, reasoning = extract_config(response_text)
        out = {
            "new_config": clamp_config({**current, **raw_config}),
            "raw_new_config": raw_config,
            "reasoning": reasoning,
            "confidence": confidence,
            "metadata": {"model_path": str(AGENT_MODEL), "direct_prompt": True},
        }
        del agent
        try:
            import torch

            torch.cuda.empty_cache()
        except Exception:
            pass
        return out
    except Exception as exc:  # noqa: BLE001
        fallback = {
            "n_t": 50,
            "n_t_sampling": 50,
            "duplicate_k": 100,
            "max_depth": 7,
            "n_estimators": 100,
            "eta": 0.3,
            "diffusion_type": "flow",
            "ycond": True,
        }
        return {
            "new_config": clamp_config({**current, **fallback}),
            "raw_new_config": fallback,
            "reasoning": f"Qwen decision failed; using official-ablation fallback. Error: {exc!r}",
            "confidence": 0.0,
            "metadata": {"fallback": True, "error": repr(exc)},
        }


def normalized_score(value: float, baseline: float) -> float:
    denom = PAPER_ANCHOR_F1 - baseline
    if abs(denom) < 1e-12:
        return 0.0
    return (value - baseline) / denom


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    total_interventions = max(1, int(os.environ.get("FOREST_DIFFUSION_INTERVENTIONS", "5")))
    history: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []

    baseline_trial = run_eval("baseline", 0, BASE_CONFIG)
    history.append(baseline_trial)
    budget_baseline = float(baseline_trial["metrics"]["f1_fake"])

    current_config = clamp_config(BASE_CONFIG)
    for decision_idx in range(total_interventions):
        old_config = current_config
        decision = decide_with_qwen(history, old_config, budget_baseline, decision_idx, total_interventions)
        next_config = clamp_config(decision["new_config"])
        trial = run_eval("intervention", decision_idx + 1, next_config)
        history.append(trial)
        decisions.append(
            {
                "decision_number": decision_idx,
                "old_config": old_config,
                "new_config": next_config,
                "raw_new_config": decision.get("raw_new_config"),
                "reasoning": decision.get("reasoning"),
                "confidence": decision.get("confidence"),
                "metadata": decision.get("metadata"),
                "metrics": trial["metrics"],
            }
        )
        current_config = next_config

    final_trial = history[-1]
    final_config = current_config
    final_f1 = float(final_trial["metrics"]["f1_fake"])

    score = normalized_score(final_f1, budget_baseline)
    summary = {
        "agent": os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal"),
        "benchmark_name": "forest_diffusion_iris_f1fake",
        "repo": "ForestDiffusion",
        "task": "Iris tabular generation with ForestDiffusion",
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "run_dir": str(OUT_DIR),
        "paper_anchor": PAPER_ANCHOR_F1,
        "budget": {
            "metric": "f1_fake",
            "seed": 0,
            "nexp": 1,
            "ngen": 2,
            "n_tries": 2,
            "baseline_config": BASE_CONFIG,
            "interventions": total_interventions,
            "protocol": "baseline_plus_sequential_interventions",
        },
        "baseline_metrics": baseline_trial["metrics"],
        "final_metrics": final_trial["metrics"],
        "final_config": final_config,
        "decisions": decisions,
        "decisions_made": len(decisions),
        "history": history,
        "search_space": SEARCH_SPACE,
        "success": True,
        "score": {
            "direction": "higher_is_better",
            "official_budget_baseline": budget_baseline,
            "paper_anchor": PAPER_ANCHOR_F1,
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
