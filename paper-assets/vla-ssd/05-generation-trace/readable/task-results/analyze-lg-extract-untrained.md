# analyze lg extract untrained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_lg_extract_untrained_20260515T174225_result.json`
- **Structured JSON:** [`246dcbd2e61f3f8e732d.json`](../../sessions/24/246dcbd2e61f3f8e732d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。10/10 tasks 成功保存，无 ERROR，结构完全符合预期。

```json
{
  "tasks_completed": "10/10",
  "extraction_time_min": 53.1,
  "feature_dim": 4096,
  "num_layers": 33,
  "dtype": "float16",
  "demos_per_task": 50,
  "exit_code": 0,
  "feature_keys": ["image_mean", "last_preaction"],
  "note": "untrained OpenVLA-7B on LIBERO-Goal, retry #1 (fixed local_files_only). Per-demo shape=(T, 33, 4096). Total output ~25GB."
}
```

与 `lg_extract_trained` 完全对齐：相同的 10 个 task、50 demos/task、4096 dim、33 layers、float16，耗时几乎一致（53.1 vs 53.4 min）。日志开头有 HuggingFace 连接失败的 traceback（retry #0 的残留），但最终运行成功，无实际 ERROR。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "tasks_completed": "10/10",
    "extraction_time_min": 53.1,
    "feature_dim": 4096,
    "num_layers": 33,
    "dtype": "float16",
    "demos_per_task": 50,
    "exit_code": 0,
    "feature_keys": [
      "image_mean",
      "last_preaction"
    ],
    "note": "untrained OpenVLA-7B on LIBERO-Goal, retry #1 (fixed local_files_only). Per-demo shape=(T, 33, 4096). Total output ~25GB."
  }
}
```

</details>

---
