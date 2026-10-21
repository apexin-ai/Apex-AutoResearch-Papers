# ops check lora only status

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_lora_only_status_20260519T071847_result.json`
- **Structured JSON:** [`0cc033018e0b68c0a058.json`](../../sessions/0c/0cc033018e0b68c0a058.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

1. **进程已死**：PID 45616 不存在，tmux session 也没了
2. **GPU 空闲**：0 MiB 显存占用，无运行进程
3. **崩溃原因**：`train_phase2.py:128` 属性名拼写错误

```
AttributeError: 'torch._C._CudaDeviceProperties' object has no attribute 'total_mem'. Did you mean: 'total_memory'?
```

`torch.cuda.get_device_properties(0).total_mem` 应改为 `total_memory`。

**修复**：`/root/turn_residual_gating/src/train_phase2.py` 第 128 行，`total_mem` → `total_memory`，然后重新启动训练。

---
