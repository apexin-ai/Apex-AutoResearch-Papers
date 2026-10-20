---
round: 8
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T01:30:03.957586+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: True
---

# 审稿报告：Reproducibility Budgets for Open-Weight LLM Evaluation

**论文**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models
**Venue**: EMNLP 2026 (via ACL ARR May 2026 cycle)
**审稿轮次**: Round 9 (Fresh)
**Reviewer 编排**: 2 人圆桌（R1 方法严谨性+实验设计, R2 新颖性+完整性+写作质量）+ 视觉审查 Agent
**日期**: 2026-05-23

---

## Summary

本文将 Generalizability Theory (G-theory) 应用于 LLM 评估方差分解，使用 8 个 7–9B 开源指令微调模型和 5 个 benchmark（MMLU, ARC, HellaSwag, GSM8K, MATH），跨 7 个 facet（item, model, precision, prompt, seed, temperature, ordering）的完全交叉因子设计，对约 230 万条二元评分记录进行方差分解。核心产出是 D-study reproducibility budgets：推荐的 3-prompt × 3-seed 设计以 178 items（1,602 次评估/模型）达到 G ≥ 0.80，相比 552 items 的单条件设计减少 3.1× 的 item 需求但增加 2.9× 的总评估量。次要发现包括 BF16/FP16 在 binary scoring 下功能不可区分（<0.1% interaction），以及 MC/FF benchmark 格式关联方差模式的 exploratory observation。

---

## Strengths

**[S1] 首次在 LLM 评估中同时交叉 infrastructure 和 methodology facets 的 G-theory 分析** [共识]
填补了现有文献仅处理单一维度方差的空白。exp-001 完全交叉设计（460,800 records）使所有 facet 及其 interaction 的方差分量可无混淆地估计。exp-002 系统性 reduced crossing（2,304,000 records）扩展至 5 个 benchmark，且验证了 reduced crossing 保留方差结构（ΔG = 0.0008）。

**[S2] 示范级的 robustness analyses** [共识]
Appendix A 覆盖了几乎所有可预见的方法论质疑：GLMM complement（ρ=1.0 rank preservation）、accuracy-range stability（r = −0.048）、Henderson Method I vs. REML 对比（Δ < 0.003pp）、probit simulation（τ = 0.81）、null calibration（observed/null = 1.0008）、facet specification sensitivity（ΔG = 0.37pp）、LOMO stability（40 subsets, CV ≤ 1.25%）、以及 reduced crossing validation。远超大多数投稿的 sensitivity 分析深度。

**[S3] D-study 预算框架的实用价值** [共识]
Table 4 和 Table 7 提供了可直接操作的评估设计指南，Figure 1 直观展示了 G coefficient 随 item 数量和条件数的变化。区分 item-minimizing（multi-facet）和 evaluation-minimizing（single-condition）两种策略及其适用场景。承诺开源 G-theory pipeline 和 D-study budget calculator。

**[S4] Related Work positioning 清晰** [共识]
准确定位了与 Messing (2026) 的三个差异化方向。系统覆盖了 IRT 方向（Lalor et al., 2019; Rodriguez et al., 2021; Maia Polo et al., 2024; Zhou et al., 2026; Li et al., 2025）、方差分解方向（Bouthillier et al., 2021; Dodge et al., 2020; Henderson et al., 2018）、psychometrics 经典文献（Shavelson &amp; Webb, 1991; Brennan, 2001; Cardinet et al., 2010）。

**[S5] Item difficulty heterogeneity 分析揭示了有意义的 benchmark typology** [共识]
MC benchmarks（item-dominated, 34–38%）vs FF benchmarks（distributed variance, prompt/model×prompt 显著）的结构差异，结合 Appendix D-F 的 cross-benchmark difficulty heterogeneity 和 residual regression 分析，为 benchmark 设计提供了有意义的分类框架。

**[S6] Limitations section 诚实且全面** [共识]
Section 6 主动覆盖了 temporal correlation、model exchangeability、binary scoring constraint、benchmark sample size (n=5)、few-shot ordering vs. identity、cross-validation 限制、以及 contamination 影响。

---

## Weaknesses

### Must-Fix / Should-Fix

