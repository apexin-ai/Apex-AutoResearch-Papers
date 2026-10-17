---
round: 3
overall_score: borderline
timestamp: 2026-05-16T12:23:20.284002+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4

**论文**: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"
**Venue**: EMNLP 2026 (ACL Rolling Review May cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达共识）

---

## Summary

本文形式化了"递归生成深度估计"任务（ordinal classification），构建了 180K 样本的 3×3 benchmark（3 model families × 3 decoding strategies × 4 depths），提取 19 维统计特征（以 perplexity tail statistics 为主导），用 Random Forest 达到 70-85% 四分类准确率（d1-d3 三分类 58.8%-82.6%）。引入 EDD metric 量化可区分深度前沿，评估了 7 个泛化轴。论文经历了 3 轮前期审稿修订，解决了公式错误、统计检验缺失、attention-importance 方法论缺陷等问题。本轮审稿聚焦于 claims 与 evidence 的对齐、统计严谨性、以及方法论新颖性。

---

## Strengths

1. **任务定义有价值**：从 binary AI detection 到 ordinal depth estimation 是有意义且自然的推进，与 model collapse 文献形成互补。
2. **系统性实验设计**：3×3 grid + 7 个泛化轴的评估相当 thorough；实验设计允许分离 model effect 和 strategy effect。
3. **关键 empirical findings 具有洞察力**：
   - Feature hierarchy 随 depth 转换（shallow: var_surprisal → deep: p90_ppl）与 model collapse 理论一致
   - Decoding strategy 对 degradation trajectory 的 qualitative reshaping（非单纯 attenuation）
   - Top-5 features 达 97.6% of full performance，揭示有效独立维度 ≈4-5
4. **Reproducibility 强**：特征定义精确、实验超参数详尽、承诺开源。
5. **诚实的 Limitations section**：主动报告 d0 inflation、cross-strategy inversion、ecological validity gap、EDD monotonicity 假设，显示学术诚信。
6. **Domain bias analysis**（Appendix）：发现并修正 seed-group confound，报告 bug fix 前后数字，透明度高。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[N1] EDD₀.₇₅=4 的 abstract 无条件陈述缺乏统计支撑** [consensus: 2/2 AGREE]

Abstract L6 宣称 "finding EDD₀.₇₅=4 for extended recursion chains"，但 §4.4 报告 GPT-2 XL d3v4 AUC=0.750（恰在阈值边界），bootstrap p=0.505（non-significant）。三模型中仅 Pythia (p=0.001) 统计显著，OLMo (p=0.091) marginal。无条件通用陈述与仅 1/3 模型达统计显著性不符。

→ **修改方向**：Abstract 改为 "EDD₀.₇₅=4 (Pythia, p=0.001; consistent direction across models with graded statistical support)" 或使用 T=0.70（所有模型均 >0.70 at d3v4）。

**[N2] Zero-shot LLM baseline 是结构性不公平对比** [consensus: 2/2 AGREE]

LLM 读 raw text 时无法获取 reference model 计算的 perplexity distribution——对比的不是"方法能力"而是"信息可及性"。§6 Discussion 中反复引用 "42pp superiority" 作为 primary comparison 属于 strawman 论证。正确定位应为 "oracle study showing statistical features are necessary for depth discrimination"。

→ **修改方向**：重新定位为 ablation study（"surface text alone ≠ depth signal"），而非 comparative advantage；或给 LLM 提供 perplexity features 作为 context（tool-use/few-shot with features）。

**[N3] Cross-scale "泛化"声明基于 N=2 个 confound-stacked 模型** [consensus: 2/2 AGREE]

仅 2 个 7B 模型，行为完全矛盾（Llama monotonic vs Qwen U-shaped）。Confounds 叠加：(1) 4-bit NF4 QLoRA（1.4B 无量化）；(2) instruction-tuned（1.4B 为 base models）；(3) 500 samples（vs 5000）；(4) 仅 nucleus。从两个矛盾 data points + 多重 confounds 无法推出 "depth signal persists at scale" 的通用结论。论文 §5.5 caveats 承认此问题但 abstract/discussion 未反映。

→ **修改方向**：降级为 "preliminary cross-scale observations"；明确列出 confound 清单；理想情况下加一个 base model at 7B。

**[N4] Cross-model recursive chain (84.75%) 存在 architecture-depth confound** [consensus: 2/2 AGREE, R1 在交叉回应中补充]

Heterogeneous chain (d1=Pythia, d2=OLMo, d3=GPT-2 XL) 将 model identity 与 depth 完全 confound。Pythia reference model 对不同架构的 text 天然产生不同 perplexity profiles，分类器可能利用 architecture fingerprint 而非 pure depth signal。"Depth signal is a property of the recursive process itself" 这一核心 claim 可能被此 confound 削弱。

→ **修改方向**：在 Appendix 讨论此 confound；弱化 abstract claim 为 "preliminary evidence consistent with process-level signal"。

---

### Should-Fix（影响评分但不一票否决）

**[W1] Feature importance "universal marker" 在极端共线性下可信度降低** [consensus: 2/2 AGREE]

VIF>10 for 14-16/19 features。Gini/SHAP/Permutation 三种方法在高共线性下有相似 instability pattern，concordance (W=0.90) 不能证明单特征级别的稳定性。Forward selection p90_ppl 仅 6/9 cells 首选。建议报告 feature group level importance 或弱化 "p90_ppl AND var_surprisal emerge as universal markers" 为 "perplexity tail statistics group dominates"。

**[W2] Curation PoC 全部 non-significant (p>0.4)** [consensus: 2/2 AGREE]

rf vs unfiltered: p=0.407/0.492/0.607——所有对比 non-significant。"Matches unfiltered with 44% data" 是 null result（无法拒绝零假设），非 positive finding。5 seeds (df=4) 统计功效极低。rf vs random 的显著性可能仅反映 "保留 d0/d1 = 保留更好文本"（binary detection 即可实现）。建议降级为 "inconclusive pilot" 或增加 seeds。

**[W3] BOS-seeded 无条件生成降低生态效度** [consensus: R1 correct, R2 初始 REBUT 后承认论文确为 BOS-seeded]

§3.2 明确 "BOS-seeded, no prompt conditioning"。无条件生成的更高 repetition/更低 coherence 可能人为放大 depth signal。Introduction/Discussion 的 deployment framing ("early-warning signal", "provenance toolkit") 与 controlled BOS-seeded setting 存在张力。

**[W4] d0 inflation 在 transfer results 中仍不够显著** [consensus: 2/2 AGREE]

In-distribution 部分已修复（Table 1 括号内含 d1-d3）。但 cross-model 66.4% 对应 d1-d3 仅 55.4% (1.66× chance)，abstract 对 transfer 结果缺显式 qualification。

**[W5] 方法论新颖性有限** [consensus: R2 critical, R1 agree with caveats → 最终 warning 级]

核心方法是标准 perplexity features + off-the-shelf RF。"Atlas" 是参数网格评估，"EDD" 是 pairwise AUC threshold。无新算法或理论框架。但 EMNLP 接收 "novel task + systematic empirical contribution" 型论文——task formalization + non-trivial empirical findings 可支撑接收，只是降低 excitement。

---

### Info / Minor

1. Abstract 信息密度过高（15+ 数字）——建议精简至核心 3-4 个
2. §4.4 footnote "AUC profiles are empirically monotonically decreasing" 已被 Qwen U-shape 违反——需更新
3. `yi2026_escaping_collapse` 为 orphan bib entry（未在正文引用）
4. Mohamed et al. (2025) "Broken Telephone" 区别仅一句——建议扩展至 2-3 句
5. C4 FPR (4.7% vs 22.4%) 建议加 95% Wilson CI（n=5000 下效应量足够大，formal test 非必需但 CI 应报告）

---

## Reviewer Consensus

两位 Reviewer 在所有 Must-Fix（N1-N4）和 Should-Fix（W1-W5）上达成完全共识，无未解决矛盾。

**共识要点**：
- 论文的核心问题不是实验不够多，而是 **claims 系统性超出 evidence 支撑范围**
- Task formalization 和 systematic empirical contribution 有价值，但 framing 需要显著降低
- 方法论新颖性有限但不构成 reject 理由（EMNLP 接收 empirical papers）
- 如修正 overclaiming + 补充统计限定，可达 Findings 或 borderline main conference 水平

## Reviewer Divergence

**唯一实质分歧**（已在交叉回应中解决）：

| 议题 | R1 | R2 | 解决 |
|------|----|----|------|
| R2-N1 "70.30% 来源不清" | REBUT: abstract 原文是 "70--85%" range | 接受 REBUT | 降为 presentation issue（abstract 密度过高增加误读风险）|
| 新颖性严重程度 | Warning (task contribution 可接受) | Critical (方法无创新) | 折中为 warning：不 reject 但降低 excitement |
| R1-W4 BOS-seeded | Valid concern | Initially REBUT (误以为 prompt-conditioned) | R1 correct——论文明确 "BOS-seeded, no prompt conditioning" |

---

## Questions

1. EDD₀.₇₅=4 是否应改用 T=0.70 使结论更稳健（所有模型均显著）？
2. Cross-model chain 的 sample size 是多少？论文未明确报告。
3. Forward selection 另 3/9 cells 首选什么特征？如是 p50/mean_surprisal 则进一步支持 "group dominance" 而非 "individual feature dominance"。
4. Curation PoC 中 oracle_strict PPL worse than unfiltered——是否意味着 depth filtering 机制需重新解释？
5. 是否考虑过至少一个 7B base model（非 instruction-tuned）来隔离 RLHF confound？

---

## Missing References

1. Guo et al., "Curious Decline of Linguistic Diversity" (2024) — LLM 输出 lexical diversity 下降
2. Padmakumar & He, "Does Writing with Language Models Reduce Content Diversity?" (2024)
3. Briesch et al., "Large Language Models Suffer From Their Own Output" (2024)
4. Self-play / iterative self-improvement 文献 (SPIN 等) — recursive generation 的另一面
5. Seddik et al. 2025 "How Bad is Training on Synthetic Data?" — scaling law 分析

---

## External Review (Stanford Agentic Reviewer)

外部审稿未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**Score: 3.25/5 — Borderline (Findings acceptance, with revision potential for main conference)**

**评分构成**: R1 = 3.5/5, R2 = 3.0/5, 加权平均 3.25/5

**置信度**: 4/5（两位 Reviewer 均报告高置信度，交叉回应中达成完全共识）

**一句话判断**: 有价值的任务定义 + 系统性实验，但 claims 系统性超出 evidence 支撑范围且方法论新颖性有限。修正 overclaiming 后可稳定进入 Findings track；如能补充理论分析（连接 model collapse theory 与 perplexity tail encoding depth 的 formal connection）或解决 confound 问题，有潜力升至 main conference borderline。

**关键修改清单（按优先级）**:
1. [Must] Abstract/Discussion 中 EDD₀.₇₅=4 加统计限定
2. [Must] LLM baseline 重新定位为 ablation 而非 comparison
3. [Must] Cross-scale 降级为 "preliminary observations" + 列 confound 清单
4. [Must] Cross-model chain 讨论 architecture-depth confound
5. [Should] Feature importance 弱化为 group level
6. [Should] Curation PoC 降级为 "inconclusive pilot"
7. [Should] 弱化 deployment-oriented framing

---

## Detailed Comments

### §1 Introduction
- Contribution bullet 3 的 "generalization across seven axes" 需加 qualification——多数 axis 的 performance 远低于 in-distribution，framing 与 evidence 存在张力
- "universal and scale-variant" 措辞需限定为 "within our experimental scope"

### §3 Method
- §3.2 BOS-seeded 设计的生态效度影响应在此处即 acknowledge（而非仅在 Limitations）
- LoRA "architecture-specific targets" 缺细节——对 reproducibility 重要

### §4 Atlas
- Table 2 feature importance 的 individual-level claims (p90_ppl 9/9, var_surprisal 8/9) 应加注 "under high multicollinearity; see §4.2 for group-level interpretation"
- §4.4 脚注关于 monotonicity 已过时

### §5 Generalization
- §5.1 LLM baseline 需 repositioning
- §5.4 Cross-scale 需更显式的 confound 声明
- Appendix K Cross-model chain 需 confound 讨论

### §6 Discussion
- "Early-warning signal for model collapse" framing 超出实验支撑
- Curation PoC 引用需降级
- "42pp" 论述逻辑需修正

### Formatting/Bib
- `yi2026_escaping_collapse` orphan entry
- Mohamed et al. 区别需扩展
- Abstract 数字密度建议精简