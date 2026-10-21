# analysis cwm relaxed matching

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cwm-relaxed-matching_20260515T140658_result.json`
- **Structured JSON:** [`7d58fccea4edf907a59c.json`](../../sessions/7d/7d58fccea4edf907a59c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Relaxed matching 使 CWM 准确率不升反降**：
- v12: 58.04% → 56.98% (L4最宽松)
- seed123: 59.09% → 55.91% (L4最宽松)

原因：unparseable 预测默认到 majority class (pass, 73%) 实际上比模型真实预测更准。当我们解析出模型的实际输出时，recovered 预测只有 60-69% 正确率，低于 73% 的 majority baseline。CWM parseable-only 准确率仅 43-53%，说明模型根本没学到有效的执行预测。

**与 CLS 的 gap 不可消除**：L0 gap = 26pp → L4 gap = 28pp，relaxed matching 反而拉大了差距。审稿人 concern 彻底排除。

产出已注册为 artifact `art_20260515_180db3`。

---
