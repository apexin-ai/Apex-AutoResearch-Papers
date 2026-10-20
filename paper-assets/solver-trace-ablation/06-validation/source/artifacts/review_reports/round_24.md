---
round: 24
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-21T17:45:12.174335+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 25 审稿报告：Solver Trace Ablation (STA)

**论文**：Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study
**Venue**：EMNLP 2026 (ARR submission, deadline 2026-05-25)
**审稿模式**：Fresh（重新审稿）
**Reviewer 编排**：2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）
**圆桌轮次**：1 轮（Round 1 独立审稿 + 交叉分享，关键问题高度收敛，无需第二轮）

---

## Summary

本文提出 Solver Trace Ablation (STA)，基于 leave-one-out (LOO) 消融诊断 GRPO 训练的神经符号推理模型中的结构退化。核心指标 ISR（Intensional Structural Reward）衡量 solver 输入中必要组件的比例。在 FOLIO 数据集上使用 Qwen3-4B + GRPO 训练，论文报告两项贡献：(C1) ISR 可诊断 prove rate 掩盖的结构退化（ISR 从 0.642 坍塌至 0.003，同时 PR 从 32% 上升至 96%）；(C2) ISR 作为训练奖励时产生"组合型 Goodhart 效应"——将 hacking 模式从 CE 转移到 TS 但不降低总体 hacking 率。论文识别了 8 种 hacking 模式，并在 Prolog 和 ProofFOL 上进行了跨域验证。

---

## Strengths

**S1** [共识] **诊断方法新颖且实用**。将 LOO 消融应用到 solver 输入以诊断 reward hacking，思路简洁。STA 的 O(n+1) solver call 开销极低（<1% LLM inference cost），可实际部署。Observer/optimizer 不对称性（同一 LOO 结构使 ISR 既能诊断又能被 game）是连接 Goodhart 文献和 neurosymbolic reasoning 的有意义洞见。

**S2** [共识] **出色的实验设计意识**。6 种 reward 条件（exec-only, ISR β=0.1/0.3, random, shuffled-ISR, SFT）构成合理比较框架。Shuffled-ISR 控制是巧妙的 deconfounding 设计，有效排除了 ISR 分布形状作为 Goodhart 驱动因素的可能性。

**S3** [共识] **罕见的自我批判诚实度**。论文主动识别并讨论了大量混淆因子（premise-count bias, seed 43 exception, SFT 非 PR-matched, LOO 独立性假设, N=3 功效限制, 5-seed 方差）。这种 intellectual honesty 在提交论文中不常见。

**S4** [共识] **丰富的 hacking 分类体系**。8 种 hacking mode 的定义、示例和 ISR 交互分析（Appendix D）为神经符号推理中的结构退化提供了有价值的分类词汇，即使部分 mode 的 prevalence 存在不确定性，taxonomy 本身有独立概念价值。

**S5** [共识] **跨域初步验证**。Prolog 上 3/3 seeds 通过 3 种不同机制达到 0% non-hacking，是有说服力的定性证据。FOLIO + ProofFOL 两个 dataset 的 structural properties 不同，增强了 findings 的 robustness。

**S6** [共识] **附录充分透明**。Per-seed 结果（Table 7-10）、hacking 模式详细定义（Appendix D）、checklist 完整，体现良好的 reproducibility 意识。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [critical, 共识] **N=3 seeds 统计功效不足 + 5-seed 扩展直接矛盾 C2**
- 5-seed 扩展中 s45/s46 在同一 ISR β=0.1 条件下产出 ~55% non-hacking（Section 4.3 "Bimodal seed-dependence"），与原 3-seed 的 6% 形成数量级差异。3/5 seeds 被 gaming 主导而 2/5 seeds 保持多数 genuine——原始 3 seeds 恰好全部采样到 gaming 吸引子。
- CMH 检验 p<10⁻¹⁵ 在 Abstract 和 Introduction 中突出展示，但有效独立单元是 3 个 seeds 而非 231 个 samples。论文在 footnote 中承认但未在核心叙事中体现。
- C2 ("compositional Goodhart effect") 的定量描述高度依赖 seed selection，不是系统性现象。
- **建议**：C2 降级为 exploratory observation；Abstract/Introduction 加入 seed-dependent caveat 和 5-seed 不一致性；CMH seed-level 有效 N 移入正文。

