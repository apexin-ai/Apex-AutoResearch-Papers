# analysis c4 decline root cause

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_decline_root_cause_20260514T180046_result.json`
- **Structured JSON:** [`66fc4d7cf461668dd3ee.json`](../../sessions/66/66fc4d7cf461668dd3ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 artifacts 并注册到 registry。核心发现：

**C4 下滑的 3 个驱动因素:**

1. **Code-side targeted 优势蒸发** (最主要) — 从 0-79 的 +40pp 崩塌到 109-125 的 0pp。后期 blind repair 大幅进步 (50%→71-88%)，而 targeted 下降 (90%→71%)。推测后期 code bug 更复杂，targeted 诊断反而锚定错误修复路径。

2. **FOL-side targeted 全线负向** (结构性) — 在所有区间都是 -33 到 -50pp。关键发现: FOL **逻辑错误**时 targeted 成功率仅 17% (1/6)，而 FOL **语法错误**时 75% (3/4)。逻辑错误太难修，blind 从头重写反而更有效。

3. **后期样本更难** (放大效应) — 109-125 的 disagree rate 53% (vs 0-79 的 30%)，FOL acc 从 81%降到 71%，Code acc 从 62%降到 53%。更多 disagree 放大了前两个问题。

**204 全量预测**: 边际趋势延续 → +5.6pp (勉强 PASS)，有 ~40% 概率跌破 5pp threshold。建议对 FOL 逻辑错误 fallback 到 blind strategy。

---
