# diagnose adaptive tau08 scratch seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_adaptive_tau08_scratch_seed42_20260521T012015_result.json`
- **Structured JSON:** [`b6be3c1cbf6d88d368a0.json`](../../sessions/b6/b6be3c1cbf6d88d368a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 memory.md。总结：

**训练进度**：step 4000/6103（65.5%，~131M/200M tokens）。日志尾部 `5974/8477` 是 eval 循环，非训练步。

**根因**：每次 eval 耗时 43 分钟，7 次完整 eval 占总时间 42%（~5h），导致 13h 墙钟时间触发 timeout。

**Checkpoint**：`checkpoint-3500` 完整可用（含 model.safetensors 1.1GB + trainer_state.json）。

**Eval 趋势**：eval_loss 从 3.128→3.040 持续下降，正常。

**Resume 方案**：
- 从 checkpoint-3500 恢复，剩余 2603 步
- 如保持 eval 每 500 步：需 ~5.2h，timeout 设 8h
- 如改为 eval 每 1000 步：需 ~3.2h，节省 ~2h eval 时间

---
