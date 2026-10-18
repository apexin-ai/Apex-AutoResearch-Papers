# code three way comparison prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_three_way_comparison_prep_20260516T020126_result.json`
- **Structured JSON:** [`97a2a64b26ebece598d7.json`](../../sessions/97/97a2a64b26ebece598d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三组数据全部加载成功：

| 数据源 | 批次数 | BCS 范围 | Acc 范围 |
|--------|--------|----------|----------|
| 16-rel 独立 pool | 100 | [0.653, 0.900] | [0.712, 0.952] |
| 80-pool → 16-sub | 63 (进行中) | [0.491, 0.654] | [0.656, 0.979] |
| 80-rel full pool | 25 | [0.646, 0.823] | [0.667, 0.938] |

脚本就绪，`/root/schema-dag-extraction/scripts/three_way_comparison.py`。80-pool 16-sub 实验完成后（100 batches），直接运行：

```bash
/root/miniconda3/bin/python scripts/three_way_comparison.py
```

注意 80-rel full pool 只有 25 个 random count_8 batch（来自 `fewrel_formal_full/eval_exp2.json`），如果需要更多数据点可以追加 `fewrel_formal/eval_exp2.json` 的数据——目前脚本只读 `fewrel_formal_full` 下的两个文件。

---
