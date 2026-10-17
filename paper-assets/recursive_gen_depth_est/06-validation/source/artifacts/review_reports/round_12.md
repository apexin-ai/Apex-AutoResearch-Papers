---
round: 12
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-20T08:50:56.839034+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 15 (Fresh Review)

**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 (ARR May 2026 cycle), Long Paper
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）
**轮次**: Round 1, 1 轮收敛（交叉分享后关键问题达成共识）

---

## Summary

论文将递归生成深度估计形式化为序数分类问题（d0-d3），构建了 180K 样本的 benchmark（3 model families × 3 decoding strategies × 4 depths），使用 19 个统计特征 + Random Forest 实现深度分类。主要贡献包括任务形式化、Depth Degradation Atlas（系统映射不同策略下的退化轨迹）和 EDD 指标（量化可区分深度范围）。In-distribution accuracy 69-86%（d1-d3: 59-82%），cross-model transfer 66.4%（d1-d3: 55.4%），cross-strategy 59.1%（d1-d3: 45.9%），14B preliminary 50.8%（EDD₀.₇₀=0）。

---

## Strengths

**S1. 新颖且有意义的任务形式化。** 将深度估计从二元检测扩展为序数分类是自然且未被充分探索的方向。在 model collapse 日益受关注的背景下，区分"生成了几轮"比仅区分"是否生成"有更强的实用价值。Definition 1（§3.1）和 EDD 指标（§3.4）提供了清晰的形式化框架。[R1-S1, R2-S1 一致]

**S2. 系统的实验设计和全面的泛化分析。** 3×3 model-strategy grid、cross-model/cross-strategy/cross-domain transfer、7-14B 规模探索、d0-d5 深度扩展、种子稳健性——分析轴覆盖广泛。29 个附录实验展现了严肃的实验态度和高复现性。[R1-S2/S4, R2-S2 一致]

**S3. Depth Degradation Atlas 的系统映射。** §4 发现了解码策略诱导的质变差异：nucleus 保持单调衰减、temperature 引入 d1/d2 boundary inversion、top-k truncation 移除 depth-discriminative 低概率 tokens。这些发现对理解递归生成的统计机制有参考价值。[R1-S2, R2-S3 一致]

**S4. Limitations 部分诚实全面。** 覆盖了 full-replacement vs accumulation、scale limitation、BOS vs prompted、reference model dependency、cross-strategy deployment constraint 等核心局限。学术诚实度值得肯定。[R2-S5]

