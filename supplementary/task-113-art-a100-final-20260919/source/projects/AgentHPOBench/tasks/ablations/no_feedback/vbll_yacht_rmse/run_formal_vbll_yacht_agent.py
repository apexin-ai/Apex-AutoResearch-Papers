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
FORMAL_DIR = ROOT / "tasks/ablations/no_feedback/vbll_yacht_rmse"
EVAL_SCRIPT = FORMAL_DIR / "eval_vbll_yacht.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "vbll_yacht_rmse"
RUN_ID = os.environ.get("RUN_ID") or f"vbll_yacht_rmse_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "vbll_yacht_rmse_QwenLocal_results.json"

PAPER_ANCHOR_RMSE = 0.86
BASE_CONFIG = {
    "hidden_features": 64,
    "num_layers": 2,
    "parameterization": "diagonal",
    "lr": 1e-3,
    "weight_decay": 1e-4,
    "batch_size": 32,
    "reg_weight_scale": 1.0,
    "prior_scale": 1.0,
    "wishart_scale": 0.1,
    "dropout": 0.0,
    "use_scheduler": False,
}
SEARCH_SPACE = {
    "hidden_features": {"choices": [32, 64, 128]},
    "num_layers": {"choices": [1, 2, 3]},
    "parameterization": {"choices": ["diagonal", "dense"]},
    "lr": {"choices": [3e-4, 1e-3, 3e-3]},
    "weight_decay": {"choices": [0.0, 1e-4, 1e-3]},
    "batch_size": {"choices": [16, 32, 64]},
    "reg_weight_scale": {"choices": [0.1, 1.0, 10.0]},
    "prior_scale": {"choices": [0.1, 1.0, 10.0]},
    "wishart_scale": {"choices": [0.01, 0.1, 1.0]},
    "dropout": {"choices": [0.0, 0.05, 0.1]},
    "use_scheduler": {"choices": [False, True]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "vbll_yacht_rmse", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)

FIXED = {"epochs": int(os.environ.get("VBLL_EPOCHS", "80"))}


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
        "hidden": "hidden_features",
        "width": "hidden_features",
        "layers": "num_layers",
        "parameterization_type": "parameterization",
        "learning_rate": "lr",
        "wd": "weight_decay",
        "batch": "batch_size",
        "kl_weight": "reg_weight_scale",
        "reg_weight": "reg_weight_scale",
        "scheduler": "use_scheduler",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "hidden_features": int(nearest(merged["hidden_features"], SEARCH_SPACE["hidden_features"]["choices"])),
        "num_layers": int(nearest(merged["num_layers"], SEARCH_SPACE["num_layers"]["choices"])),
        "parameterization": str(nearest(merged["parameterization"], SEARCH_SPACE["parameterization"]["choices"])),
        "lr": float(nearest(merged["lr"], SEARCH_SPACE["lr"]["choices"])),
        "weight_decay": float(nearest(merged["weight_decay"], SEARCH_SPACE["weight_decay"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
        "reg_weight_scale": float(nearest(merged["reg_weight_scale"], SEARCH_SPACE["reg_weight_scale"]["choices"])),
        "prior_scale": float(nearest(merged["prior_scale"], SEARCH_SPACE["prior_scale"]["choices"])),
        "wishart_scale": float(nearest(merged["wishart_scale"], SEARCH_SPACE["wishart_scale"]["choices"])),
        "dropout": float(nearest(merged["dropout"], SEARCH_SPACE["dropout"]["choices"])),
        "use_scheduler": bool(nearest(merged["use_scheduler"], SEARCH_SPACE["use_scheduler"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return (
        f"h{cfg['hidden_features']}_l{cfg['num_layers']}_{cfg['parameterization']}"
        f"_lr{cfg['lr']}_wd{cfg['weight_decay']}_b{cfg['batch_size']}"
        f"_reg{cfg['reg_weight_scale']}_prior{cfg['prior_scale']}_wish{cfg['wishart_scale']}"
        f"_drop{cfg['dropout']}_sched{int(cfg['use_scheduler'])}"
    ).replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("VBLL_CUDA_VISIBLE_DEVICES", "1")
        env["PYTHONPATH"] = f"{ROOT / 'repositories/vbll'}:{ROOT / '.python_deps'}:{env.get('PYTHONPATH', '')}"
        scheduler_flag = "--use-scheduler" if cfg["use_scheduler"] else "--no-use-scheduler"
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} "
            f"--hidden-features {cfg['hidden_features']} "
            f"--num-layers {cfg['num_layers']} "
            f"--parameterization {cfg['parameterization']} "
            f"--lr {cfg['lr']} "
            f"--weight-decay {cfg['weight_decay']} "
            f"--batch-size {cfg['batch_size']} "
            f"--epochs {FIXED['epochs']} "
            f"--reg-weight-scale {cfg['reg_weight_scale']} "
            f"--prior-scale {cfg['prior_scale']} "
            f"--wishart-scale {cfg['wishart_scale']} "
            f"--dropout {cfg['dropout']} "
            f"{scheduler_flag} "
            "--select-best-val "
            "--device cuda:0 "
            "--seed 1",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"VBLL eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def parse_config(text: str) -> dict[str, Any]:
    for pattern in [r"NEW_CONFIG\s*[:=]\s*(\{.*?\})", r"```json\s*(\{.*?\})\s*```", r"(\{[^{}]*(?:hidden|lr|parameterization)[^{}]*\})"]:
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
    history = history[:1]  # No-feedback: expose only the baseline observation.
    lines = [
        "Task: VBLL ICLR 2024 Yacht Hydrodynamics regression.",
        "Metric: test_rmse, lower is better. Secondary metric: test_nll.",
        "Paper anchor: Table 2 reports Yacht VBLL RMSE=0.86 and NLL=1.29.",
        f"Budget: fixed {FIXED['epochs']} epochs, fixed seed/split, validation-selected checkpoint.",
        f"Budget baseline test_rmse={baseline:.6f}, config={BASE_CONFIG}.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"test_rmse={m['test_rmse']:.6f} val_rmse={m['val_rmse']:.6f} "
            f"test_nll={m['test_nll']:.6f} train_loss={m['train_loss_final']:.6f}"
        )
    return "\n".join(lines)


def decide_with_qwen(history: list[dict[str, Any]], baseline: float) -> dict[str, Any]:

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
        rng = random.Random(f"{seed}:vbll_yacht_rmse:{len(history)}:{state}")
        raw = {key: rng.choice(list(spec["choices"])) for key, spec in SEARCH_SPACE.items()}
        new_config = clamp_config(raw)
        return {
            "new_config": new_config,
            "raw_new_config": raw,
            "reasoning": "Uniform random sample from the constrained VBLL search space.",
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
NEW_CONFIG: {{"hidden_features": 64, "num_layers": 2, "parameterization": "diagonal", "lr": 0.001, "weight_decay": 0.0001, "batch_size": 32, "reg_weight_scale": 1.0, "prior_scale": 1.0, "wishart_scale": 0.1, "dropout": 0.0, "use_scheduler": false}}

Choose the config most likely to reduce test_rmse under the fixed budget. Do not change epochs or data split."""
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
                raw = {"hidden_features": 128, "num_layers": 2, "parameterization": "dense", "lr": 0.003, "weight_decay": 0.0, "batch_size": 16, "reg_weight_scale": 0.1, "prior_scale": 1.0, "wishart_scale": 0.1, "dropout": 0.0, "use_scheduler": True}
                new_config = clamp_config(raw)
                metadata = {"api_backend": True, "fallback": True, "api": response.metadata, "error": str(exc), "raw_text": text[:1000]}
                confidence = 0.4
                reasoning = f"Fallback after API parse failure: {exc}. Try higher capacity, faster lr, lower KL regularization, and scheduler."
            decision = {"new_config": new_config, "raw_new_config": raw, "reasoning": reasoning, "confidence": confidence, "metadata": metadata}
            (OUT_DIR / "qwen_decision_0.json").write_text(json.dumps(decision, indent=2))
            return decision
    except Exception:
        if os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower() in {"api", "openai", "openai-compatible", "anthropic", "glm", "claude_code", "claude-code", "codex", "codex_cli", "codex-cli"}:
            raise

    os.environ["CUDA_VISIBLE_DEVICES"] = os.environ.get("QWEN_CUDA_VISIBLE_DEVICES", "1")
    tokenizer = AutoTokenizer.from_pretrained(str(AGENT_MODEL), trust_remote_code=True, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(str(AGENT_MODEL), torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True, local_files_only=True)
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
        raw = {"hidden_features": 128, "num_layers": 2, "parameterization": "dense", "lr": 0.003, "weight_decay": 0.0, "batch_size": 16, "reg_weight_scale": 0.1, "prior_scale": 1.0, "wishart_scale": 0.1, "dropout": 0.0, "use_scheduler": True}
        new_config = clamp_config(raw)
        metadata = {"fallback": True, "error": str(exc), "raw_text": text[:1000]}
        confidence = 0.4
        reasoning = f"Fallback after parse failure: {exc}. Try higher capacity, faster lr, lower KL regularization, and scheduler."
    del model
    torch.cuda.empty_cache()
    decision = {"new_config": new_config, "raw_new_config": raw, "reasoning": reasoning, "confidence": confidence, "metadata": metadata}
    (OUT_DIR / "qwen_decision_0.json").write_text(json.dumps(decision, indent=2))
    return decision


def normalized_score(value: float, baseline: float) -> float:
    denom = baseline - PAPER_ANCHOR_RMSE
    return 0.0 if denom <= 0 else (baseline - value) / denom


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    history = [run_eval("baseline", 0, BASE_CONFIG)]
    baseline = float(history[0]["metrics"]["test_rmse"])
    decision = decide_with_qwen(history, baseline)
    history.append(run_eval("final", 1, decision["new_config"]))
    final = history[-1]
    final_rmse = float(final["metrics"]["test_rmse"])
    score = normalized_score(final_rmse, baseline)
    result = {
        "task_id": "vbll_yacht_rmse",
        "repo": "vbll",
        "success": True,
        "dataset": "UCI Yacht Hydrodynamics",
        "metric": "test_rmse",
        "direction": "lower_is_better",
        "paper_anchor": PAPER_ANCHOR_RMSE,
        "paper_anchor_secondary_nll": 1.29,
        "paper_anchor_source": "VBLL ICLR 2024 paper Table 2, Yacht dataset.",
        "budget": FIXED | {"baseline_config": BASE_CONFIG, "search_space": SEARCH_SPACE},
        "baseline_metrics": history[0]["metrics"],
        "final_metrics": final["metrics"],
        "final_config": final["config"],
        "decisions": [decision],
        "decisions_made": 1,
        "history": history,
        "normalized_score": score,
        "score": {
            "direction": "lower_is_better",
            "official_budget_baseline": baseline,
            "paper_anchor": PAPER_ANCHOR_RMSE,
            "normalized_score": score,
            "scoring_eligible": True,
        },
        "run_id": RUN_ID,
        "run_dir": str(OUT_DIR),
        "result_file": str(RESULT_FILE),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.write_text(json.dumps(result, indent=2))
    (OUT_DIR / "summary.json").write_text(json.dumps(result, indent=2))
    print("RESULT_JSON " + json.dumps(result, sort_keys=True), flush=True)
    print(RESULT_FILE, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
