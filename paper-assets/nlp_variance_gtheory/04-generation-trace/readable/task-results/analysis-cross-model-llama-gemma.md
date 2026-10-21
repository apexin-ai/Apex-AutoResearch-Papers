# analysis cross model llama gemma

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_model_llama_gemma_20260521T043623_result.json`
- **Structured JSON:** [`e61cfc55f6da3cc2a90e.json`](../../sessions/e6/e61cfc55f6da3cc2a90e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果已获取。以下是跨模型 G-theory 分析汇总。

---

## 跨模型 G-theory 分析结果 (Llama + Gemma, N=325,600)

### 方差分解 (按贡献排序)

| Component | σ² | % | 95% CI |
|---|---|---|---|
| **item_id** | 0.0768 | **37.9%** | [0.0578, 0.0952] |
| **model×item_id** | 0.0530 | **26.2%** | [0.0401, 0.0677] |
| **residual** | 0.0497 | **24.5%** | [0.0440, 0.0555] |
| prompt_template×item_id | 0.0057 | 2.8% | [0.0046, 0.0067] |
| seed×item_id | 0.0050 | 2.5% | [0.0036, 0.0063] |
| precision×item_id | 0.0047 | 2.3% | [0.0038, 0.0058] |
| model×precision | 0.0029 | 1.4% | [0.0015, 0.0044] |
| temperature×item_id | 0.0027 | 1.3% | [0.0020, 0.0034] |
| ordering×item_id | 0.0013 | 0.6% | [0.0006, 0.0022] |
| model (main) | 0.0004 | 0.2% | [0.0, 0.0053] |
| 其他 | — | <0.1% | — |

### 关键对比：单模型 vs 跨模型

| 指标 | 单模型 (Llama) | 跨模型 (Llama+Gemma) | 变化 |
|---|---|---|---|
| **item_id** | **61.1%** | **37.9%** | ↓ 23.2pp |
| **model×item_id** | — | **26.2%** | 新增 |
| residual | 21.6% | 24.5% | ↑ 2.9pp |
| **G 系数** | **0.611** | **0.073** | ↓↓↓ |

### D-study: 模型数量扫描

| n_models | G |
|---|---|
| 1 | 0.042 |
| 2 | 0.073 |
| 3 | 0.097 |
| 5 | 0.131 |
| 10 | 0.179 |

### 关键发现 (Claim 1)

1. **model×item_id 交互 = 26.2%**，是第二大方差来源。不同模型在不同 item 上的表现差异巨大——这直接说明「哪些题难」的判断取决于你用哪个模型。

2. **item_id 从单模型 61.1% 降至 37.9%**（降幅 23.2pp）。引入 model facet 后，原来归因于 item 固有难度的方差中有大量被 model×item_id 交互吸收——item 难度不是模型无关的，而是 model-specific。

3. **G 系数从 0.611 暴跌至 0.073**。这意味着单模型实验中看似可靠的 item 难度排序（G=0.61），在跨模型场景下几乎不可推广。Model 切换是破坏评测可推广性的最大因素。

4. **D-study：即使增加到 10 个模型，G 仅达 0.18**。模型间的 item-level 交互极大，少量模型无法有效平均掉这部分方差。

5. **model main effect 仅 0.2%**——模型总体准确率差异很小（Llama 66.4% vs Gemma 73.2%），但 model×item_id 交互（26.2%）才是真正的问题——模型在 item 级别的差异远大于整体均值差异。

---
