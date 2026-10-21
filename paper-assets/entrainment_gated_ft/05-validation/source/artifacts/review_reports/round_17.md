---
round: 17
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-23T14:49:11.127992+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures

**Venue**: EMNLP 2026 (via ACL Rolling Review) — Long Paper
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1 方法/统计, R2 新颖性/写作）
**圆桌轮次**: 1 轮初审 + 1 轮交叉分享，关键问题已收敛

---

## Summary

本文利用 Wang et al. (2025) 的 controlled model zoo（3 种 hybrid linear recurrent architectures × 5 种 attention ratios × 2 种 scale），系统分析了增加 attention 对 per-example 预测一致性的影响。核心发现：(1) 不同架构在 aggregate accuracy 接近时，per-example helped/hurt set 重叠极低（Jaccard ≈ 0.10，约为 independence baseline 的 2 倍），在 5 架构 40 个 architecture-benchmark 组合上均显著（all p < .01）；(2) multiplicity magnitude 取决于 task type（α = 0.14–0.30）而非 attention dose（variation < 0.03）；(3) 仅 LAMBADA 显示 aggregate convergence 但未达统计显著性（Bonferroni-adjusted p = .170）。

---

## Strengths

**S1. 实验设计严谨（R1/R2 共识）**：利用 controlled model zoo 隔离 architecture 和 attention ratio 为自变量，控制 training data、tokenizer、hyperparameters，是该类分析的 gold standard 范式。

**S2. Per-example 低重叠发现稳健（R1/R2 共识）**：Jaccard ≤ 0.14 在所有 4 个 benchmark、5 个架构、所有 pairwise comparisons 上一致成立（all p < .01），通过 continuous-threshold analysis（Appendix O）和 5-architecture validation（Appendix X）得到确认。这一核心发现不依赖于有争议的 convergence claim。

**S3. 统计方法论全面（R1/R2 共识）**：exact permutation tests、bootstrap 95% CIs、Bonferroni correction、20+ 个 Appendix sections 的 robustness checks。局限性的诚实披露值得肯定。

**S4. 主题时效性强（R2）**：hybrid architectures（Jamba, Griffin, RWKV 等）正快速进入生产环境，per-example multiplicity 是一个被忽视但重要的部署维度。

**S5. 可复现性高（R1/R2 共识）**：使用公开 model zoo，承诺代码发布，实验细节充分。Reproducibility 4/5。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical] Convergence claim 统计证据结构性不足 [R1-N1 + R2 AGREE]**
- Spearman 在 n=5 时最小可达 p = 0.017（双侧），Bonferroni 10-benchmark 校正后 adjusted p = 0.170——**即使完美单调关系也无法达到常规显著性**。这是检验结构的固有限制，非数据不足。
- 尽管 §4.2 标注了 "suggestive but underpowered"，Abstract/Conclusion 仍间歇性使用 "monotonic convergence"、"aggregate metrics converge on LAMBADA" 等确认性措辞。全文措辞不一致。
- **影响**：论文的 decoupling claim（aggregate convergence vs per-example divergence 在不同 timescale 运作）悬空于不可检验的 convergence 之上。
- **修复建议**：(a) 全文将 convergence 统一降级为 descriptive/exploratory observation；(b) Abstract/Conclusion 加显式 power limitation caveat；(c) 考虑 mixed-effects regression（n=15 data points: 5 ratios × 3 architectures）替代 rank correlation。

**MF2. [critical] GDN h3-1 的 16-head confound 削弱核心发现 [R1-N2 + R2 partial AGREE]**
- GDN h3-1 使用 16 个 attention heads，其他配置均 32 个。移除 GDN 后 LAMBADA ρ 从 -1.0 降至 -0.7（Table 3, Appendix E），MMLU ρ 从 -0.7 翻转为 +0.6。
- LAMBADA 是唯一支撑 convergence claim 的 benchmark，对 GDN 的依赖是实质性威胁。
- R2 补充：此 confound **主要威胁 convergence claim（§4.2），不威胁 per-example divergence claim（§4.1）**——RetNet-HGRN2 pair 的 Jaccard 仍然很低（J ≈ 0.10）。
- **修复建议**：(a) 主文 §4.2 或 §4.3 显著讨论 GDN confound 及影响；(b) 明确 LAMBADA convergence 是 confound-dependent 的。

