---
round: 7
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T03:47:42.968802+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 8 (Fresh Review)

**论文**: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition"
**Venue**: EMNLP 2026 Main Conference (Long Paper via ARR)
**截止日期**: 2026-05-25
**审稿模式**: Fresh（独立初审）
**Reviewer 编排**: 2 人（R1 方法严谨性/实验设计，R2 新颖性/完整性/写作质量）

---

## Summary

本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated 内容控制、per-axis 风格分解和位置控制的 pairwise comparison，系统量化 LLM judge 的风格偏差。核心发现 "Likert Blindspot" 表明 Likert 评分在中等效应量下系统性遗漏 pairwise comparison 能检测到的风格偏差（信号损失 >60%），在四个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、一个 negative control（Claude Sonnet 4）、三个 benchmark（LLMBar, AlpacaEval, MT-Bench）和三个风格轴（formality, verbosity, register）上得到验证。GEE conditional decomposition 揭示 per-axis confound structure：verbosity 为 style-dominated（OR 8–13），formality 受 content quality 调节，register 为 judge-dependent。

---

## Strengths

**S1. 多层验证的实验管线（两位 Reviewer 一致认可）。** NLI gate (DeBERTa-v3-large, τ=0.90) → consistency filter → position-balanced pairwise → BT + GEE 的管线设计体现了出色的方法论思维。11 个 NLI 阈值扫描（Appendix E）、same-style double-rewrite control（Appendix O）、100-point continuous Likert（Appendix M）和 formal power analysis（Appendix K）构成严密的验证层次。

**S2. 七种统计方法的 sensitivity hierarchy。** Table 2 清晰展示：所有 Likert-based 方法（ATE, binarized, ordinal regression, GEE, Wilcoxon）均未达显著性，而 pairwise 方法（BT, sign test）达到。这是对 Likert Blindspot 的 compelling evidence，且 Appendix P 的 verbosity 复制进一步加强。

**S3. GEE conditional decomposition 是 genuinely novel 的分析贡献。** Table 3 揭示跨 judge 一致的 per-axis confound structure——verbosity style-dominated、formality conditional、register judge-dependent——超越了 "judges have style bias" 的简单叙事。Appendix C 的 correlation structure robustness 和 interaction test 验证了 GEE specification。

**S4. 100-point continuous Likert 是关键控制实验。** Appendix M 证明 Blindspot 不是 scale granularity 问题（101 值下 tie rate 仍 51–64%），而是 absolute vs. relative evaluation paradigm 差异。

**S5. 负面控制的 discriminative validity。** Claude Sonnet 4 在两个主要轴上未检测到显著偏差，支持框架不对所有 judges 产生 false positive。

**S6. 对 RATE 的比较公平且建设性。** 论文将两者定位为互补框架（§5.2），而非简单否定。

**S7. 诚实的局限性讨论。** 公开讨论了 evaluator-producer bias、measurement attenuation vs. construct divergence 歧义、样本量约束。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [critical, 共识] Primary family 构成缺乏透明度。**
Section 4.1 声明 "a primary family of six hypothesis tests (three judges × two axes)" 并应用 Holm-Bonferroni 校正，但未指明哪三个 judges 被纳入 primary family。四个 target judges 中排除哪一个（很可能是 Gemini，其 formality GEE 行为与其他三个不同）未说明。如果纳入 Gemini（8 tests），校正更保守，部分结果可能失去 adjusted significance。Table 1 将 register 标为 exploratory (†_e) 而正文说 "three judges × two axes"（不含 register），这与 Round 7 发现的 register 分类矛盾一脉相承。需在 §4.1 明确列出三个 primary judges 名称及排除理由，并报告 8-test family 下 adjusted p-values 作为 sensitivity analysis。
— R1 提出，R2 AGREE

