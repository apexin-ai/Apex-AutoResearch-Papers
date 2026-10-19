# diagnose mvp p2b contrastive training v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_p2b_contrastive_training_v2_20260512T151839_result.json`
- **Structured JSON:** [`cf9cc8c35a361ce7ae3c.json`](../../sessions/cf/cf9cc8c35a361ce7ae3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认 `choices=["random", "embedding_distance", "dataflow_aware"]`，修复后的值完全匹配。

```json
{
  "root_cause": "STRATEGIES 数组使用了缩写 'embedding' 和 'dataflow'，但 train.py --hard-negative-strategy 参数只接受 'embedding_distance' 和 'dataflow_aware'。argparse 报错 invalid choice: 'embedding'，exit code 2。",
  "error_type": "infrastructure",
  "fix_steps": [
    "将 run_p2b_all.sh 中 STRATEGIES=(random embedding dataflow) 改为 STRATEGIES=(random embedding_distance dataflow_aware)"
  ],
  "can_auto_fix": true,
  "fixed": true
}
```

需要重跑的 runs（6 个）：
- Run 4: `p2b_embedding_distance_s42`
- Run 5: `p2b_embedding_distance_s123`
- Run 6: `p2b_embedding_distance_s456`
- Run 7: `p2b_dataflow_aware_s42`
- Run 8: `p2b_dataflow_aware_s123`
- Run 9: `p2b_dataflow_aware_s456`

Random 策略的 3 个 seeds 已全部完成，脚本会自动跳过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "STRATEGIES 数组使用了缩写 'embedding' 和 'dataflow'，但 train.py --hard-negative-strategy 参数只接受 'embedding_distance' 和 'dataflow_aware'。argparse 报错 invalid choice: 'embedding'，exit code 2。",
    "error_type": "infrastructure",
    "fix_steps": [
      "将 run_p2b_all.sh 中 STRATEGIES=(random embedding dataflow) 改为 STRATEGIES=(random embedding_distance dataflow_aware)"
    ],
    "can_auto_fix": true,
    "fixed": true
  }
}
```

</details>

---
