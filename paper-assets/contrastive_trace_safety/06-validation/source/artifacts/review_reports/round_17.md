---
round: 17
review_mode: fresh
overall_score: 3.0 Findings
timestamp: 2026-05-19T10:09:02.922860+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 17 (Fresh Review)

**论文**: "Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models"
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性+统计分析; R2: 新颖性+完整性+写作质量）

---

## Summary

本文研究推理模型（reasoning LLMs）中隐状态安全探针的层选择敏感性问题。在 4 个推理模型（R1-8B, OT-7B, QwQ-32B, R1-32B）上使用 HarmThoughts 数据集，评估了 5 种层选择指标对 HS vs. text probe 结论的影响。核心发现是层选择指标的选择可以完全逆转 HS 优势结论：biased composite metric 系统性选择浅层（L2/L10），而 threshold-dependent metrics 一致选择深层（L63）。在 corrected layers 上，384d MiniLM baseline 下 3/4 模型通过 HB 校正（第 4 个 R1-32B 为 position-mediated），但升级至 1024d BGE-large 后仅 1/4 存活。

---

## Strengths

- **S1 [共识]: 层选择敏感性是重要且被忽视的方法论问题。** Table 2 清楚展示了 biased composite 在 32B 模型上选浅层、threshold-dependent metrics 选深层的系统性分歧。cosine volatility 分析（App B, Table 5）提供了可信的机制解释（浅层 representation compression 导致 crossing rate 膨胀）。这一发现对安全探针研究社区有直接实用价值。

- **S2 [共识]: 统计方法论极为周全。** BCa bootstrap (10,000 resamples) + 精确排列检验双重验证、Holm-Bonferroni 在 12-test 和 4-test 两种框架下的校正、position residualization、PCA/random projection 容量控制、CP 标注扰动分析、multi-seed 稳定性——构成了完整的鲁棒性体系。

- **S3 [共识]: 透明度出色。** Bug disclosure (App I, M002)、负面结果结构化呈现 (Table 8, 七种方法失败的诊断)、每个 32B 结论标记 † 并附 power analysis、三级证据系统 (strong/moderate/qualified)。R1-32B 的 position-mediated advantage（residualized gap +1.9pp, p=0.914）被如实报告。

- **S4 [共识]: 负面结果具有诊断价值。** 七种替代方法的失败提取了 CP 检测的四个必要条件（directional, gradual, model-specific, linearly separable），为后续工作定义了清晰的方法论边界。

- **S5 [共识]: 写作质量良好，格式合规。** 正文 8 页 ✓；`\usepackage[review]{acl}` + 行号 ✓；Anonymous ✓；Limitations section ✓；Responsible NLP Checklist ✓；无 AI 写作痕迹（em-dash 0, -ing 结尾模式 0, 黑名单词 0）。

---

## Weaknesses

### Must-Fix（影响接收决定）

- **W1 [Critical, 共识]: Abstract/Introduction framing 与证据强度不匹配。**
  - Abstract 以 384d MiniLM 下 "+19.2 to +21.9pp" 为核心数字，"three of four models" 给读者 3 个模型均有 robust HS advantage 的印象。但：(a) R1-32B 完全 position-mediated（residualized gap +1.9pp, p=0.914）；(b) 升级至 BGE-large 1024d 后仅 1/4 模型存活 HB。Discussion 的 "the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference" 是根本性限定，但在 Abstract/Introduction 中被结构性弱化。
  - **修改要求**: Abstract 需 (1) 区分 7-8B (robust) 和 32B (exploratory/position-mediated)；(2) 同时报告 384d 和 1024d 结果；(3) encoder-conditional 限定与 Discussion 同等 prominence。

