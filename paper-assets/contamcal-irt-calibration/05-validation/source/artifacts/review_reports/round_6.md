---
round: 6
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T07:45:55.047849+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 8 (Fresh Review)

**论文**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families
**目标 Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**审稿模式**: 重新审稿 (fresh)
**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计+统计声明; R2: 新颖性+Related Work+写作+格式)
**审稿轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识后收敛

---

## Summary

本文通过控制 SFT 注入（LoRA, 5 个剂量水平）对来自 4 个独立模型家族的 5 个模型（7B–14.7B）进行 benchmark 污染实验，发现污染产生了四种质性不同的剂量-响应模式（Immune / Collapse / V-Recovery / Benefit），而非通常假设的统一膨胀效应。论文使用 ContamCal——一个结合多信号 RRF 融合与污染增强 IRT (2PL+γ) 的两阶段管线——对结果进行统计表征。DiD 分析显示无 item-specific 记忆化证据，跨 benchmark 传递揭示了方向反转现象。

---

## Strengths

1. **概念新颖性强**：将 benchmark 污染建模为连续剂量-效应关系并建立 dose-response 分类是真正的新视角。"contamination ≠ inflation" 直接挑战社区普遍假设，对 benchmark 设计者和模型评估实践者有实际指导意义。[R1, R2 共识]

2. **实验设计是该领域的方法论升级**：控制 SFT 注入提供已知 ground truth 的因果推断基础，跨 4 家族 × 3 benchmark × 5 剂量 × 3 seeds 的矩阵设计在 contamination 研究中罕见。[R1, R2 共识]

3. **DiD + 跨 benchmark 证据链构成相互佐证**：Contribution 2（global modulation）是论文最强贡献——DiD 在所有家族的 treated/untreated items 上均为非显著，跨 benchmark 方向反转（Qwen-7B: MMLU −1.8pp vs GSM8K +10.1pp）进一步证明效应是全局性的。[R1, R2 共识]

4. **Appendix 详尽**：18 个 appendix sections 覆盖 identifiability simulation、DGP robustness、prior sensitivity、convergence diagnostics、classification sensitivity 等，表明作者对方法论细节的严肃态度。[R1, R2 共识]

5. **IRT 整合技术上合理**：将 contamination detection signals 作为连续协变量融入 explanatory IRT（2PL+γ）是自然的建模选择，per-benchmark fitting + domain-level γ_d 提供了实用的诊断粒度。[R1, R2 共识]

6. **多 baseline 比较**：7 个 baseline 方法（raw accuracy、remove-and-rescore、vanilla IRT、linear regression、Emperor、DCR、ContamCal variants）提供了较全面的参照。[R1]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1** [critical, R1-N1 + R2-W3, 共识] **Cross-seed stability 声明与 n=3 样本量不匹配**

n=3 seeds 下方差估计的置信区间极宽。Table 3 显示 strict sign consistency 仅 2/5 families 通过；论文通过放宽为 "taxonomy-level consistency"（CI-based aggregation rule）达到 4/5，但这一放宽本身降低了分类精度。核心贡献（dose-response taxonomy）的统计基础不充分。

→ 建议：(a) 对 ≤3B 模型增加 seeds 至 n≥5（LoRA SFT 成本可控）；(b) 报告 cross-seed bootstrap CI；(c) 至少将 claim 弱化为 "preliminary taxonomy under limited replication"。

**W2** [critical, R1-N3 + R2-W2, 共识] **DiD null result 缺乏 power analysis，"causal evidence" 声明不成立**

DiD 值范围 −0.8 到 +0.6pp，在当前样本量下检测 ~1pp item-specific 效应的 statistical power 未知。Abstract/Intro 将 "All DiD non-significant" 升级为 "causal evidence that contamination operates through global capability modulation rather than item-specific memorization"，这是 absence-of-evidence ≠ evidence-of-absence 错误。Figure 2 的 symmetry 声明依赖视觉判断而非正式检验。

→ 建议：(a) 做 post-hoc power analysis 报告 MDES；(b) 弱化为 "we find no evidence of item-specific memorization at the current power level"。

**W3** [critical, R2-N1, R1 同意] **N=4 模型族支撑 4 类分类学，泛化性证据不足**

