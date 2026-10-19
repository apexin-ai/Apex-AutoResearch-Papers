# code exp 014 bocpd read

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_014_bocpd_read_20260516T211159_result.json`
- **Structured JSON:** [`c1ed103a639bd702c579.json`](../../sessions/c1/c1ed103a639bd702c579.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整分析：

---

## exp-014 BOCPD/CUSUM 结果分析

### 数据概况
- 43 条 trace，对比 first_crossing_point (FCP, K=5) baseline

### 汇总表

| Method | Detection Rate | Mean Lead | Median Lead | Early | Late |
|--------|---------------|-----------|-------------|-------|------|
| **FCP baseline** | 65.1% (28/43) | **+4.89** | 0.0 | 13 | 13 |
| BOCPD λ=10 | **93.0%** (40/43) | +3.45 | 0.0 | 16 | 19 |
| BOCPD λ=20 | 88.4% (38/43) | +1.97 | 0.0 | 16 | 17 |
| BOCPD λ=50 | 79.1% (34/43) | +1.15 | 0.0 | 14 | 16 |
| BOCPD λ=100 | 67.4% (29/43) | +1.03 | 0.0 | 10 | 14 |
| CUSUM t0.3_h3 | 65.1% (28/43) | +0.89 | -4.0 | 11 | 17 |
| CUSUM t0.3_h5 | 44.2% (19/43) | -1.79 | -5.0 | 7 | 12 |
| CUSUM t0.4_h3 | 53.5% (23/43) | -1.00 | -4.0 | 7 | 14 |

### Head-to-Head (BOCPD λ=10 vs FCP，仅双方均检测到的 27 条 trace)
- BOCPD 更早: **16**
- FCP 更早: 6
- 平手: 5

### 分析

1. **BOCPD 优势在 detection rate**：λ=10 检测到 93% 的 trace（vs FCP 65%），覆盖率显著提升。
2. **FCP mean lead 更高（4.89 vs 3.45）**：但这是 selection bias——FCP 只在信号强（easy）的 trace 上触发，天然偏向高 lead 值。
3. **Head-to-head BOCPD 胜出**：在双方都检测到的 trace 上，BOCPD 16:6 更早。
4. **CUSUM 全面失败**：所有配置 mean lead ≤ +0.89，median 均为负值，不如 FCP 也不如 BOCPD。

### 结论：**NEGATIVE**

核心假设是 BOCPD/CUSUM 能否比 raw threshold crossing **更早**检测 commitment。答案：

- **BOCPD 没有在 mean lead time 上超越 FCP**（3.45 < 4.89），尽管 head-to-head 有优势，但那是因为 BOCPD 能检测 FCP 漏掉的 difficult trace（这些 trace lead time 低/负，拉低了均值）。
- **CUSUM 明确失败**，所有配置均劣于 FCP。
- BOCPD 的真实贡献是**提高覆盖率**（93% vs 65%），但不是**提前检测时间**。

**对 Claim 3 的影响**：Change-point methods 无法作为"pre-textual early warning"的突破口。简单阈值交叉已经是 lead time 的 upper bound（在当前 probe quality 下）。要改善 lead time 需要提升 probe 本身的信号质量，而非后处理方法。

---