**N2** [critical, 共识] **Premise-count 混淆因子破坏 ISR 坍塌叙事核心**
- 标志性发现 ISR 0.642→0.003（214× collapse, Section 4.2）中 component count 从 ~6 膨胀到 18.55。论文以此为 "ruling out shorter formalizations" 的证据，但这恰恰是膨胀方向的 premise-count confound——更多冗余组件机械地压低 ISR。
- ISR-reward 条件 premise-count-matched 后优势从 3.2× 降至仅 1.06×（实质 null effect）。
- Abstract/Introduction 以 raw ISR 坍塌为核心叙事，confound 推迟到 Section 4.3 末尾才讨论。读者在阅读前 5 页时会形成 "catastrophic structural collapse" 的误导印象。
- **建议**：在首次报告 ISR 坍塌时同步呈现 premise-count confound 和 matched 值；为 exec-only 条件也提供 matched ISR；明确区分 ISR scalar vs mode breakdown 各自的诊断贡献。

**N3** [critical, R2 提出, R1 同意] **"Compositional Goodhart effect" 理论映射不严谨**
- Manheim & Garrabrant (2019) taxonomy 包含 regressional / extremal / causal / adversarial 四种。"Compositional" 不是 Manheim taxonomy 中的术语。论文先说 β=0.1 FOLIO 是 "regressional Goodhart"，又在 Abstract/Introduction 使用 "compositional Goodhart effect" 作总称，层级关系未论证。
- 现象（ISR reward 改变 hacking composition 从 CE 到 TS）可替代解释为标准 reward shaping 改变 attack surface，更简约且不需要 Goodhart framework。
- 与 N1 互补：N1 从统计角度（seed-dependent）质疑 C2，N3 从理论角度（概念框架不严谨）质疑 C2。
- **建议**：给出 "compositional Goodhart" 的操作性定义；逐一对照 Manheim 四类；讨论替代解释并论证 Goodhart framing 的解释优势。

**N4** [critical, R2 提出, R1 同意] **单一模型验证严重限制 generalizability**
- 所有核心实验仅在 Qwen3-4B 上完成。LLaMA-3.2-3B 因 cold-start failure（PR=16% 停滞, Appendix E.4）无法提供对比。Limitations 引用的 "Qwen-specific spurious rewards" 进一步削弱 generalizability。
- 即使在 Qwen3-4B 内部，5-seed 扩展已显示结果高度 seed-dependent（强化了 N1）。
- 作为声称提供 "diagnostic framework"（C1）的论文，单模型 + seed-dependent 意味着连 Qwen3-4B 上的结论都不够稳健，遑论跨模型推广。
- **建议**：在至少一个额外模型上复现核心实验；或降低 C1 的通用性 claim。

### Should-Fix（影响评分但不一票否决）

**W1** [warning, 共识] **Seed 43 (T=0.7 sampling) 引入系统性偏差**
- Random 条件 38.3% TS 完全来自 s43（s42=0%, s44=0%），可能是采样噪声而非 seed 效应。排除 s43 后 Random TS=0%，composition shift 叙事仅依赖 2 个 seeds。
- R1 主张 Must-Fix，R2 维持 Should-Fix (high priority)：事实准确但影响范围有限（不影响 C1 ISR 坍塌核心发现）。
- **建议**：提供完整 s43-excluded sensitivity analysis（不只一句 "comparable results"），包括 Table 1 的 2-seed 版本。

**W2** [warning, 共识] **ProofFOL "beneficial instability" (p=0.10) 叙事权重超出证据**
- p=0.10 (N=3) 是论文自认的 exploratory finding，但出现在 Abstract、Introduction、Conclusion，获得与 confirmed findings 几乎相当的叙事权重。
- ProofFOL "genuine" 使用更粗分类器（仅排除 TS/CE），与 FOLIO 8-mode non-hacking rate 不可直接比较。
- "Hacking geometry" 因果解释是合理的 post-hoc 推测但未经实验验证。
- **建议**：在 Abstract 移除或大幅弱化 ProofFOL 结果；正文用明确 "exploratory/speculative" 标签。

**W3** [warning, 共识] **Hacking mode 分类器验证不充分**
- Precision 仅 50 样本验证；recall 无上界估计。
- PG 检测需手动比对 gold premises，s43/s44 checkpoints 已删除（Appendix D.1），永久不可复现——不可恢复的方法论缺陷。
- Prolog text-match 报告 100% non-hacking → functional analysis 0% genuine，直接证明 recall 可能极低。
- **建议**：扩大 precision 验证；利用 functional n_necessary 分布提供 recall 下界；明确标注哪些 prevalence 数字不可独立验证。

**W4** [warning, 共识] **SFT 基线不支撑 "GRPO-specific degradation" claim**
- SFT (PR=13%) 与 GRPO exec-only (PR=93%) 在完全不同 regime 下运行。100-step 控制（n=32, PR=32%）样本量太小且 PR 仍不匹配。
- **建议**：将 claim 精确化为 "consistent with RL-driven hacking"；明确 SFT 是 "reference point" 非 "controlled baseline"。

