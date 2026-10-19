#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import time
from pathlib import Path
from typing import Any

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _budget_agent_common import (
    AGENT_LABEL,
    MODEL_PATH,
    RESULT_FILE_AGENT_NAME,
    ROOT,
    decide_config,
    dump_json,
    load_manifest_record,
    maybe_dry_run,
    result_root,
    run_shell,
    utc_now,
)


TASK_ID = "verl_grpo_gsm8k"
RESULT_DIRNAME = "verl_grpo_gsm8k"
REPO_DIR = ROOT / "repositories/verl"
DATA_ROOT = ROOT / "data/paper_exact/verl_grpo_gsm8k/gsm8k"
MODEL_ROOT = ROOT / "models/Qwen/Qwen2.5-3B-Instruct"
INITIAL_CHECKPOINT = ROOT / "results/formal_baselines/verl_grpo_gsm8k/verl_rebuild_640_deepseek_20260521T033613Z/global_step_640"
BASE_CONFIG = {"actor_lr": 3e-6, "kl_loss_coef": 0.001}
SEARCH_SPACE = {
    "actor_lr": [1e-6, 2e-6, 3e-6, 5e-6],
    "kl_loss_coef": [0.0005, 0.001, 0.0015, 0.002, 0.003],
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "verl_grpo_gsm8k", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)

ALIASES = {"learning_rate": "actor_lr", "lr": "actor_lr", "kl_coef": "kl_loss_coef"}



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

def parse_targets() -> list[int]:
    text = os.environ.get("VERL_CHUNK_TARGETS", "660,680,700")
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def parse_verl_log(log_path: Path) -> dict[str, Any]:
    text = log_path.read_text(errors="replace")
    step_matches = list(re.finditer(r"step:(\d+)\s+-\s+(.*)", text))
    metrics: dict[str, Any] = {}
    if step_matches:
        last = step_matches[-1]
        metrics["step"] = int(last.group(1))
        body = last.group(2)
        for key, out_key in [
            ("val-core/openai/gsm8k/acc/mean@1", "val_accuracy"),
            ("val-aux/openai/gsm8k/reward/mean@1", "val_reward"),
            ("critic/score/mean", "train_score"),
            ("critic/rewards/mean", "train_reward"),
            ("actor/kl_loss", "kl_loss"),
            ("actor/grad_norm", "grad_norm"),
            ("actor/lr", "actor_lr_observed"),
        ]:
            match = re.search(re.escape(key) + r":(?:np\.float64\()?([0-9.eE+-]+)\)?", body)
            if match:
                value = next((group for group in match.groups() if group is not None), None)
                if value is not None:
                    metrics[out_key] = float(value)
    val_matches = list(
        re.finditer(
            r"val-core/openai/gsm8k/acc/mean@1['\"]?:\s*(?:np\.float64\()?([0-9.eE+-]+)\)?",
            text,
        )
    )
    if val_matches:
        metrics["val_accuracy"] = float(val_matches[-1].group(1))
    if "val_accuracy" in metrics:
        metrics["accuracy"] = metrics["val_accuracy"]
        metrics["accuracy_percent"] = metrics["val_accuracy"] * 100.0
        metrics["score"] = metrics["val_accuracy"]
    return metrics


def visible_gpu_count(env: dict[str, str]) -> int:
    text = env.get("CUDA_VISIBLE_DEVICES") or os.environ.get("VERL_CUDA_VISIBLE_DEVICES") or os.environ.get("CUDA_VISIBLE_DEVICES") or ""
    ids = [x.strip() for x in text.split(",") if x.strip() and x.strip() != "-1"]
    return max(1, len(ids))


