# diagnose eval obs only object norm01 seed74

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm01-seed74_20260521T031336_result.json`
- **Structured JSON:** [`837c613b3679858148fe.json`](../../sessions/83/837c613b3679858148fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**两个实验都没有失败。** 它们正常跑完了全部 10 tasks × 10 rollouts，并保存了完整的 JSON 结果文件。

### 实验 1: eval-obs-only-object-norm01-seed74
- **状态**: 正常完成，return_code=0
- **结果**: overall_success_rate = **13%** (13/100)
- **JSON 文件**: `/root/acr-vla-conformal-refinement/logs/norm01_seed74.json` ✓ 完整

### 实验 2: eval-obs-only-object-norm01-seed71
- **状态**: 正常完成，return_code=0
- **结果**: overall_success_rate = **16%** (16/100)
- **JSON 文件**: `/root/acr-vla-conformal-refinement/logs/norm01_seed71.json` ✓ 完整

### 根因

实验本身没有崩溃/OOM/异常。"Process exited without valid W&B metrics" 说明问题出在 **W&B 上传环节**——评估脚本没有将结果 log 到 W&B（脚本里可能根本没有 `wandb.log()` 调用，或者 wandb 未初始化），导致监控系统认为实验失败。

**结果数据完好可恢复**，不需要重跑。只需从 JSON 文件读取 `overall_success_rate` 即可。

---
