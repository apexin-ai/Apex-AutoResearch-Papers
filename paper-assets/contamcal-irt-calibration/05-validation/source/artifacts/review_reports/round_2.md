---
round: 2
overall_score: 2.5
timestamp: 2026-05-17T14:37:40.203027+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 3 审稿报告 — ContamCal: Calibrating Contaminated Benchmarks via IRT

**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Reviewers**: R1 (方法严谨性 + 实验有效性), R2 (新颖性 + 完整性 + 写作格式)
**流程**: Step 1 独立初审 → Step 2 交叉分享 (全文互传 + 逐条 [AGREE]/[REBUT]) → Step 3 收敛 → Step 4 汇总

---

## 1. Summary

ContamCal 提出通过 RRF 信号融合 + 2PL+γ IRT 模型对受污染 LLM benchmark 进行校准。核心实验发现是 IRT ability estimation 本身提供了主要校准收益（ARC MAE 降低 53%），独立于 contamination parameter γ 是否被建模。论文在 Qwen2.5 (0.5B/1.5B/3B) 和 Llama-3.2-3B 上进行 SFT 注入实验，覆盖 MMLU、ARC-Challenge、GSM8K 三个 benchmark。

论文自 Round 1/2 以来在叙事方面有改善（加入 "decomposition result" 语言、"exploratory" 标签、cross-family validation 数据），但 **8 个 critical issues 和 10+ 个 warning issues 仍然存在**，包括 title/framing 矛盾、格式不合规（desk reject 风险）、CI 覆盖报告不全、Oracle ablation 缺失等。两位 Reviewer 在所有关键问题上达成共识。

---

## 2. Strengths

**S1. 研究问题定位准确且有价值。** 桥接检测信号与计量理论校准框架的思路填补了真实空白。Introduction 对现有方法的定位清晰：检测方法止于 binary flags，IRT 方法忽略污染，DCR 缺乏 UQ。[R1, R2 一致]

**S2. 诚实报告负面结果。** 论文坦承 γ pooled 不显著、CI 覆盖不足（50% CI 仅 35% 实际覆盖）、GSM8K 过度矫正、Min-K%++ 方向性逆转。这种诚实在投稿论文中难能可贵，提升了论文的可信度。[R1, R2 一致]

**S3. Min-K%++ 方向性逆转发现有独立价值。** 在 0.5B 模型上 Cohen's d = -1.55 to -1.98（contaminated items 被判为更不可能 memorized），对从业者是重要警告。该发现独立于 ContamCal 框架本身有效。[R1, R2 一致]

**S4. Simulation identifiability boundary map 对社区有参考意义。** Figure 2 的 AUC × J heatmap 量化了"多少模型才够做 γ recovery"的问题，CI width ∝ J^{-0.48} 的经验律有实际指导价值。[R1, R2 一致]

**S5. Bayesian 推断流程规范。** NUTS sampling, split-R̂ < 1.01, bulk ESS > 400, PPP 检验, Fisher information 分析——推断流程标准且文档详尽。[R1, R2 一致]

---

## 3. Weaknesses

### 3.1 Must-Fix (Critical — 影响接收决定)

**C1. Title/Abstract 与核心发现根本矛盾 [R1-N1, R2-N1, 遗留 R2-N1 未修复]**
- Title "ContamCal: Calibrating Contaminated Benchmarks via IRT" 暗示 contamination-specific modeling 是关键贡献
- B3-Vanilla2PL(γ=0) 在 ARC MAE=0.016 优于 ContamCal 的 0.020（Table 4），MMLU/GSM8K 两者持平
- Abstract 首句仍写 "existing approaches stop at detection without quantifying how much scores are inflated"，暗示 ContamCal 解决了 quantification，但 γ 在 8/8 MMLU 域仅 1 个显著
- 自 Round 2 提出以来 **title 未改**，Contribution 1 措辞虽加了 "decomposition" 但仍 misleading
- **两位 Reviewer 三轮一致认定为 #1 must-fix**

