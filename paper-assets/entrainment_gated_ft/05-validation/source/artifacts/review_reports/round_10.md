---
round: 10
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-22T07:54:03.756832+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 10 审稿报告

**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
**Venue**: EMNLP 2026 (via ARR, Long Paper)
**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 完整性 + 写作质量）
**轮次**: Round 1（fresh 模式，无历史记忆）

---

## Summary

本文首次系统地分析了 hybrid linear recurrent 架构之间的 per-example predictive multiplicity。利用 Wang et al. (2025) 的 controlled model zoo（3 架构 × 5 attention ratio × 2 scale），在 4 个 benchmark 上做 per-example decomposition，发现：(1) cross-architecture 的 per-example overlap 极低（Jaccard ≤ 0.10），multiplicity 随 task type 变化（α = 0.14–0.30）且与 attention dose 无关；(2) 仅 LAMBADA 展示 aggregate convergence（Bonferroni-adjusted p = .100），且 aggregate convergence 与 per-example divergence 在不同 timescale 上运作（decoupling）。论文方法论透明度高，统计处理严谨，sensitivity analysis 全面。

---

## Strengths

**S1. 研究问题有实践价值。** 将 predictive multiplicity 从 seed-driven disagreement 扩展到 architectural variation 是自然但未被充分探索的方向。"aggregate 等价 ≠ per-example 等价" 对选择 hybrid recurrent backbone 的从业者有直接警示意义。[R1, R2 共识]

**S2. 方法论透明度极高。** 所有统计限制均被明确声明：bootstrap CI 在 n=3 上是 heuristic（§3.5）、permutation test 最小 p-value 为 0.017（§3.5）、Bonferroni p=.100 不达显著性（§4.1, Abstract）、GDN h3-1 的 16-head confound（Appendix E）、single training run 限制（Limitations）。这种诚实程度在投稿论文中较为少见。[R1 主导, R2 agree]

**S3. Sensitivity analysis 覆盖全面。** GDN exclusion、regression to the mean、cross-scale comparison、subsample sensitivity of α、normalized Jaccard effect size、Jaccard permutation test 均系统性地排除替代解释。Appendix 内容质量高，不是 padding。[R1, R2 共识]

**S4. 实验设计的 controlled nature。** 共享 training data、tokenizer、hyperparameters 的 model zoo 有效隔离 architecture effect。Binary decomposition 用 continuous confidence margin analysis 补充验证（Cohen's d = 0.73–0.92）。[R1, R2 共识]

**S5. 统计方法选择合理。** Permutation test、BCa bootstrap（含 percentile fallback）、Bonferroni correction、Mann-Whitney U、Kruskal-Wallis 的组合覆盖了各项分析需求。[R1, R2 共识]

**S6. 主文自包含。** 核心论点不依赖 appendix 即可理解。Appendix A-R 为补充性的 sensitivity 和 extended analysis。[R2 主导, R1 agree]

---

## Weaknesses

### Critical

**W1. Convergence claim 统计证据不足，但承担过多叙事权重。** [R1-W1 Critical, R2-N1 Critical, 交叉共识]
- LAMBADA 的 convergence（ρ = −1.0）Bonferroni-adjusted p = .100，不达 0.05 显著性。对 10 个 benchmark 校正则 p = .170。
- 去掉 GDN 后 ρ 降至 −0.7（p = .233）；MMLU 甚至翻转（ρ: −0.7 → +0.6）。
- Convergence 在 340M 上完全缺失（ρ = −0.50, p = .45）。
- 综合：convergence 仅在 "1.3B + GDN included + LAMBADA" 条件下成立，但论文叙事 ~40% 围绕此展开。
- Contribution 2（decoupling）依赖 convergence 成立——如果 convergence 本身 uncertain，decoupling 失去一个支柱。
- **注意**：R1 在交叉中精确区分了 convergence（GDN-dependent）与 decoupling（GDN-independent）——去掉 GDN 后 RetNet-HGRN2 pair 仍保留 decoupling pattern（σ ≤ 0.008, Jaccard 饱和在 0.086–0.108）。因此 decoupling 不应被标记为 "GDN-driven"，但其叙事基础（convergence）确实脆弱。

