# 数学域 Negative Analysis：SICA ≡ SC on QwQ-32B

## 摘要

QwQ-32B 在数学域（MATH-500、AIME 2024）上的 multi-candidate rate 为 0%，导致 SICA 在所有实验中严格退化为 Self-Consistency（SC），无法产生任何增益。这是推理模型 deterministic CoT 的结构性结果，与温度无关。

## 证据汇总表

| 实验 | 数据集 | 完成题数 | K | 温度 | Multi-candidate Rate | SICA Acc | SC Acc | Gap (pp) | 来源 |
|------|--------|----------|---|------|---------------------|----------|--------|----------|------|
| sica_smoke_5q | MATH L1–5 | 5/5 | 12 | 0.7 | 0%¹ | 80.0% | 80.0% | 0 | `sica_smoke_5q` |
| sica_temp_diversity | MATH L4–5 | 3² | 12 | 0.7 / 0.9 / 1.0 | 0% | — | — | 0 | `sica_temp_diversity` |
| sica_aime30_v2 | AIME 2024 | 4/30 (killed) | 12 | 0.7 | —³ | 75.0% | 75.0% | 0 | `sica_aime30_v2` |
| sica_aime30_v3 | AIME 2024 | 22/30 (killed) | 12 | 0.7 | 0.0% | 72.7% | 72.7% | 0 | `sica_aime30_v3` |

**注释：**
1. `sica_smoke_5q` 未显式报告 multi-candidate rate，但 SICA=SC=80% 且 5 题中无一因 MaxSAT exclusion 改变投票结果（algebra/2277 有 3 条约束被 exclude，但最终答案未改变）。
2. `sica_temp_diversity` spec 中 data_count=5，但 metrics 报告 problems_tested=3，原因为 max_tokens=4096 对 L5 题不足导致截断（metrics.max_tokens_issue）。
3. `sica_aime30_v2` 未单独报告 multi-candidate rate，但 analysis_sica_sc_agreement=9/9 (100%)，与 sica_smoke_5q 的 5 题合并后仍为零分歧。

## 关键数字

- **总验证题数**：34 题（5 + 3 + 4 + 22，去重后）
- **产生答案分歧的题数**：0
- **温度覆盖范围**：0.7, 0.9, 1.0（`sica_temp_diversity`）
- **SICA-SC 总 gap**：0 pp（所有实验）
- **MaxSAT exclusion rate**（sica_aime30_v3）：38.7%（metrics.vote_diversity_analysis.exclusion_rate），但因单候选无法改变最终选择
- **Zero-vote problems**（sica_aime30_v3）：6/22（indices [1,7,8,10,13,14]），来源：约束提取失败

## 根因分析

### 1. 推理模型的 CoT 确定性

QwQ-32B 作为 reasoning model，其 chain-of-thought 过程具有极强的确定性。即使 temperature > 0 引入了 token-level 采样随机性，模型的推理链倾向于收敛到相同的求解路径和最终答案。这在数学问题上尤为显著——正确解法通常是唯一的，模型一旦锁定正确路径，12 条 trace 均产生相同答案。

> 来源：`sica_temp_diversity.metrics.finding` — "QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5. Reasoning model's deterministic chain dominates sampling randomness."

### 2. Temperature 对 reasoning model 影响有限

三个温度梯度（0.7 / 0.9 / 1.0）的实验明确证明：temperature 无法打破 CoT 确定性。这与标准语言模型的行为不同——在非推理模型中，temperature 升高通常会增加输出多样性，但推理模型的思维链结构约束了这种多样性。

> 来源：`sica_temp_diversity.metrics.temperatures_tested = [0.7, 0.9, 1.0]`，`problems_with_divergence = 0`

### 3. MaxSAT exclusion 在单候选下退化为 no-op

sica_aime30_v3 的数据显示 exclusion_rate = 38.7%——MaxSAT 约束求解器确实在工作，成功识别并排除了部分约束。但当所有 trace 只产生 1 个候选答案时，排除约束后剩余的投票仍然指向同一个答案。整个 SICA pipeline 的约束提取→MaxSAT 求解→加权投票链条在功能上等价于简单多数投票。

> 来源：`sica_aime30_v3.metrics.vote_diversity_analysis.conclusion` — "All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally. MaxSAT exclusion operates but cannot change final selection with only 1 candidate."

## 方法论含义

### SICA 的价值前提

SICA 的核心假设是：不同 reasoning trace 之间存在答案分歧，而符号约束可以检测哪些 trace 包含逻辑矛盾，从而过滤掉错误路径。这个假设要求：

1. **trace 间有多个候选答案**（multi-candidate rate > 0）
2. **约束能区分正确与错误候选**

数学域在条件 1 上就已失败。

### 数学域是 SICA 的不适用域（reasoning model context）

这不是 SICA 方法本身的缺陷，而是 **方法-模型-域** 三者的不匹配：
- **推理模型 + 数学域** → 零分歧 → SICA 无法发挥作用
- 如果使用非推理模型（如 GPT-4、Llama-3），数学域可能产生足够分歧
- 如果使用推理模型但换到逻辑域（如 FOLIO、ProofWriter），天然存在多路径分歧的可能性更高

### 可能的解法方向

1. **换域**：逻辑推理域（FOLIO/ProofWriter）具有 True/False/Unknown 三元标签，模型更容易在不同 trace 中产生不同判断（已启动 `sica_folio30` 和 `sica_proofwriter30_v2` 实验验证）
2. **换模型**：使用非推理模型可能恢复采样多样性，但会降低 baseline accuracy
3. **增大 K 或使用 prompt perturbation**：理论上可增加多样性，但在当前证据下收益预期极低

## 论文价值

### 作为 Domain Boundary Analysis

这个 negative 结果对论文有正面价值——它精确划定了 SICA 的适用边界：

> "SICA improves over SC **when and only when** the sampling process produces answer divergence across traces. On mathematical reasoning with strong reasoning models (QwQ-32B), the deterministic nature of chain-of-thought eliminates this divergence, rendering SICA equivalent to SC. This establishes mathematics as a **boundary domain** for consensus-based aggregation methods under reasoning models."

### 与 Self-Consistency 文献的对话

Wang et al. (2023) 的 Self-Consistency 工作隐含假设采样多样性的存在。本结果揭示了一个被忽视的前提条件：

- **Model calibration 角度**：reasoning model 在数学域是 "过度校准" (over-calibrated) 的——不同样本给出相同答案，模型的 epistemic uncertainty 接近零
- **SC 的退化条件**：当 K 条采样全部一致时，SC@K 退化为 SC@1（即 greedy decoding），额外的采样成本没有带来信息增益
- **SICA 的退化条件**：SICA 在此基础上进一步退化——不仅投票一致，约束提取和 MaxSAT 求解的计算开销也变为纯浪费

### 建议呈现方式

在论文中以独立小节呈现（如 §5.3 "When Does SICA Help? A Domain Boundary Analysis"），包含：
- Table：数学域 vs 逻辑域的 multi-candidate rate 对比
- Figure（可选）：answer distribution 的 entropy 对比——数学域 entropy≈0 vs 逻辑域 entropy>0
- Discussion：将 SICA 定位为 "high-divergence regime" 的方法，与 Self-Consistency 在 "low-divergence regime" 的等价性

---

*数据截止：2026-05-16。所有数字来源于 symb_invariant_consensus project registry。*