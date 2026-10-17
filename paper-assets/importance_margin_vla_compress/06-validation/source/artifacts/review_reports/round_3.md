---
round: 3
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-19T06:00:24.707953+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3 (Fresh Review)

**论文**: Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility
**Venue**: CoRL 2026 (Deadline: 2026-05-29)
**Reviewer 组成**: R1（方法严谨性 + 实验设计 + 统计有效性）, R2（新颖性 + 相关工作 + 论文定位 + 写作质量）

---

## Summary

论文系统性比较了两种 VLA 架构（SmolVLA pixel-shuffle connector vs OpenVLA MLP projector）在 vision token pruning 下的行为差异。核心发现：pixel-shuffle connector 在任何形式的 token deletion 下均发生 cliff-edge failure（59.2% → 0%，即使仅移除 5% tokens），而 MLP projector 则 graceful degradation（74.0% → 37.4%）。论文通过 attention entropy ratio 提供了 mechanistic explanation，并用 cross-attention re-encoding diagnostic experiment (Smart Compress) 验证了 re-encoding 可以克服 deletion 的失败模式。

---

## Strengths

1. **研究问题重要且及时**: VLA token pruning 是当前部署的热点问题，系统性诊断 connector 对 compressibility 的影响填补了文献空白。[R1, R2 一致]

2. **Cliff-edge 发现 striking 且 well-documented**: 7 configurations × 3 mechanisms × 2 checkpoints × 3 suites 全部 collapse to 0%，排除了偶然性。k=0.95 即崩溃（仅移除 7/128 tokens）的发现对 practitioners 有直接警示意义。[R1, R2 一致]

3. **实验控制设计合理**: Extended training control (45.0%) 排除额外训练步数效应，M=128 passthrough control (59.8%) 分离 compression 和 re-encoding 效应，Wilson 95% CI 规范使用。[R1, R2 一致]

4. **诚实的 framing 和 Limitations**: 论文将 Smart Compress 定位为 diagnostic experiment 而非 method contribution，承认 scale confound，标注 concurrent work。Section 5.6 Limitations 全面。[R1, R2 一致]

5. **Offline vs closed-loop disconnect 分析有方法论价值**: Section 5.4 + Appendix 展示的 catastrophic gripper inversion 分析对 VLA compression 文献有通用参考意义。[R1, R2 一致]

6. **写作质量高**: 叙事清晰，主线统一，无 AI 写作痕迹，术语首次出现有定义，图表 caption 自包含。[R1: Clarity 4/5, R2: Clarity 7/10]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [critical, R1+R2 consensus] **Connector vs. Scale 因果混淆未解决**
- SmolVLA (0.5B, pixel-shuffle) vs OpenVLA (7B, MLP projector) 同时变动 connector 和 model scale（14× 参数差异）。
- Section 5.3 给出四条间接证据，但两位 Reviewer 逐条评估后均认为不 definitive：
  - (1) Official checkpoint 同样 cliff-edge → 仍是同一 0.5B 架构
  - (2) k=0.95 即崩溃 → 小模型可能对扰动更敏感（容量冗余更少）
  - (3) Entropy ratio 是 architectural measurement → 但 entropy 可能受 scale 影响（32 层 vs 16 层，更多层 = 更多 selective attention 机会），存在循环论证风险
  - (4) 4×4 folding mechanistic account → 最强论据，但仍为 necessary condition 非 sufficient proof
- **标题 "The Role of Vision Connectors" 本身就是因果 framing，与当前证据强度不匹配。**
- 建议：(a) matched-scale controlled experiment（理想）；(b) 在第三个 pixel-shuffle VLA 上验证 cliff-edge（退而求其次）；(c) 标题和全文改为 conditional/observational claim（最低限度）。

**MF-2** [critical, R1+R2 consensus] **Baseline 复现质量严重偏低，评估协议差异未解释**
- 两层差距：(a) 自训练 44.8% vs 官方 87.3%（batch size 4 vs 512）；(b) 官方 checkpoint 在本文评估中仅 59.2% vs 官方报告 87.3%（28pp gap）。
- 28pp 评估差异暗示评估协议存在系统性差异（action chunking? inference-time sampling? environment reset?），但论文仅用脚注一笔带过。
- 影响：undertrained 模型可能更 fragile，系统性放大 pruning 效果。Smart Compress 全部实验基于 44.8% baseline，+15pp 增益能否推广到 strong baseline 未知。
- R1 指出 M=128 (59.8%) ≈ official (59.2%) 巧合暗示 cross-attention 可能只是在补偿 batch-size 不足。
- 建议：详细说明评估协议差异；在 official checkpoint 上训练 Smart Compress；讨论 baseline 质量是否影响 cliff-edge threshold。