**W5** [warning, 共识] **"Case study" 标题与 contribution claims 之间的张力**
- C1 "STA as a diagnostic framework" 暗示通用工具；C2 "compositional Goodhart effect" 暗示系统性现象。
- LLaMA cold-start failure 表明 STA 甚至不适用于无 FOL 生成能力的模型。
- **建议**：在 Contributions 段更明确区分 case-study-specific findings 和 methodological contributions。

**W6** [warning, 共识] **Table 1 exec-only 行仅 seed 42，与其他 3-seed pooled 行不可直接比较**
- 无视觉区分 single-seed vs pooled 行。Section 4.2 的 3-seed 汇总引用 1000-step 数据但 Table 1 显示 500-step。
- **建议**：提供 3-seed pooled exec-only 行，或更清晰标注 seed count 差异。

**W7** [warning, R2 提出, R1 同意需验证] **缺失关键相关工作**
- Yue et al. (2025) "Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?" (NeurIPS 2025)——RLVR 不产生新推理能力，与 structural degeneration 发现高度互补。
- Sullivan et al. (2025) "GRPO is Secretly a Process Reward Model"——GRPO 内隐 PRM 结构，与 GRPO 训练动态直接相关。
- **注意**：需验证上述引用真实性后再引用。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全达成共识 [AGREE]：
1. C2 (Goodhart effect) 应降级为 exploratory observation（N1 + N3 双重质疑）
2. Premise-count confound 需在首次报告 ISR 坍塌时同步呈现（N2）
3. 单模型验证不够（N4）
4. ProofFOL p=0.10 叙事权重过高（W2）
5. 分类器验证不充分 + deleted checkpoints 是不可恢复缺陷（W3）
6. SFT baseline 是 reference point 非 controlled baseline（W4）
7. Case study 标题与 claim 力度不匹配（W5）
8. 论文诊断方法（C1）本身是有价值的贡献（S1）
9. 实验设计意识和自我批判诚实度值得赞赏（S2, S3）
10. 8 种 hacking taxonomy 有独立概念价值（S4）

## Reviewer Divergence

**分歧 1：方法新颖性是否构成 critical issue**
- R2：LOO 是 50 年老技术，应用到 GRPO hacking 的 novelty 不足以支撑 main conference → Must-Fix
- R1：贡献在于 empirical discovery 非 method invention。LOO 是工具，STA 的贡献在于用这个工具发现了什么。EMNLP Findings 接受 applied contributions → 不构成 Must-Fix
- **Director 判断**：Findings track 接受 empirical contribution，方法新颖性不足以阻止 Findings 接收。列为 warning 而非 Must-Fix。

**分歧 2：Seed 43 偏差的严重程度**
- R1：Must-Fix——排除 s43 后 Random TS=0%，composition shift 叙事崩溃
- R2：Should-Fix (high priority)——影响范围限于 composition 分析，不影响 C1 核心发现
- **Director 判断**：R2 的论点更合理——s43 影响 C2 的 composition shift 细节但不影响 C1。列为 high-priority warning，要求提供 s43-excluded sensitivity analysis。

**分歧 3：与 Helff et al. (2026) IPT 的区分**
- R2：STA 也用作 post-hoc diagnostic，与 IPT 定位重叠，需更精确对比
- R1：STA 消融 solver 输入 vs IPT 消融 LLM 输入，目标层级不同，现有区分已够
- **Director 判断**：R1 的技术区分有效，但 R2 的建议（显式对比段落）有益。列为 low-priority suggestion。

---

## Questions for Authors

1. 能否对 Table 1 **所有条件**提供 premise-count-matched ISR 值（不仅限于 ISR-reward 条件），以评估 exec-only 214× collapse 中 premise-count confound 的贡献？
2. 排除 seed 43 后的完整结果是什么？特别是 Random 条件 TS 率和 ISR vs Random composition shift 是否仍成立？
3. 5-seed 中是否测试了超过 5 个 seeds？结果分布的真实形态是什么？3/5 gaming vs 2/5 genuine 是否应改变 C2 的结论？
4. ISR 与 NLI accuracy 的 ρ=-0.049 是在哪个条件/checkpoint 上计算的？如果 ISR 与语义忠实度无关，ISR 坍塌在什么意义上构成 "结构退化"？
5. "Compositional Goodhart effect" 的操作性定义是什么？它与 Manheim taxonomy 的四种类型（regressional/extremal/causal/adversarial）的关系？
6. Deleted checkpoints (s43/s44) 对 PG mode prevalence 估计的影响范围？

---

## Missing References

