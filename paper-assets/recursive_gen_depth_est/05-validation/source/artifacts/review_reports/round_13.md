---
round: 13
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-20T14:19:48.651758+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints

**目标 venue**: EMNLP 2026 (ARR May cycle)
**审稿轮次**: Round 16 (Fresh Review)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+相关工作）
**日期**: 2026-05-20

---

## Summary

本文将递归生成深度估计形式化为序数分类问题，构建了 180K 段落基准（3 个 1–1.5B 模型族 × 3 种解码策略 × 4 个深度），提取 19 维参考模型困惑度统计特征并用 Random Forest 在受控全替换递归链上达到 69–86% 四分类精度（d1–d3: 59–82%）。论文提出 Effective Discriminable Depth (EDD) 指标量化可辨识深度边界，发现 perplexity tail 特征族在所有 9 个配置中一致主导深度辨识。跨模型迁移 66.4%（d1–d3: 55.4%），跨策略迁移 59.1%（d1–d3: 45.9%），14B 尺度下 EDD=0。

---

## Strengths

**S1. 新颖且动机充分的问题定义。** 将 AI 文本检测从 binary（human vs. machine）推向 ordinal depth estimation 是一个有意义的学术贡献，填补了 model collapse 文献（假设 depth 已知）与 detection 文献（丢弃 depth 信息）之间的空白。[R1-S1, R2-S1 一致]

**S2. 大规模系统化实验设计。** 9-cell grid 系统控制了模型族、解码策略和深度三个维度。180K 样本量充足，配合 bootstrap CI、5-fold stratified CV、paired permutation test，方法学规范。[R1-S2, R2-S2 一致]

**S3. 特征收敛分析。** RF/XGBoost/LightGBM 在 0.4pp 内收敛，独立的 Binoculars 特征达到等价性能（78.1% vs 78.4%, p>0.05），Merged 82.6%——三重证据有效论证了信号存在于特征而非分类器。[R1-S5, R2-S3 一致]

**S4. 报告异常诚实透明。** 主动披露 d0 膨胀（Table 2 始终并列 d1–d3）、Pythia 自引用偏差（†标记 + 4–11pp 量化）、14B 负面结果（EDD=0）、跨策略迁移仅 45.9%。这种自我批评在投稿论文中罕见。[R1-S4（附录详尽）, R2-S4 一致]

**S5. 引用质量高。** 74 条引用经独立验证，62/74 在线确认，8 条为极新 preprint（确认真实），0 条伪造。覆盖 model collapse 理论、AI text detection、ordinal classification、decoding strategy effects 五个子领域。[R1-S6, R2-S5 一致]

**S6. Limitations 异常充分。** 覆盖 full-replacement vs accumulation、控制实验设定、跨策略瓶颈、d0 膨胀、域依赖 FPR、对抗鲁棒性、EDD 单调性、参考模型依赖、单 LoRA 实例共 9 个维度。[R2-S6]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [critical] 14B 结果（EDD=0）从根本上削弱核心叙事** [R1-N4 + R2-N1, 共识]
- 论文 motivation 是 web-scale 递归污染（§1 第 1 段），但 web 上的合成内容来自 GPT-4/Claude 等大模型，不是 1.4B 模型。Qwen2.5-14B 上 EDD_{0.70}=0，mean accuracy 50.8%（2× chance），相邻深度在该尺度下不可区分。
- 5 个 confounds（self-reference、QLoRA 量化、architecture mismatch、vocabulary mismatch、scale gap）不可分离，论文未尝试同族 reference model（如 Qwen2.5-7B）消除 architecture/vocabulary mismatch。
- 7–8B 中间结果（Llama-3.1 70.2%, Qwen2.5-7B 60.1%）显示信号随尺度衰减但未消失，但这些实验也有量化 confound。
- **Director 裁定**: 这是对论文核心 thesis 的最严重挑战。论文用 "Preliminary" 修饰但实际上这一结果需要主文级别的深入分析，而非 3 行概述 + 附录。

**N2 [critical] 方法贡献不足——标准特征 + 标准分类器** [R2-N2 critical, R1 交叉 REBUT 降为 should-fix]
- 论文自述 "contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty"（§1 第 5 段）。核心 pipeline 是参考模型困惑度统计特征（均值、方差、分位数）+ Random Forest——均为标准工具。
- Binoculars 11-feat RF 达到统计等价性能（78.1% vs 78.4%, p>0.05, Table 4），表明 pipeline 并非不可替代。
- R1 反驳称 Findings 不要求算法创新，且 Binoculars 需要 observer+performer 两个模型而本文仅需单一 reference model，部署更轻量。
- **Director 裁定**: R1 的反驳部分有效——task formalization + benchmark 确实有 empirical contribution 价值。但当方法无创新、Binoculars parity、且 14B 失败三者叠加时，contribution 整体偏弱。维持 critical 但认为在 Findings 标准下通过适当 claim 调整可解决。

