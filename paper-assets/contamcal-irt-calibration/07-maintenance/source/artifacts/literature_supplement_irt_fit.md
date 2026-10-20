# Literature Supplement: IRT Model Fit, Contamination Format Sensitivity, Simpson's Paradox

检索日期：2026-05-16 | 目标会议：EMNLP 2026 ARR May 25

---

## Direction 1: IRT Model Fit Diagnostics — "Significant but Misfit"

### 1.1 Sinharay, Johnson, & Stern (2006)
- **Title:** Posterior Predictive Assessment of Item Response Theory Models
- **Venue:** Applied Psychological Measurement, 30, 298–321
- **关系：支持/方法论基础**
- 摘要：系统评估了 PPMC 框架下多种 discrepancy measures（Yen's Q1, Stone's χ², Orlando-Thissen S-X²）对 IRT 模型拟合检验的性能，建议 odds ratio 作为检测 misfit 的有力工具。我们的 PPP 计算直接基于此框架。

### 1.2 Sinharay (2025)
- **Title:** Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future Directions
- **Venue:** British Journal of Mathematical and Statistical Psychology, 78, 711–733
- **关系：支持——最新综述，reviewer 可能引用**
- 摘要：全面综述 IRT 模型拟合评估方法，涵盖 PPMC、generalized residuals、person-fit 等。指出 PPP 解释需谨慎——低 PPP 表明模型不充分但不意味着参数估计无意义。可用于论证我们 ARC 上 PPP=0.003 但 γ 仍可解释的立场。

### 1.3 Brown & Thomson (2024)
- **Title:** The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation
- **Venue:** Molecular Biology and Evolution, 41(3), msae051
- **关系：关键支撑——直接回答 "significant but misfit" 问题**
- 摘要：证明 PPP 值的期望分布本质上**非均匀**（不同于频率学派 p 值），集中在 0.5 附近。因此极端 PPP（如我们的 0.003）提供的 poor fit 证据比通常认为的更强。但关键洞察：posterior predictive test 在高度有利条件下评估模型（模型已拟合数据），所以 low PPP 并不自动否定参数估计的信息量。可用于论证 γ 的 posterior interval 排除零仍有意义，即使全局模型拟合差。

---

## Direction 2: Contamination in MC vs Generative Benchmarks

### 2.1 Deng, Zhao, Tang, Gerstein, & Cohan (2024)
- **Title:** Investigating Data Contamination in Modern Benchmarks for Large Language Models
- **Venue:** NAACL 2024 (arXiv:2311.09783)
- **关系：支持——MC 格式对 contamination 更敏感的直接证据**
- 摘要：提出 Testset Slot Guessing (TS-Guessing) 协议，mask 掉 MC 题的错误选项让模型填空。ChatGPT/GPT-4 在 MMLU 上猜对率达 52%/57%（远超随机）。证明 MC 格式因答案空间有限，contaminated model 可通过记忆选项获益，而 open-ended 格式难以通过记忆获益。直接支持我们的发现：ARC（MC）上 γ>0 而 GSM8K（generative）上 γ≈0。

### 2.2 Li et al. (2024)
- **Title:** Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs Evaluation, Benchmark, and Arena
- **Venue:** arXiv:2406.07545
- **关系：互补——MC→open-ended 的性能下降量化**
- 摘要：将 MC benchmark 转换为 open-style 问题后，所有模型准确率平均下降约 25%。说明 MC 格式本身为模型提供了额外线索（selection bias, random guessing），contaminated model 在 MC 中优势更大。支持我们将 MC/generative 格式差异作为 contamination 信号强度的调节变量。

### 2.3 Schaeffer, Kazdan, Abbasi, Liu, et al. (2026)
- **Title:** Quantifying the Effect of Test Set Contamination on Generative Evaluations
- **Venue:** arXiv:2601.04301
- **关系：互补/潜在 reviewer 会引用——generative benchmark 上 contamination 效应的首个 scaling law 研究**
- 摘要：在 MATH（generative）benchmark 上系统研究 contamination 效应，发现即使仅 1 份 test set replica 混入 pretraining 语料也能让模型突破无污染语料的 irreducible error。但效应大小远小于 MC benchmark 上的同类研究。与我们的框架一致：generative benchmark 上 contamination 效应更弱但并非为零，γ 参数预期更小。

