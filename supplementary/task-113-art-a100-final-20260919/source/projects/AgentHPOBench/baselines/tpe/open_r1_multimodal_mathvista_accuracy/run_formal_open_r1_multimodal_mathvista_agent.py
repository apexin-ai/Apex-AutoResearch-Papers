#!/usr/bin/env python3
from __future__ import annotations

import ast
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
FORMAL_DIR = ROOT / "baselines/tpe/open_r1_multimodal_mathvista_accuracy"
EVAL_SCRIPT = FORMAL_DIR / "eval_open_r1_multimodal_mathvista.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b"))) / "open_r1_multimodal_mathvista_accuracy"
RUN_ID = os.environ.get("RUN_ID") or f"openr1_mm_mathvista_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "open_r1_multimodal_mathvista_accuracy_QwenLocal_results.json"

PAPER_ANCHOR = 51.6
BASE_CONFIG = {"prompt_style": "direct", "max_new_tokens": 32, "temperature": 0.0, "top_p": 1.0}
SEARCH_SPACE = {
    "prompt_style": {"choices": ["direct", "cot", "short_cot"]},
    "max_new_tokens": {"choices": [16, 32, 64, 96]},
    "temperature": {"choices": [0.0, 0.2, 0.7]},
    "top_p": {"choices": [0.8, 0.9, 1.0]},
}
FALLBACK_CONFIGS = [
    {"prompt_style": "short_cot", "max_new_tokens": 64, "temperature": 0.0, "top_p": 1.0},
    {"prompt_style": "direct", "max_new_tokens": 16, "temperature": 0.0, "top_p": 1.0},
    {"prompt_style": "cot", "max_new_tokens": 96, "temperature": 0.0, "top_p": 1.0},
    {"prompt_style": "direct", "max_new_tokens": 32, "temperature": 0.2, "top_p": 0.9},
    {"prompt_style": "short_cot", "max_new_tokens": 32, "temperature": 0.2, "top_p": 0.8},
]


