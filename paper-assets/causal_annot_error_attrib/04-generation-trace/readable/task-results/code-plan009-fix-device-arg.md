# code plan009 fix device arg

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan009-fix-device-arg_20260520T184400_result.json`
- **Structured JSON:** [`d6a761f6e939ecf41985.json`](../../sessions/d6/d6a761f6e939ecf41985.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Running successfully on `cuda:0`.

**修复内容：**
- 在 argparse 添加了 `--device` 参数（默认 `cuda:0`）
- `parse_args()` 后用 `args.device` 覆盖全局 `DEVICE`

**新 PID：`497866`**，日志在 `artifacts/plan009/plan009_run.log`，已在正常产出数据。

---