### 2.4 Yang, Chiang, Zheng, Gonzalez, & Stoica (2023)
- **Title:** Rethinking Benchmark and Contamination for Language Models with Rephrased Samples
- **Venue:** arXiv:2311.04850
- **关系：互补——contamination 绕过 decontamination 的机制**
- 摘要：证明 paraphrase/翻译等简单变换可绕过 n-gram overlap 去污染。13B 模型通过 contaminated rephrased samples 可达 GPT-4 级性能。暗示我们测量的 γ 可能低估真实 contamination（因为部分 contamination 来自 rephrased 变体，不被完全捕捉）。

---

## Direction 3: Simpson's Paradox in Psychometrics/IRT

### 3.1 Kievit, Frankenhuis, Waldorp, & Borsboom (2013)
- **Title:** Simpson's Paradox in Psychological Science: A Practical Guide
- **Venue:** Frontiers in Psychology, 4, 513
- **关系：关键支撑——直接为 D108 发现提供理论框架**
- 摘要：论证 Simpson's paradox 在心理学研究中比传统认知更普遍。当从 population 推断到 subgroup（或反向）时，效应方向可能反转。提出 Simpson's paradox 的统计标记和 R 检测工具箱。直接适用于我们的发现：MMLU pooled 分析中 γ 不显著，但 domain-level 分析揭示部分 domain γ 显著为正、部分为负/零，聚合后相互抵消。

### 3.2 Ercikan, Arim, & Oliveri (2008)
- **Title:** Differential Item Functioning Amplification and Cancellation in a Reading Test
- **Venue:** Practical Assessment, Research, and Evaluation, 14(3)
- **关系：支持——DIF cancellation 的实证先例，与我们的 domain-level pattern 直接类比**
- 摘要：使用 multiple-group testlet IRT 模型研究阅读测试中的 DIF 放大和抵消效应。发现多数 item 存在显著 DIF，但由于不同 item 偏向不同群体，DIF 在 total test score 水平相互抵消。这与我们 MMLU 的情况直接类比：domain-level contamination signals 方向不一致，pooled 分析中被 aggregate 掩盖。

### 3.3 Penfield & Algina (2006)
- **Title:** A Generalized DIF Effect Variance Estimator for Measuring Unsigned Differential Test Functioning in Mixed Format Tests
- **Venue:** Journal of Educational Measurement, 43(4), 295–321
- **关系：方法论参考——量化 DIF cancellation 的统计工具**
- 摘要：提出 ν² 统计量用于量化 unsigned DTF（即 DIF 在 test level 的净效应），区分 DIF 完全抵消（signed DTF≈0）和 DIF 存在但方向不同（unsigned DTF>0）两种情况。分类标准：ν²<0.07 小效应，0.07–0.14 中效应，>0.14 大效应。可用于量化我们 MMLU domain-level γ 的 cancellation 程度。

---

## 论文中的使用建议

| 论文 | 建议放置位置 | 用途 |
|------|-------------|------|
| Brown & Thomson (2024) | Discussion: ARC model fit | 论证 low PPP + significant γ 的可解释性 |
| Sinharay (2025) | Method: IRT fitting | 方法论权威引用 |
| Deng et al. (2024) | Discussion: MC vs generative | MC 格式对 contamination 更敏感的证据 |
| Li et al. (2024) | Discussion: MC vs generative | MC→open-ended 性能下降的量化 |
| Schaeffer et al. (2026) | Discussion: generative benchmark | 即使 generative 也非完全免疫 |
| Kievit et al. (2013) | Results: MMLU domain analysis | Simpson's paradox 理论框架 |
| Ercikan et al. (2008) | Results: MMLU domain analysis | DIF cancellation 实证先例 |
