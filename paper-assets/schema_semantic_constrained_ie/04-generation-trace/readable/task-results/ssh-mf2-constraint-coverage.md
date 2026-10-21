# ssh mf2 constraint coverage

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mf2_constraint_coverage_20260519T073445_result.json`
- **Structured JSON:** [`e06b8de543b40b90d061.json`](../../sessions/e0/e06b8de543b40b90d061.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果写入 `artifacts/mf2_constraint_coverage_results.md`。

核心发现：

| 数据集 | Type-level 覆盖 | Instance-level 覆盖 |
|--------|----------------|-------------------|
| SciERC | 106/115 (92.2%) | 964/974 (**99.0%**) |
| DocRED | 313/360 (86.9%) | 12199/12275 (**99.4%**) |

- **未覆盖的 type pairs 与训练集中未见过的完全重合** (SciERC 9个, DocRED 47个)，说明约束表忠实反映了训练数据
- DocRED 的 gap 主要由 MISC 类型歧义驱动 (P178 developer MISC-MISC x10, P127 owned by MISC-MISC x8)
- SciERC 的 gap 集中在 Evaluate-for 关系 (5/9)
- 实例级覆盖率 >99%，未覆盖实例都是低频边缘情况，无需扩展约束表

---
