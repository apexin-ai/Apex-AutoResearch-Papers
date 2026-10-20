# analysis training status check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_training-status-check_20260514T164557_result.json`
- **Structured JSON:** [`b16b1e4fcf263f03d364.json`](../../sessions/b1/b16b1e4fcf263f03d364.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态检查 (2026-05-15 ~00:50 UTC)

### plan018-additive-random-b01-s43-r2
- 进程: **已完成** (PID 858386 不存在)
- 当前 step: **500/500 ✓ 训练完成**
- prove_rate (final): 0.5925
- ISR (final mean): 0.099
- 最后几步 (498-499): PR=1.000, ISR=0.039-0.093; step 500: PR=0.625, ISR=0.018
- 磁盘: 71G free (72%)
- 模型已保存，EXIT_CODE=0，耗时 78 min
- 状态: **正常完成**

### plan006-prolog-sta-s43
- 进程: **存活** (PID 901135, uptime 9m35s)
- 当前 step: **46/500** (9%)
- prove_rate (recent): 0.000-0.375，波动大，多数 step 在 0.25 左右
- ISR (recent): 0.000-0.115，低
- parse_rate: 1.000
- GPU 1: 90% util, 80073/97887 MiB
- ETA: ~1h42m
- 是否出现早期饱和: **否** — step 46 时 PR 仍在 0.0-0.375 波动，远未饱和，与 s42 的 step ~100 饱和模式不同（目前太早下结论）
- 状态: **正常运行**

**注意**: plan018 已完成，GPU 0 现在空闲 (0% util, 0 MiB)，可调度新任务。

---
