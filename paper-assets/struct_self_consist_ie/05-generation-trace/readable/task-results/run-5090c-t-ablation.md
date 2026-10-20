# run 5090c t ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_5090c_t_ablation_20260520T221637_result.json`
- **Structured JSON:** [`3b7e9c785ce8b8d226b4.json`](../../sessions/3b/3b7e9c785ce8b8d226b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**5090-c 当前状态：所有 GPU 被占用，T-ablation 无法启动。**

正在运行的任务：
- **Qwen2.5-32B QLoRA FewNERD 训练**（4-GPU 分布式，PID 804665-804668）
- 进度：39050/41180 steps（**94.83%**）
- 剩余时间：约 **2 小时**

训练完成后 cuda:1-3 才会释放。建议：
1. 等 ~2 小时训练完成后再启动 T-ablation
2. 或者如果有其他空闲服务器可以用

需要我设置定时检查，训练完成后自动启动 T-ablation 吗？

---
