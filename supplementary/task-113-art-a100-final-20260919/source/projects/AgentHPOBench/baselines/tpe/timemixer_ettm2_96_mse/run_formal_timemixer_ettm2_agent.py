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
FORMAL_DIR = ROOT / "baselines/tpe/timemixer_ettm2_96_mse"
EVAL_SCRIPT = FORMAL_DIR / "eval_timemixer_ettm2.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "timemixer_ettm2_96_mse"
RUN_ID = os.environ.get("RUN_ID") or f"timemixer_ettm2_96_mse_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "timemixer_ettm2_96_mse_QwenLocal_results.json"

PAPER_ANCHOR_MSE = 0.175
BASE_CONFIG = {
    "d_model": 8,
    "d_ff": 16,
    "e_layers": 1,
    "down_sampling_layers": 1,
    "down_sampling_window": 2,
    "learning_rate": 0.01,
    "batch_size": 512,
}
SEARCH_SPACE = {
    "d_model": {"choices": [8, 16, 32]},
    "d_ff": {"choices": [16, 32, 64]},
    "e_layers": {"choices": [1, 2]},
    "down_sampling_layers": {"choices": [1, 2, 3]},
    "down_sampling_window": {"choices": [2, 3]},
    "learning_rate": {"choices": [0.001, 0.005, 0.01]},
    "batch_size": {"choices": [128, 256, 512]},
}
FIXED = {"epochs": int(os.environ.get("TIMEMIXER_EPOCHS", "3"))}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def nearest(value: Any, choices: list[Any]) -> Any:
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        text = str(value).lower().strip()
        for item in choices:
            if str(item).lower() == text:
                return item
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "lr": "learning_rate",
        "learning_rate": "learning_rate",
        "width": "d_model",
        "hidden_size": "d_model",
        "ffn_dim": "d_ff",
        "layers": "e_layers",
        "num_layers": "e_layers",
        "down_layers": "down_sampling_layers",
        "downsampling_layers": "down_sampling_layers",
        "window": "down_sampling_window",
        "downsampling_window": "down_sampling_window",
        "batch": "batch_size",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "d_model": int(nearest(merged["d_model"], SEARCH_SPACE["d_model"]["choices"])),
        "d_ff": int(nearest(merged["d_ff"], SEARCH_SPACE["d_ff"]["choices"])),
        "e_layers": int(nearest(merged["e_layers"], SEARCH_SPACE["e_layers"]["choices"])),
        "down_sampling_layers": int(nearest(merged["down_sampling_layers"], SEARCH_SPACE["down_sampling_layers"]["choices"])),
        "down_sampling_window": int(nearest(merged["down_sampling_window"], SEARCH_SPACE["down_sampling_window"]["choices"])),
        "learning_rate": float(nearest(merged["learning_rate"], SEARCH_SPACE["learning_rate"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return (
        f"dm{cfg['d_model']}_df{cfg['d_ff']}_l{cfg['e_layers']}_down{cfg['down_sampling_layers']}"
        f"_win{cfg['down_sampling_window']}_lr{cfg['learning_rate']}_bs{cfg['batch_size']}"
    ).replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["TIMEMIXER_CUDA_VISIBLE_DEVICES"] = os.environ.get("TIMEMIXER_CUDA_VISIBLE_DEVICES", "1")
        env["PYTHONPATH"] = f"{ROOT / 'repositories/TimeMixer'}:{ROOT / '.python_deps'}"
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--run-name {kind}{trial_idx} "
            f"--d-model {cfg['d_model']} "
            f"--d-ff {cfg['d_ff']} "
            f"--e-layers {cfg['e_layers']} "
            f"--down-sampling-layers {cfg['down_sampling_layers']} "
            f"--down-sampling-window {cfg['down_sampling_window']} "
            f"--learning-rate {cfg['learning_rate']} "
            f"--batch-size {cfg['batch_size']} "
            f"--epochs {FIXED['epochs']} "
            "--patience 2",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        (trial_dir / "outer.log").write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"TimeMixer eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def parse_config(text: str) -> dict[str, Any]:
    for pattern in [
        r"NEW_CONFIG\s*[:=]\s*(\{.*?\})",
        r"```json\s*(\{.*?\})\s*```",
        r"(\{[^{}]*(?:d_model|learning_rate|batch_size|down_sampling)[^{}]*\})",
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
        "Task: TimeMixer ICLR 2024, ETTm2 multivariate forecasting, seq_len=96, pred_len=96.",
        "Metric: test_mse, lower is better. Paper/README searched-hyperparameter anchor for ETTm2-96: MSE=0.175, MAE=0.258.",
        "Budget: fixed 3 train epochs, official ETTm2 split and official TimeMixer code.",
        "Short-budget prior: the official unified script uses d_model=16, d_ff=32, e_layers=2, down_sampling_layers=3, window=2, lr=0.01, batch_size=128; it reached test_mse about 0.3779 in a probe.",
        f"Budget baseline test_mse={baseline:.6f}, config={BASE_CONFIG}.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"test_mse={m['test_mse']:.6f} test_mae={m['test_mae']:.6f} "
            f"val_loss={m['val_loss_final']:.6f} train_loss={m['train_loss_final']:.6f}"
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
        rng = random.Random(f"{seed}:timemixer_ettm2_96_mse:{len(history)}:{state}")
        raw = {key: rng.choice(list(spec["choices"])) for key, spec in SEARCH_SPACE.items()}
        new_config = clamp_config(raw)
        return {
            "new_config": new_config,
            "raw_new_config": raw,
            "reasoning": "Uniform random sample from the constrained TimeMixer search space.",
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
NEW_CONFIG: {{"d_model": 16, "d_ff": 32, "e_layers": 2, "down_sampling_layers": 3, "down_sampling_window": 2, "learning_rate": 0.01, "batch_size": 128}}

Choose the config most likely to reduce test_mse under the fixed 3-epoch budget. Do not change the dataset, seq_len, pred_len, epochs, model family, or metric."""
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
                raw = {"d_model": 16, "d_ff": 32, "e_layers": 2, "down_sampling_layers": 3, "down_sampling_window": 2, "learning_rate": 0.01, "batch_size": 128}
                new_config = clamp_config(raw)
                metadata = {"api_backend": True, "fallback": True, "api": response.metadata, "error": str(exc), "raw_text": text[:1000]}
                confidence = 0.4
                reasoning = f"Fallback to official unified config after API parse error: {exc}."
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
    text = tokenizer.decode(output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    (OUT_DIR / "qwen_raw_0.txt").write_text(text)
    try:
        raw = parse_config(text)
        new_config = clamp_config(raw)
        metadata = {"direct_prompt": True, "model_path": str(AGENT_MODEL)}
        confidence = 0.7
        reasoning = text
    except Exception as exc:
        raw = {"d_model": 16, "d_ff": 32, "e_layers": 2, "down_sampling_layers": 3, "down_sampling_window": 2, "learning_rate": 0.01, "batch_size": 128}
        new_config = clamp_config(raw)
        metadata = {"fallback": True, "error": str(exc), "raw_text": text[:1000]}
        confidence = 0.4
        reasoning = f"Fallback to official unified config after parse error: {exc}."
    del model
    try:
        torch.cuda.empty_cache()
    except Exception:
        pass
    return {"new_config": new_config, "raw_new_config": raw, "reasoning": reasoning, "confidence": confidence, "metadata": metadata}


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    baseline = run_eval("baseline", 0, BASE_CONFIG)
    baseline_mse = baseline["metrics"]["test_mse"]
    decision = decide_with_qwen([baseline], baseline_mse)
    final = run_eval("agent", 1, decision["new_config"])
    final_mse = final["metrics"]["test_mse"]
    denom = baseline_mse - PAPER_ANCHOR_MSE
    normalized = (baseline_mse - final_mse) / denom if abs(denom) > 1e-12 else 0.0
    payload = {
        "task_id": "timemixer_ettm2_96_mse",
        "agent": os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal"),
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "paper_anchor_mse": PAPER_ANCHOR_MSE,
        "budget_baseline_mse": baseline_mse,
        "final_mse": final_mse,
        "normalized_score": normalized,
        "higher_is_better": False,
        "metric": "test_mse",
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
