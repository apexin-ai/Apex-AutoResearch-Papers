---
round: 4
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-20T20:24:31.781131+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: "A Sharp Detection Onset in Iterative Model Collapse"
**目标 Venue**: EMNLP 2026 (Long Paper, ARR)
**截止日期**: 2026-05-25
**审稿模式**: Fresh（独立初审，无前轮记忆）
**Reviewer 编排**: 2 人（R1 方法严谨性 / R2 新颖性与完整性）

---

## Summary

本文研究迭代训练中 model collapse 的统计可检测性边界。核心发现：permutation Granger causality (PermG) 在 per-generation mixing ratio α_c≈0.476 处从 0/8 FDR-significant pairs 跃升至 6/8（"sharp detection onset"）。作者提出 Signal×Resolution (S×R) interpretive lens 解释非单调 dose-response，通过 Multi-Method Consensus Test (MMCT) 比较五种统计方法，并在 15 model-seed combinations (6 架构, 345M–6.9B) 上做跨架构验证。实证工作扎实，实验覆盖面在 model collapse 文献中属前列；但核心方法论为成熟计量经济学工具的迁移应用，"sharp onset" 本质是统计检验力穿越阈值而非新物理/信息论发现，MMCT 存在循环论证，PermG FPR 估计因非独立性被高估。

---

## Strengths

1. **问题定位独特且重要**：将 detection 框架为 onset boundary 问题——"何时统计检测变为可行"——直接回答实践中最紧迫的问题，在 model collapse 文献中是新视角
2. **实验覆盖面突出**：13 个 α 水平 × 最多 4 seeds × 6 架构 × 2 域 = 15 model-seed combinations；null-control FPR calibration 在该领域不常见
3. **统计处理规范**：first-differencing 分离 spurious regression（canary→perplexity 被正确剔除）、BH-FDR correction、permutation testing、5,000 permutations
4. **方法论诚实**：§5 Discussion 和 Limitations 均坦承 sharp onset 是 power curve crossing 而非新 physical signal，canary claim 仅限 diversity metrics
5. **Predict-then-verify 协议**：预先锁定 T=20 预测再验证的科学实践值得肯定（尽管关键 boundary 验证未完成）
6. **Intervention proof-of-concept**：从检测到 58% peak perplexity reduction 的闭环演示，threshold sensitivity analysis (5%–25%) 和 operating band [10%, 22%] 的分析有实践价值
7. **代码/数据承诺 + 参数详尽**：Reproducibility 良好

---

## Weaknesses

### CRITICAL（共识，影响接收决定）

**C1. "Sharp onset" framing 与实质不匹配** [R1-W1 + R2-N1, 强共识]
- Title/Abstract 暗示 model collapse 动力学新发现，但 §5 自承 "reflects PermG's statistical power curve crossing the detection floor...not the emergence of a new physical signal"
- S×R 框架 Power(α,T) = Φ(S·R·√T/σ) 是标准 z-test power formula 的重参数化，S·R 即标准化效应量
- 核心方法（Granger causality, first-differencing, BH-FDR, permutation testing）均为计量经济学教科书工具
- **影响**：方法论新颖性不足以支撑主会议长文接收；实证发现（onset 位置、四 regime 结构）有价值但属 Findings 级别

**C2. MMCT 循环论证** [R1-N1, R2 交叉 AGREE]
- FPR-inverse weighting 给 PermG w=100（cap by ε）vs naive XCorr w≈1.33
- 然后用 MMCT 得出 "PermG is the only method combining zero null-control FPR with consistent detection"——近乎同义反复
- Appendix P 的 4 种权重方案 ablation 在同一框架内，不是独立验证
- 即使 equal weighting，评估标准（FPR + FNR Shapley）本身偏向低 FPR 方法
- **影响**：Contribution 3 ("multi-method diagnostic toolkit") 的独立价值大幅缩水

