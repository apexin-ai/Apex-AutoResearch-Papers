# launch mf5 depth baseline westd3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_mf5_depth_baseline_westd3_20260522T102129_result.json`
- **Structured JSON:** [`f8bcec5a35dd6b36ade5.json`](../../sessions/f8/f8bcec5a35dd6b36ade5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SFT 训练正常运行中。

```
PID: 36161
GPU 3 显存: 52365 MiB
Phase 1 (prune): 已完成（首次运行，19.12% sparsity）
Phase 2 (SFT) 启动: 成功
日志确认: 正常 — 180/1870 steps (~10%), ~1.65 it/s, 预计 SFT 总时间 ~19min
```

Pipeline 从 Phase 2 开始正常推进，`&&` 链已修正确保后续阶段串联执行。预计总时间 ~5h（SFT ~19min + GRPO ~1.5h + eval×2 ~3h）。

---
