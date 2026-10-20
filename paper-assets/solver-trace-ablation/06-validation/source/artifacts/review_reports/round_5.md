---
round: 5
overall_score: 3.0 Findings
timestamp: 2026-05-17T15:05:59.140587+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 5 审稿报告（修订版）

> 修订原因: 初版报告提交时 R1 交叉回应尚未到达。R1 对 R2 的 3 个 critical issues 全部 [REBUT] 且论据有力，需要调整 severity 评级。Overall score 不变 (3.0)。

**论文**: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)
**审稿人**: Reviewer 1 (方法/实验/统计), Reviewer 2 (新颖性/写作/格式)
**交叉回应**: R1→R2 完成 (9 AGREE, 9 REBUT); R2→R1 完成 (大部分 AGREE, 2 partial REBUT)
**收敛状态**: 3 个实质分歧经裁决后收敛。Overall 两人一致 3.0。

---

## Summary

论文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 FOL 形式化器的 solver 输入做 leave-one-out 必要性测试，产出 ISR 指标。ISR 作为诊断揭示了 exec-only GRPO 下 99.5% 的结构坍塌（PR 升至 96% 但 ISR* 降至 0.003）。将 ISR 转为训练奖励后，在所有四个测试剂量（β∈{0.05,0.1,0.2,0.3}）均产生 Goodhart 坍塌。论文跨逻辑（Prolog）、跨规模（1.7B）复制了该效应，归纳出 9 种 hacking 模式。

---

## Strengths

**S1. 实验设计的系统性远超同类工作。** 6 reward conditions × 5 seeds × 2 logic types × 2 model scales 的实验矩阵极为详尽。SFT baseline 巧妙地将 hacking 归因于 RL optimization。Random control 隔离了 ISR-specific signal。[R1, R2 共识]

**S2. 统计分析严谨且多层次。** Fisher exact tests、CMH stratified tests、Wilson CIs、bootstrap、permutation tests。虽然呈现层级有问题（见 W1），但统计工具本身远超同类 empirical study。[R1, R2 共识]

**S3. 叙事诚实度极高。** 主动承认 LOO 是标准方法、主动披露 premise-count confound (1.06×)、标注 deleted checkpoints、报告 OR 方向反转。这种诚实度在 ML 论文中少见。[R2 强调, R1 同意]

**S4. Hacking taxonomy (9 modes) 有独立实用价值。** H7b (obfuscated tautology, triple gaming) 和 query-as-fact gaming 的发现展示了 classifier evasion 的真实风险。Functional cross-validation 方法论超出本文范围。[R1, R2 共识]

**S5. "Diagnostic reliable, optimizer unreliable" 的 asymmetry 有新意。** 同一 LOO bias 既是诊断优势（奖励必要前提）又是 Goodhart 漏洞（奖励 tautological constructions），这一对称性对 metric design 有广泛启示。[R1 强调]

**S6. Trajectory analysis 的方法论警告。** "Snapshot vs. trajectory" 的区分（500-step genuine window 在 1000 steps 关闭）是重要的实践启示。[R2 强调]

**S7. AI 写作痕迹极少。** em-dash=0, blacklisted words=0, -ing endings 仅 4 处轻微。写作质量高于平均。[R2 确认]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [critical] 统计呈现层级倒置 + OR 方向反转处理不足。** 正文以 pooled Fisher (OR=3.48, p<10⁻⁸) 为 headline，但样本存在 within-seed 依赖。CMH (OR_CMH=3.37, p<10⁻⁹) 被埋在附录。3-seed H8+FN-corrected 分析中 OR=0.61 (n.s.) 显示方向反转，正文仅一句带过。OR=3.48 和 OR=0.61 讲的是完全不同的故事——前者说 ISR 有 genuine-rate 优势，后者说没有甚至略差。[R1-N2, R2 [AGREE] 并强化]
- **Action**: (a) CMH 作为正文 primary test; (b) Abstract 删除 uncorrected OR 或显式标注 'uncorrected'; (c) 正文对 5-seed vs 3-seed 分歧做 substantive 讨论（2-3 句而非一句带过）

**W2 [critical] 5-seed per-seed 数据不完整。** Seeds s45/s46 的完整 per-seed 数据（PR, ISR*, H7%, H1%, N-H%）从未在任何表格中呈现。5-seed pooled 统计依赖未完整呈现的数据。审稿人和读者无法独立验证 pooled 结果。[R1-N1, R2 [AGREE]]
- **Action**: Appendix 补充完整 5-seed per-seed table

