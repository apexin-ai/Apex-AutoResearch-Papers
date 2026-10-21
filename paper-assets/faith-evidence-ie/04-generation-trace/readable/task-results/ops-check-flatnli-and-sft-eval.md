# ops check flatnli and sft eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-flatnli-and-sft-eval_20260514T122931_result.json`
- **Structured JSON:** [`50dcbeb85ccb1445aab4.json`](../../sessions/50/50dcbeb85ccb1445aab4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. mvp2_grpo_flatnli — 已终止 (KL 爆炸)

| 项目 | 值 |
|------|-----|
| 训练步数 | **5 / 756** |
| 退出原因 | **KL early stop** — KL = 50,844,539,289.6，阈值 100.0 |
| loss | 2,936,185,651.2 |
| format_reward | 0.117 |
| f1_reward | 0.062 |
| flat_nli_reward | 0.158 |
| total reward | 0.337 |
| checkpoint | 已保存到 `/root/autodl-tmp/grpo_flatnli` |
| EXIT_CODE | 129 (SIGHUP) |

**和 extract 实验一模一样 — step 5 KL 爆炸。** 训练约 14 分钟即触发 early stop。KL 从正常值直接飙到 508 亿，说明 GRPO 在当前配置下系统性不稳定，不是个别实验的偶发问题。

---

### 2. mvp2_sft_eval — 运行中

| 项目 | 值 |
|------|-----|
| 进程 | PID 47293，**存活**，已运行 41 分 11 秒 |
| 进度 | **26 / 247 batches (10.5%)**，batch_size=4 |
| 速度 | ~95s/batch |
| 预计剩余 | ~5.8 小时 (221 batches × 95s) |
| GPU | cuda:1，利用率 88%，10.7GB / 32.6GB |

---

### 3. GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| 0 | 57% | 13.1 / 32.6 GB |
| 1 | 88% | 10.7 / 32.6 GB ← sft_eval |
| 2 | 56% | 13.1 / 32.6 GB |
| 3 | 47% | 13.1 / 32.6 GB |

**GPU 0/2/3 未释放** — 各占 ~13GB。可能有残留进程，grpo_flatnli 虽然退出了但显存没回收，或者有其他任务在跑。

---
