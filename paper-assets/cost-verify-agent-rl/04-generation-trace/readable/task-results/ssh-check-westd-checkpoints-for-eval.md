# ssh check westd checkpoints for eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_checkpoints_for_eval_20260522T204123_result.json`
- **Structured JSON:** [`efc4824cd63e476f83f2.json`](../../sessions/ef/efc4824cd63e476f83f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### HF Checkpoints（可用于 eval）

| Checkpoint | 类型 |
|---|---|
| `exp029_seed100_step5_hf` | 目录（+ symlink `qwen_exp029_seed100_step5_hf`） |
| `exp029_seed2_step15_hf` | 目录（+ symlink） |
| `exp029_seed42_step5_hf` | 目录（+ symlink） |
| `exp029_seed7_high_kl_step5_hf` | 目录（+ symlink） |
| `exp029_seed7_high_kl_step7_hf` | 目录（+ symlink） |
| `intervention_c_hard_cap_step5_hf` | 目录（+ symlink） |
| `intervention_c_hard_cap_step7_hf` | 目录（+ symlink） |
| `qwen_c_prime_step5_hf` | 目录 |
| `qwen_exp029_seed8_step5_hf` | 目录 |
| `qwen_exp029_seed4_step15_hf` | symlink → `exp029-seed4/global_step_15_hf` |
| `qwen_exp029_seed5_step10_hf` | symlink → `exp029-seed5/global_step_10_hf` |
| `qwen_exp029_seed6_step15_hf` | symlink → `exp029-seed6/global_step_15_hf` |
| `qwen_seed2048_step5_hf` | symlink → `exp029_new_seed_2048/global_step_5_hf` |
| `qwen3_exp021_ragen_sft_v4` | SFT baseline |
| `qwen3_8b_sft_v1` | SFT baseline |

### Seed7 原始（非 high_kl）checkpoint

**不存在。** `find` 未找到任何非 `high_kl` 的 seed7 checkpoint。

### 磁盘

| 分区 | 总计 | 已用 | 可用 | 使用率 |
|---|---|---|---|---|
| `/root/autodl-tmp` | 250G | 116G | 135G | 47% |

### GPU 状态

| GPU | 显存占用 | 总显存 | 利用率 |
|---|---|---|---|
| cuda:0 | 90,467 MiB / 97,887 MiB | **100%** |
| cuda:1 | 0 MiB / 97,887 MiB | 0% |
| cuda:2 | 38,123 MiB / 97,887 MiB | 0% |
| cuda:3 | 36,603 MiB / 97,887 MiB | 0% |

### Seed100 Eval 状态

**已启动。** tmux session `seed100_ood` 正在运行 OOD eval（`_alfworld_seed100_step5_ood_eval`），使用 `CUDA_VISIBLE_DEVICES=0`。Ray workers 和 wandb 进程均活跃，TaskRunner 在执行中（88% CPU）。GPU 2/3 上也有约 37GB 显存占用（推测为 vLLM 推理引擎）。

---