**MF-3** [critical, R1+R2 consensus] **统计验证不足 + 实验设计不对称**
- Multi-seed 仅 2 seeds (42, 43)，CoRL 通常期望 ≥3（理想 5）。M=96 半幅差 ±2.8pp (52.6% vs 58.2%)，在 2 seeds 下无法判断 noise vs systematic。Table 8 caption "low variance across seeds" 在统计上不可信。
- 实验设计不对称：SmolVLA 7 configurations + Smart Compress + cross-suite；OpenVLA 仅 random pruning × 5 ratios，单一 suite，无 learned scoring、无 token merging、无 cross-suite。
- 建议：增加至 ≥3 seeds，报告 mean±std；补充 OpenVLA learned pruning 和 cross-suite 评估。

### Should-Fix（影响评分但不一票否决）

**SF-1** [warning, R2 critical / R1 should-fix, 分歧] **新颖性在 concurrent work 密集背景下受限**
- 至少 7 篇直接相关 concurrent work：Don't Run with Scissors (weight pruning 崩溃), See What Matters (ICML 2026, SmolVLA continuous resampling), Compressor-VLA (cross-attention 97.1% SR), EfficientVLA, VLA-IAP, SpecPrune-VLA, LightVLA。
- Cross-attention re-encoding 是 Q-Former/Perceiver 已知方案。"First systematic comparison" claim 在 concurrent work 已分别覆盖各 connector 类型的背景下不够 compelling。
- **R1 rebut**: 论文 diagnostic contribution（7-config ablation + entropy analysis + offline-vs-closed-loop disconnect）超越简单比较，与 "See What Matters" (方法论) 互补而非重叠。
- 建议：更精确 position 为 empirical analysis paper；弱化 "first" claim 或限定更窄 scope；明确区分与 concurrent work 的互补关系。

**SF-2** [warning, R2 critical / R1 should-fix, 分歧] **Simulation-only 评估对 CoRL venue fit 的影响**
- 全部实验在 LIBERO 上完成，无 real-robot 验证。CoRL 偏好 real-robot。
- **R1 rebut**: CoRL 历年接收 sim-only 分析论文；pixel-shuffle 4×4 folding 在 real-world 不会改变；sensor noise 不太可能改变 "所有 pruning → 0%" 的 categorical failure。
- 建议：如可行增加 real-robot pilot study 或第二 sim benchmark；至少更充分讨论 sim-to-real gap。

**SF-3** [warning, R1+R2 consensus] **Smart Compress 增益归因不完全 clean**
- 22.2M 额外参数容量 vs re-encoding 未分离。M=128 passthrough 仍含 cross-attention 参数。Extended training control 排除了额外步数但未排除额外容量。
- 建议：增加 matched-parameter MLP adapter control，或降低 claim 为 "adding a learnable cross-attention layer helps"。

**SF-4** [warning, R1+R2 consensus] **Attention entropy ratio 证据极薄**
- 仅 2 个数据点 (SmolVLA 0.95, OpenVLA 0.64)。Section 5.5 的 >0.9 threshold 无 empirical backing。Entropy ratio 可能受层数差异 (16 vs 32) 影响。
- 建议：在更多 VLA/VLM 上测量；弱化为 "descriptive metric" 非 "compressibility signal"。

**SF-5** [warning, R1+R2 consensus] **Cross-suite 泛化下降被低估**
- LIBERO-Goal: 63.0% → 56.4% (−6.6pp)。正文仅说 "maintains non-trivial performance"，弱化 negative signal。
- 建议：正文直接讨论下降及 implications，限定 claim 为 in-distribution 场景。

**SF-6** [warning, R1+R2 partial consensus] **EfficientVLA/CogACT 证据归因不准确**
- 97.8% SR 数据来源需核实（可能来自 VLA-IAP 而非 EfficientVLA）。Contribution 1 "three models" 容易误导为本文自有实验。CogACT 原始论文未被直接引用。
- 建议：核实数据来源，更精确表述，引用 CogACT 原始论文。

