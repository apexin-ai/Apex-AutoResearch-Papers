# ssh inventory bjb1 data

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_inventory_bjb1_data_20260523T040136_result.json`
- **Structured JSON:** [`09eed21f8dca9f9ec90f.json`](../../sessions/09/09eed21f8dca9f9ec90f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-17606 数据盘点

### 1. 总大小

| 路径 | 大小 |
|------|------|
| `/root/cost-verify-agent-rl/` | **525 MB** |
| `/root/autodl-tmp/` | **117 GB** |

### 2. 磁盘使用率

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/`（根分区） | 30G | 8.5G | 22G | 29% |
| `/dev/sda2`（数据盘，含 autodl-tmp） | 879G | 17G | 817G | 3% |

### 3. Checkpoints（/root/autodl-tmp/checkpoints/，共 90 GB，19 个条目）

| Checkpoint | 大小 |
|------------|------|
| exp029-seed4 | 25G |
| exp021_ragen_sft_v4 | 23G |
| exp029-seed200 | 21G |
| c_prime_step5_hf | 3.8G |
| exp029_seed300_step5_hf | 3.8G |
| exp029_seed42_step5_hf | 3.8G |
| exp029_seed7_high_kl_step5_hf | 3.8G |
| qwen_c_prime_step5_hf | 3.8G |
| qwen_exp029_seed200_step5_hf | 3.8G |
| qwen_exp029_seed300_step5_hf | 3.8G |
| qwen_exp029_seed4_step15_hf | 3.8G |
| qwen_exp029_seed7_high_kl_step5_hf | 3.8G |
| qwen_exp029_seed7_high_kl_step7_hf | 3.8G |
| qwen3_exp021_ragen_sft_v4 | 3.3G |
| qwen3-1.7b-exp019b-sft-v3 | symlink → 已删目录 |
| qwen3_sft_final | symlink → 已删目录 |
| qwen3_exp019b_sft | 不存在 |
| exp029-seed4-ood | 0 (空) |
| seed7-step5-mask-check | 0 (空) |

### 4. 其他大目录（/root/autodl-tmp/）

| 目录 | 大小 | 说明 |
|------|------|------|
| conda-envs | 12G | conda 环境 |
| models | 6.7G | 基座模型 |
| alfworld | 2.2G | 环境数据 |
| wandb + wandb_tmp | 174M | 实验日志 |
| pgpf | 78M | — |
| verl-agent | 95M | 框架 |
| expert_sft* (v1-v4) + sft_data | ~105M | SFT 训练数据 |
| ray_tmp + ray_seed200 + ray_1 | 88M | Ray 临时数据 |
| logs + eval_logs | 18M | 日志 |
| tmp | 43M | 临时 |

### 5. 项目代码目录（/root/cost-verify-agent-rl/，525 MB）

几乎全部被 `RAGEN/` 子模块占据（523 MB）。其余 `analysis/`、`artifacts/`、`models/` 均 < 1 MB。

### 注意

- 2 个 symlink（`qwen3-1.7b-exp019b-sft-v3`、`qwen3_sft_final`）指向的目标已不存在，可清理
- 2 个空目录（`exp029-seed4-ood`、`seed7-step5-mask-check`）可清理
- 数据盘 879G 仅用 17G（3%），空间充裕

---
