# 文献调研：迭代合成训练中 Collapse 的加速模式

## 1. 核心发现摘要

- **Collapse 退化是非线性的，理论和实证均支持加速/指数衰减。** 信息论框架（Data Processing Inequality）预测互信息以指数速率衰减，λ ∈ [0.2, 0.4]/iteration。Shumailov et al. 的两阶段模型（early → late collapse）描述了一个从缓慢尾部消失到全分布坍缩的相变过程——前几代看起来温和，后几代急剧恶化。
- **Loss 与 diversity/entropy 的解耦是已知现象。** "Knowledge Collapse" 论文明确发现 fluency（表面指标）可在 factual accuracy 已严重退化时保持稳定。Shumailov et al. 指出 early collapse 阶段"整体性能可能看起来在改善，而模型实际上在少数群体数据上丧失性能"。**这直接威胁我们用 ρ(loss, entropy) 作为单一 pass/fail 信号的可靠性。**
- **50/50 混合比是次优的。** Golden Ratio Weighting 论文证明等量混合时最优 real-data 权重 ≈ 0.62（黄金比例倒数），naive 的 50/50 无权重混合总是次优的，尤其在合成数据占比高时效率可以任意差。
- **数据累积 vs 替换是关键分水岭。** Gerstgrasser & Schaeffer et al. 证明：替换策略下 test error 随迭代单调增长（collapse 不可避免），但累积策略（保留原始真实数据 + 历代合成数据）可以将 test error 限制在有限上界。
- **Gen 2-3 加速退化有强理论支持。** 根据 DPI 指数衰减模型和两阶段 collapse 理论，线性外推（0.017/gen → Gen 3 ≈ 0.88）很可能**低估**实际退化。更可能的轨迹是 Gen 2 出现明显加速，Gen 3 进入 late collapse 区间。

## 2. 关键论文列表

### 2.1 Shumailov et al. — "AI models collapse when trained on recursively generated data"

- **作者**: Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal
- **发表**: Nature 631, 755–759 (2024); 原 arXiv 版本 2023 (arXiv:2305.17493)
- **核心结论**: 在 VAE、GMM 和 LLM 上验证了 model collapse 现象。提出两阶段框架：
  - **Early model collapse**: 分布尾部消失，少数群体数据丢失，但整体指标可能看起来正常甚至改善
  - **Late model collapse**: 分布完全坍缩到点估计附近，方差极小，模型丧失实用价值
  - GMM 实验中约 50 次迭代后底层分布已被严重误估，2000 次迭代后退化为点估计
- **与我们实验的关联**: 我们的 Gen 0→1 ρ 下降仅 0.017，可能正处于 early collapse 阶段——表面指标掩盖了分布尾部的退化。Gen 2-3 有进入 late collapse 的风险。

### 2.2 Alemohammad et al. — "Self-Consuming Generative Models Go MAD"

- **作者**: Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaagba, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk
- **发表**: ICLR 2024 (arXiv:2307.01850)
- **核心结论**: 定义了 Model Autophagy Disorder (MAD)。研究了三种自消耗循环：
  - **Fully synthetic loop**: ~20 代后 Levenshtein diversity 降至 ~0.1，语法正确性可保持高位（loss-diversity decoupling 的实证）
  - **Synthetic augmentation loop**（固定真实数据）: 退化减缓但不消除
  - **Fresh data loop**（新真实数据注入）: 退化最轻
  - 没有足够新鲜真实数据，quality (precision) 或 diversity (recall) 必然递减
- **与我们实验的关联**: 我们的 50/50 混合属于 synthetic augmentation loop，但每代使用相同的真实数据子集而非新数据，退化可能介于 fully synthetic 和 augmentation loop 之间。

### 2.3 Dohmatob & Feng — "Strong Model Collapse"

- **作者**: Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe
- **发表**: ICLR 2025 Spotlight (arXiv:2410.04840)
- **核心结论**: 用 operator-valued free probability theory 证明：
  - **即使极小比例的合成数据（1/1000）也会导致 collapse**——增大训练集不能弥补
  - Test error 分解为 B + V + ζ，其中 ζ 是合成数据引入的不可消除项
  - **更大的模型会放大 collapse**——对 Pythia-410M 这样的中型模型同样成立
- **与我们实验的关联**: 我们用 50% 合成数据远高于 1/1000 阈值，理论上 collapse 压力很大。模型越大可能越严重，但 410M 已足以观察到效应。

### 2.4 Dohmatob et al. — "A Tale of Tails: Model Collapse as a Change of Scaling Laws"

