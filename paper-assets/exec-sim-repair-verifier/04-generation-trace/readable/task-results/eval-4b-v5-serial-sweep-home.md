# eval 4b v5 serial sweep home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_4b-v5-serial-sweep-home_20260514T223225_result.json`
- **Structured JSON:** [`ff2a95c790da31534775.json`](../../sessions/ff/ff2a95c790da31534775.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Sweep 脚本已经部署好并正在运行。**

当前状态：
- **PID 3179262**: v5 ckpt-600 val@5120 eval 进行中（GPU 100%, 31.7GB 显存）
- **PID 3180425**: `run_v5_val5120_sweep.sh` 正在等待 ckpt-600 完成（每 30s 轮询）
- 脚本逻辑：ckpt-600 完成后，依次跑 ckpt-4000 → 4200 → 4400 → 4600 的 val@5120 eval
- 已有结果的 checkpoint 会自动跳过（检查 `eval_repo_cls.json` 是否存在）
- 日志输出到 `results/v5_val5120_sweep.log`

不需要额外操作，sweep 已在排队等待中。

---
