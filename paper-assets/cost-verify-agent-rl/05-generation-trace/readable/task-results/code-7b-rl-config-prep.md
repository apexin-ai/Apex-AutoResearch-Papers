# code 7b rl config prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_7b-rl-config-prep_20260519T074116_result.json`
- **Structured JSON:** [`0bfbc49ac7e58cda83d0.json`](../../sessions/0b/0bfbc49ac7e58cda83d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

YAML 格式正确，checkpoint 路径存在（7 个 safetensors 分片）。

**配置文件路径**：
- `RAGEN/config/_alfworld_8b_cell_a.yaml` — Cell A (step-independent h=2)
- `RAGEN/config/_alfworld_8b_cell_c.yaml` — Cell C (episode-level full context)

**与 1.7B 配置的关键差异**：

| 参数 | 1.7B | 8B |
|---|---|---|
| model_path | qwen3_exp021_ragen_sft_v4 | qwen3_8b_sft_v1/checkpoint-231/ |
| n_gpus_per_node | 2 | 4 |
| CUDA_VISIBLE_DEVICES | 0,1 | 0,1,2,3 |
| enable_gradient_checkpointing | 隐式 True (default) | 显式 True |
| optimizer_offload | True | True |
| ppo_max_token_len_per_gpu | 65536 | 32768 (减半) |
| log_prob_max_token_len_per_gpu | 65536 | 32768 (减半) |
| enable_think | True (default) | False |

**Cell A vs Cell C 差异**（与 1.7B 一致）：

| 参数 | Cell A | Cell C |
|---|---|---|
| context_window_mode | step_independent | full |
| step_independent_history_length | 2 | 2 (不生效) |
| total_training_steps | 15 | 30 |
| experiment_name | 8b-cell-a-step-independent-h2 | 8b-cell-c-episode-level |
| checkpoint 目录 | 8b-cell-a/ | 8b-cell-c/ |

**潜在 OOM 降级方案**（如果 96GB 卡仍不够）：
1. `ppo_mini_batch_size: 16 → 8`
2. `ppo_max_token_len_per_gpu: 32768 → 16384`
3. `es_manager.train.env_groups: 16 → 8`

---
