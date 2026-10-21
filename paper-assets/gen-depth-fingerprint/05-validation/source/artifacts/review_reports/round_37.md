---
round: 37
review_mode: fresh
overall_score: 3.0-3.5 (Findings to Borderline Conference)
timestamp: 2026-05-21T04:48:59.499721+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 37 审稿报告：Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains

**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**审稿模式**: Fresh (重新审稿)
**Reviewer 配置**: 2 人 — R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性)

---

## Summary

本文提出 "depth fingerprinting" 任务，旨在检测 LLM 文本的递归生成深度（generation depth）。作者设计了 7 个手工特征（基于 NLL 统计和词汇多样性），提出 DDR (Differential Depth Response) 分解框架，将特征分为 "drifting"（随深度单调变化）和 "near-stationary"（跨深度近似不变）两类。在 8 个 base-model 生成器、5 个模型家族上，使用 LOGO (leave-one-generator-out) 交叉验证，binary classification (gen-1 vs gen-2+) F1 = 0.694。论文配有极其扎实的 25 页附录，覆盖几乎所有可预见的消融和鲁棒性分析。

---

## Strengths

**S1** [共识] **新颖的任务定义**：将 AI 文本检测从 binary (human vs machine) 推广到 ordinal depth estimation，为递归生成文本的 provenance 分析打开新方向。DDR 的 drifting/stationary 分解提供了一个分析 iterative generation 的新框架。

**S2** [共识] **极其扎实的实证分析**：25 页附录覆盖了 length confound、prompt type generalization、temperature sensitivity、cross-domain、text perturbation、classifier alternatives、reference model variants、TOST equivalence testing、Granger causality、UMAP 可视化、cross-model chains 等。两位 Reviewer 均评价为 "近期审稿中见过的最 thorough 的实证分析之一"。

**S3** [共识] **评估协议设计严谨**：LOGO 排除 generator-level leakage + 排除 gen-0 避免 trivial human/machine 信号膨胀 + length-matched subsampling 控制长度混淆 + LOFO 进一步测试跨家族泛化。每一步都反映了对实验公平性的深思熟虑。

**S4** [共识] **统计学素养规范**：全面使用 Bootstrap 95% CI、Cohen's d、Cliff's δ、TOST 等价检验、Spearman 相关、Granger causality。Appendix V 的 exhaustive partition enumeration 和 bootstrap stability 分析尤其令人印象深刻。

**S5** [共识] **写作质量整体较好**：英文学术写作水平在平均线以上，术语使用准确，未发现明显 AI 写作痕迹。Introduction 从 "re-enter generation pipelines" 到 "data governance" 的动机链条清晰。

---

## Weaknesses

### Must-Fix (Critical) — 影响接收决定

**C1** [共识, R1-N1 + R2-N3] **Instruction-tuned 模型上 DDR 信号严重退化，核心 claim 不成立**
- Appendix K: 3-gen instruct LOGO binary F1 = 0.487（接近随机水平）；OLMo-Instruct retrained F1 仅 0.590-0.660；DDR partition silhouette 从 0.660 降至 0.372；Qwen3-instruct 出现 "3-class inversion"。
- Conclusion 中 "DDR captures generation-process invariants" 在 instruction-tuned 模型上不成立。而 2026 年几乎所有部署的 LLM 都经过 instruction tuning。
- 论文贡献从 "检测 recursive generation depth 的通用工具" 退化为 "base model continuation chain 上的现象描述"。
- **两位 Reviewer 独立提出，交叉完全 AGREE。本文最严重问题。**

**C2** [共识, R2-N1, R1 AGREE] **标题 "Depth Fingerprinting" 与实际分辨率不符，构成 overclaim**
- §4.2 承认 "depth resolution is bounded at three classes"，depth 2-4 mutually indistinguishable。5-class LOGO F1 降至 0.50。
- 系统有效分辨率仅为 gen-0/gen-1/gen-2+，核心贡献本质上是 gen-1 vs gen-2+ 的 binary 区分。
- 标题 "Detecting Recursive Generation Depth" 暗示逐步分辨能力，与实验证据有显著 gap。
- R1 补充：3-class 分辨率本身仍有价值（区分 first-generation 与 multiply-recycled text），但标题和 Abstract 应当反映这一限制。