**N3 [critical] Cross-strategy transfer 深层深度接近 chance** [R1-N3, R2 交叉 AGREE]
- Cross-strategy transfer d1–d3 仅 45.9%（Table 6），chance = 33%，仅高出 12.9pp。d0 recall ≥89% 拉高 overall 到 59.1%，掩盖了深层深度的弱识别力。
- Strategy effect (9.3pp range) 超过 model effect (7.2pp)，decoding strategy 是更强的混杂因素。
- Two-stage pipeline 回收 11.5pp，但 strategy identification 本身仅 57.8%。
- R2 补充：跨策略弱本身是有价值的 negative finding——"解码策略比模型架构更影响 depth fingerprint"对后续研究有指导意义。
- **Director 裁定**: 在 strategy-unknown 部署场景下方法实际可用性极为有限。论文应明确限定 claim 为 within-strategy 或 known-strategy 场景。

### Should-Fix（影响评分但不一票否决）

**W1 [warning, high priority] Full-replacement 设置与现实 accumulation 场景脱节** [R2-N3 critical, R1 AGREE]
- 所有实验使用 full-replacement chain，现实中是 accumulation（合成+人类数据混合）。Pilot accumulation 数据（-14 to -15pp vs 84.2%）仅以 1 行文字出现在 §6，无表格支撑。
- Director 裁定 should-fix (high priority): 是 structural limitation，论文 Limitations 已 acknowledge，但应在附录中系统呈现 accumulation 数据。

**W2 [warning, high priority] Self-reference confound** [R1-N1 critical, R2-W2 should-fix]
- Pythia-1.4B 同时做 generator 和 reference model（3/9 cells），4–11pp 系统优势。Headline 数字未修饰地包含膨胀 cells。
- R2 认为论文的透明标记（†）和 ablation（67–79%）部分缓解。
- Director 裁定 should-fix (high priority): 透明度值得肯定，但应在 Table 2 旁增加 6-cell clean subset 汇总，Abstract/§1 headline 应区分。

**W3 [warning] 多重共线性对 feature importance 叙事的影响** [R1-N2 critical, R2 REBUT]
- VIF>10 for 14–16/19 features，Gini importance 在高共线性下不稳定。
- R2 有力反驳：(1) 论文 claim 是族级而非个体特征；(2) 三种 importance measure Kendall's W=0.90；(3) 消融实验（perplexity alone 76.6% vs surprisal 73.2% vs others ≤47%）直接支撑族级 claim。
- Director 裁定 should-fix: R2 反驳有说服力，族级 claim 由消融实验直接支撑。建议增加 group-level ablation 数字到主文，使读者无需依赖 importance ranking 即可验证。

**W4 [warning] Abstract 信息过载** [R2-W1, R1 AGREE]
- 12+ 个具体数字，核心 message 被淹没。应聚焦 3 个核心发现：(1) 任务可解且信号在困惑度尾部；(2) 策略比模型更影响迁移；(3) 信号随尺度衰减。

**W5 [warning] d0 膨胀 headline metrics** [R1-N3 部分, R2 隐含]
- d0 recall >97% 系统拉高 4-class accuracy。Cross-model 66.4% 中 d0 贡献巨大（d1–d3 仅 55.4%）。论文已并列报告但 4-class 仍领头。

**W6 [warning] EDD 阈值 T=0.70 缺乏独立验证** [R1-W1, R2 AGREE]
- T=0.70 直接从 binary AUC "acceptable discrimination" 标准迁移。Sensitivity analysis 显示偏移 ≤1 level，部分缓解。

**W7 [warning] BOS-seeded generation 限制生态效度** [R1-W3, R2 AGREE]
- 180K 样本均从 BOS token 生成。Prompted generation -13.8pp 且仅 1/9 cell 验证。Prompted recursive chain（用 prompting 而非 LoRA 驱动递归）完全未测试。

**W8 [warning] Wild-data FPR 过高** [R1-W4, R2 REBUT]
- C4 34%, FineWeb 17%。R2 指出 confidence thresholding 降至 2.8%/0.7%（-0.3pp cost）。Director 保留 should-fix: 阈值方案有效但 domain-dependent。

**W9 [warning] Discussion+Conclusion 过于压缩** [R2-W5, R1 AGREE]
- §6 仅 5 行正文，同时承担 discussion/conclusion/limitations/future work。缺乏对结果的理论解读。

