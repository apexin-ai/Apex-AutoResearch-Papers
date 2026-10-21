# audit data consistency p1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data_consistency_p1_20260517T000138_result.json`
- **Structured JSON:** [`2272fd4ca098d2dbe6e0.json`](../../sessions/22/2272fd4ca098d2dbe6e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。审计结果：

**修正 1 处错误**：`appendix_sampling_table.tex` 第 9 行 SciERC Greedy CF 从 9.82 改为 9.90（registry `phase2_scierc_full_s1` CF=0.099=9.90%）。

**验证 100+ 数据点全部正确**，覆盖：
- 所有主表（SciERC ablation、DocRED ablation、cross-model、composability、FT four-way ablation、post-hoc comparison、CF-DR tradeoff、sampling robustness）
- Abstract 和 Introduction 中引用的所有数字
- 正文段落中的内联计算（百分比变化、pp 差值、相对减少率）

**无法从 registry 验证**：runtime table（无 latency 实验 metrics）、DocRED sampling 行（实验仍在 QUEUED）。

报告已写入 `artifacts/data_consistency_audit.md`。

---
