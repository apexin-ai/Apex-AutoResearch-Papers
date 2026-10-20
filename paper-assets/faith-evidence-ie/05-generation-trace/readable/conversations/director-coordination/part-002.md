# Director coordination — Part 2 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination.md) · [Structured JSON](../../../sessions/1e/1edf016a3b0527fcc112.json)

## Round 25

### Tool call

_source line 290 · 2026-05-24T23:19:34.745278+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 3 审稿报告（修订版——整合双向交叉回应）\n\n## Summary\n\n本文研究 evidence-grounded document-level relation extraction 中训练方法对 relation extraction 与 evidence grounding 耦合度的影响。提出 RSFT（Rejection Sampling Fine-Tuning）+ CED scoring pipeline，在 Qwen2.5 (1.7B–14B) 和 LLaMA-3.1-8B 上系统比较 SFT/RSFT/GRPO/DPO 四种训练范式。核心发现：(1) evidence-grounded 训练引入可量化的 accuracy tax；(2) RSFT 维持 RE-evidence coupling 而 GRPO/DPO 产生 decoupling；(3) RSFT 降低 seed variance。论文定位为实证研究。\n\n## Strengths\n\n1. **系统性实验覆盖**：5 model scales × 4 训练范式 + cross-architecture (LLaMA) 验证。在 DocRE + evidence grounding 领域属于最全面的实证比较。\n\n2. **Decoupling spectrum 概念有洞察力**：按 RE-evidence coupling 程度排列训练方法（SFT → RSFT → DPO → GRPO），为社区理解 multi-objective training dynamics 提供了有用的 conceptual framework。\n\n3. **Evidence tax 量化分析**：将 evidence grounding 成本/收益分离为 training-time (+0.25±0.47pp) 和 inference-time (−5.63pp at matched tokens) 两个维度，quantification 有实用价值。\n\n4. **Re-DocRED 测试集验证**：Table 9 所有 5 个 scale dev-test method ranking 完全一致（Spearman ρ=1.0），增强结论可靠性。\n\n5. **充分的 ablation 设计**：random selection baseline、matched@2048 evaluation、no-evidence SFT、CED vs flat-NLI——实验设计思路严谨。\n\n6. **统计方法意识**：χ² CI、Cohen's d、permutation test、partial correlation 等多层验证，虽然部分证据力度不足，但体现了正确的方法论方向。\n\n## Weaknesses\n\n### Must-Fix（两位 Reviewer 共识）\n\n**[W-MF1] GRPO QLoRA vs bf16 存在多个未隔离的混淆变量**\n- Table 3: QLoRA G=4 vs bf16 G=8 同时改变 quantization 和 group size\n- R1 补充：effective input batch 也不同（QLoRA: batch=4×grad_accum=16=64 unique docs vs bf16: batch=8×grad_accum=4=32），影响 gradient estimation quality\n- §4.3 \"confirming quantization precision rather than group size as the primary factor\" 缺乏任何控制实验\n- **要求**：增加 bf16 G=4 或 QLoRA G=8 控制组；若不可行，将结论降级为 \"quantization and/or group size and/or batch configuration\"\n- *[R1: Must-Fix, R2: AGREE]*\n\n**[W-MF2] 方差压缩：统计不足 + Abstract cherry-picking + 方法论可比性问题**\n- 统计：仅 1.7B χ² CI 不重叠；sign test p=0.0625 (>α=0.05)；4B Cohen's d=0.46 (small)\n- Cherry-picking：Abstract 第三条 contribution 选择性报告 LLaMA d=2.58 和 1.7B non-overlapping CI\n- **方法论核心问题**（R2 首提，R1 cross-response 确认为\"最有价值的独特发现\"）：§3.3 用单数 \"the SFT model\" 暗示所有 RSFT seed 从同一 SFT checkpoint 出发。若如此，SFT variance = LoRA init 全流程随机性，RSFT variance = 仅第二阶段微调随机性——比较的是不同层级的 variance，Contribution 3 在方法论上不成立\n- **要求**：(1) 移除 variance 作为独立 contribution；(2) 明确说明 RSFT seed protocol（same vs different SFT checkpoint）；(3) 如果是 same checkpoint，必须在正文承认这一根本性限制\n- *[R1: Must-Fix + cross-response 强化, R2: AGREE]*\n\n**[W-MF3] 正文超 8 页 — EMNLP 2026 格式违规**\n- §4.7 末尾和 §5 Conclusion 溢出至 page 9\n- EMNLP 2026 strict 8-page limit（Limitations 不计入）\n- R1 认为 MINOR（溢出 <0.2 页），R2 认为 MAJOR（desk reject）\n- **Director 判定：Must-Fix** — 格式违规是二元的，无论溢出量多小\n- *[R1: AGREE (minor severity), R2: AGREE (major severity)]*\n\n**[W-MF4] Abstract 可能超过 200 words — EMNLP 2026 硬约束**\n- Abstract 包含大量具体数字（-5.63pp, +0.25±0.47pp, Cohen's d=2.58, 4.7×等）\n- 即使在 200±5 边界也应主动压缩，避免 desk reject\n- *[R2: Must-Fix, R1: AGREE]*\n\n### Should-Fix（两位 Reviewer 共识）\n\n**[W-SF1] Implicit regularization 假说无法与 output constraint effect 区分**\n- Evidence model 25.5k vs no-evidence 44.6k predictions (1.75×)，duplication 60.5%→33.0%\n- 更简约解释：token budget constraint → fewer triples → fewer FP/duplicates\n- R1 cross-response补充：Appendix K 证实 evidence quality unchanged (Δ<0.4pp)，\"RSFT improves what model extracts but not how well it grounds\"\n- R2 补充：matched@2048 仍有 −5.63pp benefit，对纯 output constraint 解释构成部分挑战\n- **要求**：区分讨论两种机制；或将 \"implicit regularization\" 改为更中性表述\n- *[R1: Should-Fix, R2: AGREE with nuance]*\n\n**[W-SF2] GRPO/DPO 超参数探索严重不足**\n- DPO β=0.1: Rel-F1 从 44.39 暴跌至 33.37（−11pp）\n- R1 补充：DPO 文献中 β=0.01-0.05 常用于避免过度偏离 reference policy\n- Decoupling spectrum 结论建立在单一 β/KL 值上\n- **要求**：β∈{0.01, 0.05, 0.5} sweep 或限定结论为 \"under β=0.1\"\n- *[R1: Should-Fix, R2: 强烈 AGREE]*\n\n**[W-SF3] 14B test-set reversal 解释不充分**\n- 14B SFT truncation 50.6% vs RSFT 13.4%；test set 34.7 triples/doc vs dev 12.3\n- 仅 1 SFT seed + 2 RSFT seeds，无法判断 reversal 是噪声还是系统性\n- **要求**：precision/recall 分解 + 考虑增加 seeds\n- *[R1: Should-Fix, R2: AGREE]*\n\n**[W-SF4] RSFT \"cannot exploit trade-off\" 仅有逻辑推理，缺实证**\n- §G 完全是 structural argument，无实验验证\n- Single-objective RSFT 是 cheap 且 natural 的验证实验\n- R2 提出 random RSFT baseline 应与 SFT s42 (39.74) 比较（+1.40pp），R1 AGREES\n- **要求**：单目标 RSFT 实验或降级为 hypothesis\n- *[R1: Should-Fix, R2: AGREE]*\n\n**[W-SF5] EDCR ρ 数值跨节不一致（factual error）**\n- §3.5: ρ=−0.89 (n=7, p=0.007)\n- §4.7: ρ=−0.96 (n=7, p<0.001)\n- Appendix L: ρ=−0.9643 (n=7)\n- 三处声称相同 n=7 但给出不同 ρ 值。可能是不同聚合方式但未解释\n- **要求**：统一或解释差异\n- *[R2: raised, R1: cross-response AGREE \"真实的数值不一致\"]*\n\n**[W-SF6] 贡献定位仍有 method-innovation 暗示语言**\n- 三条 contribution 均为 empirical findings，但 \"We formalize...\"、\"we propose EDCR\" 暗示方法创新\n- R1 认为 MAJOR（非 CRITICAL）——empirical studies 在 *ACL 有接收空间，framing 调整即可\n- **要求**：移除剩余 method-innovation 措辞\n- *[R2: Must-Fix(CRITICAL), R1: AGREE but downgrades to MAJOR]*\n\n### Reviewer 分歧\n\n**[W-DIV1] EDCR mechanical correlation 控制是否充分**\n- **R1 (MAJOR)**：Cross-method FP drives both metrics; per-relation analysis from same docs not fully independent; wants partial correlation for per-relation precision\n- **R2 (WARNING)**：Per-relation ρ=-0.79 (n=76, p<0.001) adequate; within-model relation types independently vary; permutation p<0.0001 sufficient\n- **Director 判定：WARNING** — per-relation analysis 有效回避 cross-method concern；建议 per-relation precision partial correlation 作为 robustness check 但非必需\n\n**[W-DIV2] 缺少 DocRED 官方 test set 评测**\n- **R2 (Should-Fix)**：与先前工作可比性需要 CodaLab 提交\n- **R1 (REBUT)**：CodaLab 不评估 evidence metrics，本文核心贡献在 evidence-extraction interaction；Re-DocRED annotation quality 更高；Table 9 已有完整 5-model comparison\n- **Director 判定：Minor suggestion** — 为可比性可选报告 Ign-F1，但非必需\n\n**[W-DIV3] Evidence tax 方向约定是否一致**\n- **R2 (Minor)**：方向约定不一致，增加认知负担\n- **R1 (REBUT)**：数学定义完全一致（Tax = no-evi − with-evi），所有位置相同。问题仅是 \"negative tax\" 命名不直觉\n- **Director 判定：Cosmetic** — 非真正 inconsistency，但建议首次出现时明确引入 convention\n\n### Minor Issues\n\n| ID | 问题 | 共识 |\n|---|---|---|\n| M1 | Decoupling spectrum 仅 4B 验证 | AGREE — 加入 Limitations |\n| M2 | SFT no-evidence 仅 s42 (1.7B/8B)；1.7B s42 是最强 seed | AGREE — 可能放大 tax benefit |\n| M3 | CED template sensitivity + NLI model family | AGREE — 实际影响有限(0.02pp) |\n| M4 | §4.5 BM25 k=2 未 justify | AGREE — 需要 k sensitivity 或 justify |\n| M5 | Effective batch size 差异未讨论 | AGREE — GRPO 归因的额外 confound |\n| M6 | RSFT 不改善 evidence quality (Appendix K Δ<0.4pp) — CED selection 可能主要是 extraction quality filtering | AGREE |\n| M7 | bib key \"chen2025docksrag\" 实际第一作者可能是 Xu | 需验证 |\n\n## Questions for Authors\n\n1. RSFT seed protocol：每个 RSFT seed (s42/s43/s44/s45) 是从对应的 SFT seed checkpoint 出发，还是全部从同一个 SFT checkpoint 出发？这直接决定 Contribution 3 的方法论有效性。\n2. 是否可提供 bf16 G=4 的 GRPO 结果以隔离 quantization effect？\n3. Matched@2048 下 evidence model 仍获 −5.63pp benefit——如何与 \"pure output constraint\" 解释调和？有无表征层面的直接证据（attention pattern、hidden state）？\n4. EDCR ρ 三个不同数值（−0.89, −0.96, −0.9643）分别用了什么聚合方法？\n5. DPO 是否考虑过 β < 0.1？文献中 β=0.01-0.05 常见。\n6. Abstract 确切字数是多少？\n\n## Missing References\n\n| 引用 | 理由 | 共识 |\n|---|---|---|\n| DeepSeek-R1 (DeepSeek, 2025) | GRPO 最成功应用案例，仅引 DeepSeekMath 不够 | R1 AGREE |\n| ReST (Gulcehre et al., 2023) | Rejection sampling for LLM training 的重要工作，与 RSFT 直接相关 | R1 AGREE |\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未启用外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~3 分钟)\n\n| 严重性 | 位置 | 发现 |\n|---|---|---|\n| ⚠️ WARNING | p1-3 | 连续 3 页纯文本无 display item。Figure 1 直到 p4 才出现。审稿人第一印象偏\"文字墙\" |\n| ⚠️ WARNING | p18 | Figure 10 红/绿/蓝三色对色盲不友好。建议 Okabe-Ito 或 hatching |\n| ✅ | p4-8 | 结果区 display item 密度优秀，Figure/Table 紧跟首次引用 |\n| ✅ | 全文 | booktabs 统一、无 overfull box、无 [?]、ACL 匿名格式正确 |\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | 评分 | 说明 |\n|---|---|---|\n| Soundness | 3 | 核心实验设计合理但：GRPO 有 3 个 confounds 未隔离；variance claim 方法论有根本问题；统计证据多处不足 |\n| Excitement | 3 | Decoupling spectrum 有启发性；empirical findings 有实用价值但非突破性；novelty 主要在实证范围而非方法论 |\n| Reproducibility | 4 | 代码+数据承诺开源，hyperparameters 详尽，evaluation protocol 明确 |\n| Clarity | 3 | 整体结构清晰，但：EDCR ρ 数值不一致(factual error)、page/abstract 超限、implicit regularization 命名误导、method-innovation 措辞残留 |\n| Overall | 3.5 | Borderline Conference |\n\n**置信度：4/5** — 两位 Reviewer 双向交叉验证完成，10/12 条共识，2 条分歧已裁定。\n\n**推荐决定**：\n- **当前状态 → Findings (3.0-3.5)**：格式违规(8页+abstract)加上统计薄弱点（variance claim）使论文在当前状态下更适合 Findings\n- **修复 Must-Fix 后 → Conference (3.5-4.0)**：如果 (1) 修复格式、(2) GRPO confound 隔离或降级 claims、(3) variance contribution 移除或 protocol 澄清，论文可达 Conference 水平\n- **关键不确定性**：RSFT seed protocol 的答案将决定 Contribution 3 是否可保留为降级版 observation\n\n## Detailed Comments\n\n### §1 Introduction\n- Evidence tax 概念引入清晰，动机充分\n- Contribution 3（variance）需移除或根本性重写——方法论可比性存疑\n- \"We formalize\"、\"we propose EDCR\" 措辞暗示 method innovation，与 empirical study 定位矛盾\n\n### §3 Method\n- RSFT pipeline 描述完整；CED 正确定位为 scoring variant\n- §3.3 需明确 RSFT seed protocol（\"the SFT model\" vs \"each SFT seed's model\"）\n- CED hypothesis verbalization template 需讨论 sensitivity（即使实际影响有限）\n\n### §4 Results\n- Table 1 核心结果可信，cross-scale trend 清晰\n- §4.2 variance：必须全面降级措辞 + 澄清 protocol\n- §4.3 GRPO：移除 causal attribution 或增加控制实验（quantization × group size × batch size = 3 confounds）\n- §4.5 BM25 k=2 缺 justification\n\n### §5 Analysis (Decoupling Spectrum)\n- 概念框架有价值但建于有限证据（single β × single scale）\n- DPO degradation 可能是超参 artifact\n- EDCR ρ 数值必须统一（-0.89 vs -0.96 vs -0.9643 同一 n=7）\n\n### §6 Related Work\n- DeepSeek-R1 和 ReST 需引用\n- bib key \"chen2025docksrag\" 需验证第一作者\n\n### Appendix\n- Appendix K 的 \"evidence quality unchanged\" 发现与 \"implicit regularization\" framing 矛盾——需正文讨论\n- §G \"cannot exploit\" 需实证补充或降级\n- Figure 10 色盲问题（Appendix）\n\n---\n\n*本报告由 2 位 Reviewer 独立审稿 + 双向交叉回应后合成。两位 Reviewer 在 10/12 具体问题上达成共识，2 条分歧由 Director 裁定。Overall 评分一致：3.5 Borderline Conference。*",
  "project": "faith-evidence-ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 3 审稿报告（修订版——整合双向交叉回应）\n\n## Summary\n\n本文研究 evidence-grounded document-level relation extraction 中训练方法对 relation extraction 与 evidence grounding 耦合度的影响。提出 RSFT（Rejection Sampling Fine-Tuning）+ CED scoring pipeline，在 Qwen2.5 (1.7B–14B) 和 LLaMA-3.1-8B 上系统比较 SFT/RSFT/GRPO/DPO 四种训练范式。核心发现：(1) evidence-grounded 训练引入可量化的 accuracy tax；(2) RSFT 维持 RE-evidence coupling 而 GRPO/DPO 产生 decoupling；(3) RSFT 降低 seed variance。论文定位为实证研究。\n\n## Strengths\n\n1. **系统性实验覆盖**：5 model scales × 4 训练范式 + cross-architecture (LLaMA) 验证。在 DocRE + evidence grounding 领域属于最全面的实证比较。\n\n2. **Decoupling spectrum 概念有洞察力**：按 RE-evidence coupling 程度排列训练方法（SFT → RSFT → DPO → GRPO），为社区理解 multi-objective training dynamics 提供了有用的 conceptual framework。\n\n3. **Evidence tax 量化分析**：将 evidence grounding 成本/收益分离为 training-time (+0.25±0.47pp) 和 inference-time (−5.63pp at matched tokens) 两个维度，quantification 有实用价值。\n\n4. **Re-DocRED 测试集验证**：Table 9 所有 5 个 scale dev-test method ranking 完全一致（Spearman ρ=1.0），增强结论可靠性。\n\n5. **充分的 ablation 设计**：random selection baseline、matched@2048 evaluation、no-evidence SFT、CED vs flat-NLI——实验设计思路严谨。\n\n6. **统计方法意识**：χ² CI、Cohen's d、permutation test、partial correlation 等多层验证，虽然部分证据力度不足，但体现了正确的方法论方向。\n\n## Weaknesses\n\n### Must-Fix（两位 Reviewer 共识）\n\n**[W-MF1] GRPO QLoRA vs bf16 存在多个未隔离的混淆变量**\n- Table 3: QLoRA G=4 vs bf16 G=8 同时改变 quantization 和 group size\n- R1 补充：effective input batch 也不同（QLoRA: batch=4×grad_accum=16=64 unique docs vs bf16: batch=8×grad_accum=4=32），影响 gradient estimation quality\n- §4.3 \"confirming quantization precision rather than group size as the primary factor\" 缺乏任何控制实验\n- **要求**：增加 bf16 G=4 或 QLoRA G=8 控制组；若不可行，将结论降级为 \"quantization and/or group size and/or batch configuration\"\n- *[R1: Must-Fix, R2: AGREE]*\n\n**[W-MF2] 方差压缩：统计不足 + Abstract cherry-picking + 方法论可比性问题**\n- 统计：仅 1.7B χ² CI 不重叠；sign test p=0.0625 (>α=0.05)；4B Cohen's d=0.46 (small)\n- Cherry-picking：Abstract 第三条 contribution 选择性报告 LLaMA d=2.58 和 1.7B non-overlapping CI\n- **方法论核心问题**（R2 首提，R1 cross-response 确认为\"最有价值的独特发现\"）：§3.3 用单数 \"the SFT model\" 暗示所有 RSFT seed 从同一 SFT checkpoint 出发。若如此，SFT variance = LoRA init 全流程随机性，RSFT variance = 仅第二阶段微调随机性——比较的是不同层级的 variance，Contribution 3 在方法论上不成立\n- **要求**：(1) 移除 variance 作为独立 contribution；(2) 明确说明 RSFT seed protocol（same vs different SFT checkpoint）；(3) 如果是 same checkpoint，必须在正文承认这一根本性限制\n- *[R1: Must-Fix + cross-response 强化, R2: AGREE]*\n\n**[W-MF3] 正文超 8 页 — EMNLP 2026 格式违规**\n- §4.7 末尾和 §5 Conclusion 溢出至 page 9\n- EMNLP 2026 strict 8-page limit（Limitations 不计入）\n- R1 认为 MINOR（溢出 <0.2 页），R2 认为 MAJOR（desk reject）\n- **Director 判定：Must-Fix** — 格式违规是二元的，无论溢出量多小\n- *[R1: AGREE (minor severity), R2: AGREE (major severity)]*\n\n**[W-MF4] Abstract 可能超过 200 words — EMNLP 2026 硬约束**\n- Abstract 包含大量具体数字（-5.63pp, +0.25±0.47pp, Cohen's d=2.58, 4.7×等）\n- 即使在 200±5 边界也应主动压缩，避免 desk reject\n- *[R2: Must-Fix, R1: AGREE]*\n\n### Should-Fix（两位 Reviewer 共识）\n\n**[W-SF1] Implicit regularization 假说无法与 output constraint effect 区分**\n- Evidence model 25.5k vs no-evidence 44.6k predictions (1.75×)，duplication 60.5%→33.0%\n- 更简约解释：token budget constraint → fewer triples → fewer FP/duplicates\n- R1 cross-response补充：Appendix K 证实 evidence quality unchanged (Δ<0.4pp)，\"RSFT improves what model extracts but not how well it grounds\"\n- R2 补充：matched@2048 仍有 −5.63pp benefit，对纯 output constraint 解释构成部分挑战\n- **要求**：区分讨论两种机制；或将 \"implicit regularization\" 改为更中性表述\n- *[R1: Should-Fix, R2: AGREE with nuance]*\n\n**[W-SF2] GRPO/DPO 超参数探索严重不足**\n- DPO β=0.1: Rel-F1 从 44.39 暴跌至 33.37（−11pp）\n- R1 补充：DPO 文献中 β=0.01-0.05 常用于避免过度偏离 reference policy\n- Decoupling spectrum 结论建立在单一 β/KL 值上\n- **要求**：β∈{0.01, 0.05, 0.5} sweep 或限定结论为 \"under β=0.1\"\n- *[R1: Should-Fix, R2: 强烈 AGREE]*\n\n**[W-SF3] 14B test-set reversal 解释不充分**\n- 14B SFT truncation 50.6% vs RSFT 13.4%；test set 34.7 triples/doc vs dev 12.3\n- 仅 1 SFT seed + 2 RSFT seeds，无法判断 reversal 是噪声还是系统性\n- **要求**：precision/recall 分解 + 考虑增加 seeds\n- *[R1: Should-Fix, R2: AGREE]*\n\n**[W-SF4] RSFT \"cannot exploit trade-off\" 仅有逻辑推理，缺实证**\n- §G 完全是 structural argument，无实验验证\n- Single-objective RSFT 是 cheap 且 natural 的验证实验\n- R2 提出 random RSFT baseline 应与 SFT s42 (39.74) 比较（+1.40pp），R1 AGREES\n- **要求**：单目标 RSFT 实验或降级为 hypothesis\n- *[R1: Should-Fix, R2: AGREE]*\n\n**[W-SF5] EDCR ρ 数值跨节不一致（factual error）**\n- §3.5: ρ=−0.89 (n=7, p=0.007)\n- §4.7: ρ=−0.96 (n=7, p<0.001)\n- Appendix L: ρ=−0.9643 (n=7)\n- 三处声称相同 n=7 但给出不同 ρ 值。可能是不同聚合方式但未解释\n- **要求**：统一或解释差异\n- *[R2: raised, R1: cross-response AGREE \"真实的数值不一致\"]*\n\n**[W-SF6] 贡献定位仍有 method-innovation 暗示语言**\n- 三条 contribution 均为 empirical findings，但 \"We formalize...\"、\"we propose EDCR\" 暗示方法创新\n- R1 认为 MAJOR（非 CRITICAL）——empirical studies 在 *ACL 有接收空间，framing 调整即可\n- **要求**：移除剩余 method-innovation 措辞\n- *[R2: Must-Fix(CRITICAL), R1: AGREE but downgrades to MAJOR]*\n\n### Reviewer 分歧\n\n**[W-DIV1] EDCR mechanical correlation 控制是否充分**\n- **R1 (MAJOR)**：Cross-method FP drives both metrics; per-relation analysis from same docs not fully independent; wants partial correlation for per-relation precision\n- **R2 (WARNING)**：Per-relation ρ=-0.79 (n=76, p<0.001) adequate; within-model relation types independently vary; permutation p<0.0001 sufficient\n- **Director 判定：WARNING** — per-relation analysis 有效回避 cross-method concern；建议 per-relation precision partial correlation 作为 robustness check 但非必需\n\n**[W-DIV2] 缺少 DocRED 官方 test set 评测**\n- **R2 (Should-Fix)**：与先前工作可比性需要 CodaLab 提交\n- **R1 (REBUT)**：CodaLab 不评估 evidence metrics，本文核心贡献在 evidence-extraction interaction；Re-DocRED annotation quality 更高；Table 9 已有完整 5-model comparison\n- **Director 判定：Minor suggestion** — 为可比性可选报告 Ign-F1，但非必需\n\n**[W-DIV3] Evidence tax 方向约定是否一致**\n- **R2 (Minor)**：方向约定不一致，增加认知负担\n- **R1 (REBUT)**：数学定义完全一致（Tax = no-evi − with-evi），所有位置相同。问题仅是 \"negative tax\" 命名不直觉\n- **Director 判定：Cosmetic** — 非真正 inconsistency，但建议首次出现时明确引入 convention\n\n### Minor Issues\n\n| ID | 问题 | 共识 |\n|---|---|---|\n| M1 | Decoupling spectrum 仅 4B 验证 | AGREE — 加入 Limitations |\n| M2 | SFT no-evidence 仅 s42 (1.7B/8B)；1.7B s42 是最强 seed | AGREE — 可能放大 tax benefit |\n| M3 | CED template sensitivity + NLI model family | AGREE — 实际影响有限(0.02pp) |\n| M4 | §4.5 BM25 k=2 未 justify | AGREE — 需要 k sensitivity 或 justify |\n| M5 | Effective batch size 差异未讨论 | AGREE — GRPO 归因的额外 confound |\n| M6 | RSFT 不改善 evidence quality (Appendix K Δ<0.4pp) — CED selection 可能主要是 extraction quality filtering | AGREE |\n| M7 | bib key \"chen2025docksrag\" 实际第一作者可能是 Xu | 需验证 |\n\n## Questions for Authors\n\n1. RSFT seed protocol：每个 RSFT seed (s42/s43/s44/s45) 是从对应的 SFT seed checkpoint 出发，还是全部从同一个 SFT checkpoint 出发？这直接决定 Contribution 3 的方法论有效性。\n2. 是否可提供 bf16 G=4 的 GRPO 结果以隔离 quantization effect？\n3. Matched@2048 下 evidence model 仍获 −5.63pp benefit——如何与 \"pure output constraint\" 解释调和？有无表征层面的直接证据（attention pattern、hidden state）？\n4. EDCR ρ 三个不同数值（−0.89, −0.96, −0.9643）分别用了什么聚合方法？\n5. DPO 是否考虑过 β < 0.1？文献中 β=0.01-0.05 常见。\n6. Abstract 确切字数是多少？\n\n## Missing References\n\n| 引用 | 理由 | 共识 |\n|---|---|---|\n| DeepSeek-R1 (DeepSeek, 2025) | GRPO 最成功应用案例，仅引 DeepSeekMath 不够 | R1 AGREE |\n| ReST (Gulcehre et al., 2023) | Rejection sampling for LLM training 的重要工作，与 RSFT 直接相关 | R1 AGREE |\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未启用外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~3 分钟)\n\n| 严重性 | 位置 | 发现 |\n|---|---|---|\n| ⚠️ WARNING | p1-3 | 连续 3 页纯文本无 display item。Figure 1 直到 p4 才出现。审稿人第一印象偏\"文字墙\" |\n| ⚠️ WARNING | p18 | Figure 10 红/绿/蓝三色对色盲不友好。建议 Okabe-Ito 或 hatching |\n| ✅ | p4-8 | 结果区 display item 密度优秀，Figure/Table 紧跟首次引用 |\n| ✅ | 全文 | booktabs 统一、无 overfull box、无 [?]、ACL 匿名格式正确 |\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | 评分 | 说明 |\n|---|---|---|\n| Soundness | 3 | 核心实验设计合理但：GRPO 有 3 个 confounds 未隔离；variance claim 方法论有根本问题；统计证据多处不足 |\n| Excitement | 3 | Decoupling spectrum 有启发性；empirical findings 有实用价值但非突破性；novelty 主要在实证范围而非方法论 |\n| Reproducibility | 4 | 代码+数据承诺开源，hyperparameters 详尽，evaluation protocol 明确 |\n| Clarity | 3 | 整体结构清晰，但：EDCR ρ 数值不一致(factual error)、page/abstract 超限、implicit regularization 命名误导、method-innovation 措辞残留 |\n| Overall | 3.5 | Borderline Conference |\n\n**置信度：4/5** — 两位 Reviewer 双向交叉验证完成，10/12 条共识，2 条分歧已裁定。\n\n**推荐决定**：\n- **当前状态 → Findings (3.0-3.5)**：格式违规(8页+abstract)加上统计薄弱点（variance claim）使论文在当前状态下更适合 Findings\n- **修复 Must-Fix 后 → Conference (3.5-4.0)**：如果 (1) 修复格式、(2) GRPO confound 隔离或降级 claims、(3) variance contribution 移除或 protocol 澄清，论文可达 Conference 水平\n- **关键不确定性**：RSFT seed protocol 的答案将决定 Contribution 3 是否可保留为降级版 observation\n\n## Detailed Comments\n\n### §1 Introduction\n- Evidence tax 概念引入清晰，动机充分\n- Contribution 3（variance）需移除或根本性重写——方法论可比性存疑\n- \"We formalize\"、\"we propose EDCR\" 措辞暗示 method innovation，与 empirical study 定位矛盾\n\n### §3 Method\n- RSFT pipeline 描述完整；CED 正确定位为 scoring variant\n- §3.3 需明确 RSFT seed protocol（\"the SFT model\" vs \"each SFT seed's model\"）\n- CED hypothesis verbalization template 需讨论 sensitivity（即使实际影响有限）\n\n### §4 Results\n- Table 1 核心结果可信，cross-scale trend 清晰\n- §4.2 variance：必须全面降级措辞 + 澄清 protocol\n- §4.3 GRPO：移除 causal attribution 或增加控制实验（quantization × group size × batch size = 3 confounds）\n- §4.5 BM25 k=2 缺 justification\n\n### §5 Analysis (Decoupling Spectrum)\n- 概念框架有价值但建于有限证据（single β × single scale）\n- DPO degradation 可能是超参 artifact\n- EDCR ρ 数值必须统一（-0.89 vs -0.96 vs -0.9643 同一 n=7）\n\n### §6 Related Work\n- DeepSeek-R1 和 ReST 需引用\n- bib key \"chen2025docksrag\" 需验证第一作者\n\n### Appendix\n- Appendix K 的 \"evidence quality unchanged\" 发现与 \"implicit regularization\" framing 矛盾——需正文讨论\n- §G \"cannot exploit\" 需实证补充或降级\n- Figure 10 色盲问题（Appendix）\n\n---\n\n*本报告由 2 位 Reviewer 独立审稿 + 双向交叉回应后合成。两位 Reviewer 在 10/12 具体问题上达成共识，2 条分歧由 Director 裁定。Overall 评分一致：3.5 Borderline Conference。*",
    "project": "faith-evidence-ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-24T23:19:39.194581+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_84537e1e2f9ef71a90742c2db859c6f2:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4449
}
```

</details>

---


### Assistant

_source line 292 · 2026-05-24T23:19:48.823310+00:00_

Round 3 审稿报告已重新提交（整合双向交叉回应）。

**本轮审稿完成总结：**

- **评分**：3.5 Borderline Conference（两位 Reviewer 一致）
- **Must-Fix 4 项**：GRPO confound 隔离、variance claim 方法论问题+cherry-picking、正文超 8 页、Abstract 可能超 200 words
- **Should-Fix 6 项**：implicit regularization 命名、DPO/GRPO 超参sweep、14B reversal、RSFT trade-off 实证、EDCR ρ 数值不一致、novelty 措辞残留
- **分歧 3 项（已裁定）**：EDCR severity (→WARNING)、DocRED test (→minor suggestion)、tax convention (→cosmetic)
- **新增关键发现**：R1 确认 R2 提出的 RSFT variance comparability 问题为 "最有价值的独特贡献"——若 RSFT 从同一 SFT checkpoint 出发，Contribution 3 方法论不成立

报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 26

## Round 26

68 recorded events


### User

_source line 293 · 2026-05-25T22:28:00.618204+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: faith-evidence-ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-06-15
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-25T22:28:05.901430+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-25T22:28:06.002799+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-25T22:28:15.691760+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-25T22:28:15.692250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-25T22:28:20.812721+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-25T22:28:21.766393+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 300 · 2026-05-25T22:28:23.071856+00:00_

{"result":"# 项目 faith-evidence-ie 概况\n\n## 实验状态 (382 个)\n\n- **mvp2_eval_lr5e6_r1_ckpt20**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_step90**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_step100**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_ckpt10**: DONE (success) — \n- **mvp2_eval_ced_kl001_r4_early**: DONE (negative) — \n- **mvp2_grpo_flatnli_r6**: DONE (negative) — \n- **mvp2_grpo_ced_kl001_r4**: DONE (success) — \n- **mvp2_sft_eval_r3**: DONE (success) — \n- **mvp2_grpo_extract_r3**: DONE (negative) — \n- **mvp2_grpo_ced_r5**: DONE (negative) — \n- **mvp2_sft_eval_r2**: DONE (success) — \n- **precompute_nli_train**: DONE (success) — \n- **mvp2_sft_warmup**: DONE (success) — \n- **smoke_test_grpo**: DONE (success) — \n- **mvp1_ced_signal**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-25T15:49:38Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 358 个实验 — DONE 355, PREPARING 3\n**DONE 分布**: failed 62, killed 36, negative 19, success 238\n\n### GPU 占用\n- **分配**: 4 张 — rtx5090-4x:cuda:0, rtx5090-4x:cuda:1, rtx5090-4x:cuda:2, rtx5090-4x:cuda:3\n- **空闲（分配了没跑）**: rtx5090-4x:cuda:0, rtx5090-4x:cuda:1, rtx5090-4x:cuda:2, rtx5090-4x:cuda:3\n\n### 💾 磁盘余量\n- **rtx5090-4x**:\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 815G/879G 可用（已用 3%）\n- **bjb2-12179**:\n  - `/autodl-pub`: 9.2T/14T 可用（已用 35%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `d158_14b_rsft_s44_test_with_evi` [success] — 2026-05-25T10:56:00\n- `test_eval_1_7b_rsft_s44_with_evi` [success] — 2026-05-25T09:19:07\n- `d158_14b_rsft_s44_train` [success] — 2026-05-25T09:01:27\n- `test_eval_1_7b_rsft_s44_no_evi` [success] — 2026-05-25T05:37:52\n- `d158_14b_rsft_s44_ced_score` [success] — 2026-05-25T05:10:52 — HF_HOME 未设置，transformers 无法找到本地缓存的 cross-encoder/nli-deberta-v3-base 模型，网络不通无法下载\n\n<!-- AUTO-FACTS-END --
…[truncated 2549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2259
}
```

</details>

---


### Tool call

