# code gemma2 batchsize fix v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma2-batchsize-fix-v2_20260519T165056_result.json`
- **Structured JSON:** [`3fc102c2e0ae4ed0d663.json`](../../sessions/3f/3fc102c2e0ae4ed0d663.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本均已修改完成：

- `run_gemma2_s123.sh` (L24): `--batch-size 2 --grad-accum 8`
- `sft_gemma2_s0_sweep.sh` (L25): `--batch-size 2 --grad-accum 8`

effective batch size 保持 2×8=16 不变。d000 (PID 180155) 已在运行中不受影响，后续 dosage 会使用新参数。

---