**C3. PermG FPR=0% 因非独立性被严重高估** [R1-N2, R2 交叉 AGREE]
- 0/24 null-control pairs 的 Rule-of-Three 95% CI=[0%, 12.5%] 假设 24 pair 独立
- 同一 seed 内 4 个 canary→downstream pairs 共享训练轨迹、generation pipeline，拒绝/不拒绝高度相关
- 有效独立观测量可能仅 ~6（3 seeds × 2 canaries），对应 CI=[0%, 50%]
- PermG 零 FPR 是 MMCT 权重、方法选择、headline claim 的基石——如果上界高达 50%，所有下游结论需重新评估
- 论文已添加 Rule-of-Three CI 但未考虑非独立性

**C4. 遗漏 Truong & Truong (2026) "Entropy Collapse"** [R2-N2, R1 AGREE with reservation]
- arXiv:2512.12381 证明 entropy collapse 是一阶相变，不存在 early-warning signals
- 论文大量借鉴 Scheffer et al. CSD 框架（§1-§2），隐含假设二阶相变
- 如果 model collapse 是一阶相变：(a) sharp onset 是理论预期而非发现；(b) CSD 类比失效；(c) 但 R1 指出 §4.5 intervention 是纯实证，不依赖二阶假设
- **影响**：理论框架需要实质性修正

**C5. T=20 关键边界验证未完成** [R1-N3, R2 交叉 AGREE]
- Appendix Table 26 已确认 4 个预测（α=0.50/0.60/0.75/1.0），但均为 trivial（强信号保持可检测、同步 dip 保持不可检测）
- 唯一非平凡预测——α=0.45 在 T=20 下是否仍不可检测——标注 "pending"
- S×R 框架（Contribution 2）的核心 predictive claim 悬而未决
- **影响**：S×R 的预测能力无法评估

### MAJOR（共识，显著影响评分）

**J1. S×R 是标准 power formula 重新包装** [R1-W1 + R2-N1 技术层面]
- Power(α,T)=Φ(S·R·√T/σ) 中 S·R 即标准化效应量 δ
- R(α) 非单调性有描述性价值（解释 synchronous dip），但不构成独立方法论贡献
- 建议重定位为 "interpretive lens" 而非 "theory"（论文标题已从 "theory" 改为 §3.1）

**J2. First-differencing 消除 canary→perplexity 的替代解释** [R1-W2, R2 partial REBUT]
- T=10 差分后仅 9 个有效值；perplexity 轨迹更平滑→差分后 SNR 更低
- 可能是 power loss 而非 genuine null
- R2 指出方法选择本身正确（避免 spurious regression），但真正问题是 T=10 根本限制
- Appendix R 有 channel effect size 比较但缺少 simulation validation
- 建议在匹配效应量的 DGP 下模拟 first-differencing 在 T=10 的保留功效

**J3. fp32/bf16 翻转削弱 R(α) robustness** [R1-W3, R2 AGREE]
- α=0.60 时 fp32 0/8 vs bf16 8/8——完全翻转
- Synchronous dip 是 S×R 非单调性的关键实证支撑，precision-dependent 意味着 R(α) 不是固有物理量
- 建议 fp32 多 seed 复现 + 讨论 bf16 stochastic rounding 影响

**J4. α_c bootstrap CI=[0.43, 0.56] 过宽** [R1-W4, R2 partial REBUT]
- 跨 13 个百分点，覆盖有效范围约四分之一
- R2 指出 CI 忠实反映离散 α 粒度——真正问题是 transition region 采样不够密集
- 建议在 α∈[0.40, 0.55] 做更密集采样 + 报告 sigmoid steepness 参数

**J5. 非均匀 seed 覆盖 + seed 依赖性** [R1-W5 + R2-W3, 强共识]
- 13 个 α 水平中多个仅 single seed
- α=0.10 blind spot：seed 42 (0/8) vs seed 43 (3/8) 翻转——单 seed 结论不可靠
- Pythia-1.4B: seed 42 (2/8) vs seed 43 (6/8)
- 87% headline 掩盖系统性架构依赖（SmolLM3-3B 3/8, entropy 0/4 ← canary metric splitting）
- 建议至少 α=0.10 和 α_c 附近补充 multi-seed

