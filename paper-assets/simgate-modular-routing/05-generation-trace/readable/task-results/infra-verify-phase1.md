# infra verify phase1

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-phase1_20260513T062525_result.json`
- **Structured JSON:** [`b0a8bf388b7cb95816a8.json`](../../sessions/b0/b0a8bf388b7cb95816a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇报：

**1. 进程状态**
- GPU0 (PID 20296): **存活**，正常运行中
- GPU1 (PID 20374): **已死**

**2. GPU0 状态** — 正常
- 模型加载成功，Backend: HF transformers
- Task types: boil, melt, change-the-state-of-matter-of
- 已完成 Episode 0、1，正在跑 Episode 2
- GPU0 显存占用 15720MiB / 32607MiB

**3. GPU1 崩溃原因** — `CUDA error: invalid device ordinal`
```
torch.AcceleratorError: CUDA error: invalid device ordinal
GPU device may be out of range, do you have enough GPUs?
```
在 `_load_hf()` 加载模型到 `cuda:1` 时失败。错误发生在 `caching_allocator_warmup` → `mem_get_info(device)`。GPU1 物理上存在（nvidia-smi 可见，100% util 但 0MiB 显存），可能是启动时 `CUDA_VISIBLE_DEVICES=1` 导致设备在进程内变为 `cuda:0` 而非 `cuda:1`，但代码尝试访问 `cuda:1`。

**4. GPU 显存**
- GPU0: 15729MiB / 32607MiB（模型已加载）
- GPU1: 0MiB / 32607MiB（空闲，进程已死）

**修复建议**：GPU1 进程可能用了 `CUDA_VISIBLE_DEVICES=1` 但代码内部仍尝试访问 `cuda:1`。需要确认启动命令中 `--gpu` 参数与 `CUDA_VISIBLE_DEVICES` 的映射关系——当设置 `CUDA_VISIBLE_DEVICES=1` 时，该 GPU 在进程内应该是 `cuda:0`。

---
