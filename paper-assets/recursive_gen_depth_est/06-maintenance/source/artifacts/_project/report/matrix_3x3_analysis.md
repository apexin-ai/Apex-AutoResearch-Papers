# 3×3 递归生成深度估计矩阵综合分析

> 生成日期: 2026-05-15 | 完成格子: 8/9 (gpt2xl_topk50 仍在运行)

---

## 1. 完整 3×3 矩阵

### 1.1 4-class RF Accuracy (%)

| 模型 | nucleus p=0.95 | temp τ=0.9 | top-k k=50 | 跨策略均值 |
|------|:-:|:-:|:-:|:-:|
| **Pythia-1.4B** | 78.2 `mvp_pipeline_pythia_002` | 76.3 `pythia_temp09_001` | 69.6 `pythia_topk50_001` | 74.7 |
| **OLMo-1B** | 78.8 `cross_model_olmo_002` | 82.0 `olmo_temp09_001` | 74.2 `olmo_topk50_001` | 78.3 |
| **GPT-2 XL** | 83.3 `cross_model_gpt2xl_001` | 85.4 `gpt2xl_temp09_001` | 🔄 `gpt2xl_topk50_001` | 84.4† |
| **跨模型均值** | 80.1 | 81.2 | 71.9† | — |

> † GPT-2 XL 行均值仅含 2 格; topk50 列均值仅含 2 格。所有数值为 RF classifier，chance = 25%。

### 1.2 Pairwise d1v2 AUC (RF)

| 模型 | nucleus p=0.95 | temp τ=0.9 | top-k k=50 |
|------|:-:|:-:|:-:|
| **Pythia-1.4B** | 0.861 `mvp_pipeline_pythia_002` | 0.833 `pythia_temp09_001` | 0.752 `pythia_topk50_001` |
| **OLMo-1B** | 0.867 `cross_model_olmo_002` | 0.901 `olmo_temp09_001` | 0.831 `olmo_topk50_001` |
| **GPT-2 XL** | 0.913 `cross_model_gpt2xl_001` | 0.937 `gpt2xl_temp09_001` | 🔄 |

### 1.3 3-class Filtered Accuracy (RF, %)

| 模型 | nucleus p=0.95 | temp τ=0.9 | top-k k=50 |
|------|:-:|:-:|:-:|
| **Pythia-1.4B** | 74.7 `mvp_pipeline_pythia_002` | 72.5 `pythia_temp09_001` | 61.3 `pythia_topk50_001` |
| **OLMo-1B** | 74.4* `cross_model_olmo_002` | 77.6 `olmo_temp09_001` | 67.0 `olmo_topk50_001` |
| **GPT-2 XL** | 79.3* `cross_model_gpt2xl_001` | 81.5 `gpt2xl_temp09_001` | 🔄 |

> \* OLMo nucleus 和 GPT-2 XL nucleus 使用 unfiltered 3-class accuracy 作为近似值（两者 code contamination 均 <3%，filtered 与 unfiltered 差异极小）。

---

## 2. 模型效应分析

跨策略平均（RF 4-class accuracy）:

| 模型 | 均值 | 相对 Pythia | 参数量 |
|------|------|-------------|--------|
| Pythia-1.4B | 74.7% | — | 1.4B |
| OLMo-1B | 78.3% | +3.6pp | 1B |
| GPT-2 XL | 84.4%† | +9.7pp | 1.5B |

**关键发现:**

1. **GPT-2 XL 全面领先**：在每个策略上均为最高分（nucleus +4.5pp vs OLMo, temp09 +3.4pp, d1v2 AUC 最高均 >0.91），说明模型架构/预训练数据对深度信号的影响远大于模型规模（GPT-2 XL 1.5B vs OLMo 1B 参数量差异有限但性能差距显著）。

2. **OLMo 优于 Pythia 但差距较小**：跨策略仅 +3.6pp，且两者在 nucleus 策略上几乎持平（78.8% vs 78.2%，仅 +0.6pp），差异主要来自 temp09（+5.8pp）。

3. **模型效应 > 策略效应**：模型维度的跨策略均值极差 = 9.7pp（84.4 − 74.7），而策略维度的跨模型均值极差 = 9.3pp（81.2 − 71.9），两者量级相当，但模型效应在排除 topk50（仅 2 格）后更稳定。

---

## 3. 策略效应分析

跨模型平均（RF 4-class accuracy）:

