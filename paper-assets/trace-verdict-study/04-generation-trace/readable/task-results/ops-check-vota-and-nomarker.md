# ops check vota and nomarker

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_vota_and_nomarker_20260516T151603_result.json`
- **Structured JSON:** [`cfd7d6aa030849f25194.json`](../../sessions/cf/cfd7d6aa030849f25194.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. codellama13b_vota_seed42 (GPU 1)
**运行中** — PID 279473, 已运行 53 分钟

- 进度: **108/444 steps (24%)**, ~29s/step
- 预计剩余: ~2h 40min
- GPU 1: 100% 利用率, 36.5GB/97.9GB 显存

### 2. exception_only_nomarker_seed42 (GPU 0)
**已崩溃** — PID 282597 不存在

- 错误: **CUDA OOM** — 尝试分配 472MB 时失败，GPU 0 已用 46.93GB (PyTorch 分配 45.46GB)
- 崩溃位置: `trainer.train()` 启动时即 OOM (step 0)
- 原因: Qwen2.5-Coder-7B 在 GPU 0 上内存不足。GPU 0 当前仍有 49GB 被占用（可能是残留显存未释放）

### 3. GPU 全局状态

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 0% | 49.2GB / 97.9GB |
| 1 | 100% | 36.5GB / 97.9GB |

GPU 0 上只有 codellama 的进程(PID 279483)在 GPU 1 运行。GPU 0 的 49GB 占用来源不明——可能是 OOM 崩溃后显存残留未清理，或有其他进程占用。

需要清理 GPU 0 显存后重新提交 exception_only_nomarker_seed42 吗？

---
