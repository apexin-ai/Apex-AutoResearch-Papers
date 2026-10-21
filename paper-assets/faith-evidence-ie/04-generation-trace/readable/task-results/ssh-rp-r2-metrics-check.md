# ssh rp r2 metrics check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rp-r2-metrics-check_20260514T212940_result.json`
- **Structured JSON:** [`84615e4ab3ca1cfbac2d.json`](../../sessions/84/84615e4ab3ca1cfbac2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## rp_r2 训练状态

| 项目 | 状态 |
|------|------|
| 进程 | PID 94758，存活，GPU 3 占用 13645MiB/32607MiB，49% util |
| 当前 step | **39/200**（20%），已运行 ~1h24m |
| 速度 | ~112s/step，预计剩余 ~5h |
| Checkpoint | `checkpoint-20`（save_steps=20，checkpoint-40 尚未保存） |
| wandb | **未连接**（日志中无任何 wandb 相关输出） |

### 指标（trainer_state.json, checkpoint-20）

| step | reward | format | f1 | ced | frac_zero_std | loss | KL |
|------|--------|--------|----|-----|---------------|------|----|
| 10 | 0.093 | 0.093 | 0.0 | 0.0 | 0.0 | 908 | 3.9e10 |
| 15 | 0.149 | 0.146 | 0.003 | 0.0 | 0.0 | 24,650 | 1.87e6 |
| 20 | 0.147 | 0.145 | 0.002 | 0.0005 | 0.0 | 1.34e7 | 1.42e9 |

**严重问题**：KL 散度在 10^6–10^10 量级爆炸，loss 也在持续膨胀（908→1340万）。CED 和 F1 reward 几乎为零，总 reward 基本全来自 format_reward（~0.15）。frac_reward_zero_std 恒为 0.0。日志中有多次 KL 超阈值警告。

### ckpt40 eval

已启动，正在推理中（1/62 batches, ~2%）。加载的是 `/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40` adapter，在 cuda:2 上运行。

---