**W10 [warning] 缺乏具体使用场景论证** [R2-W4, R1 AGREE]
- 论文动机以 data curation 和 model collapse monitoring 开头，但无 concrete deployment scenario。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 共识 |
|------|-----|-----|------|
| 14B failure | N4 critical | N1 critical | **[AGREE]** 核心问题 |
| Cross-strategy near chance | N3 critical | Q4 隐含 | **[AGREE]** R2 补充 negative finding 价值 |
| Full-replacement gap | AGREE R2-N3 | N3 critical | **[AGREE]** |
| Method novelty | W2 should-fix | N2 critical | **分歧**：R1 认为 Findings 不要求算法创新 |
| Self-reference confound | N1 critical | W2 should-fix | **分歧**：R2 认为透明标记已缓解 |
| Multicollinearity | N2 critical | REBUT → should-fix | **分歧**：R2 反驳族级 claim 已由消融支撑 |
| Abstract overload | AGREE | W1 | **[AGREE]** |
| Overall score | 3.0 Findings | 3.0 Findings | **[AGREE]** 完全一致 |

---

## Reviewer Divergence

**分歧 1: 多重共线性的严重程度** — R1 认为 critical（VIF>10 下 Gini 不稳定动摇核心叙事），R2 REBUT 认为 should-fix（族级 claim + 消融实验不依赖 importance ranking）。Director 采纳 R2 立场：消融实验（perplexity alone 76.6% vs others ≤47%）直接支撑族级 claim，但建议主文增加 group-level ablation 数字。

**分歧 2: Self-reference confound 的严重程度** — R1 认为 critical（headline 数字包含膨胀），R2 认为 should-fix（透明标记 + ablation 67–79% 部分缓解）。Director 采纳 R2 立场但提高优先级：论文诚实度应被肯定，但 headline 数字应补充 clean subset。

**分歧 3: Method novelty 的严重程度** — R2 认为 critical（标准工具无创新），R1 REBUT 认为 should-fix（Findings track 接受 empirical contribution）。Director 维持 critical：方法无创新 + Binoculars parity + 14B 失败的组合效应使贡献整体偏弱，但在 Findings 标准下可通过 claim 调整解决。

---

## Questions（需作者澄清）

**Q1.** 如果统一使用 OLMo-1B 作为所有 9 cell 的 reference model，Table 2 的 overall accuracy 和 EDD 如何变化？[R1-Q1, R2 AGREE]

**Q2.** PCA 前 3–5 个 component 训练 RF 精度是否接近 19-feat RF？若是，则更 parsimoniously 支撑 claim。[R1-Q2, R2 AGREE]

**Q3.** Pilot accumulation 实验的具体设置——mixing ratio、cell、EDD estimate？[R2-Q1, R1 AGREE]

**Q4.** 14B 下哪些具体特征失去区分度？Lexical diversity 和 repetition 在 14B 上是否保留？[R2-Q2, R1 AGREE]

**Q5.** Strategy-unknown 条件下 pipeline 如何实际可用？[R2-Q4, R1 AGREE]

**Q6.** Cross-strategy transfer 方向性是否对称（nucleus→temp vs temp→nucleus）？[R1-Q3]

**Q7.** Binoculars parity 是否意味着 depth signal 本质是 cross-perplexity divergence，还是两条路径独立收敛于同一 information ceiling？[R2-Q5, R1 REBUT 认为是后者]

---

## Missing References

**高相关性（应引用）：**
1. Strobl et al. (2008) "Conditional variable importance for random forests" — 直接解决多重共线性下特征重要性问题 [R1]
2. Hooker et al. (2021) "Unrestricted Permutation Forces Extrapolation" — permutation importance 在 correlated features 下的偏差 [R1]

**中等相关性（建议引用）：**
3. Wang et al. (2025) "LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs" arXiv:2506.15690 — 多模型网络 collapse 动态 [R2]
4. Xie et al. (CVPR 2025) "Training Data Provenance Verification" — 跨模态数据溯源 [R2]
5. arXiv:2505.11550 "AI-Generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification" — 多分类检测 [R2]

**引用验证结果**: 74 条引用中 62/74 在线验证通过，8 条确认为极新 preprint，0 条伪造。4 条 metadata 不一致（作者排序差异，不影响真实性）。R15-MR1 遗漏的 Markovian Generation Chains (arXiv:2603.11228) 已在 §2 Related Work 中引用，标记 resolved。

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未配置 `external_review.paperreview_ai.enabled`）。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（2026-05-20 14:01–14:05）

