---
round: 4
overall_score: weak reject
timestamp: 2026-05-16T06:48:22.441348+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 6 (Fresh Review)

**论文**: "Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision"
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Reviewer 编排**: Reviewer 1 (方法与实验严谨性) + Reviewer 2 (新颖性、写作与完整性)
**外部审稿**: 未启用

---

## Summary

本文研究 LLM coding agent 的停滞检测问题，使用弱监督框架（3 个 labeling functions + majority vote）在 SWE-Agent 和 OpenHands 共 205K+ 窗口上生成 silver labels，比较结构化特征（30 维）、GRU 神经探针、LLM-as-judge 和 n-gram cycle detector 在不同部署场景下的表现。核心发现：(1) 结构特征在 zero-data 跨 agent 迁移中表现最好（GB 0.967 on silver），但 gold set 上 LLM judge 更优（0.910 vs 0.839）；(2) label 质量是迁移瓶颈；(3) 5 个 label model 均无法超越 majority vote。

---

## Strengths

**S1. 问题选择有实际价值。** Agent 停滞检测是真实部署痛点，系统性对比检测方法填补了空白。早期终止分析（15-30% compute savings）展示了明确的实用性。

**S2. 实验设计宽度出色。** 跨 agent 迁移（SWE-Agent → OH, OH → SWE 双向）、encoder ablation（3 种）、window size ablation、multi-seed stability、feature overlap decomposition、data scaling curve、6-LF scaling——消融覆盖全面，appendix 信息丰富。

**S3. 循环性问题的主动披露。** Section 5.1-5.2 坦诚承认 silver-label 评估的循环性，提供了三个 de-circulation 证据（cross-agent cmd_rep 仅 5.4% firing、instance isolation <0.1pp 变化、gold set）。Silver→gold ranking reversal（structural beats LLM on silver, LLM beats on gold）是有力的循环性证据。

**S4. 负面结果有价值。** 5 个 label model 均不优于 MV 的发现及 root cause 分析（LF quantity bottleneck），对弱监督社区有参考意义。ACR 第三 agent 迁移失败的诚实报告也是加分项。

**S5. 部署实用性清晰。** <5ms inference、无 GPU、cost 对比（structural vs LLM 8,000× 差异）——部署 trade-off 信息完整。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF-1] 循环评估贯穿全文，headline claims 误导读者**
- **共识度**: R1-W1 + R2-N2，两位 Reviewer 高度一致，交叉回应中互相确认
- **问题**: Abstract/Introduction 的 headline 数字全部基于 silver labels（0.967 cross-agent、39.4pp gap、47.6pp LLM collapse），而 silver labels 由 LF 生成，结构特征中 11/30 维直接重叠于 LF 信号。In-domain F1=0.995 本质是拟合 label 生成过程。论文自己承认 "cross-agent transfer primarily validates the transferability of LF-encoded judgment patterns"（§5.2），但叙事结构仍以 silver 数字为中心。
- Gold set（§4.7）上的非循环结果（GB 0.839）才是真实检测能力的 proxy，但被边缘化——未出现在 Abstract 中。
- 缺少关键对照：仅用 LF 规则做 threshold-based classification 的 F1 是多少？如果简单规则（如 unique_cmd_ratio > threshold）就能达到 0.95+ silver F1，那 30 维特征 + GB 的增量贡献被进一步削弱。
- **要求**: (a) 以 gold 数字重构 Abstract/Introduction 叙事；(b) silver-label 结果明确降级为 "LF-agreement scores / pipeline validation"；(c) 增加 LF threshold-based baseline 作为循环性 sanity check。

**[MF-2] Gold set 规模和质量不足以承担非循环验证角色**
- **共识度**: R1-W2 + R2-N3，两位 Reviewer 完全一致
- **问题**: (a) Fleiss' κ=0.39（fair agreement），低于 moderate 门槛（0.41），远低于 substantial（0.61）；(b) N=505 仅覆盖 SWE-Agent conf≥2——跨 agent claims（核心 selling point）完全无非循环验证；(c) 三人标注子集仅 N=52（Appendix G.5 Set A），IAA 计算基础薄弱；(d) silver-gold agreement 93.8% 可能反映标注者使用了类似 LF 的直觉（annotators 看到 command repetition 和 file diffs——正是 λ₁/λ₂ 的信号）；(e) 对于声称 "systematic empirical study" 的论文，505 samples 不足。
- **要求**: (a) 扩大至 1000+ windows；(b) 覆盖 OpenHands 以验证跨 agent claims；(c) 包含 conf=1 歧义窗口；(d) 提高 IAA 或诚实讨论 κ=0.39 意味着 stagnation 本身缺乏清晰操作定义。

