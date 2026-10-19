---
round: 2
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T11:47:30.141443+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards

**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewers**: R1（方法严谨性）、R2（新颖性与完整性）
**审稿轮次**: Round 2 (fresh)
**日期**: 2026-05-22

---

## Summary

本文研究表征工程提取的对比谄媚方向（d_syc）能否作为 GRPO 的标量 reward 信号来校准 LLM 的 sycophancy 行为。在 Qwen3-8B 上提取 d_syc（5-fold CV AUROC 0.827）并在 Llama-3-8B 上交叉验证（AUROC 0.779）后，测试了三种 reward 公式（cosine projection、binary probe、continuous probe）共六种 GRPO 配置，全部失败。R3-only GRPO（仅用 NLI 行为 reward）也失败（26 个 checkpoint 仅 4 个超过 vanilla，15.4%），而 ACT（dense per-token SFT）以 SyconScore 0.301 成功（seed 1: 16/16 checkpoints 超过 vanilla）。论文提出三个 contributions：(C1) 所有 GRPO 公式失败，(C2) probe reward 产生 stubbornness trap（behavioral death 先于 distributional collapse），(C3) 标量 per-completion reward 结构性不足。

---

## Strengths

**S1. 问题选取填补重要空白 [R1, R2 一致]**
首个系统否证 "representation discriminability → RL reward utility" 隐含假设的工作。对 representation engineering + RL 社区有直接理论意义。

**S2. 诊断链设计严谨且有教学价值 [R1, R2 一致]**
§4 的 cosine failure chain（F1a→F1b→F1c→F1d）逐步排除假说，每一步解决前一步的 failure mode 但暴露更深层问题。这种递进式消融是优秀的科学方法论。

**S3. Probe reward trap (C2) 是真正新颖的发现 [R1, R2 一致]**
Behavioral death（ToF=0 at step 500）先于 distributional collapse（entropy 0.70 持续到 step ~1840），reward 始终保持 +0.72。1,300-step 时间差意味着标准 entropy-based early stopping 完全错过行为退化。对 RLHF 安全监控实践有直接指导意义。

**S4. Cross-model direction validation [R1, R2 一致]**
在 Llama-3-8B 上独立复现 d_syc extraction，evidence-strength gradient 定性模式一致（weak→medium→strong AUROC 单调递增），表明 d_syc 不是模型特异的。

**S5. Papadatos & Freedman (2024) 对比定位精准 [R2]**
§6 的 "inference-time vs training-time × dense vs sparse supervision" 双维度分析框架，清晰地统一解释了本文 negative result 与已有 positive result。

**S6. Limitations 写作诚实 [R1]**
主动承认单模型训练、ACT seed 2 不完整、n=2 seeds、supervision granularity confound。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1 [critical] C3 "supervision density hypothesis" 因果声称超出证据范围**
[R1-N1, R2-N1, R2-N2 — 两位 Reviewer 完全一致，交叉确认]

ACT 和 GRPO 至少在 4 个维度同时不同：(a) per-token vs per-completion 梯度粒度，(b) SFT（交叉熵）vs RL（GRPO）目标函数，(c) labeled valid/invalid pairs vs online exploration with reward，(d) L2 activation consistency loss。论文将 ACT 的成功归因于 "supervision density"（§6: "The critical difference is supervision granularity"），但实验设计无法隔离这一因素。

C3 声称 "A single scalar reward per completion...cannot teach the model which belief changes are warranted"，并从 GRPO + 4 种奖励变体推广到整个 per-completion RL 方法族（§6: "we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars"）。PPO 有 value function 和 clipping 机制，RLOO 有不同的 baseline 估计，这些都可能改变 reward signal 的利用方式。

关键反事实：如果 ACT 的优势来自 labeled supervision 而非 per-token granularity，supervision density hypothesis 就不成立。缺失的关键控制实验：per-completion SFT、token-level RL reward（process reward model）、labeled-pair GRPO。