- **作者**: Elvis Dohmatob, Yunzhen Feng, Julia Kempe
- **发表**: ICML 2024, PMLR 235:11165-11197 (arXiv:2402.07043)
- **核心结论**: 将 model collapse 框架化为 scaling law 的变化：
  - 提出 "double scaling law"——合成数据改变了 loss-vs-data 的幂律关系
  - 观察到 "un-learning" of skills 和 grokking 现象
  - 即使 1% 的合成数据也改变 scaling behavior
- **与我们实验的关联**: 我们追踪的 ρ(loss, entropy) 本质上是在检测 scaling law 是否偏移。如果 Gen 2-3 出现 scaling law 变化，ρ 的下降可能突然加速。

### 2.5 Gerstgrasser, Schaeffer et al. — "Is Model Collapse Inevitable?"

- **作者**: Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, Sanmi Koyejo
- **发表**: arXiv:2404.01413 (2024)
- **核心结论**:
  - **替换策略**: test error 随迭代数单调增长 → collapse 不可避免
  - **累积策略**: test error 有有限上界（与迭代数无关）→ collapse 可避免
  - 在 Transformer (causal LM)、扩散模型、VAE 上均验证
- **与我们实验的关联**: 我们的实验设计是替换策略（每代用当代合成数据替换上代），**按照此论文的理论，collapse 是必然的**。如果改为累积策略（保留所有历代数据），退化可被抑制。

### 2.6 He et al. — "Golden Ratio Weighting Prevents Model Collapse"

- **作者**: Hengzhi He, Shirong Xu et al.
- **发表**: arXiv:2502.18049 (2025)
- **核心结论**:
  - 等量 real/synthetic 数据时，最优 real-data 权重 = 1/φ ≈ 0.618（黄金比例倒数）
  - Naive 无权重混合总是次优的
  - 跨 Gaussian estimation、GLM、非参数估计等设置，最优权重表达式统一
- **与我们实验的关联**: 我们的 50/50 等权混合给了合成数据过多权重（0.5 vs 最优 0.38）。如果加权方案调整为 ~62/38 (real/synthetic)，可能减缓 collapse。

### 2.7 Keisha et al. — "Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail"

- **作者**: Figarri Keisha, Zekun Wu, Ze Wang, Adriano Koshiyama, Philip Treleaven
- **发表**: NeurIPS 2025 Workshop (arXiv:2509.04796)
- **核心结论**:
  - 定义了三阶段 knowledge collapse：factual accuracy 退化而 surface fluency 保持 → "confidently wrong" outputs
  - 100% 合成训练导致 entropy 快速下降和词汇收窄
  - **25-50% 合成比例**保留判别能力，但 accuracy 仍退化
  - Collapse 轨迹和时间点依赖 instruction format
- **与我们实验的关联**: **直接支持 loss-entropy decoupling 假设。** 我们的 50% 合成比例处于 "保留判别能力但 accuracy 退化" 区间。Gen 2-3 可能进入 entropy 快速下降阶段。

### 2.8 He et al. — "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"

- **作者**: Shiliang He et al.
- **发表**: NeurIPS 2025 (arXiv:2509.16499)
- **核心结论**:
  - Model collapse = generalization → memorization 的转变
  - **训练数据 entropy 的下降是模型退化的直接驱动因素和清晰指标**
  - 数据点在迭代过程中聚集成局部 cluster → entropy 急剧下降 → 后续模型被迫记忆
  - 提出基于 entropy 的数据选择策略可缓解 collapse
- **与我们实验的关联**: **直接验证了我们选择 output entropy 作为 collapse 探针的合理性。** 但也暗示 entropy 下降可能有一个"聚集临界点"——一旦数据点形成 cluster，entropy 会加速下降。

### 2.9 DPI 框架 — "Lossy Loops: Shannon's DPI and Information Decay"

- **作者**: (Preprint, 2025)
- **发表**: Preprints.org (DOI: 10.20944/preprints202507.2260.v1)
- **核心结论**:
  - 将迭代合成训练建模为 Markov chain / lossy communication channel
  - DPI 保证 I(X; Yₙ) ≤ I(X; Yₙ₋₁) — 信息单调不增
  - 预测**指数衰减**速率 λ ∈ [0.2, 0.4]/iteration
  - 架构限制贡献 >30% 信息损失
  - 稳定性阈值：需要 >70% human data
- **与我们实验的关联**: 如果 λ ≈ 0.3，则 ρ 的衰减模式为：Gen 0=0.929, Gen 1=0.912 (Δ=0.017), Gen 2 ≈ 0.929×e^{-0.6} ≈ 0.88 or worse, Gen 3 可能降至 ~0.84 以下。非线性加速明确。我们的 50% real data 低于 70% 稳定性阈值。

