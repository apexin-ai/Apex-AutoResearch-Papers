# 3. Methodology

## 3.1 Multi-generation Corpus Construction

### 问题形式化

设 $X_0$ 为人类撰写的文本（seed text），建模为概率空间上的随机变量。LLM 的生成过程定义为随机信道 $\mathcal{T}: \mathcal{X} \to \mathcal{X}$，将输入文本映射到输出文本。递归生成形成 Markov chain：

$$X_0 \xrightarrow{\mathcal{T}} X_1 \xrightarrow{\mathcal{T}} X_2 \xrightarrow{\mathcal{T}} \cdots \xrightarrow{\mathcal{T}} X_K$$

其中 depth-0 文本 $X_0$ 为人类原始文本，depth-$k$ 文本 $X_k = \mathcal{T}(X_{k-1})$ 由 depth-$(k-1)$ 文本经过一次 LLM 信道产生。该形式化依赖两个关键假设：**(A1) 时不变信道**——同一 LLM 与 decoding strategy 在每次迭代中定义相同的信道 $\mathcal{T}$；**(A2) Markov 性**——$X_{k+1}$ 仅依赖 $X_k$，不依赖更早的 $X_0, \ldots, X_{k-1}$。这两个假设在 prompt-chain 设定下成立（每次生成仅以上一轮输出为输入），retrain-chain 场景需将 $\mathcal{T}$ 放宽为 $\mathcal{T}_k$。

### Prompt-chain 实现

我们采用 prompt-chain 方式构造 depth chain：每一轮将前一深度的文本嵌入固定的 rewrite prompt 模板，由模型生成同主题、同风格的新文本。具体 prompt 模板如下：

> Below is a passage. Write a new passage of similar length on the same topic and in the same style.
>
> Original passage:
> {prev\_text}
>
> New passage:

该模板要求模型保持主题与风格一致性，同时生成全新文本而非简单复述。这一设计的意图是模拟现实场景中合成文本被反复改写的过程——例如 AI 生成的内容被爬取后再次作为 LLM 的输入进行改写或续写。

Prompt-chain 与 retrain-chain（在合成数据上重新训练模型再生成）的区别值得说明。Retrain-chain 更接近 Shumailov et al. [2024] 描述的 model collapse 真实路径，但 prompt-chain 提供了一个 **upper bound estimate**：如果在 prompt-chain（模型权重不变、仅输入文本退化）下特征已饱和，retrain-chain（模型本身也退化）下只会更快饱和。我们选择 prompt-chain 作为 MVP 方案以控制变量，retrain-chain 验证留作后续研究。

### 模型选择

我们选用 **Qwen2.5-1.5B-Instruct** [Qwen Team, 2024] 作为生成模型。选择理由如下：

**Instruct 而非 base 模型**。现实世界中绝大多数合成文本（ChatGPT 输出、AI 写作工具、自动摘要等）均来自经过 instruction tuning 的模型。使用 Instruct 版本可确保生成文本的分布特征更接近实际污染数据。此外，Instruct 模型能更好地遵循 rewrite prompt 中的改写指令，生成主题一致但非直接复制的文本，而 base 模型可能简单延续原文或产生不相关内容。

**1.5B 参数规模**。选择小规模模型基于以下考量：(1) 计算效率——在单块 RTX 4090D (24GB) 上可高效完成 5000 文档 × 5 个深度的生成任务；(2) model collapse 文献 [Shumailov et al., 2024; Drayson et al., 2025] 表明退化现象在小模型上更为显著，有利于在 pilot study 中观察清晰的深度信号；(3) Qwen2.5 系列在 1.5B 规模上已展现出 competitive 的语言能力 [需验证]，足以生成流畅且有意义的文本。Full study 阶段将扩展到多模型家族（Pythia-1.4B, OLMo-1B）及更大规模（Qwen2.5-7B/14B）进行 cross-model 和 cross-scale 验证。

### 解码参数

采用 **nucleus sampling** (top-$p$ sampling)，参数设定为 $p = 0.95$, temperature $T = 1.0$。这一配置的理由在于：

