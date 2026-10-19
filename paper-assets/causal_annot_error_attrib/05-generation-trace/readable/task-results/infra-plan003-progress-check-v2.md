# infra plan003 progress check v2

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan003-progress-check-v2_20260520T145425_result.json`
- **Structured JSON:** [`578f5bb20a67aca21522.json`](../../sessions/57/578f5bb20a67aca21522.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Plan 003 标注进度报告

### 进程状态：全部存活

| 模型 | PID | 运行时间 | 内存 | 状态 |
|------|-----|---------|------|------|
| llama4 | 438497 | 54m38s | 59MB | **alive** |
| qwen3 | 438843 | 53m31s | 59MB | **alive** |
| deepseek | 439116 | 52m54s | 59MB | **alive** |

### 当前进度

三个模型均在 **第 1/9 个组合**（humaid / zero-shot）：

| 模型 | 已完成样本 (JSONL行数) | 当前组合进度 | 总进度 (of 13,500) |
|------|----------------------|-------------|-------------------|
| llama4 | 339 | 339/1500 (22.6%) | **2.5%** |
| qwen3 | 189 | 189/1500 (12.6%) | **1.4%** |
| deepseek | 274 | 274/1500 (18.3%) | **2.0%** |

### 速率与预估完成时间

| 模型 | 速率 | 剩余样本 | 预估剩余时间 | 预计完成 |
|------|------|---------|-------------|---------|
| llama4 | ~6.2 samples/min | 13,161 | **~35h** | 5月22日凌晨 |
| qwen3 | ~3.5 samples/min | 13,311 | **~63h** | 5月23日早上 |
| deepseek | ~5.2 samples/min | 13,226 | **~42h** | 5月22日上午 |

### 异常

- **502 错误**：llama4 和 qwen3 各出现 2 次和 1 次 `Server error (502)`，均自动重试成功（attempt 1/3），非阻塞性问题。qwen3 速率最慢，可能受 502 重试影响较大。
- 无 traceback 或致命错误。

### 总结

三个进程运行正常，但整体速率偏慢——qwen3 预计需要 **63 小时**才能跑完全部 9 个组合。如果想加速，可以考虑：提高 batch 并发数、或减少 sample 数。

---
