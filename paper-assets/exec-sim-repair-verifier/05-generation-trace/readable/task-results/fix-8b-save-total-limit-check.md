# fix 8b save total limit check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_8b-save-total-limit-check_20260514T105744_result.json`
- **Structured JSON:** [`0e51528e0ebaaba9d24b.json`](../../sessions/0e/0e51528e0ebaaba9d24b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### CLS 8B seed123
- **save_total_limit: 5**（已经足够）
- save_steps: 200, eval_steps: 200
- 现有 checkpoint: 200, 800, 1000, 1200, 1400
- best_model_checkpoint: checkpoint-200 (best eval_loss: 0.0862)
- global_step: 1400
- ckpt-400 和 ckpt-600 已被删除（save_total_limit=5 在累积到 >5 个时删了最旧的非 best checkpoint）

### CWM 8B
- **save_total_limit: 5**（没问题）
- save_steps: 100, eval_steps: 100
- 现有 checkpoint: 300, 400, 500, 600, 700

### CLS 8B seed42
- 现有 checkpoint: 200, 400, 600（训练已结束，3 个 checkpoint）

**结论**：两个正在运行的训练（CLS 8B seed123 和 CWM 8B）的 save_total_limit 都已经是 5，无需修改。

seed123 的 best checkpoint 是 ckpt-200（eval_loss=0.0862），目前还保留着。由于 load_best_model_at_end=True 且 metric_for_best_model=eval_loss，Trainer 删除 checkpoint 时会保护 best checkpoint，所以 ckpt-200 不会被删除。当前无需额外备份操作。

---
