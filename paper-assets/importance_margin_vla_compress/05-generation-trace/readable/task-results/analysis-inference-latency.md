# analysis inference latency

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_inference_latency_20260518T065536_result.json`
- **Structured JSON:** [`9c99daa740845a09bcc6.json`](../../sessions/9c/9c99daa740845a09bcc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

| Config | Vision Tokens | Mean Latency | Std | Speedup |
|--------|--------------|-------------|-----|---------|
| Baseline | 128 | 164.33 ms | 3.04 ms | 1.00x |
| Smart Compress M=32 | 32 | 154.78 ms | 5.36 ms | **1.06x** |
| Smart Compress M=64 | 64 | 156.16 ms | 6.37 ms | **1.05x** |

加速幅度不大（~6%），原因是 SmolVLA 的推理瓶颈在 iterative denoising loop（多步 suffix forward pass + KV cache），而 vision token 压缩只减少了 prefix computation（KV cache 填充阶段），这部分在总推理时间中占比较小。压缩器本身增加了 ~22M 参数，但因为 prefix 被缓存，这个开销不影响后续 denoising 步骤。

结果已保存到 `eval_results/inference_latency_comparison.json`，registry 状态已更新为 DONE。

---
