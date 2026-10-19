# ops plan002 cron triage

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan002-cron-triage_20260521T120116_result.json`
- **Structured JSON:** [`141ef9e048f2d199a967.json`](../../sessions/14/141ef9e048f2d199a967.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：Retry 3 真的崩了（CUDA OOM）

**PID 477148 已死亡**，不是 cron 误报。

### 崩溃原因

`torch.OutOfMemoryError` — 模型解压（decompress）阶段 OOM。日志关键行：

```
File ".../compressed_tensors/compressors/pack_quantized/helpers.py", line 159, in unpack_from_int32
    unpacked = (unpacked - offset).to(torch.int8)
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 160.00 MiB.
GPU 0 has a total capacity of 94.97 GiB of which 25.81 MiB is free.
```

Llama4 Scout W4A16 量化模型在首次前向传播时触发 `compressed_tensors` 的 decompress hook，将压缩权重解包到 GPU 显存，此时单卡 94.97GB 已被占满。

### 当前 GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 3 MiB | 0% |
| 1 | 90149 MiB (~88GB) | 0% |
| 2 | 93611 MiB (~91GB) | 0% |
| 3 | 93611 MiB (~91GB) | 0% |

GPU 1-3 仍有大量显存被占用但利用率 0%——可能是之前 retry 遗留的僵尸显存，也可能有其他进程。GPU 0 已释放（崩溃的进程所在卡）。

### 产出状态

输出目录 `/root/autodl-tmp/activations/llama4_scout/llama4_scout_w4a16/` 下创建了 13 个层目录（L0, L4, L8, ... L47）但**全部为空**——模型加载就崩了，还没开始提取 activation。

### 根因分析

Llama4 Scout 的 W4A16 量化模型在解压时需要将 INT4 权重解包为 INT8/FP16，这个中间态需要额外显存。单卡放不下整个解压后的模型。需要：
1. 用 `device_map="auto"` 分散到多卡，或
2. 设置 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` 减少碎片，或
3. 在 CPU 上解压后再分片加载到 GPU

---
