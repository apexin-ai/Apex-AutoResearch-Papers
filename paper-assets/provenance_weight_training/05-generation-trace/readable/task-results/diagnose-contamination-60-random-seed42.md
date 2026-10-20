# diagnose contamination 60 random seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_contamination_60_random_seed42_20260518T085849_result.json`
- **Structured JSON:** [`f566f080bd3e1986cde9.json`](../../sessions/f5/f566f080bd3e1986cde9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```json
{"actual_status": "completed", "last_step": 6103, "expected_total_steps": 6103, "checkpoint_path": "/root/autodl-tmp/output/models/contamination_60_random_seed42/final", "log_path": "/root/autodl-tmp/output/models/contamination_60_random_seed42/train_resume.log", "root_cause": "日志未写入 ~/runs/ 监控路径，cron 在预期路径找不到 sentinel 文件也无 W&B run，因此误判为 dead process", "evidence": "进度条 6103/6103 (100%)，日志末行 'Training complete. Model saved to .../final'，final/ 目录含完整 model.safetensors (1.19GB) + tokenizer，训练耗时 10719s (~2h58m)，另有 eval_holdout_final.log 表明 eval 已触发"}
```

关键发现：
- 训练 **已完成**，6103/6103 steps，模型已保存到 `final/` 目录
- ROADMAP 标注正确（"已完成，误标failed"）
- 被误标原因：日志写入了 output 目录而非 `~/runs/provenance_weight_training/contamination_60_random_seed42.log`，cron 在预期路径找不到 sentinel 和 W&B run

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "actual_status": "completed",
    "last_step": 6103,
    "expected_total_steps": 6103,
    "checkpoint_path": "/root/autodl-tmp/output/models/contamination_60_random_seed42/final",
    "log_path": "/root/autodl-tmp/output/models/contamination_60_random_seed42/train_resume.log",
    "root_cause": "日志未写入 ~/runs/ 监控路径，cron 在预期路径找不到 sentinel 文件也无 W&B run，因此误判为 dead process",
    "evidence": "进度条 6103/6103 (100%)，日志末行 'Training complete. Model saved to .../final'，final/ 目录含完整 model.safetensors (1.19GB) + tokenizer，训练耗时 10719s (~2h58m)，另有 eval_holdout_final.log 表明 eval 已触发"
  }
}
```

</details>

---