**[MF-3] 方法新颖性有限——本质是 Snorkel 直接应用**
- **共识度**: R2-N1 提出，R1 AGREE 并补充"如果 findings 可靠则可接受，但 findings 可靠性也不足，构成双重打击"
- **问题**: 3 LFs + majority vote 聚合是 Ratner et al. (2016/2019) data programming 的标准范式。§2 Related Work 列出的 "three ways our application differs" 是领域适配（LFs target trajectory structure / temporal dependencies / agent-specific firing）而非方法创新。30 维结构特征是标准手工特征工程。EMNLP Main Conference 对方法新颖性有要求——将现有框架应用于新领域需展示非平凡的技术挑战和解决方案。
- **要求**: (a) 明确定位为 empirical study 并 target Findings track；或 (b) 展示 naive Snorkel 不 work 的失败案例，论证领域适配中的非平凡技术挑战。

**[MF-4] LLM judge 叙事严重不平衡**
- **共识度**: R2-W2 提出，R1 交叉回应中 strongly AGREE，称此为自己审稿的盲点
- **问题**: 论文在唯一的非循环评估（gold set）上，LLM judge 以 0.910 显著胜出 structural GB 的 0.839（+7.1pp）。但 headline framing 以 silver-label 上 LLM 的 "collapse"（0.491）为主线，淡化了 gold 上 LLM 的优势。Cross-agent LLM 评估（N=500）本身也在 silver labels 上进行——受同样的循环性问题影响。此外，few-shot-CoT 在 OH 上降至 0.470 可能是 SWE-Agent examples 的负迁移，而非 LLM 本身的跨 agent 局限。
- **要求**: (a) 更平衡地呈现：LLM 在非循环准确率更优但成本高，structural 优势在效率和迁移性；(b) 用 OH-specific few-shot examples 重测 LLM cross-agent 性能；(c) gold 上 LLM 0.910 vs GB 0.839 需报告 bootstrap CI 和 p-value。

### Should-Fix（影响评分但不一票否决）

**[SF-1] Agent-agnostic claim 过度**
- R1-W4 + R2 AGREE (main point)。仅 2 个同质 agent（均在 SWE-Bench），ACR 第三 agent 仅 0.608。OH→SWE 反向迁移已报告（Appendix Table 9，R1 遗漏），双向对称（conf≥2: 0.995/0.995），但 scope 仍限于 SWE-Bench 生态。
- **要求**: 限缩为 "SWE-Bench 生态内的 agent 间可迁移性"，移除 "agent-agnostic" 表述。

**[SF-2] λ₃ 部署 caveat 和 2-LF 性能讨论不足**
- R1-W3 (Must-Fix) vs R2 REBUT (降级)。分歧：R2 引 Appendix G.6 显示 λ₃ 从不翻转 MV（100% agreement on overlapping windows），G.7 报告 2-LF 结果（RF -1.8pp, GB -12pp on conf≥2 cross-agent）。λ₃ 的实际贡献主要是 coverage（4K→43K windows）而非 label direction 改变。但 λ₃ 推理时不可用，2-LF 下 GB 降 12pp 对 "deployment-ready" claim 是显著 caveat。
- **要求**: 在正文中显著报告 2-LF only 完整结果（不仅在 Appendix），充分讨论 λ₃ 不可用时的部署影响。

**[SF-3] 统计检验部分缺失**
- R1-W5, R2 部分 REBUT。论文已报告若干 CI（39.4pp CI [37.9, 41.0], GB vs MV p<0.001, in-domain gap CI [7.44, 10.57]pp），但 gold 上 LLM 0.910 vs GB 0.839 缺 CI/p-value，label model 对比缺 CI，cross-agent LLM (N=500) 缺 CI。
- **要求**: 补充上述缺失的 bootstrap CI 和 p-values。

**[SF-4] Label model 负面结果归因需限定 scope**
- R1-W6 + R2 AGREE。Finding 3 应明确限定为 "3 binary LFs / 95% agreement / low-conflict 特定条件"——论文自己的 6-LF 实验证明 HMM 可 recover +6.5pp。实际部署仅 2 observable LFs 时，MV 退化为 AND 门，label model 讨论变得无意义。
- **要求**: 重新表述 Finding 3 scope 和条件限定。

