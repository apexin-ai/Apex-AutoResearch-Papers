# monitor exp029 mvp metrics

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp029_mvp_metrics_20260516T231108_result.json`
- **Structured JSON:** [`46ce9c55d2c7bc9e260a.json`](../../sessions/46/46ce9c55d2c7bc9e260a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部提取完毕。

## Exp029 完整 Metrics 表格

### Train Metrics (Steps 1-5)

| Metric | Step 1 | Step 2 | Step 3 | Step 4 | Step 5 |
|--------|--------|--------|--------|--------|--------|
| **success** | 17.97% | 10.16% | 35.16% | 32.81% | 10.16% |
| **pass@8** | 56.25% | 43.75% | 68.75% | 75.00% | 43.75% |
| **action_is_valid** | 0.682 | 0.573 | 0.673 | 0.674 | 0.530 |
| **entropy** | 0.0278 | 0.0320 | 0.0230 | 0.0266 | 0.0242 |
| **ppo_kl** | 0.000289 | 0.000429 | 0.000345 | 0.000600 | **0.00191** |
| **grad_norm** | 1.459 | 1.056 | 1.488 | 1.652 | 0.743 |
| **response_length** (train) | 7112 | 5902 | 6065 | 6338 | 8385 |
| **response_length** (gen) | — | 12826 | 10823 | 11463 | 14324 |

### Val Metrics (Step 0 = baseline, Step 5 = first checkpoint eval)

| Metric | Step 0 (baseline) | Step 5 |
|--------|-------------------|--------|
| **success_rate** | 12.5% | **25.0%** |
| **action_is_valid** | 0.783 | 0.704 |
| **pass@1** | 12.5% | 25.0% |
| **reward/mean@32** | 1.25 | 2.50 |
| **reward/best@32** | 9.84 | 9.99 |
| **response_length** | — | 5777 |
| **episodes** | 32 | 32 |

---

## MVP 判定

**Val success @ step 5 = 25% → PASS (阈值 ≥15%)**

- 相对 baseline (12.5%) 翻倍，绝对提升 +12.5pp
- 32 episodes 满足 C003 约束
- pass@1 = 25% 一致确认

### 关注点

1. **KL 跳升**: step 5 ppo_kl = 0.00191 (前几步 ≤0.0006)，策略正在快速偏移
2. **Train success 波动大**: step 3-4 达 ~33%，step 5 回落到 10.16%（高方差 + KL 相关）
3. **磁盘告警**: `/root/autodl-tmp/tmp/ray/` 已 95% 满（剩余 ~8.5 GB / 250 GB），继续训练可能 OOM 磁盘

---
