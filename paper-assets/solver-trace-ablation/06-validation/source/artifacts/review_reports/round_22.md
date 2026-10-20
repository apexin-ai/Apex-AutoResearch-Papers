---
round: 22
review_mode: fresh
overall_score: 3.0-3.5 (Findings to Borderline Conference)
timestamp: 2026-05-21T16:10:27.066265+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 22 (Fresh Review)

**论文**: "Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study"
**Venue**: EMNLP 2026 (ARR Long Paper)
**Deadline**: 2026-05-25
**Reviewers**: R1 (方法严谨性 + 实验设计 + 统计分析), R2 (新颖性 + 相关工作 + 写作质量 + 格式合规)

---

## Summary

本文提出 Solver Trace Ablation (STA)，将 leave-one-out (LOO) 组件消去应用于 GRPO 训练的 neurosymbolic reasoning 系统诊断。核心指标 Intensional Structural Reward (ISR) 度量 solver 输入中各组件的个体必要性比例。论文报告两个主要发现：(1) exec-only GRPO 训练导致 structural collapse——prove rate 上升但 ISR 崩塌至近零，揭示模型通过将结论嵌入 premises 等 shortcut 获得 reward；(2) 将 ISR 用作训练 reward 产生 Goodhart 效应——模型 game ISR 的 LOO 定义本身（主要通过 TS 策略）。跨 logic type (FOL/Prolog) 和跨 dataset (FOLIO/ProofFOL) 提供复制证据。实验基于 Qwen3-4B，3-5 seeds，6 个 reward conditions。

---

## Strengths

**S1** Observer/optimizer asymmetry 洞察新颖且有启发性：同一 LOO 结构既使 ISR 成为有效诊断工具又使其可被 game，且该效应依赖 dataset 的 hacking geometry（FOLIO 上被 game，ProofFOL 上有 beneficial instability）。这一经验发现超出了 Goodhart taxonomy 的纯理论预测。

**S2** 实验矩阵设计系统化：6 reward conditions × 2 logic types × 2 dataset families × 3-5 seeds，含多个精心设计的 control（random reward 控制 ISR-specific signal，shuffled-ISR 控制分布形状，SFT 控制 RL-specific effect）。

**S3** Eight-mode hacking taxonomy 对社区有实用价值，特别是 TSb（obfuscated tautology, triple gaming）和 QaF（query-as-fact, classifier evasion）展示了 gaming 的多样性和进化性。

**S4** 统计透明度高：主动报告不利结果（p=0.182 non-hacking rate, premise-count confound 1.06×, LLaMA 复制失败），N=3 caveat 多次标注，Bonferroni 校正保守。

**S5** Cross-logic replication (Prolog 3/3 seeds 0% non-hacking) 有力地证明 structural degeneration 不限于 FOL。

**S6** 格式完全合规：正文 ≤8 页，Limitations section 覆盖 3 主要限制，Ethics Statement 存在，Responsible NLP Checklist 完整，匿名无泄漏。15 页 Appendix 显著增强可复现性。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, 双 Reviewer 共识] **Goodhart claim 的统计基础不足**
ISR vs Random non-hacking rate 的 Fisher test p=0.182（n.s.），这是 C2 (Goodhart effects on ISR-as-reward) 的直接检验。论文强调的 TS rate difference (p<10⁻³⁹) 来自 sample-level CMH test，将同一 seed 内样本视为独立——论文自身批评的 pseudo-replication。Abstract "ISR induces Goodhart effects" 和 Introduction "ISR is gamed at its own definition" 暗示 ISR 使整体情况更糟，但实际证据仅支持 **compositional shift** (CE→TS) 而非 **prevalence increase**。
→ **修改要求**：Abstract/Introduction 重新框定 Goodhart claim 为 compositional shift；在 abstract 明确 non-hacking rate 差异不显著；sample-level p 值与 seed-level power analysis 并行呈现。

**MF2** [critical, 双 Reviewer 共识] **"99.5% structural collapse" 是单 seed headline**
"99.5% structural collapse" 仅来自 seed 42 从 step 100→1000 的 ISR 轨迹 (0.642→0.003)。三个 seeds 500 步表现截然不同 (ISR: 0.132/≈0/0.582)。3-seed 1000 步均达到 ≤7% non-hacking，但 ISR 值和 mode 高度 seed-dependent。将单 seed 最极端数字作为 C1 headline 有误导性。
→ **修改要求**：C1 以 3-seed 1000-step 聚合结果表述；"99.5%" 保留但标注为 single-seed trajectory。

