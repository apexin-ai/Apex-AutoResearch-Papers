---
round: 3
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T23:19:34.779441+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 3 审稿报告（修订版——整合双向交叉回应）

## Summary

本文研究 evidence-grounded document-level relation extraction 中训练方法对 relation extraction 与 evidence grounding 耦合度的影响。提出 RSFT（Rejection Sampling Fine-Tuning）+ CED scoring pipeline，在 Qwen2.5 (1.7B–14B) 和 LLaMA-3.1-8B 上系统比较 SFT/RSFT/GRPO/DPO 四种训练范式。核心发现：(1) evidence-grounded 训练引入可量化的 accuracy tax；(2) RSFT 维持 RE-evidence coupling 而 GRPO/DPO 产生 decoupling；(3) RSFT 降低 seed variance。论文定位为实证研究。

## Strengths

1. **系统性实验覆盖**：5 model scales × 4 训练范式 + cross-architecture (LLaMA) 验证。在 DocRE + evidence grounding 领域属于最全面的实证比较。

2. **Decoupling spectrum 概念有洞察力**：按 RE-evidence coupling 程度排列训练方法（SFT → RSFT → DPO → GRPO），为社区理解 multi-objective training dynamics 提供了有用的 conceptual framework。

3. **Evidence tax 量化分析**：将 evidence grounding 成本/收益分离为 training-time (+0.25±0.47pp) 和 inference-time (−5.63pp at matched tokens) 两个维度，quantification 有实用价值。

4. **Re-DocRED 测试集验证**：Table 9 所有 5 个 scale dev-test method ranking 完全一致（Spearman ρ=1.0），增强结论可靠性。

5. **充分的 ablation 设计**：random selection baseline、matched@2048 evaluation、no-evidence SFT、CED vs flat-NLI——实验设计思路严谨。

6. **统计方法意识**：χ² CI、Cohen's d、permutation test、partial correlation 等多层验证，虽然部分证据力度不足，但体现了正确的方法论方向。

## Weaknesses

### Must-Fix（两位 Reviewer 共识）

**[W-MF1] GRPO QLoRA vs bf16 存在多个未隔离的混淆变量**
- Table 3: QLoRA G=4 vs bf16 G=8 同时改变 quantization 和 group size
- R1 补充：effective input batch 也不同（QLoRA: batch=4×grad_accum=16=64 unique docs vs bf16: batch=8×grad_accum=4=32），影响 gradient estimation quality
- §4.3 "confirming quantization precision rather than group size as the primary factor" 缺乏任何控制实验
- **要求**：增加 bf16 G=4 或 QLoRA G=8 控制组；若不可行，将结论降级为 "quantization and/or group size and/or batch configuration"
- *[R1: Must-Fix, R2: AGREE]*

**[W-MF2] 方差压缩：统计不足 + Abstract cherry-picking + 方法论可比性问题**
- 统计：仅 1.7B χ² CI 不重叠；sign test p=0.0625 (>α=0.05)；4B Cohen's d=0.46 (small)
- Cherry-picking：Abstract 第三条 contribution 选择性报告 LLaMA d=2.58 和 1.7B non-overlapping CI
- **方法论核心问题**（R2 首提，R1 cross-response 确认为"最有价值的独特发现"）：§3.3 用单数 "the SFT model" 暗示所有 RSFT seed 从同一 SFT checkpoint 出发。若如此，SFT variance = LoRA init 全流程随机性，RSFT variance = 仅第二阶段微调随机性——比较的是不同层级的 variance，Contribution 3 在方法论上不成立
- **要求**：(1) 移除 variance 作为独立 contribution；(2) 明确说明 RSFT seed protocol（same vs different SFT checkpoint）；(3) 如果是 same checkpoint，必须在正文承认这一根本性限制
- *[R1: Must-Fix + cross-response 强化, R2: AGREE]*

**[W-MF3] 正文超 8 页 — EMNLP 2026 格式违规**
- §4.7 末尾和 §5 Conclusion 溢出至 page 9
- EMNLP 2026 strict 8-page limit（Limitations 不计入）
- R1 认为 MINOR（溢出 <0.2 页），R2 认为 MAJOR（desk reject）
- **Director 判定：Must-Fix** — 格式违规是二元的，无论溢出量多小
- *[R1: AGREE (minor severity), R2: AGREE (major severity)]*

**[W-MF4] Abstract 可能超过 200 words — EMNLP 2026 硬约束**
- Abstract 包含大量具体数字（-5.63pp, +0.25±0.47pp, Cohen's d=2.58, 4.7×等）
- 即使在 200±5 边界也应主动压缩，避免 desk reject
- *[R2: Must-Fix, R1: AGREE]*

### Should-Fix（两位 Reviewer 共识）

**[W-SF1] Implicit regularization 假说无法与 output constraint effect 区分**
- Evidence model 25.5k vs no-evidence 44.6k predictions (1.75×)，duplication 60.5%→33.0%
- 更简约解释：token budget constraint → fewer triples → fewer FP/duplicates
- R1 cross-response补充：Appendix K 证实 evidence quality unchanged (Δ<0.4pp)，"RSFT improves what model extracts but not how well it grounds"
- R2 补充：matched@2048 仍有 −5.63pp benefit，对纯 output constraint 解释构成部分挑战
- **要求**：区分讨论两种机制；或将 "implicit regularization" 改为更中性表述
- *[R1: Should-Fix, R2: AGREE with nuance]*

