# analysis gemma27b cross transfer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma27b_cross_transfer_20260524T091853_result.json`
- **Structured JSON:** [`377fae59ce877861c55c.json`](../../sessions/37/377fae59ce877861c55c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `results/gemma27b_cross_transfer/cross_transfer_gemma27b_matrix.json`。

## 完整结果汇总

### Transfer Matrix — 6-class Accuracy

| Train\Test | Gemma-27B | LLaMA-8B | Qwen-1.5B | Pythia-1.4B | OLMo-1B |
|---|---|---|---|---|---|
| **Gemma-27B** | **0.3106** | 0.3218 | 0.3331 | 0.3214 | 0.2892 |
| **LLaMA-8B** | 0.3048 | **0.3309** | 0.3455 | 0.3447 | 0.3047 |
| **Qwen-1.5B** | 0.2693 | 0.3122 | **0.3777** | 0.3325 | 0.3012 |
| **Pythia-1.4B** | 0.2860 | 0.3288 | 0.3418 | **0.3536** | 0.3164 |
| **OLMo-1B** | 0.2457 | 0.2551 | 0.2798 | 0.2902 | **0.3178** |

### Transfer Matrix — Kendall tau_b

| Train\Test | Gemma-27B | LLaMA-8B | Qwen-1.5B | Pythia-1.4B | OLMo-1B |
|---|---|---|---|---|---|
| **Gemma-27B** | **0.3387** | 0.3634 | 0.3914 | 0.3407 | 0.2806 |
| **LLaMA-8B** | 0.3251 | **0.3825** | 0.4180 | 0.3899 | 0.2881 |
| **Qwen-1.5B** | 0.2950 | 0.3763 | **0.4634** | 0.3933 | 0.2807 |
| **Pythia-1.4B** | 0.2956 | 0.3801 | 0.3812 | **0.3960** | 0.3000 |
| **OLMo-1B** | 0.2593 | 0.2674 | 0.2379 | 0.2663 | **0.3015** |

### Transfer Matrix — Mean Pairwise AUC

| Train\Test | Gemma-27B | LLaMA-8B | Qwen-1.5B | Pythia-1.4B | OLMo-1B |
|---|---|---|---|---|---|
| **Gemma-27B** | **0.6019** | 0.6147 | 0.6274 | 0.6166 | 0.5934 |
| **LLaMA-8B** | 0.6037 | **0.6204** | 0.6346 | 0.6269 | 0.5929 |
| **Qwen-1.5B** | 0.5949 | 0.6187 | **0.6396** | 0.6253 | 0.5922 |
| **Pythia-1.4B** | 0.5973 | 0.6163 | 0.6284 | **0.6273** | 0.5964 |
| **OLMo-1B** | 0.5455 | 0.5395 | 0.5698 | 0.5729 | **0.5968** |

### Transfer Retention（关键发现）

**Gemma-27B → 1.5B (大→小 transfer):**
| Target | Acc Retention | tau_b Retention | AUC Retention |
|---|---|---|---|
| LLaMA-8B | **103.6%** | 107.3% | 112.6% |
| Qwen-1.5B | **107.2%** | 115.6% | 125.0% |
| Pythia-1.4B | **103.5%** | 100.6% | 114.4% |
| OLMo-1B | **93.1%** | 82.8% | 91.7% |
| **平均** | **101.3%** | — | — |

**1.5B → Gemma-27B (小→大 transfer):**
| Source | Acc Retention | tau_b Retention | AUC Retention |
|---|---|---|---|
| LLaMA-8B | 92.1% | 85.0% | 86.1% |
| Qwen-1.5B | 71.3% | 63.7% | 68.0% |
| Pythia-1.4B | 80.9% | 74.7% | 76.4% |
| OLMo-1B | 77.3% | 86.0% | 47.0% |
| **平均** | **76.5%** | — | — |

**1.5B inter-model retention (对照):** 88.9%

### 核心发现

1. **Gemma-27B → 小模型 transfer 异常好**：平均 accuracy retention **101.3%**，其中 3/4 方向 >100%（超过自身 diagonal）。训练在 27B 模型上的 classifier 泛化到 1.5B-8B 模型时性能不降反升。

2. **不对称性显著**：小→大 transfer（76.5%）远低于大→小 transfer（101.3%），差距 ~25 个百分点。这与 7B 结果形成对比——7B→1.5B retention 82-85%，差距小得多。

3. **Gemma-27B diagonal accuracy (0.3106) 低于多数 off-diagonal**：这是一个独特现象——27B 模型的 generation depth signal 本身就较弱（难以自我区分），但训练在其数据上的 classifier 对更小模型的区分度反而更高，说明 27B 模型的 depth signature 是一种 "universal" feature subset。

4. **OLMo-1B 仍是最难 transfer 的目标/来源**——所有模型 transfer 到 OLMo 都有明显衰减，与 1.5B 规模实验一致。

---
