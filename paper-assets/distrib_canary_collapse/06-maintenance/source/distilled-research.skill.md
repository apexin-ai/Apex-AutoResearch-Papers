---
name: distilled-research
description: "Model collapse 领域实验设计共识、理论框架、缓解策略与研究空白（25篇论文蒸馏）"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [guo2024linguistic, chen2025scales, gambetta2024surplexity, sigma2026spectral, shumailov2024curse, li2016diversity, noci2024mind, jing2022understanding, dey2024breaking, fu2025selfconsuming, feng2025escaping, barzilai2025consistency, gu2025datamixing, briesch2024selfconsuming, ba2024fill, alemohammad2024mad, kazdan2025collapse, he2025closer, dohmatob2024tale, dohmatob2025strong, dces2026counter, truong2025entropy, wang2026contaminated, du2026geometric, gauthier2026alignment]
  last_distilled: "2026-05-22T00:00:00Z"
---

# Model Collapse — Research Skill (25 papers)

## 实验设计共识

**三种循环范式必须对比**: Replace（全替换）、Augmentation（混合固定真实数据）、Accumulate（累积所有）。Replace 在 3-5 代崩溃，Accumulate 稳定。**9/25**。来源: Alemohammad (ICLR'24), Dey (ICML'24), Kazdan (ICML'25)。高。

**跨模型族验证**: 顶会期望 collapse 在扩散模型 + LLM + 解析模型 (Gaussian/Zipf) 上复现，至少 2-3 种。**8/25**。来源: Alemohammad (DDPM+StyleGAN+NF+Gaussian)。高。

**Gaussian/Zipf 解析基准**: 先推导理论 bound 再在神经网络验证，是理论论文的标准路线。**6/25**。来源: Dohmatob (ICML'24, ICLR'25)。高。

## 指标体系

**Image**: FID + Precision/Recall (k=5 NN)。**Text**: perplexity + 多样性 (TTR, Distinct-n)。**7/25**。高。

**上升趋势 — 熵诊断**: entropy-GS 相关 r=0.91 (He2025)，优于方差；熵崩溃是一阶相变 (Truong2025)；谱分析也在兴起 (SIGMA2026)。**4/25**。中。

**多样性降级层次**: 句法 > 词汇 > 语义退化速度。**2/25**。来源: Guo (NAACL'24)。中。

## 核心理论

**Strong collapse**: Etest ≃ B+V+ζ，ζ=p₂²c² 不可消除。即使 1% 合成数据也产生误差地板。**3/25**。来源: Dohmatob (ICLR'25 Spotlight)。高。

**Scaling law 退化**: 合成数据截断分布尾部 (top-p/temperature)，power-law → plateau。E_test ≍ T^{-c}+k^{-c'}。2% 真实数据触发 grokking。**3/25**。来源: Dohmatob (ICML'24)。高。

**累积防散**: 真实数据绝对量 (cardinality) 比比例 (proportion) 重要 (R²=0.59 vs 0.34)。合成数据仅在真实数据极度稀缺 (≤1024) 时有正向价值。**5/25**。来源: Kazdan (ICML'25)。高。

**相变理论**: α_c=1/(1-β) 处一阶相变，有滞后无早期预警。**2/25**。来源: Truong2025。中。

## 缓解策略

**Quality filtering 失效**: 过滤器偏好高频样本，放大多样性损失。**2/25**。中。

**Diversity-aware selection**: 熵/特征空间距离选择有效: FID 75.7→44.7 (He2025); DCES 动态采样也有效。**3/25**。中。

**Fresh real data 最稳健**: 2% 真实数据即触发恢复（含 grokking 延迟）。**7/25**。高。

## 竞品 claim 汇总

**Competitor**: Dey — 累积即可防止 collapse; Kazdan — cardinality > proportion; He — entropy-based selection 有效缓解
**Foundation**: Dohmatob — 1% 即不可逆; Shumailov — 尾部消失; Alemohammad — 无 fresh data 必崩

## 研究空白

- **Scale**: 无 >2B 参数 collapse 研究
- **跨模态**: image/text 独立，无多模态 collapse
- **RLHF**: 仅 Gauthier2026 研究 alignment loop collapse
- **检测→行动**: spectral/entropy 诊断与缓解策略研究脱节
- **分布式**: 无多智能体/联邦场景 collapse 传播研究
