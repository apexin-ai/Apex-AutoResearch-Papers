# research paper consistency audit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_consistency_audit_20260516T051151_result.json`
- **Structured JSON:** [`d6fd28ac087a0ea04120.json`](../../sessions/d6/d6fd28ac087a0ea04120.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告写入 `artifacts/_project/paper/consistency_audit.md`。

**核心发现**：

**5 个 Critical**:
1. **method.tex:136** — n_min=1 的 "46.7% hitting ceiling at b_max=20" 实为 "b\*>2 的比例"，非 hitting ceiling
2. **experiments.tex:19** — holdout 说 "67.8K documents" 但 eval 实际用 max_docs=5000
3. **discussion.tex:17** — citation key `wang2026survive` 与全文 `wang_2026_survive_contamination` 不匹配
4. **method.tex:93** — 51,913 micro-batches 与 6103 steps×4=24,412 不符
5. **τ=0.9/0.95** 数据在 registry 中找不到对应实验

**4 个 Warning**: table1 vs results.tex 表格冲突、citation key 格式两套、intro PPL 精度不一致、batch_size=8 无 registry

**已验证正确**: Main table 全部 15 个 PPL 数值、τ sweep (0.5-0.8)、n_min 消融、detector 指标、b\* 分布统计、所有 delta 计算。

---
