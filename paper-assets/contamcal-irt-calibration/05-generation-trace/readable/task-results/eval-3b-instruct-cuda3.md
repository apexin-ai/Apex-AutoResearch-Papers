# eval 3B instruct cuda3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_3B_instruct_cuda3_20260516T075138_result.json`
- **Structured JSON:** [`8a1e9c9d14f325fa4567.json`](../../sessions/8a/8a1e9c9d14f325fa4567.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交并注册。总结：

- **Job**: `exp_001_eval_3B_instruct_aligned_para` (PID 730671)
- **GPU**: cuda:3 @ cqa1-21977
- **状态**: RUNNING，模型下载中 (~5.7GB via ModelScope，约 20-30 min)
- **流程**: 下载 Qwen2.5-3B-Instruct → aligned eval (4 benchmarks) → para_aligned eval (4 benchmarks)
- **输出**:
  - `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B-Instruct_aligned/`
  - `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B-Instruct_para_aligned/`
- **预计耗时**: 下载 ~30min + aligned eval ~2-3h + para_aligned eval ~2-3h ≈ 5-6h 总计
- **日志**: `~/runs/contamcal-irt-calibration/exp_001_eval_3B_instruct_aligned_para.log`

---