**建议**：(1) 将 C3 从因果声称降级为观察性发现；(2) "supervision density is THE critical difference" → "ONE plausible contributing factor among several confounded differences"；(3) 在正文（非仅 Limitations）完整列出 ACT vs GRPO 所有差异维度；(4) §6 对 PPO/RLOO 泛化改为 hypothesis。

**MF-2 [critical] 单模型训练，标题和正文做一般性声称**
[R1-N2, R2 同意]

所有 RL/SFT 训练仅在 Qwen3-8B 上进行。标题 "Why Sycophancy Directions Fail as Scalar RL Rewards" 和 §1 "structurally insufficient" 是一般性陈述，但仅有单模型证据。两个模型的 d_syc best layer 不同（L19 vs L16）、AUROC 不同（0.827 vs 0.779），模型间训练动态差异未被排除。

R2 补充：机制论证（d_syc 几何上无法区分 valid revision 和 capitulation）是模型无关的理论论证，可保留为假说，但经验性 claim 需限定范围。

**建议**：(1) 标题或 abstract 限定实验范围（如 "a case study on Qwen3-8B"）；(2) 在 Llama-3-8B 上至少复现一个关键训练实验（如 binary probe F2）；(3) "fail" → "failed in our experiments"，"structurally insufficient" → "insufficient in the tested configuration"。

**MF-3 [critical] 统计效力不足：n=2 seeds，ACT seed 2 仅 3/16 checkpoints**
[R1-N3, R2 同意但 severity 稍低]

- n=2 seeds 的 cross-seed rank correlation（ρ≈0.33 after step 4000）缺乏统计意义
- ACT seed 2 仅 3/16 checkpoints，论文在实验未完成时提交
- "4/26 (15.4%) exceed vanilla vs 16/16 (100%)" 忽略 checkpoint 间时间序列自相关

R2 nuance：定性模式一致性（oscillation amplitude Δ≈0.069，identical crash depth 0.074）在 negative result 论文中有价值。C2 的 probe trap（ToF→0 at step 500）是单次实验即可确认的定性现象，不受 seed 数量限制。

**建议**：(1) 完成 ACT seed 2 全部 16 checkpoints 评估；(2) 增加至少 1 个额外 seed（≥3 total）；(3) 对 Table 4 关键对比报告 bootstrap CI；(4) 如计算资源不足，大幅软化比较性声称。

**MF-4 [critical] 正文超 8 页限制**
[视觉审查发现]

Sections 1-7 占满 pages 1-8，Section 8 (Conclusion) 从 page 9 顶部开始（约 1/4-1/3 列）。EMNLP 2026 / ARR 严格要求 long paper 正文不超过 8 页（Limitations 和 References 不计入），Conclusion 属于正文。**可能触发 desk rejection。**

**建议**：压缩正文或重新排版，确保 Conclusion 在 page 8 底部结束。

### Should-Fix（影响评分但不一票否决）

**SF-1 [warning] SMART (Beigi et al., 2025) 讨论不充分 [R2-W1, R1 同意]**
§7 仅一句话提及。Supervision density hypothesis 直接预测 SMART 的 per-step process reward 应表现介于 GRPO（per-completion）和 ACT（per-token）之间。未讨论 SMART 实际结果是否验证该预测，是理论完整性缺陷。

**SF-2 [warning] 超参搜索不充分：w1 仅 0.25/0.40 [R1-W3, R2 同意]**
"Diagnostic-driven iteration" 缺乏系统性。对 F2/F3（binary probe R1=0/1 与 w1 关系不大）影响有限，但对 F1 系列可能存在未探索的有效配置。

**SF-3 [warning] 80-84% truncation (max_completion_length=256) [R1-W1, R2 同意]**
不同 reward formulations 对截断的敏感度可能不同。"Response-level decisions manifest within 100-200 tokens" 是未验证的断言。建议至少一个 config 测试 max_completion_length=512。