(1) **接近真实世界配置**。主流 LLM 应用（ChatGPT、Claude、各类 API 调用）的默认或推荐生成参数通常处于 $T \in [0.7, 1.0]$, $p \in [0.9, 0.95]$ 的区间。$T=1.0, p=0.95$ 代表了一个 moderately stochastic 的生成配置，既保留了足够的随机性以反映真实合成文本的 diversity，又不至于因过高 temperature 产生不自然的噪声文本。

(2) **信道噪声的理论考量**。在信道级联框架下，$T$ 和 $p$ 共同决定了信道 $\mathcal{T}$ 的 contraction rate $\rho$。Greedy decoding ($T \to 0$) 使信道趋近确定性（$\rho \to 1$），信息衰减慢但 diversity 低；高 temperature 使信道趋近均匀随机（$\rho \to 0$），信息快速丢失。$T=1.0, p=0.95$ 处于中间区域，既保证可观测的深度信号，又不人为加速或延缓饱和。

### 种子数据

种子数据取自 **C4 (Colossal Clean Crawled Corpus)** [Raffel et al., 2020] 的 validation split。从中采样 **5,000 篇文档**，每篇文档经 tokenizer 截断至 **256 tokens** 后作为 depth-0 文本。

选择 C4 的理由：(1) 作为广泛使用的预训练语料，C4 文本代表了典型的 web 文本分布；(2) validation split 保证不与常见模型的训练集重叠。5,000 篇文档的规模在 pilot study 中足以提供可靠的统计估计，同时控制计算成本。

截断至 256 tokens 的考量：(1) 控制生成长度一致性——过长的 seed text 导致生成文本长度方差大，干扰特征提取；(2) 256 tokens 足以包含 1-2 个完整段落的语义信息，保留主题和风格特征；(3) 与模型的 max prompt length 配合——prompt 模板 + seed text 需要在 512 tokens 内完成。

### Left-padding 技术考量

在 batch 推理中，我们采用 **left-padding** (`tokenizer.padding_side = "left"`)。这一选择对 causal language model 的生成质量至关重要：

Right-padding（将 pad token 追加到序列末尾）会导致模型在生成时"看到"大量无意义的 pad token，影响注意力分布和生成质量。Left-padding 将 pad token 置于序列左侧，真实 token 右对齐，使得模型在生成时只关注到有意义的上下文。对于 Qwen2.5 等基于 causal attention 的模型，left-padding 是 batch generation 的标准做法，可确保生成质量与单样本推理一致。

## 3.2 Feature Extraction Pipeline

我们设计了三组共 15 维统计特征，分别从 token-level surprisal dynamics、sequence-level vocabulary diversity 和 distributional-level tail structure 三个层面刻画文本的统计属性。这三组特征的设计动机来自递归生成的已知退化机制：surprisal 分布反映模型对文本的"预期程度"随深度偏移 [DivEye, 2026]；词汇多样性是 model collapse 文献中最广泛记录的退化信号 [Shumailov et al., 2024]；频率分布尾部结构则捕捉 Zipf 分布的系统性变形 [Shumailov et al., 2024]。

### 3.2.1 Surprisal Features (9D)

Surprisal 衡量模型对观测到的 token 的"惊讶程度"。给定文本序列 $\mathbf{x} = (x_1, x_2, \ldots, x_n)$ 和语言模型 $p_\theta$，token $x_t$ 的 surprisal 定义为：

$$s(x_t) = -\log p_\theta(x_t \mid x_{<t})$$

其中 $x_{<t} = (x_1, \ldots, x_{t-1})$ 为前缀上下文。

**动机**：递归生成的文本倾向于更"符合预期"——每经过一次 LLM 信道，输出文本的 token 分布趋近模型的先验偏好，surprisal 分布整体向低值偏移。这一趋势反映了信道级联中互信息 $I(X_0; X_k)$ 随深度单调衰减的理论预测。