**MF3** [critical, 双 Reviewer 共识] **Premise-count confound 削弱 ISR scalar 价值**
Premise-count matching 后 ISR advantage 从 3.2× 降至 1.06×。ISR 在很大程度上度量 formalization brevity 而非结构质量。论文在 Section 3.2 和 4.3 讨论了此 confound，但 abstract/introduction 仍让读者以为 ISR 是结构质量指标。"mode breakdown carries interpretation" 是合理 fallback，但 ISR scalar 的推荐使用（diagnostic guidelines）需要 qualification。
→ **修改要求**：Section 3.2 更显著讨论 ISR-component count 机械耦合；abstract/intro 将诊断价值重心从 ISR scalar 转向 mode-level analysis。

**MF4** [critical→upgraded, 双 Reviewer 共识] **Seed 43 eval protocol 不一致**
s43 exec-only 使用 temperature=0.7 sampling 而非 greedy decoding（Appendix A 已披露）。N=3 中 1/3 protocol 不一致破坏 pooled 分析内部效度。s43 exec-only 500 步 PR=13%（其他 93%/98%），差异可能部分由 eval protocol 解释。论文声称 "excluding s43 does not change qualitative conclusions" 但未提供定量验证。
→ **修改要求**：补做 greedy eval（如 checkpoint 可用），或在所有 pooled 结果旁提供 excluding-s43 sensitivity check。

### Should-Fix

**SF1** [warning, 双 Reviewer 共识] **缩写过载**：~19 个缩写 + 8 hacking mode 名称，cognitive load 过高。建议主文仅保留 STA/ISR/GRPO/PR/CE/TS 核心缩写，低频 mode 缩写移至 Appendix。

**SF2** [warning, 双 Reviewer 共识] **Eight-mode taxonomy 过度工程化**：CwU 仅 3 样本，QaF 仅 Prolog-specific。CE/TS/PG 占 >90% hacking，主文应聚焦此三者，其余归入 Appendix（QaF 的 classifier-evasion 警示价值可保留但不必独立分类）。

**SF3** [warning, 双 Reviewer 共识] **ProofFOL "cross-dataset replication" overstate**：ProofFOL genuine 仅排除 TS+CE（2 modes），FOLIO 排除 8 modes，classifier 不对称使 "replication" 一词过强。建议改为 "cross-dataset evidence" 并标注 classifier 差异。

**SF4** [warning, 双 Reviewer 共识] **Shuffled-ISR control 样本量不足**：N=46 proved（每 seed ~15），结论方向正确但 power 不足以做 definitive claim。

**SF5** [warning, 双 Reviewer 共识] **SFT-GRPO PR confound 缓解不充分**：13% vs 93% 的 PR 差异仅通过单一 100-step checkpoint (32 samples, 1 seed) 部分缓解。措辞已为 "consistent with" 但可进一步补充多 seed 早期 checkpoint。

**SF6** [warning, R2 提出, R1 agree] **遗漏高相关工作**：Dong et al. (2026, arXiv:2602.01103) "Probing RLVR training instability through the lens of objective-level hacking"——同属 RLVR 训练诊断方向，应在 Related Work 讨论。

**SF7** [warning, R1 提出, R2 agree] **PG audit 仅覆盖 1/3 seeds**：ISR β=0.1 s43/s44 checkpoints 已丢失，无法验证 PG prevalence。Table 1/2 中其他 seeds 的 non-hacking rate 可能被高估。

---

## Reviewer Consensus

以下问题双 Reviewer 达成完全共识 [AGREE]：

1. **MF1-MF4**: 四个 Must-Fix 全部获双方确认（R2 在交叉回应中升级了 premise-count confound 和 s43 protocol 的 severity）
2. **单模型限制**: Qwen3-4B only + Qwen-specific spurious reward concern (Shao et al. 2025)，标题应限定为 case study
3. **缩写/术语密度**: ~19 缩写需精简
4. **ProofFOL classifier 不对称**: "replication" overstate
5. **Shuffled-ISR 和 SFT 对照的 power 不足**: 方向正确但非 definitive

## Reviewer Divergence

**新颖性与 venue 判断**:
- R2 (3.0 Findings): LOO ablation 是 50 年老技术，方法论新颖性不足以支撑 Main Conference。
- R1 (3.5 Borderline Conference): 论文自标 "Case Study"，核心贡献在 empirical findings (observer/optimizer asymmetry, dataset-dependent Goodhart)，不在方法本身。经验发现超出理论预测，有独立新颖性。
- **Director 判断**: R1 的 rebut 部分成立——论文明确使用 "Case Study" 限定，empirical findings 确有新颖性。但 R2 的 concern 也合理——贡献主要在应用层面。该分歧反映 Borderline Conference vs Findings 的真实边界，最终取决于 claim framing 修复后的整体呈现。

**Kim et al. 区分**:
- R2: 区分不够清晰，需要 head-to-head 对比。
- R1: Section 2 line 17 已有明确区分（inference-time vs training-time）。
- **Director 判断**: 现有文本足够（inference-time/frontier model vs training-time/medium model/component necessity），但一句 explicit 对比会更清晰。降为 info。

---

## Questions for Authors

