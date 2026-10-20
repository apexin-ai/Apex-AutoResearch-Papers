# diagnose exception only nomarker seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exception_only_nomarker_seed42_20260516T155123_result.json`
- **Structured JSON:** [`d201b7c4b2ec5da64825.json`](../../sessions/d2/d201b7c4b2ec5da64825.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

### 根因

**CUDA OOM（显存不足）**。训练在第一个 step（0/444）就崩溃，LoRA dropout forward 时尝试分配 472 MiB 失败，GPU 94.97 GiB 中 46.93 GiB 已被占用（PyTorch 分配了 45.46 GiB）。

### 关键对比

- `exception_only_seed123` 使用完全相同的配置（4720 samples, batch=4, grad_accum=8, max_length=2048, 444 steps）并成功完成
- 两个数据集大小接近（nomarker 7.9MB vs exception_only 8.1MB），数据本身不是问题
- 同样配置同样模型，一个能跑一个 step 0 就 OOM → **GPU 上有其他进程占用了约 48 GiB 显存**

### Traceback

```
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 472.00 MiB. 
GPU 0 has a total capacity of 94.97 GiB of which 17.56 MiB is free. 
Including non-PyTorch memory, this process has 46.93 GiB memory in use.
Of the allocated memory 45.46 GiB is allocated by PyTorch, and 818.29 MiB 
is reserved by PyTorch but unallocated.
```

崩溃点：`peft/tuners/lora/layer.py:969` → `F.dropout(input, self.p, self.training, self.inplace)`

### 修复建议

1. **重跑前确认 GPU 空闲**：`nvidia-smi` 检查无其他进程占用 GPU 0
2. 如果是该进程自身占满（model loading 阶段分配了 46GB，forward 多出来的碎片无法满足），考虑：
   - 减小 `per_device_train_batch_size` 从 4 → 2
   - 或设 `PYTORCH_ALLOC_CONF=expandable_segments:True` 减少碎片

最可能的情况是 GPU 被其他训练占了一半显存。清理后直接重跑原命令即可。

---
