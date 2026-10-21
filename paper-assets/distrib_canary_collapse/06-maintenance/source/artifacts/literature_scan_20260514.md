# 文献增量扫描：Model Collapse Canary Metrics

**扫描日期**: 2026-05-14  
**覆盖范围**: 2025-01 至 2026-05  
**搜索关键词**: model collapse + early warning/canary/leading indicator, synthetic data + iterative training + calibration/ECE, model collapse + Granger causality/lead-lag, self-consuming + collapse detection, distributional shift + synthetic data + monitoring

---

## Novelty 威胁评估摘要

| 威胁等级 | 说明 |
|---------|------|
| **安全** | **Granger causality lead-lag 分析**：无任何论文将 Granger causality 应用于 collapse metric 的时间因果分析。这仍是我们的核心 novelty。 |
| **注意** | **ECE-as-canary**：chen2025scales 仍是最直接竞争者，但未扩展到 lead-lag。若其团队跟进，novelty 窗口缩小。 |
| **注意** | **Entropy collapse 一阶相变**：Truong & Truong (2512.12381) 证明 entropy collapse 是不连续跳变，无传统 early warning signals——在剧烈 collapse regime 下可能挑战 canary 前提。 |
| **安全** | **多指标 panel 框架**：无人同时追踪 ECE + token_entropy + distinct_n + effective_rank 等指标并做 cross-correlation。 |

---

## A. 直接竞争者（Competitor）