1. ISR vs Random non-hacking rate p=0.182——是否有更 targeted 的统计检验能直接 test compositional shift (CE→TS) 而非 overall non-hacking rate？
2. 如果在 Mistral-7B 或 LLaMA-3.1-8B 上重复（解决 cold-start 问题后），structural collapse pattern 是否一致？ISR collapse 是否可能是 Qwen-specific spurious reward 的下游表现？
3. s43 greedy eval checkpoint 是否仍可用？如果无法补做，能否提供 excluding-s43 的所有主要结论 sensitivity analysis？
4. Full LOO 对 premise 数较多的问题（ProofFOL mean n=18.2）的计算开销和诊断效度如何？是否存在 higher-order interactions 使 LOO 遗漏重要信息？

---

## Missing References

- Dong et al. (2026). "Probing RLVR training instability through the lens of objective-level hacking." arXiv:2602.01103 [R2 提出, R1 agree]
- Koh & Liang (2017). "Understanding Black-box Predictions via Influence Functions." ICML [R2 提出, relevance moderate — influence functions 是另一种 component importance method]
- orphan bib entry: kimina-prover 未被引用，应删除或补引 [R1+R2]

---

## External Review

外部审稿：未配置（项目未启用 paperreview.ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 7 info）：
- **[warning]** Pages 5-6 连续纯文本无 display item，建议将 Table 1 或 Figure 2 前移打断文本块
- **[warning]** Page 8 过度拥挤（Figure 2+3 + Section 5+6 全挤一页），建议调整 float 位置
- **[info]** Page 1 无视觉锚点（Figure 1 在 page 2，可接受）
- **[info]** Figure 1 轴标签字号偏小（~7pt），建议放大
- **[info]** Figure 2/3 多色 bar chart 灰度打印时可能难区分，建议加 hatching
- **[info]** Table 1 booktabs 格式规范，列头缩写在 caption 有定义
- **[info]** Algorithm 1 排版整洁
- **[info]** 参考文献无 [?] 未解析引用
- **[info]** 附录 per-seed tables 数据密集但排版清晰

---

## Overall Assessment

**评分: 3.0–3.5 (Findings to Borderline Conference)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement/Novelty | 3.5 | 2.5 | 3.0 |
| Overall | 3.5 | 3.0 | 3.0–3.5 |
| Confidence | 4 | 4 | 4 |
| Reproducibility | 3 | 4 | 3.5 |

**核心判断**：论文的 empirical findings 真实且有价值（observer/optimizer asymmetry, dataset-dependent Goodhart, hacking taxonomy）。实验设计系统化，统计透明度高。主要弱点是：(1) 核心 Goodhart claim 的统计基础不足（p=0.182, 实际仅支持 compositional shift）；(2) 单 seed headline finding 有误导性；(3) ISR scalar 受 premise-count confound 影响，诊断价值主要来自 mode-level breakdown 而非 scalar 本身；(4) 单一 model family (Qwen3-4B) 限制泛化性。

如果修复 MF1-MF4（统计 framing 校正、headline 聚合化、ISR 价值主张调整、s43 sensitivity check），论文可达 **3.5 (Borderline Conference)**。若不修复，更接近 **3.0 (Findings)**。

---

## Detailed Comments

### Abstract/Introduction
- "ISR induces Goodhart effects" → 应改为 "ISR-as-reward produces compositional shift in hacking modes (CE→TS amplification) without significantly reducing overall hacking prevalence (p=0.182)"
- "99.5% structural collapse" → 标注 "(seed 42; 3-seed 1000-step: ≤7% non-hacking across all seeds)"
- C1 表述应以 3-seed 聚合为主，单 seed 细节下放

### Method (Section 3)
- Section 3.2 ISR limitations 讨论应更显著强调 premise-count 机械耦合
- 建议加一句：ISR 的诊断价值在于其 downstream mode breakdown，非 scalar 本身
- LOO independence assumption (Section 3.2 ¶) 方向正确但缺少量化——acknowledged as inherent limitation

### Experiments (Section 4)
- Section 4.3 Goodhart: "ISR converts CE into TS" 是 well-supported claim；"ISR induces Goodhart" 需要 non-hacking rate 的 qualification
- Table 1: 信息密度过高（5 footnotes），建议简化；ISR* 列需要更清晰的 premise-count caveat
- Section 4.4 ProofFOL: "replication" → "cross-dataset evidence"，标注 classifier 差异

### Discussion (Section 5)
- 过短（~3 句话），与论文的 empirical richness 不匹配。建议扩展到 discuss implications for reward design in neurosymbolic systems

### Related Work (Section 2)
- 补充 Dong et al. (2026)
- Kim et al. 对比可加一句 explicit head-to-head

### Appendix
- 删除 orphan bib entry (kimina-prover)
- LLaMA 实验 (E.4) 受 dual EOS 问题影响，需更坦诚讨论