# ssh check westd disk

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_disk_20260521T151930_result.json`
- **Structured JSON:** [`7773f315773a1c3333e2.json`](../../sessions/77/7773f315773a1c3333e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29022 磁盘状态报告

### 磁盘总览

| 分区 | 总容量 | 已用 | 可用 | 使用率 |
|------|--------|------|------|--------|
| 根分区 `/` | 30G | 5.1G | 25G | 17% |
| 数据盘 `/root/autodl-tmp` | 619G | 610G | **9.7G** | **99%** |

**数据盘未清理，仍仅剩 9.7G。**

### 大目录 Top 10

| 目录 | 大小 |
|------|------|
| grpo_unpruned_v2 | 15G |
| grpo_cka_only_15_seed123 | 14G |
| grpo_cka_only_15_v2 | 13G |
| grpo_standard_15_seed123_v3 | 13G |
| grpo_standard_15_seed456_v3 | 13G |
| grpo_standard_15_v2 | 13G |
| grpo_shortgpt_20 | 13G |
| sft_shortgpt_20 | 13G |
| sft_standard_15 | 13G |
| sft_cka_only_15 | 13G |

共约 67 个实验目录，大多在 11-15G 之间，合计 ~610G。

### 疑似失败实验（可安全删除的候选）

| 目录 | 大小 | 原因 |
|------|------|------|
| grpo_standard_15 | 104K | 极小，疑似失败 |
| grpo_standard_15_seed123 | 212K | 极小，疑似失败 |
| grpo_standard_15_seed456 | 208K | 极小，疑似失败 |
| grpo_standard_15_seed123_v4 | 0 | 空目录 |
| grpo_standard_15_seed456_v4 | 0 | 空目录 |
| sft_standard_20_westd | 12K | 极小，疑似失败 |
| sft_unpruned_baseline | 0 | 空目录 |

但这些都很小，删除不会释放有意义的空间。要腾出空间需要删除完整的 11-15G 实验目录。

### 4 个 eval 进程状态：全部运行中

| PID | 模型 | GPU | 启动时间 |
|-----|------|-----|---------|
| 379999 | grpo_cka_only_25 | cuda:0 | 21:30 |
| 380074 | sft_cka_only_25 | cuda:2 | 21:30 |
| 382472 | grpo_random_20 (checkpoint-100) | cuda:1 | 21:57 |
| 385685 | sft_random_20 | cuda:3 | 22:45 |

### GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 16.3G / 95.6G | 98% |
| cuda:1 | 15.3G / 95.6G | 98% |
| cuda:2 | 16.3G / 95.6G | 98% |
| cuda:3 | 15.3G / 95.6G | 91% |

4 GPU 全部满载运行。

### 结论

数据盘 99% 满，仅剩 9.7G，**未发生任何清理**。失败实验目录几乎不占空间。如需释放空间，需确认哪些已完成实验的完整 checkpoint（11-15G/个）可以删除。

---