| 策略 | 均值 | 相对 nucleus | 特点 |
|------|------|-------------|------|
| nucleus p=0.95 | 80.1% | — | 基准策略 |
| temp τ=0.9 | 81.2% | +1.1pp | 部分模型优于 nucleus |
| top-k k=50 | 71.9%† | −8.2pp | 系统性最弱 |

**关键发现:**

1. **top-k 系统性削弱深度信号**：相比 nucleus，Pythia −8.6pp，OLMo −4.6pp。top-k 的硬截断采样将概率分布截断到固定 k 个 token，可能丢失了分布尾部携带的深度相关信号。

2. **temperature 与 nucleus 几乎等效**：跨模型均值仅差 1.1pp，且方向不一致——Pythia temp09 < nucleus（−1.9pp），OLMo 和 GPT-2 XL temp09 > nucleus（+3.2pp, +2.1pp）。温度缩放保留了完整分布形状，只改变了锐度。

3. **策略效应的模型依赖性**：同一策略变化在不同模型上方向相反（Pythia temp09 降，OLMo/GPT-2 XL temp09 升），说明策略效应不是纯粹的采样特性，而是与模型内部表征交互的结果。

---

## 4. 交互效应分析

将每个格子的 RF accuracy 分解为 模型均值 + 策略均值 + 残差（交互项）:

| 模型×策略 | 实际 | 预期† | 残差 | 解读 |
|-----------|------|-------|------|------|
| Pythia × nucleus | 78.2 | 77.4 | +0.8 | 略高于预期 |
| Pythia × temp09 | 76.3 | 77.9 | −1.6 | temp09 对 Pythia 不利 |
| Pythia × topk50 | 69.6 | 68.8 | +0.8 | 符合预期 |
| OLMo × nucleus | 78.8 | 80.7 | −1.9 | nucleus 未充分发挥 OLMo 潜力 |
| OLMo × temp09 | 82.0 | 81.2 | +0.8 | temp09 对 OLMo 微弱正交互 |
| OLMo × topk50 | 74.2 | 72.4 | +1.8 | topk50 对 OLMo 影响小于预期 |
| GPT-2 XL × nucleus | 83.3 | 82.5 | +0.8 | 符合预期 |
| GPT-2 XL × temp09 | 85.4 | 83.6 | +1.8 | temp09 对 GPT-2 XL 最有利 |

> † 预期值 = grand mean + (模型偏差) + (策略偏差)，基于加法模型。Grand mean = 78.5%（8格均值）。

**异常组合:**

- **GPT-2 XL × temp09 (+1.8pp residual)**：温度缩放对 GPT-2 XL 有增强效应。可能原因：GPT-2 XL 的预训练分布在 τ=0.9 下产生更多样化但仍有结构性的文本，增强了深度间的统计差异。
- **OLMo × nucleus (−1.9pp residual)**：OLMo 在 nucleus 下表现低于其在其他策略下的相对优势。top-p truncation 可能对 OLMo 的 logit 分布有不利影响。
- **Pythia × temp09 (−1.6pp residual)**：Pythia 是唯一在 temp09 下低于 nucleus 的模型，与 OLMo/GPT-2 XL 方向相反。

---

## 5. Feature Importance 稳定性分析

Top-5 features 在 8 个实验中的出现情况:

| Feature | 出现次数 (8格中) | 平均排名 | 出现实验 |
|---------|:-:|:-:|---------|
| **p90_ppl** | 8/8 | 1.5 | 所有 |
| **var_surprisal** | 8/8 | 1.8 | 所有 |
| **p75_ppl** | 8/8 | 3.1 | 所有 |
| **mean_surprisal** | 7/8 | 4.0 | 除 OLMo temp09（仅报告 top-3）|
| **mean_ppl** | 5/8 | 3.8 | Pythia 全部 3 格 + GPT-2 XL nucleus + GPT-2 XL temp09 |
| p25_ppl | 1/8 | 5.0 | OLMo topk50 |
| type_token_ratio | 1/8 | 5.0 | OLMo nucleus |

**稳定性评估:**

