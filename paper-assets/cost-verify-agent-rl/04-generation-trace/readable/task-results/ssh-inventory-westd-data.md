# ssh inventory westd data

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_inventory_westd_data_20260523T042347_result.json`
- **Structured JSON:** [`caf46edf5ef6bcab7f42.json`](../../sessions/ca/caf46edf5ef6bcab7f42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已收集完毕。汇总如下：

---

## westd-47453 数据盘点

### 1. 磁盘使用率

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/`（根分区） | 30G | 14G | 17G | 47% |
| `/root/autodl-tmp`（数据盘） | 250G | 135G | 116G | 54% |

### 2. 项目目录 `/root/cost-verify-agent-rl/` — **629M**

| 子目录 | 大小 |
|--------|------|
| RAGEN/ | 590M |
| logs/ | 39M |
| analysis/ | 284K |
| backups/ | 0 |

### 3. 数据盘 `/root/autodl-tmp/` — **135G**

**大块占用：**

| 目录 | 大小 | 说明 |
|------|------|------|
| **checkpoints/** | **109G** | 训练 checkpoint（详见下表） |
| **models/** | **20G** | 预训练模型 |
| fineweb_sample/ | 2.0G | 数据集 |
| alfworld/ | 2.2G | ALFWorld 环境 |
| expert_sft/ | 797M | SFT 数据 |
| hf_cache/ | 573M | HF 缓存 |
| 其他（ray_*、logs、wandb_tmp 等） | ~200M | 运行时临时数据 |

### 4. Checkpoints 详情（36 个目录，109G）

**大 checkpoint（原始训练输出）：**

| Checkpoint | 大小 |
|------------|------|
| exp029-seed100 | 41G |
| exp029-seed5 | 25G |

**HF 格式 checkpoint（每个 ~3.8G）：**

| Checkpoint | 大小 |
|------------|------|
| exp029_seed100_step5_hf | 6.5G |
| qwen_exp029_seed100_step10_hf | 3.8G |
| qwen_exp029_seed8_step5_hf | 3.8G |
| intervention_c_hard_cap_step5/7_hf | 3.8G × 2 |
| exp029_seed7_high_kl_step5/7_hf | 3.8G × 2 |
| qwen_c_prime_step5_hf | 3.8G |
| exp029_seed2_step15_hf | 3.8G |
| exp029_seed42_step5_hf | 3.8G |
| qwen3_exp021_ragen_sft_v4 | 3.3G |

**空目录（符号链接或已清理，0 字节）：** 7b-sft-eval-ood, 7b-zeroshot-eval, 8b-cell-c, qwen3_8b_sft_v1, exp029_seed3, sft-1.7b-baseline-ood-eval, exp029_seed8_ood_precollapse, seed2048_step5_ood_eval, intervention_c_step5_ood_eval, exp029_seed4_ood_eval, gae_baseline

**模型文件：**

| 模型 | 大小 |
|------|------|
| Qwen3-8B | 16G |
| Qwen3-1.7B | 3.8G |

### 5. 总结

- 数据盘 54% 已用，剩余 **116G** 可用
- checkpoints 是最大占用（109G），其中 exp029-seed100（41G）和 exp029-seed5（25G）占了 60%
- 11 个空 checkpoint 目录可清理
- 根分区 47%，无压力

---
