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
FORMAL_DIR = ROOT / "tasks/main/tabm_california_rmse"
EVAL_SCRIPT = FORMAL_DIR / "eval_tabm_california.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "tabm_california_rmse"
RUN_ID = os.environ.get("RUN_ID") or f"tabm_california_rmse_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "tabm_california_rmse_QwenLocal_results.json"

PAPER_ANCHOR_RMSE = 0.44139199088313996
BASE_CONFIG = {
    "arch_type": "plain",
    "k": 8,
    "n_blocks": 2,
    "d_block": 128,
    "dropout": 0.1,
    "lr": 0.001,
    "weight_decay": 0.0001,
    "batch_size": 256,
    "use_scheduler": False,
}
SEARCH_SPACE = {
    "arch_type": {"choices": ["plain", "tabm-mini", "tabm"]},
    "k": {"choices": [4, 8, 16, 32]},
    "n_blocks": {"choices": [2, 3]},
    "d_block": {"choices": [128, 256, 400]},
    "dropout": {"choices": [0.0, 0.1, 0.2]},
    "lr": {"choices": [0.0003, 0.001, 0.003]},
    "weight_decay": {"choices": [0.0, 0.0001, 0.001]},
    "batch_size": {"choices": [128, 256, 512]},
    "use_scheduler": {"choices": [False, True]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "tabm_california_rmse", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)

FIXED = {
    "epochs": int(os.environ.get("TABM_EPOCHS", "50")),
    "seed": int(os.environ.get("TABM_SEED", "1")),
}



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
    if choices and isinstance(choices[0], str):
        text = str(value).lower().strip()
        for choice in choices:
            if text == str(choice).lower():
                return choice
        return choices[0]
    if choices and isinstance(choices[0], bool):
        if isinstance(value, bool):
            return value
        return str(value).strip().lower() in {"true", "1", "yes", "y"}
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "architecture": "arch_type",
        "model": "arch_type",
        "model_type": "arch_type",
        "num_models": "k",
        "ensemble_size": "k",
        "blocks": "n_blocks",
        "n_layers": "n_blocks",
        "width": "d_block",
        "hidden_size": "d_block",
        "learning_rate": "lr",
        "wd": "weight_decay",
        "batch": "batch_size",
        "scheduler": "use_scheduler",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "arch_type": str(nearest(merged["arch_type"], SEARCH_SPACE["arch_type"]["choices"])),
        "k": int(nearest(merged["k"], SEARCH_SPACE["k"]["choices"])),
        "n_blocks": int(nearest(merged["n_blocks"], SEARCH_SPACE["n_blocks"]["choices"])),
        "d_block": int(nearest(merged["d_block"], SEARCH_SPACE["d_block"]["choices"])),
        "dropout": float(nearest(merged["dropout"], SEARCH_SPACE["dropout"]["choices"])),
        "lr": float(nearest(merged["lr"], SEARCH_SPACE["lr"]["choices"])),
        "weight_decay": float(nearest(merged["weight_decay"], SEARCH_SPACE["weight_decay"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
        "use_scheduler": bool(nearest(merged["use_scheduler"], SEARCH_SPACE["use_scheduler"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return (
        f"{cfg['arch_type']}_k{cfg['k']}_b{cfg['n_blocks']}_d{cfg['d_block']}"
        f"_drop{cfg['dropout']}_lr{cfg['lr']}_wd{cfg['weight_decay']}"
        f"_bs{cfg['batch_size']}_sched{int(cfg['use_scheduler'])}"
    ).replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("TABM_CUDA_VISIBLE_DEVICES", "1")
        env["PYTHONPATH"] = f"{ROOT / 'repositories/tabm'}:{ROOT / '.python_deps'}:{env.get('PYTHONPATH', '')}"
        scheduler_flag = "--use-scheduler" if cfg["use_scheduler"] else "--no-use-scheduler"
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--arch-type {cfg['arch_type']} "
            f"--k {cfg['k']} "
            f"--n-blocks {cfg['n_blocks']} "
            f"--d-block {cfg['d_block']} "
            f"--dropout {cfg['dropout']} "
            f"--lr {cfg['lr']} "
            f"--weight-decay {cfg['weight_decay']} "
            f"--batch-size {cfg['batch_size']} "
            f"--epochs {FIXED['epochs']} "
            f"{scheduler_flag} "
            "--early-stop --patience 12 "
            "--device cuda:0 "
            f"--seed {FIXED['seed']}",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"TabM eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def parse_config(text: str) -> dict[str, Any]:
    for pattern in [
        r"NEW_CONFIG\s*[:=]\s*(\{.*?\})",
        r"```json\s*(\{.*?\})\s*```",
        r"(\{[^{}]*(?:arch_type|lr|d_block|batch_size)[^{}]*\})",
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
        "Task: TabM ICLR 2025 California Housing regression.",
        "Metric: test_rmse in sklearn California target units, lower is better.",
        "Paper anchor: official tabm repo 15-seed California TabM mean test_rmse=0.441392.",
        "Paper MLP reference: official repo 15-seed California MLP mean test_rmse=0.494834.",
        "Official winning-ish hyperparameters in the repo include arch_type=tabm, k=32, n_blocks=3, d_block=400, dropout about 0.2, lr about 0.001.",
        f"Budget: fixed {FIXED['epochs']} epochs, fixed split/seed, validation-selected checkpoint.",
        f"Budget baseline test_rmse={baseline:.6f}, config={BASE_CONFIG}.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"test_rmse={m['test_rmse']:.6f} val_rmse={m['val_rmse']:.6f} "
            f"train_loss={m['train_loss_final']:.6f} epochs_ran={m['epochs_ran']}"
        )
    return "\n".join(lines)


def decide_with_qwen(history: list[dict[str, Any]], baseline: float) -> dict[str, Any]:

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
        rng = random.Random(f"{seed}:tabm_california_rmse:{len(history)}:{state}")
        raw = {key: rng.choice(list(values)) for key, values in SEARCH_SPACE.items()}
        new_config = clamp_config(raw)
        return {
            "new_config": new_config,
            "raw_new_config": raw,
            "reasoning": "Uniform random sample from the constrained TabM search space.",
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
NEW_CONFIG: {{"arch_type": "tabm", "k": 32, "n_blocks": 3, "d_block": 400, "dropout": 0.2, "lr": 0.001, "weight_decay": 0.0001, "batch_size": 256, "use_scheduler": true}}

Choose the config most likely to reduce test_rmse under the fixed budget. Do not change epochs, data split, seed, or metric."""
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
                raw = {"arch_type": "tabm", "k": 32, "n_blocks": 3, "d_block": 400, "dropout": 0.2, "lr": 0.001, "weight_decay": 0.0001, "batch_size": 256, "use_scheduler": True}
                new_config = clamp_config(raw)
                metadata = {"api_backend": True, "fallback": True, "api": response.metadata, "error": str(exc), "raw_text": text[:1000]}
                confidence = 0.4
                reasoning = f"Fallback to official-like TabM config after API parse error: {exc}."
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
        raw = {
            "arch_type": "tabm",
            "k": 32,
            "n_blocks": 3,
            "d_block": 400,
            "dropout": 0.2,
            "lr": 0.001,
            "weight_decay": 0.0001,
            "batch_size": 256,
            "use_scheduler": True,
        }
        new_config = clamp_config(raw)
        metadata = {"fallback": True, "error": str(exc), "raw_text": text[:1000]}
        confidence = 0.4
        reasoning = f"Fallback to official-like TabM config after parse error: {exc}."
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
    baseline_rmse = baseline["metrics"]["test_rmse"]
    decision = decide_with_qwen([baseline], baseline_rmse)
    final = run_eval("agent", 1, decision["new_config"])
    final_rmse = final["metrics"]["test_rmse"]
    denom = baseline_rmse - PAPER_ANCHOR_RMSE
    normalized = (baseline_rmse - final_rmse) / denom if abs(denom) > 1e-12 else 0.0
    payload = {
        "task_id": "tabm_california_rmse",
        "agent": os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal"),
        "model_path": str(AGENT_MODEL),
        "run_id": RUN_ID,
        "paper_anchor_rmse": PAPER_ANCHOR_RMSE,
        "budget_baseline_rmse": baseline_rmse,
        "final_rmse": final_rmse,
        "normalized_score": normalized,
        "higher_is_better": False,
        "metric": "test_rmse",
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