**[W1] "3.1× item reduction" framing 隐藏总评估量增长 — Should-Fix** [强共识: R1 AGREE + R2 Must-Fix, 交叉后统一为 Should-Fix]
- **位置**: Abstract, Section 1, Section 5
- **问题**: 论文以 "3.1× item reduction"（552 → 178 items）作为核心 headline，但推荐的 3-prompt × 3-seed 设计实际需要 178 × 9 = 1,602 次评估/模型，总计算成本增加约 2.9×。Abstract 包含 "(1,602 total evaluations per model)" 和 "(552 items, 552 evaluations)"——信息存在但 emphasis 严重失衡。对于一篇关于评估 *budget* 的论文，只报告 budget 的一个维度构成系统性误导。Section 5 承认了 tradeoff 但被埋在结论段中。
- **建议**: 在 Abstract/Introduction 中平衡呈现 item reduction (3.1×) 和 total evaluation increase (~2.9×)；或引入 cost-per-G-point 指标使对比更公正。

**[W2] C2（precision separability）应降级为 C1 子发现 — Should-Fix** [强共识]
- **位置**: Section 1 Contributions, Section 4.4
- **问题**: BF16/FP16 在 binary scoring 下功能不可区分（<0.1% interaction）是 binary 信息损失的直接推论——当 ≥99% 的 items 给出相同 0/1 判断时，方差分析当然无法区分精度。这是一个确认性结果而非新发现。Contributions 列表已改为 "As a sub-finding" 但仍占独立编号（C1 第二段），与 C1 D-study budgets 并列权重过高。
- **建议**: 将 precision separability 合并入 C1 叙述中，不再有独立编号。

**[W3] Format-associated variance patterns 统计效力不足且证据混淆呈现 — Should-Fix** [强共识]
- **位置**: Section 4.3
- **问题**: MC vs. FF 方差模式对比基于 n = 5 benchmarks（3 MC, 2 FF），Spearman ρ = 0.82 (p = 0.089) 在任何传统阈值下不显著。论文另报 ρ = 0.90 (p = 0.006, n = 10)，但 R2 指出这是 **within-MMLU 10 subjects 的结果**，不构成独立的 cross-benchmark 证据。两个层级的证据被混淆呈现。MC/FF 差异可能反映 benchmark 构建质量、难度分布等混淆因素而非格式本身。
- **建议**: 明确分离 within-MMLU subject-level 证据和 cross-benchmark 证据；缩短 §4.3 篇幅或进一步降级为 preliminary observation。

**[W4] Forward prediction（Table 8）为 in-sample 验证，非 out-of-sample — Should-Fix** [强共识]
- **位置**: Section 4.5, Table 8
- **问题**: 4-model subset（DeepSeek, Llama, Mistral, Qwen3）是 8-model 全集的子集，共享相同的 items、prompts、seeds、orderings。从子集方差分量预测全集 G 本质上是 internal consistency check。LOMO（7→8 models）同样非 truly independent validation。Error 范围 0.96–6.88% 可能低估真实预测误差。
- **建议**: 将 Table 8 重标为 "internal consistency check" 而非 "forward prediction validation"。

**[W5] Scale validation 局限于 Qwen2.5 单一架构家族 — Should-Fix** [强共识]
- **位置**: Section 4.6
- **问题**: Within-family validation（Qwen2.5 3B/7B/72B）共享 training recipe、tokenizer 和数据混合策略。"preliminary evidence that budgets generalize beyond the 7–9B range" 超出了证据支撑范围。
- **建议**: 明确限定为 "within Qwen2.5 family, variance structure is scale-invariant"；Limitations 补充 cross-family generalization gap。

**[W6] Partial-credit scoring sensitivity 对发现影响讨论严重不足 — Should-Fix** [强共识]
- **位置**: Section 4.4, Section 5, Section 6
- **问题**: Binary → partial-credit 导致 G 从 0.76 降至 0.55，ρ = 0.26（方差分量排序根本性改变），prompt variance 从 25.5% 降至 1.2%。所有 D-study budgets、format patterns、precision separability 都严格绑定 binary scoring。当前 LLM 评估越来越多使用 LLM-as-judge 和 rubric-based scoring。Conclusion 仅一句带过。
- **建议**: Section 5 或 Limitations 用 2-3 句明确所有 budgets 仅对 binary correctness 有效；讨论 partial-credit 场景下 budgets 是 upper 还是 lower bound。

**[W7] Data contamination 作为 model×item interaction 混淆变量讨论不足 — Should-Fix** [共识，R2 部分]
- **位置**: Section 6
- **问题**: Model×item interaction 高达 25–36%，differential contamination（不同模型训练时接触了不同 benchmark items）是可信 confound。论文间接证据（3 MC benchmarks 方差结构一致）不充分——一致的 contamination 模式也能产生一致的方差结构。Section 6 的 budget ratio invariance 论点有一定说服力但被埋在 Limitations 中。
- **建议**: 将 budget ratio invariance 论点移至正文（§4.2）；补充引用 contamination 检测文献。

