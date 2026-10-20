---
round: 12
overall_score: borderline
timestamp: 2026-05-16T05:32:57.676261+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 12（Fresh Review）

**项目**: struct_self_consist_ie
**论文**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Structured Information Extraction"
**目标 Venue**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
**截止日期**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计; R2: 新颖性+完整性+写作）
**轮次**: 1 轮即收敛（关键问题强共识，无重大未解决分歧）

---

## Summary

本文评估五种置信度信号（structural: SJ/VC; surface: EM/FK; model-internal: LP）在 LLM-based structured IE 中的质量估计（QE）和 best-of-N 样本选择能力，提出 "correlation-selection gap"：信号与 F1 达中等相关性（Spearman ρ up to 0.45）但无法改善样本选择，尽管 oracle headroom 达 13-18 pp。四个 instance-level 信号本质上对所有 candidate 赋予相同分数；LP（唯一 per-sample 信号）因 within-instance 压缩（中位数范围 0.041 nats, 60% tied）而失败。Free-form ablation 证明 NER LP 压缩非 constrained decoding artifact。

论文在统计方法和实验设计上达到较高标准（bootstrap CI, TOST, permutation tests, 多 seed 验证），但核心 framing 存在定义性 vs 经验性发现的混淆，标题/scope 不匹配实际覆盖度，且纯诊断性论文缺乏 remedy 尝试限制了 impact。

---

## Strengths

**S1** [两位共识] **QE vs selection 的显式形式化**：Section 3.1 首次在 IE confidence estimation 领域系统区分 per-sample 和 instance-level 信号，ρ/AUROC/selection F1 三指标的 decouple demonstration 对 test-time compute scaling 社区有直接参考价值。

**S2** [两位共识] **LP compression 分析深度突出**：多角度刻画——median range 0.041 nats, pooled within-instance ρ=0.248, non-tied subset +2.9pp (p=0.004), CDF 连续性, VerbConf 对照 (Appendix K)——是论文最有价值的 empirical contribution。

**S3** [两位共识] **统计分析全面且透明**：Bootstrap CI (B=10,000), permutation tests, Fisher combined p-values, TOST with multiple δ anchors, ε-robustness sweep, external equivalence margins。主动识别并处理了 potential circularity（TOST δ vs oracle headroom）。超过 EMNLP 平均水平。

**S4** [两位共识] **消融设计合理**：Free-form decoding ablation（4-seed, NER+RE）有效隔离 constrained decoding 影响; Scale ablation (3B-8B) 提供跨规模验证; Temperature + N-scaling 覆盖关键超参。

**S5** [两位共识] **诚实的 limitations 和 caveats**：RE 始终用 † 标注, TOST configuration-dependent 已说明, ε 标注 post-hoc, thinking token confound 有 3-part 分析。Appendix 极其详尽（15+ sections）。

**S6** [R1] **负面结果呈现方式得当**：通过 non-tied subset 展示 LP 在什么条件下能工作，并诊断出 compression 作为瓶颈，而非强行 positive spin。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, 两位强共识] **"By construction" framing 混淆定义性与经验性发现，掩盖 MBR failure 的独立价值**

论文反复声称 4/5 信号 "cannot rank candidates by construction"（Section 3.1, Abstract, Discussion），但 Table 2 显示这些信号通过 consensus-proximity selection (MBR) 确实产生了不同的 selection F1（SJ=0.646, FK=0.646, EM=0.637, VC=0.623）。Discussion 也承认 "VC becomes per-sample in the selection context." Appendix §MBR Discussion 将 selection 等价为 MBR decoding。

两位 Reviewer 一致认为：
- (a) instance-level QE 值对所有 candidate 相同——这是**定义必然**，不是经验发现
- (b) 将这些信号转化为 MBR-style per-sample utility 后 selection 仍然失败——这是**真正的经验发现**（MBR 在 MT 中有效但在 IE 中失败）
- 论文将 (a) 和 (b) 混为一谈，将 MBR 的经验性失败归为 "by construction"，既弱化了 (b) 作为独立 contribution 的价值，又在逻辑上自相矛盾

