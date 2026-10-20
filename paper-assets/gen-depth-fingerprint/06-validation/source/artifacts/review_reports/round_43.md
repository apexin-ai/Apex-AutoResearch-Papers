---
round: 43
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T06:49:26.976656+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 43 审稿报告 — gen-depth-fingerprint

**论文**: *Depth Fingerprinting: Classifying Recursive Generation Depth in Base-Model LLM Text*
**Venue**: EMNLP 2026 via ARR (May 2026 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）
**审稿模式**: fresh（重新审稿）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

论文提出 "Depth Fingerprinting" 任务——对 LLM 递归生成文本的生成深度进行分类（human / gen-1 / gen-2+），并提出 Differential Depth Response (DDR) 分解框架，将 7 个分布特征分为 drifting（位置漂移型，随深度单调变化）和 near-stationary（形态保持型，跨深度近似不变）两类。基于 8 个 base model generator、37K 样本、LOGO 交叉验证，leak-free binary F1=0.694，3-class F1=0.762；QLoRA end-to-end 分类器达 3-class F1=0.905。统计框架包含 TOST 等价检验、bootstrap CI、k-means partition 验证等。

---

## Strengths

**S1** DDR 分解是 genuine empirical contribution——将分布漂移分解为 location-shift 和 shape-preservation 两个正交维度，超越现有 binary detection 框架，提供了可解释的分析视角。k-means（silhouette=0.660）、holdout generator split、exhaustive partition enumeration 三重验证令人信服。

**S2** 统计框架在 CL 社区 empirical 论文中属上乘水准。TOST 等价检验（区分"无差异"与"无法检测差异"）、Cohen's d 效应量、Bonferroni 校正、Granger 因果检验、permutation test——方法论严谨性远超同类论文。

**S3** LOGO 评估设计规范消除了 generator leakage，leak-free binary evaluation 额外处理了 gen-0 文本重叠问题。这是评估 cross-generator 泛化的 gold standard 方法。

**S4** 消融实验极其充分：35 页论文覆盖温度敏感性、prompt 类型、解码策略、人类编辑扰动、跨域、instruction tuning、种子控制、特征消融等 20+ 项分析，thoroughness 在 EMNLP submission 中罕见。

**S5** Honest scope delineation：标题标注 "Base-Model"，Abstract/Introduction 多处明确 scope 限制，Limitations 诚实承认 instruction-tuning 衰减和 3-class 分辨率上限。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[CONSENSUS] W-C1: "Fingerprinting" 标题与 3-class 分辨率严重不匹配**
- Severity: critical
- R1 评估: N2 critical | R2 评估: N2 critical | 交叉: 双方完全同意
- 问题：5-class F1 ≈ 0.501（Table 5），gen-2/gen-3 per-class F1 仅 0.268/0.259，几乎不可区分。"Fingerprinting" 在学术语境中暗示精细识别能力（cf. browser/device fingerprinting），但系统实际分辨率仅 3 类（human / first-pass / recursive）。标题给读者的期望与论文交付能力不匹配，会引发 "overclaimed" 的判断。
- 共识建议：改用 "Depth Profiling" 或 "Depth Classification"；Abstract 首句明确 "coarse ordinal classification" 定位。R1 补充 NLP 文献中 fingerprinting 有 coarse-grained 先例，但本文语境下读者默认期望更高分辨率。

**[MAJORITY] W-C2: Scope 与 Motivation 之间的 tension**
- Severity: critical (R2) / warning (R1)
- R1 评估: W6 warning + 交叉 "AGREE with qualification" | R2 评估: N1 critical
- 问题：Introduction §1 以真实世界 LLM 文本污染（"7-17% of scientific publications"）为 motivation，但实验仅覆盖 base model，而 Appendix k 显示 instruction-tuned model 下 DDR 显著衰减（3-class F1 下降 3.7-19.9 pp，6/7 特征 ρ 反转）。最需要此技术的场景（instruct model 输出检测）恰恰是它表现最差的场景。
- 分歧：R2 认为是"根本性错位"——motivation chain 从源头被动摇；R1 认为是 "narrative tension"——论文在标题/摘要/引言中已有多处 explicit scope delineation（"base (pretrained) models"），Contributions 定位为 empirical decomposition / task formulation / scope characterization，偏分析性而非工具性。
- Director 判断：R1 的论证更有说服力——论文确实在多处前置了 scope 限制。但 Introduction 第一段的 real-world detection hook 仍给部分读者（如 R2）造成了通用框架的印象。建议缩短 §1 real-world motivation 段落，增加 base-model generation dynamics 本身作为科学问题的 motivation（model collapse、data provenance 分析），使叙事重心匹配实际贡献。不需要彻底重构。

### Should-Fix（影响评分但不一票否决）

**[CONSENSUS] W-S1: Reference model (Pythia-410M) 同族偏差主文未讨论**
- Severity: warning
- R1 评估: W2 | R2 评估: W6 | 交叉: 双方同意
- 问题：Pythia-410M 与两个 Pythia generator 共享 GPT-NeoX 架构。Table 2 中 Pythia generators F1 最高（0.795, 0.714 vs. Mistral 0.684）。Appendix s cross-family 验证（F1 变化仅 0.013）提供了部分缓解，但所有替代 reference 均为 causal LM，未测试非自回归 reference。主文未讨论此 confound。
- 建议：§3.3 或 §4.1 增加一段引用 Appendix s 结果讨论 reference model bias；提及 causal-LM-only 约束作为理论限制。

**[CONSENSUS] W-S2: Entropy/NLL 术语混淆**
- Severity: warning
- R1 评估: AGREE | R2 评估: W1
- 问题：§3.3 有 disclaimer 但全文以 "entropy_mean/std/max/min" 指代 reference-model NLL，在信息论严格的 CL 社区容易造成混淆。
- 建议：全文统一为 "ref-NLL" 或 "cross-entropy"，Table 1 feature 名可保留但加括号说明。（此 issue 自 Round 32 起反复出现。）

**[CONSENSUS] W-S3: 6-gen vs 8-gen subset 不一致**
- Severity: warning
- R1 评估: W3 | R2 评估: AGREE
- 问题：LOFO、confusion matrix、classifier sensitivity 等关键消融使用 6-gen subset，主文使用 8-gen set。特征重要性排序可能因 Llama-3.2-3B + Mistral-7B-v0.3 加入而改变。
- 建议：至少 LOFO 补充 8-gen 结果，或论证 6-gen 结论可推广。

**[CONSENSUS] W-S4: DDR partition descriptive vs mechanistic nature 未区分**
- Severity: warning
- R1 评估: W5 | R2 评估: AGREE with nuance
- 问题：DDR partition 基于特征与 depth 的 Spearman ρ 定义，这些特征随后用于分类 depth（潜在循环性）。k-means/holdout/exhaustive enumeration 验证已实质性化解循环风险，但 Discussion §5 暗示 mechanistic claim（nucleus sampling 结构性质），而 partition 本身是 descriptive observation。两个层次应清晰区分。
- 建议：Method 或 Discussion 加一段讨论 DDR 是 well-supported descriptive decomposition，nucleus sampling hypothesis 是 testable but unproven mechanistic explanation。

**[CONSENSUS] W-S5: Concurrent work 比较过于表面**
- Severity: warning
- R1 评估: AGREE | R2 评估: W5
- 问题：Table 45 仅列元数据（chain type, feature space），缺乏 finding-level 实质性对比。例如 Broken Telephone 的 factuality degradation 与 DDR location drift 的关系、Markovian Chains 的 convergence dynamics 与 greedy DDR 数据的对比。
- 建议：Discussion 或 Appendix 增加 1-2 段实质性 concurrent work comparison。

**[CONSENSUS] W-S6: Gemma-2-2B 架构敏感性暴露 unknown-architecture 风险**
- Severity: warning
- R1 评估: W1 | R2 评估: AGREE
- 问题：Gemma-2-2B 的 SentencePiece tokenizer + distinct attention 导致 gen-0/gen-1 系统性混淆。对其他 generator 影响小（F1 偏移 0.011），但暴露了部署时遇到未知架构的失败风险。
- 建议：Limitations 增加 unknown architecture 风险讨论。

**[CONSENSUS] W-S7: 跨域温度交互效应呈现不足**
- Severity: warning（R1 初审 critical，R2 成功 rebut 降级）
- 问题：R1 指出 Appendix j 用 t=1.0 超出可靠范围（t≤0.7）构成温度混淆。R2 rebut 指出论文已提供 t=0.7 跨域数据，且高温反而有利于跨域表现（方向与 R1 推断相反）——温度混淆的 confound 方向不成立。但 domain×temperature interaction 发现（主域低温好、跨域高温好）仅一句内嵌描述，对实际部署有重要意义。
- 建议：Appendix j 将此 interaction 提升为独立小节。

**[MAJORITY] W-S8: Downstream utility n=3 power 不足 + 正文引用语气过强**
- Severity: warning (R1) / info (R2)
- 问题：n=3 seeds 的 TOST 功效极低。Appendix m 已有充分 disclaimer（"preliminary observation"），但正文 §5 引用时语气更肯定。
- 建议：正文引用加 "preliminary evidence suggests" qualifier。

**[MAJORITY] W-S9: Abstract 信息密度过高**
- Severity: warning (R2) / info (R1)
- 问题：不到 250 词塞入 8+ 数值结果，核心信息被数字淹没。
- 建议：保留 core contribution 数字（DDR effect sizes, F1），将 context 信息（cost, parameter range, sampling params）移至 Introduction。

### 小问题（不影响接收）

- **I1**: Limitations 缺 English-only 语言泛化性讨论 [R2 raised, R1 agree]
- **I2**: Missing reference: Xu et al. (2024/2025) paraphrase attack [R2 raised, R1 agree]
- **I3**: Table 1 feature 名格式不统一（下划线 vs 空格）[R1]
- **I4**: Figure 3 灰度可读性不足 [R1, R2 agree]
- **I5**: 未提供 Anonymous GitHub link [R1]
- **I6**: Figure 1 caption 信息量不足 [R2]
- **I7**: Table 2 脚注 3 不易发现 [R2]
- **I8**: §3.1 depth 定义与 3-class collapse 策略位置可优化 [R2, R1 partial rebut]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识（标注 [AGREE]）：

1. **"Fingerprinting" 术语过度承诺** — 3-class 分辨率不支持此术语。建议改为 "Depth Profiling/Classification"。
2. **DDR 是 genuine empirical contribution** — drifting/stationary 分解有清晰可解释性，验证充分。
3. **统计框架异常严谨** — TOST + bootstrap + LOGO 在 CL 社区 empirical 论文中属上乘。
4. **Reference model bias 需讨论** — Pythia 同族优势未在主文 address。
5. **Instruction-tuned 衰减是重要限制** — 需更充分讨论，特别是 unknown model type 场景。
6. **Entropy/NLL 术语应统一** — 自 Round 32 起反复提出。
7. **消融实验覆盖度极好** — 25+ appendix sections 展现罕见 thoroughness。

## Reviewer Divergence

以下问题存在分歧（标注 [REBUT]）：

1. **Scope-motivation 严重性** — R2: critical（根本性错位）; R1: warning（narrative tension，多处 scope delineation 已存在）。Director 倾向 R1 判断但要求调整叙事权重。

2. **Primary metric 选择** — R2: gen-0 vs gen-1+ 更实际; R1: gen-1 vs gen-2+ 才是本文 novelty 所在，REBUT 成功。Director 采纳 R1 立场：本文贡献在 depth discrimination 而非 binary detection。

3. **Baseline 比较公平性** — R2: strawman 印象; R1: Table 3 已有 multi-feature configs，partial REBUT。Director: 数据充分，但叙事重心应向 multi-feature comparison 倾斜。

4. **跨域温度混淆** — R1 初审 critical; R2 rebut 成功（数据已存在，方向相反）→ 降为 warning。Director 采纳 R2 rebut。

---

## Questions for Authors

1. 如果将 reference model 换成完全不同架构（RWKV/Mamba），DDR partition 是否仍成立？当前所有替代 reference 均为 causal Transformer。
2. QLoRA 在 instruct 数据上恢复到 F1=0.89-0.91，是否意味着 QLoRA 的高维特征能恢复 DDR-like decomposition？这将显著增强论文贡献。
3. LOFO 分析为何未在完整 8-gen set 上更新？是计算资源限制还是其他原因？
4. Domain×temperature interaction（主域低温好、跨域高温好）的机制解释是什么？是否与 Wikipedia-specific training bias 有关？

---

## Missing References

1. **Xu et al. (2024/2025)** — paraphrase attack 对 AI text detection 的影响，与 Appendix i perturbation analysis 直接相关 [R2 raised, R1 agree]
2. **Clark et al. (2021)** — "All That's Human Is Not Gold"，与 gen-0 detection 有概念关联 [R2 raised, R1 partially agree: 关联较弱]

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

状态: **done** (耗时 ~5 分钟)

**Findings (3 warnings, 23 info):**

- ⚠️ **Pages 1-2 连续纯文本**：无任何 display item，第一个视觉锚点（Table 1）直到 page 3 才出现。审稿人前 2 页无 figure 建立对核心贡献的直觉。
- ⚠️ **Figure 1 出现在 page 6（共 8 页正文）**：论文核心可视化（DDR strip plot）位置偏晚，审稿人到正文 75% 处才看到第一个 figure。
- ⚠️ **Page 7 纯文本页**：夹在 figure-heavy 的 page 6 和 table+figure 的 page 8 之间，display item 分布节奏不均匀。
- ✓ 所有表格 booktabs 风格统一，最优值加粗，小数位一致。
- ✓ 附录 display item 密度极高（~45 tables + 15 figures / 23 页），无连续纯文本页。
- ✓ 颜色方案跨 figure 一致，语义编码统一。
- ✓ 无公式渲染错误、LaTeX 残留标记、margin overflow 或未解析引用。

注：页面预算极紧（8 页），加 method figure 风险 > 收益，视觉审查 warning 不作为评分扣分项。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 4.0 | 3.5 | 3.75 |
| Excitement | 3.0 | 2.5 | 2.75 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | 3.0 |

**置信度**: 4/5（两位 Reviewer 均熟悉 AI text detection 和 LLM 评估领域）

**理由**: DDR 分解是一个有价值的 empirical finding，统计框架严谨、消融充分。但两个 critical 问题制约了主会议接收：(1) "Fingerprinting" 术语对 3-class 分辨率过度承诺（共识），(2) Introduction motivation 与 base-model-only scope 之间的 tension（R2 critical, R1 warning）。方法论贡献偏观察性（7-feature XGBoost），novelty 主要来自 task formulation 和 empirical finding 而非方法创新。

作为 **Findings** 论文是合理的——empirical contribution 有清晰价值，scope 限制被诚实标注，附录深度远超同类论文。如果修复 framing 问题（标题调整 + Introduction 叙事重心调整 + 术语统一），有潜力在修订后达到 3.5 (Borderline Conference)。

---

## Detailed Comments

### §1 Introduction
- 第一段 real-world motivation ("7-17% of scientific publications") 与 base-model-only scope 存在 tension。建议缩短此段，增加 base-model generation dynamics 本身作为科学问题的 motivation（model collapse 研究链、data provenance 分析价值）。
- Contributions 列表（Empirical decomposition / Task formulation / Scope characterization）定位准确，无需修改。

### §2 Related Work
- §2.2 concurrent work 比较过于元数据化。Table 45 应补充 finding-level 对比：DDR 与 Broken Telephone factuality degradation 的关系、Markovian Chains convergence 与 greedy DDR 的数据对比。

### §3 Method
- §3.3 entropy/NLL 术语应统一。
- Reference model (Pythia-410M) 选择及同族偏差应在此处或 §4.1 讨论。

### §4 Results
- §4.1 leak-free binary F1=0.694 作为 primary metric 定位合理（R1 rebut R2 成功）。
- §4.2 DDR partition 讨论应明确 descriptive vs mechanistic 区分，加强 Appendix v 验证结果的主文引用。
- §4.3 baseline comparison 叙事应以 4-det+surface ensemble 为主对比点。

### §5 Discussion
- Downstream null result 引用需加 "preliminary evidence" qualifier。
- QLoRA 在 instruct 数据上的恢复（F1=0.89-0.91）值得更多讨论——暗示 depth signal 在 instruct model 中并非消失而是需要更强特征提取器。

### Limitations
- 需增加：English-only 语言限制、unknown architecture 部署风险、unknown model type（base vs instruct）场景。

### Abstract
- 数字负担过重，建议精简至 3-4 个关键指标。
- 如标题修改为 "Depth Profiling/Classification"，Abstract 首句应同步调整。

### Appendix
- Appendix j: domain×temperature interaction 提升为独立小节。
- LOFO 等关键消融建议补充 8-gen 结果。
- 建议加 Appendix Table of Contents 改善导航。