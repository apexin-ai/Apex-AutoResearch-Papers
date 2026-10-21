# research related work gaps

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related-work-gaps_20260515T143846_result.json`
- **Structured JSON:** [`407a94df907f4861f1d5.json`](../../sessions/40/407a94df907f4861f1d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研报告已保存到 `artifacts/related_work_gap_analysis.md`。

总结：

**共找到 14 篇论文**，按引用优先级分三档：

**Must-cite（4 篇）**：
- **R1-RE** (2507.04642) — sentence-level GRPO RE 成功，与我们 doc-level GRPO 失败构成正反对比
- **Minimalist Approach** (2504.11343) — 证明 rejection sampling 可匹配 GRPO/PPO，为 FREIGE 的 RSFT 提供理论正当性
- **DAPO** (2503.14476) — 识别 GRPO 的 entropy collapse，解释我们 GRPO 失败的可能原因
- **Dr. GRPO** (2503.20783) — 识别 GRPO 的 length/normalization bias，在 DocRE 长序列场景下更严重

**Should-cite（5 篇）**：
- **RelPrior** (2511.08143) — 最新 LLM DocRE SOTA，直接竞争方法
- **AutoRE** (2403.14888) — ACL 2024，RHF 三阶段 QLoRA DocRE
- **Ru-LLM** (NLPCC 2025) — 逻辑规则约束 LLM DocRE
- **GLiDRE** (2508.00757) — 轻量级 few-shot DocRE
- **R²GRPO** (2505.22068) — 唯一成功将 GRPO 应用于 RE 任务的工作，高度相关

**Nice-to-cite（5 篇）**：Contrastive Rewards、EMNLP 2024 Contrastive RM、RFT 原始论文、LMRC、ToolRE。

---
