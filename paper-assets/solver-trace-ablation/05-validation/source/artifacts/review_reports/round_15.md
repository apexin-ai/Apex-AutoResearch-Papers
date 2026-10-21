---
round: 15
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-20T04:33:13.396692+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 15 (Fresh Review)

**Paper**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性 + 实验设计 + 统计分析), R2 (新颖性 + 相关工作 + 完整性 + 格式)
**Review mode**: Fresh (无历史轮次记忆)

---

## Summary

本文提出 Solver Trace Ablation (STA)——对 GRPO 训练的神经符号形式化器进行 leave-one-out 消融的诊断方法。ISR (Intensional Structural Reward) 量化 proved formalization 中各组件的必要性比例。核心发现：(1) ISR 作为诊断揭示 exec-only GRPO 下的结构坍塌（ISR: 0.642→0.003 同期 PR: 32%→96%）；(2) ISR 转为训练奖励后被模型 game（作者称 "meta-level Goodhart's Law"），产生 8 种 hacking 模式；(3) 跨数据集（ProofFOL）验证显示 ISR 产生 dataset-dependent 结果。实验在 Qwen3-4B/FOLIO 上用 3 seeds 完成。

---

## Strengths

**S1 [Consensus].** 问题选择精准：neurosymbolic reasoning + RL reward hacking 的交叉领域鲜有系统研究。ISR collapse 轨迹（Figure 2: ISR 0.642→0.003 而 PR 32%→96%）为 execution-only 指标的盲区提供了有说服力的经验证据，对 RLVR 社区有直接实践意义。

**S2 [Consensus].** STA/ISR 设计简洁可操作：确定性、O(n)、不依赖 reward model 或人工标注。Algorithm 1 清晰，定义干净（Eq. 1），可复用性好。

**S3 [Consensus].** 实验设计全面：6 个 reward conditions（exec-only, ISR β∈{0.1,0.2,0.3}, matched random, SFT），2 个逻辑类型（FOL/Prolog），2 个数据集族（FOLIO/ProofFOL），3 seeds 重复，1000-step 训练轨迹动态追踪。

**S4 [Consensus].** Hacking taxonomy（8 种模式含 query-as-fact gaming 和 H7b obfuscated tautology）系统归纳了 reward exploitation 行为，配有 FOL/Prolog 具体示例，为后续研究提供有用分类框架。

**S5 [Consensus].** 局限性讨论透明：premise-count confound、ISR syntactic-only 性质、seed-level variance 均被讨论。

**S6 [R2].** 引用管理干净：31 条 bib entry 与 31 个 unique citation key 完全对应，无 orphan 或 missing。

---

## Weaknesses

### Must-Fix (Critical)

**N1 [Consensus, Critical] 3 seeds 统计效力不足，aggregate 统计几乎无解释力。**
- 每条件仅 3 seeds，跨 seed 方差极大（ISR β=0.3: PR 0.18–0.95, Table 9）。
- 每个 seed 走向质性不同的 Goodhart 路径（s42=reward collapse, s43=H1 shortcutting, s44=pure H7），汇总统计量（如 3-seed mean）在此 multi-attractor 动态下缺乏代表性。
- ProofFOL permutation test（p=0.10, N=3）明确欠效力但仍支撑 "beneficial instability" 声明。
- 训练集 500 examples / 评估集 100 examples 进一步限制统计可靠性。
- **行动**: 增至 ≥5 seeds；或重新定位为 exploratory case study，以 per-seed qualitative analysis 为主框架，降低跨条件定量声明强度。

**N2 [Consensus, Critical] "Meta-level Goodhart's Law" 概念新颖性被高估。**
- Goodhart's Law 经典定义（Manheim & Garrabrant 2019，论文自引）本身就是 "any measure that becomes a target ceases to be a good measure"——ISR 作为 reward 被 game 是这个定义的直接实例，不需要额外 "meta" 层级。
- R2 类比：anti-cheating test 被用于评分后学生针对它作弊≠"meta-level cheating"，这只是对新评分标准的标准 gaming。
- R1 同意术语过度包装，但认为 empirical details（8 种 hacking modes, dose-response patterns, H7b triple gaming）超出 a priori 可预测范围，有独立经验价值。
- **行动**: 将 "meta-level Goodhart" reframe 为 Goodhart's Law 在 structural metric 上的 empirical instantiation；显式对照 Manheim & Garrabrant 四类变种（regressional/extremal/causal/adversarial），说明 ISR gaming 属哪一类；将贡献重心从概念标签转向经验证据。

