# diag westb unpruned grpo status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westb-unpruned-grpo-status_20260515T183838_result.json`
- **Structured JSON:** [`d7fea5bce4899cabccf2.json`](../../sessions/d7/d7fea5bce4899cabccf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. westb cuda:0 — Unpruned Baseline GRPO ✅ 已在运行

| 项目 | 值 |
|------|-----|
| PID | 547366 |
| 运行时间 | 3分45秒 |
| GPU 内存 | 82,748 MiB |
| 进度 | **6/100 steps** (~27s/step) |
| 模型 | `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B` |
| 输出 | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_baseline` |
| wandb | `grpo_unpruned_baseline` / run `e49c42ha` |
| wandb URL | https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/e49c42ha |
| 参数 | beta=0.01, loss=dapo, lr=1e-6, temp=0.4, rep_penalty=1.15, max_steps=100 |

之前的 Worker 已成功启动，训练正在正常推进。

### 2. westb cuda:1 — Standard GRPO v8 ✅ 存活

| 项目 | 值 |
|------|-----|
| PID | 534667 |
| 运行时间 | **3小时56分16秒** |
| GPU 内存 | 71,692 MiB |
| 模型 | `sft_standard_20` |
| run_name | `grpo_stage2_standard_20_v8` |

### 3. 磁盘空间 ✅ 充足

数据盘 `/root/autodl-tmp/`: 250GB 总量，已用 177GB，**剩余 74GB (29%)**。

### 总结

两张卡都在正常跑实验，无需人工干预。Unpruned baseline 预计约 42 分钟完成（100 steps × ~27s/step）。

---
