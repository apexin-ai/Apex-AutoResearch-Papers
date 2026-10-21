# paper section3 method fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section3_method_fix_20260514T055206_result.json`
- **Structured JSON:** [`b721d247738972a0fcb5.json`](../../sessions/b7/b721d247738972a0fcb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修改已完成，两个副本均已同步：

**Warning 1 — Head type masking fallback**：与实际代码 (`type_mask_processor.py` `_mask_head_type`) 对齐。原文错误地写 fallback 到全部 $\mathcal{E}$，修正为三级逻辑：
1. $h_j \in \mathcal{D}$ 且 type $\in \operatorname{dom}(r_j)$ → 强制单一 type
2. $r_j$ 已知 → fallback 到 $\operatorname{dom}(r_j)$
3. $r_j$ 未知 → 无 semantic mask，仅 grammar 层兜底

**Warning 2 — Decidability taxonomy 去重**：§3.1 保留为 canonical definition，末尾加前向引用到 `Section~\ref{sec:composition}`。§4 已有的重复描述可在后续编辑中简化为引用回 §3.1。

---
