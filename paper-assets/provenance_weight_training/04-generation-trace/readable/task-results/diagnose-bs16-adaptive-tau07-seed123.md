# diagnose bs16 adaptive tau07 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bs16_adaptive_tau07_seed123_20260521T185432_result.json`
- **Structured JSON:** [`7d581463cdd337ea503b.json`](../../sessions/7d/7d581463cdd337ea503b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理释放了大量空间（可能存在已删除但进程仍持有句柄的隐藏文件）。103G 可用，远超所需 15G。

```json
{
  "disk_before": "100% used, 308K available",
  "cleaned_dirs": [
    "bs16_adaptive_tau07_seed123/checkpoint-500",
    "dr_epoch_matched_indep_lr_seed42/checkpoint-2000",
    "dr_epoch_matched_indep_lr_seed42/checkpoint-2500",
    "dr_epoch_matched_indep_lr_seed42/checkpoint-2533"
  ],
  "cleaned_size": "~102G (du 预估 12.8G，实际释放更多，可能有已删除未释放的孤立 inode)",
  "disk_after": "59% used, 103G available",
  "enough_for_retry": true,
  "notes": "bs16_adaptive_tau07_seed123 的 checkpoint-500 不完整（缺 scheduler.pt/trainer_state.json，optimizer.pt 可能截断）已清除；dr_epoch_matched_indep_lr_seed42 的 3 个 checkpoint 已清除，保留 final/ 和 eval_results/。103G 远超重试所需的 ~15G。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "disk_before": "100% used, 308K available",
    "cleaned_dirs": [
      "bs16_adaptive_tau07_seed123/checkpoint-500",
      "dr_epoch_matched_indep_lr_seed42/checkpoint-2000",
      "dr_epoch_matched_indep_lr_seed42/checkpoint-2500",
      "dr_epoch_matched_indep_lr_seed42/checkpoint-2533"
    ],
    "cleaned_size": "~102G (du 预估 12.8G，实际释放更多，可能有已删除未释放的孤立 inode)",
    "disk_after": "59% used, 103G available",
    "enough_for_retry": true,
    "notes": "bs16_adaptive_tau07_seed123 的 checkpoint-500 不完整（缺 scheduler.pt/trainer_state.json，optimizer.pt 可能截断）已清除；dr_epoch_matched_indep_lr_seed42 的 3 个 checkpoint 已清除，保留 final/ 和 eval_results/。103G 远超重试所需的 ~15G。"
  }
}
```

</details>

---