**SF-7** [warning, R1] **Latency 收益仅 1.06×，motivation scenario 在 128-token 模型上不成立**
- Token reduction 非 SmolVLA 的 inference bottleneck。如果无人会在 128-token 模型上做 token pruning，cliff-edge 的实际影响被夸大。
- 建议：讨论 token pruning 在什么规模 VLA 上成为实际需求；强调 memory 收益 (KV-cache 75% reduction) 而非 latency。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成明确共识 [AGREE]：
- **MF-1**: Scale confound 是论文最核心的弱点
- **MF-2**: Baseline 质量和评估差异是 critical issue
- **MF-3**: 统计验证不足（seeds、不对称设计）
- **SF-3**: Smart Compress 参数容量 vs re-encoding 未分离
- **SF-4**: Entropy ratio 仅 2 数据点不足以建立 predictive utility
- **SF-5**: Cross-suite 泛化下降被低估
- **SF-6**: EfficientVLA 证据归因需核实

## Reviewer Divergence

| 问题 | R1 判断 | R2 判断 | 分歧原因 |
|------|---------|---------|----------|
| **SF-1** (novelty) | should-fix | critical | R1 认为 diagnostic contribution（7-config ablation + entropy analysis + offline-vs-closed-loop disconnect）超越简单比较，与 concurrent work 互补 |
| **SF-2** (sim-only) | should-fix | critical | R1 认为 CoRL 接受 sim-only 分析论文，pixel-shuffle cliff-edge 是 architectural property 不依赖 real-world |
| **MF-2** (baseline severity) | critical (N2) | should-fix (W2) → 被 R1 说服升级 | R1 认为 28pp 评估差异比 R2 初始判断中更严重 |

---

## Questions to Authors

1. 官方 SmolVLA checkpoint 在本文评估中 59.2% vs 官方报告 87.3%——请详细说明评估协议差异来源（action chunking, inference-time sampling, env reset, obs preprocessing）。28pp gap 是否意味着评估整体偏严？所有 method 是否受同比例影响？
2. 是否可能在相同 backbone (Qwen2-0.5B) 上替换 pixel-shuffle 为 MLP projector 进行 controlled experiment？或在第三个 pixel-shuffle VLA 上验证 cliff-edge？
3. CogACT 的 attention entropy ratio 是多少？如有第三个数据点会大幅增强证据。
4. Smart Compress M=128 (59.8%) 与 official checkpoint (59.2%) 性能接近——cross-attention 是否本质上在"修复" batch-size 不足导致的训练问题？
5. Contribution 1 引用的 97.8% SR 具体来自 EfficientVLA 还是 VLA-IAP？请核实并准确引用。
6. "See What Matters" (ICML 2026) 的 continuous resampling 在 SmolVLA 上成功——这本质上也是 re-encoding。论文如何与此 concurrent work 区分定位？

---

## Missing References

- **CogACT 原始论文**: 通过 EfficientVLA 间接引用但无原始 citation [R1, R2]
- **OpenVLA-OFT**: Compressor-VLA 的 baseline，LIBERO 97.3% SR [R2]
- **TokenPacker / TinyLLaVA**: VLM spatial-aware token compression 相关工作 [R2]
- **TinyVLA / 小模型 VLA**: 论文涉及 0.5B VLA 但未引用小模型 VLA 领域 [R1]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Overall Assessment

**Rating: Weak Reject (4-5/10)**
- R1: 5/10 (Marginally below acceptance threshold), Confidence 4/5
- R2: 4/10 (Weak Reject), Confidence 3/5

**置信度: 4/5**

论文观察到了一个有价值的 empirical phenomenon——pixel-shuffle VLA 在 token pruning 下的 cliff-edge failure。实验控制设计有功底（7-config ablation, extended training control, passthrough control, Wilson CI），写作质量高，Limitations 诚实。

但作为以 empirical finding 为核心的论文，实验设计的严谨性是生命线，本文在三个关键维度上未达 CoRL 接收标准：

1. **因果归因不可靠 (MF-1)**: connector vs. scale 的 14× confound 未被 controlled experiment 解耦，但标题和全文做出了关于 "the role of vision connectors" 的因果 claim。四条间接证据均非 definitive，两位 Reviewer 一致。