**[SF-5] Contribution 2 证据单一**
- R2-W3 vs R1 REBUT (分歧)。R2 认为本质是 bug fix 副产物（embedding version mismatch 修复后性能提升），R1 认为发现来源不否定其价值但需更强支撑。仅 1 个 embedding version 变化作为自然实验不够。
- **要求**: 增加系统性 ablation 或降格为 observation。

**[SF-6] Claim 高度重复**
- R2-W4 + R1 AGREE。0.967/39.4pp/47.6pp/0.491/0.910/0.839 在 Abstract、Introduction、Experiments、Analysis、Conclusion 中近乎逐字重复 5 次。
- **要求**: 各 section 承担不同叙事功能，避免同一句话重复出现。

**[SF-7] "uniquely" 表述缺乏充分论证**
- R2-W1 + R1 AGREE。未比较 LF threshold-based classification、TF-IDF/BoW features、其他 rule-based anomaly detection。
- **要求**: 改为 "robust" 或增加更多 baseline。

### Minor

- **[MI-1]** 术语不一致：cross-agent vs cross-coding-agent 混用，label convention（positive class）在正文和附录间切换。(R2-W5 + R1 AGREE)
- **[MI-2]** `rath2026agentdrift` bib 条目不完整（缺 arXiv ID，author 仅 "Rath and others"）。(R1-W7 + R2-M2)
- **[MI-3]** Table 1 footnote $^b$ (GB leads fine-tuned probe by 1.65pp) 与正文叙述 (fine-tuned probe surpasses structural) 因 scope 不同而矛盾。(R2-M1 + R1 AGREE)
- **[MI-4]** Abstract "frequently" 未量化——后文有 28.5%/20.9% 应直接使用。(R2-M4 + R1 AGREE)
- **[MI-5]** 页数合规性需精确确认。R2 估算约 9 页，R1 认为可能合规（Limitations 不计页数）。(分歧，需 PDF 测量)

---

## Reviewer Consensus

两位 Reviewer 在以下核心问题上 **高度一致**：

| 问题 | R1 | R2 | 交叉结果 |
|------|----|----|----------|
| 循环评估是核心威胁 | W1 (Must-Fix) | N2 (critical) | 互相 AGREE |
| Gold set 不足 | W2 (Must-Fix) | N3 (critical) | 互相 AGREE |
| 叙事偏向结构特征 | — (遗漏) | W2 (warning) | R1 strongly AGREE |
| Agent-agnostic overclaim | W4 (Should-Fix) | — | R2 AGREE main point |
| 方法新颖性有限 | — | N1 (critical) | R1 AGREE w/ nuance |
| Claim 重复 | — | W4 (warning) | R1 AGREE |

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | 解读 |
|------|---------|---------|------|
| λ₃ 影响程度 | Must-Fix（概念混淆） | REBUT → Should-Fix（Appendix 数据表明实际影响有限） | 程度之争，非方向性分歧。λ₃ 不翻转 MV 但 2-LF 部署 caveat 确实不足 |
| Contribution 2 合法性 | Should-Fix（需更强支撑） | Should-Fix（本质是 bug fix） | 结论相同（需 strengthen），原因不同 |
| 页数是否超限 | 可能合规 | 估算约 9 页 | 需精确测量 |
| Claude API 匿名性 | 不构成问题 | Minor 提醒 | R1 论点更强（使用商业 API 是常态） |

---

## Questions to Authors

1. **[Critical]** 如果直接用 LF 规则（如 unique_cmd_ratio > threshold + edit_ratio < threshold）做 binary classification，silver-label 和 gold-label 上的 F1 各是多少？这是量化循环性影响的关键对照。
2. **[Critical]** Gold set 上 LLM 0.910 vs structural GB 0.839 的 bootstrap 95% CI 和 p-value 是什么？在 N=505 上 7.1pp 差异的统计效力如何？
3. **[Important]** λ₃ 推理不可用，2-LF 配置下 GB 跨 agent 降 12pp（Appendix G.7）。"Deployment-ready" claim 在 2-LF 条件下如何站住脚？
4. **[Important]** κ=0.39 的主要 disagreement 来源是什么？是否意味着 "stagnation" 本身缺乏清晰操作定义？如果是，这对整篇论文的前提意味着什么？
5. **[Important]** 19 个 residual features（移除 LF-overlapping）在 gold set 上的表现如何？这可以直接量化结构特征的非循环贡献。
6. **[Useful]** 为何不用 OH-specific few-shot examples 重测 LLM cross-agent 性能？当前 0.470 few-shot-CoT 可能是 SWE-Agent examples 的负迁移。
7. **[Useful]** Structural features 在 conf=1（歧义）窗口上的 isolated 性能是多少？

