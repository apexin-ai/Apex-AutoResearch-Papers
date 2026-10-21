# paper c1 c2 scope vif

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_c1_c2_scope_vif_20260522T095459_result.json`
- **Structured JSON:** [`91f330d8ae78a9c7227c.json`](../../sessions/91/91f330d8ae78a9c7227c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Body 通过 page 8 结束（main text），page 9 开始 Discussion/Limitations（EMNLP 不计入 8 页限制），page 10+ 是 references/appendix。Body ≤ 8 pages。

---

## 产出报告

### C1: Title/Abstract Scope 收紧

- **Title**：保留 "Information Extraction"，未修改
- **Abstract**：
  - 第 2 句改为 `---focusing on relation extraction as the primary testbed, with NER and event detection as boundary conditions---across four datasets`，明确 RE 为主要 testbed
  - 第 (2) 点 NER 改为 `the NER batch-level null serves as a boundary condition (dispersed error modes, BCS range compression)`，从"未检测到"改为"boundary condition"框架
- **Introduction contribution 2**：从 "task asymmetry" 改为 "task-dependent boundary"，NER null 明确标注为 `reported as a boundary condition rather than a negative result`

### C2: DocRED VIF=50.9 强化

- **§4.3 DocRED 段**：删除 R²=0.578 的 CI 和 per-count 分解（R²=0.653/0.614），改为直接声明 `uninterpretable as BCS-specific evidence`，VIF 通胀和 semipartial R²=0.056 紧跟其后。保留 ridge regularization 方向性证据和 FewRel 作为 clean evidence 的结论
- **Practical magnitude 段**：DocRED R² 提及加注 `inflated by multicollinearity (VIF=50.9)`

### 编译结果

- 0 errors, 0 undefined refs, 0 rerun warnings
- 26 pages total, body ≤ 8 pages（page 9 开始 Discussion/Limitations）

---
