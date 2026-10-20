---
round: 14
overall_score: 3.0 Findings
timestamp: 2026-05-17T23:44:54.230437+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 15 审稿报告 — gen-depth-fingerprint

**Target Venue**: EMNLP 2026 via ARR May 2026 cycle (Long Paper)
**Deadline**: 2026-05-25
**Reviewers**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作)
**Rounds**: 1 (converged after cross-sharing, no Round 2 needed)

---

## Summary

本文提出 generation depth classification 任务，将文本按递归生成深度分为 gen-0/gen-1/gen-2+，并发现 differential depth response (DDR)：central-tendency 特征随深度单调漂移，而 shape 特征近似平稳。基于此设计 7 特征 XGBoost 分类器，在 8-generator LOGO 评估下达到 leak-free binary F1 = 0.694。方法仅适用于 base model (t≤0.9)。

---

## Strengths

**S1. 任务定义新颖且有意义** [R1,R2 consensus] — 将 binary AI-text detection 扩展到 ordinal depth classification 是概念上的真实推进，与 model collapse 和 data provenance 研究直接相关。

**S2. DDR 分解有解释性价值** [R1,R2 consensus] — Drifting vs. stationary 的结构化分解提供了对递归生成过程的新理解，KS/Spearman/Levene 多角度验证充分。

**S3. 评估严谨且透明** [R1,R2 consensus] — LOGO 设计、leak-free binary metric、bootstrap CI、Bonferroni 校正、主动报告 null results。

**S4. 附录极为丰富** [R2] — 16 个附录覆盖几乎所有可预见的消融问题。

**S5. Limitations 坦诚** [R1,R2 consensus] — Instruct failure、scale degradation、temperature sensitivity 等局限充分讨论。

**S6. 写作质量好** [R2] — 无 AI 写作痕迹，叙事连贯，术语定义完整。

---

## Weaknesses

### Must-Fix (5 条, 影响接收决定)

**MF1 [critical, consensus]. Seed sharing 引入 topic fingerprint confound — 核心实验有效性受威胁**
- 约 1000 Wikipedia seeds 在 8 个 generator 间共享。LOGO hold out generator X 时，训练集仍包含从相同 seeds 生成的其他 generator 的 gen-1/gen-2+。分类器可能学到 seed-topic fingerprint 而非纯粹 depth signal。
- Binary evaluation 排除 gen-0 但不排除 gen-1/gen-2+ 的 topic confound。
- Cross-domain (Appendix G) 部分缓解但规模不足 (3 gens × 200 seeds)。
- **Required action**: 运行 disjoint-seed LOGO 实验（每个 generator 使用完全不重叠的 seed 池），量化 topic confound 贡献。
- (Tracker: R7-W1 + R14-W5, first raised R7, 9 rounds unresolved)

**MF2 [critical, consensus]. Introduction motivation 与 base-model-only scope 根本不匹配**
- §1 以 web contamination (7-17% LLM papers) 和 data quality 为动机——这些场景几乎全来自 instruct/RLHF 模型。
- 论文承认 instruct 上 F1=0.338 (§5)，最初激发研究的应用场景恰是方法不适用的。
- Title 含 "Base LLM" 但 Intro 前两段仍创造不匹配期望。
- **Required action**: 重写 Intro §1 从 scientific/theoretical 角度（recursive generation dynamics characterization）切入，而非 practical web detection。Title 加 "Base" 或 "Pretrained"。
- (Tracker: R7-W5, first raised R7, still open)

**MF3 [critical, consensus]. Downstream null result 动摇 practical motivation**
- §2.4 将 depth 定位为 data curation 的 complementary signal，但 Appendix D 显示 depth-aware curation 不优于 random subsampling (ppl 2.387 vs. 2.367, TOST confirms equivalence)。
- 如果 depth 不能改善训练数据质量，data curation 动机被自己的实验否定。
- **Required action**: 弱化 data curation motivation；重新定位 practical value 为 corpus-level auditing/provenance tracking（非 actionable filtering）。
- (Tracker: R10-N3, first raised R10)

**MF4 [critical, consensus]. 7-feature ensemble 非最优方法 — contribution framing 需调整**
- Table 2: 4-det+surface (binary 0.708, 3-class 0.795) 在两项指标上均优于 7-feature (0.705, 0.774)。
- 当前叙事暗示 7-feature 有性能优势，实际优势仅在效率 (9.7ms vs. 22.8ms)。
- **Required action**: 将贡献明确拆分为 (a) 任务定义 + DDR 现象 = 科学贡献，(b) 7-feature = 高效单参考模型实现（工程贡献）。删除任何暗示性能领先的措辞。
- (Tracker: R11-W2, first raised R11)

