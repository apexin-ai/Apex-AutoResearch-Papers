# analysis confidence gradient

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_confidence_gradient_20260514T170529_result.json`
- **Structured JSON:** [`4cc018d823d723954920.json`](../../sessions/4c/4cc018d823d723954920.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

## Confidence Gradient: Probe vs LF Disagreement

| conf | n | disagree% | P→prog, LF→stag | P→stag, LF→prog |
|------|-------|-----------|-------------------|-------------------|
| 1 | 39,408 | **23.61%** | 1,430 (3.63%) | 7,876 (19.99%) |
| 2 | 14,609 | **3.82%** | 231 (1.58%) | 327 (2.24%) |
| 3 | 792 | **0.88%** | 2 (0.25%) | 5 (0.63%) |
| ALL | 54,809 | **18.01%** | 1,663 (3.03%) | 8,208 (14.98%) |

**Label distribution per confidence:**

| conf | n | progress | stagnation | prog% |
|------|-------|----------|------------|-------|
| 1 | 39,408 | 29,654 | 9,754 | 75.2% |
| 2 | 14,609 | 9,276 | 5,333 | 63.5% |
| 3 | 792 | 279 | 513 | 35.2% |

关键发现：

1. **Disagreement 随 confidence 单调递减**：conf=1 时 23.6%，conf=2 降至 3.8%，conf=3 仅 0.88%。Probe 在高共识样本上几乎完全同意 LF。
2. **不对称性**：disagreement 主要来自 **probe→stagnation 但 LF→progress**（占总体 15.0%），集中在 conf=1 窗口（20.0%）。Probe 比 LF 更倾向于判断 stagnation。
3. **conf=1 占比 72%**（39,408/54,809），是 noise 的主要来源。这些窗口 3 个 LF 中只有 1 个投了多数方向（有 abstain 或分裂），LF label 本身可信度低。

JSON 已保存到 `artifacts/confidence_gradient.json`。

---
