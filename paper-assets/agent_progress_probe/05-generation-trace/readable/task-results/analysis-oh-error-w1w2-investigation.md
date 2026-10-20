# analysis oh error w1w2 investigation

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oh-error-w1w2-investigation_20260515T012336_result.json`
- **Structured JSON:** [`f038bccaef92b131a223.json`](../../sessions/f0/f038bccaef92b131a223.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。总结：

**W1**: 0.581 和 0.5984 都是正确的，差异来自评估范围——0.581 是全部 43,366 个 conf≥2 窗口的结果，0.5984 是 fewshot test split（6,122 窗口）的结果。同一个模型（probe-002）、同一份数据。无需修改 registry。

**W2**: 修复了 `oh_crossagent_error_analysis.py` 中的索引对齐 bug——用 `(trajectory_id, step_indices)` 键匹配替代位置索引。覆盖率从 28.4%（12,328 窗口）提升到 **100%**（43,366 窗口）。

修复后的 error overlap：
- Probe 错误 8,643 个，Structural 错误 1,342 个
- 重叠仅 358 个（probe 错误的 4.1%，structural 错误的 26.7%）
- 两种方法的错误高度互补

报告已写入 `artifacts/oh-error-analysis/w1w2_investigation.md` 并注册。

---