4 个家族恰好观测到 4 种模式，Table 1 中每种模式恰好对应一个家族（Phi-4→Immune, Qwen-14B→Collapse, Qwen-7B→V-Recovery, Gemma-2→Benefit），存在 overfitting-to-sample 风险。Algorithm 1 的 pattern 枚举从这 4 个家族归纳，无法排除第 5 种 pattern。R1 补充指出 Benefit 实际出现在 2 个家族（Gemma-2 + OLMo-2），减轻了 one-to-one 担忧，但核心论点成立。

→ 建议：(a) 增加 1-2 个模型族快速验证（LLaMA-3/Mistral，哪怕仅 1-2 个剂量水平）；(b) 若资源受限，将 "taxonomy" 改为 "observed response profiles"，并在 Discussion 中分析模型属性与 pattern 的潜在关联。

**W4** [critical, R2-N2, R1 带条件同意] **与 Han et al. (2026) 的差异化论证不充分**

Han et al. (2026, EACL Findings) 是最直接的在先工作（DIF 应用于 LLM 污染），当前仅 2 句话区分。未讨论：(1) continuous vs binary exposure 的实际效果差异；(2) 在 Stage 1 信号有噪声时 continuous 是否优于 binary；(3) 何时 group-based DIF 更稳健。R1 同意需要加强论证但反对将 Han et al. 实现为 baseline（两种方法输出类型不同，不直接可比）。

→ 建议：在 Method 或 Related Work 中增加 ~0.5 页详细方法论对比（假设差异、输入要求、输出粒度、适用范围）。

### Should-Fix（影响评分但不一票否决）

**W5** [warning, R2-W1 + R1 同意, 视觉审查确认] **正文疑似超过 8 页限制**

Section 6 (Discussion and Conclusion) 从 p.8 底部延伸至 p.9，正文估计约 8.4-8.5 页。EMNLP 2026 正文限 8 页（Limitations/Ethics 不计入）。**存在 desk-reject 风险。** 视觉审查 Agent 独立确认："Section 6 正文内容已超出第 8 页"。Section 6 的多个小标题段落内容与 §5 findings 重叠。

→ 建议：大幅压缩 Section 6，移重叠内容至 Appendix，确保 Section 6 结束于 p.8 内。

**W6** [warning, R1-W4 + R2 同意] **Bayesian 和 frequentist 术语混用**

论文使用 Bayesian MCMC (Stan/NUTS) 做 IRT 推断，但多处使用 "significant" "p-value" 等 frequentist 术语。DiD 分析 (Table 4) 的 "p > .05; ns" 似乎是 frequentist t-test，但与 Bayesian IRT 框架未明确区分。PPP 与 frequentist p-value 混淆。

→ 建议：统一为 "credible interval"（Bayesian）vs "confidence interval"（frequentist），明确标注每个检验的框架。

**W7** [warning, R1-W1 + R2 同意] **RRF fusion 缺乏 calibration 验证**

未报告 (1) RRF score 与真实 contamination 程度的校准关系；(2) S1-S4 间的 rank correlation；(3) leave-one-signal-out 消融。§5.4 的 random-subset MAE 比较（0.039±0.008 vs 0.006）间接验证了 RRF item selection 的价值，但非 exposure score 本身的校准性。

→ 建议：报告 signal rank correlation 和 leave-one-signal-out 消融。

**W8** [warning, R1-N2 子论点, R2 同意降级] **Identifiability simulation 用 uniform exposure，与实际 skewed 分布不匹配**

Appendix D 的 identifiability simulation 使用 uniform exposure 分布，但实际 RRF exposure 高度右偏（mean=0.041, median=0.016）。少数高 exposure items 可能产生 leverage effect 驱动 γ 估计。R2 指出 J=13-16 在 Linear DGP 下 coverage ≥0.93（不在边界上），但 skewed exposure gap 是真实缺陷。

→ 建议：在 simulation 中增加 skewed exposure 条件验证。

**W9** [warning, R2-W4, R1 部分同意] **Algorithm 1 阈值 sensitivity 报告过粗**

Appendix K Table 9 仅报告 30/30 pass/fail，缺乏 sensitivity curve 展示分类如何随阈值连续变化。R1 认为严重程度低于 R2 评估（direction 是 primary criterion，阈值仅影响边缘 case），但添加 sensitivity heatmap 是低成本改善。

