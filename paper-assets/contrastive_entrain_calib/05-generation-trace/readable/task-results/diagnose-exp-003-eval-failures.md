# diagnose exp 003 eval failures

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-003-eval-failures_20260521T072341_result.json`
- **Structured JSON:** [`04c7efdfa8fa101db06d.json`](../../sessions/04/04c7efdfa8fa101db06d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已注册为 `art_20260521_983af6`。

**摘要**：

- **根因**：tmux 服务器在 07:19:24 UTC 崩溃，导致所有 session 收到 SIGHUP。不是服务器重启、不是 OOM、不是 GPU 故障。Docker 容器无系统日志，tmux 崩溃的精确触发器无法追溯。
- **当前状态**：自动恢复系统已在 3 分钟内重启全部 4 个实验，均为 RUNNING 状态，4 GPU 全部在用（48-50% util）。ckpt5000-v2 已处理到 20/362。
- **无需人工干预**，无脏数据风险（旧 run 未产生结果文件）。
- 如果 tmux 崩溃频繁复现，建议改用 `nohup` 作为默认后端。

---