**MF2 [critical, 共识] Cross-rewriter independence 验证覆盖面不足。**
Appendix D 仅测试了一个 judge（Qwen3-32B）配合替代 rewriter（GPT-4o），四个 target judges 中另外三个无 cross-rewriter 验证。GPT-4o as judge 使用 Qwen3-32B 作 rewriter，可能检测到 Qwen3-32B 特有改写痕迹；Llama-70B 和 Gemini 完全无验证。R2 补充：核心 claim 不依赖 rewriter-independence（Blindspot 在全部四个 judges 上用同一 rewriter 一致确认），cross-rewriter 是 supplementary robustness，但 claim scope 应相应 downgrade。
— R1 提出，R2 AGREE（含 contextualization）

**MF3 [critical, 共识] 负面控制 TOST Δ=15pp 过宽，n=87 功效不足。**
论文最小 confirmed bias 为 +13pp（GPT-4o formality, BT 63.0%），而 TOST Δ=±15pp 几乎涵盖此范围——Claude 可能有高达 ~14pp bias 而 TOST 仍宣告等价。Appendix G 自承 Δ=10pp underpowered。建议三选一：(a) 增加 Claude 样本量使 Δ=10pp 有功效；(b) 将 Claude 重新定位为 "insufficient evidence for bias" 而非 "negative control"；(c) 报告 n=87 下能 reject 的最小 Δ。
— R1 提出 (N3)，R2 完全 AGREE (= R2-W3)

**MF4 [critical→should-fix, 分歧后降级] Novelty 定位需更诚实。**
Likert Blindspot 的概念基础（forced-choice > rating scales）在心理测量学中已有近百年历史（Thurstone 1927, Bradley & Terry 1952）。论文整体叙事——标题、Abstract、Introduction——给人 "全新发现" 印象，而非 "已知原理在 LLM judge 领域的首次系统性实证"。R1 补充 nuance：LLM 非人类 rater，表现相同心理测量脆弱性非 trivial；per-axis quantification + GEE decomposition + 100-point scale 超越 Thurstone。共识：将 novelty 从 "discovering the Blindspot" 调整为 "providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges"；将 "the first framework" 改为 "a unified framework"。
— R2 提出 (N1)，R1 AGREE（含 nuance）。Director 判定 Must-Fix（framing 层面可修复）

### Strong Should-Fix（不一票否决但显著影响评分）

**SF1 [warning, 分歧] 缺少 human validation，detection vs. amplification 未充分解决。**
论文六个 controls 排除了 specific artifacts，但无法在根本上区分 "pairwise 检测了真实偏差" 和 "pairwise 放大了微弱偏好"（Comparative Trap, Jeong et al. 2025）。唯一能解决此问题的是 human evaluation（至少一小组 pairs 的 Likert + pairwise 人类评估）。R2 列为 Must-Fix，R1 同意方向但建议降为 Strong Should-Fix（论文核心贡献是 methodology + empirical demonstration，非 resolve interpretive question）。Director 判定 Strong Should-Fix：Limitations 中应明确承认此为主要开放问题。
— R2 提出 (N2)，R1 AGREE 方向但降级

### Should-Fix（影响评分但不一票否决）

**W1 [warning, 共识] BT 模型 IIA 假设未讨论。**
Appendix H 发现 formality 存在显著方向异质性（68.9% vs. 52.6%, Fisher p=0.015），BT 单参数公式可能遗漏效应异质性。需承认 IIA 假设并报告 direction-stratified BT。
— R1 提出 (W2)，R2 AGREE

**W2 [warning, 共识] NLI gate FNR 估计样本量过小。**
FNR 基于仅 12 个 rejected pairs（Wilson 95% CI ≈ [2%, 28%]），CI 极宽。GPT-4o cross-validation 报告了 precision 但未报告 FNR CI。需量化报告。
— R1 提出 (W3)，R2 AGREE

