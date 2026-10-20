---
round: 5
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T11:21:53.499042+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 6 (Fresh Review)

**论文**: The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study
**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)
**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 写作完整性 + 格式合规）
**Overall**: 3.0 / 5（Findings）— 两位 Reviewer 一致
**Confidence**: 4 / 5 — 两位 Reviewer 一致

---

## Summary

本文系统比较了三种 execution-free code verification formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹评分），在两个模型家族（Qwen3-4B/8B、DeepSeek-Coder-6.7B）、两个复杂度级别（function-level、repo-level）、多 seed 条件下进行匹配实验。核心发现：function-level 三者近等价（TOST p=0.007, 5 seeds），repo-level CLS 领先 CWM 19-26pp（≤8B LoRA regime）。论文还提供了 failure mode taxonomy、error complementarity 分析和 oracle framework。

---

## Strengths

**S1** [R1+R2 共识] **填补真实文献空白**：首个在 matched conditions 下系统比较三种 execution-free verification formulations 的工作，研究问题定义清晰且有实际价值。

**S2** [R1+R2 共识] **统计方法论超越 NLP 常见标准**：TOST equivalence testing（而非仅用 p-value 证明差异不显著）、clustered bootstrap（114 clusters, 10K resamples）、ICC with design effect、Holm-Bonferroni correction (k=4) 的组合在 NLP 实证论文中罕见，体现了良好的方法论意识。

**S3** [R1+R2 共识] **Function-level 等价结论可信且有价值**：5 seeds × 2 model families 的充分支撑，TOST 在 ±1.52pp 仍 reject。"CWM 在 function-level 并不比 CLS 差"是一个违反直觉的发现（CWM task difficulty 明显更高），这实际上是论文最有力的结果。

**S4** [R1+R2 共识] **极高的实验透明度**：~8 页附录包含 rank ablation、majority voting、sequence-length ablation、few-shot baseline、per-mutation breakdown、error analysis、TOST sensitivity、variant-level effect sizes、parseable bias analysis 等。几乎所有可预见的 reviewer 问题都有对应的消融实验。Limitations 讨论异常详尽。

**S5** [R1] **Failure mode taxonomy 有实用价值**：§2.2 和 Table 4 的三类 failure mode（format collapse、decision collapse、aggregation penalty）为 practitioners 提供了可操作的 diagnostic framework。

**S6** [R2] **写作质量良好**：全文主线清晰，无 AI 写作痕迹（无 em-dash、无黑名单词汇、段落长度自然），Introduction 5 段叙事结构完整。格式基本合规（8 页正文、`[review]` option、匿名完整、Limitations section 存在、Checklist 逐项填写）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [R1-N1 + R2-N2, CONSENSUS] **Repo-level 核心 claims 基于 single-seed，within-formulation variance 与 between-formulation gap 量级相当**

论文最核心的 repo-level claim（CLS-CWM gap 19-26pp）几乎全部基于 seed 42 的单次实验。Table 10 揭示了 within-formulation 的巨大 seed 方差：DeepSeek CLS per-test accuracy 82.51% (s42) vs 63.51% (s123)，波动 ~19pp；variant-level 81.25% vs 29.17%，波动 >50pp。Within-formulation seed variance (~19pp per-test) 与 between-formulation gap (19-26pp) 量级相当。

§3.7 声称 "the observed 19-26pp gap exceeds any individual confound by an order of magnitude"，但 Table 10 数据直接反驳此 claim。论文在 function-level 使用了 3-5 seeds 配合 TOST，展示了良好的统计方法论意识，但在最重要的 repo-level claim 上没有贯彻同标准。Table 3 没有 ±std 或 CI。

**修复方向**：(1) 补充至少 2-3 seeds 的 repo-level 实验并报告 CI；(2) 如资源不允许，将所有 repo-level conclusions 明确标注为 "preliminary/suggestive under single-seed design"，修正 §3.7 "order of magnitude" 措辞。

**N2** [R1-N2, R2 AGREE] **Checkpoint selection 系统性偏向 CLS**

§3.1 明确说明所有 CWM 运行因 NaN val loss 使用 final-epoch checkpoint，而 CLS 部分使用 val-selected checkpoint。这是影响全部 CWM 运行的系统性偏差，非随机噪声。对一篇以 "matched conditions" 为核心方法论贡献的论文，checkpoint selection 不 matched 是核心矛盾。Generation 任务的 overfitting dynamics 与 classification 不同，CWM checkpoint 效应可能 > 论文估计的 ~2pp。偏差方向与 observed effect 一致（CWM 被系统性低估）。

