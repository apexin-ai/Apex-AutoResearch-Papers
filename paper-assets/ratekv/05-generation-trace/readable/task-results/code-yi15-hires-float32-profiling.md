# code yi15 hires float32 profiling

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_yi15_hires_float32_profiling_20260514T185833_result.json`
- **Structured JSON:** [`a841dbf106433ceff2f3.json`](../../sessions/a8/a841dbf106433ceff2f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交运行：

- **exp_id**: `yi15_hires_float32_profiling`
- **PID**: 251122 (子进程 251127)
- **GPU**: cuda:1，占用 37GB（float32 模型 35.3GB）
- **配置**: 64seq × 2048tok, float32, batch_size=2, `calibration_hires.json`
- **日志**: `/root/ratekv/logs/yi15_hires_float32_profiling.log`

**ETA 估算**：
- 每次 `compute_ppl_batched` = 32 batches × ~15s = ~8min
- Baseline 1次 + 192 heads × 3 bitwidths = 577 次 PPL 计算
- 总计 577 × 8min ≈ **77h**

这远超预期。问题在于 float32 + 2048 seq_len + 64 samples 使得每次 forward pass 太慢。

参考 D048 Qwen 7B hires profiling（112 heads × 3 = 336 evals）约 60min，那里用的是 bfloat16。float32 在 Blackwell GPU 上的 FP32 throughput 大约是 BF16 的 1/2~1/4，加上 Yi 有 192 heads（1.7× more）。合理估算是 60min × 2~3× (float32 penalty) × 1.7 (heads ratio) ≈ **200-300min (3.5-5h)**。

但 64 samples vs 之前可能 16 samples 也是 4× 的差异。如果 D048 也用了 64 samples + 2048 seq_len，那约 **3-5h** 合理。

等 baseline PPL 跑完后根据第一个 head 的实际耗时修正 ETA。

---