**MF3. [critical] 单次训练 run 无法区分 seed 效应与架构效应 [R1-N3 + R2 AGREE]**
- 所有结果来自每个配置的单次 run。Appendix W 的 Pythia 70M seed calibration 中 within-seed J = 0.312 vs cross-architecture J = 0.354，差距仅 0.042。
- **三重 mismatch**：Pythia 是 Transformer（非 hybrid）、70M（非 340M+）、accuracy range 不同。该 calibration 的 generalizability 存疑。
- R2 补充：如果 seed variation 已能产生 J ≈ 0.31 的 divergence，论文观测的 cross-architecture J ≈ 0.10 可能反映 seed+architecture 复合效应。
- **修复建议**：(a) Limitations 充分讨论 seed confounding（当前措辞 "cannot fully exclude" 低估严重性）；(b) 理想情况下对至少一个 hybrid 配置做多 seed 验证；(c) 弱化因果性措辞。

**MF4. [critical, R2 / warning, R1] Routing 分析作为方法贡献严重不足 [R2-N2 + R1-W1, 交叉双方 AGREE]**
- 仅 LAMBADA 有效（56.2% vs 50.9% MV），HellaSwag/PIQA "no benefit"，ARC-Easy +1.1pp——1/4 成功率。
- 无 ensemble baseline 对比（如 confidence-weighted majority vote）。
- 10-fold CV 未报告 fold-level SD；若 SD > 3pp 则 5.3pp 增益可能不显著。
- Conclusion 将 routing 列为 "practitioner implications"，证据不支持。
- R1 补充：routing 非论文 main contribution，但当前 framing 使其承担了过多 contribution weight。
- **严重度分歧**：R2 标为 critical（作为独立方法贡献评估），R1 标为 warning（routing 非 main contribution）。圆桌判定：**should-fix 级别**——routing 不是论文的 main claim，但当前的 over-positioning 拉低了整体评估。
- **修复建议**：(a) Conclusion 中将 routing 从 practitioner implication 降级为 future direction 或 preliminary exploration；(b) 报告 SD across CV splits；(c) 或大幅扩展：加入 ensemble baseline + learned routing + 跨 benchmark 评估。

### Should-Fix（影响评分但不一票否决）

**SF1. [warning] Task type vs evaluation format confound [R1-W2 + R2 AGREE]**
- LAMBADA 是唯一 free-form generation benchmark，其余均为 multiple-choice。LAMBADA 也恰好是唯一显示最高 multiplicity（α=0.30）和 convergence 的 benchmark。
- Multiple-choice format 机械性约束答案空间，可能降低 per-example divergence 上界——这是一个 evaluation format confound，§3.2 的 task taxonomy 未考虑。
- **修复建议**：Discussion 或 Limitations 中讨论 evaluation format 作为 alternative explanation。

**SF2. [warning] Introduction/Abstract framing 与结果强度不匹配 [R2-W3 + R1 AGREE]**
- Abstract "depends on task type rather than attention dose"——"rather than" 措辞过于绝对，本质上是 null result on attention dose（可能因 power 不足），不等于 evidence for absence。
- 36% oracle complementarity 提取率被放在 Abstract 显要位置，给人过度积极印象。
- **修复建议**：将 "rather than" 改为 "more than" 或 "primarily…rather than"；routing 结果增加 baseline comparison context。

