---
round: 2
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T05:58:40.498948+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Task-Specific Convergence and Per-Example Predictive Multiplicity in Hybrid Recurrent Architectures

**Venue**: EMNLP 2026 via ARR June 2026（截止 2026-06-15）
**Reviewer 编排**: 2 人（R1: 方法严谨性/统计分析; R2: 新颖性/related work/framing）
**轮次**: Round 1（独立审稿 + 交叉回应，1 轮收敛）
**收敛状态**: 关键问题达成广泛共识（14/16 条 AGREE），novelty 严重程度存在可记录分歧

---

## Summary

论文对 hybrid recurrent architectures（GatedDeltaNet, RetNet, HGRN2）在不同 attention ratio（0%-25%）和 scale（340M, 1.3B）下的 cross-architecture performance convergence 进行了系统的 per-example 分析。使用 Wang et al. (2025) 的 controlled model zoo，在 10 个 benchmark 上评估 aggregate convergence，并在 LAMBADA 上进行 5,153 个样本的 per-example decomposition。核心发现：(1) 仅 LAMBADA 展示 cross-architecture convergence（ρ=−1.0，但 Bonferroni 后 p=.100）；(2) convergence 在 1.3B 单调，340M 非单调；(3) aggregate convergence 与 per-example divergence（Jaccard ≤ 0.11）解耦——前者随 attention ratio 递增，后者在 4% attention 时即饱和。

---

## Strengths