**C3** [共识, R1-N2, R2 AGREE] **DDR 分类性能不优于已有检测分数组合，framing 有选择性**
- Table 3: 4-detector ensemble binary F1 = 0.706 vs 7-feature DDR F1 = 0.705（差距 0.001）。
- Abstract "surpassing individual detection baselines" 选择性突出优于*单个* baseline，而回避了 ensemble 已达同等性能的事实。
- 论文需将价值主张从 "better classifier" 转向 "analytical decomposition framework"。

### Should-Fix (Major) — 影响评分但不一票否决

**W1** [部分分歧, R2-W1 提出, R1 REBUT] **DDR 新颖性评价**
- R2 认为 DDR 分解本质是用 k-means 量化已知现象（Shumailov et al. 2024 已描述 "location shift + tail erosion"），论文将其包装为 "novel observation" 过度。
- R1 反驳：generation chain (固定模型反复推理) ≠ model collapse (递归数据上重新训练)，机制完全不同；DDR 发现 shape features 近似不变，与 model collapse 文献预期的 "tail erosion" 相反；k-means 是验证手段而非贡献本身。
- **Director 判断**：R1 的区分有实质依据，DDR 并非 model collapse 的简单重述。但论文应更清楚地阐明这一区别——"generation chain inference ≠ model collapse training"。

**W2** [共识, R1-W1, R2 AGREE] **实验范围过窄**
- 仅 English Wikipedia + continuation prompting + nucleus sampling (p=0.9, τ≤0.7)。
- Cross-domain F1 从 0.692 降至 0.647；Qwen3-1.7B cross-temperature F1 从 0.948 骤降至 0.418。
- 未测试 instruction-following、QA、摘要等真实使用场景。

**W3** [共识, R1-W3, R2 AGREE] **LOFO 跨家族泛化偏弱**
- LOGO F1 = 0.694 → LOFO F1 = 0.634（降幅 ~9%）。
- gen-2+ 的 LOFO per-class F1 极低（0.268-0.453），跨家族深度检测几乎失效。
- 部分下降源于 Pythia-410M 参考模型的 same-family affinity。

**W4** [共识, R2-W2, R1 AGREE] **Concurrent work 对比被藏在附录**
- Table 41 对 Mohamed et al. (2025) "Broken Telephone" 和 Geng et al. (2026) "Markovian Chains" 的系统对比被放在附录最后一页。作为最直接的 concurrent work，区分点应在 §2.2 正文中用至少一段深入讨论。

**W5** [共识, R1-W5, R2 AGREE] **缺失 fine-tuned transformer baseline under LOGO**
- QLoRA 实验使用 within-model 5-fold CV（F1=0.905），而主实验使用 LOGO（F1=0.694）——评估协议不可比。
- 缺少关键实验：fine-tuned transformer (RoBERTa/DeBERTa) 或 QLoRA 在 LOGO 下的表现。此实验可 settle handcrafted vs neural 的性能差距问题。

**W6** [部分分歧, R2-W3 提出, R1 REBUT] **Reference model 依赖的 tradeoff**
- R2: Table 2 surface-only (TTR+hapax) binary F1 = 0.688 vs full 7-feature F1 = 0.708，仅差 2pp，暗示参考模型边际贡献有限。
- R1 反驳：3-class F1 差距为 9pp（surface-only 0.68 → full 0.77），不是 marginal。R2 可能混淆了不同条件的数字。
- **Director 判断**：R1 的数据校正成立（3-class 差距确实显著），但论文应在 Discussion 中补充 "reference model dependency" 段落，完整讨论 binary 和 3-class 两个维度的 tradeoff。

**W7** [部分分歧, R1-W2 提出, R2 PARTIALLY REBUT] **DDR 理论基础薄弱**
- R1 要求信息论或统计学正式推导。
- R2 反驳：对 empirical paper 要求 formal proof 过于严苛；Shumailov et al. (2024, Nature) 也主要依靠实验观察。
- **共识方向**：补充 sketch-level 理论分析（如简化设置下 entropy 单调递减的 bounding argument），而非要求完整证明。