**[W8] Henderson Method I binary validation 的 bias 报告不完整 — Should-Fix** [共识，带 nuance]
- **位置**: Section 3.5, Appendix A
- **问题**: R1 最初质疑 Henderson Method I 假设连续正态数据，R2 纠正指出其对平衡设计分布无关（Brennan 2001 Ch.12）——方法论前提成立。但 probit simulation 的 ρ = 0.732 仅为中等相关，bias 报告仅覆盖 p ∈ [0.5, 0.8]，缺少极端 difficulty（p &lt; 0.3 或 p &gt; 0.9）的完整 bias/RMSE 分解。
- **建议**: 补充 full difficulty quintile 的 bias/RMSE 分解。

**[W9] Abstract 数字密度过高（>20 个数值）— Should-Fix** [共识]
- **位置**: Abstract
- **问题**: Abstract 包含 20+ 个具体数值，核心 message 被淹没。读者在首次阅读时难以在 30 秒内提取 "so what"。
- **建议**: 保留 3–4 个最关键数字（G ≥ 0.80, 178 items, item variance 占比, cross-benchmark consistency），其余移入正文。

### Minor

**[W10] Bootstrap CI 仅反映 item-sampling variability** [共识]
- Model facet 仅 8 levels + purposively selected。Item-level bootstrap 无法捕获 "换一组 models" 的 uncertainty。CI 报告应明确标注 "conditional on these 8 models"。

**[W11] Conclusion (Section 5) 对实用影响讨论不足** [共识]
- 未讨论：现有 benchmark 套件是否应据此重组、benchmark 开发者 vs 使用者应如何分别应用预算、对 leaderboard 运营的具体建议。受 8 页限制，优先级较低。

**[W12] Anonymous arXiv 自引（arXiv:2601.02310）破坏匿名性** [共识]
- 以 "Anonymous" 引用但含可解析 arXiv URL，reviewer 可通过 URL 追溯作者身份。建议评估必要性或改为不含 arXiv ID 的引用方式。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上达成强共识（交叉验证后均 AGREE）：

1. **"3.1× item reduction" framing 需要 rebalance**——信息存在但 emphasis 失衡（W1）
2. **C2 应降级为 C1 子发现**——precision separability 是 binary 信息损失的推论，非独立贡献（W2）
3. **Format-associated pattern n=5 统计效力不足**——within-MMLU 和 cross-benchmark 证据被混淆呈现（W3）
4. **Forward prediction 是 in-sample consistency check**，非 out-of-sample validation（W4）
5. **Scale validation 仅限 Qwen2.5 单一家族**——within-family ≠ cross-family generalization（W5）
6. **Partial-credit scoring limitation 讨论严重不足**——G 降幅 28%、ρ=0.26 意味着 budgets 的适用范围远比当前 framing 更窄（W6）
7. **Data contamination 作为 model×item interaction confound** 需更深入讨论（W7）
8. **Bootstrap CI 仅反映 item-sampling variability**——应明确标注条件于当前 8 models（W10）
9. **Abstract 数字过密**（W9）
10. **匿名性问题**（W12）

---

## Reviewer Divergence [REBUT]

### 分歧 1：相对于 Messing (2026) 的增量贡献（4 轮持续分歧）

- **R2 立场 (Should-Fix)**: 三个扩展方向逐一审视——(i) facet 替换非方法论创新；(ii) 跨 benchmark 增加 scope 但核心发现一致（item 在所有 benchmark 上主导）；(iii) D-study 是教科书内容非方法论贡献。属于 "competent application" 而非 "methodological advance"，excitement 不足。

- **R1 立场 (REBUT)**: 整体贡献超越三个子 claims 的加法——(i) 同时交叉 infrastructure + methodology facets 使二者 interaction 首次可估计（如 precision×temperature = 1.3%），是 design-level 创新；(ii) 跨 benchmark 结果揭示了 heterogeneity（MC item-dominated vs FF distributed），非 "核心发现一致"；(iii) D-study 方法是教科书内容但具体 budget 数字是实证贡献。

- **Director 判断**: 此分歧反映对 "应用创新 vs 方法论创新" 价值判断的根本差异。R1 论证更有说服力——将 G-theory 系统引入 LLM 评估确实是方法论应用层面的贡献，cross-benchmark heterogeneity 发现也非 trivial。但 R2 的核心质疑有效：excitement 低于 pure methodological innovation，这是限制评分的关键因素。

### 分歧 2：Model main effect 2.8% 的解读