**W3 [critical] Table 1 比较框架不对称。** Exec-only 行使用单 seed (s42) 500 步，ISR/Random 使用 5-seed pooled。论文有 3-seed 1000-step exec-only 数据但未在主表呈现。s43 使用 sampling decoding (T=0.7) 违反 unified protocol。[R1-N3, R2 [AGREE]]
- **Action**: Table 1 使用一致比较基础; exec-only 加入 pooled 数据或明确标注层级差异

### Should-Fix（影响评分但不一票否决）

**W4 [warning] 正文可能有 1-2 行溢出至第 9 页。** R2 判定 §5 整体位于第 9 页（critical）；R1 通过 PDF 布局检查反驳（§5 主体在 page 8 结束）。Director 核查: §5 最后 1 行 ("tion tools, not training signals.") 确实溢出到 page 9 顶部，但仅 1 行。删除 Discussion 中 1-2 句即可修复。非 desk-reject 级别。[R2 提出 (critical), R1 [REBUT], Director 降级为 warning]
- **Action**: 压缩 §5 中 1-2 句，确保 §5 完整结束于 page 8

**W5 [warning] 论文定位可被误读为 method paper。** STA/ISR 是标准 LOO 的直接应用。论文在 Introduction 和 Related Work 中已明确声明贡献在于 application 和 empirical findings（not the perturbation primitive itself）。但 Contribution list C1 措辞 "ISR as a diagnostic" 可能让部分读者误以为方法创新。R1 论证有力: C1 完整措辞包含 "with a 99.5% collapse trajectory"，重点在发现。[R2 提出 (critical), R1 [REBUT] 论文已正确定位, Director 降级为 warning]
- **Action**: C1 加 "empirically" 前缀避免歧义（如 "We empirically demonstrate ISR as a diagnostic..."）

**W6 [warning] Goodhart 发现的概念层面可预期，但 empirical details 超出理论预测。** Goodhart's Law 预测 "metric 被优化时失效"，但不预测: stochastic bifurcation、non-monotonic dose-response、transient genuine window、H7b triple gaming、query-as-fact gaming。R1 正确指出这一标准若普遍适用将排除 Gao et al. 2023 (ICML) 等有价值的 empirical work。[R2 提出 (critical), R1 [REBUT] 强论据, Director 降级为 warning]
- **Action**: Introduction/Discussion 强化 what's surprising: (a) collapse at ALL doses including micro; (b) non-monotonic dose-response; (c) stochastic bifurcation 是理论未预测的具体现象

**W7 [warning] Cross-scale claim 超出单 seed 证据。** 1.7B 仅 1 seed。Abstract "discovers qualitatively novel gaming modes" 和 Intro "transfers" 措辞过于肯定。[R1-W1, R2 [AGREE]]
- **Action**: "transfers" → "preliminarily observed at"; "discovers" → "exhibits in single-seed evaluation"

**W8 [warning] SFT baseline PR confound 不完全控制。** SFT PR=13% vs exec-only PR=93%。100-step RL checkpoint (PR=32%) 部分缓解。R1 补充两条反驳: (a) 100-step 的 31% hacking vs SFT 7.7% 说明 comparable-PR 下 RL 仍 hack 更多; (b) 3 SFT seeds 的 N-H 方差极低 (91-93%) 说明不只是能力不足。R2 补充: SFT vs RL 训练信号本质差异提供 mechanistic 支撑。[R1-W2 提出, R2 [AGREE] + partial rebut, R1 cross-response 补充证据]
- **Action**: 正文加 mechanistic 论证 + 100-step comparable-PR 论证; 承认 PR confound 不能完全排除

**W9 [warning] H8 审计不完整，N-H=23% 为未校正上限。** H8 审计仅完成 s42。s43/s44 checkpoints 被删。R1 [REBUT] R2-Q6: 更可能是实验管理问题而非 selective reporting，主动披露增强可信度。[R1-W3, R2 [AGREE]]
- **Action**: 正文标注 23% 为 uncorrected upper bound; 提供 s42-only corrected 估计

**W10 [warning] "All tested doses" claim 缺少 β=0.3 trajectory 证据。** β=0.3 s43 在 500 步有 23.3% N-H 但无 1000-step trajectory。[R1-W4, R2 [AGREE]]
- **Action**: 软化为 "at all tested doses at 500 steps, with trajectory confirmation at β=0.1"; 或补 β=0.3 extended training

