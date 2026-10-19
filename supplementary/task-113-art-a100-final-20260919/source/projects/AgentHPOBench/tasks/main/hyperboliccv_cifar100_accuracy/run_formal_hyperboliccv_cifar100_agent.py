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
FORMAL_DIR = ROOT / "tasks/main/hyperboliccv_cifar100_accuracy"
EVAL_SCRIPT = FORMAL_DIR / "eval_hyperboliccv_cifar100.py"
AGENT_MODEL = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
RESULT_ROOT = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "hyperboliccv_cifar100_accuracy"
RUN_ID = os.environ.get("RUN_ID") or f"hyperboliccv_cifar100_qwen3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
OUT_DIR = RESULT_ROOT / "runs" / RUN_ID
RESULT_FILE = RESULT_ROOT / "hyperboliccv_cifar100_accuracy_QwenLocal_results.json"

PAPER_ANCHOR = 78.07
FIXED = {
    "num_epochs": int(os.environ.get("HYPERCV_NUM_EPOCHS", "2")),
    "train_batches": int(os.environ.get("HYPERCV_TRAIN_BATCHES", "200")),
}
BASE_CONFIG = {
    "model_type": "E",
    "embedding_dim": 512,
    "lr": 0.1,
    "weight_decay": 5e-4,
    "batch_size": 128,
    "use_lr_scheduler": False,
}
SEARCH_SPACE = {
    "model_type": {"choices": ["E", "EL", "L"]},
    "embedding_dim": {"choices": [256, 512]},
    "lr": {"choices": [0.03, 0.1, 0.2]},
    "weight_decay": {"choices": [1e-4, 5e-4, 1e-3]},
    "batch_size": {"choices": [128, 256]},
    "use_lr_scheduler": {"choices": [False, True]},
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "hyperboliccv_cifar100_accuracy", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
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
    if choices and isinstance(choices[0], str):
        text = str(value).strip().upper()
        return text if text in choices else choices[0]
    if choices and isinstance(choices[0], bool):
        if isinstance(value, bool):
            return value
        return str(value).strip().lower() in {"1", "true", "yes", "y"}
    try:
        numeric = float(value)
        return min(choices, key=lambda item: abs(float(item) - numeric))
    except Exception:
        return choices[0]


def clamp_config(config: dict[str, Any]) -> dict[str, Any]:
    aliases = {
        "model": "model_type",
        "geometry": "model_type",
        "embed_dim": "embedding_dim",
        "learning_rate": "lr",
        "wd": "weight_decay",
        "batch": "batch_size",
        "scheduler": "use_lr_scheduler",
    }
    merged = dict(BASE_CONFIG)
    for key, value in config.items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    return {
        "model_type": str(nearest(merged["model_type"], SEARCH_SPACE["model_type"]["choices"])),
        "embedding_dim": int(nearest(merged["embedding_dim"], SEARCH_SPACE["embedding_dim"]["choices"])),
        "lr": float(nearest(merged["lr"], SEARCH_SPACE["lr"]["choices"])),
        "weight_decay": float(nearest(merged["weight_decay"], SEARCH_SPACE["weight_decay"]["choices"])),
        "batch_size": int(nearest(merged["batch_size"], SEARCH_SPACE["batch_size"]["choices"])),
        "use_lr_scheduler": bool(nearest(merged["use_lr_scheduler"], SEARCH_SPACE["use_lr_scheduler"]["choices"])),
    }


def slug(config: dict[str, Any]) -> str:
    cfg = clamp_config(config)
    return (
        f"{cfg['model_type']}_ed{cfg['embedding_dim']}_lr{cfg['lr']}_wd{cfg['weight_decay']}"
        f"_bs{cfg['batch_size']}_sched{int(cfg['use_lr_scheduler'])}"
    ).replace(".", "p")


def run_eval(kind: str, trial_idx: int, config: dict[str, Any]) -> dict[str, Any]:
    cfg = clamp_config(config)
    trial_dir = OUT_DIR / kind / f"trial{trial_idx}_{slug(cfg)}"
    metrics_path = trial_dir / "results.json"
    log_path = trial_dir / "eval.log"
    if not metrics_path.exists():
        trial_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = os.environ.get("HYPERCV_CUDA_VISIBLE_DEVICES", "1")
        env["PYTHONPATH"] = (
            f"{ROOT / 'repositories/HyperbolicCV/code/classification'}:"
            f"{ROOT / 'repositories/HyperbolicCV/code'}:"
            f"{ROOT / '.python_deps'}:{env.get('PYTHONPATH', '')}"
        )
        scheduler_flag = "--use-lr-scheduler" if cfg["use_lr_scheduler"] else "--no-use-lr-scheduler"
        cmd = [
            "bash",
            "-lc",
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh && "
            "conda activate autorep-vlm2vec && "
            f"python {EVAL_SCRIPT} "
            f"--results-dir {trial_dir} --dataset CIFAR-100 "
            f"--model-type {cfg['model_type']} "
            f"--embedding-dim {cfg['embedding_dim']} "
            f"--lr {cfg['lr']} "
            f"--weight-decay {cfg['weight_decay']} "
            f"--batch-size {cfg['batch_size']} "
            f"--num-epochs {FIXED['num_epochs']} "
            f"--train-batches {FIXED['train_batches']} "
            f"{scheduler_flag} "
            "--device cuda:0 "
            f"--seed {1 + int(os.environ.get('AUTOREP_REPLICATE_SEED', '0'))}",
        ]
        started = time.time()
        proc = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = proc.stdout.decode("utf-8", errors="replace")
        log_path.write_text(text)
        if proc.returncode != 0:
            print(text, flush=True)
            raise RuntimeError(f"HyperbolicCV eval failed rc={proc.returncode}")
        payload = load_json(metrics_path)
        payload["seconds_outer"] = round(time.time() - started, 3)
        metrics_path.write_text(json.dumps(payload, indent=2))
    payload = load_json(metrics_path)
    return {"trial": trial_idx, "kind": kind, "config": cfg, "metrics": payload, "output_dir": str(trial_dir)}


def parse_config(text: str) -> dict[str, Any]:
    patterns = [
        r"NEW_CONFIG\s*[:=]\s*(\{.*?\})",
        r"```json\s*(\{.*?\})\s*```",
        r"(\{[^{}]*(?:model_type|learning_rate|lr|batch_size)[^{}]*\})",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.S | re.I)
        if not match:
            continue
        candidate = match.group(1)
        try:
            return json.loads(candidate)
        except Exception:
            try:
                return ast.literal_eval(candidate)
            except Exception:
                continue
    raise ValueError(f"could not parse config from Qwen output: {text[:500]}")


def training_log(history: list[dict[str, Any]], baseline: float) -> str:
    lines = [
        "Task: HyperbolicCV ICLR 2024 CIFAR-100 classification.",
        "Metric: test_accuracy_percent, higher is better.",
        "Paper anchor: README Table 1 reports CIFAR-100 accuracy 78.07 for HCNN Lorentz and 77.72 for Euclidean ResNet-18.",
        f"Budget: {FIXED['num_epochs']} epochs, first {FIXED['train_batches']} train batches per epoch, full CIFAR-100 test set.",
        f"Budget baseline accuracy={baseline:.4f}, config={BASE_CONFIG}.",
        "Model types: E=Euclidean ResNet-18/SGD, EL=Euclidean encoder + Lorentz decoder/RiemannianSGD, L=fully Lorentz HCNN/RiemannianSGD.",
    ]
    for item in history:
        m = item["metrics"]
        lines.append(
            f"Trial {item['trial']} {item['kind']}: config={item['config']} "
            f"test_acc={m['test_accuracy_percent']:.4f} train_acc={m['train_accuracy_last_percent']:.4f} "
            f"test_loss={m['test_loss']:.4f} seconds={m['seconds']:.1f}"
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
        rng = random.Random(f"{seed}:hyperboliccv_cifar100_accuracy:{len(history)}:{state}")
        raw = {key: rng.choice(list(spec["choices"])) for key, spec in SEARCH_SPACE.items()}
        new_config = clamp_config(raw)
        return {
            "new_config": new_config,
            "raw_new_config": raw,
            "reasoning": "Uniform random sample from the constrained HyperbolicCV search space.",
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
NEW_CONFIG: {{"model_type": "E", "embedding_dim": 512, "lr": 0.1, "weight_decay": 0.0005, "batch_size": 128, "use_lr_scheduler": false}}

Choose the configuration most likely to improve test_accuracy_percent under this short budget. Do not change the budget."""

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
                raw_config = parse_config(text)
                new_config = clamp_config(raw_config)
                reasoning = text
                metadata = {"api_backend": True, "api": response.metadata, "model_path": str(AGENT_MODEL)}
                confidence = 0.7
            except Exception as exc:
                raw_config = {"model_type": "E", "embedding_dim": 512, "lr": 0.2, "weight_decay": 5e-4, "batch_size": 256, "use_lr_scheduler": False}
                new_config = clamp_config(raw_config)
                reasoning = f"Fallback after API parse failure: {exc}. Try larger learning rate and batch size for short-budget CIFAR training."
                metadata = {"api_backend": True, "fallback": True, "api": response.metadata, "error": str(exc), "raw_text": text[:1000]}
                confidence = 0.4
            decision = {
                "new_config": new_config,
                "raw_new_config": raw_config,
                "reasoning": reasoning,
                "confidence": confidence,
                "metadata": metadata,
            }
            (OUT_DIR / "qwen_decision_0.json").write_text(json.dumps(decision, indent=2))
            return decision
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
        raw_config = parse_config(text)
        new_config = clamp_config(raw_config)
        reasoning = text
        metadata = {"direct_prompt": True, "model_path": str(AGENT_MODEL)}
        confidence = 0.7
    except Exception as exc:
        raw_config = {"model_type": "E", "embedding_dim": 512, "lr": 0.2, "weight_decay": 5e-4, "batch_size": 256, "use_lr_scheduler": False}
        new_config = clamp_config(raw_config)
        reasoning = f"Fallback after parse failure: {exc}. Try larger learning rate and batch size for short-budget CIFAR training."
        metadata = {"fallback": True, "error": str(exc), "raw_text": text[:1000]}
        confidence = 0.4
    del model
    torch.cuda.empty_cache()
    decision = {
        "new_config": new_config,
        "raw_new_config": raw_config,
        "reasoning": reasoning,
        "confidence": confidence,
        "metadata": metadata,
    }
    (OUT_DIR / "qwen_decision_0.json").write_text(json.dumps(decision, indent=2))
    return decision


def normalized_score(value: float, baseline: float) -> float:
    denom = PAPER_ANCHOR - baseline
    return 0.0 if denom <= 0 else (value - baseline) / denom


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    history = [run_eval("baseline", 0, BASE_CONFIG)]
    baseline = float(history[0]["metrics"]["test_accuracy_percent"])
    decision = decide_with_qwen(history, baseline)
    history.append(run_eval("final", 1, decision["new_config"]))
    final = history[-1]
    final_acc = float(final["metrics"]["test_accuracy_percent"])
    score = normalized_score(final_acc, baseline)
    result = {
        "task_id": "hyperboliccv_cifar100_accuracy",
        "repo": "HyperbolicCV",
        "success": True,
        "dataset": "CIFAR-100",
        "metric": "test_accuracy_percent",
        "direction": "higher_is_better",
        "paper_anchor": PAPER_ANCHOR,
        "paper_anchor_source": "HyperbolicCV README Table 1 CIFAR-100 accuracy.",
        "budget": FIXED | {"baseline_config": BASE_CONFIG, "search_space": SEARCH_SPACE},
        "baseline_metrics": history[0]["metrics"],
        "final_metrics": final["metrics"],
        "final_config": final["config"],
        "decisions": [decision],
        "decisions_made": 1,
        "history": history,
        "normalized_score": score,
        "score": {
            "direction": "higher_is_better",
            "official_budget_baseline": baseline,
            "paper_anchor": PAPER_ANCHOR,
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