**W2. Single training run 根本性地限制了 architecture vs. seed 的区分。** [R1-W2 Critical, R2-W1 Major → R2 交叉升级为 Critical]
- 每个 configuration 对应单次训练运行。Within-architecture Jaccard (~0.33) vs. cross-architecture Jaccard (~0.10) 的 3× gap 被用作 architecture-dominance proxy，但 R1 指出两个比较维度不同——within-arch 比较的是不同 attention ratio，cross-arch 比较的是不同架构。
- 没有 multi-seed baseline，无法知道 seed-driven Jaccard 的量级。McCoy et al. (2020) 报告 ~7% MNLI disagreement，但 metric 不同无法直接比较。
- Contribution 1 的 "architectural variation produces structured multiplicity" 可能需要降级为 "some combination of architecture and seed produces multiplicity"。
- Limitations 中 McCoy calibration caveat + within-arch Jaccard proxy caveat 已加，但根本问题不可修复。

### Major

**W3. Bootstrap CI 在 n=3 上信息量极低但被频繁引用。** [R1-W3 Major, R2 agree]
- n=3 bootstrap 最多 27 unique resamples，11.25% degenerate。BCa 在 ρ = −1.0 boundary degenerate。
- CI 在 Abstract、Introduction、§4.1、§4.3、Figure 2 caption 被大量使用。"Heuristic" caveat 存在于 §3.5 但不在每次引用时重复。读者可能过度信赖这些 intervals。

**W4. Spearman ρ 在 n=5 上解释力有限。** [R1-W4 Major, R2 agree]
- Permutation test 的 p-value 分辨率为 1/120 ≈ 0.0083。能达到 p < .05 的 ρ 值只有 ρ = ±1.0（p = .017）。
- 对 "strong but not perfect" monotonic trends 完全无功效。ρ = −1.0 vs. ρ = −0.7 差异在 n=5 上可能仅为 1-2 个 rank swap（noise）。

**W5. LAMBADA 唯一 converge 的 benchmark 讨论不足。** [R1-W5 Major, R2 agree]
- Mechanistic reasoning（retrieval task, attention 提供 direct token-level access）像 post-hoc explanation。
- ARC-Easy（Mixed, ρ = −0.7, p = .233）也有中等负相关但不 converge——差异可能是 noise 而非 task-type driven。

**W6. Binary decomposition 对 multiple-choice 的 bias 方向未讨论。** [R1-W6 Major, R2 agree]
- 在 4-choice tasks 上，不同 wrong answers 都 counted as "hurt" 可能高估 Jaccard。
- R2 在交叉中指出：bias 方向实际加强 multiplicity claim（真实 Jaccard 更低），但论文应显式讨论。
- Confidence margin analysis（Appendix N）部分补充但主文 narrative 完全基于 binary counts。

**W7. 新颖性有限——纯描述性贡献，无方法创新或机制解释。** [R2-N2 Critical → R1 降级为 Major, 分歧记录]
- 所有工具均来自已有工作（metrics: Marx et al. 2020, models: Wang et al. 2025, benchmarks: lm-eval-harness）。
- Appendix F 的 attention weight analysis 显示 helped/hurt 间 entropy 差异 negligible（ΔH ≤ 0.002），论文承认 "descriptive, not causal"。
- R1 认为 descriptive empirical contribution 在 Findings track 可接受（类比 McCoy 2020, D'Amour 2022）。R2 认为缺乏 mechanism explanation 是 Critical。
- **Director 判断**：作为 Findings track 论文，descriptive contribution 可接受，但 excitement 因此受限。Severity 定为 Major。

### Minor / Warning

**W8. 因果语言偶有越界。** [R1-W8 Minor, R2 agree]
- "attention disrupts marginally correct predictions"（§4.2）、"attention compensating for differences"（§4.1）、"architectural differences produce"（§1）、"attention-driven"（§4.3）应替换为 associative language。
- §4.2 的 rescue/disruption 已加 descriptive-label clarification，但其他位置仍有因果语言。

