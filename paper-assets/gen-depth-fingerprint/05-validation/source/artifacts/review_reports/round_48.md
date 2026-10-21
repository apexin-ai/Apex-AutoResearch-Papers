---
round: 48
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T13:12:30.481149+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 48 审稿报告 — gen-depth-fingerprint

**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewers**: R1 (方法严谨性) + R2 (新颖性/完整性)
**模式**: Fresh (重新审稿)

---

## Summary

论文提出 "Depth Profiling"——使用基座模型 LLM 的 NLL 分布特征对递归生成深度进行分类。核心贡献是 Differential Depth Response (DDR) 分解框架，将 7 个分布特征划分为 "drifting"（随深度漂移）和 "near-stationary"（形状保持）两类。在 8 个 base-model generator（5 个模型家族）上通过 Leave-One-Generator-Out (LOGO) 交叉验证，XGBoost 分类器达到 3-class macro F1=0.762，leak-free binary F1=0.694。论文附有 38 页附录覆盖大量消融实验。

---

## Strengths

1. **评估方法论深度罕见** [共识, R1+R2]: LOGO CV + LOFO + TOST 等价检验 + permutation testing + Granger causality + seed control + length confound analysis + ANOVA variance decomposition 的组合在 AI text detection 领域极为少见。38 页附录覆盖了几乎所有可预见的 ablation。

2. **DDR 分解提供有用分析视角** [共识, R1+R2]: Location drift + shape stability 的二维分解有独立概念贡献——它预测了 recursive generation 的 distributional convergence 行为，并为后续研究提供结构化参考框架。R1 指出 DDR 具有功能性含义：指导 feature selection 和信息互补分析。

3. **Cross-generator 一致性验证充分** [共识, R1+R2]: DDR 在 8 gen / 5 family 上保持一致。LOFO、cross-model chains (binary F1=0.830)、8×8 transfer matrix 共同验证了泛化能力。

4. **LOGO 协议设计严谨** [R1]: 正确识别 gen-0 seed sharing 泄漏风险并通过 leak-free binary metric 处理。

5. **统计方法论扎实** [R1]: Bootstrap CI、TOST、Cohen's d、Bonferroni correction、permutation testing、Granger causality 组合体现良好统计素养。

6. **诚实 scope 声明和 negative result 报告** [R2]: Title/Abstract 限定 base-model；downstream utility 诚实报告 null result；Table 3 baseline 对比公平。

---

## Weaknesses

### Must-Fix (4 issues, 影响接收决定)

**MF-1** [critical, R1-N1, R2 未反驳→默认接受] **Drifting Features 高度共线性——有效特征维度被系统性高估**

entropy_mean、TTR、hapax_ratio 三个 drifting features 的 PCA 共享 92.3% variance (PC1)，两两 Pearson r≈0.97。本质上是同一信号（vocabulary compression under recursive generation）的不同度量。LOFO 中单独移除各 drifting feature 仅导致 ~0.4–0.6pp F1 下降，因剩余相关 feature 完全补偿——LOFO 设计无法暴露共线性 feature 的真实贡献。**论文未报告 group ablation**（同时移除全部 3 个 drifting features）。

→ 影响：论文将 "7 distributional features" 和 "drifting/shape complementarity" 作为核心贡献框架 (Contribution 1, Section 1)。若 3 个 drifting features 实为 1 个信号，有效特征空间仅 ~4–5 维，DDR 叙事需重新表述。
→ Action: (1) 报告 group ablation：{entropy_mean, TTR, hapax_ratio} vs {entropy_std, entropy_max, entropy_min, tail_decay}；(2) 主文承认共线性；(3) 可考虑 PCA 降维验证。

**MF-2** [critical, R1-N2 + R2-W3, 共识] **DDR 阈值 post-hoc 验证存在 circularity**

d=0.50/0.15 是通用 Cohen's d 惯例，非基于 NLL 分布理论推导。k-means 验证和 exhaustive split 枚举在定义分区的同一数据上执行。Table 33 显示分区在 ε∈[0.10, 0.75] 范围内稳定——这反而支持一个更强的 claim ("robust two-cluster structure stable across wide threshold range")，但论文未利用此发现，反而将 d=0.50/0.15 呈现为 definitive boundaries。

→ Action: (1) 将叙事重构为 "robust cluster structure"；(2) 或在 Split A 定义阈值、Split B 验证，形成真正 cross-validation。

**MF-3** [critical, R2-N1 + R1 AGREE, 共识] **DDR 与 Geng et al. (2026) 新颖性区分不充分**