- **R2 立场**: Model main effect 仅 2.8% 意味着模型近乎不可区分，模型样本可能过于同质，D-study budgets 泛化性存疑。

- **R1 立场 (REBUT)**: R2 误读了 G-theory。Model main effect 小意味着整体准确率相近（7-9B 同量级 expected），不等于模型 "不可区分"。Model×item interaction（30-36%）才是 ranking 信息来源。D-study 估计 ranking reliability 而非 absolute differentiation——即使 model main effect = 0%，只要 model×item interaction 够大，G 仍可很高。正确的泛化性质疑应关注 model×item interaction 在更多样模型下是否稳定。

- **Director 判断**: R1 的技术解读完全正确。Model main effect 在 G-theory 中不贡献于 G 系数计算——G 衡量的是 relative standing（ranking），不是 absolute differentiation。R2 的泛化性担忧仍然有效（model×item interaction 可能在更多样模型下改变），但论证角度需修正。

---

## Questions for Authors

**Q1.** Table 8 的 4 models 是 8 models 子集。是否有能力做 truly held-out 验证——例如用 exp-001 方差分量预测 exp-002 中某个全新 benchmark 的 G 系数？[R1, R2 AGREE]

**Q2.** Probit simulation ρ = 0.732：能否报告 variance components 的 MAPE 而非仅 rank correlation？对 D-study budget 的具体数字，magnitude accuracy 比 rank preservation 更关键。[R1, R2 AGREE]

**Q3.** Partial-credit G = 0.55, ρ = 0.26 是基于 GSM8K 单一 benchmark 还是多 benchmark？如仅一个 benchmark，partial-credit 结论的泛化性进一步受限。[R1]

**Q4.** Table 4 显示 multi-facet 3×3 设计需 1,602 evaluations，单条件设计仅需 552。能否提供具体的 GPU-hours 或 API 成本对比，明确在何种场景下 multi-facet 设计优于单条件设计？[R2]

**Q5.** 鉴于 partial credit "fundamentally reshapes variance structure"，这些基于 binary scoring 的 budgets 对非 binary 场景（LLM-as-judge, BLEU, F1, rubric-based）的参考价值如何？[R2]

---

## Missing References

以下为两位 Reviewer 共同或各自建议的缺失引用：

1. **Saxon et al. (2024)** — "Benchmarks as Microscopes: A Call for Model Metrology" (COLM 2024). 与论文的 measurement-theoretic framing 直接互补。[R2]

2. **Alzahrani et al. (2024)** — "When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards" (ACL 2024). 讨论 leaderboard 排名对评估方法论选择的敏感性。[R2]

3. **Oren et al. (2024)** — "Proving Test Set Contamination in Black Box Language Models". 可支撑 W7 data contamination 讨论。[R1]

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求**。项目未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态：已完成**（耗时约 3 分钟）。1 critical, 2 warning, 9 info。

| Severity | 页面 | 发现 |
|----------|------|------|
| **Critical** | p.16 | 末页仅顶部 5 行 prompt template 文本（~5% 面积），其余 ~95% 空白。审稿人翻到最后一页会留下"草率/未完成"的负面印象。建议将 p.15-16 prompt template 重排或合并使 p.16 消失。 |
| **Warning** | p.3-4 | 连续 2 页纯文本（Related Work + Method §3.1），Figure 1（p.2）后到 p.5 才有下一个 display item，视觉间隔 3 页。可考虑提前某个 figure。 |
| **Warning** | p.15 | Prompt template monospace 排版含原始占位符，较粗糙。建议加边框美化并减少空行。 |
| **Info** | 全局 | 首页纯文本→Figure 1 p.2 位置尚可；Figure 1 legend 字号偏小但可读；Table 1+Figure 2 (p.5) 互补；Figure 3+Table 3 (p.7) 格式规范；主文 p.8 填充 ~85%；References 整洁无未解析引用；Appendix tables/figures 密度适当。 |

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| **Soundness** | 3.5/5 | 4/5 | **3.75/5** |
| **Excitement** | 3.5/5 | 2.5/5 | **3.0/5** |
| **Reproducibility** | 4.0/5 | 4/5 | **4.0/5** |
| **Confidence** | 4/5 | 4/5 | **4/5** |

### Overall: **3.5 (Borderline Conference)** — 共识

### 总评

本文是 G-theory 在 LLM 评估领域的一项方法论 competent、实验严谨、robustness 验证深入的实证工作。**最强贡献是 D-study reproducibility budget 框架（C1）**——为评估设计者提供了可直接操作的 item 数量和条件配置指南，在评估可靠性领域有实际应用价值。

