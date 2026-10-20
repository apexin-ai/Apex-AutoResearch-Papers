# analysis dataset b gstudy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dataset_b_gstudy_20260521T053605_result.json`
- **Structured JSON:** [`3664a5e3c71394fb5b7c.json`](../../sessions/36/3664a5e3c71394fb5b7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

G-study 完成。结果保存至 `results/analysis/dataset_b_gstudy.json`。

---

## 结果汇总

### 1. 方差分量（% of total SS）

| 分量 | % |
|---|---|
| **item_id** | **52.28%** |
| residual | 25.46% |
| model×item_id | 12.23% |
| seed×item_id | 4.28% |
| prompt_template×item_id | 2.53% |
| precision×item_id | 1.06% |
| model | 0.62% |
| ordering×item_id | 0.44% |
| temperature×item_id | 0.38% |
| model×precision | 0.33% |
| precision | 0.32% |

### 2. G 系数

| 系数 | 值 |
|---|---|
| **G_item** | **0.866** |
| **G_condition** | **0.942** |

### 3. D-study

**G_item vs n_models:**

| n_models | 1 | 2 | 3 | 4 | 5 | 10 |
|---|---|---|---|---|---|---|
| G_item | 0.786 | 0.866 | 0.896 | 0.912 | 0.922 | 0.943 |

**G_item vs n_seeds:**

| n_seeds | 1 | 2 | 3 | 6 | 10 | 20 |
|---|---|---|---|---|---|---|
| G_item | 0.816 | 0.845 | 0.856 | 0.866 | 0.870 | 0.873 |

**G_item vs n_prompts:**

| n_prompts | 1 | 2 | 3 | 6 | 10 | 20 |
|---|---|---|---|---|---|---|
| G_item | 0.835 | 0.853 | 0.860 | 0.866 | 0.868 | 0.870 |

### 4. 平衡 vs 不平衡对比

| 分量 | 不平衡 (N=325,600) | 平衡 (N=230,400) | 变化 |
|---|---|---|---|
| item_id | 37.90% | 52.28% | **+14.38** |
| model×item_id | 26.20% | 12.23% | **−13.97** |
| residual | 24.50% | 25.46% | +0.96 |
| seed×item_id | 0.50% | 4.28% | **+3.78** |
| model | 3.10% | 0.62% | −2.48 |
| G_item | 0.707 | 0.866 | **+0.159** |

### 5. 关键发现

**平衡设计大幅改变了方差分解结构：**

- **item_id 从 37.9% 升至 52.3%**（排名不变，仍是第一大来源）——平衡设计消除混淆后，题目难度差异更加突出
- **model×item_id 从 26.2% 降至 12.2%**——仍是第二大来源，但不平衡数据中该项被高估了约一倍（可能因缺失 cell 导致方差混入交互项）
- **seed×item_id 从 0.5% 升至 4.3%**——不平衡中被严重低估，平衡后显示种子对不同题目的影响比之前认为的大
- **precision 相关分量**（新增）合计约 1.7%——precision 本身和 precision×item_id 贡献不大，但 model×precision 有 0.33%
- **G_item 从 0.707 升至 0.866**——平衡设计下测量信度显著提升，主要因为 model×item_id 误差项的下降
- **结论一致性**：model×item_id 仍是第二大来源——平衡设计没有改变基本排序，但修正了数值

---
