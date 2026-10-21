# ops resubmit c1 ablation

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resubmit-c1-ablation_20260518T155009_result.json`
- **Structured JSON:** [`dc00ecf22d1430c4f432.json`](../../sessions/dc/dc00ecf22d1430c4f432.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

## 报告

### 1. 死亡原因
进程**未死亡**，两个进程均正常完成 1000 步训练后退出。日志末尾显示 "Done."，checkpoint 已保存。

### 2. 实验结果（假设被否定）

| Metric | BCE+KL targets | KL distill | BCE |
|--------|---------------|-----------|-----|
| WikiText-2 PPL | **9.29** | 11.79 | 22.51 |
| Eval sparsity | 0.609 | - | - |
| Oracle agreement | 97.8% | - | - |

假设预测 BCE+KL targets 的 PPL 会接近 BCE (22.51)，但实际 PPL=9.29 比 KL (11.79) 还好。**Target quality 是关键因素，非 gradient coupling。** BCE 用 KL-derived oracle masks 作为训练目标后，因为优化地形更简单，反而超越了 KL distillation 本身。

### 3. 操作
- 无需重新提交
- Registry 已更新：status=DONE, conclusion=negative, metrics 已录入
- westd-41718 GPU 1 空闲可用于其他实验

---
