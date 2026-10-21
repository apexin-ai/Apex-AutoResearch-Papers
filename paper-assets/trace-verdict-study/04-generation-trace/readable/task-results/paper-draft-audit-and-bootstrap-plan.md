# paper draft audit and bootstrap plan

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_draft_audit_and_bootstrap_plan_20260516T010404_result.json`
- **Structured JSON:** [`6077bf98e68d6a4e2edb.json`](../../sessions/60/6077bf98e68d6a4e2edb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心结论：

**章节完成度 ~90%**。7 个章节 + appendix 均已写完，核心 3 个 claims 有充分数据支撑。

**3 个缺口需补**：
1. **DeepSeek full_trace v3 (79.16%)** — registry 已 DONE，但论文 Table 1 仍标 N/A。**最高优先级**，补上后 cross-model 对比表完整。
2. **Bootstrap 方法不统一** — 论文声明 paired bootstrap，但 DeepSeek 实验缺 save_predictions。**建议方案 A**：重跑 6 个 DeepSeek eval-only（~40min GPU），获取逐样本预测。无需重训。
3. **DebugBench / trace length ablation** — 部分实验 RUNNING/QUEUED，属锦上添花，非核心 claim 依赖。

**D034 叙事修正已全面落实** ✅ — 论文各处正确区分 full_trace label truncation vs VOTA trace content truncation。仅 appendix Table 10 标题 "label truncation bug" 措辞可进一步精确化。

详细报告、行动清单和 DDL 时间线已写入 `artifacts/paper_audit_20260516.md`。

---
