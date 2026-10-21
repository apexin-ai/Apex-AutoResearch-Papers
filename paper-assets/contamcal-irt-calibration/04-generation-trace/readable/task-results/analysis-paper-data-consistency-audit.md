# analysis paper data consistency audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper-data-consistency-audit_20260519T220906_result.json`
- **Structured JSON:** [`e87b3db381e5c4b330fe.json`](../../sessions/e8/e87b3db381e5c4b330fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**Algorithm 1**: 代码与 artifacts 伪代码完全一致。论文版本将 `V-recovery-full` 合并为 `V-recovery`（5 patterns vs 代码 6 patterns），逻辑分支全部匹配，仅标签不同。需决定是否对齐。

**Sensitivity**: **全部 6 处仍写 "30 combinations"，未更新为 180。** 涉及 method.tex、results.tex (Table 1 caption + 正文)、appendix.tex (描述 + Table caption + 数据行)。这是最大的遗留问题。

**V-recovery 双种子**: method.tex 和 results.tex 已正确反映双种子。三个小问题：limitations.tex 段落标题仍为 "Single seed."（内容已更新）、abstract 只提 partial rebound 未提 full、"Triple-seed validation in progress" 需确认是否过时。

---