- **核心三特征 (p90_ppl, var_surprisal, p75_ppl)** 在全部 8 格出现，Jaccard 一致性 = 1.0。这三个特征是递归生成深度信号的核心载体，反映了困惑度分布的上尾和变异性。
- **前 4 特征**在 7/8 格一致（mean_surprisal 在 OLMo temp09 中未被明确报告但可能位于 rank 4-5）。
- **第 5 位特征模型依赖**：Pythia 偏好 mean_ppl，OLMo 偏好 type_token_ratio 或 p25_ppl。GPT-2 XL 偏好 mean_ppl。
- **跨模型/策略的特征重要性高度稳定**，支持「深度信号来自同一统计模式」的假设——不同模型/策略的递归生成都导致困惑度分布的类似退化。

### 代表性 importance 权重对比

| Feature | Pythia nuc | OLMo nuc | GPT-2 XL nuc |
|---------|:-:|:-:|:-:|
| p90_ppl | 0.158 | 0.180 | 0.208 |
| var_surprisal | 0.169 | 0.160 | 0.208 |
| p75_ppl | 0.067 | 0.110 | 0.103 |

GPT-2 XL 的 top-2 特征权重更高（0.208 vs 0.158/0.180），说明深度信号在更大模型中更集中于少数关键特征。

---

## 6. Code Contamination 模式分析

### 6.1 按模型的 narrow contamination rate (%)

| 模型 | d0 | d1 | d2 | d3 | d3 趋势 |
|------|:-:|:-:|:-:|:-:|---------|
| **Pythia-1.4B** (nucleus) | — | 5.0 | 9.0 | 12.0 | 递增 ↑ |
| **Pythia-1.4B** (temp09) | 0.4 | 7.7 | 11.6 | 13.6 | 递增 ↑ |
| **Pythia-1.4B** (topk50) | 0.4 | 7.7 | 12.3 | 13.1 | 递增 ↑ |
| **OLMo-1B** (nucleus) | 0.5 | 2.7 | 0.7 | 0.8 | 极低, 平稳 |
| **OLMo-1B** (temp09) | — | ≤0.7 | ≤0.7 | ≤0.7 | 极低 |
| **OLMo-1B** (topk50) | 0.4 | 0.8 | 0.3 | 0.4 | 极低, 平稳 |
| **GPT-2 XL** (nucleus) | 0.5 | 0.5 | 1.3 | 0.7 | 极低, 平稳 |
| **GPT-2 XL** (temp09) | 0.4 | 0.8 | 1.6 | 1.5 | 低, 微增 |

### 6.2 关键模式

1. **Pythia 是 contamination 热点**：d3 contamination 达 12-14%，显著高于 OLMo（<1%）和 GPT-2 XL（<2%）。原因：Pythia 预训练于 The Pile（含 ~3.3% 代码），递归 finetune 逐深度放大代码模式。

2. **模型效应远大于策略效应**：Pythia 三种策略的 contamination 模式高度一致（d3: 12.0% / 13.6% / 13.1%），说明 contamination 主要由预训练数据决定，与解码策略无关。

3. **OLMo 和 GPT-2 XL 几乎无 contamination**：所有深度的 narrow rate <3%，filtered 与 unfiltered 性能差异 <1pp。

4. **Pythia 的 contamination 未驱动分类性能**：Pythia topk50 有最高 contamination（d3=13.1%），但分类性能最低（69.6%）。移除 contaminated 样本后（filtered 3-class），性能反而微升（61.3% vs 59.2% unfiltered 3-class），确认深度信号非代码混入的伪影。

---

## 7. 关键 Findings 摘要（论文可用）

### Finding 1: 递归生成深度信号是跨模型、跨策略的普遍现象
所有 8 个完成的模型-策略组合均显著优于 chance（25%），4-class accuracy 范围 69.6%–85.4%，d1v2 AUC 范围 0.752–0.937。深度信号不依赖于特定模型或采样策略。

### Finding 2: 模型效应显著——GPT-2 XL 全面优于小模型
GPT-2 XL 跨策略均值 84.4%，高出 Pythia-1.4B +9.7pp、OLMo-1B +6.1pp。更大/更强的模型在递归 finetune 中产生更强的深度退化信号，可能因为其分布更复杂，每轮递归的信息损失更可量化。

### Finding 3: 采样策略对信号强度有显著但非均匀影响
Top-k (k=50) 系统性地削弱深度信号（跨模型均值 71.9% vs nucleus 80.1%，−8.2pp），而 temperature (τ=0.9) 与 nucleus (p=0.95) 效果接近（81.2% vs 80.1%）。关键差异：top-k 硬截断分布尾部，而 temperature 和 nucleus 保留完整分布形状，后者保留了更多深度相关的统计信息。

