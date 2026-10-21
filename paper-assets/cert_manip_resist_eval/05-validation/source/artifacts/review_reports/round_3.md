---
round: 3
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-24T03:02:34.230936+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3 (Fresh Review)

**论文**: The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels
**Venue**: EMNLP 2026 via ARR May 2026 cycle (Long Paper)
**Reviewer 配置**: 2 人（R1: 方法严谨性 + 统计框架 + 实验设计；R2: 新颖性 + 相关工作 + 完整性 + 格式合规）

---

## Summary

论文研究 LLM judge panel 的对抗脆弱性如何随 panel 规模变化。在 15 个模型、6 种攻击、2 个基准、K∈{3,5,7} 的组合设计下，分解 panel 脆弱性为个体弱点 (η_max) 和结构多样性 (K_eff) 两个预测变量。核心发现：K_eff 方向一致为正（diversity 与 vulnerability 正相关），K=3 时两者共同决定，K≥5 时 K_eff 成为唯一显著预测变量（bootstrap 10/12）；聚合规则调制可预测性（threshold R²=0.83 → Bayesian R²=0.09）。

---

## Strengths

1. **实验规模与统计严谨性突出**。15 models × 6 attacks × 2 benchmarks × 3 panel sizes × 4 aggregation methods，455–6,435 panels 全组合枚举。Wild cluster bootstrap、clustered SE、mixed effects、Cinelli-Hazlett sensitivity、GAM bootstrap、fractional logit、dominance analysis 等多重鲁棒性检验互相印证，这是近期同类工作中最彻底的统计分析之一。[R1, R2 共识]

2. **Predictor shift 发现是实质性原创贡献**。η_max → K_eff 的 panel-size-dependent shift 在既有文献中未见类似发现，有明确的实践意义（小 panel 筛选个体 robustness，大 panel 管理 judge independence）。[R1, R2 共识]

3. **聚合方法对比有实用价值**。四种 aggregation 方法的系统比较（threshold R²=0.83 到 Bayesian R²=0.09 的 predictability gradient）为部署提供了 actionable guidance。Bayesian calibration 能部分化解 K_eff channel 但保留 η_max channel 的发现有防御设计意义。[R1, R2 共识]

4. **统计诚实度值得肯定**。论文坦承 K_eff 在 K=3 bootstrap 下仅 4/12 显著（vs. OLS 12/12），诚实报告 diversity-capability confound（r=0.70–0.81），不回避 Cinelli-Hazlett 的不利结果（28/36 条件下 K_eff 不抗已知混淆）。[R1, R2 共识]

5. **论文结构清晰、格式合规**。逻辑链连贯，appendix 有序（A–Q），Abstract 154 words（＜200 限制），ACL template [review] mode，匿名性完好，Limitations 位置正确，正文 8 页合规。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**M1. [critical] 因果语言与观测性设计根本矛盾** [R1-N2, R2-W3 | 共识: AGREE]
- Title "Modulates"、Abstract "determines adversarial vulnerability"、Section 6 "Predictor Shift Mechanism"——均为因果动词/概念
- 但研究本质是观测性回归：panel 通过穷举组合构造，模型非随机分配到 capability tier
- Section 6 尾句承认 "observational regression cannot reliably disentangle diversity's causal contribution"——与前文 framing 严重不一致
- **两位 Reviewer 完全一致**：需全文统一为描述性语言（"associated with" / "predicts"），标题、abstract、section headers 均需修改

**M2. [critical] Cinelli-Hazlett 敏感性分析实际削弱核心发现** [R1-N1 | 共识: AGREE]
- Table 7: K_eff 的 robustness value 仅在 8/36 条件下超过已知 η_max 混淆的 partial R²（K=3: 1/12, K=5: 3/12, K=7: 4/12）
- 意味着 78% 条件下，一个与 η_max 同等强度的混淆因子即可将 K_eff 系数解释为零
- Pool A capability-matched subsample (r=0.50) 改善到 10/12，但仅 126 panels（vs. 3,003），统计功效大幅下降
- 论文将此呈现为 "robustness increasing with K"——趋势方向正确，但不构成 K_eff 独立因果效应的有力证据
- **需在 Abstract/Introduction 中明确承认 Cinelli-Hazlett 的不利结果，而非仅在正文末尾轻描淡写**

**M3. [critical] "Predictor shift" 的 K=3 baseline 叙事随推断方法改变** [R1-N3 | 共识: AGREE with nuance]
- K=3 结果在不同推断方法下支持不同 narrative：
  - OLS: η_max 10/12, K_eff 12/12 → 两者显著
  - Clustered SE: η_max 8/12, K_eff **1/12** → η_max 独占
  - Wild bootstrap: η_max 3/12, K_eff 4/12 → 弱共决定