_source line 301 · 2026-05-25T22:28:23.624277+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-25T22:28:24.126558+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{xcolor}
16	\usepackage{multirow}
17	\usepackage{subcaption}
18	\usepackage{enumitem}
19	\usepackage{url}
20	
21	\graphicspath{{../../figures/paper/}}
22	
23	\title{Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{sections/abstract}
31	\input{sections/introduction}
32	\input{sections/related_work}
33	\input{sections/method}
34	\input{sections/experiments}
35	\input{sections/conclusion}
36	\input{sections/limitations}
37	
38	\bibliography{references}
39	
40	\appendix
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 303 · 2026-05-25T22:28:24.227443+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 304 · 2026-05-25T22:28:24.278164+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-25T22:28:26.889877+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines site:aclweb.org"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

I found search results related to EMNLP and ARR, but the results don't include a dedicated EMNLP 2026 ARR call for papers page. However, I can provide you with relevant information based on what was found:

The search results show that the 2nd BabyLM Workshop w
…[truncated 854 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 5123
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-25T22:28:32.362202+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 307 · 2026-05-25T22:28:32.814428+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers Budapest submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers Budapest submission deadline"
  }
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-25T22:28:35.654593+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-25T22:28:36.509803+00:00_

-rw-r--r-- 1 ubuntu ubuntu 4986929 May 25 20:55 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-25T22:28:36.660782+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-25T22:28:36.711495+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-25T22:28:37.816124+00:00_

Web search results for query: "EMNLP 2026 call for papers Budapest submission deadline"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026: Conference on Empirical Methods in Natural Language Processing","url":"https://www.myhuiban.com/conference/424?lang=en_us"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"}]

Based on the search results, here's the information about EMNLP 2026 in Budapest:

**Conference Details:**
EMNLP 2026 will be held October 24-29, 2026 in Budapest, Hungary.

**Main Conference Paper Submission Deadline:**
The ARR submission deadline for long and short papers is May 25, 2026, and all authors must complete the author registration form by May 27, 2026 EoD AoE.

**Industry Track Submission Deadline:**
For the Industry Track, the paper submission deadline is June 16, 2026 (11:59
…[truncated 424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 5001
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-25T22:28:39.322420+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review 2026 regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for 
…[truncated 883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 6960
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-25T22:28:56.089975+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-25T22:28:56.141122+00:00_

1	- id: "W1"
2	  summary: "GRPO QLoRA vs bf16 confounded variables — quantization and group size not isolated"
3	  category: experiment
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 1
7	  last_seen_round: 3
8	  mentions:
9	    - {round: 1, reviewers: "R1,R2", note: "Cannot support causal attribution of decoupling to QLoRA"}
10	    - {round: 2, reviewers: "R1,R2", note: "R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor."}
11	    - {round: 3, reviewers: "R1,R2", note: "Table 3 shows QLoRA G=4 vs bf16 G=8 — two variables changed simultaneously. §4.3 attribution unsupported. Need bf16 G=4 or QLoRA G=8 control. Both AGREE Must-Fix."}
12	  action_items:
13	    - {round: 1, action: "Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect", assigned_to: "Agent", status: "done"}
14	    - {round: 1, action: "Downgrade causal claim to observational", assigned_to: "Paper Agent", status: "done"}
15	    - {round: 2, action: "Deepen GRPO mechanism analysis with reward hacking lit + mechanistic chain", assigned_to: "Paper Agent", status: "done"}
16	    - {round: 3, action: "Run GRPO bf16 G=4 experiment (r3_grpo_bf16_g4). Config from plan_011 bf16 G=8, only G→4. cuda:1. Previous plan_015 v1/v2/v3 were manual kills not failures.", assigned_to: "Agent", status: "in_progress"}
17	  resolution: ""
18	  resolution_round: null
19	
20	- id: "W2"
21	  summary: "All results dev-set only, no test set"
22	  category: experiment
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 1
26	  last_seen_round: 2
27	  mentions:
28	    - {round: 1, reviewers: "R1,R2", note: "No CodaLab test results"}
29	    - {round: 2, reviewers: "R1,R2", note: "Test set results now exist (Table 9). Method ranking preserved (ρ=1.0)."}
30	  action_items:
31	    - {round: 1, action: "Add test set evaluation for all scales", assigned_to: "Agent+User", status: "don
…[truncated 23860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-25T22:29:00.758795+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-25T22:29:00.759187+00:00_

1	\begin{abstract}
2	Large Language Model (LLM)-based Document-level Relation Extraction (DocRE) now matches or exceeds encoder baselines in extraction accuracy, yet outputs bare relation triplets without identifying supporting sentences. Encoder-based evidence methods (SAIS, DREEAM) provide evidence but trail LLM approaches in accuracy, creating a gap between extraction performance and verifiability. We study evidence-grounded DocRE as structured generation and compare Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT) across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax (extraction cost of generating evidence) is scale-dependent: beneficial at 1.7B ($-$5.63pp dev Ign-F1) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B; positive $=$ cost). Gradient-based optimization amplifies evidence-extraction competition (GRPO catastrophic, DPO gradual), while RSFT with NLI-based scoring avoids decoupling through output filtering rather than gradient pressure. We define the Evidence-Decoupling Ratio (EDCR) to quantify extraction-evidence misalignment, validated at per-relation level ($\rho{=}{-}0.79$, $n{=}76$, $p{<}0.001$). Our 1.7B RSFT model (51.19 Ign-F1) approaches 8B Supervised Fine-Tuning (SFT) performance (50.19) at 4.7$\times$ fewer parameters. Test-set evaluation preserves model ranking across all scales (Spearman $\rho{=}1.0$)\footnote{Code and data are available at \url{https://anonymous.4open.science/r/faith-evidence-ie-18BD/}.}.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-25T22:29:01.062426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-25T22:29:01.062873+00:00_

1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{xu2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy, yet every one outputs bare relation triplets $(e_h, r, e_t)$ without indicating \emph{which sentences} support each prediction.
6	Without evidence, a clinician reviewing a ten-page case report must manually locate the sentences that support each extracted drug interaction, a bottleneck that undermines trust in automated extraction.
7	
8	\begin{figure*}[!t]
9	\centering
10	\includegraphics[width=0.92\textwidth]{fig_overview.pdf}
11	\vspace{-2mm}
12	\caption{Evidence-grounded DocRE produces relation triples with supporting sentence indices, unlike standard DocRE which outputs bare triples. RSFT selects the top-$k$ of $N$ CED-scored candidates per document for fine-tuning.}
13	\label{fig:overview}
14	\end{figure*}
15	
16	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
17	Both produce evidence and improve extraction, but encoder methods now trail LLM-based approaches in accuracy.
18	The community faces a gap: the most accurate extractors provide no evidence, while evidence-capable methods are no longer competitive.
19	
20	This gap reflects a structural difference.
21	In encoder methods, evidence retrieval is classification 
…[truncated 3009 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-25T22:29:01.163496+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers commitment deadline ARR site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers commitment deadline ARR site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-25T22:29:07.641067+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers commitment deadline ARR site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

Based on the search results from the official EMNLP 2026 website, here's what I found regarding the main conference call for papers and ARR commitment deadline:

## ARR Submission and Commitment Process

Papers must be submitted, at latest, by the ARR 2026 May cycle. Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.

## Important ARR 2026 May Policy

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## Author Registrat
…[truncated 476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 6477
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-25T22:29:12.209934+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" \"main conference papers\" page limit anonymity appendix guidelines 2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" \"main conference papers\" page limit anonymity appendix guidelines 2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 323 · 2026-05-25T22:29:14.067731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 324 · 2026-05-25T22:29:14.118613+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate on DocRED~\citep{yao2019docred} (3,053 training / 998 dev documents, 96 relation types) with Re-DocRED~\citep{tan2022redocred} for cross-dataset validation. Our primary model is Qwen3-4B; we also train Qwen3-1.7B, 8B, and 14B to study scale effects, with LLaMA-3.1-8B for cross-family validation. All models use LoRA~\citep{hu2022lora} ($r{=}64$, $\alpha{=}128$) with structured output jointly producing triples and evidence. RSFT selects the top-$k{=}1$ of $N{=}8$ samples by CED score (\S\ref{sec:ced}); GRPO uses group size $G{=}8$ for both configurations; DPO constructs preference pairs from CED-ranked outputs. We report Ign-F1 (primary; ignores training-set triples), Rel-F1, Evi-F1 (TP-only and joint per DREEAM protocol~\citep{ma2023dreeam}), and EDCR (\S\ref{sec:edcr}). Detailed hyperparameters appear in the Appendix.
8	
9	
10	\subsection{Main Results}
11	\label{sec:main_results}
12	
13	Table~\ref{tab:main} presents the primary comparison on Qwen3-4B. The SFT baseline exhibits high seed sensitivity (mean Ign-F1 43.58, std 3.80pp, range 39.74--47.34). Removing evidence entirely (no-evidence SFT, s42) reaches 47.21 Ign-F1.
14	
15	RSFT CED achieves 44.82 Ign-F1 (+1.24 over SFT mean) with substantially lower variance (std 0.51pp), though these reflect different sources of variation (Section~\ref{sec:scaling}). Even the weakest RSFT seed (44.23) exceeds the SFT mean. Evidence quality improves (Evi-F1 80.96 vs.\ 79.61) and coupling tightens (EDCR 0.6487 vs.\ 0.6797). Per-seed results appear in Appendix~\ref{sec:ablation_full}.
16	
17	\begin{table}[t]
18	\centering
19	\caption{Main results on DocRED dev (Qwen3-4B). Ign-F1 shows mean $\pm$ std$^{(\text{seeds})}$; other metrics are same-seed means. Best \textbf{bold}; best evidence-generating \underline{underlined}. Per-seed: Appendix~\ref{tab:ablation_full}.}
20	\label{tab:main}
21	\small
22	\resizebox
…[truncated 10004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-25T22:29:17.583533+00:00_

Web search results for query: ""EMNLP 2026" "main conference papers" page limit anonymity appendix guidelines 2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results from the EMNLP 2026 website, here are the key guidelines for main conference papers:

**Page Limits:**
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

**Anonymity:**
Following the ACL and ARR policies, there is no a
…[truncated 597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 5373
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-25T22:29:23.607790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-25T22:29:24.060034+00:00_

100	\label{sec:generalization}
101	
102	Cross-architecture validation on LLaMA-3.1-8B (Table~\ref{tab:scaling}) shows the largest RSFT gain (+5.45pp) with complete pairwise seed separation (\S\ref{sec:scaling}). The RSFT improvement transfers across datasets: on Re-DocRED~\citep{tan2022redocred}, RSFT achieves 41.45 Ign-F1 (+4.86pp over SFT 36.59), matching the DocRED gain (+5.08pp). Our best joint Evi-F1 (36.1, DREEAM-protocol) falls below supervised DREEAM (54.15\%~\citep{ma2023dreeam}), a gap driven by extraction performance rather than evidence quality (TP-only Evi-F1 exceeds 80\%). On the Re-DocRED test set, RSFT Ign-F1 drops approximately 20pp relative to dev across all evaluated scales (e.g., 14B: 57.9$\to$38.5), attributable to 2.82$\times$ higher annotation density in test (34.7 vs.\ 12.3 gold triples per document); model ranking is perfectly preserved (Spearman $\rho{=}1.0$; Table~\ref{tab:test_results} in Appendix). Full results appear in Appendix~\ref{sec:generalization_full}.
103	
104	
105	\begin{figure}[t]
106	\centering
107	\includegraphics[width=\columnwidth]{fig_evidence_tax.pdf}
108	\vspace{-4mm}
109	\caption{Inference-time evidence tax across model scales (RSFT models, Re-DocRED test). Negative values indicate evidence \emph{benefits} extraction. Error bars show $\pm$1 std (all scales have $\geq$2 seeds).}
110	\label{fig:evidence_tax}
111	\end{figure}
112	
113	\subsection{Discussion}
114	\label{sec:analysis}
115	
116	EDCR (\S\ref{sec:edcr}) validates as a diagnostic at both cross-method ($\rho = -0.96$, $n = 7$ unique methods, $p < 0.001$; Appendix~\ref{sec:edcr_per_relation}) and per-relation levels ($\rho = -0.79$, $n = 76$, $p < 0.001$; Appendix~\ref{sec:edcr_per_relation}), the latter orthogonal to Evi-F1 ($\rho = -0.06$); partial correlations controlling for shared components are virtually unchanged ($\rho = -0.9617$ vs.\ $-0.9643$). CED and flat-NLI produce comparable RSFT results (Rel-F1 45.63 vs.\ 45.61); stricter selection ($k{=}1$) outpe
…[truncated 766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-25T22:29:24.110731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-25T22:29:24.563033+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
5	\label{sec:task}
6	
7	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support (Figure~\ref{fig:overview}).
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\columnwidth]{fig_task_example.pdf}
12	\caption{Evidence-grounded DocRE example. Given a document with entity mentions, the model jointly predicts relation triples and supporting evidence sentences in a single structured output.}
13	\label{fig:task_example}
14	\end{figure}
15	
16	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central ph
…[truncated 10336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-25T22:29:24.563582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-25T22:29:24.965431+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We study evidence-grounded document-level relation extraction as structured generation. The evidence tax is scale-dependent: gradient methods amplify extraction-evidence competition while RSFT avoids it through discrete selection, improving extraction across all tested scales; a 1.7B RSFT model approaches 8B SFT at 4.7$\times$ fewer parameters.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-25T22:29:24.965782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-25T22:29:25.016228+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Data and architecture scope.}
4	We evaluate on two datasets (DocRED, Re-DocRED), both derived from Wikipedia; cross-domain evaluation is constrained by the absence of evidence-annotated DocRE datasets beyond Wikipedia, a limitation shared by all prior evidence-aware work (SAIS, DREEAM, EIDER).
5	Evidence tax patterns span two model families (Qwen3, LLaMA) with single hyperparameter settings per RL method; other architectures, scales beyond 14B, or alternative KL coefficients may produce different decoupling behaviors. The decoupling spectrum analysis is conducted entirely at 4B scale; whether the same ordering (GRPO catastrophic $\to$ DPO gradual $\to$ RSFT none) holds at other scales remains unverified.
6	
7	\paragraph{CED scoring sensitivity.}
8	CED scoring operates at the document level using an external NLI model (DeBERTa-v3); sensitivity to other NLI model families is unexplored, and sentence-level CED filtering disrupts co-reference chains (Evi-F1 $-$7.7pp).
9	
10	\paragraph{RSFT mechanistic explanation.}
11	Our explanation for why RSFT avoids decoupling (that discrete selection cannot exploit the extraction-evidence trade-off) is structural rather than empirical. We have not isolated whether RSFT's advantage stems primarily from removing low-quality training examples, from implicit data augmentation through candidate diversity, or from both. Disentangling these factors would require controlled experiments with fixed training data quality but varied selection mechanisms.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-25T22:29:29.633703+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-25T22:29:30.186358+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Document-Level Relation Extraction}
5	\label{sec:rw_docre}
6	
7	Encoder-based DocRE methods treat relation identification as classification over entity pair representations, with ATLOP \citep{zhou2021atlop} introducing adaptive thresholding and graph-based methods such as GAIN \citep{zeng2020gain} modeling inter-sentence reasoning. A parallel thread adds sentence-level evidence: SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary signal, DREEAM \citep{ma2023dreeam} extended this with dynamic memory-based retrieval, and EIDER \citep{xie2022eider} fuses evidence into the relation classifier. In all three, evidence is binary sentence classification that regularizes the encoder without increasing output length.
8	
9	Recent LLM-based methods recast DocRE as generation: AutoRE \citep{autore2024} uses QLoRA with relation-head-facts decomposition, \citet{xu2024lmrc} frame extraction as reading comprehension, RelPrior \citep{wang2025relprior} leverages relation priors, and \citet{xu2025docksrag} combine retrieval with structured knowledge. These methods match or surpass encoder baselines but produce bare triplets without evidence. At 8B, our RSFT model (54.33 Ign-F1) substantially outperforms both AutoRE (45.22\footnote{AutoRE and RelPrior DocRED dev Ign-F1 from the LLaMA3-8B reproductions by \citet{wang2025relprior}; the original AutoRE paper reports only F1.}) and RelPrior (47.70), while being the only method providing sentence-level evidence. The critical distinction is computational: in encoder methods, evidence retrieval is classification at negligible cost; in LLM-based DocRE, evidence requires generating additional tokens, imposing costs that depend on model capacity and optimization strategy.
10	
11	\subsection{Reinforcement Learning for Structured Generation}
12	\label{sec:rw_rl}
13	
14	GRPO \citep{shao2024deepseekmath} replaces PPO's \citep{schulman2017ppo} value network with
…[truncated 1639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-25T22:29:30.337438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-25T22:29:30.438574+00:00_

1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to all linear projections (attention and feed-forward). SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B with LoRA. A dash indicates non-applicable parameters. \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (\S\ref{sec:spectrum}).}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{l@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	\multicolumn{6}{l}{\textit{Model \& Adapter}} \\
16	\quad LoRA rank $r$ / $\alpha$ & 64 / 128 & 64 / 128 & 64 / 128 & 64 / 128 & 64 / 128 \\
17	\quad Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
18	\midrule
19	\multicolumn{6}{l}{\textit{Optimization}} \\
20	\quad Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-5 & 5e-7 \\
21	\quad Batch size (effective) & 16 & 16 & 4 & 1 & 4 \\
22	\quad Gradient accumulation & 4 & 4 & 16 & 1 & 4 \\
23	\quad Epochs / Max steps & 3 / -- & 3 / -- & -- / 100 & -- / 100 & 1, 3\textsuperscript{$\star$} / -- \\
24	\midrule
25	\multicolumn{6}{l}{\textit{RL / Selection}} \\
26	\quad Group size $G$ & -- & -- & 8 & 8 & -- \\
27	\quad KL coeff.\ / $\beta$ & -- & -- & 0.01 & 0.01 & 0.1 \\
28	\quad Candidates $N$ / Top-$k$ & -- & 8 / 1 & -- & -- & 8 / -- \\
29	\midrule
30	\multicolumn{6}{l}{\textit{Data}} \\
31	\quad Max new tokens & 1024 & 1024 & 1024 &
…[truncated 10458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-25T22:29:34.986636+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
  "offset": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
    "offset": "150"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-25T22:29:35.238358+00:00_

150	
151	\begin{table}[t]
152	\centering
153	\caption{Mechanistic breakdown of output quality across scales. Duplication rate: fraction of documents with degenerate outputs. Truncation $\Delta$: no-evidence rate minus with-evidence rate (positive means no-evidence truncates more).}
154	\label{tab:mechanistic}
155	\small
156	\begin{tabular}{lccccc}
157	\toprule
158	& \multicolumn{3}{c}{\textbf{Duplication Rate}} & \multicolumn{2}{c}{\textbf{Truncation}} \\
159	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
160	\textbf{Scale} & \textbf{w/ evi} & \textbf{no-evi} & \textbf{Gap} & \textbf{$\Delta$} & \textbf{Pattern} \\
161	\midrule
162	1.7B & 33.0 & 60.5 & 27.5 & +19 & no-evi worse \\
163	4B & 31.1 & 43.2 & 12.1 & +2 & neutral \\
164	8B & 29.2 & 32.9 & 3.7 & $-$9 & evi worse \\
165	\bottomrule
166	\end{tabular}
167	\end{table}
168	
169	
170	\section{Training-Time Evidence Tax}
171	\label{sec:training_tax}
172	
173	The evidence tax can be measured in two ways. The \emph{training-time} tax compares separately trained models (SFT with evidence vs.\ SFT without evidence in the training output format). The \emph{inference-time} tax (reported in Table~\ref{tab:scaling}) evaluates the same RSFT model with and without evidence at inference time.
174	
175	Na\"ive comparisons at \texttt{max\_new\_tokens}$=$1024 are confounded by differential truncation rates (e.g., 50.9\% vs.\ 31.9\% at 1.7B). To control for this, we adopt a \emph{matched@2048 fair evaluation}: both configurations are evaluated at \texttt{max\_new\_tokens}$=$2048, and the tax is computed on the intersection of documents where both models produce format-compliant output. Table~\ref{tab:training_tax} reports the matched@2048 training-time tax across Qwen3 scales.
176	
177	The tax reveals a within-family capacity threshold: evidence generation benefits 1.7B ($-$5.63pp on 971/985 fair-subset documents) but is approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B across three seeds, +0.04pp at 8B, +0.03pp at 14B). At 1.7B,
…[truncated 28643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-25T22:29:43.218377+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
  "description": "Count appendix lines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
    "description": "Count appendix lines"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-25T22:29:43.770871+00:00_

491 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-25T22:29:43.771272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
  "offset": "492"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
    "offset": "492"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-25T22:29:43.871905+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (492). The file has 492 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-25T22:30:09.590457+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf'], capture_output=True, text=True)\nfor line in result.stdout.split('\\n'):\n    if 'Pages' in line:\n        print(line)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Count PDF pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf'], capture_output=True, text=True)\nfor line in result.stdout.split('\\n'):\n    if 'Pages' in line:\n        print(line)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Count PDF pages"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-25T22:30:11.498175+00:00_

Pages:           18

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 1907
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-25T22:30:11.649388+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/  */ /g' | wc -w",
  "description": "Count abstract words roughly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/  */ /g' | wc -w",
    "description": "Count abstract words roughly"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-25T22:30:11.750292+00:00_

181

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-25T22:30:43.883817+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "faith-evidence-ie",
  "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "faith-evidence-ie",
    "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
  }
}
```

</details>

---


### Tool call

_source line 349 · 2026-05-25T22:30:44.437136+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 350 · 2026-05-25T22:31:06.287409+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22403
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-25T22:31:06.287845+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 21850
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-25T22:31:06.438680+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止**: 2026-05-25\n- **格式**: ACL 模板 [review]，Long paper 正文严格 8 页，参考文献不限\n- **Limitations**: 必须，conclusion 之后，不计入页数\n- **匿名**: Double-blind\n- **会议**: Budapest, Hungary, 2026-10-24 ~ 10-29\n\n## 论文路径\n- main.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **EDCR 指标设计与验证**：\n   - EDCR 公式的合理性——分子分母共享 TP 组件导致的机械负相关是否充分讨论？\n   - per-relation 验证 (n=76, ρ=-0.79) 的统计效力是否足够？\n   - partial correlation 和 permutation test 是否正确控制了 confound？\n\n2. **CED 评分方法论**：\n   - NLI-based scoring 的局限性：只用了 DeBERTa-v3-base，sensitivity analysis 充分吗？\n   - CED vs flat-NLI 仅差 0.02pp，contrastive formulation 的附加价值是什么？\n\n3. **实验控制与 confound**：\n   - GRPO QLoRA vs bf16 对比：quantization 和 precision 之外是否有其他未控制的变量？（lr 不同？）\n   - DPO β=0.1 单一设定，spectrum 结论的稳健性？\n   - RSFT 共享 SFT checkpoint 导致 variance 比较不公平（SFT = full randomness, RSFT = fixed-base）\n\n4. **统计严谨性**：\n   - n=3 seeds 的统计效力（sign test p=0.0625 不显著）\n   - evidence tax 的 CI 是否 cross zero？\n   - 1.7B 的 s42 是最强 seed (+3.22pp above mean)，是否影响 tax 估计？\n\n5. **Scaling claim**：\n   - 4 个 Qwen3 scale + 1 个 LLaMA，\"scale-dependent\" 结论需要多少数据点？\n   - 14B 仅 1 seed SFT baseline，可靠性？\n   - test-set 14B RSFT advantage 消失（Δ=-0.37pp），如何解释？\n\n6. **页数合规**：\n   - 18 页 PDF，正文是否超过 8 页？（EMNLP 2026 严格 8 页，超页 = desk reject）\n\n请按 Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment 的结构输出审稿意见。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止**: 2026-05-25\n- **格式**: ACL 模板 [review]，Long paper 正文严格 8 页，参考文献不限\n- **Limitations**: 必须，conclusion 之后，不计入页数\n- **匿名**: Double-blind\n- **会议**: Budapest, Hungary, 2026-10-24 ~ 10-29\n\n## 论文路径\n- main.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **EDCR 指标设计与验证**：\n   - EDCR 公式的合理性——分子分母共享 TP 组件导致的机械负相关是否充分讨论？\n   - per-relation 验证 (n=76, ρ=-0.79) 的统计效力是否足够？\n   - partial correlation 和 permutation test 是否正确控制了 confound？\n\n2. **CED 评分方法论**：\n   - NLI-based scoring 的局限性：只用了 DeBERTa-v3-base，sensitivity analysis 充分吗？\n   - CED vs flat-NLI 仅差 0.02pp，contrastive formulation 的附加价值是什么？\n\n3. **实验控制与 confound**：\n   - GRPO QLoRA vs bf16 对比：quantization 和 precision 之外是否有其他未控制的变量？（lr 不同？）\n   - DPO β=0.1 单一设定，spectrum 结论的稳健性？\n   - RSFT 共享 SFT checkpoint 导致 variance 比较不公平（SFT = full randomness, RSFT = fixed-base）\n\n4. **统计严谨性**：\n   - n=3 seeds 的统计效力（sign test p=0.0625 不显著）\n   - evidence tax 的 CI 是否 cross zero？\n   - 1.7B 的 s42 是最强 seed (+3.22pp above mean)，是否影响 tax 估计？\n\n5. **Scaling claim**：\n   - 4 个 Qwen3 scale + 1 个 LLaMA，\"scale-dependent\" 结论需要多少数据点？\n   - 14B 仅 1 seed SFT baseline，可靠性？\n   - test-set 14B RSFT advantage 消失（Δ=-0.37pp），如何解释？\n\n6. **页数合规**：\n   - 18 页 PDF，正文是否超过 8 页？（EMNLP 2026 严格 8 页，超页 = desk reject）\n\n请按 Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment 的结构输出审稿意见。"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-25T22:31:24.581630+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18142
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-25T22:31:24.783651+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止**: 2026-05-25\n- **格式**: ACL 模板 [review]，Long paper 正文严格 8 页，参考文献不限\n- **Limitations**: 必须，conclusion 之后，不计入页数\n- **匿名**: Double-blind\n- **会议**: Budapest, Hungary, 2026-10-24 ~ 10-29\n\n## 论文路径\n- main.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - 三个 contribution 的新颖性：(1) scale-dependent evidence tax, (2) decoupling spectrum + EDCR, (3) RSFT avoids decoupling\n   - 论文自我定位为 empirical study 而非 method innovation——这够 EMNLP main/findings 吗？\n   - RSFT 不是新方法（STaR 2022），CED 不是独立贡献（vs flat-NLI 仅 0.02pp）——核心新颖性在哪？\n   - EDCR 作为诊断指标的价值 vs 简单地报告 Evi-F1\n   - \"Evidence is not uniformly harmful\" 这个发现的影响力——之前文献有无类似结论？\n\n2. **Related Work 覆盖**：\n   - DocRE 领域覆盖是否充分？是否遗漏重要工作？\n   - RL for structured generation 文献是否 up to date？\n   - Evidence faithfulness 文献链是否完整？\n   - 是否有 multi-task learning / task interference 相关文献遗漏？\n\n3. **写作质量**：\n   - Abstract 是否准确反映论文核心发现？有无夸大？\n   - Introduction 的叙事是否清晰——从 gap 到 contribution 的逻辑链\n   - §4.4 (scaling) 信息密度是否过高？段落长度是否合理？\n   - Conclusion 是否过短？（当前仅 2 行）\n   - 术语一致性：evidence tax 的 sign convention 是否全文一致？\n   - Figure/Table caption 是否 self-contained？\n\n4. **格式合规**：\n   - 18 页 PDF：正文 vs Limitations vs References vs Appendix 的页数分布\n   - 匿名合规：是否有泄露作者身份的信息？\n   - Abstract 字数（~181 words，需 ≤200）\n   - 引用格式是否一致（natbib）？\n   - Appendix 结构和编号是否规范？\n\n5. **完整性**：\n   - Limitations 是否充分？遗漏了什么？\n   - 是否有未解释的异常结果？（如 14B test-set reversal、4B evidence tax inconsistency）\n   - Re-DocRED test 20pp drop 的解释是否足够？\n   - DPO 只测了 β=0.1，这个限制是否充分讨论？\n\n请按 Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment 的结构输出审稿意见。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止**: 2026-05-25\n- **格式**: ACL 模板 [review]，Long paper 正文严格 8 页，参考文献不限\n- **Limitations**: 必须，conclusion 之后，不计入页数\n- **匿名**: Double-blind\n- **会议**: Budapest, Hungary, 2026-10-24 ~ 10-29\n\n## 论文路径\n- main.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - 三个 contribution 的新颖性：(1) scale-dependent evidence tax, (2) decoupling spectrum + EDCR, (3) RSFT avoids decoupling\n   - 论文自我定位为 empirical study 而非 method innovation——这够 EMNLP main/findings 吗？\n   - RSFT 不是新方法（STaR 2022），CED 不是独立贡献（vs flat-NLI 仅 0.02pp）——核心新颖性在哪？\n   - EDCR 作为诊断指标的价值 vs 简单地报告 Evi-F1\n   - \"Evidence is not uniformly harmful\" 这个发现的影响力——之前文献有无类似结论？\n\n2. **Related Work 覆盖**：\n   - DocRE 领域覆盖是否充分？是否遗漏重要工作？\n   - RL for structured generation 文献是否 up to date？\n   - Evidence faithfulness 文献链是否完整？\n   - 是否有 multi-task learning / task interference 相关文献遗漏？\n\n3. **写作质量**：\n   - Abstract 是否准确反映论文核心发现？有无夸大？\n   - Introduction 的叙事是否清晰——从 gap 到 contribution 的逻辑链\n   - §4.4 (scaling) 信息密度是否过高？段落长度是否合理？\n   - Conclusion 是否过短？（当前仅 2 行）\n   - 术语一致性：evidence tax 的 sign convention 是否全文一致？\n   - Figure/Table caption 是否 self-contained？\n\n4. **格式合规**：\n   - 18 页 PDF：正文 vs Limitations vs References vs Appendix 的页数分布\n   - 匿名合规：是否有泄露作者身份的信息？\n   - Abstract 字数（~181 words，需 ≤200）\n   - 引用格式是否一致（natbib）？\n   - Appendix 结构和编号是否规范？\n\n5. **完整性**：\n   - Limitations 是否充分？遗漏了什么？\n   - 是否有未解释的异常结果？（如 14B test-set reversal、4B evidence tax inconsistency）\n   - Re-DocRED test 20pp drop 的解释是否足够？\n   - DPO 只测了 β=0.1，这个限制是否充分讨论？\n\n请按 Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment 的结构输出审稿意见。"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-25T22:31:26.097990+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1314
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-25T22:31:35.850502+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-25T22:31:37.214434+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'faith-evidence-ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1363
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-25T22:31:37.367003+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie -name \"*.yaml\" -o -name \"*.yml\" | head -20",
  "description": "Find config yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie -name \"*.yaml\" -o -name \"*.yml\" | head -20",
    "description": "Find config yaml files"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-25T22:31:38.171819+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/_figure_backups/20260524_052006/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/markdown_it/port.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/configs/provider/vlm/gemini.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/configs/provider/image/google_imagen.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/configs/pipeline/diagram.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/configs/pipeline/plot.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/configs/config.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/configs/eval/vlm_judge.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/configs/accelerate_4gpu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T105318/medi
…[truncated 476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 804
}
```

</details>

---


### Assistant

_source line 360 · 2026-05-25T22:31:52.751103+00:00_

外部审稿未启用（`not_requested`），跳过 Step 0.6。

当前状态：
- ✅ Venue 要求搜索完毕
- ✅ 视觉审查 Agent 已派发（fire-and-forget）
- ✅ Reviewer 1（方法严谨性 + 实验设计）已分配
- ✅ Reviewer 2（新颖性 + 完整性 + 写作质量）已分配

等待两位 Reviewer 返回 Round 1 初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 27

## Round 27

2 recorded events


### User

_source line 361 · 2026-05-25T22:37:16.929717+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 = Borderline Conference
**一句话总结**: 研究问题重要且实验覆盖面广，EDCR 指标设计新颖且验证较充分，但核心 claim（evidence tax 规模依赖性）的统计支撑不足（n=3, CI 跨零），加上 CED 对比设计未带来可衡量收益（0.02pp）以及部分实验 confound 未隔离，削弱了结论的可靠性。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 主要 claims 有实验支撑但关键效应的 CI 跨零（evidence tax @ n=3），GRPO 实验存在 lr-quantization confound，DPO 仅单一 β=0.1 |
| Excitement | 3.5/5 | 研究问题（extraction-evidence trade-off）重要且 under-explored，EDCR 诊断指标有实用价值，但 RSFT 作为方法贡献偏 incremental |
| Reproducibility | 4/5 | 代码和数据承诺公开，超参数表格完整（Table 4），实验设置描述充分，但部分配置细节（如 GRPO bf16 lr）不够透明 |
| Reviewer Confidence | 4/5 | 仔细阅读了全文和全部附录，DocRE 和 RL alignment 方法论在我的审查范围内 |

---

## 主要优势

**S1. 研究问题定义精准，实用价值高。** 论文准确识别了 LLM-based DocRE 中 evidence grounding 的代价问题——现有方法要么不产出 evidence，要么假设 evidence 免费。将 evidence-extraction trade-off 作为一个显式的研究对象是一个有价值的 framing（Section 1, contributions 1-3）。

**S2. EDCR 指标设计巧妙且验证充分。** EDCR（Eq. 2）作为 extraction-evidence decoupling 的诊断工具，概念清晰且有实际用途。Appendix L 的验证非常充分：partial correlation 控制 TP 后相关性仅下降 0.15%（ρ: -0.8541 → -0.8551），10,000 次 permutation test 确认 p<0.0001，per-relation 分析（n=76, ρ=-0.79）与 cross-method 分析（n=17）一致。这是论文最扎实的贡献。

**S3. 三范式系统对比框架有参考价值。** 将 GRPO、DPO、RSFT 统一在同一 SFT baseline、同一评估协议下对比，并用 Table 1 清晰概括三者的信号类型和训练机制差异，对 practitioner 选择后训练策略有直接指导意义。

**S4. 跨模型家族和跨规模验证增强了发现的可推广性。** 在 4 个 Qwen3 规模（1.7B-14B）和 LLaMA-3.1-8B 上的交叉验证（Table 3, Appendix H）显示 RSFT 的核心模式在不同架构上一致。

**S5. 附录质量高。** 14 个附录覆盖了消融、统计验证、error decomposition、定性分析等，显示了严谨的研究态度。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] n=3 seeds 的统计效力不足以支撑核心 claim
- 具体位置：Section 4.4, Table 7 (Appendix D), Section 4.2
- 问题：论文承认 "CI crosses zero at n=3"（p.7），但仍在 abstract 和 contributions 中将 evidence tax 描述为已确立的现象（"We observe a scale-dependent evidence tax"）。对于 3 个 seeds：
  - Sign test 最小 p-value = 0.0625，无法达到任何常规显著性水平
  - Table 7 的 95% CI 均极宽，多个配置的 RSFT gain CI 确实跨零
  - 1.7B 的 s42 是最强 seed（+3.22pp above mean），在 n=3 中有 disproportionate influence
- 为什么影响接收：evidence tax 的 scale-dependency 是论文三大贡献之一（Contribution 1），如果统计上无法排除 zero effect，则该贡献被严重削弱。
- 建议修改方向：(a) 增加到 n≥5 seeds，至少在 1.7B 和 4B 这两个关键规模上；(b) 如果计算资源有限，将语言从 "observe" 改为 "preliminary evidence suggests"，并在 abstract 中明确 CI 跨零的事实；(c) 考虑 bootstrap CI 以更好利用有限样本。

**N2** [critical] GRPO 实验中 quantization 与 learning rate 的 confound 未隔离
- 具体位置：Section 4.3, Table 4 (Appendix A)
- 问题：GRPO QLoRA（4-bit）和 GRPO bf16 两个配置之间，除了 precision 差异外，Table 4 显示它们的 learning rate、batch size 等超参可能不同。论文将 QLoRA 的 catastrophic collapse（Rel-F1: 1.38）归因于 quantization-induced divergence，并引用 Li et al. (2026)。但如果 lr 也不同，collapse 可能是 lr 过大 + quantization 的联合效应，而非单独的 quantization 问题。论文虽提供了 bf16 G=1 的补充实验（Rel-F1 28.73），但这只控制了 group size，未控制 lr。
- 为什么影响接收：GRPO catastrophic collapse 是 "decoupling spectrum" 叙事的锚点。如果 collapse 的归因不准确，整个 spectrum 框架的可信度降低。
- 建议修改方向：(a) 在 Table 4 中明确列出 GRPO QLoRA 和 bf16 的完整超参数（尤其 lr、warmup、scheduler）；(b) 做一组 matched-lr 对比（QLoRA lr = bf16 lr）以隔离 quantization 的纯效应；(c) 如无法补充实验，在讨论中明确承认 lr 是 potential confound。

**N3** [critical] DPO 仅测试 β=0.1，"spectrum" 结论缺乏支撑
- 具体位置：Section 4.3（DPO 段落），Table 2
- 问题：论文将 GRPO（catastrophic）→ DPO（gradual）→ RSFT（stable）描述为一个 "decoupling spectrum"（Section 4.3 标题即为 "Evidence-Extraction Decoupling Spectrum"）。但 DPO 只测试了 β=0.1 这一个 KL penalty 系数。β 是 DPO 中控制偏离 reference policy 程度的关键超参——小 β 意味着更激进的优化，大 β 更保守。不同 β 下 DPO 的 decoupling 行为可能截然不同：
  - β=0.5 或 β=1.0 时 DPO 可能表现得更接近 RSFT（保守优化）
  - β=0.01 时可能更接近 GRPO collapse
  论文对此完全没有讨论。
- 为什么影响接收：单一 β 下的 DPO 表现无法支撑 "DPO 天然位于 spectrum 中间" 的结论。这可能只是 β=0.1 的特定行为，而非 DPO 方法的固有属性。
- 建议修改方向：(a) 至少测试 β ∈ {0.01, 0.1, 0.5} 三个点，展示 DPO 在 spectrum 上的位移；(b) 如无法补充实验，大幅弱化 spectrum 叙事，改为 "under our specific configuration, DPO shows intermediate behavior"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] CED 对比设计的附加价值不明确
- 具体位置：Section 3.4, Section 4.7
- 问题：Section 3.4 用了大量篇幅设计 CED 的 contrastive formulation（正样本 vs. entity-sharing distractor），但 Section 4.7 承认 "CED and flat-NLI produce comparable RSFT outcomes (mean Rel-F1 difference of 0.02pp)"。0.02pp 的差异在 n=3 的实验方差范围内是 noise。论文采用 CED 而非 flat-NLI 的理由是 "per-triple discrimination supports interpretable error analysis"——但这个解释性优势在正文中没有充分展示（仅 Appendix M 的 3 个 case study 间接涉及）。
- 建议：(a) 诚实地在 Section 3.4 中前置说明 contrastive formulation 不影响选择质量，主要价值在于可解释性；(b) 削减 Section 3.4 篇幅，将节省的空间用于强化统计分析（如 N1 所建议的更多 seeds）。

**W2** [warning] 14B 仅 1 seed SFT baseline，scaling claim 不可靠
- 具体位置：Table 3, Section 4.6
- 问题：Table 3 脚注显示 14B 的 SFT baseline 仅有 1 个 seed（"1 seed remaining checkpoint"），而 RSFT 有 3 seeds。这使得 14B 的 evidence tax 估计完全依赖单一数据点，没有任何方差信息。同时，在 test set 上 14B RSFT advantage 消失（Δ=-0.37pp），论文解释为 "noise or evaluation sensitivity"（Section 4.4），但无法用 1-seed baseline 来判断这是否是 noise。
- 建议：补充至少 2 个 14B SFT seeds，或在 scaling discussion 中将 14B 结果标记为 preliminary。

**W3** [warning] RSFT 共享 SFT checkpoint 导致方差比较不公平
- 具体位置：Section 3.2, Section 4.4, Table 7
- 问题：SFT 从不同 random seeds 从头训练，variance 包括初始化 + 训练全过程的随机性。RSFT 从同一 SFT checkpoint 出发做 rejection sampling + fine-tuning，variance 仅包括 sampling + fine-tuning 阶段。论文在 Section 4.4 承认 "SFT reflects full training runs... RSFT reflects additional fine-tuning from a fixed base"，但没有讨论这对 variance comparison 的 implication——Table 7 中 RSFT 的更窄 CI 可能部分是设计 artifact 而非方法优势。
- 建议：在讨论 RSFT variance reduction 时明确说明 shared initialization 是一个 contributing factor，区分 "RSFT 方法本身减少了方差" 和 "fixed base 的设计选择减少了方差"。

**W4** [warning] Test-set evidence tax 在 8B 出现反转，解释不充分
- 具体位置：Section 4.4（p.7），Table 11 (Appendix F), Figure 6
- 问题：在 8B 规模上，test set 的 evidence tax 反转为负值（benefit 而非 cost），论文解释为 "the 8B test tax (−1.17pp) shows slight variations from its near-neutral dev counterpart (+0.04pp)"。但这个反转恰好发生在 RSFT test-set advantage 也消失的规模上，暗示 test-set 的分布可能与 dev 有系统性差异。Figure 6 也显示 8B 处 SFT 和 RSFT 的 bar 图出现交叉。论文未讨论 dev-test distribution shift 是否是系统性问题。
- 建议：(a) 报告 dev 和 test 的 document length、relation density 等统计差异；(b) 在 14B 上也检查 test-set tax 以确认是否规模相关。

---

## 小问题（不影响接收）

- **M1**: Abstract 第一句 "Large Language Model (LLM)-based Document-level Relation Extraction (DocRE) methods have surpassed encoder baselines in extraction accuracy" 缺少引用支撑，建议加上具体 benchmark 和 reference。
- **M2**: Figure 4 的 y 轴标签（Rel-F1 和 Evi-F1）在打印时可能因规模压缩而难以辨认，建议增大字号。
- **M3**: Section 2.3 "Evidence Faithfulness and Rejection Sampling" 标题暗示 rejection sampling 是关于 faithfulness 的已有工作，但实际引用的 STAR、scaling laws 等工作并非专门针对 evidence faithfulness，标题略有误导。
- **M4**: Limitations section 提到 "we have not isolated whether RSFT's advantage stems primarily from removing low-quality training examples, from implicit data augmentation through candidate diversity, or from both"——这是一个重要的 ablation gap，建议在 future work 中更突出。

---

## Questions to Authors

**Q1**: EDCR 公式中，对于 false-positive triples（无 gold evidence），所有 cited evidence 自动计为 distractor。能否报告 EDCR 仅在 TP triples 上计算的变体结果？这可以分离 "extraction error" 和 "genuine evidence misalignment" 两个来源。

**Q2**: CED 使用 DeBERTa-v3-base。Appendix B 报告替换为 v3-large 仅差 0.10pp。但是否测试过完全不同的 NLI 架构（如 RoBERTa-large-mnli）或 prompt-based NLI（如用 GPT-4 做 NLI 判断）？如果 CED 对 NLI 模型选择高度 robust，应该明确说明；如果不 robust，这是一个方法论风险。

**Q3**: RSFT 的 top-k=1 selection 策略是否尝试过 k>1？k=1 是最激进的过滤，k=3 或 k=5 可能保留更多多样性同时仍保持质量过滤。这对理解 RSFT 的 "discrete selection" 优势机制很重要。

**Q4**: DPO preference pairs 的构造中，最高 CED score 为 preferred，最低为 rejected。如果用 Evi-F1 而非 CED 来构造 preference pairs，DPO 的 decoupling 行为是否变化？这可以区分 DPO 的固有 decoupling tendency 和 CED 信号质量的 contribution。

---

## Missing References

- **Xu et al. (2024) "Towards Faithful Document-Level Relation Extraction"** — 如果该工作存在且直接研究 DocRE faithfulness，应被讨论。
- **DPO β sensitivity** 方面的工作，如 Rafailov et al. (2024) 关于 β 选择对 DPO 行为影响的分析，可以支撑或对比本文的 DPO 实验设计选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 362 · 2026-05-25T22:37:32.749619+00:00_

Reviewer 1 审稿意见已收到。评分 3.5（Borderline Conference），核心问题：n=3 统计效力不足、GRPO lr-quantization confound、DPO 单一 β。

等待 Reviewer 2 审稿意见返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 363 · 2026-05-25T22:37:39.684178+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿完成。总结：

- **Overall: 3.5（Borderline Conference）**
- **Soundness: 3.0** — n=3 seeds 的 CI 跨零削弱 evidence tax 核心 claim；GRPO 实验有 lr-quantization confound；DPO 仅 β=0.1 不足以支撑 spectrum 结论
- **Excitement: 3.5** — 研究问题有实用价值，EDCR 指标设计新颖且验证充分，但 RSFT 方法贡献偏 incremental

**3 个 Must-Fix**：(N1) 统计效力不足，需增加 seeds 或弱化 claim 语言；(N2) GRPO QLoRA vs bf16 需隔离 lr confound；(N3) DPO 需测试多个 β 值或弱化 spectrum 叙事

**4 个 Should-Fix**：CED 0.02pp 附加价值不明确、14B 单 seed baseline、RSFT 共享 checkpoint 的方差比较不公平、8B test-set tax 反转解释不充分

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 364 · 2026-05-25T22:37:47.967947+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 29

## Round 29

6 recorded events


### User

_source line 365 · 2026-05-25T22:39:18.716500+00:00_

[Reviewer 2 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 实证方法论扎实、实验规模令人信服（3 paradigms × 4 scales × 3 seeds × 2 datasets × cross-architecture），但三个 contribution 的原创性均偏弱——RSFT 是已有方法的应用、CED 相对 flat-NLI 提升微乎其微、EDCR 作为诊断指标缺乏充分验证——使论文更适合 Findings 而非主会议。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验覆盖广（3 paradigms × 4 scales × 3 seeds），但 DPO 仅测 β=0.1、GRPO 仅 G=8，核心 claim 的泛化性受限；EDCR 与 CED 共享 NLI backbone 存在循环依赖风险 |
| Excitement | 3/5 | Evidence tax 的 scale-dependent landscape 是有价值的实证发现，但方法贡献有限：RSFT=STaR+CED 筛选，CED≈flat-NLI，EDCR 是简单比率 |
| Reproducibility | 4/5 | 详细的超参数（Appendix A/Table 4）、匿名代码发布、3 seed 复现、跨架构验证 |
| Reviewer Confidence | 4/5 | 熟悉 DocRE、LLM fine-tuning、RL for LLMs 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心新颖性不足以支撑主会议接收

- 具体位置：§1 Contributions, §3.2 (RSFT), §3.3 (CED), §3.5 (EDCR)
- 问题：
  1. **RSFT 不是新方法**：论文明确承认 RSFT 建立在 STaR (Zelikman et al., 2022) 之上（§3.3 "building on Self-Taught Reasoner"）。其贡献在于将 STaR 应用到 evidence-grounded DocRE 并用 CED 做筛选——这是 engineering contribution 而非 methodological innovation。
  2. **CED vs flat-NLI 差异微乎其微**：§3.4 末段自己承认 "the contrastive formulation is not essential for data selection quality"——mean Rel-F1 差异仅 0.02pp。如果去掉 contrastive 组分，CED 退化为简单的 NLI-based 打分，大幅削弱了 CED 作为独立贡献的地位。
  3. **EDCR 是简单比率**：公式 (2) 定义 EDCR 为 distractor citation rate，本质上是 1 − precision(evidence|relation)。作为诊断指标，其独立价值需要更强的跨 backbone 验证（见 W2）。
  4. **Evidence tax 的 framing 有误导性**：§4.4 和 Appendix K (Table 15) 的 error decomposition 表明小模型的 evidence tax 主要来自 truncation（截断）和 duplication（重复），而非 evidence 本身的 harmful effect。这意味着 "evidence tax" 本质上是 generation capacity bottleneck 的表现——模型无法可靠地生成足够长的结构化输出——而非 evidence 固有的代价。论文应清晰区分这两种来源。

- 为什么影响接收：EMNLP main 要求 novelty + impact。论文诚实地定位为 empirical study，但三个 contribution 分别是：已有方法的应用、自证微效的组分、简单的诊断比率。核心 empirical finding（evidence tax 的 scale-dependence）如果剥离 truncation 因素后，剩余的 "genuine evidence interference" 有多大尚不清楚。

- 建议修改方向：
  (a) 坦诚降低 CED 的 contribution 权重，将重心放在 evidence tax landscape 的实证发现上
  (b) 在 evidence tax 分析中明确区分 "truncation-induced tax"（随 capacity 自然消失）和 "information-interference tax"（extraction-evidence 真正的冲突）——Appendix K 的 error decomposition 已有素材，但未在正文中充分利用
  (c) 对 EDCR 增加跨 NLI backbone 的稳定性 ablation

**N2** [critical] 优化超参数探索不充分，削弱 decoupling spectrum 的泛化性

- 具体位置：§3.3 (DPO β=0.1), §4.1 (GRPO G=8), Table 1
- 问题：论文的核心 claim 之一是 "gradient-based optimization (GRPO, DPO) causes extraction-evidence decoupling while RSFT avoids it"（§1 Contribution 2, §3.5 验证）。但：
  - DPO 仅测试了 β=0.1 这一个温度参数。DPO 的 β 直接控制策略偏离 reference policy 的程度——更低的 β（如 0.01）可能产生更保守的更新从而减少 decoupling，更高的 β（如 0.5）可能加剧。
  - GRPO 仅测试了 G=8（group size）。更大的 G 提供更好的 advantage 估计，可能改善 extraction-evidence coupling。
  - RSFT 使用 k=1（top-1 selection）。k>1 的效果未探索。
  - 论文未提供任何超参数敏感性分析来支撑 "gradient methods inherently decouple" 这一归因。

- 为什么影响接收：如果 decoupling 程度高度依赖超参数选择（例如特定 β 值恰好导致 extreme decoupling），则 "decoupling spectrum" 的方法论归因（Table 1 的定性分类）将从 "fundamental property of gradient optimization" 降级为 "specific hyperparameter regime behavior"。

- 建议修改方向：至少对 DPO β ∈ {0.01, 0.1, 0.5} 做消融实验；或在正文（而非仅 Limitations）中明确讨论这一限制及其对结论泛化性的影响。

**N3** [critical] Conclusion 过于简短，不符合 EMNLP 论文标准

- 具体位置：Section 5, page 8（约 3 句话，~60 words）
- 问题：Conclusion 完全未讨论：
  - **Broader implications**：evidence tax 对 LLM-based IE 系统设计的启示——什么时候应该要求模型生成 evidence？
  - **Future directions**：如何在更大规模（70B+）/ 更多 IE 任务（事件抽取、NER）上验证 evidence tax 现象？
  - **Connection to wider literature**：gradient pressure vs discrete selection 的二分法是否适用于其他 structured generation 任务（如 code generation with explanations、math with proofs）？
- 为什么影响接收：对于 empirical study，Conclusion 是 reviewer 形成对工作意义整体判断的关键段落。3 句话的 Conclusion 传递出 "作者未充分思考工作 significance" 的信号。
- 建议修改方向：扩展至 8-12 句话，覆盖 key takeaways、implications for practitioners、和 future work。仍可保持在 8 页内（当前 page 8 有空间）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Related Work 遗漏 multi-task learning / gradient conflict 文献

- 具体位置：§2.1, §2.2
- 问题：论文的核心发现是 gradient-based 优化导致 extraction 和 evidence 两个子任务 decouple。这本质上是 multi-task learning 中的 **negative transfer / gradient conflict** 问题，但论文仅在 §2.1 末尾简单提及 Ruder (2017)，缺少高度相关的文献：
  - PCGrad (Yu et al., 2020, NeurIPS)："Gradient Surgery for Multi-Task Learning"——直接处理 multi-task gradient conflict
  - Reward overoptimization (Gao et al., 2023)："Scaling Laws for Reward Model Overoptimization"——GRPO 的 catastrophic decoupling 可能与 reward hacking 相关
  - 这些方法可能提供解决 decoupling 的替代路径（如对 extraction 和 evidence sub-objectives 分别计算 gradient 并做 projection），论文未讨论。
- 建议：增加一段讨论 multi-task gradient conflict 文献，说明为什么这些方法在当前 setting 中不直接适用（或值得未来探索）。

**W2** [warning] EDCR 与 CED 共享 NLI backbone，存在 circular dependency 风险

- 具体位置：§3.4 CED definition (Equation 1), §3.5 EDCR definition (Equation 2)
- 问题：CED 使用 DeBERTa-v3 NLI 模型对候选输出评分（用于 RSFT 数据筛选）；EDCR 同样基于 NLI 判断 cited evidence 是否为 distractor。两者共享相同的 NLI backbone。因此：
  - EDCR 与 Rel-F1 的负相关（ρ=−0.79, §3.5）可能部分反映 NLI 模型的系统偏差
  - 论文声称 EDCR "independent of Evi-F1"（ρ=−0.06），但这种独立性可能是 NLI 评估维度选择的产物
  - 论文在 Appendix L 做了 partial correlation controlling for TP，但未做跨 NLI backbone 的稳定性验证
- 建议：用至少一个替代 NLI 模型（如 RoBERTa-large-MNLI 或更新的模型）重新计算 EDCR，报告跨 backbone 的 rank correlation 稳定性。

**W3** [warning] §4.4 信息密度过高，关键发现容易被忽略

- 具体位置：§4.4 (pages 6-7)，约 1.5 页内覆盖 scaling pattern、variance analysis、cross-architecture validation、RSFT scaling behavior
- 问题：密集堆积了大量数字（"variance compression 32.6× at 1.7B, 7.5× at 4B, 6.5× at 8B"、多个 Spearman ρ 值、confidence intervals、跨架构结果），读者难以区分 primary findings 和 supporting evidence。最重要的发现——evidence tax 的 scale-dependent reversal——淹没在统计细节中。
- 建议：拆分为 "4.4 Evidence Tax across Scales" 和 "4.5 Robustness and Variance"，使用小标题组织各子发现。

**W4** [warning] "Evidence tax" 术语 framing 与实际数据不完全匹配

- 具体位置：Abstract (lines 8-11), §1 (page 2), §4.4 (page 6-7), Table 9 (page 13)
- 问题：
  - "Tax" 一词天然暗示 cost/负面效应，但实验显示 1.7B 时 evidence 实际是 **benefit**（tax < 0，即 −5.63pp）
  - 论文用 sign convention "positive = cost, negative = benefit" 来化解，但这在直觉上反直觉——"negative tax" = benefit 不是自然的语义映射
  - Figure 6 展示的是 Ign-F1 bar heights（非 tax 值本身），需要读者自行计算差值
- 建议：考虑使用更中性的术语如 "evidence delta" 或 "evidence impact"，或至少在 Figure 6 中直接展示 tax 值（差值）而非原始 F1 分数。

**W5** [warning] Re-DocRED test set ~20pp performance drop 的解释不充分

- 具体位置：§4.6 (page 8), Table 10 (page 15)
- 问题：Re-DocRED test 比 dev 低约 20pp，论文归因于 annotation density 差异（test 3.47 triples/doc vs dev 12.3）。但：
  - 20pp 是极大的 gap——如果纯粹是 annotation density 导致，是否意味着模型在 sparse-annotation 场景下基本失效？
  - 是否有 domain/entity distribution 差异的贡献？
  - 这对论文 claim 的泛化性有什么影响？（如 evidence tax 在 sparse-annotation setting 下是否仍然成立？）
- 建议：增加按 annotation density 分层的分析，或在 Limitations 中更详细讨论。

---

## 小问题（不影响接收）

- **M1**: Table 2 caption 中 CED 和 EDCR 缩写首次出现未展开全称，需要读者回溯到 §3.4-3.5。建议在 caption 中加注全称。
- **M2**: "co-optimization" 和 "joint optimization" 在正文中交替使用，建议统一术语。
- **M3**: Appendix E (Controlled Evaluation Subset) 包含重要方法论信息（matched@2048 fair evaluation 的定义），这对理解 evidence tax 至关重要，考虑将核心定义移入正文或至少在正文中更明确地引用。
- **M4**: Figure 4 的 dual y-axis（Rel-F1 和 Evi-F1）如果量级差异大，可能产生视觉误导。建议明确标注刻度或使用 normalized 展示。

---

## Missing References

1. **Multi-task gradient conflict**: Yu et al. (2020, NeurIPS) "Gradient Surgery for Multi-Task Learning" — 直接相关于 extraction-evidence decoupling 的 gradient-level 解释和潜在解决方案
2. **Reward overoptimization**: Gao et al. (2023) "Scaling Laws for Reward Model Overoptimization" — GRPO 的 catastrophic decoupling 可能是 reward hacking 的 structured-generation 实例
3. **Faithfulness in generation**: Maynez et al. (2020, ACL) "On Faithfulness and Factuality in Abstractive Summarization" — evidence faithfulness 在 NLG 中的理论基础
4. **Attribution measurement**: Rashkin et al. (2023, TACL) "Measuring Attribution in Natural Language Generation Models" — 与 EDCR 的 attribution-measurement 动机高度相关

---

## 主要优势

1. **实验规模在 empirical study 中属高水平**：3 optimization paradigms × 4 model scales (1.7B, 4B, 8B, 14B) × 3 random seeds × 2 datasets (DocRED, Re-DocRED) × cross-architecture (Qwen2.5 + LLaMA-3.1)，实验矩阵覆盖全面
2. **研究问题定义清晰**：evidence-grounded DocRE 中 extraction-evidence trade-off 的研究动机有真实痛点——当前 LLM-based 方法无法同时优化 extraction accuracy 和 evidence faithfulness
3. **EDCR 的 per-relation 诊断价值**：Appendix L (Figure 8) 展示了 per-relation EDCR distribution，揭示了 aggregate metrics 不可见的 pattern——高 EDCR relations 倾向于需要 multi-hop 或 cross-sentence reasoning
4. **Error decomposition 分析有深度**：Appendix K (Table 15) 将 RSFT 改进分解为 truncation reduction、hallucination reduction、duplication elimination 三个维度，为方法选择提供了 actionable 指导
5. **Cross-architecture 泛化一致性强**：LLaMA-3.1-8B 与 Qwen2.5-8B 在 evidence tax pattern、RSFT gain、EDCR 趋势上均一致（Table 3, Appendix H）
6. **Qualitative analysis 信息量高**：Appendix M 的三个 case study（evidence quality、GRPO format gaming、EDCR diagnostics）直观地支撑了定量发现

---

## Questions for Authors

Q1: 如果用 RoBERTa-large-MNLI 替换 DeBERTa-v3 作为 EDCR 的 NLI backbone，EDCR 与 Rel-F1 的 correlation 是否稳定？这是验证 EDCR 作为 NLI-backbone-agnostic 诊断指标的关键实验。

Q2: Evidence tax 在 Appendix K 分解后，truncation 贡献了多大比例？具体来说，如果只看 non-truncated outputs，1.7B 的 evidence tax 是否仍然存在？

Q3: DPO β=0.01 和 β=0.5 下的 EDCR 是否仍显示 catastrophic decoupling？如果 β 影响大，Table 1 的定性分类需要附加条件。

Q4: RSFT 在 k>1（如 top-3 selection）时表现如何？当前 k=1 可能过于 aggressive，更多候选可能提供 diversity 收益。

Q5: 论文如何解释 14B 的 cross-seed variance 异常高（Appendix D, Table 7）——这是否暗示 evidence tax 在更大规模上不稳定？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-25T22:40:05.112440+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall: 3.5 (Borderline Conference)**\n**Soundness: 3.0/5 | Excitement: 3.5/5 | Reproducibility: 4/5 | Confidence: 4/5**\n\n### 主要优势\nS1. 研究问题定义精准，实用价值高。\nS2. EDCR 指标设计巧妙且验证充分（partial correlation 仅降 0.15%，permutation test p<0.0001，per-relation n=76 ρ=-0.79）。\nS3. 三范式系统对比框架有参考价值（GRPO/DPO/RSFT 统一 baseline 和评估协议）。\nS4. 跨模型家族和跨规模验证增强可推广性。\nS5. 附录质量高（14 个附录覆盖消融、统计、error decomposition、定性分析）。\n\n### Must-Fix\n**N1** [critical] n=3 seeds 统计效力不足——sign test p=0.0625 不显著，CI 跨零，1.7B s42 是最强 seed (+3.22pp above mean) 有 disproportionate influence。建议增加 seeds 或弱化 claim 语言。\n\n**N2** [critical] GRPO QLoRA vs bf16 存在 lr-quantization confound——lr、batch size 可能不同，collapse 可能是 lr 过大 + quantization 联合效应。bf16 G=4 补充实验仅控制 group size，未控制 lr。\n\n**N3** [critical] DPO 仅 β=0.1，\"spectrum\" 结论缺乏支撑——不同 β 下行为可能截然不同（β=0.5 可能更接近 RSFT，β=0.01 可能更接近 GRPO collapse）。\n\n### Should-Fix\n**W1** CED contrastive 设计附加价值不明确（vs flat-NLI 仅 0.02pp）。\n**W2** 14B 仅 1 seed SFT baseline，scaling claim 不可靠。\n**W3** RSFT 共享 SFT checkpoint 导致方差比较不公平（SFT = full randomness, RSFT = fixed-base）。\n**W4** Test-set evidence tax 在 8B 出现反转（dev +0.04pp → test -1.17pp），解释不充分。\n\n### Minor\nM1: Abstract 首句缺引用。M2: Figure 4 y轴字号。M3: §2.3 标题误导。M4: RSFT mechanistic explanation 应在 future work 突出。\n\n### Questions\nQ1: EDCR 仅在 TP triples 上计算的变体结果？\nQ2: 是否测过 RoBERTa-large-MNLI 或 prompt-based NLI？\nQ3: RSFT k>1 效果？（k=3 已在 Appendix B 测试，Ign-F1 下降 1.02pp）\nQ4: DPO 用 Evi-F1 而非 CED 构造 preference pairs 的 decoupling 行为？\n\n### Missing References\n- Xu et al. (2024) \"Towards Faithful Document-Level Relation Extraction\"\n- DPO β sensitivity 相关文献\n\n---\n\n请逐条回应以上每个要点。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall: 3.5 (Borderline Conference)**\n**Soundness: 3.0/5 | Excitement: 3.5/5 | Reproducibility: 4/5 | Confidence: 4/5**\n\n### 主要优势\nS1. 研究问题定义精准，实用价值高。\nS2. EDCR 指标设计巧妙且验证充分（partial correlation 仅降 0.15%，permutation test p<0.0001，per-relation n=76 ρ=-0.79）。\nS3. 三范式系统对比框架有参考价值（GRPO/DPO/RSFT 统一 baseline 和评估协议）。\nS4. 跨模型家族和跨规模验证增强可推广性。\nS5. 附录质量高（14 个附录覆盖消融、统计、error decomposition、定性分析）。\n\n### Must-Fix\n**N1** [critical] n=3 seeds 统计效力不足——sign test p=0.0625 不显著，CI 跨零，1.7B s42 是最强 seed (+3.22pp above mean) 有 disproportionate influence。建议增加 seeds 或弱化 claim 语言。\n\n**N2** [critical] GRPO QLoRA vs bf16 存在 lr-quantization confound——lr、batch size 可能不同，collapse 可能是 lr 过大 + quantization 联合效应。bf16 G=4 补充实验仅控制 group size，未控制 lr。\n\n**N3** [critical] DPO 仅 β=0.1，\"spectrum\" 结论缺乏支撑——不同 β 下行为可能截然不同（β=0.5 可能更接近 RSFT，β=0.01 可能更接近 GRPO collapse）。\n\n### Should-Fix\n**W1** CED contrastive 设计附加价值不明确（vs flat-NLI 仅 0.02pp）。\n**W2** 14B 仅 1 seed SFT baseline，scaling claim 不可靠。\n**W3** RSFT 共享 SFT checkpoint 导致方差比较不公平（SFT = full randomness, RSFT = fixed-base）。\n**W4** Test-set evidence tax 在 8B 出现反转（dev +0.04pp → test -1.17pp），解释不充分。\n\n### Minor\nM1: Abstract 首句缺引用。M2: Figure 4 y轴字号。M3: §2.3 标题误导。M4: RSFT mechanistic explanation 应在 future work 突出。\n\n### Questions\nQ1: EDCR 仅在 TP triples 上计算的变体结果？\nQ2: 是否测过 RoBERTa-large-MNLI 或 prompt-based NLI？\nQ3: RSFT k>1 效果？（k=3 已在 Appendix B 测试，Ign-F1 下降 1.02pp）\nQ4: DPO 用 Evi-F1 而非 CED 构造 preference pairs 的 decoupling 行为？\n\n### Missing References\n- Xu et al. (2024) \"Towards Faithful Document-Level Relation Extraction\"\n- DPO β sensitivity 相关文献\n\n---\n\n请逐条回应以上每个要点。"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-25T22:40:27.508026+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22395
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-25T22:40:27.710024+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall: 3.5 (Borderline Conference)**\n**Soundness: 3.5/5 | Excitement: 3.0/5 | Reproducibility: 4/5 | Confidence: 4/5**\n\n### 主要优势\n1. 实验规模高水平（3 paradigms × 4 scales × 3 seeds × 2 datasets × cross-architecture）\n2. 研究问题定义清晰——extraction-evidence trade-off 有真实痛点\n3. EDCR 的 per-relation 诊断价值（Figure 8, Appendix L）\n4. Error decomposition 分析有深度（Appendix K, Table 15）\n5. Cross-architecture 泛化一致性强\n6. Qualitative analysis 信息量高（Appendix M）\n\n### Must-Fix\n**N1** [critical] 核心新颖性不足——\n(1) RSFT = STaR + CED 筛选，是 engineering contribution 非 methodological innovation\n(2) CED vs flat-NLI 仅差 0.02pp，contrastive formulation \"not essential\"\n(3) EDCR 是简单比率（1 − precision(evidence|relation)），需跨 backbone 验证\n(4) Evidence tax 主要来自 truncation/duplication（Appendix K），非 evidence 固有代价——应区分 \"truncation-induced tax\" 和 \"information-interference tax\"\n\n**N2** [critical] 优化超参数探索不充分——DPO 仅 β=0.1，GRPO 仅 G=8，RSFT 仅 k=1，无超参数敏感性分析支撑 \"gradient methods inherently decouple\" 归因。\n\n**N3** [critical] Conclusion 过于简短（~60 words, 3 句话）——缺 broader implications、future directions、connection to wider literature。对 empirical study 而言 Conclusion 是 reviewer 判断工作意义的关键段落。\n\n### Should-Fix\n**W1** Related Work 遗漏 MTL / gradient conflict 文献（PCGrad Yu et al. 2020, Reward overoptimization Gao et al. 2023）。\n**W2** EDCR 与 CED 共享 NLI backbone，存在 circular dependency 风险——需跨 backbone 稳定性验证。\n**W3** §4.4 信息密度过高——scaling pattern、variance、cross-arch 堆叠在 1.5 页内，建议拆分。\n**W4** \"Evidence tax\" 术语 framing 反直觉——negative tax = benefit 不自然，建议改 \"evidence delta/impact\"。\n**W5** Re-DocRED test 20pp drop 归因于 annotation density，但解释不充分——是否意味模型在 sparse-annotation 下基本失效？\n\n### Minor\nM1: Table 2 caption 缩写未展开。M2: \"co-optimization\"/\"joint optimization\" 未统一。M3: Appendix E 的 matched@2048 定义应移入正文。M4: Figure 4 dual y-axis 可能视觉误导。\n\n### Missing References\n1. Yu et al. (2020, NeurIPS) \"Gradient Surgery for Multi-Task Learning\"\n2. Gao et al. (2023) \"Scaling Laws for Reward Model Overoptimization\"\n3. Maynez et al. (2020, ACL) \"On Faithfulness and Factuality in Abstractive Summarization\"\n4. Rashkin et al. (2023, TACL) \"Measuring Attribution in NLG Models\"\n\n### Questions\nQ1: RoBERTa-large-MNLI 替换 EDCR NLI backbone 后 correlation 是否稳定？\nQ2: Truncation 对 evidence tax 贡献多大？non-truncated outputs 的 1.7B tax 是否仍存在？\nQ3: DPO β=0.01 和 β=0.5 的 EDCR？\nQ4: RSFT k>1 效果？\nQ5: 14B cross-seed variance 异常高是否暗示 evidence tax 在更大规模不稳定？\n\n---\n\n请逐条回应以上每个要点。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall: 3.5 (Borderline Conference)**\n**Soundness: 3.5/5 | Excitement: 3.0/5 | Reproducibility: 4/5 | Confidence: 4/5**\n\n### 主要优势\n1. 实验规模高水平（3 paradigms × 4 scales × 3 seeds × 2 datasets × cross-architecture）\n2. 研究问题定义清晰——extraction-evidence trade-off 有真实痛点\n3. EDCR 的 per-relation 诊断价值（Figure 8, Appendix L）\n4. Error decomposition 分析有深度（Appendix K, Table 15）\n5. Cross-architecture 泛化一致性强\n6. Qualitative analysis 信息量高（Appendix M）\n\n### Must-Fix\n**N1** [critical] 核心新颖性不足——\n(1) RSFT = STaR + CED 筛选，是 engineering contribution 非 methodological innovation\n(2) CED vs flat-NLI 仅差 0.02pp，contrastive formulation \"not essential\"\n(3) EDCR 是简单比率（1 − precision(evidence|relation)），需跨 backbone 验证\n(4) Evidence tax 主要来自 truncation/duplication（Appendix K），非 evidence 固有代价——应区分 \"truncation-induced tax\" 和 \"information-interference tax\"\n\n**N2** [critical] 优化超参数探索不充分——DPO 仅 β=0.1，GRPO 仅 G=8，RSFT 仅 k=1，无超参数敏感性分析支撑 \"gradient methods inherently decouple\" 归因。\n\n**N3** [critical] Conclusion 过于简短（~60 words, 3 句话）——缺 broader implications、future directions、connection to wider literature。对 empirical study 而言 Conclusion 是 reviewer 判断工作意义的关键段落。\n\n### Should-Fix\n**W1** Related Work 遗漏 MTL / gradient conflict 文献（PCGrad Yu et al. 2020, Reward overoptimization Gao et al. 2023）。\n**W2** EDCR 与 CED 共享 NLI backbone，存在 circular dependency 风险——需跨 backbone 稳定性验证。\n**W3** §4.4 信息密度过高——scaling pattern、variance、cross-arch 堆叠在 1.5 页内，建议拆分。\n**W4** \"Evidence tax\" 术语 framing 反直觉——negative tax = benefit 不自然，建议改 \"evidence delta/impact\"。\n**W5** Re-DocRED test 20pp drop 归因于 annotation density，但解释不充分——是否意味模型在 sparse-annotation 下基本失效？\n\n### Minor\nM1: Table 2 caption 缩写未展开。M2: \"co-optimization\"/\"joint optimization\" 未统一。M3: Appendix E 的 matched@2048 定义应移入正文。M4: Figure 4 dual y-axis 可能视觉误导。\n\n### Missing References\n1. Yu et al. (2020, NeurIPS) \"Gradient Surgery for Multi-Task Learning\"\n2. Gao et al. (2023) \"Scaling Laws for Reward Model Overoptimization\"\n3. Maynez et al. (2020, ACL) \"On Faithfulness and Factuality in Abstractive Summarization\"\n4. Rashkin et al. (2023, TACL) \"Measuring Attribution in NLG Models\"\n\n### Questions\nQ1: RoBERTa-large-MNLI 替换 EDCR NLI backbone 后 correlation 是否稳定？\nQ2: Truncation 对 evidence tax 贡献多大？non-truncated outputs 的 1.7B tax 是否仍存在？\nQ3: DPO β=0.01 和 β=0.5 的 EDCR？\nQ4: RSFT k>1 效果？\nQ5: 14B cross-seed variance 异常高是否暗示 evidence tax 在更大规模不稳定？\n\n---\n\n请逐条回应以上每个要点。"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-25T22:40:29.020202+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1310
}
```

</details>

---


### Assistant

_source line 370 · 2026-05-25T22:40:31.633619+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 30

## Round 30

2 recorded events


### User

_source line 371 · 2026-05-25T22:40:34.156588+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：Overall 3.5/5 (Borderline Conference)。实验规模在 empirical study 中属高水平（3 paradigms × 4 scales × 3 seeds × 2 datasets × cross-architecture），但三个 Must-Fix 问题影响接收决定：

1. **N1 核心新颖性不足**——RSFT=STaR 应用、CED≈flat-NLI（仅差 0.02pp）、EDCR 是简单比率；且 evidence tax 在小模型上主要由 truncation 驱动（Appendix K），"tax" framing 有误导性
2. **N2 超参数探索不充分**——DPO 仅 β=0.1、GRPO 仅 G=8，decoupling 可能是特定超参数 regime 的行为而非 gradient optimization 的固有性质
3. **N3 Conclusion 仅 ~60 words**——缺少 broader implications 和 future directions

五个 Should-Fix（related work 遗漏 gradient conflict 文献、EDCR-CED circular dependency、§4.4 信息过载、terminology framing、Re-DocRED 20pp drop 解释不足）和四条 Missing References 一并列出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 372 · 2026-05-25T22:40:46.988517+00:00_

交叉分享已发出，等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。收到后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 373 · 2026-05-25T22:42:25.931282+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### 主要优势

[AGREE] R1-S1: 研究问题定义精准。Evidence-grounded DocRE 中 extraction-evidence trade-off 确实是一个有实际意义的研究空缺。

[AGREE] R1-S2: EDCR 验证充分。我在自己的审稿中也肯定了 EDCR 的 per-relation 诊断价值（Appendix L, Figure 8）。但我同时指出了 EDCR 与 CED 共享 NLI backbone 的 circular dependency 风险——R1 未提及此点（见我的 W2）。partial correlation 控制了 TP 但未控制 NLI backbone bias。

[AGREE] R1-S3: 三范式统一对比框架确实有参考价值。Table 1 的定性分类清晰，统一了 baseline（共享 SFT checkpoint）和评估协议。

[AGREE] R1-S4: 跨架构验证（Qwen2.5 + LLaMA-3.1-8B）增强可推广性。我在自己的优势部分也特别肯定了这一点。

[AGREE] R1-S5: 附录质量高。14 个 appendix sections 涵盖面广，尤其 Appendix K (error decomposition) 和 Appendix M (qualitative analysis) 信息量高。

---

### Must-Fix

[AGREE] R1-N1: n=3 seeds 统计效力不足

同意这是关键方法论弱点。补充以下证据：

1. **Appendix D (Table 7)** 的 95% CI 确实跨零：论文自己报告了置信区间。当 CI 跨零时，evidence tax 的方向性 claim 在统计上不显著。
2. **我的补充关注**：不仅是 1.7B 的 s42 issue——14B 的 cross-seed variance 也异常高（Table 7 显示 14B CI 更宽），暗示 evidence tax 在更大规模上可能不稳定。
3. **与 R1 的分歧**：R1 建议"增加 seeds 或弱化 claim 语言"。我认为增加 seeds 是理想方案但可能不现实（14B 训练成本高）；更可行的是在正文 §4.4 中用 hedging language 替代当前的断言式表述（如 "the evidence tax reverses" → "our 3-seed estimates suggest the evidence tax may reverse"）。

[AGREE] R1-N2: GRPO QLoRA vs bf16 confound

同意存在实验混淆。具体证据：

1. **Table 4 (Appendix A)** 显示 GRPO 使用 QLoRA 4-bit quantization + r=64，而 SFT/RSFT 使用 full-precision LoRA。这不是 controlled comparison——quantization 本身可能影响 gradient landscape 的稳定性。
2. **bf16 G=4 实验的局限**：论文在 Table 14 (Appendix) 提供了 bf16 补充实验，但 R1 正确指出它控制了 group size 而未控制 lr。GRPO collapse 可能是 lr × quantization 的交互效应，而非 GRPO 范式固有的 decoupling。
3. **我的补充**：不过，DPO 也展示了 substantial decoupling（Table 2: Rel-F1 drops 33-37%，§4.2），且 DPO 使用 offline 数据无需 online sampling——这意味着 gradient-based optimization 导致 decoupling 的 claim 不完全依赖于 GRPO 的 QLoRA 设置。GRPO collapse 的 severity 可能被 confound 放大，但 decoupling 方向性可能仍成立。

[AGREE] R1-N3: DPO β=0.1 单点实验

完全同意，这也是我自己 Must-Fix N2 的核心观点。补充：

1. DPO 的 β 直接控制 KL constraint 强度。β=0.1 是较小的值（弱约束），允许策略大幅偏离 reference——这可能 maximize decoupling。β=0.5 或 β=1.0 可能产生更保守的行为，减轻 decoupling。
2. 论文的 "decoupling spectrum"（Table 1）将 DPO 定性归类为 "Partial decoupling"——但这个归类完全基于 β=0.1 的单点观测。如果 β=0.5 下 DPO 表现更像 RSFT（低 decoupling），Table 1 的框架就需要重大修正。
3. **与 R1 一致**：R1 说 "β=0.01 可能更接近 GRPO collapse"——这是合理推测。低 β 意味着几乎无 KL 约束，策略可以任意偏移，更容易 exploit reward 导致 decoupling。

---

### Should-Fix

[AGREE] R1-W1: CED contrastive 设计附加价值不明确

完全同意。我在 Must-Fix N1 中将此列为核心新颖性不足的证据之一。§3.4 末段自己承认 "the contrastive formulation is not essential"——0.02pp 的差异在 3-seed variance 范围内不显著。CED 作为独立 contribution 不成立。

[AGREE] R1-W2: 14B 仅 1 seed SFT baseline

同意。14B 数据点对 scaling claim 至关重要（是最大规模），但只有 1 seed 的 SFT baseline 使得 evidence tax 的 estimation 在该规模上不可靠。Table 3 的 14B 行应标注 "single seed" 的 caveat。论文在 Table 3 脚注提到 "14B shows dev-set sign reversal"，但对 single-seed limitation 不够显眼。

[REBUT] R1-W3: RSFT 共享 SFT checkpoint 导致方差比较不公平

部分反驳。R1 的观点是：SFT 方差来自 full training randomness，RSFT 方差仅来自 post-SFT 阶段，两者不可比。但我认为这个比较有其合理性：

1. **论文的 variance comparison 回答的是实际部署问题**：practitioners 关心的是 "从头训练一个 SFT model" vs "从头训练 SFT 然后做 RSFT" 的 end-to-end variance。后者包含 SFT 阶段的 randomness（论文用 3 个不同 SFT seed 初始化 RSFT），所以 RSFT 的 variance 确实包含了 SFT 阶段的变异。
2. **但 R1 的核心关注仍然有效**：Table 7 (Appendix D) 的 variance compression ratio 可能被夸大——如果 RSFT 从 **同一个** SFT checkpoint 出发（论文在 §3.2 说 "shared SFT initialization"），那么 RSFT 的 cross-seed variance 确实不含 SFT 初始化 randomness。这是一个 **重要澄清点**：论文需要明确说明 RSFT 的 3 个 seeds 是 3 个不同 SFT seeds → 各自 RSFT，还是 1 个 SFT seed → 3 个 RSFT runs。
3. **我的判断**：从 §4.4 "RSFT seeds from a shared SFT checkpoint yield standard deviations of 0.09pp at 1.7B..." 的措辞看，RSFT 的 3 seeds 似乎来自 **同一个** SFT checkpoint。如果如此，R1 的 concern 完全成立——variance compression ratio 被人为缩小，因为 RSFT 未经历 SFT 阶段的 randomness。建议论文补充 "3 different SFT checkpoints → RSFT" 的 variance 数据。

[AGREE] R1-W4: Test-set evidence tax 在 8B 反转

同意需要更好解释。我在自己的 W5 中也提出了类似关注（Re-DocRED test 20pp drop）。具体补充：

1. Dev +0.04pp → test −1.17pp 的 sign reversal 在 n=3 seeds、CI 跨零的前提下（R1-N1），实际上 neither 方向是统计显著的。
2. 但论文 §4.4 的叙述语气暗示 dev 和 test 的 pattern 是一致的——8B 的反转挑战了这一叙述。
3. 可能解释：test set 的 entity/relation distribution 与 dev 不同，evidence 在某些 relation types 上更 costly。Appendix L 的 per-relation EDCR 分析如果能在 test set 上复现，可以 shed light。

---

### Minor

[AGREE] R1-M1: Abstract 首句 "surpasses encoder baselines" 缺引用。应 cite 至少一个 LLM-based DocRE 工作（如 AutoRE 或 ReFiRE）来 substantiate。

[AGREE] R1-M2: Figure 4 y-axis 字号偏小，在打印版本中可能难以辨认。

[REBUT] R1-M3: §2.3 标题 "Evidence Faithfulness and Rejection Sampling" 不算误导。该 section 确实同时覆盖了 NLI-based faithfulness 评估方法（Laban et al., 2022; Zhang et al., 2024）和 rejection sampling/self-improvement 方法（STaR, DeepSeek-R1），并论述了两者的理论连接——RSFT 正是将 faithfulness evaluation 作为 rejection criterion。标题反映了 section 的两个主题及其连接。不过，为清晰起见，可改为 "Evidence Faithfulness Evaluation and Rejection-Based Training"。

[AGREE] R1-M4: RSFT mechanistic explanation（当前在 Limitations 末段）应在 future work 中更突出。Limitations 提到 "we have not isolated whether RSFT's advantage stems primarily from removing low-quality training examples, from implicit regularization through candidate diversity, or from both"——这是一个值得独立段落讨论的 open question。

---

### Questions

R1-Q1 (EDCR on TP-only triples): 有价值的诊断问题。当前 EDCR 在 all predicted triples 上计算（包含 FP triples），TP-only variant 可以隔离 "evidence quality for correct predictions" vs "evidence quality overall"。论文 Appendix L 的 partial correlation 部分控制了 TP，但未直接报告 TP-only EDCR 值。

R1-Q2 (替代 NLI 模型): 这与我的 W2 (EDCR-CED circular dependency) 直接相关。我强烈支持此问题——跨 NLI backbone 验证是 EDCR 作为 robust 诊断指标的必要条件。

R1-Q3 (RSFT k>1): R1 自己已注意到 Appendix B 报告了 k=3 结果（Ign-F1 下降 1.02pp）。这说明 top-1 selection 是 RSFT 性能的关键——更 aggressive 的筛选反而更好。这个结果支持了 RSFT "quality over quantity" 的设计哲学。

R1-Q4 (DPO with Evi-F1 scoring): 有趣的实验设计问题。如果 DPO 用 Evi-F1（而非 CED）构造 preference pairs，reward signal 更直接 align with evidence quality，decoupling 可能减轻——这可以测试 "DPO decoupling 是范式固有问题 vs reward signal 设计问题"。

---

### Missing References

[AGREE] Xu et al. (2024) "Towards Faithful Document-Level Relation Extraction": 标题直接相关，如果确实发表且未被引用，是显著遗漏。

[AGREE] DPO β sensitivity 文献: 结合 R1-N3 和我的 N2，DPO 超参数敏感性的 prior work（如 Tunstall et al. 2023 的 DPO 消融）应被讨论。

---

### 综合评价

R1 和 R2（本人）的审稿意见高度一致：

**共识点**: (1) n=3 seeds 统计效力不足；(2) DPO β 单点实验削弱 decoupling spectrum claim；(3) CED vs flat-NLI 差异微乎其微；(4) 实验规模和附录质量高。

**R2 补充的 R1 未覆盖的关键问题**: (1) EDCR-CED 共享 NLI backbone 的 circular dependency；(2) evidence tax 的 truncation-vs-interference 分解不充分；(3) Conclusion 过短；(4) multi-task gradient conflict 文献遗漏；(5) "evidence tax" 术语 framing 问题。

**R1 提出的 R2 未覆盖的关键问题**: (1) GRPO QLoRA vs bf16 confound（N2）——这是我遗漏的有价值的 methodological concern；(2) RSFT 共享 SFT checkpoint 的 variance 比较公平性（W3）。

**分歧**: 仅在 §2.3 标题是否误导（M3）和 W3（RSFT variance）上有细微分歧。

**Overall 一致**: 两位 reviewer 均给出 3.5 (Borderline Conference)。论文的实证贡献扎实但方法新颖性不足，更适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 374 · 2026-05-25T22:42:31.070057+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 32

## Round 32

48 recorded events


### User

_source line 375 · 2026-05-25T22:42:36.631522+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 所有要点的逐条回应并提交给 Director。

核心结论：R1 和 R2 意见高度一致（Overall 均 3.5），在 n=3 seeds 统计效力、DPO β 单点实验、CED 微效三个核心问题上完全共识。我对 R1 的 W3（RSFT variance 比较公平性）做了部分反驳——认为 end-to-end variance 比较有一定合理性，但同意需要澄清 RSFT seeds 是否来自同一 SFT checkpoint。R1 提出的 GRPO QLoRA confound (N2) 是我原始审稿中遗漏的有价值观点，已在回应中 acknowledge。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-25T22:42:53.716083+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-25T22:42:55.675892+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 1959
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-25T22:42:55.828132+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-25T22:42:55.828644+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-25T22:43:15.745421+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-25T22:43:16.247870+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T22:30:47.440354+00:00\", \"completed_at\": \"2026-05-25T22:34:18.143480+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 3 (CED scoring example) 内部文字偏小，实体对标签和公式文字约为正文 60-65%，建议放大至 ≥70%\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4 (Decoupling spectrum) 图例文字偏小，且放在绘图区域内部，可能被数据线遮挡；建议移至图外或放大\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Appendix 单页含 4 张表 (Tables 4-7)，信息密度极高；Table 6 为全宽表列数多，数字密集但格式正确无溢出\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 7 三子图 (GRPO dynamics) 的 y 轴标签和刻度文字偏小，建议统一放大\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"末页内容约占 70-75%，底部约 1/4 空白；为 appendix 末页含 AI Assistants 声明，不影响审稿印象\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 整体清晰专业，蓝色标注 evidence 句子，色彩方案一致；caption 自包含性好\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 主结果表使用 booktabs 风格，最优结果加粗，格式规范；footnote 字号偏小但符合 ACL 模板标准\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 5 (Inference-time evidence tax) 使用正负值条形图，红/蓝对比清晰，误差条可辨\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 8}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-25T22:43:16.248405+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-25T22:43:16.248673+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-25T22:43:17.755033+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-25T22:43:18.208099+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-25T22:43:18.208563+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-25T22:43:18.710819+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_reports/round_3.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-25T22:43:18.911997+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_round_4/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_round_4/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-25T22:43:18.962729+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/_pdf_images/submitted_p16.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-25T22:44:00.166438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-25T22:44:00.518844+00:00_

1	- id: "W1"
2	  summary: "GRPO QLoRA vs bf16 confounded variables — quantization and group size not isolated"
3	  category: experiment
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 1
7	  last_seen_round: 3
8	  mentions:
9	    - {round: 1, reviewers: "R1,R2", note: "Cannot support causal attribution of decoupling to QLoRA"}
10	    - {round: 2, reviewers: "R1,R2", note: "R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor."}
11	    - {round: 3, reviewers: "R1,R2", note: "Table 3 shows QLoRA G=4 vs bf16 G=8 — two variables changed simultaneously. §4.3 attribution unsupported. Need bf16 G=4 or QLoRA G=8 control. Both AGREE Must-Fix."}
12	  action_items:
13	    - {round: 1, action: "Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect", assigned_to: "Agent", status: "done"}
14	    - {round: 1, action: "Downgrade causal claim to observational", assigned_to: "Paper Agent", status: "done"}
15	    - {round: 2, action: "Deepen GRPO mechanism analysis with reward hacking lit + mechanistic chain", assigned_to: "Paper Agent", status: "done"}
16	    - {round: 3, action: "Run GRPO bf16 G=4 experiment (r3_grpo_bf16_g4). Config from plan_011 bf16 G=8, only G→4. cuda:1. Previous plan_015 v1/v2/v3 were manual kills not failures.", assigned_to: "Agent", status: "in_progress"}
17	  resolution: ""
18	  resolution_round: null
19	
20	- id: "W2"
21	  summary: "All results dev-set only, no test set"
22	  category: experiment
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 1
26	  last_seen_round: 2
27	  mentions:
28	    - {round: 1, reviewers: "R1,R2", note: "No CodaLab test results"}
29	    - {round: 2, reviewers: "R1,R2", note: "Test set results now exist (Table 9). Method ranking preserved (ρ=1.0)."}
30	  action_items:
31	    - {round: 1, action: "Add test set evaluation for all scales", assigned_to: "Agent+User", status: "don
…[truncated 23860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-25T22:44:00.519403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_reports/round_3.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_reports/round_3.md"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-25T22:44:00.620480+00:00_

1	---
2	round: 3
3	review_mode: fresh
4	overall_score: 3.5 - Borderline Conference
5	timestamp: 2026-05-24T23:19:34.779441+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: True
9	---
10	
11	# Round 3 审稿报告（修订版——整合双向交叉回应）
12	
13	## Summary
14	
15	本文研究 evidence-grounded document-level relation extraction 中训练方法对 relation extraction 与 evidence grounding 耦合度的影响。提出 RSFT（Rejection Sampling Fine-Tuning）+ CED scoring pipeline，在 Qwen2.5 (1.7B–14B) 和 LLaMA-3.1-8B 上系统比较 SFT/RSFT/GRPO/DPO 四种训练范式。核心发现：(1) evidence-grounded 训练引入可量化的 accuracy tax；(2) RSFT 维持 RE-evidence coupling 而 GRPO/DPO 产生 decoupling；(3) RSFT 降低 seed variance。论文定位为实证研究。
16	
17	## Strengths
18	
19	1. **系统性实验覆盖**：5 model scales × 4 训练范式 + cross-architecture (LLaMA) 验证。在 DocRE + evidence grounding 领域属于最全面的实证比较。
20	
21	2. **Decoupling spectrum 概念有洞察力**：按 RE-evidence coupling 程度排列训练方法（SFT → RSFT → DPO → GRPO），为社区理解 multi-objective training dynamics 提供了有用的 conceptual framework。
22	
23	3. **Evidence tax 量化分析**：将 evidence grounding 成本/收益分离为 training-time (+0.25±0.47pp) 和 inference-time (−5.63pp at matched tokens) 两个维度，quantification 有实用价值。
24	
25	4. **Re-DocRED 测试集验证**：Table 9 所有 5 个 scale dev-test method ranking 完全一致（Spearman ρ=1.0），增强结论可靠性。
26	
27	5. **充分的 ablation 设计**：random selection baseline、matched@2048 evaluation、no-evidence SFT、CED vs flat-NLI——实验设计思路严谨。
28	
29	6. **统计方法意识**：χ² CI、Cohen's d、permutation test、partial correlation 等多层验证，虽然部分证据力度不足，但体现了正确的方法论方向。
30	
31	## Weaknesses
32	
33	### Must-Fix（两位 Reviewer 共识）
34	
35	**[W-MF1] GRPO QLoRA vs bf16 存在多个未隔离的混淆变量**
36	- Table 3: QLoRA G=4 vs bf16 G=8 同时改变 quantization 和 group size
37	- R1 补充：effective input batch 也不同（QLoRA: batch=4×grad_accum=16=64 unique docs vs bf16: batch=8×grad_accum=4=32），影响 gradient estimation quality
38	- §4.3 "confirming quantization precision rather than group size as the primary factor" 缺乏任何控制实验
39	- **要求**：增加 bf16 G=4 或 QLoRA G=8 控制组；若不可行，将结论降级为 "quantization and/or group size and/or batch configurati
…[truncated 8501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-25T22:44:33.016357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-25T22:44:33.118438+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{xcolor}
16	\usepackage{multirow}
17	\usepackage{subcaption}
18	\usepackage{enumitem}
19	\usepackage{url}
20	
21	\graphicspath{{../../figures/paper/}}
22	
23	\title{Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{sections/abstract}
31	\input{sections/introduction}
32	\input{sections/related_work}
33	\input{sections/method}
34	\input{sections/experiments}
35	\input{sections/conclusion}
36	\input{sections/limitations}
37	
38	\bibliography{references}
39	
40	\appendix
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-25T22:44:39.947801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-25T22:44:40.249247+00:00_

1	\begin{abstract}
2	Large Language Model (LLM)-based Document-level Relation Extraction (DocRE) now matches or exceeds encoder baselines in extraction accuracy, yet outputs bare relation triplets without identifying supporting sentences. Encoder-based evidence methods (SAIS, DREEAM) provide evidence but trail LLM approaches in accuracy, creating a gap between extraction performance and verifiability. We study evidence-grounded DocRE as structured generation and compare Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT) across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax (extraction cost of generating evidence) is scale-dependent: beneficial at 1.7B ($-$5.63pp dev Ign-F1) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B; positive $=$ cost). Gradient-based optimization amplifies evidence-extraction competition (GRPO catastrophic, DPO gradual), while RSFT with NLI-based scoring avoids decoupling through output filtering rather than gradient pressure. We define the Evidence-Decoupling Ratio (EDCR) to quantify extraction-evidence misalignment, validated at per-relation level ($\rho{=}{-}0.79$, $n{=}76$, $p{<}0.001$). Our 1.7B RSFT model (51.19 Ign-F1) approaches 8B Supervised Fine-Tuning (SFT) performance (50.19) at 4.7$\times$ fewer parameters. Test-set evaluation preserves model ranking across all scales (Spearman $\rho{=}1.0$)\footnote{Code and data are available at \url{https://anonymous.4open.science/r/faith-evidence-ie-18BD/}.}.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-25T22:44:40.249634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-25T22:44:40.722618+00:00_

1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{xu2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy, yet every one outputs bare relation triplets $(e_h, r, e_t)$ without indicating \emph{which sentences} support each prediction.
6	Without evidence, a clinician reviewing a ten-page case report must manually locate the sentences that support each extracted drug interaction, a bottleneck that undermines trust in automated extraction.
7	
8	\begin{figure*}[!t]
9	\centering
10	\includegraphics[width=0.92\textwidth]{fig_overview.pdf}
11	\vspace{-2mm}
12	\caption{Evidence-grounded DocRE produces relation triples with supporting sentence indices, unlike standard DocRE which outputs bare triples. RSFT selects the top-$k$ of $N$ CED-scored candidates per document for fine-tuning.}
13	\label{fig:overview}
14	\end{figure*}
15	
16	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
17	Both produce evidence and improve extraction, but encoder methods now trail LLM-based approaches in accuracy.
18	The community faces a gap: the most accurate extractors provide no evidence, while evidence-capable methods are no longer competitive.
19	
20	This gap reflects a structural difference.
21	In encoder methods, evidence retrieval is classification 
…[truncated 3009 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 472
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-25T22:44:40.728212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-25T22:44:41.292557+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate on DocRED~\citep{yao2019docred} (3,053 training / 998 dev documents, 96 relation types) with Re-DocRED~\citep{tan2022redocred} for cross-dataset validation. Our primary model is Qwen3-4B; we also train Qwen3-1.7B, 8B, and 14B to study scale effects, with LLaMA-3.1-8B for cross-family validation. All models use LoRA~\citep{hu2022lora} ($r{=}64$, $\alpha{=}128$) with structured output jointly producing triples and evidence. RSFT selects the top-$k{=}1$ of $N{=}8$ samples by CED score (\S\ref{sec:ced}); GRPO uses group size $G{=}8$ for both configurations; DPO constructs preference pairs from CED-ranked outputs. We report Ign-F1 (primary; ignores training-set triples), Rel-F1, Evi-F1 (TP-only and joint per DREEAM protocol~\citep{ma2023dreeam}), and EDCR (\S\ref{sec:edcr}). Detailed hyperparameters appear in the Appendix.
8	
9	
10	\subsection{Main Results}
11	\label{sec:main_results}
12	
13	Table~\ref{tab:main} presents the primary comparison on Qwen3-4B. The SFT baseline exhibits high seed sensitivity (mean Ign-F1 43.58, std 3.80pp, range 39.74--47.34). Removing evidence entirely (no-evidence SFT, s42) reaches 47.21 Ign-F1.
14	
15	RSFT CED achieves 44.82 Ign-F1 (+1.24 over SFT mean) with substantially lower variance (std 0.51pp), though these reflect different sources of variation (Section~\ref{sec:scaling}). Even the weakest RSFT seed (44.23) exceeds the SFT mean. Evidence quality improves (Evi-F1 80.96 vs.\ 79.61) and coupling tightens (EDCR 0.6487 vs.\ 0.6797). Per-seed results appear in Appendix~\ref{sec:ablation_full}.
16	
17	\begin{table}[t]
18	\centering
19	\caption{Main results on DocRED dev (Qwen3-4B). Ign-F1 shows mean $\pm$ std$^{(\text{seeds})}$; other metrics are same-seed means. Best \textbf{bold}; best evidence-generating \underline{underlined}. Per-seed: Appendix~\ref{tab:ablation_full}.}
20	\label{tab:main}
21	\small
22	\resizebox
…[truncated 12740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 564
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-25T22:44:41.293133+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-25T22:44:41.644603+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We study evidence-grounded document-level relation extraction as structured generation. The evidence tax is scale-dependent: gradient methods amplify extraction-evidence competition while RSFT avoids it through discrete selection, improving extraction across all tested scales; a 1.7B RSFT model approaches 8B SFT at 4.7$\times$ fewer parameters.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-25T22:44:41.745404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-25T22:44:41.795941+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Data and architecture scope.}
4	We evaluate on two datasets (DocRED, Re-DocRED), both derived from Wikipedia; cross-domain evaluation is constrained by the absence of evidence-annotated DocRE datasets beyond Wikipedia, a limitation shared by all prior evidence-aware work (SAIS, DREEAM, EIDER).
5	Evidence tax patterns span two model families (Qwen3, LLaMA) with single hyperparameter settings per RL method; other architectures, scales beyond 14B, or alternative KL coefficients may produce different decoupling behaviors. The decoupling spectrum analysis is conducted entirely at 4B scale; whether the same ordering (GRPO catastrophic $\to$ DPO gradual $\to$ RSFT none) holds at other scales remains unverified.
6	
7	\paragraph{CED scoring sensitivity.}
8	CED scoring operates at the document level using an external NLI model (DeBERTa-v3); sensitivity to other NLI model families is unexplored, and sentence-level CED filtering disrupts co-reference chains (Evi-F1 $-$7.7pp).
9	
10	\paragraph{RSFT mechanistic explanation.}
11	Our explanation for why RSFT avoids decoupling (that discrete selection cannot exploit the extraction-evidence trade-off) is structural rather than empirical. We have not isolated whether RSFT's advantage stems primarily from removing low-quality training examples, from implicit data augmentation through candidate diversity, or from both. Disentangling these factors would require controlled experiments with fixed training data quality but varied selection mechanisms.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-25T22:44:46.767223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-25T22:44:47.119220+00:00_

1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to all linear projections (attention and feed-forward). SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B with LoRA. A dash indicates non-applicable parameters. \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (\S\ref{sec:spectrum}).}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{l@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	\multicolumn{6}{l}{\textit{Model \& Adapter}} \\
16	\quad LoRA rank $r$ / $\alpha$ & 64 / 128 & 64 / 128 & 64 / 128 & 64 / 128 & 64 / 128 \\
17	\quad Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
18	\midrule
19	\multicolumn{6}{l}{\textit{Optimization}} \\
20	\quad Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-5 & 5e-7 \\
21	\quad Batch size (effective) & 16 & 16 & 4 & 1 & 4 \\
22	\quad Gradient accumulation & 4 & 4 & 16 & 1 & 4 \\
23	\quad Epochs / Max steps & 3 / -- & 3 / -- & -- / 100 & -- / 100 & 1, 3\textsuperscript{$\star$} / -- \\
24	\midrule
25	\multicolumn{6}{l}{\textit{RL / Selection}} \\
26	\quad Group size $G$ & -- & -- & 8 & 8 & -- \\
27	\quad KL coeff.\ / $\beta$ & -- & -- & 0.01 & 0.01 & 0.1 \\
28	\quad Candidates $N$ / Top-$k$ & -- & 8 / 1 & -- & -- & 8 / -- \\
29	\midrule
30	\multicolumn{6}{l}{\textit{Data}} \\
31	\quad Max new tokens & 1024 & 1024 & 1024 &
…[truncated 41097 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-25T22:45:20.736075+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-25T22:45:21.188558+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
5	\label{sec:task}
6	
7	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support (Figure~\ref{fig:overview}).
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\columnwidth]{fig_task_example.pdf}
12	\caption{Evidence-grounded DocRE example. Given a document with entity mentions, the model jointly predicts relation triples and supporting evidence sentences in a single structured output.}
13	\label{fig:task_example}
14	\end{figure}
15	
16	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central ph
…[truncated 10336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-25T22:45:21.239439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-25T22:45:21.290127+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Document-Level Relation Extraction}
5	\label{sec:rw_docre}
6	
7	Encoder-based DocRE methods treat relation identification as classification over entity pair representations, with ATLOP \citep{zhou2021atlop} introducing adaptive thresholding and graph-based methods such as GAIN \citep{zeng2020gain} modeling inter-sentence reasoning. A parallel thread adds sentence-level evidence: SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary signal, DREEAM \citep{ma2023dreeam} extended this with dynamic memory-based retrieval, and EIDER \citep{xie2022eider} fuses evidence into the relation classifier. In all three, evidence is binary sentence classification that regularizes the encoder without increasing output length.
8	
9	Recent LLM-based methods recast DocRE as generation: AutoRE \citep{autore2024} uses QLoRA with relation-head-facts decomposition, \citet{xu2024lmrc} frame extraction as reading comprehension, RelPrior \citep{wang2025relprior} leverages relation priors, and \citet{xu2025docksrag} combine retrieval with structured knowledge. These methods match or surpass encoder baselines but produce bare triplets without evidence. At 8B, our RSFT model (54.33 Ign-F1) substantially outperforms both AutoRE (45.22\footnote{AutoRE and RelPrior DocRED dev Ign-F1 from the LLaMA3-8B reproductions by \citet{wang2025relprior}; the original AutoRE paper reports only F1.}) and RelPrior (47.70), while being the only method providing sentence-level evidence. The critical distinction is computational: in encoder methods, evidence retrieval is classification at negligible cost; in LLM-based DocRE, evidence requires generating additional tokens, imposing costs that depend on model capacity and optimization strategy.
10	
11	\subsection{Reinforcement Learning for Structured Generation}
12	\label{sec:rw_rl}
13	
14	GRPO \citep{shao2024deepseekmath} replaces PPO's \citep{schulman2017ppo} value network with
…[truncated 1639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-25T22:46:24.607790+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie && wc -w docs/paper/sections/abstract.tex | head -1",
  "description": "Count words in abstract tex file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie && wc -w docs/paper/sections/abstract.tex | head -1",
    "description": "Count words in abstract tex file"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-25T22:46:25.413126+00:00_

189 docs/paper/sections/abstract.tex
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/review_director_dfe39374

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-25T22:46:25.413640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-25T22:46:26.266611+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_4/submitted.pdf (4.8MB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 852
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-25T22:51:06.881448+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-25T22:51:06.881928+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-25T22:54:08.895105+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "faith-evidence-ie",
  "issues_yaml": "- id: \"W1\"\n  summary: \"GRPO QLoRA vs bf16 confounded variables — quantization, lr, group size not isolated\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Cannot support causal attribution of decoupling to QLoRA\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Table 3 shows QLoRA G=4 vs bf16 G=8 — two variables changed simultaneously. §4.3 attribution unsupported. Need bf16 G=4 or QLoRA G=8 control. Both AGREE Must-Fix.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"bf16 G=4 added (Rel-F1 28.73) — partially helps but reveals group size causes 16.76pp drop (45.49→28.73). lr confound 10× (5e-6 vs 5e-5) described as 'residual' is understated. 'attributable to quantization precision' still too strong. Downgrade to Should-Fix given partial progress.\"}\n  action_items:\n    - {round: 1, action: \"Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade causal claim to observational\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Deepen GRPO mechanism analysis with reward hacking lit + mechanistic chain\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Run GRPO bf16 G=4 experiment\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 4, action: \"Weaken attribution language: 'is attributable to' → 'is primarily consistent with'. Acknowledge lr 10× difference explicitly.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W2\"\n  summary: \"All results dev-set only, no test set\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"No CodaLab test results\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Test set results now exist (Table 9). Method ranking preserved (ρ=1.0).\"}\n  action_items:\n    - {round: 1, action: \"Add test set evaluation for all scales\", assigned_to: \"Agent+User\", status: \"done\"}\n  resolution: \"Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0).\"\n  resolution_round: 2\n\n- id: \"W3\"\n  summary: \"Variance compression claim statistically underpowered + cherry-picking in abstract\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"SFT single seed, +4.92pp lacks stats\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"n=3 per config, σ 95% CI overlapping. Both recommend ≥5 seeds or downgrade.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Only 1.7B χ² CI non-overlapping; other 3 scales overlap. Sign test p=0.0625. 4B Cohen's d=0.46 small. Abstract cherry-picks. Both AGREE Must-Fix.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Contribution 3 downgraded to observation ✓. Caveats added ✓. But §4.4 still devotes ~250 words + precise compression ratios (32.6×, 7.5×, 6.5×) + '36× more predictable' to variance — disproportionate for acknowledged weak evidence. Compress to 2-3 sentences, move ratios to appendix.\"}\n  action_items:\n    - {round: 1, action: \"Run SFT seed43+seed44, compute bootstrap CI\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Downgrade Abstract/Contributions to 'consistently reduces'. Three-layer evidence in appendix.\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n    - {round: 3, action: \"Remove variance as standalone abstract contribution. Downgrade to observation in §4.2 with explicit caveats.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Compress §4.4 variance discussion to 2-3 sentences. Move precise compression ratios to appendix. Remove '36× more predictable' phrasing.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W4\"\n  summary: \"Scaling claim based on limited data points\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"3 points insufficient, 1.7B repetition artifact\"}\n    - {round: 2, reviewers: \"R2\", note: \"4 Qwen + 1 LLaMA still limited for general scaling claim.\"}\n    - {round: 3, note: \"Not directly re-raised in Round 3.\"}\n    - {round: 4, note: \"Not raised. Paper now uses 'scale-dependent' rather than 'non-monotonic'. 5 models across 2 families.\"}\n  action_items:\n    - {round: 1, action: \"Replace 'non-monotonic' with 'scale-dependent', add LLaMA\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5\"\n  summary: \"EDCR shared-component mechanical negative correlation with Rel-F1\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"ρ=-0.965 partially predetermined\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"TP in numerator and denominator. n=7 too small. Request partial correlation, permutation test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"DIVERGENCE. R1 wants per-relation precision partial correlation. R2 considers per-relation n=76 sufficient. Director: WARNING.\"}\n    - {round: 4, note: \"Not re-raised as major. §3.5 now properly caveats cross-method correlation as 'diagnostic pattern rather than independent discovery'. Per-relation analysis (n=76) validated. Partial correlations virtually unchanged.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicate to n=7, per-relation n=76\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade EDCR to diagnostic tool + caveat\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Compute partial correlation + permutation test + similar-TP pairs\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Add partial correlation + permutation test to appendix\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Add per-relation precision partial correlation as additional robustness check\", assigned_to: \"Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5-EDCR-INFLATION\"\n  summary: \"EDCR ρ inflated by non-independent data points and GRPO QLoRA outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"Research Reviewer\", note: \"n=7 ρ=-0.89, n=6 (no QLoRA) ρ=-0.83 p=0.042\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Re-raised: n=6 borderline significant.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion.\"}\n    - {round: 4, note: \"Not raised. EDCR ρ now consistently reported as -0.96 (n=7 methods), -0.9643 (appendix raw). Per-relation ρ=-0.79 (n=76) provides independent validation.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 sans-QLoRA + partial ρ + permutation in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W6\"\n  summary: \"CED ≈ flat-NLI (0.02pp), contrastive formulation adds no measurable value\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Contrastive adds complexity without improvement\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"0.02pp within noise. CED cannot be method contribution.\"}\n    - {round: 3, reviewers: \"R2\", note: \"CED's unique contribution is interpretability, not data selection quality. Confirmed no method contribution language.\"}\n    - {round: 4, note: \"Properly positioned as scoring variant. §3.4 and §4.7 correctly report 0.02pp difference and adopt CED for interpretability only. No contribution language.\"}\n  action_items:\n    - {round: 1, action: \"Remove CED as independent contribution\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Position as scoring variant, no contribution language\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"CED correctly positioned as scoring variant with no contribution language. 0.02pp difference honestly reported.\"\n  resolution_round: 4\n\n- id: \"W7\"\n  summary: \"Training data quantity contradiction (9042 vs 2718)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"k=3 vs k=1 root cause\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining + update section 3.3\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Paper now consistently reports k=1 with ~3000 training samples.\"\n  resolution_round: 2\n\n- id: \"W8\"\n  summary: \"EDCR ρ based on n=6, not significant without outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\"}\n    - {round: 2, reviewers: \"R1\", note: \"n=7 still small, GRPO QLoRA outlier dominance.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion.\"}\n    - {round: 4, note: \"Not raised. Per-relation validation (n=76) provides robust independent evidence.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 remove-outlier + partial correlation + permutation in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W9\"\n  summary: \"'matches' 50.50 vs 50.51 statistically meaningless\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Single seed, 0.01pp < any reasonable variance\"}\n  action_items:\n    - {round: 1, action: \"Change 'matches' to 'approaches'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Changed to 'approaches' throughout.\"\n  resolution_round: 2\n\n- id: \"W10\"\n  summary: \"Encoder baseline comparison selective in metrics presentation\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DREEAM 54.01% buried in text\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 12 emphasizes TP-only Evi-F1, downplays 16-18pp Ign-F1 gap.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n    - {round: 4, note: \"Not raised. Appendix H now explicitly discusses Ign-F1 gap ('16–18pp at 4B, narrowing to <5pp at 14B') and attributes joint Evi-F1 gap to extraction performance.\"}\n  action_items:\n    - {round: 1, action: \"Add encoder baseline comparison table\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Balance discussion: acknowledge Ign-F1 gap\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Encoder comparison balanced with explicit Ign-F1 gap discussion in Appendix H.\"\n  resolution_round: 4\n\n- id: \"W11\"\n  summary: \"GRPO/DPO hyperparameter exploration insufficient — DPO β=0.1 single point\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"GRPO only KL=0.01, DPO only beta=0.1\"}\n    - {round: 2, reviewers: \"R2\", note: \"No KL ablation, no reward normalization test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both strongly agree. DPO β=0.1 → -11pp drop suspicious. Spectrum built on single β.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"4th round recurring. Still only β=0.1. If β=0.01 avoids decoupling, entire DPO segment of spectrum collapses. Upgraded to Must-Fix given persistence. Requires β sweep or explicit scope limitation.\"}\n  action_items:\n    - {round: 1, action: \"Acknowledge in Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add explicit KL caveat to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Run DPO β=0.01 experiment\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Complete β∈{0.01,0.05} sweep OR limit all DPO conclusions to 'under β=0.1'\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W12\"\n  summary: \"Metric format inconsistency\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Percentage vs decimal mixed\"}\n  action_items:\n    - {round: 1, action: \"Unify to percentage format\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Unified to percentage format.\"\n  resolution_round: 2\n\n- id: \"W13\"\n  summary: \"Missing references (LMRC, SummaC, RelPrior, Rationale Verification)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"15 'and others', author mismatches\"}\n    - {round: 2, reviewers: \"R2,R1\", note: \"Missing LMRC, SummaC, RelPrior, Rationale Verification.\"}\n    - {round: 3, note: \"Not raised. Missing references confirmed added.\"}\n  action_items:\n    - {round: 1, action: \"Fix bib errors\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add LMRC, SummaC, RelPrior, Rationale Verification, QuRL\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All missing references added. DeepSeek-R1 and ReST also added in Round 3-4.\"\n  resolution_round: 3\n\n- id: \"W14\"\n  summary: \"1.7B implicit regularization speculation without evidence\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Fair evaluation subset undefined\"}\n  action_items:\n    - {round: 1, action: \"Define fair subset + mechanistic breakdown\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Fair subset defined in Appendix D. Mechanistic breakdown added.\"\n  resolution_round: 2\n\n- id: \"W15\"\n  summary: \"Multi-seed coverage uneven\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Table 3: 3/4 rows single seed\"}\n    - {round: 2, note: \"1.7B/4B/8B/LLaMA now 3-seed. 14B still single seed.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"SFT no-evidence baseline only s42 for 1.7B/8B. 1.7B s42 is strongest seed (+3.22pp above mean).\"}\n    - {round: 4, note: \"Not raised as major. Paper now acknowledges 1.7B s42 as strongest seed in Appendix F. 14B SFT still single seed.\"}\n  action_items:\n    - {round: 1, action: \"Add seeds for 8B/1.7B/LLaMA\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 3, action: \"Add caveat in §4.4: 1.7B/8B no-evidence SFT is single seed (s42), and 1.7B s42 is strongest SFT seed.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W16\"\n  summary: \"Missing multi-task learning / task interference references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Core finding is negative transfer, needs MTL literature\"}\n  action_items:\n    - {round: 1, action: \"Add MTL references to Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"MTL references added. Not re-raised.\"\n  resolution_round: 2\n\n- id: \"W17\"\n  summary: \"DPO 3-epoch uses different evaluation protocol — checkpoint lost\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DPO 3ep different protocol, pollutes spectrum\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Footnote 1 insufficient. Checkpoint confirmed lost.\"}\n  action_items:\n    - {round: 1, action: \"Remove internal numbering\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"DPO rebuild: retrain 1ep+3ep under unified protocol\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Update paper with new DPO numbers, remove footnote\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"DPO rebuilt from scratch, both epochs under matched@2048 protocol.\"\n  resolution_round: 3\n\n- id: \"W18\"\n  summary: \"Missing random selection baseline for RSFT\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1\", note: \"Need random-k=1 to prove selection value\"}\n  action_items:\n    - {round: 1, action: \"Run random k=1 RSFT baseline\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Random k=1 baseline added: 41.14 vs CED RSFT 44.66.\"\n  resolution_round: 2\n\n- id: \"FMT-CHECKLIST\"\n  summary: \"Responsible NLP Checklist\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"ARR mandatory\"}\n  action_items:\n    - {round: 1, action: \"Checklist via OpenReview form\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Submitted via OpenReview form.\"\n  resolution_round: 2\n\n- id: \"FMT-APPENDIX-RELCOUNT\"\n  summary: \"Appendix figure relation type count inconsistency\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"93 vs 76 vs 96 conflicting\"}\n  action_items:\n    - {round: 1, action: \"Clarify caption\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Caption clarified.\"\n  resolution_round: 2\n\n- id: \"R2-W1-NOVELTY\"\n  summary: \"Method novelty insufficient — contributions are empirical observations\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"CRITICAL: all 3 contributions empirical. R1 downgrades to MAJOR.\"}\n    - {round: 3, note: \"Implicitly addressed by empirical study framing.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Paper now positioned as empirical study ✓. But method-innovation language remnants: 'introduce the EDCR' (Contribution 2), 'we define' (§3.5). Need 'use'/'employ' instead.\"}\n  action_items:\n    - {round: 2, action: \"Reposition as empirical study, remove method-innovation language\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Replace 'introduce' with 'use'/'employ' for EDCR; replace 'we define' with 'we compute'/'we measure'\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5-NLI-SENSITIVITY\"\n  summary: \"CED sensitivity to NLI model family not analyzed\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Only DeBERTa v3 tested.\"}\n    - {round: 3, reviewers: \"R1\", note: \"Template sensitivity. R2 notes 0.02pp impact limited.\"}\n    - {round: 4, note: \"Not raised. DeBERTa-v3-base vs v3-large comparison added (Appendix B), only +1.10pp difference. Acknowledged in Limitations.\"}\n  action_items:\n    - {round: 2, action: \"Added to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-VARIANCE-SOURCE\"\n  summary: \"SFT vs RSFT variance measures different sources of randomness\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"SFT = full training randomness; RSFT = fixed-base. Comparison unfair.\"}\n    - {round: 3, reviewers: \"R2\", note: \"Confirms RSFT naturally compresses upstream variance. §4.2 caveats don't carry through to claims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"R2 partially rebutted R1: end-to-end comparison has practical value. R1 maintains methodological concern. Paper now has explicit caveat ✓ but precise ratios and 'predictable' language undermine it. Director: WARNING.\"}\n  action_items:\n    - {round: 2, action: \"Downgraded to 'consistently reduces' + acknowledged asymmetry\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Full downgrade of variance to observation. Explicit methodological asymmetry caveat.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Compress variance text, remove '36× more predictable', move precise ratios to appendix\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-LIMITATIONS\"\n  summary: \"Limitations section omissions\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"DocRED annotations, compute cost, task generalization.\"}\n  action_items:\n    - {round: 2, action: \"Added 4 points to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All points addressed in Limitations section.\"\n  resolution_round: 3\n\n- id: \"R2-W10-LLM-BASELINE\"\n  summary: \"Missing direct numerical comparison with LLM-based RE methods\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"AutoRE/GLiDRE numbers missing.\"}\n  action_items:\n    - {round: 2, action: \"Added inline comparison in Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Inline numerical comparison added. §2.1 now includes AutoRE 45.22 and RelPrior 47.70 vs our 54.33.\"\n  resolution_round: 3\n\n- id: \"VISUAL-MAIN-FIGURES\"\n  summary: \"Main text figures insufficient\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Pages 1-5 no visual anchor.\"}\n  action_items:\n    - {round: 2, action: \"Added fig_overview, fig_spectrum, fig_evidence_tax.\", assigned_to: \"Paper Agent + Director\", status: \"done\"}\n  resolution: \"Main text now has Figure 1 (p2), Figure 2 (p3), Figure 3 (p5), Figure 4 (p7), Figure 5 (p8) — well-distributed.\"\n  resolution_round: 4\n\n- id: \"VISUAL-COLORBLIND\"\n  summary: \"Figure colorblind accessibility issues\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Figure 4 red-green. Fixed with Okabe-Ito.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Figure 10 (p18) still uses red/green/blue — not colorblind friendly.\"}\n    - {round: 4, note: \"Not raised as major. Appendix figure, minor impact on review.\"}\n  action_items:\n    - {round: 2, action: \"Figure 4 changed to Okabe-Ito\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 3, action: \"Figure 10 change to Okabe-Ito or add hatching\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W9-4B-CHECKPOINT\"\n  summary: \"4B retrained checkpoint dev gap 0.35pp may affect evidence tax\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"Original 4B unavailable, retrained 43.88 vs 44.23.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n    - {round: 4, note: \"Not raised. Minor gap within seed noise.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1-IMPLICIT-REG\"\n  summary: \"Implicit regularization hypothesis indistinguishable from output constraint effect\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Evidence model 25.5k vs no-evidence 44.6k predictions. More parsimonious: output budget constraint. matched@2048 partial counter-evidence.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"NOT renamed. §4.4 still uses 'implicit regularization hypothesis'. Appendix E same. Round 3 consensus required renaming to 'structural output constraint'. Carry-over Should-Fix.\"}\n  action_items:\n    - {round: 3, action: \"Rename 'implicit regularization' to 'structural output constraint'. Add dual-mechanism discussion.\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Replace all instances of 'implicit regularization' with 'structural output constraint' or equivalent neutral term. Add sentence discussing matched@2048 counter-evidence.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2-14B-REVERSAL\"\n  summary: \"14B test-set reversal: SFT outperforms RSFT, explanation insufficient\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. 14B SFT truncation 50.6% vs RSFT 13.4%. Need precision/recall decomposition.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"No precision/recall decomposition provided. Paper attributes to truncation rate and annotation density but with only 1 SFT seed cannot distinguish noise from systematic. Carry-over Should-Fix.\"}\n  action_items:\n    - {round: 3, action: \"Extract precision/recall from existing 14B test-set predictions\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Provide precision/recall decomposition OR acknowledge single-SFT-seed limitation explicitly\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3-RSFT-TRADEOFF\"\n  summary: \"RSFT 'cannot exploit trade-off' claim purely structural, lacks empirical test\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Need single-objective RSFT or downgrade to hypothesis.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Still no experiment. §G remains structural argument only. Carry-over Should-Fix.\"}\n  action_items:\n    - {round: 3, action: \"Run single-objective RSFT (Rel-F1-only selection)\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Complete single-objective RSFT experiment OR downgrade 'cannot exploit' to 'hypothesis: discrete selection may not exploit'\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-FMT-PAGELIMIT\"\n  summary: \"Main text exceeds 8-page limit (desk reject risk)\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. §4.7 + §5 overflow to p9. EMNLP 2026 strict 8pp.\"}\n    - {round: 4, note: \"RESOLVED. Conclusion compressed to 2 sentences. Main text fits within 8 pages. PDF verified.\"}\n  action_items:\n    - {round: 3, action: \"Compress §4.7 Discussion + §5 Conclusion. Move content to appendix.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Main text now fits within 8 pages. Conclusion compressed to 2 sentences.\"\n  resolution_round: 4\n\n- id: \"R3-M1-SPECTRUM-SCALE\"\n  summary: \"Decoupling spectrum validated only at 4B scale\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Single-scale acceptable but should appear in Limitations.\"}\n    - {round: 4, note: \"RESOLVED. Limitations now states: 'The decoupling spectrum analysis is conducted entirely at 4B scale; whether the same ordering holds at other scales remains unverified.'\"}\n  action_items:\n    - {round: 3, action: \"Add to Limitations: spectrum validated only at 4B\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Added to Limitations section.\"\n  resolution_round: 4\n\n- id: \"R3-M2-TAX-CONVENTION\"\n  summary: \"Evidence tax sign convention inconsistent across sections\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Table 2 footnote vs Figure 7 caption vs Table 8 inconsistent.\"}\n    - {round: 4, note: \"RESOLVED. Convention now consistently defined at first mention in §1 and repeated in table footnotes: 'Tax = no-evi − with-evi; positive = cost'.\"}\n  action_items:\n    - {round: 3, action: \"Unify sign convention at first mention, ensure consistency.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Sign convention unified throughout.\"\n  resolution_round: 4\n\n- id: \"R4-EDCR-CONSISTENCY\"\n  summary: \"EDCR ρ numerical inconsistency across sections (Round 3 W-SF5)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"§3.5 ρ=-0.89 vs §4.7 ρ=-0.96 vs Appendix ρ=-0.9643 — three different values for same n=7.\"}\n    - {round: 4, note: \"RESOLVED. All instances now consistently report ρ=-0.96 (cross-method, n=7) and ρ=-0.79 (per-relation, n=76). Appendix raw value ρ=-0.9643 is the unrounded version of -0.96.\"}\n  action_items:\n    - {round: 3, action: \"Unify EDCR ρ values across all sections\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All EDCR ρ values now consistent.\"\n  resolution_round: 4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "faith-evidence-ie",
    "issues_yaml": "- id: \"W1\"\n  summary: \"GRPO QLoRA vs bf16 confounded variables — quantization, lr, group size not isolated\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Cannot support causal attribution of decoupling to QLoRA\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Table 3 shows QLoRA G=4 vs bf16 G=8 — two variables changed simultaneously. §4.3 attribution unsupported. Need bf16 G=4 or QLoRA G=8 control. Both AGREE Must-Fix.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"bf16 G=4 added (Rel-F1 28.73) — partially helps but reveals group size causes 16.76pp drop (45.49→28.73). lr confound 10× (5e-6 vs 5e-5) described as 'residual' is understated. 'attributable to quantization precision' still too strong. Downgrade to Should-Fix given partial progress.\"}\n  action_items:\n    - {round: 1, action: \"Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade causal claim to observational\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Deepen GRPO mechanism analysis with reward hacking lit + mechanistic chain\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Run GRPO bf16 G=4 experiment\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 4, action: \"Weaken attribution language: 'is attributable to' → 'is primarily consistent with'. Acknowledge lr 10× difference explicitly.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W2\"\n  summary: \"All results dev-set only, no test set\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"No CodaLab test results\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Test set results now exist (Table 9). Method ranking preserved (ρ=1.0).\"}\n  action_items:\n    - {round: 1, action: \"Add test set evaluation for all scales\", assigned_to: \"Agent+User\", status: \"done\"}\n  resolution: \"Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0).\"\n  resolution_round: 2\n\n- id: \"W3\"\n  summary: \"Variance compression claim statistically underpowered + cherry-picking in abstract\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"SFT single seed, +4.92pp lacks stats\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"n=3 per config, σ 95% CI overlapping. Both recommend ≥5 seeds or downgrade.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Only 1.7B χ² CI non-overlapping; other 3 scales overlap. Sign test p=0.0625. 4B Cohen's d=0.46 small. Abstract cherry-picks. Both AGREE Must-Fix.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Contribution 3 downgraded to observation ✓. Caveats added ✓. But §4.4 still devotes ~250 words + precise compression ratios (32.6×, 7.5×, 6.5×) + '36× more predictable' to variance — disproportionate for acknowledged weak evidence. Compress to 2-3 sentences, move ratios to appendix.\"}\n  action_items:\n    - {round: 1, action: \"Run SFT seed43+seed44, compute bootstrap CI\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Downgrade Abstract/Contributions to 'consistently reduces'. Three-layer evidence in appendix.\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n    - {round: 3, action: \"Remove variance as standalone abstract contribution. Downgrade to observation in §4.2 with explicit caveats.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Compress §4.4 variance discussion to 2-3 sentences. Move precise compression ratios to appendix. Remove '36× more predictable' phrasing.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W4\"\n  summary: \"Scaling claim based on limited data points\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"3 points insufficient, 1.7B repetition artifact\"}\n    - {round: 2, reviewers: \"R2\", note: \"4 Qwen + 1 LLaMA still limited for general scaling claim.\"}\n    - {round: 3, note: \"Not directly re-raised in Round 3.\"}\n    - {round: 4, note: \"Not raised. Paper now uses 'scale-dependent' rather than 'non-monotonic'. 5 models across 2 families.\"}\n  action_items:\n    - {round: 1, action: \"Replace 'non-monotonic' with 'scale-dependent', add LLaMA\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5\"\n  summary: \"EDCR shared-component mechanical negative correlation with Rel-F1\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"ρ=-0.965 partially predetermined\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"TP in numerator and denominator. n=7 too small. Request partial correlation, permutation test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"DIVERGENCE. R1 wants per-relation precision partial correlation. R2 considers per-relation n=76 sufficient. Director: WARNING.\"}\n    - {round: 4, note: \"Not re-raised as major. §3.5 now properly caveats cross-method correlation as 'diagnostic pattern rather than independent discovery'. Per-relation analysis (n=76) validated. Partial correlations virtually unchanged.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicate to n=7, per-relation n=76\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade EDCR to diagnostic tool + caveat\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Compute partial correlation + permutation test + similar-TP pairs\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Add partial correlation + permutation test to appendix\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Add per-relation precision partial correlation as additional robustness check\", assigned_to: \"Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5-EDCR-INFLATION\"\n  summary: \"EDCR ρ inflated by non-independent data points and GRPO QLoRA outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"Research Reviewer\", note: \"n=7 ρ=-0.89, n=6 (no QLoRA) ρ=-0.83 p=0.042\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Re-raised: n=6 borderline significant.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion.\"}\n    - {round: 4, note: \"Not raised. EDCR ρ now consistently reported as -0.96 (n=7 methods), -0.9643 (appendix raw). Per-relation ρ=-0.79 (n=76) provides independent validation.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 sans-QLoRA + partial ρ + permutation in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W6\"\n  summary: \"CED ≈ flat-NLI (0.02pp), contrastive formulation adds no measurable value\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Contrastive adds complexity without improvement\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"0.02pp within noise. CED cannot be method contribution.\"}\n    - {round: 3, reviewers: \"R2\", note: \"CED's unique contribution is interpretability, not data selection quality. Confirmed no method contribution language.\"}\n    - {round: 4, note: \"Properly positioned as scoring variant. §3.4 and §4.7 correctly report 0.02pp difference and adopt CED for interpretability only. No contribution language.\"}\n  action_items:\n    - {round: 1, action: \"Remove CED as independent contribution\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Position as scoring variant, no contribution language\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"CED correctly positioned as scoring variant with no contribution language. 0.02pp difference honestly reported.\"\n  resolution_round: 4\n\n- id: \"W7\"\n  summary: \"Training data quantity contradiction (9042 vs 2718)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"k=3 vs k=1 root cause\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining + update section 3.3\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Paper now consistently reports k=1 with ~3000 training samples.\"\n  resolution_round: 2\n\n- id: \"W8\"\n  summary: \"EDCR ρ based on n=6, not significant without outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\"}\n    - {round: 2, reviewers: \"R1\", note: \"n=7 still small, GRPO QLoRA outlier dominance.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion.\"}\n    - {round: 4, note: \"Not raised. Per-relation validation (n=76) provides robust independent evidence.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 remove-outlier + partial correlation + permutation in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W9\"\n  summary: \"'matches' 50.50 vs 50.51 statistically meaningless\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Single seed, 0.01pp < any reasonable variance\"}\n  action_items:\n    - {round: 1, action: \"Change 'matches' to 'approaches'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Changed to 'approaches' throughout.\"\n  resolution_round: 2\n\n- id: \"W10\"\n  summary: \"Encoder baseline comparison selective in metrics presentation\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DREEAM 54.01% buried in text\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 12 emphasizes TP-only Evi-F1, downplays 16-18pp Ign-F1 gap.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n    - {round: 4, note: \"Not raised. Appendix H now explicitly discusses Ign-F1 gap ('16–18pp at 4B, narrowing to <5pp at 14B') and attributes joint Evi-F1 gap to extraction performance.\"}\n  action_items:\n    - {round: 1, action: \"Add encoder baseline comparison table\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Balance discussion: acknowledge Ign-F1 gap\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Encoder comparison balanced with explicit Ign-F1 gap discussion in Appendix H.\"\n  resolution_round: 4\n\n- id: \"W11\"\n  summary: \"GRPO/DPO hyperparameter exploration insufficient — DPO β=0.1 single point\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"GRPO only KL=0.01, DPO only beta=0.1\"}\n    - {round: 2, reviewers: \"R2\", note: \"No KL ablation, no reward normalization test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both strongly agree. DPO β=0.1 → -11pp drop suspicious. Spectrum built on single β.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"4th round recurring. Still only β=0.1. If β=0.01 avoids decoupling, entire DPO segment of spectrum collapses. Upgraded to Must-Fix given persistence. Requires β sweep or explicit scope limitation.\"}\n  action_items:\n    - {round: 1, action: \"Acknowledge in Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add explicit KL caveat to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Run DPO β=0.01 experiment\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Complete β∈{0.01,0.05} sweep OR limit all DPO conclusions to 'under β=0.1'\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W12\"\n  summary: \"Metric format inconsistency\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Percentage vs decimal mixed\"}\n  action_items:\n    - {round: 1, action: \"Unify to percentage format\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Unified to percentage format.\"\n  resolution_round: 2\n\n- id: \"W13\"\n  summary: \"Missing references (LMRC, SummaC, RelPrior, Rationale Verification)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"15 'and others', author mismatches\"}\n    - {round: 2, reviewers: \"R2,R1\", note: \"Missing LMRC, SummaC, RelPrior, Rationale Verification.\"}\n    - {round: 3, note: \"Not raised. Missing references confirmed added.\"}\n  action_items:\n    - {round: 1, action: \"Fix bib errors\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add LMRC, SummaC, RelPrior, Rationale Verification, QuRL\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All missing references added. DeepSeek-R1 and ReST also added in Round 3-4.\"\n  resolution_round: 3\n\n- id: \"W14\"\n  summary: \"1.7B implicit regularization speculation without evidence\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Fair evaluation subset undefined\"}\n  action_items:\n    - {round: 1, action: \"Define fair subset + mechanistic breakdown\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Fair subset defined in Appendix D. Mechanistic breakdown added.\"\n  resolution_round: 2\n\n- id: \"W15\"\n  summary: \"Multi-seed coverage uneven\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Table 3: 3/4 rows single seed\"}\n    - {round: 2, note: \"1.7B/4B/8B/LLaMA now 3-seed. 14B still single seed.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"SFT no-evidence baseline only s42 for 1.7B/8B. 1.7B s42 is strongest seed (+3.22pp above mean).\"}\n    - {round: 4, note: \"Not raised as major. Paper now acknowledges 1.7B s42 as strongest seed in Appendix F. 14B SFT still single seed.\"}\n  action_items:\n    - {round: 1, action: \"Add seeds for 8B/1.7B/LLaMA\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 3, action: \"Add caveat in §4.4: 1.7B/8B no-evidence SFT is single seed (s42), and 1.7B s42 is strongest SFT seed.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W16\"\n  summary: \"Missing multi-task learning / task interference references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Core finding is negative transfer, needs MTL literature\"}\n  action_items:\n    - {round: 1, action: \"Add MTL references to Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"MTL references added. Not re-raised.\"\n  resolution_round: 2\n\n- id: \"W17\"\n  summary: \"DPO 3-epoch uses different evaluation protocol — checkpoint lost\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DPO 3ep different protocol, pollutes spectrum\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Footnote 1 insufficient. Checkpoint confirmed lost.\"}\n  action_items:\n    - {round: 1, action: \"Remove internal numbering\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"DPO rebuild: retrain 1ep+3ep under unified protocol\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Update paper with new DPO numbers, remove footnote\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"DPO rebuilt from scratch, both epochs under matched@2048 protocol.\"\n  resolution_round: 3\n\n- id: \"W18\"\n  summary: \"Missing random selection baseline for RSFT\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1\", note: \"Need random-k=1 to prove selection value\"}\n  action_items:\n    - {round: 1, action: \"Run random k=1 RSFT baseline\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Random k=1 baseline added: 41.14 vs CED RSFT 44.66.\"\n  resolution_round: 2\n\n- id: \"FMT-CHECKLIST\"\n  summary: \"Responsible NLP Checklist\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"ARR mandatory\"}\n  action_items:\n    - {round: 1, action: \"Checklist via OpenReview form\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Submitted via OpenReview form.\"\n  resolution_round: 2\n\n- id: \"FMT-APPENDIX-RELCOUNT\"\n  summary: \"Appendix figure relation type count inconsistency\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"93 vs 76 vs 96 conflicting\"}\n  action_items:\n    - {round: 1, action: \"Clarify caption\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Caption clarified.\"\n  resolution_round: 2\n\n- id: \"R2-W1-NOVELTY\"\n  summary: \"Method novelty insufficient — contributions are empirical observations\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"CRITICAL: all 3 contributions empirical. R1 downgrades to MAJOR.\"}\n    - {round: 3, note: \"Implicitly addressed by empirical study framing.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Paper now positioned as empirical study ✓. But method-innovation language remnants: 'introduce the EDCR' (Contribution 2), 'we define' (§3.5). Need 'use'/'employ' instead.\"}\n  action_items:\n    - {round: 2, action: \"Reposition as empirical study, remove method-innovation language\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Replace 'introduce' with 'use'/'employ' for EDCR; replace 'we define' with 'we compute'/'we measure'\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5-NLI-SENSITIVITY\"\n  summary: \"CED sensitivity to NLI model family not analyzed\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Only DeBERTa v3 tested.\"}\n    - {round: 3, reviewers: \"R1\", note: \"Template sensitivity. R2 notes 0.02pp impact limited.\"}\n    - {round: 4, note: \"Not raised. DeBERTa-v3-base vs v3-large comparison added (Appendix B), only +1.10pp difference. Acknowledged in Limitations.\"}\n  action_items:\n    - {round: 2, action: \"Added to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-VARIANCE-SOURCE\"\n  summary: \"SFT vs RSFT variance measures different sources of randomness\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"SFT = full training randomness; RSFT = fixed-base. Comparison unfair.\"}\n    - {round: 3, reviewers: \"R2\", note: \"Confirms RSFT naturally compresses upstream variance. §4.2 caveats don't carry through to claims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"R2 partially rebutted R1: end-to-end comparison has practical value. R1 maintains methodological concern. Paper now has explicit caveat ✓ but precise ratios and 'predictable' language undermine it. Director: WARNING.\"}\n  action_items:\n    - {round: 2, action: \"Downgraded to 'consistently reduces' + acknowledged asymmetry\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Full downgrade of variance to observation. Explicit methodological asymmetry caveat.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Compress variance text, remove '36× more predictable', move precise ratios to appendix\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-LIMITATIONS\"\n  summary: \"Limitations section omissions\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"DocRED annotations, compute cost, task generalization.\"}\n  action_items:\n    - {round: 2, action: \"Added 4 points to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All points addressed in Limitations section.\"\n  resolution_round: 3\n\n- id: \"R2-W10-LLM-BASELINE\"\n  summary: \"Missing direct numerical comparison with LLM-based RE methods\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"AutoRE/GLiDRE numbers missing.\"}\n  action_items:\n    - {round: 2, action: \"Added inline comparison in Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Inline numerical comparison added. §2.1 now includes AutoRE 45.22 and RelPrior 47.70 vs our 54.33.\"\n  resolution_round: 3\n\n- id: \"VISUAL-MAIN-FIGURES\"\n  summary: \"Main text figures insufficient\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Pages 1-5 no visual anchor.\"}\n  action_items:\n    - {round: 2, action: \"Added fig_overview, fig_spectrum, fig_evidence_tax.\", assigned_to: \"Paper Agent + Director\", status: \"done\"}\n  resolution: \"Main text now has Figure 1 (p2), Figure 2 (p3), Figure 3 (p5), Figure 4 (p7), Figure 5 (p8) — well-distributed.\"\n  resolution_round: 4\n\n- id: \"VISUAL-COLORBLIND\"\n  summary: \"Figure colorblind accessibility issues\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Figure 4 red-green. Fixed with Okabe-Ito.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Figure 10 (p18) still uses red/green/blue — not colorblind friendly.\"}\n    - {round: 4, note: \"Not raised as major. Appendix figure, minor impact on review.\"}\n  action_items:\n    - {round: 2, action: \"Figure 4 changed to Okabe-Ito\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 3, action: \"Figure 10 change to Okabe-Ito or add hatching\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W9-4B-CHECKPOINT\"\n  summary: \"4B retrained checkpoint dev gap 0.35pp may affect evidence tax\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"Original 4B unavailable, retrained 43.88 vs 44.23.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n    - {round: 4, note: \"Not raised. Minor gap within seed noise.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1-IMPLICIT-REG\"\n  summary: \"Implicit regularization hypothesis indistinguishable from output constraint effect\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Evidence model 25.5k vs no-evidence 44.6k predictions. More parsimonious: output budget constraint. matched@2048 partial counter-evidence.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"NOT renamed. §4.4 still uses 'implicit regularization hypothesis'. Appendix E same. Round 3 consensus required renaming to 'structural output constraint'. Carry-over Should-Fix.\"}\n  action_items:\n    - {round: 3, action: \"Rename 'implicit regularization' to 'structural output constraint'. Add dual-mechanism discussion.\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Replace all instances of 'implicit regularization' with 'structural output constraint' or equivalent neutral term. Add sentence discussing matched@2048 counter-evidence.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2-14B-REVERSAL\"\n  summary: \"14B test-set reversal: SFT outperforms RSFT, explanation insufficient\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. 14B SFT truncation 50.6% vs RSFT 13.4%. Need precision/recall decomposition.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"No precision/recall decomposition provided. Paper attributes to truncation rate and annotation density but with only 1 SFT seed cannot distinguish noise from systematic. Carry-over Should-Fix.\"}\n  action_items:\n    - {round: 3, action: \"Extract precision/recall from existing 14B test-set predictions\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Provide precision/recall decomposition OR acknowledge single-SFT-seed limitation explicitly\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3-RSFT-TRADEOFF\"\n  summary: \"RSFT 'cannot exploit trade-off' claim purely structural, lacks empirical test\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Need single-objective RSFT or downgrade to hypothesis.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Still no experiment. §G remains structural argument only. Carry-over Should-Fix.\"}\n  action_items:\n    - {round: 3, action: \"Run single-objective RSFT (Rel-F1-only selection)\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Complete single-objective RSFT experiment OR downgrade 'cannot exploit' to 'hypothesis: discrete selection may not exploit'\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-FMT-PAGELIMIT\"\n  summary: \"Main text exceeds 8-page limit (desk reject risk)\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. §4.7 + §5 overflow to p9. EMNLP 2026 strict 8pp.\"}\n    - {round: 4, note: \"RESOLVED. Conclusion compressed to 2 sentences. Main text fits within 8 pages. PDF verified.\"}\n  action_items:\n    - {round: 3, action: \"Compress §4.7 Discussion + §5 Conclusion. Move content to appendix.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Main text now fits within 8 pages. Conclusion compressed to 2 sentences.\"\n  resolution_round: 4\n\n- id: \"R3-M1-SPECTRUM-SCALE\"\n  summary: \"Decoupling spectrum validated only at 4B scale\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Single-scale acceptable but should appear in Limitations.\"}\n    - {round: 4, note: \"RESOLVED. Limitations now states: 'The decoupling spectrum analysis is conducted entirely at 4B scale; whether the same ordering holds at other scales remains unverified.'\"}\n  action_items:\n    - {round: 3, action: \"Add to Limitations: spectrum validated only at 4B\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Added to Limitations section.\"\n  resolution_round: 4\n\n- id: \"R3-M2-TAX-CONVENTION\"\n  summary: \"Evidence tax sign convention inconsistent across sections\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Table 2 footnote vs Figure 7 caption vs Table 8 inconsistent.\"}\n    - {round: 4, note: \"RESOLVED. Convention now consistently defined at first mention in §1 and repeated in table footnotes: 'Tax = no-evi − with-evi; positive = cost'.\"}\n  action_items:\n    - {round: 3, action: \"Unify sign convention at first mention, ensure consistency.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Sign convention unified throughout.\"\n  resolution_round: 4\n\n- id: \"R4-EDCR-CONSISTENCY\"\n  summary: \"EDCR ρ numerical inconsistency across sections (Round 3 W-SF5)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"§3.5 ρ=-0.89 vs §4.7 ρ=-0.96 vs Appendix ρ=-0.9643 — three different values for same n=7.\"}\n    - {round: 4, note: \"RESOLVED. All instances now consistently report ρ=-0.96 (cross-method, n=7) and ρ=-0.79 (per-relation, n=76). Appendix raw value ρ=-0.9643 is the unrounded version of -0.96.\"}\n  action_items:\n    - {round: 3, action: \"Unify EDCR ρ values across all sections\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All EDCR ρ values now consistent.\"\n  resolution_round: 4"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-25T22:54:09.048594+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml\", \"bytes\": 29685}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-25T22:56:43.001641+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 4 审稿报告\n\n## Summary\n\n本文研究 evidence-grounded document-level relation extraction 中不同训练范式（SFT/RSFT/GRPO/DPO）对 RE-evidence coupling 的影响。在 Qwen3 (1.7B–14B) 和 LLaMA-3.1-8B 上进行系统比较。核心发现：(1) evidence tax 是 scale-dependent 的（1.7B 有益，≥4B 近中性）；(2) gradient-based 方法导致 evidence-extraction decoupling，而 RSFT 通过 output filtering 维持 coupling；(3) EDCR 作为 diagnostic metric 量化 decoupling 程度。论文定位为实证研究。\n\n## Round 3 → Round 4 改进确认\n\n以下 Must-Fix/Should-Fix 项目已在本轮确认修复：\n- ✅ **页数限制**（R3-FMT）：正文现在 8 页内，Conclusion 压缩至 2 句。PDF 已验证。\n- ✅ **EDCR ρ 数值一致性**（R3 W-SF5）：现统一为 −0.96（cross-method, n=7）和 −0.79（per-relation, n=76），appendix 原始值 −0.9643 为未取整版本。\n- ✅ **RSFT seed protocol 透明化**：§3.3 现明确声明 primary experiments 共享 SFT s42 checkpoint，仅 LoRA init 和 data shuffling seed 不同。\n- ✅ **Variance 降级为 observation**：Contribution 3 改为 \"We observe lower cross-seed variance... though this partly reflects shared SFT initialization and is limited by n=3 seeds.\"\n- ✅ **Evidence tax sign convention**：全文统一定义 Tax = no-evi − with-evi; positive = cost。\n- ✅ **Spectrum 限制**：Limitations 已声明 spectrum 仅在 4B 验证。\n- ✅ **CED 定位**：正确定位为 scoring variant，0.02pp 差异诚实报告，无 contribution language。\n- ✅ **DeepSeek-R1 和 ReST 引用**：已添加。\n- ✅ **bf16 G=4 控制实验**：已新增（Rel-F1 28.73），部分回应 GRPO confound 问题。\n\n## Strengths\n\n1. **系统实验覆盖广泛**：5 model scales × 4 训练范式 + cross-architecture (LLaMA) + cross-dataset (Re-DocRED) 验证，在 evidence-grounded DocRE 领域是最全面的实证比较。\n\n2. **Decoupling spectrum 概念有洞察力**：按 RE-evidence coupling 程度排列训练方法的 conceptual framework 为社区理解 multi-objective training dynamics 提供有用参考。\n\n3. **Evidence tax 量化有实用价值**：将 evidence grounding 成本分离为 training-time 和 inference-time 两个维度，matched@2048 fair evaluation 方法严谨。\n\n4. **实验设计周全**：random selection baseline、matched@2048 evaluation、no-evidence SFT、CED vs flat-NLI、DeBERTa-v3-base vs large ablation 体现严谨方法论。\n\n5. **统计方法意识**：χ² CI、Cohen's d、permutation test、partial correlation 多层验证，方向正确。\n\n6. **可复现性强**：代码+数据承诺开源，hyperparameters 详尽，seed protocol 透明，evaluation protocol 明确。\n\n## Weaknesses\n\n### Must-Fix（两位 Reviewer 共识）\n\n**[W-MF1] DPO β=0.1 单点实验——连续 4 轮未解决**\n- DPO β=0.1 导致 Rel-F1 从 44.39 暴跌至 33.37（−11pp），这一异常结果高度可能是超参选择导致的\n- DPO 文献中 β=0.01-0.05 是常用范围，避免过度偏离 reference policy\n- 整个 decoupling spectrum 的 DPO 段（\"gradual decay\"）建立在单一 β 值上。若 β=0.01 下 DPO 不产生 decoupling，spectrum 的 DPO 段将失去依据\n- 此问题从 Round 1 起持续标记（Round 1: acknowledge → Round 2: caveat → Round 3: 强烈共识 → Round 4: 仍未解决）\n- **要求**：β∈{0.01, 0.05} sweep 或将所有 DPO 结论严格限定为 \"under β=0.1 with this specific configuration\"\n- *[R1, R2 强烈共识 — 4 轮 recurring, 升级为 Must-Fix]*\n\n### Should-Fix（两位 Reviewer 共识）\n\n**[W-SF1] GRPO bf16 G=4 结果反而暴露 group size 的显著影响**\n- 新增 bf16 G=4 实验（Rel-F1 28.73）是积极进展，但实际显示 group size 从 G=8 到 G=4 导致 16.76pp 性能下降（45.49 → 28.73）\n- 论文声称 \"group size alone does not cause collapse\" 在技术上正确（28.73 ≠ 1.38），但 16.76pp 的下降在实践中是 significant degradation\n- QLoRA G=8 (lr=5e-6) vs bf16 G=8 (lr=5e-5) 的学习率相差 10×，论文仅描述为 \"residual confound\"——10× lr 差异不是 residual\n- §4.3 \"the divergence is attributable to quantization precision\" 仍然过强：至少有 quantization、lr、effective batch size 三个混淆变量\n- **要求**：(1) 将 \"is attributable to\" 改为 \"is primarily consistent with\"；(2) 显式讨论 lr 10× 差异的潜在影响；(3) 承认 group size 的非trivial 贡献\n- *[R1, R2 共识 — 从 Must-Fix 降级为 Should-Fix，因 bf16 G=4 部分回应]*\n\n**[W-SF2] Variance \"observation\" 在文中篇幅与其证据力度不匹配**\n- Contribution 3 已降级为 observation（✓），caveats 已添加（✓）\n- 但 §4.4 仍用一整段（~250 words）详细报告 variance compression 的精确数字（32.6×, 7.5×, 6.5×）和 sign test / Cohen's d，以 \"36× more predictable\" 收尾\n- sign test p=0.0625 仍不显著；Cohen's d=0.46 at 4B 是 small effect\n- 精确 ratio 和 \"predictable\" 措辞与 \"observation with acknowledged limitations\" 的定位不一致\n- **要求**：压缩 variance 讨论至 2-3 句，移除精确 compression ratio（或移至 appendix），避免 \"more predictable\" 等暗示因果的表述\n- *[R1, R2 共识]*\n\n**[W-SF3] \"Implicit regularization\" 假说仍未按 Round 3 共识重命名**\n- R3 双方共识要求将 \"implicit regularization\" 改为 \"structural output constraint\" 或更中性表述\n- 当前论文 §4.4 仍使用 \"supports the implicit regularization hypothesis\"；Appendix E 同样保留\n- evidence model 25.5k vs no-evidence 44.6k predictions：更简约解释是 output budget constraint → fewer triples → fewer FP/duplicates\n- matched@2048 下 evidence model 仍有 −5.63pp benefit，对纯 constraint 解释构成部分挑战——需正文讨论这一张力\n- **要求**：替换 \"implicit regularization\" 为 \"structural output constraint\"；增加一句讨论 matched@2048 counter-evidence\n- *[R1, R2 共识 — R3 carry-over]*\n\n**[W-SF4] RSFT \"cannot exploit trade-off\" 仍缺乏实证验证**\n- §G（Appendix）的论证完全是 structural argument，无实验验证\n- Single-objective RSFT（如 Rel-F1-only selection）是 cheap 且 natural 的验证实验\n- Round 3 已将此标记为 Should-Fix 并排队实验，本轮仍未见结果\n- **要求**：完成 single-objective RSFT 实验或将 \"cannot exploit\" 降级为 \"we hypothesize that discrete selection does not exploit\"\n- *[R1, R2 共识 — R3 carry-over]*\n\n**[W-SF5] Method-innovation 语言残留**\n- Contribution 2: \"introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic\"\n- §3.5: \"we define the Evidence-Decoupling Ratio (EDCR)\"\n- 论文已正确定位为 empirical study，但 \"introduce\" 和 \"define\" 暗示 novel method contribution\n- EDCR 是一个简单的 distractor citation rate，用 \"introduce\" 过度拔高\n- **要求**：将 \"introduce\" 改为 \"use\"/\"employ\"；将 \"define\" 改为 \"compute\"/\"measure\"\n- *[R1, R2 共识]*\n\n**[W-SF6] 14B test-set reversal 仍未提供 precision/recall 分解**\n- 14B: SFT truncation 50.6% vs RSFT 13.4%；dev-test reversal (+2.78pp dev → −0.37pp test)\n- 论文将此归因于 truncation rate 和 annotation density（2.82×），合理但不充分\n- 仅 1 SFT seed，无法区分噪声和系统性\n- Round 3 要求的 precision/recall 分解仍未提供\n- **要求**：提供 precision/recall 分解，或显式承认 14B test-set 结论受限于 single SFT seed\n- *[R1, R2 共识 — R3 carry-over]*\n\n### Minor Issues\n\n| ID | 问题 | 共识 |\n|---|---|---|\n| M1 | SFT no-evidence 基线 1.7B/8B 仅 s42；1.7B s42 是最强 SFT seed (+3.22pp above mean) | AGREE — 可能放大 tax benefit |\n| M2 | CED template sensitivity 和 NLI model family 测试有限 | AGREE — 实际影响小 (0.02pp)，已在 Limitations 声明 |\n| M3 | BM25 k=2 选择未 justify | AGREE |\n| M4 | Figure 10 (Appendix) 色盲不友好 | AGREE — minor |\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上达成完全共识 [AGREE]：\n\n1. **DPO β 单点实验**：decoupling spectrum 的 DPO 段建立在单一 β=0.1 上，极可能是超参 artifact（4 轮 recurring，升级为 Must-Fix）\n2. **n=3 seeds 统计效力**：variance compression 的统计证据不足（sign test p=0.0625，多数 CI 重叠），observation 定位正确但文本过冗长\n3. **CED 微效**：contrastive component 贡献 0.02pp，无实际价值，但已正确定位\n4. **GRPO attribution**：bf16 G=4 部分帮助但暴露 group size significant effect + lr confound\n5. **Method-innovation 语言**：需进一步清理（\"introduce\"→\"use\"）\n6. **Implicit regularization**：R3 共识要求重命名，本轮仍未执行\n\n## Reviewer Divergence\n\n**[W-DIV1] RSFT variance 比较的方法论公平性**\n- **R2 部分反驳 R1**：end-to-end variance 比较虽有方法论不对称（SFT = full pipeline randomness, RSFT = fine-tuning stage only），但在实践中有价值——practitioner 关心的是 \"给定 RSFT pipeline，结果有多稳定\"\n- **R1 坚持**：RSFT 自然压缩上游 variance（因从 fixed checkpoint 出发），比较在方法论上不成立\n- **Director 判定**：R2 的 practical argument 有道理，但论文需要明确承认不对称性并避免暗示因果关系。当前 caveat（\"these measure different sources of variance\"）存在 ✓，但紧接着的精确数字和 \"predictable\" 措辞削弱了 caveat 的效果。**维持 WARNING — 需压缩 variance 讨论并移除精确 ratio。**\n\n## Questions for Authors\n\n1. bf16 G=4 实验的学习率是多少？如果与 bf16 G=8 相同（5e-5），则 Rel-F1 从 45.49 降至 28.73 纯粹由 G 导致，说明 group size 是 significant factor。\n2. DPO β=0.01 或 β=0.05 实验是否在进行中？此问题已持续 4 轮。\n3. Single-objective RSFT（Rel-F1-only selection）实验结果？\n4. 14B precision/recall 分解数据？\n\n## Missing References\n\nRound 3 指出的 DeepSeek-R1 和 ReST (Gulcehre et al., 2023) 已添加 ✓。\n本轮无新增缺失引用。\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未启用外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~3.5 分钟)\n\n| 严重性 | 位置 | 发现 |\n|---|---|---|\n| ℹ️ | p5 | Figure 3 (CED scoring) 内部文字偏小（正文 60-65%），建议 ≥70% |\n| ℹ️ | p7 | Figure 4 (Decoupling spectrum) 图例文字偏小，在绘图区域内部 |\n| ℹ️ | p12 | Appendix 单页含 4 张表，信息密度极高（格式正确无溢出） |\n| ℹ️ | p17 | Figure 7 三子图 y 轴标签和刻度文字偏小 |\n| ℹ️ | p18 | 末页约 25% 空白（Appendix 末页，不影响审稿） |\n| ✅ | p2 | Figure 1 清晰专业，蓝色标注方案一致，caption 自包含 |\n| ✅ | p6 | Table 2 booktabs 规范，最优加粗 |\n| ✅ | p8 | Figure 5 红/蓝对比清晰，误差条可辨 |\n\n**0 critical, 0 warning, 8 info** — 排版质量整体良好，无影响审稿的视觉问题。Figure 1 现在在 p2，解决了 Round 2-3 的 \"文字墙\" 问题。\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | 评分 | 说明 |\n|---|---|---|\n| Soundness | 3 | bf16 G=4 帮助但未完全隔离 GRPO confound（lr 10× + group size effect）；DPO spectrum 建于单一 β；variance 统计力度不足 |\n| Excitement | 3 | Decoupling spectrum 有启发性；empirical scope 广泛但 novelty 在 coverage 而非 method/insight 层面 |\n| Reproducibility | 4 | 代码+数据承诺开源，hyperparameters 详尽，RSFT seed protocol 现已完全透明 |\n| Clarity | 3.5 | 格式问题大部分已修复（页数✓、EDCR ρ✓、abstract✓、sign convention✓）；但 variance 段过冗长、implicit regularization 未重命名、method-innovation 语言残留 |\n| Overall | 3.5 | Borderline Conference |\n\n**置信度：4/5** — 两位 Reviewer 在核心问题上高度一致（均 3.5），交叉回应完成，仅 1 条 partial divergence 已裁定。\n\n**推荐决定**：\n- **当前状态 → Borderline Conference (3.5)**：格式问题已显著改善，variance 已降级，RSFT seed protocol 已澄清，bf16 G=4 控制实验已添加。但 DPO β 单点（4 轮 recurring Must-Fix）、RSFT \"cannot exploit\" 缺实证、GRPO attribution 仍有 confound——这些实验性不足阻碍论文获得 Conference (4.0) 评分。\n- **修复后 → Conference (4.0)**：如果 (1) 完成 DPO β sweep 或严格限定结论、(2) implicit regularization 重命名、(3) variance 讨论压缩、(4) method-innovation 语言清理、(5) RSFT single-objective 实验或降级为 hypothesis，论文可达 Conference 水平。当前的 empirical coverage 和实验设计基础是扎实的。\n- **关键阻碍**：DPO β 问题已从 Round 1 的 \"acknowledge in Limitations\" 升级为 4 轮未解决的 Must-Fix。这不是 writing fix 能解决的——需要实验数据或 scope limitation。\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 3 已正确降级为 observation with caveats ✓\n- Contribution 2 \"introduce the EDCR as a diagnostic\" → 改为 \"use\"/\"employ\"\n- Evidence tax 定义清晰，sign convention 首次出现时明确 ✓\n\n### §3 Method\n- RSFT seed protocol 完全透明 ✓（§3.3 明确声明 shared SFT s42 checkpoint）\n- CED 正确定位为 scoring variant，flat-NLI 比较到位 ✓\n- §3.5 EDCR ρ 数值一致（-0.96 cross-method, -0.79 per-relation）✓\n- §3.5 caveat \"should be interpreted as diagnostic pattern rather than independent discovery\" ✓\n\n### §4 Experiments\n- §4.2: \"though these reflect different sources of variation\" caveat ✓，但紧接精确 compression ratio 和 \"predictable\" 措辞削弱 caveat — 需压缩\n- §4.3: bf16 G=4 新增 ✓，但 \"attributable to quantization precision\" 过强。lr 差异 10×（5e-6 vs 5e-5）不是 \"residual confound\"。bf16 G=4 (28.73) vs bf16 G=8 (45.49) = 16.76pp drop 表明 group size 有实质影响\n- §4.4: \"implicit regularization hypothesis\" 仍在使用 → 需重命名为 \"structural output constraint\"\n- §4.4: Method B independent SFT base 验证 ✓（有价值的补充）\n- §4.4: variance 段落 ~250 words，远超其 evidence strength 所需篇幅\n- §4.5: BM25 k=2 缺 justification\n\n### §5 Conclusion\n- 压缩至 2 句 ✓，现符合 8 页限制 ✓\n\n### Limitations\n- 覆盖 data/architecture scope、CED sensitivity、RSFT mechanistic ✓\n- Spectrum 仅 4B 验证已声明 ✓\n- 未明确提及 DPO β single-point limitation（应补充）\n\n### Appendix\n- §G \"cannot exploit\" 仍为 structural argument，缺实证（Should-Fix）\n- §E 仍使用 \"implicit regularization hypothesis\"\n- Appendix K evidence quality unchanged (Δ<0.4pp) 与 implicit regularization framing 存在张力——需正文提及\n- Figure 10 色盲问题未修复（minor，Appendix）\n\n---\n\n*本报告由 2 位 Reviewer 独立审稿 + 双向交叉回应后合成。核心共识：DPO β 单点（4 轮 recurring）是升级为 Must-Fix 的唯一项；Round 3 的多个 Must-Fix 已修复（页数、EDCR 一致性、seed protocol）。Overall 评分一致：3.5 Borderline Conference。*",
  "project": "faith-evidence-ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 4 审稿报告\n\n## Summary\n\n本文研究 evidence-grounded document-level relation extraction 中不同训练范式（SFT/RSFT/GRPO/DPO）对 RE-evidence coupling 的影响。在 Qwen3 (1.7B–14B) 和 LLaMA-3.1-8B 上进行系统比较。核心发现：(1) evidence tax 是 scale-dependent 的（1.7B 有益，≥4B 近中性）；(2) gradient-based 方法导致 evidence-extraction decoupling，而 RSFT 通过 output filtering 维持 coupling；(3) EDCR 作为 diagnostic metric 量化 decoupling 程度。论文定位为实证研究。\n\n## Round 3 → Round 4 改进确认\n\n以下 Must-Fix/Should-Fix 项目已在本轮确认修复：\n- ✅ **页数限制**（R3-FMT）：正文现在 8 页内，Conclusion 压缩至 2 句。PDF 已验证。\n- ✅ **EDCR ρ 数值一致性**（R3 W-SF5）：现统一为 −0.96（cross-method, n=7）和 −0.79（per-relation, n=76），appendix 原始值 −0.9643 为未取整版本。\n- ✅ **RSFT seed protocol 透明化**：§3.3 现明确声明 primary experiments 共享 SFT s42 checkpoint，仅 LoRA init 和 data shuffling seed 不同。\n- ✅ **Variance 降级为 observation**：Contribution 3 改为 \"We observe lower cross-seed variance... though this partly reflects shared SFT initialization and is limited by n=3 seeds.\"\n- ✅ **Evidence tax sign convention**：全文统一定义 Tax = no-evi − with-evi; positive = cost。\n- ✅ **Spectrum 限制**：Limitations 已声明 spectrum 仅在 4B 验证。\n- ✅ **CED 定位**：正确定位为 scoring variant，0.02pp 差异诚实报告，无 contribution language。\n- ✅ **DeepSeek-R1 和 ReST 引用**：已添加。\n- ✅ **bf16 G=4 控制实验**：已新增（Rel-F1 28.73），部分回应 GRPO confound 问题。\n\n## Strengths\n\n1. **系统实验覆盖广泛**：5 model scales × 4 训练范式 + cross-architecture (LLaMA) + cross-dataset (Re-DocRED) 验证，在 evidence-grounded DocRE 领域是最全面的实证比较。\n\n2. **Decoupling spectrum 概念有洞察力**：按 RE-evidence coupling 程度排列训练方法的 conceptual framework 为社区理解 multi-objective training dynamics 提供有用参考。\n\n3. **Evidence tax 量化有实用价值**：将 evidence grounding 成本分离为 training-time 和 inference-time 两个维度，matched@2048 fair evaluation 方法严谨。\n\n4. **实验设计周全**：random selection baseline、matched@2048 evaluation、no-evidence SFT、CED vs flat-NLI、DeBERTa-v3-base vs large ablation 体现严谨方法论。\n\n5. **统计方法意识**：χ² CI、Cohen's d、permutation test、partial correlation 多层验证，方向正确。\n\n6. **可复现性强**：代码+数据承诺开源，hyperparameters 详尽，seed protocol 透明，evaluation protocol 明确。\n\n## Weaknesses\n\n### Must-Fix（两位 Reviewer 共识）\n\n**[W-MF1] DPO β=0.1 单点实验——连续 4 轮未解决**\n- DPO β=0.1 导致 Rel-F1 从 44.39 暴跌至 33.37（−11pp），这一异常结果高度可能是超参选择导致的\n- DPO 文献中 β=0.01-0.05 是常用范围，避免过度偏离 reference policy\n- 整个 decoupling spectrum 的 DPO 段（\"gradual decay\"）建立在单一 β 值上。若 β=0.01 下 DPO 不产生 decoupling，spectrum 的 DPO 段将失去依据\n- 此问题从 Round 1 起持续标记（Round 1: acknowledge → Round 2: caveat → Round 3: 强烈共识 → Round 4: 仍未解决）\n- **要求**：β∈{0.01, 0.05} sweep 或将所有 DPO 结论严格限定为 \"under β=0.1 with this specific configuration\"\n- *[R1, R2 强烈共识 — 4 轮 recurring, 升级为 Must-Fix]*\n\n### Should-Fix（两位 Reviewer 共识）\n\n**[W-SF1] GRPO bf16 G=4 结果反而暴露 group size 的显著影响**\n- 新增 bf16 G=4 实验（Rel-F1 28.73）是积极进展，但实际显示 group size 从 G=8 到 G=4 导致 16.76pp 性能下降（45.49 → 28.73）\n- 论文声称 \"group size alone does not cause collapse\" 在技术上正确（28.73 ≠ 1.38），但 16.76pp 的下降在实践中是 significant degradation\n- QLoRA G=8 (lr=5e-6) vs bf16 G=8 (lr=5e-5) 的学习率相差 10×，论文仅描述为 \"residual confound\"——10× lr 差异不是 residual\n- §4.3 \"the divergence is attributable to quantization precision\" 仍然过强：至少有 quantization、lr、effective batch size 三个混淆变量\n- **要求**：(1) 将 \"is attributable to\" 改为 \"is primarily consistent with\"；(2) 显式讨论 lr 10× 差异的潜在影响；(3) 承认 group size 的非trivial 贡献\n- *[R1, R2 共识 — 从 Must-Fix 降级为 Should-Fix，因 bf16 G=4 部分回应]*\n\n**[W-SF2] Variance \"observation\" 在文中篇幅与其证据力度不匹配**\n- Contribution 3 已降级为 observation（✓），caveats 已添加（✓）\n- 但 §4.4 仍用一整段（~250 words）详细报告 variance compression 的精确数字（32.6×, 7.5×, 6.5×）和 sign test / Cohen's d，以 \"36× more predictable\" 收尾\n- sign test p=0.0625 仍不显著；Cohen's d=0.46 at 4B 是 small effect\n- 精确 ratio 和 \"predictable\" 措辞与 \"observation with acknowledged limitations\" 的定位不一致\n- **要求**：压缩 variance 讨论至 2-3 句，移除精确 compression ratio（或移至 appendix），避免 \"more predictable\" 等暗示因果的表述\n- *[R1, R2 共识]*\n\n**[W-SF3] \"Implicit regularization\" 假说仍未按 Round 3 共识重命名**\n- R3 双方共识要求将 \"implicit regularization\" 改为 \"structural output constraint\" 或更中性表述\n- 当前论文 §4.4 仍使用 \"supports the implicit regularization hypothesis\"；Appendix E 同样保留\n- evidence model 25.5k vs no-evidence 44.6k predictions：更简约解释是 output budget constraint → fewer triples → fewer FP/duplicates\n- matched@2048 下 evidence model 仍有 −5.63pp benefit，对纯 constraint 解释构成部分挑战——需正文讨论这一张力\n- **要求**：替换 \"implicit regularization\" 为 \"structural output constraint\"；增加一句讨论 matched@2048 counter-evidence\n- *[R1, R2 共识 — R3 carry-over]*\n\n**[W-SF4] RSFT \"cannot exploit trade-off\" 仍缺乏实证验证**\n- §G（Appendix）的论证完全是 structural argument，无实验验证\n- Single-objective RSFT（如 Rel-F1-only selection）是 cheap 且 natural 的验证实验\n- Round 3 已将此标记为 Should-Fix 并排队实验，本轮仍未见结果\n- **要求**：完成 single-objective RSFT 实验或将 \"cannot exploit\" 降级为 \"we hypothesize that discrete selection does not exploit\"\n- *[R1, R2 共识 — R3 carry-over]*\n\n**[W-SF5] Method-innovation 语言残留**\n- Contribution 2: \"introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic\"\n- §3.5: \"we define the Evidence-Decoupling Ratio (EDCR)\"\n- 论文已正确定位为 empirical study，但 \"introduce\" 和 \"define\" 暗示 novel method contribution\n- EDCR 是一个简单的 distractor citation rate，用 \"introduce\" 过度拔高\n- **要求**：将 \"introduce\" 改为 \"use\"/\"employ\"；将 \"define\" 改为 \"compute\"/\"measure\"\n- *[R1, R2 共识]*\n\n**[W-SF6] 14B test-set reversal 仍未提供 precision/recall 分解**\n- 14B: SFT truncation 50.6% vs RSFT 13.4%；dev-test reversal (+2.78pp dev → −0.37pp test)\n- 论文将此归因于 truncation rate 和 annotation density（2.82×），合理但不充分\n- 仅 1 SFT seed，无法区分噪声和系统性\n- Round 3 要求的 precision/recall 分解仍未提供\n- **要求**：提供 precision/recall 分解，或显式承认 14B test-set 结论受限于 single SFT seed\n- *[R1, R2 共识 — R3 carry-over]*\n\n### Minor Issues\n\n| ID | 问题 | 共识 |\n|---|---|---|\n| M1 | SFT no-evidence 基线 1.7B/8B 仅 s42；1.7B s42 是最强 SFT seed (+3.22pp above mean) | AGREE — 可能放大 tax benefit |\n| M2 | CED template sensitivity 和 NLI model family 测试有限 | AGREE — 实际影响小 (0.02pp)，已在 Limitations 声明 |\n| M3 | BM25 k=2 选择未 justify | AGREE |\n| M4 | Figure 10 (Appendix) 色盲不友好 | AGREE — minor |\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上达成完全共识 [AGREE]：\n\n1. **DPO β 单点实验**：decoupling spectrum 的 DPO 段建立在单一 β=0.1 上，极可能是超参 artifact（4 轮 recurring，升级为 Must-Fix）\n2. **n=3 seeds 统计效力**：variance compression 的统计证据不足（sign test p=0.0625，多数 CI 重叠），observation 定位正确但文本过冗长\n3. **CED 微效**：contrastive component 贡献 0.02pp，无实际价值，但已正确定位\n4. **GRPO attribution**：bf16 G=4 部分帮助但暴露 group size significant effect + lr confound\n5. **Method-innovation 语言**：需进一步清理（\"introduce\"→\"use\"）\n6. **Implicit regularization**：R3 共识要求重命名，本轮仍未执行\n\n## Reviewer Divergence\n\n**[W-DIV1] RSFT variance 比较的方法论公平性**\n- **R2 部分反驳 R1**：end-to-end variance 比较虽有方法论不对称（SFT = full pipeline randomness, RSFT = fine-tuning stage only），但在实践中有价值——practitioner 关心的是 \"给定 RSFT pipeline，结果有多稳定\"\n- **R1 坚持**：RSFT 自然压缩上游 variance（因从 fixed checkpoint 出发），比较在方法论上不成立\n- **Director 判定**：R2 的 practical argument 有道理，但论文需要明确承认不对称性并避免暗示因果关系。当前 caveat（\"these measure different sources of variance\"）存在 ✓，但紧接着的精确数字和 \"predictable\" 措辞削弱了 caveat 的效果。**维持 WARNING — 需压缩 variance 讨论并移除精确 ratio。**\n\n## Questions for Authors\n\n1. bf16 G=4 实验的学习率是多少？如果与 bf16 G=8 相同（5e-5），则 Rel-F1 从 45.49 降至 28.73 纯粹由 G 导致，说明 group size 是 significant factor。\n2. DPO β=0.01 或 β=0.05 实验是否在进行中？此问题已持续 4 轮。\n3. Single-objective RSFT（Rel-F1-only selection）实验结果？\n4. 14B precision/recall 分解数据？\n\n## Missing References\n\nRound 3 指出的 DeepSeek-R1 和 ReST (Gulcehre et al., 2023) 已添加 ✓。\n本轮无新增缺失引用。\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未启用外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~3.5 分钟)\n\n| 严重性 | 位置 | 发现 |\n|---|---|---|\n| ℹ️ | p5 | Figure 3 (CED scoring) 内部文字偏小（正文 60-65%），建议 ≥70% |\n| ℹ️ | p7 | Figure 4 (Decoupling spectrum) 图例文字偏小，在绘图区域内部 |\n| ℹ️ | p12 | Appendix 单页含 4 张表，信息密度极高（格式正确无溢出） |\n| ℹ️ | p17 | Figure 7 三子图 y 轴标签和刻度文字偏小 |\n| ℹ️ | p18 | 末页约 25% 空白（Appendix 末页，不影响审稿） |\n| ✅ | p2 | Figure 1 清晰专业，蓝色标注方案一致，caption 自包含 |\n| ✅ | p6 | Table 2 booktabs 规范，最优加粗 |\n| ✅ | p8 | Figure 5 红/蓝对比清晰，误差条可辨 |\n\n**0 critical, 0 warning, 8 info** — 排版质量整体良好，无影响审稿的视觉问题。Figure 1 现在在 p2，解决了 Round 2-3 的 \"文字墙\" 问题。\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | 评分 | 说明 |\n|---|---|---|\n| Soundness | 3 | bf16 G=4 帮助但未完全隔离 GRPO confound（lr 10× + group size effect）；DPO spectrum 建于单一 β；variance 统计力度不足 |\n| Excitement | 3 | Decoupling spectrum 有启发性；empirical scope 广泛但 novelty 在 coverage 而非 method/insight 层面 |\n| Reproducibility | 4 | 代码+数据承诺开源，hyperparameters 详尽，RSFT seed protocol 现已完全透明 |\n| Clarity | 3.5 | 格式问题大部分已修复（页数✓、EDCR ρ✓、abstract✓、sign convention✓）；但 variance 段过冗长、implicit regularization 未重命名、method-innovation 语言残留 |\n| Overall | 3.5 | Borderline Conference |\n\n**置信度：4/5** — 两位 Reviewer 在核心问题上高度一致（均 3.5），交叉回应完成，仅 1 条 partial divergence 已裁定。\n\n**推荐决定**：\n- **当前状态 → Borderline Conference (3.5)**：格式问题已显著改善，variance 已降级，RSFT seed protocol 已澄清，bf16 G=4 控制实验已添加。但 DPO β 单点（4 轮 recurring Must-Fix）、RSFT \"cannot exploit\" 缺实证、GRPO attribution 仍有 confound——这些实验性不足阻碍论文获得 Conference (4.0) 评分。\n- **修复后 → Conference (4.0)**：如果 (1) 完成 DPO β sweep 或严格限定结论、(2) implicit regularization 重命名、(3) variance 讨论压缩、(4) method-innovation 语言清理、(5) RSFT single-objective 实验或降级为 hypothesis，论文可达 Conference 水平。当前的 empirical coverage 和实验设计基础是扎实的。\n- **关键阻碍**：DPO β 问题已从 Round 1 的 \"acknowledge in Limitations\" 升级为 4 轮未解决的 Must-Fix。这不是 writing fix 能解决的——需要实验数据或 scope limitation。\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 3 已正确降级为 observation with caveats ✓\n- Contribution 2 \"introduce the EDCR as a diagnostic\" → 改为 \"use\"/\"employ\"\n- Evidence tax 定义清晰，sign convention 首次出现时明确 ✓\n\n### §3 Method\n- RSFT seed protocol 完全透明 ✓（§3.3 明确声明 shared SFT s42 checkpoint）\n- CED 正确定位为 scoring variant，flat-NLI 比较到位 ✓\n- §3.5 EDCR ρ 数值一致（-0.96 cross-method, -0.79 per-relation）✓\n- §3.5 caveat \"should be interpreted as diagnostic pattern rather than independent discovery\" ✓\n\n### §4 Experiments\n- §4.2: \"though these reflect different sources of variation\" caveat ✓，但紧接精确 compression ratio 和 \"predictable\" 措辞削弱 caveat — 需压缩\n- §4.3: bf16 G=4 新增 ✓，但 \"attributable to quantization precision\" 过强。lr 差异 10×（5e-6 vs 5e-5）不是 \"residual confound\"。bf16 G=4 (28.73) vs bf16 G=8 (45.49) = 16.76pp drop 表明 group size 有实质影响\n- §4.4: \"implicit regularization hypothesis\" 仍在使用 → 需重命名为 \"structural output constraint\"\n- §4.4: Method B independent SFT base 验证 ✓（有价值的补充）\n- §4.4: variance 段落 ~250 words，远超其 evidence strength 所需篇幅\n- §4.5: BM25 k=2 缺 justification\n\n### §5 Conclusion\n- 压缩至 2 句 ✓，现符合 8 页限制 ✓\n\n### Limitations\n- 覆盖 data/architecture scope、CED sensitivity、RSFT mechanistic ✓\n- Spectrum 仅 4B 验证已声明 ✓\n- 未明确提及 DPO β single-point limitation（应补充）\n\n### Appendix\n- §G \"cannot exploit\" 仍为 structural argument，缺实证（Should-Fix）\n- §E 仍使用 \"implicit regularization hypothesis\"\n- Appendix K evidence quality unchanged (Δ<0.4pp) 与 implicit regularization framing 存在张力——需正文提及\n- Figure 10 色盲问题未修复（minor，Appendix）\n\n---\n\n*本报告由 2 位 Reviewer 独立审稿 + 双向交叉回应后合成。核心共识：DPO β 单点（4 轮 recurring）是升级为 Must-Fix 的唯一项；Round 3 的多个 Must-Fix 已修复（页数、EDCR 一致性、seed protocol）。Overall 评分一致：3.5 Borderline Conference。*",
    "project": "faith-evidence-ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-25T22:56:47.227342+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_84537e1e2f9ef71a90742c2db859c6f2:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4225
}
```

</details>

---


### Assistant

_source line 422 · 2026-05-25T22:56:58.756334+00:00_

**Round 4 审稿报告已投递。**

**评分：3.5 — Borderline Conference**（R1、R2 一致）

**本轮确认修复 7 项**：页数限制 ✓、EDCR ρ 一致性 ✓、RSFT seed protocol ✓、variance 降级 ✓、sign convention ✓、spectrum 限制声明 ✓、bf16 G=4 控制实验 ✓

**唯一 Must-Fix**：DPO β=0.1 单点实验（4 轮 recurring，需 β sweep 或 scope limitation）

**5 项 Should-Fix**：GRPO attribution 措辞过强、variance 段落过冗长、implicit regularization 未重命名、RSFT "cannot exploit" 缺实证、method-innovation 语言残留

**升至 4.0 的路径**：完成 DPO β sweep + 压缩 variance + 重命名 implicit regularization + 清理 framing 语言。实验基础扎实，主要差距在实验完整性和措辞精确度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 33

## Round 33

6 recorded events


### User

_source line 423 · 2026-05-25T22:56:58.763870+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE with nuance] R2-N1(1): RSFT = STaR + CED，是 engineering contribution**
同意 RSFT 本身不是方法论创新——rejection sampling fine-tuning 和 NLI-based scoring 都是已有技术。但论文的主要贡献定位是 empirical study（extraction-evidence trade-off 的系统刻画），RSFT 是三个范式之一而非核心方法贡献。问题在于 Contribution 3 的措辞（"RSFT improves extraction without decoupling"）确实将 RSFT 包装得过于像 method contribution。建议作者将 RSFT 的角色明确为 "empirical finding: discrete selection avoids decoupling" 而非暗示方法新颖性。

**[AGREE] R2-N1(2): CED vs flat-NLI 仅差 0.02pp**
完全同意。我在自己的 W1 中也标记了这一问题。Section 3.4 投入了大量篇幅设计 contrastive formulation，但 Section 4.7 自己承认 "the contrastive formulation is not essential for data selection quality"。这是论文中 effort-vs-payoff 最失衡的部分。

**[REBUT] R2-N1(3): EDCR 需跨 backbone 验证**
R2 的前提有误。EDCR（Eq. 2, Section 3.5）的定义是 Σ|E_i^pred \ E_i^gold| / Σ|E_i^pred|——纯粹比较模型预测的 evidence sentences 与 gold annotations，**不使用任何 NLI model**。EDCR 是 annotation-based 的诊断指标，与 NLI backbone 完全无关。R2 可能将 EDCR 与 CED（Section 3.4, 使用 DeBERTa-v3-base NLI）混淆了。因此"跨 backbone 验证"这一要求对 EDCR 不适用。EDCR 的验证在 Appendix L 中通过 partial correlation、permutation test 和 per-relation 分析完成，且这些验证同样不依赖 NLI backbone。

**[AGREE, 这是本轮最有力的批评之一] R2-N1(4): Evidence tax 主要来自 truncation/duplication**
强烈同意。这是 R2 审稿中最锐利的洞察。论文自己在 Appendix E（Table 9）提供了关键证据：在 matched@2048 fair evaluation 控制了 truncation 率后，1.7B 的 evidence tax **反转为 -5.63pp（beneficial）**，≥4B 近似中性（+0.25±0.47pp）。Appendix K（Table 15）的 error decomposition 进一步确认 truncation FN 是 RSFT 改进的首要机制（1.7B: +811 truncation FN reduction, −275%）。

这意味着：**论文 abstract 和 Contribution 1 中宣称的 "scale-dependent evidence tax" 在 1.7B（效应最显著的规模）实质上是 truncation artifact 而非 evidence 固有代价。** 当控制 output format compliance 后，evidence grounding 在 1.7B 是有益的。论文将 truncation-mediated 的格式限制效应包装为 "evidence tax" 是 framing 上的过度简化。

建议作者在正文中引入 "truncation-induced tax" 和 "information-interference tax" 的区分（如 R2 所建议），并将 Appendix E 的关键发现（matched@2048 结果）提升到正文 Section 4.4。

**[AGREE] R2-N2: 超参数探索不充分**
同意。我在自己的 N3 中已标记 DPO β=0.1 单一设定的问题。R2 进一步指出 GRPO G=8 和 RSFT k=1 也是单点配置，使得 "gradient methods inherently decouple" 的归因缺乏超参数敏感性支撑。特别是：
- DPO β 直接控制偏离 reference policy 的力度，不同 β 下 decoupling 行为可能质变
- RSFT k=1 是最激进的过滤策略，k=3 或 k=5 可能有不同的 extraction-evidence balance
缺少这些消融，论文无法区分 "方法固有属性" 和 "特定超参下的行为"。

**[REBUT] R2-N3: Conclusion 过于简短 → 应降级为 Should-Fix**
不同意将此列为 Must-Fix/critical。Section 5 确实只有约 60 words，但：
1. ARR review form 的 soundness 和 excitement 评分标准中不包含 "conclusion 长度" 维度
2. 论文的 broader implications 和 future directions 已在 Section 4.7 Discussion 中讨论（EDCR 的诊断价值、evidence generation 的推理时间影响、inference overhead analysis reference to Appendix N）
3. Limitations section（p.9）覆盖了 scope、CED sensitivity、RSFT 机制解耦等反思

简短 conclusion 是写作风格偏好，不是 soundness 缺陷。我同意可以适当扩充（加 2-3 句 future directions），但这不应影响接收决定。建议降为 Should-Fix。

---

### Should-Fix

**[AGREE] R2-W1: 遗漏 MTL/gradient conflict 文献**
同意。论文在 Section 4.3 详细讨论了 gradient pressure 导致 evidence-extraction decoupling，这本质上是一个 multi-task gradient conflict 问题。PCGrad（Yu et al. 2020）提出了梯度手术来解决任务间梯度冲突，直接相关。Gao et al. 2023 的 reward overoptimization scaling laws 与 GRPO 的 collapse 行为也有理论联系。这些引用的缺失使得 Related Work 2.2 的理论基础显得薄弱。

**[REBUT] R2-W2: EDCR 与 CED 共享 NLI backbone，circular dependency**
如 N1(3) 的回应所述，这是事实性错误。EDCR（Eq. 2）完全不使用 NLI——它是 gold annotation vs. predicted evidence 的集合差运算。CED（Section 3.4）使用 DeBERTa-v3-base NLI 进行 training data selection。两者没有共享组件，不存在 circular dependency。

具体地：
- **CED** 在训练阶段使用：SFT model → sample N outputs → CED(NLI) scores → select top-k → fine-tune
- **EDCR** 在评估阶段使用：trained model → predict on test set → compare E_pred vs E_gold → compute ratio
两个指标在 pipeline 中的位置完全不同（训练 vs. 评估），输入也不同（NLI logits vs. gold labels）。

**[AGREE] R2-W3: §4.4 信息密度过高**
同意。Section 4.4 在约 1.5 页内叠加了 evidence tax 定义、scale-dependency、CI 分析、cross-seed variance、cross-architecture validation、inference-time tax 等多个层面。尤其 evidence tax 的 CI 跨零这个关键 caveat 容易被淹没在密集文本中。建议拆分为 §4.4 Evidence Tax（含 CI 讨论）和 §4.5 Cross-Scale and Cross-Architecture Patterns。

**[REBUT] R2-W4: "Evidence tax" 术语不直观**
不同意。"Tax" 在经济学和 CS 中是标准隐喻，表示附加特性的代价（如 "abstraction tax"、"safety tax"）。Negative tax = benefit 符合直觉——如果你的 "税" 算出来是负的，你就是在赚钱而不是亏钱。"Evidence delta" 是方向中性的，丢失了论文核心叙事中 "evidence 有代价" 的预设检验框架。"Impact" 优于 "delta" 但不如 "tax" 精准。该术语选择是合理的。

**[AGREE] R2-W5: Re-DocRED test 20pp drop 解释不充分**
同意。论文将 Re-DocRED test 的大幅性能下降归因于 annotation density 差异（Section 4.6 提到 "annotation density"），但没有提供定量支撑（如 dev vs. test 的 average relations per document、evidence sentence coverage 等统计对比）。这个 drop 如果是系统性的，暗示模型对 annotation density 高度敏感，这对实际部署有重要 implication。

---

### Minor

**[AGREE] R2-M1**: Table 2 caption 确实有缩写未展开（如 "sd" 在脚注说明但不够显眼）。
**[AGREE] R2-M2**: "co-optimization" 和 "joint optimization" 术语未统一，应选定一个。
**[AGREE] R2-M3**: matched@2048 的定义在 Appendix E，但 Section 4.4 引用时读者需翻到附录才能理解。鉴于 matched@2048 对理解 evidence tax 至关重要（见 N1(4)），至少应在正文加一句定义。
**[AGREE] R2-M4**: Figure 4 dual y-axis 确实存在视觉误导风险——Rel-F1（40-55 range）和 Evi-F1（0-90 range）共用图面时，Rel-F1 的微小变化被放大。建议改为并排子图。

---

### Missing References

**[AGREE] Yu et al. 2020 PCGrad**: 直接相关，如 W1 所述。
**[AGREE] Gao et al. 2023 Reward Overoptimization Scaling Laws**: 与 GRPO collapse 现象有理论联系。
**[REBUT] Maynez et al. 2020**: 该工作研究 abstractive summarization 的 faithfulness，与 DocRE 的 evidence grounding 问题关联较远。论文已引用了更相关的 faithfulness 文献（Laban et al. 2022, Zhang et al. 2024 在 NLI-based faithfulness evaluation 领域）。
**[AGREE] Rashkin et al. 2023**: Attribution in NLG 与本文的 evidence citation 框架有概念对应关系，值得在 Related Work 2.3 中讨论。

---

### Questions

**[AGREE] R2-Q1**: 与我的 Q2 重合。跨 NLI backbone 对 CED（非 EDCR）的鲁棒性验证是必要的。
**[AGREE, 关键问题] R2-Q2**: Appendix E 的 matched@2048 分析部分回答了这个问题——控制 truncation 后 1.7B tax 反转。但论文应在正文显著位置报告 non-truncated outputs 的纯 evidence tax，而非埋在附录中。
**[AGREE] R2-Q3**: 与我的 N3 重合。DPO β sensitivity 是支撑 spectrum claim 的必要实验。
**[AGREE] R2-Q4**: 与我的 Q3 重合。RSFT k>1 的消融对理解 discrete selection 机制很重要。
**[AGREE] R2-Q5**: 14B 的高 cross-seed variance 加上仅 1 seed SFT baseline（我的 W2），确实暗示 evidence tax 在更大规模可能不稳定。这需要更多 seeds 来确认。

---

### 总结

R2 的审稿中最有价值的贡献是 **N1(4)**：evidence tax 的 truncation-mediation 机制。这一观点得到论文自己 Appendix E 和 K 的数据支撑，但论文正文的 framing 没有充分反映这一关键 nuance。

R2 的主要事实性错误是 **W2**：EDCR 和 CED 不共享 NLI backbone，不存在 circular dependency。

R2 将 Conclusion 长度列为 critical 我认为过重——这是写作偏好而非 soundness 问题。

综合 R2 的意见，我维持自己的 Overall 3.5（Borderline Conference）不变。N1(4) 的 truncation-mediation 论点加强了我对 evidence tax claim 统计支撑不足的担忧（我的 N1），但 EDCR 的扎实验证和 RSFT 跨规模一致性仍有 Findings-level 贡献。

---

[Reviewer 1 审稿结果]:
逐条回应已提交至 Review Director。核心判断：

- **强烈同意 R2-N1(4)**：evidence tax 的 truncation-mediation 机制是本轮最有力的批评，论文自己的 Appendix E 数据（matched@2048 下 1.7B tax 反转为 beneficial）直接支撑了这一论点
- **反驳 R2-W2**：EDCR 不使用 NLI backbone（纯 gold annotation 比较），R2 混淆了 EDCR 和 CED
- **反驳 R2-N3**：Conclusion 长度是写作偏好，不应列为 critical
- 其余 Must-Fix（N1(1)(2), N2）和大部分 Should-Fix/Minor 均同意
- 维持 Overall 3.5 不变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-25T23:01:21.723857+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "faith-evidence-ie",
  "issues_yaml": "- id: \"W1\"\n  summary: \"GRPO QLoRA vs bf16 confounded variables — quantization, lr, group size not isolated\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Cannot support causal attribution of decoupling to QLoRA\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Table 3 shows QLoRA G=4 vs bf16 G=8 — two variables changed simultaneously. §4.3 attribution unsupported. Need bf16 G=4 or QLoRA G=8 control. Both AGREE Must-Fix.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"bf16 G=4 added (Rel-F1 28.73) — partially helps but reveals group size causes 16.76pp drop (45.49→28.73). lr confound 10× (5e-6 vs 5e-5) described as 'residual' is understated. 'attributable to quantization precision' still too strong. Downgrade to Should-Fix given partial progress.\"}\n  action_items:\n    - {round: 1, action: \"Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade causal claim to observational\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Deepen GRPO mechanism analysis with reward hacking lit + mechanistic chain\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Run GRPO bf16 G=4 experiment\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 4, action: \"Weaken attribution language: 'is attributable to' → 'is primarily consistent with'. Acknowledge lr 10× difference explicitly.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W2\"\n  summary: \"All results dev-set only, no test set\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"No CodaLab test results\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Test set results now exist (Table 9). Method ranking preserved (ρ=1.0).\"}\n  action_items:\n    - {round: 1, action: \"Add test set evaluation for all scales\", assigned_to: \"Agent+User\", status: \"done\"}\n  resolution: \"Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0).\"\n  resolution_round: 2\n\n- id: \"W3\"\n  summary: \"Variance compression claim statistically underpowered + cherry-picking in abstract\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"SFT single seed, +4.92pp lacks stats\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"n=3 per config, σ 95% CI overlapping. Both recommend ≥5 seeds or downgrade.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Only 1.7B χ² CI non-overlapping; other 3 scales overlap. Sign test p=0.0625. 4B Cohen's d=0.46 small. Abstract cherry-picks. Both AGREE Must-Fix.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Contribution 3 downgraded to observation ✓. Caveats added ✓. But §4.4 still devotes ~250 words + precise compression ratios (32.6×, 7.5×, 6.5×) + '36× more predictable' to variance — disproportionate for acknowledged weak evidence. Compress to 2-3 sentences, move ratios to appendix.\"}\n  action_items:\n    - {round: 1, action: \"Run SFT seed43+seed44, compute bootstrap CI\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Downgrade Abstract/Contributions to 'consistently reduces'. Three-layer evidence in appendix.\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n    - {round: 3, action: \"Remove variance as standalone abstract contribution. Downgrade to observation in §4.2 with explicit caveats.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Compress §4.4 variance discussion to 2-3 sentences. Move precise compression ratios to appendix. Remove '36× more predictable' phrasing.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W4\"\n  summary: \"Scaling claim based on limited data points\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"3 points insufficient, 1.7B repetition artifact\"}\n    - {round: 2, reviewers: \"R2\", note: \"4 Qwen + 1 LLaMA still limited for general scaling claim.\"}\n    - {round: 3, note: \"Not directly re-raised in Round 3.\"}\n    - {round: 4, note: \"Not raised. Paper now uses 'scale-dependent' rather than 'non-monotonic'. 5 models across 2 families.\"}\n  action_items:\n    - {round: 1, action: \"Replace 'non-monotonic' with 'scale-dependent', add LLaMA\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5\"\n  summary: \"EDCR shared-component mechanical negative correlation with Rel-F1\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"ρ=-0.965 partially predetermined\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"TP in numerator and denominator. n=7 too small. Request partial correlation, permutation test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"DIVERGENCE. R1 wants per-relation precision partial correlation. R2 considers per-relation n=76 sufficient. Director: WARNING.\"}\n    - {round: 4, reviewers: \"R1\", note: \"R1 confirms EDCR is purely annotation-based (Eq. 2), does NOT use NLI. R2 confused EDCR with CED. No circular dependency exists. Per-relation validation (n=76) + partial correlation + permutation test are solid.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicate to n=7, per-relation n=76\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade EDCR to diagnostic tool + caveat\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Compute partial correlation + permutation test + similar-TP pairs\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Add partial correlation + permutation test to appendix\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Add per-relation precision partial correlation as additional robustness check\", assigned_to: \"Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5-EDCR-INFLATION\"\n  summary: \"EDCR ρ inflated by non-independent data points and GRPO QLoRA outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"Research Reviewer\", note: \"n=7 ρ=-0.89, n=6 (no QLoRA) ρ=-0.83 p=0.042\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Re-raised: n=6 borderline significant.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion.\"}\n    - {round: 4, note: \"Not raised. Per-relation validation (n=76) provides robust independent evidence.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 sans-QLoRA + partial ρ + permutation in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W6\"\n  summary: \"CED ≈ flat-NLI (0.02pp), contrastive formulation adds no measurable value\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Contrastive adds complexity without improvement\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"0.02pp within noise. CED cannot be method contribution.\"}\n    - {round: 3, reviewers: \"R2\", note: \"CED's unique contribution is interpretability, not data selection quality.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Both agree: §3.4 effort-vs-payoff most imbalanced part. But correctly positioned as scoring variant. No contribution language.\"}\n  action_items:\n    - {round: 1, action: \"Remove CED as independent contribution\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Position as scoring variant, no contribution language\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"CED correctly positioned as scoring variant with no contribution language. 0.02pp difference honestly reported.\"\n  resolution_round: 4\n\n- id: \"W7\"\n  summary: \"Training data quantity contradiction (9042 vs 2718)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"k=3 vs k=1 root cause\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining + update section 3.3\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Paper now consistently reports k=1 with ~3000 training samples.\"\n  resolution_round: 2\n\n- id: \"W8\"\n  summary: \"EDCR ρ based on n=6, not significant without outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\"}\n    - {round: 2, reviewers: \"R1\", note: \"n=7 still small, GRPO QLoRA outlier dominance.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion.\"}\n    - {round: 4, note: \"Not raised. Per-relation validation (n=76) provides robust independent evidence.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 remove-outlier + partial correlation + permutation in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W9\"\n  summary: \"'matches' 50.50 vs 50.51 statistically meaningless\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Single seed, 0.01pp < any reasonable variance\"}\n  action_items:\n    - {round: 1, action: \"Change 'matches' to 'approaches'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Changed to 'approaches' throughout.\"\n  resolution_round: 2\n\n- id: \"W10\"\n  summary: \"Encoder baseline comparison selective in metrics presentation\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DREEAM 54.01% buried in text\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 12 emphasizes TP-only Evi-F1, downplays 16-18pp Ign-F1 gap.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n    - {round: 4, note: \"Not raised. Appendix H now explicitly discusses Ign-F1 gap.\"}\n  action_items:\n    - {round: 1, action: \"Add encoder baseline comparison table\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Balance discussion: acknowledge Ign-F1 gap\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Encoder comparison balanced with explicit Ign-F1 gap discussion in Appendix H.\"\n  resolution_round: 4\n\n- id: \"W11\"\n  summary: \"GRPO/DPO hyperparameter exploration insufficient — DPO β=0.1, GRPO G=8, RSFT k=1 all single point\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"GRPO only KL=0.01, DPO only beta=0.1\"}\n    - {round: 2, reviewers: \"R2\", note: \"No KL ablation, no reward normalization test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both strongly agree. DPO β=0.1 → -11pp drop suspicious. Spectrum built on single β.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"4th round recurring. R1 cross-response adds: RSFT k=1 is most aggressive filter — k=3/k=5 may show different extraction-evidence balance. Cannot distinguish 'method inherent property' from 'specific hyperparameter behavior' without sweeps.\"}\n  action_items:\n    - {round: 1, action: \"Acknowledge in Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add explicit KL caveat to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Run DPO β=0.01 experiment\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Complete β∈{0.01,0.05} sweep OR limit all DPO conclusions to 'under β=0.1'. Also consider RSFT k>1 ablation.\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W12\"\n  summary: \"Metric format inconsistency\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Percentage vs decimal mixed\"}\n  action_items:\n    - {round: 1, action: \"Unify to percentage format\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Unified to percentage format.\"\n  resolution_round: 2\n\n- id: \"W13\"\n  summary: \"Missing references (LMRC, SummaC, RelPrior, Rationale Verification)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"15 'and others', author mismatches\"}\n    - {round: 2, reviewers: \"R2,R1\", note: \"Missing LMRC, SummaC, RelPrior, Rationale Verification.\"}\n    - {round: 3, note: \"Not raised. Missing references confirmed added.\"}\n  action_items:\n    - {round: 1, action: \"Fix bib errors\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add LMRC, SummaC, RelPrior, Rationale Verification, QuRL\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All missing references added. DeepSeek-R1 and ReST also added in Round 3-4.\"\n  resolution_round: 3\n\n- id: \"W14\"\n  summary: \"1.7B implicit regularization speculation without evidence\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Fair evaluation subset undefined\"}\n  action_items:\n    - {round: 1, action: \"Define fair subset + mechanistic breakdown\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Fair subset defined in Appendix D. Mechanistic breakdown added.\"\n  resolution_round: 2\n\n- id: \"W15\"\n  summary: \"Multi-seed coverage uneven\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Table 3: 3/4 rows single seed\"}\n    - {round: 2, note: \"1.7B/4B/8B/LLaMA now 3-seed. 14B still single seed.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"SFT no-evidence baseline only s42 for 1.7B/8B. 1.7B s42 is strongest seed (+3.22pp above mean).\"}\n    - {round: 4, note: \"Not raised as major. Paper acknowledges 1.7B s42 as strongest seed in Appendix F.\"}\n  action_items:\n    - {round: 1, action: \"Add seeds for 8B/1.7B/LLaMA\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 3, action: \"Add caveat in §4.4: 1.7B/8B no-evidence SFT is single seed (s42)\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W16\"\n  summary: \"Missing multi-task learning / task interference references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Core finding is negative transfer, needs MTL literature\"}\n  action_items:\n    - {round: 1, action: \"Add MTL references to Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"MTL references added. Not re-raised.\"\n  resolution_round: 2\n\n- id: \"W17\"\n  summary: \"DPO 3-epoch uses different evaluation protocol — checkpoint lost\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DPO 3ep different protocol, pollutes spectrum\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Footnote 1 insufficient. Checkpoint confirmed lost.\"}\n  action_items:\n    - {round: 1, action: \"Remove internal numbering\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"DPO rebuild: retrain 1ep+3ep under unified protocol\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Update paper with new DPO numbers, remove footnote\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"DPO rebuilt from scratch, both epochs under matched@2048 protocol.\"\n  resolution_round: 3\n\n- id: \"W18\"\n  summary: \"Missing random selection baseline for RSFT\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1\", note: \"Need random-k=1 to prove selection value\"}\n  action_items:\n    - {round: 1, action: \"Run random k=1 RSFT baseline\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Random k=1 baseline added: 41.14 vs CED RSFT 44.66.\"\n  resolution_round: 2\n\n- id: \"FMT-CHECKLIST\"\n  summary: \"Responsible NLP Checklist\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"ARR mandatory\"}\n  action_items:\n    - {round: 1, action: \"Checklist via OpenReview form\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Submitted via OpenReview form.\"\n  resolution_round: 2\n\n- id: \"FMT-APPENDIX-RELCOUNT\"\n  summary: \"Appendix figure relation type count inconsistency\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"93 vs 76 vs 96 conflicting\"}\n  action_items:\n    - {round: 1, action: \"Clarify caption\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Caption clarified.\"\n  resolution_round: 2\n\n- id: \"R2-W1-NOVELTY\"\n  summary: \"Method novelty insufficient — contributions are empirical observations\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"CRITICAL: all 3 contributions empirical. R1 downgrades to MAJOR.\"}\n    - {round: 3, note: \"Implicitly addressed by empirical study framing.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"R1 agrees RSFT = STaR + CED = engineering contribution. Paper positioned as empirical study ✓. But 'introduce EDCR' and Contribution 3 'RSFT improves extraction without decoupling' still read as method contributions. Need 'empirical finding: discrete selection avoids decoupling'.\"}\n  action_items:\n    - {round: 2, action: \"Reposition as empirical study, remove method-innovation language\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Replace 'introduce' with 'use'/'employ' for EDCR; reframe Contribution 3 as empirical finding\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5-NLI-SENSITIVITY\"\n  summary: \"CED sensitivity to NLI model family not analyzed\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Only DeBERTa v3 tested.\"}\n    - {round: 3, reviewers: \"R1\", note: \"Template sensitivity. R2 notes 0.02pp impact limited.\"}\n    - {round: 4, reviewers: \"R1\", note: \"R1 cross-response agrees CED (not EDCR) cross-backbone validation is necessary. DeBERTa-v3-base vs v3-large shows +1.10pp within seed noise — promising but same family.\"}\n  action_items:\n    - {round: 2, action: \"Added to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-VARIANCE-SOURCE\"\n  summary: \"SFT vs RSFT variance measures different sources of randomness\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"SFT = full training randomness; RSFT = fixed-base. Comparison unfair.\"}\n    - {round: 3, reviewers: \"R2\", note: \"Confirms RSFT naturally compresses upstream variance.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"R2 partially rebutted R1: practical value argument. R1 maintains methodological concern. Paper has caveat ✓ but precise ratios and 'predictable' language undermine it. Director: WARNING.\"}\n  action_items:\n    - {round: 2, action: \"Downgraded to 'consistently reduces' + acknowledged asymmetry\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Full downgrade of variance to observation.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Compress variance text, remove '36× more predictable', move precise ratios to appendix\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-LIMITATIONS\"\n  summary: \"Limitations section omissions\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"DocRED annotations, compute cost, task generalization.\"}\n  action_items:\n    - {round: 2, action: \"Added 4 points to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All points addressed in Limitations section.\"\n  resolution_round: 3\n\n- id: \"R2-W10-LLM-BASELINE\"\n  summary: \"Missing direct numerical comparison with LLM-based RE methods\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"AutoRE/GLiDRE numbers missing.\"}\n  action_items:\n    - {round: 2, action: \"Added inline comparison in Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Inline numerical comparison added.\"\n  resolution_round: 3\n\n- id: \"VISUAL-MAIN-FIGURES\"\n  summary: \"Main text figures insufficient\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Pages 1-5 no visual anchor.\"}\n  action_items:\n    - {round: 2, action: \"Added fig_overview, fig_spectrum, fig_evidence_tax.\", assigned_to: \"Paper Agent + Director\", status: \"done\"}\n  resolution: \"Main text now has 5 figures well-distributed across pages.\"\n  resolution_round: 4\n\n- id: \"VISUAL-COLORBLIND\"\n  summary: \"Figure colorblind accessibility issues\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Figure 4 red-green. Fixed with Okabe-Ito.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Figure 10 (p18) still uses red/green/blue.\"}\n    - {round: 4, note: \"Not raised as major. Appendix figure, minor impact.\"}\n  action_items:\n    - {round: 2, action: \"Figure 4 changed to Okabe-Ito\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 3, action: \"Figure 10 change to Okabe-Ito or add hatching\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W9-4B-CHECKPOINT\"\n  summary: \"4B retrained checkpoint dev gap 0.35pp may affect evidence tax\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"Original 4B unavailable, retrained 43.88 vs 44.23.\"}\n    - {round: 3, note: \"Not raised.\"}\n    - {round: 4, note: \"Not raised. Minor gap within seed noise.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1-IMPLICIT-REG\"\n  summary: \"Implicit regularization hypothesis indistinguishable from output constraint effect\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. More parsimonious: output budget constraint.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"NOT renamed. §4.4 and Appendix E still use 'implicit regularization hypothesis'. R1 cross-response: evidence tax at 1.7B is primarily truncation-mediated — the 'regularization' is just format constraint, not a learning effect.\"}\n  action_items:\n    - {round: 3, action: \"Rename 'implicit regularization' to 'structural output constraint'.\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Replace all 'implicit regularization' with 'structural output constraint'. Add dual-mechanism discussion with matched@2048 counter-evidence.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2-14B-REVERSAL\"\n  summary: \"14B test-set reversal: SFT outperforms RSFT, explanation insufficient\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Need precision/recall decomposition.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"No precision/recall decomposition provided. R1 cross-response: 14B high cross-seed variance + 1 SFT seed → evidence tax at larger scale may be unstable, needs more seeds.\"}\n  action_items:\n    - {round: 3, action: \"Extract precision/recall from 14B test-set predictions\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Provide precision/recall decomposition OR acknowledge single-SFT-seed limitation\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3-RSFT-TRADEOFF\"\n  summary: \"RSFT 'cannot exploit trade-off' claim purely structural, lacks empirical test\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Need single-objective RSFT or downgrade to hypothesis.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Still no experiment. R1 adds: RSFT k>1 ablation also needed to understand discrete selection mechanism.\"}\n  action_items:\n    - {round: 3, action: \"Run single-objective RSFT\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Complete single-objective RSFT OR downgrade 'cannot exploit' to hypothesis\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-FMT-PAGELIMIT\"\n  summary: \"Main text exceeds 8-page limit (desk reject risk)\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. §4.7 + §5 overflow to p9.\"}\n    - {round: 4, note: \"RESOLVED. Conclusion compressed to 2 sentences. Main text fits 8 pages.\"}\n  action_items:\n    - {round: 3, action: \"Compress §4.7 + §5.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Main text now fits within 8 pages.\"\n  resolution_round: 4\n\n- id: \"R3-M1-SPECTRUM-SCALE\"\n  summary: \"Decoupling spectrum validated only at 4B scale\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Should appear in Limitations.\"}\n    - {round: 4, note: \"RESOLVED. Limitations now states spectrum is 4B only.\"}\n  action_items:\n    - {round: 3, action: \"Add to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Added to Limitations section.\"\n  resolution_round: 4\n\n- id: \"R3-M2-TAX-CONVENTION\"\n  summary: \"Evidence tax sign convention inconsistent across sections\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Inconsistent across tables/figures.\"}\n    - {round: 4, note: \"RESOLVED. Convention consistent throughout.\"}\n  action_items:\n    - {round: 3, action: \"Unify sign convention.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Sign convention unified throughout.\"\n  resolution_round: 4\n\n- id: \"R4-EDCR-CONSISTENCY\"\n  summary: \"EDCR ρ numerical inconsistency across sections (Round 3 W-SF5)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"§3.5 ρ=-0.89 vs §4.7 ρ=-0.96 vs Appendix ρ=-0.9643.\"}\n    - {round: 4, note: \"RESOLVED. All now consistently ρ=-0.96 / -0.9643.\"}\n  action_items:\n    - {round: 3, action: \"Unify EDCR ρ values\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All EDCR ρ values now consistent.\"\n  resolution_round: 4\n\n- id: \"R4-TAX-TRUNCATION\"\n  summary: \"Evidence tax at 1.7B is primarily truncation-mediated, not inherent evidence cost\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"R1 calls this 'the most incisive observation'. Appendix E matched@2048: 1.7B tax reverses to -5.63pp (beneficial). Appendix K: truncation FN is #1 RSFT improvement mechanism (-22% at 1.7B). Abstract/Contribution 1 'scale-dependent evidence tax' at 1.7B is truncation artifact, not inherent evidence cost. Paper buries this in appendix. R1 recommends distinguishing 'truncation-induced tax' from 'information-interference tax' and promoting matched@2048 findings to main text.\"}\n  action_items:\n    - {round: 4, action: \"Distinguish truncation-induced vs information-interference components of evidence tax in §4.4. Promote matched@2048 key finding to main text (currently Appendix E/F). Revise Contribution 1 framing.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-MISSING-REFS\"\n  summary: \"Missing references: PCGrad, Rashkin et al. 2023 Attribution\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"PCGrad (Yu et al. 2020): gradient surgery for multi-task conflict, directly relevant to §4.3 gradient pressure discussion. Rashkin et al. 2023: Attribution in NLG, conceptual correspondence to evidence citation. R1 agrees on both. R1 rebuts Maynez et al. 2020 (too distant from DocRE).\"}\n  action_items:\n    - {round: 4, action: \"Add PCGrad (Yu et al. 2020) to §2.2 and Rashkin et al. 2023 to §2.3\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-SECTION44-DENSITY\"\n  summary: \"§4.4 information density too high — tax definition, CI, variance, cross-arch all in 1.5 pages\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"R1 agrees with R2: §4.4 packs too many layers (tax definition, scale-dependency, CI analysis, cross-seed variance, cross-architecture, inference-time tax). CI-crosses-zero caveat easily drowned. R1 suggests splitting into §4.4 Evidence Tax (with CI) and §4.5 Cross-Scale/Cross-Architecture.\"}\n  action_items:\n    - {round: 4, action: \"Split §4.4 into two subsections or compress variance portion to reduce density\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "faith-evidence-ie",
    "issues_yaml": "- id: \"W1\"\n  summary: \"GRPO QLoRA vs bf16 confounded variables — quantization, lr, group size not isolated\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Cannot support causal attribution of decoupling to QLoRA\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Table 3 shows QLoRA G=4 vs bf16 G=8 — two variables changed simultaneously. §4.3 attribution unsupported. Need bf16 G=4 or QLoRA G=8 control. Both AGREE Must-Fix.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"bf16 G=4 added (Rel-F1 28.73) — partially helps but reveals group size causes 16.76pp drop (45.49→28.73). lr confound 10× (5e-6 vs 5e-5) described as 'residual' is understated. 'attributable to quantization precision' still too strong. Downgrade to Should-Fix given partial progress.\"}\n  action_items:\n    - {round: 1, action: \"Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade causal claim to observational\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Deepen GRPO mechanism analysis with reward hacking lit + mechanistic chain\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Run GRPO bf16 G=4 experiment\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 4, action: \"Weaken attribution language: 'is attributable to' → 'is primarily consistent with'. Acknowledge lr 10× difference explicitly.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W2\"\n  summary: \"All results dev-set only, no test set\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"No CodaLab test results\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Test set results now exist (Table 9). Method ranking preserved (ρ=1.0).\"}\n  action_items:\n    - {round: 1, action: \"Add test set evaluation for all scales\", assigned_to: \"Agent+User\", status: \"done\"}\n  resolution: \"Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0).\"\n  resolution_round: 2\n\n- id: \"W3\"\n  summary: \"Variance compression claim statistically underpowered + cherry-picking in abstract\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"SFT single seed, +4.92pp lacks stats\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"n=3 per config, σ 95% CI overlapping. Both recommend ≥5 seeds or downgrade.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Only 1.7B χ² CI non-overlapping; other 3 scales overlap. Sign test p=0.0625. 4B Cohen's d=0.46 small. Abstract cherry-picks. Both AGREE Must-Fix.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Contribution 3 downgraded to observation ✓. Caveats added ✓. But §4.4 still devotes ~250 words + precise compression ratios (32.6×, 7.5×, 6.5×) + '36× more predictable' to variance — disproportionate for acknowledged weak evidence. Compress to 2-3 sentences, move ratios to appendix.\"}\n  action_items:\n    - {round: 1, action: \"Run SFT seed43+seed44, compute bootstrap CI\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Downgrade Abstract/Contributions to 'consistently reduces'. Three-layer evidence in appendix.\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n    - {round: 3, action: \"Remove variance as standalone abstract contribution. Downgrade to observation in §4.2 with explicit caveats.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Compress §4.4 variance discussion to 2-3 sentences. Move precise compression ratios to appendix. Remove '36× more predictable' phrasing.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W4\"\n  summary: \"Scaling claim based on limited data points\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"3 points insufficient, 1.7B repetition artifact\"}\n    - {round: 2, reviewers: \"R2\", note: \"4 Qwen + 1 LLaMA still limited for general scaling claim.\"}\n    - {round: 3, note: \"Not directly re-raised in Round 3.\"}\n    - {round: 4, note: \"Not raised. Paper now uses 'scale-dependent' rather than 'non-monotonic'. 5 models across 2 families.\"}\n  action_items:\n    - {round: 1, action: \"Replace 'non-monotonic' with 'scale-dependent', add LLaMA\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5\"\n  summary: \"EDCR shared-component mechanical negative correlation with Rel-F1\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"ρ=-0.965 partially predetermined\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"TP in numerator and denominator. n=7 too small. Request partial correlation, permutation test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"DIVERGENCE. R1 wants per-relation precision partial correlation. R2 considers per-relation n=76 sufficient. Director: WARNING.\"}\n    - {round: 4, reviewers: \"R1\", note: \"R1 confirms EDCR is purely annotation-based (Eq. 2), does NOT use NLI. R2 confused EDCR with CED. No circular dependency exists. Per-relation validation (n=76) + partial correlation + permutation test are solid.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicate to n=7, per-relation n=76\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade EDCR to diagnostic tool + caveat\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Compute partial correlation + permutation test + similar-TP pairs\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Add partial correlation + permutation test to appendix\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Add per-relation precision partial correlation as additional robustness check\", assigned_to: \"Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5-EDCR-INFLATION\"\n  summary: \"EDCR ρ inflated by non-independent data points and GRPO QLoRA outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"Research Reviewer\", note: \"n=7 ρ=-0.89, n=6 (no QLoRA) ρ=-0.83 p=0.042\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Re-raised: n=6 borderline significant.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion.\"}\n    - {round: 4, note: \"Not raised. Per-relation validation (n=76) provides robust independent evidence.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 sans-QLoRA + partial ρ + permutation in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W6\"\n  summary: \"CED ≈ flat-NLI (0.02pp), contrastive formulation adds no measurable value\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Contrastive adds complexity without improvement\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"0.02pp within noise. CED cannot be method contribution.\"}\n    - {round: 3, reviewers: \"R2\", note: \"CED's unique contribution is interpretability, not data selection quality.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Both agree: §3.4 effort-vs-payoff most imbalanced part. But correctly positioned as scoring variant. No contribution language.\"}\n  action_items:\n    - {round: 1, action: \"Remove CED as independent contribution\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Position as scoring variant, no contribution language\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"CED correctly positioned as scoring variant with no contribution language. 0.02pp difference honestly reported.\"\n  resolution_round: 4\n\n- id: \"W7\"\n  summary: \"Training data quantity contradiction (9042 vs 2718)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"k=3 vs k=1 root cause\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining + update section 3.3\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Paper now consistently reports k=1 with ~3000 training samples.\"\n  resolution_round: 2\n\n- id: \"W8\"\n  summary: \"EDCR ρ based on n=6, not significant without outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\"}\n    - {round: 2, reviewers: \"R1\", note: \"n=7 still small, GRPO QLoRA outlier dominance.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion.\"}\n    - {round: 4, note: \"Not raised. Per-relation validation (n=76) provides robust independent evidence.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 remove-outlier + partial correlation + permutation in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W9\"\n  summary: \"'matches' 50.50 vs 50.51 statistically meaningless\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Single seed, 0.01pp < any reasonable variance\"}\n  action_items:\n    - {round: 1, action: \"Change 'matches' to 'approaches'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Changed to 'approaches' throughout.\"\n  resolution_round: 2\n\n- id: \"W10\"\n  summary: \"Encoder baseline comparison selective in metrics presentation\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DREEAM 54.01% buried in text\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 12 emphasizes TP-only Evi-F1, downplays 16-18pp Ign-F1 gap.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n    - {round: 4, note: \"Not raised. Appendix H now explicitly discusses Ign-F1 gap.\"}\n  action_items:\n    - {round: 1, action: \"Add encoder baseline comparison table\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Balance discussion: acknowledge Ign-F1 gap\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Encoder comparison balanced with explicit Ign-F1 gap discussion in Appendix H.\"\n  resolution_round: 4\n\n- id: \"W11\"\n  summary: \"GRPO/DPO hyperparameter exploration insufficient — DPO β=0.1, GRPO G=8, RSFT k=1 all single point\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"GRPO only KL=0.01, DPO only beta=0.1\"}\n    - {round: 2, reviewers: \"R2\", note: \"No KL ablation, no reward normalization test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both strongly agree. DPO β=0.1 → -11pp drop suspicious. Spectrum built on single β.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"4th round recurring. R1 cross-response adds: RSFT k=1 is most aggressive filter — k=3/k=5 may show different extraction-evidence balance. Cannot distinguish 'method inherent property' from 'specific hyperparameter behavior' without sweeps.\"}\n  action_items:\n    - {round: 1, action: \"Acknowledge in Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add explicit KL caveat to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Run DPO β=0.01 experiment\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Complete β∈{0.01,0.05} sweep OR limit all DPO conclusions to 'under β=0.1'. Also consider RSFT k>1 ablation.\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W12\"\n  summary: \"Metric format inconsistency\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Percentage vs decimal mixed\"}\n  action_items:\n    - {round: 1, action: \"Unify to percentage format\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Unified to percentage format.\"\n  resolution_round: 2\n\n- id: \"W13\"\n  summary: \"Missing references (LMRC, SummaC, RelPrior, Rationale Verification)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"15 'and others', author mismatches\"}\n    - {round: 2, reviewers: \"R2,R1\", note: \"Missing LMRC, SummaC, RelPrior, Rationale Verification.\"}\n    - {round: 3, note: \"Not raised. Missing references confirmed added.\"}\n  action_items:\n    - {round: 1, action: \"Fix bib errors\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add LMRC, SummaC, RelPrior, Rationale Verification, QuRL\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All missing references added. DeepSeek-R1 and ReST also added in Round 3-4.\"\n  resolution_round: 3\n\n- id: \"W14\"\n  summary: \"1.7B implicit regularization speculation without evidence\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Fair evaluation subset undefined\"}\n  action_items:\n    - {round: 1, action: \"Define fair subset + mechanistic breakdown\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Fair subset defined in Appendix D. Mechanistic breakdown added.\"\n  resolution_round: 2\n\n- id: \"W15\"\n  summary: \"Multi-seed coverage uneven\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Table 3: 3/4 rows single seed\"}\n    - {round: 2, note: \"1.7B/4B/8B/LLaMA now 3-seed. 14B still single seed.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"SFT no-evidence baseline only s42 for 1.7B/8B. 1.7B s42 is strongest seed (+3.22pp above mean).\"}\n    - {round: 4, note: \"Not raised as major. Paper acknowledges 1.7B s42 as strongest seed in Appendix F.\"}\n  action_items:\n    - {round: 1, action: \"Add seeds for 8B/1.7B/LLaMA\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 3, action: \"Add caveat in §4.4: 1.7B/8B no-evidence SFT is single seed (s42)\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W16\"\n  summary: \"Missing multi-task learning / task interference references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Core finding is negative transfer, needs MTL literature\"}\n  action_items:\n    - {round: 1, action: \"Add MTL references to Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"MTL references added. Not re-raised.\"\n  resolution_round: 2\n\n- id: \"W17\"\n  summary: \"DPO 3-epoch uses different evaluation protocol — checkpoint lost\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DPO 3ep different protocol, pollutes spectrum\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Footnote 1 insufficient. Checkpoint confirmed lost.\"}\n  action_items:\n    - {round: 1, action: \"Remove internal numbering\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"DPO rebuild: retrain 1ep+3ep under unified protocol\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Update paper with new DPO numbers, remove footnote\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"DPO rebuilt from scratch, both epochs under matched@2048 protocol.\"\n  resolution_round: 3\n\n- id: \"W18\"\n  summary: \"Missing random selection baseline for RSFT\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1\", note: \"Need random-k=1 to prove selection value\"}\n  action_items:\n    - {round: 1, action: \"Run random k=1 RSFT baseline\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Random k=1 baseline added: 41.14 vs CED RSFT 44.66.\"\n  resolution_round: 2\n\n- id: \"FMT-CHECKLIST\"\n  summary: \"Responsible NLP Checklist\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"ARR mandatory\"}\n  action_items:\n    - {round: 1, action: \"Checklist via OpenReview form\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Submitted via OpenReview form.\"\n  resolution_round: 2\n\n- id: \"FMT-APPENDIX-RELCOUNT\"\n  summary: \"Appendix figure relation type count inconsistency\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"93 vs 76 vs 96 conflicting\"}\n  action_items:\n    - {round: 1, action: \"Clarify caption\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Caption clarified.\"\n  resolution_round: 2\n\n- id: \"R2-W1-NOVELTY\"\n  summary: \"Method novelty insufficient — contributions are empirical observations\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"CRITICAL: all 3 contributions empirical. R1 downgrades to MAJOR.\"}\n    - {round: 3, note: \"Implicitly addressed by empirical study framing.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"R1 agrees RSFT = STaR + CED = engineering contribution. Paper positioned as empirical study ✓. But 'introduce EDCR' and Contribution 3 'RSFT improves extraction without decoupling' still read as method contributions. Need 'empirical finding: discrete selection avoids decoupling'.\"}\n  action_items:\n    - {round: 2, action: \"Reposition as empirical study, remove method-innovation language\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Replace 'introduce' with 'use'/'employ' for EDCR; reframe Contribution 3 as empirical finding\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5-NLI-SENSITIVITY\"\n  summary: \"CED sensitivity to NLI model family not analyzed\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Only DeBERTa v3 tested.\"}\n    - {round: 3, reviewers: \"R1\", note: \"Template sensitivity. R2 notes 0.02pp impact limited.\"}\n    - {round: 4, reviewers: \"R1\", note: \"R1 cross-response agrees CED (not EDCR) cross-backbone validation is necessary. DeBERTa-v3-base vs v3-large shows +1.10pp within seed noise — promising but same family.\"}\n  action_items:\n    - {round: 2, action: \"Added to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-VARIANCE-SOURCE\"\n  summary: \"SFT vs RSFT variance measures different sources of randomness\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"SFT = full training randomness; RSFT = fixed-base. Comparison unfair.\"}\n    - {round: 3, reviewers: \"R2\", note: \"Confirms RSFT naturally compresses upstream variance.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"R2 partially rebutted R1: practical value argument. R1 maintains methodological concern. Paper has caveat ✓ but precise ratios and 'predictable' language undermine it. Director: WARNING.\"}\n  action_items:\n    - {round: 2, action: \"Downgraded to 'consistently reduces' + acknowledged asymmetry\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Full downgrade of variance to observation.\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 4, action: \"Compress variance text, remove '36× more predictable', move precise ratios to appendix\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-LIMITATIONS\"\n  summary: \"Limitations section omissions\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"DocRED annotations, compute cost, task generalization.\"}\n  action_items:\n    - {round: 2, action: \"Added 4 points to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All points addressed in Limitations section.\"\n  resolution_round: 3\n\n- id: \"R2-W10-LLM-BASELINE\"\n  summary: \"Missing direct numerical comparison with LLM-based RE methods\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"AutoRE/GLiDRE numbers missing.\"}\n  action_items:\n    - {round: 2, action: \"Added inline comparison in Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Inline numerical comparison added.\"\n  resolution_round: 3\n\n- id: \"VISUAL-MAIN-FIGURES\"\n  summary: \"Main text figures insufficient\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Pages 1-5 no visual anchor.\"}\n  action_items:\n    - {round: 2, action: \"Added fig_overview, fig_spectrum, fig_evidence_tax.\", assigned_to: \"Paper Agent + Director\", status: \"done\"}\n  resolution: \"Main text now has 5 figures well-distributed across pages.\"\n  resolution_round: 4\n\n- id: \"VISUAL-COLORBLIND\"\n  summary: \"Figure colorblind accessibility issues\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Figure 4 red-green. Fixed with Okabe-Ito.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Figure 10 (p18) still uses red/green/blue.\"}\n    - {round: 4, note: \"Not raised as major. Appendix figure, minor impact.\"}\n  action_items:\n    - {round: 2, action: \"Figure 4 changed to Okabe-Ito\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 3, action: \"Figure 10 change to Okabe-Ito or add hatching\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W9-4B-CHECKPOINT\"\n  summary: \"4B retrained checkpoint dev gap 0.35pp may affect evidence tax\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"Original 4B unavailable, retrained 43.88 vs 44.23.\"}\n    - {round: 3, note: \"Not raised.\"}\n    - {round: 4, note: \"Not raised. Minor gap within seed noise.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1-IMPLICIT-REG\"\n  summary: \"Implicit regularization hypothesis indistinguishable from output constraint effect\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. More parsimonious: output budget constraint.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"NOT renamed. §4.4 and Appendix E still use 'implicit regularization hypothesis'. R1 cross-response: evidence tax at 1.7B is primarily truncation-mediated — the 'regularization' is just format constraint, not a learning effect.\"}\n  action_items:\n    - {round: 3, action: \"Rename 'implicit regularization' to 'structural output constraint'.\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Replace all 'implicit regularization' with 'structural output constraint'. Add dual-mechanism discussion with matched@2048 counter-evidence.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2-14B-REVERSAL\"\n  summary: \"14B test-set reversal: SFT outperforms RSFT, explanation insufficient\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Need precision/recall decomposition.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"No precision/recall decomposition provided. R1 cross-response: 14B high cross-seed variance + 1 SFT seed → evidence tax at larger scale may be unstable, needs more seeds.\"}\n  action_items:\n    - {round: 3, action: \"Extract precision/recall from 14B test-set predictions\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Provide precision/recall decomposition OR acknowledge single-SFT-seed limitation\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3-RSFT-TRADEOFF\"\n  summary: \"RSFT 'cannot exploit trade-off' claim purely structural, lacks empirical test\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Need single-objective RSFT or downgrade to hypothesis.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Still no experiment. R1 adds: RSFT k>1 ablation also needed to understand discrete selection mechanism.\"}\n  action_items:\n    - {round: 3, action: \"Run single-objective RSFT\", assigned_to: \"Agent\", status: \"in_progress\"}\n    - {round: 4, action: \"Complete single-objective RSFT OR downgrade 'cannot exploit' to hypothesis\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-FMT-PAGELIMIT\"\n  summary: \"Main text exceeds 8-page limit (desk reject risk)\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. §4.7 + §5 overflow to p9.\"}\n    - {round: 4, note: \"RESOLVED. Conclusion compressed to 2 sentences. Main text fits 8 pages.\"}\n  action_items:\n    - {round: 3, action: \"Compress §4.7 + §5.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Main text now fits within 8 pages.\"\n  resolution_round: 4\n\n- id: \"R3-M1-SPECTRUM-SCALE\"\n  summary: \"Decoupling spectrum validated only at 4B scale\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Should appear in Limitations.\"}\n    - {round: 4, note: \"RESOLVED. Limitations now states spectrum is 4B only.\"}\n  action_items:\n    - {round: 3, action: \"Add to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Added to Limitations section.\"\n  resolution_round: 4\n\n- id: \"R3-M2-TAX-CONVENTION\"\n  summary: \"Evidence tax sign convention inconsistent across sections\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Inconsistent across tables/figures.\"}\n    - {round: 4, note: \"RESOLVED. Convention consistent throughout.\"}\n  action_items:\n    - {round: 3, action: \"Unify sign convention.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Sign convention unified throughout.\"\n  resolution_round: 4\n\n- id: \"R4-EDCR-CONSISTENCY\"\n  summary: \"EDCR ρ numerical inconsistency across sections (Round 3 W-SF5)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"§3.5 ρ=-0.89 vs §4.7 ρ=-0.96 vs Appendix ρ=-0.9643.\"}\n    - {round: 4, note: \"RESOLVED. All now consistently ρ=-0.96 / -0.9643.\"}\n  action_items:\n    - {round: 3, action: \"Unify EDCR ρ values\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All EDCR ρ values now consistent.\"\n  resolution_round: 4\n\n- id: \"R4-TAX-TRUNCATION\"\n  summary: \"Evidence tax at 1.7B is primarily truncation-mediated, not inherent evidence cost\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"R1 calls this 'the most incisive observation'. Appendix E matched@2048: 1.7B tax reverses to -5.63pp (beneficial). Appendix K: truncation FN is #1 RSFT improvement mechanism (-22% at 1.7B). Abstract/Contribution 1 'scale-dependent evidence tax' at 1.7B is truncation artifact, not inherent evidence cost. Paper buries this in appendix. R1 recommends distinguishing 'truncation-induced tax' from 'information-interference tax' and promoting matched@2048 findings to main text.\"}\n  action_items:\n    - {round: 4, action: \"Distinguish truncation-induced vs information-interference components of evidence tax in §4.4. Promote matched@2048 key finding to main text (currently Appendix E/F). Revise Contribution 1 framing.\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-MISSING-REFS\"\n  summary: \"Missing references: PCGrad, Rashkin et al. 2023 Attribution\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"PCGrad (Yu et al. 2020): gradient surgery for multi-task conflict, directly relevant to §4.3 gradient pressure discussion. Rashkin et al. 2023: Attribution in NLG, conceptual correspondence to evidence citation. R1 agrees on both. R1 rebuts Maynez et al. 2020 (too distant from DocRE).\"}\n  action_items:\n    - {round: 4, action: \"Add PCGrad (Yu et al. 2020) to §2.2 and Rashkin et al. 2023 to §2.3\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-SECTION44-DENSITY\"\n  summary: \"§4.4 information density too high — tax definition, CI, variance, cross-arch all in 1.5 pages\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"R1 agrees with R2: §4.4 packs too many layers (tax definition, scale-dependency, CI analysis, cross-seed variance, cross-architecture, inference-time tax). CI-crosses-zero caveat easily drowned. R1 suggests splitting into §4.4 Evidence Tax (with CI) and §4.5 Cross-Scale/Cross-Architecture.\"}\n  action_items:\n    - {round: 4, action: \"Split §4.4 into two subsections or compress variance portion to reduce density\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-25T23:01:21.879370+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml\", \"bytes\": 31112}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 155
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-25T23:04:05.174085+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 4 审稿报告（修订版——整合双向交叉回应）\n\n## Summary\n\n本文研究 evidence-grounded document-level relation extraction 中不同训练范式（SFT/RSFT/GRPO/DPO）对 RE-evidence coupling 的影响。在 Qwen3 (1.7B–14B) 和 LLaMA-3.1-8B 上进行系统比较。核心发现：(1) evidence tax 是 scale-dependent 的（1.7B 有益，≥4B 近中性）；(2) gradient-based 方法导致 evidence-extraction decoupling，而 RSFT 通过 output filtering 维持 coupling；(3) EDCR 作为 diagnostic metric 量化 decoupling 程度。论文定位为实证研究。\n\n## Round 3 → Round 4 改进确认\n\n以下 Must-Fix/Should-Fix 已确认修复：\n- ✅ **页数限制**（R3-FMT）：正文 8 页内，Conclusion 压缩至 2 句。PDF 已验证。\n- ✅ **EDCR ρ 一致性**（R3 W-SF5）：统一为 −0.96（cross-method, n=7）/ −0.79（per-relation, n=76）。\n- ✅ **RSFT seed protocol 透明化**：§3.3 明确声明 primary experiments 共享 SFT s42 checkpoint。\n- ✅ **Variance 降级为 observation**：Contribution 3 添加 shared SFT initialization 和 n=3 caveats。\n- ✅ **Evidence tax sign convention**：全文统一 Tax = no-evi − with-evi; positive = cost。\n- ✅ **Spectrum 限制**：Limitations 声明 spectrum 仅 4B 验证。\n- ✅ **CED 定位**：正确定位为 scoring variant，0.02pp 诚实报告，无 contribution language。\n- ✅ **DeepSeek-R1 + ReST 引用**：已添加。\n- ✅ **bf16 G=4 控制实验**：已新增（Rel-F1 28.73）。\n\n## Strengths\n\n1. **系统实验覆盖广泛**：5 model scales × 4 训练范式 + cross-architecture (LLaMA) + cross-dataset (Re-DocRED) 验证，evidence-grounded DocRE 领域最全面的实证比较。\n\n2. **Decoupling spectrum 有洞察力**：按 RE-evidence coupling 程度排列训练方法的 conceptual framework 为社区提供有用参考。\n\n3. **Evidence tax 量化有实用价值**：training-time 和 inference-time 双维度分离，matched@2048 fair evaluation 方法严谨。\n\n4. **实验设计周全**：random selection baseline、matched@2048 evaluation、no-evidence SFT、CED vs flat-NLI、DeBERTa base vs large ablation。\n\n5. **EDCR 验证扎实**：per-relation 分析 (n=76, ρ=−0.79)、partial correlation、permutation test、similar-TP pairs——R1 确认 EDCR 是纯 annotation-based 指标（不使用 NLI），验证链完整且独立。\n\n6. **可复现性强**：代码+数据开源承诺，hyperparameters 详尽，seed protocol 透明。\n\n## Weaknesses\n\n### Must-Fix（两位 Reviewer 共识）\n\n**[W-MF1] DPO β=0.1 单点实验——连续 4 轮未解决**\n- DPO β=0.1 导致 Rel-F1 从 44.39 暴跌至 33.37（−11pp），高度可能是超参选择导致\n- DPO 文献中 β=0.01-0.05 常用，避免过度偏离 reference policy\n- 整个 decoupling spectrum 的 DPO 段（\"gradual decay\"）建立在单一 β 值上\n- R1 补充：RSFT k=1 也是最激进的过滤策略——k=3/k=5 可能有不同 extraction-evidence balance。缺少这些消融，无法区分\"方法固有属性\"和\"特定超参下的行为\"\n- **要求**：β∈{0.01, 0.05} sweep 或将所有 DPO 结论限定为 \"under β=0.1\"\n- *[R1, R2 强烈共识 — 4 轮 recurring, 升级为 Must-Fix]*\n\n### Should-Fix（两位 Reviewer 共识）\n\n**[W-SF1] Evidence tax 1.7B 核心效应是 truncation artifact，framing 过度简化 ⚠️ NEW**\n- **R1 称此为\"本轮最有力的批评\"**，R2 首提，R1 cross-response 强烈同意\n- 论文自己的 Appendix E：matched@2048 fair evaluation 控制 truncation 后，1.7B tax **反转为 −5.63pp（beneficial）**；≥4B 近中性 (+0.25±0.47pp)\n- Appendix K：truncation FN 是 RSFT 改进的首要机制（1.7B: −22% truncation FN reduction）\n- 这意味着 Abstract/Contribution 1 宣称的 \"scale-dependent evidence tax\" 在 1.7B（效应最显著的规模）**实质是 truncation/format compliance artifact，非 evidence 固有代价**\n- 论文将此关键 nuance 埋在 Appendix E，正文 §4.4 仅一笔带过\n- **要求**：(1) 在正文 §4.4 区分 \"truncation-induced tax\" 和 \"information-interference tax\"；(2) 将 matched@2048 的关键发现从附录提升到正文显著位置；(3) 修订 Contribution 1 framing，承认 1.7B benefit 主要来自格式约束效应\n- *[R1 强烈同意 R2 — 双向交叉确认]*\n\n**[W-SF2] GRPO bf16 G=4 暴露 group size + lr confound**\n- bf16 G=4（Rel-F1 28.73）vs bf16 G=8（45.49）= 16.76pp drop → group size 有显著影响\n- QLoRA G=8 (lr=5e-6) vs bf16 G=8 (lr=5e-5) 学习率差 10×，非 \"residual confound\"\n- §4.3 \"attributable to quantization precision\" 仍过强\n- **要求**：弱化归因语言；显式讨论 lr 10× 差异；承认 group size 非trivial 贡献\n- *[R1, R2 共识 — 从 Must-Fix 降级为 Should-Fix，因 bf16 G=4 部分回应]*\n\n**[W-SF3] Variance \"observation\" 在文中篇幅与其证据力度不匹配**\n- §4.4 仍用 ~250 words + 精确 ratio (32.6×, 7.5×, 6.5×) + \"36× more predictable\"\n- sign test p=0.0625 不显著；Cohen's d=0.46 at 4B = small effect\n- **要求**：压缩至 2-3 句，精确 ratio 移至 appendix，移除 \"predictable\" 措辞\n- *[R1, R2 共识]*\n\n**[W-SF4] \"Implicit regularization\" 仍未按 R3 共识重命名**\n- §4.4 和 Appendix E 仍使用 \"implicit regularization hypothesis\"\n- R1 cross-response进一步指出：结合 W-SF1 的 truncation-mediation 发现，所谓 \"regularization\" 实质是格式约束效应，非 learning effect\n- **要求**：替换为 \"structural output constraint\"；增加 matched@2048 counter-evidence 讨论\n- *[R1, R2 共识 — R3 carry-over, 被 W-SF1 进一步强化]*\n\n**[W-SF5] RSFT \"cannot exploit trade-off\" 缺实证**\n- §G 仍为纯 structural argument，无实验验证\n- R1 补充：RSFT k>1 ablation 也是理解 discrete selection 机制的必要实验\n- **要求**：完成 single-objective RSFT 或降级为 hypothesis\n- *[R1, R2 共识 — R3 carry-over]*\n\n**[W-SF6] Method-innovation 语言残留**\n- Contribution 2: \"introduce the EDCR as a diagnostic\"\n- §3.5: \"we define the EDCR\"\n- R1：应将 RSFT 的角色明确为 \"empirical finding: discrete selection avoids decoupling\" 而非暗示方法新颖性\n- **要求**：\"introduce\" → \"use\"/\"employ\"；\"define\" → \"compute\"/\"measure\"；Contribution 3 reframe 为 empirical finding\n- *[R1, R2 共识]*\n\n**[W-SF7] §4.4 信息密度过高**\n- R1 同意 R2：§4.4 在 ~1.5 页内叠加 tax 定义、scale-dependency、CI 分析、cross-seed variance、cross-architecture、inference-time tax\n- CI-crosses-zero 这个关键 caveat 容易被淹没\n- **要求**：拆分为 §4.4 Evidence Tax（含 CI）和 §4.5 Cross-Scale Patterns；或压缩 variance 部分\n- *[R1, R2 共识]*\n\n**[W-SF8] 14B test-set reversal 仍缺 precision/recall 分解**\n- 14B: SFT truncation 50.6% vs RSFT 13.4%；dev +2.78pp → test −0.37pp\n- R1 补充：14B 高 cross-seed variance + 仅 1 SFT seed，evidence tax 在更大规模可能不稳定\n- **要求**：precision/recall 分解或显式承认 single-SFT-seed 限制\n- *[R1, R2 共识 — R3 carry-over]*\n\n### Minor Issues\n\n| ID | 问题 | 共识 |\n|---|---|---|\n| M1 | SFT no-evidence 1.7B/8B 仅 s42；1.7B s42 是最强 seed | AGREE |\n| M2 | \"co-optimization\" 和 \"joint optimization\" 术语未统一 | AGREE |\n| M3 | matched@2048 定义在 Appendix E，§4.4 引用时读者需翻附录 | AGREE — 至少加一句定义 |\n| M4 | Figure 4 dual y-axis 视觉误导（Rel-F1 40-55 vs Evi-F1 0-90 range）| AGREE — 建议并排子图 |\n| M5 | CED template sensitivity / NLI model family 测试有限 | AGREE — 影响小 |\n| M6 | BM25 k=2 未 justify | AGREE |\n| M7 | Re-DocRED test 20pp drop 缺定量统计支撑（dev vs test annotation density）| AGREE |\n| M8 | Figure 10 (Appendix) 色盲不友好 | AGREE — minor |\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上达成完全共识 [AGREE]：\n\n1. **DPO β 单点**：4 轮 recurring，升级为 Must-Fix。无法区分 method property 和 hyperparameter artifact\n2. **Evidence tax truncation-mediation**（NEW）：1.7B 的 evidence tax 主要是 truncation artifact。R1 称为 \"本轮最有力的批评\"\n3. **n=3 seeds 统计效力**：variance evidence 不足，observation 定位正确但文本过冗长\n4. **GRPO attribution**：bf16 G=4 部分回应，但暴露 group size effect + lr confound\n5. **Implicit regularization**：R3 共识未执行，被 truncation-mediation 发现进一步削弱\n6. **Method-innovation 语言**：\"introduce\"/\"define\" 暗示 novel contribution\n7. **EDCR 验证扎实**：R1 确认 EDCR 是纯 annotation-based 指标，per-relation 验证链完整\n\n## Reviewer Divergence\n\n**[W-DIV1] RSFT variance 比较的方法论公平性**\n- **R2 部分反驳 R1**：end-to-end variance 比较有实践价值（practitioner 关心 pipeline 稳定性）\n- **R1 坚持**：方法论不对称（SFT = full pipeline, RSFT = fine-tuning stage only）\n- **Director 判定**：R2 practical argument 有道理，但精确 ratio 和 \"predictable\" 措辞削弱 caveat。**WARNING — 压缩 variance 讨论。**\n\n**[W-DIV2] Conclusion 长度**\n- **R2**：列为 critical（过短，无 broader implications）\n- **R1 反驳**：Conclusion 长度是写作偏好；broader implications 在 §4.7 Discussion 中讨论；ARR 评分标准不含 conclusion 长度\n- **Director 判定：Minor** — R1 论点更有说服力。简短 conclusion 不影响 soundness。可选扩充 2-3 句 future directions。\n\n**[W-DIV3] EDCR-CED circular dependency**\n- **R2 原始意见**：EDCR 和 CED 共享 NLI backbone，存在 circular dependency\n- **R1 反驳（factual correction）**：EDCR（Eq. 2）是纯 annotation-based 指标（gold vs predicted evidence 集合差运算），**完全不使用 NLI**。CED（§3.4）使用 DeBERTa-v3 NLI。两者无共享组件。R2 混淆了 EDCR 和 CED。\n- **Director 判定：R1 正确。** R2 此条为事实性错误，不纳入报告 weakness。EDCR 验证链完整且独立。\n\n**[W-DIV4] \"Evidence tax\" 术语**\n- **R2**：术语不直观，建议改为 \"evidence delta\"/\"evidence impact\"\n- **R1 反驳**：Tax 是标准隐喻（\"abstraction tax\"、\"safety tax\"），negative tax = benefit 符合直觉。\"Delta\" 方向中性，丢失核心叙事\n- **Director 判定：R1 正确。** 术语选择合理，不需更改。\n\n## Questions for Authors\n\n1. bf16 G=4 实验的学习率是多少？如与 bf16 G=8 相同 (5e-5)，则 16.76pp drop 纯粹由 G 导致。\n2. DPO β=0.01 或 β=0.05 实验是否在进行中？已持续 4 轮。\n3. Single-objective RSFT / RSFT k>1 ablation 结果？\n4. 14B precision/recall 分解数据？\n5. Appendix E matched@2048 结果何时提升到正文？这是 evidence tax framing 的关键 nuance。\n\n## Missing References\n\n| 引用 | 理由 | 共识 |\n|---|---|---|\n| Yu et al. 2020 (PCGrad) | 梯度手术解决 multi-task gradient conflict，直接关联 §4.3 gradient pressure 讨论 | R1 AGREE |\n| Rashkin et al. 2023 (Attribution) | NLG 中的 attribution 与 evidence citation 有概念对应 | R1 AGREE |\n| ~~Maynez et al. 2020~~ | R1 反驳：abstractive summarization faithfulness 与 DocRE evidence 关联较远 | R1 REBUT |\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未启用外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~3.5 分钟)\n\n| 严重性 | 位置 | 发现 |\n|---|---|---|\n| ℹ️ | p5 | Figure 3 (CED scoring) 内部文字偏小（正文 60-65%），建议 ≥70% |\n| ℹ️ | p7 | Figure 4 图例文字偏小，在绘图区域内部 |\n| ℹ️ | p12 | Appendix 单页含 4 张表，信息密度极高（格式正确） |\n| ℹ️ | p17 | Figure 7 三子图 y 轴标签偏小 |\n| ℹ️ | p18 | 末页约 25% 空白（Appendix 末页） |\n| ✅ | p2 | Figure 1 清晰专业 |\n| ✅ | p6 | Table 2 booktabs 规范 |\n| ✅ | p8 | Figure 5 红/蓝对比清晰 |\n\n**0 critical, 0 warning, 8 info** — 排版质量良好。Figure 1 在 p2，解决了 Round 2-3 的 \"文字墙\" 问题。\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | 评分 | 说明 |\n|---|---|---|\n| Soundness | 3 | DPO spectrum 建于单一 β（4 轮未解决）；evidence tax 1.7B 核心效应是 truncation artifact 而非 evidence cost（framing gap）；GRPO attribution 有 confound；variance 统计力度不足 |\n| Excitement | 3 | Decoupling spectrum 有启发性；evidence tax truncation-mediation 机制的发现有价值（若正确 frame 的话）；novelty 在 empirical coverage 而非 method |\n| Reproducibility | 4 | 代码+数据开源承诺，hyperparameters 详尽，seed protocol 完全透明 |\n| Clarity | 3.5 | 格式问题大部分已修复；但 §4.4 密度过高、variance 段过长、implicit regularization 未重命名、evidence tax 关键 nuance 埋在附录 |\n| Overall | 3.5 | Borderline Conference |\n\n**置信度：4/5** — 两位 Reviewer 双向交叉回应完成，核心问题高度一致。4 条分歧中 2 条为 R2 factual error（已纠正），1 条为 writing preference（不影响评分），1 条 Director 裁定 WARNING。\n\n**推荐决定**：\n- **当前状态 → Borderline Conference (3.5)**：格式显著改善，多个 R3 Must-Fix 已修复。但 DPO β 4 轮 recurring + evidence tax framing gap（truncation-mediation 发现未反映在正文）+ GRPO attribution confound + RSFT \"cannot exploit\" 缺实证——这些问题阻碍 Conference (4.0) 评分。\n- **修复后 → Conference (4.0)**：如果 (1) DPO β sweep 或 scope limitation、(2) evidence tax framing 整合 truncation-mediation、(3) implicit regularization 重命名、(4) variance 压缩 + method-innovation 语言清理、(5) §4.4 密度降低——论文可达 Conference。empirical coverage 和 EDCR 验证基础扎实。\n- **关键阻碍**：DPO β（4 轮未解决，需实验数据）和 evidence tax framing（需 writing 重组，将 Appendix E 关键发现提升到正文）。\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 1：\"scale-dependent evidence tax\" 在 1.7B 的核心效应是 truncation-mediated → 需修订 framing\n- Contribution 2：\"introduce EDCR\" → 改为 \"use\"/\"employ\"\n- Contribution 3：已降级为 observation ✓，但 \"RSFT improves extraction without decoupling\" 仍读如 method contribution → reframe 为 empirical finding\n\n### §3 Method\n- RSFT seed protocol 透明 ✓\n- §3.4 CED：effort-vs-payoff 最失衡部分（大量篇幅描述 contrastive design，0.02pp 差异）— R1+R2 均指出\n- §3.5 EDCR：R1 确认验证链完整，R2 的 circular dependency 担忧为事实性错误\n- EDCR = 纯 annotation-based 指标，不使用 NLI backbone\n\n### §4 Experiments\n- §4.2：\"different sources of variation\" caveat ✓，但精确 ratio 和 \"predictable\" 削弱\n- §4.3：bf16 G=4 新增 ✓；\"attributable to quantization precision\" 过强；lr 10× 非 \"residual\"\n- §4.4：信息密度过高（R1+R2 共识）；evidence tax matched@2048 关键 nuance 埋在附录；\"implicit regularization\" 被 truncation-mediation 发现进一步削弱\n- §4.5：BM25 k=2 缺 justification\n\n### §5 Conclusion\n- 2 句，符合 8 页 ✓\n- R2 认为过短 (critical)，R1 反驳（writing preference），Director 判定 Minor\n\n### Limitations\n- 覆盖 data/architecture scope、CED sensitivity、RSFT mechanistic ✓\n- Spectrum 仅 4B ✓\n- 未提及 DPO β single-point limitation（应补充）\n\n### Appendix\n- §E/F：matched@2048 和 truncation analysis 是论文最有价值的分析之一，但被埋在附录——需提升到正文\n- §G：\"cannot exploit\" 仍为 structural argument\n- Appendix K：evidence quality unchanged (Δ<0.4pp) 与 \"implicit regularization\" framing 矛盾\n\n---\n\n*本报告由 2 位 Reviewer 独立审稿 + 双向交叉回应后合成。R1 cross-response 纠正了 R2 的 1 条事实性错误（EDCR 不使用 NLI），并强化了 evidence tax truncation-mediation 为本轮核心新发现。4 条分歧已裁定。Overall 评分一致：3.5 Borderline Conference。*",
  "project": "faith-evidence-ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 4 审稿报告（修订版——整合双向交叉回应）\n\n## Summary\n\n本文研究 evidence-grounded document-level relation extraction 中不同训练范式（SFT/RSFT/GRPO/DPO）对 RE-evidence coupling 的影响。在 Qwen3 (1.7B–14B) 和 LLaMA-3.1-8B 上进行系统比较。核心发现：(1) evidence tax 是 scale-dependent 的（1.7B 有益，≥4B 近中性）；(2) gradient-based 方法导致 evidence-extraction decoupling，而 RSFT 通过 output filtering 维持 coupling；(3) EDCR 作为 diagnostic metric 量化 decoupling 程度。论文定位为实证研究。\n\n## Round 3 → Round 4 改进确认\n\n以下 Must-Fix/Should-Fix 已确认修复：\n- ✅ **页数限制**（R3-FMT）：正文 8 页内，Conclusion 压缩至 2 句。PDF 已验证。\n- ✅ **EDCR ρ 一致性**（R3 W-SF5）：统一为 −0.96（cross-method, n=7）/ −0.79（per-relation, n=76）。\n- ✅ **RSFT seed protocol 透明化**：§3.3 明确声明 primary experiments 共享 SFT s42 checkpoint。\n- ✅ **Variance 降级为 observation**：Contribution 3 添加 shared SFT initialization 和 n=3 caveats。\n- ✅ **Evidence tax sign convention**：全文统一 Tax = no-evi − with-evi; positive = cost。\n- ✅ **Spectrum 限制**：Limitations 声明 spectrum 仅 4B 验证。\n- ✅ **CED 定位**：正确定位为 scoring variant，0.02pp 诚实报告，无 contribution language。\n- ✅ **DeepSeek-R1 + ReST 引用**：已添加。\n- ✅ **bf16 G=4 控制实验**：已新增（Rel-F1 28.73）。\n\n## Strengths\n\n1. **系统实验覆盖广泛**：5 model scales × 4 训练范式 + cross-architecture (LLaMA) + cross-dataset (Re-DocRED) 验证，evidence-grounded DocRE 领域最全面的实证比较。\n\n2. **Decoupling spectrum 有洞察力**：按 RE-evidence coupling 程度排列训练方法的 conceptual framework 为社区提供有用参考。\n\n3. **Evidence tax 量化有实用价值**：training-time 和 inference-time 双维度分离，matched@2048 fair evaluation 方法严谨。\n\n4. **实验设计周全**：random selection baseline、matched@2048 evaluation、no-evidence SFT、CED vs flat-NLI、DeBERTa base vs large ablation。\n\n5. **EDCR 验证扎实**：per-relation 分析 (n=76, ρ=−0.79)、partial correlation、permutation test、similar-TP pairs——R1 确认 EDCR 是纯 annotation-based 指标（不使用 NLI），验证链完整且独立。\n\n6. **可复现性强**：代码+数据开源承诺，hyperparameters 详尽，seed protocol 透明。\n\n## Weaknesses\n\n### Must-Fix（两位 Reviewer 共识）\n\n**[W-MF1] DPO β=0.1 单点实验——连续 4 轮未解决**\n- DPO β=0.1 导致 Rel-F1 从 44.39 暴跌至 33.37（−11pp），高度可能是超参选择导致\n- DPO 文献中 β=0.01-0.05 常用，避免过度偏离 reference policy\n- 整个 decoupling spectrum 的 DPO 段（\"gradual decay\"）建立在单一 β 值上\n- R1 补充：RSFT k=1 也是最激进的过滤策略——k=3/k=5 可能有不同 extraction-evidence balance。缺少这些消融，无法区分\"方法固有属性\"和\"特定超参下的行为\"\n- **要求**：β∈{0.01, 0.05} sweep 或将所有 DPO 结论限定为 \"under β=0.1\"\n- *[R1, R2 强烈共识 — 4 轮 recurring, 升级为 Must-Fix]*\n\n### Should-Fix（两位 Reviewer 共识）\n\n**[W-SF1] Evidence tax 1.7B 核心效应是 truncation artifact，framing 过度简化 ⚠️ NEW**\n- **R1 称此为\"本轮最有力的批评\"**，R2 首提，R1 cross-response 强烈同意\n- 论文自己的 Appendix E：matched@2048 fair evaluation 控制 truncation 后，1.7B tax **反转为 −5.63pp（beneficial）**；≥4B 近中性 (+0.25±0.47pp)\n- Appendix K：truncation FN 是 RSFT 改进的首要机制（1.7B: −22% truncation FN reduction）\n- 这意味着 Abstract/Contribution 1 宣称的 \"scale-dependent evidence tax\" 在 1.7B（效应最显著的规模）**实质是 truncation/format compliance artifact，非 evidence 固有代价**\n- 论文将此关键 nuance 埋在 Appendix E，正文 §4.4 仅一笔带过\n- **要求**：(1) 在正文 §4.4 区分 \"truncation-induced tax\" 和 \"information-interference tax\"；(2) 将 matched@2048 的关键发现从附录提升到正文显著位置；(3) 修订 Contribution 1 framing，承认 1.7B benefit 主要来自格式约束效应\n- *[R1 强烈同意 R2 — 双向交叉确认]*\n\n**[W-SF2] GRPO bf16 G=4 暴露 group size + lr confound**\n- bf16 G=4（Rel-F1 28.73）vs bf16 G=8（45.49）= 16.76pp drop → group size 有显著影响\n- QLoRA G=8 (lr=5e-6) vs bf16 G=8 (lr=5e-5) 学习率差 10×，非 \"residual confound\"\n- §4.3 \"attributable to quantization precision\" 仍过强\n- **要求**：弱化归因语言；显式讨论 lr 10× 差异；承认 group size 非trivial 贡献\n- *[R1, R2 共识 — 从 Must-Fix 降级为 Should-Fix，因 bf16 G=4 部分回应]*\n\n**[W-SF3] Variance \"observation\" 在文中篇幅与其证据力度不匹配**\n- §4.4 仍用 ~250 words + 精确 ratio (32.6×, 7.5×, 6.5×) + \"36× more predictable\"\n- sign test p=0.0625 不显著；Cohen's d=0.46 at 4B = small effect\n- **要求**：压缩至 2-3 句，精确 ratio 移至 appendix，移除 \"predictable\" 措辞\n- *[R1, R2 共识]*\n\n**[W-SF4] \"Implicit regularization\" 仍未按 R3 共识重命名**\n- §4.4 和 Appendix E 仍使用 \"implicit regularization hypothesis\"\n- R1 cross-response进一步指出：结合 W-SF1 的 truncation-mediation 发现，所谓 \"regularization\" 实质是格式约束效应，非 learning effect\n- **要求**：替换为 \"structural output constraint\"；增加 matched@2048 counter-evidence 讨论\n- *[R1, R2 共识 — R3 carry-over, 被 W-SF1 进一步强化]*\n\n**[W-SF5] RSFT \"cannot exploit trade-off\" 缺实证**\n- §G 仍为纯 structural argument，无实验验证\n- R1 补充：RSFT k>1 ablation 也是理解 discrete selection 机制的必要实验\n- **要求**：完成 single-objective RSFT 或降级为 hypothesis\n- *[R1, R2 共识 — R3 carry-over]*\n\n**[W-SF6] Method-innovation 语言残留**\n- Contribution 2: \"introduce the EDCR as a diagnostic\"\n- §3.5: \"we define the EDCR\"\n- R1：应将 RSFT 的角色明确为 \"empirical finding: discrete selection avoids decoupling\" 而非暗示方法新颖性\n- **要求**：\"introduce\" → \"use\"/\"employ\"；\"define\" → \"compute\"/\"measure\"；Contribution 3 reframe 为 empirical finding\n- *[R1, R2 共识]*\n\n**[W-SF7] §4.4 信息密度过高**\n- R1 同意 R2：§4.4 在 ~1.5 页内叠加 tax 定义、scale-dependency、CI 分析、cross-seed variance、cross-architecture、inference-time tax\n- CI-crosses-zero 这个关键 caveat 容易被淹没\n- **要求**：拆分为 §4.4 Evidence Tax（含 CI）和 §4.5 Cross-Scale Patterns；或压缩 variance 部分\n- *[R1, R2 共识]*\n\n**[W-SF8] 14B test-set reversal 仍缺 precision/recall 分解**\n- 14B: SFT truncation 50.6% vs RSFT 13.4%；dev +2.78pp → test −0.37pp\n- R1 补充：14B 高 cross-seed variance + 仅 1 SFT seed，evidence tax 在更大规模可能不稳定\n- **要求**：precision/recall 分解或显式承认 single-SFT-seed 限制\n- *[R1, R2 共识 — R3 carry-over]*\n\n### Minor Issues\n\n| ID | 问题 | 共识 |\n|---|---|---|\n| M1 | SFT no-evidence 1.7B/8B 仅 s42；1.7B s42 是最强 seed | AGREE |\n| M2 | \"co-optimization\" 和 \"joint optimization\" 术语未统一 | AGREE |\n| M3 | matched@2048 定义在 Appendix E，§4.4 引用时读者需翻附录 | AGREE — 至少加一句定义 |\n| M4 | Figure 4 dual y-axis 视觉误导（Rel-F1 40-55 vs Evi-F1 0-90 range）| AGREE — 建议并排子图 |\n| M5 | CED template sensitivity / NLI model family 测试有限 | AGREE — 影响小 |\n| M6 | BM25 k=2 未 justify | AGREE |\n| M7 | Re-DocRED test 20pp drop 缺定量统计支撑（dev vs test annotation density）| AGREE |\n| M8 | Figure 10 (Appendix) 色盲不友好 | AGREE — minor |\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上达成完全共识 [AGREE]：\n\n1. **DPO β 单点**：4 轮 recurring，升级为 Must-Fix。无法区分 method property 和 hyperparameter artifact\n2. **Evidence tax truncation-mediation**（NEW）：1.7B 的 evidence tax 主要是 truncation artifact。R1 称为 \"本轮最有力的批评\"\n3. **n=3 seeds 统计效力**：variance evidence 不足，observation 定位正确但文本过冗长\n4. **GRPO attribution**：bf16 G=4 部分回应，但暴露 group size effect + lr confound\n5. **Implicit regularization**：R3 共识未执行，被 truncation-mediation 发现进一步削弱\n6. **Method-innovation 语言**：\"introduce\"/\"define\" 暗示 novel contribution\n7. **EDCR 验证扎实**：R1 确认 EDCR 是纯 annotation-based 指标，per-relation 验证链完整\n\n## Reviewer Divergence\n\n**[W-DIV1] RSFT variance 比较的方法论公平性**\n- **R2 部分反驳 R1**：end-to-end variance 比较有实践价值（practitioner 关心 pipeline 稳定性）\n- **R1 坚持**：方法论不对称（SFT = full pipeline, RSFT = fine-tuning stage only）\n- **Director 判定**：R2 practical argument 有道理，但精确 ratio 和 \"predictable\" 措辞削弱 caveat。**WARNING — 压缩 variance 讨论。**\n\n**[W-DIV2] Conclusion 长度**\n- **R2**：列为 critical（过短，无 broader implications）\n- **R1 反驳**：Conclusion 长度是写作偏好；broader implications 在 §4.7 Discussion 中讨论；ARR 评分标准不含 conclusion 长度\n- **Director 判定：Minor** — R1 论点更有说服力。简短 conclusion 不影响 soundness。可选扩充 2-3 句 future directions。\n\n**[W-DIV3] EDCR-CED circular dependency**\n- **R2 原始意见**：EDCR 和 CED 共享 NLI backbone，存在 circular dependency\n- **R1 反驳（factual correction）**：EDCR（Eq. 2）是纯 annotation-based 指标（gold vs predicted evidence 集合差运算），**完全不使用 NLI**。CED（§3.4）使用 DeBERTa-v3 NLI。两者无共享组件。R2 混淆了 EDCR 和 CED。\n- **Director 判定：R1 正确。** R2 此条为事实性错误，不纳入报告 weakness。EDCR 验证链完整且独立。\n\n**[W-DIV4] \"Evidence tax\" 术语**\n- **R2**：术语不直观，建议改为 \"evidence delta\"/\"evidence impact\"\n- **R1 反驳**：Tax 是标准隐喻（\"abstraction tax\"、\"safety tax\"），negative tax = benefit 符合直觉。\"Delta\" 方向中性，丢失核心叙事\n- **Director 判定：R1 正确。** 术语选择合理，不需更改。\n\n## Questions for Authors\n\n1. bf16 G=4 实验的学习率是多少？如与 bf16 G=8 相同 (5e-5)，则 16.76pp drop 纯粹由 G 导致。\n2. DPO β=0.01 或 β=0.05 实验是否在进行中？已持续 4 轮。\n3. Single-objective RSFT / RSFT k>1 ablation 结果？\n4. 14B precision/recall 分解数据？\n5. Appendix E matched@2048 结果何时提升到正文？这是 evidence tax framing 的关键 nuance。\n\n## Missing References\n\n| 引用 | 理由 | 共识 |\n|---|---|---|\n| Yu et al. 2020 (PCGrad) | 梯度手术解决 multi-task gradient conflict，直接关联 §4.3 gradient pressure 讨论 | R1 AGREE |\n| Rashkin et al. 2023 (Attribution) | NLG 中的 attribution 与 evidence citation 有概念对应 | R1 AGREE |\n| ~~Maynez et al. 2020~~ | R1 反驳：abstractive summarization faithfulness 与 DocRE evidence 关联较远 | R1 REBUT |\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未启用外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~3.5 分钟)\n\n| 严重性 | 位置 | 发现 |\n|---|---|---|\n| ℹ️ | p5 | Figure 3 (CED scoring) 内部文字偏小（正文 60-65%），建议 ≥70% |\n| ℹ️ | p7 | Figure 4 图例文字偏小，在绘图区域内部 |\n| ℹ️ | p12 | Appendix 单页含 4 张表，信息密度极高（格式正确） |\n| ℹ️ | p17 | Figure 7 三子图 y 轴标签偏小 |\n| ℹ️ | p18 | 末页约 25% 空白（Appendix 末页） |\n| ✅ | p2 | Figure 1 清晰专业 |\n| ✅ | p6 | Table 2 booktabs 规范 |\n| ✅ | p8 | Figure 5 红/蓝对比清晰 |\n\n**0 critical, 0 warning, 8 info** — 排版质量良好。Figure 1 在 p2，解决了 Round 2-3 的 \"文字墙\" 问题。\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | 评分 | 说明 |\n|---|---|---|\n| Soundness | 3 | DPO spectrum 建于单一 β（4 轮未解决）；evidence tax 1.7B 核心效应是 truncation artifact 而非 evidence cost（framing gap）；GRPO attribution 有 confound；variance 统计力度不足 |\n| Excitement | 3 | Decoupling spectrum 有启发性；evidence tax truncation-mediation 机制的发现有价值（若正确 frame 的话）；novelty 在 empirical coverage 而非 method |\n| Reproducibility | 4 | 代码+数据开源承诺，hyperparameters 详尽，seed protocol 完全透明 |\n| Clarity | 3.5 | 格式问题大部分已修复；但 §4.4 密度过高、variance 段过长、implicit regularization 未重命名、evidence tax 关键 nuance 埋在附录 |\n| Overall | 3.5 | Borderline Conference |\n\n**置信度：4/5** — 两位 Reviewer 双向交叉回应完成，核心问题高度一致。4 条分歧中 2 条为 R2 factual error（已纠正），1 条为 writing preference（不影响评分），1 条 Director 裁定 WARNING。\n\n**推荐决定**：\n- **当前状态 → Borderline Conference (3.5)**：格式显著改善，多个 R3 Must-Fix 已修复。但 DPO β 4 轮 recurring + evidence tax framing gap（truncation-mediation 发现未反映在正文）+ GRPO attribution confound + RSFT \"cannot exploit\" 缺实证——这些问题阻碍 Conference (4.0) 评分。\n- **修复后 → Conference (4.0)**：如果 (1) DPO β sweep 或 scope limitation、(2) evidence tax framing 整合 truncation-mediation、(3) implicit regularization 重命名、(4) variance 压缩 + method-innovation 语言清理、(5) §4.4 密度降低——论文可达 Conference。empirical coverage 和 EDCR 验证基础扎实。\n- **关键阻碍**：DPO β（4 轮未解决，需实验数据）和 evidence tax framing（需 writing 重组，将 Appendix E 关键发现提升到正文）。\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 1：\"scale-dependent evidence tax\" 在 1.7B 的核心效应是 truncation-mediated → 需修订 framing\n- Contribution 2：\"introduce EDCR\" → 改为 \"use\"/\"employ\"\n- Contribution 3：已降级为 observation ✓，但 \"RSFT improves extraction without decoupling\" 仍读如 method contribution → reframe 为 empirical finding\n\n### §3 Method\n- RSFT seed protocol 透明 ✓\n- §3.4 CED：effort-vs-payoff 最失衡部分（大量篇幅描述 contrastive design，0.02pp 差异）— R1+R2 均指出\n- §3.5 EDCR：R1 确认验证链完整，R2 的 circular dependency 担忧为事实性错误\n- EDCR = 纯 annotation-based 指标，不使用 NLI backbone\n\n### §4 Experiments\n- §4.2：\"different sources of variation\" caveat ✓，但精确 ratio 和 \"predictable\" 削弱\n- §4.3：bf16 G=4 新增 ✓；\"attributable to quantization precision\" 过强；lr 10× 非 \"residual\"\n- §4.4：信息密度过高（R1+R2 共识）；evidence tax matched@2048 关键 nuance 埋在附录；\"implicit regularization\" 被 truncation-mediation 发现进一步削弱\n- §4.5：BM25 k=2 缺 justification\n\n### §5 Conclusion\n- 2 句，符合 8 页 ✓\n- R2 认为过短 (critical)，R1 反驳（writing preference），Director 判定 Minor\n\n### Limitations\n- 覆盖 data/architecture scope、CED sensitivity、RSFT mechanistic ✓\n- Spectrum 仅 4B ✓\n- 未提及 DPO β single-point limitation（应补充）\n\n### Appendix\n- §E/F：matched@2048 和 truncation analysis 是论文最有价值的分析之一，但被埋在附录——需提升到正文\n- §G：\"cannot exploit\" 仍为 structural argument\n- Appendix K：evidence quality unchanged (Δ<0.4pp) 与 \"implicit regularization\" framing 矛盾\n\n---\n\n*本报告由 2 位 Reviewer 独立审稿 + 双向交叉回应后合成。R1 cross-response 纠正了 R2 的 1 条事实性错误（EDCR 不使用 NLI），并强化了 evidence tax truncation-mediation 为本轮核心新发现。4 条分歧已裁定。Overall 评分一致：3.5 Borderline Conference。*",
    "project": "faith-evidence-ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-25T23:04:10.789382+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_84537e1e2f9ef71a90742c2db859c6f2:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5615
}
```

</details>

---


### Assistant

_source line 428 · 2026-05-25T23:04:20.758456+00:00_

Round 4 审稿报告（修订版）已投递至 Research Director。

**本轮审稿总结**：

- **评分**：3.5 Borderline Conference（R1、R2 一致）
- **Must-Fix**：DPO β=0.1 单点（4 轮 recurring，升级为 Must-Fix）
- **核心新发现**：R1 强烈认同 R2 提出的 evidence tax truncation-mediation 机制——1.7B 的 evidence tax 实质是 truncation artifact，论文将此关键 nuance 埋在附录
- **已修复**：页数限制✓、EDCR ρ 一致性✓、seed protocol✓、variance 降级✓、sign convention✓
- **R1 纠正 R2 事实性错误**：EDCR 不使用 NLI backbone（纯 annotation-based），不存在 circular dependency
- **4 条分歧已裁定**：Conclusion 长度→Minor、EDCR-CED circular→R2 factual error、evidence tax 术语→保留、variance 公平性→WARNING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---
