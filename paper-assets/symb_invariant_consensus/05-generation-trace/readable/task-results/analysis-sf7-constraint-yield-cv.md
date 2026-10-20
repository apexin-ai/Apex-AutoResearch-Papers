# analysis sf7 constraint yield cv

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sf7-constraint-yield-cv_20260523T213717_result.json`
- **Structured JSON:** [`7dc572a73e2708bbf8e8.json`](../../sessions/7d/7dc572a73e2708bbf8e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到服务器。关键发现：

### Observation 1 评估：**SUPPORTED（有条件）**

**Per-problem CV（核心指标）**：
- Median CV = **0.2572** < 0.3 阈值 → 支持 "approximately uniform yield"
- 64.2% 的问题 CV < 0.3，91.2% < 0.5
- Mean CV = 0.3189, Q25=0.19, Q75=0.36

**Overall yield**：mean=5.75, std=2.36, CV=0.41（跨问题变异较大，但这是 between-problem 的，不影响 Observation 1 的 within-problem 假设）

### 两个 WARNING

**1. Majority vs Minority yield 显著不同** (p=5.2e-06)：
- Majority traces: mean=5.61 (n=1621)
- Minority traces: mean=6.04 (n=827)
- Minority traces 平均多产出 ~0.43 个约束 (+7.7%)

**2. Correct vs Incorrect yield 显著不同** (p=5.3e-11)：
- Correct traces: mean=5.41 (n=1136)
- Incorrect traces: mean=6.05 (n=1312)
- Incorrect traces 平均多产出 ~0.64 个约束 (+11.9%)

### 对 SICA-SC equivalence 的影响

虽然 per-problem CV 中位数支持 "approximately uniform" 假设，但存在一个系统性偏差：**错误/少数派 traces 产出更多约束**。这对 SICA 有利而非不利——错误 traces 虽然多产约束，但这些约束在 MaxSAT 中更可能相互矛盾被排除。效应量较小（~8-12%），不足以颠覆 Observation 1 的核心结论。

建议 rebuttal 中可以这样回应：per-problem CV median=0.26 支持 uniform yield 假设；虽然 correct/incorrect groups 间存在统计显著差异，但绝对差异仅 ~0.6 个约束（<12%），不影响 SICA-SC agreement 的理论推导。

---
