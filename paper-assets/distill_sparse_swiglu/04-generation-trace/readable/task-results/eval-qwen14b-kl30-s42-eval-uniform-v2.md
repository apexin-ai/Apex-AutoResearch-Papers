# eval qwen14b kl30 s42 eval uniform v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen14b_kl30_s42_eval_uniform_v2_20260519T132416_result.json`
- **Structured JSON:** [`e4c5e636b7c79bd4bbc6.json`](../../sessions/e4/e4c5e636b7c79bd4bbc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### 1. 提交状态
- **PID**: 108497 (nohup, westd-34887 cuda:0)
- **Registry**: `qwen14b_kl30_s42_eval_uniform_v2` → RUNNING
- **日志**: `/root/distill_sparse_swiglu/logs/qwen14b_kl30_s42_eval_uniform_v2.log`
- 当前进度：已完成 per-layer sparsity 打印，正在跑 WikiText-2 PPL (145 sequences)

### 2. Per-layer sparsity 对比结论

**三个 seed (s42/s123/s456) 的 per-layer sparsity 完全一致：**

| Layer | Sparsity |
|-------|----------|
| 0 | 0.301 |
| **1-4** | **0.000** |
| 5-47 | 0.301 |
| Model-level | 0.275 |

**结论：Layer 1-4 sparsity=0.000 是 predictor 的确定性特征，与 seed 无关。** 这些层的 sigmoid 输出在 uniform allocation 下全部超过 threshold，predictor 一致决定不剪枝。s42 checkpoint 没有问题。Model-level sparsity 为 0.275（低于 target 0.3），正是因为这 4 层贡献了 0 sparsity 拉低了全局均值。

---