**MF5 [critical, consensus]. Cross-model chains vs LOGO 评估协议不可比 — causal claim 不成立**
- Cross-model chains 使用 5-fold CV（所有 5 generators 在训练集出现），LOGO 完全 hold out generator。
- Binary 0.764 vs. 0.694 差距可完全由 (a) 评估协议差异 + (b) easier 5-gen subset (avg LOGO ~0.707 vs. 8-gen 0.694) 解释。
- "Generator heterogeneity amplifies distributional shifts" (§4.1) 是不受控的 causal claim。
- **Required action**: 对 cross-model chains 应用 LOGO，或删除 causal claim 改为描述性报告。报告 5-gen subset 的 single-generator LOGO 作为对照。
- (Tracker: R15-N1, new this round)

### Should-Fix (5 条, 影响评分)

**SF1 [warning, consensus]. "Approximately preserves shape" claim 偏强**
- Levene test 对所有 features 拒绝等方差 (p<10^-10)，包括 shape features。CV shift <3% vs >15% 是 informative 但 "preserves" 太强。
- Action: 改为 "remains comparatively stable" + 报告 Cohen's d 或 variance ratio + 加 reconciliation statement。
- (Tracker: R7-W2, first raised R7)

**SF2 [warning, consensus]. DDR novelty positioning 不精确**
- "Drift happens" 在 model collapse 文献中已知 (Shumailov, Guo)。Novel contribution 是 drifting/stationary 分解 + location-shift-preserves-shape 的特定发现。§1/§4.2 有时混淆这两个层次。
- Action: 在 Introduction 明确区分 known (drift) vs. novel (structured decomposition)。
- (Tracker: R15-W2, new this round)

**SF3 [warning, consensus]. Prompt type 限制未在 main results 反映**
- Main experiment 仅用 continuation (best-case, 0.781)。Paraphrastic 0.671 差 11pp。读者必须到 Appendix 才能了解 severity。
- Action: §4 Results 加一段 prompt-type sensitivity summary。
- (Tracker: R15-W3, new this round)

**SF4 [warning, partial consensus]. Feature redundancy — effective dimensionality ~5**
- TTR-hapax r=0.97, 两者与 entropy_mean 强相关。R2 partial REBUT: LOFO 显示边际贡献 (TTR -0.55pp, hapax -0.42pp)。Consensus: tree-based model 可利用微小差异，但 "7-feature" branding 夸大。
- Action: 加一句 acknowledge effective dimensionality ~5。
- (Tracker: R15-W1, new this round)

**SF5 [warning, partial consensus]. Scale 退化趋势**
- Binary F1: Pythia-1B (0.718) → Qwen3-8B (0.692) → Mistral-7B (0.633)。无 fundamental limit 分析。
- R1 partial REBUT: theoretical analysis 超出 empirical paper scope。但 scaling plot (F1 vs log params) 有价值。
- Action: 在 Discussion 增加 scaling trend 定量描述。
- (Tracker: R13-SF7, updated)

### Nice-to-Have (4 条)

**NH1.** 缺少 qualitative examples（gen-0→gen-1→gen-2+ 文本对比）[R2-M3]
**NH2.** 附录 6-gen/8-gen 标注可更一致 [R2-M1]
**NH3.** 缺少 threshold-based binary detection ROC-AUC 作为 reference point [R1-W4 partial]
**NH4.** Bib entries: 核查 self_consuming_mad first author 顺序 [R2-M4]

---

## Reviewer Consensus

| Issue | R1 | R2 | Verdict |
|-------|----|----|---------|
| MF1: Seed sharing topic confound | AGREE (N1) | AGREE | **Consensus** |
| MF2: Motivation-scope mismatch | AGREE (W3) | AGREE (N1) | **Consensus** |
| MF3: Downstream null result | AGREE (W5) | AGREE (N2) | **Consensus** |
| MF4: 7-feature not best | AGREE (N3) | AGREE (N3) | **Consensus** |
| MF5: Cross-model protocol | AGREE (N2) | AGREE | **Consensus** |
| SF1: Shape preservation | AGREE (W1) | AGREE (W5) | **Consensus** |
| SF2: DDR novelty | AGREE | AGREE (W1) | **Consensus** |
| SF3: Prompt type | AGREE | AGREE (W4) | **Consensus** |
| SF4: Feature redundancy | Raised (W2) | Partial REBUT | **Partial** |
| SF5: Scale degradation | Partial REBUT | Raised (W2) | **Partial** |

---

## Reviewer Divergence

| Issue | R1 Position | R2 Position | Resolution |
|-------|-------------|-------------|------------|
| Baseline fairness (R1-W4) | Should-Fix: single-score forced to ordinal | REBUT: binary IS native task, same XGBoost | **Agreed to disagree**: binary eval is fair, but threshold-based reference would help |
| Scale analysis depth (R2-W2) | REBUT: theoretical limit out of scope | Should-Fix: need fundamental limit | **Agreed**: scaling plot yes, theoretical analysis no |
| Feature redundancy severity | Should-Fix: effective dim ~4-5 | Partial REBUT: LOFO shows marginal value | **Agreed**: acknowledge ~5 effective dims, retain both |