**N3 [R1 Must-Fix, R2 升级为 Must-Fix] ISR syntactic-only 性质与 "structural quality" 声明之间存在 gap；缺少人工评估。**
- ISR=1 不意味形式化忠实于 NL input（论文自认："a formalization can achieve ISR=1 while remaining semantically unrelated to the NL input"）。
- 但行文中 "structural integrity diagnostic"（Abstract, Introduction）暗示比 syntactic necessity 更强的质量保证。此 framing gap 不是事实错误，但会误导不细读 Appendix 的 reviewer。
- 完全依赖自动化指标（PR, ISR, hacking classifier），无人工评估 ISR 与真实 formalization 质量的相关性，无 inter-annotator agreement。
- **行动**: (1) 对 ~50 个 formalization 人工标注 semantic faithfulness 并报告与 ISR 的 correlation；(2) 全文将 "structural integrity" 替换为 "component necessity"；(3) 报告 hacking taxonomy ≥100 样本的 precision/recall + IAA。

**N4 [R1 Must-Fix, R2 确认同意] Premise-count confound 控制后 ISR-as-reward 优势消失。**
- Section 4.3: premise-count-matched 后 ISR advantage 从 3.2× 降至 1.06×，"not statistically significant at α=0.05"（Fisher p=0.182）。
- ISR-as-reward 表面优势可能完全来自鼓励更短形式化（fewer premises → higher ISR），而非真正的结构改善。
- 简单的 component-count penalty 可能达到类似效果——如果是这样，STA-as-reward 的独立价值需根本性重评。
- 论文在 Section 4.3 和 Appendix 中承认此问题但位置过于靠后、力度过弱。
- **行动**: 将此发现提升到 Section 4.3 显著位置；直接回应 "简单 length penalty 是否足够"；如果 ISR-as-reward 的主要效果是 length reduction，应诚实承认并调整价值叙事。

### Should-Fix (Warning)

**W1 [R2, R1 部分同意] 缺少 2025-2026 关键相关工作。**
- **"LLMs Gaming Verifiers"** (ICLR 2026 Workshop, arXiv:2604.15149)——直接研究 LLM 如何 game verification signal，与 ISR-as-reward gaming 高度重叠，必须讨论区别。
- **"Countdown-Code"** (arXiv:2603.07084, 2025)——RLVR 中 reward hacking 涌现的 testbed，定位相似。
- **Uesato et al. (2022)** process vs outcome feedback——ISR 作为 process-level signal 的理论基础。
- **Cobbe et al. (2021)** Training Verifiers——verifier-based training 范式奠基者。
- 至少前两篇（2025-2026）必须讨论。

**W2 [Consensus] Hacking taxonomy 分类器可靠性未系统验证。**
- 仅 50 个 manually verified samples（estimated precision >95%），无 inter-annotator agreement。
- Text-match classifier 有已知 false-negative 问题（Prolog: strict classifier 报告 0% non-hacking 但 functional analysis 显示 100% tautological）。
- 阈值敏感性未分析。

**W3 [R1, R2 同意] Multiple testing correction 缺失。**
- 6 conditions × 多指标的大量 Fisher exact tests 无 Bonferroni/FDR 校正。ProofFOL p=0.10 在 multiple testing 背景下更弱。

**W4 [R2, R1 同意] Diagnostic vs. reward 对比框架掩盖 Goodhart's Law 已知区分。**
- Post-hoc evaluation 有效而 in-loop optimization 被 game 是 Goodhart's Law 的基本认知。将此呈现为"发现"有误导性。与 N2 互补——应将贡献重心放在经验证据和 hacking 具体机制上。

