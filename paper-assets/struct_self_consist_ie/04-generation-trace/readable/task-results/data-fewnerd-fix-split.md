# data fewnerd fix split

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_fewnerd_fix_split_20260516T100409_result.json`
- **Structured JSON:** [`6287ad7bd6531d2a5d06.json`](../../sessions/62/6287ad7bd6531d2a5d06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**验证通过，exp-020 可以启动。**

修复结果：

| Split | Instances | Entities | Entity Types |
|-------|-----------|----------|--------------|
| train | 131,767 | 340,180 | **全部 8 种** (location 95k, person 76k, org 67k, other 34k, product 22k, building 18k, art 15k, event 14k) |
| dev | 18,824 | 48,741 | **全部 8 种** (location 14k, person 11k, org 10k, other 5k, product 3k, building 2.5k, art 2k, event 2k) |
| test | 37,648 | 96,842 | **全部 8 种** (location 27k, person 22k, org 19k, other 10k, product 6k, building 5k, art 4k, event 4k) |

所有 split 都有全部 8 种 entity types，0 offset errors。旧 intra 数据已备份到 `_intra_backup/`。LLM Factory 训练数据已重新生成。

---