**W9. 可重复性细节缺失。** [R1-W7 Minor, R2 agree]
- lm-eval-harness 版本/commit 未报告；decoding strategy 未明确；主文 bootstrap seed 未报告；无 code/data availability statement。

**W10. Scale 分析不足以支撑 practical protocol 的外推。** [R2-W2 Major → R1 部分同意]
- 仅 340M 和 1.3B 两个 scale。R1 指出 per-example multiplicity pattern 本身 scale-robust（Jaccard 0.08–0.10 at both scales），但 convergence direction 需 scale 限定。

**W11. Task taxonomy 事前性质弱。** [R2-W4 Warning → R1 降级为 Minor]
- Appendix A 声称 taxonomy "fixed prior to analysis" 但非 formal pre-registration。核心结果不依赖 taxonomy 分类。

---

## Reviewer Consensus [AGREE]

1. **Overall 3.0 (Findings)**：两位 Reviewer 独立给出相同评分，交叉后确认。
2. **Contribution 1（per-example multiplicity）是论文最强部分**：Jaccard 分析 + permutation test + cross-benchmark variation 形成完整证据链，novel 且统计稳固。
3. **Convergence claim 统计基础不足**：Bonferroni p = .100，GDN-dependent，single benchmark，absent at 340M。叙事权重与证据强度不匹配。
4. **Single training run 是最根本的实验限制**：无法 disentangle architecture vs. seed effects。within-arch Jaccard 作为 proxy 的维度不匹配。
5. **Bootstrap CI (n=3) 引用过频**：信息量极低但给读者 well-characterized 的印象。
6. **因果语言偶有越界**：应全面替换为 associative language。
7. **Findings track 定位合理**：descriptive empirical contribution + 有实践价值 + 统计严谨 → Findings 可接受。

---

## Reviewer Divergence [REBUT]

1. **新颖性 severity**：R2 标为 Critical（无方法创新，纯描述性），R1 降为 Major（descriptive contribution 在 Findings track 可接受，类比 McCoy 2020, D'Amour 2022）。Director 采纳 Major。
2. **GDN-decoupling 关系**：R2 认为 decoupling 是 "GDN-driven"，R1 REBUT——§4.4 明确表明 decoupling 在去掉 GDN 后仍成立（RetNet-HGRN2 pair: σ ≤ 0.008, J 饱和在 0.086–0.108）。R2 在交叉中未反驳此 REBUT。Director 采纳 R1 的区分：convergence 是 GDN-dependent，decoupling 是 GDN-independent。
3. **"Predictive multiplicity" 术语**：R2 认为被 "stretched"（不在 Rashomon set 内），R1 REBUT（α metric 的使用技术上合法，三个架构在 aggregate 上 near-equivalent）。分歧未完全解决。Director 判断：术语使用可接受，但建议在 §2 或 §3 加一句澄清与 formal Rashomon set 的关系。

---

## Questions

1. 如果对 LAMBADA convergence 做 one-sided permutation test（prior: attention 应 reduce variance），p-value 和 Bonferroni 校正后结果？[R1-Q1]
2. 是否计算过 choice-level Jaccard（看具体选项而非仅对/错）？[R1-Q3]
3. 是否尝试过 confidence-weighted ensemble 或 learned selector？"accessing complementary knowledge requires more sophisticated methods" 的 claim 仅有 majority vote 一个 baseline。[R1-Q4]
4. GDN h3-1 使用 16 heads vs. 其他 32 heads，这一不对称是否足以解释 LAMBADA 上 GDN 的异常 convergence 行为？[R2-Q1]
5. Appendix F 无法找到 helped/hurt 的 attention weight discriminative pattern——是否尝试过分析 recurrent layer 的 hidden state / gate activation patterns？[R2-Q4]
6. Wang et al. (2025) model zoo 是否公开可用？论文缺少 code/data availability statement。[R1-Q6]

