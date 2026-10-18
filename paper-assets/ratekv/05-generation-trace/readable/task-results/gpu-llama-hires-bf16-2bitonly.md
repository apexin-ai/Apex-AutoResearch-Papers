# gpu llama hires bf16 2bitonly

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_llama_hires_bf16_2bitonly_20260514T201839_result.json`
- **Structured JSON:** [`e5742c275742b075a6df.json`](../../sessions/e5/e5742c275742b075a6df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正在并行进行，4 个 safetensors 分片 + original pth，总速度约 15-20MB/s 聚合。

**当前状态：**
- 模型下载进行中 (PID=257255)，预计 25-30 分钟完成 safetensors（约 15GB）
- original/consolidated.00.pth (15GB) 更久但不影响实验
- 脚本 `run_llama_hires_bf16_2bitonly.py` 已就绪
- cuda:0 空闲

**下一步：** 下载完成后需要重新启动 profiling 脚本。模型最终路径应为 `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B`（ModelScope 下载惯例，点号变下划线）。

需要我过几分钟后轮询下载状态并自动启动 profiling 吗？还是你稍后手动触发？

---