**修复方向**：(1) 修复 CWM val loss 计算使 checkpoint selection 一致；(2) 提供 CLS final-epoch vs val-selected 消融量化 bias；(3) 将此从脚注级 caveat 升级为 §3.7 中的 prominent confound。

**N3** [R1-N4, R2 AGREE] **Oracle ensemble accuracy 数值自相矛盾**

§3.6 报告 "oracle combination achieves 90.63%"，Conclusion 报告 "oracle ensemble: 90.63%"。但 Appendix H(a) 报告 "achieves 96.03% accuracy, +3.12pp over 87.51%"。验证：87.51 + 3.12 = 90.63 ≠ 96.03。正文与附录数字矛盾。Error complementarity 是核心 contribution 之一，数字不一致直接损害可信度。

**修复方向**：核实并统一所有 oracle accuracy 数字。

**N4** [R2-N1, R1 AGREE] **Novelty 有限：核心发现可预期，叙事权重错配**

"Classification > generation when outputs are complex"（repo-level CLS 领先 CWM 19-26pp）在概念上可预期：CWM 需精确生成长序列（~477 tokens），错误乘法累积；CLS 只需 1 token。论文的 failure mode taxonomy（format collapse, token exhaustion）本质上是形式化这个直觉，而非挑战它。

更重要的是 claim-evidence 权重错配：论文将 repo-level divergence（可预期 + single-seed + checkpoint confound）作为 headline，而 function-level equivalence（违反直觉 + 统计 robust）在叙事中处于从属地位。"CWM 在 function-level 并不比 CLS 差"这一结论实际上更有趣，因为 CWM 的 task difficulty 明显更高。

**修复方向**：重新平衡叙事，将 function-level equivalence 升为核心故事，repo-level divergence 降为 supporting evidence with explicit caveats。

---

### Should-Fix（影响评分但不一票否决）

**W1** [R1-N3, R2 AGREE WITH NUANCE; severity 分歧：R1 critical, R2 should-fix] **SESOI ±2pp 缺乏 domain-grounded justification**

"±2pp corresponds to ~15 additional errors per 500 predictions" 是循环论证（restated 含义而非 domain justification）。Lakens (2017) 要求 SESOI 基于 domain knowledge。"approximately 30% headroom" 计算有误：(2.0−1.52)/2.0 = 24%。R2 认为 TOST 是辅助证据，function-level equivalence 不依赖 margin 选择，故降为 should-fix。

**修复方向**：从下游应用角度重写 SESOI justification（如 best-of-n pipeline impact）；修正 headroom 计算。

**W2** [R1-W3 + R2-W2, CONSENSUS] **CWM regime qualifier (≤8B LoRA) 在 Abstract/Conclusion 不充分**

Abstract "generation-based simulation falling below majority baseline" 无 regime qualifier。Conclusion practical recommendations 同样缺失。读者可能误解为 CWM 在所有场景下都低于 majority baseline。CWM 劣势可能是 capacity artifact（≤8B）而非 formulation 固有限制。

**修复方向**：Abstract/Conclusion 中所有 CWM 劣势 claim 加 "under ≤8B LoRA fine-tuning" 限定。

**W3** [R1-W4, R2 AGREE+] **Re-repair negative result (δ=0) 与 diagnostic granularity narrative 矛盾**

Re-repair pilot (Appendix H(j), n=44, p=0.42, effect size δ=0) 是唯一测试 diagnostic value 是否 translates to downstream benefit 的实验，得到 negative result。论文以 "insufficient sample size (power ~0.3)" dismiss，但 effect size 本身为零——增加 sample size 不会改变结论方向。这与第四条 contribution "Diagnostic granularity with configuration-dependent cost" 直接矛盾。R2 认为此问题 severity 应更高。

**修复方向**：将 diagnostic granularity 从 core contribution 降级为 "potential advantage pending downstream validation"。

**W4** [R1-W1, R2 AGREE] **TRAJ 训练配置差异过大，downsample ablation 未控制 label granularity**

TRAJ ~400 instances vs CLS/CWM ~70K，lr 不同，且 downsample ablation 只控制 volume 未控制 granularity（per-test vs variant-level labels），volume-matched ≠ information-matched。