**J6. α_c vs CMR 关系未厘清** [R2-W1, R1 AGREE]
- α_c≈0.50 是检测方法灵敏度阈值还是 collapse 本身临界点？
- 与 Gu et al. (2024 CMR, 2025 data mixing) 的 critical mixture ratio 的定量关系未探讨
- 如果是同一 threshold 的不同观察角度，novelty 进一步降低

**J7. "Four methodological gaps" straw-man 倾向** [R2-W4, R1 partial REBUT]
- 四个 gap 被归于整个 model collapse 文献，但引用的 works 主要贡献是描述 collapse 现象而非 monitoring
- R1 指出 §1 原文限定为 "detection and monitoring analyses"，但读者可能理解为更广泛的批评
- 建议重述为 "four design choices in monitoring analyses"

### MINOR

- **L1.** Abstract ≥20 个数值，信息过载（R1+R2 共识）
- **L2.** §3.1 中 σ 未定义（residual SD vs signal SD）（R1）
- **L3.** Appendix N power simulation DGP 使用简单线性耦合，与实际非线性动态 mismatch（R1）
- **L4.** Figure 1 transition region 仅 3-4 个数据点（R2）
- **L5.** bib first author mismatch: `alemohammad2024mad`, `marcinkevics2022neural`（R2）

---

## Reviewer Consensus

以下关键问题两位 Reviewer 达成 **[AGREE]** 共识：

1. **Sharp onset = power threshold crossing, not new physical phenomenon**（C1）
2. **MMCT circularity**（C2）：FPR-inverse weighting + PermG dominance
3. **PermG FPR non-independence**（C3）：有效 N 远小于 24
4. **T=20 boundary pending**（C5）：唯一可证伪预测未验证
5. **S×R = standard power formula**（J1）
6. **fp32/bf16 flip**（J3）：削弱 R(α) robustness
7. **Seed coverage non-uniform**（J5）：聚合统计量掩盖条件间显著方差
8. **Cross-architecture heterogeneity understated**（J5 overlap）：87% headline 掩盖失败案例

---

## Reviewer Divergence

两处 partial REBUT，均为补充而非根本分歧：

1. **First-differencing**（J2）：R1 认为可能是 power loss；R2 认为方法选择正确但 T=10 是根本限制。本质上不矛盾——方法正确但 power 不足是同一问题的两面。Director 判定：**MAJOR**，建议 simulation validation。

2. **α_c CI width**（J4）：R1 批评 CI 过宽；R2 认为应批评实验设计粒度不足而非 bootstrap 本身。互补视角。Director 判定：**MAJOR**，建议 transition region 密集采样。

3. **"Four gaps" straw-man**（J7）：R1 partial REBUT，认为 §1 原文已限定范围。R2 坚持认为读者可能理解为更广泛批评。Director 判定：**MAJOR (mild)**，措辞调整即可解决。

---

## Questions

**Q1** (R1): MMCT 在等权重下的 consensus 结果是否改变？
**Q2** (R1): Null-control 下 seed 内 metric pair 的拒绝/不拒绝相关性是多少？
**Q3** (R1): First-differencing 在 T=10 下对已知 Granger link 的保留 power 是多少？
**Q4** (R1): α=0.60 的 fp32/bf16 翻转是否有多 seed 复现？
**Q5** (R1): Sigmoid steepness 参数及与 gradual onset 模型的拟合优度对比？
**Q6** (R1): 15% intervention threshold 是预设还是 post-hoc？

---

## Missing References

### Must-cite（CRITICAL）
1. **Truong & Truong (2026)** "Entropy Collapse" (arXiv:2512.12381) — entropy collapse 一阶相变，直接挑战 CSD 框架类比

