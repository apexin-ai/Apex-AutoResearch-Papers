# diagnose eval openvla random k085 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_random_k085_object_seed42_20260526T192153_result.json`
- **Structured JSON:** [`50f9a6593854da30f43f.json`](../../sessions/50/50f9a6593854da30f43f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**没有失败**，已成功完成。10 个 task 全部跑完，结果已保存。

```json
{"root_cause":"实验实际成功完成，无错误。Overall SR: 0.6040 (302/500)，结果已保存至 openvla_random_prune_k085_object_seed42.json","error_type":"infrastructure","fix_steps":["无需修复，实验已正常完成","进程死亡5次可能是监控误报或之前的重试，最终一次成功跑完","Wall clock 16717.8s 包含了前几次失败重试的时间"],"can_auto_fix":true,"partial_results":"有，完整结果：Overall SR=60.4% (302/500)，耗时267.1min，结果文件：/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k085_object_seed42.json"}
```

关键发现：实验最终成功，SR=60.4%（与 v2 的 61.4% 接近）。Wall clock 16717s 是因为前几次进程死亡重试累计的时间，最后一次完整运行耗时 267.1min（~4.5h）正常。无需任何修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "实验实际成功完成，无错误。Overall SR: 0.6040 (302/500)，结果已保存至 openvla_random_prune_k085_object_seed42.json",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复，实验已正常完成",
      "进程死亡5次可能是监控误报或之前的重试，最终一次成功跑完",
      "Wall clock 16717.8s 包含了前几次失败重试的时间"
    ],
    "can_auto_fix": true,
    "partial_results": "有，完整结果：Overall SR=60.4% (302/500)，耗时267.1min，结果文件：/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k085_object_seed42.json"
  }
}
```

</details>

---