**C2. ARR 格式不合规——Desk reject 风险 [R2-N2, 遗留 R2-N6 部分修复]**
- Limitations 位于 `\appendix` 中、`\bibliography{references}` 之后（main.tex L31-33）。ARR 要求 Limitations 作为独立 `\section*{Limitations}` 出现在 references 之前，不计入页数
- 全文无 Ethics Statement / Ethical Considerations section。ARR review form 明确评估 ethical concerns
- Figures 和 Appendix sections 已修复（Round 2 提出的部分问题已解决）
- **修复成本极低（<30 分钟）但不修复后果是 desk reject**

**C3. CI 覆盖率报告不完整，UQ claim 无法成立 [R1-N2, 遗留 R2-N2 未修复]**
- §4.3 列出 50%/80%/95% 三个 CI 级别作为评估指标
- §5.1 仅报告 50% level（~35% 实际覆盖），80% 和 95% 完全缺失
- 如果 50% CI 仅 35%，95% CI 可能仅约 70%，这使 "credible intervals" 作为方法优势的 claim 无法成立
- R1 在交叉回应中认同 R2-Q5 的假设：local independence violation 可能是 root cause（同一模型对相关 items 的 memorization patterns 相关）
- 自 Round 2 提出以来 **未修复**

**C4. Within-family ARC PPP 缺失，疑似隐藏 model misfit [R1-N3, 新发现]**
- Cross-family ARC PPP=0.45（Table 3，可接受）
- 但 Round 1 发现 within-family J=13 ARC PPP=0.003，§5.1 对此完全沉默
- §5.1 声称 "ARC passes gating"（MAE 降低 + γ CI excluding zero）但未报告 PPP
- 如果 PPP=0.003 仍然成立，ARC 的 γ 显著性可能是 model misfit artifact
- **新 critical issue，R2 在交叉中确认同意**

**C5. J=13 自证 underpowered，Contribution 4 逻辑矛盾 [R1-N4, 遗留 R2-N4 部分修复]**
- §3.4: reliable γ recovery 需要 J≥50；§5.3: 实际操作 J=13；8/8 MMLU 域仅 1 个 γ 显著
- 已加 "exploratory" 标签（部分修复）
- 但 Contribution 4 仍将 simulation-derived boundary（方法论贡献）和 empirical domain diagnosis（underpowered 探索）合并为单一 contribution——逻辑自相矛盾
- **两位 Reviewer 一致要求拆分 Contribution 4**

**C6. Oracle Exposure Ablation 缺失——零成本关键实验 [R1-N6, 遗留 R2-W2 升级为 critical]**
- Ground-truth injection labels（精确知道哪些 items 被注入）在手，但从未用作 oracle e_{ij}
- 零成本消融实验回答：如果信号完美 (AUC=1.0)，γ 在 J=13 下是否显著？
  - 若 oracle γ 仍不显著 → J 不足是唯一瓶颈，Stage 1 pipeline 无关
  - 若 oracle γ 显著 → RRF 信号质量是瓶颈，Stage 1 改进有方向
- 这直接决定 ContamCal 作为完整框架（Stage 1 + Stage 2）的存亡问题
- R2-Q1 "如果 detection 不重要，Stage 1 价值何在？为什么不直接推荐 vanilla 2PL？"指向同一核心
- 自 Round 2 提出以来 **未执行**，Round 3 R1 升级为 critical，R2 同意

**C7. Baseline 配置不一致，DCR 来源不明 [R1-N5, 新发现]**
- 主 Table 4: J=13 (1.5B+3B) 仅展示 B0/B3/ContamCal 三个方法
- 附录 Table 5: ARC 使用 J=8 (0.5B+1.5B) 不同配置
- 附录 Table 6: GSM8K 使用 0.5B only 配置，其中 B0-Raw MAE=0.003 而 ContamCal MAE=0.020（ContamCal 使校准恶化 6.7×）
- §4.4 称 DCR "qualitative comparison; no public implementation"，但附录给出精确 MAE 数字（0.245/0.263）。来源未交代
- §5.1 "overcorrection ratio is 11×"具体计算未说明
- **缺乏统一配置下的完整 baseline 比较，构成 cherry-picking 风险**