- **W2 [Critical, R1 主导/R2 升级同意]: 32B 样本量 (n=19-20) 不足以支撑可靠统计推断。**
  - BCa 加速度参数在 n=19-20 上估计不稳定；MDE 为 8.6-9.5pp；R1-32B 仅 25% coverage (5/20 traces)；LOO-CV 显示 BA-optimal 层跨 fold 跨度达 24 层。超参数搜索空间 (2,240 configs) 与 per-class 验证集 (4-10 traces) 严重不匹配。Nested CV 未采用。K=5 声称 pre-selected on R1-8B pilot 但无 pilot 细节。
  - **修改要求**: (1) 32B 结论在 Abstract 中明确标记为 exploratory；(2) 报告 validation-test gap；(3) 解释 nested CV 不可行的原因或提供替代方案；(4) 提供 K=5 pilot 细节。

- **W3 [Critical, R1 主导/R2 REBUT 部分接受]: "Biased vs Corrected" 指标分类的 post-hoc 性质。**
  - 将 5 种指标分为 "biased" 和 "corrected" 是事后观察归纳，而非先验假设。R2 提出 cosine compression (App B, Table 5) 提供了独立的机制支撑，这一 REBUT 有一定道理——论证的物理基础（浅层表征压缩）是独立可验证的。但 "biased/corrected" 命名携带 normative judgment，且论文未解释为何选择这 5 种指标而非 F1/AUROC/MCC。
  - **Director 判断**: 循环论证风险被 R2 的 REBUT 部分化解（机制有独立支撑），但命名和指标选择范围需改进。严重程度从 R1 的 Critical 调整为 **Major-to-Critical**。
  - **修改要求**: (1) 用更中性术语替代 "biased/corrected"（如 "composite/threshold-dependent"）；(2) 明确说明分类时序（empirical observation → mechanism investigation）；(3) 讨论 F1/AUROC/MCC 未被纳入的理由。

### Should-Fix（影响论文质量）

- **W4 [Major, 共识]: 单数据集 (HarmThoughts) 验证对方法论贡献不充分。**
  - 层选择敏感性被宣称为通用发现（Discussion: "likely generalizable to any threshold-based detection study"），但验证仅在 HarmThoughts 上。IAA 未报告。32B 模型 trace 数量不到 8B 一半，harmful category 覆盖可能更少。如果标注者对 CP 位置有 1-2 步分歧，不同层可能对标签噪声有不同敏感度，直接影响层选择结论。
  - **修改要求**: (1) 报告 HarmThoughts harmful category 分布及 CP 位置特征；(2) 讨论 IAA 缺失对层选择结论的具体影响；(3) 如可能，在第二数据集上验证 Contribution 1。

- **W5 [Major, 共识]: 模型多样性不足，"spanning two architectures" 有误导性。**
  - 3/4 模型共享 Qwen 基座。R1 认为对方法论贡献 (Contribution 1) 损害较小（层选择敏感性在 R1-8B Llama 和 Qwen 模型上均存在），但对实证贡献 (Contribution 2: HS advantage) 损害较大。
  - **修改要求**: Introduction/Abstract 使用更精确措辞（如 "four reasoning models based on two architectures, with Qwen being the dominant base (3/4 models)"）。

- **W6 [Minor-to-Major, 分歧→共识 Minor]: 与 Boxo et al. (2025) 差异化不充分。**
  - Boxo 发现 linear probes 依赖 textual evidence，与本文浅层探针利用 text feature leakage 高度相关。R1 补充：R1-32B 深层 residualized selectivity 仅 3.0pp，暗示深层 probe 可能也依赖 textual evidence。
  - **修改要求**: Discussion 增加与 Boxo et al. 的对比讨论，结合 control task selectivity 结果。

### Minor Issues

- **W7 [Minor, 共识]: R1-8B FPR p=0.044 在 12-test HB 下是最弱通过者。** Multi-seed 3/5 HB。论文已透明报告，无需大改，但可加 caveat。

- **W8 [Minor, 共识]: Abstract CP 定义与 Section 3.1 不完全一致。** "irreversibly committed to an unsafe conclusion" vs "safety deliberation permanently ceases"。统一措辞即可。

