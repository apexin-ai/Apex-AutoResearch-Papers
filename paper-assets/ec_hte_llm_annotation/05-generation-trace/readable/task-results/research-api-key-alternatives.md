# research api key alternatives

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_api-key-alternatives_20260521T004725_result.json`
- **Structured JSON:** [`07c741f922ac0a54554b.json`](../../sessions/07/07c741f922ac0a54554b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估报告已写入 `/home/ubuntu/ec_hte_llm_annotation/results/llm_alternatives_assessment.md`。

核心结论：

1. **首选方案**: Qwen2.5-72B-Instruct-AWQ (INT4) — 单张 A100 80GB 可运行，~1.5 小时完成 5000 条标注，费用 <¥20，accuracy ~82-85%
2. **建议立即走本地模型路径**，不再等 API key — 开源模型已达 GPT-4 的 90%+ 性能，且可复现性更好
3. **向 Director 申请**: 1x A100 80GB 半天使用权（AutoDL 租用约 ¥50 以内含冗余）
4. **额外价值**: 可同时跑 7B 和 72B 两个模型，形成"高/低质量标注者"对比，增强 HTE 实验发现

---