**[W-SF2] GRPO/DPO 超参数探索严重不足**
- DPO β=0.1: Rel-F1 从 44.39 暴跌至 33.37（−11pp）
- R1 补充：DPO 文献中 β=0.01-0.05 常用于避免过度偏离 reference policy
- Decoupling spectrum 结论建立在单一 β/KL 值上
- **要求**：β∈{0.01, 0.05, 0.5} sweep 或限定结论为 "under β=0.1"
- *[R1: Should-Fix, R2: 强烈 AGREE]*

**[W-SF3] 14B test-set reversal 解释不充分**
- 14B SFT truncation 50.6% vs RSFT 13.4%；test set 34.7 triples/doc vs dev 12.3
- 仅 1 SFT seed + 2 RSFT seeds，无法判断 reversal 是噪声还是系统性
- **要求**：precision/recall 分解 + 考虑增加 seeds
- *[R1: Should-Fix, R2: AGREE]*

**[W-SF4] RSFT "cannot exploit trade-off" 仅有逻辑推理，缺实证**
- §G 完全是 structural argument，无实验验证
- Single-objective RSFT 是 cheap 且 natural 的验证实验
- R2 提出 random RSFT baseline 应与 SFT s42 (39.74) 比较（+1.40pp），R1 AGREES
- **要求**：单目标 RSFT 实验或降级为 hypothesis
- *[R1: Should-Fix, R2: AGREE]*

**[W-SF5] EDCR ρ 数值跨节不一致（factual error）**
- §3.5: ρ=−0.89 (n=7, p=0.007)
- §4.7: ρ=−0.96 (n=7, p<0.001)
- Appendix L: ρ=−0.9643 (n=7)
- 三处声称相同 n=7 但给出不同 ρ 值。可能是不同聚合方式但未解释
- **要求**：统一或解释差异
- *[R2: raised, R1: cross-response AGREE "真实的数值不一致"]*

**[W-SF6] 贡献定位仍有 method-innovation 暗示语言**
- 三条 contribution 均为 empirical findings，但 "We formalize..."、"we propose EDCR" 暗示方法创新
- R1 认为 MAJOR（非 CRITICAL）——empirical studies 在 *ACL 有接收空间，framing 调整即可
- **要求**：移除剩余 method-innovation 措辞
- *[R2: Must-Fix(CRITICAL), R1: AGREE but downgrades to MAJOR]*

### Reviewer 分歧

**[W-DIV1] EDCR mechanical correlation 控制是否充分**
- **R1 (MAJOR)**：Cross-method FP drives both metrics; per-relation analysis from same docs not fully independent; wants partial correlation for per-relation precision
- **R2 (WARNING)**：Per-relation ρ=-0.79 (n=76, p<0.001) adequate; within-model relation types independently vary; permutation p<0.0001 sufficient
- **Director 判定：WARNING** — per-relation analysis 有效回避 cross-method concern；建议 per-relation precision partial correlation 作为 robustness check 但非必需

**[W-DIV2] 缺少 DocRED 官方 test set 评测**
- **R2 (Should-Fix)**：与先前工作可比性需要 CodaLab 提交
- **R1 (REBUT)**：CodaLab 不评估 evidence metrics，本文核心贡献在 evidence-extraction interaction；Re-DocRED annotation quality 更高；Table 9 已有完整 5-model comparison
- **Director 判定：Minor suggestion** — 为可比性可选报告 Ign-F1，但非必需

**[W-DIV3] Evidence tax 方向约定是否一致**
- **R2 (Minor)**：方向约定不一致，增加认知负担
- **R1 (REBUT)**：数学定义完全一致（Tax = no-evi − with-evi），所有位置相同。问题仅是 "negative tax" 命名不直觉
- **Director 判定：Cosmetic** — 非真正 inconsistency，但建议首次出现时明确引入 convention

### Minor Issues

| ID | 问题 | 共识 |
|---|---|---|
| M1 | Decoupling spectrum 仅 4B 验证 | AGREE — 加入 Limitations |
| M2 | SFT no-evidence 仅 s42 (1.7B/8B)；1.7B s42 是最强 seed | AGREE — 可能放大 tax benefit |
| M3 | CED template sensitivity + NLI model family | AGREE — 实际影响有限(0.02pp) |
| M4 | §4.5 BM25 k=2 未 justify | AGREE — 需要 k sensitivity 或 justify |
| M5 | Effective batch size 差异未讨论 | AGREE — GRPO 归因的额外 confound |
| M6 | RSFT 不改善 evidence quality (Appendix K Δ<0.4pp) — CED selection 可能主要是 extraction quality filtering | AGREE |
| M7 | bib key "chen2025docksrag" 实际第一作者可能是 Xu | 需验证 |

## Questions for Authors

