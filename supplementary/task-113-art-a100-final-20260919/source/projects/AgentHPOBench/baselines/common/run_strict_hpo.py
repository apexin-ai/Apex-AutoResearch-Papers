#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import inspect
import json
import math
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(os.environ.get("AUTOREP_ROOT", "."))
TASK_ROOT = Path(os.environ.get("AUTOREP_SERIAL_TASK_ROOT", str(ROOT / "baselines/tpe")))
SLUG = os.environ.get("AUTOREP_SERIAL_SLUG", "hpo_strict5_seed0")
MODEL_PATH = (
    os.environ.get("AUTOREP_SERIAL_MODEL_PATH")
    or os.environ.get("AUTOREP_MODEL_PATH")
    or str(ROOT / "models/Qwen/Qwen3-8B")
)
AGENT_BACKEND = (os.environ.get("AUTOREP_SERIAL_BACKEND") or os.environ.get("AUTOREP_AGENT_BACKEND") or "hf").strip()
AGENT_LABEL = os.environ.get("AUTOREP_SERIAL_AGENT_LABEL") or os.environ.get("AUTOREP_AGENT_LABEL") or "Qwen3-8B"
MODEL_LABEL = os.environ.get("AUTOREP_SERIAL_MODEL_LABEL") or os.environ.get("AUTOREP_MODEL_LABEL") or AGENT_LABEL
RESULT_AGENT_NAME = os.environ.get("RESULT_FILE_AGENT_NAME", "QwenLocal")
RESULTS_BASE = Path(os.environ.get("AUTOREP_SERIAL_RESULTS_BASE", str(ROOT / "results/hpo" / SLUG)))
LOG_BASE = Path(os.environ.get("AUTOREP_SERIAL_LOG_BASE", str(ROOT / "logs/hpo" / SLUG)))
TARGET_INTERVENTIONS = int(os.environ.get("AUTOREP_SERIAL_INTERVENTIONS", "5"))
GPU = os.environ.get("PILOT_CUDA_VISIBLE_DEVICES", os.environ.get("CUDA_VISIBLE_DEVICES", "0")).split(",")[0]
WORKER_NAME = os.environ.get("PILOT_WORKER_NAME", "main")
TASK_TIMEOUT = int(os.environ.get("TASK_TIMEOUT", "21600"))


CONDA_ROOT = Path(os.environ.get("CONDA_ROOT", "/opt/miniconda3"))
CONDA_SITE_PACKAGES = Path(
    os.environ.get(
        "AUTOREP_CONDA_SITE_PACKAGES",
        str(CONDA_ROOT / "envs/autorep-vlm2vec/lib/python3.10/site-packages"),
    )
)


for _path in reversed((str(ROOT), str(CONDA_SITE_PACKAGES))):
    if _path not in sys.path:
        sys.path.insert(0, _path)


TASKS: list[tuple[int, str]] = [
    (1, "llm_c_fineweb10b"),
    (2, "torch_conv_kan_cifar10"),
    (3, "open_r1_math500"),
    (4, "agent_lightning_room_selector"),
    (5, "uni2ts_lsf_etth1"),
    (6, "timesfm_etth1_long_horizon"),
    (7, "modernbert_mnli_accuracy"),
    (8, "cifar10_airbench94"),
    (9, "noisygl_cora_uniform30_gcn"),
    (10, "tabmini_molecular_biology_promoters_auc"),
    (11, "binary_diffusion_adult_rf"),
    (12, "xlstm_parity"),
    (13, "vbll_yacht_rmse"),
    (14, "tabm_california_rmse"),
    (15, "timexer_pjm_168_24_mse"),
    (16, "ablkit_hwf_reasoning_accuracy"),
    (17, "tunedgnn_cora_gcn_accuracy"),
    (18, "verl_grpo_gsm8k"),
    (19, "forest_diffusion_iris_f1fake"),
    (20, "var_imagenet256"),
    (21, "align_anything_ragen_bandit"),
    (22, "chronos_t5_tiny_monash_weather_wql"),
    (23, "hyperboliccv_cifar100_accuracy"),
    (24, "itransformer_ettm2_96_mse"),
    (25, "timemixer_ettm2_96_mse"),
    (26, "art_2048_win_rate"),
    (27, "open_r1_multimodal_mathvista_accuracy"),
    (28, "rankup_utkface_mae"),
    (29, "sparsetsf_ettm1_96_mse"),
    (30, "simple_rl_reason_qwen25_05b_math500"),
]


STRICT_REUSE_FROM_QWEN3_8B = {
    "modernbert_mnli_accuracy",
    "ablkit_hwf_reasoning_accuracy",
    "tunedgnn_cora_gcn_accuracy",
    "var_imagenet256",
    "chronos_t5_tiny_monash_weather_wql",
    "open_r1_multimodal_mathvista_accuracy",
    "rankup_utkface_mae",
}


NATIVE_SCRIPT_TASKS = {
    "llm_c_fineweb10b",
    "align_anything_ragen_bandit",
    "art_2048_win_rate",
    "simple_rl_reason_qwen25_05b_math500",
}


GENERIC_MODULE_TASKS = {
    "open_r1_math500",
    "uni2ts_lsf_etth1",
    "timesfm_etth1_long_horizon",
    "cifar10_airbench94",
    "noisygl_cora_uniform30_gcn",
    "tabmini_molecular_biology_promoters_auc",
    "binary_diffusion_adult_rf",
    "xlstm_parity",
    "vbll_yacht_rmse",
    "tabm_california_rmse",
    "timexer_pjm_168_24_mse",
    "hyperboliccv_cifar100_accuracy",
    "itransformer_ettm2_96_mse",
    "timemixer_ettm2_96_mse",
    "sparsetsf_ettm1_96_mse",
    "forest_diffusion_iris_f1fake",
}


SPECIAL_TASKS = {
    "torch_conv_kan_cifar10",
    "agent_lightning_room_selector",
    "vlm2vec_mmeb_v2",
    "moge_eval_all",
}


LOWER_IS_BETTER = {
    "llm_c_fineweb10b",
    "uni2ts_lsf_etth1",
    "timesfm_etth1_long_horizon",
    "vbll_yacht_rmse",
    "tabm_california_rmse",
    "timexer_pjm_168_24_mse",
    "moge_eval_all",
    "var_imagenet256",
    "chronos_t5_tiny_monash_weather_wql",
    "itransformer_ettm2_96_mse",
    "timemixer_ettm2_96_mse",
    "rankup_utkface_mae",
    "sparsetsf_ettm1_96_mse",
}


