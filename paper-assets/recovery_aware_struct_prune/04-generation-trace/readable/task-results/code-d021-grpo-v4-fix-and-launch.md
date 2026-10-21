# code d021 grpo v4 fix and launch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d021-grpo-v4-fix-and-launch_20260515T081725_result.json`
- **Structured JSON:** [`1f618116837dba0c1772.json`](../../sessions/1f/1f618116837dba0c1772.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

First GRPO step involves generating completions (2048 tokens, 4 generations per prompt) — takes a few minutes. GPU 0 at 100% confirms active generation.

Here's the full status report:

---

## GRPO v4 Launch Report

### 1. TRL Version & ref_model 方案

- **TRL 1.1.0** — `GRPOTrainer.__init__` 不接受 `ref_model` 参数，而是通过 `create_model_from_path` 内部创建
- **方案 B: monkey-patch** `trl.trainer.grpo_trainer.create_model_from_path`
  - 检测 config 中的 `per_layer_intermediate_size` 属性
  - 有此属性时路由到 `load_pruned_model`（支持非均匀 MLP 维度）
  - 无此属性时回退到原始函数

### 2. train_grpo_v4.py 关键改动

| 改动 | v3 | v4 |
|------|----|----|
| ref_model 加载 | 无处理（crash） | monkey-patch → `load_pruned_model` |
| temperature | 0.7 | **0.4** |
| repetition_penalty | 无 | **1.15** |
| save_steps | 200 | **100** |
| save_total_limit | 5 | **3** |
| gradient_checkpointing | 未设 | **true** |

### 3. v4 完整参数表

| 参数 | 值 |
|------|----|
| model_path | `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20` |
| output_dir | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v4` |
| GPU | cuda:0 |
| learning_rate | 1e-6 |
| num_train_epochs | 1 |
| max_samples | 1000 |
| per_device_train_batch_size | 1 |
| gradient_accumulation_steps | 4 |
| num_generations | 4 |
| max_completion_length | 2048 |
| beta | 0.01 |
| loss_type | dapo |
| temperature | 0.4 |
| repetition_penalty | 1.15 |
| format_reward_weight | 0.1 |
| gradient_checkpointing | true |
| save_steps | 100 |
| save_total_limit | 3 |
| reward_desert_patience | 50 |
| dtype | bfloat16 |

### 4. Launch 验证

| 项目 | 状态 |
|------|------|
| tmux session | `grpo_stage2_rasp_20_v4` 存活 |
| PID | 339111 (R state, 416 threads) |
| GPU 0 显存 | **68643 MiB / 97887 MiB (70%)**, 100% utilization |
| GPU 1 | 51575 MiB (sft_standard_20_retrain 运行中) |
| ref_model | monkey-patch 成功，16:49 加载完成 (8 min) |
| wandb | run `grpo_stage2_rasp_20_v4` (ID: `75d1o9wa`) |
| 训练进度 | 0/250 步（首步生成中） |
| 报错 | 无 |

### 5. 磁盘空间

| 分区 | 容量 | 已用 | 可用 |
|------|------|------|------|
| / (root) | 30G | 8.6G | **22G** |
| /root/autodl-tmp (data) | 250G | 141G | **110G** |

---

Standard variant 脚本 (`run_grpo_stage2_v4_standard.sh`) 已创建但未启动，cuda:1 当前被 `sft_standard_20_retrain` 占用。

---