---

## Missing References

1. **Fort et al. (2019), "Deep Ensembles: A Loss Landscape Perspective"** — cross-architecture disagreement 的理论视角，与 majority vote / oracle accuracy 讨论相关。[R1 agree, R2 suggest]
2. **Niven and Kao (2019), "Probing Neural Network Comprehension of Natural Language Arguments"** — 与 benchmark artifacts 和 helped/hurt decomposition 相关。[R2 suggest]
3. **Jiang et al. (2024), "Characterizing model multiplicity in foundation models"**（如存在）— predictive multiplicity 在 foundation models 上的近期扩展。[R1 suggest]
4. 确认 Gorbett and Jana (2026) 和 Haghighat et al. (2026) 的 preprint/published 状态——如果是 concurrent work 应标注。[R1 suggest]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置中 external_review 未配置）。

---

## Visual Layout Check（非评分项）

状态：**已完成**（2026-05-22 07:34–07:37，耗时约 3 分钟）

**Findings：**

- **[Warning] Pages 3-5**：连续 3 页纯文本（Related Work + Method + Statistical Methods），无 figure/table/equation 穿插。建议 Method 段增加实验设置概览图或将关键公式提升为 display math 打断文本墙。
- **[Info] Pages 1-8**：主正文仅 4 个 display items（2 figure + 2 table），对于实证分析论文偏少。大量结果表被推到 appendix，主正文视觉说服力减弱。
- **[Info] Page 6**：Figure 2 的 scatter plot 较小，数据点标签和轴标签字号偏小（接近 6-7pt），打印或低分辨率屏幕上可能难以辨认。
- **[Info] Page 2**：Figure 1 caption 非常长（约 6 行），建议精简为 3-4 行。
- **[Info] Pages 6-7**：Table 1 和 Table 2 使用 booktabs 风格，最优值加粗标注，小数位数一致——表格排版质量良好。
- **[Info] Page 19**：Appendix 末页内容仅占 ~55%，底部 ~45% 空白。

无 critical 排版问题。

---

## Overall Assessment

**Overall: 3.0 — Findings**

**Confidence: 4/5**

### 评分综合

| 维度 | R1 | R2 | 综合 | 理由 |
|------|-----|-----|------|------|
| Soundness | 3.0 | 3.5 | 3.0 | 方法选择合理、limitation 透明，但 n=3 + n=5 + single seed 的根本功效限制使 convergence claim 统计证据不足。Per-example multiplicity 部分 sound。 |
| Excitement | 3.0 | 2.5 | 2.5 | 问题重要且观察新颖，但 actionability 有限（MV 失败无替代方案），最有趣的发现（decoupling）统计证据不足，且贡献纯描述性缺乏机制解释。 |
| Reproducibility | 3.5 | 4.0 | 3.5 | Model zoo 来自公开资源，方法描述详细；但缺少 lm-eval-harness 版本、decoding 参数、code availability statement。 |

### 核心判断

**适合 Findings 的理由：**
- Per-example multiplicity 的发现（Contribution 1）新颖且有稳固的统计支撑——Jaccard 分析、permutation test、normalized ES、cross-benchmark/cross-scale variation 形成完整证据链。
- 研究问题有实践价值，方法论透明度高，sensitivity analysis 全面。
- 对 EMNLP 社区的贡献在于揭示了一个被 aggregate evaluation 掩盖的现象。

**不足以支撑 Main Conference（3.5+）的原因：**
- Contribution 2（convergence-decoupling）建立在 p = .100 的 convergence claim 上，仅在 LAMBADA + GDN included 的条件下成立，absent at 340M。叙事权重与证据强度不匹配。
- Single training run 无法 disentangle architecture vs. seed effects，限制了 Contribution 1 的 claim 精度。
- 无方法创新或机制解释，贡献纯描述性。
- Excitement 受限：majority vote 失败但未提出替代方案；mechanistic analysis（Appendix F）未找到 discriminative pattern。

