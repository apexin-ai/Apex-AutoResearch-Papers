---
round: 14
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T15:18:25.111514+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 16 (Fresh Review)

**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
**Venue**: EMNLP 2026 Long Paper (ARR May cycle)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人 — R1 方法严谨性+实验设计, R2 新颖性+完整性+写作质量
**轮次**: 1 轮独立审稿 + 1 轮交叉分享，达成共识

---

## Summary

论文系统比较了三种 execution-free 代码修复验证公式（CLS 分类、CWM 生成、TRAJ 轨迹级），在 Qwen3 和 DeepSeek-Coder 两个模型族、function-level 和 repo-level 两个复杂度层级、5 seeds 下进行实验。核心发现：function-level 三公式近似等价（CLS–CWM TOST p=0.007），repo-level 在 ≤8B LoRA 下 CLS 显著优于 CWM（18–26pp gap，format collapse 驱动）。14B 初步数据显示三公式收敛至 1.07pp 以内。

---

## Strengths

**S1. 统计方法论的深度和一致性（两位 Reviewer 共识最强优势）。** TOST + Holm-Bonferroni + Bayesian ROPE + ICC + clustered bootstrap + mixed-effects LPM 的多层验证框架在 NLP 实证论文中罕见。每种方法的适用性和局限性均有讨论。[§3.1, §3.4, Appendix G-M]

**S2. 跨模型族一致性。** 在 Qwen3 和 DeepSeek-Coder 两个模型族上均展示 function-level CLS-CWM 等价性和 repo-level 分歧，增强了结论的 robustness。[Table 1-3]

**S3. 实用的故障模式分类。** Format collapse / decision collapse / aggregation penalty 的分类（Table 4）为实践者选择验证公式提供了可操作的诊断标准，超越单纯的准确率对比。[§3.5, Table 4]

**S4. 诚实的 negative results 报告。** CLS–TRAJ 功效不足、四种 intervention 全部失败、CWM parseable bias、routing heuristic <0.4pp 等均被坦率报告。[§3.4, §3.5, Appendix I, N]

**S5. 充实的附录（13 页）。** 涵盖 oracle advantage、ablation studies、qualitative error analysis、TOST sensitivity、Bayesian ROPE、mixed-effects regression 等，为主文结论提供了充分的 robustness check。

**S6. Related Work 覆盖全面。** 引用了 SWE-RM、Patch Reasoner、GenRM/GenPRM、CodeRM、Aletheia、CodeScaler 等近期高度相关工作，cross-domain 与 math reasoning 的对比也有涉及。[§4]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [critical, consensus] Complexity-dependent 核心叙事存在 complexity 与 output format/length 的未解耦混淆。**
论文将 function→repo 分歧归因为 "code complexity"，但论文自身的分析已表明 format collapse（53–74% unparseable, Table 4）是 repo-level CWM 退化的直接机制。Function-level CWM 输出平均 ~5–15 tokens；repo-level 平均 ~477 tokens。这更直接指向 output format/length 效应。四种 intervention（capacity ×2、majority voting、relaxed matching、LoRA rank 32）均未攻击 output length 本身（如 constrained decoding）。如果退化主要由 output format 驱动，则 "complexity-dependent formulation choice" 的推荐需重新表述。**两位 Reviewer 共识。** [§3.5, §3.6, Table 4, Appendix I, Limitations]

**N2 [critical, consensus] ≤8B LoRA 范围限制下标题和 abstract 的泛化声明过广。**
标题 "A Systematic Comparison of Execution-Free Verification Formulations for Code Repair" 暗示通用性，但所有实验限于 ≤8B + LoRA。Abstract 虽有 "≤8B LoRA fine-tuning" 限定，但标题无。14B "capacity-dependent convergence" 仅基于 3 seeds × 1 family（Qwen3），Figure 2 仅 3 个 scale points（4B, 8B, 14B），degrees of freedom = 0。Abstract 中给予此观察不成比例的 prominence。**两位 Reviewer 共识。** [Title, Abstract, §3.3, Figure 2]

**N3 [critical, consensus] CLS–TRAJ 等价检验 power ~0.3 导致该比较 uninformative，但论文措辞暗示 "可能不等价"。**
TOST power ~0.3 意味着即使 CLS 和 TRAJ 真正等价，也有 70% 概率检测不到。Abstract "TRAJ parity is not confirmed after multiple comparison correction at current power (~0.3)" 虽有功效限定语，但放在 abstract 中仍容易让读者误解为存在差异的证据。Bayesian ROPE P(ROPE)=0.542（per-test level）同样 inconclusive。CLS–TRAJ 比较是论文三组比较之一，若该比较 uninformative，核心贡献缩水。**两位 Reviewer 共识。** [Abstract, §3.4, Appendix G.1]