**W3 [warning, 共识] Verbosity direction-aware gating 可能引入 selection bias。**
Direction-aware gate 额外放入 21 pairs (+32%)，但这些 pairs 与 bidirectional-pass pairs 的特征可能不同。需报告两组分别的 BT estimates 作对比。
— R1 提出 (W4)，R2 AGREE

**W4 [warning, 共识] 3 个风格轴限制 "framework" 泛化声明。**
Register 仅 exploratory，实质只有 2 轴有 confirmatory evidence。CSD 方法论 axis-agnostic，但 "framework" 措辞暗示更广适用性。建议改为 "methodology"，Limitations 中列出未覆盖轴。
— R2 提出 (W1)，R1 AGREE

**W5 [warning, 共识] Measurement attenuation vs. construct divergence 歧义影响核心叙事。**
"Blindspot" 术语偏向 attenuation 解释。如果 construct divergence 成立，Likert 并非 "盲"，而是测量不同构念。论文 §5.2/§6/Limitations 已有 balanced discussion，但标题和 Abstract framing 偏颇。至少在 Abstract 结尾加 caveat。
— R1 提出 (W5)，R2 AGREE

**W6 [warning, 共识] 生态效度讨论不足。**
Controlled manipulation → naturalistic evaluation 的 generalizability gap 未讨论。自然文本中 style 和 content 共变，NLI gate 无法直接应用。
— R1 提出 (W6)，R2 AGREE

**W7 [warning, 部分共识] Rewriting artifact 的 style-specific polishing interaction 未讨论。**
Same-style double-rewrite 控制 style-neutral polishing，但 formal rewriting 的 polishing 可能不同于 casual rewriting。Formality 方向异质性可能混合 originality confound 和 style-specific polishing。
— R2 提出 (W4)，R1 PARTIALLY AGREE

**W8 [warning, 共识] Introduction motivating example 需 acknowledge formality-quality nuance。**
"Average height" 例子暗示 formality bias 完全不合理，但论文自己的 GEE 结果显示 formality 存在 significant Originality effect——偏好 formal 文本可能部分反映合理质量判断。
— R2 提出 (W5)，R1 AGREE

### Minor

- **M1**: Abstract 首句 "near-perfect correlation" 过于绝对（76–92% ≠ near-perfect）。改为 "strong correlation"。（R2 提出，R1 AGREE）
- **M2**: Figure 2 (DAG) 尺寸偏小，颜色编码在低 DPI 下辨认困难。（Visual Check + R2）
- **M3**: Pages 3–4 连续纯文本无 figure/table 穿插，视觉单调。建议将 Figure 2 前移。（Visual Check）
- **M4**: Table 1 信息密度过高，建议增加 reading guide 或拆分。（R2 提出，R1 AGREE）
- **M5**: §4.1 GEE exchangeable correlation 假设 justification 缺失。（R2-M3）
- **M6**: Appendix 连续 4 页 12 张表格形成 "表格墙"。（Visual Check）
- **M7**: NLI threshold 0.90 在主文缺 inline justification，需读者翻到 Appendix E。建议 §3.2 加一句简要说明。（R2-Q1，R1 AGREE）

---

## Reviewer Consensus

| Issue | R1 | R2 | 共识 |
|-------|----|----|------|
| MF1: Primary family transparency | 提出 (N1) | AGREE | **Must-Fix** |
| MF2: Cross-rewriter coverage | 提出 (N2) | AGREE (contextualize) | **Must-Fix** |
| MF3: TOST Δ too wide | 提出 (N3) | AGREE (= W3) | **Must-Fix** |
| MF4: Novelty positioning | AGREE (nuance) | 提出 (N1) | **Must-Fix** |
| SF1: Human validation gap | AGREE (downgrade) | 提出 (N2) | **Strong Should-Fix** |
| W1-W8: 8 Should-Fix issues | 见上 | 见上 | **Should-Fix** |
| M1-M7: 7 Minor issues | 见上 | 见上 | **Minor** |

---