- **W9 [Minor, R2 提出/R1 降级]: 五步审计协议缺乏形式化。** R2 评 Minor-to-Major，R1 REBUT 至 Minor（其价值在于揭示的问题而非 workflow 自身完备性）。Director 判断 Minor。

- **W10 [Info, R2-Q2]: Table 3 中 1024d 行 BA/FPR 标记为 "--" 未解释。** 需在 caption 或 footnote 中说明。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致（[AGREE]）：

1. **单数据集限制**: 方法论贡献需跨数据集验证。IAA 缺失加剧此问题。（R1-W5, R2-W3）
2. **32B 统计功效不足**: n=19-20 的结论均为 exploratory，无论积极还是消极。（R1-W2, R2-W5）
3. **模型多样性**: 3/4 Qwen 基座限制泛化声明。（R1-W7, R2-W2）
4. **Abstract/Introduction framing gap**: 证据的条件性（encoder-conditional, position-mediated）在 Abstract 中未获充分传达。（R1-W6, R2-W1）
5. **IAA 缺失**: Responsible NLP Checklist 回避了此问题。（R1-Q6, R2-W3 部分）
6. **Overall 3.0 (Findings)**: 两位 Reviewer 独立评出相同分数。

---

## Reviewer Divergence

1. **"Biased vs Corrected" 循环论证严重程度**
   - R1: Critical — post-hoc 分类削弱核心贡献
   - R2: [REBUT] — cosine compression 是独立机制支撑，实质不循环，但命名需改
   - **Director 判断**: R2 的 REBUT 部分有效（机制有独立物理基础），但 R1 关于 post-hoc 性质和指标选择范围的 concern 合理。调整为 **Major-to-Critical**，要求改命名+补充指标选择理由。

2. **Position confound 与 selectivity 的可分离性**
   - R1: Major — selectivity (11.1-16.8pp) 与 position contribution (9-20pp) 数值重叠，独立性未讨论
   - R2: [REBUT] — App F residualized selectivity 已直接回答（3/4 模型 >5pp，R1-32B 3.0pp 与 position-mediated 一致）
   - **Director 判断**: R2 的 REBUT 有效。App F 的 residualized selectivity 确实回答了可分离性问题（R1 可能未充分注意此分析）。R1-32B 的 3.0pp 恰好与 position-mediated 结论一致。此 issue 降为 **info-level commentary** 而非 weakness，但正文可更显式地讨论 selectivity 与 position 的关系。

3. **32B 统计功效问题的严重程度**
   - R1: Critical（占论文 1/3 讨论内容，所有 32B 结论不可靠）
   - R2: Minor（已有 † 标记和 power analysis）
   - **Director 判断**: R1 的论证更有说服力——32B 结果在超参数搜索空间与验证集大小的不匹配下确实不可靠。采纳 **Critical**。

4. **五步审计协议形式化**
   - R2: Minor-to-Major（缺伪代码和验证）
   - R1: [REBUT] Minor（描述性建议，非声称的 formal contribution）
   - **Director 判断**: 采纳 R1 的 Minor 评级。Contribution 列表未声称 formal protocol。

---

## Questions（需作者澄清）

1. 5 种层选择指标的选择依据？为何不包括 F1/AUROC/MCC？
2. K=5 pilot study 的具体细节（数据量、评估 K 值范围、选择依据）？
3. HarmThoughts 的 harmful category 分布及不同 category 的 CP 位置特征差异？
4. Table 3 中 1024d 行 BA/FPR 为 "--" 的原因？
5. R1-32B 在 W=1 时 coverage 仅 25%——这是否暗示 32B 模型的安全承诺过程有本质区别？
6. 层选择敏感性是否特定于安全探针任务，还是可泛化到其他 probing 任务？

---

## Missing References

引用验证结果：61 条 bib entries 均被引用，无 orphan。8 条近期 arXiv 预印本无法在线验证（合理）。

