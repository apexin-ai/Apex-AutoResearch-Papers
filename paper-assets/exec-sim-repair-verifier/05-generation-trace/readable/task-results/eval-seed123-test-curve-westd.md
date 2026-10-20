# eval seed123 test curve westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_seed123-test-curve-westd_20260515T094140_result.json`
- **Structured JSON:** [`5fdb4c4706a0bbf3b729.json`](../../sessions/5f/5fdb4c4706a0bbf3b729.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval job 已提交：

| 实验 | GPU | PID | 日志 |
|------|-----|-----|------|
| `cls8b-seed123-ckpt6200-test8192-eval` | cuda:0 | 353094 | `~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6200-test8192-eval.log` |
| `cls8b-seed123-ckpt6400-test8192-eval` | cuda:3 | 353235 | `~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6400-test8192-eval.log` |

结果将输出到各 checkpoint 目录下的 `eval_test8192/` 子目录。cron 会监控完成状态。

---