**核心弱点**体现在三个层面：

1. **Framing 层面**（W1, W2, W3）: "3.1× item reduction" headline 隐藏了总评估量 2.9× 增加的事实；C2 是确认性结果而非发现；format-associated pattern (n=5, p=0.10) 统计效力不足但证据被混淆呈现。三个 contributions 中实际上只有 C1 是 substantive contribution。

2. **Generalizability 层面**（W4, W5, W6, W7）: Forward prediction 为 in-sample consistency check 而非 out-of-sample validation；scale validation 限于 Qwen2.5 单一家族；所有发现严格绑定 binary correctness scoring（partial-credit 导致 G 降 28%, ρ=0.26）；data contamination 可能 inflate model×item interaction。Scope 受限于 8 个同质 7-9B 模型 + binary scoring，限制了结论的外推性。

3. **Novelty 层面**（分歧）: 相对于 Messing (2026)，本文使用相同框架、不同 facets、更多 benchmarks，属于 systematic extension。R1 认为整体贡献超越子 claims 加法，R2 认为 excitement 不足。Director 判断：方法论应用层面的贡献有价值，但缺乏方法论创新或出人意料的发现。

**使论文从 3.5 提升至 4.0 (Conference) 需要**：
1. 透明呈现评估成本 tradeoff（item reduction vs total evaluation increase）
2. 将 C2 合并入 C1、format pattern 更显著标注为 preliminary
3. 强化 partial-credit limitation 讨论（当前 LLM 评估大量使用非 binary 评分）
4. 精简 Abstract 数字密度
5. Forward prediction 重标为 consistency check

**当前适合 Findings (3.0-3.5 range)**：Soundness 足够，practical value 有，robustness analyses 出色，但 excitement 和 novelty 未达 main conference 阈值。9 个 Should-Fix + 3 个 Minor 虽非 fatal flaws，但累积起来使核心 claims 需更多 qualification。

---

## Detailed Comments

### Section-by-Section

**Abstract**: 数字密度过高（W9），需精简至 3-4 个关键数字。"3.1× item reduction" 需平衡呈现总评估量增加（W1）。

**Section 1 (Introduction)**: Motivation 有效——"piecemeal approach cannot capture interactions" 论证清晰。Contributions 列表中 C1 有实质内容，但 C2（precision separability）应合并为 C1 子发现（W2）。

**Section 2 (Related Work)**: 覆盖面广，positioning 与 Messing (2026) 的差异化方向描述准确。建议补充 Saxon et al. (2024) 和 Alzahrani et al. (2024)。

**Section 3 (Method)**: G-theory 引入清晰，D-study 解释直观。§3.5 的 Henderson Method I 辩护需补充极端 difficulty 的 bias 报告（W8）。§3.6 的 quasi-random model facet 论证（LOMO + Cohen's κ）证明了 internal consistency 但非 representativeness。

**Section 4.1-4.2 (Main Results)**: 方差分解表达清晰，Table 2-3 信息密度适当。Model×item interaction 30-36% 与 DIF 文献的关联有价值。

**Section 4.3 (Format-Associated Patterns)**: 统计效力不足（n=5, p=0.10），within-MMLU 和 cross-benchmark 证据混淆呈现（W3）。建议缩短或降级。

**Section 4.4 (Scoring Sensitivity)**: Partial-credit pilot 发现方差结构根本性改变——这是论文中最重要但最 underplayed 的发现之一。需更充分讨论对 D-study budgets 适用范围的影响（W6）。

**Section 4.5 (Forward Prediction)**: 应重标为 "internal consistency check"（W4）。

**Section 4.6 (Scale Validation)**: 需明确限定为 "within Qwen2.5 family"（W5）。

**Section 5 (Conclusion)**: 过于简短。需增加 practical implications 段——benchmark developer vs user guidance、leaderboard 建议（W11）。

**Section 6 (Limitations)**: 覆盖面广但部分关键限制（binary scoring、contamination）权重不足。

**Appendix A (Robustness)**: 出色。建议补充 probit simulation 的 full difficulty quintile bias/RMSE 分解（W8）。

**Appendix G (Prompts)**: p.16 末页 95% 空白需修复（Visual Check critical）。

### 格式合规检查

- **页数**: 正文 8 页 ✓（ACL template, review mode）
- **匿名性**: "Anonymous ACL submission" ✓，但 arXiv:2601.02310 自引有匿名性风险（W12）
- **Limitations**: 存在且覆盖面广 ✓
- **References**: 格式整洁，无 [?] 未解析引用 ✓
- **模板**: ACL `\usepackage[review]{acl}` ✓