我们从 surprisal 序列 $\{s(x_t)\}_{t=2}^{n}$ 中提取以下统计量：

**基础统计量 (4D)**：
- $\mu_s = \frac{1}{n-1}\sum_{t=2}^{n} s(x_t)$ — surprisal 均值，反映文本整体的可预测程度
- $\sigma_s = \text{std}(\{s(x_t)\})$ — surprisal 标准差，反映 token 间可预测性的变异程度
- $\gamma_s = \text{skewness}(\{s(x_t)\})$ — 偏度，捕捉 surprisal 分布的不对称性
- $\kappa_s = \text{kurtosis}(\{s(x_t)\})$ — 峰度，捕捉 surprisal 分布的尾部厚度

**一阶差分统计量 (3D)**：定义一阶差分 $\Delta s_t = s(x_{t+1}) - s(x_t)$，反映相邻 token 间 surprisal 的局部变化动态。提取：
- $\mu_{\Delta s}$ — 一阶差分均值
- $\sigma_{\Delta s}$ — 一阶差分标准差
- $\gamma_{\Delta s}$ — 一阶差分偏度（当 $|\Delta s| \geq 3$ 时计算，否则置为 0）

**二阶差分统计量 (2D)**：定义二阶差分 $\Delta^2 s_t = \Delta s_{t+1} - \Delta s_t$，捕捉 surprisal 变化的加速度。提取：
- $\mu_{\Delta^2 s}$ — 二阶差分均值
- $\sigma_{\Delta^2 s}$ — 二阶差分标准差

一阶和二阶差分的引入受 DivEye [2026] 的启发——它们捕捉 surprisal 的 **temporal dynamics** 而非仅仅 distributional shape，能够反映递归生成文本中 token-level 可预测性的局部模式变化。

**实现细节**：Surprisal 通过同一生成模型（Qwen2.5-1.5B-Instruct）计算。对于每个 token $x_t$，我们使用模型在前缀 $x_{<t}$ 上的 logits 取 log-softmax 后的负对数概率。序列长度不足 3 个 token 的样本各维度置 0。计算采用 batch 推理（batch size = 8），使用 FP16 精度以控制显存占用。

### 3.2.2 Vocabulary Diversity Features (3D)

词汇多样性特征从 sequence level 衡量文本的词汇丰富度和重复模式。

**Type-Token Ratio (TTR)**：

$$\text{TTR} = \frac{|\mathcal{V}(\mathbf{x})|}{|\mathbf{x}|}$$

其中 $\mathcal{V}(\mathbf{x})$ 为文本 $\mathbf{x}$ 中出现的不同词 (types) 的集合，$|\mathbf{x}|$ 为总词数 (tokens)。TTR 越低，词汇重复度越高。

**Hapax Ratio**：

$$\text{Hapax} = \frac{|\{w \in \mathcal{V}(\mathbf{x}) : \text{freq}(w) = 1\}|}{|\mathcal{V}(\mathbf{x})|}$$

即只出现一次的词 (hapax legomena) 占全部不同词的比例。Hapax ratio 对词频分布的尾部敏感——递归生成的尾部消失 (tail disappearance) 直接表现为 hapax ratio 下降。

**Self-BLEU**：

$$\text{Self-BLEU}(\mathbf{x}_i) = \frac{1}{|R|} \sum_{j \in R} \text{BLEU}_4(\mathbf{x}_i, \mathbf{x}_j)$$

其中 $R$ 是从同一 depth 随机采样的参考文本集合（$|R| = 100$），$\text{BLEU}_4$ 为标准的 4-gram BLEU score（含 brevity penalty）。Self-BLEU 衡量同一 depth 内不同文档间的 n-gram 重叠程度。

**动机**：Self-BLEU 越高，说明同一深度的文本之间越相似——这正是递归生成导致的 progressive homogenization [Shumailov et al., 2024] 的直接度量。与 TTR 和 Hapax ratio 关注单文档内部的多样性不同，Self-BLEU 捕捉的是同深度文档 **之间** 的多样性坍缩。