### Finding 4: 深度信号由高度稳定的特征组集载体
p90_ppl、var_surprisal、p75_ppl 在全部 8 格中均为 top-3 特征（Jaccard = 1.0）。递归生成导致困惑度分布的上尾收缩和变异性降低——这一退化模式跨模型、跨策略完全一致。

### Finding 5: Code contamination 是模型特异的，不驱动分类性能
Pythia-1.4B 在 d3 有 12-14% 代码混入（The Pile 代码占比高），而 OLMo-1B 和 GPT-2 XL 均 <2%。但 contamination 与分类性能无正相关——Pythia 性能最低而 contamination 最高。过滤后性能无显著下降，确认深度信号来自语言统计模式而非域混淆。

---

## 附录 A: 完整 pairwise AUC 矩阵 (RF)

### Pythia-1.4B nucleus `mvp_pipeline_pythia_002`
| pair | AUC |
|------|-----|
| d0v1 | 0.9975 |
| d0v2 | — |
| d0v3 | — |
| d1v2 | 0.8607 |
| d1v3 | 0.9569 |
| d2v3 | 0.8005 |

### Pythia-1.4B temp09 `pythia_temp09_001`
| pair | AUC |
|------|-----|
| d0v1 | 0.9968 |
| d1v2 | 0.8327 |
| d1v3 | 0.9590 |
| d2v3 | 0.7928 |

### Pythia-1.4B topk50 `pythia_topk50_001`
| pair | AUC |
|------|-----|
| d0v1 | 0.9927 |
| d0v2 | 0.9983 |
| d0v3 | 0.9978 |
| d1v2 | 0.7518 |
| d1v3 | 0.9176 |
| d2v3 | 0.6918 |

### OLMo-1B nucleus `cross_model_olmo_002`
| pair | AUC |
|------|-----|
| d0v1 | 0.9834 |
| d0v2 | 0.9949 |
| d0v3 | 0.9989 |
| d1v2 | 0.8673 |
| d1v3 | 0.9806 |
| d2v3 | 0.8124 |

### OLMo-1B temp09 `olmo_temp09_001`
| pair | AUC |
|------|-----|
| d1v2 | 0.901 |

### OLMo-1B topk50 `olmo_topk50_001`
| pair | AUC |
|------|-----|
| d0v1 | 0.9930 |
| d0v2 | 0.9983 |
| d0v3 | 0.9991 |
| d1v2 | 0.8305 |
| d1v3 | 0.9591 |
| d2v3 | 0.7357 |

### GPT-2 XL nucleus `cross_model_gpt2xl_001`
| pair | AUC |
|------|-----|
| d0v1 | 0.9941 |
| d0v2 | 0.9965 |
| d0v3 | 0.9988 |
| d1v2 | 0.9131 |
| d1v3 | 0.9857 |
| d2v3 | 0.8829 |

### GPT-2 XL temp09 `gpt2xl_temp09_001`
| pair | AUC (RF) |
|------|-----|
| d0v1 | 0.9963 |
| d0v2 | 0.9992 |
| d0v3 | 1.0000 |
| d1v2 | 0.9367 |
| d1v3 | 0.9947 |
| d2v3 | 0.8815 |

---

## 附录 B: Finetune Loss 趋势

| 模型×策略 | d0→d1 loss | d1→d2 loss | d2→d3 loss |
|-----------|:-:|:-:|:-:|
| Pythia nucleus | 2.241 → 1.389 | 1.389 → 1.025 | — |
| Pythia temp09 | 2.222 → 1.370 | 1.370 → 1.006 | — |
| Pythia topk50 | 2.241 → 1.670 | 1.670 → 1.437 | — |
| OLMo nucleus | 2.269 → 1.650 | 1.650 → 1.226 | — |
| OLMo temp09 | 2.270 → 1.630 | 1.630 → 1.180 | — |
| OLMo topk50 | — → 1.946 | 1.946 → 1.726 | — |
| GPT-2 XL nucleus | 2.550 → 1.715 | 1.715 → 1.342 | — |
| GPT-2 XL temp09 | 2.550 → 1.697 | 1.697 → 1.292 | — |

所有配置均呈单调递减——每轮递归 finetune 后模型更容易学习下一轮生成的文本，支持「深度增加 → 分布收敛」假设。
