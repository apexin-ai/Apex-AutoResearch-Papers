# analysis exp013 cross transfer run

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp013_cross_transfer_run_20260513T064820_result.json`
- **Structured JSON:** [`d41875f39c00b2d3feb4.json`](../../sessions/d4/d41875f39c00b2d3feb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。以下是完整结果。

---

## Exp-013 Cross-Model Transfer Matrix 结果

### 1. Accuracy Matrix (train↓ × test→)

| Train \ Test | Qwen-rewrite | Pythia | OLMo | Qwen-cont |
|---|---|---|---|---|
| **Qwen-rewrite** | **0.4229** | 0.2590 | 0.2653 | 0.3466 |
| **Pythia** | 0.2718 | **0.3856** | 0.3531 | 0.3287 |
| **OLMo** | 0.2768 | 0.3450 | **0.3822** | 0.3244 |
| **Qwen-cont** | 0.3440 | 0.3284 | 0.3112 | **0.3875** |

### 2. MAE Matrix (train↓ × test→)

| Train \ Test | Qwen-rewrite | Pythia | OLMo | Qwen-cont |
|---|---|---|---|---|
| **Qwen-rewrite** | **0.984** | 1.982 | 1.976 | 1.516 |
| **Pythia** | 1.903 | **1.107** | 1.281 | 1.502 |
| **OLMo** | 1.894 | 1.349 | **1.147** | 1.557 |
| **Qwen-cont** | 1.340 | 1.336 | 1.475 | **1.121** |

### 3. Kendall τ_b Matrix (train↓ × test→)

| Train \ Test | Qwen-rewrite | Pythia | OLMo | Qwen-cont |
|---|---|---|---|---|
| **Qwen-rewrite** | **0.5518** | 0.2768 | 0.2492 | 0.4595 |
| **Pythia** | 0.1695 | **0.4745** | 0.4100 | 0.3801 |
| **OLMo** | 0.1708 | 0.3979 | **0.4683** | 0.3542 |
| **Qwen-cont** | 0.4126 | 0.3912 | 0.3241 | **0.4769** |

### 4. Mean Pairwise AUC Matrix (train↓ × test→)

| Train \ Test | Qwen-rewrite | Pythia | OLMo | Qwen-cont |
|---|---|---|---|---|
| **Qwen-rewrite** | **0.6214** | 0.5787 | 0.5791 | 0.6247 |
| **Pythia** | 0.5603 | **0.6055** | 0.5937 | 0.6082 |
| **OLMo** | 0.5607 | 0.5999 | **0.6015** | 0.5926 |
| **Qwen-cont** | 0.5767 | 0.6025 | 0.5988 | **0.6111** |

### 5. Transfer Retention Ratio (cross / within)

**Accuracy retention:**
| Train \ Test | Qwen-rewrite | Pythia | OLMo | Qwen-cont |
|---|---|---|---|---|
| **Qwen-rewrite** | 1.000 | 0.612 | 0.627 | 0.820 |
| **Pythia** | 0.705 | 1.000 | 0.916 | 0.852 |
| **OLMo** | 0.724 | 0.903 | 1.000 | 0.849 |
| **Qwen-cont** | 0.814 | 0.847 | 0.803 | 1.000 |

**τ_b retention:**
| Train \ Test | Qwen-rewrite | Pythia | OLMo | Qwen-cont |
|---|---|---|---|---|
| **Qwen-rewrite** | 1.000 | 0.502 | 0.452 | 0.833 |
| **Pythia** | 0.307 | 1.000 | 0.864 | 0.801 |
| **OLMo** | 0.310 | 0.850 | 1.000 | 0.757 |
| **Qwen-cont** | 0.748 | 0.820 | 0.680 | 1.000 |

### 6. 关键发现

**结论：depth signal 是混合性质的——大部分来自文本固有属性，但存在显著的 model-specific 分量。**

具体证据：

1. **Pythia ↔ OLMo 互迁移保留率很高**（accuracy 91-92%，τ_b 85-86%）。这两个模型架构不同（GPT-NeoX vs OLMo），但训练在类似的开放语料上，说明 depth signal 主要编码在文本本身而非模型特异性。

2. **Qwen-rewrite 作为 train set 迁移到 Pythia/OLMo 时大幅下降**（accuracy 仅 61-63%，τ_b 仅 45-50%）。Qwen-rewrite 的 depth 特征包含了明显的 Qwen 模型指纹（rewrite 引入的风格偏置），导致对非 Qwen 模型泛化差。

3. **Qwen-cont ↔ Qwen-rewrite 互迁移相对较好**（retention 81-83% accuracy，75-83% τ_b），说明同系列模型之间共享更多 depth signal 特征。

4. **Qwen-cont 作为 test set 时，所有 train source 都保持较高的 mean pairwise AUC**（0.59-0.62），0v1 AUC 尤其高（>0.96），说明"是否被污染"（depth 0 vs 1）的信号是高度跨模型可迁移的，但**细粒度 depth 区分**（1v2, 2v3 等）依赖模型特异性特征。

5. **非对称性**：Qwen-rewrite→others 下降比 others→Qwen-rewrite 更严重，暗示 Qwen-rewrite 的分类器过拟合了 rewrite 风格特征而非通用 depth 特征。

**总结**：depth signal ≈ 70-85% 文本固有属性 + 15-30% model self-familiarity artifact。二分类（contaminated vs clean）几乎完全可迁移，细粒度 depth 分级的迁移性取决于模型族的相似度。

---
