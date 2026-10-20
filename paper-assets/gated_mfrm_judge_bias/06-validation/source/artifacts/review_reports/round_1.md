---
round: 1
review_mode: fresh
overall_score: 1.5 - Resubmit after next cycle
timestamp: 2026-05-22T16:41:11.341520+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Fair Scores via Joint Calibration (G-MFRM)

**项目**: gated_mfrm_judge_bias
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**截止日期**: 2026-05-26
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性 / R2: 新颖性与完整性）
**交叉讨论**: 1 轮，共识收敛

---

## Summary

本文提出 Gated Many-Facet Rasch Model (G-MFRM)，通过在 MFRM 线性预测器中引入乘法门控项 $c_n \cdot e_i$ 联合建模 LLM 评估中的 judge bias 和 benchmark contamination。论文将两类偏差的交互形式化为 omitted variable bias (OVB) 问题（Section 2），提出三阶段估计方法并给出 identifiability 分析和 error propagation bounds（Section 3）。**然而，论文严重不完整：Section 4 (Experiments)、Section 6 (Conclusion)、Limitations 三个核心章节完全为空**，Abstract 和 Introduction 中的定量声明（43.8% RMSE reduction、τ=0.922）无独立实验章节支撑，多处交叉引用断裂（Figure ??、Table ??），Introduction Contribution 4 标注 "numbers TBD"。

---

## Strengths

**S1. 问题定位有洞察力 [R1 ✓, R2 ✓]**
将 judge bias 和 contamination 的交互识别为 OVB 问题是新的 problem identification。Section 2 清晰展示了 sequential estimation（无论 bias-first 还是 contamination-first）的结构性失败模式：lenient judges 放大 exposed items 的分数膨胀，strict judges 压缩之，产生系统性非正交依赖。Figure 1 的 synthetic validation（r=0.86, p<0.001）直观有力。

**S2. Identifiability 分析方向正确 [R1 ✓, R2 ✓]**
Proposition 1（No New Indeterminacy）→ Proposition 2（Exposure Variation Necessary）→ Theorem 1（Sufficient Conditions）构成完整的识别性论证链。Fisher information determinant 的 Cauchy-Schwarz 论证思路正确。

**S3. Error propagation 的 σ_crit 阈值有实用价值 [R1 ✓, R2 ✓]**
$\sigma_{\mathrm{crit}} = \sqrt{\mathrm{Var}(e_i)}$ 为实践者提供了判断 Stage 2 exposure 估计质量是否足够的定量工具，使 staged approximation 具有可证伪性。

**S4. 三阶段估计策略设计合理 [R1 ✓, R2 ✓]**
将 bilinear product 的识别问题通过 staged estimation 解决——先外部固定 $e_i$ 再联合估计其余参数——是规避根本性不可识别问题的实用方案。

**S5. Horseshoe prior 选择得当 [R1 ✓, R2 ✓]**
Contamination 在模型群体中应当是稀疏的，regularized horseshoe 的 adaptive shrinkage 比 Lasso 或 spike-and-slab 更适合这种稀疏结构。

---

## Weaknesses

### Fatal / Must-Fix

**W1 [Critical, R1+R2 共识]: 论文严重不完整——Experiments/Conclusion/Limitations 三章为空**
- Section 4 仅含占位注释 `%% [Phase 2: to be written after exp-001 through exp-005 complete]`
- Section 6 (Conclusion) 和 Limitations 同为占位注释
- Abstract 声称的 43.8% RMSE reduction 和 τ=0.922 无独立实验表格/图表支撑
- Introduction Contribution 4 标注 "numbers TBD"
- **Limitations 缺失违反 ARR mandatory section 要求，可构成 desk rejection**
- 全文仅 1 个 figure、0 个 table，实际内容约 6 页

**W2 [Critical, R1 提出, R2 同意]: OVB 公式从线性到非线性模型的迁移缺乏严格论证**
- Observation 1（Eq. 3）直接将 Angrist & Pischke (2009) 线性 OVB 公式应用于 ordinal logistic MFRM
- 论文自身承认 "In the linear analogue"（§2），但 formal statement 未限定为近似
- 非线性模型中 OVB 的方向和量级依赖参数真值，存在 collider bias 等额外效应
- 需要：(1) 在 Observation 1 中明确标注线性近似限定，(2) 引用 Wooldridge (2010) §15.8，(3) simulation 验证近似精度