1. RSFT seed protocol：每个 RSFT seed (s42/s43/s44/s45) 是从对应的 SFT seed checkpoint 出发，还是全部从同一个 SFT checkpoint 出发？这直接决定 Contribution 3 的方法论有效性。
2. 是否可提供 bf16 G=4 的 GRPO 结果以隔离 quantization effect？
3. Matched@2048 下 evidence model 仍获 −5.63pp benefit——如何与 "pure output constraint" 解释调和？有无表征层面的直接证据（attention pattern、hidden state）？
4. EDCR ρ 三个不同数值（−0.89, −0.96, −0.9643）分别用了什么聚合方法？
5. DPO 是否考虑过 β < 0.1？文献中 β=0.01-0.05 常见。
6. Abstract 确切字数是多少？

## Missing References

| 引用 | 理由 | 共识 |
|---|---|---|
| DeepSeek-R1 (DeepSeek, 2025) | GRPO 最成功应用案例，仅引 DeepSeekMath 不够 | R1 AGREE |
| ReST (Gulcehre et al., 2023) | Rejection sampling for LLM training 的重要工作，与 RSFT 直接相关 | R1 AGREE |

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 本轮未启用外部审稿。

## Visual Layout Check（非评分项）

**状态：已完成** (耗时 ~3 分钟)

| 严重性 | 位置 | 发现 |
|---|---|---|
| ⚠️ WARNING | p1-3 | 连续 3 页纯文本无 display item。Figure 1 直到 p4 才出现。审稿人第一印象偏"文字墙" |
| ⚠️ WARNING | p18 | Figure 10 红/绿/蓝三色对色盲不友好。建议 Okabe-Ito 或 hatching |
| ✅ | p4-8 | 结果区 display item 密度优秀，Figure/Table 紧跟首次引用 |
| ✅ | 全文 | booktabs 统一、无 overfull box、无 [?]、ACL 匿名格式正确 |

## Overall Assessment

**评分：3.5 — Borderline Conference**

| 维度 | 评分 | 说明 |
|---|---|---|
| Soundness | 3 | 核心实验设计合理但：GRPO 有 3 个 confounds 未隔离；variance claim 方法论有根本问题；统计证据多处不足 |
| Excitement | 3 | Decoupling spectrum 有启发性；empirical findings 有实用价值但非突破性；novelty 主要在实证范围而非方法论 |
| Reproducibility | 4 | 代码+数据承诺开源，hyperparameters 详尽，evaluation protocol 明确 |
| Clarity | 3 | 整体结构清晰，但：EDCR ρ 数值不一致(factual error)、page/abstract 超限、implicit regularization 命名误导、method-innovation 措辞残留 |
| Overall | 3.5 | Borderline Conference |

**置信度：4/5** — 两位 Reviewer 双向交叉验证完成，10/12 条共识，2 条分歧已裁定。

**推荐决定**：
- **当前状态 → Findings (3.0-3.5)**：格式违规(8页+abstract)加上统计薄弱点（variance claim）使论文在当前状态下更适合 Findings
- **修复 Must-Fix 后 → Conference (3.5-4.0)**：如果 (1) 修复格式、(2) GRPO confound 隔离或降级 claims、(3) variance contribution 移除或 protocol 澄清，论文可达 Conference 水平
- **关键不确定性**：RSFT seed protocol 的答案将决定 Contribution 3 是否可保留为降级版 observation

## Detailed Comments

### §1 Introduction
- Evidence tax 概念引入清晰，动机充分
- Contribution 3（variance）需移除或根本性重写——方法论可比性存疑
- "We formalize"、"we propose EDCR" 措辞暗示 method innovation，与 empirical study 定位矛盾

### §3 Method
- RSFT pipeline 描述完整；CED 正确定位为 scoring variant
- §3.3 需明确 RSFT seed protocol（"the SFT model" vs "each SFT seed's model"）
- CED hypothesis verbalization template 需讨论 sensitivity（即使实际影响有限）

### §4 Results
- Table 1 核心结果可信，cross-scale trend 清晰
- §4.2 variance：必须全面降级措辞 + 澄清 protocol
- §4.3 GRPO：移除 causal attribution 或增加控制实验（quantization × group size × batch size = 3 confounds）
- §4.5 BM25 k=2 缺 justification

### §5 Analysis (Decoupling Spectrum)
- 概念框架有价值但建于有限证据（single β × single scale）
- DPO degradation 可能是超参 artifact
- EDCR ρ 数值必须统一（-0.89 vs -0.96 vs -0.9643 同一 n=7）

### §6 Related Work
- DeepSeek-R1 和 ReST 需引用
- bib key "chen2025docksrag" 需验证第一作者

### Appendix
- Appendix K 的 "evidence quality unchanged" 发现与 "implicit regularization" framing 矛盾——需正文讨论
- §G "cannot exploit" 需实证补充或降级
- Figure 10 色盲问题（Appendix）

---

*本报告由 2 位 Reviewer 独立审稿 + 双向交叉回应后合成。两位 Reviewer 在 10/12 具体问题上达成共识，2 条分歧由 Director 裁定。Overall 评分一致：3.5 Borderline Conference。*