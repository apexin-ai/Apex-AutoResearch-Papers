# code cross temp qwen only

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross-temp-qwen-only_20260517T125436_result.json`
- **Structured JSON:** [`076ba34f28431c6f2bf1.json`](../../sessions/07/076ba34f28431c6f2bf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `results/cross_temp_transfer_qwen_only.json`。

**结果摘要：**

| Condition | Binary F1 | 95% CI | 3-class F1 | 95% CI |
|-----------|-----------|--------|------------|--------|
| 0.7→0.7 | 0.9262 | [0.916, 0.935] | 0.7690 | [0.756, 0.781] |
| 0.7→1.0 | 0.7574 | [0.745, 0.770] | 0.4581 | [0.445, 0.472] |
| 1.0→1.0 | 0.8248 | [0.810, 0.838] | 0.5738 | [0.560, 0.588] |
| 1.0→0.7 | 0.9443 | [0.936, 0.953] | 0.6014 | [0.593, 0.611] |

**Transfer deltas:**
- 0.7-trained, cross→1.0: binary **-16.9 pp**, 3-class **-31.1 pp** (大幅下降)
- 1.0-trained, cross→0.7: binary **+12.0 pp**, 3-class **+2.8 pp** (反而提升)

关键发现：transfer 是非对称的。t=0.7 训练的分类器迁移到 t=1.0 时严重衰减，但 t=1.0 训练的分类器迁移到 t=0.7 时 binary F1 反而更高（0.9443 vs 0.8248）。这说明 t=1.0 的特征分布更 "spread out"，学到的 decision boundary 在 t=0.7 上也适用，但反向不行。3-class 任务中 gen-1 类别（per-class F1 在 1.0→0.7 中仅 0.05）是主要瓶颈。

---