**SF3. [warning] BCa bootstrap 在 n=3 上不可靠 [R1-W3 + R2 AGREE]**
- BCa acceleration parameter 基于仅 3 个 jackknife 值，CI 覆盖率远低于 nominal 95%。Appendix D.1 已改用 percentile CI，但主文仍引用 bootstrap CI。
- **修复建议**：全面改用 percentile bootstrap 并标注 heuristic indicator，或在 §3.5 显式说明 n=3 coverage 问题。

**SF4. [warning] 5 架构扩展验证仅限 340M + Scale 局限性未在 Conclusion 限定 [R1-W5 + R2-W4, 双方 AGREE]**
- GLA 和 DeltaNet 仅 340M 可用（model zoo 限制）。Conclusion 的 practitioner implications 使用不加限定的一般性语言。
- **修复建议**：§4.3 引用 5-arch 结果时加 "at 340M"；Conclusion 添加 scale 限定词。

**SF5. [warning] Confirmatory/exploratory benchmark 分类缺乏预注册 [R1-W4 + R2 partial AGREE]**
- "informal pre-analysis plan" 无 external timestamp。主文已用 all-10 correction（更保守），但 Appendix A 报告 6-benchmark correction 给选择性引用空间。
- R2 指出两种 correction 在 LAMBADA 上 adjusted p 相同（p_min = 0.017 不变），降低严重度。
- **修复建议**：Appendix A 明确 all-10 为唯一有效 correction。

### Minor（不影响接收）

- **m1**: Figure 1 排版信息量大但效果好（R2 S4 肯定）。Pages 3-5 连续 3 页纯文本无 display item，节奏前松后紧（视觉审查 warning）。
- **m2**: Page 8 三个 figure 挤在同一页，Figure 4/5 尺寸偏小（视觉审查 warning）。
- **m3**: Table 1 列名缩写缺 inline 解释（R1-M2）。
- **m4**: §4.1 "saturates" 暗示 ceiling，实际接近 floor（independence baseline ~0.05），建议改为 "remains at a low plateau"（R1-M3）。
- **m5**: Abstract 接近 200 word 上限，inline 统计量增加认知负荷，建议精简（R1-M6 + R2-M4）。
- **m6**: "model zoo" 术语来自 Wang et al. 原文（Zoology），R1 判断无需修改。

---

## Reviewer Consensus

以下问题两位 Reviewer 在交叉分享后达成一致：

1. **[AGREE] Convergence claim 必须降级为 exploratory**：n=5 Spearman 结构性限制 + GDN confound + 全文措辞不一致 → 不能作为已确立发现呈现
2. **[AGREE] Routing 需降级或大幅加强**：1/4 benchmark 有效，无 variance 报告，无 ensemble baseline
3. **[AGREE] Seed confound 是根本性威胁**：Pythia calibration 三重 mismatch，论文措辞低估严重性
4. **[AGREE] 统计报告需全文统一为 descriptive/suggestive 措辞**
5. **[AGREE] Scale 限制应在 Conclusion 明确限定**
6. **[AGREE] BCa bootstrap n=3 应标注 heuristic**
7. **[AGREE] Per-example 低重叠（Jaccard ≤ 0.14）是稳健且有价值的发现**

---

## Reviewer Divergence

**核心分歧：概念新颖性的定级**

- **R2 立场（N1 critical）**：论文的核心发现本质上是 ecological fallacy（Robinson 1950）在 architecture comparison 场景下的已知实例化。方法论（Jaccard + permutation test）无创新。贡献仅为 domain transfer，概念增量有限。EMNLP main conference 要求更强 novelty。
- **R1 立场（REBUT，should-fix 级别）**：ecological fallacy 是通用框架，不预测具体的 Jaccard saturation pattern 或 task-dependent spectrum。论文定位为 empirical contribution，ACL/EMNLP 接收高质量 empirical characterization（类比 McCoy et al. 2020）。但同意应更明确定位为 empirical contribution。
- **部分收敛**：双方均同意论文应明确定位为 empirical contribution 而非发现新现象。分歧在于这是否构成 Must-Fix（影响 Conference vs Findings 定位）。

