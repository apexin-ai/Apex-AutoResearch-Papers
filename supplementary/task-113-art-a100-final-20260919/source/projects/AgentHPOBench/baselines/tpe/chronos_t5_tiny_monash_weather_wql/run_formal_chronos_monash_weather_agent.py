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
FORMAL_DIR = ROOT / "baselines/tpe/chronos_t5_tiny_monash_weather_wql"
EVAL_SCRIPT = FORMAL_DIR / "eval_chronos_monash_weather.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b"))) / "chronos_t5_tiny_monash_weather_wql"
RUN_ID = os.environ.get("RUN_ID") or f"chronos_monash_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "chronos_t5_tiny_monash_weather_wql_QwenLocal_results.json"

PAPER_ANCHOR_WQL = 0.14787595319625085
BASE_CONFIG = {
    "context_length": 512,
    "num_samples": 20,
    "temperature": 1.0,
    "top_k": 50,
    "top_p": 1.0,
}
SEARCH_SPACE = {
    "context_length": {"choices": [96, 192, 336, 512, 768, 1024, 0]},
    "num_samples": {"choices": [5, 10, 20, 40]},
    "temperature": {"choices": [0.7, 1.0, 1.3]},
    "top_k": {"choices": [20, 50, 100]},
    "top_p": {"choices": [0.9, 1.0]},
}
FALLBACK_CONFIGS = [
    {"context_length": 1024, "num_samples": 20, "temperature": 1.0, "top_k": 50, "top_p": 1.0},
    {"context_length": 768, "num_samples": 40, "temperature": 1.0, "top_k": 50, "top_p": 1.0},
    {"context_length": 512, "num_samples": 40, "temperature": 0.7, "top_k": 100, "top_p": 0.9},
    {"context_length": 336, "num_samples": 20, "temperature": 1.3, "top_k": 50, "top_p": 1.0},
    {"context_length": 0, "num_samples": 10, "temperature": 1.0, "top_k": 20, "top_p": 1.0},
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
        "context": "context_length",
        "ctx": "context_length",
        "samples": "num_samples",
        "n_samples": "num_samples",
        "temp": "temperature",
        "topk": "top_k",
        "topp": "top_p",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "context_length": int(nearest(merged["context_length"], SEARCH_SPACE["context_length"]["choices"])),
        "num_samples": int(nearest(merged["num_samples"], SEARCH_SPACE["num_samples"]["choices"])),
        "temperature": float(nearest(merged["temperature"], SEARCH_SPACE["temperature"]["choices"])),
        "top_k": int(nearest(merged["top_k"], SEARCH_SPACE["top_k"]["choices"])),
        "top_p": float(nearest(merged["top_p"], SEARCH_SPACE["top_p"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return f"ctx{cfg['context_length']}_s{cfg['num_samples']}_t{cfg['temperature']}_k{cfg['top_k']}_p{cfg['top_p']}".replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("CHRONOS_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "1"))
        env["PYTHONPATH"] = f"{ROOT / '.python_deps'}:{ROOT / 'repositories/chronos-forecasting/src'}:{ROOT}:{env.get('PYTHONPATH', '')}"
        max_series = os.environ.get("CHRONOS_MAX_SERIES", "0")
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            "--method chronos "
            "--prediction-length 30 "
            f"--context-length {cfg['context_length']} "
            f"--num-samples {cfg['num_samples']} "
            f"--temperature {cfg['temperature']} "
            f"--top-k {cfg['top_k']} "
            f"--top-p {cfg['top_p']} "
            f"--max-series {max_series} "
            "--chunk-size 64 "
            "--device cuda "
            "--seed 0",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"Chronos monash_weather eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def parse_config(text: str) -> dict[str, Any]:
    patterns = [
        r"NEW_CONFIG\s*[:=]\s*(\{.*?\})",
        r"```json\s*(\{.*?\})\s*```",
        r"(\{[^{}]*(?:context_length|num_samples|temperature|top_k|top_p)[^{}]*\})",
    ]
    for pattern in patterns:
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
    raise ValueError(f"could not parse config from response: {text[:500]}")


def training_log(history: list[dict[str, Any]], baseline: float) -> str:
    lines = [
        "Task: Chronos-T5-Tiny zero-shot forecasting on the official monash_weather dataset.",
        "Metric: weighted quantile loss (WQL), lower is better.",
        "Official anchor: chronos-t5-tiny-zero-shot.csv reports monash_weather WQL=0.14787595319625085.",
        f"Budget baseline WQL={baseline:.6f}, config={BASE_CONFIG}.",
        "Fixed protocol: prediction_length=30, offset=-30, all 3010 series unless CHRONOS_MAX_SERIES is set for smoke.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"WQL={m['WQL']:.6f} median_mae={m['median_mae']:.4f} series={m['num_series']} seconds={m['seconds']}"
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
    prompt = f"""You are choosing Chronos-T5-Tiny decoding and context hyperparameters.

{training_log(history, baseline)}

Search space:
{json.dumps(SEARCH_SPACE, indent=2)}

Return exactly one line:
NEW_CONFIG: {{"context_length": 512, "num_samples": 20, "temperature": 1.0, "top_k": 50, "top_p": 1.0}}

Choose the configuration most likely to reduce WQL. Do not change prediction length or dataset."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"qwen_prompt_{trial_idx}.txt").write_text(prompt)
    agent = None
    try:
        from agenthpobench.agents.open_source.qwen_agent import QwenAgent

        os.environ["CUDA_VISIBLE_DEVICES"] = os.environ.get("QWEN_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "1"))
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
        fallback = FALLBACK_CONFIGS[min(trial_idx - 1, len(FALLBACK_CONFIGS) - 1)]
        (OUT_DIR / f"qwen_error_{trial_idx}.txt").write_text(repr(exc))
        return clamp_config(fallback)
    finally:
        if agent is not None:
            del agent
        cleanup_torch()


def score(value: float, baseline: float) -> float:
    denom = baseline - PAPER_ANCHOR_WQL
    if abs(denom) < 1e-12:
        return 0.0
    return float((baseline - value) / denom)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    history: list[dict[str, Any]] = []
    baseline = run_eval("baseline", 0, BASE_CONFIG)
    baseline_wql = float(baseline["metrics"]["WQL"])
    history.append(baseline)
    current = dict(BASE_CONFIG)
    interventions = int(os.environ.get("AUTOREP_INTERVENTIONS", "5"))
    for trial_idx in range(1, interventions + 1):
        current = decide_with_qwen(history, baseline_wql, trial_idx)
        history.append(run_eval("agent", trial_idx, current))

    best = min(history, key=lambda item: float(item["metrics"]["WQL"]))
    final = history[-1]
    payload = {
        "task": "chronos_t5_tiny_monash_weather_wql",
        "paper_anchor_WQL": PAPER_ANCHOR_WQL,
        "baseline_config": BASE_CONFIG,
        "baseline_metric": baseline_wql,
        "best_metric": float(best["metrics"]["WQL"]),
        "final_metric": float(final["metrics"]["WQL"]),
        "best_score_vs_budget_baseline": score(float(best["metrics"]["WQL"]), baseline_wql),
        "final_score_vs_budget_baseline": score(float(final["metrics"]["WQL"]), baseline_wql),
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