2. **Baseline 质量和评估可靠性存疑 (MF-2)**: 自训练 44.8% baseline 严重 undertrained，官方 checkpoint 评估 59.2% vs 官方报告 87.3% 的 28pp gap 未解释。Smart Compress 增益能否在 strong baseline 下复现未知。

3. **统计验证不足 (MF-3)**: 2 seeds 不符合 CoRL 标准，实验设计在两架构间严重不对称。

此外，novelty 在 concurrent work 密集的背景下受限（R2 列为 critical，R1 认为论文的 diagnostic contribution 有独立价值），simulation-only 评估对 CoRL venue fit 有一定影响。

如果作者在 rebuttal 中能提供 matched-scale experiment（或第三个 pixel-shuffle VLA 的 cliff-edge 验证）、解释评估协议差异、增加 seeds 至 ≥3，评分有上调至 borderline (5-6) 的空间。但在当前状态下，cannot recommend acceptance。

---

## Detailed Comments

### Abstract
- 约 220 words，符合 150-250 范围但偏长。包含过多数字细节（"7 of 128"、"Wilson 95% CI"、"$k{=}0.95$"），更适合放在 Results。
- "strongly linked to the vision connector design" 仍是隐含因果 claim。

### Introduction
- 叙事线清晰，从 ViT pruning 成功 → VLA 应用前景 → SmolVLA cliff-edge → 架构分析 → re-encoding 验证。
- Contribution 1 "supported by concurrent findings from EfficientVLA across three models and two connector families" 中的 "three models" 容易误导为本文实验覆盖 3 模型。97.8% SR 数据来源需核实。
- Contribution 2 "may serve as a preliminary compressibility signal" 措辞合适，但 Section 5.5 的具体 threshold 建议与此措辞矛盾。

### Related Work
- 引用覆盖较全，包含 7 篇 VLA token compression concurrent work + VLM token efficiency + ViT pruning。
- 缺少：CogACT 原始论文、OpenVLA-OFT、TokenPacker/TinyLLaVA、小模型 VLA。
- Positioning 基本准确。"None reports the cliff-edge failure we observe on pixel-shuffle VLAs" 在 "Don't Run with Scissors" (weight pruning → 0%) 存在的情况下需更精确限定为 "token pruning on pixel-shuffle"。

### Experimental Setup
- Section 3 标题 "Experimental Setup" 但包含 Smart Compress 方法描述 (Section 3.4)，属于 method 而非 setup。考虑改为 "Methods and Setup"。
- Table 11 (Appendix) 训练细节完整（lr, optimizer, batch size, GPU 等），但正文 Section 3.4 仅说 "trained end-to-end"——"Total trainable parameters: 122.1M / 472.2M (25.85%)" 暗示冻结了 vision encoder 但解冻了 LLM backbone，这个关键信息应在正文明确。

### Results
- Table 1 SmolVLA ablation 结构清晰，7 configurations 覆盖 scoring × ratio × mechanism 三轴。
- Table 1 "True removal" 行 CI upper bound 0.80% vs 其他行 0.76%——episode 数差异未说明。
- OpenVLA degradation curve 数据点充分 (6 ratios)，但仅 random pruning 限制了比较公平性。

### Analysis and Discussion
- Section 5.1 pixel-shuffle mechanistic account 是全文最强论据。
- Section 5.1 "total variation 0.05" vs "total variation 0.50"——"total variation" 在统计学中有特定含义（TV distance），这里指 range，用词可能误解。
- Section 5.3 的 disentangling 论证结构合理但力度不足（见 MF-1）。末段 "we cannot fully exclude model scale" 的 hedging 恰当但与标题的因果语气矛盾。
- Section 5.4 offline metric disconnect 论证：3.4× action error 本身就是负面信号，"misleadingly positive" 的 claim 需要展示某个 offline metric 看起来正常但 closed-loop 崩溃的对比。
- Section 5.5 Design Implications Item 1 的 >0.9 threshold 建议无充分 empirical backing。

### Appendix
- 内容丰富：per-task breakdowns, full ablation, cross-suite, training details, offline error analysis, entropy details, cost-benefit。
- background.tex 和 experiments_deprecated.tex 存在于 paper 目录但未被 main.tex include——提交源码包时应清理。

### References
- 30 条引用。`oquab2023dinov2` bib key year 2023 但 venue TMLR 2024；`bolya2023tome` bib year 2023 但可能应为 2022——建议核实。