**N4 [critical, R1 primary, R2 implicit agree] Repo-level 2–3 seeds 无法可靠支撑 18–26pp gap 的 formulation 归因。**
Training seed 是真正的 replication unit，n=2-3 的 bootstrap CI 可靠性极低。Mixed-effects LPM 用 n=56,480 per-test observations 但 seed 内高度相关（ICC=0.191），有效自由度远低于名义值。论文 §3.5 已有 "exploratory due to limited seed coverage" 标注，但 Table 3 和 abstract 的呈现方式仍偏向于 definitive 结论。[§3.5, Table 3, Appendix M, O]

### Should-Fix（影响评分但不一票否决）

**W1 [warning, consensus] 统计方法多样但主次层次不清。** TOST/Bayesian ROPE/clustered bootstrap/mixed-effects LPM/GEE/ICC 多种框架但未声明 primary vs robustness check。LPM vs GEE 对 model identity 给出不一致结论（p=0.002 vs p=0.449），读者无法判断应采信哪个。[§3.4, Appendix M]

**W2 [warning, consensus] TRAJ 比较与 CLS-CWM 比较性质差异未充分区分。** CLS/CWM 是同一 task 的不同 formulation（per-test），TRAJ 是不同 task structure（variant-level）。Abstract 承认 "inherently confounded" 但正文 Table 1-3 仍并列呈现。[§2.1, Table 1-3]

**W3 [warning, consensus] Error complementarity 作为 contribution 被高估。** Oracle routing 仅 single-seed（90.63%），simple heuristics <0.4pp。本质上是 negative result——互补性存在但无法被简单利用。论文 §1 Contribution 2 已重写为 negative result framing，但措辞仍偏正面。[§3.6, §1]

**W4 [warning, R1] CWM format collapse 的定性归因不清：inherent formulation limitation vs engineering artifact。** 53–74% unparseable defaulting to majority class。四种 interventions 失败但 intervention 空间有限——constrained decoding 未实验验证。如果 format collapse 可通过 engineering 缓解，18–26pp gap 中有多少归因于 decoding strategy 而非 formulation？[§3.5, §3.6, Limitations]

**W5 [warning, R1] TOST ±2pp margin 缺乏正式论证。** "Deployment relevance" 但无推导过程、无 code verification 领域先例引用。虽未 pre-registered 但已诚实披露。Sensitivity analysis 显示 minimum margin ±1.52pp 仅低 0.48pp。[§3.4, Appendix G]

**W6 [warning, R1] 训练数据量严重不对称未充分控制。** CLS/CWM ~70K instances vs TRAJ ~1,386 variant-level instances。Downsample ablation（Appendix O）控制了 volume 但未控制 label granularity（per-test vs variant-level），后者是 formulation-inherent confound。[§3.1, Appendix O]

**W7 [warning, R2] 跨领域 code vs math GenRM 对比分析浅薄。** 仅 observation-level 对比，未分析 WHY 代码验证中 generative 不如 discriminative（与 math reasoning 相反）。[§4, §5]

**W8 [warning, R1] 外部效度受限于合成数据和 Python-only。** Synthetic mutation operators vs real developer patches 的分布差异可能系统性影响 formulation 比较结论。Limitations 已提及但讨论不深。[Limitations, Appendix P]

---

## Reviewer Consensus [AGREE]

1. **Complexity vs output format 混淆**（R2-N1, R1 AGREE）：核心叙事框架需修正
2. **≤8B scope 泛化过广**（R2-N2, R1 AGREE）：标题应加限定
3. **CLS–TRAJ 比较 uninformative**（R1-N1, R2-W1 AGREE）：power ~0.3 使该比较无信息量
4. **Repo-level seed 不足**（R1-N2, R2 implicit AGREE）：2–3 seeds 无法可靠归因
5. **Error complementarity 高估**（R2-W2, R1 AGREE）：<0.4pp gain 是 negative result
6. **统计方法主次不清**（R2-W5, R1 AGREE）：应声明 primary framework
7. **Abstract 14B convergence 过强**（R2-W6, R1 AGREE）：仅 3 seeds × 1 family

## Reviewer Divergence [REBUT]

1. **单一 benchmark 限制泛化**（R2-W3, R1 REBUT）：R1 认为 HumanEval+MBPP 和 SWE-bench Verified 是领域标准 benchmark，且已有 per-mutation-type stratification，单一 benchmark 不构成 strong weakness。
2. **Template ablation**（R2-Q4, R1 REBUT）：R1 认为 prompt template 是 formulation 定义的一部分而非独立 confound——CLS 用 classification template 是因为 CLS 就是 classification。

---

## Questions

**Q1** [R2, R1 AGREE]: 是否尝试过在 function-level 让 CWM 生成更长输出（如完整执行 trace），以检验 repo-level 退化是否主要由 output length 驱动而非 task complexity？