**实现细节**：TTR 和 Hapax ratio 基于 whitespace tokenization（空格分词）在 word level 计算。Self-BLEU 的参考集从同深度文本中随机采样 100 篇（固定随机种子以保证可复现性），使用不依赖 NLTK 的轻量 4-gram BLEU 实现。

### 3.2.3 Tail-thinning Features (3D)

尾部稀疏特征从 distributional level 刻画文本词频分布的 Zipf 结构变化。

**Frequency Kurtosis**：

$$\kappa_f = \text{kurtosis}(\{c_w : w \in \mathcal{V}(\mathbf{x})\})$$

其中 $c_w = \text{freq}(w, \mathbf{x})$ 为词 $w$ 在文本 $\mathbf{x}$ 中的出现次数。Kurtosis 衡量词频分布的尖峰和厚尾程度。当 unique types 不足 4 时置 0。

**Frequency Entropy**：

$$H_f = -\sum_{w \in \mathcal{V}(\mathbf{x})} \hat{p}(w) \log_2 \hat{p}(w)$$

其中 $\hat{p}(w) = c_w / \sum_{w'} c_{w'}$ 为 empirical unigram probability。Frequency entropy 衡量词频分布的均匀程度——entropy 越高，词频分布越接近均匀（diversity 越高）。

**Low-frequency Ratio**：

$$\text{LFR} = \frac{|\{w \in \mathcal{V}(\mathbf{x}) : c_w = 1\}|}{|\mathcal{V}(\mathbf{x})|}$$

即频次为 1 的词占所有 unique types 的比例。

**动机**：Shumailov et al. [2024] 将 model collapse 分为三个阶段：tail disappearance → diversity loss → mode conflation。Tail-thinning features 直接刻画第一阶段——随着递归深度增加，词频分布的长尾逐渐消失，frequency kurtosis 下降（分布趋向扁平），frequency entropy 降低（分布集中于高频词），low-frequency ratio 减小（罕见词消失）。这些特征与 surprisal features 互补：surprisal 反映模型视角下的可预测性变化，而 tail-thinning 反映文本自身词频分布的结构性退化。

**实现细节**：基于 whitespace tokenization 的词频统计。Entropy 计算中添加 $10^{-12}$ 的 smoothing 以避免 log(0)。

### 特征总结

| 特征组 | 维度 | 特征名 | 捕捉的退化信号 |
|--------|------|--------|--------------|
| Surprisal | 9 | surp\_mean, surp\_std, surp\_skew, surp\_kurt, surp\_d1\_mean, surp\_d1\_std, surp\_d1\_skew, surp\_d2\_mean, surp\_d2\_std | Token-level 可预测性偏移与动态变化 |
| Vocab Diversity | 3 | ttr, hapax\_ratio, self\_bleu | 词汇丰富度衰减与文档间同质化 |
| Tail-thinning | 3 | freq\_kurtosis, freq\_entropy, low\_freq\_ratio | Zipf 尾部消失与频率分布集中化 |

全部 15 维特征均在 inference 时可计算（不依赖 paired original text 或跨深度信息），满足实际部署中仅有待检测文本可用的约束。

## 3.3 Ordinal Depth Classifier

### 分类器选择：LightGBM

我们选用 **LightGBM** [Ke et al., 2017] 作为 depth classification 的 baseline 分类器。在 tabular features（低维手工特征）场景下，gradient boosted decision trees (GBDT) 通常优于或 comparable to 深度学习方法 [Grinsztajn et al., 2022, 需验证]，同时提供以下关键优势：

(1) **可解释性**：LightGBM 原生提供 feature importance（基于 split gain 或 split count），使我们能够分析哪些特征对 depth discrimination 贡献最大，进而揭示递归生成的 linguistic degradation ordering。

(2) **训练效率**：15 维特征 × 30,000 样本（5,000 docs × 6 depths）的规模下，LightGBM 训练仅需秒级时间，支持大量 ablation 实验和 cross-validation。

