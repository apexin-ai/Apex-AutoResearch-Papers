# diagnose a1 lora object pudding s0

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_a1_lora_object_pudding_s0_20260522T135429_result.json`
- **Structured JSON:** [`ab1c93c304afdfc3a6d2.json`](../../sessions/ab/ab1c93c304afdfc3a6d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

```json
{
  "actually_completed": true,
  "steps_completed": 30000,
  "best_loss": 0.01326,
  "final_loss": 0.0184,
  "phase2_lora_active": false,
  "root_cause": "M016 false positive",
  "checkpoints_found": ["29999", "30000", "best"],
  "error_type": "false_positive"
}
```

**详细发现**：

- **训练完整完成** 30000/30000 steps，总耗时 ~33h，~3.96s/step，进程已正常退出
- **无任何错误** — grep error/traceback/oom/killed 全部零匹配
- **Checkpoints 完整** — `29999/`、`30000/`、`best/` 三个目录均存在，`model.safetensors` 约 6.7GB，时间戳 May 22 21:44-21:45
- **best_loss = 0.01326**（step 29999）
- **确认 M016 误报** — WANDB_MODE=disabled 导致 cron 无法读取 W&B metrics，误判为 failed

**LoRA 警告**：日志末尾的诊断输出显示 steps 0-90 期间 `LoRA params: 0`，整个训练过程未检测到 Phase 2 / unfreeze / LoRA inject 相关日志。仅有 658,948 个可训练参数（均非 LoRA）。如果此实验预期启用 LoRA，这可能是一个问题——但不影响"训练已完成"的判定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "actually_completed": true,
    "steps_completed": 30000,
    "best_loss": 0.01326,
    "final_loss": 0.0184,
    "phase2_lora_active": false,
    "root_cause": "M016 false positive",
    "checkpoints_found": [
      "29999",
      "30000",
      "best"
    ],
    "error_type": "false_positive"
  }
}
```

</details>

---