- 论文选择 bootstrap 结果构建 "co-determination at K=3" 叙事，但 clustered SE 给出完全不同结论
- **R2 nuance**: K≥5 的 shift 方向在多方法下一致（η_max 下降、K_eff 上升），predictor shift 的方向是 robust 的，但 K=3 处的具体叙事是 method-dependent
- **需增加 method-comparison 表格，明确展示差异；将 K=3 结论修正为 method-sensitive pattern**

**M4. [critical] "Diversity hurts" 的新颖性声明过度** [R2-N1 | 共识: 部分 AGREE]
- Tramèr et al. (2018)、Kariyappa & Qureshi (2019)、Pang et al. (2019) 已证明 ensemble diversity 在 adversarial transfer 下增加攻击面
- "Contrary to CJT predictions" 的 framing 属 overclaiming——CJT 显式假设 independent non-adversarial errors，adaptive adversary 下不适用是 trivially expected
- **R1 nuance**: predictor shift 本身（方向已知→K-dependent transition 未知）、LLM judge context（语言操纵 vs. 梯度对抗）、aggregation modulation 构成增量新颖性，R2 低估了这些
- **需重新校准 contribution 定位**：弱化 "contrary to CJT" framing，强调 predictor shift phenomenon 和 aggregation comparison 作为核心贡献

**M5. [critical] K_eff 作为 diversity measure 的独特贡献不充分** [R2-N2 | 共识: AGREE]
- Table 11 (Appendix P): κ-diversity (ρ=0.942 with K_eff, 7/12 sig, |β̄|=0.194) 与 K_eff (8/12 sig, |β̄|=0.164) 表现相当甚至更优
- 论文声称 interpretability advantage，但为主观判断
- **R1 补充**: K_eff 的 SDPI 理论联系（η_joint ≤ K_eff · η_max）是 κ-diversity 不具备的，应将此作为核心 justification
- **需在正文展示 Table 11 对比，诚实讨论 trade-off；或弱化 K_eff 本身的 novelty claim**

### Should-Fix（影响评分但不一票否决）

**S1. [warning] K_eff–η_max 共线性使 predictor decomposition 统计不可靠** [R1-W5 | 共识: AGREE]
- r=0.70 (K=3) 到 r=0.81 (K=5)，VIF≈2.0–2.9
- 两个预测变量实质上反映同一底层结构（panel capability 组成），回归无法可靠分离
- 与 M2 (Cinelli-Hazlett) 形成一致证据链
- Section 6 "Diversity–Capability Confound" 应从 "可通过子样本分析部分缓解" 升级为 "根本性局限"

**S2. [warning] Wild cluster bootstrap 聚类数不足** [R1-W1 | 共识: AGREE, moderate]
- K=3: 13 clusters/position, K=5: ≤11, K=7: ≤9——均低于 Cameron et al. (2008) ≥20 推荐值
- 论文已用 Rademacher weights 缓解（MacKinnon & Webb 2018），但未充分讨论 K≥5 cluster 数更少的影响
- 可能导致 bootstrap 过于保守，K=3 的 4/12 可能是 power 不足而非效应不存在

**S3. [warning] Tier 分类偏斜与 capability-quantization 混淆** [R1-W2 | 共识: AGREE]
- 15 模型中 9 个 lightweight（60%），含 6 个 AWQ INT4 量化模型（clean accuracy 0.253–0.543）
- Tier 边界不透明：gemini-3.5-flash (MMLU 0.968) mid-tier vs gpt-5.5 (0.957) frontier
- 6 个本地量化模型 clean accuracy 极低（接近 random），无法分离 "能力弱" 与 "量化损伤"

**S4. [warning] 攻击模板覆盖不足** [R1-W4 | 共识: AGREE]
- 每种攻击仅 1-2 template variants，缺少 attack strength gradient
- Prompt injection 仅覆盖最经典形式（"Ignore previous instructions"），未涉及 indirect injection 等更隐蔽方式
- 结论可能与特定模板措辞高度绑定

**S5. [warning] 相关工作遗漏** [R2-W1 | R1 条件性 AGREE]
- Maloyan et al. 2025 (arXiv:2505.13348): prompt injection on LLM-as-Judge，与 Attack Type 1 直接相关
- TAMAS benchmark (arXiv:2511.05269): multi-agent LLM adversarial benchmark
- Adversary-Resistant Multi-Agent via Credibility Scoring (arXiv:2505.24239): credibility-based 防御

**S6. [warning] Kuai et al. (2026) 讨论不足** [R2-W2 | R1 条件性 AGREE]
- 已引用但仅作旁证。其 Difficulty-Weighted Behavioral Entanglement Index 和 de-entangled reweighting 方法与 K_eff 高度相关，应深入讨论