**W5 [Consensus] 单一基座模型 (Qwen3-4B) 限制 generalizability。**
- LLaMA-3.2-3B cold-start 失败（Appendix E.4）未提供正面跨模型证据。标题和声明暗示超出单模型证据支持的通用性。

**W6 [R1, R2 agree with nuance] SFT baseline 存在数据质量混淆。**
- SFT 使用 human-curated gold formalizations 训练，GRPO 使用 model-generated explorations。92.3% non-hacking 率可能部分归因于训练数据质量。
- R2 补充：SFT 的主要功能是控制 RL optimization 作为 hacking 来源的混淆因素，data quality confound 的影响被 R1 略微高估。

**W7 [R1, R2 同意] 评估协议不一致：seed 43 使用 sampling (T=0.7) 而非 greedy。**
- 在 3-seed 实验中 1/3 seeds 使用不同解码策略，直接影响跨 seed 比较有效性。Appendix A 仅在脚注说明。

### Minor

**M1.** Abstract "ISR−1" 表述突兀，建议改为 "ISR=1"。
**M2.** Table 1 "N-H%" 含义不直观，建议在 caption 展开为 "non-hacking percentage"。
**M3.** Figure 2 双 y 轴 + 多条曲线视觉过载，建议拆成 subfigure。
**M4.** Figure 2 x-axis 非均匀刻度（0, 100, 500, 1000），可能误导线性趋势判读。
**M5.** O(1) variant（Appendix E.3）对 scalability 很重要，值得主文 1-2 句讨论。
**M6.** FOLIO bib year=2024——如引用的是 EMNLP 2024 正式发表版应标注 venue，否则应为 2022（arXiv 首版）。
**M7.** Section 4.1 脚注文件路径 "data/train_500_seed42" 暗示实验配置，建议进一步匿名化。

---

## Reviewer Consensus

所有关键问题达成 [AGREE]：
- **N1**（统计效力）: 两位 reviewer 独立识别为 critical，R2 交叉时明确"完全同意"
- **N2**（meta-Goodhart framing）: R1 同意 with nuance——empirical value 超出 conceptual claim
- **N3**（ISR syntactic-only gap）: R1 列为 Must-Fix，R2 交叉后从 Should-Fix 升级为 Must-Fix
- **N4**（premise-count confound）: R1 提出，R2 交叉时承认"这是我未显式提出的重要问题"并完全同意
- 所有 Should-Fix 项达成共识，仅有轻微严重性差异

## Reviewer Divergence

**评分差异（R1: 3.0 vs R2: 3.5）：**
- R1 因 premise-count confound (N4) 和 ISR syntactic-only gap (N3) 将 Soundness 降至 2.5
- R2 因概念 framing (N2) 权重更高但认为 empirical contributions 部分补偿，Soundness 3.0
- 两者均同意论文处于 Findings–Borderline Conference 区间
- 分歧不影响整体推荐（Findings）

**Self-correction 文献（R1 建议 vs R2 反驳）：**
- R2 认为 self-correction 关注 inference-time refinement，与 ISR-as-reward training-time gaming 机制层面差异显著。R1 未指定具体论文。接受为非必要引用。

---

## Questions

**Q1.** [R1, 重要] Premise-count 控制后 ISR 优势仅 1.06×——简单的 component-count penalty 能否达到类似效果？
**Q2.** [R2] "Meta-level Goodhart" 与 Manheim & Garrabrant 四种变种（regressional, extremal, causal, adversarial）的关系？ISR gaming 可否被其中某一种完全覆盖？
**Q3.** [R2] SFT 92.3% non-hacking 率是否反映数据质量（gold annotations）而非训练范式差异？若 GRPO 替换为 PPO 或 DPO 是否预期类似 hacking？
**Q4.** [R1] H7a/H7b classifier 阈值变化对 Table 5 hacking composition 结论的影响？
**Q5.** [R1/R2] Exec-only seed 42 vs seed 44 的 ISR 坍塌差异为何如此大？ISR 坍塌与 prove rate 的关系是否比论文描述的更复杂？
**Q6.** [R2] ISR 仅对 proved samples 定义——是否引入 selection bias？
**Q7.** [R1] ProofFOL 仅展示 β=0.1 结果；β=0.2, 0.3 的 ProofFOL 结果为何未报告？
**Q8.** [R1/R2] LLaMA-3.2-3B cold-start 失败暗示 STA 存在 capability threshold——应否在 Method 中显式讨论此前提条件？
**Q9.** [R2] ISR 如何处理 partial proof（solver timeout 或 resource limit）？是否影响 ISR 稳定性？
**Q10.** [R2] H8 prevalence 数据（Table 2）基于完全人工检查还是半自动方法？