**评分差异**：

| 维度 | R1 | R2 | 差异原因 |
|------|-----|-----|----------|
| Soundness | 2.5 | 3.5 | R1 对 n=5 power + GDN confound 更严格；R2 区分 convergence 和 divergence 两个 claims |
| Excitement | 3.0 | 2.5 | R1 更看重 practical relevance；R2 更看重 conceptual novelty |
| Overall | 3.0 | 3.5 | R1 认为 statistical limitations fundamental；R2 认为 novelty 不足但 soundness adequate for Findings |

---

## Questions

1. 如果 GDN h3-1 的 16-head confound 可通过重训 32-head 版本解决，LAMBADA convergence 是否仍然成立？（R1-Q1）
2. Jaccard ≈ 0.10 在实际部署中的风险量化？能否提供具体部署场景？（R1-Q2）
3. 是否考虑过 mixed-effects model 替代 Spearman 以提高统计效力？（R1-Q3, R2 交叉支持）
4. Appendix W 的 Pythia 70M seed calibration 在 340M hybrid 上预期差距会增大还是缩小？（R1-Q4）
5. Section F attention weight analysis 得出 null result 后，per-example divergence 的 root cause 是什么？（R2-Q1）
6. 为何不使用 continuous Jaccard（而非 binarized）作为主文的 primary metric？（R2-Q4）

---

## Missing References

**R2 建议（R1 部分 REBUT，需核实时效性）**：
1. Ye et al. (2026), "A Provable Expressiveness Hierarchy in Hybrid Linear-Full Attention"（arXiv: 2602.01763）——为 hybrid architecture expressiveness gap 提供理论基础，可能解释 per-example divergence
2. arXiv: 2601.09071 (Jan 2026), "Resolving Predictive Multiplicity for the Rashomon Set"——multiplicity resolution 方法，与 routing 相关
3. arXiv: 2602.09520, "Rashomon Sets and Model Multiplicity in Federated Learning"

**R1 建议**：
4. Zamba / Jamba-1.5 等生产级 hybrid 架构——加强 motivation
5. Diversity-aware ensemble 方法文献——与 routing/ensemble 应用相关

**注**：R1 指出 R2 所列 2026 arXiv 文献需核实是否在 ARR submission deadline 前发布。论文已引用的 predictive multiplicity 核心文献（Marx et al. 2020, Watson-Daniels et al. 2023, D'Amour et al. 2022, Black et al. 2022）覆盖较为完整。

---

## External Review (Stanford Agentic Reviewer)

未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

**状态**：✅ 已完成

**Findings**（0 critical, 2 warning, 7 info）：

- ⚠️ **Pages 3-5**：连续 3 页纯文本（Related Work → Method §3.1-3.5），无 display item 穿插。Method section 约 2.5 页缺少实验设置概览图或 model zoo 汇总表，审稿人容易失去注意力。
- ⚠️ **Page 8**：3 个 figure（Figure 3 heatmap + Figure 4 线图 + Figure 5 柱状图）挤在同一页，加上正文和 Limitations section，版面拥挤。Figure 4/5 尺寸偏小。
- ℹ️ Figure 1 双面板效果好，Caption 自包含。Table 1/2 booktabs 风格规范。References 格式统一，无未解析引用。Display items 集中在后 1/3（pages 2, 6, 7, 8 有全部 7 个，pages 1, 3, 4, 5 为零），节奏前松后紧。

---

## Overall Assessment

**综合评分：3.0 — Findings**

**置信度**：4/5（两位 Reviewer 交叉后在大多数关键问题上达成共识，统计分析均属专长领域）

### 给分理由

**支持 Findings 的因素**：
- Per-example 低重叠发现（Jaccard ≤ 0.14, all p < .01）稳健，通过多种 robustness checks 确认
- Controlled experimental design 是该类分析的 gold standard
- 主题时效性强，对 hybrid architecture 部署实践有参考价值
- 统计局限性的诚实披露值得肯定