**S7. [warning] 术语不一致** [R2-W4 | 共识: AGREE]
- "regime transition" vs "predictor shift" 交替使用，应统一为一个术语（建议 "predictor shift"）

**S8. [warning] Benchmark 局限** [R2-W6 | 共识: AGREE, 论文已部分覆盖]
- 仅 MMLU 和 ARC（multiple-choice），open-ended evaluation（MT-Bench 风格）的 generalizability 未知
- Limitations 已提及但可加强讨论

### 小问题（Info）

- ε 敏感性：K=3 时 3 个条件出现 K_eff 符号翻转（ε=10⁻⁶ vs 10⁻⁹），应在正文提及
- 300-item 样本代表性：MMLU 57 subjects ≈ 5.3/subject，subject 异质性未探讨
- Table 3 标注："Bayesian η_max 9/12 is OLS; bootstrap validation pending"——未完成验证的数据不应无标注出现
- Table 3 vs Table 4 比较误导性：K=3 OLS vs K=5 bootstrap 使用不同推断方法
- Figure 2 y-axis label 字号偏小
- OpenRouter "May 2026 snapshots" 缺乏版本锁定保证

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识 [AGREE]：
1. **因果语言需全面修正** — Title/Abstract/Section headers 的因果动词与观测性设计矛盾 [M1]
2. **Cinelli-Hazlett 不利结果需前置** — 78% 条件下 K_eff 不抗已知混淆，不应仅在正文末尾提及 [M2]
3. **K_eff–η_max 共线性是根本性局限** — r=0.70–0.81 使 predictor decomposition 不可靠 [S1]
4. **K_eff 的 uniqueness claim 不充分** — Table 11 显示 κ-diversity 表现相当 [M5]
5. **术语应统一** — "regime transition" vs "predictor shift" [S7]

## Reviewer Divergence

| 问题 | R1 | R2 | 裁定 |
|------|----|----|------|
| Theorem 1 覆盖率 58% [R1-W3] | Should-Fix: 适用范围有限 | REBUT: 58% 是 ecosystem 描述而非定理缺陷，跨 tier pairs 大多满足 | **采纳 R2**: Theorem 1 是条件定理，stochastic dominance 是否成立是实证问题，58% 是对 LLM 生态的描述而非定理的缺陷。但建议在定理后量化适用范围。|
| 攻击模板 dual-use disclosure [R2-W5] | REBUT: 模板均来自已发表工作，dual-use 风险极低 | Should-Fix: 缺少 responsible disclosure 讨论 | **采纳 R1**: 所有攻击模板来自 Perez & Ribeiro (2022)、Greshake et al. (2023) 等已发表工作，未引入新型攻击。ARR Responsible NLP Checklist 在 OpenReview form 中填写，不需要论文内单独讨论。降级为 info。 |
| R2-N1 novelty 严重程度 | 部分 AGREE: CJT overclaiming 成立，但增量新颖性（predictor shift, LLM context, aggregation）被低估 | Critical: "diversity hurts" 非 novel | **综合判断**: "diversity hurts" 方向上确实非 novel，但 predictor shift phenomenon、LLM judge 语言攻击 context、aggregation modulation 构成有意义的增量贡献。需重新校准 framing 而非否定全部新颖性。 |

---

## Questions for Authors

1. 如果在 K_eff 对 η_max 回归取残差后，用残差预测 ASR，K_eff 的 independent contribution 是否仍然显著？这比 Cinelli-Hazlett 的 hypothetical confound 分析更直接。
2. API-only subset (9 models, r=0.85) "does not replicate the transition"——这是否意味着 predictor shift 本质上是由 AWQ INT4 量化模型驱动的 artifact？
3. Bayesian calibration 的 clean accuracy prior 在何种攻击条件下会被 adaptive adversary exploit？是否有实验验证？
4. 300 items per benchmark 的 subject-level 异质性如何？是否存在某些 MMLU subjects 上 K_eff effect 特别强或特别弱？

---

## Missing References

| 论文 | 相关性 | 处理建议 |
|------|--------|----------|
| Maloyan et al. 2025 (arXiv:2505.13348) | 高 | 必须引用——prompt injection on LLM judge 的 direct prior work |
| TAMAS benchmark (arXiv:2511.05269) | 中 | 建议引用 |
| Adversary-Resistant Multi-Agent via Credibility Scoring (arXiv:2505.24239) | 中 | 建议在 aggregation 讨论中引用 |
| Kuai et al. 2026 (arXiv:2604.07650) | 高 | 已引用但需大幅扩展讨论 |

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置中 external_review 未启用）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 7 info）。主要发现：