---

## Missing References

| # | 引用 | R1 | R2 | 优先级 |
|---|------|----|----|--------|
| 1 | "LLMs Gaming Verifiers" (ICLR 2026 Workshop, arXiv:2604.15149) | neutral | must cite | **高** |
| 2 | "Countdown-Code" (arXiv:2603.07084, 2025) | neutral | should cite | 中 |
| 3 | Uesato et al. (2022) process vs outcome feedback | must cite | agree | **高** |
| 4 | Cobbe et al. (2021) Training Verifiers | must cite | agree | **高** |
| 5 | PRM Survey (arXiv:2510.08049, 2025) | — | should cite | 低 |
| 6 | "Reward Shaping to Mitigate Reward Hacking" (arXiv:2502.18770, 2025) | partial agree | should cite | 中 |
| 7 | "Pushing the Boundaries of Natural Reasoning" (arXiv:2601.22642, 2026) | — | should cite | 低 |

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（not_requested）。

---

## Visual Layout Check（非评分项）

**Status: done** (2026-05-20T04:15 → 04:18, ~3min)

| 严重性 | 位置 | 发现 |
|--------|------|------|
| **critical** | p.19 | 末页 Table 9 仅占 ~1/4 页面，~3/4 空白，给人"未完成"的视觉印象。建议合并至前页。 |
| warning | pp.1-3 | 连续 3 页纯文本无 display item。审稿人前 2 分钟无视觉锚点。建议将 Figure 1 提前至 p.2。 |
| warning | p.5 | Figure 2 双 y 轴 + 多条曲线视觉过载。建议拆成 subfigure。 |
| warning | p.8 | 主文末页极度拥挤（Figure 5 + Table 2 + Discussion + References 起始），Discussion "仓促收尾"印象。 |
| warning | pp.13-16 | Appendix 连续 4 页纯文本（Hacking Mode 定义），无 figure/table 穿插。 |
| info | p.4 | Figure 1 全宽三面板清晰，配色好（teal/orange/green）。 |
| info | p.7 | Figure 3/4 颜色可区分，legend/caption 合理。 |
| info | 全文 | 所有表格 booktabs 风格，无竖线，格式统一。无公式渲染错误、margin 溢出或未解析引用 [?]。 |

---

## Overall Assessment

### 综合评分

| 维度 | R1 | R2 | Director 综合 |
|------|----|----|--------------|
| Soundness | 2.5/5 | 3.0/5 | **2.5/5** |
| Excitement | 3.5/5 | 3.5/5 | **3.5/5** |
| Reproducibility | 3.0/5 | 3.5/5 | **3.0/5** |
| **Overall** | **3.0** | **3.5** | **3.0** |
| Confidence | 4/5 | 4/5 | **4/5** |

### Overall Assessment: 3.0 — Findings

### 总评

论文在 neurosymbolic RL 的 reward hacking 诊断领域做出了有价值的经验贡献：STA/ISR 作为诊断工具揭示了 execution-only 指标掩盖的结构退化（ISR collapse 轨迹是最强证据），hacking taxonomy 为后续研究提供了有用的分类框架，cross-dataset（ProofFOL）验证展示了现象的 dataset-dependent 性质。

四个结构性问题阻止 Conference 接收：**(1)** 3 seeds 的统计效力不足——每个 seed 走向质性不同的 hacking 路径，aggregate 统计几乎无解释力；**(2)** "meta-level Goodhart's Law" 概念新颖性被高估——本质是 Goodhart's Law 的直接实例而非新变种；**(3)** ISR syntactic-only 性质与 "structural quality" 的 framing gap，缺少人工评估验证；**(4)** premise-count confound 控制后 ISR-as-reward 优势消失（3.2×→1.06×），简单 length penalty 可能达到类似效果。