**建议**：Contribution list 重组——将 instance-level/per-sample 分类降为 Section 3 前提，将 MBR within-instance failure 提升为独立 empirical contribution，LP compression 保持为核心 contribution。Appendix §MBR Discussion 的 within-instance failure 分析应进入主文。

**MF2** [critical, 两位强共识] **标题 "Structured Information Extraction" 与实际覆盖严重不匹配**

"Structured IE" 通常涵盖 NER、RE、Event Extraction 等。论文的核心证据来自 3 个 NER benchmark（flat entity recognition），RE 仅 SciERC 一个 benchmark（40% zero-F1）作为 "exploratory extension"，全文用 †RE 标注 preliminary。无 Event Extraction。实质上是 NER confidence estimation 论文附带初步 RE 探索。

此问题已**持续 13 轮**（首次提出于 Round 0），是最顽固的 issue。每轮 Reviewer 均指出标题/scope 落差。

**建议**：(a) 将标题限定为 NER / Entity Set Extraction，RE 作为 exploratory extension; 或 (b) 增加至少一个独立 RE dataset（如 DocRED）使 RE 结论不再 preliminary。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, 两位共识] **ρ=0.45 描述为 "strong quality estimation" 措辞过度**

R2 原列为 Must-Fix，R1 有效 rebut 后降为 Should-Fix。Cohen's benchmarks (0.1/0.3/0.5) 适用于行为科学，不直接适用于 NLP unsupervised QE。但 ρ=0.45 仅解释 ~20% 方差，"strong" 确实 overstate。

**建议**：改为 "moderate-to-strong by domain standards, substantially exceeding random baselines"。

**SF2** [warning, 两位共识] **未测试 entity-token-only LP——Discussion 假说 (d) 的直接检验缺失**

Discussion 列出 hypothesis (d) "format-token dilution" 为 LP compression 主因（fine-tuned models 对 schema tokens 赋予极高 LP），但未直接验证。Entity-name-token-only LP 是零成本消融实验，缺失令人费解。两位 Reviewer 独立提出。

**建议**：增加 entity-token-only LP 消融；如不可行需解释原因。

**SF3** [warning, 两位共识] **纯诊断无 remedy 尝试，限制论文 impact**

论文诊断了问题但未尝试任何解决方案（哪怕是简单的 LP×consistency 组合、LP z-score 归一化、或 entity-token LP）。R1 认为 diagnostic papers 在 EMNLP 有先例（probing/analysis 传统），R2 认为严重限制 impact。共识：Should-Fix level，至少一个 pilot remedy（即使 negative）会显著增强。

**SF4** [warning, 两位共识] **ε=0.05 threshold 依赖影响核心叙事**

"60% tied" 是论文反复引用的核心数字（Abstract, Discussion），高度依赖 ε=0.05。ε=0.03 时 tied fraction 仅 31.8%。LP 是连续信号，二元 threshold 叙述人为。Appendix 有 CDF 和 sweep 但被埋在附录中。

**建议**：主文改用 continuous characterization（pooled within-instance ρ=0.248, CDF 特征）作为 primary evidence，ε-based 分析标注 post-hoc exploratory。

**SF5** [warning, 两位共识] **模型规模覆盖不足（3B-8B）**

3B-8B 本质是同一 capability tier。LP compression 可能在 70B+ 上缓解（更大模型可能产生更多样化 samples）。Conclusion "consistent across two model families (3B–8B)" 暗示超过实际证据的普适性。

**建议**：在 Conclusion/Discussion 明确限定为 small-model regime，或增加 ≥30B 模型 pilot。

**SF6** [warning, 两位共识] **Kendall W=1.000 (n=3 seeds) 统计效力不足**

n=3 排 5 个 signal 的 W=1.000 p≈0.05 仅 borderline significant。Appendix 承认 "statistical power with n=3 is limited" 但正文未体现。

**建议**：正文降低表述强度，改为 "consistent with stable rankings but insufficient power to confirm."

**SF7** [warning, 两位共识] **Table 2 NER 2-seed vs RE single-seed 不一致未解释**

Appendix 有 3-seed RE QE 数据，但 selection 仅 single seed。需在正文或 footnote 说明原因。