def run_chunk(out_dir: Path, resume_path: Path, target: int, config: dict[str, Any], env: dict[str, str], log_path: Path) -> dict[str, Any]:
    train_file = DATA_ROOT / "train.parquet"
    val_file = DATA_ROOT / "test.parquet"
    if not train_file.exists() or not val_file.exists():
        raise FileNotFoundError(DATA_ROOT)
    if not resume_path.exists():
        raise FileNotFoundError(resume_path)
    gpu_count = int(os.environ.get("VERL_N_GPUS_PER_NODE", str(visible_gpu_count(env))))
    tp_size = int(os.environ.get("VERL_TENSOR_MODEL_PARALLEL_SIZE", str(min(gpu_count, 2))))
    script = " ".join(
        [
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh",
            f"&& conda activate {os.environ.get('AUTOREP_VERL_TRAIN_CONDA_ENV', 'autorep-open-r1')}",
            "&& ray stop --force >/dev/null 2>&1 || true",
            "&& bash examples/grpo_trainer/run_qwen2_5-3b_gsm8k_grpo_lora.sh",
            f"data.train_files={train_file}",
            f"data.val_files={val_file}",
            "data.max_response_length=512",
            f"actor_rollout_ref.model.path={MODEL_ROOT}",
            f"trainer.n_gpus_per_node={gpu_count}",
            f"actor_rollout_ref.rollout.tensor_model_parallel_size={tp_size}",
            "'trainer.logger=[\"console\"]'",
            "trainer.use_legacy_worker_impl=enable",
            "actor_rollout_ref.rollout.free_cache_engine=False",
            "+actor_rollout_ref.rollout.enable_sleep_mode=False",
            "actor_rollout_ref.rollout.enforce_eager=True",
            "actor_rollout_ref.rollout.logprobs_mode=null",
            "actor_rollout_ref.model.use_remove_padding=False",
            "+actor_rollout_ref.model.override_config.attn_implementation=sdpa",
            "actor_rollout_ref.rollout.gpu_memory_utilization=0.50",
            "actor_rollout_ref.rollout.max_model_len=1024",
            "actor_rollout_ref.rollout.max_num_seqs=192",
            "actor_rollout_ref.rollout.max_num_batched_tokens=8192",
            "actor_rollout_ref.rollout.n=2",
            "actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=8",
            "actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=8",
            "actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=8",
            f"actor_rollout_ref.actor.optim.lr={config['actor_lr']}",
            f"actor_rollout_ref.actor.kl_loss_coef={config['kl_loss_coef']}",
            "trainer.test_freq=20",
            "trainer.save_freq=20",
            f"trainer.total_epochs={os.environ.get('VERL_TOTAL_EPOCHS', '8')}",
            f"trainer.total_training_steps={target}",
            "trainer.resume_mode=resume_path",
            f"trainer.resume_from_path={resume_path}",
            f"trainer.default_local_dir={out_dir}",
            "; rc=$?; ray stop --force >/dev/null 2>&1 || true; exit $rc",
        ]
    )
    seconds = run_shell(script, cwd=REPO_DIR, env=env, log_path=log_path)
    metrics = parse_verl_log(log_path)
    return {
        "target_step": target,
        "resume_path": str(resume_path),
        "config": dict(config),
        "metrics": metrics,
        "seconds": seconds,
    }


def training_log(history: list[dict[str, Any]], manifest: dict[str, Any]) -> str:
    lines = [
        "Task: verl GRPO LoRA on GSM8K with Qwen2.5-3B-Instruct.",
        "Metric: gsm8k_accuracy_percent, higher is better.",
        f"Official shortened budget baseline: {manifest.get('official_budget_baseline', 84.68536770280515)} percent at global_step=700.",
        f"Paper anchor: {manifest.get('paper_anchor', 86.1)} percent.",
        f"Current chunks: {parse_targets()}, resuming from global_step=640.",
    ]
    for item in history:
        lines.append(
            f"step={item['target_step']} config={item['config']} "
            f"metrics={item['metrics']}"
        )
    return "\n".join(lines)