## Reviewer Divergence

**分歧 1：因果框架表述一致性（R1-W1）**
R1 认为全文因果术语不一致（"Controlled Style Decomposition" + DAG 暗示因果，§3.5 hedge 为 interventionist）。R2 REBUT：§3.5 的 caveat 恰当，"controlled" 指实验操控而非因果推断，DAG 常被用作 design rationale。**Director 判定：R2 REBUT 成立。** §3.5 的 hedge 措辞清晰，"controlled" 在实验设计语境下准确。仅建议在 §3.5 开头加一句统一声明。降为 Minor。

**分歧 2：Likert vs. pairwise 比较的方法论公平性（R1-Q5）**
R1 担忧不同统计效率的方法在同一样本量下比较对 Likert 不公平。R2 REBUT：Power analysis（Appendix K）+ 100-point continuous Likert（Appendix M）双重证据已表明问题超越简单样本量差异——Likert 模式下 judges 根本不产生 score variance，是 paradigmatic limitation 而非 power limitation。**Director 判定：R2 REBUT 成立。** 但建议在 §5.2 更明确回应此公平性 concern。

---

## Questions（需要作者澄清）

1. Primary family 包含哪三个 judges？排除第四个的理由？是否有 pre-registration？
2. Cross-rewriter independence test 仅覆盖 Qwen3-32B 是否资源约束？能否至少对 GPT-4o as judge 补一个小规模验证？
3. Claude Sonnet 4 TOST 在 n=87 下能 reject 的最小 Δ 是多少？
4. 是否考虑过 direction-stratified BT（按 original text direction 分层估计 win probability）？
5. LLMBar 100 pairs 是从完整 benchmark 中 sample 还是用了全集？
6. 100-point continuous Likert 仅用 Qwen3-32B，其他 judges 是否也显示相同 pattern？
7. GEE formality interaction term 的 point estimates 和 direction？（即使不显著）

---

## Missing References

1. **Girrbach et al. (2025/2026)** "Likert or Not" — LLM Likert 评分行为研究，与 Appendix M 直接相关（R2 建议，需验证真实性）
2. **PRePair** (Jeong et al., 2025) — pairwise + pointwise 整合方法，可能是缓解 Blindspot 的替代方案（R2 建议）
3. **Acquiescence bias / central tendency bias** — Likert scale 经典问题，§2 中一句话 mention 即可（R2 建议，R1 AGREE）

---

## External Review

**外部审稿：未启用。** 本轮未配置 Stanford Agentic Reviewer。

---

## Visual Layout Check（非评分项）

**状态：已完成** (done, 耗时 ~3 min)

| 严重度 | 数量 | 主要发现 |
|--------|------|----------|
| Critical | 0 | — |
| Warning | 1 | Pages 3–4 连续纯文本无图表穿插，视觉单调。建议将 Figure 2 (DAG) 前移至 §3.5 首次引用处 |
| Info | 10 | Table 1 信息密度高但可读；Figure 2 尺寸偏小；Figure 3/4 灰度区分良好；Appendix "表格墙"；booktabs 格式规范统一；参考文献无未解析引用 |

---

## Overall Assessment

**Overall Score: 3.5 / 5 — Borderline Conference**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 3.0 | 3.25 |
| Reproducibility | — | 4.0 | 4.0 |
| Confidence | 4 | 4 | 4 |

**支持 Conference (4.0) 的因素：**
- 实验设计严谨度远超该领域平均水平（NLI gate + negative control + 7 种统计方法 + 100-point Likert + cross-benchmark + cross-rewriter + formal power analysis）
- Likert Blindspot 的 empirical quantification 对 LLM evaluation 社区有直接实用价值
- GEE per-axis confound decomposition 是 genuinely novel 的分析贡献
- 五个 judges 跨三个 benchmark 的一致性令人信服
- Appendix A–P 展示了出色的 rigor