**C8. 贡献新颖性不足——PSN-IRT 直接竞争者未引用 [R2-N3, 新发现]**
- IRT for LLM evaluation 已有 TinyBenchmarks, Growing Pains, HiBayES, ATLAS, PSN-IRT 等
- PSN-IRT (Zhou et al., AAAI 2026) 在 bib 中 (`zhou_2025_psnirt`) 但从未 `\cite`——直接竞争者遗漏
- Contribution 1 "IRT calibration decomposition" 是 empirical observation 而非 method contribution
- Contribution 2 (RRF) 在实践中退化为 S1-only（§5.2 已承认但 Contribution 措辞未调整）
- R1 部分同意：novelty concern 真实但非 fatal，Contributions 3-4（signal failure + identifiability）有独立价值
- **R2 认为适合 Findings 或 short paper；R1 认为 Findings long paper 可接受**（评分分歧点）

### 3.2 Should-Fix (Warning — 影响评分但不一票否决)

**W1. 主表信息密度低——7 baselines 定义但仅展示 3 个 [R1, R2 一致]**
- 主 Table 4 仅 B0/B3/ContamCal。至少应加 B2 (Single2PL+γ) 和 B4 (LinearRegression) 以展示 IRT vs linear 对比

**W2. Related Work 过薄——3 段 ~40 行，33 citations，58 orphan bib entries [R1, R2 一致]**
- PSN-IRT, Kocyigit et al. (NeurIPS 2025), Schaeffer et al. (2026), Holland/Wainer (1993) DIF 均在 bib 中未 cite
- bib 中有重复条目（holland_1993_dif 和 holland1993dif）
- 33 citations 对 EMNLP long paper 偏少，需扩展至 40+

**W3. LoRA SFT ≠ pretraining contamination，生态效度讨论不足 [R1, R2 一致]**
- Introduction 以 pretraining contamination 为动机，但实验仅验证 SFT 场景
- 0.5B position bias (A-option 46%→98%) 可能是 SFT-specific artifact
- Limitations 仅一句 "Single injection protocol" 带过

**W4. Independent per-domain fitting 破坏 θ common scale [R1, R2 一致]**
- Table 2 STEM γ=+0.50 vs Social Sci γ=-0.57 的跨域 magnitude 比较在独立 fitting 下缺乏统计基础
- STEM 三域 (Math/Science/CS) γ 均为 +0.50 且 CI 几乎一致——疑似 prior 主导或共线性 artifact

**W5. Discussion (~10 行) 和 Conclusion (~5 行) 对 long paper 过短 [R2 提出, R1 部分同意]**
- 讨论内容散布在 §5 Results 各段落中，Discussion section 名义上过短
- 建议将讨论性段落（overcorrection 影响、γ 定位、方法适用边界）整合到 Discussion

**W6. GSM8K 11× overcorrection 无实践决策规则 [R1, R2 一致]**
- ContamCal 在已良好校准的数据上反而有害（GSM8K 0.5B: MAE 0.003→0.020）
- 缺乏"何时不应使用 ContamCal"的明确指导

**W7. Cross-family validation underpowered, Contribution 1 "validated" overclaims [R1, R2 一致]**
- Llama N=3-4 (single seed), GSM8K J=28 中 Llama 仅 14%
- "validated across two model families" 对 single-seed N=3-4 数据过强

**W8. RRF→S1-only, Contribution 2 措辞 overclaims [R1, R2 一致]**
- "Multi-signal exposure detection via RRF" 暗示多信号均有贡献，实际 S2/S4 在 0.5B 无效，1.5B+ 仅 marginal

**W9. Additive γ linearity 未经验证 [R1 提出]**
- 真实污染效应可能是 threshold-like，linear γ 可能被 averaged down 导致不显著

**W10. 46% 排除率缺乏 sensitivity analysis [R1, R2 一致]**
- Appendix C 加了排除细节（部分改善），但仍无 sensitivity analysis 说明排除对结论的影响

---

## 4. Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全一致：

