# diagnose repo level cwm v10

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_repo-level-cwm-v10_20260513T062823_result.json`
- **Structured JSON:** [`7d2d73258a242c1b95bb.json`](../../sessions/7d/7d2d73258a242c1b95bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整诊断结果：

**Summary**:
- 进程 PID 105205 已死，EXIT_CODE=1，日志中**零 Traceback、零 Error**
- 日志在第 16 次 eval（step 1800 后）的 1281/9335 处突然截断
- **前 15 次 eval（step 300-1700）全部正常完成**，每次 ~730s
- CPU RAM 充足（754GB total, 25GB used）— 排除 CPU OOM
- 磁盘 43% 使用 — 排除磁盘满
- checkpoint-400（best）存在
- GPU 2 当前被新进程 123230（eval_repo_cwm.py on checkpoint-400）占用

**根因**: 15 次 eval 正常 → 第 16 次 crash = 累积性 CUDA 显存泄漏/碎片化。`compute_loss` 每次 eval step 生成完整 logits 张量（~600MB），经过 1600+ 训练步 + 15 轮完整 eval（15 × 9335 步），显存碎片化到无法分配连续块。进程被 SIGKILL，无 Python traceback。

**过拟合趋势**:
| Step | eval_loss | 
|------|-----------|
| 300 | 0.3228 |
| **400** | **0.2975 (best)** |
| 500 | 0.3294 |
| ... | 持续上升 |
| 1700 | 0.3699 |
| 1800 | CRASHED |

```json
{"root_cause":"CUDA OOM from GPU memory fragmentation after 15 eval cycles — process killed without Python traceback at eval step 1281/9335 during 16th eval (step ~1800). No Traceback/Error in log, EXIT_CODE=1 = external SIGKILL.","error_type":"resource","fix_steps":["不需要继续训练——best checkpoint 在 step 400 (eval_loss=0.2975)，之后持续过拟合到 0.37","当前已有进程 PID 123230 在用 checkpoint-400 跑 eval_repo_cwm.py，等它完成","下次训练添加 eval_accumulation_steps=50 到 TrainingArguments 防止 eval 阶段显存累积","添加 EarlyStoppingCallback(early_stopping_patience=3) 避免无效训练","降低 dataloader_num_workers 从 4 到 2"],"can_auto_fix":false,"best_checkpoint_exists":true,"checkpoint_list":["checkpoint-400","checkpoint-1600","checkpoint-1700"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "CUDA OOM from GPU memory fragmentation after 15 eval cycles — process killed without Python traceback at eval step 1281/9335 during 16th eval (step ~1800). No Traceback/Error in log, EXIT_CODE=1 = external SIGKILL.",
    "error_type": "resource",
    "fix_steps": [
      "不需要继续训练——best checkpoint 在 step 400 (eval_loss=0.2975)，之后持续过拟合到 0.37",
      "当前已有进程 PID 123230 在用 checkpoint-400 跑 eval_repo_cwm.py，等它完成",
      "下次训练添加 eval_accumulation_steps=50 到 TrainingArguments 防止 eval 阶段显存累积",
      "添加 EarlyStoppingCallback(early_stopping_patience=3) 避免无效训练",
      "降低 dataloader_num_workers 从 4 到 2"
    ],
    "can_auto_fix": false,
    "best_checkpoint_exists": true,
    "checkpoint_list": [
      "checkpoint-400",
      "checkpoint-1600",
      "checkpoint-1700"
    ]
  }
}
```

</details>

---
