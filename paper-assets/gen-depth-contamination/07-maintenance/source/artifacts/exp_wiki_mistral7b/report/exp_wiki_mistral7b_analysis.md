# exp_wiki_mistral7b 分析

## 结论
K* = 1 | conclusion = success

Mistral-7B-v0.3 在 Wikipedia domain 上表现为 one-wash model，与 C4 结果一致（K*=1），与 arXiv 结果（K*=3）形成对比。支持 domain-dependent K* 假说。

## 核心指标

### Pairwise AUC（相邻 depth 可区分性，5-fold CV）

| Depth Pair | AUC (mean) | AUC (std) | Folds |
|------------|-----------|-----------|-------|
| 0 vs 1 | **0.9607** | 0.0023 | [0.9585, 0.9638, 0.9625, 0.9576, 0.9610] |
| 1 vs 2 | 0.5552 | 0.0114 | [0.5608, 0.5451, 0.5443, 0.5509, 0.5747] |
| 2 vs 3 | 0.5236 | 0.0105 | [0.5280, 0.5415, 0.5120, 0.5216, 0.5148] |
| 3 vs 4 | 0.5181 | 0.0053 | [0.5134, 0.5212, 0.5207, 0.5247, 0.5105] |
| 4 vs 5 | 0.5012 | 0.0094 | [0.5051, 0.4939, 0.4965, 0.4926, 0.5179] |

### Pairwise JSD

| Depth Pair | JSD |
|------------|-----|
| 0 vs 1 | 0.054134 |
| 1 vs 2 | 0.005678 |
| 2 vs 3 | 0.003698 |
| 3 vs 4 | 0.003459 |
| 4 vs 5 | 0.003274 |

### Ordinal Classification（6-class, 5-fold CV）

| Metric | Value |
|--------|-------|
| Ordinal MAE | 1.3445 |
| Accuracy | 0.3273 |

### Top-10 Feature Importance

| Feature | Importance |
|---------|-----------|
| freq_entropy | 9129.0 |
| surp_mean | 8815.6 |
| surp_d1_skew | 7958.2 |
| surp_std | 7880.6 |
| surp_d1_mean | 7737.6 |
| surp_d2_mean | 7701.4 |
| freq_kurtosis | 7697.8 |
| ttr | 7126.0 |
| hapax_ratio | 7081.4 |
| surp_kurt | 6980.2 |

## K* 判定依据

K* 定义：最大 depth k 使得 gen_k vs gen_{k+1} 的 pairwise AUC > 0.60。

- **depth 0 vs 1: AUC = 0.9607** — 极强可区分性。原始文本与首轮生成之间存在巨大分布差异。JSD = 0.054 远高于其他对。
- **depth 1 vs 2: AUC = 0.5552** — 接近 chance level (0.50)。JSD 从 0.054 骤降至 0.006，降幅达 9.5 倍。分类器几乎无法区分。
- **depth 2-5: AUC 0.50-0.52** — 完全不可区分。JSD 稳定在 0.003-0.004 范围，无系统性趋势。

判定：K* = 1。仅 depth 0 vs 1 可区分，depth 1 之后所有生成已完全饱和。这是典型的 one-wash pattern：模型一次生成就抹除了源文本的统计指纹。

## 与已知结果对比

### vs Mistral-7B 其他 domain
| Domain | K* | Pattern |
|--------|-----|---------|
| C4 | 1 | one-wash |
| **Wikipedia** | **1** | **one-wash** |
| arXiv | 3 | domain rescue |

Wikipedia 与 C4 结果完全一致，arXiv 是唯一展现 domain rescue 的 domain。

### vs 其他模型 Wikipedia 结果
| Model | Wikipedia K* | Pattern |
|-------|-------------|---------|
| Pythia | 1 | one-wash |
| OLMo | 1 | one-wash |
| Qwen-1.5B | 2 | mild rescue |
| LLaMA-8B | 1 | negative |
| **Mistral-7B** | **1** | **one-wash** |

Mistral-7B Wikipedia K*=1 与大多数模型一致。Wikipedia 上仅 Qwen-1.5B 展现 K*=2 的 mild rescue。

## 对论文 framing 的影响

1. **强化 domain-dependent K* narrative**：Mistral-7B 在 Wikipedia（K*=1）和 C4（K*=1）上一致 one-wash，而在 arXiv（K*=3）上 domain rescue。这支持核心论点：K* 取决于 domain 与预训练数据的重叠程度，而非模型本身的固有属性。

2. **Wikipedia 作为 "well-represented domain" 的佐证**：Wikipedia 是几乎所有 LLM 预训练语料的核心组成部分。K*=1 的结果符合预期：模型对 Wikipedia 风格文本高度熟悉，一次生成即收敛到模型自身分布。

3. **arXiv 的特殊性更加突出**：在所有测试的 model-domain 组合中，arXiv 是唯一反复展现 K*>1 的 domain。这强化了 arXiv 作为 "specialized/underrepresented domain" 的 positioning，其专业术语和格式为模型提供了更持久的统计锚点。

4. **实验矩阵更加完整**：Mistral-7B 现在有 3 个 domain 的完整数据（C4, Wikipedia, arXiv），是跨 domain K* 比较最丰富的模型，适合作为论文核心案例。
