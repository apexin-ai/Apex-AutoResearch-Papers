# binary_correct vs text_exact_match 双变量深度分析

**数据来源**: MVP Phase A — Llama-3.1-8B-Instruct, 108 conditions × 50 items = 5,400 observations  
**日期**: 2026-05-20

## 1. 方差分解对比表

按 binary_correct 占比降序排列：

| Component | binary_correct (%) | text_exact_match (%) | Δ (text − binary) |
|---|---:|---:|---:|
| item_id | **58.44** | 0.00 | −58.44 |
| residual | **17.59** | **40.67** | +23.08 |
| precision:item_id | 7.24 | 0.63 | −6.61 |
| temperature:item_id | 6.85 | 2.47 | −4.38 |
| prompt_template:item_id | 5.73 | **37.46** | +31.73 |
| seed:item_id | 2.70 | 0.00 | −2.70 |
| precision | 0.87 | 0.00 | −0.87 |
| ordering:item_id | 0.44 | 0.30 | −0.14 |
| temperature:seed | 0.04 | 0.00 | −0.04 |
| prompt_template | 0.03 | 0.00 | −0.03 |
| precision:prompt_template | 0.02 | 0.01 | −0.01 |
| temperature:ordering | 0.02 | 0.00 | −0.02 |
| precision:ordering | 0.00 | 0.02 | +0.02 |
| prompt_template:ordering | 0.01 | 0.07 | +0.06 |
| temperature:prompt_template | 0.00 | 0.24 | +0.24 |
| precision:temperature | 0.00 | **1.26** | +1.26 |
| temperature | 0.00 | **16.86** | +16.86 |
| seed | 0.00 | 0.00 | 0.00 |
| ordering | 0.00 | 0.00 | 0.00 |
| precision:seed | 0.00 | 0.00 | 0.00 |
| prompt_template:seed | 0.00 | 0.00 | 0.00 |
| seed:ordering | 0.00 | 0.00 | 0.00 |

**Total variance**: binary = 0.2298, text = 0.1503

## 2. 关键发现

1. **两个 metric 测量的是完全不同的构念。** binary_correct 以 item 难度为主导（58.4%），衡量的是"能否答对"；text_exact_match 以 prompt_template:item_id 交互（37.5%）和 temperature（16.9%）为主导，衡量的是"输出文本是否确定性一致"。二者的方差结构几乎没有重叠。

2. **Temperature 对准确性几乎无影响，但对确定性有决定性影响。** temp=0.0 时 text_exact_match 均值为 0.247，temp=0.5 时骤降至 0.019（降 92%）。而 binary_correct 仅从 0.643 微升至 0.669。这说明 temperature 引入的采样随机性改变了文字表述但几乎不改变最终选择的答案字母。

3. **Prompt template 对答案正确性影响极小（0.03%），但对文本确定性有巨大的 item-specific 效应（37.5%）。** 不同 prompt 模板导致模型对不同 item 产生不同的文本表述模式，但最终提取的答案字母大致稳定。

4. **Item-level 无显著相关。** 两个 metric 在 item 水平的 Spearman ρ = −0.214（p = 0.135），说明一个 item 答对率高并不意味着其输出更确定，反之亦然。

5. **Float32 在两个 metric 上都表现最差。** bc_mean = 0.599（vs bf16/fp16 ≈ 0.684），tem_mean = 0.097（vs ≈ 0.150）。这可能与该精度下模型行为的某种系统性差异有关。

## 3. Item-Level 不一致性分析

最不一致的 10 个 items（bc_mean − tem_mean 差值最大）：

| Item | Subject | binary_correct | text_exact_match | Δ |
|---|---|---:|---:|---:|
| professional_medicine_49 | Prof. Medicine | 1.000 | 0.074 | +0.926 |
| professional_medicine_193 | Prof. Medicine | 1.000 | 0.083 | +0.917 |
| professional_medicine_135 | Prof. Medicine | 1.000 | 0.102 | +0.898 |
| us_foreign_policy_27 | US Foreign Policy | 1.000 | 0.102 | +0.898 |
| abstract_algebra_31 | Abstract Algebra | 0.991 | 0.102 | +0.889 |
| us_foreign_policy_54 | US Foreign Policy | 1.000 | 0.111 | +0.889 |
| us_foreign_policy_97 | US Foreign Policy | 1.000 | 0.111 | +0.889 |
| world_religions_6 | World Religions | 1.000 | 0.111 | +0.889 |
| world_religions_150 | World Religions | 1.000 | 0.120 | +0.880 |
| world_religions_114 | World Religions | 1.000 | 0.130 | +0.870 |