### Should-cite（MAJOR/MINOR）
2. **Entropy Sentinel (arXiv:2601.09001, 2026)** — entropy-based monitoring 方法论关联
3. **Benjamini & Yekutieli (2001)** — FDR under arbitrary dependence (BY procedure)
4. **Donoho & Jin (2004)** — Higher criticism detectability boundary
5. **Breitung & Candelon (2006)** — Frequency-domain Granger causality for short series
6. **Lehmann & Romano (2005)** — Permutation test power theory (Ch. 15)

---

## External Review (Stanford Agentic Reviewer)

**状态：未返回（pending）**。外部审稿请求已于 2026-05-20T20:08 发送，尚未收到结果。如后续返回，建议 Research Director 将外部审稿发现与本报告对照。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 12 info）。主要发现：

**Warning:**
- Pages 4-5 连续 2 页纯文本（§3 Method → §4 Setup），无 display item，审稿人注意力可能流失。建议添加方法流程图或实验设置汇总表。
- 主文 8 页仅 4 个 display items（Figure 1-2 + Table 1-2），对实证论文偏少（推荐 5-8 个）。大量数据表在 Appendix，可能给审稿人"证据在附录里"的印象。

**Info（精选）:**
- Figure 1 regime 标签字号偏小，红-绿配色对色盲不友好
- Figure 2 单栏宽度多条曲线区分度有限
- Table 2 脚注约 6pt，包含重要注释但字号低于舒适阈值
- Figure 3 (power analysis) 和 Figure 4 (Shapley) 质量高，建议提一个到主文

---

## Overall Assessment

**评分: 3.0 — Findings（可被 Findings 接收）**

**置信度: 4/5**（两位 Reviewer 均从专长角度独立评估，交叉回应后高度一致）

**理由**：

实证发现有价值：sharp detection onset at α_c≈0.50、四 regime dose-response 结构、cross-architecture 验证（13/15 conditions）、canary intervention PoC。这些为 model collapse monitoring 提供了实用参考。

但主会议接收存在三个结构性障碍：
1. **方法论新颖性**：核心统计工具为计量经济学标准工具的直接迁移，"sharp onset" 是统计检验力穿越阈值的标准行为
2. **内部一致性**：MMCT 循环论证 + PermG FPR 非独立性 → 方法选择和方法评估的基石存疑
3. **未完成验证**：T=20 α=0.45 pending → S×R predictive claim 无法评估

作为 Findings 论文，实验覆盖面、null-control 设计、first-differencing scoping、统计处理规范性构成充分的贡献。

---

## Detailed Comments（逐节）

### Abstract
- ≥20 个数值过载，建议精简至 ≤10 个核心数字
- "Granger-causal detection" 首次出现应有脚注说明 Granger precedence ≠ true causation
- 建议删除 Fisher p=3.45×10^{-11} 等过度精确数值

### §1 Introduction
- "four methodological gaps" 建议改为 "four design choices absent from existing monitoring analyses"
- Figure 1 caption 应注明 forward-only direction
- 与 Truong & Truong (2026) 的关系需在此处或 §2 讨论

### §2 Related Work
- 对 Du et al. (2026 geometric) 的四点差异声明基本成立
- 遗漏 Truong & Truong (2026)、Entropy Sentinel
- 与 Gu et al. CMR 的讨论过于简略（仅 Extended Discussion 一句 future work）

### §3 Method
- MMCT 应重定位为 method disagreement diagnostic 而非 method ranking tool
- S×R 应明确承认与 z-test power formula 的关系
- σ 需定义

### §4 Experiments
- §4.2: PermG FPR CI 需考虑非独立性
- §4.3: 跨架构失败案例分析应从脚注升为完整段落
- §4.4: T=20 应完成 α=0.45 验证或降级 predictive claim
- §4.5: 15% threshold 需明确是预设/post-hoc + 更多 α 水平

### §5 Discussion
- 方法论诚实性好（明确 power curve crossing, not physical signal）
- 但这种诚实性与 title/abstract framing 存在张力
- fp32/bf16 翻转对 R(α) 的影响应在此处讨论

### Limitations
- 覆盖较充分
- 建议补充：MMCT 权重方案依赖性、PermG FPR 非独立性、CSD 框架适用性条件
