# analysis supplementary completeness

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_supplementary-completeness_20260521T075031_result.json`
- **Structured JSON:** [`eb520e940ed55463dcae.json`](../../sessions/eb/eb520e940ed55463dcae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。`artifacts/supplementary_completeness_audit.md` 已注册。

核心发现：

- **88/132 (67%)** 实验已在论文中引用
- **28 个 val/test sweep 实验**是主要遗漏——可做一张 appendix checkpoint sweep 图，视觉化支撑 "<1pp checkpoint selection noise" 的声明
- **16 个**是训练/中间产物，无需引用
- **所有有科学价值的 negative 结果**已在论文中覆盖（P2P regression、majority voting 失败、re-repair 失败、4B seed123 不稳定）

唯一的 HIGH 优先级建议：用现有的 28 个 sweep 数据点画一张 checkpoint selection sensitivity 图加入 appendix。

---