**拉向 Findings (3.0) 的因素：**
- 核心概念（forced-choice > rating）在 psychometrics 中已有近百年历史；novelty 定位需更诚实
- Primary family 构成透明度不足，影响 FWER 控制可信度
- Cross-rewriter 验证仅覆盖 1/4 judges，限制 rewriter-independence claim
- TOST negative control 功效不足（Δ=15pp 几乎涵盖最小 confirmed bias）
- 缺少 human validation 区分 detection vs. amplification
- 仅 3 个风格轴限制 framework 级别泛化

**净判断：** 论文处于 Conference 和 Findings 边界。实验执行质量高，但多个方法论透明度问题（MF1 primary family、MF3 TOST）和 novelty 定位（MF4）需要在修改中解决。MF1/MF3 是纯写作/分析补充问题，可在一轮修改中完成。MF4（novelty reframing）需要调整叙事策略但不改变实验。SF1（human validation）是结构性限制，可通过 Limitations 重写部分 mitigate。如果 MF1–MF4 均得到充分回应，论文有潜力达到 4.0 (Conference)。

---

## Detailed Comments（逐节）

### Abstract
信息密度高但可接受。"near-perfect correlation" 应改为 "strong correlation"（76–92% ≠ near-perfect）。GEE per-axis confound structure 的描述清晰且增量准确。建议移除部分括号内统计数字以降低认知负荷。

### Section 1 (Introduction)
Opening example 直观有效。但需 acknowledge formality-quality nuance：formality 改变可能合法影响 perceived quality（论文自己的 GEE 结果支持此点）。"black-box controlled framework" 表述准确（black-box 指 judge 而非 pipeline），但 "framework" 可改为 "methodology"。Contributions 列表清晰，item 1 的 "the first" 应改为 "a unified"。

### Section 2 (Related Work)
覆盖面广且组织良好。对 RATE 的对比公平。可补充 Likert scale 在社会科学中的经典问题（acquiescence bias, central tendency bias）一句话。

### Section 3 (Method)
§3.1 rewriting protocol 清晰。§3.2 NLI gate 设计精巧（bidirectional + direction-aware）。§3.3 measurement protocol 标准。§3.5 Design Rationale 的 DAG 和三个识别假设清晰，caveat 措辞恰当。假设 (iii)（style rewrite 不引入 target axis 之外的系统差异）最难验证，same-style DR 仅部分检验。

### Section 4 (Experiments)
§4.1 statistical framework 需明确 primary family 组成（MF1）。LLMBar n=100（NLI 后 n=88）是 moderate 样本；scaled replication n=355 仅覆盖一个 cell，对 generalizability 支持有限。

### Section 5 (Analysis)
§5.1 NLI gate validation thorough（FNR 8.4%, precision 98.9%, AC1=0.89），但 FNR 样本过小（n=12, CI 宽）。§5.2 核心发现清晰呈现；七方法 sensitivity hierarchy 有说服力。§5.3–5.4 cross-judge 和 cross-axis replication 增强结论稳健性。§5.5 register 过于压缩但在 8 页限制下可理解。§5.6 GEE decomposition 是论文第二主要贡献。

### Section 6 (Conclusion)
适当总结两个主要发现。"whether measurement attenuation or construct divergence" 的 open question 处理诚实。

### Limitations
覆盖了关键 weak points（evaluator-producer bias, methodology/scale, validation）。遗漏项：(1) 缺少 human validation 作为最主要的 open question；(2) 3 轴 coverage limitation；(3) 生态效度；(4) style-specific polishing interaction。

### 格式合规
- 正文 ≤8 页 ✓
- Double-blind 匿名 ✓（"Anonymous ACL submission"，未发现自引泄漏）
- ACL 双栏格式 ✓
- Limitations 章节 ✓（3 段，覆盖适当，不过长）
- ARR Checklist 不在 PDF 中 ✓
- 参考文献格式一致 ✓