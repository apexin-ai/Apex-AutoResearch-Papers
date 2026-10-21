# paper reference expansion

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference_expansion_20260517T170455_result.json`
- **Structured JSON:** [`e323f56b75218315e8c0.json`](../../sessions/e3/e323f56b75218315e8c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

- **总引用数：62**（远超 30+ 目标）
- **无重复 bib 条目**
- **所有 `\cite{}` 在 bib 中均有对应条目**
- **无 undefined citation**

新增 3 篇（均来自 literature_map 中已有但 bib 中缺失的条目）：

| 引用键 | 论文 | 会议 | 集成位置 |
|--------|------|------|----------|
| `tulchinskii2024_intrinsic_dim` | Intrinsic Dimension Estimation for Robust Detection | NeurIPS 2023 | Related Work: AI Text Detection 段 |
| `li2024_mage` | MAGE: Machine-generated Text Detection in the Wild | ACL 2024 | Related Work: AI Text Detection 段（benchmark 列表） |
| `penedo2024_fineweb` | The FineWeb Datasets | NeurIPS 2024 | Discussion: data curation 引用链 |

论文已有的 62 篇引用覆盖了任务要求的所有类别。literature_map 中 43 篇条目现已全部在 bib 中有对应。

---