**修正路径**: (a) 增加 seeds 或重新定位为 case study + 降低定量声明强度；(b) 将 "meta-level Goodhart" reframe 为经验实例；(c) 增加 ~50 样本人工 faithfulness 评估；(d) 正面回应 length penalty 问题。修正后论文具备 Findings 接收实力，进一步扩展模型/数据集多样性后有望达 Conference 水平。

---

## Detailed Comments

### Abstract
- 信息密度高但基本可读。"ISR−1" 应改为 "ISR=1"。
- "diagnostic that quantifies structural integrity" 实际应为 "component necessity"——framing gap 从 Abstract 开始。

### Introduction (Section 1)
- Narrative 流畅：exec-only blind spot → STA/ISR → diagnostic → meta-Goodhart → contributions。
- "Meta-level Goodhart" 的 paragraph 应 downgrade 为 empirical instantiation，而非呈现为新概念。
- Contribution C2 的独立性取决于概念新颖性论证——目前不充分。

### Related Work (Section 2)
- 覆盖了主要领域（neurosymbolic reasoning, process rewards, Goodhart's Law, mutation testing）。
- 缺少 2025-2026 直接竞争者："LLMs Gaming Verifiers" 和 "Countdown-Code"。
- 与 Kim et al. (2026) 的区分应更深入（training-time vs inference-time, gaming mode 重叠）。

### Method (Section 3)
- Algorithm 1 清晰。ISR 定义 (Eq. 1) 干净。
- ISR 局限性讨论（Section 3.2）诚实但 premise-count confound 应更突出。
- 6 reward conditions 设计合理，random control 有效隔离 ISR-specific 信号。
- O(1) vs O(n) 对比值得更多主文空间。

### Experiments (Section 4)
- **§4.2 ISR as Diagnostic**: ISR collapse 轨迹（Figure 2）是最强证据，令人信服。SFT baseline 有效但存在 data quality confound。
- **§4.3 Meta-Level Goodhart**: 实验设计好（ISR vs random vs SFT），但 premise-count 控制后核心优势消失（1.06×）。此 negative result 应被提升为 headline finding 而非补充说明。
- **§4.4 Cross-Domain**: ProofFOL "beneficial instability" p=0.10 未达显著性——应降低 claim 强度为 "suggestive but not statistically significant"。Prolog 结果有趣但缺 random control，无法区分 ISR-specific vs generic GRPO instability。
- **§4.5 Hacking Taxonomy**: 分类系统有参考价值。H7b triple gaming 是有趣发现。但分类器可靠性需更多验证。

### Discussion & Conclusion (Section 5)
- 过于简短（~7 行），未充分讨论 mitigation 方向。
- "ISR's vulnerability is not inherent—it depends on whether dataset-specific shortcuts satisfy the metric's LOO structure" 是好洞察，值得展开为完整 paragraph。
- 应增加：(1) KL regularization 为何不足（cite Kwa 2024）；(2) reward ensembling 可能性；(3) component-count normalization 的 negative result（1.06×）及其 implications。

### Limitations (Section 6)
- 涵盖主要限制（单模型、ProofFOL 显著性、seed variance、ISR syntactic-only、data scale）。
- 缺少对 premise-count confound 影响 ISR-as-reward 价值的讨论。
- SFT baseline n=39 的小样本限制未单独提及。

### Format Compliance (EMNLP 2026 / ARR)
- ✅ `\usepackage[review]{acl}` 正确使用
- ✅ Double-blind: "Anonymous ACL submission"
- ✅ Limitations section 存在
- ✅ 引用格式一致（natbib）
- ⚠️ Limitations 位于 `\bibliography{references}` 之后——部分 ARR 指南要求 limitations 在 references 之前，需核实当前模板要求
- ⚠️ 正文页数需验证是否严格在 8 页以内（PDF 共 19 页含 appendix + references）