# analysis eval smart compress m96

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_smart_compress_m96_20260518T050941_result.json`
- **Structured JSON:** [`9b6d3d0f52f32c23456e.json`](../../sessions/9b/9b6d3d0f52f32c23456e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。status=DONE, conclusion=success, checkpoint_path 和 log_path 已在 spec 中设置。

**汇总：**

| 指标 | 值 |
|------|-----|
| **overall_sr** | 52.6% |
| **total_episodes** | 500 |
| **total_successes** | 263 |
| **95% Wilson CI** | [48.2%, 56.9%] |
| **运行时间** | ~55 min (wall clock 3526s) |
| **conclusion** | success |

**per_task_sr:**
```python
{"alphabet_soup": 40, "cream_cheese": 52, "salad_dressing": 56, "bbq_sauce": 40, 
 "ketchup": 26, "tomato_sauce": 50, "butter": 72, "milk": 62, 
 "chocolate_pudding": 86, "orange_juice": 42}
```

**对比：**
| 配置 | overall_sr |
|------|-----------|
| SmolVLA baseline (no compress) | 44.8% |
| **M=96 (25% compress)** | **52.6%** |
| M=64 (50% compress) | 61.6% |
| M=32 (75% compress) | 61.6% |

假设被否定：M=96 并非上界，反而是三个压缩配置中最差的。压缩程度与性能之间不是单调关系，M=32 和 M=64 都优于 M=96 约 9 个百分点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "alphabet_soup": 40,
    "cream_cheese": 52,
    "salad_dressing": 56,
    "bbq_sauce": 40,
    "ketchup": 26,
    "tomato_sauce": 50,
    "butter": 72,
    "milk": 62,
    "chocolate_pudding": 86,
    "orange_juice": 42
  }
}
```

</details>

---