建议核实：
- `geiger2025causal` bib year (2025) vs OpenAlex 记录 (2023)
- `wollschlager2025geometry` 标题与 OpenAlex 记录的 match

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0/5 | 3.5/5 | 3.0/5 |
| Excitement | 3.0/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**核心判断**: 论文识别了层选择作为安全探针研究中被忽视的关键自由度这一重要方法论问题，统计分析框架设计周全，透明度堪称范本。这些构成 solid 的 Findings-level 贡献。但以下问题阻止 Conference-level 评价：

1. **HS 优势是 encoder-conditional 而非 fundamental modality difference** — 对更强 text encoder (BGE-large 1024d) 仅 1/4 模型存活 HB，核心 takeaway 变为 "depends on how good the text encoder is"，作为会议论文的 message 不够有力
2. **32B 结论不可靠** — n=19-20, 2240 configs vs 4-10 per-class validation traces, LOO-CV 跨度 24 层, R1-32B 完全 position-mediated
3. **单数据集 + Qwen 主导** — 方法论贡献的泛化性缺乏验证
4. **"Biased/corrected" 分类的 post-hoc 性质** — 有独立机制支撑（cosine compression），但命名和指标选择范围需改进

**可行修改路径（从 3.0 → 3.5+）**:
- Abstract/Introduction 诚实反映 encoder-conditional 和 32B exploratory 性质
- 在第二数据集（哪怕小规模）上验证层选择敏感性
- 改善 "biased/corrected" 命名和指标选择理由
- 提供 K=5 pilot 细节和 nested CV 讨论

---

## Detailed Comments

### Abstract (p.1)
- "principled layer selection recovers significant HS precision gains in three of four models (+19.2 to +21.9pp, Holm-Bonferroni corrected)" — 此范围包含 R1-32B 的 +15.4pp（position-mediated, residualized gap +1.9pp, p=0.914），读者会误认为 3 个模型都有 robust HS advantage。建议区分 7-8B (robust) 和 32B (exploratory)
- "against a stronger 1024-dimensional text encoder, only 1/4 models survives correction" — 在积极结果之间处于弱势位置，应提前或给予更多 prominence
- CP 定义 "irreversibly committed to an unsafe conclusion" 与 Section 3.1 "safety deliberation permanently ceases" 不一致

### Introduction (Section 1, p.1-2)
- "four reasoning models spanning two architectures (Llama, Qwen) and two scales (7-8B, 32B)" — 3/4 为 Qwen 基座，"spanning two architectures" 传达比实际更广泛的多样性
- Contribution 2 中 R1-32B 的限定（"passes HB but its advantage is position-mediated"）准确但 prominence 不足

### Method (Section 3, p.3-4)
- Section 3.3: "The biased-vs-corrected classification is an empirical observation from metric disagreement, not an a priori design choice" — 承认 post-hoc 但未消除循环论证 concern。补充 cosine compression 的理论解释可强化论证
- Section 3.5: K=5 "pre-selected on R1-8B pilot before evaluating other models" — 需提供 pilot 细节
- 未讨论为何选择这 5 种指标而非 F1/AUROC/MCC

### Experiments (Section 4, p.4-7)
- Table 3: 1024d 行 BA/FPR 为 "--" 未解释
- Section 4.3 "Encoder robustness": BGE-large 1/4 HB 仅在附录详细报告，应在正文给予更多 prominence
- Section 4.4: "Both 32B results are exploratory" — 与 Abstract 的 "three of four" 存在 tension
- Section 4.3 capacity control: PCA-384d 同样仅 1/4 HB（R1 交叉回应中指出），暗示维度优势是 HS advantage 的重要成分

### Discussion (Section 5, p.8)
- "likely generalizable to any threshold-based detection study" — 在单数据集验证下此声明过强
- 与 Boxo et al. (2025) 的对比仅一句话，需扩展：深层 HS probe 是否也存在 textual evidence leakage？R1-32B residualized selectivity 3.0pp 暗示可能

### Limitations (Section 7, p.8)
- 单数据集列为首要限制 ✓
- IAA 缺失的影响讨论可更深入（不同层对标签噪声的敏感度差异）
- 3/4 Qwen 基座应更显式讨论