核心 finding 重叠高于论文承认：两篇都发现 (1) distributional drift with depth，(2) ~3 个可区分 depth class，(3) cross-generator 一致性。DDR 的 location/shape 分解是唯一真正增量贡献，但主文仅 Table 47 (Appendix z.7) 有系统对比。R1 指出 DDR 有功能性含义（指导 feature selection），但此价值未在主文充分表达。

→ Action: (1) 主文（非仅 Appendix）用结构化表格对比 DDR vs Geng et al.；(2) 实验量化 DDR 框架附加价值（如 shape features 在 Geng 方法中是否被隐式捕获）。

**MF-4** [critical, R2-N2 + R1 AGREE, 共识] **Abstract headline metric 定义混淆**

(a) "binary F1=0.694" 未标注是 gen-1 vs gen-2+（非 human-vs-AI），极易误读；(b) "matching multi-detector ensembles at ~2.1× lower cost" 使用 binary F1=0.705 (Table 3)，与 Abstract 的 0.694 不一致（不同 binary task 定义？）；(c) QLoRA 结果在 Abstract 中未标注是 6-gen LOGO 且 5→3 class post-hoc。

→ Action: Abstract 标注 "(gen-1 vs. gen-2+)"；统一所有 binary 定义；QLoRA 标注评估条件。

---

### Reviewer Divergence (1 issue)

**DIV-1** [R2: critical → R1: should-fix] **"Structural property of autoregressive generation" overclaim / Base-model-only 影响力**

- **R2 立场**: IT 后 3-class F1 降至 0.259、DDR partition 反转（"3-inversion"），说明 DDR 非 autoregressive generation 通用性质；Discussion 的 "structural property" 定位构成 overclaim；Limitations 处理不充分。
- **R1 立场**: Scope 在 Title/Abstract/Introduction 均已明确声明；IT 退化本身是有信息量的发现（DDR 是 pretraining distributional dynamics 特征而非 surface artifact）；base models 在 continued pretraining 生态中有独立应用价值。但同意 Discussion 应更充分讨论 IT 机制（掩盖 vs 破坏）。
- **Director 裁定**: 采纳 R1 降级建议，作为 **Should-Fix** 处理。但要求：(1) "structural property of autoregressive generation" 改为 "unaligned autoregressive generation"；(2) Discussion 增加 IT 机制讨论。

---

### Should-Fix (11 issues, 影响评分但不一票否决)

**SF-1** [R2-W1 + R1 AGREE] 主文约 8.2 页，超出 8 页限制约 0.2 页（Discussion 溢出到 p.9）。此问题在 Round 39 曾被修复但可能回归。**格式硬约束，必须修正。**

**SF-2** [R1-W1] Gemma-2-2B binary F1=0.440 暴露方法架构敏感性。Gemma-2 是主流开源模型，此失败应在 Limitations（而非仅 Appendix z.6）讨论。"Cross-generator" 声称需限定为 "across the eight tested base models from five families"。

**SF-3** [R1-W2 + R2-W5] Generator pool 中 Qwen 过度代表（3/8=37.5%），且 **Section 3.2 遗漏 Qwen3-1.7B**（仅列 2 个 Qwen 模型却声称 8 个 generator）。LOFO 中 Qwen held-out F1 仅 0.535（显著低于均值 0.621），暗示 family-level 脆弱性。

**SF-4** [R1-W3] XGBoost 超参数（n_estimators=200, max_depth=6, lr=0.1）固定不调。不同 feature 空间维度可能需要不同树复杂度。至少需 max_depth∈{3,4,6,8} sensitivity analysis。

**SF-5** [R1-W4] Binary F1=0.694 的实际应用价值未充分 grounding。gen-2/gen-3 recall 仅 0.268/0.259（~70%+ 误分类）。Discussion 中 "depth-stratified curation" 和 "contamination estimation" 场景未量化所需性能水平。

**SF-6** [R1-W5] tail_decay 的 rank 范围（100–1000）缺乏 justification。为什么不是 50–500 或 200–2000？

**SF-7** [R2-W2 reframe] Section 2.2 中与 Geng et al. 差异化仅 1 句话。详细对比被放在 Appendix z.7，主文 Related Work 应加强。

**SF-8** [R2-W3] Table 3 baselines 全是 binary detection methods，缺与 concurrent depth classification methods (Geng et al., Mohamed et al.) 的直接实验对比。

**SF-9** [R2-W4] 模型规模全部 ≤8.2B（仅 Appendix z.6 有 1 个 14B 初步数据）。"Cross-generator" claim 在 >10B 模型上未验证。

