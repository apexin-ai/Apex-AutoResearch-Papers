# monitor mag sweep progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_mag-sweep-progress_20260515T051416_result.json`
- **Structured JSON:** [`68d41ce0063b96ed42c3.json`](../../sessions/68/68d41ce0063b96ed42c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Magnitude Sweep 实时进度 — bjb2-28827

**运行时间**: ~2h | **所有 6 进程存活** | **GPU 利用率**: 18-20%, ~5.2 GB/卡

### 进度总表

| exp_id | norm | mode | tasks_done | per-task SR | running_avg | current | ETA |
|--------|------|------|-----------|-------------|-------------|---------|-----|
| perdof-norm003 | 0.03 | perdof | 2/10 | T0=60%, T1=100% | **80.0%** | 等待 T2 启动 | ~8h |
| perdof-norm005 | 0.05 | perdof | 2/10 | T0=50%, T1=100% | **75.0%** | 等待 T2 启动 | ~8h |
| perdof-norm02 | 0.2 | perdof | 2/10 | T0=60%, T1=90% | **75.0%** | 等待 T2 启动 | ~8h |
| perdof-norm03 | 0.3 | perdof | **1/10** | T0=70% | **70.0%** | T1: 5/10 rollouts (1/5) | ~9h |
| obsonly-norm005 | 0.05 | obs_only | 2/10 | T0=80%, T1=90% | **85.0%** | 等待 T2 启动 | ~8h |
| obsonly-norm02 | 0.2 | obs_only | 2/10 | T0=90%, T1=100% | **95.0%** | 等待 T2 启动 | ~8h |

### 关键发现（初步，仅 T0-T1）

**所有实验当前 SR 远高于 argmin baseline (42.9%)**——但只完成了 2 个最简单的 task，后续 task 难度递增，SR 会下降。

**更值得关注的信号：obs_only 在同 norm 下一致性地优于 perdof：**
- norm=0.05: obs_only **85%** vs perdof **75%** (+10pp)
- norm=0.2: obs_only **95%** vs perdof **75%** (+20pp)

如果这个趋势在 T2-T9 上延续，per-DOF conformal claim 不仅不会复活，反而可能成为 negative result——perdof CRM 比 obs_only CRM 更差。但只有 2 个 task，**过早下结论**。需要等到至少 T0-T6 完成（匹配 argmin baseline 的 task 范围）才能做裁决。

预计完成时间：约 8-9 小时后（今晚深夜/明早凌晨）。

---
