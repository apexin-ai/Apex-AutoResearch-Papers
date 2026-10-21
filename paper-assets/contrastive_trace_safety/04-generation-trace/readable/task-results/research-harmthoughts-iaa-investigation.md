# research harmthoughts iaa investigation

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_harmthoughts_iaa_investigation_20260519T181350_result.json`
- **Structured JSON:** [`00ce8de881d0485814fd.json`](../../sessions/00/00ce8de881d0485814fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成，文件已写入 `artifacts/harmthoughts_iaa_investigation.md`。

核心发现：

1. **IAA 有报告**：Fleiss' κ = 0.74 (Group 1) 和 0.80 (Group 2)，但仅覆盖 13 条 trace (691 sentences)，占总数据的 1.2%
2. **98.8% 数据由 Claude Sonnet 4.6 标注**，human-LLM 一致性仅通过 JSD=0.035 bits 验证（分布级别，非逐样本）
3. **CP 是我们自己的构造**：HarmThoughts 本身不定义 Commitment Point，我们从其 behavioral labels（RA/AL/CC/ED/IA 永久消失的位置）推导而来
4. **零引用**，无外部讨论——论文太新（2026年4月）

**Rebuttal 最大风险**：reviewer 可能质疑 LLM 标注的逐样本可靠性，因为原论文只做了分布级验证，未报告 human-vs-LLM 的 per-instance agreement。

---
