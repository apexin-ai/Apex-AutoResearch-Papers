# analyze d111 4b sft s42 reeval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d111_4b_sft_s42_reeval_20260519T035307_result.json`
- **Structured JSON:** [`a4366e7b49a04247696e.json`](../../sessions/a4/a4366e7b49a04247696e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。下面是结果分析：

D076 协议下 s42 的 ign_f1 = **0.3974**，与之前三次结果中的最低值完全一致（0.4106 / 0.4036 / 0.3974）。这说明之前 0.3974 那次就是用了与 D076 等价的协议，而 0.4106 和 0.4036 可能有协议差异（如 batch_size、max_new_tokens、quantize 设置不同）。

**3-seed 对比（D076 协议，ign_f1）：**

| Seed | ign_f1 |
|------|--------|
| s42  | 0.3974 |
| s43  | 0.4365 |
| s44  | 0.4734 |
| **Mean** | **0.4358** |
| **Std**  | **0.0310** |

```json
{
  "ign_f1": 0.3974,
  "rel_f1": 0.4049,
  "evi_f1": 0.7986,
  "evi_f1_joint": 0.3147,
  "edcr": 0.6982,
  "three_seed_mean": 0.4358,
  "three_seed_std": 0.0310,
  "comparison_note": "D076 reeval confirms s42=0.3974, matching the lowest of the 3 prior inconsistent results exactly. s42 is the weakest seed — 7.6pp below s44, 3.9pp below s43. 3-seed std=0.031 indicates moderate variance across seeds."
}
```

s42 是最弱的 seed，与 s44 差距 7.6pp。3-seed 标准差 0.031 偏大，说明 4B SFT 模型的 seed sensitivity 较高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "ign_f1": 0.3974,
    "rel_f1": 0.4049,
    "evi_f1": 0.7986,
    "evi_f1_joint": 0.3147,
    "edcr": 0.6982,
    "three_seed_mean": 0.4358,
    "three_seed_std": 0.031,
    "comparison_note": "D076 reeval confirms s42=0.3974, matching the lowest of the 3 prior inconsistent results exactly. s42 is the weakest seed — 7.6pp below s44, 3.9pp below s43. 3-seed std=0.031 indicates moderate variance across seeds."
  }
}
```

</details>

---