**SF-4 [warning] Evidence strength 三级标注缺少 IAA [R1-W4, R2 同意]**
直接影响 §3 evidence-strength stratified AUROC（weak 0.675→medium 0.883→strong 0.929）的可信度。未报告标注者身份、人数和 inter-annotator agreement。

**SF-5 [warning] 可复现性信息严重不足 [R2-W5, R1 同意]**
GRPO 关键超参数（采样数/group size、KL penalty coefficient、learning rate、batch size）未披露。181 对比对的 GPT-4.1 prompt template 未提供。无代码/数据可用性声明。对 negative result 论文，可复现性尤其重要。

**SF-6 [warning] CRAFT 对比讨论可深化 [R2-W2, R1 部分同意]**
§7 已提供 CRAFT vs 本文的 geometric separability 框架，但可量化 CRAFT 的 representation gap 与本文 0.098 cosine gap 的差异。R1 认为对比已存在但深度不足。

**SF-7 [warning] "Latent-GRPO" 非原文命名 [R2-W4, R1 同意]**
Zhang et al. (2026) 原标题 "Silence the Judge"。应使用原文名称或首次引用时标注 "(hereafter Latent-GRPO)"。

**SF-8 [warning] 遗漏高度相关工作 [R2-W3, Director 已验证]**
Wu & Tang (2026) "When Reward Hacking Rebounds" (arXiv:2604.01476) 在 GRPO 中成功使用 representation-level concept directions 做 advantage modification。与本文 negative result 形成重要对比：representation directions 在 reward hacking detection 中成功进入 GRPO training loop，在 sycophancy 中失败。**已验证真实存在，必须引用。**

### Minor（不影响接收）

- Abstract 接近一整栏，建议压缩到 150-200 词 [R1, R2]
- Introduction 与后续章节大量数字重复，Introduction 应侧重 high-level narrative [R1, R2]
- Table 4 Cosine R1 显示 "collapse" 而非数值，应报告最后稳定 checkpoint 的 SyconScore [R2, R1]
- Figure 1 中 Llama-3-8B 仅显示 layers 16-31，完整层 profile 更 informative [R1]
- Figure 3 多线灰度打印时可能难以区分，建议增加 marker/line style 变化 [视觉审查]
- §2.1 丢弃 19/200 pairs 是否引入 selection bias [R1]
- Appendix B Stubbornness Taxonomy 基于单一 checkpoint 手动检查 100 responses，无 IAA [R1]
- Chen et al. (EMNLP 2025) "Self-Augmented Preference Alignment" 未引用 [R2]
- Lightman et al. (2024) process reward models 与 supervision density 讨论相关 [R1]
- 建议 supplementary 中同时报告 arithmetic mean 和 harmonic mean 结果以增强 metric 选择透明度

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上达成完全一致：

1. **MF-1 (C3 overclaim)**：ACT vs GRPO 存在多重混淆变量，"supervision density hypothesis" 的因果归因不成立。两位独立识别，交叉完全确认。
2. **MF-2 (单模型泛化)**：标题和 claim scope 远超实验覆盖范围。
3. **MF-3 (统计效力)**：n=2 seeds 不足，ACT seed 2 需完成。（R2 severity 稍低但方向一致）
4. **SF-1 ~ SF-8**：所有 Should-Fix 均获两位一致或部分一致。

## Reviewer Divergence [REBUT — 已解决]

1. **NLI 评估循环性**（R1-W2 提出 vs R2 反驳）：R2 论证循环性**有利于** R3-only GRPO（优化自己被评估的指标），使其失败更有说服力；对 d_syc-based methods 和 ACT 不存在循环。**Director 判断：R2 论证有效，降级为 minor concern。**

2. **SyconScore harmonic mean**（R1-W5 提出 vs R2 反驳）：R2 引用 F-score 类比——precision=0.95 + recall=0.07 的 arithmetic mean 0.51 掩盖了极端不平衡，harmonic mean 是惩罚不平衡的标准做法。**Director 判断：R2 论证有效，harmonic mean 是合理设计。建议 supplementary 中报告 arithmetic mean 结果。**