**SF-10** [R2-W6] Perturbation robustness 仅测试 random word replacement，未测试 paraphrasing。10% replacement 已导致 F1 下降 9%。

**SF-11** [R2-W4 + R1 AGREE] 仅覆盖英语 Wikipedia seed texts + 3 个 cross-domain。非英语完全未覆盖。对 "structural property" 声称经验基础不够充分。

---

### Minor Issues (13 items)

1. **CI typo** p.5: "[0.653, 0.0703]" → "[0.653, 0.703]" [R1+R2]
2. DDR 缩写在 Abstract 中引入过晚 [R2]
3. Figure 2 灰度打印下 marker 不可辨 [R1+R2]
4. p.14, p.34 大面积排版空白 [R1+R2 + Visual Check]
5. Table 1 "Ref. NLL" vs "Surface" 区分可添加简短定义 [R1+R2]
6. Figure 2 y 轴符号缩写（µ, σ 等）未在 caption 完整定义 [R1]
7. Appendix b 未报告 length-matching 后样本量损失比例 [R1]
8. Appendix c 仅测试简单单句 prompt [R1]
9. Footnote 2 bootstrap n=2000 与主 Table n=1000 不一致 [R1]
10. Table 2 CI 列宽压缩影响可读性 [R2]
11. Figure 1 y 轴刻度跨子图不一致 [R2]
12. Appendix 编号到 z.7 不直观 [R2]
13. Section 2.4 仅 4 行过短，应合并至 2.3 [R2]

---

## Reviewer Consensus [AGREE]

1. **DDR 新颖性与 Geng et al. 重叠需更充分区分** (MF-3)
2. **Abstract metric 定义必须统一** (MF-4)
3. **DDR 阈值叙事应重构为 "robust cluster structure"** (MF-2)
4. **页面限制必须遵守** (SF-1)
5. **评估方法论是本文最大优势**
6. **DDR 框架有组织价值但属于描述性贡献，缺 mechanistic grounding**

## Reviewer Divergence [REBUT]

**Base-model-only 约束的严重程度**（见 DIV-1）
- R2: Must-Fix — DDR 非通用性质，overclaim
- R1: Should-Fix — scope 明确声明，IT 退化有信息量
- Director: 采纳 R1 降级，但要求修改措辞 + 补 IT 机制讨论

---

## Questions to Authors

**来自 R1**:
1. 同时移除全部 3 个 drifting features 后的 LOGO binary F1？同时移除全部 4 个 shape features？
2. 能否在 Split A generators 上计算 Cohen's d 并确定阈值，在 Split B 上验证 feature assignment 一致性？
3. Gemma-2-2B binary F1=0.440 的具体失败模式（gen-1→gen-0 误分？gen-2+→gen-1 误分？）
4. Hold-out Qwen (3 models) vs Pythia (2 models) vs single-model families 的 F1 对比？
5. 用 7B 级别 reference model 替代 Pythia-410M，DDR partition 和 F1 是否变化？

**来自 R2**:
1. 将 DDR 分解应用于 Geng et al. (2026) 的 generation chains，partition 是否成立？
2. IT 后 DDR 反转——是 RLHF mode-seeking behavior 还是 SFT 多样性掩盖？
3. 仅用 TTR + hapax（无 reference model）时 LOGO binary F1 下界？
4. Table 3 "Bin F1" 与 Abstract "binary F1=0.694" 是否指同一 binary task？
5. 是否考虑从 autoregressive 采样数学性质解释 DDR（如 softmax temperature 对 mean vs max 的不同影响）？

---

## Missing References

- **Geng et al. (2026)**: 主文应有 finding-level 结构化对比（当前仅 Appendix z.7 Table 47）
- **Mohamed et al. (2025)**: 作为 concurrent depth work 应纳入 Table 3 直接对比
- **Penedo et al. (2024)**: FineWeb data curation（跨轮追踪 R46-W2，仍 open）
- **Welleck et al. (2020)**: Neural text degeneration（跨轮追踪 R46-W2，仍 open）

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未启用。项目配置 `external_review.paperreview_ai.enabled` 为 false。

---

## Visual Layout Check（非评分项）

**状态**: done（耗时 ~4 分钟）

**Critical (1)**:
- p.34: Figure 13 (cross-generator transfer heatmap) 下方约 35–40% 页面空白——全文最严重的空白浪费

**Warning (4)**:
- p.1–2: 连续 2 页纯文本无 display item，首个 Figure (Figure 1) 推迟到 p.6
- p.14: Figure 4 (violin plots) caption 下方约 15% 空白
- p.33: Figure 8 (per-feature depth trends) caption 下方约 10% 空白