**W8** [共识, R1-W4, R2 AGREE] **Binary metric 排除 gen-0，不反映完整部署场景**
- 排除 gen-0 是为避免 trivial human/machine signal inflating F1（负责任的评估选择）。
- 但实际部署需要 3-class 或更细粒度的完整场景。3-class 中 gen-2+ F1 仅 0.60-0.70，这一不均衡应在主文中更显著呈现。

---

## Reviewer Consensus [AGREE]

1. **Instruction-tuned 退化是致命弱点**：两位 Reviewer 独立提出（R1-N1, R2-N3），交叉完全 AGREE。这是论文最需要解决的问题。
2. **标题 overclaim**：有效分辨率仅 3 class，标题暗示的逐步分辨能力与实验证据不符。
3. **分类性能 ≤ baseline ensemble**：DDR 的价值应定位为分析框架而非分类工具。
4. **实验范围过窄**：English Wikipedia + continuation + nucleus sampling only。
5. **Concurrent work 对比应提升到正文**。
6. **QLoRA 需要 LOGO 评估**。
7. **任务新颖、实证极其扎实、统计严谨、写作质量好**——论文的实验覆盖度在 empirical NLP 中属于上乘。

---

## Reviewer Divergence [REBUT]

1. **DDR 新颖性**：R2 认为是已知现象的量化（severity: major），R1 反驳 generation chain ≠ model collapse 且 shape stability 与 model collapse 预期相反（降级为 minor）。分歧持续。
2. **Reference model 边际贡献**：R2 认为 binary 仅差 2pp（有限），R1 校正 3-class 差 9pp（显著）。数据层面 R1 更准确。
3. **DDR 理论基础要求的严格程度**：R1 要求 formal 推导（major），R2 认为对 empirical paper 过于严苛（降级为 should-have-sketch）。

---

## Questions for Authors

1. **[共识]** Table 2 surface-only F1 = 0.688 仅比 7-feature 低 2pp (binary)。这是否意味着不需要参考模型就能获得接近的性能？如果是，DDR 框架的价值主张如何调整？
2. **[共识]** Instruction-tuned 模型 depth > 2 的链是否产生任何可检测的信号？如果 instruction tuning 消除了 depth signal，depth fingerprinting 是否仅适用于越来越小众的 base model 场景？
3. **[共识]** Binary F1 = 0.694 对应约 30% 错误率。对于 "data governance" 应用，是否有 precision-recall tradeoff 分析？
4. **[R1]** LOFO 失败案例分析——哪些 family 被 hold out 时 F1 下降最大？是否与 model scale 或 tokenizer 类型相关？
5. **[R2]** 如果生成器是 much larger model (如 70B)，参考模型 (410M) 与生成器之间的 capacity gap 是否改变 DDR 特征行为？

---

## Missing References

**共识建议补充**：
1. **Briesch et al. (2023)** "Large Language Models Suffer From Their Own Output" — 直接研究 LLM iterative generation 退化，与论文主题高度相关
2. **Diaz & Karampatziakis (2019)** "Soft Labels for Ordinal Regression" — depth task 具有 ordinal 性质，方法论参考

**R2 建议（R1 评估 nice-to-have）**：
3. C2PA content provenance 标准 — 概念上相关但非核心
4. Supervised neural detector (RoBERTa/DeBERTa) 在 depth task 上的对比 — 更适合作为实验建议而非引用

**R1 建议（R2 部分反驳）**：
5. Guo et al. (2023) "How Close is ChatGPT to Human Experts?" (AAAI) — R2 认为关联较弱，nice-to-have

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求** — 项目配置中未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态：已完成**（2026-05-21 04:25 → 04:29，耗时约 4 分钟）