(3) **对特征分布的鲁棒性**：GBDT 对特征缩放不敏感、能自然处理非线性关系和特征交互，无需额外的特征工程或归一化。

### 任务设定

我们在两个粒度上评估 depth discrimination 能力：

**Pairwise Binary Classification**：对每对相邻深度 $(k-1, k)$，训练独立的二分类器。输入为 15 维特征向量，输出为 $\{k-1, k\}$ 的深度标签。pairwise AUC 是衡量相邻深度可区分性的核心指标，直接用于 $K^*$ 的计算。

分类器参数：`n_estimators=200, max_depth=6, learning_rate=0.05, num_leaves=31`。

**Ordinal Multi-class Classification**：将全部 6 个深度 (depth 0--5) 作为一个有序多分类问题。使用 LightGBM 的 `multiclass` objective，参数设为 `n_estimators=300, max_depth=8, num_leaves=63`。

### 评估协议

所有实验采用 **5-fold stratified cross-validation**。Stratified split 确保每个 fold 中各深度类别的比例一致。

[TODO: grouped by doc\_id 的实现——当前代码使用 StratifiedKFold 但未按 doc\_id 分组。严格来说，同一 doc\_id 在不同 depth 的文本应当被分配到同一 fold，以避免同源文档信息在训练集和测试集间泄露。这是一个需要在正式实验中修复的设计点。]

### 评估指标

- **Pairwise AUC**：每对相邻深度的 ROC-AUC，5-fold 均值和标准差。这是最核心的指标，直接反映每一步递归生成引入的 distributional shift 是否可被统计特征捕捉。

- **MAE (Mean Absolute Error)**：ordinal classification 的预测深度与真实深度之差的均值。MAE 对 ordinal 结构敏感——将 depth-0 误分为 depth-1（MAE=1）比误分为 depth-5（MAE=5）惩罚更轻，符合"相邻深度更难区分"的直觉。

- **Accuracy**：ordinal classification 的精确匹配准确率。

- **Feature Importance**：LightGBM 的 split-based feature importance，按贡献排序，用于分析哪些特征组（surprisal / vocab diversity / tail-thinning）在 depth discrimination 中最为关键。

## 3.4 Saturation Boundary $K^*$

### 操作性定义

我们定义 **判别饱和边界 (discriminability saturation boundary)** $K^*$ 为：

$$K^* = \max\{k : \text{AUC}(\text{depth } k{-}1 \text{ vs } k) > 0.60\}$$

即 $K^*$ 是满足相邻深度 pairwise AUC 大于 0.60 的最大深度。$K^*$ 之后（depth $> K^*$），相邻深度的文本在 15 维特征空间中不再具有可靠的统计可区分性。

### 阈值选择理由

选择 0.60 作为阈值基于以下考量：

(1) **与 chance level 的间距**。二分类的 chance AUC = 0.50。阈值 0.60 对应 Cohen's $d$ [TODO: 计算对应效应量] 的 small-to-medium effect size，表示 "微弱但可靠的可区分性"。

(2) **实践意义**。AUC = 0.60 意味着在随机抽取一对（depth $k{-}1$, depth $k$）样本时，分类器有 60% 的概率正确排序——略好于随机猜测，但已可为 downstream curation 提供有意义的信号。

(3) **保守性**。相比更高阈值（如 0.70），0.60 允许更多深度被纳入"可区分"范围，使 $K^*$ 的估计偏向乐观。如果在此保守阈值下 $K^*$ 仍然较小，则更加确证了 depth discrimination 的 fundamental limit。

### 与 DPI 理论的联系

在信道级联框架下，$K^*$ 有明确的 information-theoretic 解释。由 Data Processing Inequality (DPI)，对 Markov chain $X_0 \to X_1 \to \cdots \to X_K$，有：

$$I(X_0; X_k) \leq I(X_0; X_{k-1}) \leq \cdots \leq I(X_0; X_1) \leq H(X_0)$$

