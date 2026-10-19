# fix disk cleanup p2b

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_disk_cleanup_p2b_20260512T162138_result.json`
- **Structured JSON:** [`851e415914ab6bdd2737.json`](../../sessions/85/851e415914ab6bdd2737.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

```json
{
  "disk_before_gb": 14,
  "disk_after_gb": 91,
  "freed_gb": 77,
  "enough_for_5_runs": true,
  "cleaned_items": [
    "p2b_embedding_distance_s123/ (failed, 7.1G)",
    "p2b_embedding_distance_s456/ (failed, 196K)",
    "p2b_dataflow_aware_s42/ (failed, 196K)",
    "p2b_dataflow_aware_s123/ (failed, 196K)",
    "p2b_dataflow_aware_s456/ (failed, 196K)",
    "p2b_random_s42/checkpoint-{200,400,600} (intermediate, 17.4G)",
    "p2b_random_s123/checkpoint-{200,400,600} (intermediate, 17.4G)",
    "p2b_random_s456/checkpoint-{200,400,600} (intermediate, 17.4G)",
    "p2b_embedding_distance_s42/checkpoint-{200,400,600} (intermediate, 17.4G)"
  ]
}
```

保留的 4 个 `final/` checkpoint 各 5.8G，数据盘从 93% 降到 47%，91G 可用，远超 5 runs 所需的 6.5G。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "disk_before_gb": 14,
    "disk_after_gb": 91,
    "freed_gb": 77,
    "enough_for_5_runs": true,
    "cleaned_items": [
      "p2b_embedding_distance_s123/ (failed, 7.1G)",
      "p2b_embedding_distance_s456/ (failed, 196K)",
      "p2b_dataflow_aware_s42/ (failed, 196K)",
      "p2b_dataflow_aware_s123/ (failed, 196K)",
      "p2b_dataflow_aware_s456/ (failed, 196K)",
      "p2b_random_s42/checkpoint-{200,400,600} (intermediate, 17.4G)",
      "p2b_random_s123/checkpoint-{200,400,600} (intermediate, 17.4G)",
      "p2b_random_s456/checkpoint-{200,400,600} (intermediate, 17.4G)",
      "p2b_embedding_distance_s42/checkpoint-{200,400,600} (intermediate, 17.4G)"
    ]
  }
}
```

</details>

---
