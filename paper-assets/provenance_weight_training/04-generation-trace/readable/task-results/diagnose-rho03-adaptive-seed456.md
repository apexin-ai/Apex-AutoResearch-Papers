# diagnose rho03 adaptive seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_rho03_adaptive_seed456_20260523T032401_result.json`
- **Structured JSON:** [`d79d043565fc04c39cc4.json`](../../sessions/d7/d79d043565fc04c39cc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

- 目录存在，但**没有任何 checkpoint 子目录**，只有 `config.json` 和 `step_metrics.jsonl`
- 训练跑到 step 999（共 4000 行 metrics，每步约 4 条记录），在 step 1000 尝试保存 checkpoint 时失败
- 磁盘剩余 99GB，不是空间问题
- 总训练目标 6103 steps，完成约 16%

结论：checkpoint 从未成功写入，可能是保存逻辑有 bug（例如 `save_steps=1000` 但目录创建或写入失败）。没有任何可恢复的 checkpoint。

```json
{"checkpoint_exists": false, "valid_checkpoints": [], "disk_free_gb": 99, "recommendation": "restart_from_scratch"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "checkpoint_exists": false,
    "valid_checkpoints": [],
    "disk_free_gb": 99,
    "recommendation": "restart_from_scratch"
  }
}
```

</details>

---
