# code wnut17 data prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wnut17_data_prep_20260514T100828_result.json`
- **Structured JSON:** [`4c3e5649258db9b0cdcc.json`](../../sessions/4c/4c3e5649258db9b0cdcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出已生成，汇总如下：

### 产出文件
| 文件 | 大小 |
|------|------|
| `data/wnut17/train.json` | 950KB |
| `data/wnut17/dev.json` | 280KB |
| `data/wnut17/test.json` | 399KB |
| `data/wnut17/llmfactory_train.json` | 2.3MB |
| `code/convert_wnut17.py` | 转换脚本 |

### 数据统计
| Split | Instances | Entities |
|-------|-----------|----------|
| train | 3,394 | 1,975 |
| dev | 1,009 | 836 |
| test | 1,287 | 1,079 |

### Entity type 分布 (train)
person: 660, location: 548, group: 264, corporation: 221, product: 142, creative-work: 140

### 验证结果
- test 集 1,079 个 entity 全部通过 `text[start:end] == entity["text"]` 校验，0 错误
- 非标准标签（DAY, CULTURE 等共 7 个 token）已过滤

### Schema hint
```python
WNUT17_SCHEMA_HINT = "Entity types: corporation, creative-work, group, location, person, product"
```

---