→ 建议：在 Appendix 增加 τ × σ 分类一致性 heatmap。

### Minor（不影响接收）

- **M1**: "pp" (percentage points) 在 Abstract 首次使用时未定义 [R2]
- **M2**: Gemma-2 GSM8K 排除在 §5.2 出现突然，应在 §4 预先说明 [R2]
- **M3**: Algorithm 1 正文未给 default τ 值，需翻 Appendix [R1]
- **M4**: Figure 1 caption 未标注 seed=42 [R1]
- **M5**: Eq. (2) decontamination 的具体计算路径不明确（per-MCMC-sample zero-out vs analytic） [R1]
- **M6**: 引用年份：holland_1993_dif 和 lord_1980_irt 可能是再版年份 [R1, R2]

---

## Reviewer Consensus

以下问题两位 Reviewer **完全一致** [AGREE]：
- n=3 seeds 不足以支撑 cross-seed stability claims
- DiD null result 缺乏 power analysis，因果声明过强
- N=4 模型族的 taxonomy 泛化性不足
- Han et al. (2026) 差异化论证需加强
- 正文可能超 8 页限制（desk-reject 风险）
- Bayesian/frequentist 术语需统一
- RRF fusion 需 calibration 验证
- SFT ecological validity 是已知局限（但不构成拒稿理由）
- 遗漏引用：Yang et al. (2023), Golchin & Surdeanu (2024), Sainz et al. (2023)

## Reviewer Divergence

**IRT identifiability 严重程度** — R1 列为 critical（J=13-16 在边界上），R2 反驳（Linear DGP coverage ≥0.93，coverage 下降仅在 J=500 Threshold DGP 下）。R2 的反驳有论文数据支撑（Appendix P），但 R1 关于 skewed exposure 的子论点被 R2 认可为 Should-Fix。**最终定级：Should-Fix**（W8）。

**ContamCal baseline 优势** — R1 指出 GSM8K 上 B4 优于 ContamCal；R2 反驳 ContamCal 核心价值在 uncertainty quantification + domain diagnosis 而非 MAE，且 MMLU/ARC 上 ContamCal 最优。**不列为独立 weakness**（ContamCal 的定位已从 calibration 工具转为诊断框架）。

**Bakhtin et al. (2024) 引用** — R1 建议引用，R2 反驳（pretraining deduplication 与本文主题关联较远）。**不列为遗漏**。

---

## Questions（需要作者澄清）

1. Appendix P 中 CI coverage 随 J 增大下降——能否详细解释 bias 来源？这是否意味着 2PL+γ 在大样本下是 misspecified 的？
2. RRF exposure 的 right-skewed 分布是否引入 leverage effect？是否做了 influential observation 诊断？
3. 低剂量（d005, d025）下 cross-benchmark transfer pattern 是否与 d100 一致？
4. 0.5B 的 A-option position bias（46%→98%）是否暗示 small models 有完全不同的 dose-response 机制？是否考虑过 position bias correction 后的补充分析？

---

## Missing References

1. **Golchin & Surdeanu (2024)** "Time Travel in LLMs: Tracing Data Contamination in Large Language Models" (ICLR 2024) — instance-level 污染检测代表性工作 [R2]
2. **Sainz et al. (2023)** "NLP Evaluation in Trouble: On the Need to Measure LLM Data Contamination for each Benchmark" (EMNLP 2023 Findings) — per-benchmark 污染度量 [R2]
3. **Yang et al. (2023)** "Rethinking Benchmark and Contamination for Language Models with Rephrased Samples" — rephrasing 绕过检测，与 S3 (ConStat) 设计动机直接相关 [R1, R2]
4. **Recht et al. (2019)** "Do ImageNet Classifiers Generalize to ImageNet?" — benchmark overfitting 经典工作 [R1，R2 同意但优先级较低]

---

## External Review

**外部审稿**: 未请求（项目未配置 paperreview_ai）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成（5 warnings, 0 critical, 8 info）：

