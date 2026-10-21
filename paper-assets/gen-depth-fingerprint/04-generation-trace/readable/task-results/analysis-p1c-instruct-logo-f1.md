# analysis p1c instruct logo f1

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p1c-instruct-logo-f1_20260515T154858_result.json`
- **Structured JSON:** [`e7280f151af6463d0cea.json`](../../sessions/e7/e7280f151af6463d0cea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `results/p1c_instruct_logo_f1.json`。

**关键发现：**

| 指标 | 值 |
|------|-----|
| 7-gen LOGO avg F1 | **0.7498** (vs 6-gen base 0.789, 下降 0.039) |
| 7-gen binary F1 | **0.768** (vs 6-gen base 0.723, 上升 0.045) |

**Instruct vs Base 对比：**

| Generator | 3-class F1 | Binary F1 |
|-----------|-----------|-----------|
| qwen3-1.7b-instruct (held out) | **0.5434** | 0.6582 |
| qwen3-1.7b-base (held out) | **0.8023** | 0.8208 |
| **Delta** | **-0.2589** | -0.1626 |

Instruct held-out F1 大幅低于 base（0.543 vs 0.802）。方向反转使得 base 训练的分类器难以泛化到 instruct 数据——6 个 base model 学到的 "depth 越深 diversity 越低" 模式在 instruct 上完全反转，导致预测失败。XGBoost 虽然不假设方向，但训练数据中 6/7 都是同一方向，held-out 时自然偏向 base 模式。

---
