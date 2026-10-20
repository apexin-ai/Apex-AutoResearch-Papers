# analysis math data quality

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_math-data-quality_20260515T090125_result.json`
- **Structured JSON:** [`4605eb40fe607623b9ce.json`](../../sessions/46/4605eb40fe607623b9ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是结构化报告：

---

## MATH 数据质量验证报告

### 1. Fix-applied subset (N=250, problems 51-300)

| 指标 | 值 | 95% Bootstrap CI |
|------|-----|-----------------|
| Internal accuracy | 82.0% | [77.2%, 86.8%] |
| Code interpreter accuracy | 77.6% | [72.4%, 82.4%] |
| **Diff (internal − code)** | **+4.4%** | **[−0.4%, +9.2%]** |

**关键判断：差异 CI 包含 0，不再显著。** N=300 时 CI 为 [+0.7%, +9.3%] 刚好排除 0，去掉 buggy pilot 后变为 [−0.4%, +9.2%]，不再排除 0。

### 2. N=300 vs N=250 对比

| 指标 | N=300 | N=250 | 变化 |
|------|-------|-------|------|
| Internal acc | 81.7% [77.3%, 86.0%] | 82.0% [77.2%, 86.8%] | +0.3pp |
| Code acc | 76.7% [71.7%, 81.3%] | 77.6% [72.4%, 82.4%] | +0.9pp |
| Diff | +5.0% [+0.7%, +9.3%] | +4.4% [−0.4%, +9.2%] | −0.6pp, **显著性消失** |

Pilot (N=50) 单独指标：Internal 80.0%, Code 72.0%, Diff **+8.0%** — pilot 的 diff 是 fixed subset 的近两倍，明显拉高了全量估计。

### 3. Per-level breakdown（全部 300 题均为 Algebra）

数据中无 multi-topic，所有题目都是 Algebra。改用 difficulty level 拆分：

**N=250 (fix-applied):**

| Level | N | Internal | Code | Diff (code−int) |
|-------|---|----------|------|------------------|
| Level 4 | 122 | 86.9% | 84.4% | −2.5% |
| Level 5 | 128 | 77.3% | 71.1% | −6.2% |

**N=300 (full):**

| Level | N | Internal | Code | Diff (code−int) |
|-------|---|----------|------|------------------|
| Level 4 | 152 | 84.2% | 80.3% | −3.9% |
| Level 5 | 148 | 79.1% | 73.0% | −6.1% |

Level 5 的 code interpreter 劣势更大（−6.2% vs −2.5%），符合预期——更难的题 code interpreter 更容易出错。

### 4. Filtered problems 来源分析

| 指标 | Pilot (1-50) | Fixed (51-300) |
|------|-------------|----------------|
| Filtered (无代码执行) | 9/50 (18.0%) | 73/250 (29.2%) |
| **Empty code output (sandbox bug)** | **16/50 (32.0%)** | **9/250 (3.6%)** |
| Empty outputs / total executions | 17/46 (37.0%) | 11/207 (5.3%) |

**Sandbox bug 集中在 pilot：** pilot 中 32% 的题产生 empty output，fixed subset 仅 3.6%。Bug 使 pilot 的 code accuracy 被人为压低（72.0% vs 77.6%），导致 pilot diff 膨胀到 +8.0%，拉高全量 diff 至 +5.0% 并刚好越过显著性门槛。

### 关键结论

**N=250 的 diff CI [−0.4%, +9.2%] 包含 0。** 论文中 "internal reasoning significantly outperforms code interpreter" 的措辞需要调整。选项：

1. **报告 N=250 clean subset**，承认差异在 95% CI 下不显著（但 point estimate 仍为 +4.4%，方向一致）
2. **同时报告 N=300 和 N=250**，注明 pilot sandbox bug 及其影响
3. **软化措辞**：从 "significantly higher" 改为 "numerically higher but not statistically significant after removing contaminated pilot data"

---