METRIC_KEYS = {
    "llm_c_fineweb10b": ["val_loss"],
    "agent_lightning_room_selector": ["accuracy"],
    "align_anything_ragen_bandit": ["success_rate"],
    "art_2048_win_rate": ["win_rate"],
    "verl_grpo_gsm8k": ["accuracy_percent", "gsm8k_accuracy_percent", "accuracy"],
    "simple_rl_reason_qwen25_05b_math500": ["math500_accuracy_percent", "accuracy_percent", "accuracy"],
    "open_r1_math500": ["accuracy_percent", "math500_accuracy_percent"],
    "uni2ts_lsf_etth1": ["MSE[0.5]", "mse", "MSE"],
    "timesfm_etth1_long_horizon": ["wape", "smape", "mse"],
    "cifar10_airbench94": ["accuracy_percent", "test_accuracy", "accuracy"],
    "noisygl_cora_uniform30_gcn": ["accuracy_percent", "test_accuracy", "accuracy"],
    "tabmini_molecular_biology_promoters_auc": ["auc", "test_auc"],
    "binary_diffusion_adult_rf": ["test_accuracy_percent", "rf_accuracy_percent", "accuracy_percent", "accuracy"],
    "xlstm_parity": ["scaled_accuracy", "accuracy", "test_accuracy"],
    "vbll_yacht_rmse": ["test_rmse", "rmse"],
    "tabm_california_rmse": ["test_rmse", "rmse"],
    "timexer_pjm_168_24_mse": ["test_mse", "mse"],
    "var_imagenet256": ["subset_diag_fid", "subset_fid", "fid"],
    "chronos_t5_tiny_monash_weather_wql": ["WQL", "wql", "mean_wql"],
    "hyperboliccv_cifar100_accuracy": ["test_accuracy_percent", "accuracy_percent", "test_accuracy", "accuracy"],
    "itransformer_ettm2_96_mse": ["test_mse", "mse"],
    "timemixer_ettm2_96_mse": ["test_mse", "mse"],
    "sparsetsf_ettm1_96_mse": ["test_mse_at_best_val", "test_mse", "mse"],
    "forest_diffusion_iris_f1fake": ["f1_fake", "F1_fake", "score"],
    "torch_conv_kan_cifar10": ["accuracy_percent", "accuracy"],
    "vlm2vec_mmeb_v2": ["image_task_mean_primary_score", "mean_primary_score"],
    "moge_eval_all": ["ddad_depth_scale_invariant_rel_percent"],
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def dump_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def event(kind: str, **payload: Any) -> None:
    LOG_BASE.mkdir(parents=True, exist_ok=True)
    record = {"time": utc_now(), "worker": WORKER_NAME, "kind": kind, **payload}
    with (LOG_BASE / "strict_serial_status.jsonl").open("a") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")
    print(json.dumps(record, sort_keys=True), flush=True)


def selected_tasks() -> list[tuple[int, str]]:
    raw = os.environ.get("PILOT_TASKS", "").strip()
    tasks = TASKS
    if raw:
        wanted = {x.strip() for x in raw.split(",") if x.strip()}
        tasks = [(idx, task) for idx, task in TASKS if str(idx) in wanted or f"{idx:02d}" in wanted or task in wanted]
    if os.environ.get("PILOT_REVERSE", "0").lower() in {"1", "true", "yes", "on"}:
        tasks = list(reversed(tasks))
    return tasks


def base_env() -> dict[str, str]:
    env = os.environ.copy()
    env.update(
        {
            "AUTOREP_ROOT": str(ROOT),
            "AUTOREP_MODEL_SLUG": SLUG,
            "AUTOREP_MODEL_LABEL": MODEL_LABEL,
            "AUTOREP_AGENT_LABEL": AGENT_LABEL,
            "AUTOREP_AGENT_BACKEND": AGENT_BACKEND,
            "AUTOREP_MODEL_PATH": MODEL_PATH,
            "QWEN3_MODEL": MODEL_PATH,
            "RESULT_FILE_AGENT_NAME": RESULT_AGENT_NAME,
            "AUTOREP_AGENT_RESULTS_BASE": str(RESULTS_BASE),
            "AUTOREP_AGENT_LOG_BASE": str(LOG_BASE),
            "AUTOREP_USE_CHAT_TEMPLATE": "1",
            "AUTOREP_QWEN_NO_THINK": os.environ.get("AUTOREP_QWEN_NO_THINK", "0"),
            "AUTOREP_AGENT_MAX_NEW_TOKENS": os.environ.get("AUTOREP_AGENT_MAX_NEW_TOKENS", "384"),
            "AUTOREP_AGENT_TEMPERATURE": os.environ.get("AUTOREP_AGENT_TEMPERATURE", "0.1"),
            "AUTOREP_AGENT_TORCH_DTYPE": os.environ.get("AUTOREP_AGENT_TORCH_DTYPE", "bfloat16"),
            "AUTOREP_KEEP_AGENT_LOADED": os.environ.get("AUTOREP_KEEP_AGENT_LOADED", "0"),
            "AUTOREP_INTERVENTIONS": str(TARGET_INTERVENTIONS),
            "CUDA_VISIBLE_DEVICES": GPU,
            "QWEN_CUDA_VISIBLE_DEVICES": GPU,
            "OPENR1_CUDA_VISIBLE_DEVICES": GPU,
            "AUTOREP_BENCHMARK_DEVICE": "cuda:0",
            "HF_HUB_OFFLINE": os.environ.get("HF_HUB_OFFLINE", "1"),
            "TRANSFORMERS_OFFLINE": os.environ.get("TRANSFORMERS_OFFLINE", "1"),
            "HF_DATASETS_OFFLINE": os.environ.get("HF_DATASETS_OFFLINE", "1"),
            "TOKENIZERS_PARALLELISM": "false",
            "PYTHONPATH": f"{ROOT}:{ROOT / '.python_deps'}:{env.get('PYTHONPATH', '')}",
            "CHRONOS_CUDA_VISIBLE_DEVICES": GPU,
            "HYPERCV_CUDA_VISIBLE_DEVICES": GPU,
            "ITRANSFORMER_CUDA_VISIBLE_DEVICES": GPU,
            "TIMEMIXER_CUDA_VISIBLE_DEVICES": GPU,
            "SPARSETSF_CUDA_VISIBLE_DEVICES": GPU,
            "MATHVISTA_CUDA_VISIBLE_DEVICES": GPU,
            "RANKUP_CUDA_VISIBLE_DEVICES": GPU,
            "TABM_CUDA_VISIBLE_DEVICES": GPU,
            "TIMEXER_CUDA_VISIBLE_DEVICES": GPU,
            "TIMESFM_CUDA_VISIBLE_DEVICES": GPU,
            "UNI2TS_CUDA_VISIBLE_DEVICES": GPU,
            "VLM2VEC_CUDA_VISIBLE_DEVICES": GPU,
            "VAR_CUDA_VISIBLE_DEVICES": GPU,
            "MOGE_CUDA_VISIBLE_DEVICES": GPU,
            "TORCH_CONV_KAN_CUDA_VISIBLE_DEVICES": GPU,
            "SIMPLE_RL_CUDA_VISIBLE_DEVICES": GPU,
            "VERL_CUDA_VISIBLE_DEVICES": GPU,
        }
    )
    env.update(
        {
            "AUTOREP_VERL_TRAIN_CONDA_ENV": os.environ.get("AUTOREP_VERL_TRAIN_CONDA_ENV", "autorep-open-r1"),
            "VERL_DISABLE_VLLM": os.environ.get("VERL_DISABLE_VLLM", "1"),
            "VERL_ATTN_IMPLEMENTATION": os.environ.get("VERL_ATTN_IMPLEMENTATION", "eager"),
            "SIMPLE_RL_ROLLOUT_BACKEND": os.environ.get("SIMPLE_RL_ROLLOUT_BACKEND", "hf"),
            "SIMPLE_RL_ROLLOUT_N": os.environ.get("SIMPLE_RL_ROLLOUT_N", "1"),
            "SIMPLE_RL_TRAIN_BATCH_SIZE": os.environ.get("SIMPLE_RL_TRAIN_BATCH_SIZE", "2"),
            "SIMPLE_RL_VAL_BATCH_SIZE": os.environ.get("SIMPLE_RL_VAL_BATCH_SIZE", "8"),
            "SIMPLE_RL_PPO_MINI_BATCH_SIZE": os.environ.get("SIMPLE_RL_PPO_MINI_BATCH_SIZE", "2"),
            "SIMPLE_RL_PPO_MICRO_BATCH_SIZE": os.environ.get("SIMPLE_RL_PPO_MICRO_BATCH_SIZE", "1"),
            "SIMPLE_RL_MICRO_ROLLOUT_BATCH_SIZE": os.environ.get("SIMPLE_RL_MICRO_ROLLOUT_BATCH_SIZE", "2"),
            "SIMPLE_RL_LOGPROB_MICRO_BATCH_SIZE": os.environ.get("SIMPLE_RL_LOGPROB_MICRO_BATCH_SIZE", "1"),
            "SIMPLE_RL_REF_LOGPROB_MICRO_BATCH_SIZE": os.environ.get("SIMPLE_RL_REF_LOGPROB_MICRO_BATCH_SIZE", "1"),
            "SIMPLE_RL_CRITIC_MICRO_BATCH_SIZE": os.environ.get("SIMPLE_RL_CRITIC_MICRO_BATCH_SIZE", "1"),
            "SIMPLE_RL_MAX_RESPONSE_LENGTH": os.environ.get("SIMPLE_RL_MAX_RESPONSE_LENGTH", "128"),
        }
    )
    if AGENT_BACKEND.lower() in {"api", "openai", "openai-compatible", "anthropic", "glm", "claude_code", "claude-code", "codex", "codex_cli", "codex-cli"}:
        env["AUTOREP_API_PATCH_TRANSFORMERS"] = os.environ.get("AUTOREP_API_PATCH_TRANSFORMERS", "1")
        env["AUTOREP_API_TIMEOUT"] = os.environ.get("AUTOREP_API_TIMEOUT", "300")
        env["AUTOREP_API_RETRIES"] = os.environ.get("AUTOREP_API_RETRIES", "10")
    return env


def result_file(task: str) -> Path:
    return RESULTS_BASE / task / f"{task}_{RESULT_AGENT_NAME}_results.json"


def discover_script(task: str) -> Path:
    scripts = sorted((TASK_ROOT / task).glob("run_formal*.sh"))
    if not scripts:
        raise FileNotFoundError(task)
    agent = [p for p in scripts if p.name.endswith("_agent.sh")]
    return agent[0] if agent else scripts[0]


def run_shell_task(task: str, extra_env: dict[str, str] | None = None) -> dict[str, Any]:
    env = base_env()
    env.update(extra_env or {})
    env["RUN_ID"] = f"{SLUG}_{task}_{WORKER_NAME}_{utc_now().replace(':', '').replace('+', '_')}"
    script = discover_script(task)
    log_path = LOG_BASE / "tasks" / f"{task}.{WORKER_NAME}.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    event("native_start", task=task, script=str(script), gpu=GPU)
    started = time.time()
    with log_path.open("wb") as log:
        proc = subprocess.run(["bash", str(script)], cwd=str(ROOT), env=env, stdout=log, stderr=subprocess.STDOUT, timeout=TASK_TIMEOUT)
    seconds = round(time.time() - started, 3)
    if proc.returncode != 0:
        raise RuntimeError(f"{task} native script failed rc={proc.returncode}, log={log_path}")
    path = result_file(task)
    fallback_path = RESULTS_BASE / task / f"{task}_QwenLocal_results.json"
    if not path.exists() and RESULT_AGENT_NAME != "QwenLocal" and fallback_path.exists():
        fallback_payload = load_json(fallback_path)
        has_metric_payload = any(
            key in fallback_payload
            for key in ("score", "best_metric", "final_metric", "agent_budget_result", "final_agent_budget_result")
        )
        if fallback_payload.get("success") is False and fallback_payload.get("agent_success") is False:
            raise RuntimeError(f"{task} fallback result reports failure: {fallback_path}")
        if not has_metric_payload or fallback_payload.get("error"):
            raise RuntimeError(f"{task} fallback result is not scoring-ready: {fallback_path}")
        path = fallback_path
    payload = load_json(path)
    payload["strict_serial_protocol"] = True
    payload["strict_serial_note"] = "Native runner executed with five serial interventions."
    payload["strict_serial_seconds"] = seconds
    payload["strict_serial_worker"] = WORKER_NAME
    dump_json(path, payload)
    expected_path = result_file(task)
    if path != expected_path and not expected_path.exists():
        dump_json(expected_path, payload)
        path = expected_path
    return {"ok": True, "task": task, "mode": "native", "seconds": seconds, "result": str(path)}


def module_path(task: str) -> Path:
    files = sorted((TASK_ROOT / task).glob("run_formal*.py"))
    if not files:
        raise FileNotFoundError(task)
    return files[0]


def import_task_module(task: str) -> Any:
    os.environ.update(base_env())
    os.environ["RUN_ID"] = f"{SLUG}_{task}_{WORKER_NAME}_{utc_now().replace(':', '').replace('+', '_')}"
    path = module_path(task)
    name = f"serial_{task}_{int(time.time() * 1000)}"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def as_number(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)) and math.isfinite(float(value)):
        return float(value)
    if isinstance(value, str):
        try:
            out = float(value.strip().rstrip("%"))
        except ValueError:
            return None
        return out if math.isfinite(out) else None
    return None


