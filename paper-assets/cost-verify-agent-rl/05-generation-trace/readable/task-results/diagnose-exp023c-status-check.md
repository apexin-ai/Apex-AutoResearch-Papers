# diagnose exp023c status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp023c-status-check_20260515T042047_result.json`
- **Structured JSON:** [`f5a48b3ad385bb22f07a.json`](../../sessions/f5/f5a48b3ad385bb22f07a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集所有信息。

```json
{
  "status": "running",
  "current_step": 1,
  "total_steps": 30,
  "step_time_seconds": 240.14,
  "estimated_remaining": "1h56m (ETA ~06:15 UTC / 14:15 local)",
  "initial_validation_metrics": {
    "success_rate": 0.0625,
    "pass@1": 0.0625,
    "action_is_valid": 0.6875,
    "action_is_effective": 1.0,
    "num_actions": 28.6875,
    "response_length": 2818.25,
    "reward_mean@16": 0.625,
    "reward_best@16_mean": 6.28
  },
  "training_metrics": "not yet logged (step 1 just completed, no step-level metrics printed yet)",
  "config": {
    "kl_loss_coef": 0.5,
    "use_kl_loss": true,
    "kl_loss_type": "kl",
    "entropy_coeff": 0.001,
    "score (reward on success)": 10.0,
    "parallel_friendly": false,
    "max_workers": 1,
    "val_env_groups": 16,
    "val_n_groups": [16],
    "train_env_groups": 4,
    "train_group_size": 16,
    "lr": 5e-7,
    "clip_ratio": "0.2-0.28",
    "ppo_epochs": 1,
    "save_freq": 5,
    "test_freq": 20
  },
  "command": "cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp023_grpo_parallel model_path=/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4 trainer.experiment_name=exp023c-alfworld-grpo-serial trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp023c/ trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp023c/ es_manager.val.env_groups=16 \"es_manager.val.env_configs.n_groups=[16]\"",
  "env_vars": "TMPDIR=/root/autodl-tmp/tmp/ ALFWORLD_DATA=/root/autodl-tmp/alfworld RAY_memory_monitor_refresh_ms=0 RAY_SYSTEM_MEMORY=210000000000 HYDRA_FULL_ERROR=1",
  "log_path": "/root/autodl-tmp/checkpoints/exp023c/train.log",
  "checkpoint_path": "/root/autodl-tmp/checkpoints/exp023c/ (empty, first save at step 5)",
  "gpu_status": "GPU 0: 61127/97887 MiB (0% util), GPU 1: 61173/97887 MiB (0% util)",
  "model": "qwen3 (num_hidden_layers=28, num_attention_heads=16, num_key_value_heads=8)",
  "base_checkpoint": "/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4"
}
```

**要点**：
- 训练正常运行，step 1 刚完成（240s/step），正在做 step 2 的 rollout（GPU 0% 利用率 = CPU-bound ALFWorld 环境交互阶段）
- 初始 validation success rate 6.25%（16 episodes 中 1 个成功）
- 所有关键配置符合预期：`kl_loss_coef=0.5`, `score=10.0`, `parallel_friendly=false`, `max_workers=1`, `val_env_groups=16`
- 第一个 checkpoint 将在 step 5 保存，第一次 test eval 在 step 20

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "status": "running",
    "current_step": 1,
    "total_steps": 30,
    "step_time_seconds": 240.14,
    "estimated_remaining": "1h56m (ETA ~06:15 UTC / 14:15 local)",
    "initial_validation_metrics": {
      "success_rate": 0.0625,
      "pass@1": 0.0625,
      "action_is_valid": 0.6875,
      "action_is_effective": 1.0,
      "num_actions": 28.6875,
      "response_length": 2818.25,
      "reward_mean@16": 0.625,
      "reward_best@16_mean": 6.28
    },
    "training_metrics": "not yet logged (step 1 just completed, no step-level metrics printed yet)",
    "config": {
      "kl_loss_coef": 0.5,
      "use_kl_loss": true,
      "kl_loss_type": "kl",
      "entropy_coeff": 0.001,
      "score (reward on success)": 10.0,
      "parallel_friendly": false,
      "max_workers": 1,
      "val_env_groups": 16,
      "val_n_groups": [
        16
      ],
      "train_env_groups": 4,
      "train_group_size": 16,
      "lr": 5e-07,
      "clip_ratio": "0.2-0.28",
      "ppo_epochs": 1,
      "save_freq": 5,
      "test_freq": 20
    },
    "command": "cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp023_grpo_parallel model_path=/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4 trainer.experiment_name=exp023c-alfworld-grpo-serial trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp023c/ trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp023c/ es_manager.val.env_groups=16 \"es_manager.val.env_configs.n_groups=[16]\"",
    "env_vars": "TMPDIR=/root/autodl-tmp/tmp/ ALFWORLD_DATA=/root/autodl-tmp/alfworld RAY_memory_monitor_refresh_ms=0 RAY_SYSTEM_MEMORY=210000000000 HYDRA_FULL_ERROR=1",
    "log_path": "/root/autodl-tmp/checkpoints/exp023c/train.log",
    "checkpoint_path": "/root/autodl-tmp/checkpoints/exp023c/ (empty, first save at step 5)",
    "gpu_status": "GPU 0: 61127/97887 MiB (0% util), GPU 1: 61173/97887 MiB (0% util)",
    "model": "qwen3 (num_hidden_layers=28, num_attention_heads=16, num_key_value_heads=8)",
    "base_checkpoint": "/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4"
  }
}
```

</details>

---