**Q2** [R1]: 是否做过 downsample CLS 到 ~1,386 instances 与 TRAJ 对比？如果 CLS 在此数据量下也表现类似 TRAJ，formulation 差异结论不成立。（注：论文已在 Appendix O 报告 CLS downsample 到 ~8K 的结果为 80.74%，仍高于 TRAJ 72.92%，但未进一步下采样至 ~1,386。）

**Q3** [R2, R1 AGREE]: 14B capacity-dependent convergence 是否有 DeepSeek-Coder 14B 或 32B 的任何初步证据？

**Q4** [R1]: 去除 unparseable outputs 后（即只看 parseable subset），CLS vs CWM 的 repo-level gap 是否缩小或反转？（注：论文报告 parseable-only accuracy 38–43%，低于 majority baseline，说明 parseable subset 中 CWM 更差。）

**Q5** [R2, R1 AGREE]: Error complementarity 在不同 seeds 之间的一致性如何？互补模式是否在 5 个 seeds 中稳定存在？

**Q6** [R1]: Mixed-effects regression z=−23.7 是否主要由 n=56,480 驱动而非大 effect size？（注：Appendix M 已报告 logistic regression OR=0.31, AME=−21.6pp，与 LPM concordant。）

**Q7** [R2]: Matched-context ablation 只解释 CLS-CWM gap 的 <3%。如果 context overlap 对 CLS-CWM 影响小，为什么 TRAJ 的 context 差异（collapsing per-test into variant-level）就构成 "inherent confound"？

---

## Missing References

- **Constrained decoding**: Scholak et al. (2021) PICARD; Poesia et al. (2022) Synchromesh — 与 CWM format collapse 缓解直接相关（R1 提出）
- **Equivalence testing in NLP**: Dror et al. (2018) "The Hitchhiker's Guide to Testing Statistical Significance in NLP" — equivalence testing 应用讨论（R1 提出）
- **Ma et al. (July 2025)**: "Rethinking Verification for LLM Code Generation: From Generation to Testing" NeurIPS 2025 — 系统探讨 code generation 验证（R2 提出，需确认引用真实性）

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 已完成

| 严重性 | 位置 | 发现 |
|--------|------|------|
| warning | page 23 | Appendix 末页仅顶部约 8 行文字，~90% 页面空白 |
| info | pages 1-2 | 前 2 页无 display item，第一个视觉锚点在 page 3 |
| info | page 3 | Figure 1 内部文字字号偏小（约正文 60-65%），接近可读性下限 |
| info | pages 16-17 | Appendix H 连续 2 页纯文本，可考虑用代码片段或表格打破 |
| info | pages 20-22 | Appendix M-O 连续 3 页纯文本统计分析 |

---

## Overall Assessment

**评分: 3.5 / 5 — Borderline Conference**

**置信度: 4/5**（两位 Reviewer 均熟悉统计检验方法论、代码修复评估和 LLM fine-tuning 实验设计）

**理由**: 论文的统计方法论是其最大亮点——TOST 等价检验 + 多层 robustness check 的框架在 NLP 实证论文中罕见，failure mode taxonomy 有独立实用价值。但核心贡献受限于三个方面：

1. **新颖性不足**: 核心发现（短输出公式等价、长输出生成退化）在直觉上可预测，缺乏 surprising insight（R1/R2 Excitement 均为 3/5）。
2. **核心叙事框架问题**: "Complexity-dependent" 的归因可能更准确地是 "output-format-dependent"，这不是措辞问题而是对结论 takeaway 的根本性影响。
3. **泛化范围有限**: ≤8B LoRA × 2 families × synthetic data × Python-only 的范围限制了结论的实用覆盖面。

**EMNLP 2026 定位**: 按 ARR 评分标准，3.5 = Borderline Conference。论文质量足够达到 Findings 水平（3.0），但 main conference 需要更强的 novelty 或更明确的 scope 限定 + 解耦 complexity vs output format 的核心混淆。若能修复 N1（核心叙事框架）和 N2（scope 限定），评分有望提升至 3.5–4.0 区间。

---

## Detailed Comments

**格式合规**: 正文 8 页合规；Limitations section 存在且覆盖 3 点；Abstract ~185 words（<200）；匿名合规（"Anonymous ACL submission"）；ACL review 模板正确。

**Appendix**: 13 页附录内容充实但部分 appendix（H, M-O）连续纯文本偏密。末页（p.23）~90% 空白，建议内容重分布。

**小问题**: "pp" 缩写首次使用未定义（§1）；Table 1 DeepSeek "2 seeds" 注释在 caption 中容易被忽略；§3.4 "523 variant-level instances across five seeds" 应明确为 Qwen3-only 分析。