**模式**: 所有 top-10 不一致 items 都是 bc_mean ≈ 1.0 但 tem_mean 极低的"高准确-低确定"型。模型几乎总是选对答案字母，但每次生成的解释文本都不同。没有出现反向模式（低准确-高确定），这说明 text_exact_match 的 baseline 本身就很低（overall mean = 0.133）。

**整体 text_exact_match 均值只有 13.3%**，说明即使在 temp=0 的条件下，模型输出的 verbatim 一致性也很低。这是因为 text_exact_match 对模型的"canonical"输出是以多数票定义的，而 108 个条件中包含了大量 prompt template 和精度组合，每种组合都倾向于产生不同的文本。

## 4. Facet-Level 条件均值

### Precision
| Level | binary_correct | text_exact_match |
|---|---:|---:|
| bfloat16 | 0.684 | 0.152 |
| float16 | 0.683 | 0.149 |
| float32 | 0.599 | 0.097 |

### Temperature
| Level | binary_correct | text_exact_match |
|---|---:|---:|
| 0.0 | 0.643 | **0.247** |
| 0.5 | 0.669 | **0.019** |

### Prompt Template
| Level | binary_correct | text_exact_match |
|---|---:|---:|
| 1 | 0.663 | 0.142 |
| 2 | 0.671 | 0.126 |
| 3 | 0.633 | 0.131 |

### Seed
| Level | binary_correct | text_exact_match |
|---|---:|---:|
| 42 | 0.661 | 0.132 |
| 123 | 0.649 | 0.135 |
| 456 | 0.658 | 0.132 |

### Ordering
| Level | binary_correct | text_exact_match |
|---|---:|---:|
| 1 | 0.657 | 0.138 |
| 2 | 0.654 | 0.128 |

## 5. 对 exp-001 的 Implications

### 两个 metric 应该继续同时用吗？

**是的，必须同时保留。** 两个 metric 测量完全不同的维度：
- **binary_correct** 测量评估的 *有效性*（evaluation validity）— 模型是否真的能答对这道题
- **text_exact_match** 测量评估的 *可复现性*（evaluation reproducibility）— 在不同实验条件下，模型输出是否一致

G-theory 的核心价值在于同时量化这两个维度的方差来源。一个 G 系数高的 metric 意味着该维度可以用较少的条件数达到可靠测量。

### text_exact_match 是否足以替代 binary_correct？

**不能替代。** 原因：
1. 两者的 Spearman 相关不显著（ρ = −0.21），说明它们提供正交信息
2. text_exact_match 的 overall mean 只有 13.3%，variance 主要来自 prompt × item 交互和 temperature，而非 item 本身的特征 — 它更多反映了"实验条件的影响"而非"item 的内在属性"
3. binary_correct 的 G = 0.357（偏低，需要更多条件），text_exact_match 的 G = 0.975（已经很高）— 这反映的不是 text 更好，而是 text 的方差主要由可控的 facet 解释，残差占比相对较小

### 实验设计启示

- **Temperature 是 text_exact_match 的关键控制变量**：如果关注文本确定性，必须固定 temperature（最好为 0）
- **Prompt template 的 item-specific 效应巨大**：不同 prompt 对不同 item 的文本输出影响差异极大（37.5%），在扩展到更多 prompt 变体时需要充分交叉
- **binary_correct 的 G 系数偏低（0.357）主要因为 item 难度方差太大**：50 个 items 跨 5 个 subject，难度分布极不均匀。D-study 应探索按 subject 分层采样或增加 item 数量

## 6. 图表

- **Figure 1**: [Variance Decomposition Comparison](fig1_variance_decomposition_comparison.png)
- **Figure 2**: [Item-Level Scatter (Accuracy vs Determinism)](fig2_item_scatter.png)
- **Figure 3**: [Facet-Level Mean Heatmap](fig3_facet_heatmap.png)