def metric_value(task: str, obj: Any) -> tuple[float | None, str | None]:
    if isinstance(obj, dict):
        for key in METRIC_KEYS.get(task, []):
            val = as_number(obj.get(key))
            if val is not None:
                return val, key
        for key in ("metrics", "final_metrics", "baseline_metrics", "score", "final", "agent_metrics"):
            val, metric = metric_value(task, obj.get(key))
            if val is not None:
                return val, metric
        for key, value in obj.items():
            if isinstance(key, str) and any(token in key.lower() for token in ["accuracy", "auc", "mse", "rmse", "mae", "wape", "score", "rel"]):
                val = as_number(value)
                if val is not None:
                    return val, key
    return None, None


def direction(task: str) -> str:
    return "lower_is_better" if task in LOWER_IS_BETTER else "higher_is_better"


def normalized(task: str, value: float, baseline: float, paper: float | None) -> float | None:
    if paper is None or abs(paper - baseline) < 1e-12:
        return None
    if direction(task) == "lower_is_better":
        return (baseline - value) / (baseline - paper)
    return (value - baseline) / (paper - baseline)


def best_trial(task: str, history: list[dict[str, Any]]) -> dict[str, Any]:
    candidates = history[1:] if len(history) > 1 else history
    reverse = direction(task) == "higher_is_better"
    return sorted(candidates, key=lambda item: metric_value(task, item)[0] if metric_value(task, item)[0] is not None else (-1e99 if reverse else 1e99), reverse=reverse)[0]