**修复方向**：明确讨论 volume vs granularity 区别。

**W5** [R1-W2, R2 AGREE] **"Formulation × model × complexity interaction" 未做形式化统计检验**

论文反复使用此三阶交互表述（Abstract, §1, §3.5, §5），但从未通过 factorial ANOVA 或 mixed-effects model 检验。所有证据是描述性的。在 single-seed repo-level 数据下，三阶交互统计检验甚至不可行。

**修复方向**：降级 "interaction" 措辞为 "observed pattern"。

**W6** [R2-N3 → R1 rebut to should-fix; severity 分歧] **合成 mutation 数据外部效度未验证**

所有训练/测试数据基于 synthetic mutation operators。R1 认为论文关心 relative ranking 而非 absolute performance，若 distribution shift 是 formulation-agnostic 的则排序有效，故定为 should-fix。R2 认为应为 must-fix。采纳 should-fix，但记录分歧。

**修复方向**：更明确讨论 Andrews/Just 引用的适用范围；如可行在真实 bug 上做 transfer sanity check。

**W7** [R2-W1, R1 AGREE] **Abstract ~120-130 词偏短**

低于 ARR 推荐 150-250 词。缺少问题重要性论述和 function-level equivalence 这个更 surprising 结论。

**修复方向**：扩展至 ~180 词。

**W8** [R2-W3, R1 PARTIAL REBUT] **可能遗漏近期相关工作**

R2 指出 Aletheia (2601.12186), VeRPO (2601.03525), ExecVerify (2603.11226)。R1 要求 R2 说明具体关系——若涉及 formulation comparison 则为重要遗漏，若仅为 general code verification 则已有 60 条引用覆盖度可能足够。待验证。

---

### Minor（不影响接收）

- **M1**: Tables 1-3 缺少次优下划线标记（NLP 标准做法）
- **M2**: Checklist C4 version numbers 需补全（当前 "Partially"）
- **M3**: Figure 2 bar chart 信息密度偏低，可加 CI 或 per-model breakdown
- **M4**: 8 条 bib entry 未被 OpenAlex 索引（较新 preprint，不影响引用真实性）
- **M5**: §3.3 中 function-level 和 repo-level 数据在同段交叉引用易混淆

---

## Reviewer Consensus

以下问题两位 Reviewer 独立提出并在交叉分享中确认：

| Issue | R1 | R2 | Cross-share |
|-------|----|----|-------------|
| Single-seed repo-level | N1 (critical) | N2 (critical) | [AGREE] 最高共识 |
| Checkpoint selection bias | N2 (critical) | — | R2 [AGREE] |
| Oracle number contradiction | N4 (critical) | — | R2 [AGREE] |
| Novelty / claim-evidence rebalancing | — | N1 (critical) | R1 [AGREE] direction |
| CWM regime qualifier | W3 (warning) | W2 (warning) | [AGREE] 独立一致 |
| Re-repair vs diagnostic value | W4 (warning) | — | R2 [AGREE+] severity 更高 |
| TRAJ training confound | W1 (warning) | — | R2 [AGREE] |
| Interaction not formally tested | W2 (warning) | — | R2 [AGREE] |
| Synthetic data validity | W5 (warning) | N3 (critical) | 分歧：R1 should-fix, R2 must-fix |
| Abstract 偏短 | — | W1 (warning) | R1 [AGREE] |

## Reviewer Divergence

| Issue | R1 | R2 | 分歧性质 |
|-------|----|----|----------|
| SESOI justification severity | N3 (critical) | AGREE with nuance → should-fix | R2 认为 TOST 是辅助证据 |
| Synthetic data severity | W5 (should-fix) | N3 (must-fix) | R1 认为 relative ranking 不受影响 |
| Missing references (Aletheia etc.) | PARTIAL REBUT | W3 (should-fix) | R1 要求说明具体关系 |
| Venue fit | REBUT | W5 (should-fix) | R1 引用 EMNLP 近年 code 论文 |

---

## Questions for Authors

