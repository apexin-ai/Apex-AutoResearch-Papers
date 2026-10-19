# ops post restart3 status 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart3-status-28034_20260519T131603_result.json`
- **Structured JSON:** [`d4805d0e2912ae915c1f.json`](../../sessions/d4/d4805d0e2912ae915c1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 使用

| GPU | Mem | 任务 |
|-----|-----|------|
| 0 | 17.2/31.8 GB | exp-004 eval |
| 1 | 30.7/31.8 GB | exp-008v3 training |
| 2 | 29.9/31.8 GB | exp-008v3 training |
| 3 | 16.1/31.8 GB | exp-016 eval |

---

### 1. exp-004 multi-checkpoint eval (GPU 0)

- **PID**: 134070（不是 134064，可能重启过）
- **状态**: 运行中，checkpoint-500 的 eval，**120/362 (33%)**
- 21:01 启动，21:16 到 120/362，速率 ~8 samples/min
- **尚未完成任何 checkpoint** — 输出目录只有 log，无 json 结果
- 预计 checkpoint-500 完成: ~21:46
- 5 个 checkpoint 全部完成: **约 01:00 (May 20)**

---

### 2. exp-016 ActAdd re-eval (GPU 3, PID 126897)

- **状态**: 运行中，alpha=1.00 的 eval，**260/362 (72%)**
- 已完成: alpha=0.00 (18:33→19:33), alpha=0.50 (19:33→20:33) — 每个 ~1h
- 当前 alpha=1.00 从 20:33 开始
- **尚未写出任何 json 结果**（结果目录为空，可能全部跑完后统一写入）
- 剩余: alpha=1.00 约 15min + alpha=2.0 + alpha=5.0 各 ~1h
- 预计全部完成: **约 23:30**

---

### 3. exp-008v3 training (GPU 1+2, DeepSpeed)

- **状态**: 运行中，**step 1178/8000 (14.7%)**
- 14:41 启动，已跑 6h35m
- 速率: ~20-21 s/step
- 近期 reward: combined_mean 波动在 0.29-0.59，r1_mean ~0.25-0.375，r2_mean 始终 0.000
- **预计完成: ~May 21 11:00**（还需 ~38h）

---

### 注意事项

1. **r2_mean 持续为 0** — 如果 r2 是有效的 reward 分量，需要检查是否有 bug
2. exp-004 和 exp-016 的 eval 结果都是全部跑完后才写 json，中途无法查看部分结果
3. exp-004 的 PID 与预期不符 (134070 vs 134064)，可能是之前的进程挂了被重启

---
