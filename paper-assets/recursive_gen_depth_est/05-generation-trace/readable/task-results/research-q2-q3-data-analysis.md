# research q2 q3 data analysis

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_q2_q3_data_analysis_20260516T140423_result.json`
- **Structured JSON:** [`5addd9790dc3d0f00193.json`](../../sessions/5a/5addd9790dc3d0f00193.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Q2 答案

Cross-model chain 实验采用 leave-one-model-out 设计：

| 维度 | 数量 |
|------|------|
| 模型 | 3 (Pythia, OLMo, GPT-2 XL) |
| 策略 | 3 (nucleus p=0.95, temp=0.9, top-k=50) |
| 深度 | 4 (d0, d1, d2, d3) |
| 每 cell 每 depth | **5,000 samples** |
| 每 cell 总计 | 20,000 (5,000 × 4 depths) |
| 每模型总计 | 60,000 (3 strategies × 20,000) |
| **总样本量** | **180,000** |

每次 LOO rotation：train = 2 models × 3 strategies = 120,000, test = 1 model × 3 strategies = 60,000（每 depth 15,000）。

## Q3 答案

Forward feature selection 中，**3 个 Pythia cells** 第一步选了 `var_surprisal` 而非 `p90_ppl`：

| Cell (Model × Strategy) | 第一步选择的特征 | 单特征准确率 |
|---|---|---|
| Pythia × nucleus (p=0.95) | `var_surprisal` | 0.6215 |
| Pythia × temperature (0.9) | `var_surprisal` | 0.6396 |
| Pythia × top-k (50) | `var_surprisal` | 0.5626 |

其余 6/9 cells（所有 OLMo + 所有 GPT-2 XL）第一步都选了 `p90_ppl`。

**规律**：Pythia 模型的 perplexity 分布方差更大（surprisal variance 对 depth 区分度更高），因此 `var_surprisal` 在 Pythia 上比 `p90_ppl` 具有更强的单特征分类能力。这与 feature importance (Gini) 排名一致——Pythia 3 cells 中 `var_surprisal` importance 均高于 `p90_ppl`（~0.164–0.174 vs. ~0.124–0.151）。

---