**Critical findings:**
1. **前 3 页无视觉锚点** — 审稿人连续阅读 3 页纯文本后才看到首个 display item（Table 1, page 4）。强烈建议在 page 1–2 加入概念图或核心结果 overview figure。
2. **页数合规性存疑** — 视觉审查报告 Discussion 延伸至 page 9 约 1/3。但 R15 视觉审查曾确认合规（正文 pp.1–8, Limitations p.9 起）。**需重新验证 PDF**，可能是编译版本差异。

**Warning findings:**
3. Display items 分布严重不均（pp.1–5 仅 1 个，pp.6–8 堆积 8 个）。
4. Page 8 过度密集：3 tables + 1 figure（Figure 3 混淆矩阵数字 <6pt，打印后可能难辨）。

**Info findings:** Figure 1 热力图可读但单元格文字偏小；Figure 2 AUC 曲线清晰；所有表格 booktabs 风格规范；参考文献格式统一；Appendix 尾页正常。

---

## Overall Assessment

**Overall**: 3.0 (Findings — 可被 Findings 接收)

**Soundness**: 3.5/5 — 受控设定内的主要 claim（depth discriminability exists at 1–1.5B scale）有充分实验支撑。统计方法学规范（bootstrap CI, 5-fold CV, permutation test）。但 self-reference confound 膨胀 1/3 cells 的 headline 数字，14B 实验有 5 个不可分离的 confounds。

**Excitement**: 2.5/5 — 任务形式化新颖（ordinal depth estimation），但方法无算法创新，14B 尺度障碍严重限制实际意义。perplexity tail dominance 和 strategy > model 的 finding 对后续研究有指导价值，但 information ceiling (~78%) 和 EDD=0@14B 限制了 excitement。

**Reproducibility**: 4/5 — 超参数、pipeline 细节、代码结构在 supplementary 中完整披露。数据承诺 acceptance 后发布。Cross-seed replication 仅 3/9 cells（wont_fix），但已报告 seed=43 结果。

**Confidence**: 4/5

**理由**: 两位 Reviewer 独立给出完全一致的 3.0 Findings 评分。论文在任务形式化、benchmark 设计和报告诚实度方面达到了高水准。三个互相关联的 critical 问题阻止主会议推荐：(1) 14B 失败意味着方法在实际相关尺度上未被验证；(2) 标准方法 + Binoculars parity 使方法贡献不足；(3) cross-strategy d1–d3 仅 45.9% 限制了实际部署场景。作为 empirical characterization study，论文属于 Findings 上段——实验扎实、报告诚实、有 useful findings（perplexity tail dominance、strategy > model for transfer、EDD ceiling、feature convergence across classifiers）。建议修改方向：(1) 限缩 scope 为 "small-scale within-strategy depth estimation"；(2) 主文扩展 14B 分析；(3) 补充 accumulation 数据；(4) 报告 clean 6-cell baseline。

---

## Detailed Comments（逐节）

**Abstract**: 12+ 个数字过载。建议精简为 3 个核心发现 + 1 个核心局限（14B EDD=0）。

**§1 Introduction**: Motivation 清晰但 scope 与实验能力不匹配——以 web-scale 开头但方法仅验证于 1–1.5B。建议开门见山限定 scope。缺乏具体使用场景描述。

**§2 Related Work**: 覆盖全面（1 页），但可压缩以释放空间给 Discussion。引用可补充 Strobl (2008) 和 Hooker (2021) 以支持 feature importance 讨论。

**§3 Method**: 问题定义清晰（§3.1）。EDD 定义（Definition 1, §3.3）有概念价值但 T=0.70 的阈值选择需增加 justification。BOS-seeded 生成应在此节讨论其对信号强度的影响。

**§4 Depth Degradation Atlas**: 核心实验节。Table 2 应补充 6-cell clean subset。Feature importance 分析应在主文报告 group-level ablation 数字。Figure 1 热力图可读但列宽受限。

**§5 Generalization**: 最关键的评估节。Cross-model (66.4%) 和 cross-strategy (59.1%) 的 d1–d3 数字应更突出。§5.4 的 14B 结果需大幅扩展。Binoculars parity 讨论应更深入分析 information ceiling 假说。

**§6 Discussion+Conclusion**: 仅 5 行，严重不足。应拆分 Discussion 和 Conclusion，Discussion 增加：(1) perplexity tail dominance 的理论 implications；(2) strategy-dependent trajectories 对 AI safety 的意义；(3) depth signal 的 scale dependence 对 model collapse 理论的 feedback。

**Limitations**: 异常充分（9 个维度），但缺少 BOS vs prompted gap 和 wild-data FPR 的部署影响讨论。

**Ethics**: 覆盖基本要求。

**Appendix**: 21 个 section，透明度极高。关键建议：per-class recall 和 reference model ablation 的核心数字应提升到主文。