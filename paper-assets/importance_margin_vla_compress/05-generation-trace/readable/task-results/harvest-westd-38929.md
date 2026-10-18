# harvest westd 38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_westd-38929_20260523T143932_result.json`
- **Structured JSON:** [`90b6e1ac3ce30b3c6c92.json`](../../sessions/90/90b6e1ac3ce30b3c6c92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 不允许 PREPARING→RUNNING 直接转换。实验仍在运行中，暂不更新状态。

## 当前状态汇总

所有 4 个 E5 X-VLA attention pruning k=0.3 实验**仍在运行**，于 22:08 启动，已运行约 35 分钟。

| 实验 | Suite | 进度 | 已完成任务 SR | 估计剩余 |
|------|-------|------|--------------|---------|
| attn_mean Object k=0.3 | Object (10 tasks) | Task 8/10, ep 22/50 | T0=96%, T1=98%, T2=88%, T3=92%, T4=98%, T5=96%, T6=100%, T7=94% | ~30 min |
| attn_rollout Object k=0.3 | Object (10 tasks) | Task 7/10, ep 35/50 | T0=88%, T1=100%, T2=82%, T3=86%, T4=92%, T5=96%, T6=100% | ~40 min |
| attn_last Spatial k=0.3 | Spatial (10 tasks) | Task 5/10, ep 40/50 | T0=100%, T1=100%, T2=100%, T3=100%, T4=86% (task 5 几乎全 FAIL) | ~1-1.5h |
| attn_mean Spatial k=0.3 | Spatial (10 tasks) | Task 6/10, ep 11/50 | T0=100%, T1=100%, T2=100%, T3=100%, T4=86%, **T5=32%** | ~1h |

**中间趋势**：
- **Object k=0.3**: mean 暂时 running avg ~95.3%，rollout ~92.0%。比 k=0.5 的 mean=67.6%、rollout=63.6% **显著更高**，异常——可能后续任务会拉低
- **Spatial k=0.3**: 前 4 个任务几乎满分，但 Task 4-5 开始大幅下降（86%→32%），attn_last Task 5 也几乎全 FAIL。最终 SR 可能在 70-80% 范围

实验预计在 1-1.5 小时后全部完成。需要等完成后再来收割结果并更新 registry。

---
