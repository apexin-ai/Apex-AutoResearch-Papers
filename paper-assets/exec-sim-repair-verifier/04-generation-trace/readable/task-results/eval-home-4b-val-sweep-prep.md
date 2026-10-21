# eval home 4b val sweep prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_home-4b-val-sweep-prep_20260515T014541_result.json`
- **Structured JSON:** [`5bde5bf247d99511eae6.json`](../../sessions/5b/5bde5bf247d99511eae6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务已提交。总结：

**4B CLS v5 Val Sweep 状态：**

| Checkpoint | Val 状态 | Accuracy |
|---|---|---|
| ckpt-600 | DONE | 82.82% |
| ckpt-4000 | DONE | 89.84% |
| ckpt-4400 | RUNNING (1536/9335, ~60min left) | - |
| ckpt-4600 | QUEUED (等 4400 完) | - |
| ckpt-4200 | QUEUED (等 4600 完) | - |

**执行方式：** tmux 会话 `cls4b_val_sweep`，脚本等 ckpt-4400 PID 完成后自动依次跑 ckpt-4600 → ckpt-4200。日志在 `logs/cls4b_val_sweep.log`。

**之前 sweep 失败原因：** `run_v5_val5120_sweep.sh` 用了 `python` 而非 `python3`。

**已确认：** `max_new_tokens=512` 硬编码在 `eval_repo_cls.py:201`，所有 eval 自动满足 D063 约束。

预计全部完成时间：~3 小时（每个 checkpoint ~1 小时）。

---