def prompt_history_item(task: str, item: dict[str, Any]) -> dict[str, Any]:
    value, metric = metric_value(task, item)
    return {
        "trial": item.get("trial"),
        "kind": item.get("kind"),
        "config": item.get("config"),
        "metric": metric,
        "value": value,
    }


def agent_metric_history_item(task: str, item: dict[str, Any]) -> tuple[Any, dict[str, Any], Any, Any]:
    value, metric = metric_value(task, item)
    return (
        item.get("trial"),
        {"metric": metric, "value": value},
        item.get("config"),
        item.get("kind"),
    )


def call_run_eval(module: Any, task: str, kind: str, trial: int, config: dict[str, Any]) -> dict[str, Any]:
    sig = inspect.signature(module.run_eval)
    params = list(sig.parameters)
    if params == ["kind", "trial_idx", "config", "limit"]:
        limit = getattr(module, "FINAL_LIMIT", getattr(module, "PROXY_LIMIT", 0))
        return module.run_eval(kind, trial, config, limit)
    if params == ["kind", "trial_idx", "config", "max_windows"]:
        return module.run_eval(kind, trial, config, 0)
    return module.run_eval(kind, trial, config)


def call_decide(module: Any, task: str, history: list[dict[str, Any]], current: dict[str, Any], baseline: float, step: int) -> dict[str, Any]:
    if AGENT_BACKEND.lower() in {"random", "random_search", "tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
        backend_spec = importlib.util.spec_from_file_location("strict_hpo_backend_generic", TASK_ROOT / "tpe_backend.py")
        if backend_spec is None or backend_spec.loader is None:
            raise RuntimeError(f"cannot import HPO backend from {TASK_ROOT}")
        hpo_backend = importlib.util.module_from_spec(backend_spec)
        backend_spec.loader.exec_module(hpo_backend)
        return hpo_backend.tpe_decision_from_call(
            task,
            {
                "history": history,
                "current": current,
                "baseline": baseline,
                "decision_number": step - 1,
                "search_space": getattr(module, "SEARCH_SPACE", {}),
            },
            vars(module),
        )
    fn = module.decide_with_qwen
    params = list(inspect.signature(fn).parameters)
    if params == ["history", "config", "budget_remaining", "decision_number"]:
        try:
            return fn(history, current, TARGET_INTERVENTIONS - step + 1, step - 1)
        except Exception:
            if hasattr(module, "fallback_decision"):
                return module.fallback_decision(history, current, step - 1)
            raise
    if params == ["history", "current", "baseline"]:
        return fn(history, current, baseline)
    if params == ["history", "current", "baseline", "decision_number", "total_interventions"]:
        return fn(history, current, baseline, step - 1, TARGET_INTERVENTIONS)
    if params == ["history", "current", "budget_baseline"]:
        return fn(history, current, baseline)
    if params == ["history", "current"]:
        return fn(history, current)
    if params == ["history", "baseline"]:
        return fn(history, baseline)
    raise RuntimeError(f"unsupported decide signature for {task}: {params}")


def clamp(module: Any, config: dict[str, Any]) -> dict[str, Any]:
    if hasattr(module, "clamp_config"):
        return module.clamp_config(config)
    return dict(config)


def run_generic_module(task: str) -> dict[str, Any]:
    module = import_task_module(task)
    started = time.time()
    history: list[dict[str, Any]] = []
    current = dict(module.BASE_CONFIG)
    baseline = call_run_eval(module, task, "baseline", 0, current)
    baseline["kind"] = baseline.get("kind", "baseline")
    history.append(baseline)
    baseline_value, metric_name = metric_value(task, baseline)
    if baseline_value is None:
        raise RuntimeError(f"{task}: cannot find baseline metric")
    decisions: list[dict[str, Any]] = []
    for step in range(1, TARGET_INTERVENTIONS + 1):
        decision = call_decide(module, task, history, current, baseline_value, step)
        new_config = clamp(module, decision.get("new_config", current))
        decisions.append(
            {
                "decision_number": step - 1,
                "old_config": dict(current),
                "new_config": dict(new_config),
                "raw_new_config": decision.get("raw_new_config"),
                "reasoning": decision.get("reasoning"),
                "confidence": decision.get("confidence"),
                "metadata": decision.get("metadata", {}),
            }
        )
        current = dict(new_config)
        trial = call_run_eval(module, task, f"intervention_{step}", step, current)
        trial["kind"] = f"intervention_{step}"
        if isinstance(trial.get("config"), dict):
            current = dict(trial["config"])
        history.append(trial)
    best = best_trial(task, history)
    best_value, best_metric = metric_value(task, best)
    paper = None
    for name in ("PAPER_ANCHOR", "PAPER_ANCHOR_ACC", "PAPER_ANCHOR_AUC", "PAPER_ANCHOR_RMSE", "PAPER_ANCHOR_MSE", "PAPER_ANCHOR_WAPE"):
        if hasattr(module, name):
            paper = float(getattr(module, name))
            break
    score = normalized(task, float(best_value), baseline_value, paper) if best_value is not None else None
    path = result_file(task)
    payload = {
        "experiment_name": f"{task}_{RESULT_AGENT_NAME}",
        "benchmark_name": task,
        "task_id": task,
        "agent": AGENT_LABEL,
        "agent_name": AGENT_LABEL,
        "model_path": MODEL_PATH,
        "created_at": utc_now(),
        "strict_serial_protocol": True,
        "strict_serial_note": "Baseline followed by five serial interventions; every decision sees the prior history.",
        "success": True,
        "agent_success": True,
        "direction": direction(task),
        "metric": best_metric or metric_name,
        "official_budget_baseline": baseline_value,
        "paper_anchor": paper,
        "agent_budget_result": best_value,
        "agent_final_config": best.get("config"),
        "final_config": best.get("config"),
        "final_metrics": best.get("metrics"),
        "best_trial": best.get("trial"),
        "best_kind": best.get("kind"),
        "normalized_score": score,
        "score": {
            "direction": direction(task),
            "official_budget_baseline": baseline_value,
            "paper_anchor": paper,
            "normalized_score": score,
            "scoring_eligible": paper is not None,
        },
        "baseline_metrics": baseline.get("metrics"),
        "history": history,
        "decisions": decisions,
        "decisions_made": len(decisions),
        "agent_decisions_made": len(decisions),
        "search_space": getattr(module, "SEARCH_SPACE", {}),
        "total_time": round(time.time() - started, 3),
        "result_file": str(path),
    }
    dump_json(path, payload)
    return {"ok": True, "task": task, "mode": "generic_module", "seconds": payload["total_time"], "result": str(path)}


def run_torch_conv(task: str) -> dict[str, Any]:
    module = import_task_module(task)
    started = time.time()
    manifest = module.load_manifest_record(module.TASK_ID)
    epochs = int(os.environ.get("TORCH_CONV_KAN_EPOCHS", "10"))
    result_dir = RESULTS_BASE / task
    run_dir = result_dir / "runs" / f"{SLUG}_{task}_{WORKER_NAME}_{utc_now().replace(':', '').replace('+', '_')}"
    run_dir.mkdir(parents=True, exist_ok=True)
    module.ensure_data_link()

    def eval_config(kind: str, trial: int, config: dict[str, Any]) -> dict[str, Any]:
        output_dir = run_dir / f"trial_{trial}_{kind}" / "outputs"
        logging_dir = run_dir / f"trial_{trial}_{kind}" / "train_logs"
        wandb_dir = run_dir / f"trial_{trial}_{kind}" / "wandb"
        env = base_env()
        env["WANDB_MODE"] = "offline"
        env["WANDB_DIR"] = str(wandb_dir)
        # .python_deps contains timm 0.6.x and shadows the conda timm with timm.layers.
        env["PYTHONPATH"] = ":".join(
            part for part in env.get("PYTHONPATH", "").split(":")
            if part and part != str(ROOT / ".python_deps")
        )
        output_dir.mkdir(parents=True, exist_ok=True)
        logging_dir.mkdir(parents=True, exist_ok=True)
        wandb_dir.mkdir(parents=True, exist_ok=True)
        cmd = " ".join(
            [
                "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh",
                "&& conda activate autorep-vlm2vec",
                "&& accelerate launch cifar.py",
                f"output_dir={output_dir}",
                f"logging_dir={logging_dir}",
                f"epochs={epochs}",
                f"train_batch_size={config['batch_size']}",
                "val_batch_size=256",
                f"dataloader_num_workers={os.environ.get('TORCH_CONV_KAN_NUM_WORKERS', '8')}",
                f"optim.learning_rate={config['learning_rate']}",
                f"optim.adam_weight_decay={config['weight_decay']}",
                f"loss.label_smoothing={config['label_smoothing']}",
                "+save_checkpoints=false",
            ]
        )
        seconds = module.run_shell(cmd, cwd=module.REPO_DIR, env=env, log_path=run_dir / f"trial_{trial}_{kind}.log")
        wandb_payload = module.parse_wandb_run(module.newest_wandb_file(wandb_dir))
        metrics = dict(wandb_payload["metrics"])
        metrics["accuracy_percent"] = float(metrics["accuracy"]) * 100.0
        metrics["seconds"] = seconds
        return {"trial": trial, "kind": kind, "config": dict(config), "metrics": metrics, "wandb": wandb_payload, "output_dir": str(output_dir)}

    history = [eval_config("baseline", 0, module.BASE_CONFIG)]
    baseline_value = float(history[0]["metrics"]["accuracy_percent"])
    current = dict(module.BASE_CONFIG)
    decisions: list[dict[str, Any]] = []
    for step in range(1, TARGET_INTERVENTIONS + 1):
        decision = module.decide_config(
            task_name=module.TASK_ID,
            current_config=current,
            search_space=module.SEARCH_SPACE,
            aliases=module.ALIASES,
            training_log=module.training_log(manifest) + "\nPrior history:\n" + json.dumps(history, indent=2),
            metrics_history=[(item["trial"], item["metrics"]["accuracy_percent"], item["config"], item["kind"]) for item in history],
            budget_remaining=TARGET_INTERVENTIONS - step + 1,
            total_budget=TARGET_INTERVENTIONS,
            decision_number=step - 1,
        )
        current = module.clamp_config(decision["new_config"], current, module.SEARCH_SPACE, aliases=module.ALIASES) if hasattr(module, "clamp_config") else decision["new_config"]
        decisions.append({"decision_number": step - 1, "new_config": current, **{k: decision.get(k) for k in ("reasoning", "confidence", "metadata", "raw_new_config")}})
        history.append(eval_config(f"intervention_{step}", step, current))
    best = best_trial(task, history)
    best_value, metric = metric_value(task, best)
    paper = float(manifest.get("paper_anchor", 84.17))
    payload = {
        "experiment_name": f"{task}_{RESULT_AGENT_NAME}",
        "benchmark_name": task,
        "agent_name": AGENT_LABEL,
        "agent_model": MODEL_PATH,
        "created_at": utc_now(),
        "strict_serial_protocol": True,
        "success": True,
        "agent_success": True,
        "direction": "higher_is_better",
        "metric": metric or "accuracy_percent",
        "agent_budget_result": best_value,
        "agent_final_config": best.get("config"),
        "official_budget_baseline": baseline_value,
        "paper_anchor": paper,
        "history": history,
        "decisions": decisions,
        "decisions_made": len(decisions),
        "agent_decisions_made": len(decisions),
        "score": {"direction": "higher_is_better", "official_budget_baseline": baseline_value, "paper_anchor": paper, "normalized_score": normalized(task, float(best_value), baseline_value, paper)},
        "total_epochs": epochs,
        "total_time": round(time.time() - started, 3),
        "run_dir": str(run_dir),
    }
    dump_json(result_file(task), payload)
    return {"ok": True, "task": task, "mode": "torch_conv_special", "seconds": payload["total_time"], "result": str(result_file(task))}


def run_cached_common(task: str) -> dict[str, Any]:
    module = import_task_module(task)
    started = time.time()
    metrics = module.summarize_scores() if task == "vlm2vec_mmeb_v2" else module.summarize_moge()
    manifest = module.load_manifest_record(module.TASK_ID)
    current = dict(module.BASE_CONFIG)
    history = [{"trial": 0, "kind": "baseline", "config": dict(current), "metrics": metrics}]
    baseline, metric = metric_value(task, metrics)
    if baseline is None:
        raise RuntimeError(f"{task}: cannot extract cached metric")
    decisions = []
    for step in range(1, TARGET_INTERVENTIONS + 1):
        decision = module.decide_config(
            task_name=module.TASK_ID,
            current_config=current,
            search_space=module.SEARCH_SPACE,
            aliases=getattr(module, "ALIASES", {}),
            training_log=module.training_log(metrics, manifest)
            + "\nPrior serial history:\n"
            + json.dumps([prompt_history_item(task, item) for item in history], indent=2),
            metrics_history=[agent_metric_history_item(task, item) for item in history],
            budget_remaining=TARGET_INTERVENTIONS - step + 1,
            total_budget=TARGET_INTERVENTIONS,
            decision_number=step - 1,
        )
        current = decision["new_config"]
        decisions.append({"decision_number": step - 1, "new_config": current, **{k: decision.get(k) for k in ("reasoning", "confidence", "metadata", "raw_new_config")}})
        history.append({"trial": step, "kind": f"intervention_{step}", "config": dict(current), "metrics": metrics})
    paper = float(manifest.get("paper_anchor", 0.0)) if manifest.get("paper_anchor") is not None else None
    best = best_trial(task, history)
    value, metric = metric_value(task, best)
    payload = {
        "experiment_name": f"{task}_{RESULT_AGENT_NAME}",
        "benchmark_name": task,
        "agent_name": AGENT_LABEL,
        "agent_model": MODEL_PATH,
        "created_at": utc_now(),
        "strict_serial_protocol": True,
        "strict_serial_note": "Cached-eval task: decisions are serial, metric artifact is fixed by the available official cache.",
        "success": True,
        "agent_success": True,
        "direction": direction(task),
        "metric": metric,
        "official_budget_baseline": baseline,
        "paper_anchor": paper,
        "agent_budget_result": value,
        "agent_final_config": best.get("config"),
        "history": history,
        "decisions": decisions,
        "decisions_made": len(decisions),
        "agent_decisions_made": len(decisions),
        "evaluation_mode": "cached_official_eval_summary",
        "total_time": round(time.time() - started, 3),
    }
    dump_json(result_file(task), payload)
    if hasattr(module, "copy_result_alias"):
        module.copy_result_alias(result_file(task), getattr(module, "ALIAS_DIRNAME", None))
    return {"ok": True, "task": task, "mode": "cached_common", "seconds": payload["total_time"], "result": str(result_file(task))}


def preseed_reuse(task: str) -> dict[str, Any]:
    src = ROOT / "results/main/qwen3_8b_seed0_final30" / task / f"{task}_QwenLocal_results.json"
    dst = result_file(task)
    if not src.exists():
        raise FileNotFoundError(src)
    payload = load_json(src)
    payload["strict_serial_protocol"] = True
    payload["strict_serial_note"] = "Reused existing qwen3_8b result because it already contains baseline plus five serial interventions."
    payload["strict_serial_reused_from"] = str(src)
    payload["strict_serial_reused_at"] = utc_now()
    dump_json(dst, payload)
    return {"ok": True, "task": task, "mode": "reused_native_strict", "seconds": 0.0, "result": str(dst)}


def allow_qwen3_8b_reuse() -> bool:
    raw = os.environ.get("AUTOREP_SERIAL_REUSE_QWEN3_8B", "auto").strip().lower()
    if raw in {"1", "true", "yes", "on"}:
        return True
    if raw in {"0", "false", "no", "off"}:
        return False
    return AGENT_BACKEND.lower() == "hf" and "qwen3_8b" in SLUG.lower()


def run_one(task: str) -> dict[str, Any]:
    if result_file(task).exists() and os.environ.get("PILOT_FORCE", "0") != "1":
        return {"ok": True, "task": task, "mode": "skip_existing", "seconds": 0.0, "result": str(result_file(task))}
    if task in STRICT_REUSE_FROM_QWEN3_8B and allow_qwen3_8b_reuse():
        return preseed_reuse(task)
    if task in STRICT_REUSE_FROM_QWEN3_8B:
        return run_shell_task(task, {"AUTOREP_INTERVENTIONS": str(TARGET_INTERVENTIONS)})
    if task == "llm_c_fineweb10b":
        return run_shell_task(task, {"LLMC_CHUNK_TARGETS": os.environ.get("LLMC_CHUNK_TARGETS", "167,334,501,668,835,1000")})
    if task == "simple_rl_reason_qwen25_05b_math500":
        return run_shell_task(task, {"SIMPLE_RL_CHUNK_TARGETS": os.environ.get("SIMPLE_RL_CHUNK_TARGETS", "1,2,4,6,8,10")})
    if task == "verl_grpo_gsm8k":
        return run_shell_task(task, {"VERL_CHUNK_TARGETS": os.environ.get("VERL_CHUNK_TARGETS", "660,680,700,720,740,760")})
    if task in {"align_anything_ragen_bandit", "art_2048_win_rate"}:
        return run_shell_task(task, {"AUTOREP_INTERVENTIONS": str(TARGET_INTERVENTIONS)})
    if task == "torch_conv_kan_cifar10":
        return run_torch_conv(task)
    if task in {"vlm2vec_mmeb_v2", "moge_eval_all"}:
        return run_cached_common(task)
    if task == "agent_lightning_room_selector":
        return run_agent_lightning(task)
    if task in GENERIC_MODULE_TASKS:
        return run_generic_module(task)
    raise RuntimeError(f"no strict serial adapter for {task}")


def run_agent_lightning(task: str) -> dict[str, Any]:
    # The original task optimizes prompt candidates rather than scalar hyperparameters.
    # A strict serial variant evaluates one newly proposed template per intervention,
    # with prior train/validation results included in the next prompt context.
    deps_path = str(ROOT / ".python_deps")
    while deps_path in sys.path:
        sys.path.remove(deps_path)
    sys.path.insert(0, deps_path)
    try:
        import transformers.utils.import_utils as _tf_import_utils

        _tf_import_utils.is_flash_attn_2_available = lambda: False
        _tf_import_utils.is_flash_attn_greater_or_equal = lambda *args, **kwargs: False
        _tf_import_utils.is_flash_attn_greater_or_equal_2_10 = lambda: False
    except Exception:
        pass
    module = import_task_module(task)
    import torch
    from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer
    try:
        _parallel_styles = {"colwise", "rowwise", "colwise_rep", "rowwise_rep", "local_colwise", "local_rowwise", "gather", "sequence_parallel"}
        import transformers.modeling_utils as _modeling_utils
        import transformers.integrations.tensor_parallel as _tensor_parallel

        _modeling_utils.ALL_PARALLEL_STYLES = _parallel_styles
        _tensor_parallel.ALL_PARALLEL_STYLES = _parallel_styles
    except Exception:
        pass

    started = time.time()
    all_tasks = module.load_tasks()
    split = len(all_tasks) // 2
    train_limit = int(os.environ.get("AGENT_LIGHTNING_TRAIN_LIMIT", "36"))
    val_limit = int(os.environ.get("AGENT_LIGHTNING_VAL_LIMIT", "80"))
    train_pool = all_tasks[:split]
    val_pool = all_tasks[split:]
    train_tasks = train_pool if train_limit <= 0 else train_pool[:train_limit]
    val_tasks = val_pool if val_limit <= 0 else val_pool[:val_limit]
    if not train_tasks or not val_tasks:
        raise RuntimeError(f"Agent-Lightning room-selector split is empty: train={len(train_tasks)} val={len(val_tasks)}")
    batch_size = int(os.environ.get("AGENT_LIGHTNING_BATCH_SIZE", "8"))

    try:
        from agenthpobench.agents.api_decision_client import api_backend_enabled as _api_backend_enabled, call_decision_api as _call_decision_api
        api_backend = _api_backend_enabled()
    except Exception:
        if AGENT_BACKEND.lower() in {"api", "openai", "openai-compatible", "anthropic", "glm", "claude_code", "claude-code", "codex", "codex_cli", "codex-cli"}:
            raise
        api_backend = False
        _call_decision_api = None

    def _messages_to_prompt(messages: list[dict[str, str]]) -> str:
        parts = []
        for message in messages:
            role = str(message.get("role", "user")).upper()
            parts.append(f"{role}:\n{message.get('content', '')}")
        return "\n\n".join(parts)

    def _api_generate_texts(messages_list: list[list[dict[str, str]]], *, max_new_tokens: int, batch_size: int) -> list[str]:
        assert _call_decision_api is not None
        outputs = []
        for messages in messages_list:
            response = _call_decision_api(
                _messages_to_prompt(messages),
                temperature=0.0,
                max_tokens=int(os.environ.get("AUTOREP_API_MAX_TOKENS", str(max_new_tokens))),
            )
            outputs.append(response.text)
        return outputs

    def _generate_texts(messages_list: list[list[dict[str, str]]], *, max_new_tokens: int, batch_size: int) -> list[str]:
        if api_backend:
            return _api_generate_texts(messages_list, max_new_tokens=max_new_tokens, batch_size=batch_size)
        return module.generate_texts(model, tokenizer, messages_list, max_new_tokens=max_new_tokens, batch_size=batch_size)

    def _evaluate_candidate(candidate: Any, tasks: list[dict[str, Any]], *, batch_size: int) -> dict[str, Any]:
        if not api_backend:
            return module.evaluate_candidate(model, tokenizer, candidate, tasks, batch_size=batch_size)
        messages = [module.build_eval_messages(item, candidate.template) for item in tasks]
        generations = _api_generate_texts(messages, max_new_tokens=96, batch_size=batch_size)
        records = []
        correct = 0
        for item, generation in zip(tasks, generations):
            prediction = module.extract_choice(generation)
            expected = item["expected_choice"]
            is_correct = module.normalize_choice(prediction) == module.normalize_choice(expected)
            correct += int(is_correct)
            records.append({"id": item["id"], "expected": expected, "prediction": prediction, "correct": is_correct, "generation": generation})
        return {"name": candidate.name, "source": candidate.source, "template": candidate.template, "accuracy": correct / len(tasks), "correct": correct, "total": len(tasks), "records": records}

    def _template_from_response(text: str) -> str | None:
        snippets = [text.strip()]
        for pattern in (r"\{[\s\S]*\}", r"\[[\s\S]*\]"):
            match = re.search(pattern, text)
            if match:
                snippets.append(match.group(0))
        for snippet in snippets:
            try:
                parsed = json.loads(snippet)
            except Exception:
                continue
            candidates = parsed if isinstance(parsed, list) else [parsed]
            for item in candidates:
                value = item.get("template") if isinstance(item, dict) else item
                if isinstance(value, str) and "{date}" in value and "{attendees}" in value:
                    return value
        return None

    model = None
    tokenizer = None
    if not api_backend:
        os.environ["CUDA_VISIBLE_DEVICES"] = GPU
        tokenizer = AutoTokenizer.from_pretrained(str(module.MODEL_PATH), trust_remote_code=True, local_files_only=True)
        if tokenizer.pad_token_id is None and tokenizer.eos_token is not None:
            tokenizer.pad_token = tokenizer.eos_token
            tokenizer.pad_token_id = tokenizer.eos_token_id
        model_config = AutoConfig.from_pretrained(str(module.MODEL_PATH), trust_remote_code=True, local_files_only=True)
        model_config._attn_implementation = os.environ.get("AUTOREP_ATTN_IMPLEMENTATION", "eager")
        model = AutoModelForCausalLM.from_pretrained(
            str(module.MODEL_PATH),
            config=model_config,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            trust_remote_code=True,
            local_files_only=True,
            attn_implementation=os.environ.get("AUTOREP_ATTN_IMPLEMENTATION", "eager"),
        )
        if getattr(model, "generation_config", None) is not None and tokenizer.pad_token_id is not None:
            model.generation_config.pad_token_id = tokenizer.pad_token_id
    candidates = [module.PromptCandidate("baseline", module.BASELINE_TEMPLATE, "repo_baseline")]
    template_pool = [module.BASELINE_TEMPLATE, *list(module.FALLBACK_TEMPLATES)]
    backend_spec = importlib.util.spec_from_file_location("strict_hpo_backend", TASK_ROOT / "tpe_backend.py")
    if backend_spec is None or backend_spec.loader is None:
        raise RuntimeError(f"cannot import HPO backend from {TASK_ROOT}")
    hpo_backend = importlib.util.module_from_spec(backend_spec)
    backend_spec.loader.exec_module(hpo_backend)
    history = []
    baseline_train = _evaluate_candidate(candidates[0], train_tasks, batch_size=batch_size)
    baseline_val = _evaluate_candidate(candidates[0], val_tasks, batch_size=batch_size)
    history.append({"trial": 0, "kind": "baseline", "config": {"template_index": 0, "template": candidates[0].template}, "train_metrics": baseline_train, "metrics": baseline_val})
    decisions = []
    current_index = 0
    for step in range(1, TARGET_INTERVENTIONS + 1):
        decision = hpo_backend.tpe_decision_from_call(
            task,
            {
                "history": history,
                "current": {"template_index": current_index},
                "decision_number": step - 1,
                "search_space": {"template_index": list(range(len(template_pool)))},
            },
            {},
        )
        proposal = decision.get("new_config") or {}
        current_index = int(proposal.get("template_index", current_index))
        current_index = max(0, min(current_index, len(template_pool) - 1))
        template = template_pool[current_index]
        text = json.dumps(
            {
                "backend": decision.get("metadata", {}).get("backend", "strict_hpo_discrete"),
                "template_index": current_index,
            },
            sort_keys=True,
        )
        cand = module.PromptCandidate(f"intervention_{step}", template, f"{SLUG}_serial")
        train = _evaluate_candidate(cand, train_tasks, batch_size=batch_size)
        val = _evaluate_candidate(cand, val_tasks, batch_size=batch_size)
        history.append({"trial": step, "kind": f"intervention_{step}", "config": {"template_index": current_index, "template": template}, "train_metrics": train, "metrics": val})
        decisions.append({"decision_number": step - 1, "new_config": {"template_index": current_index, "template": template}, "reasoning": text[:2000], "confidence": 0.0, "metadata": {"raw_text": text[:4000], "backend": decision.get("metadata", {}).get("backend", "strict_hpo_discrete")}})
    if model is not None:
        del model
    try:
        torch.cuda.empty_cache()
    except Exception:
        pass
    best = max(history[1:], key=lambda item: float(item["metrics"]["accuracy"]))
    value = float(best["metrics"]["accuracy"])
    baseline_value = float(baseline_val["accuracy"])
    payload = {
        "experiment_name": f"{task}_{RESULT_AGENT_NAME}",
        "benchmark_name": task,
        "agent_name": AGENT_LABEL,
        "model_path": str(module.MODEL_PATH),
        "strict_serial_protocol": True,
        "success": True,
        "direction": "higher_is_better",
        "metric": "validation_accuracy",
        "official_budget_baseline": baseline_value,
        "paper_anchor": module.PAPER_ANCHOR,
        "agent_budget_result": value,
        "agent_final_config": best["config"],
        "history": history,
        "decisions": decisions,
        "decisions_made": len(decisions),
        "agent_decisions_made": len(decisions),
        "normalized_score": module.normalized_score(value),
        "total_time": round(time.time() - started, 3),
        "created_at": utc_now(),
    }
    dump_json(result_file(task), payload)
    return {"ok": True, "task": task, "mode": "agent_lightning_special", "seconds": payload["total_time"], "result": str(result_file(task))}



def normalize_strict_result(task: str) -> dict[str, Any]:
    path = result_file(task)
    payload = load_json(path)
    if isinstance(payload.get("chunk_summaries"), list):
        history_field = "chunk_summaries"
    elif isinstance(payload.get("history"), list):
        history_field = "history"
    else:
        raise RuntimeError(f"{task}: no explicit strict trajectory in {path}")
    sequence = payload[history_field]
    if len(sequence) != TARGET_INTERVENTIONS + 1:
        raise RuntimeError(f"{task}: expected {TARGET_INTERVENTIONS + 1} observations, found {len(sequence)}")
    values = []
    for step, item in enumerate(sequence):
        value, metric = metric_value(task, item)
        if value is None:
            raise RuntimeError(f"{task}: missing metric at step {step}")
        values.append((float(value), metric))
    decisions = payload.get("decision_history") if isinstance(payload.get("decision_history"), list) else payload.get("decisions")
    decision_count = len(decisions) if isinstance(decisions, list) else int(payload.get("agent_decisions_made", payload.get("decisions_made", 0)))
    if decision_count != TARGET_INTERVENTIONS:
        if all(isinstance(item, dict) and isinstance(item.get("config"), dict) for item in sequence[1:]):
            if decisions:
                payload["legacy_decisions"] = decisions
            decisions = [
                {
                    "decision_number": step - 1,
                    "new_config": sequence[step]["config"],
                    "reasoning": "Recovered from the executed strict trajectory.",
                    "confidence": 0.0,
                    "metadata": {"source": "reconstructed_from_executed_history"},
                }
                for step in range(1, TARGET_INTERVENTIONS + 1)
            ]
            payload["decisions"] = decisions
            payload["decision_recovery_source"] = "reconstructed_from_executed_history"
            decision_count = len(decisions)
        else:
            raise RuntimeError(f"{task}: expected {TARGET_INTERVENTIONS} decisions, found {decision_count}")
    final_item = sequence[-1]
    final_value, final_metric = values[-1]
    best_step = best_index = max(range(len(values)), key=lambda idx: values[idx][0])
    if direction(task) == "lower_is_better":
        best_step = best_index = min(range(len(values)), key=lambda idx: values[idx][0])
    best_value, _ = values[best_step]
    payload["strict_serial_protocol"] = True
    payload["strict_observation_count"] = len(sequence)
    payload["strict_decision_count"] = decision_count
    payload["strict_history_field"] = history_field
    payload["strict_final_step"] = TARGET_INTERVENTIONS
    payload["strict_final_metric_value"] = final_value
    payload["strict_final_metric_key"] = final_metric
    payload["final_agent_budget_result"] = final_value
    payload["final_metrics"] = final_item.get("metrics") if isinstance(final_item, dict) else None
    payload["final_config"] = final_item.get("config") if isinstance(final_item, dict) else None
    payload["agent_final_config"] = payload["final_config"]
    payload["best_observed_step"] = best_step
    payload["best_observed_metric_value"] = best_value
    payload["best_observed_metrics"] = sequence[best_step].get("metrics") if isinstance(sequence[best_step], dict) else None
    payload["best_observed_config"] = sequence[best_step].get("config") if isinstance(sequence[best_step], dict) else None
    dump_json(path, payload)
    return {
        "history_field": history_field,
        "observations": len(sequence),
        "decisions": decision_count,
        "final_value": final_value,
        "best_step": best_step,
        "best_value": best_value,
    }

def main() -> int:
    RESULTS_BASE.mkdir(parents=True, exist_ok=True)
    LOG_BASE.mkdir(parents=True, exist_ok=True)
    (LOG_BASE / f"strict_serial_{WORKER_NAME}.pid").write_text(f"{os.getpid()}\n")
    tasks = selected_tasks()
    event("serial_start", slug=SLUG, gpu=GPU, tasks=[task for _, task in tasks])
    summary = []
    started = time.time()
    for idx, task in tasks:
        event("task_start", idx=idx, task=task)
        task_started = time.time()
        try:
            result = run_one(task)
            result["strict_audit"] = normalize_strict_result(task)
            result["elapsed_since_task_start"] = round(time.time() - task_started, 3)
        except Exception as exc:
            tb = traceback.format_exc()
            result = {"ok": False, "task": task, "idx": idx, "mode": "error", "error": repr(exc), "traceback": tb, "elapsed_since_task_start": round(time.time() - task_started, 3)}
            event("task_error", idx=idx, task=task, error=repr(exc), traceback=tb[-4000:])
        result["idx"] = idx
        summary.append(result)
        dump_json(LOG_BASE / f"strict_serial_summary_{WORKER_NAME}.json", {"updated_at": utc_now(), "worker": WORKER_NAME, "summary": summary})
        event("task_end", idx=idx, task=task, ok=result.get("ok"), mode=result.get("mode"), seconds=result.get("seconds"))
        if os.environ.get("AUTOREP_STOP_ON_TASK_ERROR", "0") == "1" and not result.get("ok"):
            total = round(time.time() - started, 3)
            dump_json(
                LOG_BASE / f"strict_serial_summary_{WORKER_NAME}.json",
                {
                    "updated_at": utc_now(),
                    "worker": WORKER_NAME,
                    "ok_tasks": sum(1 for item in summary if item.get("ok")),
                    "total_tasks": len(tasks),
                    "total_seconds": total,
                    "stopped_on_task_error": True,
                    "summary": summary,
                },
            )
            event("serial_abort", idx=idx, task=task, total_seconds=total)
            return 1
    total = round(time.time() - started, 3)
    dump_json(
        LOG_BASE / f"strict_serial_summary_{WORKER_NAME}.json",
        {
            "updated_at": utc_now(),
            "worker": WORKER_NAME,
            "ok_tasks": sum(1 for item in summary if item.get("ok")),
            "total_tasks": len(tasks),
            "total_seconds": total,
            "summary": summary,
        },
    )
    event("serial_end", ok_tasks=sum(1 for item in summary if item.get("ok")), total_tasks=len(tasks), total_seconds=total)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