1. **实验设计干净**: Controlled model zoo 排除训练数据和超参数差异的混淆，isolate 了 architecture 和 attention ratio 的效果（§3.1）。[R1, R2 共识]
2. **统计报告透明度异常高**: 主动报告 Bonferroni 后不显著（p=.100）、bootstrap degenerate resamples（11.25%）、GDN head-count confound、normalized ES（5-7%）——这种透明度在 NLP 论文中罕见。[R1, R2 共识]
3. **Per-example decomposition 分析视角有价值**: Helped/hurt/unchanged 分类 + Jaccard overlap + normalized effect size 是一套系统的分析工具。[R1, R2 共识]
4. **Appendix robustness checks 充分**: GDN exclusion sensitivity、attention weight analysis、cross-scale Jaccard、permutation independence test、confidence margin analysis（Appendices B-K）。[R1, R2 共识]
5. **Decoupling 发现有新意**: Aggregate convergence 和 per-example divergence 在不同时间尺度运作的发现，如果能在更多 benchmark 上验证，对 practitioners 有重要意义。[R1 肯定; R2 部分肯定]
6. **可复现性高**: 基于公开 model zoo + lm-evaluation-harness 标准评估。[R1, R2 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [critical | statistical_methodology] **统计功效天花板：设计层面不可能达到校正后显著性**

n=5 attention ratios 的精确排列检验最小可达 p=2/120=0.0167；Bonferroni 校正 6 个 confirmatory benchmarks 后 ≥ 0.100。即使 ρ=−1.0（最极端结果），在实验设计层面也不可能达到 α=0.05。论文转向 n=3 架构 bootstrap CI 作为"complementary characterization"（§4.1），但该 CI 仅有 24 种非退化组合（3^3=27 中 3 种退化，占 11.1%），BCa 在边界值退化回退到 percentile CI，n=3 无渐近覆盖保证。p 值不显著时依赖 CI，实质上是 post-hoc 证据标准切换。[R1-N1, R1-N2; R2 [AGREE]]

**N2** [critical | generalizability] **核心发现仅在 1/10 benchmarks 上成立，标题暗示更广适用性**

10 个 benchmark 中仅 LAMBADA 表现出 monotonic convergence（ρ=−1.0），其余 9 个 |ρ| ≤ 0.7，p ≥ .233。Bonferroni 后 LAMBADA 也不显著（p=.100）。标题 "Task-Specific Convergence" 暗示按任务区分的系统性规律，实际是 1 个正例 + 9 个零结果。Decoupling claim（标题级发现）完全建立在 LAMBADA 这一个统计证据不充分的 benchmark 上——如果 convergence 不成立，decoupling 前提也不成立。[R1-N3, R2-N1; 双方交叉 [AGREE]]

**N3** [critical | related_work] **遗漏关键相关工作**

- **Fehlauer, Mahowald & Pimentel (EMNLP 2025)** "Convergence and Divergence of LMs under Different Random Seeds"——同 venue 前一年，直接研究 LM convergence/divergence，发现 larger models reconverge faster。R2 认为 must-cite + novelty 重叠；R1 认为 should-cite（不同 variation source：seed vs architecture），但**双方均同意应引用**。
- **Sellam et al. (ICLR 2022)** MultiBERTs——25 个不同 seed 的 BERT 模型 + per-example robustness 分析。[R1, R2 共识 should-cite]

---

### Reviewer Consensus（AGREE）

以下问题两位 Reviewer 在交叉回应中达成共识：

**W1** [warning | confound] **GDN h3-1 的 16-head confound 应在正文讨论**

GDN h3-1 在 1.3B 使用 16 attention heads（vs 其他 32）。移除 GDN 后 LAMBADA ρ 从 −1.0 降至 −0.7（p=.233），MMLU 方向反转。§4.5 RetNet-HGRN2 pair 部分缓解（σ 下降 54%），但 "monotonic convergence at 1.3B" 叙事不再完全成立。目前仅在 Appendix C 讨论。[R1-W1; R2 [AGREE] 并从 Minor 升级]

**W2** [warning | overclaim] **Scale claim 过度推断**

"Scale as necessary condition" 基于 2 个 data points（340M, 1.3B）。Introduction 用 "We characterize" 提升为 contribution，但 §4.2 自己承认 "a preliminary observation from two data points"。措辞不一致。[R1-W4, R2-W1; 双方 [AGREE]]

**W3** [warning | framing] **标题 scope 过大**

"Hybrid Recurrent Architectures" 暗示普适覆盖，实际仅 3 个架构 + 1 个核心 benchmark。R1 建议 "...Evidence from LAMBADA"；R2 建议 "A Case Study of Three..."。[R2-W3; R1 [AGREE with nuance]]

**W4** [warning | methodology] **Predictive Multiplicity 框架应用不严格**

Jaccard similarity 是 overlap proxy，不是 formal multiplicity metric。至少应计算 ambiguity（Marx et al. 2020: fraction of examples where models disagree）或 discrepancy。标题写入 "Predictive Multiplicity" 但未使用任何 formal metric。[R2-W4; R1 [AGREE]]

**W5** [warning | experimental_validity] **Jaccard "nearly disjoint" 表述过度**

J_obs ≈ 0.10 仅为 J_null ≈ 0.05 的 2 倍；normalized ES 仅 5-7% of theoretical maximum。"Nearly disjoint" 过度简化——更准确是 "low overlap, approximately twice independence baseline"。[R1-W3; R2 [AGREE]]

**W6** [warning | impact] **使用他人 model zoo 的贡献边界**

无新训练、新数据、干预实验。纯分析贡献需更强统计证据或更广实证覆盖来补偿。[R1-W2; R2 [AGREE]]

**W7** [warning | overclaim] **Attention weight analysis 结论过强**

Cosine similarity、entropy、last-5 attention mass 均为 null results。"Per-example effects originate primarily in recurrent layers"（§4.4）是排除法推断，无直接 recurrent layer 分析。应改为 "are not explained by attention layers, consistent with originating in..."。[R1-W5; R2 [AGREE]]

---

### Reviewer Divergence（分歧）

**N4** [R2: critical; R1: should-fix | novelty] **新颖性评估分歧**

- **R2 观点**: 论文本质上是 D'Amour et al. (2022) underspecification 在 hybrid recurrent 设定下的验证，使用他人 model zoo + 标准方法，无方法论增量。Predictive multiplicity 写入标题但未使用 formal metric。构成 critical 问题。
- **R1 反驳**: (1) Variation source 是 architectural backbone 而非 random seed，不是 underspecification 的复现；(2) Dataset Cartography (Swayamdipta et al., 2020, EMNLP) 是纯观察性分析被接收的先例；(3) 但同意 formal multiplicity metric 缺失是 should-fix。
- **Director 判断**: 两种评估均有合理依据。R2 的 critical 评级基于更严格的增量标准；R1 的 should-fix 基于分析论文先例。记录分歧供 Research Director 判断。

---

## Questions

1. 是否考虑 FDR 控制（Benjamini-Hochberg）替代 Bonferroni？BH 校正下 LAMBADA 的 adjusted p ≈ 0.017 可能通过 α=0.05。
2. 对 ARC-Easy（ρ=−0.7）和 MMLU（ρ=−0.7）能否做类似 LAMBADA 的 per-example 分析？即使 convergence 不显著，Jaccard saturation 的测试仍有价值——如果在非 convergence benchmark 上也观察到类似的 per-example overlap 模式，能提供有意义的对照。
3. GDN confidence margin 分析为何使用 h12-1 而非 h3-1（Appendix K）？如果因 16-head confound，请在正文说明。
4. 是否有计划公开分析代码和 per-example 分类数据？

---

## Missing References

| 文献 | 相关性 | 审稿人共识 |
|------|--------|-----------|
| Fehlauer, Mahowald & Pimentel (EMNLP 2025) "Convergence and Divergence of LMs under Different Random Seeds" | 高度相关——同 venue 前一年 | R2: must-cite; R1: should-cite |
| Sellam et al. (ICLR 2022) "The MultiBERTs" | 相关——per-example robustness across seeds | R1, R2: should-cite |
| Bui et al. (IJCNLP-AACL 2025) "Macro and Micro Effects of Random Seeds" | 边缘相关 | R2: can-cite |

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 external_review）。

---

## Visual Layout Check（非评分项）

视觉审查已完成。发现摘要：

- **Critical（1）**: 末页（p.15）约 75% 为空白，仅一张表格占底部——视觉上不专业，应重新排布
- **Warning（4）**:
  - pp.3-5 连续 3 页纯文本（Related Work + Method），无任何 display item（figure/table/equation）——审稿人易失去注意力
  - 主正文 8 页仅 3 个 display items（Figure 1, Figure 2, Table 1），远低于实证论文常见密度（5-8/页）；核心发现以文字呈现而 Appendix 堆积 14 张表
  - Method 部分核心定义（σ reduction, Jaccard, convergence ratio）仅以 inline math 呈现，缺少 numbered display equations
  - Conclusion + Limitations 页纯文本无 visual element
- **Info（6）**: Figure 1 位置良好但 axis label 偏小；Figure 2 受限单栏；Table 1 格式规范；Appendix 表格密度高但可读；References 格式统一无错误

---

## Overall Assessment

**Overall Score: 3.0（Findings）**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0 | 3.0 | 3.0 |
| Excitement | 2.5 | 2.5 | 2.5 |
| Overall | 3.0 | 2.5 | 3.0 |
| Confidence | 4/5 | 4/5 | 高 |
| Reproducibility | 4/5 | 4/5 | 4/5 |

**综合评价**:

论文提出了一个有价值的研究问题（architectural predictive multiplicity），分析方法系统且统计报告透明度异常高。Decoupling 发现——aggregate convergence 和 per-example divergence 的时间尺度分离——在概念上是论文最有趣的贡献。

但三个核心问题严重限制了当前版本的 impact：

1. **统计功效先天不足**（n=5 + Bonferroni = 设计层面不可能显著），且 CI 替代证据基于 n=3 bootstrap，形成两端不牢靠的证据链
2. **Single-benchmark scope**: 标题级 claim 建立在单一 benchmark（LAMBADA）的非显著统计结果上
3. **GDN confound**: 移除有混淆变量的架构后核心结论显著弱化（ρ: −1.0 → −0.7）

论文更适合 **Findings track**。统计报告的诚实和分析的系统性值得肯定，但 scope 过窄和统计局限性限制了 conference-level impact。

**Rebuttal 提升路径**（如全部解决，评分可望提升至 3.5 Borderline Conference）：
- (a) 扩展 per-example 分析到 ARC-Easy/MMLU 以测试 decoupling 泛化性
- (b) 引入 formal multiplicity metric（ambiguity/discrepancy）
- (c) 采用 BH 替代 Bonferroni
- (d) 补引 Fehlauer et al. (EMNLP 2025) 并明确 differentiate
- (e) 标题加 scope qualifier

---

## Issue Tracker 状态

已同步更新 `review_issues.yaml`（15 个 issue）：
- Critical: 3（stat power, single-benchmark scope, missing refs）
- Major: 1（novelty — Reviewer 分歧）
- Warning: 11（GDN confound, scale overclaim, title scope, multiplicity formal, Jaccard wording, contribution boundary, attention overreach, practical impact, pre-registration, entropy, attn-overreach）
- 上轮已修复: 2 个 issue 本轮未被提及（W-preregistration, W-entropy），标记为可能已修复
- 新增: 3 个 issue（W-attn-overreach, W-contribution-boundary, W-multiplicity-formal）