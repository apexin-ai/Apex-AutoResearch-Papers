# ops emergency disk cleanup

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency_disk_cleanup_20260523T092620_result.json`
- **Structured JSON:** [`6573374211a8e6ae954f.json`](../../sessions/65/6573374211a8e6ae954f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

- **释放空间**: 30G → 22G used，**可用 9.0G**（71% 使用率）
- **K=16 s123 (PID 128425)**: 仍在运行
- 清理内容：K=2/K=4/K=8/K=16 中间 step checkpoint + K=16 s456 整目录 + pip cache (103MB)，共释放约 8GB
- 所有 final checkpoint (`predictor_perlayer_kl_k4.pt`) 均保留完好

9GB 剩余空间足够 step_1000 checkpoint (~435MB) 保存。

---
