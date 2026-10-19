# monitor eval progress check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_eval-progress-check_20260514T181508_result.json`
- **Structured JSON:** [`c844d69becc51b4b2136.json`](../../sessions/c8/c844d69becc51b4b2136.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 5 路 Eval 实验进度汇总

| # | 实验 | 服务器 | GPU | 运行时间 | 已完成 rollouts | 进度 | 预估剩余 | 状态 |
|---|------|--------|-----|---------|----------------|------|---------|------|
| 1 | eval-acr-spatial-v3 | bjb1 | cuda:0 | ~6.0h | 40/100 | 40% | ~9h | 运行中 |
| 2 | eval-acr-object-v3 | bjb1 | cuda:3 | ~6.0h | 40/100 | 40% | ~9h | 运行中 |
| 3 | eval-argmin-only-spatial | bjb1 | cuda:1 | ~28min | 0/100 | ~0% | ~14h | 运行中，尚无 rollout 输出 |
| 4 | eval-tiny-correction-spatial | bjb1 | cuda:2 | ~27min | 5/100 | 5% | ~8.5h | 运行中 |
| 5 | eval-vla-mean-spatial | bjb2 | cuda:0 | ~15.1h | 75/100 | 75% | ~5h | 运行中 |

### 关键观察

**实验 5 (VLA mean baseline)** 进度最快，预计再 ~5h 完成。K=10 mean 在 4090D 上约 5 rollouts/h。

**实验 1 & 2 (ACR v2)** 同步推进，各完成 4/10 tasks。速率 ~6.7 rollouts/h (4090)。

**实验 3 & 4** 刚启动 ~27 分钟。实验 4 已有 5 rollouts 输出（首个 task 5/10），实验 3 尚未产出第一个 checkpoint（K=10 reconvla，预计 ~45min 才会看到首条 rollout 5/10 输出）。

### 中间成功率速览

| 实验 | 已完成 tasks 的平均成功率 |
|------|------------------------|
| eval-acr-spatial-v3 | 2.5% (1/40) |
| eval-acr-object-v3 | 0.0% (0/40) |
| eval-tiny-correction-spatial | 4/5 = 80% (仅 task1 前半) |
| eval-vla-mean-spatial | 40.0% (28/70) |

值得注意：**tiny-correction (max_norm=0.05)** 前 5 rollouts 成功率 80%，远高于完整 CRM correction 的 spatial v3 (2.5%)。vla-mean baseline 总体 40%。数据还很少，待完整结果确认。

---