def cleanup_torch() -> None:
    try:
        import gc

        gc.collect()
        import torch

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            try:
                torch.cuda.ipc_collect()
            except Exception:
                pass
        gc.collect()
    except Exception:
        pass


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def nearest(value: Any, choices: list[Any]) -> Any:
    if choices and isinstance(choices[0], str):
        text = str(value).strip().lower()
        return text if text in choices else choices[0]
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {"prompt": "prompt_style", "max_tokens": "max_new_tokens", "temp": "temperature", "topp": "top_p"}
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "prompt_style": str(nearest(merged["prompt_style"], SEARCH_SPACE["prompt_style"]["choices"])),
        "max_new_tokens": int(nearest(merged["max_new_tokens"], SEARCH_SPACE["max_new_tokens"]["choices"])),
        "temperature": float(nearest(merged["temperature"], SEARCH_SPACE["temperature"]["choices"])),
        "top_p": float(nearest(merged["top_p"], SEARCH_SPACE["top_p"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return f"{cfg['prompt_style']}_tok{cfg['max_new_tokens']}_t{cfg['temperature']}_p{cfg['top_p']}".replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("MATHVISTA_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "0"))
        max_examples = os.environ.get("MATHVISTA_MAX_EXAMPLES", "0")
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--prompt-style {cfg['prompt_style']} "
            f"--max-new-tokens {cfg['max_new_tokens']} "
            f"--temperature {cfg['temperature']} "
            f"--top-p {cfg['top_p']} "
            f"--max-examples {max_examples} "
            "--seed 0",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"MathVista eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def parse_config(text: str) -> dict[str, Any]:
    for pattern in [r"NEW_CONFIG\s*[:=]\s*(\{.*?\})", r"```json\s*(\{.*?\})\s*```", r"(\{[^{}]*(?:prompt_style|max_new_tokens|temperature|top_p)[^{}]*\})"]:
        match = re.search(pattern, text, flags=re.S | re.I)
        if not match:
            continue
        block = match.group(1)
        try:
            return json.loads(block)
        except Exception:
            try:
                return ast.literal_eval(block)
            except Exception:
                continue
    raise ValueError(f"could not parse config: {text[:500]}")


def training_log(history: list[dict[str, Any]], baseline: float) -> str:
    lines = [
        "Task: open-r1-multimodal MathVista-mini evaluation with local Qwen2-VL-2B-Instruct.",
        "Metric: accuracy_percent, higher is better.",
        "Official anchor: README reports Qwen2-VL-2B-Instruct without reasoning MathVista-mini accuracy=51.6.",
        f"Budget baseline accuracy={baseline:.4f}, config={BASE_CONFIG}.",
        "Do not change the model or dataset; tune prompt/decoding only.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"accuracy={m['accuracy_percent']:.4f} correct={m['correct']}/{m['total']} seconds={m['seconds']}"
        )
    return "\n".join(lines)


def decide_with_qwen(history: list[dict[str, Any]], baseline: float, trial_idx: int) -> dict[str, Any]:

    import os as _tpe_os
    if _tpe_os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower() in {"random", "random_search", "tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
        import sys as _tpe_sys
        from pathlib import Path as _TpePath
        _tpe_sys.path.insert(0, str(_TpePath(__file__).resolve().parents[1]))
        from tpe_backend import tpe_decision_from_call
        return tpe_decision_from_call(globals().get("TASK_ID", _TpePath(__file__).resolve().parent.name), locals(), globals())
    deps = ROOT / ".python_deps"
    if deps.exists():
        sys.path.insert(0, str(deps))
    sys.path.insert(0, str(ROOT))
    prompt = f"""You are choosing one visual-reasoning evaluation configuration.

{training_log(history, baseline)}

Search space:
{json.dumps(SEARCH_SPACE, indent=2)}

Return exactly one line:
NEW_CONFIG: {{"prompt_style": "direct", "max_new_tokens": 32, "temperature": 0.0, "top_p": 1.0}}
"""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"qwen_prompt_{trial_idx}.txt").write_text(prompt)
    agent = None
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
        response = agent._generate(prompt)
        (OUT_DIR / f"qwen_raw_{trial_idx}.txt").write_text(response)
        raw = parse_config(response)
        return clamp_config(raw)
    except Exception as exc:  # noqa: BLE001
        (OUT_DIR / f"qwen_error_{trial_idx}.txt").write_text(repr(exc))
        return clamp_config(FALLBACK_CONFIGS[min(trial_idx - 1, len(FALLBACK_CONFIGS) - 1)])
    finally:
        if agent is not None:
            del agent
        cleanup_torch()


def score(value: float, baseline: float) -> float:
    denom = PAPER_ANCHOR - baseline
    if abs(denom) < 1e-12:
        return 0.0
    return float((value - baseline) / denom)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    history: list[dict[str, Any]] = []
    baseline = run_eval("baseline", 0, BASE_CONFIG)
    baseline_acc = float(baseline["metrics"]["accuracy_percent"])
    history.append(baseline)
    interventions = int(os.environ.get("AUTOREP_INTERVENTIONS", "5"))
    current = dict(BASE_CONFIG)
    for trial_idx in range(1, interventions + 1):
        current = decide_with_qwen(history, baseline_acc, trial_idx)
        history.append(run_eval("agent", trial_idx, current))
    best = max(history, key=lambda item: float(item["metrics"]["accuracy_percent"]))
    final = history[-1]
    payload = {
        "task": "open_r1_multimodal_mathvista_accuracy",
        "paper_anchor_accuracy_percent": PAPER_ANCHOR,
        "baseline_config": BASE_CONFIG,
        "baseline_metric": baseline_acc,
        "best_metric": float(best["metrics"]["accuracy_percent"]),
        "final_metric": float(final["metrics"]["accuracy_percent"]),
        "best_score_vs_budget_baseline": score(float(best["metrics"]["accuracy_percent"]), baseline_acc),
        "final_score_vs_budget_baseline": score(float(final["metrics"]["accuracy_percent"]), baseline_acc),
        "best_trial": best,
        "final_trial": final,
        "history": history,
        "run_id": RUN_ID,
    }
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(payload, indent=2))
    print("RESULT_JSON " + json.dumps(payload, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
