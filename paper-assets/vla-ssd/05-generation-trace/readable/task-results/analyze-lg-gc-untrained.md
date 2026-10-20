# analyze lg gc untrained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_lg_gc_untrained_20260515T180209_result.json`
- **Structured JSON:** [`713702a6d86eea4040fb.json`](../../sessions/71/713702a6d86eea4040fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整分析。

---

## lg_gc_untrained 实验结果

### 数值汇总

| 指标 | 值 |
|------|-----|
| best_layer | 1 (layers 1-9 均为 100%) |
| best_accuracy | **1.0000** |
| best_traj_accuracy | 1.0000 |
| best_macro_f1 | 1.0000 |
| worst_layer | 31 (acc=0.9971) |
| n_classes / n_train / n_val | 10 / 50880 / 12848 |

Layer 0 = 15.82% (random level, 只预测 class 1)。Layer 1 起直接跳到 100%。深层略有下降但最差也 99.71%。

### Gate 判定

**G2-GC: FAIL**
- Δ(trained - untrained) = 1.0 - 1.0 = **0.0 pp** (阈值 25pp)
- 两者从 layer 1 起完全一致

### 三组实验交叉分析

| 实验 | best_acc | Layer 0 | Layer 1+ | feature_dim |
|------|----------|---------|----------|-------------|
| **lg_gc_trained** (trained VLA) | 100% | 15.82% | 100% all layers | 4096 |
| **lg_gc_untrained** (random LLM) | 100% | 15.82% | 100% → 99.71% | 4096 |
| **lg_gc_dino** (DINO-V2) | 86.26% | — | 86.26% (1 layer) | 1024 |

### 核心发现

1. **Goal classification 不是有效的 trained vs untrained 判别器。** 随机 LLM 权重 + 一层 transformer 就能把 10 个 goal 类别完美分开。4096 维空间中 10 个类别的线性可分性在随机投影下几乎必然成立——这是高维空间的几何性质，不是训练的贡献。

2. **Layer 0 的 15.82% 值得注意。** Trained 和 untrained 的 layer 0 acc 完全相同（都是 15.82%，都只预测 class 1）。这说明 SigLIP 视觉编码经过投影层进入 LLM 嵌入空间后，class-discriminative 信息被破坏了（无论 LLM 是否 trained）。而 DINO 用 1024-dim 原始视觉特征能达到 86.26%——确认 goals 在视觉上可区分，但投影层丢失了这个信息。

3. **Untrained 比 trained 在深层略差（~0.3pp）。** 这是唯一差异，但远不足以通过 25pp 的 gate。可能反映 trained LLM 的深层 attention pattern 比随机权重稍微更稳定，但差异微不足道。

### 对论文 story 的影响

**Goal classification probe 这条线作废了。** 原本想说"trained VLA encodes goal knowledge that untrained VLA doesn't"，但数据完全不支持——随机 LLM 同样能做到。这不是因为 goals 不重要，而是 MLP probe + 4096-dim features + 10 classes 这个实验设计太容易了。

**可能的 pivot 方向**：
- 用**线性 probe** (logistic regression) 替代 MLP，降低 probe 的拟合能力
- 增加类别数（更细粒度的 goal 区分）
- 换成更难的任务：**action prediction probe**（不是分类 10 个 goal，而是回归连续动作空间）——这对 trained vs untrained 更有区分度
- 看 LIBERO-Goal 实验是否应该直接跳到 action decoding 类型的 probe

---