| Severity | 数量 | 主要发现 |
|----------|------|----------|
| Critical | 1 | 前 4 页连续纯文本，无任何 display item（Figure/Table），首个 Table 1 直到第 5 页。对 empirical paper 第一印象极差。 |
| Warning | 5 | (1) 最后一页 Table 41 仅占 1/3，60% 空白；(2) Display item 分布严重不均（pp.1-4 零个，p.7 堆叠 3 个）；(3) Figure 2/3 尺寸偏小，打印后可能难辨；(4) Figure 4 独占整页但底部 15% 空白（违反附录可视化图应嵌入文字的规则）；(5) Figure 8/9 堆叠在同一页，面板极小 |
| Info | 10 | Title/Abstract 排版整洁；Table 1/2 booktabs 规范；参考文献无 [?] 未解析；无 margin 溢出；所有表格精度统一、最优值加粗 |

**关键建议**：将 Figure 1 或概念图前移至 p.1-2，打破前 4 页纯文字密度。

---

## Overall Assessment

**综合评分：3.0–3.5 (Findings to Borderline Conference)**
- R1: 3.5 (Borderline Conference) — Soundness 3.5, Excitement 3.0, Confidence 4/5
- R2: 3.0 (Findings) — Soundness 4.0, Excitement 2.5, Confidence 4/5

**Director 评判**：分歧 0.5 分，集中在 Excitement 维度。R1 更看重 DDR 作为分析框架的潜在影响力；R2 对 headline result 的实用价值更悲观。两者均有合理依据。

**核心判断**：这是一篇实证质量极高但技术新颖性有限的 empirical analysis paper。三个关键限制——(1) instruction-tuned 模型上 DDR 信号严重退化使核心 claim 不成立；(2) 有效深度分辨率仅 3 class 与标题不符；(3) 分类性能不优于 baseline ensemble——使其更适合 Findings。

**上调条件**（可达 3.5 Borderline Conference）：
- 诚实调整 framing（标题/Abstract）以匹配实际 3-class 能力
- 将 QLoRA 对比在 LOGO 下评估并纳入正文
- 补充至少 2 个 instruction-tuned 模型的完整评估
- Concurrent work 对比提升到正文

---

## Detailed Comments

### §1 Introduction
- "surpassing individual detection baselines" 应改为更准确的表述（DDR 与 baseline ensemble 性能相当）
- Contribution 3 的 "proof-of-concept" 定位已到位，但 Contribution 1 的 "novel observation" 措辞仍需斟酌（R2-W1）

### §2 Related Work
- §2.2 与 Mohamed et al. (2025) 和 Geng et al. (2026) 的区分讨论应从 Appendix Z.5 提升到此处
- 建议补充 Briesch et al. (2023) 和 Diaz & Karampatziakis (2019) 引用

### §3 Method
- §3.3 参考模型 (Pythia-410M) 选择的 rationale 和 same-family confound 应更显式讨论
- 7 个特征的充分性缺少理论锚点（至少可补 sketch-level 分析）

### §4 Results
- §4.1 应展示 per-class F1 breakdown（当前仅在附录 Table 4）
- §4.2 DDR 分解的分辨率上限（3 class）应更 prominently 讨论
- §4.3 应在 Abstract 中反映 DDR 与 baseline ensemble 性能相当的事实
- LOFO gen-2+ per-class F1 极低（0.268-0.453）的含义应在正文讨论

### §5 Discussion
- 应补充 "reference model dependency" 段落
- 应补充 instruction-tuned 退化的正文讨论（当前仅在 Appendix K）
- "generation-process invariants" 表述需限定为 "base-model continuation chain"

### §7 Limitations
- 当前内容充实，但可增加 precision-recall tradeoff 在不同应用场景下的分析

### Appendix
- Appendix E (QLoRA) 需补充 LOGO 评估或明确标注 within-model CV 的局限性
- Appendix K (instruction-tuned) 的关键数据应提升到正文
- Table 41 (concurrent work 对比) 应移入正文 §2.2

### 格式
- ✅ 正文 8 页，ACL 模板，double-blind，Limitations + Ethics 存在
- ⚠️ 前 4 页无 display item，建议前移 Figure 1
- ⚠️ Figure 1/2 颜色编码不一致
- ⚠️ Figure 3 caption 缺 inference cost 定义