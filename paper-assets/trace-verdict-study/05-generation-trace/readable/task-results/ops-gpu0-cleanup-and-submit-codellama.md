# ops gpu0 cleanup and submit codellama

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu0-cleanup-and-submit-codellama_20260516T190805_result.json`
- **Structured JSON:** [`8d7820574299e89ca355.json`](../../sessions/8d/8d7820574299e89ca355.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，模型加载完毕正在 tokenize 数据。

**汇报：**

1. **GPU 0 清理**：无法释放孤立显存（49GB 无进程持有，GPU reset 不支持）。但 GPU 0 仍有 48GB 可用空间，足够加载 CodeLlama-13B（已分配 25.7GB）。
2. **codellama13b_exception_only_seed123**：提交成功，PID 299731（实际 Python PID 299741），模型已加载，正在 tokenize 训练数据。GPU 0 当前用量 75GB/96GB。
3. **双 GPU 状态**：
   - GPU 0: 75GB/96GB（codellama13b_exception_only_seed123 训练中 + 49GB 孤立显存）
   - GPU 1: 47GB/96GB, 100% 利用率（exception_only_nomarker_seed456 训练中）

---
