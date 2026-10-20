# data build response matrix

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_build_response_matrix_20260520T203701_result.json`
- **Structured JSON:** [`586284519a1a5b291f4f.json`](../../sessions/58/586284519a1a5b291f4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证全部通过：

- **Shape**: (5227, 12508) — 12508 items 精确匹配 IRT 参数，5227 models = 5219 (accuracy CSV) + 8 个只出现在部分 subject 的额外模型
- **Density**: 59.1% — 与预期均值 accuracy ~0.59 完全吻合
- **Model accuracy cross-check**: 5 个随机模型 delta 全为 0.0000
- **Item IRT match**: 12508/12508 (100%)
- **Missing entries**: 仅 12,611 (0.019%)

产出文件：
| 文件 | 大小 | 说明 |
|------|------|------|
| `response_matrix.npz` | 48.3MB | CSR sparse (5227×12508), int8 |
| `response_matrix_index.npz` | 0.1MB | model_names + item_ids 索引 |
| `item_metadata.csv` | 1.5MB | 12508 items, IRT params + empirical_p |
| `model_metadata.csv` | 0.4MB | 5227 models, family/cohort/accuracy |

`empirical_p` 和 `irt_diff` 的关系符合预期：diff 是 IRT 估计的难度参数（logistic scale），empirical_p 是原始正确率，两者呈单调正相关但非线性（empirical_p ≈ 0.75× irt_diff 的逆 logit 映射）。

---