**W3 [Critical, R1 提出, R2 同意]: Theorem 1 仅为 proof sketch，缺乏完整证明**
- Fisher information weights $w_{nij}$ 未显式定义
- $b_i$/$d_j$ 子块仅声称 "inherit from standard MFRM" 而无推导——G-MFRM 加入 $c_n \cdot e_i$ 后子块结构已变
- Cross-block coupling（$\theta_n$ 与 $c_n$ 之间的 off-diagonal blocks）未讨论
- 论文声称 "formal identifiability guarantees" 但仅提供 sketch，不匹配

**W4 [Critical, R1+R2 共识]: 断裂的交叉引用和 TBD 占位符**
- §3.4 引用 "Figure ?? and Table ??" 指向不存在的图表
- Introduction Contribution 4 含 `%% [Phase 2: numbers TBD]`
- 表明论文未经完整编译检查，处于草稿状态

### Major

**W5 [Major, R1 提出, R2 同意]: Error propagation 的 i.i.d. Gaussian 噪声假设过强**
- 异方差性：$e_i$ 接近 0/1 时误差分布与中间值处不同
- 非独立性：Stage 2 使用 response data 统计量，$\epsilon_i$ 与 Stage 3 参数不完全独立
- 非正态性：clip 到 [0,1] 后误差分布非对称
- Eq. 7 attenuation factor 的实际精度存疑

**W6 [Major, R1 提出, R2 同意]: Stage 2 exposure estimation 设计决策缺乏论证**
- 75/25 权重（anchoring vs. agreement）无 sensitivity analysis
- Reference model（gpt-4-0314）如自身有 contamination 会引入 circular dependency
- Clipping to [0,1] 引入 bias，与 §3.4 unbiased noise 假设矛盾
- 作为 identifiability 完全依赖的环节，细节严重不足

**W7 [Major, R1+R2 共识]: G-MFRM 相对 DG-IRT 的增量贡献需消融实验量化**
- 三个声称差异中：(1) continuous→binary 是自然扩展，(2) 加 $d_j$ 是 MFRM 标准做法
- 实质创新在 (3) external estimation + identifiability 分析
- 需消融实验：binary vs. continuous gating、with/without $d_j$、joint vs. staged

**W8 [Major, R1 提出, R2 同意]: MCMC 收敛标准偏宽松**
- $\hat{R} < 1.05$ 是旧标准，Vehtari et al. (2021) 推荐 $\hat{R} < 1.01$ + rank-normalized split-$\hat{R}$
- ESS > 200 对 posterior quantiles 不够，horseshoe prior 的 heavy-tailed 参数可能遗漏尾部不收敛
- 仅在 footnote 中报告了一组 synthetic data 的收敛指标

**W9 [Major, R2 提出, R1 部分同意]: Related Work 遗漏 contamination avoidance 范式**
- LiveBench、SEAL、TRUCE 代表一类完全不同的应对方法（从源头避免 contamination）
- 论文仅讨论 post-hoc detection/correction，应解释为什么 post-hoc modeling 仍然必要

**W10 [Major, R2 提出, R1 部分同意]: OVB 作为 Contribution 1 的贡献层次需校准**
- 作者自认 "direct application of the classical OVB result"（§2）
- R1 认为 problem identification 本身有价值，listing as Contribution 1 合理，但需更严格论证（与 W2 关联）
- R2 认为应重新定位为 motivation 而非 contribution
- **共识**：OVB 的 problem identification 有价值，但 formal statement 需限定为近似

### Minor

**W11 [Minor, R1]: Theorem 1 条件 (iii) 和 (iv) 逻辑冗余**
- $|\{e_i\}| \geq 2$ 在 fully crossed design 下蕴含 $\mathrm{Var}(e_i) > 0$

**W12 [Minor, R1]: $c_n \geq 0$ 约束排除负向 contamination**
- 假设 contamination 只提升分数，但存在反例（记忆旧版答案等）
- 应在 Limitations 中讨论

**W13 [Minor, R2]: 遗漏近期 IRT+LLM 相关工作**
- Choi et al. (2026) "Diagnosing the Reliability of LLM-as-a-Judge via IRT" (arXiv:2602.00521)
- Polo et al. (2024) tinyBenchmarks (ICML 2024)
- R1 认为 Polo et al. 与本文 framing 不直接相关，可选引用

---

## Reviewer Consensus