---

## Questions to Authors

**Q1.** [R1,R2] Disjoint-seed LOGO F1 是多少？（500/500 split, 每个 generator 独立 seed pool）

**Q2.** [R1,R2] Cross-model chains 在 LOGO 协议下（hold out 一个 generator 完全不参与任何 step）的 binary F1？

**Q3.** [R1] 选择 7-feature 而非 4-det+surface 作为 primary method 的技术理由是什么（除效率外）？

**Q4.** [R2] "Corpus-level flagging" claim (§5) 是否有 aggregation experiment 支持？（如 batch 中 gen-2+ 比例估计精度）

**Q5.** [R1] Topic-agnostic normalization（z-norm within each seed）后 depth signal 是否保留？

---

## Missing References

- **Briesch et al. (2023)** "Large Language Models Suffer From Their Own Output" — training-free iterative degradation
- **Zhang et al. (2024)** "Watermark Stealing in Large Language Models" — watermark decay in multi-step chains
- **"Your Large Language Models Are Leaving Fingerprints" (ACL 2025 GenAIDetect Workshop)** — LLM linguistic fingerprinting
- **Tang et al. 2024** "Science in the age of large language models" — web contamination motivation
- 核查 **Geng et al. 2026 (markovian_chains)** 是否有更新版本

---

## External Review (Stanford Agentic Reviewer)

未配置。无外部审稿结果。

---

## Overall Assessment

**Overall Score: 3.0 / 5 (Findings)**

| Reviewer | Soundness | Excitement | Overall | Confidence |
|----------|-----------|------------|---------|------------|
| R1 | 3/5 | 3/5 | 3.0 | 4/5 |
| R2 | 3.5/5 | 2.5/5 | 3.0 | 4/5 |
| **Average** | **3.25** | **2.75** | **3.0** | **4** |

**一句话总结**: 一篇方法论严谨、实验丰富的 phenomenon paper，提出了有意义的新任务和结构化发现 (DDR)，但 seed sharing 对核心实验有效性的威胁未解决、motivation 与 scope 不匹配、proposed method 非最优。适合 EMNLP Findings 而非主会议。

**Recommendation**: Findings-level acceptance contingent on:
1. Disjoint-seed LOGO 实验证明 F1 不显著下降（MF1）
2. Introduction motivation 重写为 scientific characterization（MF2+MF3）
3. Contribution framing 调整为 task+DDR phenomenon（MF4）
4. Cross-model causal claim 删除或补充控制实验（MF5）

若 MF1 实验显示 disjoint-seed F1 大幅下降（>5pp），则 depth signal 本身的有效性存疑，评分可能降至 2.5 (Borderline Findings)。

---

## Detailed Comments

### Abstract
- 准确反映内容，无过度宣传
- "approximately preserves distributional shape" 作为 abstract-level claim 仍偏强 (SF1)
- 建议更早/更显著标明 base-model scope

### Introduction (§1)
- 叙事结构完整但 motivation 与 scope 不匹配 (MF2)
- 第1段 7-17% citation 暗示 instruct-model 场景
- Contribution 第2条混合 phenomenon (DDR) 和 method (7-feature)，建议拆分

### Related Work (§2)
- 覆盖全面（61条引用），四条线索清晰
- 与 broken_telephone、markovian_chains 的区分到位
- DDR vs. model collapse 区分在 §2.2 已改善（R14 fix confirmed）
- 可补充 5 条 missing references

### Method (§3)
- Task formulation 简洁清晰
- §3.2 seed sharing 讨论过于轻描淡写——需面对 gen-1/gen-2+ 层面的 topic confound
- entropy_min 保留理由 weak (LOFO Δ=+0.01pp)
- Feature correlation acknowledgment 缺失 (SF4)

### Results (§4)
- §4.1 gen-0 caveat 处理得当，但 cross-model vs LOGO 比较有 protocol confound (MF5)
- §4.2 DDR 展示 convincing，但 shape preservation claim 需 soften (SF1)
- §4.3 baseline comparison 公平（同 XGBoost），但 7-feature 不优于 multi-detector 需更 prominent 讨论 (MF4)
- 缺失 prompt-type sensitivity summary (SF3)

### Discussion (§5)
- 温度、instruct failure、resolution ceiling 讨论 balanced
- "Corpus-level flagging" claim 无实验支撑
- DDR vs model collapse 区分是重要 conceptual contribution

### Limitations
- 异常全面（~1页），覆盖所有主要局限
- 论文显著优点

### Format Compliance
- 8 页正文 ✓, ACL review template ✓, 行号 ✓, 匿名 ✓, 附录双栏 ✓, natbib ✓
- Responsible NLP Checklist: 未在提交材料中确认（需 ARR 提交时填写）