3. **d_syc 提取方法替代方案**（R2 minor 提出 vs R1 反驳）：R1 指出 recalibration 已将 AUROC 提升至 0.910 仍 fail，更高 discriminability 不解决 geometric overlap 的根本问题。**Director 判断：R1 论证有效，此项不构成实质问题。**

---

## Questions for Authors

1. 如果给 GRPO 提供 labeled valid/invalid pairs（如 expert demonstrations 构建 comparison group），GRPO 是否仍会失败？这能隔离 supervision granularity 和 label availability 两个因素。
2. Token-level RL reward（如 process reward model 为每个 token 打分）是否改变结论？这能隔离 "representation direction 问题" 和 "per-completion compression 问题"。
3. PPO 的 value function 和 clipping mechanism 是否对 reward noise 更鲁棒？排除 PPO 的理由？
4. Probe reward trap 的 behavioral-before-distributional 时序分离是否在 cosine formulations 中也观察到？
5. 仅在 strong evidence 子集上训练 RL（利用高判别力区间 AUROC 0.929）是否能避免 conflation？
6. 更温和的 recalibration 策略（EMA、延长间隔至 1000/2000 步）是否缓解 F1c 的 mode collapse？

---

## Missing References

1. **Wu & Tang (2026) "When Reward Hacking Rebounds" (arXiv:2604.01476)** — 在 GRPO 中成功使用 representation-level concept directions，与本文 negative result 形成重要对比。**必须引用。已验证真实存在。**
2. **Chen, Huang & Chen (2025) "Self-Augmented Preference Alignment for Sycophancy Reduction" (EMNLP 2025)** — preference alignment 具体实例，与 DPO/KTO 讨论互补。建议引用。
3. **Lightman et al. (2024) "Let's Verify Step by Step"** — process reward models 经典工作，与 supervision density 讨论直接相关。建议引用。
4. 建议验证 "Latent-GRPO" 命名是否为 Zhang et al. (2026) 原文使用，若非则标注简称来源。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：**未配置**。项目 `external_review.paperreview_ai.enabled` 未启用。

---

## Visual Layout Check（非评分项）

状态：**已完成**（2026-05-22 11:29→11:33）

| Severity | Finding |
|----------|---------|
| **Critical** | 正文超 8 页——Sections 1-7 占满 pages 1-8，Conclusion 从 page 9 开始（约 1/4-1/3 列）。已提升为 MF-4。 |
| Warning | 前 3 页无 figure/table（首个 display item 在 page 4），审稿人缺乏视觉锚点。建议 page 1-2 加 motivating figure 或核心结果 teaser。 |
| Warning | Pages 1-2 连续纯文本，视觉节奏单调。 |
| Warning | Pages 8-9 连续无 display item（Related Work + Conclusion），与 pages 4-7 密集图表形成节奏落差。 |
| Info | Figure 2 双 y 轴确保标签清晰；Figure 3 多线灰度区分可改善；Table 4 "collapse" 文本可标准化；Figure 1 和 booktabs 表格质量好；无 margin 溢出或未解析引用。 |

---

## Overall Assessment

**Overall Score: 3.0 — Findings**
**Confidence: 4/5**

### 评分理由

论文的贡献在证据强度上呈现明显分层：

**C1（d_syc-based reward 失败）和 C2（probe reward trap）有较强实验支持。** 六种 GRPO 配置一致失败，诊断链设计优秀。Probe trap 的 behavioral-before-distributional collapse（1,300-step 时间差，reward +0.72 全程）具有独立价值和实际安全意义。这两个贡献达到 Findings 标准。

**C3（supervision density hypothesis）是证据最薄弱的环节，恰恰也是论文试图从 diagnostic paper 升级为 explanatory paper 的关键。** ACT vs GRPO 对比存在至少 4 个混淆变量（两位 Reviewer 完全一致），单模型训练不支持标题和正文的一般性声称，n=2 seeds 且 ACT seed 2 不完整进一步削弱统计基础。