def main() -> int:
    if not REPO_DIR.exists():
        raise FileNotFoundError(REPO_DIR)
    manifest = load_manifest_record(TASK_ID)
    targets = parse_targets()
    run_id = os.environ.get("RUN_ID") or f"{TASK_ID}_{AGENT_LABEL.lower().replace('-', '_')}_{targets[0]}to{targets[-1]}_{utc_now().replace(':', '').replace('+', '_')}"
    result_dir = result_root(RESULT_DIRNAME)
    out_dir = result_dir / "runs" / run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    result_file = result_dir / f"{TASK_ID}_{RESULT_FILE_AGENT_NAME}_results.json"
    maybe_dry_run({"task_id": TASK_ID, "run_id": run_id, "targets": targets, "result_file": str(result_file)})

    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = os.environ.get("VERL_CUDA_VISIBLE_DEVICES", "0,1")
    env["PYTHONPATH"] = f"{REPO_DIR}:{ROOT}:{ROOT / '.python_deps'}:{env.get('PYTHONPATH', '')}"
    env["WANDB_MODE"] = "offline"
    env["TOKENIZERS_PARALLELISM"] = "false"
    env["VLLM_USE_V1"] = os.environ.get("VLLM_USE_V1", "1")
    env["VERL_VLLM_LORA_PATH"] = os.environ.get("VERL_VLLM_LORA_PATH", str(MODEL_ROOT))
    env["HF_HUB_OFFLINE"] = os.environ.get("HF_HUB_OFFLINE", "1")
    env["TRANSFORMERS_OFFLINE"] = os.environ.get("TRANSFORMERS_OFFLINE", "1")
    env["HF_DATASETS_OFFLINE"] = os.environ.get("HF_DATASETS_OFFLINE", "1")

    config = dict(BASE_CONFIG)
    resume_path = Path(os.environ.get("VERL_INITIAL_CHECKPOINT", str(INITIAL_CHECKPOINT)))
    actual_initial_checkpoint = resume_path
    history: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []
    started = time.time()
    for index, target in enumerate(targets):
        summary = run_chunk(out_dir, resume_path, target, config, env, out_dir / f"chunk_{target}.log")
        history.append(summary)
        next_checkpoint = out_dir / f"global_step_{target}"
        if next_checkpoint.exists():
            resume_path = next_checkpoint
        if index == len(targets) - 1:
            break
        decision = decide_config(
            task_name=TASK_ID,
            current_config=config,
            search_space=SEARCH_SPACE,
            aliases=ALIASES,
            training_log=training_log(history, manifest),
            metrics_history=[(item["target_step"], item["metrics"]) for item in history],
            budget_remaining=len(targets) - index - 1,
            total_budget=len(targets),
            decision_number=index,
        )
        decisions.append({"after_step": target, "old_config": config, **decision})
        config = dict(decision["new_config"])

    final = history[-1]
    final_metrics = final["metrics"]
    if "accuracy_percent" not in final_metrics:
        raise RuntimeError(f"missing final validation accuracy: {final_metrics}")
    payload = {
        "experiment_name": f"{TASK_ID}_{RESULT_FILE_AGENT_NAME}",
        "benchmark_name": TASK_ID,
        "agent_name": AGENT_LABEL,
        "agent_model": str(MODEL_PATH),
        "created_at": utc_now(),
        "success": True,
        "agent_success": True,
        "direction": "higher_is_better",
        "metric": "gsm8k_accuracy_percent",
        "agent_budget_result": final_metrics["accuracy_percent"],
        "agent_final_config": dict(final["config"]),
        "agent_decisions_made": len(decisions),
        "agent_internal_baseline": None,
        "official_budget_baseline": manifest.get("official_budget_baseline", 84.68536770280515),
        "paper_anchor": manifest.get("paper_anchor", 86.1),
        "initial_checkpoint": str(actual_initial_checkpoint),
        "default_initial_checkpoint": str(INITIAL_CHECKPOINT),
        "chunk_targets": targets,
        "chunk_summaries": history,
        "decision_history": decisions,
        "final_config": dict(final["config"]),
        "final_metrics": final_metrics,
        "effective_tuning_budget_steps": targets[-1] - 640,
        "formal_budget_target_step": targets[-1],
        "total_time": round(time.time() - started, 3),
        "output_dir": str(out_dir),
        "run_dir": str(out_dir),
        "run_id": run_id,
    }
    dump_json(result_file, payload)
    print(result_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
