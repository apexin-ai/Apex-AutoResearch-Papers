# data fewnerd preparation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_fewnerd_preparation_20260516T094449_result.json`
- **Structured JSON:** [`38a00bd94bd76a293c0d.json`](../../sessions/38/38a00bd94bd76a293c0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据加载和验证全部通过。

## 完成总结

**Few-NERD INTRA 数据已转换并集成到项目中。**

### 文件产出

| 文件 | 路径 |
|------|------|
| train.json | `data/fewnerd/train.json` (99,519 JSONL) |
| dev.json | `data/fewnerd/dev.json` (19,358 JSONL) |
| test.json | `data/fewnerd/test.json` (44,059 JSONL) |
| llmfactory_train.json | `data/fewnerd/llmfactory_train.json` |
| llmfactory_dev.json | `data/fewnerd/llmfactory_dev.json` |
| README.md | `data/fewnerd/README.md` |
| convert_fewnerd.py | `code/convert_fewnerd.py` |

### 统计

| Split | Instances | Entities | Avg tok/sent | Avg ent/sent | Entity Types |
|-------|-----------|----------|-------------|-------------|-------------|
| train | 99,519 | 208,637 | 26.9 | 2.10 | person (108k), other (48k), product (31k), art (21k) |
| dev | 19,358 | 28,649 | 26.0 | 1.48 | building (17k), event (12k) |
| test | 44,059 | 107,163 | 23.0 | 2.43 | location (64k), organization (43k) |

注：Few-NERD INTRA 设计特点 — 每个 split 使用不同的 entity type（用于 few-shot 评估）。

### 代码修改
- `sampling.py`: 添加 `FEWNERD_SCHEMA_HINT`
- `run_mvp_pilot.py`: 添加 `load_fewnerd` 导入、`--dataset fewnerd` 选项、schema hint 映射
- `data_utils.py`: 添加 `load_fewnerd()` 函数
- `dataset_info.json`: 添加 `fewnerd_uie_train` / `fewnerd_uie_dev` 条目

---