**S5. 引用质量高。** 74 篇引用中 63 篇 OpenAlex 验证通过，无伪造引用，所有 \cite 均有对应 bib 条目。[R1-S5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. [critical] Pipeline 缺乏算法创新，且与 Binoculars 无显著差异。**
核心 pipeline 是 19 个标准统计特征（perplexity moments/quantiles、surprisal statistics、lexical diversity、n-gram repetition）+ 标准 Random Forest（200 trees, 5-fold CV），无任何算法层面创新。更严重的是，Binoculars 11-feat RF 达到 78.1%，与本文 19-feat RF 的 78.4% 无显著差异（p>0.05, Table 4）。Merged 30-feat 82.6% 说明信息互补而非本文特征优越；Binoculars 独有 5 特征的边际贡献 (+4.2pp) 反而大于本文独有 13 特征 (+2.5pp, Appendix B.26)。
→ 论文的方法论贡献被大幅稀释。"discriminative signal resides in feature design"（Abstract）的 claim 恰好被 Binoculars 平局反驳。
[R1-N1 + R2-N1 + R2-N2 一致, 交叉 AGREE]

**C2. [critical] Cross-strategy 和 cross-scale 泛化严重不足，动摇方法实用性。**
- Cross-strategy transfer d1-d3 仅 45.9%（chance 33%），出现 d1/d2 boundary inversion。z-score normalization 修复 logistic regression 但不修复 RF，说明不同策略产生结构性不同的 depth signal（§5.3）。
- 14B cross-scale mean 50.8%，EDD₀.₇₀=0，5 个 confounders 未分离（§5.4）。
- 两个问题叠加：在 unknown strategy + large scale 部署场景下，pipeline 有效性几乎不可预期。
- 2026 年主流模型 7B-70B+，≤1.5B 结论实用参考价值有限。
→ 这不仅是 limitation，而是动摇核心 claim 的根本质疑。
[R1-N4 + R2-N3 + R2-W6 一致, 交叉 AGREE]

**C3. [critical] Self-reference confound 使 1/3 in-distribution 结果存在系统性偏差。**
Pythia-1.4B 同时是 generator 和 reference model，Table 2 显示 Pythia 比 OLMo/GPT-2 XL 高 4-11pp。Appendix B.13 换用 GPT-2 XL reference 时 accuracy 降至 67.3%（−11pp）。Cross-model transfer 中 Pythia holdout 62.4% 低于 OLMo 69.2%——self-reference confound 传递到 transfer 场景。Table 2 的 † 脚注和 B.13 ablation 部分缓解但 headline 数字仍包含膨胀。
[R1-N2 Must-Fix, R2 偏 Should-Fix; Director 裁定 Must-Fix — headline 数字直接受 confound 影响]

### Should-Fix（影响评分但不一票否决）

**W1. d0 膨胀 headline metrics。** d0 recall >97%（本质是已解决的 binary detection）。Cross-model headline 66.4% 排除 d0 后降至 55.4%，cross-strategy 59.1% 降至 45.9%。论文已在括号内并列 d1-d3 数字但不够突出——Abstract 和 §6 首句仍以 4-class accuracy 领头。
[R1-N3 Must-Fix, R2-W2 Should-Fix; Director 裁定 Should-Fix（高优先级）— 数据完整，问题在 framing]

**W2. EDD 阈值 T=0.70 理论依据不足。** 借自 Hosmer & Lemeshow (2000) 的 binary logistic regression AUC 标准，迁移到 ordinal pairwise AUC 未被论证。T=0.80 时多个 cell 丢失 depth level，结论对阈值敏感。monotonicity assumption 在 14B 打破。
[R1-W6 + R2-W4 一致, 交叉 AGREE]

**W3. 多重共线性（VIF>10 for 14-16/19）与可解释性 claim 矛盾。** Gini importance 和 SHAP 在高共线性下不稳定，§4.2 的特征重要性排序可靠性存疑。Appendix B.2 的 permutation importance 部分缓解但 SHAP（TreeSHAP）同样受影响。
[R1-W1, R2 交叉 AGREE]

**W4. Full-replacement 设置与现实 accumulation 场景脱节。** 主实验无 accumulation 条件。§6 引用 pilot 数据（70.1%/69.1% vs 84.2%）但缺乏系统评估。Limitations 透明但主实验 gap 仍在。
[R1-W3 + R2-W3 一致, 交叉 AGREE]

**W5. LoRA 微调超参无 ablation。** r=16, α=32 的选择直接影响生成文本质量和 depth signatures，不同 LoRA 配置可能产生不同退化模式。
[R1-W2, R2 交叉 AGREE]

**W6. Abstract 信息密度过载。** 10+ 个数字，核心 message 被淹没。建议精简至 3-4 个最关键数字。
[R2-W1, R1 交叉 AGREE]

**W7. Cross-domain web 文本 FPR 偏高。** C4 34%, FineWeb 17%（Appendix B.11），template/SEO content 的 n-gram repetition 触发 false positive。正文未充分讨论。
[R1-W4, R2 交叉 AGREE（修正"单域"表述）]

**W8. 多重比较未校正。** 多组 pairwise comparisons 未做 Bonferroni/FDR 校正。实际影响可能有限但统计规范性不足。
[R1-W5, R2 交叉 AGREE]

### Minor

- M1: 2 个 orphan bib entries (dsir2023, qurating2024)。[R1+R2 一致]
- M2: Binary RF 500 trees vs 4-class RF 200 trees 未解释。[R1]
- M3: 主文过度引用附录（§4-§6 几乎每段有 Appendix B.X），阅读碎片化。[R2]
- M4: Figure 3 混淆矩阵数字极小，建议改用 figure* 全宽。[视觉审查]
- M5: 引用 author 顺序 mismatch：alemohammad2024_mad、guo2024_biscope、hosmer2000。[R2]

---

## Reviewer Consensus [AGREE]

以下关键问题两位 Reviewer 达成完全共识：

1. **Binoculars 平局 + 无算法创新** → 方法论贡献不足以支撑 Main Conference [R1-N1 = R2-N1/N2]
2. **Cross-strategy/scale 泛化失败** → 实际部署价值受限 [R1-N4 = R2-N3/W6]
3. **EDD 阈值缺乏理论依据** → 核心指标稳健性存疑 [R1-W6 = R2-W4]
4. **d0 膨胀需处理**（严重程度有细微差异但问题本身无争议）[R1-N3 ≈ R2-W2]
5. **Full-replacement 脱离现实** [R1-W3 = R2-W3]
6. **论文定位为 Findings 更合适** [R1 Overall 3.0 = R2 Overall 3.0]

## Reviewer Divergence [REBUT]

1. **d0 膨胀的严重程度**：R1 列为 Must-Fix（headline 数字误导），R2 列为 Should-Fix（论文已并列报告 d1-d3）。
   → Director 裁定：**Should-Fix（高优先级）**。论文确实在关键位置并列了 d1-d3 数字，但应将 d1-d3 作为主打而非补充。

2. **Self-reference confound 严重程度**：R1 列为 Must-Fix（1/3 结果系统偏差），R2 认为 B.13 ablation 部分缓解。
   → Director 裁定：**Must-Fix**。虽然 ablation 在附录中，但 headline 数字（Abstract, Table 2）直接受 confound 影响，需要在主文中报告 excluding-Pythia 的 conservative estimate。

3. **Atlas 循环性（R2-W5）**：R1 [REBUT] 论证 Atlas 使用测量工具描述测量发现不构成循环，负面发现（某些特征不随 depth 单调变化）证明了非循环性。
   → Director 裁定：**接受 R1 的 REBUT**。Atlas 的 methodology 可用于任何特征集，其发现（strategy-dependent trajectories、feature hierarchy shifts with depth）是 legitimate empirical contribution。此项不列为 weakness。

---

## Questions（需作者澄清）

**Q1.** 如果使用完全不同架构的 reference model（如 Mamba/RWKV），特征提取结果会如何？当前 ablation（B.13）仅在 Transformer 内部换模型。[R1-Q1]

**Q2.** Perplexity tail features 捕获的是 depth-specific signature 还是仅仅是文本质量代理？depth-1 低质量文本与 depth-2 "正常"文本，特征能否区分？[R1-Q2]

**Q3.** z-score normalization 修复 logistic regression 但不修复 RF 的根本原因是什么？是否说明 RF 学到了 strategy-specific 非线性边界？[R1-Q3]

**Q4.** 14B 实验中 5 个 confounders 能否通过实验设计分离？例如用 14B reference model，或测试 Pythia-6.9B base（同架构无 instruction-tuning）。[R1-Q5]

**Q5.** 19-feature pipeline 相对 Binoculars 的实际优势是什么？科学上无显著差异（p>0.05），工程优势（1 model vs 2 models）是否足够？[R2-Q2]

**Q6.** 主 benchmark 仅 seed=42，能否提供 in-distribution multi-seed 结果？Appendix B.24 的 3 seeds 仅测 classifier seed，未测 data generation seed。[R2-Q4]

**Q7.** surprisal variance 和 perplexity tail（如 p90_ppl）在信息论上有何区别？是否是同一信号的不同视角？[R2-Q5]

---

## Missing References

**MR1. [critical]** Markovian Generation Chains in Large Language Models (arxiv:2603.11228, ICLR 2026)。直接研究 LLM 迭代生成的 Markov 链动态（convergence to fixed points、cycle behavior、decoding strategy 影响），与本文 recursive generation setup 和 strategy-dependent trajectory 发现高度相关。[R2 提出, R1 未独立验证真实性，建议作者核实]

**MR2. [minor]** Min-K%++（Zhang et al., 2024）。Min-K% Prob 的改进版本，应作为更强的 membership inference baseline 考虑。[R1]

**MR3. [minor]** RAID benchmark（Dugan et al., 2024）已引用但未解释为何不采用其评估协议。RAID 覆盖 11 个 LLMs + 多种 attack 手段，其 robustness evaluation framework 可提供更强验证。[R1+R2]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：**未请求**（项目未配置 `external_review.paperreview_ai.enabled`）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~4 分钟）。发现 2 critical + 4 warning + 9 info：

**Critical:**
- **前 3 页无任何 display item**（纯文字墙）。第一个 table（Table 1）在 p4，第一个 figure（Figure 1）在 p6。审稿人前 2 分钟内缺乏视觉锚点。**强烈建议在 p1-2 加入 pipeline 概览图或 teaser figure。**
- **Page 8 过度拥挤**：3 个 table（Table 4/5/6）+ 1 个 figure（Figure 3），Figure 3 混淆矩阵数字极小。

**Warning:**
- Display item 分布严重不均：前 5 页仅 1 个 table，后 3 页 8 个 display items。
- Page 5 纯文本页（§3.5 + §4 开头），形成额外文字断层。
- 全文缺少方法概览图/架构图（3 个 figure 全为分析性图表）。
- Figure 3 混淆矩阵字号远低于正文 70%，建议改用 figure*。

**页数合规**：正文 pp.1-8，Limitations p.9 起，符合 EMNLP 2026 8 页限制。
**匿名合规**：`\usepackage[review]{acl}`，"Anonymous ACL submission"，未发现去匿名化内容。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**
**Confidence: 4/5**

**评分理由：**

论文提出了一个新颖且有意义的任务形式化（递归生成深度的序数分类），构建了系统全面的 benchmark（180K, 3×3 grid），通过 Depth Degradation Atlas 和 EDD 指标提供了有价值的 empirical contribution。实验设计严谨，Limitations 诚实，附录极其详尽。

但论文的核心瓶颈在于：

1. **方法论贡献不足**：标准 RF + 标准统计特征，无算法创新，且与已有 Binoculars 特征无显著差异（p>0.05）。EMNLP 主会议期望至少在方法或理论层面有实质推进。

2. **泛化严重受限**：cross-strategy d1-d3 仅 45.9%（接近 chance），14B EDD₀.₇₀=0。在 2026 年 7B-70B+ 为主流的背景下，≤1.5B 的结论实用价值有限。

3. **Self-reference confound 膨胀 headline 数字**：1/3 in-distribution 结果存在系统偏差（4-11pp），headline 数字未充分修正。

这些问题使论文距离 Conference 水平（4.0）有明显差距。但 task formalization 的新颖性、benchmark 的系统性、Atlas 的 empirical value 使其达到 Findings 水平（3.0）——贡献真实且可复现，对 model collapse / data provenance / AI text detection 社区有参考价值。

**达到 Conference 水平的路径（供参考，非建议）：**
- 在 7B+ 规模提供完整 3×3 grid 并分离 confounders
- 引入超越标准 RF 的方法创新（如利用 LLM hidden states）或展示显著超越 Binoculars 的场景
- 以 non-overlapping reference model 报告 conservative headline 数字

---

## Detailed Comments（逐节）

**Abstract**: 信息密度过高（10+ 数字）。建议精简至：问题定义 → 方法概要 → 最重要的 2-3 个 takeaway（优先报告 d1-d3 balanced accuracy）。当前 framing 暗示 pipeline 方法本身是贡献，但 Binoculars 平局表明真正贡献在 task formalization + Atlas。

**§1 Introduction**: Narrative flow 清晰（recursive loop → depth matters → no ordinal estimation → our approach）。但 contributions 列表中"statistical features dominated by the perplexity tail family"容易被误读为特征设计创新，建议调整措辞为"we find that..."的 empirical finding 语气。

**§2 Related Work**: 覆盖面广（model collapse theory、AI text detection、membership inference、adjacent tasks、ordinal classification、decoding strategy effects），但遗漏 Markovian Generation Chains (ICLR 2026) 是一个 gap。PAN 2026 / M4-SemEval 的讨论过于简略。

**§3 Method**: 形式化清晰（Definition 1, §3.1）。Benchmark 构建合理但 LoRA 超参缺 ablation（r=16 是否 robust？）。19 特征的 VIF>10 应在此处注明而非推到 §4.2。EDD 定义（Eq. 1）形式正确但 τ=0.70 的选择需要更充分论证。

**§4 Depth Degradation Atlas**: 系统映射是论文最强贡献。Feature importance 分析（§4.2）受共线性影响需 caveat。Strategy-dependent trajectories（§4.5）发现有价值。EDD analysis（§4.4）中 depth ceiling 发现重要但 monotonicity claim 应明确限定在 ≤1.5B 范围。

**§5 Generalization and Robustness**: 覆盖全面但暴露了方法的核心局限。Table 4 的 Binoculars 对比是最大的方法论挑战。Cross-model transfer（§5.2）数字包含 self-reference confound。Cross-strategy transfer（§5.3）的 45.9% d1-d3 是严重的泛化警报。§5.4 的 14B 结果措辞已审慎（"Preliminary"）但 5 个 confounders 使结论几乎不可解读。

**§6 Discussion and Conclusion**: 密度适当，PLM R²<0 洞察和 accumulation 数据是有价值的补充。但"perplexity tail family dominates across all nine cells"的 claim 需修饰——cross-strategy transfer 失败表明 dominance 是 strategy-entangled 的。

**Limitations**: 诚实全面，覆盖了主要局限。建议增加：(1) Binoculars 平局的讨论；(2) multicollinearity 对 feature importance 的影响；(3) data generation seed 的 variance 未充分量化。

**Ethics Statement**: 存在且合理，讨论了潜在滥用风险。

**格式**: 页数合规（正文 8 页），匿名合规，引用格式统一。2 个 orphan bib entries 需清理。视觉审查发现前 3 页缺 figure、page 8 拥挤等布局问题（详见 Visual Layout Check 章节）。