| # | Issue | R1 | R2 | 共识 |
|---|-------|----|----|------|
| 1 | Title/framing 与核心发现矛盾 | N1 Critical | N1 Critical | **最高优先级修改** |
| 2 | ARR 格式不合规 (Limitations + Ethics) | 交叉确认 Critical | N2 Critical | **Desk reject 风险** |
| 3 | CI 覆盖仅报告 50% | N2 Critical | 隐含同意 | **UQ claim 不成立** |
| 4 | Oracle Exposure ablation 缺失 | N6 Critical | Q1 + 交叉确认 | **零成本关键实验** |
| 5 | J=13 自证 underpowered | N4 Critical | 隐含同意 | **Contribution 4 需拆分** |
| 6 | Baseline 配置不一致 | N5 Critical | W7 Warning | **统一配置必须** |
| 7 | PSN-IRT 未引用 | 交叉确认 | N3 内含 | **直接竞争者遗漏** |
| 8 | 主表仅 3/7 baselines | 交叉确认 | W1 Warning | **信息密度低** |
| 9 | Related Work 过薄 + orphan bib | 交叉确认 | W2 Warning | **需扩展** |
| 10 | LoRA SFT 生态效度不足 | W5 Warning | W3 Warning | **需扩展 Limitations** |

---

## 5. Reviewer Divergence [REBUT]

| # | Issue | R1 立场 | R2 立场 | 评估 |
|---|-------|---------|---------|------|
| 1 | Overall score | 3.0 (Findings) | 2.5 (Borderline Findings) | R1 认为格式问题不应影响科学价值评估；R2 认为格式问题是 desk reject 的现实风险且压低 excitement |
| 2 | Novelty 严重程度 | Warning (incremental but genuine) | Critical (insufficient for long paper) | R1 认为 Contributions 3-4 有独立价值支撑 Findings long paper；R2 认为主要 contributions (1-2) 价值不足 |
| 3 | Discussion 长度 | 部分同意 (内容存在但分散) | W4 (过短) | 不影响结论，属组织问题 |

**Director 判断**: 分歧不涉及核心技术判断，仅涉及严重性权重。格式问题确实构成 desk reject 风险（即使修复成本低），因此最终评分偏向 R2。

---

## 6. Questions (需要作者澄清)

**Q1.** Within-family ARC PPP 值具体是多少？如果 PPP < 0.05，如何解释 "ARC passes gating"？[R1-N3]

**Q2.** §5.1 "11× overcorrection ratio" 的具体计算来源？主表 ContamCal/B0-Raw 比值不等于 11×。[R1-Q2]

**Q3.** DCR MAE=0.245/0.263 如何获得？是自行实现、从原论文推算、还是在相同实验条件下重新运行？[R1-Q3]

**Q4.** 如果用 oracle exposure (ground-truth injection labels e_{ij}=dosage/100) 替代 RRF，γ 显著性、MAE、CI coverage 如何变化？[R1-Q4, R2-Q1]

**Q5.** Table 2 中 STEM 三域 γ 均为 +0.50 且 CI 几乎相同——是否 prior N(0,1) 在 J=13 下主导了 posterior？如果是，domain-level diagnosis 的信息量来自 data 还是 prior？[R2-Q2, R1 交叉确认]

**Q6.** Cross-family pooling (J=28 GSM8K) 中 θ scale identification 如何处理？Qwen 和 Llama 的 θ 是否在同一 scale 上？有无 linking 或 anchor 机制？[R1-Q5]

**Q7.** Qwen Δθ=+0.57 (d000→d100) 而 Llama Δθ≈+0.05。论文声称 "IRT absorbs contamination into θ"——如果 θ 已被 contamination inflate，Eq. 3 的 calibrated score 为何仍然 accurate？校准是 robust 还是 coincidence？[R2-Q4, R1 交叉回应提出 clean anchor 约束机制]

---

## 7. Missing References

**直接相关但未引用（在 bib 中）**:
- Zhou et al. PSN-IRT (AAAI 2026) — IRT for LLM evaluation，直接竞争者 [R2, R1 确认]
- Kocyigit et al. (NeurIPS 2025) — post-training 对 contamination detection 的影响 [R2]
- Schaeffer et al. (2026) — generative evaluation 中的 contamination [R2]
- Holland & Wainer (1993) DIF 专著 — DIF 理论基础（bib 中有两个重复条目）[R2, R1 确认]

