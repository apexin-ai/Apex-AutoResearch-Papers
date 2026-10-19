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
FORMAL_DIR = ROOT / "baselines/tpe/sparsetsf_ettm1_96_mse"
EVAL_SCRIPT = FORMAL_DIR / "eval_sparsetsf_ettm1.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "sparsetsf_ettm1_96_mse"
RUN_ID = os.environ.get("RUN_ID") or f"sparsetsf_ettm1_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "sparsetsf_ettm1_96_mse_QwenLocal_results.json"

PAPER_ANCHOR_MSE = 0.314
BASE_CONFIG = {
    "lr": 0.02,
    "weight_decay": 0.0,
    "batch_size": 256,
    "period_len": 24,
    "model_type": "linear",
    "d_model": 128,
    "grad_clip": 0.0,
    "cosine": False,
}
SEARCH_SPACE = {
    "lr": {"choices": [0.002, 0.005, 0.01, 0.02, 0.03]},
    "weight_decay": {"choices": [0.0, 1e-4, 1e-3]},
    "batch_size": {"choices": [128, 256, 512]},
    "period_len": {"choices": [6, 12, 24, 48]},
    "model_type": {"choices": ["linear", "mlp"]},
    "d_model": {"choices": [64, 128, 256]},
    "grad_clip": {"choices": [0.0, 1.0]},
    "cosine": {"choices": [False, True]},
}
FIXED = {
    "epochs": int(os.environ.get("SPARSETSF_EPOCHS", "1")),
    "seed": int(os.environ.get("SPARSETSF_SEED", "2023")),
    "seq_len": 720,
    "pred_len": 96,
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def nearest(value: Any, choices: list[Any]) -> Any:
    if isinstance(choices[0], bool):
        if isinstance(value, str):
            return value.strip().lower() in {"1", "true", "yes", "on"}
        return bool(value)
    if isinstance(choices[0], str):
        candidate = str(value).strip().lower()
        return candidate if candidate in choices else choices[0]
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "learning_rate": "lr",
        "wd": "weight_decay",
        "batch": "batch_size",
        "period": "period_len",
        "w": "period_len",
        "type": "model_type",
        "hidden": "d_model",
        "hidden_dim": "d_model",
        "clip": "grad_clip",
        "use_cosine": "cosine",
        "scheduler": "cosine",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "lr": float(nearest(merged["lr"], SEARCH_SPACE["lr"]["choices"])),
        "weight_decay": float(nearest(merged["weight_decay"], SEARCH_SPACE["weight_decay"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
        "period_len": int(nearest(merged["period_len"], SEARCH_SPACE["period_len"]["choices"])),
        "model_type": nearest(merged["model_type"], SEARCH_SPACE["model_type"]["choices"]),
        "d_model": int(nearest(merged["d_model"], SEARCH_SPACE["d_model"]["choices"])),
        "grad_clip": float(nearest(merged["grad_clip"], SEARCH_SPACE["grad_clip"]["choices"])),
        "cosine": bool(nearest(merged["cosine"], SEARCH_SPACE["cosine"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    parts = [
        f"lr{cfg['lr']}",
        f"wd{cfg['weight_decay']}",
        f"bs{cfg['batch_size']}",
        f"w{cfg['period_len']}",
        cfg["model_type"],
        f"d{cfg['d_model']}",
        f"clip{cfg['grad_clip']}",
        f"cos{int(cfg['cosine'])}",
    ]
    return "_".join(parts).replace(".", "p").replace("-", "m")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("SPARSETSF_CUDA_VISIBLE_DEVICES", "1")
        env["PYTHONPATH"] = f"{ROOT / 'repositories/SparseTSF'}:{ROOT}:{ROOT / '.python_deps'}:{env.get('PYTHONPATH', '')}"
        cosine_flag = " --cosine" if cfg["cosine"] else ""
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--seq-len {FIXED['seq_len']} "
            f"--pred-len {FIXED['pred_len']} "
            f"--period-len {cfg['period_len']} "
            f"--model-type {cfg['model_type']} "
            f"--d-model {cfg['d_model']} "
            f"--lr {cfg['lr']} "
            f"--weight-decay {cfg['weight_decay']} "
            f"--batch-size {cfg['batch_size']} "
            f"--grad-clip {cfg['grad_clip']} "
            f"--epochs {FIXED['epochs']} "
            f"--seed {FIXED['seed']} "
            "--device cuda:0"
            f"{cosine_flag}",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT / "repositories/SparseTSF"), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text[-8000:], flush=True)
            raise RuntimeError(f"SparseTSF eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def parse_config(text: str) -> dict[str, Any]:
    for pattern in [
        r"NEW_CONFIG\s*[:=]\s*(\{.*?\})",
        r"```json\s*(\{.*?\})\s*```",
        r"(\{[^{}]*(?:lr|weight_decay|batch_size|period_len|model_type|d_model|cosine)[^{}]*\})",
    ]:
        match = re.search(pattern, text, flags=re.S | re.I)
        if not match:
            continue
        payload = match.group(1)
        try:
            return json.loads(payload)
        except Exception:
            try:
                return ast.literal_eval(payload)
            except Exception:
                pass
    raise ValueError("no JSON config found")


def training_log(history: list[dict[str, Any]], baseline: float) -> str:
    lines = [
        "Task: SparseTSF ETTm1 multivariate long-term forecasting, pred_len=96.",
        "Metric: test_mse_at_best_val over the fixed epoch budget, lower is better.",
        "Paper anchor: ICML 2024 SparseTSF official long-term forecasting table reports ETTm1 horizon-96 MSE=0.314.",
        "Official script default for ETTm1 linear: seq_len=720, pred_len=96, period_len=24, batch_size=256, lr=0.02.",
        f"Budget: fixed {FIXED['epochs']} epochs and seed={FIXED['seed']} on the original ETTm1 split.",
        f"Budget baseline test_mse_at_best_val={baseline:.6f}, config={BASE_CONFIG}.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"test_mse={m['test_mse_at_best_val']:.6f} val_mse={m['best_val_mse']:.6f} "
            f"best_epoch={m['best_epoch']} seconds={m['seconds']}"
        )
    return "\n".join(lines)


def decide_with_qwen(history: list[dict[str, Any]], baseline: float) -> dict[str, Any]:

    import os as _tpe_os
    if _tpe_os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower() in {"random", "random_search", "tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
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
        rng = random.Random(f"{seed}:sparsetsf_ettm1_96_mse:{len(history)}:{state}")
        raw = {key: rng.choice(list(spec["choices"])) for key, spec in SEARCH_SPACE.items()}
        new_config = clamp_config(raw)
        return {
            "new_config": new_config,
            "raw_new_config": raw,
            "reasoning": "Uniform random sample from the constrained SparseTSF search space.",
            "confidence": 0.0,
            "metadata": {"backend": "random_search", "seed": seed, "search_space_keys": sorted(SEARCH_SPACE)},
        }

    deps = ROOT / ".python_deps"
    if deps.exists():
        sys.path.insert(0, str(deps))
    from transformers import AutoModelForCausalLM, AutoTokenizer
    import torch

    prompt = f"""You are choosing one hyperparameter configuration for a budget-limited reproduction benchmark.

{training_log(history, baseline)}

Search space:
{json.dumps(SEARCH_SPACE, indent=2)}

Return exactly one line:
NEW_CONFIG: {{"lr": 0.02, "weight_decay": 0.0, "batch_size": 256, "period_len": 24, "model_type": "linear", "d_model": 128, "grad_clip": 0.0, "cosine": false}}

Choose the config most likely to reduce test_mse_at_best_val under the fixed budget. Do not change epochs, data split, dataset, seq_len, pred_len, model family, or metric."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if os.environ.get("AUTOREP_QWEN_NO_THINK", "0").strip().lower() in {"1", "true", "yes", "on"}:
        prompt = prompt + "\n/no_think\nDo not output thinking. Return only the NEW_CONFIG line."
    (OUT_DIR / "qwen_prompt_0.txt").write_text(prompt)
    try:
        from agenthpobench.agents.api_decision_client import api_backend_enabled, call_decision_api
        if api_backend_enabled():
            response = call_decision_api(prompt, temperature=0.0, max_tokens=int(os.environ.get("AUTOREP_API_MAX_TOKENS", "384")))
            text = response.text
            (OUT_DIR / "qwen_raw_0.txt").write_text(text)
            try:
                raw = parse_config(text)
                new_config = clamp_config(raw)
                metadata = {"api_backend": True, "api": response.metadata, "model_path": str(AGENT_MODEL)}
                confidence = 0.7
                reasoning = text
            except Exception as exc:
                raw = dict(BASE_CONFIG)
                new_config = clamp_config(raw)
                metadata = {"api_backend": True, "fallback": True, "api": response.metadata, "error": str(exc), "raw_text": text[:1000]}
                confidence = 0.4
                reasoning = f"Fallback to official default config after API parse error: {exc}."
            return {"new_config": new_config, "raw_new_config": raw, "reasoning": reasoning, "confidence": confidence, "metadata": metadata}
    except Exception:
        if os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower() in {"api", "openai", "openai-compatible", "anthropic", "glm", "claude_code", "claude-code", "codex", "codex_cli", "codex-cli"}:
            raise

    os.environ["CUDA_VISIBLE_DEVICES"] = os.environ.get("QWEN_CUDA_VISIBLE_DEVICES", "1")
    tokenizer = AutoTokenizer.from_pretrained(str(AGENT_MODEL), trust_remote_code=True, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        str(AGENT_MODEL),
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
        local_files_only=True,
    )
    rendered_prompt = prompt
    if os.environ.get("AUTOREP_USE_CHAT_TEMPLATE", "0").strip().lower() in {"1", "true", "yes", "on"} and hasattr(tokenizer, "apply_chat_template"):
        try:
            rendered_prompt = tokenizer.apply_chat_template([{"role": "user", "content": prompt}], tokenize=False, add_generation_prompt=True)
        except Exception:
            rendered_prompt = prompt
    inputs = tokenizer(rendered_prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=int(os.environ.get("AUTOREP_AGENT_MAX_NEW_TOKENS", "1024")), do_sample=False)
    text = tokenizer.decode(output[0, inputs["input_ids"].shape[1] :], skip_special_tokens=True)
    (OUT_DIR / "qwen_raw_0.txt").write_text(text)
    try:
        raw = parse_config(text)
        new_config = clamp_config(raw)
        metadata = {"direct_prompt": True, "model_path": str(AGENT_MODEL)}
        confidence = 0.7
        reasoning = text
    except Exception as exc:
        raw = dict(BASE_CONFIG)
        new_config = clamp_config(raw)
        metadata = {"fallback": True, "error": str(exc), "raw_text": text[:1000]}
        confidence = 0.4
        reasoning = f"Fallback to official default config after parse error: {exc}."
    del model
    try:
        torch.cuda.empty_cache()
    except Exception:
        pass
    return {
        "new_config": new_config,
        "raw_new_config": raw,
        "reasoning": reasoning,
        "confidence": confidence,
        "metadata": metadata,
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    baseline = run_eval("baseline", 0, BASE_CONFIG)
    baseline_mse = baseline["metrics"]["test_mse_at_best_val"]
    decision = decide_with_qwen([baseline], baseline_mse)
    final = run_eval("agent", 1, decision["new_config"])
    final_mse = final["metrics"]["test_mse_at_best_val"]
    denom = baseline_mse - PAPER_ANCHOR_MSE
    normalized = (baseline_mse - final_mse) / denom if abs(denom) > 1e-12 else 0.0
    payload = {
        "task_id": "sparsetsf_ettm1_96_mse",
        "agent": os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal"),
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "paper_anchor_mse": PAPER_ANCHOR_MSE,
        "budget_baseline_mse": baseline_mse,
        "final_mse": final_mse,
        "normalized_score": normalized,
        "higher_is_better": False,
        "metric": "test_mse_at_best_val",
        "baseline": baseline,
        "decision": decision,
        "final": final,
        "result_dir": str(OUT_DIR),
    }
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(payload, indent=2))
    (OUT_DIR / "summary.json").write_text(json.dumps(payload, indent=2))
    print("FINAL_RESULT " + json.dumps(payload, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
