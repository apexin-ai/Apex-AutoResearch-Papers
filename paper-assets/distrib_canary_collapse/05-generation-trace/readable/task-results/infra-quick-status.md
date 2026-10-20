# infra quick status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_quick-status_20260514T072106_result.json`
- **Structured JSON:** [`19a9ff556694160b32bd.json`](../../sessions/19/19a9ff556694160b32bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## verify_gen01 实验状态

| 项目 | 状态 |
|------|------|
| **进程** | 存活。PID 10293，`iterative_train.py`，CPU 202%，已运行 ~28 分钟 |
| **GPU** | GPU 0 占用 12,522 MiB / 97,887 MiB，利用率 87%。GPU 1 空闲 |
| **当前阶段** | Gen 1 训练中（gen_1/trainer 目录已建，synthetic_data 已生成，但 metrics.json / checkpoint 尚未产出） |

### Gen 0 metrics.json（已完成）
```json
{
  "token_entropy": 3.234,
  "self_bleu": 0.0102,
  "distinct_1": 0.098,
  "distinct_2": 0.518,
  "distinct_3": 0.813,
  "ece": 0.0108,
  "effective_rank": 46.61,
  "perplexity": 315.08,
  "mauve": 0.034,
  "generation": 0
}
```

### Gen 1
- `synthetic_data/` 已生成
- `trainer/` 目录刚建立（15:21），训练正在进行
- `metrics.json`、`checkpoint/`、`all_metrics.json` 均未产出

**结论：实验正在运行，Gen 0 已完成，Gen 1 正在训练中，尚未结束。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "token_entropy": 3.234,
    "self_bleu": 0.0102,
    "distinct_1": 0.098,
    "distinct_2": 0.518,
    "distinct_3": 0.813,
    "ece": 0.0108,
    "effective_rank": 46.61,
    "perplexity": 315.08,
    "mauve": 0.034,
    "generation": 0
  }
}
```

</details>

---
