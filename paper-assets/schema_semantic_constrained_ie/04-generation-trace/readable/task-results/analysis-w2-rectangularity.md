# analysis w2 rectangularity

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w2_rectangularity_20260515T085632_result.json`
- **Structured JSON:** [`5ce9605b92cff1a376d9.json`](../../sessions/5c/5ce9605b92cff1a376d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/rebuttal/w2_rectangularity_report.md`。

**核心数据:**

| 数据集 | Relations | Rectangular | head-only over-perm | indep dom/range over-perm |
|---|---:|---:|---:|---:|
| SciERC | 7 | 0/7 (0.0%) | 1.50× | 1.50× |
| DocRED | 96 | 23/96 (24.0%) | **3.46×** | 1.58× |

**代码逻辑确认:** `ontology_compiler.py:38` 的 `valid_tail_types_for_head(head_type)` 在 `type_mask_processor.py:323` 被调用。head 端独立检查 `dom(r)`，tail 端在 head 已确定后条件检查 σ(r) 切片 — 最终输出 pair 必然 ∈ σ(r)（pair-based）。

**论文修改方向:** §3 应改为 σ(r) ⊆ T × T 的 pair-based 表述，并加入 rectangularity 表。SciERC 100% / DocRED 76% 的 schema 非 rectangular，head-only 假设在 DocRED 上多放过 3.46× 非法 pair，是 reviewer 提出的代码-论文差距的合理性根据。

---