**完全共识（[AGREE]）**：
1. 三个空章节是 fatal flaw，论文不可评审（W1）
2. Overall 1.5（Resubmit after next cycle）
3. 理论框架有潜力，问题定位精准（S1-S5）
4. Stage 2 是方法论的薄弱环节（W6）
5. DG-IRT 增量贡献需消融实验（W7）
6. Reproducibility 极低（1/5）
7. 缺 Limitations 可构成 ARR desk rejection（W1）
8. OVB 非线性迁移需严格论证（W2）
9. Theorem 1 需完整证明（W3）

## Reviewer Divergence

**轻微分歧**（不影响整体判断）：

1. **OVB 贡献定位**（W10）：R1 认为作为 Contribution 1 在 problem identification 层面合理，R2 认为应定位为 motivation。共识：无论定位如何，formal statement 需限定为线性近似。

2. **Missing references 严重程度**（W13）：R1 认为遗漏个别论文（tinyBenchmarks）不构成 major weakness，建议降为 minor；R2 维持 major。共识：contamination avoidance 范式（W9）确需讨论，个别 IRT 论文可选。

---

## Questions（需作者澄清）

**Q1**: Observation 1 的 OVB 公式在 MFRM（ordinal logistic model）中的精确适用条件是什么？是否验证过该线性近似在典型 MFRM 参数范围内的误差？

**Q2**: Theorem 1 的完整证明是否可用？特别是完整 Fisher information matrix 的非奇异性如何从各子块推出？Cross-block coupling 如何处理？

**Q3**: Stage 2 的 75/25 权重如何确定？不同权重比例（50/50、90/10）的 sensitivity analysis 结果如何？如果 reference model 本身被 contaminate 会怎样？

**Q4**: Horseshoe prior 超参数（$\tau_c$, $c^2_{\mathrm{slab}}$）的 sensitivity analysis？在 contamination 比例不同（0% vs. 50%）的场景下 prior 行为是否稳定？

**Q5**: 论文引用的 exp-012 synthetic results 的完整实验设定（DGP 参数、随机种子数、baseline 细节）在哪里？

**Q6**: Murphy-Topel variance correction 的具体推导及对 CI coverage 的影响？

**Q7**: MCMC 计算成本如何？50 models × 1000 items × 10 judges 的收敛时间？horseshoe prior 的 funnel geometry 是否导致 NUTS 步长适应困难？

**Q8**: 如果 human annotators 自身有 bias（如 Chatbot Arena ELO），G-MFRM 与 human ranking 的对齐度高不一定意味着校正正确——如何界定 ground truth？

---

## Missing References

1. **Vehtari, Gelman, Simpson, Carpenter & Bürkner (2021)** — "Rank-normalization, folding, and localization: An improved R̂"：当代 MCMC 收敛诊断标准
2. **Wooldridge (2010)** — *Econometric Analysis of Cross Section and Panel Data* §15.8：非线性模型中 OVB 讨论
3. **LiveBench (White et al., 2024)** — contamination avoidance 范式代表（ICLR 2025 Spotlight）
4. **TRUCE (Rajore et al., 2024)** — private benchmarking 防止 contamination
5. **SEAL (Scale AI, 2024)** — private benchmark leaderboard
6. **Choi et al. (2026)** — "Diagnosing the Reliability of LLM-as-a-Judge via IRT" (arXiv:2602.00521)

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成

视觉审查 Agent 发现 3 critical / 4 warning / 3 info：

**Critical findings**:
- 多处未解析 LaTeX 交叉引用（"Figure ??"、"Table ??"），页 2 和页 6 可见
- 文中引用的 Figure 和 Table 在 PDF 中完全缺失（全文仅 Figure 1，零 Table）
- 整篇 8 页论文仅 1 个 figure、0 个 table——实验结果全靠行内数字传达

**Warning findings**:
- 前 3 页连续纯文本无视觉锚点，审稿人前 2 分钟内只看到密集文字
- 页 5-7 连续 3 页无 figure/table
- Section 4 "Experiments" 仅约半页篇幅无任何结果表或图
- 末页仅 ~35-40% 填充（全为 references），空间利用率低

**Info findings**:
- Figure 1 散点图质量可接受（分辨率清晰、axis label 可读）
- 数学公式渲染正确，Observation/Proposition/Theorem 排版规范
- References 格式统一，无 [?] 未解析引用

---