**格式问题**：正文超 8 页限制，在 ARR 可能触发 desk rejection。

**Reviewer 评分分布**：R1 = 3.0（Findings），R2 = 3.5（Borderline Conference）。分歧在 0.5 分以内，核心问题判断一致。R1 额外重视统计效力和单模型泛化；R2 对定性模式一致性和 C2 的独立价值给予更多信用。

**综合判断**：以 C1+C2 为核心，论文定位为 Findings 是合理的。如果作者能 (1) 将 C3 从因果声称降级为观察性发现, (2) 限定标题和 claim 范围, (3) 完成 ACT seed 2 全部评估, (4) 解决正文超页问题, 论文可在 Findings 得到稳固接收，且有潜力达到 3.5 (Borderline Conference)。当前状态下，C3 的 overclaim 和格式违规阻碍了更高评分。

### 修改优先级

1. **MF-4**: 正文超页（格式硬伤，立即修复）
2. **MF-1**: C3 因果声称降级 + 混淆变量讨论（核心叙事调整）
3. **MF-2**: 标题和 claim 限定实验范围
4. **MF-3**: 完成 ACT seed 2 + 增强统计报告
5. **SF-1→SF-8**: 按 severity 排序

---

## Detailed Comments（逐节）

**Abstract**: 过长（接近一整栏），包含过多实验细节。建议压缩到 150-200 词，保留核心发现和 insight。

**§1 Introduction**: (1) 具体数字（AUROC 0.827、σ=0.028、15.4% 等）与后续章节完全重复，建议移除，侧重 high-level narrative；(2) C3 贡献声明措辞需软化——从 "cannot teach" 改为 "failed to teach in our experiments"。

**§2 Experimental Framework**: (1) §2.1 pairs 构建过程现已描述（GPT-4.1 pipeline、style matching validation），但 evidence strength 标注的 annotator 信息和 IAA 仍缺失；(2) §2.2 w1 选择说明仍不充分（仅两个值）；(3) §2.5 SyconScore harmonic mean 的 justification 可接受（F-score 类比），建议 supplementary 中补充 arithmetic mean 结果。

**§3 Direction Discriminability**: 质量好。Cross-model validation、evidence-strength stratification、training stability 分析全面。Figure 1 清晰。

**§4 Cosine R1 Failure**: 诊断链设计优秀。Table 2 和论证逻辑清晰。

**§5 Probe Reward Trap**: C2 是论文最强的贡献。Table 3 和 Figure 2 有效展示 behavioral-before-distributional collapse。Stubbornness taxonomy (Appendix B) 提供 ground-level 理解。

**§6 Analysis**: (1) "The critical difference is supervision granularity" 需大幅弱化；(2) 应在此节（非仅 Limitations）完整列出 ACT vs GRPO 的所有差异维度；(3) PPO/RLOO 泛化声称改为 hypothesis；(4) SMART 讨论需扩展；(5) "When Reward Hacking Rebounds" 应在此节引用讨论。

**§7 Related Work**: (1) CRAFT 对比可深化——量化 representation gap 差异；(2) "Latent-GRPO" 命名需确认来源；(3) 补充 arXiv:2604.01476 和 Lightman et al. (2024)。

**§8 Conclusion**: 需压缩到 page 8 以内。措辞限定实验范围。

**Limitations**: 写作诚实，但 supervision granularity confound 的讨论应在正文中更突出，而非仅在 Limitations 中提及。

**Appendix A**: 需补充完整 GRPO 超参数表。Truncation 已披露但影响分析不足。

**References**: (1) 当前 bib 条目格式比 Round 1 改善明显；(2) 需补充 arXiv:2604.01476；(3) 建议补充 Chen et al. (EMNLP 2025) 和 Lightman et al. (2024)。