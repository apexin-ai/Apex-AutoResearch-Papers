# Related Work Literature Notes

**Project:** provenance_weight_training — 基于收敛理论的自适应污染重加权
**Generated:** 2026-05-14

---

### Machine-Generated Text Detection Prevents Language Model Collapse (EMNLP 2025)

**BibTeX:**
```bibtex
@inproceedings{drayson2025machine,
  title={Machine-generated text detection prevents language model collapse},
  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
  booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
  year={2025}
}
```

**摘要:** 提出用机器生成文本检测器进行重要性重采样（importance resampling），在数据来源未知的现实场景下缓解模型坍塌。在 GPT-2 和 SmolLM2（124M–1.7B）上验证，证明检测+重加权不仅防止坍塌，还优于仅用人类数据训练。

**技术细节:**
- **检测器:** ModernBERT（encoder-only），in-distribution AUC=0.986，out-of-distribution AUC=0.943
- **加权公式:** $w_j = (1 - q(x_j))^b / \sum_l (1 - q(x_l))^b$，其中 $q(x_j)$ 是样本被判为机器生成的概率
- **b 选择:** 在 Wikitext-2 validation set 上调参，per-model 固定：GPT-2/SmolLM2-135M/360M 用 b=10，SmolLM2-1.7B 用 b=1
- **混合比例:** 不假设已知（"does not assume access to the values of the mixing coefficients"）

**与我们的差异:**
| 维度 | Drayson et al. | Ours |
|------|---------------|------|
| b 选择 | Validation-based empirical search，per-model 固定 | 理论推导 adaptive b*(α_eff)，根据检测器置信度自适应 |
| 检测器 | ModernBERT (AUC=0.986)，重量级 | TF-IDF (AUC=0.939)，轻量级，证明 sufficiency |
| 混合比例 | 不假设已知，但不显式估计 | 显式估计 α_eff(b) 并纳入理论框架 |
| 理论保证 | 无收敛理论 | 基于收敛理论推导最优权重指数 |
| b 值 | 固定（10 或 1），需 per-model tuning | 自适应，无需额外 validation |

**在我们论文中的定位:** direct-competitor（最接近的工作，差异化的核心对比对象）

---

### Golden Ratio Weighting Prevents Model Collapse (arXiv 2025)

**BibTeX:**
```bibtex
@article{he2025golden,
  title={Golden Ratio Weighting Prevents Model Collapse},
  author={He, Hengzhi and Xu, Shirong and Cheng, Guang},
  journal={arXiv preprint arXiv:2502.18049},
  year={2025}
}
```

**摘要:** 在迭代训练（real + synthetic data 混合）框架下，理论推导最优加权方案。在 Gaussian 估计、广义线性模型、非参数估计三种设定中，证明真实数据的最优权重渐近等于黄金比例的倒数（≈0.618）。

**与我们的差异:**
- 研究的是迭代生成式训练（model_t → data → model_{t+1}）中的最优权重，假设知道哪些是 real/synthetic
- 我们处理的是 unknown provenance setting，数据来源未知，需要先检测再加权
- 他们的最优权重是全局常数（golden ratio），我们的 b* 是 adaptive 的
- 理论框架不同：他们基于 bias-variance tradeoff 的渐近分析，我们基于收敛速率理论

**在我们论文中的定位:** background（理论动机相关，但 setting 不同——known provenance vs unknown provenance）

---

### Strong Model Collapse (ICLR 2025)

**BibTeX:**
```bibtex
@inproceedings{dohmatob2025strong,
  title={Strong Model Collapse},
  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
  booktitle={International Conference on Learning Representations},
  year={2025}
}
```

**摘要:** 在 scaling laws 范式下证明模型坍塌的"强形式"：即使训练数据中仅含 0.1% 的合成数据，增大数据集也无法提升性能。更大的模型可能放大坍塌（插值阈值以下），但超过插值阈值后可缓解但不能完全防止。GPT-2 + BabiStories 实验验证。

**与我们的差异:**
- 诊断性工作（证明问题存在），不提供解决方案
- 我们直接提供解决方案（adaptive reweighting）
- 他们的结果为我们的动机提供理论支撑：即使微量污染也需处理

**在我们论文中的定位:** background（motivation — 证明即使少量污染也致命，强化我们方法的必要性）

---

### Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining (ICLR 2025)

