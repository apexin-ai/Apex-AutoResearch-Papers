# gpu mistral download speed check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_mistral_download_speed_check_20260514T213030_result.json`
- **Structured JSON:** [`cc3383565380e11b5258.json`](../../sessions/cc/cc3383565380e11b5258.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三次采样结果：

| 采样 | 大小 (bytes) | 增量 | 估算速度 |
|------|-------------|------|---------|
| #1 | 10,205,957,326 | — | — |
| #2 | 10,489,072,846 | 283 MB | ~8.5 MB/s |
| #3 | 11,107,732,686 | 619 MB | ~15+ MB/s |

**结论：下载速度 8.5–15+ MB/s，远超 5MB/s 阈值，无需切 ModelScope。**

- 当前已下载：~10.3 GB
- Mistral-7B-v0.3 总大小：~14.7 GB（3 个 safetensors shard）
- 剩余：~4.4 GB
- 预计完成时间：约 5–8 分钟

**background task PID=262493 still running, 需要后续 Worker 轮询验证。** 下载完成后需执行 Step 3 验证（3 shard 完整性 + safetensor 加载 + transformers 加载）和 Step 4 提交实验（`mistral_hires_bf16_2bitonly_v3` → `submit_training_job` on cuda:1）。

---
