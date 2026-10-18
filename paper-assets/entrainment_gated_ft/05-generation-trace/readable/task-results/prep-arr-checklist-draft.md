# prep arr checklist draft

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_arr-checklist-draft_20260522T185615_result.json`
- **Structured JSON:** [`de3f916e410aa550465d.json`](../../sessions/de/de3f916e410aa550465d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。草稿写入 `artifacts/arr_checklist_draft.txt` 并注册到 manifest。

要点：
- A1-A4 全部 Yes，覆盖 Limitations section 的五个方面（单次训练、覆盖范围、仅预训练、统计功效、Bonferroni 报告）
- B1-B3 Yes（Wang et al. model zoo、lm-eval-harness、flash-linear-attention 均已引用），B4-B6 N/A
- C1-C4 Yes，报告了 RTX PRO 6000、~5 GPU-hours inference-only、340M/1.3B 参数量、无超参搜索、完整统计方法
- D 全部 N/A（纯计算实验）
- E1 Yes（AI 写作辅助）
- 额外补充了 fairness/bias implications 段落，强调 per-example multiplicity 的公平性含义（Jaccard ≤ 0.10, alpha 0.14-0.30）

注意：现有 `arr_checklist.tex`（论文 PDF 内）仍写的是 3 architectures / 30 models，但论文实际已扩展到 5 architectures。本草稿按最新 5-arch 状态撰写。PDF 内的 checklist.tex 也需要同步更新。

---