### 1. Chen et al. — Characterizing Model Behavior Under Synthetic Data Training
- **arXiv**: [2510.05133](https://arxiv.org/abs/2510.05133)
- **发表**: 2025-10
- **核心方法**: Pythia 410M-12B 在 0-50% synthetic data mixing ratio 下评估 ECE、accuracy、output diversity
- **关键发现**: ECE 在 30% synthetic 时上升 75%，accuracy 尚未显著变化；更大模型（6.9B-12B）对 synthetic data 更 robust
- **与我们的关系**: **最直接竞争者**。观察到 "calibration degradation precedes accuracy loss" 但 (1) 未做 Granger causality / lead-lag 量化 (2) 未做多指标 panel (3) 仅横截面分析，非迭代 generation 纵向追踪
- **Novelty 威胁**: 中等。其 ECE-as-canary 观察与我们重叠，但方法论深度完全不同

### 2. SIGMA — Scalable Spectral Insights for LLM Model Collapse
- **arXiv**: [2601.03385](https://arxiv.org/abs/2601.03385)
- **发表**: 2026-01 (revised 2026-03)
- **核心方法**: Embedding Gram matrix 谱分析，导出确定性和随机谱界，可扩展到大模型
- **关键发现**: 谱收缩能追踪表征空间退化，提供可扩展的 collapse 健康监控工具
- **与我们的关系**: **互补+部分竞争**。我们的 effective_rank 是其谱方法的简化版。SIGMA 提供更严格的数学框架但 (1) 不做 lead-lag 时间因果 (2) 不追踪 calibration
- **Novelty 威胁**: 低。方法论正交，可作为 related work 中的互补方法引用

### 3. Gambetta et al. — Learning by Surprise: Surplexity for Mitigating Model Collapse
- **arXiv**: [2410.12341](https://arxiv.org/abs/2410.12341)
- **发表**: 2024-10 (revised 2025)
- **核心方法**: 从 next-token probability 分布直接度量 collapse（surplexity = 模型对文档的"惊讶度"），用高 surplexity 过滤训练数据
- **关键发现**: Collapse 发生在模型训练数据不再"令其惊讶"时；surplexity 过滤比人类数据 baseline 更有效
- **与我们的关系**: **互补**。Surplexity 与我们的 token_entropy 概念上相关（均基于 next-token distribution），但其目标是 mitigation（数据过滤），而非 prediction（lead-lag 预警）
- **Novelty 威胁**: 低

### 4. DCES — Dynamic Center-Edge Sampling for Iterative Self-Training
- **来源**: [MDPI Electronics 2025](https://www.mdpi.com/2079-9292/15/4/869)
- **发表**: 2025-02
- **核心方法**: Clustering-based 动态采样，用 intra-cluster dispersion 做实时监控，自适应调整 center/edge 采样比
- **关键发现**: 减缓 PPL/loss 退化和 entropy collapse
- **与我们的关系**: **互补**。同样用 metric 做实时监控，但目标是 mitigation（动态采样），不做 lead-lag 因果分析
- **Novelty 威胁**: 低

---

## B. 理论基础（Background）

### 5. Dohmatob, Feng & Pu — Strong Model Collapse
- **arXiv**: [2410.04840](https://arxiv.org/abs/2410.04840)
- **发表**: ICLR 2025 Spotlight
- **核心发现**: 即使 synthetic data 比例仅 1/1000，也会导致 asymptotic collapse；大模型先放大后减轻 collapse（double descent）
- **与我们的关系**: **背景**。为我们的 synthetic ratio 实验提供理论动机

### 6. Fu et al. — How to Prevent Model Collapse in Self-consuming Training Loops
- **arXiv**: [2502.18865](https://arxiv.org/abs/2502.18865)
- **发表**: ICLR 2025
- **核心发现**: 固定比例 real data 保证收敛（recursive stability）；对 transformer ICL 同样成立
- **与我们的关系**: **背景**。为我们的 alpha-sweep（synthetic ratio 扫描）提供理论基础

### 7. Gerstgrasser et al. — Is Model Collapse Inevitable?
- **arXiv**: [2404.01413](https://arxiv.org/abs/2404.01413)
- **发表**: ICLR 2025
- **核心发现**: 累积 real + synthetic data 可避免 collapse；完全替换则必然 collapse
- **与我们的关系**: **背景**。支持我们 pure synthetic (ratio=1.0) 作为压力测试的实验设计

### 8. Truong & Truong — Entropy Collapse: A Universal Failure Mode
- **arXiv**: [2512.12381](https://arxiv.org/abs/2512.12381)
- **发表**: 2025-12 (revised 2026-03)
- **核心发现**: Entropy collapse 是**一阶（不连续）相变**，hysteresis 约 2.73 nats，传统 early warning signals（autocorrelation, variance, critical slowing down）在此 regime 失效
- **与我们的关系**: **重要理论约束**。在凸反馈 regime 下，canary early warning 可能失效。我们的 100% synthetic 实验可能恰好处于此 regime（collapse 剧烈到 ECE/entropy 与 perplexity 同步跳变）。论文需讨论此局限性
- **Novelty 威胁**: 不直接威胁 novelty，但限制 claim scope

### 9. Schaeffer et al. — Position: Model Collapse Does Not Mean What You Think
- **arXiv**: [2503.03150](https://arxiv.org/abs/2503.03150)
- **发表**: 2025-03
- **核心发现**: Model collapse 有 8 种不等价定义（3 大类）；公共话语过度简化了科学证据
- **与我们的关系**: **背景/方法论**。我们需要明确界定使用哪种 collapse 定义（diversity collapse via distinct_n vs quality collapse via perplexity）

### 10. Shi et al. — A Closer Look at Model Collapse: Generalization-to-Memorization
- **arXiv**: [2509.16499](https://arxiv.org/abs/2509.16499)
- **发表**: NeurIPS 2025 Spotlight
- **核心发现**: Diffusion model 中 collapse 表现为从泛化到记忆的转变；提出 entropy-based 数据选择策略缓解 collapse
- **与我们的关系**: **互补**。Entropy 作为 collapse 指标的思路与我们一致，但 (1) 在 diffusion model 而非 LLM (2) 用于 mitigation 而非 temporal prediction

### 11. Guo et al. — The Curious Decline of Linguistic Diversity
- **arXiv**: [2311.09807](https://arxiv.org/abs/2311.09807)
- **发表**: NAACL 2024 Findings
- **核心发现**: Iterative self-training 下 lexical/syntactic/semantic diversity 持续下降；创意任务下降最快
- **与我们的关系**: **背景**。为我们的 distinct_n diversity collapse 度量提供先验支持

---

## C. Mitigation / Prevention（不直接竞争）

### 12. Feng et al. — Escaping Model Collapse via Synthetic Data Verification
- **arXiv**: [2510.16657](https://arxiv.org/abs/2510.16657)
- **发表**: 2025-10 (revised 2026-03)
- **核心方法**: 外部 verifier（人类或更强模型）过滤 synthetic data
- **与我们的关系**: **互补**。解决 "如何修复 collapse" 而非 "如何预测 collapse"

### 13. Wei & Zhang — Self-Consuming Generative Models with Adversarially Curated Data
- **arXiv**: [2505.09768](https://arxiv.org/abs/2505.09768)
- **发表**: ICML 2025
- **核心方法**: Adversarial curation 下 retraining 鲁棒性分析
- **与我们的关系**: **背景**

### 14. Falahati et al. — Curated Synthetic Data Doesn't Have to Collapse
- **arXiv**: [2605.07724](https://arxiv.org/abs/2605.07724)
- **发表**: 2026-05 (非常新)
- **核心方法**: 多 reward function curation 保持 diversity，收敛到加权 Nash 均衡
- **与我们的关系**: **背景**。理论上表明 collapse 可通过 pluralistic curation 避免

### 15. Bakshi & Chakraborty — From Collapse to Improvement
- **arXiv**: [2602.10531](https://arxiv.org/abs/2602.10531)
- **发表**: 2026-02
- **核心方法**: 统计分析 next-token LM 迭代训练中 mixture weight + sample size 对长期性能的影响
- **与我们的关系**: **背景**。为 synthetic ratio 的理论影响提供额外视角

---

## D. 相关但非直接相关

### 16. 多模态 Collapse
- Morreale et al. — Multi-modal Synthetic Data Finetuning and Model Collapse ([2505.08803](https://arxiv.org/abs/2505.08803))
- VLM + Diffusion model collapse 特征不同于 LLM
- **与我们的关系**: 仅作为扩展讨论

### 17. Calibration in Aligned LLMs
- Restoring Calibration for Aligned Large Language Models (ICML 2025, [OpenReview](https://openreview.net/forum?id=51tMpvPNSm))
- Alignment 后 LLM 校准退化
- **与我们的关系**: 背景。表明 ECE 退化不仅在 synthetic data training 中出现

### 18. OOD Detection with Synthetic Data
- ICLR 2025 SynthData Workshop: LLM-prompted synthetic OOD samples 用于 OOD 检测器训练
- **与我们的关系**: 弱相关

---

## 关键结论

### Novelty 状态：安全
1. **Granger causality lead-lag 框架**：文献中完全空白。无人对 collapse 指标做时间因果分析。
2. **多指标 panel（ECE + token_entropy + distinct_n + effective_rank）**：无人构建多维 canary dashboard。
3. **ECE leads diversity collapse 的量化证据**：chen2025scales 观察到 ECE 提前退化，但无 lag 量化。

### 需要在论文中讨论的约束
1. **Truong & Truong 一阶相变**（2512.12381）：在凸反馈 regime 下，entropy collapse 是不连续跳变，canary early warning 可能失效。我们需要：
   - 明确声明 canary 有效的 regime（渐进 collapse，如低 synthetic ratio）
   - 讨论 100% synthetic 下 canary 与 collapse 同步跳变的限制
2. **Schaeffer et al. 定义歧义**（2503.03150）：需精确界定我们的 "collapse" 指 diversity collapse（distinct_n 下降）而非 quality collapse（perplexity 增长）
3. **已有结果约束**：canary 仅 lead diversity metrics，不 lead perplexity——需在温和 collapse 条件下补充实验

### 建议引用优先级

**必引**:
- chen2025scales (直接竞争者)
- Dohmatob et al. Strong Collapse
- Fu et al. Recursive Stability
- Truong & Truong Entropy Collapse
- SIGMA 谱监控
- Gerstgrasser Accumulation

**应引**:
- Gambetta et al. Surplexity
- DCES 动态采样
- Shi et al. Gen-to-Mem
- Schaeffer Position Paper
- Guo Linguistic Diversity
- Feng Verification

**可引**:
- Wei & Zhang Adversarial
- Morreale 多模态
- Falahati 2026
- OOD Workshop
- Bakshi 2026
- Calibration Aligned LLM
