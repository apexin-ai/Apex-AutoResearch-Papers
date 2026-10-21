# monitor exp028c step5 val

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp028c_step5_val_20260516T030007_result.json`
- **Structured JSON:** [`1a47d586e4feb9ecbe42.json`](../../sessions/1a/1a47d586e4feb9ecbe42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是结构化报告。

---

## exp028c_selfguide_recipe 训练进度报告

### 基本状态
- **PID 824675**: 运行中，已运行 5h22m
- **当前步数**: Step 6/100（正在训练 step 6）
- **进度**: 6%
- **无 NaN / 无 OOM / 无异常错误** — 训练技术上完全健康

### 逐步 Metrics

| Step | Type | Success | Action Valid | Pass@8/1 | KL Loss | Entropy | Step 耗时 |
|------|------|---------|-------------|----------|---------|---------|-----------|
| 0 | **VAL** | **6.25%** | 74.49% | pass@1: 6.25% | — | — | — |
| 1 | train | 13.28% | 76.43% | 37.5% | 0.013 | 0.263 | 54.2 min |
| 2 | train | 6.25% | 83.20% | 25.0% | 0.171 | 0.247 | 52.0 min |
| 3 | train | 15.63% | 85.95% | 68.75% | 0.112 | 0.249 | 45.6 min |
| 4 | train | 18.75% | 87.94% | 62.5% | 0.031 | 0.234 | 46.1 min |
| 5 | train | 9.375% | 89.60% | 37.5% | **0.824** ⚠️ | 0.236 | 60.2 min |
| 5 | **VAL** | **6.25%** | **96.5%** | pass@1: 6.25% | — | — | (含 eval) |

### 重点：Step 5 Val 结果

**val success = 6.25%** — 与 step 0 baseline 持平，无提升。

vs MVP 阈值：
- **< 20% = FAIL**
- **20-25% = weak pass**
- **30%+ = strong pass**
- 当前 6.25% 远低于 20% fail 线

### 积极信号
- **val action_is_valid**: 74.49% → **96.5%**（+22pp），模型学会了生成合法动作
- **val reward mean**: 0.1186 → **0.5183**（+4.4x），整体 reward 在上升
- **val action_is_effective**: 95% → **100%**
- **Entropy 稳定** 在 0.234-0.263 区间，无 collapse 迹象

### 警告信号
1. **KL loss 在 step 5 飙升 27x**（0.031 → 0.824），可能是瞬态，需观察 step 6-7 是否回落
2. **Train success 高方差**: 13.28% → 6.25% → 15.63% → 18.75% → 9.375%，不稳定
3. **Val success 完全没动**，尽管行为质量指标（valid, effective）大幅改善

### 时间预估
- 平均 ~51.7 min/step（非 eval step ~49 min，eval step ~60 min）
- 已完成 5 个 train step + 进入 step 6
- **剩余 ~94 步 ≈ 81 小时（~3.4 天）**
- 下一个 val checkpoint: **step 10**（预计 ~4 小时后）

### 判断
Step 5 val 结果令人失望（success 未动），但只看过 1 个 val 点（step 0 → step 5），还太早下结论。action_is_valid 和 reward mean 的改善说明模型在学有用的行为，但还不足以完成完整任务。**建议至少等到 step 10 的 val 结果再做 pass/fail 判定。** 如果 step 10 val success 仍然 ≤ 6.25%，在已过 10% 训练进程的情况下 success 零增长，MVP 前景堪忧。

---
