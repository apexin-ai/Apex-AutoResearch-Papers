# paper section5 scierc draft

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section5_scierc_draft_20260514T051334_result.json`
- **Structured JSON:** [`cef0222e05c5a2ede089.json`](../../sessions/ce/cef0222e05c5a2ede089.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/section5_scierc_draft.tex` 并注册。

内容结构：
- **Table 1**: 5×8 消融表（DR/ΔDR/RV/ET/CF + Rel-F1/Ent-F1），含 bold 标注和 multicolumn 分组
- **(a) Core result**: DR 15.37→0.93 (↓94%), R-F1 +0.13pp (F1-neutral), per-relation 数据, CF 升高指向 Discussion
- **(b) Grammar layer**: RV/ET→0% 零代价, DR 不变 (-0.53pp), 定位为 semantic 的前提
- **(c) Enabling dependency**: semantic-only ↓24% 且无法消 RV/ET, 加 grammar 后再降 92%, 证明 prerequisite 结构
- **(d) S1 vs S2**: S2 DR 持平但 R-F1 -0.33pp, triples 更少, CF 无实质改善, S1 为推荐配置

所有数字均与 registry 交叉验证，每个 quantitative claim 附 `% exp_id` 注释。

---