**应考虑引用（可能不在 bib 中）**:
- Chalmers (2012) mirt R package — 多维 IRT 标准实现 [R1]
- Bock & Aitkin (1981) MML — IRT 参数估计经典方法 [R1]
- Kolen & Brennan (2014) Test Equating — θ scale linking 权威参考 [R1]
- Yang et al. (EMNLP Findings 2024) — inference-time decontamination [R2]
- Zhang et al. (ICML 2025) — decontamination [R2]

**工程问题**: 91 bib entries 仅 cite 33，58 个 orphan entries 需清理。

---

## 8. Overall Assessment

**综合评分: 2.5 / 5 (Borderline Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0 | 3.0 | **3.0** |
| Excitement | 3.0 | 2.5 | **2.5** |
| Reproducibility | 3.5 | 3.5 | **3.5** |
| Overall | 3.0 | 2.5 | **2.5** |
| Confidence | 4/5 | 4/5 | **4/5** |

**评分理由**:

论文提出了一个有意义的研究问题，"IRT alone suffices for calibration" 是一个 clean empirical finding。诚实报告负面结果值得肯定。Min-K%++ 方向性逆转和 identifiability boundary map 有独立社区价值。

但以下结构性问题阻止更高评分：

1. **Framing 失调 (三轮未修复)**：Title 和核心 contributions 仍暗示 contamination-specific calibration 是贡献，但实验反驳了这一叙事。这不是 cosmetic 问题——审稿人在 30 秒内就会发现 title 与 Table 4 的矛盾。

2. **格式 desk reject 风险**：Limitations 位置错误 + Ethics 缺失。修复成本极低但当前状态会被直接退回。

3. **统计证据链断裂**：CI coverage 报告不全（UQ claim 无法验证）、ARC PPP 隐藏（gating claim 可疑）、Oracle ablation 未做（Stage 1 价值未证明）。这三个问题形成连锁反应——如果 CI 不准、model misfit、且信号质量未经 oracle 验证，整个框架的可信度受损。

4. **自证 underpowered**：论文自己的 simulation 证明 J≥50 才够，但在 J=13 下操作，8/8 MMLU 域仅 1 个 γ 显著。

5. **新颖性边界**：PSN-IRT 未引用，Contribution 1 是 empirical observation，Contribution 2 实际退化为 S1-only。

**提升路径**：
- 修复 C1 (retitle/reframe) + C2 (format) + C3 (full CI coverage) + C6 (oracle ablation) → 可达 3.0 (Findings)
- 额外修复 C4 (ARC PPP) + C5 (split Contribution 4) + C7 (unified baselines) + C8 (cite PSN-IRT) → 可达 3.5 (Borderline Conference)
- 根本性改善需要 J≥30 的实验数据，超出当前 deadline 可行范围

---

## 9. Detailed Comments by Section

### Title
- 必须改。"ContamCal" 暗示 contamination-aware calibration 是贡献，但核心发现是 vanilla IRT 已够用。建议："IRT-Based Calibration of Contaminated LLM Benchmarks: Ability Estimation Suffices" 或 "When IRT Alone Suffices: Decomposing Calibration and Contamination in LLM Benchmarks"

### Abstract
- 首句 "existing approaches stop at detection without quantifying how much scores are inflated" → 暗示 ContamCal 做到了 quantification，但 γ 在多数情况下不显著
- "Social Sciences reaching significance (γ = -0.57, CI excluding zero)" → 在 8 个独立检验中仅 1 个显著，未做多重比较校正（Bonferroni α=0.00625 下可能不再显著）
- 建议 Abstract 第 3 句明确写出 "γ does not improve calibration beyond vanilla IRT"

### Introduction (§1)
- 段落结构清晰，5 段叙事线完整
- Contribution 1 "validated across two model families" → 对 single-seed Llama N=3-4 overclaims
- Contribution 4 混合 simulation boundary + empirical diagnosis → 应拆分

### Related Work (§2)
- 仅 3 段 ~40 行对 EMNLP long paper过薄
- 缺少 PSN-IRT (bib 中有!)、DIF 文献 (Holland & Wainer)、Kocyigit et al.
- "Calibration disambiguation" 段落有价值但可以更深入
- 建议增加 DIF 段落（ContamCal 的 γ 本质上是 explanatory DIF）

### Method (§3)
- 技术上 sound，Bayesian 设置标准
- Eq. 4 additive γ linearity 未经验证——如果污染效应是 threshold-like，linear γ 会被 diluted
- §3.1 三个 adaptations 组织清晰
- §3.5 calibration value decomposition 是论文的理论亮点，应更突出

### Experimental Setup (§4)
- LoRA 参数详尽 (α=32, r=16, lr=5e-5)
- 排除理由在 Appendix C 中可见但属工程错误非设计选择，缺 sensitivity analysis
- "GSM8K retains all scales" 与主表 J=13 配置的关系需要澄清

### Results (§5)
- Table 4 清楚展示 decomposition 结果
- 但缺失关键信息：within-family ARC PPP, 80%/95% CI coverage
- §5.1 "11×" overcorrection 出处不明
- §5.4 STEM 三域 γ=+0.50 完全相同——需要解释
- Figure 1-4 均存在且 self-contained

### Discussion (§6)
- 仅 ~11 行，实质讨论散布在 §5 中
- 缺少：方法何时不应使用（GSM8K case）、additive linearity limitation、ARC misfit implications
- "Scaling to J≥50" 作为 future work 合理但回避了当前 J=13 的核心矛盾

### Appendix
- Limitations 位置必须移到 references 前
- Appendix C (exclusion details) 有价值
- Tables 5-6 使用不同配置引起混乱
- 需要增加 Ethics Statement

---

## 10. Round 1-2 遗留 Issues 修复状态总结

| Issue ID | Summary | Round 2 Status | Round 3 Status | 修复程度 |
|----------|---------|----------------|----------------|----------|
| R2-N1 | γ 无校准收益 framing | open | open | 部分改善（加 decomposition 语言）但 title 未改 |
| R2-N2 | CI 覆盖 | open | open | **未修复** |
| R2-N3 | 46% 排除率 | open | open | 部分改善（加 Appendix C），无 sensitivity |
| R2-N4 | J=13 vs J≥50 | open | open | 部分改善（加 exploratory 标签） |
| R2-N5 | DCR 比较 | open | open | 部分改善（有数字），来源不明 |
| R2-N6 | 格式不合规 | open | open | 部分修复（Figures/Appendix 加了），Limitations 位置+Ethics 仍错 |
| R2-W1 | RRF→S1 | open | open | §5.2 承认但 Contribution 未调整 |
| R2-W2 | Oracle ablation | open | open → **critical** | **未修复**，升级 |
| R2-W5 | 主表不完整 | open | open | **未修复** |
| R2-W7 | GSM8K 过校正 | open | open | **未修复** |
| R2-W8 | Related Work 缺引用 | open | open | 微量改善（33 vs 30），核心遗漏仍在 |
| R1-C2 | Cross-family N 不足 | in_progress | open | 加了 exploratory + power ref，但 Contribution 1 overclaims |
| R1-W2 | 叙事转向 | in_progress | open | Subsumed by R2-N1 |
| R1-W3 | IRT 新颖性 | in_progress | open | 升级为 R3-N7 (PSN-IRT 未引用) |
| R1-A1 | ARC PPP | in_progress | open | 升级为 R3-N3 |

**总结**: 15 个追踪的 open issues 中，0 个完全修复，6 个部分改善，9 个未修复。3 个新 critical issues 在 Round 3 发现（ARC PPP 隐藏、baseline 配置不一致、PSN-IRT 未引用）。

---

## Issue Tracker 已同步

所有 Round 3 发现已写入 `projects/contamcal-irt-calibration/artifacts/review_issues.yaml`，包括新发现 R3-N3, R3-N5, R3-N7, R3-W10, R3-W11, R3-W12，以及对所有遗留 issues 的 Round 3 status 更新。