**SF8** [warning, R1 提出 R2 同意] **Gold-empty filtering 在 QE 和 Selection 之间不一致**

Section 3.3 说 "selection retains the full set"（n=3453），但 Table A13 CoNLL 标注 n=2756。无论哪个正确，存在矛盾需修正。

---

## Reviewer Consensus

以下问题两位 Reviewer 独立提出并在交叉分享中确认共识：

| Issue | R1 | R2 | Status |
|-------|----|----|--------|
| By-construction framing 问题 | N1 [AGREE] | N1 [AGREE] | **强共识** |
| 标题/scope 不匹配 | N2 [AGREE] | N2 [AGREE] | **强共识** |
| Entity-token LP 未测试 | W3 [AGREE] | Q1 [AGREE] | **强共识** |
| ε threshold 依赖 | — [AGREE] | W4 [AGREE] | **强共识** |
| Model scale 不足 | W5 [AGREE] | W2 [AGREE] | **强共识** |
| Kendall W 效力 | W1 [AGREE] | — [AGREE] | **强共识** |
| NER/RE seed 不对称 | W2 [AGREE] | — [AGREE] | **强共识** |
| Gold-empty filtering | W4 [AGREE] | — [AGREE] | **共识** |
| LP hypotheses 编号错误 | minor [AGREE] | minor [AGREE] | **共识** |

## Reviewer Divergence

