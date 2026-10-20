# verify md5sum best dir

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_md5sum-best-dir_20260515T184723_result.json`
- **Structured JSON:** [`34d0f4cf77909f83671e.json`](../../sessions/34/34d0f4cf77909f83671e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**`best/` 既不是 checkpoint-1000 也不是 checkpoint-6633。**

`trainer_state.json` 明确记录：

```
best_global_step: 200
best_model_checkpoint: /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200
best_metric: 0.07963339239358902 (eval_loss at epoch ~0.09)
```

`best/` 是 Trainer 在训练结束时（`load_best_model_at_end=True`）从**旧训练 run** `checkpoints_repo_cls_8b_conda/checkpoint-200` 加载并保存的副本。

时间线佐证：
| 目录 | 创建时间 |
|------|---------|
| checkpoint-1000 | 2026-05-15 07:15:49 |
| checkpoint-6633 | 2026-05-16 02:33:55.678 |
| **best/** | **2026-05-16 02:33:55.930** (+252ms after 6633) |

checkpoint-6633（最后一步）先保存，252ms 后 Trainer 保存了 best model——内容来自 step 200（旧 run）。

**注意**：`ssh_read_only` 白名单不允许 `md5sum`，无法做字节级对比。如需 100% 确认 `best/` 与 `checkpoint-200` 二进制一致，需用 `ssh_execute` 执行 `md5sum`。

---
