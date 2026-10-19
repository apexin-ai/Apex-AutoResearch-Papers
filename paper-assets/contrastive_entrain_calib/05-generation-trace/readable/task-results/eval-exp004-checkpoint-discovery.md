# eval exp004 checkpoint discovery

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp004-checkpoint-discovery_20260520T141134_result.json`
- **Structured JSON:** [`fc12d51316833a445e8b.json`](../../sessions/fc/fc12d51316833a445e8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总结果

### 1. exp-004 Checkpoint 列表

全部 16 个 checkpoint 在 **westd-28034**：`/root/autodl-tmp/outputs/exp-004-act-baseline/`

| Checkpoint | 大小 | 状态 |
|------------|------|------|
| checkpoint-500 | 682M | **已 eval** |
| checkpoint-1000 | 682M | 需补充 eval |
| checkpoint-1500 | 682M | 需补充 eval |
| checkpoint-2000 | 682M | **已 eval** |
| checkpoint-2500 | 682M | 需补充 eval |
| checkpoint-3000 | 682M | 需补充 eval |
| checkpoint-3500 | 682M | 需补充 eval |
| checkpoint-4000 | 682M | 需补充 eval |
| checkpoint-4500 | 682M | 需补充 eval |
| checkpoint-5000 | 682M | 需补充 eval |
| checkpoint-5500 | 682M | 需补充 eval |
| checkpoint-6000 | 682M | 需补充 eval |
| checkpoint-6500 | 682M | 需补充 eval |
| checkpoint-7000 | 682M | 需补充 eval |
| checkpoint-7500 | 682M | 需补充 eval |
| checkpoint-8000 | 682M | **已 eval** |

每个 checkpoint 是 LoRA adapter（~698MB safetensors + tokenizer）。**13 个需要补充 eval。**

westd-29046 上**无 exp-004 checkpoint**。

### 2. exp-003 训练状态（westd-29046）

| 进程 | PID | 状态 | 已运行时间 |
|------|-----|------|-----------|
| seed 1 | 70649 | **Rl+ (运行中)** | 1天21小时21分 |
| seed 2 | 237432 | **Ss+ (运行中)** | 13小时54分 |

两个 GPU 均满载（GPU 0: 38049 MiB / 95%, GPU 1: 38161 MiB / 95%）。

### 3. westd-28034 GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 2 MiB | 0% |
| 1 | 2 MiB | 0% |
| 2 | 2 MiB | 0% |
| 3 | 2 MiB | 0% |

**4 个 GPU 全部空闲。** 无 Python 训练进程在跑。ckpt-4000 rerun **未在运行**（可能已完成或未启动）。

### 4. SCP 计划

**不需要 SCP。** 13 个待 eval checkpoint 已在 28034 上，且 28034 四个 GPU 全部空闲——直接在 28034 上跑补充 eval 是最优方案。29046 两个 GPU 被 exp-003 占满，不可用。

---
