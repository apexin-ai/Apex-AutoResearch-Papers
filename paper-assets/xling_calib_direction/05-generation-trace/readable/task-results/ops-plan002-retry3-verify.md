# ops plan002 retry3 verify

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan002-retry3-verify_20260521T120039_result.json`
- **Structured JSON:** [`7434c21562526c695b5e.json`](../../sessions/74/7434c21562526c695b5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**PID 477148 已死。** 进程不存在。

**崩溃原因：CUDA OOM**
- 日志显示 `torch.OutOfMemoryError`，在模型解压缩阶段（`compressed_tensors` 的 `unpack_from_int32`）爆显存
- GPU 0 的 94.97 GiB 全部用尽，仅剩 25.81 MiB 时尝试分配 160 MiB 失败
- 发生在 `extract_activations.py:411` 的 `model(**inputs)` 首次前向传播时

**当前 GPU 状态：**

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 3 MiB | 0% |
| 1 | 90149 MiB | 0% |
| 2 | 93611 MiB | 0% |
| 3 | 93611 MiB | 0% |

GPU 0 已释放（进程死了），但 GPU 1-3 仍被其他进程占用。

**核心问题：** 量化模型（`compressed_tensors`）在首次前向传播时需要解压缩权重，解压过程的峰值显存超过单卡 95GB。可能需要：
1. 用 `device_map="auto"` 把模型分布到多卡
2. 或换用更小的模型/更激进的量化格式

---