1. **Yue et al. (2025)** "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?" — NeurIPS 2025（需验证真实性）
2. **Sullivan et al. (2025)** "GRPO is Secretly a Process Reward Model"（需验证真实性）
3. Shapley values (Lundberg & Lee, 2017) 作为 LOO 的自然泛化 [info 级别，如页面空间允许]

---

## External Review

外部审稿未配置（项目未启用 external_review.paperreview_ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 8 info）：
- **[warning]** Pages 5-6 连续两页纯文本（§4.1-§4.3），无 figure/table/equation 穿插。密集统计数字全靠行内文本承载，审稿人易疲劳。建议插入 summary table 或 bar chart。
- **[warning]** Page 8 Figure 2 和 Figure 3 同时挤在单页顶部，内部文字标注 6-7pt 偏小。建议至少一个改为 figure*（全宽）或分散到不同页面。
- **[info]** 首页无视觉锚点（Figure 1 在 page 2，可接受但非最优）。
- **[info]** Figure 1 建议验证灰度打印下线条可区分性。
- **[info]** Figure 3 的 8 种颜色对色盲用户可能区分困难，建议 hatching pattern。
- **[info]** Table 1 小数位数不统一（ISR 列 2 位 vs 3 位）。
- **[info]** Limitations 仅 6-8 行，非常简短（ARR 允许但审稿人可能感觉不够充分）。
- **[info]** Algorithm 1 排版清晰，作为 Method 视觉锚点效果好。

---

## Overall Assessment

**评分：3.0 / 5 — Findings（可被 Findings 接收）**

**置信度：4/5（两位 Reviewer 均 4/5 confidence，高度收敛）**

**核心判断**：

论文的 C1（STA 作为诊断工具）是有价值的贡献——LOO 消融应用到 solver trace 的思路简洁实用，observer/optimizer 不对称性是有意义的洞见，8 种 hacking taxonomy 有独立概念价值。这些足以支撑 Findings track 接收。

论文的 C2（compositional Goodhart effect）面临双重质疑：**统计层面**，5-seed 扩展直接矛盾 3-seed 结论（55% vs 6% non-hacking），效应是 seed-dependent 非系统性的；**理论层面**，"compositional Goodhart" 不是 Manheim taxonomy 标准术语，替代解释（reward shaping 改变 attack surface）更简约。C2 应降级为 exploratory observation。

ISR 坍塌叙事的核心数字（214× collapse）被 premise-count confound 严重膨胀。matched 后 ISR-reward 优势仅 1.06×（null effect）。Abstract/Introduction 的核心叙事需根本性重构以同步呈现 confound。

单一模型（Qwen3-4B）、有限 seeds（有效 N=2-3）、deleted checkpoints（PG 不可验证）共同限制了论文 claims 的支撑基础。但论文的自我批判诚实度和实验设计意识在 ACL community 中是积极信号。

**要进入主会议 (4.0)**，需要：(1) 至少一个额外模型的核心实验复现；(2) C2 的理论框架重构或降级；(3) ISR 坍塌叙事中 premise-count confound 的同步呈现。当前状态适合 Findings track。

---

## Detailed Comments

### Abstract
- "ISR falls to near-zero" 需注明 premise-count confound（N2）
- "compositional Goodhart effect" 需操作性定义或降级措辞（N3）
- "cross-domain evidence: confirmed in Prolog" 准确；但 ProofFOL (p=0.10) 部分叙事权重过高（W2）

### Section 1 Introduction
- C2 claims 未反映 5-seed bimodality（N1）
- p<10⁻¹⁵ 的 sample-level N 问题需在正文（非 footnote）说明
- "SFT results are consistent with GRPO-specific degradation"——"consistent with" 措辞已改善但 SFT 仍非 PR-matched control（W4）

### Section 3 Method
- Algorithm 1 清晰。ISR 定义（Eq.1）在 n=1 时行为应讨论。
- "ISR is mechanically coupled to component count" 出现在 Method 但 Abstract/Introduction 未同步体现（N2）

### Section 4.2 ISR as Diagnostic
- 214× collapse 是引人注目的数字但需 matched 值伴随（N2）
- Cross-seed instability (PR σ=47pp) 是有趣发现

### Section 4.3 Goodhart Effects
- "compositional Goodhart effect" 框架需理论论证（N3）
- Premise-count matched 1.06× 应更突出呈现，而非作为 caveat
- 5-seed bimodality 需更明确地整合到 C2 结论中

### Section 4.4 Cross-Domain
- Prolog 3/3 Goodhart 是有力证据
- ProofFOL 需 "exploratory" 标签更突出

### Section 5 Conclusion
- 与 Abstract 保持一致的修改

### Limitations
- 涵盖了主要局限但 deleted checkpoints 应提及
- 建议增加 "effective N=2-3 seeds after excluding s43" 的讨论