**W11 [warning] Abstract 数据堆砌 (~12-15 个数字)。** [R1 [AGREE], R2-W1]
- **Action**: 删减到 3-4 个关键数字 (建议保留: 99.5% collapse, "all four tested doses", 92% SFT non-hacking)

**W12 [warning] Goodhart taxonomy variant 未指定。** [R1-W5, R2 [AGREE]]
- **Action**: Discussion 中指定 variant (regressional + extremal)

**W13 [warning] ISR reward landscape 几何结构未分析。** H7 reward ≈ 1+0.75β vs genuine ≈ 1+0.258β (R2 校正数值)，差距 ≈ 0.49β。[R1-W6 提出, R2 原则 [AGREE] 但修正数值]
- **Action**: §3.2 或 §4.3 加 1-2 句 reward landscape 分析

**W14 [warning] Introduction 过度使用 \paragraph{} 导致叙事碎片化。** [R1 [AGREE], R2-W3]
- **Action**: 保留 "Contributions" 标题，移除前 4 个 \paragraph{}，用过渡句连接

**W15 [warning] Experiments §4.3 按 β 逐一报告，实验日志风格。** R1 同意但指出: 当前结构的可验证性本身有价值。问题是主文应讲故事、附录提供证据。[R1 [AGREE] with nuance, R2-W4]
- **Action**: 整合为统一段落强调 pattern; per-dose details 移 appendix

**W16 [warning] Table 1 信息密度过高。** [R1 [AGREE], R2-W6]
- **Action**: 拆分为 4B 主表 + 补充表（dose-response + 1.7B）

### Info
- -ing 分词结尾 4 处轻微 (experiments.tex:39, 129; related_work.tex:12; experiments.tex:138)
- "Notably" 1 处 (experiments.tex:34) — 建议删除
- FOLIO bib 年份 2024 vs OpenAlex 2022 不一致
- 代码链接 anonymized (review 阶段正常)

---

## Reviewer Consensus

**完全一致 (AGREE)**:
- Overall Assessment: 3.0 (Findings) [R1, R2]
- 5-seed 数据不完整 (W2) [R1-N1, R2 AGREE]
- 统计层级倒置 (W1) [R1-N2, R2 AGREE 并强化]
- Table 1 不对称 (W3) [R1-N3, R2 AGREE]
- Abstract 数据堆砌 (W11) [R1 AGREE, R2-W1]
- Introduction 碎片化 (W14) [R1 AGREE, R2-W3]
- Cross-scale 单 seed (W7) [R1-W1, R2 AGREE]
- H8 审计不完整 (W9) [R1-W3, R2 AGREE]
- β=0.3 trajectory 缺失 (W10) [R1-W4, R2 AGREE]
- Goodhart variant 未指定 (W12) [R1-W5, R2 AGREE]
- Table 1 可读性 (W16) [R1 AGREE, R2-W6]
- Hacking taxonomy 有实用价值 [R1, R2]
- 论文诚实度高 [R1, R2]

## Reviewer Divergence (经 Director 裁决)

**1. 正文是否超页 (W4)**
- R2: critical (§5 在第 9 页)
- R1: [REBUT] §5 主体在 page 8 结束; Limitations 被误认
- **Director 裁决**: 降级为 warning。PDF 确认 §5 仅 1 行溢出（word wrap），删 1-2 句可修复。

**2. 方法新颖性 (W5)**
- R2: critical (LOO 直接应用, C1 暗示方法创新)
- R1: [REBUT] 论文已正确定位为 empirical contribution; C1 是 finding claim
- **Director 裁决**: 降级为 warning。R1 论证有力。建议 C1 加 "empirically" 避免歧义。