---

## Missing References

两位 Reviewer 共同建议补充：
1. **AgentMonitor / Who Monitors the Monitor** 等 agent 运行时监控系统工作
2. **Conformance Checking in Process Mining** — trace-level anomaly detection 与 window-level detection 的方法论相似性
3. **Post-Snorkel 弱监督改进** — Interactive Weak Supervision (Boecking et al. 2021), Language Model in the Loop (Smith et al. 2022) 等
4. **Self-Play / Self-Debugging approaches** — stagnation detection 的下游应用场景
5. **IAA 解读文献** — Landis & Koch (1977), Artstein & Poesio (2008) "Inter-Coder Agreement for Computational Linguistics"

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**Overall Score: weak reject (Main Conference) / borderline (Findings track)**

**R1**: 2.5/5 | Soundness 2.5 | Excitement 3 | Reproducibility 3.5 | Confidence 4
**R2**: 3/5 | Soundness 3 | Excitement 2 | Reproducibility 4 | Confidence 4

**Consolidated**: 2.75/5 | Confidence 4/5

**评估说明**：

本文选择了一个有实际价值的问题（agent stagnation detection），展示了系统性的实验设计和诚实的自我批判（循环性讨论、负面结果报告）。但存在四个结构性问题使其不适合 EMNLP Main Conference：

1. **循环评估贯穿核心 claims**：headline 数字全部基于 silver labels，而 silver labels 对结构特征天然有利。论文虽承认此问题，但叙事结构未做相应调整——读者被引导相信 0.967 是真实检测能力。

2. **Gold set 不足以打破循环**：N=505, κ=0.39, 仅 SWE-Agent conf≥2，不覆盖 OpenHands——跨 agent 迁移（论文最重要的 claim）完全没有非循环验证。

3. **方法新颖性有限**：核心方法是 Snorkel pipeline 的直接应用，30 维手工特征是标准工程。作为 empirical study 可接受，但前提是 findings 可靠——而 (1)(2) 削弱了 findings 的可靠性，构成双重打击。

4. **叙事不平衡**：gold 上 LLM judge 0.910 显著优于 structural GB 0.839，但论文淡化此事实，以 silver-label 上 LLM 的 "collapse" 为主线——这在非循环视角下不成立。

**改进路径**：(a) 以 gold 数字重构叙事；(b) 扩大 gold set（1000+, 含 OH, 含 conf=1）；(c) 明确定位为 Findings track empirical study；(d) 重新平衡 LLM vs structural 的叙事。如果这些改进到位，论文有望达到 Findings track 的标准。

---

## Detailed Comments

### Abstract & Introduction
- Headlines 需用 gold 数字替换 silver 数字
- "uniquely enable" → "robustly enable"
- "frequently" 应量化（28.5%/20.9%）
- Contribution 2 需 strengthen 或降格
- 减少数字重复——findings 在 intro 仅概述方向，不重复精确数字

### Method (§3)
- §3.2 应更显著讨论 Snorkel pipeline 的标准性，以及本文领域适配中的具体挑战
- λ₃ 的 privileged nature 应在首次出现时即标注 caveat（不仅在 Limitations）
- 30 维特征中 11 个 LF-overlapping 的事实应在 §3.3 提前披露

### Experiments (§4)
- "Main Results" (§4.2) 应重命名或重构——当前标题暗示 silver-label 结果是主要结果
- §4.7 Gold Set 应升级为核心结果节而非附属
- 2-LF 部署结果应从 Appendix 提升至正文

### Analysis (§5)
- §5.1 循环性讨论是论文的亮点，但需与叙事结构匹配（不能承认循环性的同时仍以 silver 为 headline）
- §5.2 Feature Overlap 结论 "LF-overlap features alone exceed full model" 进一步加强了循环性担忧——但被低调处理

### Conclusion (§6)
- 过于简短（3 句），未讨论 limitations 的 implications
- 应反映 gold 上 LLM > structural 的 nuanced picture

### Appendix
- 内容丰富且有价值，尤其是 G.5 (gold protocol)、G.6 (λ₃ analysis)、G.7 (2-LF degradation)
- G.7 的 2-LF 结果应提升至正文
- G.9 bidirectional transfer 在正文仅一句提及，可在 §4.3 给予更多篇幅