即关于原始人类文本 $X_0$ 的信息量随递归深度 **单调非递增**。每经过一次 LLM 信道 $\mathcal{T}$（假设为 strictly lossy channel，即任何 temperature > 0 或 nucleus 截断都引入不可逆信息损失），互信息严格递减。

$K^*$ 对应于 $I(X_0; X_k)$ 降至 noise floor 的临界深度——不是分类器的能力上限，而是 **information-theoretic impossibility boundary**：任何方法（无论多复杂）都无法区分 depth $> K^*$ 的文本，因为原始人类文本的信息已被信道噪声完全淹没。

形式化地，若信道 $\mathcal{T}$ 关于某分布度量 $d$ 是 contractive 的（即 $d(\mathcal{T}(P), \mathcal{T}(Q)) \leq \rho \cdot d(P, Q)$，$0 < \rho < 1$），则 $P_{X_k}$ 以几何速率趋近不动点分布 $P^*$：

$$d(P_{X_k}, P^*) \leq \rho^k \cdot d(P_{X_0}, P^*)$$

相邻深度的分布差异同样以几何速率趋零：

$$D(k, k{+}1) \leq (\rho^k + \rho^{k+1}) \cdot d(P_{X_0}, P^*)$$

从而 $K^*(\epsilon)$ 对任意阈值 $\epsilon > 0$ 必然有限，其粗略 scaling 为：

$$K^* = O\left(\frac{\log(d(P_{X_0}, P^*) / \epsilon)}{\log(1/\rho)}\right)$$

这表明 $K^*$ 由信道的 contraction rate $\rho$ 和 seed 文本分布到不动点的初始距离共同决定。

### 经验验证方法

我们使用 pairwise AUC 作为 discriminability 的 empirical proxy，配合 Jensen-Shannon Divergence (JSD) 作为 distributional distance 的 computationally tractable proxy：

$$\text{JSD}(P_{X_k} \| P_{X_{k'}}) = \frac{1}{2} D_{\text{KL}}(P_{X_k} \| M) + \frac{1}{2} D_{\text{KL}}(P_{X_{k'}} \| M)$$

其中 $M = \frac{1}{2}(P_{X_k} + P_{X_{k'}})$。JSD 在 unigram level 上按 feature 维度分别计算（基于 50-bin 直方图估计），取均值作为综合度量。

需要承认的局限：unigram-level JSD 忽略了序列结构（n-gram patterns、句法依赖等），不等价于真正的互信息 $I(X_0; X_k)$。但 DPI 的定性结论——单调衰减——在 JSD 框架下同样成立，因此作为 tracking metric 仍然有效。

### $K^*$ 的科学意义

$K^*$ 是本工作提出的首次被系统测量的科学量。此前关于递归生成退化的研究 [Shumailov et al., 2024; Alemohammad et al., 2024; Drayson et al., 2025] 主要提供定性描述（"early generations show most change"）或仅做 binary 过滤（synthetic vs human），但从未给出精确的判别边界。Drayson et al. (EMNLP 2025) 是最接近的先行工作——他们训练 MGT 检测器做 importance resampling 防止 model collapse，但仍限于 binary detection，不估计生成深度。我们的 ordinal depth estimation 是其自然推广：从 binary filtering 到 graduated weighting。$K^*$ 的测量具有直接的实践指导价值：

- **对数据 curation 从业者**：$K^*$ 告诉你在当前模型和生成配置下，depth-aware filtering 能有效区分多少层深度——depth $\leq K^*$ 的文本可进行 graduated weighting，depth $> K^*$ 的文本可统一处理。
- **对 model collapse 研究**：$K^*$ 量化了 Shumailov et al. 描述的 "early collapse" 与 "late collapse" 之间的精确过渡边界。
- **对 AI 生成文本检测**：$K^*$ 揭示了 depth estimation 作为检测范式的 fundamental resolution limit——无论特征工程或分类器如何改进，信息论约束决定了 $K^*$ 之外不可能做得更好。

[TODO: 补充 MVP 实验中测得的 $K^*$ 实际值及其置信区间]
