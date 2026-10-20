# analysis exp arXiv llama8b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_arXiv_llama8b_20260517T140046_result.json`
- **Structured JSON:** [`f052c779419f4e8f3165.json`](../../sessions/f0/f052c779419f4e8f3165.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B 工具有内部问题，但所有关键数据已从结果文件获取。以下是完整分析。

---

## exp_arXiv_llama8b 实验分析报告

### 实验状态
**正常完成** (EXIT_CODE=0)，无 error/exception。

### Pairwise Discrimination AUC（5-fold CV）

| Depth Pair | LLaMA-3.1-8B (本实验) | Qwen2.5-1.5B (exp_024) | Pythia-1.4B (exp_025) |
|:----------:|:---------------------:|:----------------------:|:---------------------:|
| 0 vs 1     | **0.9754** ± 0.0014   | 0.9948 ± 0.0008        | 0.9877 ± 0.0028       |
| 1 vs 2     | **0.8447** ± 0.0099   | 0.8581 ± 0.0125        | 0.8047 ± 0.0133       |
| 2 vs 3     | **0.6215** ± 0.0188   | 0.6436 ± 0.0236        | 0.6545 ± 0.0132       |
| 3 vs 4     | **0.5362** ± 0.0117   | 0.5440 ± 0.0177        | 0.5507 ± 0.0097       |
| 4 vs 5     | **0.5331** ± 0.0175   | 0.5299 ± 0.0245        | 0.5287 ± 0.0120       |

### JSD（Jensen-Shannon Divergence）

| Depth Pair | JSD      |
|:----------:|:--------:|
| 0 vs 1     | 0.1296   |
| 1 vs 2     | 0.0785   |
| 2 vs 3     | 0.0177   |
| 3 vs 4     | 0.0077   |
| 4 vs 5     | 0.0073   |

### K* 判定

**K* = 3**（阈值 θ = 0.60）

- 0v1 AUC = 0.9754 >> θ（强可区分）
- 1v2 AUC = 0.8447 >> θ（强可区分）
- 2v3 AUC = 0.6215 > θ（仍可区分，但边际）
- **3v4 AUC = 0.5362 ≈ random**（不可区分，跌破阈值）
- 4v5 AUC = 0.5331 ≈ random

K* = 3 的含义：depth 0, 1, 2 的文本可被 scorer 逐级区分，但从 depth 3 开始文本统计特征趋于饱和，更深的 rewriting 不再产生可检测差异。

### 与 Parent 实验对比

三个 generator 在 arXiv domain 上的 K* **完全一致**：

| Generator       | Params | K* | 2v3 AUC | 3v4 AUC |
|:---------------:|:------:|:--:|:-------:|:-------:|
| Qwen2.5-1.5B    | 1.5B   | 3  | 0.6436  | 0.5440  |
| Pythia-1.4B      | 1.4B   | 3  | 0.6545  | 0.5507  |
| **LLaMA-3.1-8B** | **8B** | **3** | **0.6215** | **0.5362** |

关键观察：
- LLaMA-8B 的 0v1 AUC (0.9754) 略低于 Qwen-1.5B (0.9948)，说明 8B 模型的 generation 0→1 改写更接近原文（更强的 continuation 能力），但差异仍然可检测
- 2v3 边界处 LLaMA-8B (0.6215) 略低于 Qwen (0.6436) 和 Pythia (0.6545)，暗示更大模型的饱和收敛略快，但不改变 K*
- 3v4 和 4v5 三个模型均收敛至 ~0.53（接近 random 0.5）

### Ordinal Classification

| Metric   | LLaMA-8B | Qwen-1.5B | Pythia-1.4B |
|:--------:|:--------:|:---------:|:-----------:|
| MAE      | 0.8806   | 0.8256    | 0.8518      |
| Accuracy | 0.4549   | 0.4767    | 0.4545      |

LLaMA-8B 的 ordinal MAE 略高，与 2v3 AUC margin 更窄一致。

### Top Feature Importance

freq_entropy (9477) > surp_std (7644) > surp_d1_skew (7339) > surp_d2_mean (7301)

### 结论

**SUCCESS — arXiv domain K\*=3 在 8B scale 确认成立。**

LLaMA-3.1-8B 作为 generator 在 arXiv abstracts 上的 K* = 3，与 Qwen2.5-1.5B 和 Pythia-1.4B 完全一致。这排除了"K*=3 是小模型 capacity artifact"的假说，证明 K*=3 是 arXiv domain 的内在属性，不随 generator 模型规模变化。

### 文件路径
- **结果目录**: `cqa1-22115:/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_llama8b/`
- **日志**: `cqa1-22115:~/runs/gen-depth-contamination/exp_arXiv_llama8b.log`

---