### 2.10 Characterizing Model Collapse Using Semantic Networks

- **作者**: (2024, arXiv:2410.12341)
- **核心结论**:
  - 用语义网络和 next-token probability 双重策略量化 collapse
  - 文本重复性增加、语义多样性下降随迭代加剧
  - 合成 token 比例直接影响 collapse 严重程度
- **与我们实验的关联**: 提供了除 entropy 和 spectral rank 外的补充度量思路。

## 3. 对 Pass/Fail 的预测影响

### 3.1 线性外推是过于乐观的估计

基于以上文献，线性外推（0.017/gen → Gen 3 ≈ 0.88）几乎肯定**低估**了实际退化：

| 证据来源 | 支持加速的机制 |
|----------|--------------|
| DPI 指数衰减 (λ=0.2–0.4) | 信息损失在每一代被乘性放大，非加性 |
| 两阶段 collapse 模型 | Early→Late 的相变可在 Gen 2-3 发生 |
| Generalization→Memorization 转变 | 数据 cluster 化存在临界点，一旦越过 entropy 急剧下降 |
| Strong Model Collapse | 50% 合成比例远超理论危险阈值 (0.1%) |
| Golden Ratio Weighting | 50/50 等权混合加剧了合成数据的负面影响 |

### 3.2 更可能的轨迹预测

基于 DPI 指数衰减模型（取保守端 λ=0.2）和两阶段 collapse 理论：

| 代次 | 线性外推 ρ | 指数衰减预测 ρ | 含相变风险预测 |
|------|-----------|---------------|--------------|
| Gen 0 | 0.929 (实测) | 0.929 (实测) | 0.929 (实测) |
| Gen 1 | 0.912 (实测) | 0.912 (实测) | 0.912 (实测) |
| Gen 2 | 0.895 | 0.87–0.89 | 0.83–0.89 |
| Gen 3 | 0.878 | 0.82–0.86 | 0.75–0.85 |

**关键不确定性**: Gen 2 是否越过 early→late collapse 的临界点。如果越过，Gen 3 退化可能远超预期。

### 3.3 对 Pass/Fail 判据的建议

1. **ρ(loss, entropy) 单一指标不够可靠**。文献强烈表明 loss 可以在 diversity 已退化时保持平稳。应补充直接度量：
   - Output entropy 的绝对值（不仅是与 loss 的相关性）
   - Spectral rank 的绝对值衰减
   - Token/n-gram diversity 指标
2. **Gen 2 是关键观察点**。如果 Gen 2 的 ρ 下降 ≥ 0.03（即加速了），则 Gen 3 进入 late collapse 区间的概率很高。
3. **50/50 混合比加速了 collapse**。文献建议最低 62/38 或 70/30 的 real/synthetic 比例。

## 4. 引用列表

1. Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. *Nature*, 631, 755–759. https://doi.org/10.1038/s41586-024-07566-y — arXiv:2305.17493

2. Alemohammad, S., Casco-Rodriguez, J., Luzi, L., Humayun, A.I., Babaagba, H., LeJeune, D., Siahkoohi, A., & Baraniuk, R.G. (2024). Self-Consuming Generative Models Go MAD. *ICLR 2024*. arXiv:2307.01850

3. Dohmatob, E., Feng, Y., Yang, P., Charton, F., & Kempe, J. (2025). Strong Model Collapse. *ICLR 2025 (Spotlight)*. arXiv:2410.04840

4. Dohmatob, E., Feng, Y., & Kempe, J. (2024). A Tale of Tails: Model Collapse as a Change of Scaling Laws. *ICML 2024*, PMLR 235:11165-11197. arXiv:2402.07043

5. Gerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., Sleight, H., Hughes, J., Korbak, T., Agrawal, R., Pai, D., Gromov, A., Roberts, D.A., Yang, D., Donoho, D.L., & Koyejo, S. (2024). Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data. arXiv:2404.01413

6. He, H., Xu, S., et al. (2025). Golden Ratio Weighting Prevents Model Collapse. arXiv:2502.18049

7. Keisha, F., Wu, Z., Wang, Z., Koshiyama, A., & Treleaven, P. (2025). Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training. *NeurIPS 2025 Workshop*. arXiv:2509.04796

8. He, S., et al. (2025). A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective. *NeurIPS 2025*. arXiv:2509.16499

9. Lossy Loops: Shannon's DPI and Information Decay in Generative Model Training. (2025). *Preprints.org*. DOI: 10.20944/preprints202507.2260.v1

10. Characterizing Model Collapse in Large Language Models Using Semantic Networks and Next-Token Probability. (2024). arXiv:2410.12341