| Issue | R1 Position | R2 Position | Resolution |
|-------|-------------|-------------|------------|
| ρ=0.45 "strong" 措辞 | Should-Fix (domain standards differ) | Must-Fix (Cohen's moderate) | **降为 Should-Fix**: R1 有效 rebut, domain-specific 标准有道理 |
| No remedy 的严重程度 | Should-Fix (diagnostic papers 有先例) | 接近 Must-Fix | **Should-Fix**: 共识 pilot remedy 会增强但非必须 |
| Contribution 3 (difficulty-dependent) | 有独立价值 (WNUT-17 collapse) | 较弱 | **保留**: WNUT-17 boundary collapse 对 practitioners 有意义 |
| RE free-form reversal 呈现 | 应更突出 | 谨慎处理适当 | **定位为 promising direction**: 单 benchmark 限制了 claim 强度 |
| Yao et al. 差异描述 | 现有描述充分 | 需更精确 | **Camera-ready refinement**: 现有 3 项差异清晰 |

---

## Questions（需作者回答）

**Q1** [两位共识]: Consensus-proximity selection (MBR) 对 instance-level signals 来说实质上产生了 per-sample ranking。请解释为什么论文将其归类为 "fail by construction" 而非 "MBR fails empirically for IE"——这两者的理论含义截然不同。

**Q2** [两位共识]: Entity-token-only LP（仅对 entity mention tokens 计算 LP，排除 JSON schema tokens）是否被考虑过？如果排除 schema tokens，within-instance compression 是否缓解？这是 Discussion hypothesis (d) 的直接检验。

**Q3** [R1]: Table A13 (cross_selection) 标注 CoNLL n=2756，但 Section 3.3 说 "selection retains the full set" (n=3453)。哪个正确？

**Q4** [R1, R2 同意]: TOST external anchors 显示 Qwen CoNLL selection 比 single-sample 显著更差（0.9-1.5pp degradation，所有外部 δ 下不通过等价检验）。某些配置下 signals 是否主动损害 selection？这与正文 "no signal consistently improves" 的表述不一致。

**Q5** [R2]: Contribution 1 中 ρ, AUROC, selection F1 decouple 的 empirical surprise 在哪里？这三个指标衡量不同的东西（rank correlation, binary discrimination, per-sample selection），decouple 本身是否只是 expected behavior？

**Q6** [R2]: CoNLL (F1≈0.91, oracle headroom ~4pp) 的 selection 分析是否有意义？R1 回应这是必要的 ceiling-effect control，但正文可否避免对 near-ceiling 配置过度解读？

---

## Missing References

两位 Reviewer 共识应补充：
1. **Deguchi et al. (2024)** "Centroid-Based Efficient Minimum Bayes Risk Decoding" — MBR mode-seeking bias 分析，与 Appendix MBR Discussion 直接相关
2. **Mejer & Crammer (2011)** "Confidence Estimation in Structured Prediction" — 经典 structured prediction confidence 先驱工作
3. **Xie et al. (2024)** "Self-Evaluation Improves Selective Generation" (NeurIPS 2024) — LLM per-sample self-evaluation for selective generation

待核实：
4. **Bertoldi et al. (2024)** "Beyond Self-Consistency: Ensemble Reasoning in LLMs" — R1 推荐，R2 rebut 未能找到。需作者核实是否存在。

已有引用无问题：
- R2 引用完整性检查: 47 entries, 0 orphan, 0 missing, 40/47 OpenAlex verified, 无幻觉引用
- oh2025latentsc bib year 建议更新为 2026

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿 (paperreview.ai disabled)。

---

## Overall Assessment

**Overall Score**: Borderline — 介于 Findings (3.0) 和 Conference (3.5) 之间

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 3.0 | 2.5 | **2.75** |
| Reproducibility | 4.0 | 4.0 | **4.0** |
| Overall | 3.5 | 3.0 | **3.25** |

**置信度**: 4/5（两位 Reviewer 均仔细阅读全文及 appendix，熟悉相关文献）

**核心判断**：
- **值得发表**的内容：LP compression 分析、MBR within-instance failure、QE/selection 解耦形式化、统计方法论标准
- **阻碍 Conference acceptance** 的问题：(1) framing 的定义性/经验性混淆（MF1）；(2) 标题/scope 不匹配（MF2，持续 13 轮）
- **如果 MF1+MF2 修正**（contribution 重组 + 标题精确化），可提升至 Conference acceptance (3.5-4.0)
- **当前版本**更适合 **Findings track**：实验扎实、统计全面、负面结果有价值，但 framing 不当和 scope overclaiming 使 main conference 定位困难

---

## Detailed Comments（逐节）

### Abstract
- 信息密度过高（一句话内 ρ=0.45, 0.041 nats, 60% tied, +1.8±0.1 pp）
- "strong quality estimation" → 建议改为 "moderate-to-strong"
- "Four instance-level signals fail by construction" 暗示 LP 是唯一 empirical finding，降低 MBR failure 地位

### Introduction
- Contribution 1 需重组：definitional 部分降为 background，突出 empirical dissociation 的具体 pattern
- Contribution 3 (difficulty-dependent rankings) 较弱但有价值（WNUT-17 collapse 对 practitioners 有意义）
- 与 Yao et al. (2026) 的差异清晰但可更精确

### Method (Section 3)
- Signal 定义严谨，SJ/FK/VC/EM/LP 形式化清晰
- "Soft Jaccard" 命名不准确（分母是 max 不是 union），建议改名或说明
- FK entity set adaptation 非标准但 Appendix permutation test 验证充分

### Experiments (Section 4)
- Table 1: 单 seed 已在 caption 标注，cross-ref Table A7 合理
- Table 2: NER 2-seed vs RE single-seed 不一致需解释
- Section 4.2: "no signal consistently improves selection" 与 TOST external anchors（Qwen CoNLL degradation）存在张力
- Scale ablation (Table 3): 3B-8B 覆盖不足

### Discussion (Section 5)
- LP hypotheses 标注 "three mechanisms" 但列出 4 个——编号错误
- Hypothesis (d) format-token dilution 是最有力假说但未直接测试
- RE free-form reversal (+1.84±0.12pp) 被谨慎处理——建议定位为 promising direction
- "Effective selection likely requires trained verifiers" 指向合理但论文未尝试任何 remedy

### Limitations
- 诚实全面，覆盖了 RE 单 benchmark、model scale、verifier 缺失、ε 选择等已知限制
- 可补充：entity-token LP 未测试的明确说明

### Appendix
- 极其详尽（15+ sections），覆盖了几乎所有消融方向
- MBR Discussion (Appendix L) 的 within-instance failure 分析应进入主文
- RE Conditional Selection (Appendix M) 排除 zero-F1 后 signals 更差 (VC: -10.0pp)——重要结果应在主文提及