# monitor progress check all 7

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress-check-all-7_20260514T212540_result.json`
- **Structured JSON:** [`73c8d3f993ae29b9f356.json`](../../sessions/73/73c8d3f993ae29b9f356.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度总结 (2026-05-15 05:26 UTC)

| 实验 | 服务器 | 进度 | 关键指标 | ETA |
|------|--------|------|---------|-----|
| eval-vla-mean-spatial | bjb2 GPU0 | **9/10 tasks** | avg 34.4% | ~2h |
| eval-argmin-only-spatial | bjb1 GPU1 | 3/10 tasks | avg 53.3% (3 tasks) | ~8h |
| eval-tiny-correction-spatial | bjb1 GPU2 | 3/10 tasks | avg 53.3% (3 tasks) | ~8h |
| **eval-acr-spatial-v4-default** | **bjb1 GPU0** | **0/10 — 未运行!** | **无进程** | **N/A** |
| eval-acr-spatial-v4-small | bjb1 GPU3 | 1/10 tasks | T1: 60% | ~9h |
| crm-train-v3-norm-obs-only | bjb1 GPU0 | epoch 26/50 | best val=0.01669 | ~35m |
| crm-train-v3-norm-scalar-unc | bjb1 GPU3 | epoch 26/50 | best val=0.03998 ↓ | ~35m |

### 早期信号对比（前 3 tasks）

| 实验 | T1 | T2 | T3 | 3-task avg |
|------|-----|-----|-----|-----------|
| vla-mean (K=10 baseline) | 70% | 100% | 0% | 56.7% |
| argmin-only (no CRM) | 60% | 100% | 0% | 53.3% |
| tiny-correction (norm=0.05) | 70% | 90% | 0% | 53.3% |
| v4-small (v3-norm, norm=0.1) | 60% | — | — | 60% |

### 异常告警

**eval-acr-spatial-v4-default 未运行** — Registry 标记 RUNNING 但服务器上无对应进程。GPU 0 被旧的 eval-acr-spatial-v3 tmux 会话 + crm-train-obs-only 占用。这是核心判定实验，建议：
1. CRM 训练 ~35min 后完成，届时 GPU 0 释放
2. 杀掉 stale eval-acr-spatial-v3 tmux 会话
3. 重启 v4-default eval

---
