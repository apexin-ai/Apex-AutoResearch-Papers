# analysis n500 preliminary

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n500-preliminary_20260514T235742_result.json`
- **Structured JSON:** [`9f4e9297e329a642f2d4.json`](../../sessions/9f/9f4e9297e329a642f2d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是汇总。

---

## n=500 Preliminary Analysis Results (s015 + s020, 8 conditions)

### 1. Median II (low−high) + Bootstrap CI (B=10,000)

**DeepSeek** (n_valid=496 per condition)

| Condition | Median II | 95% CI | CI excludes 0 | p_bonf |
|-----------|-----------|--------|---------------|--------|
| imp_s015 | +0.391 | [0.350, 0.443] | **Yes** | <0.001 |
| imp_s020 | +1.215 | [1.107, 1.336] | **Yes** | <0.001 |
| rand_s015 | +0.014 | [−0.017, 0.039] | No | 1.0 |
| rand_s020 | +0.032 | [−0.011, 0.077] | No | 1.0 |

**Qwen** (n_valid=475 per condition)

| Condition | Median II | 95% CI | CI excludes 0 | p_bonf |
|-----------|-----------|--------|---------------|--------|
| imp_s015 | +0.066 | [0.049, 0.093] | **Yes** | <0.001 |
| imp_s020 | +0.307 | [0.261, 0.356] | **Yes** | <0.001 |
| rand_s015 | −0.011 | [−0.039, 0.012] | No | 1.0 |
| rand_s020 | +0.015 | [−0.015, 0.068] | No | 1.0 |

### 2. d_z Within-Importance (s015 vs s020)

| Model | d_z | 95% CI | Interpretation | n_paired |
|-------|-----|--------|----------------|----------|
| DeepSeek | −0.468 | [−0.528, −0.415] | small | 496 |
| Qwen | −0.509 | [−0.608, −0.422] | medium | 475 |

负号表示 s020 的 II 显著大于 s015（符合预期的 dose-response 方向）。

### 3. 与 n=50 Baseline 对比

| Condition | n=50 Median | n=50 CI | n=500 Median | n=500 CI |
|-----------|-------------|---------|--------------|----------|
| DS imp s015 | 0.324 | [0.199, 0.472] | 0.391 | [0.350, 0.443] |
| DS imp s020 | 1.152 | [0.655, 1.256] | 1.215 | [1.107, 1.336] |
| QW imp s015 | 0.048 | [−0.005, 0.110] | 0.066 | [0.049, 0.093] |
| QW imp s020 | 0.208 | [0.067, 0.402] | 0.307 | [0.261, 0.356] |

关键观察：
- **CI 大幅收窄**（~3× narrower），10× 样本量的直接效果
- **QW imp s015 从 marginal 变为 clearly significant** — n=50 时 CI 触及零 [−0.005, 0.110]，n=500 完全排除零 [0.049, 0.093]
- 点估计方向一致，magnitude 略有上升但在 n=50 CI 范围内 — 无方向反转
- Random masking 在两个 n 下都一致显示零效应

### 4. 异常/风险标记

1. **Qwen mid_null_rate = 45.2%** — 近半数 prompts 无中相段（DeepSeek 仅 10.2%）。这降低了 Qwen 的有效中相样本量但不影响 II(low−high) 主指标。
2. **LaTeX 输出 bug** — `analyze_n500_unified.py:442` 对 random conditions 报 `KeyError: 'median_ii_diff_ci'`，JSON key 命名不一致。非阻塞，JSON/CSV 输出完整。
3. **Dose-response 测试不可用** — 需 ≥3 sparsity levels，当前只有 2 个。等 s025 完成后可执行。
4. **无方向反转、无 CI 跨零的 importance conditions** — 数据质量正常。

---