**限制至 Findings（而非 Conference）的因素**：
- **Statistical rigor**：最具创新性的 claim——aggregate convergence vs per-example divergence 的 decoupling——因 n=5 结构性限制和 GDN confound 而缺乏充分统计支撑（R1/R2 共识）
- **Novelty**：核心方法论（Jaccard + permutation test）为已有工具的直接应用；ecological fallacy 框架已知（R2 主张，R1 部分同意——empirical first 有价值但不足以支撑 Conference）
- **Seed confound**：单次 run + Pythia 70M calibration 三重 mismatch，无法确立架构选择（而非 seed variation）驱动 per-example divergence（R1/R2 共识）
- **Routing**：仅 1/4 benchmark 有效，缺乏 variance 和 baseline，不足以作为独立方法贡献（R1/R2 共识）
- **Scale**：≤ 1.3B 结论在 7B+ 部署场景下外推有风险

### EMNLP 2026 评分映射
- 3.0 = Findings（可被 Findings 接收）
- R1 评 3.0，R2 评 3.5（Borderline Conference）
- 圆桌判定：3.0。Per-example 发现虽稳健，但 convergence decoupling 的 unsupported claim 和 novelty 限制使论文难以达到 Conference 档位。若 MF1-MF3 的统计问题得到实质性解决（而非仅 hedging），可上升至 3.5。

---

## Detailed Comments

### Section 1 (Introduction)
- "We present the first systematic per-example analysis"——定位为 empirical first 是恰当的，但建议进一步明确这是 empirical characterization 而非新概念发现。
- BCa CI [-1.0, -0.7] 首次出现时缺乏 n=3 heuristic caveat（R1-W3, R2 交叉 AGREE）。
- "Confidence-informed routing extracts 36% of oracle complementarity"——建议加 benchmark specificity（仅 LAMBADA）。

### Section 3 (Method)
- §3.2 Task Taxonomy 按 cognitive demand 分类但忽略 evaluation format confound（R1-W2）。LAMBADA 作为唯一 free-form benchmark 的特殊性需讨论。
- §3.5 Statistical Methods 对 n=5 power limitation 的说明在主文较充分，但应与 §4.2 措辞保持一致。

### Section 4 (Experiments)
- §4.1 Per-Example Divergence：核心发现稳健。"saturates" 一词建议改为 "remains at a low plateau"——Jaccard ≈ 0.10 接近 floor 而非 ceiling（R1-M3）。
- §4.1 Routing：SD across CV splits 必须报告。考虑加入 confidence-weighted majority vote 作为 baseline。
- §4.2 Aggregate Trends：全文最需修改的 section。"Only LAMBADA shows monotonic convergence" 应改为 "LAMBADA shows a monotonically decreasing pattern that does not reach statistical significance"。所有 non-significant findings 统一标注 descriptive/suggestive。
- §4.3 Robustness：GDN exclusion 的讨论已存在但需加强——明确 LAMBADA convergence 是 confound-dependent。五架构验证标注 "at 340M"。

### Section 5 (Conclusion)
- "Per-example multiplicity in hybrid recurrent models" → 加 "in 340M–1.3B"。
- Routing 从 practitioner implication 降级为 preliminary exploration / future direction。
- 两条 practitioner implications（α > 0.2 warrants audit; low-Jaccard pairs maximize complementarity）措辞应限定 scale 和 architecture coverage。

### Limitations
- Single-seed 讨论应加强——当前 "cannot fully exclude" 低估了 Pythia calibration 的 gap 仅 0.042 的严重含义。
- 增加 evaluation format confound 的讨论。

### Appendix
- A: 明确 all-10 Bonferroni 为唯一有效 correction。
- D.1: Bootstrap CI caveat 应传导到主文引用处。
- P: 核心发现（AUC 0.70–0.74）应在主文简述。
- W: Seed calibration 的三重 mismatch 应更显著标注。