### 提升至 3.5 的路径

1. **重新平衡叙事**：将 convergence 从 Contribution 级别降为 supplementary observation，增加 per-example multiplicity 本身的叙事权重。将 C2 重新表述为 "per-example multiplicity persists regardless of aggregate trend"（不需要 convergence 成立）。
2. **增加 mechanism depth**：在 recurrent layer hidden state 层面分析 helped/hurt 差异（gate activation patterns, state norm），超越 Appendix F 的 negative result。
3. **添加 seed baseline**：至少在一个架构上跑 2-3 个 seeds，bound seed-driven Jaccard。
4. **添加 reproducibility details**：lm-eval-harness 版本、decoding parameters、code/data availability。

---

## Detailed Comments

### Abstract
- 信息密度适中，关键统计量均出现。"Exploratory evidence" 和 "Bonferroni-adjusted p = .100" 措辞准确。
- BCa 95% CI 在 Abstract 中出现有误导风险——n=3 bootstrap CI 信息量极低，建议移除或替换为 "excludes zero under heuristic bootstrap"。
- "single training runs per configuration" caveat 出现在 Abstract 中，值得肯定。

### §1 Introduction
- 结构清晰，问题动机充分。开篇即给出具体数字（"at most 10%, far below 78-92% theoretical maximum"）有力。
- Contribution 1 包含 "though we cannot fully disentangle" caveat——好。
- Contribution 2 的 "rather than uniform rescue" 排他性语言偏强，证据支持 "consistent with" 但不足以 "rather than"。
- ~40% 叙事围绕 convergence 展开，与 exploratory 定性不匹配。

### §2 Related Work
- 覆盖全面：hybrid architectures、linear recurrent models、underspecification/multiplicity 三个方向。
- 缺少 Fort et al. (2019) Deep Ensembles。Arora et al. (2024b, Based) 已在 §4.1 引用但 §2 中无显式讨论。
- 与 Swayamdipta et al. (2020) 的 differentiation（training dynamics vs. deployment-time decomposition）清晰。

### §3 Method
- §3.3 Convergence Metrics：定义清晰，但缺 power analysis——应指出 n=5 permutation test 仅 ρ=±1.0 能达 p<.05。
- §3.4 Per-Example Decomposition：binary decomposition + Jaccard 组合合理，但缺少 bias 方向讨论（multiple-choice 上可能高估 Jaccard）。
- §3.5 Statistical Methods：方法选择均合理，heuristic caveat 到位。Bootstrap 的 27 unique resamples 含义应更明确。

### §4 Experiments
- §4.1：Table 1 信息密度高，格式清晰。"Only benchmark exhibiting monotonic convergence" 在 n=5 ρ=−1.0 vs −0.7 分辨率下需谨慎。
- §4.2：**论文最强部分。** Jaccard 分析 + permutation test + normalized ES + confidence margin mechanism 形成令人信服的证据链。
- §4.3：描述性观察有说服力（σ 单调下降 vs Jaccard 早期饱和），但依赖 convergence 的统计成立。
- §4.4：GDN exclusion 分析是负责任的。"convergence dependent on GDN; decoupling is not" 区分清楚。

### §5 Conclusion
- Majority vote 负面结果 + oracle gap（+7-14 pp）的讨论有趣。
- Practical protocol 缺乏 scale 泛化基础（仅 2 个 scale 点）。

### Limitations
- 全面且诚实。Coverage、methodological constraints、pre-training only 三段覆盖。
- McCoy calibration caveat 和 within-arch Jaccard proxy caveat 已加。
- 内容实质，3 段结构符合 EMNLP 规则。

### Appendix
- 质量高、不冗余。Subsample sensitivity（App R）直接回答 "COPA 排除原因"。Transformer entrainment comparison（App L）提供补充视角。

### 格式合规
- `\usepackage[review]{acl}` ✓
- 正文 8 页 ✓
- `\author{Anonymous}` ✓，无自引泄露
- Limitations + Ethics 不计入页数 ✓
- 参考文献无限制 ✓