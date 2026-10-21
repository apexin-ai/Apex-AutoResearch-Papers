# code conll2003 data prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_conll2003_data_prep_20260514T100814_result.json`
- **Structured JSON:** [`bee55d145b0bca98c99c.json`](../../sessions/be/bee55d145b0bca98c99c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出汇总：

**生成文件：**
- `data/conll2003/train.json` — 14,041 instances, 23,499 entities
- `data/conll2003/dev.json` — 3,250 instances, 5,942 entities
- `data/conll2003/test.json` — 3,453 instances, 5,648 entities
- `data/conll2003/llmfactory_train.json` — 14,041 sharegpt 训练样本
- `code/convert_conll2003.py` — 转换脚本

**Entity type 分布（全量）：**

| Type | Train | Dev | Test |
|------|-------|-----|------|
| PER | 6,600 | 1,842 | 1,617 |
| ORG | 6,321 | 1,341 | 1,661 |
| LOC | 7,140 | 1,837 | 1,668 |
| MISC | 3,438 | 922 | 702 |

**验证：** 10 条抽样全部 `text[start:end] == entity["text"]` 通过。

**CoNLL-2003 Schema hint：**
```
Entity types: PER, ORG, LOC, MISC
```

---