## Overall Assessment

### 评分: 1.5 — Resubmit after next cycle

**R1**: 1.5 (Confidence 4/5)
**R2**: 1.5 (Confidence 4/5)

### 维度评分汇总

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 2.5/5 | 2/5 | 2/5 — 理论框架有骨架但三处关键论证不完整（W2/W3/W5），实验完全缺失 |
| Excitement | 3/5 | 3/5 | 3/5 — 问题定位有价值，但 novelty 为增量式组合 |
| Reproducibility | 1/5 | 1/5 | 1/5 — 无实验、无代码、无数据、Stage 2 细节模糊 |

### 判断理由

**给 1.5 而非 2 的原因**：2 分意味着"需大幅修改，可在下一周期完成"。但本文的问题不仅是缺少实验——即使补上实验，还需要：(1) OVB 非线性论证或 simulation-based validation（W2），(2) Theorem 1 完整证明（W3），(3) Stage 2 exposure estimation 的 sensitivity analysis（W6），(4) 消融实验（W7）。这些理论和实验工作的总量可能超出一个 ARR cycle。

**给 1.5 而非 1 的原因**：论文的核心 framing（OVB in joint measurement）是有价值的 problem identification，identifiability 分析的方向正确，staged estimation 设计逻辑合理。这不是需要"完全重做"的论文，而是需要完成和加强的论文。

### 投稿就绪度

**当前状态不适合提交到 EMNLP 2026 ARR May cycle。** 距 deadline 4 天，即使假设实验代码已完成，补全 Experiments + Conclusion + Limitations + 修复交叉引用 + 确保格式合规的工作量不现实。更重要的是，W2（OVB 非线性论证）和 W3（Theorem 1 完整证明）需要实质性理论工作，不是写作时间问题。

### 提升路径

如果论文在未来版本中补全以下内容，评分有潜力提升至 **3.0-3.5（Findings / Borderline Conference）**：
1. 完整 Experiments section（合成 + 真实数据 + 消融实验）
2. Observation 1 在非线性设定下的严格论证或 simulation validation
3. Theorem 1 完整证明（Appendix）
4. Stage 2 exposure estimation 的 sensitivity analysis
5. Conclusion 和 Limitations sections
6. Related Work 补充 contamination avoidance 范式
7. MCMC 收敛标准更新至 Vehtari et al. (2021)

---

## Detailed Comments

### Section 1 (Introduction)
- Contribution 1-3 的理论声明有对应内容支撑（§2-§3），但 Contribution 4（Arena-Hard real-data validation）对应章节为空
- "numbers TBD" 占位符必须在投稿前移除
- 建议在 OVB formalization（Contribution 1）中明确标注为近似结果

### Section 2 (Confounding in LLM Evaluation)
- Observation 1 的 OVB 论证逻辑正确但形式化不严格——plim 公式在 ordinal logistic 模型中仅为近似（W2）
- Figure 1 是全文唯一图表，质量可接受但 caption 可更自包含
- Synthetic validation（r=0.86）有说服力，但实验设定（N=50, I=100, J=8, ρ=0.6, 20 seeds）仅在文中简述

### Section 3 (The G-MFRM Framework)
- §3.1 Model Specification：horseshoe prior 选择合理，与 DG-IRT 对比定位清晰
- §3.2 Staged Estimation：Stage 2 描述过于模糊——reference model 选择标准、75/25 权重理由、cross-model agreement 计算方式均未详述（W6）
- §3.3 Identifiability：Proposition 1-2 证明完备，Theorem 1 仅为 sketch（W3）。条件 (iii)+(iv) 冗余（W11）
- §3.4 Error Propagation：attenuation factor 推导正确但假设过强（W5）。Murphy-Topel correction 仅一句话提及
- §3.5 Fair Scores：概念清晰但无实验验证

### Section 4 (Experiments)
- **完全为空**。这是论文最致命的缺陷。

### Section 5 (Related Work)
- 四个段落（Judge Bias / Contamination Detection / Preference Leakage / IRT+MFRM）覆盖较广
- 遗漏 contamination avoidance 范式（W9）和部分近期 IRT+LLM 工作（W13）
- Preference leakage 段落的讨论有价值——指出 G-MFRM 的 $d_j$ 可部分捕捉但不完全覆盖

### Section 6 (Conclusion) & Limitations
- **完全为空**。Limitations 缺失违反 ARR 规定。