**Warnings:**
1. **Pages 1-3 纯文本无 display item**：连续 3 页无 figure/table，直到 p.4 才出现 Algorithm 1，p.6 才出现首个 figure。建议将核心结果图或方法概览图提前至 p.1-2。
2. **Figure 1 位置偏后且尺寸偏小**：全文首个 figure 出现在 p.6，单栏宽度，建议改用 `figure*` 双栏全宽并提前放置。
3. **正文超 8 页**：Section 6 延伸至 p.9 约 40%，与 Reviewer 共识一致。
4. **Appendix 末页大面积空白**：Tables 12-13 下方约 60% 空白，可合并或重组。
5. **Pages 4-5 视觉断档**：Experimental Setup + Results 开头连续 2 页无 figure/table。

**Info (正面):**
- Title/Author/Abstract 排版整洁，ACL 匿名格式正确
- 公式渲染正确，无 LaTeX 残留错误
- Tables 使用 booktabs 风格，专业规范
- Figure 2 散点图清晰可读
- 参考文献格式统一，无未解析引用

---

## Overall Assessment

**评分: 3.0 — Findings**

**置信度: 4/5**（两位 Reviewer 均有强领域背景，交叉回应后关键问题达成高度共识）

**理由**:

论文的核心贡献——用控制实验揭示 "contamination ≠ inflation"——有真实价值，实验设计是该领域的方法论升级。然而，四个 critical 问题共同限制了论文达到主会议水平的证据强度：

1. **统计功效不足**：n=3 seeds 和 J=13-16 的组合意味着 taxonomy stability claims 和 DiD causal claims 都在统计功效边界上运行。两个核心贡献（taxonomy + global modulation）的 claim 强度均超出了证据支撑范围。

2. **泛化性未验证**：N=4 家族上的 4 类分类学更接近 post-hoc 描述而非可泛化的分类体系。没有 out-of-sample 验证，taxonomy 的预测力未知。

3. **差异化不充分**：与最直接的在先工作 Han et al. (2026) 仅有 2 句话区分，审稿人无法充分评估增量贡献。

4. **格式风险**：正文疑似超 8 页，存在 desk-reject 风险。

如果作者能：(a) 增加 seeds 或弱化 claims，(b) 补充 power analysis，(c) 增加 Han et al. 对比，(d) 修复页数问题——论文有潜力提升至 3.5 (Borderline Conference)。当前状态适合 Findings 接收。

---

## Detailed Comments

### Section 1 (Introduction)
- Contribution 2 声称 "causal evidence that SFT contamination operates through global capability modulation" 过强，需降级为 "no detectable evidence of item-specific memorization"
- "qualitatively different dose-response patterns" 的措辞 OK，但应注明样本量限制

### Section 2 (Related Work)
- Han et al. 段落需扩展至 ~0.5 页详细方法论对比
- 缺 Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023)
- DIF 经典文献（Camilli, Swaminathan, Holland）已引用 ✓

### Section 3 (Method)
- 2PL+γ 模型数学正确，假设合理 ✓
- Eq. (2) 应补充计算路径说明
- RRF fusion 需 signal rank correlation + leave-one-signal-out 消融
- Algorithm 1 需在正文给出 default τ 值

### Section 4 (Experimental Setup)
- 控制注入方案合理 ✓；AUGMENT mode 需在正文早期说明
- Gemma-2 GSM8K 排除应提前声明
- 0.5B 排除理由充分 ✓

### Section 5 (Results)
- Table 1 (dose-response patterns): 应注明 "N=4 families, preliminary" 性质
- Table 2 (cross-benchmark): 仅报告 d100，低剂量结果缺失
- Table 3 (cross-seed): n=3 下 CI 宽度需显著声明
- Table 4 (DiD): 需 power analysis；"causal evidence" 需降级
- §5.5 (Calibration): ContamCal 核心价值在诊断而非 MAE——当前叙述可更突出此点
- §5.7 (Domain): Social Sciences γ_d 通过 Bonferroni ✓；exploratory caveat ✓

### Section 6 (Discussion and Conclusion)
- 必须压缩至 p.8 内——多段内容与 §5 重叠
- "Pretraining contamination may produce qualitatively different effects" 的 caveat 恰当 ✓

### Limitations
- 覆盖 10 个点，内容充分 ✓（R1 认为不应压缩）
- 不计入页数，不影响格式合规

### Ethics Statement
- 恰当，覆盖了 dual-use risk ✓

### Appendix
- 详尽且有价值 ✓
- DGP robustness (Appendix P) 需补充 skewed exposure 条件
- S4 details (Appendix E) 已补充 ✓
- Training convergence (Appendix F) 已补充但较简略