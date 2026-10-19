# monitor factorial progress check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_factorial-progress-check_20260518T034634_result.json`
- **Structured JSON:** [`459b63151a88c173da0f.json`](../../sessions/45/459b63151a88c173da0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## factorial_h2_episodeadv_seed1 状态报告

**进度**: Step 8/15 (53%) | 已运行 ~7h | 预计剩余 ~6h23m (完成 ~17:10 UTC)

### Train Metrics (Step 7,最新)

| 指标 | 值 | 趋势 |
|------|-----|------|
| Success | 17.2% | Step 1: 20.3% → 无上行 |
| Action Valid | 77.2% | 85.6% → 下降 |
| Action Effective | 87.8% | 97.0% → 下降 |
| Pass@8 | 43.8% | 68.8% → 下降 |
| Entropy | 0.621 | 0.359 → 上升 |
| KL Loss | 1.774 | 0.238 → 持续上升 |

### Val Metrics (Step 5, AlfworldOOD)
- **Success**: 5.97% (pass@1)
- **Action Valid**: 57.6%
- **Manager Invalid Action**: 33.4%
- 下一次 val 在 step 10

### GPU 健康
4 张 GPU 均已分配 ~45GB 显存，GPU 2 满载 (100%)，GPU 3 38%，GPU 0/1 瞬时 0%（FSDP 计算间隙，正常）。

### 关注点
1. **KL loss 快速膨胀** (0.24→1.77)，policy 大幅偏离 reference
2. **Train success 无上行趋势**，action validity 持续退化
3. **Train-val gap 大**: train 15.6% vs val 5.97%
4. **Step 时间变长**: 42min → 56min (response length 增长所致)

---
