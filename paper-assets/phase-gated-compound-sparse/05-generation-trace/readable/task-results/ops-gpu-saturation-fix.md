# ops gpu saturation fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_saturation_fix_20260516T031832_result.json`
- **Structured JSON:** [`60bcbf2a6cd8c7f6644f.json`](../../sessions/60/60bcbf2a6cd8c7f6644f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 诊断报告

### 各 GPU 状态

| GPU | 显存占用 | 利用率 | 进程 | 说明 |
|-----|---------|--------|------|------|
| **0** | 39.6GB / 96GB | 74-75% | PID 307021: `analysis_c5_gini.py` (24GB, 运行 3h+)&lt;br>PID 308765: `think_phase_kappa_math500.py` (15.5GB) | **两个进程共享 GPU 0** |
| **1** | 3MB / 96GB | 0% | 无 | **完全空闲，可立即使用** |
| **2** | 21.3GB / 96GB | 78% | PID 310131: c8 Llama dry-run profiling (21GB) | 活跃运行中 |
| **3** | 3MB / 96GB | 0% | 无 | **完全空闲，可立即使用** |

### c4_v2 进程 (PID 308759 → 308765)

- PID 308759 是 bash wrapper，**仍然存活**，它 spawn 了实际 python 进程 PID 308765
- PID 308765 运行 `think_phase_kappa_math500.py`，**在 GPU 0 上**（不是单独占 GPU），占用 15.5GB 显存
- 进度：**30/50 (DeepSeek 模型)**，已运行约 18 分钟，每题约 30-60 秒
- 注意：大量 `No &lt;/think> found` 警告，很多样本 kappa 被跳过
- 预计还需约 10-15 分钟完成 DeepSeek 部分（之后可能还有其他模型）

### 结论

- **GPU 1、GPU 3 完全空闲**，可立即调度新任务
- c4_v2 和 c5_gini 挤在 GPU 0 上，但显存总占用 39.6GB / 96GB，暂时够用
- c8 dry-run 在 GPU 2 上独占运行，利用率 78%

---
