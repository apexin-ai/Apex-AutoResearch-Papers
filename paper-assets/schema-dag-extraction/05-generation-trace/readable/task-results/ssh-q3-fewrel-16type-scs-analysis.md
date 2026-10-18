# ssh q3 fewrel 16type scs analysis

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_q3_fewrel_16type_scs_analysis_20260517T145436_result.json`
- **Structured JSON:** [`13b2d912deaa8ae440f9.json`](../../sessions/13/13b2d912deaa8ae440f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**数据来源**:
- SCS: 80-type all-MiniLM-L6-v2 cosine similarity matrix,提取 16 val types 的 16×16 子矩阵
- Confusion: `fewrel_16rel_bootstrap` 实验 (100 bootstrap batches × 8 types/batch, Qwen3-32B-FP8, 49,600 predictions)
- 16 val types 与 64 train types **完全不重叠** (PIDs disjoint)

**Spearman correlation**:

| Setting | Pairs | ρ | p-value |
|---|---|---|---|
| 80-type training pool (d051, count_80) | 3160 | 0.158 | 5.1×10⁻¹⁹ |
| 80-type pool, count_16 subsets | 3160 | 0.153 | 6.3×10⁻¹⁸ |
| **16 val types (held-out)** | **120** | **0.470** | **6.1×10⁻⁸** |

方向一致（均为正相关），val split 的 ρ 更强（0.470 vs 0.158）。

Top confused pairs 也符合语义直觉：child↔mother (conf=1033, SCS=0.84)、competition class↔sport (conf=285, SCS=0.71)、member of↔part of (conf=177, SCS=0.90)。

**论文用一句话**: On the held-out FewRel validation split (16 relation types fully disjoint from the 64 training types), pairwise SCS-confusion Spearman correlation remains positive and significant (ρ = 0.470, p < 10⁻⁷, n = 120 pairs), ruling out training-set contamination as the driver of the observed relationship.

---
