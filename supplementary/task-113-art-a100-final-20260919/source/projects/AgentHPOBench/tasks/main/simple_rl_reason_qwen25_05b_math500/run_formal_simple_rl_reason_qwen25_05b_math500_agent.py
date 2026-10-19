#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import time
from pathlib import Path
from typing import Any

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _budget_agent_common import (  # noqa: E402
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


TASK_ID = "simple_rl_reason_qwen25_05b_math500"
RESULT_DIRNAME = TASK_ID
REPO_DIR = ROOT / "repositories/simpleRL-reason"
DATA_ROOT = ROOT / "data/formal/simple_rl_reason_qwen25_05b_math500/simplelr_qwen_level3to5"
MODEL_ROOT = Path(os.environ.get("SIMPLE_RL_QWEN25_05B_MODEL", str(ROOT / "models/Qwen2___5-0___5B")))

BASE_CONFIG = {
    "actor_lr": 5e-7,
    "kl_loss_coef": 1e-4,
    "entropy_coeff": 0.001,
    "rollout_n": 1,
}
SEARCH_SPACE = {
    "actor_lr": [2e-7, 5e-7, 1e-6, 2e-6],
    "kl_loss_coef": [5e-5, 1e-4, 2e-4, 5e-4],
    "entropy_coeff": [0.0, 0.0005, 0.001, 0.002],
    "rollout_n": [1],
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "simple_rl_reason_qwen25_05b_math500", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)

ALIASES = {
    "learning_rate": "actor_lr",
    "lr": "actor_lr",
    "kl_coef": "kl_loss_coef",
    "entropy_coeffient": "entropy_coeff",
    "n": "rollout_n",
}


FORMAL_DEFAULT_ENV = {
    "AUTOREP_VERL_TRAIN_CONDA_ENV": "autorep-open-r1",
    "VERL_DISABLE_VLLM": "1",
    "VERL_ATTN_IMPLEMENTATION": "eager",
    "SIMPLE_RL_ROLLOUT_BACKEND": "hf",
    "SIMPLE_RL_ROLLOUT_N": "1",
    "SIMPLE_RL_TRAIN_BATCH_SIZE": "2",
    "SIMPLE_RL_VAL_BATCH_SIZE": "8",
    "SIMPLE_RL_PPO_MINI_BATCH_SIZE": "2",
    "SIMPLE_RL_PPO_MICRO_BATCH_SIZE": "1",
    "SIMPLE_RL_MICRO_ROLLOUT_BATCH_SIZE": "2",
    "SIMPLE_RL_LOGPROB_MICRO_BATCH_SIZE": "1",
    "SIMPLE_RL_REF_LOGPROB_MICRO_BATCH_SIZE": "1",
    "SIMPLE_RL_CRITIC_MICRO_BATCH_SIZE": "1",
    "SIMPLE_RL_MAX_RESPONSE_LENGTH": "128",
    "SIMPLE_RL_ROLLOUT_TOP_K": "0",
    "TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD": "1",
    "AUTOREP_KEEP_AGENT_LOADED": "0",
    "PYTORCH_CUDA_ALLOC_CONF": "expandable_segments:True",
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

def apply_formal_defaults() -> None:
    for key, value in FORMAL_DEFAULT_ENV.items():
        os.environ.setdefault(key, value)


def parse_targets() -> list[int]:
    text = os.environ.get("SIMPLE_RL_CHUNK_TARGETS", "2,4,6,8,10")
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def parse_verl_log(log_path: Path) -> dict[str, Any]:
    text = log_path.read_text(errors="replace") if log_path.exists() else ""
    metrics: dict[str, Any] = {}
    step_matches = list(re.finditer(r"step:(\d+)\s+-\s+(.*)", text))
    if step_matches:
        last = step_matches[-1]
        metrics["step"] = int(last.group(1))
        body = last.group(2)
        patterns = [
            (r"val-core/[^\\s'\"]*math[^\\s'\"]*/acc/mean@1", "val_accuracy"),
            (r"val-core/[^\\s'\"]*MATH[^\\s'\"]*/acc/mean@1", "val_accuracy"),
            (r"val-aux/[^\\s'\"]*math[^\\s'\"]*/reward/mean@1", "val_reward"),
            (r"val/test_correctness/[^\s:'\"]*", "val_accuracy"),
            (r"val/test_score/[^\s:'\"]*", "val_reward"),
            (r"critic/score/mean", "train_score"),
            (r"critic/rewards/mean", "train_reward"),
            (r"actor/kl_loss", "kl_loss"),
            (r"actor/entropy_loss", "entropy_loss"),
            (r"actor/lr", "actor_lr_observed"),
        ]
        for key_regex, out_key in patterns:
            match = re.search(key_regex + r":\\s*[\\\'\\\"]?(?:np\\.float64\\()?([0-9][0-9.eE+-]*)\\)?", body)
            if match:
                value = next((group for group in reversed(match.groups()) if group is not None), None)
                if value is not None:
                    metrics[out_key] = float(value)
    final_match = re.search(r"val-core/[^'\"]*?[Mm][Aa][Tt][Hh][^'\"]*?/acc/mean@1['\"]?:\s*['\"]?(?:np\.float64\()?([0-9][0-9.eE+-]*)", text)
    if final_match:
        metrics["val_accuracy"] = float(final_match.group(1))
    simple_rl_match = re.search(r"val/test_correctness/[^\s:'\"]+['\"]?:?\s*['\"]?(?:np\.float64\()?([0-9][0-9.eE+-]*)\)?", text)
    if simple_rl_match:
        metrics["val_accuracy"] = float(simple_rl_match.group(1))
    if "val_accuracy" in metrics:
        metrics["math500_accuracy_percent"] = metrics["val_accuracy"] * 100.0
        metrics["score"] = metrics["math500_accuracy_percent"]
    return metrics


def run_chunk(out_dir: Path, resume_path: Path | None, target: int, config: dict[str, Any], env: dict[str, str], log_path: Path) -> dict[str, Any]:
    train_file = DATA_ROOT / "train.parquet"
    val_file = DATA_ROOT / "test.parquet"
    if not REPO_DIR.exists():
        raise FileNotFoundError(REPO_DIR)
    if not MODEL_ROOT.exists():
        raise FileNotFoundError(MODEL_ROOT)
    if not train_file.exists() or not val_file.exists():
        raise FileNotFoundError(DATA_ROOT)
    rollout_backend = os.environ.get("SIMPLE_RL_ROLLOUT_BACKEND", "vllm")
    rollout_n = int(os.environ.get("SIMPLE_RL_ROLLOUT_N", str(config["rollout_n"])))

    overrides = [
        "python3 -m verl.trainer.main_ppo",
        "algorithm.adv_estimator=grpo",
        "+trainer.val_before_train=False",
        f"data.train_files={train_file}",
        f"data.val_files={val_file}",
        f"data.train_batch_size={os.environ.get('SIMPLE_RL_TRAIN_BATCH_SIZE', '16')}",
        f"data.val_batch_size={os.environ.get('SIMPLE_RL_VAL_BATCH_SIZE', '128')}",
        f"data.max_prompt_length={os.environ.get('SIMPLE_RL_MAX_PROMPT_LENGTH', '1024')}",
        f"data.max_response_length={os.environ.get('SIMPLE_RL_MAX_RESPONSE_LENGTH', '1024')}",
        f"actor_rollout_ref.model.path={MODEL_ROOT}",
        f"actor_rollout_ref.actor.optim.lr={config['actor_lr']}",
        "actor_rollout_ref.model.use_remove_padding=True",
        f"actor_rollout_ref.actor.ppo_mini_batch_size={os.environ.get('SIMPLE_RL_PPO_MINI_BATCH_SIZE', '16')}",
        f"actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu={os.environ.get('SIMPLE_RL_PPO_MICRO_BATCH_SIZE', '4')}",
        "actor_rollout_ref.actor.use_kl_loss=True",
        f"actor_rollout_ref.actor.kl_loss_coef={config['kl_loss_coef']}",
        "actor_rollout_ref.actor.kl_loss_type=low_var_kl",
        f"actor_rollout_ref.actor.entropy_coeff={config['entropy_coeff']}",
        "actor_rollout_ref.model.enable_gradient_checkpointing=True",
        "actor_rollout_ref.actor.fsdp_config.param_offload=False",
        "actor_rollout_ref.actor.fsdp_config.grad_offload=False",
        "actor_rollout_ref.actor.fsdp_config.optimizer_offload=False",
        f"actor_rollout_ref.rollout.temperature={os.environ.get('SIMPLE_RL_ROLLOUT_TEMPERATURE', '1.0')}",
        f"actor_rollout_ref.rollout.top_p={os.environ.get('SIMPLE_RL_ROLLOUT_TOP_P', '0.95')}",
        f"actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu={os.environ.get('SIMPLE_RL_LOGPROB_MICRO_BATCH_SIZE', '4')}",
        f"actor_rollout_ref.rollout.tensor_model_parallel_size={os.environ.get('SIMPLE_RL_TENSOR_PARALLEL_SIZE', '1')}",
        f"actor_rollout_ref.rollout.name={rollout_backend}",
        f"actor_rollout_ref.rollout.gpu_memory_utilization={os.environ.get('SIMPLE_RL_GPU_MEMORY_UTILIZATION', '0.45')}",
        f"actor_rollout_ref.rollout.n={rollout_n}",
        f"actor_rollout_ref.rollout.top_k={os.environ.get('SIMPLE_RL_ROLLOUT_TOP_K', '0' if rollout_backend == 'hf' else '-1')}",
        "actor_rollout_ref.rollout.load_format=safetensors",
        f"actor_rollout_ref.rollout.micro_rollout_batch_size={os.environ.get('SIMPLE_RL_MICRO_ROLLOUT_BATCH_SIZE', '16')}",
        f"actor_rollout_ref.rollout.max_num_batched_tokens={os.environ.get('SIMPLE_RL_MAX_NUM_BATCHED_TOKENS', '2048')}",
        f"actor_rollout_ref.rollout.max_num_seqs={os.environ.get('SIMPLE_RL_MAX_NUM_SEQS', '64')}",
        f"actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu={os.environ.get('SIMPLE_RL_REF_LOGPROB_MICRO_BATCH_SIZE', '4')}",
        "actor_rollout_ref.ref.fsdp_config.param_offload=True",
        f"algorithm.kl_ctrl.kl_coef={config['kl_loss_coef']}",
        f"critic.ppo_micro_batch_size_per_gpu={os.environ.get('SIMPLE_RL_CRITIC_MICRO_BATCH_SIZE', '2')}",
        "trainer.critic_warmup=0",
        "'trainer.logger=[\"console\"]'",
        "trainer.project_name=autorep_simple_rl_reason",
        f"trainer.experiment_name={TASK_ID}_{AGENT_LABEL}",
        f"trainer.n_gpus_per_node={os.environ.get('SIMPLE_RL_N_GPUS_PER_NODE', '1')}",
        "trainer.nnodes=1",
        f"trainer.save_freq={os.environ.get('SIMPLE_RL_SAVE_FREQ', '2')}",
        f"trainer.test_freq={os.environ.get('SIMPLE_RL_TEST_FREQ', '2')}",
        "trainer.total_epochs=1",
        f"trainer.total_training_steps={target}",
        f"trainer.default_local_dir={out_dir}",
        "trainer.remove_previous_ckpt=False",
    ]
    if resume_path and resume_path.exists():
        overrides.extend(["trainer.resume_mode=resume_path", f"trainer.resume_from_path={resume_path}"])
    extra = os.environ.get("SIMPLE_RL_EXTRA_OVERRIDES", "").strip()
    if extra:
        overrides.append(extra)
    script = " ".join(
        [
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh",
            f"&& conda activate {os.environ.get('AUTOREP_VERL_TRAIN_CONDA_ENV', 'autorep-verl')}",
            "&& ray stop --force >/dev/null 2>&1 || true",
            "&&",
            " ".join(overrides),
            "; rc=$?; ray stop --force >/dev/null 2>&1 || true; exit $rc",
        ]
    )
    seconds = run_shell(script, cwd=REPO_DIR, env=env, log_path=log_path)
    return {
        "target_step": target,
        "resume_path": str(resume_path) if resume_path else None,
        "config": dict(config),
        "metrics": parse_verl_log(log_path),
        "seconds": seconds,
    }


def training_log(history: list[dict[str, Any]], manifest: dict[str, Any]) -> str:
    lines = [
        "Task: SimpleRL-reason GRPO on Qwen2.5-0.5B using SimpleRL-Zoo level3to5 data.",
        "Metric: MATH-500 accuracy percent, higher is better.",
        "Official base model anchor: Qwen-2.5-0.5B MATH 500 = 15.8.",
        "Official SimpleRL-Zoo anchor: Qwen-2.5-0.5B + SimpleRL-Zoo MATH 500 = 34.4.",
        f"Current standard-budget chunks: {parse_targets()}.",
    ]
    if manifest:
        lines.append(f"Manifest: {manifest}")
    for item in history:
        lines.append(f"step={item['target_step']} config={item['config']} metrics={item['metrics']}")
    return "\n".join(lines)


def main() -> int:
    apply_formal_defaults()
    manifest = load_manifest_record(TASK_ID)
    targets = parse_targets()
    run_id = os.environ.get("RUN_ID") or f"{TASK_ID}_{AGENT_LABEL.lower().replace('-', '_')}_{targets[0]}to{targets[-1]}_{utc_now().replace(':', '').replace('+', '_')}"
    result_dir = result_root(RESULT_DIRNAME)
    out_dir = result_dir / "runs" / run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    result_file = result_dir / f"{TASK_ID}_{RESULT_FILE_AGENT_NAME}_results.json"
    maybe_dry_run({"task_id": TASK_ID, "run_id": run_id, "targets": targets, "result_file": str(result_file)})

    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = os.environ.get("SIMPLE_RL_CUDA_VISIBLE_DEVICES", "0")
    env["PYTHONPATH"] = f"{REPO_DIR}:{ROOT}:{ROOT / '.python_deps'}:{env.get('PYTHONPATH', '')}"
    env["WANDB_MODE"] = "offline"
    env["TOKENIZERS_PARALLELISM"] = "false"
    env["VLLM_USE_V1"] = os.environ.get("VLLM_USE_V1", "1")
    env["HF_HUB_OFFLINE"] = os.environ.get("HF_HUB_OFFLINE", "1")
    env["TRANSFORMERS_OFFLINE"] = os.environ.get("TRANSFORMERS_OFFLINE", "1")
    env["HF_DATASETS_OFFLINE"] = os.environ.get("HF_DATASETS_OFFLINE", "1")

    config = dict(BASE_CONFIG)
    resume_path: Path | None = None
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
    if "math500_accuracy_percent" not in final_metrics:
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
        "metric": "math500_accuracy_percent",
        "agent_budget_result": final_metrics["math500_accuracy_percent"],
        "agent_final_config": dict(final["config"]),
        "agent_decisions_made": len(decisions),
        "agent_internal_baseline": 15.8,
        "official_budget_baseline": manifest.get("official_budget_baseline", 15.8),
        "paper_anchor": manifest.get("paper_anchor", 34.4),
        "chunk_targets": targets,
        "chunk_summaries": history,
        "decision_history": decisions,
        "final_config": dict(final["config"]),
        "final_metrics": final_metrics,
        "effective_tuning_budget_steps": targets[-1],
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
