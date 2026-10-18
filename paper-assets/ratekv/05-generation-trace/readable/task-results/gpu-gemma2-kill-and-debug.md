# gpu gemma2 kill and debug

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_gemma2_kill_and_debug_20260514T160301_result.json`
- **Structured JSON:** [`8dc41cff7353c655d3be.json`](../../sessions/8d/8dc41cff7353c655d3be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复验证成功。所有 head 现在都有非零 delta：

| Head | bf16 (bug) | fp32 (fix) |
|---|---|---|
| L0H0 @2bit | 0.000000 | **0.001494** |
| L0H1 @2bit | 0.148030 | **0.141953** |
| L5H3 @2bit | 0.000000 | **0.015703** |
| L21H0 @2bit | 0.000000 | **0.066817** |

## 总结

**Kill 状态**：Gemma-2 profiling 进程已不在运行（GPU 0MiB），tmux session 已 kill。

**Bug 位置**：`run_gemma2_full_pipeline.py` 的 `Gemma2Profiler._compute_ppl()` 第 180 行和 `evaluate_perplexity()` 第 270 行。

**根因**：`F.cross_entropy(bfloat16_logits, ...)` 返回 **bfloat16 标量**。总 loss ~18300 处 bfloat16 精度为 128 ULP，单 head 量化引起的 loss 变化（1-60）远小于 128，被精度截断为零。Qwen profiler 有同样的潜在 bug 但因 GQA ratio=7（影响 25% Q heads）效果更大不触发。

**修复**：两处 `shift_logits.view(...)` → `shift_logits.float().view(...)`，已应用到本地和服务器。诊断报告已写入 `/root/ratekv/gemma2_ppl_debug_report.txt`。

---