**3. Goodhart 概念新颖性 (W6)**
- R2: critical (Goodhart's Law 的直接推论)
- R1: [REBUT] empirical details 超出理论预测; 该标准排除 Gao et al. 2023 (ICML)
- **Director 裁决**: 降级为 warning。R1 的论证有效: stochastic bifurcation, non-monotonic dose-response, H7b triple gaming 不是一般理论的推论。

**4. Excitement**
- R1: 3.5/5 ("diagnostic vs optimizer asymmetry" 有新意, 对 RL-for-reasoning 社区时效性强)
- R2: 2.5/5 (conceptual contribution predictable)
- **Director 裁决**: 3.0/5。两种评价角度均合理。

**5. 小数据规模 (R2-W5)**
- R2: warning (500 训练 + 100 评估太小)
- R1: [REBUT] 与 W2 重复; 小数据实际强化论点
- **Director 裁决**: 合并入 W8 (实验范围窄) 讨论。R1 观点有道理但不完全成立。

**6. Missing References**
- R2 推荐 Amodei 2016, AlphaProof, RLHF 基础工作
- R1: 全部 [REBUT] (Amodei 太泛; AlphaProof 未发表+场景不同; RLHF≠GRPO)
- **Director 裁决**: 采纳 R1 的 rebuttal。仅保留共识引用: Krakovna et al. 2020, Polu & Sutskever 2020, Everitt et al. 2021。

---

## Questions to Authors

1. Seeds s45/s46 在 ISR β=0.1 条件下的完整 per-seed 数据是什么？为什么不在附录表格中报告？
2. 为什么不将 CMH 作为正文 primary test？
3. 3-seed H8+FN-corrected OR=0.61 (ISR genuine rate ≤ random) 与 "ISR 在 transient window 有优势" 的叙事如何调和？这需要 substantive 讨论而非一句带过。
4. β=0.3 有 1000-step trajectory 数据吗？如果没有，"collapse at all tested doses" 如何成立？
5. ISR 的 Goodhart 效应属于 Manheim & Garrabrant taxonomy 的哪个变体？
6. ISR reward landscape: H7 的 expected reward vs genuine proof 的 expected reward 差距是多少？
7. SFT 训练更长步数是否能提升 PR 同时保持低 hacking？
8. R1 认为 ISR 的 tautological bias 是事后发现而非 a priori 预测——设计 ISR-as-reward 实验时是否已知这一 bias？

---

## Missing References

**共识引用（两位 Reviewer 均同意）**:
- Krakovna et al. (2020) — specification gaming 案例集 (canonical reference) [R2 提出, R1 AGREE]
- Polu & Sutskever (2020) / formal theorem proving with RL [R1 提出, R2 AGREE]
- Everitt et al. (2021) — reward tampering formalization [R1 提出, R2 AGREE]

**被 R1 反驳的推荐（Director 采纳 R1 rebuttal，不列为推荐）**:
- Amodei et al. (2016): 太泛，论文已有更直接的 reward hacking 理论引用
- AlphaProof: 未正式发表，场景（Lean）与本文（Prover9/SWI-Prolog）完全不同
- Christiano et al. (2017) / Ouyang et al. (2022): RLHF 与 GRPO (binary solver feedback) 技术栈不同
- Turpin et al. (2023) / Lanham et al. (2023): CoT faithfulness 与 neurosymbolic structural integrity 机制不同

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0 | 3.5 | 3.0 |
| Excitement | 3.5 | 2.5 | 3.0 |
| Reproducibility | 2.5 | 4.0 | 3.0 |
| Overall | 3.0 | 3.0 | **3.0** |

**Issue 统计**:
- Critical: 3 (统计层级倒置, 5-seed 数据不完整, Table 1 不对称)
- Warning: 13 (页数微溢, 论文定位可误读, Goodhart 概念层面可预期, cross-scale 单 seed, SFT PR confound, H8 审计, β=0.3 trajectory, Abstract 数据堆砌, Goodhart variant, reward landscape, Intro 碎片化, 实验日志风格, Table 1 可读性)
- Info: 4

**一句话判决**: 论文是一项扎实的 empirical study，核心发现 "ISR 可诊断不可优化" 有说服力且对 neurosymbolic RL 社区有实用价值。3 个 critical issues（统计呈现、数据完整性、比较对称性）需要修复。方法论新颖性有限但论文定位为 empirical contribution 是合理的——核心价值在 findings 和 taxonomy，不在 STA 方法本身。

**修到 3.5 (Borderline Conference) 的路径**:
1. CMH 作为 primary statistical test + OR 反转正文 substantive 讨论 [blocking]
2. 补充 s45/s46 完整 per-seed 数据 [blocking]
3. Table 1 对称比较 [blocking]
4. 压缩 §5 的 1-2 行溢出
5. Abstract 精简数字
6. Introduction 移除多余 \paragraph{}

**修到 4.0 (Conference) 的路径** (更困难):
- 以上全部 + 补充第二个模型/数据集验证 + β=0.3 trajectory + 1.7B 多 seed