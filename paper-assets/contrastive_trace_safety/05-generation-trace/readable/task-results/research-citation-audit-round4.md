# research citation audit round4

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation_audit_round4_20260517T175404_result.json`
- **Structured JSON:** [`57fcc76952a3a5fbf3ec.json`](../../sessions/57/57fcc76952a3a5fbf3ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已完成的三项工作：**

1. **6 篇新论文验证 + bib 生成** — 全部通过 WebSearch 确认存在，bib 条目已追加到 `references.bib`（第 313-360 行）

2. **Novelty threat 评估** — `hu2026refusal_dynamics` (arXiv:2605.02958) 威胁程度**低-中等**：
   - 它用 Causal Tracing 追踪标准 LLM 单次前向传播的跨层 refusal 传播
   - 本文用 temporal probing 追踪 reasoning model CoT 生成的跨时间步 safety commitment
   - 研究对象（标准 LLM vs reasoning models）、方法（causal tracing vs probing）、分析维度（层/空间 vs 步/时间）、核心贡献（adversarial robustness vs probe modality comparison）均不同
   - 建议在 Related Work 作为 concurrent work 引用并明确区分

3. **完整报告** 已保存到：
   `artifacts/citation_audit_round4.md`

**引用覆盖提升：** 现有 ~15 effective → 整合后 ~28（+6 新增 +7 orphan）。仍需后续 round 补充至 40+ 目标。

---