- **[warning]** Page 7 单页承载 Figure 3 + Figure 4 + Table 3 共 3 个 display items，视觉密度偏高
- **[warning]** Page 18 末页仅 3 条 references（~15% 内容），85% 空白
- **[info]** Figure 2 y 轴标签字号偏小（接近可读下限），建议放大至 ≥9pt
- **[info]** Table 2 符号标记（+/−/Co）信息密集但需反复查看 caption
- **[info]** Figures 2-5 统一 blue/orange 配色，颜色一致性好
- **[info]** 所有 table 统一 booktabs 风格，专业
- **[info]** Limitations 位于正文第 8 页，符合 EMNLP 2026 要求

---

## Overall Assessment

**评分: 3.0 / 5 — Findings**

**置信度: 4 / 5**（两位 Reviewer 均精读全文含附录，统计方法论和 LLM evaluation 均为专业领域）

**理由**:

论文对一个重要且时效性强的问题——LLM judge panel 的对抗脆弱性如何随 panel 规模变化——给出了系统性的描述性发现。实验设计覆盖广泛，统计分析深度在同类工作中突出，K_eff 正方向一致性（12/12 条件 × 多种推断方法）和 predictor shift（K=3 → K≥5）是有价值的描述性贡献。

阻止上升至 Conference (4.0) 的核心问题：

1. **因果 overclaiming 严重且贯穿全文**（M1）——Title/Abstract/Section headers 使用因果语言，但 Cinelli-Hazlett 分析表明 78% 条件下 K_eff 无法与 η_max 混淆分离（M2），K=3 baseline 叙事随推断方法改变（M3）。如果核心 claim 的因果解读不成立，贡献从"发现因果机制"降级为"描述性关联"——这本身仍有价值，但需要匹配的 framing。

2. **新颖性需重新校准**（M4, M5）——"diversity hurts under adaptive attack" 的方向性结论在 ensemble adversarial robustness 文献中已有理论基础；K_eff 相对 κ-diversity 无显著量化优势。论文的真正增量贡献是 predictor shift phenomenon 和 aggregation modulation，这些足以支撑 Findings 但需要更诚实的定位。

3. **共线性是根本性局限**（S1）——r=0.70–0.81 意味着 diversity 和 capability 在当前 LLM 生态中结构性耦合，仅靠观测回归无法分离。这不是可以通过子样本分析完全解决的问题。

论文的描述性发现（K_eff 方向一致为正、predictor shift pattern、aggregation predictability gradient）在修正 framing 后适合 Findings 发表。如果能在 revision 中完成因果语言的全面修正、Cinelli-Hazlett 结果的前置讨论、K_eff uniqueness 的诚实评估以及缺失相关工作的补充，有可能提升至 Borderline Conference (3.5)。

---

## Detailed Comments

### Title & Abstract
- Title "Modulates" → 建议改为描述性表述，如 "Panel-Size-Dependent Predictors of..."
- Abstract "determines adversarial vulnerability" → "is associated with" / "predicts"
- Abstract "Contrary to Condorcet Jury Theorem predictions" → 改为 "Consistent with adversarial ML predictions but newly characterized in the LLM judge panel setting"

### Section 1 Introduction
- Contribution 1 "Uniform diversity–vulnerability association" 的 "contrary to CJT/BFT predictions" framing 需弱化
- 应在 Introduction 末尾加入 caveat：结果为描述性关联，因果归因受限于 diversity-capability 共线性

### Section 3 Threat Model
- Theorem 1: 建议在定理后紧跟适用范围的定量限制（58% pairs, 跨 tier 覆盖更高）

### Section 4 Methodology
- Table 1: tier 分类标准应明确说明或在附录中验证不同划分方案下的稳健性
- Section 4.6: 应明确报告每个 K 值下的 cluster 数量及其对推断可靠性的影响

### Section 5 Results
- Section 5.1: 需增加 method-comparison 表格（OLS / Clustered SE / Mixed Effects / Bootstrap 在 K=3 的完整结果），避免单一选择 bootstrap 构建叙事
- Section 5.2: "co-determination" 表述需加 method-sensitivity caveat
- Table 3 "Bayesian η_max 9/12 is OLS; bootstrap validation pending" — 未完成验证的数据应明确标注

### Section 6 Analysis
- "Predictor Shift Mechanism" → 删除 "Mechanism"（暗示因果）
- "Diversity–Capability Confound" 应从 "可通过子样本分析部分缓解" 升级为 "根本性局限"，在 Limitations 中首要讨论

### Appendix P (Alternative Diversity Measures)
- Table 11 应移至正文或在正文中详细讨论 K_eff vs κ-diversity 的 trade-off
- K_eff 的 SDPI 理论联系应作为核心 justification 展开论证

### Related Work
- 增加 ensemble adversarial robustness 文献的深入讨论（Tramèr 2018, Kariyappa 2019, Pang 2019），说明 LLM judge panel 与 vision ensemble 的关键差异
- 扩展 Kuai et al. (2026) 讨论
- 补充 Maloyan et al. (2025) 等缺失引用