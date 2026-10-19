# code fix literature warnings

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-literature-warnings_20260516T004234_result.json`
- **Structured JSON:** [`e50ba6a54c813ebaf35d.json`](../../sessions/e5/e50ba6a54c813ebaf35d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 warning 修复完成。

---

## 修复总结

### Warning 1: GRACE 幻觉引用 — **论文真实存在，无需删除**
- WebSearch 确认：[GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion](https://arxiv.org/abs/2509.05980)
- 作者：Xingliang Wang 等，2025，`wang2025grace` 引用键正确
- `related_work_v1.md` 中的描述（多层代码图 + 层次化检索增强补全）与论文内容吻合
- 此前 `related_work_expansion_report.md` 错误地排除了该论文

### Warning 2: literature_map.yaml 同步 — **新增 21 篇**
| 分类 | 新增 |
|------|------|
| hard_negative_mining | +8（InfoNCE, HCL, DCL, MoCHi, Understanding HN, ProGCL, WCL, CAPSTONE） |
| contrastive_code_learning | +3（CoCoSoDa, SynCoBERT, ContraBERT） |
| program_analysis_for_ml | +2（ProGraML, CrossCodeEval） |
| code_embeddings_search | +1（CoSQA） |
| graph_guided_inference | +1（GRACE） |
| representation_geometry（新建） | +6（Alignment&Uniformity, RepDegen, Anisotropy, BERT-flow, SimCSE, Whitening） |

总计：39 → 60 entries，8 个分类

### Warning 3: UniXcoder 事实错误 — **已修正**
- 文件：`artifacts/literature/related_work_references.md` 第 68 行
- 删除"StructFuse 的 backbone encoder 之一"，改为"代码检索领域的重要 baseline，不是 StructFuse 的 backbone。StructFuse 使用 Qwen2.5-Coder-3B 和 StarCoder2-3B"

### Warning 4: Dataflow negatives 方向错误 — **已修正**
- 文件：`artifacts/paper_drafts/related_work_supplement.md` Supplement B
- "share data-flow context" → "do *not* share data-flow context (¬reachable_G(x,q))"

### 修改文件列表
1. `artifacts/literature/related_work_references.md` — UniXcoder 描述修正
2. `artifacts/paper_drafts/related_work_supplement.md` — dataflow negatives 方向修正
3. `literature_map.yaml` — 新增 21 篇论文 + 新建 representation_geometry 分类

---