**BibTeX:**
```bibtex
@inproceedings{sow2025dynamic,
  title={Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining},
  author={Sow, Daouda and Woisetschl{\"a}ger, Herbert and Bulusu, Saikiran and Wang, Shiqiang and Jacobsen, Hans Arno and Liang, Yingbin},
  booktitle={International Conference on Learning Representations},
  year={2025}
}
```

**摘要:** 提出基于 loss 值的动态样本重加权策略（LinUpper, Quadratic, Extremes），在训练过程中在线调整每个样本权重，使模型聚焦于当前阶段最有信息量的样本。提供首个 loss-based reweighting 对梯度优化收敛影响的理论分析。在 1.4B 和 7B LLM 预训练中验证。

**与我们的差异:**
- 加权信号不同：他们基于 training loss（模型内部信号），我们基于 provenance detection score（外部检测器信号）
- 目标不同：他们优化通用预训练效率（课程学习风格），我们专门解决数据污染问题
- 不涉及 synthetic data / model collapse 场景
- 理论框架不同：他们分析 loss-based reweighting 的收敛 bound，我们从污染比例推导最优权重指数

**在我们论文中的定位:** background（同为 sample reweighting for pretraining，但动机和信号来源完全不同）

---

### SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training (ACL 2024)

**BibTeX:**
```bibtex
@inproceedings{he2024softdedup,
  title={SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training},
  author={He, Nan and Xiong, Weichen and Liu, Hanwen and Liao, Yi and Ding, Lei and Zhang, Kai and Tang, Guohua and Han, Xiao and Yang, Wei},
  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={4011--4022},
  year={2024},
  address={Bangkok, Thailand}
}
```

**摘要:** 提出软去重方法，用 n-gram 模型度量"data commonness"（数据常见度），降低高常见度样本的采样权重而非直接删除。实现等效 perplexity 下训练步数减少 ≥26%，few-shot 下游准确率提升 1.77%。

**与我们的差异:**
- 目标不同：他们处理重复/高频数据，我们处理合成数据污染
- 信号不同：n-gram commonness vs provenance detection score
- 他们的权重基于数据频率统计，我们基于来源判别概率
- 不涉及 model collapse

**在我们论文中的定位:** background（data reweighting for pretraining 的代表工作，不同 reweighting signal）

---

### Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (arXiv 2025)

**BibTeX:**
```bibtex
@article{yi2025escaping,
  title={Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},
  author={Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},
  journal={arXiv preprint arXiv:2510.16657},
  year={2025}
}
```

**摘要:** 证明通过外部验证器（人类或更强模型）注入信息可避免模型坍塌。理论分析（线性回归 setting）表明 verifier-guided retraining 可获得短期改善，但长期收敛到验证器的"knowledge center"。除非验证器完全可靠，早期收益会趋于平台期甚至逆转。在线性回归、VAE (MNIST)、SmolLM2-135M (XSUM) 上验证。

**与我们的差异:**
- 他们的 verifier 做二元判断（accept/reject synthetic sample），我们用检测器分数做软加权
- 他们分析的是迭代训练的长期收敛行为，我们关注单轮训练中的最优加权
- 他们的理论框架基于线性回归，我们基于通用收敛理论
- 他们指出 verifier 不完美时存在 ceiling effect，我们的理论能在检测器不完美时推导最优 b*

**在我们论文中的定位:** direct-competitor（同为 detection/verification + model collapse，但 hard filter vs soft weighting）

---

### Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training (arXiv 2026)

**BibTeX:**
```bibtex
@article{wang2026can,
  title={Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training},
  author={Wang, Kevin and Niu, Hongqian and Li, Didong},
  journal={arXiv preprint arXiv:2602.16065},
  year={2026}
}
```

**摘要:** 在极小假设下（不限定数据分布，允许通用函数逼近器）证明：污染递归训练仍然收敛，收敛速率等于基线模型收敛速率与真实数据比例二者的较小值。这是首个不依赖分布假设的递归训练正面理论结果。

**与我们的差异:**
- 他们提供的是"不干预也能收敛"的理论保证（被动分析），我们提供主动干预手段（adaptive reweighting）提升收敛
- 他们的收敛速率被 min(baseline rate, real data fraction) 约束，我们的加权方案旨在突破这个约束
- 他们的理论是我们的 motivation 来源之一：收敛速率依赖真实数据比例 → 通过加权等效提升真实数据占比

**在我们论文中的定位:** method-component（理论 motivation 直接来源——我们从他们的收敛速率公式出发，推导加权方案来优化这个速率）
