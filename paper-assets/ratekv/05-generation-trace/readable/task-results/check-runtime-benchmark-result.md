# check runtime benchmark result

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_runtime_benchmark_result_20260514T093352_result.json`
- **Structured JSON:** [`778a4af67b1a4d675701.json`](../../sessions/77/778a4af67b1a4d675701.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 报告

### (1) 实验结果：成功

三个条件全部完成，10 runs/条件，数据完整。

### (2) 关键指标

| 条件 | Prefill (ms) | Decode (ms/tok) | Throughput (tok/s) | 理论 KV 内存 |
|------|-------------|----------------|-------------------|-------------|
| baseline_bf16 | 45.9±0.8 | 33.78±0.15 | 29.6±0.1 | 21 MB |
| uniform_4bit | 54.2±2.5 | 42.46±0.33 | 23.6±0.2 | 5.25 MB |
| constrained_mckp | 57.0±4.7 | 46.09±3.65 | 21.8±1.7 | 5.25 MB |

- 理论 KV cache 压缩比：4x（uniform 和 MCKP 相同，因为 budget=0.25）
- MCKP bit 分配：4-bit×100 头 + 8-bit×4 头 + 2-bit×8 头
- MCKP solver 耗时仅 5ms
- 注意：decode latency 包含模拟 quant/dequant 开销（上界），实际部署会更快
- Peak GPU memory 三者相同（14627MB），因为是模拟量化，实际存储仍为 bf16

### (3) GPU 当前状态

| GPU | 已用 | 总量 | 占用率 |
|-----|------|------|--------|
| cuda:0 | 74,195 MiB | 97,887 MiB | 75.8% |
| cuda:1 | 82,590 MiB | 97,887 MiB | 84.4% |

正在运行的进程：
- `run_multi_seed.py` (PID 199409, cuda 占用中)
- `run_cross_domain.py` (PID 204197, cuda 占用中)
- `run_c4_cross_dataset_v2.py` (PID 209268, cuda 占用中)

**两块 GPU 均被占满，当前无空间跑 c4_rerun。**

---
