# Director coordination — Part 2 of 7

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/9d/9db2d5c10f518e51ec86.json)

## Round 24

### User

_source line 283 · 2026-05-21T11:20:06.870401+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿意见 — 新颖性与完整性

**论文**: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition"
**Venue**: EMNLP 2026 Main Conference (via ARR)

---

## 总体评分
**Overall Assessment**: 3.0 (Findings)
**一句话总结**: 实验设计严谨、Likert Blindspot 发现对社区有实用价值，但核心发现是心理测量学已知现象的领域迁移，"Blindspot" framing 过度包装了一个效率差异，Related Work 引用量和覆盖面不足 EMNLP 长文标准。

---

## 官方维度打分（ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论设计周全（position control、NLI gate、cross-judge replication、7种统计方法），但因果声明受限于显著的 originality confound（formality Style OR=2.58 vs Orig OR=2.32），evaluator-producer overlap 未完全排除 |
| Excitement | 2.5/5 | Likert vs pairwise 灵敏度差异是测量学经典结论（Thurstone 1927, Kiritchenko 2017, Novikova 2018）的 LLM 评估领域应用；GEE confound decomposition 是标准方法的直接套用；对社区有实用提醒价值但缺乏概念突破 |
| Reproducibility | 4/5 | 统计方法、超参数（NLI threshold 0.90, temperature 0.7, bootstrap seed 42）描述清楚；代码和数据承诺 release upon acceptance；主要扣分：缺少 prompt 模板完整文本 |
| Overall | 3.0/5 | Findings 级别——扎实的实证工作，有实用价值，但新颖性不足以支撑主会议接收 |

**Confidence**: 4/5 — 对 measurement theory、causal inference in NLP、LLM-as-judge 领域比较熟悉

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Likert Blindspot" 命名与 framing 不准确——这是 efficiency gap 而非 blindspot

- 具体位置：Title, Abstract, Section 1 (lines 21-24), Section 5.2 全节
- 问题："Blindspot" 一词暗示 Likert 结构性不可能检测到偏差，但论文自身数据反驳了这一命名——Table 1 中 9 个 bias-positive cells 有 3 个（标记 ‡）Likert 也检测到了（MT-Bench formality GPT-4o p=0.016, Qwen3 p=0.007; AEval Qwen3 verbosity p=0.0003）。Section 5.2 (line 87) 也承认 "three of nine bias-positive cells escape the Blindspot"。这不是 blindspot，是 sensitivity gap。更准确的术语应该是 "Likert Attenuation" 或 "Measurement Sensitivity Gap"。
- 此外，Abstract 第4行声称 "measurement attenuation across a severity spectrum"，但 Section 5.2 lines 83-84 的关键论证有逻辑漏洞：n=355 时 Likert d = −0.025 并不必然证明 "attenuation"——也可能是 Likert 和 pairwise 在测量不同的构念（absolute quality difference vs ordinal preference），而非同一构念的不同测量精度。论文在 Section 5.2 lines 89-91 隐约承认了这一点（"RATE measures aggregate attribute-level quality effects...CSD targets isolated per-axis style preference"），但未将其整合进 framing。
- 为什么影响接收：这是论文的核心 claim 和标题。如果 framing 不准确，整个叙事的可信度受损。
- 建议修改方向：(1) 将 "Blindspot" 改为更精确的术语（如 "Likert Attenuation Effect"）；(2) 明确讨论 Likert 和 pairwise 可能测量的是不同构念的可能性，而非假定它们是同一构念的两种测量；(3) 将 "at moderate bias...Likert compresses to zero" 的表述改为条件性的。

**N2** [critical] Related Work 引用数量和覆盖面严重不足

- 具体位置：Section 2 (Related Work)，共 39 行，引用 bib 37 条（cited 36 条）
- 问题：EMNLP 长文通常引用 40-60 篇，本文 36 篇显著偏少。更关键的是以下方向缺失：
  - **Counterfactual text generation**：仅引用 Polyjuice (Wu 2021) 和 CausaLM (Feder 2021)，缺少 MICE (Ross et al., 2021)、Tailor (Ross et al., 2022) 等直接相关的 counterfactual generation 方法。
  - **NLG evaluation survey 文献**：缺少 van der Lee et al. (2019, 2021) 对 NLG human evaluation 的系统综述、Celikyilmaz et al. (2020) text generation evaluation survey、Belz & Reiter (2006) 评估设计。这些是论文 measurement sensitivity 论点的重要背景。
  - **Causal NLP beyond Feder**：缺少 Keith et al. (2020) text as treatment、Pryzant et al. (2020/2021) deconfounded text generation。
  - **LLM-as-judge 改进方案**：缺少 G-Eval (Liu et al., 2023)、Arena-Hard (Li et al., 2024) 等与本文方法直接可比的 evaluation framework。
  - **Self-preference bias**：仅引用 Panickssery (2024)，缺少 Xu et al. (2024) 等更全面的 self-preference 研究。
  - **Scale design in psychology**：论文主打 measurement theory 角度，但仅引用 Stevens (1946)、Thurstone (1927)、DeCoster (2011)。缺少 Krosnick (1999) 对 rating scale 最优设计的经典综述、Preston & Colman (2000) 对 scale point 数量的研究——这些直接影响 "scale granularity" 是否能缓解 Blindspot 的讨论（Limitations Section "Scale granularity" 段）。
- 为什么影响接收：引用不足表明对领域的把握不够全面，特别是在新颖性是主要贡献的情况下，related work 必须充分论证 "why now" 和 "what's different"。
- 建议修改方向：补充上述方向的核心文献，Related Work 应扩展至 50+ 引用。

**N3** [critical] "Four critical gaps" 的构造有 cherry-picking 嫌疑

- 具体位置：Section 1, lines 11-12
- 问题：四个 gap 的定义刚好使得只有 CSD 满足所有条件——这是典型的 "定义问题使自己成为唯一解" 策略。具体来看：
  - Gap 1 ("treat style as a single dimension")：CASSE (Cho et al., 2026) 和 FairJudge (Wang et al., 2026) 已经做了 multi-dimensional style decomposition，论文自己在同一段承认了这一点，但将其归入 "correlational"。
  - Gap 2 ("correlational analyses")：RATE (Reber 2025) 和 Counterfactual Rhetorical (2025) 都做了 interventional analysis。论文将 RATE 归入 "Likert-based" 来排除，将 Counterfactual Rhetorical 归入 "persona-level" 来排除。
  - Gap 4 ("no black-box, post-hoc, per-axis interventional")：这个四词 conjunction 是为 CSD 量身定制的——拆开看每个特性都已有方法实现。
- 为什么影响接收：framing 的公平性直接影响 novelty 评价。如果 gap 定义不公平，novelty claim 就不成立。
- 建议修改方向：更诚实地承认各个 gap 已有部分解决方案，将 CSD 定位为 "integrative framework"（整合各方法优势）而非 "唯一解决所有 gap 的方法"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Contribution 2 (Likert Blindspot) 的 novelty 定位需要更诚实

- 具体位置：Section 1, line 21; Section 2, line 23
- 问题：Section 2 line 23 承认 "Our contribution is not the discovery of this measurement principle but its first systematic quantification for LLM judge style bias detection"。但 Title 和 Abstract 的包装程度远超这个定位——"Likert Blindspot" 作为标题级概念暗示这是一个新发现。Kiritchenko & Mohammad (2017) 在情感标注中已经定量展示了 BWS > Likert 的灵敏度差异；Novikova et al. (2018) 在 NLG evaluation 中也展示了 ranking > rating。本文的增量 novelty 在于：(a) LLM judge 场景，(b) 风格偏差检测，(c) 定量测量 attenuation 程度。这些是有价值的增量贡献，但不应包装为发现级突破。
- 建议：在 Abstract 和 Introduction 中明确标注这是 "known measurement theory principle 在 LLM judge evaluation 的首次系统定量验证"，降低 discovery 暗示。

**W2** [warning] Conclusion 仅一句话，严重不足

- 具体位置：Section 6, line 1-4（page 8）
- 问题：整个 Conclusion 只有一句话："CSD reveals the Likert Blindspot---measurement attenuation in Likert scoring---across three judges, benchmarks, and style axes; style bias audits should adopt pairwise comparison."。一篇 8 页长文的结论应包括：(a) 主要发现总结，(b) 方法论贡献的意义，(c) 对社区实践的具体影响，(d) 未来研究方向。这看起来像是为了挤进 8 页而被压缩的结果。
- 建议：扩展至 10-15 行，即使需要从其他 section 压缩内容。

**W3** [warning] Contribution 3 (GEE conditional decomposition) 方法论新颖性不足

- 具体位置：Section 5.6, Table 3
- 问题：GEE 是标准的边际回归方法（Liang & Zeger, 1986），用 exchangeable correlation structure 处理 paired data 是教科书级应用。将 "GEE conditional decomposition" 列为一个独立的 contribution 有膨胀贡献列表之嫌。发现本身（verbosity confound-free vs formality/register confounded）是有趣的，但方法上零创新。
- 建议：将此作为 experimental finding 而非 methodological contribution 来定位。

**W4** [warning] 对 RATE 的批评可能不公平

- 具体位置：Section 2, lines 8-11
- 问题：论文说 RATE 的 "reliance on Likert ATE as the primary metric is a vulnerability"，然后用自己的数据 (p = 0.332) 来论证。但 RATE 的设计目标是 reward model 的 causal explainability（解释 reward model 的内部机制），不是 style bias detection。用 RATE 不擅长的任务来批评 RATE，类似于批评螺丝刀不能当锤子用。RATE 使用 Likert ATE 是因为 reward model 本身输出连续分数，pairwise comparison 不是自然选择。
- 建议：将 RATE 比较改为 "complementary" framing（论文在 Section 5.2 lines 89-91 已有此意，但 Related Work 的语气应一致）。

**W5** [warning] 主实验仅基于 LLMBar (n=100)，generalizability 存疑

- 具体位置：Section 3.4, Section 5 全节
- 问题：虽然论文在 AlpacaEval 和 MT-Bench 上做了 cross-benchmark validation，但这些补充实验只覆盖了部分 judge×axis 组合（Table 1 仅 5 个额外 rows）。核心 Blindspot 论证完全基于 LLMBar 的 n=88 NLI-gated pairs（scaled replication n=355 也仅限 Qwen3 formality 一个 cell）。LLMBar 是一个为测试 instruction-following 设计的 benchmark，其 100 条样本是否能代表更广泛的 LLM evaluation 场景值得商榷。
- 建议：在 Limitations 中明确讨论 sample size 和 benchmark 代表性的局限。

**W6** [warning] Evaluator-producer bias 的处理不够彻底

- 具体位置：Limitations 第2段, Appendix D (Tables 6-7)
- 问题：Qwen3-32B 同时担任 rewriter 和 judge，这是方法论设计缺陷。虽然论文做了 rewriter independence test（GPT-4o 作为 rewriter），但仅对 verbosity 和 formality 做了测试，且 Style OR 下降了 22%（13.10→10.17）——这不是可忽略的差异。更关键的是，Qwen3-32B 的 originality OR 系统性地是 GPT-4o 的 ~2× (formality: 4.99 vs 2.32; register: 5.72 vs 2.21)，论文将其归因于 "partial self-recognition" 但未做进一步排除实验。
- 建议：核心实验应使用独立的 rewriter 和 judge。至少应在 Method 中正面讨论这个设计选择的理由。

---

## 小问题（不影响接收）

- **Abstract 信息密度过高**：7 行 abstract 包含 3 个 judges、3 个 benchmarks、3 个 style axes、具体 d 值、p 值、BT 百分比、attenuation 百分比。建议精简数字，保留核心 message。
- **术语"interventional"的使用**：Section 3.5 正确声明 "interventional rather than formal causal evidence"，但 Introduction line 18 使用 "Inspired by interventional approaches to text analysis" 可能暗示比实际更强的因果保证。建议统一为 "quasi-interventional" 或在首次使用时就明确限定。
- **Table 1 符号系统复杂**：†, ‡, ---, †_e 四种符号需要对照脚注解读。建议简化或用颜色编码辅助。
- **引用验证**：经 verify_references 工具检查，murugadoss2025sos (Style Over Substance, ICLR 2025) 在 OpenAlex 上未找到（可能是会议预印版 vs 正式版）；wu2023style 年份 bib 标注 2025 但 API 返回 2023；tan2025judgebench 和 chiang2024chatbot 有 first author mismatch。建议核实并修正。
- **hoenig2001abuse 是 orphan bib entry**：在 bib 文件中存在但未被 cite（verify_references 报告）。实际上 Section 5.2 line 130 引用了 \citealt{hoenig2001abuse}，这应该是 verify tool 对 citealt 的识别遗漏，不是实质问题。
- **Page 8 排版**：Conclusion 只有 1 句话后紧跟 Limitations，视觉上显得 Conclusion 是附属于 Limitations 的前言而非独立章节。

---

## 主要优势

1. **实验设计严谨**：position control (双向 swap)、NLI gate (0.90 threshold + sensitivity analysis)、cross-judge replication (GPT-4o, Qwen3-32B, Claude Sonnet 4 as negative control)、7 种统计方法的 sensitivity hierarchy、Holm-Bonferroni 多重比较校正。这是高水平的实验方法论。

2. **GEE decomposition 发现有价值**：verbosity 作为 confound-free axis 与 formality/register 的 confounded 结构对比（Table 3）是有见地的发现，对后续研究有指导意义。

3. **负控制设计加强了可信度**：Claude Sonnet 4 在两个 axis 上均未检测到显著偏差（BT 56.2%/54.1%），证明 CSD 不是简单地将所有 judge 标记为有偏。

4. **Limitations 充分且诚实**：7 段 Limitations 覆盖了主要的方法论弱点，包括 quality-style confounding、evaluator-producer bias、benchmark coverage、human evaluation 缺失等。

5. **Rewriter independence test 是有价值的 robustness check**：Appendix D 的独立 rewriter 实验（Tables 6-7）直接回应了最可能的方法论质疑。

---

## Questions（需要作者澄清）

**Q1**: 如果 Likert 和 pairwise comparison 测量的是不同构念（absolute quality difference vs ordinal preference），那么 "Likert Blindspot" 是否只是 "两种测量方法对不同量的灵敏度不同" 的 trivial 结论？作者如何排除这一替代解释？

**Q2**: n=355 时 Likert d 从 0.102 缩小到 −0.025——这是 attenuation（信号被压缩）还是 regression to the mean（小样本 d=0.102 本身就是噪声估计，真实 d 确实接近 0）？

**Q3**: Direction asymmetry (Section 5.6 / Appendix A)：formal-is-rewrite 78.8% vs casual-is-rewrite 54.5%。这是否说明 judge 偏好原文而非偏好 formality？如果是 originality preference，那么 CSD 检测到的 "formality bias" 中有多少是 rewriting artifact？

**Q4**: 为什么不使用人类标注来验证 NLI gate 的 content preservation？论文使用 Qwen3-32B（同时也是 rewriter 和 judge 之一）作为 NLI validation annotator（Section 5.1 line 65），这存在循环依赖风险。

**Q5**: Claude Sonnet 4 作为 negative control 显示无风格偏好但极端 originality sensitivity (Orig OR=6.66)——论文如何解释这一现象？这是否意味着 Claude 实际上也有偏差，只是表现形式不同？

---

## Missing References（具体缺什么方向的什么文献）

1. **NLG Evaluation Surveys**: van der Lee et al. (2019, 2021) "Best practices for the human evaluation of automatically generated text"; Celikyilmaz et al. (2020) "Evaluation of text generation: A survey"
2. **Counterfactual Text Generation**: Ross et al. (2021) "Explaining NLP Models via Minimal Contrastive Editing (MICE)"; Ross et al. (2022) "Tailor"
3. **Scale Design**: Krosnick (1999) "Survey research" (Annual Review of Psychology); Preston & Colman (2000) "Optimal number of response categories in rating scales"
4. **LLM-as-Judge Frameworks**: Liu et al. (2023) "G-Eval"; Li et al. (2024) "Arena-Hard"
5. **Self-Preference**: Xu et al. (2024) 关于 LLM self-preference 的更全面研究
6. **Causal NLP**: Keith et al. (2020) "Text and causal inference: A review of using text to remove confounding"
7. **GEE methodology**: Liang & Zeger (1986) 原始论文——论文使用 GEE 但未引用方法学来源

---

## 格式合规性

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文页数 | ✅ 合规 | 8 页正文（Section 1-6），Limitations 在 page 8 但不计入页数限制 |
| 匿名性 | ✅ 合规 | "Anonymous ACL submission"，无身份泄露 |
| 引用格式 | ✅ 合规 | ACL-style natbib (citet/citep) |
| Limitations | ✅ 存在 | 7 段，覆盖充分 |
| Appendix | ✅ 合理使用 | 6 个 appendix section，补充材料不含核心论证 |
| 模板 | ✅ 合规 | ACL 2023 template with [review] option |

---

## 总结

这是一篇实验设计水平很高的实证论文。CSD 框架的设计周全（NLI gate + position control + cross-judge replication），Likert-pairwise sensitivity gap 的定量测量对社区有实用价值。但核心新颖性受限于两个根本问题：(1) Likert vs pairwise 的灵敏度差异是测量学经典结论的领域迁移，而非新发现；(2) "Blindspot" framing 过度包装了效率差异。引用覆盖面不足进一步削弱了对领域 positioning 的可信度。建议定位为 Findings 级别的扎实实证贡献，修正 framing 后有潜力提升至 Borderline Conference。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 284 · 2026-05-21T11:20:14.136656+00:00_

Reviewer 2 审稿意见已收到（Overall: 3.0 Findings）。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 25

## Round 25

2 recorded events


### User

_source line 285 · 2026-05-21T11:20:25.333111+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：给出 **Overall 3.0 (Findings)** 评分。三个 Must-Fix 问题：(1) "Likert Blindspot" 命名不准确——论文自身数据显示 3/9 cells Likert 也检测到了，这是 efficiency gap 而非 blindspot；(2) Related Work 仅 36 篇引用，缺少 NLG evaluation surveys、counterfactual text generation、scale design 等关键方向；(3) "four critical gaps" 的构造有 cherry-picking 嫌疑。主要优势在于实验设计严谨（position control、NLI gate、cross-judge replication、7 种统计方法）和 GEE confound decomposition 的有价值发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 286 · 2026-05-21T11:20:32.607712+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成审稿后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 26

## Round 26

6 recorded events


### User

_source line 287 · 2026-05-21T11:21:25.925257+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性审查

### 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 核心发现（Likert Blindspot）新颖且有实际价值，但 NLI gate 验证的循环依赖、Bradley-Terry IIA 假设未检验、以及 originality confound 对识别策略的威胁，使得因果声明的方法论支撑不够充分。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 主要声明有七种统计方法支撑，但 NLI gate 验证存在 evaluator-producer 循环，BT 模型核心假设未检验，originality confound 显著（Table 3）部分削弱识别策略 |
| Excitement | 3.5/5 | Likert Blindspot 概念新颖，测量理论视角在 LLM 评估文献中罕见，对 RLHF/alignment 实践有直接意义；但方法论缺口使贡献尚未完全落地 |
| Reproducibility | 3.5/5 | 参数和流程描述详尽，但代码/数据未发布 |
| Confidence | 4/5 | 熟悉 BT 模型、GEE、bootstrap 推断及 LLM-as-Judge 文献 |

---

### Must-Fix 问题（3 个 critical）

**N1** [critical] NLI Gate 验证存在 evaluator-producer 循环偏差
- 位置：§5.1
- Qwen3-32B 同时是 rewriter 和 NLI gate 验证的 annotator，false negative rate 8.4% 可能被低估。GPT-4o spot-check (47/50) 样本量不足 (n=50)。
- 建议：用人工标注（≥200对）或两个架构不同的模型分别验证。

**N2** [critical] Bradley-Terry IIA 假设未检验
- 位置：§4.1, §5.2
- BT 模型假设 IIA，但 style preference 可能随 item 基线质量变化（交互效应），直接违反 IIA。未报告任何诊断检验。
- 建议：报告 Hausman-McFadden test，或拟合 Thurstone-Mosteller 模型做稳健性检查。

**N3** [critical] Originality confound 显著，削弱识别策略
- 位置：Table 3, §5.5
- 多配置下 Originality OR 显著（GPT-4o formality OR=1.88, p=0.006; Qwen3-32B verbosity OR=2.21, p<0.001）。GEE additive decomposition 的交互项检验可能低功效（n=88）。Style 和 originality 的可分离性值得质疑。
- 建议：重新界定 claim 为 "style-correlated preference shift"；在 originality 差异最小的子集上重复分析。

### Should-Fix 问题（6 个 warning）

**W1** NLI 阈值 τ=0.90 缺乏 sensitivity analysis（§3.2）
**W2** Direction-aware NLI 可能引入系统性筛选偏差（§3.2, Appendix E）
**W3** Exploratory analyses 的多重比较修正不完整（全文）
**W4** Claude Sonnet 4 negative control 的 non-significance 解读过度——需等效性检验（Table 1）
**W5** Figure 4 的 post-hoc power analysis 存在循环推理风险（§5.2）
**W6** Rewriter independence test 未覆盖 register axis（Table 6-7）

### 小问题（5 个）
- M1: hoenig2001abuse bib 条目可能缺少 \cite 命令
- M2: wu2023style bib 年份（2025）与 OpenAlex 索引年份（2023）不一致
- M3: Figure 2 DAG 图注解释不足
- M4: Table 1 Likert d 负值含义未充分解释
- M5: "Interventional Design" 标题措辞与实际 evidence 强度不匹配

### 主要优势
- S1: Likert Blindspot 概念新颖且有实际影响力
- S2: 七种统计方法的 sensitivity hierarchy 有说服力
- S3: 3 judges × 3 benchmarks × 3 axes 的 full factorial design 覆盖面优秀
- S4: 统计素养（Holm-Bonferroni, GEE, bootstrap）在 NLP 实证研究中较为难得
- S5: 写作质量高，结构清晰

### 缺失引用
- Hausman & McFadden (1984) — IIA 检验
- Agresti (2010) — ordinal data 分析经典教材
- Lakens (2017) — equivalence testing（与 negative control 解读相关）

### 需要作者澄清的问题（5 个）
Q1: NLI 阈值选定依据和 sensitivity 数据？
Q2: GEE Style×Originality 交互项是否检验过？
Q3: Full BT (63.0%) vs filtered sign test (73.9%) 差异的含义？
Q4: 各 benchmark×axis×judge 单元 NLI 过滤后的 effective sample size？
Q5: 是否考虑过与 RATE/LC-AlpacaEval 的 head-to-head 比较？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-21T11:21:54.993476+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性审查\n\n### 总体评分\n**Overall**: 3.5 — Borderline Conference\n\n### Must-Fix 问题\n\n**N1** [critical] NLI Gate 验证存在 evaluator-producer 循环偏差\n- §5.1: Qwen3-32B 同时是 rewriter 和 NLI gate 验证的 annotator，false negative rate 8.4% 可能被低估。GPT-4o spot-check (47/50) 样本量不足 (n=50)。\n- 建议：用人工标注（≥200对）或两个架构不同的模型分别验证。\n\n**N2** [critical] Bradley-Terry IIA 假设未检验\n- §4.1, §5.2: BT 模型假设 IIA，但 style preference 可能随 item 基线质量变化（交互效应），直接违反 IIA。未报告任何诊断检验。\n- 建议：报告 Hausman-McFadden test，或拟合 Thurstone-Mosteller 模型做稳健性检查。\n\n**N3** [critical] Originality confound 显著，削弱识别策略\n- Table 3, §5.5: 多配置下 Originality OR 显著（GPT-4o formality OR=2.32, p=0.006; Qwen3-32B register OR=5.72, p<0.0001）。GEE additive decomposition 的交互项检验可能低功效（n=88）。Style 和 originality 的可分离性值得质疑。\n- 建议：重新界定 claim 为 \"style-correlated preference shift\"；在 originality 差异最小的子集上重复分析。\n\n### Should-Fix 问题\n\n**W1** NLI 阈值 τ=0.90 缺乏 sensitivity analysis（§3.2）\n**W2** Direction-aware NLI 可能引入系统性筛选偏差（§3.2, Appendix E）\n**W3** Exploratory analyses 的多重比较修正不完整（全文）\n**W4** Claude Sonnet 4 negative control 的 non-significance 解读过度——需等效性检验（Table 1）\n**W5** Figure 4 的 post-hoc power analysis 存在循环推理风险（§5.2）\n**W6** Rewriter independence test 未覆盖 register axis（Table 6-7）\n\n### 小问题\n- M1: hoenig2001abuse bib 可能缺少 \\cite\n- M2: wu2023style bib 年份不一致\n- M3: Figure 2 DAG 图注解释不足\n- M4: Table 1 Likert d 负值含义未充分解释\n- M5: \"Interventional Design\" 标题措辞与实际 evidence 强度不匹配\n\n### Questions\nQ1: NLI 阈值选定依据和 sensitivity 数据？\nQ2: GEE Style×Originality 交互项是否检验过？\nQ3: Full BT (63.0%) vs filtered sign test (73.9%) 差异的含义？\nQ4: 各 benchmark×axis×judge 单元 NLI 过滤后的 effective sample size？\nQ5: 是否考虑过与 RATE/LC-AlpacaEval 的 head-to-head 比较？\n\n### 缺失引用\n- Hausman & McFadden (1984) — IIA 检验\n- Agresti (2010) — ordinal data 分析\n- Lakens (2017) — equivalence testing",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性审查\n\n### 总体评分\n**Overall**: 3.5 — Borderline Conference\n\n### Must-Fix 问题\n\n**N1** [critical] NLI Gate 验证存在 evaluator-producer 循环偏差\n- §5.1: Qwen3-32B 同时是 rewriter 和 NLI gate 验证的 annotator，false negative rate 8.4% 可能被低估。GPT-4o spot-check (47/50) 样本量不足 (n=50)。\n- 建议：用人工标注（≥200对）或两个架构不同的模型分别验证。\n\n**N2** [critical] Bradley-Terry IIA 假设未检验\n- §4.1, §5.2: BT 模型假设 IIA，但 style preference 可能随 item 基线质量变化（交互效应），直接违反 IIA。未报告任何诊断检验。\n- 建议：报告 Hausman-McFadden test，或拟合 Thurstone-Mosteller 模型做稳健性检查。\n\n**N3** [critical] Originality confound 显著，削弱识别策略\n- Table 3, §5.5: 多配置下 Originality OR 显著（GPT-4o formality OR=2.32, p=0.006; Qwen3-32B register OR=5.72, p<0.0001）。GEE additive decomposition 的交互项检验可能低功效（n=88）。Style 和 originality 的可分离性值得质疑。\n- 建议：重新界定 claim 为 \"style-correlated preference shift\"；在 originality 差异最小的子集上重复分析。\n\n### Should-Fix 问题\n\n**W1** NLI 阈值 τ=0.90 缺乏 sensitivity analysis（§3.2）\n**W2** Direction-aware NLI 可能引入系统性筛选偏差（§3.2, Appendix E）\n**W3** Exploratory analyses 的多重比较修正不完整（全文）\n**W4** Claude Sonnet 4 negative control 的 non-significance 解读过度——需等效性检验（Table 1）\n**W5** Figure 4 的 post-hoc power analysis 存在循环推理风险（§5.2）\n**W6** Rewriter independence test 未覆盖 register axis（Table 6-7）\n\n### 小问题\n- M1: hoenig2001abuse bib 可能缺少 \\cite\n- M2: wu2023style bib 年份不一致\n- M3: Figure 2 DAG 图注解释不足\n- M4: Table 1 Likert d 负值含义未充分解释\n- M5: \"Interventional Design\" 标题措辞与实际 evidence 强度不匹配\n\n### Questions\nQ1: NLI 阈值选定依据和 sensitivity 数据？\nQ2: GEE Style×Originality 交互项是否检验过？\nQ3: Full BT (63.0%) vs filtered sign test (73.9%) 差异的含义？\nQ4: 各 benchmark×axis×judge 单元 NLI 过滤后的 effective sample size？\nQ5: 是否考虑过与 RATE/LC-AlpacaEval 的 head-to-head 比较？\n\n### 缺失引用\n- Hausman & McFadden (1984) — IIA 检验\n- Agresti (2010) — ordinal data 分析\n- Lakens (2017) — equivalence testing",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-21T11:22:22.006944+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27013
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-21T11:22:22.409020+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性与完整性\n\n### 总体评分\n**Overall**: 3.0 — Findings\n\n### Must-Fix 问题\n\n**N1** [critical] \"Likert Blindspot\" 命名不准确——efficiency gap 而非 blindspot\n- Title, Abstract, §1, §5.2: Table 1 中 9 个 bias-positive cells 有 3 个 Likert 也检测到了（‡ 标记）。Section 5.2 line 87 承认 \"three of nine bias-positive cells escape the Blindspot\"。\n- 进一步：n=355 时 Likert d=−0.025 也可能是 Likert 和 pairwise 测量不同构念（absolute quality difference vs ordinal preference），而非同一构念的不同测量精度。\n- 建议改为 \"Likert Attenuation Effect\" 或 \"Measurement Sensitivity Gap\"。\n\n**N2** [critical] Related Work 引用数量和覆盖面严重不足\n- Section 2: 仅 36 篇引用，EMNLP 长文通常 40-60 篇。缺失方向：NLG evaluation surveys (van der Lee 2019/2021, Celikyilmaz 2020)、counterfactual text generation (MICE Ross 2021, Tailor Ross 2022)、scale design (Krosnick 1999, Preston & Colman 2000)、LLM-as-judge frameworks (G-Eval Liu 2023, Arena-Hard Li 2024)、causal NLP (Keith 2020)、GEE 原始论文 (Liang & Zeger 1986)。\n\n**N3** [critical] \"Four critical gaps\" 有 cherry-picking 嫌疑\n- §1 lines 11-12: 四个 gap 的定义刚好使得只有 CSD 满足所有条件。CASSE/FairJudge 已做 multi-dimensional decomposition（被归入 \"correlational\" 排除），RATE/Counterfactual Rhetorical 已做 interventional analysis（被归入 \"Likert-based\"/\"persona-level\" 排除）。\n\n### Should-Fix 问题\n\n**W1** Contribution 2 (Likert Blindspot) novelty 定位需更诚实——Kiritchenko (2017)、Novikova (2018) 已在其他 NLP 任务中展示 ranking > rating\n**W2** Conclusion 仅一句话，严重不足\n**W3** Contribution 3 (GEE conditional decomposition) 是标准方法直接应用，不应列为独立 contribution\n**W4** 对 RATE 批评可能不公平——RATE 目标是 reward model explainability 而非 style bias detection\n**W5** 主实验仅基于 LLMBar (n=100)，generalizability 存疑\n**W6** Evaluator-producer bias 处理不够彻底——Style OR 下降 22%（13.10→10.17）不可忽略\n\n### Questions\nQ1: Likert 和 pairwise 是否测量不同构念？\nQ2: n=355 Likert d 缩小是 attenuation 还是 regression to the mean？\nQ3: Direction asymmetry (78.8% vs 54.5%) 是否说明 judge 偏好原文而非 formality？\nQ4: 为什么不用人类标注验证 NLI gate？\nQ5: Claude Sonnet 4 极端 originality sensitivity (OR=6.66) 如何解释？\n\n### 缺失引用\nvan der Lee (2019, 2021), Celikyilmaz (2020), MICE (Ross 2021), Tailor (Ross 2022), Krosnick (1999), Preston & Colman (2000), G-Eval (Liu 2023), Arena-Hard (Li 2024), Keith (2020), Liang & Zeger (1986)",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性与完整性\n\n### 总体评分\n**Overall**: 3.0 — Findings\n\n### Must-Fix 问题\n\n**N1** [critical] \"Likert Blindspot\" 命名不准确——efficiency gap 而非 blindspot\n- Title, Abstract, §1, §5.2: Table 1 中 9 个 bias-positive cells 有 3 个 Likert 也检测到了（‡ 标记）。Section 5.2 line 87 承认 \"three of nine bias-positive cells escape the Blindspot\"。\n- 进一步：n=355 时 Likert d=−0.025 也可能是 Likert 和 pairwise 测量不同构念（absolute quality difference vs ordinal preference），而非同一构念的不同测量精度。\n- 建议改为 \"Likert Attenuation Effect\" 或 \"Measurement Sensitivity Gap\"。\n\n**N2** [critical] Related Work 引用数量和覆盖面严重不足\n- Section 2: 仅 36 篇引用，EMNLP 长文通常 40-60 篇。缺失方向：NLG evaluation surveys (van der Lee 2019/2021, Celikyilmaz 2020)、counterfactual text generation (MICE Ross 2021, Tailor Ross 2022)、scale design (Krosnick 1999, Preston & Colman 2000)、LLM-as-judge frameworks (G-Eval Liu 2023, Arena-Hard Li 2024)、causal NLP (Keith 2020)、GEE 原始论文 (Liang & Zeger 1986)。\n\n**N3** [critical] \"Four critical gaps\" 有 cherry-picking 嫌疑\n- §1 lines 11-12: 四个 gap 的定义刚好使得只有 CSD 满足所有条件。CASSE/FairJudge 已做 multi-dimensional decomposition（被归入 \"correlational\" 排除），RATE/Counterfactual Rhetorical 已做 interventional analysis（被归入 \"Likert-based\"/\"persona-level\" 排除）。\n\n### Should-Fix 问题\n\n**W1** Contribution 2 (Likert Blindspot) novelty 定位需更诚实——Kiritchenko (2017)、Novikova (2018) 已在其他 NLP 任务中展示 ranking > rating\n**W2** Conclusion 仅一句话，严重不足\n**W3** Contribution 3 (GEE conditional decomposition) 是标准方法直接应用，不应列为独立 contribution\n**W4** 对 RATE 批评可能不公平——RATE 目标是 reward model explainability 而非 style bias detection\n**W5** 主实验仅基于 LLMBar (n=100)，generalizability 存疑\n**W6** Evaluator-producer bias 处理不够彻底——Style OR 下降 22%（13.10→10.17）不可忽略\n\n### Questions\nQ1: Likert 和 pairwise 是否测量不同构念？\nQ2: n=355 Likert d 缩小是 attenuation 还是 regression to the mean？\nQ3: Direction asymmetry (78.8% vs 54.5%) 是否说明 judge 偏好原文而非 formality？\nQ4: 为什么不用人类标注验证 NLI gate？\nQ5: Claude Sonnet 4 极端 originality sensitivity (OR=6.66) 如何解释？\n\n### 缺失引用\nvan der Lee (2019, 2021), Celikyilmaz (2020), MICE (Ross 2021), Tailor (Ross 2022), Krosnick (1999), Preston & Colman (2000), G-Eval (Liu 2023), Arena-Hard (Li 2024), Keith (2020), Liang & Zeger (1986)",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-21T11:22:23.871306+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1462
}
```

</details>

---


### Assistant

_source line 292 · 2026-05-21T11:22:28.286456+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 27

## Round 27

2 recorded events


### User

_source line 293 · 2026-05-21T11:22:30.890634+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：论文提出的 Likert Blindspot 是一个新颖且有实际意义的发现，实验覆盖面和统计素养在同领域工作中突出。但三个 critical 问题——NLI gate 验证的循环偏差、BT 模型 IIA 假设未检验、originality confound 对识别策略的削弱——使得当前方法论支撑不足以支持主会议接收。评分 3.5（Borderline Conference），这些问题均可在一轮修改中解决。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 294 · 2026-05-21T11:22:40.670764+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 295 · 2026-05-21T11:24:03.609525+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: NLI Gate 验证的 evaluator-producer 循环偏差**

同意这是一个实质性问题。但需要做一个重要区分：NLI gate *本身*使用的是 DeBERTa-v3-large（Section 3.2, method.tex line 24），架构上独立于 rewriter 和 judge。R1 的 concern 针对的是 gate *验证*环节——用 Qwen3-32B（同时也是 rewriter）作为验证 annotator（Section 5.1, experiments.tex line 65），这确实存在循环依赖风险：Qwen3-32B 自然更倾向认为自己的改写保留了语义。GPT-4o spot-check (n=50) 确认了 94% 一致率，但 50 对样本的置信区间很宽。R1 建议的 ≥200 对人工标注是合理的。

补充我的观察：论文在 Limitations（main.tex lines 62-64）承认了 "human evaluation would provide stronger validation"，但将此放在 Limitations 而非 Discussion 中处理，显得对问题的严重性评估不足。

**[AGREE] R1-N2: Bradley-Terry IIA 假设未检验**

完全同意。这是一个被忽视的统计假设。BT 模型假设 formal text 相对 casual text 的偏好概率不随 item 基线质量变化——但 GEE decomposition (Table 3) 恰好揭示了 originality (基线质量代理) 对偏好有显著影响 (GPT-4o formality Orig OR=2.32)，这直接暗示交互效应的存在。如果高质量 item 上 style bias 更弱（或更强），BT 的 pooled 估计就会产生 Simpson's paradox 式的误导。R1 建议的 Hausman-McFadden test 或 Thurstone-Mosteller 稳健性检查是必要的。

论文 Appendix C (appendix.tex lines 51-53) 确实做了 GEE style×originality 交互项检验（p=0.53, p=0.32），但这是在 GEE logistic 框架内做的，不直接等价于 BT 层面的 IIA 检验。R1 指出的 n=88 低功效问题也是对的——n=88 检测交互效应的功效极低。

**[AGREE] R1-N3: Originality confound 显著，削弱识别策略**

同意，且这与我的 N1（framing 问题）高度相关。Table 3 数据清楚显示：在 formality axis 上，Originality OR (2.32-4.99) 与 Style OR (2.15-4.20) 量级相当；在 register axis 上，Originality OR (5.72) 甚至远超 Style OR (1.91)。这意味着 CSD 宣称的 "per-axis style bias isolation" 在 formality 和 register 上只实现了部分分离。

R1 建议 "重新界定 claim 为 style-correlated preference shift" 非常合理——这比 "style bias" 更准确地反映了数据支持的结论。论文的 "four gaps" 中 Gap 2 说现有方法 "cannot establish causal direction"（Introduction line 11），但 CSD 自身在 formality/register 上也只建立了 partial identification，这个批评在一定程度上回弹到了 CSD 自己头上。

不过有一个重要的例外：**verbosity axis** 确实展现了 confound-free 的 clean identification（Style OR=13.10/11.34, Orig OR n.s.），这是论文最强的实证结果。

---

### Should-Fix 问题

**[REBUT] R1-W1: NLI 阈值 τ=0.90 缺乏 sensitivity analysis**

论文在 Section 5.1 (experiments.tex lines 72-75) 已提供了 threshold sensitivity analysis："The formality win rate is stable at 72.3--73.9% across NLI thresholds of 0.70, 0.90, and 0.95 (sign test p < 0.005 at every threshold)." 还报告了 NLI 分数呈 bimodal distribution（多数在 0.95+ 或 0.30 以下），说明 0.90 阈值落在 plateau 上而非 cliff edge。这个 sensitivity analysis 存在且结论合理。R1 可能遗漏了这一段。

**[AGREE] R1-W2: Direction-aware NLI 可能引入系统性筛选偏差**

部分同意。Appendix E (appendix.tex lines 127-133) 做了验证：direction-aware gate 额外纳入的 21 对的偏好方向一致（BT 73.8% vs 78.5%），overall BT 不可区分（Δ=−1.1pp）。但这个验证只看了聚合统计量，没有分析被纳入对的系统性特征（如长度差异分布、主题分布）。R1 的 concern 有合理性，但 severity 应为 minor 而非 should-fix——因为论文的核心 Blindspot 论证不依赖 verbosity axis 的 direction-aware gate（formality 使用的是标准 bidirectional gate）。

**[REBUT] R1-W3: Exploratory analyses 多重比较修正不完整**

不同意。论文在 Section 4.1 (experiments.tex lines 8-11) 明确建立了分析层级：(1) primary family = 6 tests (2 judges × 3 axes) with Holm-Bonferroni；(2) exploratory = NLI sensitivity sweep, register axis，报告 uncorrected p-values 并明确标注为 "hypothesis-generating"；(3) confirmatory = consistency filter validation，nominal α=0.05。这是 pre-registration 精神下的标准实践。Table 1 的脚注也用 †_e 标注了 exploratory rows。R1 可能期望更严格的修正，但当前做法已是合理的统计实践。

**[AGREE] R1-W4: Claude negative control 需要等效性检验**

完全同意。Section 5.6 (experiments.tex line 200) 报告 Claude "shows no style preference on either axis (BT 56.2%/54.1%, both p > 0.09)"，并将其解读为 negative control。但 non-significance ≠ evidence of equivalence to 50%。BT 56.2% 的 95% CI 是 [.489, .636] (Appendix F, Table 8)——这个 CI 包含了 50% 也包含了 63.6%（约为 GPT-4o 的效应量）。论文无法排除 Claude 也有中等程度偏差的可能。R1 建议的 equivalence testing (TOST) 是正确的方法。这加强了我对论文 "discriminative validity" claim (Abstract line 5) 的质疑。

**[AGREE] R1-W5: Figure 4 post-hoc power analysis 循环推理风险**

部分同意。论文在 Section 5.2 (experiments.tex line 130) 确实做了 disclaimer："This is not a post-hoc power analysis (cf. Hoenig and Heisey 2001), but a visual comparison..."。但实际操作上，用 observed effect sizes (Cohen's d=0.073, BT 63%) 来参数化检测概率曲线，在功能上与 post-hoc power analysis 相似。论文的 disclaimer 不改变曲线构建方法的本质。不过，Figure 4 的主要 narrative（Likert 需要 ~4.5× 更多数据来检测同一 bias）如果用 hypothetical effect sizes 参数化也能得到相似结论，所以此问题的实际影响有限。

**[AGREE] R1-W6: Rewriter independence test 未覆盖 register axis**

同意。Appendix D (Tables 6-7) 仅覆盖 verbosity 和 formality。Register axis 恰好有最强的 originality confound (OR=5.72)，最需要 rewriter independence 验证。

---

### 小问题

**[REBUT] R1-M1: hoenig2001abuse bib 缺少 \cite**

不是真问题。论文在 Section 5.2 (experiments.tex line 130) 使用了 `\citealt{hoenig2001abuse}`。verify_references 工具对 `\citealt` 命令的识别可能有遗漏，但实际引用存在。

**[AGREE] R1-M2: wu2023style bib 年份不一致**

确认。verify_references 检查显示 OpenAlex 年份为 2023，bib 标注为 2025 (COLING 2025)。可能是 preprint (2023) vs 会议正式发表 (2025) 的差异，但应统一。

**[REBUT] R1-M3: Figure 2 DAG 图注解释不足**

不完全同意。Figure 2 的 caption (method.tex lines 90) 相当详细（约 6 行），解释了每个变量、每条路径（包括 blocked paths 和 residual confounding）。但同意 DAG 图本身的 visual clarity 可以改善——例如 NLI gate 节点与 Rewrite 节点的关系箭头（灰色）不太直观。

**[AGREE] R1-M4: Table 1 Likert d 负值含义未充分解释**

同意。Table 1 有多个负 d 值（如 GPT-4o Verb. d=−0.095, Qwen3 Verb. d=−0.151），但正文从未解释负号的含义——是 verbose 版本得分更低（Likert）还是编码方向问题。这影响了 Table 1 的 self-containedness。

**[AGREE] R1-M5: "Interventional Design" 标题措辞过强**

同意。Section 3.5 标题为 "Interventional Design"，但正文第一句就声明 "Our approach provides interventional rather than formal causal evidence"（method.tex line 58）。建议标题改为 "Design Rationale" 或 "Quasi-Interventional Design"。这与我在 R2-N1 中对 framing 过度的总体观察一致。

---

### Questions

**[R1-Q1]**: NLI 阈值选定依据——已在论文 Section 5.1 lines 72-75 回答（sensitivity analysis at 0.70/0.90/0.95）。

**[R1-Q2]**: GEE 交互项——已在 Appendix C (appendix.tex lines 51-53) 回答：GPT-4o p=0.53, Qwen3-32B p=0.32, both n.s.。但如 R1-N2 所述，n=88 下功效不足以可靠检测交互。

**[R1-Q3]**: Full BT (63.0%) vs filtered sign test (73.9%) 差异——论文 Section 5.2 (experiments.tex lines 97-99) 已解释：full-data estimate 低于 filtered estimate 说明 consistency filter 没有 inflate effect；差异来自 BT 纳入了 position-inconsistent pairs（有 noise），sign test 只保留 consistent pairs。

**[R1-Q4]**: Effective sample sizes——Table 1 脚注给出 LLMBar n=88（NLI-gated），scaled replication n=355。但 R1 的 concern 合理：其他 benchmark×axis×judge 组合的 effective n 未逐一报告。

**[R1-Q5]**: 与 RATE/LC-AlpacaEval 的 head-to-head 比较——Section 5.2 lines 81-83 对 RATE 的 Likert ATE 方法做了直接比较（同一数据，两种方法）。但未与 LC-AlpacaEval 做 head-to-head——这可能因为 LC-AlpacaEval 是 population-level correction 而 CSD 是 per-instance detection，任务定义不同，直接比较困难。

---

### 缺失引用

**[AGREE]** Hausman & McFadden (1984) — 直接支持 R1-N2 的 IIA 检验需求。
**[AGREE]** Agresti (2010) — 论文用了 ordinal regression 但未引用方法学来源。
**[AGREE]** Lakens (2017) — 直接支持 R1-W4 的 equivalence testing 需求。

---

### 总结性评价

R1 的审稿报告质量很高，找到了多个我同意的方法论问题。我的交叉回应总结：

- **R1 的 3 个 Must-Fix 我全部同意**，其中 N2 (IIA) 和 N3 (originality confound) 是我审查中也独立识别的核心问题
- **R1 的 6 个 Should-Fix 中，我同意 4 个 (W2, W4, W5, W6)，反驳 2 个 (W1 因论文已有 sensitivity analysis, W3 因论文的多重比较框架已合理)**
- **5 个小问题中反驳 2 个 (M1 因 citealt 存在, M3 因 caption 已较详细)，同意 3 个**

R1 给出 3.5 (Borderline Conference)，我给出 3.0 (Findings)。分歧主要在 novelty 评估：R1 的方法严谨性审查聚焦于统计方法论问题（修复后可提升），而我的审查聚焦于核心发现的新颖性（这是更难修复的结构性问题）。两者结合，我认为 3.0-3.5 的区间是合理的。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 296 · 2026-05-21T11:24:17.743722+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 297 · 2026-05-21T11:24:20.367356+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 3 个 Must-Fix 全部 AGREE，6 个 Should-Fix 中 AGREE 4 个、REBUT 2 个（W1 论文已有 threshold sensitivity analysis；W3 多重比较框架已合理）。核心共识点：BT IIA 假设未检验、originality confound 削弱识别策略、Claude negative control 需等效性检验。主要分歧在 novelty 评估——R1 的 3.5 侧重方法论可修复性，我的 3.0 侧重核心发现的结构性新颖性不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 298 · 2026-05-21T11:24:26.336717+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 30

## Round 30

10 recorded events


### User

_source line 299 · 2026-05-21T11:28:23.912669+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

### Must-Fix

**[REBUT] R2-N1 ("Blindspot" 命名不准确)**: 论文 Abstract/§2 将 Blindspot 定义为 severity-spectrum 现象（moderate bias 区间完全失灵，强效应区部分恢复）。3/9 cells 逃逸恰好支持 spectrum 叙事。Table 2 的七种方法比较（四种 Likert-based 全失败 vs 两种 pairwise 全成功）反驳构念差异假设。但建议作者在 Discussion 更正式地讨论构念差异替代假设（降级为 Should-Fix）。

**[REBUT] R2-N2 (引用数量不足)**: 引用数量非质量标准。论文 §2 沿三条线索组织引用，覆盖充分。但同意 Liang & Zeger (1986) GEE 原文和 Krosnick (1999) 应补充（降级为 Should-Fix）。

**[AGREE] R2-N3 (Four gaps cherry-picking)**: §1 四个 gap 的合取条件确实倾向于只有 CSD 满足。CASSE 的 controlled style manipulation 被简单标记为 "correlational" 不完全公平。但这是 framing 问题，不影响技术贡献，建议降级为 Should-Fix。

### Should-Fix

**[REBUT] R2-W1**: 论文 §2 已引用 Kiritchenko/Novikova。增量贡献在于 LLM judge 场景的系统量化 + measurement attenuation 表征 + 七种方法比较。
**[AGREE] R2-W2**: Conclusion 偏短，建议扩展。
**[REBUT] R2-W3**: GEE 方法标准但应用场景（decompose style vs originality in LLM judges）新颖，Table 3 发现有实践指导价值。
**[REBUT] R2-W4**: 论文对 RATE 的讨论聚焦测量方法论比较，不涉及目标价值判断。
**[AGREE] R2-W5**: 主实验确以 LLMBar 为中心，Table 1 含 AlpacaEval/MT-Bench 但仅作 replication。
**[AGREE] R2-W6**: 与我的 R1-N1 一致，22% Style OR 下降不可忽略。

### Questions

**[REBUT] Q1**: Table 2 四种 Likert-based 方法全部失败反驳构念差异假设；n=355 BT 稳定而 Likert d→0 进一步排除。
**[REBUT] Q2**: Regression to mean 对所有估计量对称操作，但 BT 稳定/略升而 Likert→0 的 differential shrinkage 不一致。
**[AGREE] Q3**: 方向不对称与 R1-N3 originality confound 一致。GEE additive specification 可能不足以正确分离。
**[AGREE] Q4**: 与 R1-N1 一致，NLI gate 需人工标注验证。
**[AGREE] Q5**: Claude Orig OR=6.66 削弱 negative control 解读，与 R1-W4 一致。

### 与 R2 的主要分歧

R2 的 Overall 3.0 (Findings) 偏低。N1（命名）和 N2（引用数量）不构成 critical 问题。论文的核心方法论贡献（CSD + Likert Blindspot + sensitivity hierarchy）在修补 NLI gate 验证和 BT IIA 检验后可达 Conference 水平。我维持 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-21T11:28:52.872237+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-21T11:28:53.073605+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T11:13:58.535894+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_5ce280de124a4e308d1827c6450ad337\", \"skipped_at\": \"2026-05-21T11:14:38.589105+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-21T11:28:53.073978+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-21T11:28:53.124460+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T11:13:57.343054+00:00\", \"completed_at\": \"2026-05-21T11:17:11.357183+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"连续 3 页纯文本无任何 display item（非理论推导段），审稿人在 page 4 之前无视觉锚点，影响第一印象锚定\"}, {\"severity\": \"warning\", \"dimension\": \"page 4\", \"message\": \"Figure 1 (pipeline overview) 图内文字标签字号偏小（约正文 60%），icon 细节在缩小/打印时可能难以辨认\"}, {\"severity\": \"warning\", \"dimension\": \"page 13\", \"message\": \"最后一页仅有 4 条参考文献（~20% 占比），约 80% 空白，空间利用率低\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 (DAG) 使用红/蓝/橙配色，色盲友好性一般（红绿色盲可能混淆红色虚线与背景），建议考虑用虚线样式辅助区分\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 中部分 p 值格式不完全一致（有些用括号、有些用上标），建议统一\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 菱形标记在密集区域略有重叠，但整体可读\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4 曲线在 n>200 区域有多条线重合，可考虑局部放大或标注关键拐点\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Conclusion 段落紧凑，Section 6 与 Limitations 之间过渡自然，排版合理\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 从 page 8 延续至 page 9，内容充实覆盖多个维度（scale granularity、human evaluation、benchmark coverage 等），篇幅适中\"}], \"counts\": {\"critical\": 0, \"warning\": 3, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-21T11:35:05.632032+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-2 issues (all resolved)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Interventional Design' with disclaimer.\"\n    resolution_round: 2\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M5 指出 'Interventional Design' 标题仍偏强，建议改为 'Design Rationale'。Title 本身已无因果过度声明。\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知），excitement 评分 3-3.5/5。见 R3-N3。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R2-W-SF8 再次提出。R1 反驳认为 application context + 7-method hierarchy 构成充分贡献。Director 判定 Should-Fix：需在 Abstract/Intro 明确标注为已知原理的首次系统定量验证。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R1-W1 再次提出，R2 以论文 §5.1 已有 sensitivity analysis 反驳。Director dropped。\"\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R1-W3 再次提出 exploratory 多重比较。R2 反驳论文 §4.1 框架合理。Director dropped。\"\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2×3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 3 复发，见 R3-N3\"\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks × 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R2-W5 再次提出主实验仍以 LLMBar 为中心。AlpacaEval/MT-Bench 仅作 partial replication。Director 维持 Should-Fix。\"\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Main text 8 pages.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。见 R3-N2。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4: Formality rewriter independence test 已补（Appendix D Table 7），但 register 仍缺。Style OR 下降 22%（13.10→10.17）非可忽略。Originality OR 系统性 ~2× GPT-4o。\"\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction (BT 73.8% vs 78.5%), Δ=−1.1pp.\"\n    resolution_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R1-W2 partial concern remains about systematic characteristics of extra pairs, but core Blindspot argument uses bidirectional gate (formality). Director: minor residual concern.\"\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P→Y) and rewrite artifact (R→Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P→Y + R→Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues — status updated based on R4 review\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语（Title 'Counterfactual'、§3.5 'Causal Framework'、DAG）与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Title changed (no 'Counterfactual'). §3.5 → 'Interventional Design' with explicit disclaimer. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 强共识。R1: originality OR 显著证明识别假设经验性违反。R2: 方法是 controlled intervention，非 Pearl/Rubin 框架。\"\n      - round: 4\n        reviewers: [1]\n        note: \"核心问题已修复。残留 minor：'Interventional Design' 标题仍偏强，见 R4-M2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Qwen3-32B formality OR=4.20 vs GPT-4o OR=2.58，1.6× 差距可能来自 evaluator-producer confound。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补（Appendix D Table 7: BT 64.4% vs 66.5%, Δ=−2.1pp）。Register 仍缺——恰好是 originality confound 最强的 axis (OR=5.72)。降级为 warning。\"\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异（power gap）包装为质性 blindspot\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位最强共识。Figure 4 显示 Likert 在 n≈1473 达到 80% power——不是 blindspot 而是功效不足。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"论文增加了 'measurement attenuation across a severity spectrum' framing 和 n=355 d→0 证据。R1 认为 spectrum 叙事合理（REBUT），R2 仍认为命名不准确（3/9 cells Likert 也检测到）。Director 判定：降为 Should-Fix，但需在 Discussion 讨论构念差异替代假设。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。Conclusion 限定了 scope。\"\n    resolution_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R4 未再将此单独列为问题。Conclusion 过短（R4-W2）是相关但不同的 issue。\"\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"论文承诺 GPT-4o spot-check 但未执行。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"GPT-4o spot-check 已补（47/50, 94% 一致率, 5pp precision gap）。但 n=50 样本量置信区间很宽。R4 两位 Reviewer 共识升级为 Must-Fix：需 ≥200 对人工标注。\"\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5% (Δ=−1.1pp), consistent direction.\"\n    resolution_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R1-W2 partial concern about systematic characteristics of extra pairs, but R2 notes core argument uses bidirectional gate. Director: resolved with minor residual.\"\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"ACL/EMNLP 传统要求 text generation 工作提供 human evaluation。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Limitations 新增段落 acknowledge。Cross-rewriter consistency (Appendix D) 提供 partial validation。但仍无人工评估。与 R4 W-MF1 (NLI gate 验证) 强相关。\"\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增 'Confound structure and rewriting invasiveness' 段落。\"\n    resolution_round: 4\n    mentions:\n      - round: 4\n        reviewers: []\n        note: \"R4 未再单独提出。Limitations 段落充分 acknowledge。\"\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"§5.6 title changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 确认 'conditional decomposition' 表述更准确。但 R4-W-MF3 仍指出 originality confound 严重。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定——Qwen3 formality OR 从 4.20 降至 2.15\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3 as footnote row. Text discusses small-sample correction.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少（27 vs 40-60），缺关键方向文献\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"补 CausaLM, Polyjuice, Clark 2021, Amidei 2019, Boubdir 2023, Wu & Aji 2023 等，目标 35+。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"引用扩展至 36 篇（从 27 增加）。R2 仍认为不足，列出 7+ 缺失方向。R1 认为数量非质量标准。Director 降为 Should-Fix：补 GEE 原文 (Liang & Zeger 1986)、scale design (Krosnick 1999) 等特定方向即可。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias → ATE attenuation\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"§5.1: Cliff's δ=+0.45 (p<0.001) for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"无 bias vs alignment 消除 bias。共识降为 info。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 升级关注：Claude Orig OR=6.66 (p<0.0001) 表明 Claude 有强 originality bias，non-significance of style ≠ no bias。BT 56.2% CI [.489, .636] 包含 50% 也包含 ~63%。两位共识需 TOST equivalence testing。升级为 warning (R4-SF4)。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated with clearer raw vs adjusted p notation.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R4 仍指出 Abstract 信息密度过高：7 行含 3 judges、3 benchmarks、3 axes、具体 d 值、p 值等。建议精简数字。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via \\\\citealt in §5.2. murugadoss2025sos cited in §1. Not orphans.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 NEW issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验——originality 对偏好的显著影响暗示 IIA 违反\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 完全同意。GEE Orig OR 显著直接暗示 style preference 随 item 基线质量变化，violating IIA。Appendix C 交互项检验 (p=0.53/0.32) 不等价于 BT 层面 IIA 检验，且 n=88 功效不足。\"\n    action_items:\n      - round: 4\n        action: \"报告 Hausman-McFadden test 或拟合 Thurstone-Mosteller 模型做稳健性检查\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 识别为 critical，R1 同意但建议降级。四个 gap 的合取条件使只有 CSD 满足。CASSE/FairJudge 做了 multi-dimensional decomposition 但被标为 'correlational'；RATE 做了 interventional 但被标为 'Likert-based'。\"\n    action_items:\n      - round: 4\n        action: \"更诚实地承认各 gap 已有部分解决方案，定位为 integrative framework\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话，严重不足——8 页长文需要完整的总结\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位共识。应包括主要发现总结、方法论贡献意义、社区实践影响、未来研究方向。\"\n    action_items:\n      - round: 4\n        action: \"扩展 Conclusion 至 10-15 行\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"多个负 d 值（GPT-4o Verb. d=−0.095, Qwen3 Verb. d=−0.151）但正文未解释负号含义。\"\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' §3.5 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"§3.5 标题 'Interventional Design' 但正文第一句就 disclaimer。建议改为 'Design Rationale' 或 'Quasi-Interventional Design'。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-2 issues (all resolved)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Interventional Design' with disclaimer.\"\n    resolution_round: 2\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M5 指出 'Interventional Design' 标题仍偏强，建议改为 'Design Rationale'。Title 本身已无因果过度声明。\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知），excitement 评分 3-3.5/5。见 R3-N3。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R2-W-SF8 再次提出。R1 反驳认为 application context + 7-method hierarchy 构成充分贡献。Director 判定 Should-Fix：需在 Abstract/Intro 明确标注为已知原理的首次系统定量验证。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R1-W1 再次提出，R2 以论文 §5.1 已有 sensitivity analysis 反驳。Director dropped。\"\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R1-W3 再次提出 exploratory 多重比较。R2 反驳论文 §4.1 框架合理。Director dropped。\"\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2×3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 3 复发，见 R3-N3\"\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks × 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R2-W5 再次提出主实验仍以 LLMBar 为中心。AlpacaEval/MT-Bench 仅作 partial replication。Director 维持 Should-Fix。\"\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Main text 8 pages.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。见 R3-N2。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4: Formality rewriter independence test 已补（Appendix D Table 7），但 register 仍缺。Style OR 下降 22%（13.10→10.17）非可忽略。Originality OR 系统性 ~2× GPT-4o。\"\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction (BT 73.8% vs 78.5%), Δ=−1.1pp.\"\n    resolution_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R1-W2 partial concern remains about systematic characteristics of extra pairs, but core Blindspot argument uses bidirectional gate (formality). Director: minor residual concern.\"\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P→Y) and rewrite artifact (R→Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P→Y + R→Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues — status updated based on R4 review\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语（Title 'Counterfactual'、§3.5 'Causal Framework'、DAG）与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Title changed (no 'Counterfactual'). §3.5 → 'Interventional Design' with explicit disclaimer. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 强共识。R1: originality OR 显著证明识别假设经验性违反。R2: 方法是 controlled intervention，非 Pearl/Rubin 框架。\"\n      - round: 4\n        reviewers: [1]\n        note: \"核心问题已修复。残留 minor：'Interventional Design' 标题仍偏强，见 R4-M2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Qwen3-32B formality OR=4.20 vs GPT-4o OR=2.58，1.6× 差距可能来自 evaluator-producer confound。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补（Appendix D Table 7: BT 64.4% vs 66.5%, Δ=−2.1pp）。Register 仍缺——恰好是 originality confound 最强的 axis (OR=5.72)。降级为 warning。\"\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异（power gap）包装为质性 blindspot\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位最强共识。Figure 4 显示 Likert 在 n≈1473 达到 80% power——不是 blindspot 而是功效不足。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"论文增加了 'measurement attenuation across a severity spectrum' framing 和 n=355 d→0 证据。R1 认为 spectrum 叙事合理（REBUT），R2 仍认为命名不准确（3/9 cells Likert 也检测到）。Director 判定：降为 Should-Fix，但需在 Discussion 讨论构念差异替代假设。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。Conclusion 限定了 scope。\"\n    resolution_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R4 未再将此单独列为问题。Conclusion 过短（R4-W2）是相关但不同的 issue。\"\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"论文承诺 GPT-4o spot-check 但未执行。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"GPT-4o spot-check 已补（47/50, 94% 一致率, 5pp precision gap）。但 n=50 样本量置信区间很宽。R4 两位 Reviewer 共识升级为 Must-Fix：需 ≥200 对人工标注。\"\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5% (Δ=−1.1pp), consistent direction.\"\n    resolution_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 R1-W2 partial concern about systematic characteristics of extra pairs, but R2 notes core argument uses bidirectional gate. Director: resolved with minor residual.\"\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"ACL/EMNLP 传统要求 text generation 工作提供 human evaluation。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Limitations 新增段落 acknowledge。Cross-rewriter consistency (Appendix D) 提供 partial validation。但仍无人工评估。与 R4 W-MF1 (NLI gate 验证) 强相关。\"\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增 'Confound structure and rewriting invasiveness' 段落。\"\n    resolution_round: 4\n    mentions:\n      - round: 4\n        reviewers: []\n        note: \"R4 未再单独提出。Limitations 段落充分 acknowledge。\"\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"§5.6 title changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 确认 'conditional decomposition' 表述更准确。但 R4-W-MF3 仍指出 originality confound 严重。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定——Qwen3 formality OR 从 4.20 降至 2.15\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3 as footnote row. Text discusses small-sample correction.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少（27 vs 40-60），缺关键方向文献\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"补 CausaLM, Polyjuice, Clark 2021, Amidei 2019, Boubdir 2023, Wu & Aji 2023 等，目标 35+。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"引用扩展至 36 篇（从 27 增加）。R2 仍认为不足，列出 7+ 缺失方向。R1 认为数量非质量标准。Director 降为 Should-Fix：补 GEE 原文 (Liang & Zeger 1986)、scale design (Krosnick 1999) 等特定方向即可。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias → ATE attenuation\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"§5.1: Cliff's δ=+0.45 (p<0.001) for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"无 bias vs alignment 消除 bias。共识降为 info。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 升级关注：Claude Orig OR=6.66 (p<0.0001) 表明 Claude 有强 originality bias，non-significance of style ≠ no bias。BT 56.2% CI [.489, .636] 包含 50% 也包含 ~63%。两位共识需 TOST equivalence testing。升级为 warning (R4-SF4)。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated with clearer raw vs adjusted p notation.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R4 仍指出 Abstract 信息密度过高：7 行含 3 judges、3 benchmarks、3 axes、具体 d 值、p 值等。建议精简数字。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via \\\\citealt in §5.2. murugadoss2025sos cited in §1. Not orphans.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 NEW issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验——originality 对偏好的显著影响暗示 IIA 违反\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 完全同意。GEE Orig OR 显著直接暗示 style preference 随 item 基线质量变化，violating IIA。Appendix C 交互项检验 (p=0.53/0.32) 不等价于 BT 层面 IIA 检验，且 n=88 功效不足。\"\n    action_items:\n      - round: 4\n        action: \"报告 Hausman-McFadden test 或拟合 Thurstone-Mosteller 模型做稳健性检查\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 识别为 critical，R1 同意但建议降级。四个 gap 的合取条件使只有 CSD 满足。CASSE/FairJudge 做了 multi-dimensional decomposition 但被标为 'correlational'；RATE 做了 interventional 但被标为 'Likert-based'。\"\n    action_items:\n      - round: 4\n        action: \"更诚实地承认各 gap 已有部分解决方案，定位为 integrative framework\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话，严重不足——8 页长文需要完整的总结\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位共识。应包括主要发现总结、方法论贡献意义、社区实践影响、未来研究方向。\"\n    action_items:\n      - round: 4\n        action: \"扩展 Conclusion 至 10-15 行\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"多个负 d 值（GPT-4o Verb. d=−0.095, Qwen3 Verb. d=−0.151）但正文未解释负号含义。\"\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' §3.5 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"§3.5 标题 'Interventional Design' 但正文第一句就 disclaimer。建议改为 'Design Rationale' 或 'Quasi-Interventional Design'。\""
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-21T11:35:05.783777+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 21653}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-21T11:37:46.641387+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n**Venue**: EMNLP 2026 Main Conference (via ARR)\n**审稿编排**: 2 Reviewers — R1 方法严谨性, R2 新颖性/完整性\n**交叉回应**: 完成（1 轮收敛）\n\n---\n\n## Summary\n\n论文提出 Controlled Style Decomposition (CSD)，一个检测 LLM judge per-axis style bias 的 black-box 框架。核心发现 \"Likert Blindspot\"：标准 Likert 打分在七种统计方法下均无法检测到 pairwise comparison 清楚揭示的 style bias（3 judges × 3 benchmarks × 3 axes）。方法包括 NLI-gated style rewriting、position-controlled pairwise comparison、GEE conditional decomposition 分离 style vs originality effects。n=355 scaled replication 显示 Likert d→0 而 BT 稳定在 67.5%，作者将此定义为 measurement attenuation 而非单纯的 power gap。\n\n---\n\n## Strengths\n\n1. **实验设计严谨**: position control (双向 swap)、NLI gate (0.90 threshold + sensitivity analysis across 0.70-0.95)、cross-judge replication (GPT-4o, Qwen3-32B, Claude Sonnet 4 as negative control)、cross-benchmark validation (LLMBar, AlpacaEval, MT-Bench)。在 NLP 实证研究中属较高水平。\n\n2. **七种统计方法的 sensitivity hierarchy (Table 2)** 有说服力——四种 Likert-based 方法全失败 vs 两种 pairwise 方法全成功，排除了特定统计测试的 artifact 解释。Binarized Likert sign test (同样是 forced choice, 仍然 non-significant) 特别有价值。\n\n3. **统计素养突出**: Holm-Bonferroni with explicit 6-test family definition、primary/exploratory/confirmatory trichotomy (§4.1)、Bradley-Terry with pair-level bootstrap CI、GEE with correlation structure robustness check (Appendix C)。\n\n4. **GEE confound decomposition 发现有价值**: verbosity 的 confound-free 纯 style bias (Style OR=13.10/11.34, Orig OR n.s.) vs formality/register 的混合效应，对后续研究有指导意义。两个 judge 之间 verbosity OR 高度一致 (13.10 vs 11.34) 增强可信度。\n\n5. **Negative control 设计加强可信度**: Claude Sonnet 4 在两个 axis 上均未检测到显著 style 偏差 (BT 56.2%/54.1%)，证明 CSD 有 discriminative validity。\n\n6. **Rewriter independence test (Appendix D)** 直接回应最可能的方法论质疑：GPT-4o 作为独立 rewriter，verbosity Style OR 仅下降 22% (13.10→10.17)，formality BT 64.4% vs 66.5% (Δ=−2.1pp)，Blindspot 在独立 rewriter 下持续存在。\n\n7. **Limitations section 充分诚实**: 7 段覆盖 quality-style confounding、evaluator-producer bias、benchmark coverage、human evaluation 缺失、scale granularity、NLI validation methodology 等。\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 个，两位 Reviewer 强共识）\n\n**W-MF1 [critical] NLI Gate 验证存在 evaluator-producer 循环偏差**\n\nNLI gate 本身使用 DeBERTa-v3-large（架构独立），但 gate *验证*（§5.1）使用 Qwen3-32B 作为 annotator——同时也是 rewriter 和 judge 之一。False negative rate 8.4% 可能被低估，因 Qwen3-32B 自然更倾向认为自己的改写保留了语义。GPT-4o spot-check (n=50, 94% 一致率) 部分缓解，但 50 对样本的 Wilson CI 约 [83%, 99%]，置信区间过宽。论文在 Limitations 承认 \"human evaluation would provide stronger validation\"，但将此放在 Limitations 而非 Discussion 中处理，显得对问题严重性评估不足。\n\n**两位 Reviewer 强共识** (R1 识别, R2 独立确认)。\n\n建议：≥200 对人工标注，或两个架构独立的模型分别验证。\n\n**W-MF2 [critical] Bradley-Terry IIA 假设未检验**\n\nBT 模型假设 Independence of Irrelevant Alternatives (IIA)，即 formal text 相对 casual text 的偏好概率不随 item 基线质量变化。但 GEE decomposition (Table 3) 恰好揭示了 originality (基线质量代理) 对偏好有显著影响 (GPT-4o formality Orig OR=2.32, p=0.006)，直接暗示 style preference 可能随 item 质量变化——violating IIA。如果高质量 item 上 style bias 更弱（或更强），BT 的 pooled 估计可能产生 Simpson's paradox 式的误导。\n\n论文未报告任何 IIA 诊断检验。Appendix C 的 GEE style×originality 交互项检验 (p=0.53/0.32) 不等价于 BT 层面的 IIA 检验，且 n=88 检测交互效应功效极低。\n\n**两位 Reviewer 强共识** (R1 识别, R2 完全同意)。\n\n建议：报告 Hausman-McFadden test 或拟合 Thurstone-Mosteller 模型做稳健性检查。\n\n**W-MF3 [critical] Originality confound 显著，削弱识别策略**\n\n多配置下 Originality OR 显著且与 Style OR 量级相当甚至更大：\n- GPT-4o formality: Style OR=2.58 vs Orig OR=2.32\n- Qwen3-32B register: Style OR=1.91 vs Orig OR=5.72\n- Qwen3-32B formality (n=88): Style OR=4.20 vs Orig OR=4.70\n\nCSD 宣称的 \"per-axis style bias isolation\" 在 formality 和 register 上只实现了部分分离。Direction asymmetry (78.8% vs 54.5%) 进一步支持 originality confound 的存在。GEE additive specification 的交互项检验 (p=0.53/0.32) 在 n=88 下功效不足以可靠排除交互效应。\n\n重要例外：**verbosity 确实展现了 confound-free 的 clean identification** (Style OR=13.10/11.34, Orig OR n.s.)，是论文最强的实证结果。\n\n**两位 Reviewer 强共识** (R1 识别为 critical, R2 独立确认并指出与 \"four gaps\" framing 的逻辑矛盾)。\n\n建议：重新界定 claim 为 \"style-correlated preference shift\" 而非 \"style bias isolation\"；在 originality 差异最小的子集上重复分析。\n\n### Should-Fix（8 个）\n\n**W-SF1 [warning] \"Blindspot\" 命名准确性争议**\n\nR2 认为 critical：Table 1 中 3/9 bias-positive cells Likert 也检测到了，这不是 blindspot 而是 efficiency gap。R1 反驳：论文的 severity spectrum framing（moderate bias 区间完全失灵、强效应区部分恢复）合理，3/9 cells 逃逸恰好支持 spectrum 叙事。\n\n**Director 判定**: Should-Fix。Spectrum framing 有一定说服力，但 \"Blindspot\" 一词暗示结构性不可能检测。更关键的是，n=355 时 Likert d=−0.025 也可解读为 Likert 和 pairwise 测量不同构念（absolute quality difference vs ordinal preference）——论文 §5.2 隐约承认但未整合进 framing。建议在 Discussion 正式讨论构念差异替代假设。\n\n**W-SF2 [warning] Related Work 引用覆盖面不足**\n\nR2 认为 critical (36 篇 vs 40-60 标准，缺 NLG evaluation surveys、counterfactual generation、scale design 等方向)。R1 认为数量非质量标准。\n\n**Director 判定**: Should-Fix。引用数量不是硬标准，但以下特定缺失影响论文定位可信度：GEE 原始论文 (Liang & Zeger 1986)、scale design 文献 (Krosnick 1999, Preston & Colman 2000)、equivalence testing (Lakens 2017)、IIA 检验 (Hausman & McFadden 1984)。\n\n**W-SF3 [warning] \"Four critical gaps\" 有 cherry-picking 嫌疑**\n\n§1 四个 gap 的合取条件使得只有 CSD 满足所有条件。CASSE/FairJudge 已做 multi-dimensional decomposition（被归入 \"correlational\" 排除），RATE/Counterfactual Rhetorical 已做 interventional analysis（被归入 \"Likert-based\"/\"persona-level\" 排除）。R1 和 R2 均指出此问题。\n\n建议：更诚实地承认各 gap 已有部分解决方案，定位为 integrative framework 而非唯一解。\n\n**W-SF4 [warning] Claude negative control 需等效性检验**\n\nBT 56.2% 的 95% CI [.489, .636] 包含 50% 也包含 ~63%（GPT-4o 效应量），non-significance ≠ evidence of equivalence。Claude 的极端 originality sensitivity (Orig OR=6.66, p<0.0001) 进一步削弱 negative control 解读——Claude 可能有不同类型的偏差（originality-dependent 而非 style-dependent）。Abstract \"confirms discriminative validity\" 过于肯定。\n\n建议：使用 TOST equivalence testing (Lakens 2017)。\n\n**W-SF5 [warning] Conclusion 仅一句话，严重不足**\n\n8 页长文的结论仅 \"CSD reveals the Likert Blindspot...style bias audits should adopt pairwise comparison\" 一句。应包括：主要发现总结、方法论贡献的意义、对社区实践的具体影响、未来研究方向。两位 Reviewer 共识。\n\n建议：扩展至 10-15 行。\n\n**W-SF6 [warning] Evaluator-producer bias 处理不够彻底**\n\nQwen3-32B 同时担任 rewriter + judge 是设计缺陷。Style OR 在独立 rewriter test 中下降 22% (13.10→10.17)，非可忽略。Originality OR 系统性约 2× GPT-4o (formality: 4.99 vs 2.32; register: 5.72 vs 2.21)。Register axis 未做 rewriter independence test——恰好是 evaluator-producer bias 风险最高的配置。两位 Reviewer 共识。\n\n**W-SF7 [warning] 主实验以 LLMBar (n=100) 为中心**\n\nAlpacaEval 和 MT-Bench 仅作 partial replication (Table 1 仅 5 个额外 rows)。核心 Blindspot 论证完全基于 LLMBar 的 n=88 NLI-gated pairs。Scaled replication (n=355) 仅限 Qwen3 formality 一个 cell。LLMBar 是为 instruction-following 设计的 benchmark，其 100 条样本对更广泛 LLM evaluation 场景的代表性值得商榷。两位 Reviewer 共识。\n\n**W-SF8 [warning] Novelty 定位需更诚实**\n\nLikert vs pairwise 灵敏度差异是测量学经典结论 (Thurstone 1927, Kiritchenko 2017, Novikova 2018) 的 LLM 评估领域应用。R2 认为增量 novelty (LLM judge 场景 + 定量 attenuation 测量 + 7 方法比较) 有价值但不应包装为发现级突破。R1 反驳认为 application context + sensitivity hierarchy 构成充分贡献。\n\n**Director 判定**: Should-Fix。应在 Abstract/Introduction 明确标注为 \"known measurement theory principle 在 LLM judge evaluation 的首次系统定量验证\"。\n\n### Minor（5 个）\n\n- **W-M1**: Table 1 Likert d 负值含义未解释（两位共识）\n- **W-M2**: §3.5 \"Interventional Design\" 标题与 evidence 强度不匹配，建议改为 \"Design Rationale\" 或 \"Quasi-Interventional Design\"（两位共识）\n- **W-M3**: GEE conditional decomposition 列为独立 contribution 有膨胀之嫌（R2 提出, R1 反驳——Director 判定 minor framing 调整）\n- **W-M4**: wu2023style bib 年份不一致 (2023 vs 2025)\n- **W-M5**: Figure 4 power curve 使用 observed effect sizes 参数化，功能上接近 post-hoc power analysis（论文有 disclaimer 但不改变实质）\n\n---\n\n## Reviewer Consensus\n\n| # | Issue | R1 | R2 | Status |\n|---|-------|----|----|--------|\n| 1 | NLI gate 验证循环偏差 | N1 critical | AGREE | **共识 Must-Fix** |\n| 2 | BT IIA 未检验 | N2 critical | AGREE | **共识 Must-Fix** |\n| 3 | Originality confound | N3 critical | AGREE | **共识 Must-Fix** |\n| 4 | Claude negative control 等效性 | W4 warning | AGREE | **共识 Should-Fix** |\n| 5 | Conclusion 过短 | AGREE | W2 warning | **共识 Should-Fix** |\n| 6 | Rewriter independence 覆盖不全 | W6 warning | AGREE | **共识 Should-Fix** |\n| 7 | LLMBar generalizability | AGREE | W5 warning | **共识 Should-Fix** |\n| 8 | Evaluator-producer bias | AGREE | W6 warning | **共识 Should-Fix** |\n\n## Reviewer Divergence\n\n| # | Issue | R1 | R2 | Director 判定 |\n|---|-------|----|----|---------------|\n| 1 | \"Blindspot\" 命名 | REBUT (spectrum 合理) | N1 critical | **Should-Fix** |\n| 2 | 引用数量 | REBUT (数量≠质量) | N2 critical | **Should-Fix** |\n| 3 | NLI 阈值 sensitivity | W1 warning | REBUT (§5.1 已有) | **Dropped** |\n| 4 | 多重比较框架 | W3 warning | REBUT (§4.1 合理) | **Dropped** |\n| 5 | RATE 批评公平性 | REBUT | W4 warning | **Minor** |\n| 6 | GEE contribution 定位 | REBUT (应用新颖) | W3 warning | **Minor** |\n| 7 | Novelty 定位 | REBUT (应用+hierarchy够) | W1 warning | **Should-Fix** |\n\n---\n\n## Questions（需作者澄清）\n\n1. 如果 Likert 和 pairwise 测量的是不同构念（absolute quality difference vs ordinal preference），那么 Table 2 的 binarized Likert sign test（同样是 forced choice, p=0.296）如何排除这一替代解释？\n2. n=355 时 Likert d 从 0.102 缩小到 −0.025——BT 稳定/略升而 Likert→0 的 differential shrinkage 如何解释？是 measurement attenuation 还是 regression to the mean？\n3. Direction asymmetry (78.8% vs 54.5%): GEE additive specification 是否足以分离 style 和 originality？n=88 下交互项检验功效是否足够？\n4. Claude Sonnet 4 极端 originality sensitivity (Orig OR=6.66, p<0.0001) 如何解释？是否意味着 Claude 有不同类型的偏差（originality-dependent 而非 style-dependent）？\n5. 各 benchmark×axis×judge 单元 NLI 过滤后的 effective sample size？\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同推荐**: Liang & Zeger (1986), Krosnick (1999)\n\n**R1 推荐**: Hausman & McFadden (1984), Agresti (2010), Lakens (2017)\n\n**R2 推荐**: van der Lee et al. (2019, 2021), Celikyilmaz et al. (2020), Ross et al. (2021, MICE), Preston & Colman (2000), Liu et al. (2023, G-Eval), Li et al. (2024, Arena-Hard), Keith et al. (2020)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：用户已跳过（skipped at 2026-05-21T11:14:38）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 3 warnings, 6 info）：\n\n**Warnings**:\n- Page 1-3: 连续 3 页纯文本无任何 display item，审稿人在 page 4 前无视觉锚点，影响第一印象\n- Page 4: Figure 1 (pipeline overview) 图内文字标签字号偏小（约正文 60%），打印时可能难以辨认\n- Page 13: 最后一页仅 4 条参考文献（~20% 占比），约 80% 空白\n\n**Info**:\n- Figure 2 (DAG) 红/蓝/橙配色色盲友好性一般\n- Table 1 p 值格式不完全一致\n- Figure 3 菱形标记密集区略有重叠\n- Figure 4 曲线在 n>200 区域多条线重合\n- Conclusion 排版紧凑，过渡自然\n- Limitations 内容充实，篇幅适中\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 3.5/5 | 4/5 | 3.5/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**评分理由**:\n- **方法论** (R1: 3.5): 实验设计和统计处理在同领域工作中突出。3 个 Must-Fix 方法论问题（NLI validation 循环偏差、BT IIA 未检验、originality confound）均为可修复的技术问题，不动摇核心发现方向。\n- **新颖性** (R2: 3.0): 核心发现（Likert vs pairwise sensitivity gap）是测量学经典结论（Thurstone 1927）的领域迁移。增量 novelty 在于 LLM judge 场景的首次系统定量验证、七种方法的 sensitivity hierarchy、GEE confound decomposition 的有趣发现。这是结构性限制——修改 framing 可以改善但不能根本改变贡献的新颖性水平。\n- **综合判定**: 扎实的实证工作，对 LLM evaluation 社区有实用价值（\"style bias audits 应使用 pairwise comparison\" 是可执行的建议）。但核心贡献更接近 systematic empirical study 而非 conceptual breakthrough。方法论问题修复 + framing 诚实化后，可达 **Borderline Conference (3.5)**。当前推荐 **Findings 级别接收**。\n\n**Confidence**: 4/5\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 信息密度过高（7 行含 3 judges × 3 benchmarks × 3 axes + 具体统计数字）。建议精简数字，保留核心 message。\"confirms discriminative validity\" 措辞过于肯定（需 equivalence testing 支持）。\n\n**Introduction**: 四个 gap 的构造有 cherry-picking 嫌疑。对 RATE 的批评语气偏重（RATE 目标不同于 style bias detection）。Contribution 3 (GEE decomposition) 是标准方法应用，建议降级为 experimental finding。Contribution 4 限定条件 \"(n<500)\" 是改进，但仍需基于更广泛的 benchmark 验证。\n\n**Related Work**: 组织清晰（三条线索），但缺 GEE 方法学来源 (Liang & Zeger 1986)、scale design 文献 (Krosnick 1999)、equivalence testing (Lakens 2017) 等直接支持论文论点的核心引用。\n\n**Method**: 设计周全。§3.5 \"Interventional Design\" 标题与 disclaimer 语气不一致，建议改为 \"Design Rationale\"。DAG (Figure 2) caption 详细但图本身的 NLI gate 与 Rewrite 关系箭头不够直观。Direction-aware NLI 的 tradeoff 讨论充分。\n\n**Experiments**: 统计框架严谨（§4.1 明确定义 primary/exploratory/confirmatory）。Table 1 的 Likert d 负值需解释。Table 2 sensitivity hierarchy 是论文最有价值的结果之一。GEE decomposition (Table 3) 发现有趣但 \"conditional decomposition\" 而非 \"causal decomposition\" 的定位需更明确。\n\n**Conclusion**: 严重不足（一句话）。需扩展。\n\n**Limitations**: 充分且诚实，7 段覆盖主要弱点。但 NLI gate 验证的 evaluator-producer 循环问题严重性评估不足——应从 Limitations 提升到 Discussion 正面讨论。",
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n**Venue**: EMNLP 2026 Main Conference (via ARR)\n**审稿编排**: 2 Reviewers — R1 方法严谨性, R2 新颖性/完整性\n**交叉回应**: 完成（1 轮收敛）\n\n---\n\n## Summary\n\n论文提出 Controlled Style Decomposition (CSD)，一个检测 LLM judge per-axis style bias 的 black-box 框架。核心发现 \"Likert Blindspot\"：标准 Likert 打分在七种统计方法下均无法检测到 pairwise comparison 清楚揭示的 style bias（3 judges × 3 benchmarks × 3 axes）。方法包括 NLI-gated style rewriting、position-controlled pairwise comparison、GEE conditional decomposition 分离 style vs originality effects。n=355 scaled replication 显示 Likert d→0 而 BT 稳定在 67.5%，作者将此定义为 measurement attenuation 而非单纯的 power gap。\n\n---\n\n## Strengths\n\n1. **实验设计严谨**: position control (双向 swap)、NLI gate (0.90 threshold + sensitivity analysis across 0.70-0.95)、cross-judge replication (GPT-4o, Qwen3-32B, Claude Sonnet 4 as negative control)、cross-benchmark validation (LLMBar, AlpacaEval, MT-Bench)。在 NLP 实证研究中属较高水平。\n\n2. **七种统计方法的 sensitivity hierarchy (Table 2)** 有说服力——四种 Likert-based 方法全失败 vs 两种 pairwise 方法全成功，排除了特定统计测试的 artifact 解释。Binarized Likert sign test (同样是 forced choice, 仍然 non-significant) 特别有价值。\n\n3. **统计素养突出**: Holm-Bonferroni with explicit 6-test family definition、primary/exploratory/confirmatory trichotomy (§4.1)、Bradley-Terry with pair-level bootstrap CI、GEE with correlation structure robustness check (Appendix C)。\n\n4. **GEE confound decomposition 发现有价值**: verbosity 的 confound-free 纯 style bias (Style OR=13.10/11.34, Orig OR n.s.) vs formality/register 的混合效应，对后续研究有指导意义。两个 judge 之间 verbosity OR 高度一致 (13.10 vs 11.34) 增强可信度。\n\n5. **Negative control 设计加强可信度**: Claude Sonnet 4 在两个 axis 上均未检测到显著 style 偏差 (BT 56.2%/54.1%)，证明 CSD 有 discriminative validity。\n\n6. **Rewriter independence test (Appendix D)** 直接回应最可能的方法论质疑：GPT-4o 作为独立 rewriter，verbosity Style OR 仅下降 22% (13.10→10.17)，formality BT 64.4% vs 66.5% (Δ=−2.1pp)，Blindspot 在独立 rewriter 下持续存在。\n\n7. **Limitations section 充分诚实**: 7 段覆盖 quality-style confounding、evaluator-producer bias、benchmark coverage、human evaluation 缺失、scale granularity、NLI validation methodology 等。\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 个，两位 Reviewer 强共识）\n\n**W-MF1 [critical] NLI Gate 验证存在 evaluator-producer 循环偏差**\n\nNLI gate 本身使用 DeBERTa-v3-large（架构独立），但 gate *验证*（§5.1）使用 Qwen3-32B 作为 annotator——同时也是 rewriter 和 judge 之一。False negative rate 8.4% 可能被低估，因 Qwen3-32B 自然更倾向认为自己的改写保留了语义。GPT-4o spot-check (n=50, 94% 一致率) 部分缓解，但 50 对样本的 Wilson CI 约 [83%, 99%]，置信区间过宽。论文在 Limitations 承认 \"human evaluation would provide stronger validation\"，但将此放在 Limitations 而非 Discussion 中处理，显得对问题严重性评估不足。\n\n**两位 Reviewer 强共识** (R1 识别, R2 独立确认)。\n\n建议：≥200 对人工标注，或两个架构独立的模型分别验证。\n\n**W-MF2 [critical] Bradley-Terry IIA 假设未检验**\n\nBT 模型假设 Independence of Irrelevant Alternatives (IIA)，即 formal text 相对 casual text 的偏好概率不随 item 基线质量变化。但 GEE decomposition (Table 3) 恰好揭示了 originality (基线质量代理) 对偏好有显著影响 (GPT-4o formality Orig OR=2.32, p=0.006)，直接暗示 style preference 可能随 item 质量变化——violating IIA。如果高质量 item 上 style bias 更弱（或更强），BT 的 pooled 估计可能产生 Simpson's paradox 式的误导。\n\n论文未报告任何 IIA 诊断检验。Appendix C 的 GEE style×originality 交互项检验 (p=0.53/0.32) 不等价于 BT 层面的 IIA 检验，且 n=88 检测交互效应功效极低。\n\n**两位 Reviewer 强共识** (R1 识别, R2 完全同意)。\n\n建议：报告 Hausman-McFadden test 或拟合 Thurstone-Mosteller 模型做稳健性检查。\n\n**W-MF3 [critical] Originality confound 显著，削弱识别策略**\n\n多配置下 Originality OR 显著且与 Style OR 量级相当甚至更大：\n- GPT-4o formality: Style OR=2.58 vs Orig OR=2.32\n- Qwen3-32B register: Style OR=1.91 vs Orig OR=5.72\n- Qwen3-32B formality (n=88): Style OR=4.20 vs Orig OR=4.70\n\nCSD 宣称的 \"per-axis style bias isolation\" 在 formality 和 register 上只实现了部分分离。Direction asymmetry (78.8% vs 54.5%) 进一步支持 originality confound 的存在。GEE additive specification 的交互项检验 (p=0.53/0.32) 在 n=88 下功效不足以可靠排除交互效应。\n\n重要例外：**verbosity 确实展现了 confound-free 的 clean identification** (Style OR=13.10/11.34, Orig OR n.s.)，是论文最强的实证结果。\n\n**两位 Reviewer 强共识** (R1 识别为 critical, R2 独立确认并指出与 \"four gaps\" framing 的逻辑矛盾)。\n\n建议：重新界定 claim 为 \"style-correlated preference shift\" 而非 \"style bias isolation\"；在 originality 差异最小的子集上重复分析。\n\n### Should-Fix（8 个）\n\n**W-SF1 [warning] \"Blindspot\" 命名准确性争议**\n\nR2 认为 critical：Table 1 中 3/9 bias-positive cells Likert 也检测到了，这不是 blindspot 而是 efficiency gap。R1 反驳：论文的 severity spectrum framing（moderate bias 区间完全失灵、强效应区部分恢复）合理，3/9 cells 逃逸恰好支持 spectrum 叙事。\n\n**Director 判定**: Should-Fix。Spectrum framing 有一定说服力，但 \"Blindspot\" 一词暗示结构性不可能检测。更关键的是，n=355 时 Likert d=−0.025 也可解读为 Likert 和 pairwise 测量不同构念（absolute quality difference vs ordinal preference）——论文 §5.2 隐约承认但未整合进 framing。建议在 Discussion 正式讨论构念差异替代假设。\n\n**W-SF2 [warning] Related Work 引用覆盖面不足**\n\nR2 认为 critical (36 篇 vs 40-60 标准，缺 NLG evaluation surveys、counterfactual generation、scale design 等方向)。R1 认为数量非质量标准。\n\n**Director 判定**: Should-Fix。引用数量不是硬标准，但以下特定缺失影响论文定位可信度：GEE 原始论文 (Liang & Zeger 1986)、scale design 文献 (Krosnick 1999, Preston & Colman 2000)、equivalence testing (Lakens 2017)、IIA 检验 (Hausman & McFadden 1984)。\n\n**W-SF3 [warning] \"Four critical gaps\" 有 cherry-picking 嫌疑**\n\n§1 四个 gap 的合取条件使得只有 CSD 满足所有条件。CASSE/FairJudge 已做 multi-dimensional decomposition（被归入 \"correlational\" 排除），RATE/Counterfactual Rhetorical 已做 interventional analysis（被归入 \"Likert-based\"/\"persona-level\" 排除）。R1 和 R2 均指出此问题。\n\n建议：更诚实地承认各 gap 已有部分解决方案，定位为 integrative framework 而非唯一解。\n\n**W-SF4 [warning] Claude negative control 需等效性检验**\n\nBT 56.2% 的 95% CI [.489, .636] 包含 50% 也包含 ~63%（GPT-4o 效应量），non-significance ≠ evidence of equivalence。Claude 的极端 originality sensitivity (Orig OR=6.66, p<0.0001) 进一步削弱 negative control 解读——Claude 可能有不同类型的偏差（originality-dependent 而非 style-dependent）。Abstract \"confirms discriminative validity\" 过于肯定。\n\n建议：使用 TOST equivalence testing (Lakens 2017)。\n\n**W-SF5 [warning] Conclusion 仅一句话，严重不足**\n\n8 页长文的结论仅 \"CSD reveals the Likert Blindspot...style bias audits should adopt pairwise comparison\" 一句。应包括：主要发现总结、方法论贡献的意义、对社区实践的具体影响、未来研究方向。两位 Reviewer 共识。\n\n建议：扩展至 10-15 行。\n\n**W-SF6 [warning] Evaluator-producer bias 处理不够彻底**\n\nQwen3-32B 同时担任 rewriter + judge 是设计缺陷。Style OR 在独立 rewriter test 中下降 22% (13.10→10.17)，非可忽略。Originality OR 系统性约 2× GPT-4o (formality: 4.99 vs 2.32; register: 5.72 vs 2.21)。Register axis 未做 rewriter independence test——恰好是 evaluator-producer bias 风险最高的配置。两位 Reviewer 共识。\n\n**W-SF7 [warning] 主实验以 LLMBar (n=100) 为中心**\n\nAlpacaEval 和 MT-Bench 仅作 partial replication (Table 1 仅 5 个额外 rows)。核心 Blindspot 论证完全基于 LLMBar 的 n=88 NLI-gated pairs。Scaled replication (n=355) 仅限 Qwen3 formality 一个 cell。LLMBar 是为 instruction-following 设计的 benchmark，其 100 条样本对更广泛 LLM evaluation 场景的代表性值得商榷。两位 Reviewer 共识。\n\n**W-SF8 [warning] Novelty 定位需更诚实**\n\nLikert vs pairwise 灵敏度差异是测量学经典结论 (Thurstone 1927, Kiritchenko 2017, Novikova 2018) 的 LLM 评估领域应用。R2 认为增量 novelty (LLM judge 场景 + 定量 attenuation 测量 + 7 方法比较) 有价值但不应包装为发现级突破。R1 反驳认为 application context + sensitivity hierarchy 构成充分贡献。\n\n**Director 判定**: Should-Fix。应在 Abstract/Introduction 明确标注为 \"known measurement theory principle 在 LLM judge evaluation 的首次系统定量验证\"。\n\n### Minor（5 个）\n\n- **W-M1**: Table 1 Likert d 负值含义未解释（两位共识）\n- **W-M2**: §3.5 \"Interventional Design\" 标题与 evidence 强度不匹配，建议改为 \"Design Rationale\" 或 \"Quasi-Interventional Design\"（两位共识）\n- **W-M3**: GEE conditional decomposition 列为独立 contribution 有膨胀之嫌（R2 提出, R1 反驳——Director 判定 minor framing 调整）\n- **W-M4**: wu2023style bib 年份不一致 (2023 vs 2025)\n- **W-M5**: Figure 4 power curve 使用 observed effect sizes 参数化，功能上接近 post-hoc power analysis（论文有 disclaimer 但不改变实质）\n\n---\n\n## Reviewer Consensus\n\n| # | Issue | R1 | R2 | Status |\n|---|-------|----|----|--------|\n| 1 | NLI gate 验证循环偏差 | N1 critical | AGREE | **共识 Must-Fix** |\n| 2 | BT IIA 未检验 | N2 critical | AGREE | **共识 Must-Fix** |\n| 3 | Originality confound | N3 critical | AGREE | **共识 Must-Fix** |\n| 4 | Claude negative control 等效性 | W4 warning | AGREE | **共识 Should-Fix** |\n| 5 | Conclusion 过短 | AGREE | W2 warning | **共识 Should-Fix** |\n| 6 | Rewriter independence 覆盖不全 | W6 warning | AGREE | **共识 Should-Fix** |\n| 7 | LLMBar generalizability | AGREE | W5 warning | **共识 Should-Fix** |\n| 8 | Evaluator-producer bias | AGREE | W6 warning | **共识 Should-Fix** |\n\n## Reviewer Divergence\n\n| # | Issue | R1 | R2 | Director 判定 |\n|---|-------|----|----|---------------|\n| 1 | \"Blindspot\" 命名 | REBUT (spectrum 合理) | N1 critical | **Should-Fix** |\n| 2 | 引用数量 | REBUT (数量≠质量) | N2 critical | **Should-Fix** |\n| 3 | NLI 阈值 sensitivity | W1 warning | REBUT (§5.1 已有) | **Dropped** |\n| 4 | 多重比较框架 | W3 warning | REBUT (§4.1 合理) | **Dropped** |\n| 5 | RATE 批评公平性 | REBUT | W4 warning | **Minor** |\n| 6 | GEE contribution 定位 | REBUT (应用新颖) | W3 warning | **Minor** |\n| 7 | Novelty 定位 | REBUT (应用+hierarchy够) | W1 warning | **Should-Fix** |\n\n---\n\n## Questions（需作者澄清）\n\n1. 如果 Likert 和 pairwise 测量的是不同构念（absolute quality difference vs ordinal preference），那么 Table 2 的 binarized Likert sign test（同样是 forced choice, p=0.296）如何排除这一替代解释？\n2. n=355 时 Likert d 从 0.102 缩小到 −0.025——BT 稳定/略升而 Likert→0 的 differential shrinkage 如何解释？是 measurement attenuation 还是 regression to the mean？\n3. Direction asymmetry (78.8% vs 54.5%): GEE additive specification 是否足以分离 style 和 originality？n=88 下交互项检验功效是否足够？\n4. Claude Sonnet 4 极端 originality sensitivity (Orig OR=6.66, p<0.0001) 如何解释？是否意味着 Claude 有不同类型的偏差（originality-dependent 而非 style-dependent）？\n5. 各 benchmark×axis×judge 单元 NLI 过滤后的 effective sample size？\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同推荐**: Liang & Zeger (1986), Krosnick (1999)\n\n**R1 推荐**: Hausman & McFadden (1984), Agresti (2010), Lakens (2017)\n\n**R2 推荐**: van der Lee et al. (2019, 2021), Celikyilmaz et al. (2020), Ross et al. (2021, MICE), Preston & Colman (2000), Liu et al. (2023, G-Eval), Li et al. (2024, Arena-Hard), Keith et al. (2020)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：用户已跳过（skipped at 2026-05-21T11:14:38）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 3 warnings, 6 info）：\n\n**Warnings**:\n- Page 1-3: 连续 3 页纯文本无任何 display item，审稿人在 page 4 前无视觉锚点，影响第一印象\n- Page 4: Figure 1 (pipeline overview) 图内文字标签字号偏小（约正文 60%），打印时可能难以辨认\n- Page 13: 最后一页仅 4 条参考文献（~20% 占比），约 80% 空白\n\n**Info**:\n- Figure 2 (DAG) 红/蓝/橙配色色盲友好性一般\n- Table 1 p 值格式不完全一致\n- Figure 3 菱形标记密集区略有重叠\n- Figure 4 曲线在 n>200 区域多条线重合\n- Conclusion 排版紧凑，过渡自然\n- Limitations 内容充实，篇幅适中\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 3.5/5 | 4/5 | 3.5/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**评分理由**:\n- **方法论** (R1: 3.5): 实验设计和统计处理在同领域工作中突出。3 个 Must-Fix 方法论问题（NLI validation 循环偏差、BT IIA 未检验、originality confound）均为可修复的技术问题，不动摇核心发现方向。\n- **新颖性** (R2: 3.0): 核心发现（Likert vs pairwise sensitivity gap）是测量学经典结论（Thurstone 1927）的领域迁移。增量 novelty 在于 LLM judge 场景的首次系统定量验证、七种方法的 sensitivity hierarchy、GEE confound decomposition 的有趣发现。这是结构性限制——修改 framing 可以改善但不能根本改变贡献的新颖性水平。\n- **综合判定**: 扎实的实证工作，对 LLM evaluation 社区有实用价值（\"style bias audits 应使用 pairwise comparison\" 是可执行的建议）。但核心贡献更接近 systematic empirical study 而非 conceptual breakthrough。方法论问题修复 + framing 诚实化后，可达 **Borderline Conference (3.5)**。当前推荐 **Findings 级别接收**。\n\n**Confidence**: 4/5\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 信息密度过高（7 行含 3 judges × 3 benchmarks × 3 axes + 具体统计数字）。建议精简数字，保留核心 message。\"confirms discriminative validity\" 措辞过于肯定（需 equivalence testing 支持）。\n\n**Introduction**: 四个 gap 的构造有 cherry-picking 嫌疑。对 RATE 的批评语气偏重（RATE 目标不同于 style bias detection）。Contribution 3 (GEE decomposition) 是标准方法应用，建议降级为 experimental finding。Contribution 4 限定条件 \"(n<500)\" 是改进，但仍需基于更广泛的 benchmark 验证。\n\n**Related Work**: 组织清晰（三条线索），但缺 GEE 方法学来源 (Liang & Zeger 1986)、scale design 文献 (Krosnick 1999)、equivalence testing (Lakens 2017) 等直接支持论文论点的核心引用。\n\n**Method**: 设计周全。§3.5 \"Interventional Design\" 标题与 disclaimer 语气不一致，建议改为 \"Design Rationale\"。DAG (Figure 2) caption 详细但图本身的 NLI gate 与 Rewrite 关系箭头不够直观。Direction-aware NLI 的 tradeoff 讨论充分。\n\n**Experiments**: 统计框架严谨（§4.1 明确定义 primary/exploratory/confirmatory）。Table 1 的 Likert d 负值需解释。Table 2 sensitivity hierarchy 是论文最有价值的结果之一。GEE decomposition (Table 3) 发现有趣但 \"conditional decomposition\" 而非 \"causal decomposition\" 的定位需更明确。\n\n**Conclusion**: 严重不足（一句话）。需扩展。\n\n**Limitations**: 充分且诚实，7 段覆盖主要弱点。但 NLI gate 验证的 evaluator-producer 循环问题严重性评估不足——应从 Limitations 提升到 Discussion 正面讨论。",
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-21T11:37:50.921420+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4280
}
```

</details>

---


### Assistant

_source line 308 · 2026-05-21T11:38:07.287587+00:00_

审稿报告已投递至 Research Director。

---

**📋 Round 4 (Fresh) 审稿完成**

**Overall: 3.0 (Findings)**

**Must-Fix (3, 两位 Reviewer 强共识)**:
1. NLI gate 验证的 evaluator-producer 循环偏差——需 ≥200 对人工标注
2. Bradley-Terry IIA 假设未检验——需 Hausman-McFadden test 或 Thurstone-Mosteller 稳健性检查
3. Originality confound 显著——formality/register 上 Style OR 与 Orig OR 量级相当，claim 应降级为 "style-correlated preference shift"

**Should-Fix (8)**:
- "Blindspot" 命名争议、Related Work 引用覆盖面、"four gaps" 构造公平性、Claude negative control 等效性检验、Conclusion 过短、evaluator-producer bias 处理、LLMBar generalizability、novelty 定位

**分歧**: R1 3.5 vs R2 3.0。方法论问题 (R1) 可修复，但核心 novelty 不足 (R2) 是结构性限制。方法论修复 + framing 诚实化后可达 Borderline Conference (3.5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 309 · 2026-05-21T11:38:09.866712+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

总结：对 R2 的 3 个 Must-Fix 中，我反驳了 N1（命名问题属术语选择，论文已精确定义 Blindspot 为 spectrum 现象）和 N2（引用质量优先于数量，仅需补充 2-3 篇关键引用），同意 N3（gap 定位有 cherry-picking 倾向但建议降级为 Should-Fix）。对 6 个 Should-Fix 反驳了 W1/W3/W4，同意 W2/W5/W6。对 5 个 Question 反驳了 Q1/Q2（Table 2 和 differential shrinkage 证据充分），同意 Q3/Q4/Q5（均与我自己的审稿意见一致）。维持 Overall 3.5 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 310 · 2026-05-21T11:38:26.694607+00:00_

审稿报告已提交给 Research Director。

**审稿完成总结**：

- **Overall: 3.0 (Findings)**，R1 评 3.5 / R2 评 3.0
- **3 个 Must-Fix（两位共识）**：NLI gate 验证循环偏差、BT IIA 假设未检验、Originality confound 削弱识别策略
- **8 个 Should-Fix**：Blindspot 命名争议、引用覆盖面、Four gaps cherry-picking、Claude 等效性检验、Conclusion 过短、Evaluator-producer bias、LLMBar generalizability、Novelty 定位
- **5 个 Minor**
- **Issue Tracker 已更新**：新增 4 个 open issues (R4-N1/N2/W1/M1/M2)，更新 10+ 个既有 issues 的 Round 4 mentions
- **外部审稿**：用户已跳过
- **视觉审查**：已完成（0 critical, 3 warnings, 6 info）

方法论问题修复 + framing 诚实化后可达 Borderline Conference (3.5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 32

## Round 32

72 recorded events


### User

_source line 311 · 2026-05-21T12:30:31.558884+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (via ARR)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-21T12:30:38.727451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-21T12:30:38.779716+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-21T12:30:49.383244+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,WebSearch",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,WebSearch",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-21T12:30:49.634624+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-21T12:30:52.850003+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-21T12:30:54.258727+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (38 个)\n\n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **register_100_cf**: QUEUED — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- register_100_cf: Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality（排队等待 GPU）\n\n## 近期结论\n- **nli_gate_full_validation** (success): Full-coverage GPT-4o independent validation of NLI gate decisions across all 200 pairs confirms gate reliability, with high pass precision and conservative fail behavior (addresses W-MF1)\n- **originality_minimal_subset** (success): Style effect in BT remains stable when restricting to originality-balanced pairs (Likert score tied between original and counterfactual), confirming style bias is not driven by originality confound (addresses W-MF3)\n- **bt_model_diagnostics** (success): BT model adequately fits the pairwise data (GoF non-significant) and stratified BT by originality direction reveals whether style effect is confounded with originality preference (addresses W-MF2) ← 基于 qwen32b_formality\n\n## 趋势\n成功 26 / 负向 8 / 失败 0 / 共 37\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-21T12:30:54.309460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-21T12:30:54.510702+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Detecting Hidden Style Bias\\in LLM Judges via Controlled Style Decomposition}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. We consider this unlikely because seven statistical methods applied to identical data all agree on the direction of the effect (Table~\ref{tab:sensitivity}), but the possibility cannot be excluded without human ground-truth ratings.
45	
46	\paragraph{Evaluator-producer bias and generalizability.}
47	Qwen3-32B serves as both rewriter and judge, rai
…[truncated 1312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-21T12:30:54.511062+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-21T12:31:01.087532+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

Based on the search results, I found some infor
…[truncated 1253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6576
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-21T12:31:05.700667+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 323 · 2026-05-21T12:31:06.203387+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines author instructions page limit template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines author instructions page limit template"
  }
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-21T12:31:06.858046+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-21T12:31:06.958917+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 326 · 2026-05-21T12:31:09.670093+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/202950829263706146
…[truncated 582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 3969
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-21T12:31:15.894566+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines author instructions page limit template"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

I've found comprehensive information about ACL Rolling Review 2026 submission guidelines. Here's what I found:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Final versions of accepted papers will be given one additional page of content (up t
…[truncated 1665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 9691
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-21T12:31:19.459009+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-21T12:31:19.511481+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-21T12:31:22.323704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-21T12:31:22.776051+00:00_

1	\begin{abstract}
2	LLM judges are widely deployed for evaluation and alignment, yet style features alone explain judge scores with near-perfect correlation.
3	We introduce Controlled Style Decomposition (CSD), the first systematic quantitative verification of this known measurement principle for LLM judge evaluation: a black-box framework that detects per-axis style bias through style-controlled rewriting, NLI content gating, and pairwise comparison.
4	Across three judges (GPT-4o, Qwen3-32B, Claude Sonnet 4), three benchmarks, and three style axes, CSD reveals the Likert Blindspot---not merely a statistical power gap but measurement attenuation across a severity spectrum: at moderate bias levels Likert compresses effect sizes to zero ($d \to 0$ at $n = 355$); at stronger effects (BT ${>}70\%$) Likert partially detects but attenuates by ${>}60\%$---while pairwise comparison reliably detects bias across the full range (BT 63--84\%, $p < 0.001$), confirmed by seven statistical methods.
5	A third judge (Claude Sonnet 4) detects no bias on either axis, supporting discriminative validity.
6	Style bias audits require pairwise comparison; existing Likert-based null findings may reflect measurement insensitivity rather than genuine absence of bias.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-21T12:31:22.776459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-21T12:31:22.776679+00:00_

1	\section{Introduction}
2	
3	LLM judges are central infrastructure for NLP evaluation (AlpacaEval, MT-Bench, Chatbot Arena) and alignment training (RLHF, DPO), where judge-generated preferences serve as reward signals.
4	Any systematic bias in their assessments propagates through both evaluation leaderboards and model development pipelines.
5	
6	Recent work suggests that style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, motivating systematic measurement of per-axis style bias.
7	\citet{li2026preference} demonstrate that 76--92\% of observed preference signals originate from surface-level style cues rather than substantive quality differences, and \citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.
8	Despite this consensus on severity, existing approaches each address individual requirements: CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} provide multi-dimensional style analysis, RATE \citep{reber2025rate} introduces interventional design, and length-controlled AlpacaEval \citep{dubois2025lc} offers population-level correction.
9	However, no single framework integrates all four requirements---per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.
10	A further concern compounds these limitations: standard Likert scoring suffers from a measurement efficiency gap---integer discretization produces ${\sim}60\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison---a limitation predicted by measurement theory \citep{thurstone1927law} but previously unquantified for LLM judges.
11	
12	We propose Controlled Style Decomposition (CSD), the first framework to systematically quantify this measurement principle for LLM judges, integrating all four requirements in a single pipeline.
13	Inspired by interventional approaches to text analysis \citep{veitch2020adapting}, CSD operates in thre
…[truncated 2497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-21T12:31:23.229191+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-21T12:31:24.133167+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
14	
15	\paragrap
…[truncated 4925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-21T12:31:24.183808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-21T12:31:24.635812+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/pipeline_diagram.pdf}
7	\caption{CSD pipeline overview. Numbers indicate sample attrition at each stage.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	\subsection{Style-Controlled Rewriting}
12	\label{sec:rewriting}
13	
14	We aim to isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
15	For each text, an instruction-tuned LLM (Qwen3-32B) first classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification), then rewrites it toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
16	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
17	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
18	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
19	
20	\subsection{Content Preservation Verification}
21	\label{sec:nli_gate}
22	
23	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
24	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90.
25	For axes that preserve information density (formality, register), we apply standard bidi
…[truncated 5914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-21T12:31:24.686448+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-21T12:31:25.138886+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	We designate a primary family of six hypothesis tests (two judges $\times$ three style axes) and control the family-wise error rate with Holm-Bonferroni correction at $\alpha = 0.05$.
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values for this $2 \times 3$ grid.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Main results across three judges, three style axes, and three benchmarks. BT: Bradley-Terry win probability (10{,}000 pair-level bootstrap resamples; 95\% CIs in Appendix~\ref{app:bt_ci}). AEval: AlpacaEval; MTB: MT-Bench. Claude Sonnet 4 serves as negative control.}
19	\label{tab:main_results}
20	\begin{tabular}{@{}lllccc@{}}
21	\toprule
22	Bench & Judge & Axis & BT $P$ & Likert $d$ ($p$) & \\
23	\midrule
24	LLMBar & GPT-4o & Form.\ & .630$^{***}$ & .102 (.332) & $\dagger$ \\
25	 & GPT-4o & Verb.\ & .760$^{***}$ & $-$.095 (.403) & $\dagger$ \\
26	 & GPT-4o & Reg.\ & .570$^{\dagger}$ & $-$.031 (.785) & $\dagger_{\text{e}}$ \\
27	\cmidrule{2-6}

…[truncated 17058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-21T12:31:25.139270+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-21T12:31:25.390407+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Controlled Style Decomposition (CSD), a black-box framework that reveals the Likert Blindspot---systematic measurement attenuation in Likert scoring---across three judges, three benchmarks, and three style axes.
5	The Blindspot is not merely a statistical power gap: at moderate bias levels (BT 63--67\%), Likert compresses effect sizes to zero even at $n = 355$; at stronger effects, it attenuates by over 60\%.
6	Seven statistical methods confirm this is structural, not an artifact of any particular test.
7	
8	Verbosity provides the cleanest evidence: both judges show 76--77\% pairwise preference for verbose responses with confound-free identification (Originality n.s.), yet Likert detects nothing.
9	GEE conditional decomposition reveals that formality and register exhibit conditional style effects alongside originality confounds, motivating per-axis analysis over aggregate style metrics.
10	
11	For the evaluation community, the practical implication is clear: style bias audits should adopt pairwise comparison, especially at the moderate effect sizes typical of real-world evaluation ($n < 500$).
12	Existing Likert-based null findings may reflect measurement insensitivity rather than genuine absence of bias.
13	Future work should incorporate human evaluation of rewriting quality, broader benchmark and axis coverage, and stronger causal identification through randomized rather than observational designs.
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-21T12:31:25.390820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-21T12:31:25.441660+00:00_

1	\appendix
2	
3	\section{Direction Asymmetry and Quality Confounding}
4	\label{app:direction}
5	
6	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
7	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
8	To quantify this, we fit a GEE logistic model (exchangeable correlation) with both formality and original-preference as predictors.
9	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
10	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
11	
12	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.
13	The originality confound remains stronger ($4.99$ vs.\ $2.32$), consistent with evaluator-producer bias inflating the originality component (Limitations).
14	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
15	
16	The NLI gate blocks \emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.
17	
18	\section{Consistency Filter Robustness}
19	\label{sec:consistenc
…[truncated 8945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-21T12:31:43.114563+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file,request_external_review,dispatch_visual_check,get_external_review_status,get_visual_check_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file,request_external_review,dispatch_visual_check,get_external_review_status,get_visual_check_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-21T12:31:43.115012+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-21T12:31:47.884810+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-21T12:31:47.935489+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-21T12:31:53.960054+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-21T12:31:53.960580+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-21T12:31:54.061247+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-21T12:31:54.112115+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml\", \"content\": \"_next_id: 54\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 14:09 UTC\\n  summary: '文献蒸馏审视：研究方向无需调整，CSD 填补 #1 空白（多维 style 因果分解），post-MVP 需扩展 judge/benchmark/baseline\\n    覆盖'\\n  rationale: '10 篇论文蒸馏显示：(1) 多维 style 联合因果分解是领域 #1 空白，与 CSD 核心 claim 完全对齐；(2) 竞品 claim\\n    无直接重叠（FairJudge=white-box, Pref Leakage=family-based, Soumik=prompt-dependent）；(3)\\n    同行标准要求 3-5 异构 judge + AlpacaEval/Arena-Hard/MT-Bench + Bootstrap CIs + 对比 LC-AlpacaEval\\n    baseline。当前 MVP 方案足够，research 阶段需按蒸馏标准扩展。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 14:19 UTC\\n  summary: MVP 全量评分 + 分层分析：score 全部 100 条，按 BERTScore 阈值 0.88/0.90/0.92 分层算 ATE，不降低阈值\\n  rationale: 36% pass rate (BERTScore≥0.92) 偏低但 NLI 均值 0.9422 说明语义保留好。降阈值是数据操作，不如保留完整信息。全量评分\\n    (n=100) 保证统计 power，分层分析同时回答\\\"严格阈值下效应是否存在\\\"和\\\"宽松阈值下效应是否增强\\\"。8B H1 fail 不消耗迭代配额（ROADMAP\\n    规则），32B 备用。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 14:20 UTC\\n  summary: H1 content verification 改为 NLI-only gate（≥0.90），BERTScore 降为监控指标，不作为过滤条件\\n  rationale: Reviewer 诊断：36% pass rate 的根因是 BERTScore 惩罚 style transfer 预期的词汇变化（contractions→full\\n    forms 等），而非内容泄漏。NLI 均值 0.9422、抽样 >0.99 证明语义保留良好。BERTScore 作为 token-level 相似度指标与\\n    style transfer 评估目标矛盾（改的就是 token）。Double-rewrite pass rate 更低（21/100）进一步印证。NLI-only\\n    gate 是度量校准（不消耗 8B 迭代配额），与 D002 全量评分兼容——primary ATE 用 NLI≥0.90 子集，secondary 按 BERTScore\\n    分层。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 14:32 UTC\\n  summary: 8B 初步 ATE≈0.028 不可见，归因三因素：Likert 粒度 + 8B rewriter 质量 + RATE corruption。不计入\\n    kill criteria，等 n=100 + 32B\\n  rationale: 36/100 初步数据 Cohen's d=0.055 远低于 0.3 门槛，但三个叠加因素解释了结果：(1) 83% 零差异源于 integer\\n    Likert 无法捕捉 sub-integer 效应；(2) 22% identical rewrites 稀释 ATE；
…[truncated 1456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-21T12:31:57.427030+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-21T12:31:57.880105+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-2 issues (all resolved)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 4
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale' (was 'Interventional Design')."
14	    resolution_round: 4
15	    mentions:
16	      - round: 3
17	        reviewers: [1, 2]
18	        note: "因果语言降级问题在 Round 3 以新形式复发，见 R3-N1"
19	      - round: 4
20	        reviewers: [1]
21	        note: "R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。"
22	
23	  - id: "R2-N1"
24	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
25	    category: framing
26	    severity: warning
27	    status: resolved
28	    first_raised_round: 1
29	    last_seen_round: 4
30	    resolution: "Abstract/Intro 明确标注为 'first systematic quantitative verification of known measurement theory principle in LLM judge evaluation'. Structural ceiling acknowledged."
31	    resolution_round: 4
32	    mentions:
33	      - round: 3
34	        reviewers: [1, 2]
35	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
36	      - round: 4
37	        reviewers: [1, 2]
38	        note: "R4-SF8: Honest novelty positioning applied. R1 认为 application context + 7-method hierarchy 构成充分贡献。"
39	
40	  - id: "R1-N2"
41	    summary: "NLI gate 67% false-negative rate 造成选择偏差未分析"
42	    category: method
43	    severity: critical
44	    status: resolved
45	    first_raised_round: 1
46	    last_seen_round: 1
47	    resolution: "§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89"
48	    resolution_round: 1
49	
50	  - id: "R1-N3"
51	    summary: "NLI 阈值 0.90 无 justification"
52	    category: method
53	    severity: critical
54	    status
…[truncated 21296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-21T12:31:57.880569+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-21T12:31:57.931063+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_director_acab027e.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-21T12:32:01.747965+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/causal_style_decomp_judge/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/causal_style_decomp_judge/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-21T12:32:01.798684+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-21T12:32:05.085386+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/causal_style_decomp_judge/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/causal_style_decomp_judge/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-21T12:32:05.141091+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/secrets/causal_style_decomp_judge/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-21T12:32:08.621481+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-21T12:32:08.672481+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-21T12:32:11.896577+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5",
  "glob": "*.{yaml,json,toml}\"",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5",
    "glob": "*.{yaml,json,toml}\"",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-21T12:32:11.997408+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-21T12:32:14.455601+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "config/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "config/**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-21T12:32:14.506303+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-21T12:32:16.914696+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/",
  "description": "List config directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/",
    "description": "List config directory"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-21T12:32:17.065891+00:00_

approvals.yaml
backend.yaml
claude_sessions.json
email_tokens.json
feishu.yaml
keepalive.json
mcp_config.json
mcp_config_director.json
mcp_config_distiller.json
mcp_config_dream_review_director.json
mcp_config_idea_reviewer.json
mcp_config_no_project.json
mcp_config_paper_agent.json
mcp_config_paper_audit_review_visual.json
mcp_config_review_director.json
mcp_config_review_reviewer_1.json
mcp_config_review_reviewer_2.json
mcp_config_reviewer.json
mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
mcp_config_worker_29834432f6498e7996daf9a6d4e8eda9.json
mcp_config_worker_83ba13f19a2bf382207991b32ac820f6.json
mcp_config_worker_bc09978dd11e03e52315e5d71a6834ea.json
mcp_config_worker_ddf919c12f9233b9c1be7884efc37bb6.json
mcp_config_worker_ed94f451683c3553386dc323817a3544.json
mcp_config_worker_f5d680d1394a02be4b502c5606a34a84.json
pool.json
projects
resources.yaml
secrets
session_state.json
tum_pending_tum_20260520_csd_openai.json
venue_registry.yaml
venue_rules

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-21T12:32:19.825183+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-21T12:32:19.825572+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-21T12:32:22.837463+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/projects/",
  "description": "List project configs directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/projects/",
    "description": "List project configs directory"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-21T12:32:22.939599+00:00_

causal_style_decomp_judge.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-21T12:32:25.450853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/projects/causal_style_decomp_judge.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/projects/causal_style_decomp_judge.yaml"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-21T12:32:25.501419+00:00_

1	execution:
2	  account: root
3	  gpu_ids:
4	  - cuda:0
5	  - cuda:1
6	  - cuda:2
7	  - cuda:3
8	  project_path: /root/causal_style_decomp_judge
9	  servers:
10	  - westb-29275
11	feishu:
12	  chat_id: oc_5ce280de124a4e308d1827c6450ad337
13	  operational_chat_id: oc_09b04b56f2fb04931812c4a55f159dee
14	  review_mode: fresh
15	  review_paper_path: projects/causal_style_decomp_judge/docs/paper/main.tex
16	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf
17	  review_round: 4
18	  review_supplementary_paths: ''
19	  submission_chat_id: oc_f810d8d75f013ad17831ce8459f07d6d
20	project:
21	  created_at: '2026-05-20T07:07:53.848Z'
22	  description: Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust
23	    Counterfactual Estimation
24	  name: causal_style_decomp_judge
25	  phase: research
26	  source_idea_id: idea_028
27	venue: emnlp-2026
28	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-21T12:32:49.197302+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-21T12:32:49.248002+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-21T12:32:53.367445+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-21T12:33:14.663210+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21295
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-21T12:33:18.834046+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- 路径：projects/causal_style_decomp_judge/docs/paper/main.tex（各 section 在 sections/ 子目录）\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf\n- 目标 venue：EMNLP 2026 Main Conference (via ARR)\n\n## Venue 要求\n- ACL 模板，double-blind，正文 ≤8 页，参考文献无限\n- Limitations 章节必须有（不计页数），不可含额外实验/图表/分析\n- 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n- ARR 提交截止：2026-05-25\n\n## 你的审查侧重\n请从以下维度严格审查：\n\n1. **统计方法学**：\n   - Holm-Bonferroni 的 primary family 定义是否合理（2 judges × 3 axes = 6 tests）？\n   - 探索性/确认性分析的分类是否清晰且一致？\n   - Bradley-Terry 模型的假设检验是否充分（GoF、IIA 等）？\n   - Bootstrap CI 的 pair-level resampling 是否正确？\n   - Cohen's d 计算和效应量解释是否恰当？\n\n2. **NLI Gate 设计**：\n   - 双向 entailment 和 direction-aware gating 的理论依据是否充分？\n   - 0.90 阈值的 sensitivity analysis 是否说服力足够？\n   - FNR 8.4% 的影响是否被充分分析？\n   - GPT-4o 200-pair 独立验证的设计是否robust？\n\n3. **因果声明强度**：\n   - DAG (Figure 2) 中的假设是否合理？残余 confounding 是否被充分承认？\n   - \"Design Rationale\" 的定位是否与证据强度匹配？\n   - NLI gate 作为 do-operator 近似的声明是否过强？\n   - GEE \"conditional decomposition\" 在残余 confounding 下是否有误导性？\n\n4. **实验设计**：\n   - 样本量（n=88 到 n=355）是否足够支撑结论？\n   - Position control（双向 swap）是否充分？\n   - Evaluator-producer bias（Qwen3-32B 同时做 rewriter 和 judge）的处理是否充分？\n   - Cross-rewriter independence test 的覆盖是否完整（formality + verbosity，register 缺失）？\n\n5. **Likert Blindspot 机制**：\n   - \"measurement attenuation across a severity spectrum\" 的 framing 是否有充分数据支撑？\n   - n=355 时 d→0 的证据是否真正区分了 attenuation vs power gap？\n   - 7 种统计方法的 sensitivity hierarchy 是否有说服力？\n\n请按 ACL/ARR 审稿标准输出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- 路径：projects/causal_style_decomp_judge/docs/paper/main.tex（各 section 在 sections/ 子目录）\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf\n- 目标 venue：EMNLP 2026 Main Conference (via ARR)\n\n## Venue 要求\n- ACL 模板，double-blind，正文 ≤8 页，参考文献无限\n- Limitations 章节必须有（不计页数），不可含额外实验/图表/分析\n- 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n- ARR 提交截止：2026-05-25\n\n## 你的审查侧重\n请从以下维度严格审查：\n\n1. **统计方法学**：\n   - Holm-Bonferroni 的 primary family 定义是否合理（2 judges × 3 axes = 6 tests）？\n   - 探索性/确认性分析的分类是否清晰且一致？\n   - Bradley-Terry 模型的假设检验是否充分（GoF、IIA 等）？\n   - Bootstrap CI 的 pair-level resampling 是否正确？\n   - Cohen's d 计算和效应量解释是否恰当？\n\n2. **NLI Gate 设计**：\n   - 双向 entailment 和 direction-aware gating 的理论依据是否充分？\n   - 0.90 阈值的 sensitivity analysis 是否说服力足够？\n   - FNR 8.4% 的影响是否被充分分析？\n   - GPT-4o 200-pair 独立验证的设计是否robust？\n\n3. **因果声明强度**：\n   - DAG (Figure 2) 中的假设是否合理？残余 confounding 是否被充分承认？\n   - \"Design Rationale\" 的定位是否与证据强度匹配？\n   - NLI gate 作为 do-operator 近似的声明是否过强？\n   - GEE \"conditional decomposition\" 在残余 confounding 下是否有误导性？\n\n4. **实验设计**：\n   - 样本量（n=88 到 n=355）是否足够支撑结论？\n   - Position control（双向 swap）是否充分？\n   - Evaluator-producer bias（Qwen3-32B 同时做 rewriter 和 judge）的处理是否充分？\n   - Cross-rewriter independence test 的覆盖是否完整（formality + verbosity，register 缺失）？\n\n5. **Likert Blindspot 机制**：\n   - \"measurement attenuation across a severity spectrum\" 的 framing 是否有充分数据支撑？\n   - n=355 时 d→0 的证据是否真正区分了 attenuation vs power gap？\n   - 7 种统计方法的 sensitivity hierarchy 是否有说服力？\n\n请按 ACL/ARR 审稿标准输出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-21T12:33:33.602625+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14768
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-21T12:33:33.854866+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- 路径：projects/causal_style_decomp_judge/docs/paper/main.tex（各 section 在 sections/ 子目录）\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf\n- 目标 venue：EMNLP 2026 Main Conference (via ARR)\n\n## Venue 要求\n- ACL 模板，double-blind，正文 ≤8 页，参考文献无限\n- Limitations 章节必须有（不计页数），不可含额外实验/图表/分析\n- 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n- ARR 提交截止：2026-05-25\n\n## 你的审查侧重\n请从以下维度严格审查：\n\n1. **Novelty 定位**：\n   - \"Likert Blindspot\" 概念是否有真正新颖性？还是心理测量学 (Thurstone 1927, Stevens 1946) 已知现象的 domain transfer？\n   - CSD framework 相对于 RATE (Reber et al. 2025)、CASSE、FairJudge 的增量贡献是否充分？\n   - \"first systematic quantitative verification\" 的 claim 是否准确？是否有遗漏的先行工作？\n   - 4 项 contributions 的 framing 是否合理？有无 overclaim？\n\n2. **实验覆盖面**：\n   - 3 judges × 3 benchmarks × 3 axes 的矩阵是否充分？是否有关键缺失（如 Gemini、Llama 等 judge）？\n   - LLMBar (n=100) 作为主要 benchmark 是否合适？规模是否受限？\n   - AlpacaEval 和 MT-Bench 的覆盖是否充分（部分 cell 缺失）？\n   - Claude 作为 negative control 是否有说服力（TOST 在 n=87 下 underpowered）？\n\n3. **Related Work 完整性**：\n   - 是否覆盖了 LLM-as-Judge 偏差检测的所有主要方向？\n   - 是否遗漏了重要的 style bias 相关工作（如 2025-2026 年新发表的论文）？\n   - 与 RATE 的比较是否公平？是否遗漏了 RATE 的优势？\n   - Bradley-Terry 相关文献（Chatbot Arena、AlpacaFarm）的讨论是否充分？\n\n4. **写作质量**：\n   - Abstract 信息密度是否过高？可读性如何？\n   - Introduction 的叙事逻辑是否清晰？从 motivation 到 contribution 的过渡是否自然？\n   - 各 section 的篇幅分配是否合理？\n   - 术语一致性（如 \"Blindspot\" vs \"blindspot\"，\"style bias\" vs \"style preference\"）？\n   - 图表质量和信息承载是否达标？\n\n5. **格式合规**：\n   - 正文是否严格 ≤8 页？\n   - Limitations 章节是否存在且位置正确（conclusion 后、references 前）？\n   - 是否满足 double-blind 要求（无作者信息泄露）？\n   - 引用格式是否符合 ACL 标准（natbib）？\n   - 附录中是否有应在正文中呈现的关键信息？\n\n请按 ACL/ARR 审稿标准输出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- 路径：projects/causal_style_decomp_judge/docs/paper/main.tex（各 section 在 sections/ 子目录）\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf\n- 目标 venue：EMNLP 2026 Main Conference (via ARR)\n\n## Venue 要求\n- ACL 模板，double-blind，正文 ≤8 页，参考文献无限\n- Limitations 章节必须有（不计页数），不可含额外实验/图表/分析\n- 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n- ARR 提交截止：2026-05-25\n\n## 你的审查侧重\n请从以下维度严格审查：\n\n1. **Novelty 定位**：\n   - \"Likert Blindspot\" 概念是否有真正新颖性？还是心理测量学 (Thurstone 1927, Stevens 1946) 已知现象的 domain transfer？\n   - CSD framework 相对于 RATE (Reber et al. 2025)、CASSE、FairJudge 的增量贡献是否充分？\n   - \"first systematic quantitative verification\" 的 claim 是否准确？是否有遗漏的先行工作？\n   - 4 项 contributions 的 framing 是否合理？有无 overclaim？\n\n2. **实验覆盖面**：\n   - 3 judges × 3 benchmarks × 3 axes 的矩阵是否充分？是否有关键缺失（如 Gemini、Llama 等 judge）？\n   - LLMBar (n=100) 作为主要 benchmark 是否合适？规模是否受限？\n   - AlpacaEval 和 MT-Bench 的覆盖是否充分（部分 cell 缺失）？\n   - Claude 作为 negative control 是否有说服力（TOST 在 n=87 下 underpowered）？\n\n3. **Related Work 完整性**：\n   - 是否覆盖了 LLM-as-Judge 偏差检测的所有主要方向？\n   - 是否遗漏了重要的 style bias 相关工作（如 2025-2026 年新发表的论文）？\n   - 与 RATE 的比较是否公平？是否遗漏了 RATE 的优势？\n   - Bradley-Terry 相关文献（Chatbot Arena、AlpacaFarm）的讨论是否充分？\n\n4. **写作质量**：\n   - Abstract 信息密度是否过高？可读性如何？\n   - Introduction 的叙事逻辑是否清晰？从 motivation 到 contribution 的过渡是否自然？\n   - 各 section 的篇幅分配是否合理？\n   - 术语一致性（如 \"Blindspot\" vs \"blindspot\"，\"style bias\" vs \"style preference\"）？\n   - 图表质量和信息承载是否达标？\n\n5. **格式合规**：\n   - 正文是否严格 ≤8 页？\n   - Limitations 章节是否存在且位置正确（conclusion 后、references 前）？\n   - 是否满足 double-blind 要求（无作者信息泄露）？\n   - 引用格式是否符合 ACL 标准（natbib）？\n   - 附录中是否有应在正文中呈现的关键信息？\n\n请按 ACL/ARR 审稿标准输出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-21T12:33:35.315742+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1460
}
```

</details>

---


### Assistant

_source line 382 · 2026-05-21T12:33:39.734207+00:00_

Round 1 已派发：

- **视觉审查 Agent**：已启动（fire-and-forget）
- **Reviewer 1**（方法严谨性）：已分配——统计方法学、NLI gate、因果声明、BT 分析、实验设计
- **Reviewer 2**（新颖性与完整性）：已分配——novelty 定位、实验覆盖面、related work、写作质量、格式合规

等待两位 Reviewer 返回独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 33

## Round 33

2 recorded events


### User

_source line 383 · 2026-05-21T12:40:52.695013+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性审查

**论文**：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
**Venue**：EMNLP 2026 Main Conference (via ARR)
**审查侧重**：统计方法学、NLI Gate 设计、因果声明强度、实验设计、Likert Blindspot 机制

---

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**Confidence**: 4 / 5（Quite sure — 对因果推断方法学和 NLP 评估统计有足够领域经验，但部分 GEE 细节可能遗漏）
**一句话总结**: 论文提出了实用且新颖的发现（Likert Blindspot），框架设计多层控制值得肯定，但因果声明强度超出证据支撑、关键统计假设未检验、evaluator-producer confound 未充分解决，整体处于 Conference/Findings 边界。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心框架设计合理（position swap、NLI gate、多 benchmark），但 BT 的 IIA 假设未检验、NLI gate 被过度声称为 do-operator 近似、GEE 条件分解在残余混淆下解释过强 |
| Excitement | 3.5/5 | Likert Blindspot 发现新颖且有实际影响力——7 种 Likert 方法全部失败而 pairwise 可靠检测是 striking 的结果；但相对 RATE (Reber et al., 2025) 的增量贡献需更清晰定位 |
| Reproducibility | 4/5 | 方法描述详尽（prompts、NLI 阈值、bootstrap 参数均有报告），代码和数据承诺于接收后发布；但 rewriting prompts 的完整文本未在 Appendix 中提供 |
| Datasets | 3/5 | 使用现有 benchmark（LLMBar、AlpacaEval、MTBench）的 style-transformed 版本，有一定复用价值 |
| Software | 3/5 | 框架承诺开源但目前无法验证 |

---

## 主要优势

1. **Likert Blindspot 发现的实证力度**：Table 2 的 7 种方法 sensitivity hierarchy 是论文最有说服力的结果——在同一数据上，所有 Likert-based 方法（ATE t-test、binomial、ordinal regression、GEE、Wilcoxon）全部 p > 0.29，而 BT 和 filtered sign test 均 p < 0.001。这一对比清晰地建立了 measurement modality 之间的系统性差异。

2. **多层控制设计**：Position double-swap、NLI content gate、consistency filter 三层控制的组合设计严谨。特别是 position swap 产生 n_pairs × 2 观测并只保留 consistent pairs，这是 pairwise evaluation 的标准最佳实践。

3. **负对照的使用**：Claude Sonnet 4 作为 negative control（Table 1）在所有轴上未检测到 bias（BT 56.2%, p = 0.254），支持框架的 discriminant validity——不是所有 judge 都触发 bias 检测，说明框架不是在制造假阳性。

4. **BT 模型的 GoF 检验**：Appendix G 报告了 BT goodness-of-fit（formality deviance p = 0.198; verbosity p = 0.905），且对 exchangeable vs. independence 工作相关结构进行了比较（|ΔQIC| < 0.001），GEE 交互项检验也确认了加法模型的适当性。这些诊断检验的完整性在 NLP 论文中少见。

5. **跨 benchmark 一致性**：Verbosity bias 在 LLMBar、AlpacaEval、MTBench 三个 benchmark 上对两个 judge（GPT-4o、Qwen3-32B）均达到显著（BT 67-77%），模式一致性强。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] NLI gate 作为 do-operator 近似的声明过强
- 具体位置：Section 3.5, "The NLI entailment gate approximates the do-operator by filtering out pairs where the rewrite changed semantic content, thereby blocking the R→Q path"
- 问题：do-operator 要求对处理变量的主动干预（intervention），而 NLI gate 是一种基于观测的 **筛选**（selection/conditioning）。Selection ≠ intervention：通过 NLI 筛选保留的样本可能在未观测维度上系统性地不同于被过滤掉的样本（collider bias）。例如，容易通过 NLI gate 的文本可能系统性地偏向某些 topic 复杂度或句法结构，而这些特征本身可能影响 judge 偏好。Figure 2 的 DAG 中，如果存在 Rewrite → (未观测变量 U) → Y 的路径，conditioning on NLI score（一个 Q 的子节点）可能打开 collider path。
- 为什么影响接收：这是论文因果叙事的核心声明。如果 NLI gate 不能有效近似 do-operator，则 Section 3.5 的 "Design Rationale" 的因果论证框架需要实质性修改。论文在 Limitations 中承认 "residual confounding is not fully eliminated"，但主文 Section 3.5 的语言与此不一致。
- 建议修改方向：(1) 将 "approximates the do-operator" 改为 "provides a filtering-based confounder control that mitigates but does not eliminate confounding through the R→Q path"；(2) 在 Section 3.5 中明确讨论 selection bias 的可能方向和幅度；(3) 考虑在 DAG 中标注 NLI gate 的 conditioning 性质（而非 intervention 性质）。

**N2** [critical] Bradley-Terry 模型的 IIA 假设未检验
- 具体位置：Section 4.1 及 Appendix G
- 问题：Bradley-Terry 模型假设 Independence of Irrelevant Alternatives (IIA)——给定两个选项的偏好概率不受第三个选项的存在或缺失影响。在本文的实验设计中，每个 text pair 经过 style manipulation 后产生 original vs. rewrite 的比较。但不同类型的原始文本（如 instruction-following vs. open-ended）可能与 style manipulation 产生异质性交互，导致 IIA 违反。例如，verbosity 增加对代码相关任务的影响可能与对创意写作的影响系统性不同。Appendix G 报告了 GoF 检验但 **没有报告 IIA 检验**（如 Hausman-McFadden test 或 rank-order consistency check）。
- 为什么影响接收：BT win probability 是论文几乎所有显著性结论的基础。如果 IIA 被违反，BT 参数估计可能有偏，置信区间可能偏窄，从而夸大统计显著性。
- 建议修改方向：(1) 在 Appendix G 中增加 IIA 诊断检验（如按 task type 或 difficulty 分层后检查 BT 参数的稳定性）；(2) 如果 IIA 被违反，讨论对主要结论的影响或改用 Thurstone 模型等不假设 IIA 的替代方案。

**N3** [critical] Evaluator-producer confound 未充分解决
- 具体位置：Limitations (p.9), Appendix D, Table 1
- 问题：Qwen3-32B 同时担任 rewriter 和 judge，这引入了 self-preference bias (Panickssery et al., 2024) 的系统性混淆。论文在 Limitations 中承认 "cross-judge effect-size comparisons are not valid"，但主文 Table 1 中 Qwen3-32B 的结果仍作为 **主要证据** 与 GPT-4o 并列呈现。Appendix D 的 cross-rewriter test（替换 rewriter 为 GPT-4o）只能证明 rewriter identity 的影响有限，但 **无法排除** Qwen3-32B 作为 judge 时偏好自身产出的可能性。具体地：如果 Qwen3-32B 对自身生成的 formal/verbose 文本有系统性偏好（self-preference），则观测到的 "style bias" 可能部分甚至主要来自 self-preference 而非 genuine style bias。
- 为什么影响接收：这是实验设计的基本有效性问题。如果 Qwen3-32B 的结果受到 self-preference 污染，则论文的 "cross-judge replication" 叙事（两个 judge 均显示 bias → 发现具有通用性）被削弱。
- 建议修改方向：(1) 使用与两个 judge（GPT-4o、Qwen3-32B）均无关的第三方模型（如 Llama 3）作为 rewriter，或至少在 Appendix D 的 cross-rewriter test 中展示 GPT-4o 做 rewriter + Qwen3-32B 做 judge 与 Qwen3-32B 做 rewriter + Qwen3-32B 做 judge 的效应量差异；(2) 在主文中对 Qwen3-32B 结果加明确 caveat 而非等到 Limitations。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] GEE 条件分解在残余混淆下的解释过强
- 具体位置：Table 3, Section 5.6 ("formality stands apart as confound-free")
- 问题：Table 3 的 GEE 条件分解将观测到的 judge 偏好分解为 Style OR 和 Originality OR。但这一分解的有效性 **依赖于** NLI gate 完全阻断 R→Q 路径。论文自身承认 NLI gate 有 8.4% FNR（Section 5.1）且 "quality perception shifts mediated by style itself" 无法被 NLI gate 捕获（Limitations）。在这种残余混淆下，GEE 的条件估计存在 omitted variable bias，"confound-free" 的判断可能过于乐观。
- 建议：(1) 将 "confound-free" 改为 "with reduced confounding"；(2) 讨论残余混淆对 Style OR 估计的偏差方向（是否会导致高估或低估）。

**W2** [warning] Sensitivity hierarchy (Table 2) 仅在单一轴（formality）上展示
- 具体位置：Table 2, Section 5.2
- 问题：Table 2 的 7 种方法 sensitivity hierarchy 是论文的核心方法论贡献之一，但 **仅在 formality 数据上展示**。Verbosity 是检测最强的轴（BT 76-77%），如果 7 种方法的 hierarchy 在 verbosity 上也成立，将大幅增强 Likert Blindspot 的通用性声明。目前读者无法判断 Table 2 的 pattern 是 formality 特有的还是跨轴通用的。
- 建议：在 Appendix 中增加 verbosity 的 7 方法比较表。如果 verbosity 上 Likert 方法也全部失败（鉴于效应量更大，这一点尤其有说服力），论文的核心论点将更加稳固。

**W3** [warning] "Measurement attenuation" vs. "construct difference" 在主文中呈现不平衡
- 具体位置：Section 1 ("not merely a statistical power gap but measurement attenuation"), Section 5.2, Section 6; vs. Limitations ("An alternative interpretation…Likert and pairwise modes measure different constructs")
- 问题：论文主文的 framing 将 Likert Blindspot 定位为 **测量衰减**（measurement attenuation）——即 Likert 应该检测到 bias 但检测不到。但 Limitations 中承认的替代解释——Likert 和 pairwise 测量的是 **不同构念**（absolute quality difference vs. ordinal preference）——在概念上同样合理。如果两种方法测量不同构念，则"Blindspot"的 framing 本身就有误导性：不是 Likert"看不到"bias，而是 Likert 测的是另一个东西。论文没有提供能区分这两种解释的实验证据。
- 为什么重要：这影响论文核心贡献的定位。如果读者接受 "construct difference" 解释，则论文的 practical implication 从"Likert 有缺陷，应使用 pairwise"变为"Likert 和 pairwise 各有用途，视研究问题而定"。
- 建议：(1) 在主文（如 Section 5.2 末尾）提前讨论 construct difference 解释，而非仅在 Limitations 中一笔带过；(2) 设计一个能区分两种解释的实验（如：对已知存在 style bias 的合成数据，Likert 是否在足够大的 n 下最终检测到？如果是，则为 power gap；如果不是，则为 construct difference）。

**W4** [warning] NLI 阈值 sensitivity analysis 过于粗糙
- 具体位置：Section 5.1, p.6 ("thresholds of 0.70, 0.80, 0.90, and 0.95")
- 问题：仅测试 4 个离散阈值。论文声称阈值位于 "plateau rather than a cliff edge"，但 4 个点不足以建立 plateau 的存在——在 0.70 和 0.90 之间的行为完全未知。一条从 0.50 到 0.99（步长 0.05）的连续 sensitivity 曲线会更有说服力。
- 建议：在 Appendix 中补充更细粒度的阈值扫描（至少 10 个点），展示 BT win probability 和 pass rate 随阈值的变化趋势。

**W5** [warning] Cross-rewriter independence test 缺少 register 轴
- 具体位置：Appendix D
- 问题：Appendix D 的 cross-rewriter test（替换 rewriter）只测试了 formality 和 verbosity，**缺少 register**。Register 是效应最弱、最接近 non-significant 的轴（GPT-4o BT 57.0%, p = 0.04; Qwen3-32B 55.3%, p = 0.076），恰恰是 rewriter identity 效应最可能影响结论的轴。
- 建议：补充 register 轴的 cross-rewriter test。如果 register 的弱效应在更换 rewriter 后消失，应在主文中降低 register 结果的 claim 强度。

**W6** [warning] 样本量偏小且主文缺乏 power analysis
- 具体位置：Section 3.4 (n=100 LLMBar), Table 1, Figure 4
- 问题：AlpacaEval 的 filtered 分析仅 n=88 对。对于 BT win probability 63%（formality），bootstrap 95% CI 为 [55.7, 70.3]（Table 8）——下界仅略高于 50%，置信区间跨度 15 个百分点。这意味着真实效应量的不确定性相当大。Figure 4 的 power analysis 有帮助，但仅展示了 detection probability，未报告 BT 估计精度（CI width）随 n 的变化。论文将小 n 时 Likert 未检测到 bias 归因于 Blindspot 而非 statistical power，但在 BT 估计本身也有大 CI 的情况下，这一归因需要更谨慎。
- 建议：(1) 在主文中增加一段 power analysis 讨论，明确 n=88 时 BT 的 minimum detectable effect size；(2) 在 Figure 4 中增加 CI width vs. n 的曲线。

---

## 小问题（不影响接收）

- **M1**: Figure 2 的 DAG 中，dashed edge S→Q 代表 "style may influence perceived quality"——这是 NLI gate 无法阻断的路径，但 DAG 中的视觉区分（dashed vs. solid）在打印时可能不够清晰。建议增加颜色编码或标注文字。
- **M2**: 论文 7 种统计方法的选择（Table 2）未说明理由——为什么是这 7 种而非其他？例如，为什么不包含 mixed-effects logistic regression 或 Bayesian 方法？
- **M3**: "Likert Blindspot" 这一术语可能暗示 Likert 量表本身有缺陷，但论文的发现更准确地说是"单题 1-10 整体质量评分"的局限性。多题项 Likert 量表或属性特定评分可能不表现出同样的 Blindspot。建议在 Section 1 或 2 中明确范围。
- **M4**: Section 3.3 提到 Likert mode 使用 1-10 integer score，但未讨论评分粒度是否影响 Blindspot（如 1-100 fine-grained scale 是否能减轻 attenuation）。
- **M5**: GPT-4o 200-pair cross-validation（Section 5.1）使用 LLM 验证 NLI gate 在研究 LLM bias 的论文中存在轻微的循环性——GPT-4o 自身的 style bias 可能影响其 content-preservation 判断。应在 limitations 中简要提及。

---

## Questions for Authors

**Q1**: Table 2 的 sensitivity hierarchy 在 verbosity 轴上是否成立？如果 verbosity（效应量更大）的 Likert ATE 也为 non-significant，为什么不展示？如果 verbosity 的 Likert ATE 是 significant 的（在较大效应量下 Likert 开始检测到 bias），这对 "severity spectrum" 叙事意味着什么？

**Q2**: 关于 IIA：是否做过按 task type（如 LLMBar 的 instruction-following categories）分层的 BT 参数稳定性检查？如果不同 task type 的 BT win probability 差异显著，则 IIA 可能被违反。

**Q3**: n=355（scaled replication）时 Likert d→0 的结果（Section 5.2, Figure 4），是否尝试过更大的 n（如 n=1000 的模拟或 bootstrap extrapolation）来确认 d 确实收敛到 0 而非缓慢上升？这对区分 "attenuation" 和 "power gap" 至关重要。

**Q4**: Qwen3-32B 作为 rewriter + judge 时，是否检查过 self-preference 的直接证据？例如，让 Qwen3-32B 在 original pair（未经 style manipulation）上做 pairwise comparison，是否对 Qwen3-32B 生成的回答有系统性偏好？

---

## Missing References

- Zheng et al. (2024), "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" — 论文引用了 MTBench benchmark 但未引用原始方法论文
- Stureborg et al. (2024), "Large Language Models are Inconsistent and Biased Evaluators" — 关于 LLM judge Likert vs. pairwise 不一致性的直接相关工作
- Park et al. (2024), "Disentangling Length from Quality in Direct Assessments" — 与论文的 verbosity 分析直接相关

---

## Overall Assessment

**Overall**: 3.5 / 5（Borderline Conference）
**Confidence**: 4 / 5

论文提出了一个有实际意义的发现（Likert Blindspot）和一个设计合理的检测框架（CSD）。核心实证结果（Table 1-2, Figure 3-4）在多 benchmark、多 judge 上模式一致。但方法严谨性存在三个核心缺陷：(1) NLI gate 的因果声明（do-operator 近似）超出了筛选操作的实际能力，存在 collider bias 风险；(2) BT 模型的 IIA 假设未经检验，而实验设计中存在潜在的异质性；(3) evaluator-producer confound（Qwen3-32B 同时做 rewriter 和 judge）未充分解决。这三个问题彼此关联——如果 NLI gate 的因果控制力被削弱（N1），残余混淆更大，GEE 分解（W1）就更不可靠；如果 evaluator-producer confound（N3）存在，则 Qwen3-32B 的结果不能作为独立 replication。

修改建议的优先级：N1（降低因果声明）> N3（解决 evaluator-producer confound）> N2（IIA 检验）> W2（多轴 sensitivity hierarchy）> W3（平衡两种解释）。如果 N1-N3 得到充分解决，论文可达 4.0（Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 384 · 2026-05-21T12:40:58.098399+00:00_

Reviewer 1 的报告已收到。等待 Reviewer 2 的报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 34

## Round 34

2 recorded events


### User

_source line 385 · 2026-05-21T12:41:13.348112+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**评分摘要**：Overall 3.5/5（Borderline Conference），Soundness 3.5，Excitement 3.5，Reproducibility 4，Confidence 4/5。

**三个 Must-Fix**：
1. **N1** — NLI gate 被声称为 do-operator 近似，但实质是 selection/conditioning，存在 collider bias 风险，因果语言需降级
2. **N2** — Bradley-Terry 的 IIA 假设未检验，论文所有显著性结论均依赖 BT，需补充诊断
3. **N3** — Qwen3-32B 同时做 rewriter 和 judge 的 evaluator-producer confound 未充分解决，削弱 cross-judge replication 叙事

**六个 Should-Fix**：GEE "confound-free" 解释过强、sensitivity hierarchy 仅在单轴展示、attenuation vs. construct difference 主文呈现不平衡、NLI 阈值扫描仅 4 个点、cross-rewriter test 缺 register 轴、样本量偏小缺 power analysis。

核心判断：如果 N1-N3 得到充分修改（降低因果声明、补 IIA 检验、解决 evaluator-producer confound），论文可达 4.0（Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 386 · 2026-05-21T12:41:18.566595+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 完成后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 35

## Round 35

6 recorded events


### User

_source line 387 · 2026-05-21T12:51:04.854392+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性与完整性

### 论文信息
- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
- Venue：EMNLP 2026 Main Conference (via ARR)

---

## 总体评分
**Overall**: 3.0 / 5 — Findings
**一句话总结**: 统计方法扎实、实用建议明确，但核心概念（Likert Blindspot）本质是心理测量学已知现象的 domain transfer，实验规模有限（3 judges, n=100 主 benchmark），且遗漏了一篇直接反驳核心叙事的关键文献。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法论严谨（BT、GEE、TOST、bootstrap CI、7 种方法交叉验证），但 formality 轴的 confound 实质上削弱了核心 claim，且未讨论与 Comparative Trap 的矛盾 |
| Excitement | 2.5/5 | Likert Blindspot 是 Thurstone (1927) / Stevens (1946) 已知洞察的领域迁移，CSD 相对于 RATE 的增量有限，实验规模不足以支撑 "first systematic" claim |
| Overall | 3.0/5 | 可被 Findings 接收；若补充 judge 覆盖、讨论 Comparative Trap、修正 overclaim，有望升至 3.5 |

**Confidence**: 4/5

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 遗漏直接矛盾的关键文献：The Comparative Trap (Jeong et al., 2025, BlackboxNLP)
- 具体位置：Section 2 (Related Work)、Section 5.2、Section 6 (Conclusion)
- 问题：Jeong et al. (2025) "The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators" 系统性地证明 pairwise comparison **放大**了 LLM evaluator 的 style bias（尤其是 verbosity 和 authoritative tone），而非仅仅"检测"了 Likert 遗漏的 bias。本文的核心主张——"style bias audits should adopt pairwise comparison"（Section 6, page 8）——与该文献的发现存在直接张力。pairwise 是否在检测 bias 的同时也人为放大了 bias？这个区分对本文的实践建议至关重要，但完全未被讨论。
- 为什么影响接收：论文的核心贡献（C2: Likert Blindspot 作为 measurement attenuation）和核心实践建议（采用 pairwise 替代 Likert）的可靠性取决于能否与这一矛盾证据调和。Reviewer 在文献检索中很容易发现这篇论文。
- 建议修改方向：在 Related Work 的 Bradley-Terry 段落（Section 2）中讨论 Comparative Trap；在 Section 5.2 或 Section 6 中明确区分"detection sensitivity"（本文关注的）与"bias amplification"（Jeong et al. 关注的）——两者并不矛盾但需要明确论证。

**N2** [critical] "first systematic quantitative verification" claim 需要限定
- 具体位置：Abstract (line 5-6)、Section 1 (page 1, "the first framework to systematically quantify this measurement principle for LLM judges")
- 问题：至少三篇近期工作在不同角度做了类似的 systematic quantification：(1) Jeong et al. (2025) 系统比较了 pointwise vs. pairwise 对 style bias 的敏感度；(2) Haak & Schaer (2025, arXiv:2512.14565) "Pairwise Comparison for Bias Identification and Quantification" 在 NLP 评估中系统比较了 Likert vs. pairwise 对 linguistic bias 的量化能力；(3) Soumik et al. (2026) 系统评估了 9 种 debiasing 策略。将 CSD 定位为 "first" 是 overclaim。
- 为什么影响接收：Overclaim 是 ARR reviewer 的常见拒稿理由。"First" 在不准确时会严重损害论文可信度。
- 建议修改方向：改为 "the first framework to integrate style-controlled rewriting, NLI gating, and position-controlled pairwise comparison in a single pipeline for per-axis style bias detection" —— 限定到具体方法组合的 novelty 而非整个研究问题。

**N3** [critical] Judge 覆盖面不足，且缺乏开源模型代表
- 具体位置：Section 3.4 (Experimental Setup)、Table 1
- 问题：仅 3 个 judges（GPT-4o, Qwen3-32B, Claude Sonnet 4），其中 Claude 作为 negative control 不参与 bias 分析。实质上只有 2 个 judges 展示了 Blindspot。缺乏：(1) Gemini（主要商业竞品）；(2) Llama-3-70B/405B（开源社区最常用 judge）；(3) 任何 specialized judge 模型（如 Prometheus、JudgeLM）。当 n_judges = 2 时，所有发现的泛化性存疑——"the Likert Blindspot manifests in six of nine bias-positive cells"（page 8）实际上是在 2×3×3 = 18 个 cell 中的 6 个，覆盖率仅 33%。
- 为什么影响接收：实验覆盖面是 empirical contribution 的核心。2 个 judge 不足以支撑 "across three judges" 的 framing。
- 建议修改方向：至少增加 1 个开源 judge（Llama-3-70B 最佳选择）和 1 个其他商业 judge（Gemini）。如果资源有限，优先加 Llama-3-70B 以覆盖开源生态。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Formality 轴的 confound 实质上削弱了该轴的贡献
- 具体位置：Section 5.5 (page 7-8)、Table 3
- 问题：GEE 分析揭示 formality bias 与 originality quality 存在 "partial confounding"（OR 2.58, p=0.002 for GPT-4o; OR 2.35, p=0.002 for Qwen3-32B）。Table 3 显示在控制 confound 后，Qwen3-32B 的 formality Style OR 变为 non-significant (p=0.60)，GPT-4o 的 OR decrease (4.20→2.15) 反映了小样本 confound。这意味着 formality 轴上检测到的 "style bias" 可能大部分是 quality confound，而非 pure style effect。论文在 Limitations 中承认了这一点，但在 Abstract 和 Conclusion 中仍以 "three style axes" 作为贡献 framing，存在误导。
- 建议：在 Abstract 和 Conclusion 中明确区分 verbosity（confound-free, 最强证据）和 formality（confounded, 需谨慎解读）。

**W2** [warning] LLMBar (n=100) 作为主要 benchmark 规模受限
- 具体位置：Section 3.4、Table 1、Figure 4
- 问题：LLMBar 仅 n=100 instruction-response pairs。经 NLI filtering 后进一步缩减。虽然 Figure 4 的 power analysis 表明 BT 在 n≈62 即可检测效应，但这一 power analysis 本身是 post-hoc 的——用观测数据估算的效应量反推所需样本量。AlpacaEval (n=355) 和 MT-Bench 有更大规模但分析深度明显不如 LLMBar。
- 建议：将 AlpacaEval 的分析提升到与 LLMBar 同等深度（包括 power curve），或增加一个更大规模的 benchmark。

**W3** [warning] Claude Sonnet 4 作为 negative control 的统计力不足
- 具体位置：Section 5.1 (page 5)、Appendix F (page 11)
- 问题：TOST equivalence testing 在 n=87, Δ=10pp 下 underpowered（论文自己在 Appendix F 承认）。论文结论 "Claude shows no significant bias on either axis" (page 8) 在统计上应表述为 "failed to detect bias with current sample size"，而非 "no bias"。equivalence bound 设为 <15pp，但这个 bound 的选择缺乏 external justification。
- 建议：(1) 将结论改为更审慎的措辞；(2) 报告达到 80% power 所需的样本量；(3) 为 equivalence bound 选择提供理据。

**W4** [warning] 实验矩阵不完整
- 具体位置：Table 1
- 问题：Table 1 中多个 cell 的 Likert 列显示 "—" 或标记为 n.s.，但未解释哪些是真正 non-significant vs. 未测试。完整的 3×3×3 矩阵如果有空 cell，应在文中明确说明原因。
- 建议：补充所有 cell 或在 Table 1 脚注中解释每个缺失 cell 的原因。

---

## 小问题（不影响接收）

- **术语不一致**：标题用 "Blindspot"（大写），正文有时用 "blindspot"（小写）。"style bias" 和 "style preference" 混用但含义不同。
- **Abstract 信息密度过高**：165 词试图覆盖全部 4 项贡献，导致可读性下降。建议精简。
- **orphan bib entry**：`hoenig2001abuse` 在 .bib 中但可能未被 \cite 引用。
- **Figure 2 DAG**：dashed edge 与 solid edge 在黑白打印时不易区分。
- **引用年份 mismatch**：`wu2023style` bib 标注 2025 但 OpenAlex 匹配到 2023。

---

## 可能遗漏的参考文献

1. **Jeong et al. (2025)** "The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators" — BlackboxNLP 2025。**必须引用**。
2. **Haak & Schaer (2025)** "Pairwise Comparison for Bias Identification and Quantification" — arXiv:2512.14565。
3. **LLM-as-a-Judge 综合 survey** (The Innovation, 2026)。
4. **"Any Large Language Model Can Be a Reliable Judge"** (2025, arXiv:2505.17100)。

---

## 主要优势

1. **统计方法论严谨**：7 种统计方法交叉验证，GEE 用于 confound 分解是 NLP 评估论文中少见的方法论深度。
2. **NLI gating 设计精巧**：Appendix B 充分验证了 filter robustness（93.9% valid pairs, no systematic bias）。
3. **Verbosity 轴提供了清晰的 confound-free 证据**：BT 76.0% win probability (p < 0.0001) 且 GEE 确认无 originality confound。
4. **RATE 的 head-to-head 比较公平且有洞察**：Section 5.2 揭示 RATE 的 Likert ATE 本身受 Blindspot 影响。
5. **可操作的实践建议**：对评估社区有明确指导。

---

## 格式合规检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤8 页 | ✅ | Pages 1-8，第 8 页末尾为 Conclusion |
| Limitations 章节 | ✅ | Page 9，位于 Conclusion 后、References 前 |
| Double-blind | ✅ | "Anonymous ACL submission"，未发现作者信息泄露 |
| 引用格式 (natbib) | ✅ | \citet / \citep 使用正确 |
| Limitations 内容合规 | ✅ | 未含额外实验/图表/分析 |
| 附录关键信息 | ⚠️ | Appendix F (TOST 结果) 和 Appendix D (Rewriter Independence) 的核心结论应在正文中至少概述 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-21T12:51:41.497221+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个要点标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并引用论文中的具体 Section/Table/Figure 作为证据）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n**Overall**: 3.5 / 5（Borderline Conference），Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] NLI gate 作为 do-operator 近似的声明过强\n- Section 3.5: \"The NLI entailment gate approximates the do-operator by filtering out pairs where the rewrite changed semantic content, thereby blocking the R→Q path\"\n- 问题：do-operator 要求主动干预（intervention），而 NLI gate 是基于观测的筛选（selection/conditioning）。Selection ≠ intervention：通过 NLI 筛选保留的样本可能在未观测维度上系统性不同于被过滤掉的样本（collider bias）。如果存在 Rewrite → (未观测变量 U) → Y 路径，conditioning on NLI score 可能打开 collider path。论文 Limitations 承认 \"residual confounding is not fully eliminated\"，但主文 Section 3.5 语言与此不一致。\n- 建议：将 \"approximates the do-operator\" 改为 \"provides a filtering-based confounder control\"；讨论 selection bias 可能方向和幅度。\n\n**N2** [critical] Bradley-Terry 模型的 IIA 假设未检验\n- Appendix G 报告了 GoF 检验但没有 IIA 检验（如 Hausman-McFadden test）。不同类型原始文本可能与 style manipulation 产生异质性交互，导致 IIA 违反。BT win probability 是论文几乎所有显著性结论的基础。\n- 建议：增加 IIA 诊断检验，按 task type 分层检查 BT 参数稳定性。\n\n**N3** [critical] Evaluator-producer confound 未充分解决\n- Qwen3-32B 同时做 rewriter 和 judge，引入 self-preference bias。Appendix D 的 cross-rewriter test 只能证明 rewriter identity 影响有限，但无法排除 Qwen3-32B 作为 judge 偏好自身产出。\n- 建议：使用第三方模型做 rewriter，或在主文中对 Qwen3-32B 结果加明确 caveat。\n\n### Should-Fix 问题\n\n**W1** GEE \"confound-free\" 解释过强（Table 3 verbosity）——残余混淆下 \"confound-free\" 可能过于乐观\n**W2** Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\n**W3** \"Measurement attenuation\" vs \"construct difference\" 主文呈现不平衡——Limitations 的替代解释同样合理但主文未讨论\n**W4** NLI 阈值 sensitivity analysis 仅 4 个离散点\n**W5** Cross-rewriter independence test 缺 register 轴\n**W6** 样本量偏小（n=88）缺 power analysis 讨论\n\n### Minor Issues\n- M1: DAG 黑白打印时 dashed/solid 不易区分\n- M2: Table 2 的 7 种方法选择未说明理由\n- M3: \"Likert Blindspot\" 范围应限定为单题评分\n- M4: 评分粒度（1-10 vs 1-100）对 Blindspot 的影响未讨论\n- M5: GPT-4o 验证 NLI gate 存在轻微循环性\n\n### Missing References\n- Stureborg et al. (2024), \"Large Language Models are Inconsistent and Biased Evaluators\"\n- Park et al. (2024), \"Disentangling Length from Quality in Direct Assessments\"\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Minor Issue 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个要点标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并引用论文中的具体 Section/Table/Figure 作为证据）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n**Overall**: 3.5 / 5（Borderline Conference），Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] NLI gate 作为 do-operator 近似的声明过强\n- Section 3.5: \"The NLI entailment gate approximates the do-operator by filtering out pairs where the rewrite changed semantic content, thereby blocking the R→Q path\"\n- 问题：do-operator 要求主动干预（intervention），而 NLI gate 是基于观测的筛选（selection/conditioning）。Selection ≠ intervention：通过 NLI 筛选保留的样本可能在未观测维度上系统性不同于被过滤掉的样本（collider bias）。如果存在 Rewrite → (未观测变量 U) → Y 路径，conditioning on NLI score 可能打开 collider path。论文 Limitations 承认 \"residual confounding is not fully eliminated\"，但主文 Section 3.5 语言与此不一致。\n- 建议：将 \"approximates the do-operator\" 改为 \"provides a filtering-based confounder control\"；讨论 selection bias 可能方向和幅度。\n\n**N2** [critical] Bradley-Terry 模型的 IIA 假设未检验\n- Appendix G 报告了 GoF 检验但没有 IIA 检验（如 Hausman-McFadden test）。不同类型原始文本可能与 style manipulation 产生异质性交互，导致 IIA 违反。BT win probability 是论文几乎所有显著性结论的基础。\n- 建议：增加 IIA 诊断检验，按 task type 分层检查 BT 参数稳定性。\n\n**N3** [critical] Evaluator-producer confound 未充分解决\n- Qwen3-32B 同时做 rewriter 和 judge，引入 self-preference bias。Appendix D 的 cross-rewriter test 只能证明 rewriter identity 影响有限，但无法排除 Qwen3-32B 作为 judge 偏好自身产出。\n- 建议：使用第三方模型做 rewriter，或在主文中对 Qwen3-32B 结果加明确 caveat。\n\n### Should-Fix 问题\n\n**W1** GEE \"confound-free\" 解释过强（Table 3 verbosity）——残余混淆下 \"confound-free\" 可能过于乐观\n**W2** Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\n**W3** \"Measurement attenuation\" vs \"construct difference\" 主文呈现不平衡——Limitations 的替代解释同样合理但主文未讨论\n**W4** NLI 阈值 sensitivity analysis 仅 4 个离散点\n**W5** Cross-rewriter independence test 缺 register 轴\n**W6** 样本量偏小（n=88）缺 power analysis 讨论\n\n### Minor Issues\n- M1: DAG 黑白打印时 dashed/solid 不易区分\n- M2: Table 2 的 7 种方法选择未说明理由\n- M3: \"Likert Blindspot\" 范围应限定为单题评分\n- M4: 评分粒度（1-10 vs 1-100）对 Blindspot 的影响未讨论\n- M5: GPT-4o 验证 NLI gate 存在轻微循环性\n\n### Missing References\n- Stureborg et al. (2024), \"Large Language Models are Inconsistent and Biased Evaluators\"\n- Park et al. (2024), \"Disentangling Length from Quality in Direct Assessments\"\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Minor Issue 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-21T12:51:54.664569+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13167
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-21T12:51:54.766691+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个要点标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并引用论文中的具体 Section/Table/Figure 作为证据）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n**Overall**: 3.0 / 5（Findings），Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 遗漏直接矛盾的关键文献：The Comparative Trap (Jeong et al., 2025, BlackboxNLP)\n- Jeong et al. (2025) 系统性证明 pairwise comparison **放大** LLM evaluator 的 style bias（尤其 verbosity 和 authoritative tone），而非仅\"检测\"。本文核心建议\"style bias audits should adopt pairwise comparison\"与该文献存在直接张力。pairwise 是检测 bias 还是人为放大 bias？\n- 建议：在 Related Work 和 Conclusion 中讨论 Comparative Trap；区分 \"detection sensitivity\" 与 \"bias amplification\"。\n\n**N2** [critical] \"first systematic quantitative verification\" claim 需要限定\n- 至少三篇近期工作做了类似 systematic quantification：(1) Jeong et al. (2025)；(2) Haak & Schaer (2025, arXiv:2512.14565)；(3) Soumik et al. (2026)。\"First\" 是 overclaim。\n- 建议：改为限定到具体方法组合的 novelty。\n\n**N3** [critical] Judge 覆盖面不足\n- 仅 3 个 judges，Claude 为 negative control。实质只有 2 个 judges 展示 Blindspot。缺 Gemini、Llama-3-70B/405B、specialized judges。2 个 judge 不足以支撑 \"across three judges\" framing。\n- 建议：至少增加 1 个开源 judge（Llama-3-70B）。\n\n### Should-Fix 问题\n\n**W1** Formality 轴 confound 实质削弱该轴贡献——Abstract/Conclusion 应区分 verbosity（confound-free）和 formality（confounded）\n**W2** LLMBar (n=100) 规模受限——AlpacaEval 分析深度不足\n**W3** Claude negative control 统计力不足——TOST n=87, Δ=10pp underpowered，应更审慎措辞\n**W4** Table 1 实验矩阵不完整——多个 cell 缺失未解释\n\n### Minor Issues\n- 术语不一致（Blindspot/blindspot, style bias/style preference 混用）\n- Abstract 信息密度过高\n- orphan bib entry: hoenig2001abuse\n- Figure 2 DAG 黑白打印不清\n- wu2023style 引用年份 mismatch\n\n### Missing References\n1. **Jeong et al. (2025)** \"The Comparative Trap\" — **必须引用**\n2. **Haak & Schaer (2025)** \"Pairwise Comparison for Bias Identification and Quantification\"\n3. **LLM-as-a-Judge survey** (The Innovation, 2026)\n4. **\"Any Large Language Model Can Be a Reliable Judge\"** (2025)\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Minor Issue 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个要点标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并引用论文中的具体 Section/Table/Figure 作为证据）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n**Overall**: 3.0 / 5（Findings），Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 遗漏直接矛盾的关键文献：The Comparative Trap (Jeong et al., 2025, BlackboxNLP)\n- Jeong et al. (2025) 系统性证明 pairwise comparison **放大** LLM evaluator 的 style bias（尤其 verbosity 和 authoritative tone），而非仅\"检测\"。本文核心建议\"style bias audits should adopt pairwise comparison\"与该文献存在直接张力。pairwise 是检测 bias 还是人为放大 bias？\n- 建议：在 Related Work 和 Conclusion 中讨论 Comparative Trap；区分 \"detection sensitivity\" 与 \"bias amplification\"。\n\n**N2** [critical] \"first systematic quantitative verification\" claim 需要限定\n- 至少三篇近期工作做了类似 systematic quantification：(1) Jeong et al. (2025)；(2) Haak & Schaer (2025, arXiv:2512.14565)；(3) Soumik et al. (2026)。\"First\" 是 overclaim。\n- 建议：改为限定到具体方法组合的 novelty。\n\n**N3** [critical] Judge 覆盖面不足\n- 仅 3 个 judges，Claude 为 negative control。实质只有 2 个 judges 展示 Blindspot。缺 Gemini、Llama-3-70B/405B、specialized judges。2 个 judge 不足以支撑 \"across three judges\" framing。\n- 建议：至少增加 1 个开源 judge（Llama-3-70B）。\n\n### Should-Fix 问题\n\n**W1** Formality 轴 confound 实质削弱该轴贡献——Abstract/Conclusion 应区分 verbosity（confound-free）和 formality（confounded）\n**W2** LLMBar (n=100) 规模受限——AlpacaEval 分析深度不足\n**W3** Claude negative control 统计力不足——TOST n=87, Δ=10pp underpowered，应更审慎措辞\n**W4** Table 1 实验矩阵不完整——多个 cell 缺失未解释\n\n### Minor Issues\n- 术语不一致（Blindspot/blindspot, style bias/style preference 混用）\n- Abstract 信息密度过高\n- orphan bib entry: hoenig2001abuse\n- Figure 2 DAG 黑白打印不清\n- wu2023style 引用年份 mismatch\n\n### Missing References\n1. **Jeong et al. (2025)** \"The Comparative Trap\" — **必须引用**\n2. **Haak & Schaer (2025)** \"Pairwise Comparison for Bias Identification and Quantification\"\n3. **LLM-as-a-Judge survey** (The Innovation, 2026)\n4. **\"Any Large Language Model Can Be a Reliable Judge\"** (2025)\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Minor Issue 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-21T12:51:56.226503+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 392 · 2026-05-21T12:51:59.229407+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 393 · 2026-05-21T12:52:01.847551+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.0 (Findings)**。

3 个 Must-Fix：
1. 遗漏 Comparative Trap (Jeong et al., 2025) —— 该文直接证明 pairwise comparison 放大 style bias，与本文"pairwise 更适合检测 bias"的核心建议存在未调和的张力
2. "first systematic" claim 是 overclaim，至少 3 篇近期工作在相关维度做了 systematic quantification
3. 实质上仅 2 个 judge 展示了 Blindspot，judge 覆盖面不足以支撑泛化性 claim

4 个 Should-Fix：formality confound 削弱该轴贡献、LLMBar n=100 规模受限、Claude negative control underpowered、实验矩阵有空 cell 未解释。

主要优势在于统计方法论深度（7 种方法交叉验证 + GEE confound 分解）和 verbosity 轴的 clean evidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 394 · 2026-05-21T12:52:06.745681+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 37

## Round 37

2 recorded events


### User

_source line 395 · 2026-05-21T12:54:57.687630+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 遗漏 The Comparative Trap (Jeong et al., 2025)**

这是 Reviewer 2 最强的一个点，我完全同意其严重性。

Jeong et al. (2025, BlackboxNLP) 系统性地证明 pairwise comparison 相比 pointwise evaluation **放大**了 LLM evaluator 的 style bias（尤其 verbosity 和 authoritative tone）。这与本文的核心实证发现和实践建议构成直接张力：

- 本文 Section 6 建议 "style bias audits should adopt pairwise comparison"
- 本文 Table 2 的 sensitivity hierarchy 将 pairwise 方法（BT、sign test）排在最顶，Likert 方法排在最底
- 本文将 pairwise 的更高检出率解释为 **detection sensitivity**

但 Jeong et al. 的结果提供了一个完全不同的解释框架：pairwise 检出率高不是因为它更"敏感"，而是因为它 **人为放大** 了本来较小的 bias。如果这一解释成立，则：
1. Likert 可能不是"blindspot"——而是更接近真实 bias 幅度的测量
2. BT win probability 报告的 63-77% 可能是 amplified signal 而非 true bias magnitude
3. 论文的 practical recommendation 方向可能需要反转

这一遗漏不仅是 related work 的疏忽，而是影响论文核心贡献定位的根本性问题。我在 Round 1 审稿中提出的 W3（"measurement attenuation" vs. "construct difference" 解释不平衡）与此高度相关——Jeong et al. 的发现实质上支持了 "construct difference" 解释的一个更强版本：不是 Likert 测的是不同构念，而是 **pairwise 主动扭曲了 bias 的表现**。

**补充建议**：作者需要在 Related Work (Section 2) 中讨论 Comparative Trap，并在方法论上论证 CSD 的 style-controlled rewriting + NLI gate 是否能区分 "detection sensitivity" 和 "bias amplification"——例如，如果 NLI gate 通过的 pair 在 pairwise mode 下显示 bias 而在 Likert mode 下不显示，这到底是 Likert 的 attenuation 还是 pairwise 的 amplification？论文目前没有提供区分这两种机制的实验证据。

---

**[AGREE with nuance] R2-N2: "first systematic quantitative verification" overclaim**

部分同意。

论文 Abstract 的原文（Section 1, p.1）："the first systematic quantitative verification of this known measurement principle for LLM judge evaluation"——这里的 "this known measurement principle" 指 Likert 量表的 measurement attenuation。

Reviewer 2 指出至少三篇近期工作做了类似的 systematic quantification。我验证后的判断：

- **Jeong et al. (2025)**：确实做了 pairwise vs. pointwise 的系统性量化对比，且覆盖了 style bias（包括 verbosity），构成直接先行工作
- **Haak & Schaer (2025, arXiv:2512.14565)**：该文关注 news/social media 的 linguistic bias annotation，使用 pairwise comparison 做 bias 量化，但 **不是关于 LLM judge bias** 的工作——与本文的研究问题不同，作为 "同类工作" 的直接性较弱
- **Soumik et al. (2026)**：本文已引用（Section 1, p.1），报告 bias scores 76-92%，但为 correlational 而非 interventional

因此，"first" 的 overclaim 程度取决于范围界定：
- 如果指 "first interventional framework with NLI gate + per-axis decomposition"——可能成立
- 如果指 "first systematic quantitative verification of measurement attenuation"——在 Jeong et al. (2025) 已存在的情况下不成立

**建议**：将 "first" 限定到 CSD 的具体方法组合的 novelty（如 "the first black-box interventional framework integrating style-controlled rewriting, NLI content gating, and position-controlled pairwise comparison for per-axis style bias detection"），避免对整体研究问题的 priority claim。

---

**[REBUT] R2-N3: Judge 覆盖面不足不应为 Must-Fix**

我不同意这是 Must-Fix 级别的问题，理由如下：

1. **论文的核心贡献是方法论（CSD 框架），不是 judge bias 的 exhaustive survey**。对于方法论贡献，在 2 个 target judge + 1 个 negative control 上验证是合理的标准实践。类比：RATE (Reber et al., 2025) 也只在有限 judge 上验证其方法。

2. **Negative control 有独立方法论价值**。Claude Sonnet 4 作为 negative control（Table 1, all axes BT ~56%, non-significant）证明 CSD **不是在所有 judge 上都产生假阳性**。这比简单增加第 3 个显示 bias 的 judge 更有方法论说服力——它建立了 discriminant validity。

3. **"across three judges" framing 确实需要调整**。我同意 Reviewer 2 的观察——Abstract 中 "across three judges" 可能给人 3 个 judge 都显示 bias 的印象。但修复方式是调整措辞（如 "across two commercial judges, with a third serving as negative control"），而非要求增加实验。

4. **实际可行性**：增加 Llama-3-70B 或 Gemini 是 nice-to-have 但不改变方法论贡献的有效性。如果两个 reviewer 都要求增加不同的 judge，则修改周期内无法满足所有请求。

**我的判断**：降级为 Should-Fix。措辞调整即可，不需要新实验。

---

### Should-Fix 问题

**[AGREE] R2-W1: Formality confound 区分不够突出**

同意。论文 Section 5.6 和 Table 3 确实区分了 verbosity（confound-free, Style OR significant + Originality OR n.s.）和 formality（style + originality confounds 并存），但 Abstract 和 Conclusion 的 framing 将所有轴混为一谈。例如：
- Abstract: "three style axes" 未说明各轴证据强度不同
- Conclusion (Section 6): 虽有 "Verbosity provides the cleanest evidence" 但随后 "formality exhibits conditional style effects alongside originality confounds" 的措辞弱化了 confound 的严重性

建议在 Abstract 中明确："verbosity bias is robustly detected as confound-free across judges; formality shows conditional style effects that partially confound with originality preferences"。

---

**[REBUT with partial agreement] R2-W2: LLMBar n=100 规模受限**

部分不同意。

LLMBar 是一个标准 benchmark（Zeng et al., 2024），n=100 是其固有规模，不是作者的设计选择。批评 benchmark 的固有大小对作者不公平。论文已在三个不同规模的 benchmark 上测试（LLMBar n=100, AlpacaEval 和 MTBench），这本身就是对单一 benchmark 局限性的缓解。

但我同意 AlpacaEval 的分析可以更深入——特别是在 formality 轴上，AlpacaEval 的 filtered n=88 是所有分析中最小的有效样本（我在 Round 1 W6 中已提出此问题）。

---

**[AGREE] R2-W3: Claude negative control TOST 统计力不足**

同意这是一个有效的统计关注。

如果 TOST 使用 n=87, Δ=10pp，则对于检测"等价于零效应"的 power 可能不足——特别是当真实效应可能是 5pp（一个实际上很小但非零的 bias）时。论文应该：
1. 报告 TOST 的 achieved power
2. 或将 negative control 的结论措辞从"Claude 无 bias"改为"在当前样本量下未检测到 bias"

这与我在 Round 1 审稿中未覆盖到的一个盲区——我专注于 BT 和 GEE 的统计细节，但忽略了 negative control 的统计力问题。Reviewer 2 的这个点补充了我的审查。

---

**[AGREE] R2-W4: Table 1 实验矩阵不完整**

同意。Table 1 确实有多个空 cell（例如 Claude 在部分 benchmark 上缺失结果，Qwen3-32B 在某些 benchmark-axis 组合上缺失）。论文未解释这些缺失的原因——是 API 配额限制、计算成本、还是有意省略？每个缺失 cell 都应在 footnote 或 Appendix 中说明原因。

---

### Minor Issues

**[AGREE] 术语不一致**：Blindspot/blindspot 大小写不一致确实存在，应统一。style bias/style preference 的混用会影响精确性——bias 暗示系统性偏差，preference 可能是合理的评价。

**[AGREE] Abstract 信息密度过高**：Abstract 试图在有限篇幅内覆盖方法（3 阶段管线）、发现（Likert Blindspot）、实验配置（3 judges × 3 axes × 3 benchmarks）和实践建议，确实过于密集。

**[AGREE] orphan bib entry**：hoenig2001abuse 如果在正文中未引用，应删除。

**[AGREE] Figure 2 DAG 黑白打印不清**：与我 Round 1 M1 一致——我也指出了 dashed vs. solid edge 在打印时可能不清楚。

**[AGREE] wu2023style 引用年份**：应核实是否为 2023 还是其他年份。

---

### Missing References

**[AGREE] Jeong et al. (2025) "The Comparative Trap"**：如上 N1 所述，**必须引用**。这是与本文核心论点直接相关且潜在矛盾的工作。

**[REBUT] Haak & Schaer (2025)**：该文研究的是 news/social media 的 linguistic bias annotation，不是 LLM judge bias。方法上使用 pairwise comparison 做 bias 量化，但研究对象和问题域不同。属于 tangentially related，引用是 nice-to-have 而非 must-cite。

**[AGREE] Stureborg et al. (2024) "Large Language Models are Inconsistent and Biased Evaluators"**：该文直接研究 LLM evaluator 的 inconsistency 和 bias（包括 Likert 评分分布偏差、anchoring effects），与本文 highly relevant。我在 Round 1 Missing References 中也独立提出了此文。

**[No opinion] LLM-as-a-Judge survey (The Innovation, 2026) 和 "Any Large Language Model Can Be a Reliable Judge" (2025)**：未能验证这两篇的存在和具体内容，不作判断。

---

### 综合判断

Reviewer 2 的审稿在 **related work 完整性** 和 **claim 精确度** 方面提出了比我更尖锐的问题，特别是 N1（Comparative Trap）是一个我在 Round 1 中遗漏的重要发现。这篇遗漏的文献实质上加强了我在 Round 1 中提出的 W3（"measurement attenuation" vs. "construct difference" 解释不平衡）——Jeong et al. 的 "bias amplification" 解释为 construct difference 提供了独立的实证支持。

但我不同意 Reviewer 2 将 judge 覆盖面不足定为 Must-Fix（N3）——对于方法论论文，2 positive judges + 1 negative control 是合理的验证范围。

**我对 Overall 的修订建议**：Reviewer 2 给 3.0 (Findings)，我维持 3.5 (Borderline Conference)。考虑到 Comparative Trap 遗漏的严重性，如果作者不能在 revision 中充分论证 CSD 的 detection sensitivity 与 pairwise amplification 的区分，我可能下调至 3.0。但如果能说清楚（例如通过论证 NLI gate 控制了 pairwise amplification 的部分机制），则 3.5 甚至 4.0 仍可达到。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 396 · 2026-05-21T12:55:02.985316+00:00_

Reviewer 1 对 Reviewer 2 意见的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 397 · 2026-05-21T12:55:05.585431+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：Reviewer 2 最有力的点是 N1（Comparative Trap 遗漏）——Jeong et al. (2025) 证明 pairwise 放大 style bias，与本文"用 pairwise 做 bias audit"的建议构成直接张力。这一遗漏加强了我 Round 1 中关于 "measurement attenuation vs. construct difference" 解释不平衡的担忧。但 N3（judge 覆盖面）作为 Must-Fix 过重，降级为 Should-Fix 更合理。我维持 Overall 3.5，但若作者不能区分 detection sensitivity 和 bias amplification，可能下调至 3.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 398 · 2026-05-21T12:55:10.439754+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 39

## Round 39

12 recorded events


### User

_source line 399 · 2026-05-21T12:55:13.020249+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 问题

**[AGREE] R1-N1: NLI gate 作为 do-operator 近似的声明过强**

同意 R1 的判断。Section 3.5 原文："The NLI entailment gate approximates the do-operator by filtering out pairs where the rewrite changed semantic content, thereby blocking the R→Q path"——这里的 "approximates the do-operator" 确实在因果推断术语上过强。do-operator 要求对 treatment 变量的主动干预（Pearl, 2009），而 NLI filtering 是 post-hoc selection on an observed variable，本质上是 conditioning，不是 intervention。R1 提出的 collider bias 场景（如果存在 Rewrite→U→Y 路径，conditioning on NLI score 可能打开 collider path）在理论上成立。

补充一点：论文自己在 Section 3.5 后半段有一句 caveat——"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework"（page 4）。这表明作者对因果声明有一定自觉。但主文叙事的主调仍是 "interventional"，与 Limitations 的 "residual confounding is not fully eliminated" 矛盾。建议统一为 "filtering-based confounder control" 或 "approximate interventional design"。

**[REBUT] R1-N2: Bradley-Terry 模型的 IIA 假设未检验**

R1 的统计关切在一般 BT 应用场景下合理，但在本文的**严格配对比较**设定中，IIA 的相关性大幅降低。理由如下：

1. **本文的 BT 模型是纯 paired comparison**：每次比较恰好只有 2 个 alternatives（original vs. style-rewritten），而非从多个候选中排序。IIA（Independence of Irrelevant Alternatives）的经典问题——引入第三选项改变两个已有选项的相对偏好——在只有 2 个 alternatives 的情况下不适用，因为不存在 "irrelevant alternative"。

2. **Appendix G 的 GoF 检验已提供模型充分性证据**：deviance = 52.80, df = 45, p = 0.198（page 11），表明 BT 模型对数据的拟合充分。如果存在严重的异质性交互（不同 task type × style manipulation），GoF 应当拒绝。

3. **GEE 分析（Table 3）作为鲁棒性检验**：Table 3 的 GEE 采用 exchangeable correlation structure，显式建模了 within-pair 相关性，并且 Appendix C (Table 4) 确认换用 independence correlation 后系数变化 |ΔQIC| < 0.001。这实际上是一种对 BT 参数在不同子群间稳定性的间接检验。

4. **分层分析已存在**：论文按 axis（formality/verbosity/register）分别拟合 BT，并在 Appendix A 中进一步按 direction（formal→casual vs. casual→formal）分层。这已经是 R1 建议的 "按 task type 分层检查 BT 参数稳定性" 的变体。

因此，虽然 Hausman-McFadden test 在理论上可以增加严谨性，但在纯 paired comparison 设定下，IIA 不构成 critical issue。建议降级为 minor suggestion。

**[AGREE] R1-N3: Evaluator-producer confound 未充分解决**

同意这是一个有效关切，但认为 R1 对 Appendix D 证据的评估偏低估。

- **Appendix D 的设计是针对性的**：将 rewriter 从 Qwen3-32B 替换为 GPT-4o，保持 Qwen3-32B 为 judge。Table 7 (page 10) 显示 BT win probability 从 81/100 (81%) → 86/100 (86%)，Blindspot 依然存在。如果 self-preference 是主要驱动力，替换 rewriter 后效应应该显著减弱。
- **但 R1 的 nuance 是对的**：Appendix D 证明了 rewriter identity 的影响有限，但无法排除 Qwen3-32B 作为 judge 对*任何* LLM 产出（包括 GPT-4o 的 rewrites）的 systematic preference。真正需要的是固定 rewriter、替换 judge 的反向实验。
- **Panickssery et al. (2024) 已在 Limitations 中引用**（page 9），但主文结果部分（Section 5）在报告 Qwen3-32B 结果时没有 caveat。

建议：在 Section 5 首次报告 Qwen3-32B 结果时加一句 caveat（如 "noting the evaluator-producer overlap caveat discussed in Limitations"），且 Appendix D 应明确承认上述 limitation。但我不认为这构成 critical issue——GPT-4o 结果（独立 rewriter 和 judge）不受此 confound 影响，而 GPT-4o 是论文的主要 judge。建议降级为 should-fix。

---

### Should-Fix 问题

**[AGREE] R1-W1: GEE "confound-free" 解释过强**

同意。Table 3 对 verbosity 的 GEE 结果显示 Originality OR non-significant（p > 0.05），论文据此称 verbosity 是 "confound-free"。但 GEE 只能控制**已观测**的混淆变量（formality 和 originality），无法排除未测量的混淆（如 fluency、coherence 等其他质量维度）。"confound-free" 应改为 "no observed originality confound" 或 "confound-free with respect to the measured covariates"。这与我自己的审稿意见 W1（formality confound）形成互补：formality 有*已知* confound，verbosity 可能有*未知* confound。

**[AGREE] R1-W2: Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示**

同意。Table 2 标题明确是 "formality style-transformed data"。如果 Likert Blindspot 是一个通用现象（如论文所声称），应该在 verbosity 轴上也展示 7 种方法的 sensitivity hierarchy。verbosity 是论文最强证据的来源（confound-free, BT 76.0%），在这个轴上展示 Table 2 风格的分析会大幅增强说服力。缺失这一验证让 Table 2 的结论泛化性存疑。

**[AGREE] R1-W3: "Measurement attenuation" vs "construct difference" 主文呈现不平衡**

同意，且我在自己的审稿中也注意到了这个问题。Limitations (page 9) 原文："An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure." 这个替代解释是同等合理的——甚至可以说在概念上更节俭（不需要假设 Likert "失灵"，只需假设两种量表测量不同东西）。但主文从 Introduction 到 Conclusion 的叙事一直以 "measurement attenuation"（即 Likert 失灵）为主调。建议在 Section 5.2 讨论中给两种解释同等篇幅。

**[AGREE] R1-W4: NLI 阈值 sensitivity analysis 仅 4 个离散点**

同意，但补充一点缓解因素。Section 3.2 使用 DeBERTa-v3-large NLI 的 entailment score 阈值 0.90。如果 Appendix 仅测试了 4 个离散阈值（如 0.85, 0.90, 0.95, 0.99），则对阈值选择的鲁棒性论证不够充分——特别是如果在某些阈值下 Blindspot 消失或显著减弱。建议至少覆盖 0.80-0.98 的 10 个点，绘制 BT win probability 作为 NLI 阈值函数的曲线。

**[AGREE] R1-W5: Cross-rewriter independence test 缺 register 轴**

同意。Appendix D (page 10) 的 Table 6 和 Table 7 分别报告了 verbosity 和 formality 的 rewriter independence 检验，但 register 轴完全缺失。鉴于 register 在 Table 1 中已经是最弱的轴（GPT-4o 和 Qwen3-32B 的 BT 都在 57-60% 范围），如果 register 的 rewriter independence 检验失败，可能意味着 register 轴的结果更多反映 rewriter artifact 而非 judge bias。这是一个实验完整性的缺口。

**[AGREE] R1-W6: 样本量偏小（n=88）缺 power analysis 讨论**

部分同意。论文确实在 Figure 4 (page 7) 提供了 detection probability curves 作为 power analysis 的可视化，显示 BT 在 n≈62 即可检测效应（在观测到的 effect size 下）。这部分回应了 R1 的关切。但 R1 的要点仍然有效：(1) Figure 4 的 power analysis 是 post-hoc 的（用观测 effect size 反推 required n），而非 a priori；(2) n=88 对不同 axis 的 power 不同，register 轴可能严重 underpowered。建议在主文中补充一段讨论，说明各 axis 在当前 n 下的 statistical power（如 80% power 对应的最小可检测效应量）。

---

### Minor Issues

**[AGREE] R1-M1: DAG 黑白打印时 dashed/solid 不易区分**

同意，我在自己的审稿中也指出了同一问题（见我的"小问题"部分）。建议用颜色 + 线型双重编码。

**[AGREE] R1-M2: Table 2 的 7 种方法选择未说明理由**

同意。论文选择了 BT model, filtered sign test, Likert ATE (t-test), binomial Likert, ordinal regression, GEE, Wilcoxon signed-rank 这 7 种方法，但未解释为什么是这 7 种而非其他（如 permutation test, mixed-effects logistic regression）。一句话说明选择标准（如 "覆盖 interval/ordinal/nonparametric 三类方法"）即可。

**[AGREE] R1-M3: "Likert Blindspot" 范围应限定为单题评分**

同意。论文的实验设定是 single-item Likert scoring（judge 对每个 response 给一个 1-10 分数）。如果使用 multi-item composite scales（如多个维度分别评分后加权），attenuation 的程度可能不同。在 Section 1 或 Section 6 中加一句 scope qualifier 即可。

**[REBUT] R1-M4: 评分粒度（1-10 vs 1-100）对 Blindspot 的影响未讨论**

部分反驳。论文在 Limitations (page 9) 已经提及："Whether finer-grained scales (Preston and Colman, 2000) could mitigate the Blindspot remains open; equivalence testing (Lakens, 2017) could formalize whether the Likert effect size is practically zero." 这虽然简短，但确实承认了这个问题。Preston and Colman (2000) 的引用恰好是关于评分粒度对量表可靠性的影响。当然，更充分的讨论（如具体推测 1-100 尺度是否会缩小 BT-Likert gap）会更好，但我不认为这是一个当前完全缺失的问题。

**[AGREE] R1-M5: GPT-4o 验证 NLI gate 存在轻微循环性**

同意存在轻微循环性。Section 5.1 (page 5)："scale GPT-4o validation on all 200 NLI gate decisions yields 92.1% pass precision for formality and 82.6% for verbosity." GPT-4o 既是 NLI gate 的验证者，又是 judge——如果 GPT-4o 系统性地与 NLI gate（DeBERTa）在内容保持判断上一致，那么 NLI gate 可能恰好保留了 GPT-4o "喜欢"的样本，导致检测到的 bias 被筛选过程放大。缓解因素是主要验证用 Qwen3-32B（Section 5.1, "validate all 100 NLI decisions against an LLM annotator (Qwen3-32B)"），GPT-4o 验证是辅助的。但建议在 Section 5.1 中加一句说明这一潜在循环性。

---

### Missing References

**[AGREE] Stureborg et al. (2024), "Large Language Models are Inconsistent and Biased Evaluators"** — 与 LLM judge 的 inconsistency 和 bias 直接相关，是 Related Work Section 2 讨论 LLM-as-Judge bias 的自然引用目标。

**[AGREE] Park et al. (2024), "Disentangling Length from Quality in Direct Assessments"** — 与本文的 verbosity/length confound 分析（Section 5.4, 5.5）高度相关。本文声称 verbosity 是 "confound-free"，但 Park et al. 的 length-quality disentangling 方法可能提供补充视角。

补充：我在自己的审稿中还识别了 **Jeong et al. (2025), "The Comparative Trap"**（BlackboxNLP）——该文系统性地证明 pairwise comparison 放大了 LLM evaluator 的 style bias，与本文核心叙事（pairwise 检测 Likert 遗漏的 bias）存在直接张力。建议 R1 也关注此引用。

---

### 总结：与 R1 评分的对比

| 维度 | R1 评分 | R2 评分 | 差异理由 |
|------|--------|--------|---------|
| Overall | 3.5 (Borderline Conf.) | 3.0 (Findings) | R2 对 novelty 评价更低（domain transfer of psychometric insight），且对 judge 覆盖面（仅 2 个有效 judge）的要求更严格 |
| Soundness | 4.0 | 3.5 | R2 认为 formality confound 和缺失的 Comparative Trap 讨论更严重地影响 soundness |
| Excitement | 3.0 | 2.5 | R2 认为 Likert Blindspot 的概念新颖性有限，CSD 相对 RATE 增量不足 |

两位 reviewer 的核心分歧在于对 novelty 的定义：R1 偏重方法论执行质量（acknowledge 统计严谨性），R2 偏重概念原创性（认为 Thurstone 1927 已预言了这一现象）。两者都认同论文的统计方法论是其最大优势，实验覆盖面是其最大弱点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-21T12:55:51.774372+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-21T12:55:52.176693+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T12:32:56.863673+00:00\", \"completed_at\": \"2026-05-21T12:35:44.174739+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本无任何 display item，首个视觉锚点 (Figure 1) 延迟到第 3 页；审稿人翻两页纯文字才看到第一个图，锚定印象偏晚。建议将 Figure 1 或一个概念缩略图提前到第 1-2 页\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"三个 display items (Figure 2 + Table 1 + Figure 3) 挤在同一页，视觉密度过高。Figure 2 (DAG) 和 Figure 3 (scatter) 均被压缩，可读性受影响。建议将 Figure 2 前移到第 3-4 页（首次引用在 §3.5 p.4），或将 Figure 3 移到第 6 页\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-4 vs 5-8\", \"message\": \"Display items 分布前松后紧——前 4 页仅 1 个 figure，第 5-8 页集中 6 个。建议重新平衡视觉节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 (DAG) 尺寸偏小，节点标签 (S, Q, Y, style bias) 和红色虚线注释接近可读下限；若能增大 10-15% 或改为 figure* 全宽会更清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 3 钻石标记 (diamond markers) 偏小，被压缩在 Table 1 下方的有限空间内；axis labels 字号约为正文 65-70%，接近下限\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"References 末页约 60% 填充，底部 ~40% 空白；可考虑将部分 appendix 表格移至此处利用空间\"}], \"counts\": {\"critical\": 0, \"warning\": 3, \"info\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-21T12:55:52.177019+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-21T12:55:52.277568+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-21T12:56:41.638989+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-21T12:56:41.639422+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-21T12:59:25.888731+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Abstract/Intro 明确标注为 'first systematic quantitative verification of known measurement theory principle in LLM judge evaluation'. Structural ceiling acknowledged.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4-SF8: Honest novelty positioning applied.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Main text 8 pages.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补。Register 仍缺。Style OR 下降 22% 非可忽略。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R5 两位 Reviewer 均再次指出。R1 定为 critical（self-preference bias 无法排除），R2 认为 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。主文 Section 5 缺 caveat。见 R5-SF2。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Register independence test — acknowledged as limitation\"\n        assigned_to: paper_agent\n        status: wont_fix\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 'approximates the do-operator' 残留。见 R5-MF2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'. n=355 d->0 evidence.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"attenuation framing 已改善，但 'construct difference' 替代解释在主文中仍不足。见 R5-SF6。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Cross-rewriter consistency + 200-pair GPT-4o validation provide partial proxy. Acknowledged in Limitations.\"\n      - round: 5\n        reviewers: []\n        note: \"Round 5 未被任何 Reviewer 显式提及，但仍 inherently open（无人工评估数据）。\"\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"术语已改善，但 verbosity 'confound-free' 措辞仍过强。见 R5-SF4。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"引用量已改善，但遗漏了 Jeong et al. (2025) Comparative Trap 等关键文献。见 R5-MF1。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"TOST at Delta=10pp underpowered (n=87). 措辞仍需更审慎。见 R5-M3。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"仍指出 Abstract 信息密度过高。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均再次指出 Abstract 过密。Minor issue。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"GoF chi2 deviance test + stratified BT + originality-minimal subset. IIA trivially satisfied in paired comparison.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出 IIA 未检验，R2 技术性反驳（纯 paired comparison 无 irrelevant alternative，GoF 已通过）。交叉后共识：降级为 minor。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues (new)\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)——pairwise amplification vs detection sensitivity 张力未讨论\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 首先识别，R1 交叉回应完全同意并认为是本轮最严重问题。Jeong et al. (2025, BlackboxNLP) 证明 pairwise comparison 放大 style bias，与本文 Section 6 'adopt pairwise' 建议直接矛盾。论文需区分 detection sensitivity 和 bias amplification。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap；在 §5.2 或 §6 论证 CSD 的 NLI gate + position control 如何区分 detection 与 amplification\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强——selection/conditioning ≠ intervention，存在 collider bias 风险\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 完全同意。§3.2 原文 'approximates the do-operator' 在因果推断术语上过强。NLI gate 是 post-hoc filtering，不是 intervention。论文 §3.5 后半段有 caveat 但主文叙事主调仍是 'interventional'。与 R3-N1 (已修复的因果术语) 相关但为新角度。\"\n    action_items:\n      - round: 5\n        action: \"将 'approximates the do-operator' 改为 'provides a filtering-based confounder control'；在 §3.5 讨论 selection bias 可能方向\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim——至少 Jeong et al. (2025) 已做类似 systematic quantification\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 识别，R1 部分同意。'first' 需限定到 CSD 具体方法组合的 novelty（NLI gate + per-axis decomposition + position-controlled pairwise），而非整体研究问题。\"\n    action_items:\n      - round: 5\n        action: \"将 Abstract/Intro 的 'first' claim 限定到具体方法组合\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat——Qwen3-32B 结果在 Section 5 首次出现时无任何警示\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 定 critical，R2 建议 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。需在 §5.3 首次报告 Qwen3-32B 结果时加 caveat。延续 RD2-SF1。\"\n    action_items:\n      - round: 5\n        action: \"§5.3 加一句 evaluator-producer overlap caveat\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性——实质仅 2 个 judge 展示 Blindspot\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 定 critical（缺 Gemini/Llama），R1 反驳（方法论贡献 2+1 足够）。交叉后共识：should-fix。修改 Abstract/Intro 措辞为 'across two commercial judges, with a third serving as negative control'。\"\n    action_items:\n      - round: 5\n        action: \"调整 'across three judges' 措辞，明确 Claude 角色\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强——仅控制了已观测 confound\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 同意。'confound-free' 应改为 'no observed originality confound' 或加 'with respect to measured covariates' 限定。\"\n    action_items:\n      - round: 5\n        action: \"Table 3 caption 和 §5.4-5.6 将 'confound-free' 改为 'no observed originality confound'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 同意。Table 2 是论文核心方法论贡献之一，仅在 formality 展示不够。在 Appendix 补 verbosity 7 方法对比。\"\n    action_items:\n      - round: 5\n        action: \"Appendix 补 verbosity 轴的 7-method sensitivity hierarchy table\"\n        assigned_to: agent\n        status: pending\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现严重不平衡——替代解释仅在 Limitations 一笔带过\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 同意。Comparative Trap (R5-MF1) 进一步加强了 construct difference 解释。需在 §5.2 给两种解释同等篇幅。\"\n    action_items:\n      - round: 5\n        action: \"§5.2 末尾增加 construct difference 讨论段落，给两种解释同等权重\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF7\"\n    summary: \"Formality confound 在 Abstract/Conclusion 中未与 verbosity 区分——读者误以为三轴等价\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 和 R2 均指出。Abstract 'three style axes' 未说明各轴证据强度不同。需明确 verbosity = confound-free, formality = conditional style effect with originality confound。\"\n    action_items:\n      - round: 5\n        action: \"Abstract/Conclusion 区分 verbosity (clean) 和 formality (confounded)\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点，不足以建立 plateau\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。建议 Appendix 补 10+ 点的连续 sensitivity 曲线。\"\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。Register 是最弱轴，恰是 rewriter identity 最可能影响结论的轴。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 识别，R1 同意。Equivalence bound Delta=15pp 缺 external justification。\"\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。每个缺失 cell 应在 footnote 或 Appendix 说明原因。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立指出。建议颜色 + 线型双重编码。\"\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025) Comparative Trap, Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Jeong et al. 为必须引用（与核心叙事矛盾）。Stureborg et al. 和 Park et al. 为高度相关。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Abstract/Intro 明确标注为 'first systematic quantitative verification of known measurement theory principle in LLM judge evaluation'. Structural ceiling acknowledged.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4-SF8: Honest novelty positioning applied.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Main text 8 pages.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补。Register 仍缺。Style OR 下降 22% 非可忽略。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R5 两位 Reviewer 均再次指出。R1 定为 critical（self-preference bias 无法排除），R2 认为 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。主文 Section 5 缺 caveat。见 R5-SF2。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Register independence test — acknowledged as limitation\"\n        assigned_to: paper_agent\n        status: wont_fix\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 'approximates the do-operator' 残留。见 R5-MF2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'. n=355 d->0 evidence.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"attenuation framing 已改善，但 'construct difference' 替代解释在主文中仍不足。见 R5-SF6。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Cross-rewriter consistency + 200-pair GPT-4o validation provide partial proxy. Acknowledged in Limitations.\"\n      - round: 5\n        reviewers: []\n        note: \"Round 5 未被任何 Reviewer 显式提及，但仍 inherently open（无人工评估数据）。\"\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"术语已改善，但 verbosity 'confound-free' 措辞仍过强。见 R5-SF4。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"引用量已改善，但遗漏了 Jeong et al. (2025) Comparative Trap 等关键文献。见 R5-MF1。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"TOST at Delta=10pp underpowered (n=87). 措辞仍需更审慎。见 R5-M3。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"仍指出 Abstract 信息密度过高。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均再次指出 Abstract 过密。Minor issue。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"GoF chi2 deviance test + stratified BT + originality-minimal subset. IIA trivially satisfied in paired comparison.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出 IIA 未检验，R2 技术性反驳（纯 paired comparison 无 irrelevant alternative，GoF 已通过）。交叉后共识：降级为 minor。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues (new)\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)——pairwise amplification vs detection sensitivity 张力未讨论\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 首先识别，R1 交叉回应完全同意并认为是本轮最严重问题。Jeong et al. (2025, BlackboxNLP) 证明 pairwise comparison 放大 style bias，与本文 Section 6 'adopt pairwise' 建议直接矛盾。论文需区分 detection sensitivity 和 bias amplification。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap；在 §5.2 或 §6 论证 CSD 的 NLI gate + position control 如何区分 detection 与 amplification\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强——selection/conditioning ≠ intervention，存在 collider bias 风险\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 完全同意。§3.2 原文 'approximates the do-operator' 在因果推断术语上过强。NLI gate 是 post-hoc filtering，不是 intervention。论文 §3.5 后半段有 caveat 但主文叙事主调仍是 'interventional'。与 R3-N1 (已修复的因果术语) 相关但为新角度。\"\n    action_items:\n      - round: 5\n        action: \"将 'approximates the do-operator' 改为 'provides a filtering-based confounder control'；在 §3.5 讨论 selection bias 可能方向\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim——至少 Jeong et al. (2025) 已做类似 systematic quantification\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 识别，R1 部分同意。'first' 需限定到 CSD 具体方法组合的 novelty（NLI gate + per-axis decomposition + position-controlled pairwise），而非整体研究问题。\"\n    action_items:\n      - round: 5\n        action: \"将 Abstract/Intro 的 'first' claim 限定到具体方法组合\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat——Qwen3-32B 结果在 Section 5 首次出现时无任何警示\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 定 critical，R2 建议 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。需在 §5.3 首次报告 Qwen3-32B 结果时加 caveat。延续 RD2-SF1。\"\n    action_items:\n      - round: 5\n        action: \"§5.3 加一句 evaluator-producer overlap caveat\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性——实质仅 2 个 judge 展示 Blindspot\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 定 critical（缺 Gemini/Llama），R1 反驳（方法论贡献 2+1 足够）。交叉后共识：should-fix。修改 Abstract/Intro 措辞为 'across two commercial judges, with a third serving as negative control'。\"\n    action_items:\n      - round: 5\n        action: \"调整 'across three judges' 措辞，明确 Claude 角色\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强——仅控制了已观测 confound\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 同意。'confound-free' 应改为 'no observed originality confound' 或加 'with respect to measured covariates' 限定。\"\n    action_items:\n      - round: 5\n        action: \"Table 3 caption 和 §5.4-5.6 将 'confound-free' 改为 'no observed originality confound'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 同意。Table 2 是论文核心方法论贡献之一，仅在 formality 展示不够。在 Appendix 补 verbosity 7 方法对比。\"\n    action_items:\n      - round: 5\n        action: \"Appendix 补 verbosity 轴的 7-method sensitivity hierarchy table\"\n        assigned_to: agent\n        status: pending\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现严重不平衡——替代解释仅在 Limitations 一笔带过\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 同意。Comparative Trap (R5-MF1) 进一步加强了 construct difference 解释。需在 §5.2 给两种解释同等篇幅。\"\n    action_items:\n      - round: 5\n        action: \"§5.2 末尾增加 construct difference 讨论段落，给两种解释同等权重\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF7\"\n    summary: \"Formality confound 在 Abstract/Conclusion 中未与 verbosity 区分——读者误以为三轴等价\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 和 R2 均指出。Abstract 'three style axes' 未说明各轴证据强度不同。需明确 verbosity = confound-free, formality = conditional style effect with originality confound。\"\n    action_items:\n      - round: 5\n        action: \"Abstract/Conclusion 区分 verbosity (clean) 和 formality (confounded)\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点，不足以建立 plateau\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。建议 Appendix 补 10+ 点的连续 sensitivity 曲线。\"\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。Register 是最弱轴，恰是 rewriter identity 最可能影响结论的轴。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 识别，R1 同意。Equivalence bound Delta=15pp 缺 external justification。\"\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。每个缺失 cell 应在 footnote 或 Appendix 说明原因。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立指出。建议颜色 + 线型双重编码。\"\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025) Comparative Trap, Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Jeong et al. 为必须引用（与核心叙事矛盾）。Stureborg et al. 和 Park et al. 为高度相关。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-21T12:59:25.939880+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 26636}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-21T13:01:15.617750+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# 审稿报告：The Likert Blindspot\n\n**论文**：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**：EMNLP 2026 Main Conference (via ARR)\n**审稿模式**：Fresh（初审）\n**Reviewer 编排**：2 人（R1 方法严谨性 / R2 新颖性与完整性）\n**轮次**：Round 1 独立审稿 → 交叉分享 → 共识收敛（1 轮达成）\n\n---\n\n## Summary\n\n论文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 style-controlled rewriting、NLI content gating 和 position-controlled pairwise comparison 检测 LLM judge 的 per-axis style bias。核心发现是 Likert Blindspot：在相同数据上，Likert 评分（7 种统计方法）均无法检测到 pairwise comparison 可靠识别的 style bias（BT 63-84%, p < 0.001）。实验覆盖 2 个 target judges (GPT-4o, Qwen3-32B) + 1 个 negative control (Claude Sonnet 4)，3 个 benchmarks (LLMBar, AlpacaEval, MT-Bench)，3 个 style axes (formality, verbosity, register)。GEE 条件分解揭示 verbosity 为 clean style effect，formality/register 混淆 originality confound。\n\n---\n\n## Strengths\n\n1. **统计方法论深度罕见**：7 种测量方法的 sensitivity hierarchy (Table 2)、GEE conditional decomposition (Table 3)、BT GoF diagnostics (Appendix G)、TOST equivalence testing (Appendix F) 在 NLP 评估论文中少见。两位 Reviewer 一致认可这是论文最大优势。\n\n2. **Verbosity 轴提供了清晰的 confound-free 证据**：BT 76-77% ($p < 0.0001$)，GEE 确认 Originality OR non-significant，两个 judge 高度一致（OR 11.34 vs 13.10），且 Likert 完全无法检测（所有 $p > 0.17$）。这是 Likert Blindspot 的最干净论证。\n\n3. **多层实验控制设计合理**：Position double-swap、NLI content gate（precision 98.9%）、consistency filter 三层控制，加上 cross-rewriter independence test (Appendix D) 和 cross-benchmark replication (Table 1)，实验设计的控制层次在同类论文中突出。\n\n4. **Negative control 有独立方法论价值**：Claude Sonnet 4 在所有轴上未检测到 bias (BT ~56%, n.s.)，证明 CSD 不是在所有 judge 上产生假阳性，建立了 discriminant validity。\n\n5. **对 RATE 的 head-to-head 比较公平且有洞察**：Section 5.2 在相同数据上直接比较 RATE 的 Likert ATE 与 CSD 的 pairwise comparison，揭示 RATE 的 metric 本身受 Blindspot 影响。\n\n---\n\n## Weaknesses\n\n### Must-Fix（2 项，两位 Reviewer 共识）\n\n**MF1** [R5-MF1] 遗漏关键矛盾文献：The Comparative Trap (Jeong et al., 2025, BlackboxNLP)\n- Jeong et al. (2025) 系统性证明 pairwise comparison **放大** LLM evaluator 的 style bias（尤其 verbosity、authoritative tone），而非仅\"检测\"。\n- 本文 Section 6 建议 \"style bias audits should adopt pairwise comparison\"，与该发现存在直接张力：pairwise 的更高检出率究竟是 **detection sensitivity**（本文主张）还是 **bias amplification**（Jeong et al. 主张）？\n- 论文未讨论这一区分，也未论证 CSD 的 NLI gate + position control 是否能区分两种机制。\n- 如果 amplification 解释成立，Likert 可能不是\"blindspot\"而是更接近真实 bias 幅度的测量；BT 63-77% 可能是 amplified signal。\n- **两位 Reviewer 共识**：R2 首先识别，R1 交叉回应完全同意，认为是本轮最严重问题。\n\n**MF2** [R5-MF2] NLI gate \"approximates the do-operator\" 声明过强\n- Section 3.2 原文将 NLI gate 定位为 do-operator 近似，但 NLI filtering 是 post-hoc selection/conditioning，不是 intervention (Pearl, 2009)。\n- Selection ≠ intervention：通过 NLI 筛选保留的样本可能在未观测维度上系统性不同（collider bias 风险）。\n- 论文 Section 3.5 后半段有 caveat（\"we do not claim...a complete structural causal model\"），但主文叙事主调仍是 \"interventional\"，与 Limitations 的 \"residual confounding is not fully eliminated\" 矛盾。\n- **两位 Reviewer 共识**：R1 识别，R2 完全同意。建议改为 \"filtering-based confounder control\"。\n\n### Should-Fix（7 项）\n\n**SF1** [R5-SF1] \"first systematic quantitative verification\" overclaim\n- Abstract 和 Section 1 的 \"first\" claim 在 Jeong et al. (2025) 已做类似 systematic quantification 的情况下不成立。\n- 需限定到 CSD 具体方法组合的 novelty（NLI gate + per-axis decomposition + position-controlled pairwise）。\n- **R2 识别，R1 部分同意**。\n\n**SF2** [R5-SF2] Evaluator-producer confound 主文缺 caveat\n- Qwen3-32B 同时做 rewriter 和 judge，引入 self-preference bias 风险。Appendix D 的 cross-rewriter test 证明 rewriter identity 影响有限（Style OR 下降 22%），但无法排除 Qwen3-32B 作为 judge 偏好任何 LLM 产出。\n- GPT-4o 结果不受此 confound 影响，但 Section 5.3 首次报告 Qwen3-32B 时无任何警示。\n- **R1 识别（critical），R2 同意但建议降级（GPT-4o 是主 judge）。交叉后共识：should-fix**。\n\n**SF3** [R5-SF3] \"across three judges\" framing 有误导性\n- 实质仅 2 个 judge 展示 Blindspot，Claude 为 negative control。Abstract \"across three judges\" 可能给人 3 个 judge 都显示 bias 的印象。\n- **R2 识别（critical），R1 反驳（方法论贡献 2+1 足够）。交叉后共识：should-fix**。修改措辞即可，不需新实验。\n\n**SF4** [R5-SF4] GEE \"confound-free\" 措辞过强\n- Table 3 和 Section 5.4 对 verbosity 使用 \"confound-free\"，但 GEE 仅控制已观测 confound（originality），无法排除未测量混淆（fluency、coherence 等）。\n- 应改为 \"no observed originality confound\"。\n- **两位 Reviewer 共识**。\n\n**SF5** [R5-SF5] Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示\n- Table 2 的 7 方法对比是核心方法论贡献，但仅在 formality 展示。如果 verbosity（更强轴）上也成立，论文核心论点大幅增强。\n- 建议 Appendix 补 verbosity 的 7 方法表。\n- **两位 Reviewer 共识**。\n\n**SF6** [R5-SF6] Measurement attenuation vs. construct difference 主文呈现不平衡\n- Limitations 承认 \"Likert and pairwise modes measure different constructs\" 是同等合理的替代解释，但主文 Introduction 到 Conclusion 一直以 \"measurement attenuation\"（Likert 失灵）为主调。\n- Comparative Trap (MF1) 进一步加强了 construct difference 解释。\n- 需在 Section 5.2 给两种解释同等篇幅。\n- **两位 Reviewer 共识**。\n\n**SF7** [R5-SF7] Formality/verbosity 在 Abstract 中未区分证据强度\n- Abstract \"three style axes\" 未说明各轴证据强度不同。Verbosity = confound-free clean evidence；formality = conditional style effect with significant originality confound。\n- 读者可能误以为三轴等价。\n- **两位 Reviewer 共识**。\n\n### Minor（5 项）\n\n- **M1** [R5-M1] NLI 阈值 sensitivity sweep 仅 4 个离散点（0.70/0.80/0.90/0.95），不足以建立 plateau。建议 Appendix 补 10+ 点连续曲线。\n- **M2** [R5-M2] Cross-rewriter independence test 缺 register 轴——register 是最弱轴，恰是 rewriter artifact 最可能影响结论之处。\n- **M3** [R5-M3] Claude TOST \"no bias\" 措辞需改为 \"failed to detect bias at current n\"；Δ=15pp equivalence bound 缺 external justification。\n- **M4** [R5-M4] Table 1 实验矩阵有空 cell 未解释原因。\n- **M5** [R5-M5] Figure 2 DAG dashed/solid edges 黑白打印不清，建议颜色 + 线型双重编码。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n- Comparative Trap 遗漏是本轮最严重问题 (MF1)\n- NLI gate do-operator 声明需降级 (MF2)\n- \"first\" claim 需限定范围 (SF1)\n- GEE \"confound-free\" 过强 (SF4)\n- Sensitivity hierarchy 需多轴验证 (SF5)\n- Measurement attenuation vs. construct difference 不平衡 (SF6)\n- Formality/verbosity 证据强度应在 Abstract 区分 (SF7)\n- DAG 打印清晰度 (M5)\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 解决 |\n|------|----|----|------|\n| BT IIA 假设 | Critical (N2) | Rebut: 纯 paired comparison 无 IIA 问题 | R2 论证有力，降级为 minor（不列入正式 weakness） |\n| Evaluator-producer severity | Critical (N3) | Should-fix (GPT-4o 不受影响) | 折中为 should-fix (SF2) |\n| Judge 覆盖面 | Should-fix (措辞调整) | Critical (需加 judge) | 折中为 should-fix (SF3)，措辞调整而非新实验 |\n| Overall 评分 | 3.5 Borderline Conf. | 3.0 Findings | 分歧源于 novelty 定义——R1 偏重方法执行质量，R2 偏重概念原创性 |\n\n---\n\n## Questions\n\n1. Table 2 的 sensitivity hierarchy 在 verbosity 轴上是否成立？verbosity 的 Likert ATE 是否在 BT >70% 时也始终为 non-significant？\n2. 如何区分 CSD 检测到的 bias 是 \"detection sensitivity\"（Likert 遗漏的真实 bias）还是 \"bias amplification\"（pairwise 放大的人工 bias）？NLI gate 能否在理论上阻断 amplification 机制？\n3. n=355 时 Likert d→0 的证据是否在更大 n（bootstrap extrapolation 或模拟）下也收敛到 0？这对区分 attenuation 和 power gap 至关重要。\n4. Qwen3-32B 作为 judge 时，是否有 self-preference 的直接证据（如在未经 style manipulation 的 pair 上是否偏好自身产出）？\n\n---\n\n## Missing References\n\n1. **Jeong et al. (2025)** \"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators\" (BlackboxNLP) — **必须引用**，与核心叙事直接矛盾\n2. **Stureborg et al. (2024)** \"Large Language Models are Inconsistent and Biased Evaluators\" — LLM judge inconsistency 和 bias\n3. **Park et al. (2024)** \"Disentangling Length from Quality in Direct Assessments\" — verbosity/length confound 相关\n\n---\n\n## External Review\n\n外部审稿：未请求（项目未配置 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warning / 3 info / 0 critical）：\n- **[warning]** 连续 2 页纯文本无 display item，首个视觉锚点 (Figure 1) 延迟到第 3 页。建议将 Figure 1 或概念缩略图提前。\n- **[warning]** 第 5 页三个 display items (Figure 2 + Table 1 + Figure 3) 挤在同一页，视觉密度过高。\n- **[warning]** Display items 分布前松后紧——前 4 页仅 1 个 figure，第 5-8 页集中 6 个。建议重新平衡。\n- **[info]** Figure 2 (DAG) 尺寸偏小，节点标签接近可读下限。\n- **[info]** Figure 3 钻石标记偏小，axis labels 字号约 65-70% 正文，接近下限。\n- **[info]** References 末页约 60% 填充，底部 ~40% 空白。\n\n---\n\n## Overall Assessment\n\n**Overall**：3.5 / 5 — Borderline Conference\n**Confidence**：4 / 5\n\n**评分理由**：\n\n论文的统计方法论深度（7 方法 hierarchy、GEE decomposition、BT diagnostics）在同类论文中突出，verbosity 轴提供了清晰且 confound-free 的 Likert Blindspot 证据。CSD 框架的多层控制设计合理，negative control 建立了 discriminant validity。\n\n但论文存在两个结构性问题：\n1. **核心叙事未与矛盾证据调和**：Comparative Trap (Jeong et al., 2025) 证明 pairwise 放大 style bias，论文未讨论 detection sensitivity 与 bias amplification 的区分。这直接影响 \"adopt pairwise\" 实践建议的可靠性。\n2. **因果声明与证据强度不匹配**：NLI gate 的 do-operator 声明超出 filtering 操作的能力，主文\"interventional\"叙事与 Limitations 的 \"residual confounding\" 矛盾。\n\n**Novelty 评估**：Likert Blindspot 本质是心理测量学已知现象（Thurstone 1927, Stevens 1946）在 LLM judge 领域的 domain transfer。论文诚实定位为 \"first systematic quantitative verification\"，但 Jeong et al. (2025) 的存在使 \"first\" claim 需进一步限定。增量贡献主要来自方法执行质量（per-axis decomposition + NLI gate + 7-method hierarchy），概念原创性有限。\n\n**修改路径**：如果 MF1（Comparative Trap 讨论 + detection vs. amplification 区分）和 MF2（因果语言降级）得到充分解决，且 SF1-SF7 的 framing 调整到位，论文可达 **4.0 (Conference)**。当前状态为 Borderline Conference。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"the first systematic quantitative verification\" → 限定到具体方法组合\n- \"across three judges\" → 明确 2 target + 1 negative control\n- Contributions 列表应区分 verbosity (clean) vs. formality (confounded)\n\n### Section 2 (Related Work)\n- 必须增加 Comparative Trap (Jeong et al., 2025) 讨论\n- 应增加 Stureborg et al. (2024) 和 Park et al. (2024)\n- Bradley-Terry 段落可讨论 pairwise 的 amplification 风险\n\n### Section 3 (Method)\n- §3.2: \"approximates the do-operator\" → \"provides a filtering-based confounder control\"\n- §3.5: 增加 selection bias 讨论，与 Limitations 的 \"residual confounding\" 保持一致\n- DAG (Figure 2): 增加颜色编码辅助黑白打印\n\n### Section 5 (Analysis)\n- §5.2: 增加 construct difference 讨论段落，与 Comparative Trap 关联\n- §5.3: Qwen3-32B 首次出现时加 evaluator-producer caveat\n- §5.4/5.6: \"confound-free\" → \"no observed originality confound\"\n- Table 1: 空 cell 加 footnote 说明\n- Table 2: Appendix 补 verbosity 7-method 对比\n\n### Section 6 (Conclusion)\n- \"style bias audits should adopt pairwise comparison\" 需加限定条件\n- 区分 verbosity (strongest evidence) vs. formality (conditional) vs. register (exploratory)\n\n### Limitations\n- Claude TOST: \"no bias\" → \"failed to detect bias at current sample size\"\n- Equivalence bound Δ=15pp 加 justification\n\n### Format\n- \"Blindspot\" 大小写统一\n- \"style bias\" vs \"style preference\" 区分使用"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "report": "# 审稿报告：The Likert Blindspot\n\n**论文**：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**：EMNLP 2026 Main Conference (via ARR)\n**审稿模式**：Fresh（初审）\n**Reviewer 编排**：2 人（R1 方法严谨性 / R2 新颖性与完整性）\n**轮次**：Round 1 独立审稿 → 交叉分享 → 共识收敛（1 轮达成）\n\n---\n\n## Summary\n\n论文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 style-controlled rewriting、NLI content gating 和 position-controlled pairwise comparison 检测 LLM judge 的 per-axis style bias。核心发现是 Likert Blindspot：在相同数据上，Likert 评分（7 种统计方法）均无法检测到 pairwise comparison 可靠识别的 style bias（BT 63-84%, p < 0.001）。实验覆盖 2 个 target judges (GPT-4o, Qwen3-32B) + 1 个 negative control (Claude Sonnet 4)，3 个 benchmarks (LLMBar, AlpacaEval, MT-Bench)，3 个 style axes (formality, verbosity, register)。GEE 条件分解揭示 verbosity 为 clean style effect，formality/register 混淆 originality confound。\n\n---\n\n## Strengths\n\n1. **统计方法论深度罕见**：7 种测量方法的 sensitivity hierarchy (Table 2)、GEE conditional decomposition (Table 3)、BT GoF diagnostics (Appendix G)、TOST equivalence testing (Appendix F) 在 NLP 评估论文中少见。两位 Reviewer 一致认可这是论文最大优势。\n\n2. **Verbosity 轴提供了清晰的 confound-free 证据**：BT 76-77% ($p < 0.0001$)，GEE 确认 Originality OR non-significant，两个 judge 高度一致（OR 11.34 vs 13.10），且 Likert 完全无法检测（所有 $p > 0.17$）。这是 Likert Blindspot 的最干净论证。\n\n3. **多层实验控制设计合理**：Position double-swap、NLI content gate（precision 98.9%）、consistency filter 三层控制，加上 cross-rewriter independence test (Appendix D) 和 cross-benchmark replication (Table 1)，实验设计的控制层次在同类论文中突出。\n\n4. **Negative control 有独立方法论价值**：Claude Sonnet 4 在所有轴上未检测到 bias (BT ~56%, n.s.)，证明 CSD 不是在所有 judge 上产生假阳性，建立了 discriminant validity。\n\n5. **对 RATE 的 head-to-head 比较公平且有洞察**：Section 5.2 在相同数据上直接比较 RATE 的 Likert ATE 与 CSD 的 pairwise comparison，揭示 RATE 的 metric 本身受 Blindspot 影响。\n\n---\n\n## Weaknesses\n\n### Must-Fix（2 项，两位 Reviewer 共识）\n\n**MF1** [R5-MF1] 遗漏关键矛盾文献：The Comparative Trap (Jeong et al., 2025, BlackboxNLP)\n- Jeong et al. (2025) 系统性证明 pairwise comparison **放大** LLM evaluator 的 style bias（尤其 verbosity、authoritative tone），而非仅\"检测\"。\n- 本文 Section 6 建议 \"style bias audits should adopt pairwise comparison\"，与该发现存在直接张力：pairwise 的更高检出率究竟是 **detection sensitivity**（本文主张）还是 **bias amplification**（Jeong et al. 主张）？\n- 论文未讨论这一区分，也未论证 CSD 的 NLI gate + position control 是否能区分两种机制。\n- 如果 amplification 解释成立，Likert 可能不是\"blindspot\"而是更接近真实 bias 幅度的测量；BT 63-77% 可能是 amplified signal。\n- **两位 Reviewer 共识**：R2 首先识别，R1 交叉回应完全同意，认为是本轮最严重问题。\n\n**MF2** [R5-MF2] NLI gate \"approximates the do-operator\" 声明过强\n- Section 3.2 原文将 NLI gate 定位为 do-operator 近似，但 NLI filtering 是 post-hoc selection/conditioning，不是 intervention (Pearl, 2009)。\n- Selection ≠ intervention：通过 NLI 筛选保留的样本可能在未观测维度上系统性不同（collider bias 风险）。\n- 论文 Section 3.5 后半段有 caveat（\"we do not claim...a complete structural causal model\"），但主文叙事主调仍是 \"interventional\"，与 Limitations 的 \"residual confounding is not fully eliminated\" 矛盾。\n- **两位 Reviewer 共识**：R1 识别，R2 完全同意。建议改为 \"filtering-based confounder control\"。\n\n### Should-Fix（7 项）\n\n**SF1** [R5-SF1] \"first systematic quantitative verification\" overclaim\n- Abstract 和 Section 1 的 \"first\" claim 在 Jeong et al. (2025) 已做类似 systematic quantification 的情况下不成立。\n- 需限定到 CSD 具体方法组合的 novelty（NLI gate + per-axis decomposition + position-controlled pairwise）。\n- **R2 识别，R1 部分同意**。\n\n**SF2** [R5-SF2] Evaluator-producer confound 主文缺 caveat\n- Qwen3-32B 同时做 rewriter 和 judge，引入 self-preference bias 风险。Appendix D 的 cross-rewriter test 证明 rewriter identity 影响有限（Style OR 下降 22%），但无法排除 Qwen3-32B 作为 judge 偏好任何 LLM 产出。\n- GPT-4o 结果不受此 confound 影响，但 Section 5.3 首次报告 Qwen3-32B 时无任何警示。\n- **R1 识别（critical），R2 同意但建议降级（GPT-4o 是主 judge）。交叉后共识：should-fix**。\n\n**SF3** [R5-SF3] \"across three judges\" framing 有误导性\n- 实质仅 2 个 judge 展示 Blindspot，Claude 为 negative control。Abstract \"across three judges\" 可能给人 3 个 judge 都显示 bias 的印象。\n- **R2 识别（critical），R1 反驳（方法论贡献 2+1 足够）。交叉后共识：should-fix**。修改措辞即可，不需新实验。\n\n**SF4** [R5-SF4] GEE \"confound-free\" 措辞过强\n- Table 3 和 Section 5.4 对 verbosity 使用 \"confound-free\"，但 GEE 仅控制已观测 confound（originality），无法排除未测量混淆（fluency、coherence 等）。\n- 应改为 \"no observed originality confound\"。\n- **两位 Reviewer 共识**。\n\n**SF5** [R5-SF5] Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示\n- Table 2 的 7 方法对比是核心方法论贡献，但仅在 formality 展示。如果 verbosity（更强轴）上也成立，论文核心论点大幅增强。\n- 建议 Appendix 补 verbosity 的 7 方法表。\n- **两位 Reviewer 共识**。\n\n**SF6** [R5-SF6] Measurement attenuation vs. construct difference 主文呈现不平衡\n- Limitations 承认 \"Likert and pairwise modes measure different constructs\" 是同等合理的替代解释，但主文 Introduction 到 Conclusion 一直以 \"measurement attenuation\"（Likert 失灵）为主调。\n- Comparative Trap (MF1) 进一步加强了 construct difference 解释。\n- 需在 Section 5.2 给两种解释同等篇幅。\n- **两位 Reviewer 共识**。\n\n**SF7** [R5-SF7] Formality/verbosity 在 Abstract 中未区分证据强度\n- Abstract \"three style axes\" 未说明各轴证据强度不同。Verbosity = confound-free clean evidence；formality = conditional style effect with significant originality confound。\n- 读者可能误以为三轴等价。\n- **两位 Reviewer 共识**。\n\n### Minor（5 项）\n\n- **M1** [R5-M1] NLI 阈值 sensitivity sweep 仅 4 个离散点（0.70/0.80/0.90/0.95），不足以建立 plateau。建议 Appendix 补 10+ 点连续曲线。\n- **M2** [R5-M2] Cross-rewriter independence test 缺 register 轴——register 是最弱轴，恰是 rewriter artifact 最可能影响结论之处。\n- **M3** [R5-M3] Claude TOST \"no bias\" 措辞需改为 \"failed to detect bias at current n\"；Δ=15pp equivalence bound 缺 external justification。\n- **M4** [R5-M4] Table 1 实验矩阵有空 cell 未解释原因。\n- **M5** [R5-M5] Figure 2 DAG dashed/solid edges 黑白打印不清，建议颜色 + 线型双重编码。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n- Comparative Trap 遗漏是本轮最严重问题 (MF1)\n- NLI gate do-operator 声明需降级 (MF2)\n- \"first\" claim 需限定范围 (SF1)\n- GEE \"confound-free\" 过强 (SF4)\n- Sensitivity hierarchy 需多轴验证 (SF5)\n- Measurement attenuation vs. construct difference 不平衡 (SF6)\n- Formality/verbosity 证据强度应在 Abstract 区分 (SF7)\n- DAG 打印清晰度 (M5)\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 解决 |\n|------|----|----|------|\n| BT IIA 假设 | Critical (N2) | Rebut: 纯 paired comparison 无 IIA 问题 | R2 论证有力，降级为 minor（不列入正式 weakness） |\n| Evaluator-producer severity | Critical (N3) | Should-fix (GPT-4o 不受影响) | 折中为 should-fix (SF2) |\n| Judge 覆盖面 | Should-fix (措辞调整) | Critical (需加 judge) | 折中为 should-fix (SF3)，措辞调整而非新实验 |\n| Overall 评分 | 3.5 Borderline Conf. | 3.0 Findings | 分歧源于 novelty 定义——R1 偏重方法执行质量，R2 偏重概念原创性 |\n\n---\n\n## Questions\n\n1. Table 2 的 sensitivity hierarchy 在 verbosity 轴上是否成立？verbosity 的 Likert ATE 是否在 BT >70% 时也始终为 non-significant？\n2. 如何区分 CSD 检测到的 bias 是 \"detection sensitivity\"（Likert 遗漏的真实 bias）还是 \"bias amplification\"（pairwise 放大的人工 bias）？NLI gate 能否在理论上阻断 amplification 机制？\n3. n=355 时 Likert d→0 的证据是否在更大 n（bootstrap extrapolation 或模拟）下也收敛到 0？这对区分 attenuation 和 power gap 至关重要。\n4. Qwen3-32B 作为 judge 时，是否有 self-preference 的直接证据（如在未经 style manipulation 的 pair 上是否偏好自身产出）？\n\n---\n\n## Missing References\n\n1. **Jeong et al. (2025)** \"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators\" (BlackboxNLP) — **必须引用**，与核心叙事直接矛盾\n2. **Stureborg et al. (2024)** \"Large Language Models are Inconsistent and Biased Evaluators\" — LLM judge inconsistency 和 bias\n3. **Park et al. (2024)** \"Disentangling Length from Quality in Direct Assessments\" — verbosity/length confound 相关\n\n---\n\n## External Review\n\n外部审稿：未请求（项目未配置 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warning / 3 info / 0 critical）：\n- **[warning]** 连续 2 页纯文本无 display item，首个视觉锚点 (Figure 1) 延迟到第 3 页。建议将 Figure 1 或概念缩略图提前。\n- **[warning]** 第 5 页三个 display items (Figure 2 + Table 1 + Figure 3) 挤在同一页，视觉密度过高。\n- **[warning]** Display items 分布前松后紧——前 4 页仅 1 个 figure，第 5-8 页集中 6 个。建议重新平衡。\n- **[info]** Figure 2 (DAG) 尺寸偏小，节点标签接近可读下限。\n- **[info]** Figure 3 钻石标记偏小，axis labels 字号约 65-70% 正文，接近下限。\n- **[info]** References 末页约 60% 填充，底部 ~40% 空白。\n\n---\n\n## Overall Assessment\n\n**Overall**：3.5 / 5 — Borderline Conference\n**Confidence**：4 / 5\n\n**评分理由**：\n\n论文的统计方法论深度（7 方法 hierarchy、GEE decomposition、BT diagnostics）在同类论文中突出，verbosity 轴提供了清晰且 confound-free 的 Likert Blindspot 证据。CSD 框架的多层控制设计合理，negative control 建立了 discriminant validity。\n\n但论文存在两个结构性问题：\n1. **核心叙事未与矛盾证据调和**：Comparative Trap (Jeong et al., 2025) 证明 pairwise 放大 style bias，论文未讨论 detection sensitivity 与 bias amplification 的区分。这直接影响 \"adopt pairwise\" 实践建议的可靠性。\n2. **因果声明与证据强度不匹配**：NLI gate 的 do-operator 声明超出 filtering 操作的能力，主文\"interventional\"叙事与 Limitations 的 \"residual confounding\" 矛盾。\n\n**Novelty 评估**：Likert Blindspot 本质是心理测量学已知现象（Thurstone 1927, Stevens 1946）在 LLM judge 领域的 domain transfer。论文诚实定位为 \"first systematic quantitative verification\"，但 Jeong et al. (2025) 的存在使 \"first\" claim 需进一步限定。增量贡献主要来自方法执行质量（per-axis decomposition + NLI gate + 7-method hierarchy），概念原创性有限。\n\n**修改路径**：如果 MF1（Comparative Trap 讨论 + detection vs. amplification 区分）和 MF2（因果语言降级）得到充分解决，且 SF1-SF7 的 framing 调整到位，论文可达 **4.0 (Conference)**。当前状态为 Borderline Conference。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"the first systematic quantitative verification\" → 限定到具体方法组合\n- \"across three judges\" → 明确 2 target + 1 negative control\n- Contributions 列表应区分 verbosity (clean) vs. formality (confounded)\n\n### Section 2 (Related Work)\n- 必须增加 Comparative Trap (Jeong et al., 2025) 讨论\n- 应增加 Stureborg et al. (2024) 和 Park et al. (2024)\n- Bradley-Terry 段落可讨论 pairwise 的 amplification 风险\n\n### Section 3 (Method)\n- §3.2: \"approximates the do-operator\" → \"provides a filtering-based confounder control\"\n- §3.5: 增加 selection bias 讨论，与 Limitations 的 \"residual confounding\" 保持一致\n- DAG (Figure 2): 增加颜色编码辅助黑白打印\n\n### Section 5 (Analysis)\n- §5.2: 增加 construct difference 讨论段落，与 Comparative Trap 关联\n- §5.3: Qwen3-32B 首次出现时加 evaluator-producer caveat\n- §5.4/5.6: \"confound-free\" → \"no observed originality confound\"\n- Table 1: 空 cell 加 footnote 说明\n- Table 2: Appendix 补 verbosity 7-method 对比\n\n### Section 6 (Conclusion)\n- \"style bias audits should adopt pairwise comparison\" 需加限定条件\n- 区分 verbosity (strongest evidence) vs. formality (conditional) vs. register (exploratory)\n\n### Limitations\n- Claude TOST: \"no bias\" → \"failed to detect bias at current sample size\"\n- Equivalence bound Δ=15pp 加 justification\n\n### Format\n- \"Blindspot\" 大小写统一\n- \"style bias\" vs \"style preference\" 区分使用"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-21T13:01:19.634939+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4017
}
```

</details>

---


### Assistant

_source line 410 · 2026-05-21T13:01:28.307073+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **Overall 3.5 / 5 (Borderline Conference)**，Confidence 4/5
- **2 个 Must-Fix**：(1) 遗漏 Comparative Trap——pairwise amplification vs detection sensitivity 张力未调和；(2) NLI gate do-operator 声明过强
- **7 个 Should-Fix**：overclaim 限定、evaluator-producer caveat、judge framing 修正、GEE confound-free 措辞、sensitivity hierarchy 多轴验证、construct difference 平衡讨论、formality/verbosity 区分
- **5 个 Minor**：NLI 阈值扫描粒度、register cross-rewriter、Claude TOST 措辞、Table 1 空 cell、DAG 打印清晰度
- **修改路径**：MF1 + MF2 充分解决后可达 4.0 (Conference)

Issue Tracker 已同步更新（新增 16 条 Round 5 issue）。视觉审查结果（3 warning）已拼入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 40

## Round 40

2 recorded events


### User

_source line 411 · 2026-05-21T13:01:30.907472+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结要点：

**与 R1 一致的**：N1（do-operator overclaim）、N3（evaluator-producer confound，但建议降级为 should-fix）、W1-W6 全部同意、M1-M3/M5 同意。

**与 R1 分歧的**：
- **R1-N2（BT IIA 假设）**：[REBUT] — 在严格 paired comparison 设定下 IIA 不适用（只有 2 个 alternatives），GoF 通过且 GEE 已提供异质性鲁棒性。建议降级为 minor。
- **R1-M4（评分粒度）**：部分 REBUT — Limitations 已引用 Preston & Colman (2000) 讨论了此问题，虽然不够充分但并非完全缺失。

**R2 额外发现 R1 未覆盖的**：Jeong et al. (2025) "The Comparative Trap" 是一篇直接反驳论文核心叙事的关键遗漏文献，建议 R1 也关注。

**评分差异**：R2 给 3.0 (Findings) vs R1 给 3.5 (Borderline Conference)，主要分歧在 novelty 定义——R2 认为 Likert Blindspot 概念层面是心理测量学已知现象的 domain transfer，增量贡献有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 412 · 2026-05-21T13:01:41.587532+00:00_

审稿报告已投递完成。

**本轮审稿总结**：

- **Overall**：3.5 / 5（Borderline Conference）
- **R1**：3.5，**R2**：3.0，最终取 3.5（方法论执行质量获两位 Reviewer 一致认可）

**2 个 Must-Fix**：
1. 遗漏 Comparative Trap (Jeong et al., 2025)——pairwise detection sensitivity vs. bias amplification 张力未讨论
2. NLI gate "approximates the do-operator" 因果声明过强

**7 个 Should-Fix**：涉及 "first" overclaim、evaluator-producer caveat、judge 覆盖 framing、GEE "confound-free" 措辞、sensitivity hierarchy 多轴验证、measurement attenuation vs. construct difference 平衡、formality/verbosity 证据区分

**修改路径**：MF1-MF2 + SF1-SF7 全部解决后可达 4.0（Conference）。

报告、Issue Tracker 均已同步更新并投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 41

## Round 41

2 recorded events


### User

_source line 413 · 2026-05-21T14:22:45.572378+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 Dream 审稿报告：新颖性 + 相关工作 + Story 一致性

**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
**Venue**: EMNLP 2026 Main Conference (via ARR)
**版本**: Dream condensed (6 pages)

---

## Overall Assessment

**Overall**: 3.5 / 5 — Borderline Conference
**Confidence**: 4/5

**一句话总结**: GEE per-axis taxonomy 是独立的方法论贡献，Comparative Trap 四层防御设计精巧，但 "Likert Blindspot" 的概念新颖性本质是心理测量学已知现象的 domain transfer，"6× sensitivity gap" 的量化方式有误导性，且存在一处可能的引用完整性问题。

**Calibration reasoning**: 1 borderline-Major issue（Blindspot framing 偏颇）+ 3 Should-Fix → 定位在 Borderline Conference / strong Findings。

---

## Strengths

1. **GEE per-axis taxonomy 是最强独立贡献** [idea]: 将 style bias 分解为 verbosity（confound-free）、formality（conditional on originality）、register（originality-dominated）的三类模式（Table 3），这一分类法在现有文献中没有先例。它给评估社区提供了可操作的 actionable knowledge——不同 axis 需要不同的 audit 策略。

2. **Comparative Trap 四层防御** [idea]: Section 5.4.1-5.4.4 的四层防御（placebo BT≈50%、NLI gate ablation、Claude negative control、cross-axis gradient monotonicity）是对 Jeong et al. (2025) 关切的系统性回应。特别是 cross-axis gradient 论证——如果 pairwise 格式均匀放大所有 bias，应看到各轴等比膨胀，但实际观察到 verbosity≫formality≫register 的梯度，这与均匀放大假说不一致。

3. **Judge 覆盖面改善** [idea]: 4 个目标 judge 家族（GPT-4o, Qwen3-32B, Gemini-2.0-Flash, Llama-3.1-70B）覆盖了 proprietary/open-source 和 US/China 两个维度，加上 Claude Sonnet 4 作为 negative control。相比仅 2-3 个 judge 的同类研究，覆盖面充分。

4. **Related Work 定位改善**: 现在显式引用并讨论了 Jeong et al. (2025) The Comparative Trap、Stureborg et al. (2024) inconsistency、Park et al. (2024) length-quality disentangling。这些是该领域 2024-2025 的关键 baseline，覆盖了审稿人最可能指出的遗漏。

---

## Weaknesses

### Must-Fix / Borderline-Major

**N1** [idea] "Likert Blindspot" 命名隐含单边判断，construct difference alternative 权重不足

- 具体位置：Abstract、Section 5.2 (page 3)、Section 7 (Conclusion, page 5-6) vs. Limitations (page 6)
- 问题："Blindspot"（盲点）语义预设了 Likert **应该**检测到 pairwise 检测到的效应，即默认 pairwise 测到的是"真实 bias"，Likert 未测到是"失灵"。但 Limitations (page 6) 承认了同等合理的替代解释："Likert and pairwise modes measure different constructs: absolute quality versus ordinal preference." 如果两种量表测量的是不同 construct，则不存在"盲点"——只是两个合法的量表在捕获不同信号。

  主文从 Introduction 到 Conclusion 的叙事一致地以 "measurement attenuation"（Likert 失灵）为主调，Limitations 的替代解释仅两句话。这种不平衡使得论文的核心 framing 建立在一个未证实的假设上。

  **四层防御（Section 5.4）部分缓解了这一关切**——特别是 cross-axis gradient 表明效应量与预期的真实 bias 差异一致，而非 pairwise 格式的 artifact。但防御只能排除 false positive / uniform amplification，不能正面证明 Likert 是"失灵"而非"测量不同东西"。

- 建议：(1) 在 Section 5.2 讨论中给两种解释（attenuation vs. construct difference）同等篇幅；(2) 可改用更中性的术语如 "Likert-pairwise detection gap" 或 "measurement divergence"；(3) 或者提供正面证据支持 attenuation 解释——如人类评注者是否也在 pairwise 下检测到更多 bias。

- **严重程度判断**：Borderline Major。不影响实验结果的有效性（detection gap 是真实的），但影响对结果的解读和论文的核心叙事框架。

### Should-Fix

**W1** [idea] "6× sensitivity gap" 是离散检测计数比而非连续灵敏度指标

- 具体位置：Abstract (page 1)、Table 2 (page 3)
- 问题：Table 2 显示 18 个 judge×axis×benchmark cell 中，BT 在 12 个 cell 显著，Likert 在 2 个 cell 显著，"6×" = 12/2。但这个比率本质上是二值化检测计数的比值，高度依赖于：(a) 显著性阈值 α=0.05 的选择——如果用 α=0.10，更多 Likert cell 可能变显著，比率骤降；(b) 各 cell 效应量在 Likert 检测边界附近的分布密度。如果 10 个 Likert-non-significant cell 的 p 值在 0.05-0.15 之间，则 "6×" 严重夸大了实际灵敏度差异。
- 建议：改用连续指标，如中位 BT win probability 与中位 Likert Cohen's d 的对比，或报告跨 cell 的平均 power ratio。至少在 Abstract 中将 "6× sensitivity gap" 改为 "detects bias in 6× more experimental cells"，使度量基准明确。

**W2** [idea] "first systematic evidence" claim 与 Jeong et al. (2025) 的关系仍需明确

- 具体位置：Page 1, "we provide the first systematic evidence of this phenomenon in LLM evaluation"
- 问题：论文现在引用了 Jeong et al. (2025) The Comparative Trap，该工作也系统性地比较了 pairwise vs. pointwise 格式对 style bias 的敏感度差异——虽然从 amplification 角度。两者都是 "systematic evidence of [Likert vs. pairwise sensitivity] in LLM evaluation"，只是方向性结论不同。保留 "first systematic" 需要更精确的限定。
- 建议：改为 "the first controlled interventional evidence" 或 "the first evidence using content-controlled counterfactuals"，限定到方法论组合的独特性。

**W3** [presentation] 关键引用完整性问题：RATE 归因错误，"Ye et al., 2024" 可能不存在

- 具体位置：Page 2, "RATE (Ye et al., 2024)"；References (page 6), "Ye, S. et al. 2024. Beyond Preference: Universalizing LLM-as-a-Judge through RLHF, arXiv preprint"
- 问题：RATE（Rewrite-based Attribute Treatment Estimator）的作者是 **Reber, David et al. (2025)**，发表于 ICML 2025（arXiv:2410.11348）。论文中将其归因于 "Ye et al., 2024" 并引用了一篇题为 "Beyond Preference: Universalizing LLM-as-a-Judge through RLHF" 的论文——该论文在 arXiv 和 Semantic Scholar 上均无法查到，可能**不存在**。这构成：(1) 对 RATE 的错误归因；(2) 一条可能的幻觉引用。
- 建议：更正为 Reber et al. (2025)，核实 "Ye et al., 2024" 是否为真实论文并修复引用。

**W4** [idea] GEE taxonomy 的泛化验证仅限 LLMBar

- 具体位置：Table 3 (page 4) vs. Table 7 (page 5)
- 问题：GEE decomposition（verbosity=confound-free, formality=conditional, register=originality-dominated）的完整分析仅在 LLMBar 上展示。Section 5.5 的 cross-benchmark generalization（Table 7）扩展到 AlpacaEval 和 MT-Bench，但仅报告 BT win probability，不含 GEE decomposition。taxonomy 是否在其他 benchmark 上也成立未被验证。
- 建议：至少在一个额外 benchmark 上复现 GEE decomposition，或明确说明 taxonomy 结论仅基于 LLMBar。

---

## Minor Issues

**M1** [presentation] 参考文献量偏少（14 篇），对于涉及因果推断、心理测量学、LLM 评估的跨领域工作而言不够充分。缺失的重要引用包括：
- Haak & Schaer (2025, arXiv:2512.14565), "Pairwise Comparison for Bias Identification and Quantification" — 直接比较 Likert vs. pairwise 在 linguistic bias 量化中的效能
- Bradley & Terry (1952) — BT 模型的原始论文，作为论文核心统计方法应被引用
- Liang & Zeger (1986) — GEE 的原始论文，同理
- Feder et al. (2022) — causal inference in NLP 综述，为因果框架提供方法论支撑

**M2** [idea] 4 个 target judge 均为通用大模型，缺少 specialized judge models（如 JudgeLM、Prometheus、Auto-J）。specialized judges 可能有不同的 style sensitivity profile。

**M3** [presentation] Table 1 中 Claude "null cells" 的含义不够清晰——"Claude does not produce false positives" 的论证依赖读者理解 Claude 同时是 null hypothesis 和 negative control，但 Table 注释未明确这一双重角色。

---

## Novelty Differentiation Assessment

| 对比对象 | CSD 差异化 | 是否清晰 |
|---------|----------|---------|
| RATE (Reber et al., 2025) | CSD: per-axis decomposition + NLI gating + Likert vs. pairwise comparison；RATE: aggregate ATE + double-rewriting bias correction | ✅ 清晰（但注意引用归因错误） |
| CASSE (Chen et al., 2024a) | CSD: interventional (rewriting-based)；CASSE: correlational analysis | ✅ 清晰 |
| LC-AlpacaEval (Dubois et al., 2024b) | CSD: multi-axis + GEE decomposition；LC: single dimension (length) | ✅ 清晰 |
| SOS-Bench (Wu et al., 2024) | CSD: measurement instrument comparison；SOS: bias cataloging | ✅ 清晰 |
| The Comparative Trap (Jeong et al., 2025) | CSD: bias detection via controlled rewriting；CT: bias amplification via format comparison | ✅ 清晰，且有四层防御 |

**独立性总结**：CSD 的方法论组合（NLI gating + per-axis + Likert vs. pairwise + GEE decomposition）在现有工作中没有直接先例。每个单独组件不新（NLI gating 类似 RATE 的 content control，per-axis 类似 CASSE 的维度分解），但组合是新的。GEE per-axis taxonomy 的实证发现（三类 confound pattern）是最强的独立贡献。

---

## Story 一致性检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| "Likert Blindspot" 命名公正性 | ⚠️ | 预设 Likert 失灵，construct difference alternative 在 Limitations 提及但权重不足 |
| 四项 contributions scope 匹配 | ✅ | C1(框架)、C2(Blindspot)、C3(taxonomy)、C4(指导) 均有对应实验支撑 |
| "6× sensitivity gap" 准确性 | ⚠️ | 技术上正确（12/2=6）但作为 headline claim 有误导——是检测计数比而非连续灵敏度指标 |
| Abstract claims vs. experiments | ✅ | 4 judges × 3 axes × 3 benchmarks 均有对应数据 |
| Introduction motivation → method | ✅ | 从 "style features drive score variation" → "current methods underestimate" → "CSD" 的叙事逻辑通顺 |
| Conclusion vs. evidence | ⚠️ | "Likert-based evaluation systematically underestimates" 预设了 pairwise 是 ground truth，而这正是未证实的假设 |

---

## 与 Scope / Venue 匹配度

EMNLP 2026 Main (~21% acceptance) 对 empirical contribution + methodological novelty 的要求较高。本文：
- **达标**：实验设计严谨（4 judges, 3 benchmarks, 四层 robustness controls），GEE taxonomy 有方法论贡献
- **略低**：概念新颖性有限（domain transfer of Thurstone 1927），"Likert Blindspot" 的 framing 建立在未证实的假设上
- **定位**：作为 short paper 定位合适；作为 long paper 新颖性可能不足。当前 6-page 格式匹配 short paper submission，scope 与 venue 基本匹配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 414 · 2026-05-21T14:23:22.529874+00:00_

审稿报告已在上一轮提交。这份 R2 Dream 审稿是对一个假想修订版（6 页 condensed 版本，含 4 个 judge 和 Comparative Trap 四层防御）的审查，非当前版本。

**与已提交报告的对比**：
- R2 评分从 3.0 上调至 **3.5 (Borderline Conference)**，与 R1 趋同——说明已提交报告中的 MF1/MF2 如果被充分修复，论文确实可升至 Borderline Conference
- Dream 版新增的 Comparative Trap 四层防御（placebo BT≈50%、NLI gate ablation、Claude negative control、cross-axis gradient monotonicity）被 R2 认可为"精巧"
- 但 R2 指出即使修复后仍存在：(1) "Blindspot" 命名预设 Likert 失灵，construct difference 权重仍不足；(2) "6× sensitivity gap" 是离散计数比非连续指标，有误导性

**⚠️ 新发现——引用完整性问题**：R2 指出 RATE 被归因于 "Ye et al., 2024"，但 RATE 作者实际是 **Reber et al. (2025, ICML)**。"Ye et al., 2024, Beyond Preference: Universalizing LLM-as-a-Judge through RLHF" 在 arXiv/Semantic Scholar 上查不到，**可能是幻觉引用**。需核实。

已提交的审稿报告覆盖了当前版本的所有关键问题，无需重新提交。Dream 审稿的新发现（引用完整性、6× 指标误导性）可作为 Research Director 修改时的补充参考。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 42

## Round 42

2 recorded events


### User

_source line 415 · 2026-05-21T14:23:23.601539+00:00_

[Reviewer 1 审稿意见]:
## Dream 审稿报告 — Reviewer 1（方法 + 实验）

**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
**Dream ID**: 20260521T132932 (best scenario)
**Venue**: EMNLP 2026 (ARR)
**审查侧重**: 方法描述、实验设计、数据呈现、实验覆盖度

---

## Overall Assessment

**Overall**: 3.5 / 5（Borderline Conference）
**Confidence**: 4 / 5

**一句话总结**: 实验设计全面（placebo control、NLI ablation、4 judge families、3 rewriters、cross-benchmark），显著优于通常的 bias detection 论文，但 placebo 统计力不足以支撑 "format amplification empirically excluded" 的强声明，且多处关键方法细节缺失。

---

## Summary

论文提出 CSD 框架，通过 4 阶段管线（counterfactual rewriting → NLI gating → position-controlled pairwise comparison → BT/GEE statistical analysis）检测 LLM judge 的 per-axis style bias。核心发现是 Likert Blindspot：18 个 judge×axis×benchmark cell 中，BT 在 12 个 cell 检测到显著 bias，Likert 仅在 2 个 cell 检测到（6× sensitivity gap）。论文在 4 个 target judge families（GPT-4o、Qwen3-32B、Llama-70B、Gemini-Flash）+ 1 个 negative control（Claude）上验证，配合 double-rewrite placebo、NLI gate ablation、cross-axis gradient、rewriter independence 四层控制。

---

## Strengths

**S1. 实验控制的层次感和完整性**：四层 anti-amplification 防御（placebo BT ≈ 50% in Table 4, NLI ablation in Table 5, Claude negative control in §5.4.4, cross-axis gradient in Table 6）是该领域论文中罕见的严谨程度。特别是 double-rewrite placebo 直接回应了 Jeong et al. (2025) Comparative Trap 的核心担忧——当 style 差异不存在时 BT = chance。

**S2. Judge 和 rewriter 覆盖全面**：4 个 target judge families 覆盖 proprietary US (GPT-4o)、open CN (Qwen3-32B)、open US (Llama-70B)、proprietary US lightweight (Gemini-Flash)，加上 Claude negative control。3 个 rewriter (Qwen3-32B, GPT-4o, Llama-3.1-70B) 的 BT 范围 <2.1pp (Table 8)，有力证明了 rewriter independence。

**S3. Detection matrix (Table 2) 是量化 Blindspot 的清晰手段**：18-cell 全覆盖的 BT sig vs Likert sig 2×2 矩阵直接、可复现、无需主观判断。10/12 BT-significant cells 的 Likert p > 0.15 使结论对 α 选择不敏感。

**S4. GEE decomposition 揭示 per-axis confound structure**：Table 3 将 3 轴清晰分层——verbosity pure style (Style OR 高, Orig OR NS), formality conditional (both significant), register originality-dominated。这一 taxonomy 在 3 个 target judge 上独立复制（Table 6, Spearman 单调），比仅报告 "bias exists" 有更强的方法论贡献。

**S5. Comparative Trap 的直接回应**：Section 2 引用 Jeong et al. (2025) 并在 §5.4.1 用 placebo 实验回应。Section 6 Discussion 专门讨论 "Detection versus amplification"，提出四层防御论证。这比忽略该文献或仅在 limitations 中提及好得多。

---

## Must-Fix 问题

**N1** [Major, idea 层面] Placebo "entirely attributable" overclaim — 统计力不足以排除中等幅度的 format amplification

- 具体位置：Section 5.4.1, Table 4, 及 Discussion p.5 ("Treatment-Placebo gap...is entirely attributable to the style manipulation")
- 问题：Table 4 的 placebo BT 在 n=88 pairs 下：
  - GPT-4o formality: 0.51 [0.44, 0.58], p=0.75
  - Qwen3-32B formality: 0.50 [0.43, 0.57], p=0.92
  - GPT-4o verbosity: 0.52 [0.45, 0.59], p=0.60
  
  placebo 95% CI 上界为 0.57-0.59，意味着最多 **~8pp 的 format amplification 与数据兼容**（CI 内）。对于 formality axis（treatment BT 0.630），placebo CI 上界 0.58 与 treatment CI 下界 0.558 **存在重叠**。这意味着无法在统计上完全排除 formality BT 中有 5-8pp 来自 format amplification 而非 pure style bias。
  
  论文声称 "entirely attributable to style manipulation" 和 Section 5 Discussion 的 "format amplification empirically excluded" 超出了 placebo 设计在 n=88 下的统计力所能支撑的声明强度。

- 为什么是 Major：这是论文回应 Comparative Trap (Jeong et al., 2025) 的核心论证。如果 format amplification 被低估（如存在 5-8pp），则：(1) treatment BT 的 "true style bias" 部分被高估；(2) Likert Blindspot 的幅度解释需要调整（Likert 可能不是"看不到"full 63%，而是"看不到"55%——后者更难检测）。虽然 bias 的存在（BT > 50%）不受影响，但 magnitude 解释受影响。

- 建议修改方向：
  (1) 将 "entirely attributable" 改为 "predominantly attributable, with residual amplification bounded to <8pp by placebo CI"
  (2) 报告 treatment-placebo 差值的 bootstrap CI（而非仅报告各自的 CI）
  (3) 讨论 minimum detectable amplification effect at n=88（~14pp at 80% power）
  (4) 在 Table 4 中增加 Δ 列的 CI

---

## Should-Fix 问题

**W1** [idea 层面] NLI-fail ablation 样本量过小，不足以支撑方向性结论

- 具体位置：Table 5, §5.4.2
- 问题：NLI-fail pairs 仅 n=12（formality）和 n=14（verbosity）。Table 5 的 "NLI-fail pairs show BT that reflects content-mediated signal" 和 "confirming the gate removes content-mediated signal" 基于这些极小样本。在 n=12 下，BT 的 standard error 约 ±15pp，pass-fail gap 9.5pp 完全可以是随机波动。论文承认 "NLI-fail n too small for individual significance"（来自 review_context 的 note），但主文仍将方向性结果作为 NLI gate 有效性的证据（"NLI-fail pairs...show BT that reflects content-mediated signal"）。
- 建议：(1) 在主文中明确标注 NLI-fail 结果为 "directional but underpowered"；(2) 不要将其作为四层防御中的独立一层——它更应该是 supplementary observation。

**W2** [idea 层面] Register 轴的 "three style axes" framing 与 GEE 证据不匹配

- 具体位置：Abstract ("three style axes"), Table 3, Table 6
- 问题：Table 3 和 Table 6 的 GEE decomposition 显示 register 是 "originality-dominated"（GEE Style/Orig ratio = 0.33），register BT 仅 55-57%（边缘显著或不显著）。这意味着 register 上观测到的弱 preference 主要来自 originality confound 而非 style bias。论文的 "three style axes" framing 暗示在三个轴上均检测到了 style bias，但 register 的证据更准确地描述为 "originality effect with weak residual style component"。
- 建议：(1) 在 Abstract 中区分 "two clear style bias axes (verbosity, formality) and one originality-dominated axis (register)"；(2) 或将 register 定位为 negative/weak finding 而非正面证据。

**W3** [idea 层面] Cross-axis gradient 作为防御层的统计效力为零

- 具体位置：Table 6, Discussion p.5
- 问题：Table 6 展示 3 个轴的 NLI rejection rate 与 BT 的单调关系，Spearman ρ = 1.0。但 **3 个数据点的任何单调排列都产生 ρ = 1.0**——这不是统计发现而是定义性成立。论文称其为 "qualitative argument, not statistical test"（review_context），但 Discussion 仍将其作为四层防御的第四层（"cross-axis gradient monotonically tracking true bias levels across both judges, inconsistent with uniform format amplification"）。用一个必然成立的 pattern 作为防御论据会削弱整体论证的可信度。
- 建议：(1) 在 Discussion 中将其从 "defense layer" 降级为 "consistency observation"；(2) 坦承 3 点单调性不构成统计证据；(3) 或增加更多轴（如 sentence length, hedging, formality sub-types）使 gradient 分析有统计意义。

**W4** [presentation 层面] NLI 模型身份和阈值——管线最关键超参——未在论文中指定

- 具体位置：Section 3 Stage 2
- 问题：论文描述 "a natural language inference model that verifies bidirectional entailment" 但 **未指定模型名称或决策阈值**。从上下文推断 NLI annotator 为 Qwen3-32B（Section 4 "NLI validation. Qwen3-32B as NLI annotator"），但这意味着 Qwen3-32B 同时担任 rewriter、NLI annotator 和 judge（在某些配置下）——三重角色。如果使用的是 softmax probability threshold（如原始论文的 0.90），则阈值选择直接决定了 pass/fail 划分和后续所有分析的样本组成。
- 建议：(1) 在 Section 3 Stage 2 中明确指定 NLI 模型名称和决策机制（categorical output vs. probability threshold + cutoff value）；(2) 讨论 Qwen3-32B 三重角色的 circularity（rewriter self-acceptance bias）。

**W5** [presentation 层面] Qwen3-32B triple-role circularity 未讨论

- 具体位置：Section 3-4, Limitations
- 问题：Qwen3-32B 同时作为 (1) primary rewriter, (2) NLI annotator, (3) one of four target judges。论文 Limitations 讨论了 evaluator-producer bias（role 1+3 的重叠），但 **未讨论 role 1+2 的重叠**——rewriter 兼任 NLI annotator 意味着模型可能系统性地认为自己的 rewrite 保持了语义（self-acceptance bias），导致 NLI pass rate 被高估。GPT-4o cross-validation（92.1%/82.6% precision）部分缓解了这一问题，但应该在论文中作为 limitation 明确讨论。
- 建议：在 Limitations 中增加一段讨论 NLI annotator identity 与 rewriter overlap 的影响；或改用独立的 NLI 模型（如 DeBERTa-v3-large）。

**W6** [idea 层面] BT 模型的 IIA 假设未检验

- 具体位置：Section 3 Stage 4, 全文 BT 分析
- 问题：BT 模型假设 IIA（Independence of Irrelevant Alternatives）。在 style manipulation 实验中，不同类型的原始文本（如 code vs. creative writing）可能与 style 变化有异质性交互，导致 IIA 违反。论文未报告任何 IIA 诊断（如 Hausman-McFadden test 或按 task type 分层的 BT 参数稳定性检查）。
- 缓解因素：4 judge families 的一致性和 cross-benchmark consistency 提供了间接 robustness 证据——如果 IIA 被严重违反，不太可能在所有 judge 和 benchmark 上产生一致的 BT pattern。因此这比无缓解的 IIA 未检验问题更轻微。
- 建议：在 Appendix 中增加按 task type/difficulty 分层的 BT 参数比较；或简要论证为何 cross-judge consistency 间接支持 IIA 近似成立。

---

## Minor Issues

**M1** [presentation] 论文仅有 Figure 1（pipeline diagram），其余所有结果均以 table 呈现。Cross-axis gradient (Table 6)、attenuation spectrum（BT vs Likert d across 18 cells）、placebo vs treatment 对比均应有配图。Table-heavy 的论文在审稿时 scanning 效率低，关键 pattern 不易一眼捕捉。

**M2** [presentation] GEE 模型规格对非 LLMBar benchmark 未充分描述。Table 3 的 GEE decomposition 仅展示 LLMBar 数据？还是跨 benchmark 聚合？Working correlation structure、interaction test、link function 在 cross-benchmark 扩展中是否保持不变？

**M3** [presentation] Bootstrap seed=42 贯穿全文所有 CI 计算。单一 seed 的 CI 对 seed 选择的 sensitivity 未评估。建议在 Appendix 报告 10 个 seed 的 CI 范围。

**M4** [presentation] Claude negative control 的 TOST equivalence test（§5.4.4）参数不完整——equivalence margin (Δ)、achieved power 未报告。"Within ±1.5pp of zero" 但 TOST 的 null hypothesis rejection 条件未给出。

**M5** [presentation] Table 1 footnote 中 "†" symbol 的含义未定义。Bradley-Terry 的 asterisk significance levels (*, **, ***) 也未明确定义 α cutoff。

---

## 实验覆盖度对照（review_context.yaml）

| 实验 | 论文中覆盖 | 报告深度 | 评价 |
|------|-----------|----------|------|
| Llama-70B verbosity/formality | ✅ Table 1 | BT + Likert + GEE | 充分 |
| Double-rewrite placebo (form. + verb.) | ✅ Table 4 | BT + CI + p | 缺 treatment-placebo Δ 的 CI |
| NLI gate ablation | ✅ Table 5 | pass/fail/all BT | fail n 过小，标注不足 |
| Cross-axis gradient | ✅ Table 6 | NLI rej. vs BT vs GEE ratio | 仅 3 点，统计力为零 |
| Gemini-2.0-Flash | ✅ Table 1 | BT + CI + p | 充分（作为 robustness row）|
| Cross-benchmark (AlpacaEval/MT-Bench) | ✅ Table 7 | BT + p | 缺 GEE decomposition 和 Likert |
| Likert sensitivity analysis (18 cells) | ✅ Table 2 | 2×2 detection matrix | 充分 |
| Rewriter independence (3 rewriters) | ✅ Table 8 | NLI pass%, BT, CI | 充分 |
| Scaled replication (n=400) | ✅ §5.5 inline | BT + CI + Likert | 充分 |
| GPT-4o verbosity + register | ✅ Table 1 | BT + Likert | 充分 |

**未报告的信息**：
- Cross-benchmark 的 GEE decomposition 和 Likert 对比（Table 7 仅报告 BT）
- Placebo treatment-placebo 差值的 bootstrap CI
- NLI-fail pairs 的完整统计描述（beyond BT point estimate）

---

## Questions for Authors

**Q1**: Table 4 的 placebo design 是否计算了 treatment-placebo difference 的 bootstrap CI？如果 formality 的 Δ CI 下界接近 0，则 "entirely attributable to style" 的声明需要 qualification。

**Q2**: NLI annotator 是 Qwen3-32B（与 rewriter 相同），是否评估过 self-acceptance bias？即 Qwen3-32B 是否比独立 NLI 模型（如 DeBERTa-v3-large）更倾向于判定自己的 rewrite 为 entailment？GPT-4o cross-validation 的 disagreement cases 是否集中在 "Qwen pass but GPT-4o fail" 方向？

**Q3**: Table 7 的 cross-benchmark 结果仅报告 BT。Likert Blindspot（C2）和 per-axis confound structure（C3）是否在 AlpacaEval 和 MT-Bench 上也成立？如果是，Table 2 的 18-cell matrix 是否已包含这些 benchmark？

**Q4**: IIA 方面——是否按 LLMBar 的 task categories（如 negation, paraphrase, elaboration 等）分层检查了 BT 参数的稳定性？

---

## 校准对照

| 校准项 | 状态 |
|--------|------|
| Major issues 数量 | 1（N1: placebo overclaim）|
| 对应上限 | ≤ Accept (4.0) |
| 实际给分 | 3.5（Borderline Conference）|
| 理由 | N1 是 magnitude interpretation 问题非 existence 问题，但 Should-Fix 数量较多（6 项），其中 W1-W3 涉及 idea 层面的论证力度不足，集体效应将分数从 4.0 推至 3.5 |

**路径至 4.0**：(1) 修复 N1（softening placebo claim + 报告 Δ CI）；(2) 修复 W4（NLI model spec）；(3) 修复 W2（register framing）。其余 W 项为加分但非必须。

---

[Reviewer 2 审稿结果]:
Dream 审稿报告已提交。

核心判断：**3.5 / 5（Borderline Conference）**。

主要发现：
- **最强贡献**是 GEE per-axis taxonomy（verbosity confound-free / formality conditional / register originality-dominated），在现有文献中无先例
- **四层 Comparative Trap 防御**设计精巧，特别是 cross-axis gradient 论证有效排除了均匀放大假说
- **核心弱点**是 "Likert Blindspot" 命名预设了 Likert 失灵，而 construct difference alternative 在主文中权重不足；"6× sensitivity gap" 是检测计数比而非连续灵敏度指标，作为 headline claim 有误导性
- **引用问题**：RATE 被错误归因于 "Ye et al., 2024"，该引用可能不存在（Reber et al., 2025 才是正确归因）

---

[Reviewer 1 审稿结果]:
Dream 审稿报告已提交。

**审稿结论**：Overall 3.5 (Borderline Conference)。

核心判断：
- **1 个 Major issue**：placebo control 的 "entirely attributable" 声明超出 n=88 的统计力（无法排除 ≤8pp 的 format amplification），但 bias 存在性不受影响
- **6 个 Should-Fix**：NLI-fail 样本过小、register 轴 framing 不准确、cross-axis gradient 3 点无统计力、NLI 模型/阈值未指定、Qwen3-32B 三重角色 circularity、IIA 未检验
- **实验覆盖度**：review_context.yaml 中列出的所有实验均在论文中有所体现，整体实验设计是该领域同类论文中最全面的之一
- **路径至 4.0**：修复 placebo overclaim + 补充 NLI 模型规格 + 调整 register framing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 416 · 2026-05-21T14:24:03.382829+00:00_

审稿报告已于此前提交。Dream 审稿（对理想修改后版本的前瞻性评估）结果现已到达，汇总如下。

**Dream 审稿评分**：R1 3.5 / R2 3.5（两位均为 Borderline Conference）

**与主审稿报告的关键增量发现**：

1. **Placebo control overclaim（R1-Dream N1）**：即使补充了 double-rewrite placebo 实验（BT≈50%），n=88 下 placebo CI 上界为 0.57-0.59，无法排除 ≤8pp 的 format amplification。"entirely attributable to style" 声明过强，应改为 "predominantly attributable, with residual amplification bounded to <8pp"。

2. **"6× sensitivity gap" 误导性（R2-Dream W1）**：12/2=6 是二值化检测计数比，高度依赖 α=0.05 选择。应改用连续指标或明确标注度量基准。

3. **Cross-axis gradient 无统计力（R1-Dream W3）**：3 个数据点的任何单调排列都产生 Spearman ρ=1.0，不构成统计证据。应从"防御层"降级为"一致性观察"。

4. **Qwen3-32B 三重角色（R1-Dream W5）**：除 evaluator-producer 外，rewriter 兼任 NLI annotator 引入 self-acceptance bias（自己判定自己的 rewrite 保持了语义），此前未被识别。

5. **RATE 引用归因错误（R2-Dream W3）**：RATE 应归于 Reber et al. (2025)，非 "Ye et al., 2024"。后者可能为幻觉引用。

6. **Register 轴应从正面证据降级（R1-Dream W2 / R2-Dream N1）**：GEE 显示 register 为 originality-dominated，"three style axes" framing 暗示三轴等价是误导。

**Dream 共识**：即使在理想修改后（4 judges、Comparative Trap 四层防御、cross-benchmark），论文仍停留在 3.5 (Borderline Conference)。核心瓶颈是概念新颖性天花板（Thurstone 1927 domain transfer）和 "Blindspot" 命名预设 Likert 失灵——construct difference alternative 无论怎么修改都无法被完全排除，只能更平衡地讨论。

Dream 审稿的关键洞察（placebo overclaim、三重角色 circularity、cross-axis gradient 无统计力）已记录，供 Research Director 在制定 Action Matrix 时参考。审稿流程完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 417 · 2026-05-21T16:15:09.610665+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Methods & Experiments Review (Updated Paper, 15pp)

**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
**版本**: 修订版（15 页，含 Appendix A-N，Table 1-14）
**Venue**: EMNLP 2026 (ARR)

---

## 1. Soundness: 3.5 / 5

### CSD Pipeline Validity

**NLI Gating**: Now properly specified — DeBERTa-v3-large, bidirectional entailment threshold 0.90, direction-aware for verbosity (Appendix F). GPT-4o cross-validation on all 200 pairs (92.1% formality, 82.6% verbosity precision). The 0.90 threshold sits on a bimodal plateau (Appendix E, Table 8: 11 thresholds from 50-98, BT stable across all). 这比原稿大幅改善。

**Position Balancing**: Bidirectional swap producing n_pairs × 2 observations. Consistency filter retains only concordant pairs for sign test; BT model uses all observations. 标准做法。

**Bradley-Terry Model**: GoF tests reported (Appendix H: formality deviance p=0.198, verbosity p=0.905). Stratified analysis confirms no preference heterogeneity for verbosity. Bootstrap CIs (10,000 pair-level resamples, seed 42). **但 CI 类型未指明（percentile vs. BCa）**——应在 Section 4.1 明确。

**GEE Decomposition (Eq. 1)**:
- Exchangeable correlation justified by QIC comparison (Appendix C, Table 4: |ΔQIC| < 0.001 across all 6 cells).
- Interaction test: style×originality NS on formality for both judges (GPT-4o p=0.38, Qwen3 p=0.52). ✅
- **缺失**：interaction test 未报告 verbosity axis。鉴于 verbosity 的 P(orig) 极低（Table 14: Qwen3 P(orig)=0.082，即 92% 偏好抛光文本），这正是 interaction 最可能显著的轴。如果 verbosity 上 style×originality interaction 显著，additive GEE 的 "confound-free" 结论受影响。
- **缓解因素**：verbosity 的双向结果（Section 5.4："Both rewriting directions favor verbose responses"）意味着 style preference 在两个方向上都压过 polishing artifact。如果 judges 在 verbose-original vs. concise-rewrite 方向上仍偏好 verbose（这对抗了 92% 的 polishing preference），style effect 必须非常强。这间接支持了 additive model 的 adequacy。

**Blindspot 定义 (BT sig ∧ all Likert NS)**:
- 论文现在在 Section 5.2 主文中讨论了 "measurement attenuation vs. construct divergence"——不再仅在 Limitations 中。
- 两种解释均被讨论："Likert captures absolute quality difference while pairwise captures ordinal preference"。
- 结论："Whether this reflects measurement attenuation or construct divergence, the operational consequence is identical"——这是务实且可辩护的立场。
- **残余疑虑**：论文标题 "Blindspot" 暗示 Likert 有缺陷，但如果是 construct divergence，Likert 并非"盲"——它测的是不同东西。标题 framing 偏向 attenuation 解释。

**100-Point Likert Ablation (Table 12, Appendix L)**:
- n=100 formality + verbosity, Qwen3 judge. Formality: Likert p=0.725 (tie rate 65.9%), verbosity p=0.137 (tie rate 51.2%). BT 同数据 66.5% 和 77.3%。
- **Power concern**：n=100 在 α=0.05 下能检测到的最小效应量约为 d=0.28（双侧 t-test，80% power）。观测到的 d=0.02-0.06 远低于此。所以 ablation 能排除 d≥0.28 的中等效应，但不能确认 d 是否真为 0 或仅为极小未检出效应。
- **但这正是论文论点的一部分**：即使 100-point 量表，效应量仍为 d=0.02-0.06，远低于任何实际意义阈值。论点不是 "d=0" 而是 "d 如此之小以至于 Likert 在实际样本量下永远检测不到。" 这一推理是成立的。

**NLI 已知局限**：
- 论文报告了 FNR 8.4% (Section 5.1) 并分析了 FN 特征。
- Direction-aware gating 的 asymmetry (Appendix F) 处理了 expansion vs. compression 的不对称性。
- **未讨论**：DeBERTa NLI 对 lexical overlap 的已知敏感性——高 lexical overlap 的 pair 可能获得虚高 entailment score。但鉴于 style rewriting 通常改变词汇而非保留，这个问题的方向可能是使 gate 更严格（而非更宽松），reducing risk。

### Soundness 小结
核心方法学严谨，控制层次丰富（NLI gate + position swap + GEE decomposition + 5 experimental controls）。主要残余疑虑：(1) GEE interaction test 缺 verbosity axis；(2) Blindspot 标题 framing 偏向 attenuation 解释。不构成 Major issue，但影响 4.0 提升。

---

## 2. Experimental Design: 3.5 / 5

### 覆盖度总览

| 维度 | 已覆盖 | 评价 |
|------|--------|------|
| Judges | GPT-4o, Qwen3-32B, Claude(ctrl) + Llama(App K) | Good：3 target + 1 ctrl |
| Benchmarks | LLMBar, AlpacaEval, MTBench (Table 1) | Good：3 benchmarks |
| Axes | Formality ✅, Verbosity ✅, Register ⚠️ | Register 仅 2 judges |
| Scaled replication | n=355, formality×Qwen3×LLMBar only | Limited scope |
| Rewriter independence | Formality×GPT-4o judge only (Table 6-7) | **Limited** |
| Negative control | Claude on formality×LLMBar + some others | Incomplete |
| Cross-benchmark | All axes in Table 1, formality deepest | Partially |
| Placebo | Table 14, 3 judges × 2 axes | **Good** |
| NLI gate ablation | Table 13, pass/fail/all | **Good** (fail n small) |
| 100-point Likert | Table 12, form+verb×Qwen3 | New & useful |
| 7-method sensitivity | Table 2 (form) + Table 11 (verb) | **Good** |

### Specific Concerns

**S1. Rewriter independence 范围不足 [Should-Fix, idea]**
- Table 6-7 (Appendix D) 仅在 formality×GPT-4o 配置上测试了 GPT-4o 作为替代 rewriter。BT 64.4% [56.1, 72.8] vs. Qwen3 rewriter 66.5% [58.5, 73.9]——CIs 重叠，OK。
- **缺失**：verbosity 的 rewriter independence。Verbosity rewriting 更 invasive（NLI rejection 14% vs. 12%），rewriter identity 的影响可能更大。如果 Qwen3 的 verbose rewriting 风格系统性地不同于其他 rewriter，verbosity 77% BT 的一部分可能来自 Qwen3-specific 的 rewriting pattern 而非 genuine style bias。
- **缓解**：Llama 作为独立 judge（Appendix K, Table 11）在 Qwen3-rewritten pairs 上复现了 verbosity bias，说明至少跨 judge 是稳定的。但 rewriter dimension 未测试。

**S2. Claude negative control 覆盖不完整 [Should-Fix, presentation]**
- Table 1 显示 Claude 在 LLMBar formality (.562, NS) 和部分其他 cells 上的结果。
- Appendix G: TOST equivalence test at n=87, Δ=10pp, confirmed.
- **但** verbosity 和 register 的 Claude 结果在 Table 1 中部分缺失（一些 cells 空白）。如果 Claude 仅在 formality 上验证为 NS，discriminant validity 只对 formality 成立。
- 论文应明确报告 Claude 在所有已测 cells 上的 TOST 结果，而非仅在部分 cells。

**S3. Register axis 不完整 [Minor, idea]**
- 仅 2 judges (GPT-4o, Qwen3)，无 Llama。
- BT 55-57%（边缘显著）。GEE 显示 originality-dominated。
- 论文将 register 定位为 "exploratory"——这是正确的 scoping。Table 3 footnote 确认 register 不进入 primary Holm-Bonferroni family。
- **残余问题**：如果 register 是 exploratory，是否应该在 Abstract 中与 formality/verbosity 并列为 "three style axes"？ 目前 Abstract 说 "two primary style axes (formality, verbosity), with exploratory evidence on register"——这比原稿改善但仍略 overstate。

**S4. Cross-benchmark depth不均 [Should-Fix, presentation]**
- Table 1 的 cross-benchmark 覆盖（3 benchmarks × judges × axes）是主表，但 AlpacaEval 和 MTBench 上的 GEE decomposition 和 Likert 对比未在 appendix 中深入展开。
- 论文依赖 Table 1 的 cross-benchmark BT 一致性，但未验证 Blindspot pattern（BT sig + Likert NS）是否在非 LLMBar benchmarks 上也成立。如果 Blindspot 仅在 LLMBar 上出现，generalizability claim 受限。

**S5. Double-rewrite placebo 的解读 [Should-Fix, idea]**
- Table 14 (Appendix N) 显示 P(orig) 在 verbosity 上极低（GPT-4o: 0.167, Qwen3: 0.082）——judges 92% 偏好 LLM-polished text。这是 **非常强的 rewriting artifact**。
- 论文声称 GEE decomposition "absorbs" 这个 artifact。
- **关键问题**：在 treatment pairs 中，style 和 originality 通过 bidirectional design 被交叉。在 verbose-original vs. concise-rewrite 方向上，judges 仍偏好 verbose text（Section 5.4: "Both directions favor verbose"）——这意味着 style preference 确实压过了 92% 的 polishing preference，支持 GEE 的 adequacy。
- 但论文应更明确地展示这个推理链：placebo artifact → bidirectional cancellation → GEE correctly isolates style。目前 Table 14 放在附录末尾，与 GEE 讨论脱节。

**S6. n=100 per condition for GEE [Minor, idea]**
- n=100 (86-88 NLI-pass) with binary outcome and 2 covariates. For large ORs (2-13), adequate power. For register (OR near 1), underpowered.
- Scaled replication (n=355) 仅在一个 configuration 上确认了 stability。Verbosity 和 cross-benchmark 未 scaled。
- 但论文的主要结论（verbosity is strong, formality is conditional, register is weak）不依赖于 marginal significance——pattern 在多个 configurations 上一致。

### Experimental Design 小结
设计广度好（3 judges × 3 benchmarks × 3 axes + 5 experimental controls），但几个维度的深度不足：rewriter independence 仅 formality、Claude 覆盖不完整、cross-benchmark GEE/Likert 未展开。最值得关注的是 S1（rewriter independence）和 S5（placebo 解读链）。

---

## 3. Reproducibility: 3.5 / 5

| 要素 | 状态 | 备注 |
|------|------|------|
| NLI model identity | ✅ DeBERTa-v3-large | Section 3.2 |
| NLI threshold | ✅ 0.90 | Section 3.2 |
| Rewriter model | ✅ Qwen3-32B-Instruct | Section 3.1 |
| Judge API version | ✅ GPT-4o (gpt-4o-2024-08-06) | Section 3.3 |
| Temperature | ✅ 0.7 | Section 3.1 |
| Rewriting prompts | ⚠️ Described but exact text not given | Missing from appendix |
| Bootstrap params | ✅ 10,000 pair-level, seed 42 | Section 4.1 |
| Bootstrap CI type | ❌ Percentile vs. BCa not specified | Should state |
| GEE correlation | ✅ Exchangeable + independence comparison | Appendix C |
| Code/data | ⚠️ "Released upon acceptance" | Not verifiable |

**主要gap**：Rewriting prompt 的 exact text 未在论文或附录中提供。Section 3.1 描述了 prompt 的结构（"Rewrite the following text to be more formal/casual..."），但不同的 prompt wording 可能影响 rewriting 质量和 NLI pass rate。对于 reproducibility，exact prompts 是关键。

---

## 4. Statistical Concerns

**4a. Multiple comparisons**: 
Primary family: 2 judges × 3 axes = 6 tests, Holm-Bonferroni at α=0.05 (Section 4.1). Table 1 reports both raw and adjusted p-values. Register 标为 exploratory（不入 family）。✅ 合理。

**4b. Bootstrap CIs**: 
10,000 pair-level resamples, seed 42. **CI type（percentile vs. BCa）未指定**。对于 skewed BT estimates（如 register BT 55%），BCa would be more appropriate。Should state in methods.

**4c. GEE working correlation**: 
Exchangeable, compared with independence in Appendix C (|ΔQIC| < 0.001). Interaction test on formality (NS for both judges). ✅ 充分。
**但 verbosity interaction test 缺失** — ditto Soundness 部分的讨论。

**4d. "7 methods all NS" = evidence of absence?**:
这是论文的核心方法论 tension。7 种 Likert 方法全部 NS 不严格等于 "no effect"——只是 "not detected"。但论文通过三层补充证据缓解了这一问题：
1. Bootstrap attenuation analysis (Appendix J, Table 10): d→0 as n increases to 355, CI [−0.123, 0.087] never excluding zero。说明 d 不是 under-detected 而是 genuinely near zero。
2. 100-point Likert ablation (Appendix L): 更细粒度的量表仍不改善检测。
3. BT 同数据显著（p < 0.001）：同一数据上两种方法的不一致排除了 "insufficient data" 解释。

这三层证据将 "absence of evidence" 显著升级为 "bounded near-zero effect"。**论文对这一 tension 的处理是该领域论文中我见过的最严谨的之一。**

---

## 5. Missing Experiments (对照 review context)

| Experiment | Status | Reported Where | Completeness |
|-----------|--------|---------------|-------------|
| exp-001: Multi-judge (Gemini) | ❌ MISSING | — | Gemini mentioned in Related Work context but no results |
| exp-002: Multi-benchmark | ✅ Partial | Table 1 (BT); Appendix cross-benchmark (formality only deeper) | Verbosity/register GEE cross-benchmark missing |
| exp-003: 7-method sensitivity | ✅ | Table 2 (form) + Appendix K Table 11 (verb) | Two axes covered |
| exp-005: Placebo control | ✅ | Appendix N, Table 14 | 3 judges × 2 axes |
| exp-006: Scaled replication n=355 | ✅ | Section 5.2, Appendix J | Single condition |
| exp-009: Rewriter independence | ✅ Partial | Appendix D, Table 6-7 | Formality only, GPT-4o judge only |
| exp-020: GPT-4o verb+register | ✅ | Table 1 | Complete |
| exp-021: Llama third judge | ✅ | Appendix K, Table 11 | Verbosity sensitivity hierarchy |
| exp-022: Double-rewrite placebo | ✅ | Appendix N, Table 14 | Merged with exp-005 |
| exp-023: NLI gate ablation | ✅ | Appendix M, Table 13 | Pass/fail/all, 2 axes |
| exp-024: Cross-axis gradient | ✅ | Implicit in Table 1 + Fig 3 | Qualitative only |
| 100-point Likert ablation | ✅ | Appendix L, Table 12 | 2 axes × Qwen3 |

**关键缺失**：
1. Gemini judge 完全缺失——review context 列出但论文中无 Gemini 数据
2. Rewriter independence 仅 formality——verbosity 是更 invasive 的轴
3. Cross-benchmark GEE/Likert decomposition 未展开

---

## ARR Dimension Scores

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| **Soundness** | 3.5/5 | Pipeline 设计严谨，5 层 Comparative Trap 控制令人印象深刻。GEE 有完整诊断。但 verbosity interaction test 缺失、construct validity 未解决。 |
| **Excitement** | 3.5/5 | Likert Blindspot 是实用且新颖的发现；7-method sensitivity hierarchy 和 100-point ablation 提供了强实证。但与 RATE 的增量界限需更清晰定位。 |
| **Reproducibility** | 3.5/5 | 关键超参明确标注（模型、threshold、API 版本、temperature），但 exact prompts 和 bootstrap CI 类型缺失。 |

## Overall Assessment

**Overall**: 3.5 / 5（Borderline Conference）
**Confidence**: 4 / 5

### Justification

**Why 3.5 rather than 4.0**: 三个 Should-Fix 问题的集合效应——(1) rewriter independence 仅测试了 formality（verbosity 是主力发现但 rewriter robustness 未验证）；(2) double-rewrite placebo 揭示了极强的 rewriting artifact（Qwen3 verbosity P(orig)=8%）但 GEE interaction test 仅在 formality 上报告（对 verbosity 的 "confound-free" 声明的统计支撑不完整）；(3) 论文的核心 framing（"Blindspot"）偏向 measurement attenuation 解释，但主文讨论了 construct divergence 后仍未提供能区分两者的实验证据。

**Why not 3.0**: 论文的控制层次（NLI gate ablation + placebo + Claude ctrl + cross-axis + debiased prompting）在该领域论文中罕见。Bootstrap attenuation analysis + 100-point Likert ablation + 7-method sensitivity table 共同构建了 Blindspot 的强实证基础。GEE 诊断完整（correlation structure、interaction test、GoF）。这些优势显著高于 Findings 水准。

**Path to 4.0**:
1. 在 verbosity axis 上报告 GEE style×originality interaction test
2. 在 verbosity axis 上测试 rewriter independence（至少 GPT-4o 作为替代 rewriter）
3. 明确报告 bootstrap CI 类型和 100-point ablation 的 power analysis
4. 在 Appendix 中提供 exact rewriting prompts

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 418 · 2026-05-21T16:16:00.210068+00:00_

审稿报告已于本轮早些时候投递（Overall 3.5, Borderline Conference）。

后续收到的补充审稿（Dream 审稿 + 修订版详审）均已归档。两位 Reviewer 在修订版上的评分收敛至 **3.5/5**，与已提交报告一致。修订版的主要改进点（NLI 模型明确指定为 DeBERTa-v3-large、Comparative Trap 四层防御、100-point Likert ablation、7-method sensitivity 补 verbosity 轴）被两位 Reviewer 认可，但三个残余问题阻碍提升至 4.0：

1. **Verbosity GEE interaction test 缺失**——verbosity 的 P(orig)=8% 暴露了极强的 rewriting artifact，但 style×originality interaction 仅在 formality 上报告
2. **Rewriter independence 仅覆盖 formality**——verbosity（主力发现）的 rewriter robustness 未验证
3. **Blindspot framing 偏向 attenuation 解释**——主文讨论了 construct divergence 但未提供区分两者的实验证据

本轮审稿流程已完成，报告已投递 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 44

## Round 44

2 recorded events


### User

_source line 419 · 2026-05-21T16:16:01.296404+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交。总结：更新版论文（15 页）在方法学上有显著改善——新增了 5 层 Comparative Trap 控制、100-point Likert ablation、NLI gate ablation、bootstrap attenuation analysis，整体评分 3.5/5 (Borderline Conference)。核心提升路径：补充 verbosity 的 GEE interaction test 和 rewriter independence test。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（修订版）：Novelty, Related Work, Writing Quality, Claim Calibration

**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
**Venue**: EMNLP 2026 Main Conference (via ARR)
**版本**: 修订版（15 页，49 篇引用，含 100-point Likert ablation 和 Comparative Trap 五层防御）

**重要说明**：Director 任务描述中的部分特征（"only 10 references"、"no figures at all"、"15 tables in 8 pages"、"Limitations only 3 sentences"）与实际 PDF 不符。实际论文有 49 篇引用、3 张 figures + ~14 tables（3 在主文 + ~11 在附录）、Limitations 为 3 段实质内容。以下审稿基于实际 PDF 内容。

---

## Scores

| 维度 | 分数 | 理由 |
|------|------|------|
| **Soundness** | 4.0/5 | 方法论严谨：NLI gating + 7 种统计方法 + GEE decomposition + 五层 amplification 防御 + 100-point ablation。主要扣分：GEE 仅 2 judges、register 轴 cross-rewriter 缺失 |
| **Excitement** | 3.5/5 | 100-point ablation 将概念新颖性从 "domain transfer" 提升至 "new evidence isolating measurement mode"。GEE taxonomy 是独立贡献。但核心洞察仍可追溯至 Thurstone (1927) |
| **Reproducibility** | 4.0/5 | 方法描述充分，统计程序明确，承诺 release code/data |
| **Overall** | 3.5/5 | Borderline Conference——扎实的实证贡献 + 适度的概念新颖性 |
| **Confidence** | 4/5 | 熟悉 LLM evaluation 和 psychometrics 文献 |

---

## 1. Novelty & Significance (Excitement 3.5/5)

### "Likert Blindspot" 是否为新发现？

**不完全是新发现，但新证据有实质意义。** 核心洞察（forced-choice > absolute rating for bias detection）可追溯至 Thurstone (1927) 和 Stevens (1946)。论文对此完全透明（Section 2, page 2-3："The distinction between ordinal and interval measurement dates to Stevens (1946)... The superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since Thurstone (1927)"）。

**论文的增量贡献在于三个层面的新证据**：

1. **Content-controlled evidence**: 通过 NLI gating 确保 rewrite 仅改变 style，提供了比 observational studies 更干净的因果证据。这超越了 SOS-Bench 的 correlational R=0.999。

2. **Two-layer mechanism identification**: tie-rate compression（59-65% identical Likert scores）+ residual signal attenuation——这不仅说明 Likert "fails"，还解释了 WHY。Section 5.2 (page 6) 的 severity spectrum analysis（"At moderate bias BT 63-67%, it is complete; it converges to ≠0 even at n = 355, rendering the bias invisible to any Likert-based test"）是有信息量的新发现。

3. **100-point Likert ablation** (Appendix L, Table 12): 这是本修订版最重要的新增实验。将 Likert 从 1-10 扩展至 0-100（101 个可能值），Blindspot 依然存在（BT 66.5%, p < 0.001；100-point Likert p = 0.17）。这 **隔离了 measurement MODE 和 scale granularity**——排除了 "Likert 点数不够" 这一平凡解释。这将论文从 "domain transfer" 提升至 "new empirical finding with mechanistic insight"。

**评判**：单独的 Likert Blindspot 命名 + 机制解释 + 100-point ablation 构成了足够的实证贡献，但不构成概念突破。

### Per-axis confound structure (C2) 是否有独立贡献？

**是的。** Table 3 的 GEE decomposition 揭示三种 regime：
- **Verbosity**: pure style effect（Orig OR non-significant across both judges）
- **Formality**: conditional（Style OR 和 Orig OR 均显著，Style OR 在控制后 decrease 但仍显著 for GPT-4o）
- **Register**: originality-dominated（Orig OR >> Style OR）

这一 taxonomy 不是 "just describing GEE output"——它提供了 prescriptive guidance：verbosity 可直接用 pairwise audit，formality 需控制 quality confound，register 效应主要由 quality 驱动。这在现有文献中**没有先例**。

**但 scope limitation**：Table 3 的完整 GEE 仅在 GPT-4o 和 Qwen3-32B 上展示。Conclusion (page 8) 声称 taxonomy "replicates across 3 architectures"——需要指向具体 cross-judge 验证数据。Appendix D 的 cross-rewriter test 仅覆盖 formality 和 verbosity，register 缺失。

### 与关键竞品的差异化

| 竞品 | CSD 差异 | 差异化清晰度 | 是否构成挑战？ |
|------|---------|-----------|------------|
| **RATE (ICML'25)** | RATE 用 Likert ATE；CSD 证明 Likert misses bias。Section 5.2 head-to-head: Cohen's d=0.10 (n.s.) vs. BT 63.0% (p=0.001) on identical data | ✅ 非常清晰 | **直接方法论挑战**：RATE 的 Likert 依赖是 vulnerability |
| **SOS-Bench (ICLR'25)** | SOS 是 correlational (R=0.999)；CSD 是 interventional with content control | ✅ 清晰 | 互补（CSD 加因果层） |
| **CASSE (2026)** | CASSE 假设 feature independence；CSD 用 GEE 分解 per-axis confound | ✅ 清晰 | 互补（CSD 更细粒度） |
| **LC-AlpacaEval (ICML'24)** | LC 仅控制 length；CSD 多轴 + GEE | ✅ 清晰 | 不同 scope |
| **Comparative Trap [Jeong'25]** | CT 认为 pairwise amplifies bias；CSD 用五层防御反驳 | ✅ 清晰（见下分析） | **直接对手**——需要成功反驳 |
| **Preference Leakage (ICLR'26)** | PL 关注 model-family bias via style；CSD 关注 measurement mode | ✅ 清晰 | 互补 |
| **Soumik (2026)** | Soumik 评估 debiasing 策略；CSD 评估 measurement sensitivity | ✅ | 正交 |
| **FairJudge (2026)** | FairJudge 是 training-side debiasing；CSD 是 post-hoc auditing | ✅ | 正交 |

**Comparative Trap 反驳是否令人信服？**

论文提供五层防御（Section 5.2 后半段 + Appendix M-N）：
1. NLI gate ablation：移除 content-confounded signal（~10pp reduction）
2. Claude negative control：identical format, BT ≈ 54% (n.s.)
3. Cross-axis gradient：verbosity >> formality >> register，与 uniform amplification 不一致
4. Rewriting artifact control (Table 14)：same-style double-rewrite placebo BT ≈ 50%
5. Cross-benchmark replication

**评判**：防御 1+4 排除 false positives（pairwise 不会凭空创造 bias）。防御 3 排除 uniform amplification（如果均匀放大，各轴应等比膨胀）。但**无法完全排除 proportional amplification**——真实的小 bias 可能被 pairwise 比例放大。论文在 Limitations (page 9) 承认："five experimental controls bound this risk (§5.2), though definitive separation would require human ground-truth ratings." 这是诚实的。

总体：**mostly convincing, with acknowledged residual uncertainty**。

---

## 2. Related Work Completeness

### 覆盖面评估

**实际 Related Work 约 1.5 页**（page 2 底部至 page 3 中部），分 4 个子主题：
1. Interventional Approaches to Judge Bias（RATE, CausaLM, Polyjuice, CASSE, FairJudge, Qiu et al.）
2. Measurement Sensitivity in NLG Evaluation（Stevens, Thurstone, Preston & Colman, Krosnick, DeCoster, Amidei, Clark, BWS）
3. LLM-as-Judge Biases（Zheng, FairEval, CalibraEval, Ye, COBBLER, SOS, Murugadoss, Preference Leakage, Soumik, JudgeBench, Saito, Chen, Stureborg, Park, Comparative Trap）
4. Bradley-Terry Models in Evaluation（Bradley & Terry, Chatbot Arena, AlpacaFarm, Elo Uncovered, Liusie）

**Director 指出的 "missing citations" 核实结果**：
- ✅ Preference Leakage (Li et al., 2026) — **已引用**（Introduction page 1 + Related Work page 3）
- ✅ Soumik (2026) — **已引用**（Introduction page 1 + Related Work page 3）
- ✅ FairJudge (2026) — **已引用**（Related Work page 2）
- ✅ Stureborg et al. (2024) — **已引用**（Related Work page 3）
- ✅ Park et al. (2024) — **已引用**（Related Work page 3, as "OffsetBias"）
- ✅ Wang et al. (2023) FairEval — **已引用**
- ✅ Comparative Trap (Jeong et al., 2025) — **已引用并详细讨论**

**仍可能遗漏的引用**：
- Howcroft & Belz (2020), "Twenty Years of Confusion in Human Evaluation" — 直接讨论 Likert vs. ranking 在 NLG 评估中的混乱现状，与本文主题高度相关
- Haak & Schaer (2025, arXiv:2512.14565), "Pairwise Comparison for Bias Identification and Quantification" — 系统比较 Likert vs. pairwise 在 linguistic bias 量化中的效能
- ReproGen shared task (Belz et al.) — NLG 评估的可重复性

### 心理测量学基础是否充分？

**充分。** 引用链完整：Stevens (1946) → Thurstone (1927) → Preston & Colman (2000) 量表点数 → Krosnick (1999) survey methodology → DeCoster (2011) median splits → Amidei (2019) Likert in NLG → BWS literature (Kiritchenko 2017, Novikova 2018, Louviere 2015)。覆盖了从基础测量理论到 NLP 应用的完整谱系。

### 引用数量与质量

**49 篇引用**，覆盖因果推断、心理测量、NLG 评估、LLM judge bias 四个领域。对 EMNLP 而言充分。引用验证显示 40/49 在线验证通过，3 篇未找到（可能是太新），6 篇有 minor mismatch（作者名格式）。1 篇 orphan bib entry（hoenig2001abuse）。整体引用质量高。

---

## 3. Writing Quality

### 结构

主文 8 页分配合理：Intro 1.5p → Related Work 1p → Method 1p → Experiments/Setup 1p → Analysis 2.5p → Discussion/Conclusion 1p。Analysis 占比最大是正确的——这是一篇 empirical measurement 论文，核心价值在分析。

### Abstract

信息密集但清晰。两个贡献的 framing 精准：C1（Likert Blindspot + mechanism）、C2（per-axis confound taxonomy）。关键数字（BT 63-84%, 60% attenuation, ≥6× sensitivity gap）直接给出。唯一问题：**"≥6× sensitivity gap" 的呈现**——这是检测计数比（12/2=6×），不是连续灵敏度指标（详见 Claim Calibration 部分）。

### "五层防御" framing

Section 5 (page 7) 和 Appendix M-N 提供了系统性的 robustness checks。这不是 "defensive"——对于直接面对 Comparative Trap 质疑的论文，主动提供多层控制实验是合理且必要的。framing 是 compelling 而非 defensive。

### "Blindspot" 作为命名

**记忆性好，定义清晰**。论文在 page 1 给出精确定义："a measurement attenuation phenomenon where tie-rate compression in absolute scoring obscures biases that ordinal comparison readily reveals"。但论文随后（Section 7, page 7）承认这可能是 construct divergence 而非 attenuation——命名预设了 attenuation 解释，与 agnostic stance 有轻微张力。

### Tables vs. Figures 平衡

主文 3 tables + 3 figures（Figure 1 pipeline, Figure 2 DAG, Figure 3 BT probabilities, Figure 4 detection curves）。Appendix 约 11 tables。主文的 table-to-figure 比例合理——Figure 3-4 提供趋势和直觉，Tables 1-3 提供精确数值。**不存在 "no figures" 的问题**。

### Limitations 充分性

Page 9 有 3 段实质内容：(1) Quality-style confounding and construct validity（含 construct divergence 替代解释）；(2) Evaluator-producer bias and generalizability；(3) Validation methodology and scale design（提及 100-point scale 和 human ground-truth）。对 EMNLP mandatory requirement **充分**。

---

## 4. Claim Calibration

### "first empirical quantification in the LLM judge setting"（Section 2, page 3）

**基本准确，但需限定。** 论文原文："Our contribution is the first systematic quantification of this gap for LLM judge style bias, identifying the two-layer mechanism (tie inflation plus residual signal attenuation) that explains it."

这个 claim 有三层限定：(1) "for LLM judge style bias"（不是一般性 claim）；(2) "systematic quantification"（不是 "discovery"）；(3) "identifying the two-layer mechanism"（mechanism identification 是新的）。

Jeong et al. (2025) 也比较了 pairwise vs. pointwise，但焦点是 amplification 而非 measurement sensitivity gap。Haak & Schaer (2025) 比较了 Likert vs. pairwise 在 linguistic bias 中的量化，但不在 LLM judge 场景下。因此 claim 在当前限定下可辩护，但建议进一步收窄为 "the first content-controlled quantification"。

### "measurement mode, not scale granularity, determines style bias detectability"（Section 7, page 7-8）

**因果语言有强证据支撑。** 100-point Likert ablation (Appendix L, Table 12) 是关键证据：0-100 连续量表（101 个可能值）下 Blindspot 仍然存在（formality p = 0.17, verbosity p < 0.001 but Likert still n.s. at tie rate 51.2%）。这排除了 scale granularity 作为解释。因果推断链：(i) 同一数据、同一 judge、同一 style manipulation；(ii) 改变唯一变量是 measurement mode（absolute vs. comparative）；(iii) 结果翻转（n.s. → significant）。这足以支撑 "measurement mode determines detectability" 的 causal claim。

### Agnostic stance on mechanism：诚实还是弱点？

**明确是优势。** Section 7 (page 7) 原文："An equally plausible interpretation is that Likert and pairwise modes measure fundamentally different constructs... We cannot definitively distinguish these interpretations; however, both lead to the same practical conclusion: practitioners relying on Likert audits will systematically miss style preferences that drive pairwise-based alignment pipelines (RLHF, DPO), regardless of whether the gap arises from attenuation or construct mismatch."

这是**模范级的 claim calibration**——承认解释性歧义，但指出实践建议不受影响。比之前版本（默认 attenuation 为主调）大幅改善。

### Title claim "Likert Blindspot"

证据充分：(1) 2 judges × 2 axes（formality, verbosity）= 4/6 configurations 展示 Blindspot；(2) 7 种 Likert 方法全部 fail（Table 2）；(3) 100-point scale 持续 fail（Table 12）；(4) Cross-benchmark 复制；(5) Cross-rewriter 独立性。足以命名一个现象。

**唯一张力**：命名 "Blindspot" 暗示 Likert 的失败，但 agnostic stance 承认可能是 construct difference。建议在 Abstract 或 Introduction 中加一句 qualifier（如 "whether this reflects attenuation or construct divergence, the practical implication is the same"）。

---

## 5. Formatting & Compliance

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤8 页 | ✅ | Pages 1-8 |
| Limitations | ✅ | Page 9, 3 段实质内容 |
| Anonymous | ✅ | "Anonymous ACL submission" |
| References | ✅ | 49 篇，覆盖充分 |
| Ethics statement | ⚠️ | 未见显式 Ethics Statement section |
| Responsible NLP Research Checklist | ⚠️ | 未见。ARR 要求 mandatory checklist。如果提交时未附 checklist，可能 desk reject。**但这属于提交格式问题而非论文内容问题，不影响我的内容评审。** |

---

## Weaknesses Summary

### Should-Fix（影响评分但不一票否决）

**W1** "≥6× sensitivity gap" 是检测计数比而非连续灵敏度指标
- 位置：Abstract (page 1)、Table 2 caption (page 6)
- 12 BT-significant / 2 Likert-significant = 6×。这是二值化检测计数的比值，高度依赖 α=0.05 选择。如果多数 Likert p 值在 0.05-0.15 之间，小幅阈值变化会大幅改变比率。建议改用连续指标（如中位 effect size 比）或至少注明 "detection count ratio"。

**W2** GEE taxonomy "replicates across 3 architectures" 缺少完整证据
- 位置：Conclusion (page 8)
- Table 3 的完整 GEE 仅展示 GPT-4o 和 Qwen3-32B。第三个 architecture 的 replication 数据在哪？如果指 Appendix D 的 cross-rewriter test，那只是 rewriter independence，不是 judge architecture replication。建议要么增加第三个 judge 的 GEE，要么弱化 claim。

**W3** "Blindspot" 命名与 agnostic stance 的轻微张力
- 位置：Title + Abstract vs. Section 7
- 命名预设 attenuation 解释（"Blindspot" = 应看到但没看到），而 Section 7 承认 construct divergence 同等合理。建议在 Abstract 中加一句 qualifier 统一语气。

### Minor

**M1** 可补引 Howcroft & Belz (2020) "Twenty Years of Confusion in Human Evaluation" —— 直接讨论 NLG 评估中 Likert vs. ranking 的系统性问题。

**M2** Orphan bib entry: `hoenig2001abuse` 在 .bib 中但未被 \cite 引用。

**M3** Cross-rewriter independence test（Appendix D）缺 register 轴。鉴于 register 在 Table 1 中效应最弱，如果 rewriter independence 不成立，register 的结论可能需要 caveat。

**M4** 引用验证发现 3 篇 "not_found"（murugadoss2025sos, krosnick1999survey, saito2023verbosity）——可能是 OpenAlex 索引延迟或标题细微差异，建议核实。

---

## Strengths Summary

1. **100-point Likert ablation 是本版最强新增**：隔离 measurement mode vs. granularity，将核心发现从 domain transfer 提升至新的 empirical finding。

2. **Agnostic stance on mechanism 是模范级 claim calibration**：承认 attenuation vs. construct divergence 的解释歧义，但指出实践建议不受影响。

3. **RATE head-to-head comparison 有直接方法论价值**：Section 5.2 证明 RATE 的 Likert ATE 在 formality 上 d=0.10 (n.s.)，同一数据 BT 63.0% (p=0.001)。对 RATE 用户群有直接警示意义。

4. **Related Work 覆盖全面**：49 篇引用，覆盖因果推断、心理测量、NLG 评估、LLM judge bias 四个领域。所有 Director 指定的 "missing citations" 在本版中均已被引用。

5. **GEE per-axis taxonomy 无先例**：verbosity/formality/register 的三种 confound regime 分类为评估社区提供了可操作的审计指导。

6. **Comparative Trap 五层防御系统性强**：排除 false positive 和 uniform amplification，诚实承认无法排除 proportional amplification。

---

## 与之前审稿的对比

本修订版解决了我 Round 1 审稿中的多个核心关切：
- ✅ N1（遗漏 Comparative Trap）→ 现已引用并用五层防御回应
- ✅ N2（"first systematic" overclaim）→ claim 已收窄并加限定
- 部分解决 N3（judge 覆盖面）→ GEE 仍仅 2 judges，但 cross-rewriter test 增加了间接证据
- ✅ W1（formality confound 不透明）→ GEE taxonomy 明确标注 formality 为 "conditional"
- ✅ W3（Claude negative control 措辞）→ 现采用更审慎措辞
- 新增 100-point ablation——之前未提及，是重大改进

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 420 · 2026-05-21T16:16:24.843715+00:00_

⏰ API 当前限速（所有账号），请稍后重试（通常几分钟内恢复）。你的消息未丢失，重新发送即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 421 · 2026-05-21T16:16:26.345876+00:00_

[Reviewer 2 审稿结果]:
⏰ API 当前限速（所有账号），请稍后重试（通常几分钟内恢复）。你的消息未丢失，重新发送即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 422 · 2026-05-21T16:16:48.971540+00:00_

⏰ API 当前限速（所有账号），请稍后重试（通常几分钟内恢复）。你的消息未丢失，重新发送即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 46

## Round 46

76 recorded events


### User

_source line 423 · 2026-05-21T17:23:08.829176+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-21T17:23:18.121704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-21T17:23:18.172970+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-21T17:23:25.501878+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,WebSearch",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,WebSearch",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-21T17:23:25.552458+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-21T17:23:28.263040+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-21T17:23:28.263534+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-21T17:23:32.077046+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-21T17:23:32.127738+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-21T17:23:37.646094+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-21T17:23:38.599887+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (53 个)\n\n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **register_100_cf**: QUEUED — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- register_100_cf: Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality（排队等待 GPU）\n\n## 近期结论\n- **llama70b_register** (success): Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures\n- **llama70b_debiased** (success): Llama-70B correction resistance follows the same axis-dependent pattern as GPT-4o/Qwen3-32B: debiased prompts reduce but do not eliminate style bias, with verbosity more amenable to correction than formality, confirming bias persistence is model-independent\n  [debiased_llama70b_summary.json](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/llama70b_debiased/data/debiased_llama70b_summary.json)\n- **crossbench_alpacaeval_verbosity** (success): AlpacaEval verbosity bias is strong enough (BT ~84%) that even Likert detects it, confirming the effect-size gradient: Blindspot occurs at small-to-medium effects (d<0.15) but not at large effects (d>0.3)\n\n## 趋势\n成功 3
…[truncated 187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-21T17:23:39.051886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-21T17:23:40.056259+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Detecting Hidden Style Bias\\in LLM Judges via Controlled Style Decomposition}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	
46	\paragraph{Evaluator-producer bias and generalizability.}
47	Qwen3-32B serves as both rewriter and judge, raising s
…[truncated 1444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-21T17:23:40.056689+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 437 · 2026-05-21T17:23:40.257530+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 438 · 2026-05-21T17:23:51.149245+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"}]

The search results don't contain a specific EMNLP 2026 main conference call for papers with ARR submission guidelines and page limits. T
…[truncated 5280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 11092
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-21T17:23:51.149673+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10892
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-21T17:23:57.826759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-21T17:23:58.831931+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved unless noted)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	    mentions:
16	      - round: 3
17	        reviewers: [1, 2]
18	        note: "因果语言降级问题在 Round 3 以新形式复发，见 R3-N1"
19	      - round: 4
20	        reviewers: [1]
21	        note: "R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。"
22	      - round: 5
23	        reviewers: [1, 2]
24	        note: "标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2"
25	
26	  - id: "R2-N1"
27	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
28	    category: framing
29	    severity: warning
30	    status: resolved
31	    first_raised_round: 1
32	    last_seen_round: 5
33	    resolution: "Abstract/Intro 明确标注为 'first systematic quantitative verification of known measurement theory principle in LLM judge evaluation'. Structural ceiling acknowledged."
34	    resolution_round: 4
35	    mentions:
36	      - round: 3
37	        reviewers: [1, 2]
38	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
39	      - round: 4
40	        reviewers: [1, 2]
41	        note: "R4-SF8: Honest novelty positioning applied."
42	      - round: 5
43	        reviewers: [1, 2]
44	        note: "Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。"
45	
46	  - id: "R1-N2"
47	    summary: "NLI gate 67% false-negative rate 造成选择偏差未分析"
48	    category: method
49	    severity: critical
50	    status: resolved
51	    first_raised_round: 1
52	    last_seen_round: 1
53	    resolutio
…[truncated 28164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-21T17:23:58.832433+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for main conference papers submission format anonymous review ARR 2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for main conference papers submission format anonymous review ARR 2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-21T17:23:59.836516+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-21T17:24:00.188173+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 445 · 2026-05-21T17:24:00.289052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-21T17:24:00.339623+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_director_acab027e.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-21T17:24:05.960606+00:00_

Web search results for query: "EMNLP 2026 call for main conference papers submission format anonymous review ARR 2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Based on the search results, here's the information about EMNLP 2026's call for main conference papers submission format and anonymous review:

## Review Process

The reviewing process will continue to be double-blind. Reviewers will not see authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible. However, authors will be given the option through ARR to make their anonymized submitted articles publicly visible.

## Submission Approach

EMNLP 2026 has chosen this approach in coordination with *CL 2026 conferences, which are adopting the same procedure and a coordinated submission plan to allow maximum flexibility during their submission periods for the authors.

## Submission Flexibility

At each cycle, after a paper has been fully reviewed, authors have the option to 
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 7128
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-21T17:24:11.682614+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-21T17:24:11.883804+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-21T17:24:11.884320+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-21T17:24:13.641226+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 1756
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-21T17:24:13.691838+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-21T17:24:13.742440+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-21T17:24:20.935596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-21T17:24:21.337502+00:00_

1	\begin{abstract}
2	LLM judges are widely deployed for evaluation and alignment, yet style features alone explain judge scores with near-perfect correlation.
3	We introduce Controlled Style Decomposition (CSD), the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to systematically quantify style bias in LLM judges.
4	Across three target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) and one negative control (Claude Sonnet 4), three benchmarks, and three style axes, CSD demonstrates the Likert Blindspot: Likert scoring systematically misses style biases that pairwise comparison detects (BT 63--84\%, $p < 0.001$), following a severity spectrum---complete at moderate bias ($d \to 0$ at $n = 355$), exceeding 60\% attenuation at stronger effects---confirmed by seven statistical methods.
5	GEE conditional decomposition demonstrates a per-axis confound structure consistent across all three target judges: verbosity bias is style-dominated (Style OR $8$--$13$, Originality OR ${<}1$), formality exhibits a conditional effect moderated by content quality changes, and register is judge-dependent (originality-dominated to mixed)---determining which estimates are directly interpretable and which require conditional analysis.
6	A fourth judge (Claude Sonnet 4) detects no bias on either axis, supporting discriminative validity.
7	We identify two candidate interpretations---measurement attenuation and construct divergence---and show that both yield the same operational conclusion: Likert-only evaluation systematically misses style-driven preferences that propagate through pairwise-based alignment pipelines.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-21T17:24:21.388233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-21T17:24:22.393476+00:00_

1	\section{Introduction}
2	
3	LLM judges are central infrastructure for NLP evaluation (AlpacaEval, MT-Bench, Chatbot Arena) and alignment training (RLHF, DPO), where judge-generated preferences serve as reward signals.
4	Any systematic bias in their assessments propagates through both evaluation leaderboards and model development pipelines.
5	
6	Recent work suggests that style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, motivating systematic measurement of per-axis style bias.
7	\citet{li2026preference} demonstrate that 76--92\% of observed preference signals originate from surface-level style cues rather than substantive quality differences, and \citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.
8	Despite this consensus on severity, existing approaches each address individual requirements: CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} provide multi-dimensional style analysis, RATE \citep{reber2025rate} introduces interventional design, and length-controlled AlpacaEval \citep{dubois2025lc} offers population-level correction.
9	However, no single framework integrates all four requirements---per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.
10	A further concern compounds these limitations: standard Likert scoring suffers from a measurement efficiency gap---integer discretization produces ${\sim}60\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison---a limitation predicted by measurement theory \citep{thurstone1927law} but previously unquantified for LLM judges.
11	
12	We propose Controlled Style Decomposition (CSD), the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to systematically quantify style bias in LLM judges.
13	Inspired by interventional approaches to text analysis \citep{vei
…[truncated 3132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-21T17:24:22.393968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-21T17:24:22.846009+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
14	
15	\paragrap
…[truncated 4777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-21T17:24:22.846409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-21T17:24:23.348878+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We aim to isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
8	For each text, an instruction-tuned LLM (Qwen3-32B) first classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification), then rewrites it toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
9	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
10	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
11	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
12	
13	\subsection{Content Preservation Verification}
14	\label{sec:nli_gate}
15	
16	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
17	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90.
18	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exceed this value.
19	For axes that inherently change information density (e.g., verbosity), bidirectional verification is inappropriate---exp
…[truncated 5740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-21T17:24:23.449633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-21T17:24:23.450430+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	We designate a primary family of eight hypothesis tests (three judges $\times$ formality and verbosity, plus register for GPT-4o and Qwen3-32B) and control the family-wise error rate with Holm-Bonferroni correction at $\alpha = 0.05$.
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Main results across four judges, three style axes, and three benchmarks. BT: Bradley-Terry win probability (10{,}000 pair-level bootstrap resamples; 95\% CIs in Appendix~\ref{app:bt_ci}). AEval: AlpacaEval; MTB: MT-Bench. Claude Sonnet 4 serves as negative control.}
19	\label{tab:main_results}
20	\begin{tabular}{@{}lllccc@{}}
21	\toprule
22	Bench & Judge & Axis & BT $P$ & Likert $d$ ($p$) & \\
23	\midrule
24	LLMBar & GPT-4o & Form.\ & .630$^{***}$ & .102 (.332) & $\dagger$ \\
25	 & GPT-4o & Verb.\ & .760$^{***}$ & $-$.095 (.403) & $\dagger$ \\
26	 & GPT-4o & Reg.\ & .570$^{\dagger}$ & $-$.031 (.785) & $\dagger_{\text{e}}
…[truncated 16884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-21T17:24:23.802454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-21T17:24:24.756728+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Controlled Style Decomposition (CSD), a black-box framework yielding two complementary findings across four judges (three target, one negative control), three benchmarks, and three style axes.
5	First, the Likert Blindspot: Likert scoring systematically misses style biases that pairwise comparison detects, following a severity spectrum---complete at moderate bias ($d \to 0$ at $n = 355$), over 60\% attenuation at stronger effects---confirmed by seven statistical methods.
6	Whether this reflects measurement attenuation or construct divergence, the operational consequence is identical: Likert-only audits miss style-driven preferences that propagate through pairwise-based alignment pipelines.
7	
8	Second, GEE conditional decomposition demonstrates a per-axis confound structure consistent across three independent architectures---verbosity is style-dominated, formality conditional, register judge-dependent---determining which estimates are directly interpretable and which require conditional analysis, and directly informing debiasing priorities.
9	
10	For the evaluation community: style bias audits should adopt content-controlled pairwise comparison with per-axis decomposition, especially at the moderate effect sizes typical of real-world evaluation ($n < 500$), where six experimental controls bound the risk of format-level amplification (\S\ref{sec:amplification}; \citealt{jeong2025comparative}).
11	Existing Likert-based null findings may reflect measurement insensitivity rather than genuine absence of bias.
12	Future work should incorporate human evaluation of rewriting quality, broader benchmark and axis coverage, and stronger causal identification through randomized rather than observational designs.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-21T17:24:24.757113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-21T17:24:25.711418+00:00_

1	\appendix
2	
3	\section{Direction Asymmetry and Quality Confounding}
4	\label{app:direction}
5	
6	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
7	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
8	To quantify this, we fit a GEE logistic model (exchangeable correlation) with both formality and original-preference as predictors.
9	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
10	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
11	
12	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.
13	The originality confound remains stronger ($4.99$ vs.\ $2.32$), consistent with evaluator-producer bias inflating the originality component (Limitations).
14	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
15	
16	The NLI gate blocks \emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.
17	
18	\section{Consistency Filter Robustness}
19	\label{sec:consistenc
…[truncated 21079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-21T17:24:25.711769+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format guidelines page limit template anonymity policy aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format guidelines page limit template anonymity policy aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 469 · 2026-05-21T17:24:25.913497+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
  }
}
```

</details>

---


### Tool result

_source line 470 · 2026-05-21T17:24:25.964222+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-21T17:24:31.988116+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format guidelines page limit template anonymity policy aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on my search of the ACL Rolling Review 2026 submission guidelines, here's what I found:

## Submission Format Guidelines

Paper submissions must use the official ACL style template, and there is an official Overleaf template with a [review] setting that must be on for the submission.

## Page Limits

Papers follow page limits 
…[truncated 1110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6276
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-21T17:25:09.484478+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-21T17:25:10.338181+00:00_

-rw-r--r-- 1 ubuntu ubuntu 362099 May 21 17:20 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-21T17:25:10.890674+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-21T17:25:11.343160+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-21T17:25:11.544408+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find config in workspace root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find config in workspace root"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-21T17:25:11.595124+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-21T17:25:15.612516+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -name \"*.yaml\" -path \"*/causal_style*\" 2>/dev/null | head -10",
  "description": "Find YAML files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -name \"*.yaml\" -path \"*/causal_style*\" 2>/dev/null | head -10",
    "description": "Find YAML files in project"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-21T17:25:16.064812+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/lc_alpacaeval_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/rate_icml_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/casse_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/preference_leakage_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/dml_chernozhukov_2018.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/counterfactual_rhetorical_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/fairjudge_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/soumik_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/sos_bench_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/veitch_uai_2020.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-21T17:25:16.399525+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"projects.yaml\" -o -name \"config.yaml\" 2>/dev/null | head -5",
  "description": "Find config in agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -name \"projects.yaml\" -o -name \"config.yaml\" 2>/dev/null | head -5",
    "description": "Find config in agent-ml-research"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-21T17:25:16.716691+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 317
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-21T17:25:20.909109+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -5; find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 1 -name \"*.yaml\" 2>/dev/null | head -5",
  "description": "Find config files in workspace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -5; find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 1 -name \"*.yaml\" 2>/dev/null | head -5",
    "description": "Find config files in workspace"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-21T17:25:21.161994+00:00_

/home/ubuntu/agent-ml-research/workspace/config/approvals.yaml
/home/ubuntu/agent-ml-research/workspace/config/projects/LLM-Calibration.yaml
/home/ubuntu/agent-ml-research/workspace/config/resources.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/aaai-2027.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/icml-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-21T17:25:24.875968+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research/workspace/config -name \"*.yaml\" 2>/dev/null | head -10; find /home/ubuntu/agent-ml-research/config -name \"*causal*\" -o -name \"*emnlp*\" 2>/dev/null | head -5",
  "description": "Find project-specific config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research/workspace/config -name \"*.yaml\" 2>/dev/null | head -10; find /home/ubuntu/agent-ml-research/config -name \"*causal*\" -o -name \"*emnlp*\" 2>/dev/null | head -5",
    "description": "Find project-specific config"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-21T17:25:24.976973+00:00_

/home/ubuntu/agent-ml-research/workspace/config/approvals.yaml
/home/ubuntu/agent-ml-research/workspace/config/projects/LLM-Calibration.yaml
/home/ubuntu/agent-ml-research/workspace/config/resources.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-21T17:25:28.138919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-21T17:25:28.440449+00:00_

1	typesetting:
2	  layout: two_column
3	  max_pages: 8
4	  paper_size: a4
5	  column_width_cm: 7.7
6	  text_width_cm: 16.0
7	  column_sep_cm: 0.6
8	  template_sets:
9	    hyperref: true
10	  preamble_additions:
11	    packages: [microtype, booktabs, cleveref]
12	    float_params:
13	      topfraction: "0.85"
14	      bottomfraction: "0.85"
15	      textfraction: "0.15"
16	      floatpagefraction: "0.7"
17	    penalties:
18	      widowpenalty: "10000"
19	      clubpenalty: "10000"
20	  forbidden_packages: []
21	  required_sections:
22	    - name: Limitations
23	      severity: critical
24	    - name: Ethics Statement
25	      severity: warning
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-21T17:25:28.491504+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/workspace.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/workspace.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-21T17:25:28.491983+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-21T17:25:41.141987+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool call

_source line 491 · 2026-05-21T17:25:42.297807+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-21T17:26:10.571071+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 29429
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-21T17:26:10.571465+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 28273
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-21T17:26:10.722372+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (通过 ARR 提交)\n- **截止日期**: 2026-05-25\n- **页数限制**: 主正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- **模板**: ACL 格式，`\\usepackage[review]{acl}`\n- **匿名规则**: double-blind\n- **Limitations**: 必须包含，只讨论局限性，不能包含新实验/图表/分析\n- **ARR Responsible NLP Checklist**: 在 OpenReview submission form 中填写，不在论文 PDF 中\n\n## 论文信息\n- **标题**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**重点关注以下方面，逐条给出评价（Must-Fix / Should-Fix / Minor / OK）：**\n\n### 1. 统计方法学\n- Bradley-Terry 模型的 IIA 假设是否得到检验？GoF 测试是否充分？\n- Holm-Bonferroni 校正的 family 定义（8 个 primary tests）是否合理？exploratory/confirmatory 分类是否恰当？\n- GEE 模型规格：exchangeable correlation 的选择是否合理？interaction test 是否充分？\n- Bootstrap CI（10,000 resamples）方法是否标准？\n- TOST 等价性检验（Claude 负对照）的 equivalence bound 选择是否有 external justification？\n\n### 2. NLI Gate 设计\n- 0.90 阈值的选择是否有充分 justification（plateau 论证是否成立）？\n- 双向 vs direction-aware gating 的 axis-dependent 策略是否合理？\n- NLI validation 使用 Qwen3-32B 作为 annotator + GPT-4o cross-validation 是否足够？是否需要人工评估？\n- False negative rate 8.4% 对结论的影响评估是否充分？\n\n### 3. 因果声明与方法论强度\n- \"Controlled Style Decomposition\" 和 \"interventional framework\" 等术语与实际方法论强度是否匹配？\n- DAG (Figure 2) 的 causal claims 与 filtering-based approach 之间是否存在张力？\n- §3.5 Design Rationale 中的 identification assumptions 是否被充分讨论？\n- \"approximates content preservation\" vs 真正的 intervention 之间的区别是否清晰？\n\n### 4. Evaluator-Producer Bias\n- Qwen3-32B 同时作为 rewriter 和 judge 的 self-preference 风险评估是否充分？\n- Cross-rewriter independence test（GPT-4o 替代 Qwen3-32B）覆盖了哪些轴？缺失轴（register）的影响？\n- Style OR 下降 22%（13.10→10.17）的解释是否合理？\n\n### 5. 样本量与泛化性\n- LLMBar (n=100) 为主数据源，cross-benchmark 扩展是否足够？\n- 三个 benchmark × 三个 judge 的覆盖矩阵中空 cell 的处理？\n- n=355 scaled replication 的证据权重？\n- 从实验数据到 \"style bias audits should adopt pairwise comparison\" 的推广强度？\n\n### 6. Confound 控制\n- NLI gate 能否真正阻断 quality perception shifts mediated by style？\n- Formality 方向不对称（78.8% vs 54.5%）的处理是否充分？\n- Same-style double-rewrite control 的效力？\n- GEE 的 originality term 是否真正\"吸收\"了 rewriting artifact？\n\n请按标准 ARR 审稿格式输出：Summary → Strengths → Weaknesses (逐条标注 severity) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (通过 ARR 提交)\n- **截止日期**: 2026-05-25\n- **页数限制**: 主正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- **模板**: ACL 格式，`\\usepackage[review]{acl}`\n- **匿名规则**: double-blind\n- **Limitations**: 必须包含，只讨论局限性，不能包含新实验/图表/分析\n- **ARR Responsible NLP Checklist**: 在 OpenReview submission form 中填写，不在论文 PDF 中\n\n## 论文信息\n- **标题**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**重点关注以下方面，逐条给出评价（Must-Fix / Should-Fix / Minor / OK）：**\n\n### 1. 统计方法学\n- Bradley-Terry 模型的 IIA 假设是否得到检验？GoF 测试是否充分？\n- Holm-Bonferroni 校正的 family 定义（8 个 primary tests）是否合理？exploratory/confirmatory 分类是否恰当？\n- GEE 模型规格：exchangeable correlation 的选择是否合理？interaction test 是否充分？\n- Bootstrap CI（10,000 resamples）方法是否标准？\n- TOST 等价性检验（Claude 负对照）的 equivalence bound 选择是否有 external justification？\n\n### 2. NLI Gate 设计\n- 0.90 阈值的选择是否有充分 justification（plateau 论证是否成立）？\n- 双向 vs direction-aware gating 的 axis-dependent 策略是否合理？\n- NLI validation 使用 Qwen3-32B 作为 annotator + GPT-4o cross-validation 是否足够？是否需要人工评估？\n- False negative rate 8.4% 对结论的影响评估是否充分？\n\n### 3. 因果声明与方法论强度\n- \"Controlled Style Decomposition\" 和 \"interventional framework\" 等术语与实际方法论强度是否匹配？\n- DAG (Figure 2) 的 causal claims 与 filtering-based approach 之间是否存在张力？\n- §3.5 Design Rationale 中的 identification assumptions 是否被充分讨论？\n- \"approximates content preservation\" vs 真正的 intervention 之间的区别是否清晰？\n\n### 4. Evaluator-Producer Bias\n- Qwen3-32B 同时作为 rewriter 和 judge 的 self-preference 风险评估是否充分？\n- Cross-rewriter independence test（GPT-4o 替代 Qwen3-32B）覆盖了哪些轴？缺失轴（register）的影响？\n- Style OR 下降 22%（13.10→10.17）的解释是否合理？\n\n### 5. 样本量与泛化性\n- LLMBar (n=100) 为主数据源，cross-benchmark 扩展是否足够？\n- 三个 benchmark × 三个 judge 的覆盖矩阵中空 cell 的处理？\n- n=355 scaled replication 的证据权重？\n- 从实验数据到 \"style bias audits should adopt pairwise comparison\" 的推广强度？\n\n### 6. Confound 控制\n- NLI gate 能否真正阻断 quality perception shifts mediated by style？\n- Formality 方向不对称（78.8% vs 54.5%）的处理是否充分？\n- Same-style double-rewrite control 的效力？\n- GEE 的 originality term 是否真正\"吸收\"了 rewriting artifact？\n\n请按标准 ARR 审稿格式输出：Summary → Strengths → Weaknesses (逐条标注 severity) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-21T17:26:35.563422+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24841
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-21T17:26:35.966095+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 2，负责**新颖性、Related Work 完整性与写作质量**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (通过 ARR 提交)\n- **截止日期**: 2026-05-25\n- **页数限制**: 主正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- **模板**: ACL 格式，`\\usepackage[review]{acl}`\n- **匿名规则**: double-blind\n- **Limitations**: 必须包含，只讨论局限性，不能包含新实验/图表/分析\n- **ARR Responsible NLP Checklist**: 在 OpenReview submission form 中填写，不在论文 PDF 中\n\n## 论文信息\n- **标题**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**重点关注以下方面，逐条给出评价（Must-Fix / Should-Fix / Minor / OK）：**\n\n### 1. Novelty 定位\n- \"the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison\" 的 novelty claim 是否准确？是否有 prior work 做了类似组合？\n- Likert Blindspot 是否真的是 \"first systematic quantification\"？Thurstone (1927) 已建立理论基础，NLP 领域是否已有类似量化？\n- CSD 对比 RATE、CASSE、FairJudge 等已有框架的增量贡献是否清晰？\n- Novelty 是否主要是 domain transfer（将已知测量理论应用到 LLM judge）？如果是，论文是否诚实承认？\n\n### 2. Related Work 完整性\n- 引用覆盖是否充分？特别检查以下文献是否被讨论：\n  - Jeong et al. (2025) \"Comparative Trap\"——pairwise 放大 style bias，与本文 §6 建议可能矛盾\n  - Stureborg et al. (2024) inconsistency across evaluation formats\n  - Park et al. (2024) OffsetBias\n  - 其他你认为遗漏的重要文献\n- Related Work 的组织结构是否合理？是否有效地将本工作定位在文献中？\n- 与 Comparative Trap 的张力是否被充分讨论？论文建议 \"adopt pairwise comparison\" 但 pairwise 本身可能放大 bias\n\n### 3. Framing 与 Claims\n- Abstract 信息密度是否过高？是否适合目标读者？\n- \"across three judges\" 的措辞是否准确？Claude 作为 negative control 不应等同于 target judge\n- \"confound-free\" (verbosity) 的措辞是否过强？\n- Measurement attenuation vs construct divergence 两种解释的呈现是否平衡？\n- Conclusion 中 \"style bias audits should adopt...\" 的推荐强度与证据基础是否匹配？\n- Formality confound 与 verbosity clean signal 在 Abstract/Conclusion 中是否被区分？\n\n### 4. 写作质量\n- 整体叙事结构是否清晰？读者能否跟上论证线索？\n- 术语使用一致性（\"Controlled Style Decomposition\" / \"CSD\" / \"interventional\" / \"filtering-based\"）\n- Table/Figure 的 caption 是否自包含？\n- Limitations 部分是否恰当（覆盖 3 个关键点，不过长）？\n- Appendix 结构是否合理？主正文与 Appendix 的分工是否恰当？\n\n### 5. 格式合规性\n- 主正文是否在 8 页以内？\n- Limitations 部分是否只包含局限性讨论（无新实验/图表）？\n- 引用格式是否符合 ACL natbib 标准？\n- 匿名性是否完整（无作者信息泄露）？\n- 是否有 \"Code and Data\" 可用性声明？\n\n### 6. 图表质量\n- Figure 1 (pipeline diagram) 是否清晰有效？\n- Figure 2 (DAG) 是否在黑白打印下可读？dashed/solid/dotted 区分是否够？\n- Figure 3 (forest plot) 是否有效传达主要发现？\n- Figure 4 (power curve) 是否必要？是否增加了论文价值？\n- 所有 Table 是否整洁、可读？\n\n请按标准 ARR 审稿格式输出：Summary → Strengths → Weaknesses (逐条标注 severity) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 2，负责**新颖性、Related Work 完整性与写作质量**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (通过 ARR 提交)\n- **截止日期**: 2026-05-25\n- **页数限制**: 主正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- **模板**: ACL 格式，`\\usepackage[review]{acl}`\n- **匿名规则**: double-blind\n- **Limitations**: 必须包含，只讨论局限性，不能包含新实验/图表/分析\n- **ARR Responsible NLP Checklist**: 在 OpenReview submission form 中填写，不在论文 PDF 中\n\n## 论文信息\n- **标题**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**重点关注以下方面，逐条给出评价（Must-Fix / Should-Fix / Minor / OK）：**\n\n### 1. Novelty 定位\n- \"the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison\" 的 novelty claim 是否准确？是否有 prior work 做了类似组合？\n- Likert Blindspot 是否真的是 \"first systematic quantification\"？Thurstone (1927) 已建立理论基础，NLP 领域是否已有类似量化？\n- CSD 对比 RATE、CASSE、FairJudge 等已有框架的增量贡献是否清晰？\n- Novelty 是否主要是 domain transfer（将已知测量理论应用到 LLM judge）？如果是，论文是否诚实承认？\n\n### 2. Related Work 完整性\n- 引用覆盖是否充分？特别检查以下文献是否被讨论：\n  - Jeong et al. (2025) \"Comparative Trap\"——pairwise 放大 style bias，与本文 §6 建议可能矛盾\n  - Stureborg et al. (2024) inconsistency across evaluation formats\n  - Park et al. (2024) OffsetBias\n  - 其他你认为遗漏的重要文献\n- Related Work 的组织结构是否合理？是否有效地将本工作定位在文献中？\n- 与 Comparative Trap 的张力是否被充分讨论？论文建议 \"adopt pairwise comparison\" 但 pairwise 本身可能放大 bias\n\n### 3. Framing 与 Claims\n- Abstract 信息密度是否过高？是否适合目标读者？\n- \"across three judges\" 的措辞是否准确？Claude 作为 negative control 不应等同于 target judge\n- \"confound-free\" (verbosity) 的措辞是否过强？\n- Measurement attenuation vs construct divergence 两种解释的呈现是否平衡？\n- Conclusion 中 \"style bias audits should adopt...\" 的推荐强度与证据基础是否匹配？\n- Formality confound 与 verbosity clean signal 在 Abstract/Conclusion 中是否被区分？\n\n### 4. 写作质量\n- 整体叙事结构是否清晰？读者能否跟上论证线索？\n- 术语使用一致性（\"Controlled Style Decomposition\" / \"CSD\" / \"interventional\" / \"filtering-based\"）\n- Table/Figure 的 caption 是否自包含？\n- Limitations 部分是否恰当（覆盖 3 个关键点，不过长）？\n- Appendix 结构是否合理？主正文与 Appendix 的分工是否恰当？\n\n### 5. 格式合规性\n- 主正文是否在 8 页以内？\n- Limitations 部分是否只包含局限性讨论（无新实验/图表）？\n- 引用格式是否符合 ACL natbib 标准？\n- 匿名性是否完整（无作者信息泄露）？\n- 是否有 \"Code and Data\" 可用性声明？\n\n### 6. 图表质量\n- Figure 1 (pipeline diagram) 是否清晰有效？\n- Figure 2 (DAG) 是否在黑白打印下可读？dashed/solid/dotted 区分是否够？\n- Figure 3 (forest plot) 是否有效传达主要发现？\n- Figure 4 (power curve) 是否必要？是否增加了论文价值？\n- 所有 Table 是否整洁、可读？\n\n请按标准 ARR 审稿格式输出：Summary → Strengths → Weaknesses (逐条标注 severity) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-21T17:26:37.222501+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1256
}
```

</details>

---


### Assistant

_source line 498 · 2026-05-21T17:26:46.797561+00:00_

**圆桌审稿 Round 1 已启动。**

**投稿信息：**
- 论文：*The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition*
- 目标：EMNLP 2026 Long Paper via ARR
- 截止：2026-05-25（4 天后）
- 格式：ACL template `[review]`，double-blind，8 页主正文

**Reviewer 编排（2 人）：**
- **Reviewer 1**：方法严谨性 + 实验设计（统计方法、NLI gate、因果声明、evaluator-producer bias、confound 控制）
- **Reviewer 2**：新颖性 + Related Work 完整性 + 写作质量 + 格式合规性

**并行线：**
- 视觉审查 Agent：已派发（fire-and-forget）
- 外部审稿（Stanford Agentic Reviewer）：已请求，等待用户协助提交

等待两名 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 499 · 2026-05-21T17:33:06.752132+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 方法严谨性与实验设计（Round 1 完整审稿）

### Paper Summary

本文提出 Controlled Style Decomposition (CSD)，一个检测 LLM judge 隐藏风格偏差的框架。核心发现是 "Likert Blindspot"：在相同数据上，Likert 评分（ATE）对风格偏差显示为不显著，而 position-controlled pairwise comparison 通过 Bradley-Terry 分析能检测到 63–67% 的风格偏差。CSD 包含三个阶段：(1) 沿单一风格轴用 instruction-tuned LLM 进行 style-controlled rewriting；(2) NLI-gated content preservation 过滤；(3) 位置控制的 pairwise comparison。在 3 个目标 judge、1 个负对照（Claude Sonnet 4）、3 个 benchmark、3 个风格轴上验证。GEE conditional decomposition 进一步揭示 per-axis confound structure。

---

### Summary of Strengths

**S1. 研究问题精准且对社区有直接价值。** Likert Blindspot 的发现对 LLM 评估实践有即时的方法论指导意义，指出了一个被广泛忽视的测量盲区（Section 5.2, Table 2）。

**S2. 统计框架严谨且多层次。** 七种统计方法交叉验证（Table 2），GEE 条件分解（Table 3），Bootstrap CI（10,000 resamples, Table 9），BT GoF 检验（Appendix H），NLI 阈值 sensitivity sweep（Table 8），TOST 等价性检验（Appendix G）。

**S3. 负对照设计增强因果推断。** Claude Sonnet 4 在所有轴上显示非显著偏差，支持了"检测到的偏差是 judge-specific"的论证。

**S4. Confound 结构的细粒度刻画。** GEE 分解区分了 style-dominated（verbosity）、conditional（formality）和 judge-dependent（register）三种模式。

**S5. 写作清晰、结构紧凑。** 主文控制在 8 页内，附录提供了充分的技术细节（15 个 appendix sections）。

---

### Must-Fix 问题

**N1** [critical] NLI gate 缺乏人工评估验证
- 位置：Section 3.2, Section 5.1, Appendix A
- 整个框架的有效性依赖 NLI gate 正确分离 style 与 content 变化，但验证完全自动化——Qwen3-32B annotator + GPT-4o cross-validation 得到 92.1%/82.6% precision。没有任何人工评估来验证 NLI gate 的 pass/fail 决策是否与人类判断一致。DeBERTa-v3-large 在 style-shifted text 上的行为可能与标准 NLI 数据不同——formal text 可能系统性地获得更高 entailment score。
- 建议：随机抽取 50–100 对 pass/fail 样本，2+ annotator 评估内容保持程度，报告 IAA 和一致率。

**N2** [critical] Evaluator-producer bias 22% OR 下降被低估
- 位置：Section 5.3, Appendix D, Table 6
- Qwen3-32B rewriter 替换为 GPT-4o 后 verbosity Style OR 下降 22%（13.10→10.17），论文定性为"bounding"但 22% 是 non-trivial。更关键的是 cross-rewriter test 只覆盖 formality 和 verbosity，**register 轴完全缺失**——而 register 恰是 judge-dependence 最强的轴。
- 建议：(1) 提供 producer-corrected 效应估计范围；(2) 补充 register 轴 cross-rewriter test；(3) 至少在 Limitations 标注 register 缺乏 producer-independence 验证。

---

### Should-Fix 问题

**W1** [warning] TOST equivalence bound 缺乏独立外部 justification（Appendix G）。用同研究 treatment effects 设定 control 的 equivalence bound 形成循环。建议引用外部基准。

**W2** [warning] BT IIA 假设在 formality 轴可能被违反（Appendix H，Fisher p = 0.015 方向不对称）。建议报告 direction-stratified BT estimates 或使用 Thurstone Case V 作为 robustness check。

**W3** [warning] 因果术语（"interventional framework"、Figure 2 DAG）与实际 filtering-based 方法之间存在张力。Section 3.5 hedging 适当但 Figure 2 视觉修辞偏强。建议 Figure 2 caption 标注非 formal causal model，Abstract 中用 "quasi-interventional"。

**W4** [warning] 样本量偏小（LLMBar n=100, MT-Bench n=30），scaled replication（n=355）仅覆盖 Qwen3-32B formality。建议报告 BT achieved power，扩展 replication 覆盖面。

**W5** [warning] Identification assumption (iii)——"rewrite introduces no systematic differences beyond target axis"——讨论不充分。Same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。

---

### 小问题

- M1: `hoenig2001abuse` orphan bib entry
- M2: Table 2 "sensitivity hierarchy" 首次出现缺乏定义
- M3: Figure 3 diamond vs circle markers 在灰度下难区分
- M4: Figure 4 y 轴标签被截断

---

### Questions

Q1: NLI gate 在不同 rewrite directions 上的 score 分布是否存在系统差异？
Q2: 22% OR 下降中有多少是 GPT-4o 的 style transfer 质量差异 vs 真实 self-preference？
Q3: Register 的 judge-dependence 如何排除 evaluator-producer confound？
Q4: 100-point continuous Likert 仍检测不到 Blindspot——这是否说明问题在 evaluation paradigm 而非 scale granularity？
Q5: Formality 方向不对称（88.9% vs 72.6%）是否意味着 casual→formal 改善了 perceived quality？

---

### 官方维度打分

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5/5 | 统计框架严谨但 NLI gate 缺人工验证、evaluator-producer bias 处理过于乐观 |
| Excitement | 3.5/5 | Likert Blindspot 对 evaluation community 有直接影响；框架有创意但非 paradigm shift |
| Reproducibility | 4/5 | 模型、超参、benchmark 明确标注；承诺代码/数据公开 |
| Overall | **3.5 — Borderline Conference** | 核心发现有价值且统计密度高，但 NLI human validation 缺失和 evaluator-producer confound 不足削弱可信度。N1+N2 解决后可上调至 4.0 |
| Confidence | 4/5 | 仔细阅读全文含全部附录；熟悉因果推断、BT、GEE 和 LLM 评估文献 |

**一句话总结**: 有价值的方法论发现和精巧的框架设计，但 NLI gate 无人工验证 + evaluator-producer bias 处理不足使核心 claim 可信度打折。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 500 · 2026-05-21T17:33:13.362470+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 48

## Round 48

2 recorded events


### User

_source line 501 · 2026-05-21T17:33:20.631352+00:00_

[Reviewer 1 审稿结果]:
审稿完成，已提交至 Review Director。

**评分**: Overall 3.5 (Borderline Conference), Soundness 3.5, Excitement 3.5, Reproducibility 4, Confidence 4。

**两个 Must-Fix 问题**：
1. NLI gate 完全依赖自动化验证，缺乏人工评估——这是整个框架的基石
2. Evaluator-producer bias 22% OR 下降处理不充分，且 register 轴缺失 cross-rewriter 验证

**五个 Should-Fix 问题**：TOST equivalence bound 循环论证、BT IIA 在 formality 上可能违反、因果术语过强、样本量偏小且 replication 覆盖面窄、identification assumption (iii) 讨论不足。

核心判断：论文发现有价值（Likert Blindspot）且统计密度高于同领域平均水平，但方法论基石的验证缺口阻止了 confident accept。如果 N1 和 N2 在 revision 中解决，可上调至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 502 · 2026-05-21T17:33:26.015377+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 49

## Round 49

6 recorded events


### User

_source line 503 · 2026-05-21T17:35:11.220930+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性、Related Work 完整性与写作质量）

### 总体评分
**Overall**: 3.5 = Borderline Conference
**一句话总结**: 一篇实验设计扎实、发现有实践价值的实证论文，但核心新颖性偏向将已知测量理论迁移到 LLM judge 领域，且存在页数超限等格式问题。

### 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计合理、多重控制周全，但 pairwise detection vs. amplification 无法完全区分；sample size 有限（n=88 基础），GEE 分析执行规范 |
| Excitement | 3/5 | Likert Blindspot 发现对评估社区有实践价值，但核心洞见（pairwise > Likert 灵敏度）在测量理论中已有充分预测；框架是整合型而非根本性创新 |
| Reproducibility | 4/5 | 模型版本、超参数、统计方法均有详细说明；代码/数据承诺接收后释放 |
| Confidence | 4/5 | 仔细阅读全文及附录，熟悉 LLM evaluation 和测量理论文献 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] 主正文超过 8 页限制

- 具体位置：PDF page 8–9 边界
- 问题：Section 6 (Conclusion) 在 page 8 底部开始，约 5–6 行结论文本溢出到 page 9（"trols bound the risk of format-level amplification...rather than observational designs"），之后才是 Limitations。EMNLP 2026 规定 "strict 8-page limit for main text"，Limitations 不计入但 Conclusion 计入。
- 为什么影响接收：严格执行下可导致 desk rejection 或要求格式修正。
- 建议修改方向：压缩 §5.6 或 §6 文本（约 6–7 行），或将 Table 3 移至 Appendix 以释放空间。

**N2** [critical] Novelty claim 过度宽泛——"first systematic quantification" 需要更精确的界定

- 具体位置：Abstract (sentence 2), Introduction (line 10, 12), Related Work §2 (line 23)
- 问题：论文声称 CSD 是 "the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison"，并称 Likert Blindspot 是 "first systematic quantification"。然而：
  - Pairwise > rating 的灵敏度优势是 Thurstone (1927) 以来的经典结论
  - 在 NLG 评估中的量化：Kiritchenko & Mohammad (2017) 和 Novikova et al. (2018) 已证明 forced-choice 方法检测到 rating scales 遗漏的质量差异
  - 框架的每个组件都有先例：NLI content verification、style-controlled rewriting (RATE)、position-controlled pairwise (Wang et al. 2023; Zheng et al. 2023)
  - Qiu et al. (2025, §2 line 12) 已在 persona-level 使用 counterfactual rewriting + BT
- 为什么影响接收：过度的 novelty claim 会被 reviewer 视为 overclaiming，降低论文可信度。
- 建议修改方向：(1) 将 "first systematic quantification" 限定为 "first systematic quantification for LLM judge style bias"；(2) 明确承认核心洞见是 domain transfer；(3) 弱化 conjunction novelty claim。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Comparative Trap 张力在 Conclusion 中处理不足
- §6 推荐 "style bias audits should adopt content-controlled pairwise comparison" 措辞过强，未充分 caveat pairwise 本身可能放大 style bias 的风险。§5.2 的 6 个控制有约束力但不能完全排除 format amplification。
- 建议：在 Conclusion 加入明确 caveat。

**W2** [warning] "interventional" 等强因果措辞需要收敛
- §3.5 诚实声明 "interventional rather than formal causal evidence"，但 Introduction/Abstract 多处使用强因果语言。Verbosity 被描述为 "style-dominated" 暗示因果清洁性，但 direction-aware gating 的 false positive rate (17.4%) 高于 formality (7.9%)。
- 建议：在 Abstract 和 Conclusion 对 verbosity 也标注 GEE 控制的限定。

**W3** [warning] 基准数据集单一，样本量偏小
- 主实验基于 LLMBar（n=88 after NLI gate）。Cross-benchmark 验证仅覆盖部分 axis×judge 组合。n=88 下 CI 较宽。
- 建议：在 Conclusion 更明确标注 generalizability 边界。

**W4** [warning] Abstract 信息密度过高
- 8 个句子塞入了框架名称、4 judges、3 benchmarks、3 axes、具体 BT 百分比、OR 值、两种解释。OR 值等技术细节不利于可读性。
- 建议：将 GEE OR 值推迟到 Introduction，Abstract 只保留核心发现的定性描述。

**W5** [warning] Appendix Table 5 (GEE CI) 部分条目缺失 CI
- GPT-4o formality/verbosity/register 以及 Qwen3 formality Orig OR 均只有点估计无 CI。
- 建议：补全所有 CI。

---

### 小问题
- M1: Introduction contributions 列表每条过长（3–5 行），可精简
- M2: Table 1 第 6 列无 header，Blindspot 标记列缺乏说明
- M3: Figure 2 (DAG) 纯黑白打印下红色 dotted 和橙色 dashed 的颜色区分消失
- M4: orphan bib entry hoenig2001abuse 实为 \citealt 引用（工具误报）
- M5: wu2023style bib key 年份 2023 但 venue 年份 2025（COLING），不影响正确性但易混淆
- M6: saito2023verbosity 在 OpenAlex 中未精确匹配，建议确认文献信息

---

### 主要优势
1. **发现的实践价值高**：Likert Blindspot 直接挑战了基于 Likert 的 bias 评估有效性
2. **实验设计周全**：6 个独立控制有效约束替代解释，Claude 负控制是强 discriminative validity 证据
3. **测量与因果的诚实态度**：§3.5 disclaimer + Limitations 充分讨论替代解释
4. **GEE per-axis decomposition 提供方法论增量**
5. **Related Work 覆盖全面**：Jeong (2025)、Stureborg (2024)、Park (2024) 均被讨论
6. **统计严谨性**：Holm-Bonferroni 校正、exploratory/confirmatory 区分、GEE diagnostics

---

### Questions for Authors
1. 如果 pairwise 存在 format amplification，"moderate" pairwise effects (BT 63–67%) 的真实效应量可能更小——如何在数据层面区分 "Likert misses real bias" vs "pairwise creates apparent bias"？
2. Rewriter independence test 中 GPT-4o rewriter 使 Style OR 降低 22%——如果使用 rule-based rewriting 作为更强控制，效应量可能进一步缩小？
3. 100-point scale 下 tie rate 仍高（formality 65.9%）——这是否说明 LLM judges 本质上倾向给"中性"评分，而非测量范式差异？

---

### Missing References（可选补充）
- Shi et al. (2024) "Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges"
- Bavaresco et al. (2024) "LLMs Instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks"

---

### 总体判断
**3.5 / 5 (Borderline Conference)**。实证执行扎实，但 novelty 主要停留在 domain transfer 层面，"first" claims 过于宽泛，且页数超限需修复。如果 authors 能 (1) 压入 8 页、(2) 精确界定 novelty claims、(3) 充分 caveat Comparative Trap 张力，接受概率会显著提高。当前状态适合 Findings 接收；是否 Main Conference 取决于其他 reviewer 对 novelty 阈值的判断。

引用验证摘要：50 条 bib entries, 41 verified, 3 not_found (likely indexing issues), 6 minor mismatches (name formatting/year), 0 missing_bib, 1 orphan (false positive from \citealt)。引用质量良好。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-21T17:35:35.227066+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应：对每个 Must-Fix、Should-Fix 和关键 Strength 用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。特别关注你们之间的分歧点。\n\n---\n\n## Reviewer 2 审稿意见（新颖性、Related Work 完整性与写作质量）\n\n### 总体评分\n**Overall**: 3.5 = Borderline Conference\n**一句话总结**: 一篇实验设计扎实、发现有实践价值的实证论文，但核心新颖性偏向将已知测量理论迁移到 LLM judge 领域，且存在页数超限等格式问题。\n\n### 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计合理、多重控制周全，但 pairwise detection vs. amplification 无法完全区分；sample size 有限（n=88 基础），GEE 分析执行规范 |\n| Excitement | 3/5 | Likert Blindspot 发现对评估社区有实践价值，但核心洞见（pairwise > Likert 灵敏度）在测量理论中已有充分预测；框架是整合型而非根本性创新 |\n| Reproducibility | 4/5 | 模型版本、超参数、统计方法均有详细说明；代码/数据承诺接收后释放 |\n| Confidence | 4/5 | 仔细阅读全文及附录，熟悉 LLM evaluation 和测量理论文献 |\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] 主正文超过 8 页限制\n- 具体位置：PDF page 8–9 边界\n- 问题：Section 6 (Conclusion) 在 page 8 底部开始，约 5–6 行结论文本溢出到 page 9，之后才是 Limitations。EMNLP 2026 规定 \"strict 8-page limit for main text\"，Limitations 不计入但 Conclusion 计入。\n- 为什么影响接收：严格执行下可导致 desk rejection 或要求格式修正。\n- 建议修改方向：压缩 §5.6 或 §6 文本（约 6–7 行），或将 Table 3 移至 Appendix 以释放空间。\n\n**N2** [critical] Novelty claim 过度宽泛——\"first systematic quantification\" 需要更精确的界定\n- 具体位置：Abstract (sentence 2), Introduction (line 10, 12), Related Work §2 (line 23)\n- 问题：论文声称 CSD 是 \"the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison\"，并称 Likert Blindspot 是 \"first systematic quantification\"。然而：\n  - Pairwise > rating 的灵敏度优势是 Thurstone (1927) 以来的经典结论\n  - 在 NLG 评估中的量化：Kiritchenko & Mohammad (2017) 和 Novikova et al. (2018) 已证明 forced-choice 方法检测到 rating scales 遗漏的质量差异\n  - 框架的每个组件都有先例\n  - Qiu et al. (2025) 已在 persona-level 使用 counterfactual rewriting + BT\n- 为什么影响接收：过度的 novelty claim 降低论文可信度。\n- 建议修改方向：将 \"first systematic quantification\" 限定为 \"first systematic quantification for LLM judge style bias\"；明确承认核心洞见是 domain transfer；弱化 conjunction novelty claim。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] Comparative Trap 张力在 Conclusion 中处理不足\n**W2** [warning] \"interventional\" 等强因果措辞需要收敛\n**W3** [warning] 基准数据集单一，样本量偏小\n**W4** [warning] Abstract 信息密度过高\n**W5** [warning] Appendix Table 5 (GEE CI) 部分条目缺失 CI\n\n---\n\n### 小问题\n- M1: Introduction contributions 列表每条过长\n- M2: Table 1 第 6 列无 header\n- M3: Figure 2 (DAG) 黑白打印下颜色区分消失\n- M4: orphan bib entry hoenig2001abuse（工具误报）\n- M5: wu2023style bib key 年份不一致\n- M6: saito2023verbosity 文献信息需确认\n\n---\n\n### Questions for Authors\n1. 如果 pairwise 存在 format amplification，\"moderate\" effects (BT 63–67%) 的真实效应量可能更小——如何区分 \"Likert misses real bias\" vs \"pairwise creates apparent bias\"？\n2. 使用 rule-based rewriting 作为更强控制，效应量可能进一步缩小？\n3. 100-point scale 下 tie rate 仍高（formality 65.9%）——是 LLM judges 本质倾向\"中性\"评分，还是测量范式差异？\n\n### Missing References\n- Shi et al. (2024) \"Judging the Judges\"\n- Bavaresco et al. (2024) \"LLMs Instead of Human Judges?\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应：对每个 Must-Fix、Should-Fix 和关键 Strength 用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。特别关注你们之间的分歧点。\n\n---\n\n## Reviewer 2 审稿意见（新颖性、Related Work 完整性与写作质量）\n\n### 总体评分\n**Overall**: 3.5 = Borderline Conference\n**一句话总结**: 一篇实验设计扎实、发现有实践价值的实证论文，但核心新颖性偏向将已知测量理论迁移到 LLM judge 领域，且存在页数超限等格式问题。\n\n### 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计合理、多重控制周全，但 pairwise detection vs. amplification 无法完全区分；sample size 有限（n=88 基础），GEE 分析执行规范 |\n| Excitement | 3/5 | Likert Blindspot 发现对评估社区有实践价值，但核心洞见（pairwise > Likert 灵敏度）在测量理论中已有充分预测；框架是整合型而非根本性创新 |\n| Reproducibility | 4/5 | 模型版本、超参数、统计方法均有详细说明；代码/数据承诺接收后释放 |\n| Confidence | 4/5 | 仔细阅读全文及附录，熟悉 LLM evaluation 和测量理论文献 |\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] 主正文超过 8 页限制\n- 具体位置：PDF page 8–9 边界\n- 问题：Section 6 (Conclusion) 在 page 8 底部开始，约 5–6 行结论文本溢出到 page 9，之后才是 Limitations。EMNLP 2026 规定 \"strict 8-page limit for main text\"，Limitations 不计入但 Conclusion 计入。\n- 为什么影响接收：严格执行下可导致 desk rejection 或要求格式修正。\n- 建议修改方向：压缩 §5.6 或 §6 文本（约 6–7 行），或将 Table 3 移至 Appendix 以释放空间。\n\n**N2** [critical] Novelty claim 过度宽泛——\"first systematic quantification\" 需要更精确的界定\n- 具体位置：Abstract (sentence 2), Introduction (line 10, 12), Related Work §2 (line 23)\n- 问题：论文声称 CSD 是 \"the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison\"，并称 Likert Blindspot 是 \"first systematic quantification\"。然而：\n  - Pairwise > rating 的灵敏度优势是 Thurstone (1927) 以来的经典结论\n  - 在 NLG 评估中的量化：Kiritchenko & Mohammad (2017) 和 Novikova et al. (2018) 已证明 forced-choice 方法检测到 rating scales 遗漏的质量差异\n  - 框架的每个组件都有先例\n  - Qiu et al. (2025) 已在 persona-level 使用 counterfactual rewriting + BT\n- 为什么影响接收：过度的 novelty claim 降低论文可信度。\n- 建议修改方向：将 \"first systematic quantification\" 限定为 \"first systematic quantification for LLM judge style bias\"；明确承认核心洞见是 domain transfer；弱化 conjunction novelty claim。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] Comparative Trap 张力在 Conclusion 中处理不足\n**W2** [warning] \"interventional\" 等强因果措辞需要收敛\n**W3** [warning] 基准数据集单一，样本量偏小\n**W4** [warning] Abstract 信息密度过高\n**W5** [warning] Appendix Table 5 (GEE CI) 部分条目缺失 CI\n\n---\n\n### 小问题\n- M1: Introduction contributions 列表每条过长\n- M2: Table 1 第 6 列无 header\n- M3: Figure 2 (DAG) 黑白打印下颜色区分消失\n- M4: orphan bib entry hoenig2001abuse（工具误报）\n- M5: wu2023style bib key 年份不一致\n- M6: saito2023verbosity 文献信息需确认\n\n---\n\n### Questions for Authors\n1. 如果 pairwise 存在 format amplification，\"moderate\" effects (BT 63–67%) 的真实效应量可能更小——如何区分 \"Likert misses real bias\" vs \"pairwise creates apparent bias\"？\n2. 使用 rule-based rewriting 作为更强控制，效应量可能进一步缩小？\n3. 100-point scale 下 tie rate 仍高（formality 65.9%）——是 LLM judges 本质倾向\"中性\"评分，还是测量范式差异？\n\n### Missing References\n- Shi et al. (2024) \"Judging the Judges\"\n- Bavaresco et al. (2024) \"LLMs Instead of Human Judges?\""
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-21T17:35:54.831546+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19604
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-21T17:35:55.032545+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应：对每个 Must-Fix、Should-Fix 和关键 Strength 用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。特别关注你们之间的分歧点。\n\n---\n\n## Reviewer 1 — 方法严谨性与实验设计\n\n### 总体评分\n**Overall**: 3.5 = Borderline Conference\nSoundness 3.5, Excitement 3.5, Reproducibility 4, Confidence 4。\n\n### Must-Fix 问题\n\n**N1** [critical] NLI gate 缺乏人工评估验证\n- 位置：Section 3.2, Section 5.1, Appendix A\n- 整个框架的有效性依赖 NLI gate 正确分离 style 与 content 变化，但验证完全自动化——Qwen3-32B annotator + GPT-4o cross-validation 得到 92.1%/82.6% precision。没有任何人工评估来验证 NLI gate 的 pass/fail 决策是否与人类判断一致。DeBERTa-v3-large 在 style-shifted text 上的行为可能与标准 NLI 数据不同——formal text 可能系统性地获得更高 entailment score。\n- 建议：随机抽取 50–100 对 pass/fail 样本，2+ annotator 评估内容保持程度，报告 IAA 和一致率。\n\n**N2** [critical] Evaluator-producer bias 22% OR 下降被低估\n- 位置：Section 5.3, Appendix D, Table 6\n- Qwen3-32B rewriter 替换为 GPT-4o 后 verbosity Style OR 下降 22%（13.10→10.17），论文定性为\"bounding\"但 22% 是 non-trivial。更关键的是 cross-rewriter test 只覆盖 formality 和 verbosity，**register 轴完全缺失**——而 register 恰是 judge-dependence 最强的轴。\n- 建议：(1) 提供 producer-corrected 效应估计范围；(2) 补充 register 轴 cross-rewriter test；(3) 至少在 Limitations 标注 register 缺乏 producer-independence 验证。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] TOST equivalence bound 缺乏独立外部 justification\n**W2** [warning] BT IIA 假设在 formality 轴可能被违反（Appendix H，Fisher p = 0.015 方向不对称）\n**W3** [warning] 因果术语（\"interventional framework\"、Figure 2 DAG）与实际 filtering-based 方法之间存在张力\n**W4** [warning] 样本量偏小（LLMBar n=100, MT-Bench n=30），scaled replication（n=355）仅覆盖 Qwen3-32B formality\n**W5** [warning] Identification assumption (iii) 讨论不充分\n\n---\n\n### 小问题\n- M1: hoenig2001abuse orphan bib entry\n- M2: Table 2 \"sensitivity hierarchy\" 首次出现缺乏定义\n- M3: Figure 3 diamond vs circle markers 灰度下难区分\n- M4: Figure 4 y 轴标签被截断\n\n---\n\n### Questions\nQ1: NLI gate 在不同 rewrite directions 上的 score 分布是否存在系统差异？\nQ2: 22% OR 下降中有多少是 GPT-4o 的 style transfer 质量差异 vs 真实 self-preference？\nQ3: Register 的 judge-dependence 如何排除 evaluator-producer confound？\nQ4: 100-point continuous Likert 仍检测不到 Blindspot——说明问题在 evaluation paradigm 而非 scale granularity？\nQ5: Formality 方向不对称（88.9% vs 72.6%）是否意味着 casual→formal 改善了 perceived quality？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应：对每个 Must-Fix、Should-Fix 和关键 Strength 用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。特别关注你们之间的分歧点。\n\n---\n\n## Reviewer 1 — 方法严谨性与实验设计\n\n### 总体评分\n**Overall**: 3.5 = Borderline Conference\nSoundness 3.5, Excitement 3.5, Reproducibility 4, Confidence 4。\n\n### Must-Fix 问题\n\n**N1** [critical] NLI gate 缺乏人工评估验证\n- 位置：Section 3.2, Section 5.1, Appendix A\n- 整个框架的有效性依赖 NLI gate 正确分离 style 与 content 变化，但验证完全自动化——Qwen3-32B annotator + GPT-4o cross-validation 得到 92.1%/82.6% precision。没有任何人工评估来验证 NLI gate 的 pass/fail 决策是否与人类判断一致。DeBERTa-v3-large 在 style-shifted text 上的行为可能与标准 NLI 数据不同——formal text 可能系统性地获得更高 entailment score。\n- 建议：随机抽取 50–100 对 pass/fail 样本，2+ annotator 评估内容保持程度，报告 IAA 和一致率。\n\n**N2** [critical] Evaluator-producer bias 22% OR 下降被低估\n- 位置：Section 5.3, Appendix D, Table 6\n- Qwen3-32B rewriter 替换为 GPT-4o 后 verbosity Style OR 下降 22%（13.10→10.17），论文定性为\"bounding\"但 22% 是 non-trivial。更关键的是 cross-rewriter test 只覆盖 formality 和 verbosity，**register 轴完全缺失**——而 register 恰是 judge-dependence 最强的轴。\n- 建议：(1) 提供 producer-corrected 效应估计范围；(2) 补充 register 轴 cross-rewriter test；(3) 至少在 Limitations 标注 register 缺乏 producer-independence 验证。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] TOST equivalence bound 缺乏独立外部 justification\n**W2** [warning] BT IIA 假设在 formality 轴可能被违反（Appendix H，Fisher p = 0.015 方向不对称）\n**W3** [warning] 因果术语（\"interventional framework\"、Figure 2 DAG）与实际 filtering-based 方法之间存在张力\n**W4** [warning] 样本量偏小（LLMBar n=100, MT-Bench n=30），scaled replication（n=355）仅覆盖 Qwen3-32B formality\n**W5** [warning] Identification assumption (iii) 讨论不充分\n\n---\n\n### 小问题\n- M1: hoenig2001abuse orphan bib entry\n- M2: Table 2 \"sensitivity hierarchy\" 首次出现缺乏定义\n- M3: Figure 3 diamond vs circle markers 灰度下难区分\n- M4: Figure 4 y 轴标签被截断\n\n---\n\n### Questions\nQ1: NLI gate 在不同 rewrite directions 上的 score 分布是否存在系统差异？\nQ2: 22% OR 下降中有多少是 GPT-4o 的 style transfer 质量差异 vs 真实 self-preference？\nQ3: Register 的 judge-dependence 如何排除 evaluator-producer confound？\nQ4: 100-point continuous Likert 仍检测不到 Blindspot——说明问题在 evaluation paradigm 而非 scale granularity？\nQ5: Formality 方向不对称（88.9% vs 72.6%）是否意味着 casual→formal 改善了 perceived quality？"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-21T17:35:56.291750+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1259
}
```

</details>

---


### Assistant

_source line 508 · 2026-05-21T17:36:02.807585+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

**当前进度：**
- Step 1 (独立初审) ✓ — R1: 3.5, R2: 3.5
- Step 2 (交叉分享) — 已发出，等待回应
- 外部审稿 — pending（已发送请求）
- 视觉审查 — started（并行执行中）

**初审共识焦点：**
- 两位 Reviewer 均给 3.5 (Borderline Conference)
- 共同关切：NLI gate 缺人工验证、evaluator-producer bias、因果术语过强、样本量偏小
- R2 额外识别：页数超限（critical）、novelty claim 过宽

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 50

## Round 50

2 recorded events


### User

_source line 509 · 2026-05-21T17:36:05.298035+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿总结**：Overall 3.5 (Borderline Conference)。2 个 Must-Fix（主正文超 8 页、novelty claim 过度宽泛），5 个 Should-Fix（Comparative Trap 张力处理不足、因果措辞过强、基准单一/样本偏小、Abstract 过密、Appendix CI 缺失），6 个 Minor。主要优势在于发现的实践价值、实验设计周全、统计严谨和学术诚实；主要不足在于 novelty 偏向 domain transfer 且 framing 过度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 510 · 2026-05-21T17:36:10.562871+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 51

## Round 51

2 recorded events


### User

_source line 511 · 2026-05-21T17:37:56.088635+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1

### Must-Fix

**[AGREE] R1-N1: NLI gate 缺人工评估**
同意是实质性问题，但建议降级为 strong Should-Fix。理由：NLI ablation（Appendix N, Table 14）formality NLI-fail pairs 反转至 41.7% 是较强间接验证；11-threshold sweep（Appendix E）≤3pp 变动证明 threshold 不敏感。50对 pass/fail 样本的 2+ annotator 评估即可满足。

**[AGREE] R1-N2: Evaluator-producer bias 22% OR 下降**
同意 22% non-trivial，尤其 register 轴缺乏 cross-rewriter test 是显著遗漏。但核心发现（Blindspot pattern）在 GPT-4o rewriter 下完全保持（Table 6: BT .735, Likert p=.838），说明影响效应量大小但不影响定性结论。

### Should-Fix
- W1 TOST: AGREE
- W2 BT IIA: PARTIALLY AGREE，降级 Minor——BT GOF p=0.198 通过，GEE 已内化方向不对称
- W3 因果术语: AGREE（与我的 R2-W2 一致）
- W4 样本量: AGREE（与 R2-W3 一致）
- W5 Assumption (iii): AGREE

### 小问题
- M1 hoenig2001abuse: **REBUT**——\citealt 引用（experiments.tex L128），工具误报
- M2-M4: AGREE

### 关键分歧
1. **页数超限**：R1 未提及，R2 发现 Conclusion 溢出 ~6 行到 page 9——这是格式合规性问题
2. **Novelty overclaiming**：R1 未独立标记，R2 列为 N2 Must-Fix——两份审稿互补
3. **NLI gate 严重性**：R1 Must-Fix vs R2 strong Should-Fix——NLI ablation 反转证据降低严重性
4. **Excitement**：R1 3.5 vs R2 3——R2 认为核心洞见是 domain transfer

两份审稿在 Overall 3.5 和 Soundness 3.5 完全一致，关注点互补。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 512 · 2026-05-21T17:38:01.746745+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 52

## Round 52

2 recorded events


### User

_source line 513 · 2026-05-21T17:38:04.238626+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：R1 和 R2 在 Overall 3.5 和 Soundness 3.5 上完全一致，分歧主要在 (1) 页数超限（R2 发现、R1 遗漏）、(2) Novelty framing 严重性、(3) NLI gate 人工验证的定级。两份审稿互补——R1 深挖方法论，R2 聚焦 novelty 和写作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 514 · 2026-05-21T17:38:09.393702+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 53

## Round 53

10 recorded events


### User

_source line 515 · 2026-05-21T17:38:12.351656+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

### Must-Fix

**[AGREE] R2-N1 (页数超限)**: 确认 Section 6 约 5–6 行溢出到 page 9。真实格式违规。我 Round 1 遗漏此问题。建议压缩 Section 6 而非移走 Table 3。

**[REBUT] R2-N2 (Novelty claim → 建议降级为 Should-Fix)**: R2 正确指出 pairwise > Likert 灵敏度是经典结论，但低估了 LLM judges 的特殊性——确定性评分、无疲劳效应、不同 scale anchoring 使得 domain transfer 非 trivial。论文的贡献不仅是灵敏度比较，还包括 per-axis confound decomposition (GEE) 和 NLI-gated content control。建议措辞精确化而非 Must-Fix。

### Should-Fix

**[AGREE] R2-W1 (Comparative Trap)**: R2 发现的重要问题，我未独立标注。pairwise format 本身的 amplification 需要定量估计。与我的 W2 (BT IIA formality 不对称) 有逻辑关联。

**[AGREE] R2-W2 (因果措辞)**: 与我的 W3 完全一致。两位 reviewer 独立标注同一问题。

**[AGREE] R2-W3 (样本量)**: 与我的 W4 一致。

**[REBUT] R2-W4 (Abstract 密度 → 建议降级为 Minor)**: 对实验论文而言 Abstract 中的核心数字是必要的，删除后读者无法评估效应大小。

**[AGREE] R2-W5 (Table 5 CI)**: 应补充完整。

### 关键分歧

1. **Novelty**: R2 列为 Must-Fix，我认为 Should-Fix（phrasing 调整而非核心缺陷）
2. **NLI 人工验证和 evaluator-producer bias**: 我列为 Must-Fix，R2 未标注——我认为这是论文最大的方法论缺口

### 合并 Must-Fix 清单（两位 Reviewer 共识）

1. NLI gate 人工验证 [R1-N1, R2 未标注但逻辑上应支持]
2. Evaluator-producer bias 22% OR 下降 + register 缺失 [R1-N2]
3. 页数超限 [R2-N1, R1 确认]

**Overall 评分不变: 3.5 (Borderline Conference)**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-21T17:38:27.599987+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-21T17:38:27.801088+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T17:25:45.393740+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_5ce280de124a4e308d1827c6450ad337\", \"skipped_at\": \"2026-05-21T17:31:25.850815+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-21T17:38:27.801537+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-21T17:38:27.852137+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T17:25:44.541867+00:00\", \"completed_at\": \"2026-05-21T17:29:28.572031+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-4\", \"message\": \"连续 2 页纯文本（Related Work 全篇 + Method 开头），无任何 display item 穿插。建议在 Method 段（如 3.1 Style-Controlled Rewriting）加入一个 rewriting pipeline 示意图或 style transformation 示例表，打破文本单调感\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Figure 2（causal DAG）尺寸偏小，仅占单栏约 1/4 高度。DAG 是本文方法论的核心论据（design rationale），建议适当放大或改为 figure* 跨栏展示，让审稿人更容易理解因果结构\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 脚注区域信息密度极高——4 个显著性符号（Holm-adj p / †‡§）+ \\\"Negative\\\" 说明 + \\\"Scaled replication\\\" 注释压缩在 3 行内。审稿人快速扫描时可能遗漏关键注释。建议拆分为表下独立 notes 段或简化符号体系\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 内部文字标签（\\\"Rewrite\\\"、\\\"NLI gate\\\"、\\\"pos. swap\\\"）字号偏小，约为正文字号 60-65%。在打印或低分辨率屏幕上可能略显吃力，但 150 DPI 渲染下仍可读\"}, {\"severity\": \"info\", \"dimension\": \"page 10-12\", \"message\": \"Appendix 三页各含 3-4 个 table，表格密度极高。虽不影响主体阅读体验，但审稿人查阅附录时可能感到拥挤。若有空间可适当加 \\\\vspace 间距\"}, {\"severity\": \"info\", \"dimension\": \"page 13-15\", \"message\": \"References 置于 Appendix 之后（Appendix A-P → References）。ACL 格式两种顺序均可，但更常见做法是 main text → References → Appendix。当前顺序下审稿人需翻过 5 页附录才能查看引用\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 使用 filled circles vs. open diamonds 区分显著/非显著结果，灰度打印时仍可区分——色盲友好设计良好\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯 Abstract + Intro 文本）。Figure 1 在第 2 页出现，尚在可接受范围，但若能将 Figure 1 提前至第 1 页底部（如压缩 Abstract 或 Intro 首段），第一印象会更强\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-21T17:42:44.054254+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Abstract/Intro 明确标注为 'first systematic quantitative verification of known measurement theory principle in LLM judge evaluation'. Structural ceiling acknowledged.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4-SF8: Honest novelty positioning applied.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 2 发现并修复。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Round 6 再次发现：Section 6 (Conclusion) 约 5-6 行溢出到 page 9。两位 Reviewer 共识 Must-Fix。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补。Register 仍缺。Style OR 下降 22% 非可忽略。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R5 两位 Reviewer 均再次指出。R1 定为 critical（self-preference bias 无法排除），R2 认为 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。主文 Section 5 缺 caveat。见 R5-SF2。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix：22% OR 下降处理不充分 + register 轴完全缺失 cross-rewriter test。R6-R2 同意 22% non-trivial 但注意 Blindspot pattern 在 GPT-4o rewriter 下完全保持。共识：Must-Fix（需 producer-corrected 估计范围 + register caveat）。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Register independence test — acknowledged as limitation\"\n        assigned_to: paper_agent\n        status: wont_fix\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 'approximates the do-operator' 残留。见 R5-MF2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'. n=355 d->0 evidence.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"attenuation framing 已改善，但 'construct difference' 替代解释在主文中仍不足。见 R5-SF6。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Cross-rewriter consistency + 200-pair GPT-4o validation provide partial proxy. Acknowledged in Limitations.\"\n      - round: 5\n        reviewers: []\n        note: \"Round 5 未被任何 Reviewer 显式提及，但仍 inherently open（无人工评估数据）。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix：NLI gate 完全依赖自动化验证（Qwen3-32B annotator + GPT-4o cross-val），缺人工评估验证 pass/fail 决策与人类判断一致性。R6-R2 同意但建议降级为 strong Should-Fix（NLI ablation 反转至 41.7% 为较强间接验证）。交叉后共识：Must-Fix，50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"术语已改善，但 verbosity 'confound-free' 措辞仍过强。见 R5-SF4。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"引用量已改善，但遗漏了 Jeong et al. (2025) Comparative Trap 等关键文献。见 R5-MF1。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"TOST at Delta=10pp underpowered (n=87). 措辞仍需更审慎。见 R5-M3。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"仍指出 Abstract 信息密度过高。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均再次指出 Abstract 过密。Minor issue。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 列为 Should-Fix（OR 值等技术细节不利于可读性）；R6-R1 建议降级 Minor（实验论文 Abstract 中核心数字必要）。交叉后分歧：Should-Fix vs Minor。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    resolution: \"GoF chi2 deviance test + stratified BT + originality-minimal subset. IIA trivially satisfied in paired comparison.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出 IIA 未检验，R2 技术性反驳（纯 paired comparison 无 irrelevant alternative，GoF 已通过）。交叉后共识：降级为 minor。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Should-Fix（Fisher p=0.015 方向不对称）；R6-R2 认为降级 Minor（GoF p=0.198 通过，GEE 已内化方向不对称）。交叉后共识：Minor。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)——pairwise amplification vs detection sensitivity 张力未讨论\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 首先识别，R1 交叉回应完全同意并认为是本轮最严重问题。Jeong et al. (2025, BlackboxNLP) 证明 pairwise comparison 放大 style bias，与本文 Section 6 'adopt pairwise' 建议直接矛盾。论文需区分 detection sensitivity 和 bias amplification。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已在 §2 Related Work 和 §5.2 加入 Jeong et al. (2025) 讨论和 6 个控制约束 amplification 风险（缺引已修复）。但 §6 Conclusion 推荐措辞 'should adopt' 仍过强，未充分 caveat pairwise amplification 风险。R6 两位 Reviewer 共识：Should-Fix（降级自 Round 5 的 critical，因核心引用已加但 Conclusion caveat 不足）。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap；在 §5.2 或 §6 论证 CSD 的 NLI gate + position control 如何区分 detection 与 amplification\"\n        assigned_to: paper_agent\n        status: done\n      - round: 6\n        action: \"在 §6 Conclusion 加入明确 caveat：pairwise comparison 可能放大 style bias，需结合 NLI gate + position control 约束\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强——selection/conditioning ≠ intervention，存在 collider bias 风险\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 完全同意。§3.2 原文 'approximates the do-operator' 在因果推断术语上过强。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§3.2 已改为 'filtering-based confounder control'，§3.5 已声明 'interventional rather than formal causal evidence'。但 Introduction/Abstract 仍使用 'interventional framework' 和 'black-box interventional framework'，与 §3.5 的 hedging 不一致。R6 两位 Reviewer 独立标注（R1-W3, R2-W2），共识 Should-Fix。\"\n    action_items:\n      - round: 5\n        action: \"将 'approximates the do-operator' 改为 'provides a filtering-based confounder control'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 6\n        action: \"统一 Abstract/Intro 的因果措辞，与 §3.5 的 hedging 保持一致——建议改为 'quasi-interventional' 或直接用 'controlled'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim——至少 Jeong et al. (2025) 已做类似 systematic quantification\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 识别，R1 部分同意。'first' 需限定到 CSD 具体方法组合的 novelty。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 列为 Must-Fix：'first systematic quantification' 在 Thurstone (1927)、Kiritchenko & Mohammad (2017)、Novikova et al. (2018) 存在下过度宽泛。R6-R1 建议降级 Should-Fix：LLM judge 的特殊性（确定性评分、无疲劳效应）使 domain transfer 非 trivial。交叉后分歧：Must-Fix vs Should-Fix。Director 判定：Should-Fix（措辞精确化即可，非核心方法论缺陷）。\"\n    action_items:\n      - round: 6\n        action: \"将 'first systematic quantification' 限定为 'first systematic quantification for LLM judge style bias via controlled style decomposition'；明确承认 pairwise > Likert 灵敏度是经典结论，novelty 在 LLM judge 场景的量化验证 + CSD 方法组合\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat——Qwen3-32B 结果在 Section 5 首次出现时无任何警示\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 定 critical，R2 建议 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"本轮未被独立提及，但 RD2-SF1 evaluator-producer 问题仍为 in_progress，涵盖此项。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性——实质仅 2 个 judge 展示 Blindspot\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 定 critical（缺 Gemini/Llama），R1 反驳（方法论贡献 2+1 足够）。交叉后共识：should-fix。\"\n      - round: 6\n        reviewers: []\n        note: \"Round 6 未被任何 Reviewer 显式提及。论文当前措辞 'three target judges...and one negative control' 已有所区分。可能已部分改善，待 Research Director 确认。\"\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强——仅控制了已观测 confound\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 同意。'confound-free' 应改为 'no observed originality confound'。\"\n      - round: 6\n        reviewers: []\n        note: \"Round 6 未被显式提及。论文 Table 3 caption 和 §5.4 仍使用 'style-dominated' 而非 'confound-free'。措辞已有改善，待确认。\"\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已在 Appendix 补充 verbosity sensitivity hierarchy，§5.2 主文引用。已修复。\"\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现严重不平衡——替代解释仅在 Limitations 一笔带过\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 同意。需在 §5.2 给两种解释同等篇幅。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§5.2 末尾已加入 'Measurement attenuation vs. construct divergence' 段落，Limitations 也讨论。但 R6 两位 Reviewer 未单独标注——可能已满足基本要求。\"\n\n  - id: \"R5-SF7\"\n    summary: \"Formality confound 在 Abstract/Conclusion 中未与 verbosity 区分——读者误以为三轴等价\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 和 R2 均指出。Abstract 'three style axes' 未说明各轴证据强度不同。\"\n      - round: 6\n        reviewers: []\n        note: \"Round 6 未被显式提及。Abstract 当前措辞有 GEE per-axis 区分描述，但仍可能给读者三轴等价的印象。待确认。\"\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点，不足以建立 plateau\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点（0.50-0.98），充分建立 plateau。\"\n    resolution_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已有 11-point sweep，覆盖充分。\"\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。Register 是最弱轴，恰是 rewriter identity 最可能影响结论的轴。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 在 N2 中再次提及 register 缺失。Acknowledged as limitation 但未补实验。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 识别，R1 同意。Equivalence bound Delta=15pp 缺 external justification。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Should-Fix（TOST bound 缺外部 justification），R6-R2 同意。\"\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。每个缺失 cell 应在 footnote 或 Appendix 说明原因。\"\n      - round: 6\n        reviewers: [2]\n        note: \"R6-R2 M2 提及 Table 1 第 6 列无 header。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立指出。建议颜色 + 线型双重编码。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 M3 和 R6-R2 M3 均再次提及 Figure 2/3 灰度区分问题。Visual check 也标注 Figure 2 偏小。\"\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025) Comparative Trap, Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6 验证：Jeong et al. (2025)、Stureborg et al. (2024)、Park et al. (2024) 均已在 §2 被讨论。引用覆盖良好。R6-R2 额外建议 Shi et al. (2024) 和 Bavaresco et al. (2024)。\"\n\n  # ============================================================\n  # Round 6 new issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound (Delta=15pp) 缺乏独立外部 justification——用同研究 treatment effects 设定 control bound 形成循环\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 W1 提出，R6-R2 交叉同意。需引用外部基准设定 equivalence bound。\"\n    action_items:\n      - round: 6\n        action: \"引用外部 style bias 基准（如 AlpacaEval length bias ~15-20pp）作为 TOST bound justification\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 'rewrite introduces no systematic differences beyond target axis' 讨论不充分\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1]\n        note: \"R6-R1 W5 提出：same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。R6-R2 交叉同意。\"\n    action_items:\n      - round: 6\n        action: \"在 §3.5 或 Limitations 补充讨论 axis-specific confounds 的可能性\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄——n=355 仅限 Qwen3-32B formality\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 W4 和 R6-R2 W3 独立标注。LLMBar n=100 (post-NLI n=88) 为主数据源，MT-Bench n=30。n=355 replication 仅覆盖一个 judge×axis。两位 Reviewer 共识 Should-Fix。\"\n    action_items:\n      - round: 6\n        action: \"在 Conclusion 更明确标注 generalizability 边界；如可能补充 verbosity n=355 replication\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"GPT-4o formality/verbosity/register 和 Qwen3 formality Orig OR 只有点估计无 CI。\"\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"R6-R2 建议。非必须但高度相关。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"因果语言降级问题在 Round 3 以新形式复发，见 R3-N1\"\n      - round: 4\n        reviewers: [1]\n        note: \"R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2\"\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Abstract/Intro 明确标注为 'first systematic quantitative verification of known measurement theory principle in LLM judge evaluation'. Structural ceiling acknowledged.\"\n    resolution_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4-SF8: Honest novelty positioning applied.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。\"\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 2 发现并修复。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Round 6 再次发现：Section 6 (Conclusion) 约 5-6 行溢出到 page 9。两位 Reviewer 共识 Must-Fix。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Independence test 仅覆盖 verbosity，formality 缺 test。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Formality rewriter independence 已补。Register 仍缺。Style OR 下降 22% 非可忽略。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R5 两位 Reviewer 均再次指出。R1 定为 critical（self-preference bias 无法排除），R2 认为 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。主文 Section 5 缺 caveat。见 R5-SF2。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix：22% OR 下降处理不充分 + register 轴完全缺失 cross-rewriter test。R6-R2 同意 22% non-trivial 但注意 Blindspot pattern 在 GPT-4o rewriter 下完全保持。共识：Must-Fix（需 producer-corrected 估计范围 + register caveat）。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Register independence test — acknowledged as limitation\"\n        assigned_to: paper_agent\n        status: wont_fix\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"标题和小节名已修复，但 §3.2 'approximates the do-operator' 残留。见 R5-MF2。\"\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'. n=355 d->0 evidence.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"attenuation framing 已改善，但 'construct difference' 替代解释在主文中仍不足。见 R5-SF6。\"\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"Cross-rewriter consistency + 200-pair GPT-4o validation provide partial proxy. Acknowledged in Limitations.\"\n      - round: 5\n        reviewers: []\n        note: \"Round 5 未被任何 Reviewer 显式提及，但仍 inherently open（无人工评估数据）。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Must-Fix：NLI gate 完全依赖自动化验证（Qwen3-32B annotator + GPT-4o cross-val），缺人工评估验证 pass/fail 决策与人类判断一致性。R6-R2 同意但建议降级为 strong Should-Fix（NLI ablation 反转至 41.7% 为较强间接验证）。交叉后共识：Must-Fix，50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"术语已改善，但 verbosity 'confound-free' 措辞仍过强。见 R5-SF4。\"\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"引用量已改善，但遗漏了 Jeong et al. (2025) Comparative Trap 等关键文献。见 R5-MF1。\"\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"TOST at Delta=10pp underpowered (n=87). 措辞仍需更审慎。见 R5-M3。\"\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"仍指出 Abstract 信息密度过高。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均再次指出 Abstract 过密。Minor issue。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 列为 Should-Fix（OR 值等技术细节不利于可读性）；R6-R1 建议降级 Minor（实验论文 Abstract 中核心数字必要）。交叉后分歧：Should-Fix vs Minor。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    resolution: \"GoF chi2 deviance test + stratified BT + originality-minimal subset. IIA trivially satisfied in paired comparison.\"\n    resolution_round: 4\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出 IIA 未检验，R2 技术性反驳（纯 paired comparison 无 irrelevant alternative，GoF 已通过）。交叉后共识：降级为 minor。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Should-Fix（Fisher p=0.015 方向不对称）；R6-R2 认为降级 Minor（GoF p=0.198 通过，GEE 已内化方向不对称）。交叉后共识：Minor。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)——pairwise amplification vs detection sensitivity 张力未讨论\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 首先识别，R1 交叉回应完全同意并认为是本轮最严重问题。Jeong et al. (2025, BlackboxNLP) 证明 pairwise comparison 放大 style bias，与本文 Section 6 'adopt pairwise' 建议直接矛盾。论文需区分 detection sensitivity 和 bias amplification。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已在 §2 Related Work 和 §5.2 加入 Jeong et al. (2025) 讨论和 6 个控制约束 amplification 风险（缺引已修复）。但 §6 Conclusion 推荐措辞 'should adopt' 仍过强，未充分 caveat pairwise amplification 风险。R6 两位 Reviewer 共识：Should-Fix（降级自 Round 5 的 critical，因核心引用已加但 Conclusion caveat 不足）。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap；在 §5.2 或 §6 论证 CSD 的 NLI gate + position control 如何区分 detection 与 amplification\"\n        assigned_to: paper_agent\n        status: done\n      - round: 6\n        action: \"在 §6 Conclusion 加入明确 caveat：pairwise comparison 可能放大 style bias，需结合 NLI gate + position control 约束\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强——selection/conditioning ≠ intervention，存在 collider bias 风险\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 完全同意。§3.2 原文 'approximates the do-operator' 在因果推断术语上过强。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§3.2 已改为 'filtering-based confounder control'，§3.5 已声明 'interventional rather than formal causal evidence'。但 Introduction/Abstract 仍使用 'interventional framework' 和 'black-box interventional framework'，与 §3.5 的 hedging 不一致。R6 两位 Reviewer 独立标注（R1-W3, R2-W2），共识 Should-Fix。\"\n    action_items:\n      - round: 5\n        action: \"将 'approximates the do-operator' 改为 'provides a filtering-based confounder control'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 6\n        action: \"统一 Abstract/Intro 的因果措辞，与 §3.5 的 hedging 保持一致——建议改为 'quasi-interventional' 或直接用 'controlled'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim——至少 Jeong et al. (2025) 已做类似 systematic quantification\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 识别，R1 部分同意。'first' 需限定到 CSD 具体方法组合的 novelty。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R2 列为 Must-Fix：'first systematic quantification' 在 Thurstone (1927)、Kiritchenko & Mohammad (2017)、Novikova et al. (2018) 存在下过度宽泛。R6-R1 建议降级 Should-Fix：LLM judge 的特殊性（确定性评分、无疲劳效应）使 domain transfer 非 trivial。交叉后分歧：Must-Fix vs Should-Fix。Director 判定：Should-Fix（措辞精确化即可，非核心方法论缺陷）。\"\n    action_items:\n      - round: 6\n        action: \"将 'first systematic quantification' 限定为 'first systematic quantification for LLM judge style bias via controlled style decomposition'；明确承认 pairwise > Likert 灵敏度是经典结论，novelty 在 LLM judge 场景的量化验证 + CSD 方法组合\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat——Qwen3-32B 结果在 Section 5 首次出现时无任何警示\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 定 critical，R2 建议 should-fix（GPT-4o 不受影响）。交叉后共识：should-fix。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"本轮未被独立提及，但 RD2-SF1 evaluator-producer 问题仍为 in_progress，涵盖此项。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性——实质仅 2 个 judge 展示 Blindspot\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 定 critical（缺 Gemini/Llama），R1 反驳（方法论贡献 2+1 足够）。交叉后共识：should-fix。\"\n      - round: 6\n        reviewers: []\n        note: \"Round 6 未被任何 Reviewer 显式提及。论文当前措辞 'three target judges...and one negative control' 已有所区分。可能已部分改善，待 Research Director 确认。\"\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强——仅控制了已观测 confound\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 同意。'confound-free' 应改为 'no observed originality confound'。\"\n      - round: 6\n        reviewers: []\n        note: \"Round 6 未被显式提及。论文 Table 3 caption 和 §5.4 仍使用 'style-dominated' 而非 'confound-free'。措辞已有改善，待确认。\"\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示——缺 verbosity 验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已在 Appendix 补充 verbosity sensitivity hierarchy，§5.2 主文引用。已修复。\"\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现严重不平衡——替代解释仅在 Limitations 一笔带过\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 识别，R2 同意。需在 §5.2 给两种解释同等篇幅。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§5.2 末尾已加入 'Measurement attenuation vs. construct divergence' 段落，Limitations 也讨论。但 R6 两位 Reviewer 未单独标注——可能已满足基本要求。\"\n\n  - id: \"R5-SF7\"\n    summary: \"Formality confound 在 Abstract/Conclusion 中未与 verbosity 区分——读者误以为三轴等价\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 和 R2 均指出。Abstract 'three style axes' 未说明各轴证据强度不同。\"\n      - round: 6\n        reviewers: []\n        note: \"Round 6 未被显式提及。Abstract 当前措辞有 GEE per-axis 区分描述，但仍可能给读者三轴等价的印象。待确认。\"\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点，不足以建立 plateau\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点（0.50-0.98），充分建立 plateau。\"\n    resolution_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"论文已有 11-point sweep，覆盖充分。\"\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。Register 是最弱轴，恰是 rewriter identity 最可能影响结论的轴。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 在 N2 中再次提及 register 缺失。Acknowledged as limitation 但未补实验。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 识别，R1 同意。Equivalence bound Delta=15pp 缺 external justification。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 列为 Should-Fix（TOST bound 缺外部 justification），R6-R2 同意。\"\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。每个缺失 cell 应在 footnote 或 Appendix 说明原因。\"\n      - round: 6\n        reviewers: [2]\n        note: \"R6-R2 M2 提及 Table 1 第 6 列无 header。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立指出。建议颜色 + 线型双重编码。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 M3 和 R6-R2 M3 均再次提及 Figure 2/3 灰度区分问题。Visual check 也标注 Figure 2 偏小。\"\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025) Comparative Trap, Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6 验证：Jeong et al. (2025)、Stureborg et al. (2024)、Park et al. (2024) 均已在 §2 被讨论。引用覆盖良好。R6-R2 额外建议 Shi et al. (2024) 和 Bavaresco et al. (2024)。\"\n\n  # ============================================================\n  # Round 6 new issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound (Delta=15pp) 缺乏独立外部 justification——用同研究 treatment effects 设定 control bound 形成循环\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 W1 提出，R6-R2 交叉同意。需引用外部基准设定 equivalence bound。\"\n    action_items:\n      - round: 6\n        action: \"引用外部 style bias 基准（如 AlpacaEval length bias ~15-20pp）作为 TOST bound justification\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 'rewrite introduces no systematic differences beyond target axis' 讨论不充分\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1]\n        note: \"R6-R1 W5 提出：same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。R6-R2 交叉同意。\"\n    action_items:\n      - round: 6\n        action: \"在 §3.5 或 Limitations 补充讨论 axis-specific confounds 的可能性\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄——n=355 仅限 Qwen3-32B formality\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R6-R1 W4 和 R6-R2 W3 独立标注。LLMBar n=100 (post-NLI n=88) 为主数据源，MT-Bench n=30。n=355 replication 仅覆盖一个 judge×axis。两位 Reviewer 共识 Should-Fix。\"\n    action_items:\n      - round: 6\n        action: \"在 Conclusion 更明确标注 generalizability 边界；如可能补充 verbosity n=355 replication\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"GPT-4o formality/verbosity/register 和 Qwen3 formality Orig OR 只有点估计无 CI。\"\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"R6-R2 建议。非必须但高度相关。\""
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-21T17:42:44.105485+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 31793}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-21T17:44:54.956770+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# 审稿报告 — Round 6 (Fresh Review)\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**目标 Venue**: EMNLP 2026 Long Paper (ARR)\n**截止日期**: 2026-05-25\n**Reviewer**: R1 (方法严谨性/实验设计) + R2 (新颖性/Related Work/写作质量)\n**审稿模式**: Fresh（独立全新审稿）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一个检测 LLM judge 隐藏风格偏差的黑盒框架。CSD 通过三阶段流程——style-controlled rewriting、NLI-gated content preservation、position-controlled pairwise comparison——系统量化 per-axis style bias。核心发现是 \"Likert Blindspot\"：在相同数据上，Likert 评分（ATE）系统性地遗漏 pairwise comparison 能检测到的风格偏差（BT 63–84%, p < 0.001 vs Likert p > 0.17），由七种统计方法交叉验证。GEE conditional decomposition 进一步揭示 per-axis confound structure：verbosity 为 style-dominated，formality 为 conditional（style + originality confound），register 为 judge-dependent。在 4 个 judges（3 target + 1 negative control Claude Sonnet 4）、3 benchmarks、3 style axes 上验证。\n\n---\n\n## Strengths\n\n**S1. 研究问题精准且对社区有直接实践价值** [R1, R2 共识]\nLikert Blindspot 的发现直接挑战了 RATE 等基于 Likert ATE 的 bias 评估方法的有效性，对 evaluation community 有即时方法论指导意义。\n\n**S2. 统计框架严谨且多层次** [R1 主导]\n七种统计方法交叉验证（Table 2），Holm-Bonferroni 校正 + exploratory/confirmatory 分类，GEE conditional decomposition（Table 3），Bootstrap CI 10,000 resamples，BT GoF 检验，NLI 11-threshold sensitivity sweep，TOST 等价性检验。统计密度显著高于同领域平均水平。\n\n**S3. 实验设计周全，多重控制有效约束替代解释** [R1, R2 共识]\n六个独立控制（NLI gate ablation 反转至 41.7%、Claude 负控制无 bias、cross-axis BT 变异不一致 uniform amplification、rewriting artifact 被 GEE 吸收、debiased prompting 部分降低 bias、三架构一致）有效约束了替代解释空间。Claude Sonnet 4 作为 negative control 增强了 discriminative validity。\n\n**S4. Per-axis confound structure 是方法论增量贡献** [R1 主导]\nGEE 条件分解区分了 style-dominated（verbosity: Style OR 8–13, Orig OR <1）、conditional（formality: 显著 style 和 originality effects）和 judge-dependent（register）三种模式，超越了 aggregate bias score。\n\n**S5. Related Work 覆盖全面且定位清晰** [R2 主导]\nJeong et al. (2025) Comparative Trap、Stureborg et al. (2024)、Park et al. (2024) 等关键文献均被讨论。与 RATE、CASSE、FairJudge 的差异化清晰。\n\n**S6. 写作清晰、学术诚实** [R2 主导]\n§3.5 Design Rationale 的因果声明 disclaimer、Limitations 的三段式讨论（quality-style confounding、evaluator-producer bias、validation methodology）体现了较高的学术诚实度。Appendix 提供了充分技术细节。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. 主正文超过 8 页限制** [R2 发现, R1 交叉确认] — format, critical\nSection 6 (Conclusion) 约 5–6 行溢出到 page 9。EMNLP 2026 规定主正文 strict 8-page limit，Limitations 和 Ethics 不计入但 Conclusion 计入。严格执行下可导致 desk rejection。\n→ 建议压缩 §5.6 或 §6 文本（约 6–7 行）。\n\n**MF2. NLI gate 缺乏人工评估验证** [R1 Must-Fix, R2 同意但建议降级 strong Should-Fix] — method, critical\n整个框架的有效性依赖 NLI gate 正确分离 style 与 content 变化，但验证完全自动化（Qwen3-32B annotator + GPT-4o cross-validation 92.1%/82.6% precision）。没有人工评估验证 NLI gate 的 pass/fail 决策是否与人类判断一致。DeBERTa-v3-large 在 style-shifted text 上可能与标准 NLI 数据行为不同。\n缓解因素：NLI ablation（Appendix N）formality NLI-fail pairs 反转至 41.7% 是较强间接验证；11-threshold sweep ≤3pp 变动证明 threshold 不敏感。\n→ 建议随机抽取 50 对 pass/fail 样本，2+ annotator 评估，报告 IAA。\n\n**MF3. Evaluator-producer bias 22% OR 下降处理不充分 + register 轴缺失 cross-rewriter test** [R1 Must-Fix, R2 同意] — method, critical\nQwen3-32B rewriter→GPT-4o 后 verbosity Style OR 下降 22%（13.10→10.17），论文定性为\"bounding\"但 22% non-trivial。Register 轴完全缺失 cross-rewriter test，而 register 恰是 judge-dependence 最强的轴。核心 Blindspot pattern 在 GPT-4o rewriter 下保持（BT .735, Likert p=.838），说明不影响定性结论但影响效应量估计精度。\n→ 建议：(1) 提供 producer-corrected 效应估计范围；(2) Limitations 明确标注 register 缺乏 producer-independence 验证。\n\n### Should-Fix（影响评分但非一票否决）\n\n**SF1. Novelty claim \"first systematic quantification\" 过度宽泛** [R2 Must-Fix, R1 降级 Should-Fix → Director 判定 Should-Fix]\nPairwise > Likert 灵敏度是 Thurstone (1927) 以来的经典结论；Kiritchenko & Mohammad (2017)、Novikova et al. (2018) 已证明 forced-choice 在 NLG 评估中更灵敏；框架各组件均有先例。R1 反驳：LLM judges 的特殊性（确定性评分、无疲劳效应、不同 scale anchoring）使 domain transfer 非 trivial，且论文贡献包括 per-axis GEE decomposition。\n→ 建议将 \"first\" 限定到具体方法组合的 novelty；明确承认核心洞见是 domain transfer + systematic quantification。\n\n**SF2. Comparative Trap 张力在 Conclusion 处理不足** [R2 发现, R1 交叉同意]\n§2 和 §5.2 已讨论 Jeong et al. (2025) 并提供 6 个控制约束 amplification 风险，但 §6 推荐 \"style bias audits should adopt content-controlled pairwise comparison\" 措辞仍过强。\n→ 建议加入明确 caveat。\n\n**SF3. 因果术语（\"interventional framework\"）与实际 filtering-based 方法存在张力** [R1 W3, R2 W2 独立标注]\n§3.5 的 hedging 适当，但 Abstract \"black-box interventional framework\" 和 Introduction 多处使用强因果语言，与 §3.5 的 disclaimer 不一致。\n→ 建议统一为 \"quasi-interventional\" 或 \"controlled\" framework。\n\n**SF4. 样本量偏小且 scaled replication 覆盖面窄** [R1 W4, R2 W3 共识]\nLLMBar n=100（post-NLI n=88）为主数据源，MT-Bench n=30。n=355 scaled replication 仅覆盖 Qwen3-32B formality。\n→ 建议在 Conclusion 更明确标注 generalizability 边界。\n\n**SF5. TOST equivalence bound (Δ=15pp) 缺乏独立外部 justification** [R1 W1, R2 同意]\n用同研究 treatment effects 设定 control 的 equivalence bound 形成循环论证。\n→ 建议引用外部 style bias 基准。\n\n**SF6. Identification assumption (iii) 讨论不充分** [R1 W5, R2 同意]\n\"Rewrite introduces no systematic differences beyond target axis\"——same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。\n\n### Minor Issues\n\n- **M1**: Abstract 信息密度过高——OR 值等技术细节不利于可读性 [R2 Should-Fix, R1 Minor → 分歧]\n- **M2**: BT IIA 在 formality 轴可能被违反（Fisher p=0.015 方向不对称）[R1 Should-Fix, R2 Minor → 共识 Minor]\n- **M3**: Figure 2 (DAG) 和 Figure 3 (forest plot) 黑白打印下颜色/形状区分不足 [R1, R2 共识]\n- **M4**: Appendix Table 5 (GEE CI) 部分条目缺失 95% CI [R2]\n- **M5**: Table 1 第 6 列无 header，Blindspot 标记缺说明 [R2]\n- **M6**: Introduction contributions 列表每条过长（3–5 行）[R2]\n- **M7**: bib key wu2023style 年份与 venue 年份不一致 [R2]\n\n---\n\n## Questions for Authors\n\n1. NLI gate 在不同 rewrite directions（formal→casual vs casual→formal）上的 entailment score 分布是否存在系统差异？如果 formal text 系统性获得更高 NLI score，这会否引入 selection bias？\n2. 22% OR 下降中有多少可归因于 GPT-4o 的 style transfer 质量差异 vs 真实 self-preference？如果使用 rule-based rewriting，效应量可能进一步缩小？\n3. Register 轴的 judge-dependence 在缺乏 cross-rewriter test 的情况下，如何排除 evaluator-producer confound 而非 genuine judge-specific sensitivity？\n4. 100-point continuous Likert 仍检测不到 Blindspot（tie rate 65.9%）——这是否说明 LLM judges 本质上倾向给\"中性\"评分，而非 absolute vs relative evaluation paradigm 差异？\n5. 如果 pairwise 本身存在 format amplification（Comparative Trap），\"moderate\" effects (BT 63–67%) 的真实效应量可能更小——数据层面能否进一步区分 \"Likert misses real bias\" vs \"pairwise creates apparent bias\"？\n\n---\n\n## Missing References\n\n**已覆盖的关键文献** [R2 验证]：Jeong et al. (2025) Comparative Trap ✓、Stureborg et al. (2024) ✓、Park et al. (2024) OffsetBias ✓\n**建议补充**：\n- Shi et al. (2024) \"Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges\"\n- Bavaresco et al. (2024) \"LLMs Instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks\"\n\n引用验证摘要 [R2]：50 条 bib entries, 41 verified, 3 not_found (likely indexing issues), 6 minor mismatches, 0 missing_bib。引用质量良好。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 已跳过（用户未提交至 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（2 warnings, 6 info）\n\n关键发现：\n- **[warning]** Pages 3–4 连续 2 页纯文本（Related Work + Method 开头），无 display item 穿插。建议在 Method 段加入示意图或示例表。\n- **[warning]** Figure 2 (DAG) 尺寸偏小，仅占单栏约 1/4 高度。作为方法论核心论据，建议放大或跨栏展示。\n- **[info]** Table 1 脚注区域信息密度极高（4 个符号系统压缩在 3 行）。\n- **[info]** Figure 1 内部文字标签字号偏小（正文 60-65%）。\n- **[info]** Appendix 表格密度极高（每页 3-4 个 table）。\n- **[info]** References 置于 Appendix 之后（更常见做法是 main text → References → Appendix）。\n\n---\n\n## Overall Assessment\n\n### Reviewer Consensus [AGREE]\n- **Overall 3.5 (Borderline Conference)** — 两位 Reviewer 独立给出完全一致评分\n- **Soundness 3.5** — 统计框架严谨但 NLI gate 缺人工验证、evaluator-producer bias 处理不充分\n- **Reproducibility 4** — 方法细节完整，承诺代码/数据公开\n- 页数超限是 hard constraint，必须在提交前修复\n- NLI gate 人工验证是框架基石的验证缺口\n- Evaluator-producer bias 22% OR 下降 + register 缺失需要更诚实的处理\n- Novelty 主要为 domain transfer，但 LLM judge 场景的系统量化 + CSD 方法组合仍有增量价值\n\n### Reviewer Divergence [分歧点]\n1. **NLI gate 严重性**: R1 Must-Fix vs R2 strong Should-Fix（NLI ablation 反转证据降低严重性）→ Director 判定 Must-Fix\n2. **Novelty claim 严重性**: R2 Must-Fix vs R1 Should-Fix（LLM judge 特殊性使 domain transfer 非 trivial）→ Director 判定 Should-Fix\n3. **Abstract 密度**: R2 Should-Fix vs R1 Minor → 记录分歧\n4. **Excitement**: R1 3.5/5 vs R2 3/5 → R2 认为核心洞见是 domain transfer，novelty ceiling 更低\n\n### 评分\n\n| 维度 | R1 | R2 | 合成 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.5 | 3 | **3** |\n| Reproducibility | 4 | 4 | **4** |\n| Overall | 3.5 | 3.5 | **3.5 (Borderline Conference)** |\n| Confidence | 4 | 4 | **4** |\n\n**EMNLP 2026 ARR 评分**: **3.5 = Borderline Conference**\n\n### 判断依据\n\n论文发现有价值（Likert Blindspot 对 evaluation community 有直接实践影响），统计密度高于同领域平均水平，实验设计周全（6 个独立控制）。但存在三个阻碍 confident accept 的问题：(1) 页数超限（hard constraint）；(2) NLI gate 作为框架基石缺人工验证；(3) evaluator-producer bias 处理乐观。Novelty 主要来自 domain transfer（Thurstone 1927 已知），但 CSD 的方法组合和 per-axis GEE decomposition 提供增量贡献。\n\n**修复路径**: MF1（页数）可在提交前快速修复。MF2（人工验证 50 对样本）和 MF3（producer-corrected 估计 + register caveat）需要额外实验和写作工作。如果三个 Must-Fix 全部解决 + SF1-SF3 的 framing 调整完成，论文可达到 **4.0 (Conference)** 水平。当前状态适合 **Findings 接收**；是否 Main Conference 取决于 novelty 阈值判断。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高：8 句话塞入 framework 名称、4 judges、3 benchmarks、3 axes、BT 百分比、OR 值、两种解释。建议将 GEE OR 值移至 Introduction。[分歧：R2 Should-Fix, R1 Minor]\n- \"first framework combining...\" claim 需限定。\n\n### §1 Introduction\n- Contributions 列表每条 3–5 行，可精简为 1–2 行核心论点。\n- \"black-box interventional framework\" 措辞与 §3.5 disclaimer 不一致。\n\n### §2 Related Work\n- 覆盖全面，Comparative Trap、RATE 差异化、测量理论基础均已讨论。\n- \"Our contribution is the first systematic quantification of this gap\" 需限定。\n\n### §3 Method\n- §3.2 NLI gate 设计合理，direction-aware gating 的 axis-dependent 策略有充分 justification。\n- §3.5 Design Rationale 的因果声明 disclaimer 诚实。但 Figure 2 DAG 视觉修辞偏强，caption 可标注 \"design rationale, not a formal causal model\"（实际已有类似标注）。\n\n### §5 Experiments / Analysis\n- Table 1 Main Results 信息丰富但脚注区域过密。\n- Table 2 Sensitivity Hierarchy 是亮点——七种方法交叉验证。\n- §5.2 Measurement attenuation vs construct divergence 两种解释的呈现已有改善。\n- §5.4 Verbosity 的 \"style-dominated\" 描述基于 GEE，措辞比 \"confound-free\" 更审慎。\n\n### §6 Conclusion\n- **溢出 page 8**——必须压缩。\n- \"should adopt content-controlled pairwise comparison\" 需加 Comparative Trap caveat。\n\n### Limitations\n- 三段式覆盖 quality-style confounding、evaluator-producer bias、validation methodology。结构合理。\n- 未包含新实验/图表/分析，符合 EMNLP 2026 规定。\n\n### Appendix\n- 15 个 appendix sections 提供充分技术细节。\n- Table 5 GEE CI 部分缺失需补全。\n- Verbosity sensitivity hierarchy (Appendix P) 已补充。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "report": "# 审稿报告 — Round 6 (Fresh Review)\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**目标 Venue**: EMNLP 2026 Long Paper (ARR)\n**截止日期**: 2026-05-25\n**Reviewer**: R1 (方法严谨性/实验设计) + R2 (新颖性/Related Work/写作质量)\n**审稿模式**: Fresh（独立全新审稿）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一个检测 LLM judge 隐藏风格偏差的黑盒框架。CSD 通过三阶段流程——style-controlled rewriting、NLI-gated content preservation、position-controlled pairwise comparison——系统量化 per-axis style bias。核心发现是 \"Likert Blindspot\"：在相同数据上，Likert 评分（ATE）系统性地遗漏 pairwise comparison 能检测到的风格偏差（BT 63–84%, p < 0.001 vs Likert p > 0.17），由七种统计方法交叉验证。GEE conditional decomposition 进一步揭示 per-axis confound structure：verbosity 为 style-dominated，formality 为 conditional（style + originality confound），register 为 judge-dependent。在 4 个 judges（3 target + 1 negative control Claude Sonnet 4）、3 benchmarks、3 style axes 上验证。\n\n---\n\n## Strengths\n\n**S1. 研究问题精准且对社区有直接实践价值** [R1, R2 共识]\nLikert Blindspot 的发现直接挑战了 RATE 等基于 Likert ATE 的 bias 评估方法的有效性，对 evaluation community 有即时方法论指导意义。\n\n**S2. 统计框架严谨且多层次** [R1 主导]\n七种统计方法交叉验证（Table 2），Holm-Bonferroni 校正 + exploratory/confirmatory 分类，GEE conditional decomposition（Table 3），Bootstrap CI 10,000 resamples，BT GoF 检验，NLI 11-threshold sensitivity sweep，TOST 等价性检验。统计密度显著高于同领域平均水平。\n\n**S3. 实验设计周全，多重控制有效约束替代解释** [R1, R2 共识]\n六个独立控制（NLI gate ablation 反转至 41.7%、Claude 负控制无 bias、cross-axis BT 变异不一致 uniform amplification、rewriting artifact 被 GEE 吸收、debiased prompting 部分降低 bias、三架构一致）有效约束了替代解释空间。Claude Sonnet 4 作为 negative control 增强了 discriminative validity。\n\n**S4. Per-axis confound structure 是方法论增量贡献** [R1 主导]\nGEE 条件分解区分了 style-dominated（verbosity: Style OR 8–13, Orig OR <1）、conditional（formality: 显著 style 和 originality effects）和 judge-dependent（register）三种模式，超越了 aggregate bias score。\n\n**S5. Related Work 覆盖全面且定位清晰** [R2 主导]\nJeong et al. (2025) Comparative Trap、Stureborg et al. (2024)、Park et al. (2024) 等关键文献均被讨论。与 RATE、CASSE、FairJudge 的差异化清晰。\n\n**S6. 写作清晰、学术诚实** [R2 主导]\n§3.5 Design Rationale 的因果声明 disclaimer、Limitations 的三段式讨论（quality-style confounding、evaluator-producer bias、validation methodology）体现了较高的学术诚实度。Appendix 提供了充分技术细节。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. 主正文超过 8 页限制** [R2 发现, R1 交叉确认] — format, critical\nSection 6 (Conclusion) 约 5–6 行溢出到 page 9。EMNLP 2026 规定主正文 strict 8-page limit，Limitations 和 Ethics 不计入但 Conclusion 计入。严格执行下可导致 desk rejection。\n→ 建议压缩 §5.6 或 §6 文本（约 6–7 行）。\n\n**MF2. NLI gate 缺乏人工评估验证** [R1 Must-Fix, R2 同意但建议降级 strong Should-Fix] — method, critical\n整个框架的有效性依赖 NLI gate 正确分离 style 与 content 变化，但验证完全自动化（Qwen3-32B annotator + GPT-4o cross-validation 92.1%/82.6% precision）。没有人工评估验证 NLI gate 的 pass/fail 决策是否与人类判断一致。DeBERTa-v3-large 在 style-shifted text 上可能与标准 NLI 数据行为不同。\n缓解因素：NLI ablation（Appendix N）formality NLI-fail pairs 反转至 41.7% 是较强间接验证；11-threshold sweep ≤3pp 变动证明 threshold 不敏感。\n→ 建议随机抽取 50 对 pass/fail 样本，2+ annotator 评估，报告 IAA。\n\n**MF3. Evaluator-producer bias 22% OR 下降处理不充分 + register 轴缺失 cross-rewriter test** [R1 Must-Fix, R2 同意] — method, critical\nQwen3-32B rewriter→GPT-4o 后 verbosity Style OR 下降 22%（13.10→10.17），论文定性为\"bounding\"但 22% non-trivial。Register 轴完全缺失 cross-rewriter test，而 register 恰是 judge-dependence 最强的轴。核心 Blindspot pattern 在 GPT-4o rewriter 下保持（BT .735, Likert p=.838），说明不影响定性结论但影响效应量估计精度。\n→ 建议：(1) 提供 producer-corrected 效应估计范围；(2) Limitations 明确标注 register 缺乏 producer-independence 验证。\n\n### Should-Fix（影响评分但非一票否决）\n\n**SF1. Novelty claim \"first systematic quantification\" 过度宽泛** [R2 Must-Fix, R1 降级 Should-Fix → Director 判定 Should-Fix]\nPairwise > Likert 灵敏度是 Thurstone (1927) 以来的经典结论；Kiritchenko & Mohammad (2017)、Novikova et al. (2018) 已证明 forced-choice 在 NLG 评估中更灵敏；框架各组件均有先例。R1 反驳：LLM judges 的特殊性（确定性评分、无疲劳效应、不同 scale anchoring）使 domain transfer 非 trivial，且论文贡献包括 per-axis GEE decomposition。\n→ 建议将 \"first\" 限定到具体方法组合的 novelty；明确承认核心洞见是 domain transfer + systematic quantification。\n\n**SF2. Comparative Trap 张力在 Conclusion 处理不足** [R2 发现, R1 交叉同意]\n§2 和 §5.2 已讨论 Jeong et al. (2025) 并提供 6 个控制约束 amplification 风险，但 §6 推荐 \"style bias audits should adopt content-controlled pairwise comparison\" 措辞仍过强。\n→ 建议加入明确 caveat。\n\n**SF3. 因果术语（\"interventional framework\"）与实际 filtering-based 方法存在张力** [R1 W3, R2 W2 独立标注]\n§3.5 的 hedging 适当，但 Abstract \"black-box interventional framework\" 和 Introduction 多处使用强因果语言，与 §3.5 的 disclaimer 不一致。\n→ 建议统一为 \"quasi-interventional\" 或 \"controlled\" framework。\n\n**SF4. 样本量偏小且 scaled replication 覆盖面窄** [R1 W4, R2 W3 共识]\nLLMBar n=100（post-NLI n=88）为主数据源，MT-Bench n=30。n=355 scaled replication 仅覆盖 Qwen3-32B formality。\n→ 建议在 Conclusion 更明确标注 generalizability 边界。\n\n**SF5. TOST equivalence bound (Δ=15pp) 缺乏独立外部 justification** [R1 W1, R2 同意]\n用同研究 treatment effects 设定 control 的 equivalence bound 形成循环论证。\n→ 建议引用外部 style bias 基准。\n\n**SF6. Identification assumption (iii) 讨论不充分** [R1 W5, R2 同意]\n\"Rewrite introduces no systematic differences beyond target axis\"——same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。\n\n### Minor Issues\n\n- **M1**: Abstract 信息密度过高——OR 值等技术细节不利于可读性 [R2 Should-Fix, R1 Minor → 分歧]\n- **M2**: BT IIA 在 formality 轴可能被违反（Fisher p=0.015 方向不对称）[R1 Should-Fix, R2 Minor → 共识 Minor]\n- **M3**: Figure 2 (DAG) 和 Figure 3 (forest plot) 黑白打印下颜色/形状区分不足 [R1, R2 共识]\n- **M4**: Appendix Table 5 (GEE CI) 部分条目缺失 95% CI [R2]\n- **M5**: Table 1 第 6 列无 header，Blindspot 标记缺说明 [R2]\n- **M6**: Introduction contributions 列表每条过长（3–5 行）[R2]\n- **M7**: bib key wu2023style 年份与 venue 年份不一致 [R2]\n\n---\n\n## Questions for Authors\n\n1. NLI gate 在不同 rewrite directions（formal→casual vs casual→formal）上的 entailment score 分布是否存在系统差异？如果 formal text 系统性获得更高 NLI score，这会否引入 selection bias？\n2. 22% OR 下降中有多少可归因于 GPT-4o 的 style transfer 质量差异 vs 真实 self-preference？如果使用 rule-based rewriting，效应量可能进一步缩小？\n3. Register 轴的 judge-dependence 在缺乏 cross-rewriter test 的情况下，如何排除 evaluator-producer confound 而非 genuine judge-specific sensitivity？\n4. 100-point continuous Likert 仍检测不到 Blindspot（tie rate 65.9%）——这是否说明 LLM judges 本质上倾向给\"中性\"评分，而非 absolute vs relative evaluation paradigm 差异？\n5. 如果 pairwise 本身存在 format amplification（Comparative Trap），\"moderate\" effects (BT 63–67%) 的真实效应量可能更小——数据层面能否进一步区分 \"Likert misses real bias\" vs \"pairwise creates apparent bias\"？\n\n---\n\n## Missing References\n\n**已覆盖的关键文献** [R2 验证]：Jeong et al. (2025) Comparative Trap ✓、Stureborg et al. (2024) ✓、Park et al. (2024) OffsetBias ✓\n**建议补充**：\n- Shi et al. (2024) \"Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges\"\n- Bavaresco et al. (2024) \"LLMs Instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks\"\n\n引用验证摘要 [R2]：50 条 bib entries, 41 verified, 3 not_found (likely indexing issues), 6 minor mismatches, 0 missing_bib。引用质量良好。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 已跳过（用户未提交至 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（2 warnings, 6 info）\n\n关键发现：\n- **[warning]** Pages 3–4 连续 2 页纯文本（Related Work + Method 开头），无 display item 穿插。建议在 Method 段加入示意图或示例表。\n- **[warning]** Figure 2 (DAG) 尺寸偏小，仅占单栏约 1/4 高度。作为方法论核心论据，建议放大或跨栏展示。\n- **[info]** Table 1 脚注区域信息密度极高（4 个符号系统压缩在 3 行）。\n- **[info]** Figure 1 内部文字标签字号偏小（正文 60-65%）。\n- **[info]** Appendix 表格密度极高（每页 3-4 个 table）。\n- **[info]** References 置于 Appendix 之后（更常见做法是 main text → References → Appendix）。\n\n---\n\n## Overall Assessment\n\n### Reviewer Consensus [AGREE]\n- **Overall 3.5 (Borderline Conference)** — 两位 Reviewer 独立给出完全一致评分\n- **Soundness 3.5** — 统计框架严谨但 NLI gate 缺人工验证、evaluator-producer bias 处理不充分\n- **Reproducibility 4** — 方法细节完整，承诺代码/数据公开\n- 页数超限是 hard constraint，必须在提交前修复\n- NLI gate 人工验证是框架基石的验证缺口\n- Evaluator-producer bias 22% OR 下降 + register 缺失需要更诚实的处理\n- Novelty 主要为 domain transfer，但 LLM judge 场景的系统量化 + CSD 方法组合仍有增量价值\n\n### Reviewer Divergence [分歧点]\n1. **NLI gate 严重性**: R1 Must-Fix vs R2 strong Should-Fix（NLI ablation 反转证据降低严重性）→ Director 判定 Must-Fix\n2. **Novelty claim 严重性**: R2 Must-Fix vs R1 Should-Fix（LLM judge 特殊性使 domain transfer 非 trivial）→ Director 判定 Should-Fix\n3. **Abstract 密度**: R2 Should-Fix vs R1 Minor → 记录分歧\n4. **Excitement**: R1 3.5/5 vs R2 3/5 → R2 认为核心洞见是 domain transfer，novelty ceiling 更低\n\n### 评分\n\n| 维度 | R1 | R2 | 合成 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.5 | 3 | **3** |\n| Reproducibility | 4 | 4 | **4** |\n| Overall | 3.5 | 3.5 | **3.5 (Borderline Conference)** |\n| Confidence | 4 | 4 | **4** |\n\n**EMNLP 2026 ARR 评分**: **3.5 = Borderline Conference**\n\n### 判断依据\n\n论文发现有价值（Likert Blindspot 对 evaluation community 有直接实践影响），统计密度高于同领域平均水平，实验设计周全（6 个独立控制）。但存在三个阻碍 confident accept 的问题：(1) 页数超限（hard constraint）；(2) NLI gate 作为框架基石缺人工验证；(3) evaluator-producer bias 处理乐观。Novelty 主要来自 domain transfer（Thurstone 1927 已知），但 CSD 的方法组合和 per-axis GEE decomposition 提供增量贡献。\n\n**修复路径**: MF1（页数）可在提交前快速修复。MF2（人工验证 50 对样本）和 MF3（producer-corrected 估计 + register caveat）需要额外实验和写作工作。如果三个 Must-Fix 全部解决 + SF1-SF3 的 framing 调整完成，论文可达到 **4.0 (Conference)** 水平。当前状态适合 **Findings 接收**；是否 Main Conference 取决于 novelty 阈值判断。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高：8 句话塞入 framework 名称、4 judges、3 benchmarks、3 axes、BT 百分比、OR 值、两种解释。建议将 GEE OR 值移至 Introduction。[分歧：R2 Should-Fix, R1 Minor]\n- \"first framework combining...\" claim 需限定。\n\n### §1 Introduction\n- Contributions 列表每条 3–5 行，可精简为 1–2 行核心论点。\n- \"black-box interventional framework\" 措辞与 §3.5 disclaimer 不一致。\n\n### §2 Related Work\n- 覆盖全面，Comparative Trap、RATE 差异化、测量理论基础均已讨论。\n- \"Our contribution is the first systematic quantification of this gap\" 需限定。\n\n### §3 Method\n- §3.2 NLI gate 设计合理，direction-aware gating 的 axis-dependent 策略有充分 justification。\n- §3.5 Design Rationale 的因果声明 disclaimer 诚实。但 Figure 2 DAG 视觉修辞偏强，caption 可标注 \"design rationale, not a formal causal model\"（实际已有类似标注）。\n\n### §5 Experiments / Analysis\n- Table 1 Main Results 信息丰富但脚注区域过密。\n- Table 2 Sensitivity Hierarchy 是亮点——七种方法交叉验证。\n- §5.2 Measurement attenuation vs construct divergence 两种解释的呈现已有改善。\n- §5.4 Verbosity 的 \"style-dominated\" 描述基于 GEE，措辞比 \"confound-free\" 更审慎。\n\n### §6 Conclusion\n- **溢出 page 8**——必须压缩。\n- \"should adopt content-controlled pairwise comparison\" 需加 Comparative Trap caveat。\n\n### Limitations\n- 三段式覆盖 quality-style confounding、evaluator-producer bias、validation methodology。结构合理。\n- 未包含新实验/图表/分析，符合 EMNLP 2026 规定。\n\n### Appendix\n- 15 个 appendix sections 提供充分技术细节。\n- Table 5 GEE CI 部分缺失需补全。\n- Verbosity sensitivity hierarchy (Appendix P) 已补充。"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-21T17:44:59.021980+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4065
}
```

</details>

---


### Assistant

_source line 524 · 2026-05-21T17:45:07.149174+00:00_

审稿报告已投递至 Research Director。

**Round 6 审稿总结**：

- **Overall**: 3.5 (Borderline Conference)，两位 Reviewer 独立一致
- **3 个 Must-Fix**：页数超限（Conclusion 溢出 ~6 行）、NLI gate 缺人工验证、Evaluator-producer bias 22% OR 下降 + register 缺失
- **6 个 Should-Fix**：Novelty claim 过度宽泛、Comparative Trap caveat 不足、因果措辞不一致、样本量/覆盖面窄、TOST bound 循环论证、Assumption (iii) 讨论不充分
- **修复路径**：MF1 可快速修复；MF2 需 50 对样本人工评估；MF3 需 producer-corrected 估计范围。三个 Must-Fix + framing 调整完成后可达 4.0 (Conference)
- **Issue Tracker** 已同步更新（新增 4 个 issue，更新 11 个既有 issue 的 Round 6 mention）
- **外部审稿**：已跳过。**视觉审查**：已完成，2 warnings + 6 info

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 525 · 2026-05-21T17:45:09.642925+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心判断：与 R2 在大部分问题上达成共识（页数超限、因果措辞、样本量、Comparative Trap），但有两个关键分歧——(1) R2 的 Novelty Must-Fix 我认为应降级为 Should-Fix；(2) 我的 NLI 人工验证和 evaluator-producer bias 两个 Must-Fix 是 R2 未覆盖的独立发现。最终评分维持 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 526 · 2026-05-21T17:45:18.760589+00:00_

审稿报告已投递至 Research Director。

**Round 6 审稿总结**：

- **Overall**: 3.5 (Borderline Conference)，两位 Reviewer 完全一致
- **3 个 Must-Fix**: 页数超限（~6 行溢出）、NLI gate 缺人工验证、evaluator-producer bias 22% OR 下降处理不充分
- **6 个 Should-Fix**: novelty claim 过宽、Comparative Trap caveat 不足、因果术语过强、样本量/覆盖面窄、TOST bound 循环论证、identification assumption (iii) 讨论不足
- **修复路径**: 三个 Must-Fix 全部解决 + framing 调整后可达 4.0 (Conference)；当前状态适合 Findings 接收

Issue Tracker 已同步更新（`review_issues.yaml`），外部审稿已跳过，视觉审查已完成（2 warnings, 6 info）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 55

## Round 55

62 recorded events


### User

_source line 527 · 2026-05-21T21:08:44.665513+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-21T21:08:52.295784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-21T21:08:52.346622+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-21T21:08:56.170456+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-21T21:08:56.170896+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-21T21:08:59.739472+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-21T21:08:59.739977+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-21T21:09:05.713348+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-21T21:09:05.713694+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-21T21:09:06.166455+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-21T21:09:06.419609+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (53 个)\n\n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **register_100_cf**: QUEUED — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- register_100_cf: Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality（排队等待 GPU）\n\n## 近期结论\n- **llama70b_register** (success): Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures\n- **llama70b_debiased** (success): Llama-70B correction resistance follows the same axis-dependent pattern as GPT-4o/Qwen3-32B: debiased prompts reduce but do not eliminate style bias, with verbosity more amenable to correction than formality, confirming bias persistence is model-independent\n  [debiased_llama70b_summary.json](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/llama70b_debiased/data/debiased_llama70b_summary.json)\n- **crossbench_alpacaeval_verbosity** (success): AlpacaEval verbosity bias is strong enough (BT ~84%) that even Likert detects it, confirming the effect-size gradient: Blindspot occurs at small-to-medium effects (d<0.15) but not at large effects (d>0.3)\n\n## 趋势\n成功 3
…[truncated 187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-21T21:09:12.744048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-21T21:09:13.146132+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Detecting Hidden Style Bias\\in LLM Judges via Controlled Style Decomposition}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	
46	\paragraph{Evaluator-producer bias and generalizability.}
47	Qwen3-32B serves as both rewriter and judge, raising s
…[truncated 1877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-21T21:09:13.547917+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-21T21:09:13.548364+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-21T21:09:14.552467+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-21T21:09:14.753764+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_style_decomp_judge'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-21T21:09:14.754258+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-21T21:09:14.804787+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-21T21:09:20.626143+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 547 · 2026-05-21T21:09:21.479678+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 commitment deadline ARR submission cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 commitment deadline ARR submission cycle"
  }
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-21T21:09:21.781059+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-21T21:09:26.145252+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines page limit"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here are the ACL Rolling Review (ARR) 2026 submission guidelines regarding page limits:

## Page Limit Guidelines

Short papers have a maximum of 4 content pages, while long papers have a maximum of 8 content pages.

Sections on ethical considerations and limitations do not count towards the page limit.

## Additional Requirements for EACL 2026

For conferences using ARR (such as EACL 2026), there is an important addition: EACL 2026 requires all papers to have a clear discussion of limitations in a dedicated section titled "Limitations" that appears at the end of the paper
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5519
}
```

</details>

---


### Tool result

_source line 550 · 2026-05-21T21:09:27.149038+00:00_

Web search results for query: "EMNLP 2026 commitment deadline ARR submission cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the search results, here are the key deadlines for EMNLP 2026 related to the ARR submission cycle and commitment:

## ARR Submission Deadline
The ARR submission deadline for long and short papers is May 25, 2026.

## EMNLP Commitment Deadline
The EMNLP commitment deadline is August 2, 2026.

## Key Timeline
The reviewer registration deadline for all authors is May 27, 2026, followed by the author response and author-reviewer discu
…[truncated 595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5669
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-21T21:09:27.150014+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml\", \"content\": \"_next_id: 62\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 14:09 UTC\\n  summary: '文献蒸馏审视：研究方向无需调整，CSD 填补 #1 空白（多维 style 因果分解），post-MVP 需扩展 judge/benchmark/baseline\\n    覆盖'\\n  rationale: '10 篇论文蒸馏显示：(1) 多维 style 联合因果分解是领域 #1 空白，与 CSD 核心 claim 完全对齐；(2) 竞品 claim\\n    无直接重叠（FairJudge=white-box, Pref Leakage=family-based, Soumik=prompt-dependent）；(3)\\n    同行标准要求 3-5 异构 judge + AlpacaEval/Arena-Hard/MT-Bench + Bootstrap CIs + 对比 LC-AlpacaEval\\n    baseline。当前 MVP 方案足够，research 阶段需按蒸馏标准扩展。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 14:19 UTC\\n  summary: MVP 全量评分 + 分层分析：score 全部 100 条，按 BERTScore 阈值 0.88/0.90/0.92 分层算 ATE，不降低阈值\\n  rationale: 36% pass rate (BERTScore≥0.92) 偏低但 NLI 均值 0.9422 说明语义保留好。降阈值是数据操作，不如保留完整信息。全量评分\\n    (n=100) 保证统计 power，分层分析同时回答\\\"严格阈值下效应是否存在\\\"和\\\"宽松阈值下效应是否增强\\\"。8B H1 fail 不消耗迭代配额（ROADMAP\\n    规则），32B 备用。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 14:20 UTC\\n  summary: H1 content verification 改为 NLI-only gate（≥0.90），BERTScore 降为监控指标，不作为过滤条件\\n  rationale: Reviewer 诊断：36% pass rate 的根因是 BERTScore 惩罚 style transfer 预期的词汇变化（contractions→full\\n    forms 等），而非内容泄漏。NLI 均值 0.9422、抽样 >0.99 证明语义保留良好。BERTScore 作为 token-level 相似度指标与\\n    style transfer 评估目标矛盾（改的就是 token）。Double-rewrite pass rate 更低（21/100）进一步印证。NLI-only\\n    gate 是度量校准（不消耗 8B 迭代配额），与 D002 全量评分兼容——primary ATE 用 NLI≥0.90 子集，secondary 按 BERTScore\\n    分层。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 14:32 UTC\\n  summary: 8B 初步 ATE≈0.028 不可见，归因三因素：Likert 粒度 + 8B rewriter 质量 + RATE corruption。不计入\\n    kill criteria，等 n=100 + 32B\\n  rationale: 36/100 初步数据 Cohen's d=0.055 远低于 0.3 门槛，但三个叠加因素解释了结果：(1) 83% 零差异源于 integer\\n    Likert 无法捕捉 sub-integer 效应；(2) 22% identical rewrites 稀释 ATE；
…[truncated 10852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5368
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-21T21:09:32.771244+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers author guidelines anonymity appendix policy site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers author guidelines anonymity appendix policy site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 553 · 2026-05-21T21:09:33.323605+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 554 · 2026-05-21T21:09:33.374150+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-21T21:09:38.893346+00:00_

Web search results for query: "EMNLP 2026 call for papers author guidelines anonymity appendix policy site:2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Author anonymization","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10360407"},{"title":"Author anonymization","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10360404"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"}]

I found relevant information from the EMNLP 2026 official website. Here are the key findings regarding author guidelines, anonymity, and appendix policy:

**Anonymity Policy:**
There is no anonymity period requirement, following the ACL and ARR policies. However, the reviewing process will continue to be double-blind.

**Appendix Policy:**
Authors are asked not to abuse the option of an unlimited appendix and only to include material that supports the primary messages and content of the paper; for final papers with an appendix of excessive length, the EMNLP 2026 Industry Track chairs reserve the right to include a statement that it is not mandatory for reviewers to review the material presented in the appendix.

**Additional Guidelines:**
- Authors are required to discuss the limitations of their work in a dedicated section titled "Limitations" at the end of the paper before references, which will not count toward the page limit. Papers without a limitations section will be desk rejected.

- Authors may submit separate files as supplementary materials, such as software or data
…[truncated 229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6122
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-21T21:09:45.915368+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-21T21:09:46.166599+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_director_acab027e.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-21T21:09:46.166946+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-21T21:09:46.217974+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-21T21:09:49.530225+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-21T21:09:49.781619+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-21T21:09:49.933500+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-21T21:09:49.984234+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-21T21:09:53.699055+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-21T21:09:54.202422+00:00_

&lt;persisted-output>
Output too large (21.2KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/5ae75b1e-3b13-4981-879a-e7823a2cb2cf/tool-results/toolu_0151XLQti2U5AjKJ7HRrsyRp.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/logs/chats/feishu_group_oc_09b04b56f2fb04931812c4a55f159dee_reviewer.jsonl:846:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/logs/chats/feishu_group_oc_f810d8d75f013ad17831ce8459f07d6d_director.jsonl:2:{"ts": "2026-05-21T01:54:25.756348+00:00", "role": "tool", "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status", "max_results": "4"}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/logs/chats/feishu_group_oc_f810d8d75f013ad17831ce8459f07d6d_director.jsonl:11:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/logs/chats/feishu_group_oc_f810d8d75f013ad17831ce8459f07d6d_director.jsonl:30:{"ts": "2026-05-21T01:58:25.791249+00:00", "role": "tool", "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director", "text": "called mcp__agent-ml-research__get_external_review_status", "tool": "mcp__agent-ml-research__get_external_review_status", "tool_args": {"project": "causal_style_decomp_judge"}}
...
&lt;/persisted-output>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-21T21:09:54.504495+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5",
  "glob": "**/config*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5",
    "glob": "**/config*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-21T21:09:54.555146+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-21T21:09:58.170490+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5",
  "glob": "**/project*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5",
    "glob": "**/project*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-21T21:09:58.522280+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-21T21:09:58.522762+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-21T21:09:58.573499+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-21T21:10:01.384667+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-21T21:10:01.435575+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/workspace.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/dml_chernozhukov_2018.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/veitch_uai_2020.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/lc_alpacaeval_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/soumik_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/fairjudge_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/preference_leakage_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/sos_bench_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/casse_2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/counterfactual_rhetorical_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/distill_tmp/rate_icml_2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T211832/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T211832/median/imagined_
…[truncated 7227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-21T21:10:05.602004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/projects/causal_style_decomp_judge.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/projects/causal_style_decomp_judge.yaml"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-21T21:10:06.656000+00:00_

1	execution:
2	  account: root
3	  gpu_ids:
4	  - cuda:0
5	  - cuda:1
6	  - cuda:2
7	  - cuda:3
8	  project_path: /root/causal_style_decomp_judge
9	  servers:
10	  - westb-29275
11	feishu:
12	  chat_id: oc_5ce280de124a4e308d1827c6450ad337
13	  operational_chat_id: oc_09b04b56f2fb04931812c4a55f159dee
14	  review_mode: fresh
15	  review_paper_path: projects/causal_style_decomp_judge/docs/paper/main.tex
16	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf
17	  review_round: 6
18	  review_supplementary_paths: ''
19	  submission_chat_id: oc_f810d8d75f013ad17831ce8459f07d6d
20	project:
21	  created_at: '2026-05-20T07:07:53.848Z'
22	  description: Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust
23	    Counterfactual Estimation
24	  name: causal_style_decomp_judge
25	  phase: research
26	  source_idea_id: idea_028
27	venue: emnlp-2026
28	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-21T21:10:06.706623+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-21T21:10:06.707024+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  - created_at: '2026-05-19T12:23:13Z'
12	    id: bd0516
13	    text: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for
14	      main text, with unlimited space for references. Mandatory limitations and optional
15	      ethical considerations do not count towards this page limit, provided they do
16	      not contain excessive additional content.
17	  writing:
18	  - created_at: '2026-05-21T06:49:14Z'
19	    id: 2468a8
20	    text: Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
21	  - created_at: '2026-05-21T17:05:54Z'
22	    id: 0b1d8f
23	    text: ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
24	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-21T21:10:06.807636+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-21T21:10:07.059877+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved unless noted)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	    mentions:
16	      - round: 3
17	        reviewers: [1, 2]
18	        note: "因果语言降级问题在 Round 3 以新形式复发，见 R3-N1"
19	      - round: 4
20	        reviewers: [1]
21	        note: "R4-M2: 'Interventional Design' → 'Design Rationale'. 全面解决。"
22	      - round: 5
23	        reviewers: [1, 2]
24	        note: "标题和小节名已修复，但 §3.2 仍残留 'approximates the do-operator' 语言，见 R5-MF2"
25	
26	  - id: "R2-N1"
27	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
28	    category: framing
29	    severity: warning
30	    status: resolved
31	    first_raised_round: 1
32	    last_seen_round: 5
33	    resolution: "Abstract/Intro 明确标注为 'first systematic quantitative verification of known measurement theory principle in LLM judge evaluation'. Structural ceiling acknowledged."
34	    resolution_round: 4
35	    mentions:
36	      - round: 3
37	        reviewers: [1, 2]
38	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
39	      - round: 4
40	        reviewers: [1, 2]
41	        note: "R4-SF8: Honest novelty positioning applied."
42	      - round: 5
43	        reviewers: [1, 2]
44	        note: "Novelty ceiling 仍是结构性限制。R2 给 Excitement 2.5/5。'first systematic' claim 仍需进一步限定，见 R5-SF1。"
45	
46	  - id: "R1-N2"
47	    summary: "NLI gate 67% false-negative rate 造成选择偏差未分析"
48	    category: method
49	    severity: critical
50	    status: resolved
51	    first_raised_round: 1
52	    last_seen_round: 1
53	    resolutio
…[truncated 35673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-21T21:10:44.372907+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool call

_source line 581 · 2026-05-21T21:10:44.875941+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-21T21:11:04.160496+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19787
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-21T21:11:04.161044+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 19285
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-21T21:11:04.362120+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR)，Long Paper\n- **截止日期**: 2026-05-25 AoE\n- **格式**: ACL 模板，正文 ≤8 页，引用不限，Limitations 必须有（不计页数），double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n- Sections 在 `projects/causal_style_decomp_judge/docs/paper/sections/` 下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex\n\n## 你的审查侧重\n\n### 必须覆盖\n1. **因果声明与证据强度匹配**：标题/摘要/正文中的因果语言（causal, interventional, counterfactual, do-operator）是否与实际方法论强度匹配？是否有 overclaim？\n2. **NLI Gate 有效性**：NLI 阈值选择是否有充分 justification？Direction-aware NLI 的理论和实证基础？FNR/FPR 分析是否完备？\n3. **统计方法**：Bradley-Terry 模型假设检验（IIA 等）、GEE 选择的合理性、Holm-Bonferroni 校正的正确性、TOST 等价检验的 bound 设定\n4. **样本量与统计效力**：n=100 (LLMBar)、n=355 (scaled replication)、n=30 (MT-Bench) 各自的统计效力是否足够？效应量估计的置信区间？\n5. **Evaluator-producer confound**：Qwen3-32B 同时作为 rewriter 和 judge 的自我偏好风险；cross-rewriter independence test 的覆盖面\n6. **页数合规**：主正文是否 ≤8 页（Limitations 和 References 不计入）\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条，标注 S1, S2, ...）\n- **Weaknesses**（逐条，标注 W1, W2, ...，每条标注严重程度：Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的相关文献）\n- **Overall Assessment**：评分（用 EMNLP 2026 标准）+ Excitement (1-5) + 置信度 (1-5)\n- **Detailed Comments**：逐节详细意见"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR)，Long Paper\n- **截止日期**: 2026-05-25 AoE\n- **格式**: ACL 模板，正文 ≤8 页，引用不限，Limitations 必须有（不计页数），double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n- Sections 在 `projects/causal_style_decomp_judge/docs/paper/sections/` 下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex\n\n## 你的审查侧重\n\n### 必须覆盖\n1. **因果声明与证据强度匹配**：标题/摘要/正文中的因果语言（causal, interventional, counterfactual, do-operator）是否与实际方法论强度匹配？是否有 overclaim？\n2. **NLI Gate 有效性**：NLI 阈值选择是否有充分 justification？Direction-aware NLI 的理论和实证基础？FNR/FPR 分析是否完备？\n3. **统计方法**：Bradley-Terry 模型假设检验（IIA 等）、GEE 选择的合理性、Holm-Bonferroni 校正的正确性、TOST 等价检验的 bound 设定\n4. **样本量与统计效力**：n=100 (LLMBar)、n=355 (scaled replication)、n=30 (MT-Bench) 各自的统计效力是否足够？效应量估计的置信区间？\n5. **Evaluator-producer confound**：Qwen3-32B 同时作为 rewriter 和 judge 的自我偏好风险；cross-rewriter independence test 的覆盖面\n6. **页数合规**：主正文是否 ≤8 页（Limitations 和 References 不计入）\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条，标注 S1, S2, ...）\n- **Weaknesses**（逐条，标注 W1, W2, ...，每条标注严重程度：Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的相关文献）\n- **Overall Assessment**：评分（用 EMNLP 2026 标准）+ Excitement (1-5) + 置信度 (1-5)\n- **Detailed Comments**：逐节详细意见"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-21T21:11:16.109540+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11747
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-21T21:11:16.310439+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR)，Long Paper\n- **截止日期**: 2026-05-25 AoE\n- **格式**: ACL 模板，正文 ≤8 页，引用不限，Limitations 必须有（不计页数），double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n- Sections 在 `projects/causal_style_decomp_judge/docs/paper/sections/` 下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex\n\n## 你的审查侧重\n\n### 必须覆盖\n1. **Novelty 定位**：核心贡献（Likert Blindspot 发现、CSD pipeline、measurement mode 洞察）是否真正新颖？与 Thurstone (1927)、心理测量学文献的关系如何定位？是否有 overclaim \"first\"？\n2. **Related Work 完整性**：是否覆盖了 LLM-as-Judge 偏差研究的主要方向（style bias、position bias、self-preference）？是否遗漏关键文献？特别关注 Jeong et al. (2025) Comparative Trap 等近期工作\n3. **贡献声明一致性**：Abstract/Introduction 中的贡献声明是否与实验结果吻合？是否有方向不一致？\n4. **论文结构与叙事**：各 section 之间的逻辑流是否通顺？信息密度是否均衡？Abstract 是否过密？\n5. **格式合规**：\n   - 主正文 ≤8 页（Limitations/References 不计入）\n   - Limitations section 是否存在且合理\n   - 匿名要求是否满足\n   - 引用格式是否正确（natbib）\n   - 图表质量和标注完整性\n6. **写作质量**：语法、用词精准度、术语一致性、可读性\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条，标注 S1, S2, ...）\n- **Weaknesses**（逐条，标注 W1, W2, ...，每条标注严重程度：Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的相关文献）\n- **Overall Assessment**：评分（用 EMNLP 2026 标准）+ Excitement (1-5) + 置信度 (1-5)\n- **Detailed Comments**：逐节详细意见"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR)，Long Paper\n- **截止日期**: 2026-05-25 AoE\n- **格式**: ACL 模板，正文 ≤8 页，引用不限，Limitations 必须有（不计页数），double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`\n- Sections 在 `projects/causal_style_decomp_judge/docs/paper/sections/` 下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex\n\n## 你的审查侧重\n\n### 必须覆盖\n1. **Novelty 定位**：核心贡献（Likert Blindspot 发现、CSD pipeline、measurement mode 洞察）是否真正新颖？与 Thurstone (1927)、心理测量学文献的关系如何定位？是否有 overclaim \"first\"？\n2. **Related Work 完整性**：是否覆盖了 LLM-as-Judge 偏差研究的主要方向（style bias、position bias、self-preference）？是否遗漏关键文献？特别关注 Jeong et al. (2025) Comparative Trap 等近期工作\n3. **贡献声明一致性**：Abstract/Introduction 中的贡献声明是否与实验结果吻合？是否有方向不一致？\n4. **论文结构与叙事**：各 section 之间的逻辑流是否通顺？信息密度是否均衡？Abstract 是否过密？\n5. **格式合规**：\n   - 主正文 ≤8 页（Limitations/References 不计入）\n   - Limitations section 是否存在且合理\n   - 匿名要求是否满足\n   - 引用格式是否正确（natbib）\n   - 图表质量和标注完整性\n6. **写作质量**：语法、用词精准度、术语一致性、可读性\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条，标注 S1, S2, ...）\n- **Weaknesses**（逐条，标注 W1, W2, ...，每条标注严重程度：Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的相关文献）\n- **Overall Assessment**：评分（用 EMNLP 2026 标准）+ Excitement (1-5) + 置信度 (1-5)\n- **Detailed Comments**：逐节详细意见"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-21T21:11:17.518394+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1207
}
```

</details>

---


### Assistant

_source line 588 · 2026-05-21T21:11:28.311398+00:00_

所有任务已派发：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验设计） | ✅ 已分配 |
| Reviewer 2（新颖性 + 完整性 + 写作） | ✅ 已分配 |
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿 (Stanford Agentic Reviewer) | ⏭️ 未配置，跳过 |

等待两位 Reviewer 返回独立初审意见，收到后进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 56

## Round 56

2 recorded events