**Info highlights**:
- 所有表格 booktabs 风格，最优值加粗，精度一致，格式专业
- 未发现 [?] 未解析引用、LaTeX 渲染错误或 margin 溢出
- Figure 2/5 子图字号偏小（约正文 55–65%），打印后可能难辨
- 颜色方案整体一致，色盲友好性可接受

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
| Excitement | 3.5/5 | 2.5/5 | 2.75/5 |
| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |
| Overall | 3.5 | 3.0 | **3.0** |

**置信度**: 4/5（两位 Reviewer 均熟悉 AI text detection 和 model collapse 文献）

### 评分依据

论文在评估方法论上达到顶会水平（38 页附录、统计检验组合、严格的泄漏控制），这是两位 Reviewer 的强共识。DDR 分解作为描述性框架有学术参考价值。

但以下问题共同阻止 main conference 接收：

1. **有效新颖性被双重削弱**: (a) drifting features 共线性（r≈0.97, 92.3% PCA variance）使 "7-feature" 叙事的有效维度降至 ~4–5；(b) 与 Geng et al. 的核心 finding 重叠（~3 depth classes + cross-generator consistency）使 DDR 增量贡献主要限于 location/shape 分解，而这作为描述性标签概念深度有限。

2. **方法论基础的两个 circularity**: (a) DDR 阈值在同一数据上定义和验证；(b) LOFO 中单 feature 移除无法暴露共线性 feature 的真实贡献（需 group ablation）。

3. **Excitement 不足**: 核心观察（递归生成降低文本多样性）并不出人意料；base-model-only 约束限制实际影响面；binary F1=0.694（gen-2+ recall ~27%）实际应用价值存疑。

### Findings 推荐理由

论文是扎实的 empirical contribution——问题提出清晰、评估设计严谨、报告诚实透明。DDR 框架为后续研究提供了有用的组织视角。适合 Findings 轨道。若能解决 collinearity group ablation 和 concurrent work 差异化，有望升至 Borderline Conference。

---

## Detailed Comments

### Abstract
- "binary F1=0.694" 必须标注 "(gen-1 vs. gen-2+)"
- "matching multi-detector ensembles" 的 binary F1 定义需与 0.694 对齐
- QLoRA 结果需标注 "(6-gen LOGO; Appendix)"

### Section 1 (Introduction)
- Contributions 中 "7 distributional features" 的有效独立维度需限定
- 与 concurrent work 的 finding-level 差异应在此节展开

### Section 2.2 (Related Work - Concurrent)
- 与 Geng et al. 差异化仅 1 句话不够，需结构化对比

### Section 3.2 (Generator Pool)
- **Qwen3-1.7B 被遗漏**——列表仅列 7 个 generator 却声称 8 个
- Qwen 家族占比 3/8=37.5% 需讨论潜在 bias

### Section 3.3 (Feature Extraction)
- tail_decay rank 范围 100–1000 缺选择理由

### Section 3.4 (Classification)
- XGBoost 超参数固定需至少做 max_depth sensitivity analysis

### Section 4.2 (DDR Analysis)
- **三个 drifting features 共线性（r≈0.97）必须在此节明确承认**
- **Group ablation 结果应补充**（同时移除 3 drifting / 4 shape features）
- 阈值叙事建议重构为 "robust two-cluster structure stable across ε∈[0.10, 0.75]"

### Section 5 (Discussion)
- 需压缩约 15 行以满足 8 页限制
- IT 对 DDR 的机制性含义（掩盖 vs 破坏）需讨论
- "structural property of autoregressive generation" 应改为更精确限定
- Binary F1=0.694 的 practical deployment requirements 需分析

### Table 3 (Baseline Comparison)
- 缺与 concurrent depth classification methods (Geng, Mohamed) 直接对比

### Limitations
- Gemma-2-2B 泛化失败应在此节讨论
- English-only 限制可更显著

---

## Issue Tracker 同步

已更新 `review_issues.yaml`：73 条（14 open + 3 in_progress + 13 条 R48 新增 + 7 条既有条目追加 R48 mention）。

新增 critical issues: R48-N1 (collinearity), R48-N2 (threshold circularity), R48-N3 (Geng novelty), R48-N4 (abstract metric)。
新增 warning issues: R48-DIV1 (overclaim), R48-W1–W8 (generator pool, hyperparams, practical value, page limit, language coverage, perturbation, concurrent baselines)。
跨轮追踪更新: R39-W2 (concurrent work 再次被提出), R39-N2 (page limit 可能回归), R43-W1 (Gemma 再次被提出), R44-N1/R46-W1/R47-W1 (本轮未提及标注)。