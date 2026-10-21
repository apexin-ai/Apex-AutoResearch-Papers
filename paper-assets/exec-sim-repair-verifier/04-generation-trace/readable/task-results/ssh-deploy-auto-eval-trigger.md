# ssh deploy auto eval trigger

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-auto-eval-trigger_20260522T224059_result.json`
- **Structured JSON:** [`24ee97f850941988542e.json`](../../sessions/24/24ee97f850941988542e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

| 项目 | tmux session | 监控 PID | Eval GPU | 状态 |
|------|-------------|----------|----------|------|
| CWM 14B | `auto-eval-cwm14b` | 211098 (已跑 2h15m) | GPU 1 | 轮询监控中 |
| CLS 14B v2 | `auto-eval-cls14b` | 215642 (已跑 1h04m) | GPU 3 | 轮询监控中 |

两个监控脚本已在 tmux 中运行，每 60 秒检查一次训练进程。训练结束后会自动查找 best checkpoint 并启动 eval。日志分别在 `/tmp/auto_eval_cwm14b.log` 和 `/tmp/auto_eval_cls14b.log`。

---