1. [R1-Q1] Table 10 中 DeepSeek CLS 19pp seed variance 中 preprocessing vs checkpoint vs random seed 各贡献多少？
2. [R1-Q2] bf16-only TOST p-value 是多少？如果 p>0.05，equivalence claim 需重新 qualify。
3. [R1-Q3] Repo-level ICC=0.3146 对应 DEFF=114.4，effective n≈86。Repo-level CLS-CWM 的 clustered bootstrap 95% CI？
4. [R1-Q4] CWM unparseable 默认改为 FAIL 或 random 50/50 时 accuracy 如何变化？
5. [R2-Q1] CWM 原始论文 (Meta FAIR, 32B) 在 repo-level 的表现如何？是否有证据支持 CWM 劣势是 capacity-limited？
6. [R2-Q2] 论文声称 error complementarity motivates "complexity-aware routing"——是否有 preliminary 验证？

---

## Missing References

- CWM 原始论文 (FAIR, 32B) 的 benchmark 结果需在 Related Work 中更详细对比（R1）
- Aletheia (2601.12186), VeRPO (2601.03525), ExecVerify (2603.11226) — 待验证相关性（R2，R1 部分反驳）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，无外部审稿结果。

---

## Overall Assessment

**评分：3.0 / 5（Findings）— 两位 Reviewer 一致**

**EMNLP 2026 ARR 评分对应**：3.0 = Findings（可被 Findings 接收）

**核心判断**：

论文填补了一个真实的文献空白（execution-free verification formulation 的系统比较），统计方法论和实验透明度超越 NLP 常见标准。Function-level equivalence 结论有 5 seeds × 2 model families 的充分支撑，是论文最 robust 的发现。

但论文存在四个互相关联的核心问题：(1) repo-level claims 基于 single-seed，within-formulation variance 与 between-formulation gap 量级相当；(2) checkpoint selection 系统性偏向 CLS；(3) 核心发现（classification > generation at repo-level）在概念上可预期，novelty 主要在 methodology 而非 insight；(4) oracle ensemble 数字矛盾。这些问题共同将论文定位在 Findings 而非主会议。

**如果修复**：补充多 seed repo-level 实验（N1）、修复 checkpoint 一致性或量化 bias（N2）、统一 oracle 数字（N3）、重新平衡叙事以 function-level equivalence 为核心（N4），论文有潜力提升到 3.5 (Borderline Conference)。但补充 repo-level 多 seed 实验需要额外计算资源和时间，在 ARR May deadline (5/25) 前可能不可行。

---

## Detailed Comments（逐节）

### Abstract
- ~120-130 词偏短（ARR 推荐 150-250）
- "generation-based simulation falling below majority baseline" 缺 regime qualifier (≤8B LoRA)
- 缺少问题重要性动机和 function-level equivalence 的突出
- 建议扩展至 ~180 词

### Introduction
- 5 段叙事结构完整，逻辑清晰
- "formulation × model × complexity interaction" 未经统计检验，建议降级为 "observed pattern"
- 第四条 contribution (diagnostic granularity) 与 re-repair negative result (δ=0) 矛盾，需降级或加 caveat

### Method (§2)
- Formulation 定义清晰，§2.2 failure mode taxonomy 有价值
- §2.3 Oracle framework 的 κ 中 n 定义不明确

### Experiments (§3)
- §3.1 Setup 文档化充分
- §3.2 Function-level 结论 robust（5 seeds, TOST, 2 model families）
- §3.3 Scaling 结论受限于 2 seeds（42, 123），但 direction 一致
- §3.4 TOST equivalence: SESOI justification 需加强，headroom 计算有误
- §3.5 Repo-level: **最弱环节**——single-seed, checkpoint confound, high within-formulation variance
- §3.6 Analysis: oracle 数字矛盾必须修复；re-repair negative result 需更平衡呈现
- §3.7 Threats: "order of magnitude" 表述被 Table 10 反驳

### Related Work (§4)
- 三段结构清晰，归纳优于列举
- Process vs outcome supervision 的 NLP 框架连接有价值
- 引用覆盖基本充分（60 条），但可能遗漏若干近期工作（待验证）

### Conclusion (§5)
- CWM 劣势 claim 需加 regime qualifier
- Practical recommendations 过于 definitive given single-seed repo-level evidence

### Appendices
- 极其详尽（A-N, ~8 页），覆盖几乎所有 reviewer 可能的疑问
- Appendix H(a) oracle 数字需修正
- Appendix M Threats 讨论 "order of magnitude" 需修正

### Checklist
- 逐项认真填写，C4 需补全 version numbers
