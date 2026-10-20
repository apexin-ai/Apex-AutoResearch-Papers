# Director coordination — Part 3 of 3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination.md) · [Structured JSON](../../../sessions/77/770846f5df99c753aaca.json)

## Round 52

### Tool call

_source line 624 · 2026-05-24T18:25:54.293820+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "\n# Round 8 审稿报告：How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs\n\n**Venue**: EMNLP 2026 (via ARR)  \n**Reviewers**: R1（方法严谨性）, R2（新颖性/完整性）  \n**审稿模式**: Fresh（重新审稿）  \n**交叉回应**: 完成，1 轮即收敛（分歧明确且不可调和，不启动额外轮次）\n\n---\n\n## Summary\n\n本文研究结构化 MLP 剪枝准则对推理型 LLM 后续恢复训练（SFT + GRPO）的影响。核心发现：(1) CKA-based diversity-preserving pruning 在 GRPO reward recovery 上显著优于 importance-based pruning（3-seed, p=0.0009, Cohen's d=11.1）；(2) 所有方法 GRPO 后精度增量 <1pp（\"reward-accuracy decoupling\"）；(3) 提出 RASP scoring 结合 importance 与 diversity。实验基于 DeepSeek-R1-Distill-Qwen-7B，在 GSM8K/MATH-500/MBPP 上评估，20% sparsity 为主设定。\n\n---\n\n## Strengths\n\n**S1. 研究问题有真实价值。** 剪枝准则如何影响 RLVR 恢复是一个未被充分研究的问题，对部署优化有直接意义。\n\n**S2. 核心统计设计严谨。** CKA-only vs Standard 的 3-seed 比较 + Welch's t-test (p=0.0009) + Cohen's d=11.1 + 95% CI [3.62, 5.47]pp，在同类实验论文中属上乘。\n\n**S3. Dose-response 方法论引入。** 将药理学 dose-response 框架应用于剪枝超参分析（α-sweep），方法论思路新颖。\n\n**S4. TOST 等价性检验。** 使用 TOST 形式化 \"decoupling\"（ε=2pp, 7/8 通过），方法论意识优于多数同类工作。\n\n**S5. 透明度高。** 诚实报告 RASP 单 seed、TOST 不同 ε 值结果、MBPP 不显著等不利信息。\n\n**S6. 多维评估。** GSM8K + MATH-500 (OOD) + MBPP (跨域)，加 throughput/memory 效率指标。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**C1. RASP 方法贡献 validity 存疑——单 seed + 叙事自相矛盾 [共识]**\n\nRASP（论文的核心方法贡献）存在双重问题：\n- **统计**：RASP α=2.0 优于 CKA-only 仅 +1.72pp (66.11% vs 64.39%)，基于单 seed。CKA-only 的 3-seed σ=0.18pp 暗示此差距可能显著，但 RASP 自身方差未知。Dose-response 非单调性（α=2.0→3.0 降 4.65pp，α=3.0→4.0 升 1.31pp）在 N=1 下极可能为噪声。\n- **叙事**：论文声称 RASP \"平衡 importance 与 diversity\"，但 α=1.0（名义平衡点）collapse（52.83%），最优 α=2.0 中 diversity 权重为 importance 的 (1-F)^2 ≈ 4×，本质是 CKA-dominant。\"平衡\"叙事不准确。\n- **函数形式**：乘法形式 I(h)×(1-F(h))^α 使 importance=0 时 score=0，可能人为导致 α=1.0 collapse。加法形式下此问题可能不存在，但论文未讨论选择理由。\n\n**R1 Critical / R2 Critical（叙事）+ Minor（统计）。Director 综合判定 Critical**——R1 正确指出 R2 自身的叙事矛盾论证逻辑上依赖 RASP 统计可靠性，二者不可分。如多 seed 验证失败，论文方法贡献归零。\n\n**C2. Cross-architecture 泛化严重不足，Title overclaim [共识 Critical]**\n\nTitle \"Reasoning LLMs\"（复数）但所有完整 SFT+GRPO 验证仅在 Qwen2.5 架构族内：DeepSeek-R1-Distill-Qwen-7B（主实验）+ DeepSeek-R1-Distill-Qwen-1.5B（cross-scale）。Qwen2.5-Math-7B 仅有 SFT 验证，GRPO 被推迟到 future work。两个共享 Qwen2.5 底层的模型不构成 cross-architecture 验证。Appendix O \"Cross-Architecture Validation\" 标题具有误导性。\n\n**C3. Reward-accuracy decoupling 可能是训练不足的 artifact [分歧：R2 Critical / R1 Warning]**\n\n100 步 GRPO（扩展 300 步）远少于典型 RLVR 训练（1000+ 步）。<1pp 精度增量可能仅反映训练不充分：\n- SFT 贡献 ~60pp 恢复（post-prune ~1% → 59-64%），GRPO <1pp。GRPO 有 ~27pp 理论 headroom 但仅利用 <4%。\n- **论文自身 15% sparsity 数据反证**：Section 4.3 报告 15% 下 GRPO 放大了 CKA-only 优势（SFT gap 5.69pp → GRPO gap 7.20pp），说明当 headroom 更大时 GRPO 有增量贡献——undermines decoupling 的普遍性。\n- **300 步扩展选择性省略 accuracy**：Appendix E 仅报告 reward gap 维持（5.5×），关键性地缺失 accuracy 数据。\n- **R1 反论**：Standard 的 reward 在 100 步已 collapse 到 0.054（peak 0.081），300 步仍未恢复。这是结构性崩溃而非简单欠拟合——\"训练更久就能恢复\"需要更强证据。\n\n**Director 判定**：核心 decoupling claim 的 robustness 存在合理质疑，但 reward collapse 的结构性证据也不能忽视。保留为 Critical 级讨论点，建议作者提供至少 1000 步 accuracy 数据或限定 claim scope。\n\n### Warning\n\n**W1. Dose-response max_completion_length 混杂 [共识]**\n\n主实验中 Random 用 512 tokens（其他方法 1024）。此不对称恰好压低 Random 的 reward，强化了论文 spectrum 叙事。核心 CKA-only vs Standard 比较（均 1024）未受影响，但 Random 在 spectrum 中的排序不可靠。\n\n**W2. Discussion/Conclusion 过于单薄 [共识]**\n\nSection 5 仅约 7-8 行。对于有如此丰富发现的论文，Discussion 应至少讨论：spectrum 部署指导意义、SFT vs GRPO 角色分离、与 Ji et al. (2026) self-healing 结论的对话、CKA-only 机制解释。\n\n**W3. Calibration 数据量 M=512 未在正文说明理由 [共识]**\n\nSection 3.2 定义 D_cal 但未给出 M 值或选择依据。\n\n**W4. Title/叙事焦点与实际恢复来源错位 [共识]**\n\nTitle 聚焦 \"Post-RLVR Recovery\" 但 SFT 完成 95%+ 的恢复。GRPO 独特贡献在 reward trajectory 差异化但不转化为 accuracy。Discussion 应显式分离两者角色。\n\n**W5. 缺失 3 篇高度相关文献 [R2 提出，R1 部分同意]**\n\n1. \"When Reasoning Meets Compression\" (Li et al., 2025, arXiv:2504.02010) — 直接 benchmark 剪枝对 DeepSeek-R1 推理影响\n2. \"Can Pruning Improve Reasoning?\" (2025, arXiv:2505.14582) — 标题直接相关\n3. \"GPrune-LLM\" (2026, arXiv:2603.13418) — generalization-aware pruning（可能时间上来不及）\n\n**W6. TOST ε=2pp 未 justify [共识 Minor-Warning]**\n\nε=2pp 未预注册。ε=1pp 功效不足（Appendix T），ε=3pp 全通过。论文透明度是加分项，但应在正文 justify 2pp 选择的合理性。\n\n**W7. MBPP 不显著结果被引用为支持证据 [共识]**\n\nAppendix G 承认 MBPP 不显著，但 Section 4.3 仍引用其支持 decoupling。需加注或降低引用强度。\n\n### Minor\n\n- **M1**: Recovery capacity 概念先用后定义（abstract/intro 中使用但 Section 3 才定义）\n- **M2**: Figure 2 信息密度过高（structural analysis + scoring + pipeline + spectrum 合一图）\n- **M3**: \"Reward-accuracy decoupling\" 术语引入时未充分建立先验预期（为何二者应耦合）\n- **M4**: 无代码/checkpoint 发布承诺（对 controlled experiment 论文尤为重要）\n- **M5**: Lottery Ticket Hypothesis 类比过于表面（LTH: pruning at initialization vs 本文: post-training structured pruning）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Cross-architecture overclaiming**: Title \"Reasoning LLMs\" 远超证据支撑范围（仅 Qwen2.5 家族）→ 需限定或补实验\n2. **RASP 叙事不准确**: \"平衡 importance 与 diversity\" 与 α=2.0 CKA-dominant 现实不符 → 需修改叙事\n3. **Discussion 单薄**: 发现丰富但讨论不足\n4. **Calibration M 未说明**: 正文遗漏\n5. **SFT 主导恢复但叙事聚焦 GRPO**: 比例失衡应讨论\n6. **30% sparsity 全 collapse**: 有效窗口窄（20-25%），应讨论突破方向\n7. **缺失引用**: 至少 2 篇高度相关工作未引用\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 议题 | R1 | R2 | Director 裁定 |\n|------|-----|-----|--------------|\n| GRPO 训练步数 / SFT ceiling | Warning（reward collapse 证据使 \"训练更久\" 不 plausible） | **Critical**（15% 数据自相矛盾 + 300 步省略 accuracy） | Critical-leaning（数据 gap 真实存在） |\n| RASP 单 seed 统计 | **Critical**（方法贡献 validity 核心） | Minor（RASP 非核心 claim 支撑） | Critical（R1 论证 R2 W3 逻辑上依赖此点） |\n| Random baseline 不公平 | Critical（影响 spectrum 排序） | Warning（Random 非核心对比对象） | Warning（核心比较 CKA vs Standard 未受影响） |\n| CKA 双重角色 / 循环论证 | Warning | **Minor**（两种 CKA 计算技术上不同） | Minor（R2 技术论证成立，但建议加说明） |\n\n---\n\n## Questions for Authors\n\n1. **300 步 GRPO 的 accuracy 数据是什么？** Appendix E 仅报告 reward。如果 Standard 的 accuracy 在 300 步仍无改善而 CKA-only 有提升，这会大幅强化 decoupling；反之则 weaken。\n2. **RASP α=2.0 的多 seed 结果？** 哪怕 2 seeds 也能大幅减少不确定性。如 +1.72pp 优势不可复现，RASP 作为方法贡献是否应降级？\n3. **为何选择乘法形式而非加法？** 是否尝试过 βI(h) + (1-β)(1-F(h))？\n4. **15% sparsity 下 GRPO amplifies gap 与 20% decoupling 的张力如何解释？** 这是 sparsity-dependent 现象吗？\n5. **Appendix O \"Cross-Architecture\" 标题的修改计划？** Qwen2.5-Math-7B 共享底层架构。\n\n---\n\n## Missing References\n\n1. **Li et al. (2025). \"When Reasoning Meets Compression.\"** arXiv:2504.02010. 直接在 DeepSeek-R1 上 benchmark 剪枝对推理的影响——与本文有直接可比性。\n2. **\"Can Pruning Improve Reasoning?\" (2025).** arXiv:2505.14582. 研究剪枝是否能改善推理能力，与 recovery capacity spectrum 有对话空间。\n3. **\"GPrune-LLM: Generalization-Aware Structured Pruning\" (2026).** arXiv:2603.13418. \"Generalization-aware\" 与 \"recovery-aware\" 有概念亲缘性（可在 camera-ready 补充）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~3 分钟)\n\n**Findings (2 Warning, 9 Info):**\n\n- ⚠️ **Page 16**（Appendix 末页）：仅约 1/4 有内容（Table 16 + AI 声明），3/4 空白。视觉不专业。\n- ⚠️ **Page 7-8**：Figure 3/5/6 面板较小，axis labels/legend/tick labels 字号偏小（≤6pt），审稿人可能需放大。Page 8 尤其密集。\n- ℹ️ Page 1 无视觉锚点（首个 display item 在 page 2，可接受）\n- ℹ️ Page 3-4 连续密集文本（Method section，有公式节奏，合理）\n- ℹ️ Page 5 Figure 2 出现稍晚于理想位置但质量好\n- ℹ️ Figure 1 色盲友好，caption 自包含\n- ℹ️ Table 1/2 booktabs 规范\n- ℹ️ Figure 5 灰度打印下可能难以区分\n- ℹ️ Limitations 简短精炼（3 点），符合 EMNLP 2026\n- ℹ️ Appendix 表格格式统一\n- ℹ️ References 格式统一，无 [?] 未解析\n\n**总评**：排版整体合格，无 critical 排版问题。Page 7-8 图表密度和字号是唯一需关注的视觉问题。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n\n**置信度：4/5（High）**\n\n### 评分理由\n\n**核心贡献评估：**\n\n1. **Recovery capacity spectrum（CKA-only ≫ Standard）**：有 3-seed 统计支撑，核心发现 sound。但 scope 被严重 overclaim（仅 Qwen2.5 family, 20-25% sparsity window）。\n2. **Reward-accuracy decoupling**：新颖观察，但存在合理的训练充分性质疑，15% 数据自相矛盾，300 步 accuracy 缺失。\n3. **RASP method**：单 seed、叙事矛盾、函数形式未推导——方法贡献不可靠。\n\n**为何 3.0 而非 3.5：**\n- 如果 RASP 多 seed 不可复现（当前证据不足以判断），论文核心贡献变为纯 empirical finding——spectrum ordering 有价值但 novelty 有限（CKA/diversity-preserving pruning 优于 importance-based 不令人意外）。\n- Title/scope overclaiming 是系统性问题（已连续 4 轮提出），修复后论文叙事需大幅调整。\n- Decoupling 作为独立贡献在训练充分性未验证前难以成立。\n\n**升分条件（→ 3.5 Borderline Conference）：**\n- (a) RASP α=2.0 多 seed 验证确认 +1.72pp 优势显著\n- (b) 1000 步 GRPO accuracy 数据证实 decoupling 持续存在\n- (c) 至少一个非 Qwen2.5 架构的完整 SFT+GRPO 验证\n- 满足 (a)+(b) 或 (a)+(c) 即可升至 3.5\n\n**当前论文适合 Findings track**——empirical findings 有价值但方法贡献和 claim scope 问题阻碍 Main Conference 接收。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"holds across sparsity levels\" overclaims（仅 20-25% 成立，15% 下 GRPO amplifies，30% collapse）→ 改为 \"at moderate sparsity (20-25%)\"\n- \"Reasoning LLMs\" 复数 overclaim → 限定为 Qwen2.5 family 或加 \"A Case Study\"\n- 考虑加代码发布承诺\n\n### Section 1 (Introduction)\n- Recovery capacity 概念先用后定义——首次出现时加括号简述\n- \"Reward-accuracy decoupling\" 首次使用时应建立先验预期（为何二者通常耦合）\n\n### Section 2 (Related Work)\n- Lottery Ticket Hypothesis 类比表面——LTH 研究 pruning at initialization，与本文场景有本质区别。弱化类比或加说明\n- 缺失 Li et al. (2025) 和 \"Can Pruning Improve Reasoning?\" (2025)\n\n### Section 3 (Method)\n- **3.2**: D_cal 的 M=512 未在正文指定\n- **Eq. 3 (RASP)**: 乘法形式选择未讨论理由。应解释为何 I(h)×(1-F(h))^α 而非 βI(h)+(1-β)(1-F(h))\n- RASP \"平衡 importance 与 diversity\" 叙事需修改为 \"CKA-dominant with importance correction\"\n\n### Section 4 (Experiments)\n- **4.1**: Random baseline max_completion_length=512 应标注并讨论影响\n- **4.2 (Dose-response)**: α 值间 max_completion_length 不一致是关键混杂。Inverted-U 峰值不可靠直到统一条件后复现\n- **4.3**: 引用 MBPP 时需注明统计不显著\n- **4.3**: 15% vs 20% sparsity 对 GRPO 行为的差异应讨论——这是 decoupling 非普遍性的内部证据\n- **4.4 (TOST)**: ε=2pp 选择需 justify\n- **4.5 (Layer-wise CKA)**: 虽然 intra-layer CKA（剪枝）与 layer-wise CKA（分析）技术上不同，应加一句说明避免循环论证印象\n\n### Section 5 (Discussion/Conclusion)\n- 显著扩充 Discussion：加入 SFT vs GRPO 角色分离、spectrum 实用指导、与 self-healing 文献对话、30% ceiling 突破方向\n- Throughput regression (-19%) 应在 Limitations 讨论\n\n### Appendix\n- **Appendix E**: 补充 300 步 accuracy 数据（关键缺失）\n- **Appendix O**: \"Cross-Architecture Validation\" 标题误导——Qwen2.5-Math-7B 共享架构。建议改为 \"Cross-Model Validation within Qwen2.5 Family\"\n- RASP 所有 α 值和 Random 应标注 \"single seed\" 脚注\n\n---\n\n**R1 评分**: 3.5 (Borderline Conference)  \n**R2 评分**: 3.0 (Findings)  \n**Director 综合**: 3.0 (Findings)\n\n综合评分倾向 R2 的 3.0 而非 R1 的 3.5，原因：(1) RASP 方法贡献在多 seed 验证前不可靠——如果方法贡献归零，novelty 降为 empirical observation level；(2) scope overclaiming 是系统性问题；(3) decoupling 的训练充分性质疑虽非定论但合理。R1 的 3.5 基于 \"decoupling 发现本身有 novelty\"，这一立场成立但需要更强的 robustness 证据。\n",
  "project": "recovery_aware_struct_prune",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "\n# Round 8 审稿报告：How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs\n\n**Venue**: EMNLP 2026 (via ARR)  \n**Reviewers**: R1（方法严谨性）, R2（新颖性/完整性）  \n**审稿模式**: Fresh（重新审稿）  \n**交叉回应**: 完成，1 轮即收敛（分歧明确且不可调和，不启动额外轮次）\n\n---\n\n## Summary\n\n本文研究结构化 MLP 剪枝准则对推理型 LLM 后续恢复训练（SFT + GRPO）的影响。核心发现：(1) CKA-based diversity-preserving pruning 在 GRPO reward recovery 上显著优于 importance-based pruning（3-seed, p=0.0009, Cohen's d=11.1）；(2) 所有方法 GRPO 后精度增量 <1pp（\"reward-accuracy decoupling\"）；(3) 提出 RASP scoring 结合 importance 与 diversity。实验基于 DeepSeek-R1-Distill-Qwen-7B，在 GSM8K/MATH-500/MBPP 上评估，20% sparsity 为主设定。\n\n---\n\n## Strengths\n\n**S1. 研究问题有真实价值。** 剪枝准则如何影响 RLVR 恢复是一个未被充分研究的问题，对部署优化有直接意义。\n\n**S2. 核心统计设计严谨。** CKA-only vs Standard 的 3-seed 比较 + Welch's t-test (p=0.0009) + Cohen's d=11.1 + 95% CI [3.62, 5.47]pp，在同类实验论文中属上乘。\n\n**S3. Dose-response 方法论引入。** 将药理学 dose-response 框架应用于剪枝超参分析（α-sweep），方法论思路新颖。\n\n**S4. TOST 等价性检验。** 使用 TOST 形式化 \"decoupling\"（ε=2pp, 7/8 通过），方法论意识优于多数同类工作。\n\n**S5. 透明度高。** 诚实报告 RASP 单 seed、TOST 不同 ε 值结果、MBPP 不显著等不利信息。\n\n**S6. 多维评估。** GSM8K + MATH-500 (OOD) + MBPP (跨域)，加 throughput/memory 效率指标。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**C1. RASP 方法贡献 validity 存疑——单 seed + 叙事自相矛盾 [共识]**\n\nRASP（论文的核心方法贡献）存在双重问题：\n- **统计**：RASP α=2.0 优于 CKA-only 仅 +1.72pp (66.11% vs 64.39%)，基于单 seed。CKA-only 的 3-seed σ=0.18pp 暗示此差距可能显著，但 RASP 自身方差未知。Dose-response 非单调性（α=2.0→3.0 降 4.65pp，α=3.0→4.0 升 1.31pp）在 N=1 下极可能为噪声。\n- **叙事**：论文声称 RASP \"平衡 importance 与 diversity\"，但 α=1.0（名义平衡点）collapse（52.83%），最优 α=2.0 中 diversity 权重为 importance 的 (1-F)^2 ≈ 4×，本质是 CKA-dominant。\"平衡\"叙事不准确。\n- **函数形式**：乘法形式 I(h)×(1-F(h))^α 使 importance=0 时 score=0，可能人为导致 α=1.0 collapse。加法形式下此问题可能不存在，但论文未讨论选择理由。\n\n**R1 Critical / R2 Critical（叙事）+ Minor（统计）。Director 综合判定 Critical**——R1 正确指出 R2 自身的叙事矛盾论证逻辑上依赖 RASP 统计可靠性，二者不可分。如多 seed 验证失败，论文方法贡献归零。\n\n**C2. Cross-architecture 泛化严重不足，Title overclaim [共识 Critical]**\n\nTitle \"Reasoning LLMs\"（复数）但所有完整 SFT+GRPO 验证仅在 Qwen2.5 架构族内：DeepSeek-R1-Distill-Qwen-7B（主实验）+ DeepSeek-R1-Distill-Qwen-1.5B（cross-scale）。Qwen2.5-Math-7B 仅有 SFT 验证，GRPO 被推迟到 future work。两个共享 Qwen2.5 底层的模型不构成 cross-architecture 验证。Appendix O \"Cross-Architecture Validation\" 标题具有误导性。\n\n**C3. Reward-accuracy decoupling 可能是训练不足的 artifact [分歧：R2 Critical / R1 Warning]**\n\n100 步 GRPO（扩展 300 步）远少于典型 RLVR 训练（1000+ 步）。<1pp 精度增量可能仅反映训练不充分：\n- SFT 贡献 ~60pp 恢复（post-prune ~1% → 59-64%），GRPO <1pp。GRPO 有 ~27pp 理论 headroom 但仅利用 <4%。\n- **论文自身 15% sparsity 数据反证**：Section 4.3 报告 15% 下 GRPO 放大了 CKA-only 优势（SFT gap 5.69pp → GRPO gap 7.20pp），说明当 headroom 更大时 GRPO 有增量贡献——undermines decoupling 的普遍性。\n- **300 步扩展选择性省略 accuracy**：Appendix E 仅报告 reward gap 维持（5.5×），关键性地缺失 accuracy 数据。\n- **R1 反论**：Standard 的 reward 在 100 步已 collapse 到 0.054（peak 0.081），300 步仍未恢复。这是结构性崩溃而非简单欠拟合——\"训练更久就能恢复\"需要更强证据。\n\n**Director 判定**：核心 decoupling claim 的 robustness 存在合理质疑，但 reward collapse 的结构性证据也不能忽视。保留为 Critical 级讨论点，建议作者提供至少 1000 步 accuracy 数据或限定 claim scope。\n\n### Warning\n\n**W1. Dose-response max_completion_length 混杂 [共识]**\n\n主实验中 Random 用 512 tokens（其他方法 1024）。此不对称恰好压低 Random 的 reward，强化了论文 spectrum 叙事。核心 CKA-only vs Standard 比较（均 1024）未受影响，但 Random 在 spectrum 中的排序不可靠。\n\n**W2. Discussion/Conclusion 过于单薄 [共识]**\n\nSection 5 仅约 7-8 行。对于有如此丰富发现的论文，Discussion 应至少讨论：spectrum 部署指导意义、SFT vs GRPO 角色分离、与 Ji et al. (2026) self-healing 结论的对话、CKA-only 机制解释。\n\n**W3. Calibration 数据量 M=512 未在正文说明理由 [共识]**\n\nSection 3.2 定义 D_cal 但未给出 M 值或选择依据。\n\n**W4. Title/叙事焦点与实际恢复来源错位 [共识]**\n\nTitle 聚焦 \"Post-RLVR Recovery\" 但 SFT 完成 95%+ 的恢复。GRPO 独特贡献在 reward trajectory 差异化但不转化为 accuracy。Discussion 应显式分离两者角色。\n\n**W5. 缺失 3 篇高度相关文献 [R2 提出，R1 部分同意]**\n\n1. \"When Reasoning Meets Compression\" (Li et al., 2025, arXiv:2504.02010) — 直接 benchmark 剪枝对 DeepSeek-R1 推理影响\n2. \"Can Pruning Improve Reasoning?\" (2025, arXiv:2505.14582) — 标题直接相关\n3. \"GPrune-LLM\" (2026, arXiv:2603.13418) — generalization-aware pruning（可能时间上来不及）\n\n**W6. TOST ε=2pp 未 justify [共识 Minor-Warning]**\n\nε=2pp 未预注册。ε=1pp 功效不足（Appendix T），ε=3pp 全通过。论文透明度是加分项，但应在正文 justify 2pp 选择的合理性。\n\n**W7. MBPP 不显著结果被引用为支持证据 [共识]**\n\nAppendix G 承认 MBPP 不显著，但 Section 4.3 仍引用其支持 decoupling。需加注或降低引用强度。\n\n### Minor\n\n- **M1**: Recovery capacity 概念先用后定义（abstract/intro 中使用但 Section 3 才定义）\n- **M2**: Figure 2 信息密度过高（structural analysis + scoring + pipeline + spectrum 合一图）\n- **M3**: \"Reward-accuracy decoupling\" 术语引入时未充分建立先验预期（为何二者应耦合）\n- **M4**: 无代码/checkpoint 发布承诺（对 controlled experiment 论文尤为重要）\n- **M5**: Lottery Ticket Hypothesis 类比过于表面（LTH: pruning at initialization vs 本文: post-training structured pruning）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Cross-architecture overclaiming**: Title \"Reasoning LLMs\" 远超证据支撑范围（仅 Qwen2.5 家族）→ 需限定或补实验\n2. **RASP 叙事不准确**: \"平衡 importance 与 diversity\" 与 α=2.0 CKA-dominant 现实不符 → 需修改叙事\n3. **Discussion 单薄**: 发现丰富但讨论不足\n4. **Calibration M 未说明**: 正文遗漏\n5. **SFT 主导恢复但叙事聚焦 GRPO**: 比例失衡应讨论\n6. **30% sparsity 全 collapse**: 有效窗口窄（20-25%），应讨论突破方向\n7. **缺失引用**: 至少 2 篇高度相关工作未引用\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 议题 | R1 | R2 | Director 裁定 |\n|------|-----|-----|--------------|\n| GRPO 训练步数 / SFT ceiling | Warning（reward collapse 证据使 \"训练更久\" 不 plausible） | **Critical**（15% 数据自相矛盾 + 300 步省略 accuracy） | Critical-leaning（数据 gap 真实存在） |\n| RASP 单 seed 统计 | **Critical**（方法贡献 validity 核心） | Minor（RASP 非核心 claim 支撑） | Critical（R1 论证 R2 W3 逻辑上依赖此点） |\n| Random baseline 不公平 | Critical（影响 spectrum 排序） | Warning（Random 非核心对比对象） | Warning（核心比较 CKA vs Standard 未受影响） |\n| CKA 双重角色 / 循环论证 | Warning | **Minor**（两种 CKA 计算技术上不同） | Minor（R2 技术论证成立，但建议加说明） |\n\n---\n\n## Questions for Authors\n\n1. **300 步 GRPO 的 accuracy 数据是什么？** Appendix E 仅报告 reward。如果 Standard 的 accuracy 在 300 步仍无改善而 CKA-only 有提升，这会大幅强化 decoupling；反之则 weaken。\n2. **RASP α=2.0 的多 seed 结果？** 哪怕 2 seeds 也能大幅减少不确定性。如 +1.72pp 优势不可复现，RASP 作为方法贡献是否应降级？\n3. **为何选择乘法形式而非加法？** 是否尝试过 βI(h) + (1-β)(1-F(h))？\n4. **15% sparsity 下 GRPO amplifies gap 与 20% decoupling 的张力如何解释？** 这是 sparsity-dependent 现象吗？\n5. **Appendix O \"Cross-Architecture\" 标题的修改计划？** Qwen2.5-Math-7B 共享底层架构。\n\n---\n\n## Missing References\n\n1. **Li et al. (2025). \"When Reasoning Meets Compression.\"** arXiv:2504.02010. 直接在 DeepSeek-R1 上 benchmark 剪枝对推理的影响——与本文有直接可比性。\n2. **\"Can Pruning Improve Reasoning?\" (2025).** arXiv:2505.14582. 研究剪枝是否能改善推理能力，与 recovery capacity spectrum 有对话空间。\n3. **\"GPrune-LLM: Generalization-Aware Structured Pruning\" (2026).** arXiv:2603.13418. \"Generalization-aware\" 与 \"recovery-aware\" 有概念亲缘性（可在 camera-ready 补充）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~3 分钟)\n\n**Findings (2 Warning, 9 Info):**\n\n- ⚠️ **Page 16**（Appendix 末页）：仅约 1/4 有内容（Table 16 + AI 声明），3/4 空白。视觉不专业。\n- ⚠️ **Page 7-8**：Figure 3/5/6 面板较小，axis labels/legend/tick labels 字号偏小（≤6pt），审稿人可能需放大。Page 8 尤其密集。\n- ℹ️ Page 1 无视觉锚点（首个 display item 在 page 2，可接受）\n- ℹ️ Page 3-4 连续密集文本（Method section，有公式节奏，合理）\n- ℹ️ Page 5 Figure 2 出现稍晚于理想位置但质量好\n- ℹ️ Figure 1 色盲友好，caption 自包含\n- ℹ️ Table 1/2 booktabs 规范\n- ℹ️ Figure 5 灰度打印下可能难以区分\n- ℹ️ Limitations 简短精炼（3 点），符合 EMNLP 2026\n- ℹ️ Appendix 表格格式统一\n- ℹ️ References 格式统一，无 [?] 未解析\n\n**总评**：排版整体合格，无 critical 排版问题。Page 7-8 图表密度和字号是唯一需关注的视觉问题。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n\n**置信度：4/5（High）**\n\n### 评分理由\n\n**核心贡献评估：**\n\n1. **Recovery capacity spectrum（CKA-only ≫ Standard）**：有 3-seed 统计支撑，核心发现 sound。但 scope 被严重 overclaim（仅 Qwen2.5 family, 20-25% sparsity window）。\n2. **Reward-accuracy decoupling**：新颖观察，但存在合理的训练充分性质疑，15% 数据自相矛盾，300 步 accuracy 缺失。\n3. **RASP method**：单 seed、叙事矛盾、函数形式未推导——方法贡献不可靠。\n\n**为何 3.0 而非 3.5：**\n- 如果 RASP 多 seed 不可复现（当前证据不足以判断），论文核心贡献变为纯 empirical finding——spectrum ordering 有价值但 novelty 有限（CKA/diversity-preserving pruning 优于 importance-based 不令人意外）。\n- Title/scope overclaiming 是系统性问题（已连续 4 轮提出），修复后论文叙事需大幅调整。\n- Decoupling 作为独立贡献在训练充分性未验证前难以成立。\n\n**升分条件（→ 3.5 Borderline Conference）：**\n- (a) RASP α=2.0 多 seed 验证确认 +1.72pp 优势显著\n- (b) 1000 步 GRPO accuracy 数据证实 decoupling 持续存在\n- (c) 至少一个非 Qwen2.5 架构的完整 SFT+GRPO 验证\n- 满足 (a)+(b) 或 (a)+(c) 即可升至 3.5\n\n**当前论文适合 Findings track**——empirical findings 有价值但方法贡献和 claim scope 问题阻碍 Main Conference 接收。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"holds across sparsity levels\" overclaims（仅 20-25% 成立，15% 下 GRPO amplifies，30% collapse）→ 改为 \"at moderate sparsity (20-25%)\"\n- \"Reasoning LLMs\" 复数 overclaim → 限定为 Qwen2.5 family 或加 \"A Case Study\"\n- 考虑加代码发布承诺\n\n### Section 1 (Introduction)\n- Recovery capacity 概念先用后定义——首次出现时加括号简述\n- \"Reward-accuracy decoupling\" 首次使用时应建立先验预期（为何二者通常耦合）\n\n### Section 2 (Related Work)\n- Lottery Ticket Hypothesis 类比表面——LTH 研究 pruning at initialization，与本文场景有本质区别。弱化类比或加说明\n- 缺失 Li et al. (2025) 和 \"Can Pruning Improve Reasoning?\" (2025)\n\n### Section 3 (Method)\n- **3.2**: D_cal 的 M=512 未在正文指定\n- **Eq. 3 (RASP)**: 乘法形式选择未讨论理由。应解释为何 I(h)×(1-F(h))^α 而非 βI(h)+(1-β)(1-F(h))\n- RASP \"平衡 importance 与 diversity\" 叙事需修改为 \"CKA-dominant with importance correction\"\n\n### Section 4 (Experiments)\n- **4.1**: Random baseline max_completion_length=512 应标注并讨论影响\n- **4.2 (Dose-response)**: α 值间 max_completion_length 不一致是关键混杂。Inverted-U 峰值不可靠直到统一条件后复现\n- **4.3**: 引用 MBPP 时需注明统计不显著\n- **4.3**: 15% vs 20% sparsity 对 GRPO 行为的差异应讨论——这是 decoupling 非普遍性的内部证据\n- **4.4 (TOST)**: ε=2pp 选择需 justify\n- **4.5 (Layer-wise CKA)**: 虽然 intra-layer CKA（剪枝）与 layer-wise CKA（分析）技术上不同，应加一句说明避免循环论证印象\n\n### Section 5 (Discussion/Conclusion)\n- 显著扩充 Discussion：加入 SFT vs GRPO 角色分离、spectrum 实用指导、与 self-healing 文献对话、30% ceiling 突破方向\n- Throughput regression (-19%) 应在 Limitations 讨论\n\n### Appendix\n- **Appendix E**: 补充 300 步 accuracy 数据（关键缺失）\n- **Appendix O**: \"Cross-Architecture Validation\" 标题误导——Qwen2.5-Math-7B 共享架构。建议改为 \"Cross-Model Validation within Qwen2.5 Family\"\n- RASP 所有 α 值和 Random 应标注 \"single seed\" 脚注\n\n---\n\n**R1 评分**: 3.5 (Borderline Conference)  \n**R2 评分**: 3.0 (Findings)  \n**Director 综合**: 3.0 (Findings)\n\n综合评分倾向 R2 的 3.0 而非 R1 的 3.5，原因：(1) RASP 方法贡献在多 seed 验证前不可靠——如果方法贡献归零，novelty 降为 empirical observation level；(2) scope overclaiming 是系统性问题；(3) decoupling 的训练充分性质疑虽非定论但合理。R1 的 3.5 基于 \"decoupling 发现本身有 novelty\"，这一立场成立但需要更强的 robustness 证据。\n",
    "project": "recovery_aware_struct_prune",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-24T18:25:58.261166+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_04e6cf8fe41be27a49d5657e80962f12:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3967
}
```

</details>

---


### Assistant

_source line 626 · 2026-05-24T18:26:06.033880+00:00_

Round 8 审稿报告已投递。

**结论：3.0 (Findings)**

核心问题：
1. RASP 方法贡献单 seed + 叙事矛盾（Critical，共识）
2. 模型范围 overclaim——仅 Qwen2.5 家族（Critical，共识）
3. Decoupling 训练充分性存疑（Critical，分歧但证据充分）

升至 3.5 的条件：RASP 多 seed 验证 + 1000 步 accuracy 数据 + 非 Qwen 架构验证（至少满足两项）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 53

## Round 53

72 recorded events


### User

_source line 627 · 2026-05-25T21:13:11.407938+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recovery_aware_struct_prune
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-25T21:13:20.443642+00:00_

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
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-25T21:13:21.397579+00:00_

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
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-25T21:13:21.548579+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-25T21:13:21.599292+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-25T21:13:25.834994+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-25T21:13:25.835370+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-25T21:13:29.498892+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-25T21:13:29.499244+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-25T21:13:29.851418+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-25T21:13:30.955828+00:00_

{"result":"# 项目 recovery_aware_struct_prune 概况\n\n## 实验状态 (462 个)\n\n- **grpo_stage2_rasp_20_v2**: DONE (negative) — \n- **grpo_stage2_standard_20**: DONE (killed) — \n- **grpo_stage2_rasp_20**: DONE (killed) — \n- **sft_standard_20**: DONE (success) — \n- **sft_rasp_20**: DONE (success) — \n- **grpo_rasp_20_4096**: DONE (failed) — \n- **grpo_standard_20_4096**: DONE (negative) — \n- **grpo_standard_20_fast**: DONE (negative) — \n- **grpo_rasp_20_fast**: DONE (negative) — \n- **mvp_rasp_pipeline_v4**: PREPARING — \n- **grpo_standard_20**: DONE (killed) — \n- **grpo_rasp_20**: DONE (killed) — \n- **mvp_rasp_pipeline_v3**: DONE (negative) — \n- **mvp_rasp_pipeline_v2**: DONE (failed) — \n- **mvp_rasp_pipeline**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- floor_ablation_0p3_cka_only_20: Floor ratio ablation: lowering the MLP floor from 0.4 to 0.3 allows more aggressive pruning of unimportant layers while CKA-only criterion preserves critical structure. If floor=0.3 maintains GSM8K accuracy within 2pp of floor=0.4 baseline, it demonstrates robustness of CKA-guided pruning to floor choice.（已分配 ? GPU:?，等待提交）\n- floor_ablation_0p5_cka_only_20: Floor ratio ablation: raising the MLP floor from 0.4 to 0.5 constrains pruning to be more conservative. If floor=0.5 improves GSM8K accuracy over floor=0.4, it suggests CKA-only criterion benefits from a higher minimum layer size. Maps the sensitivity curve of floor parameter on recovery quality.（已分配 ? GPU:?，等待提交）\n- …另有 38 项\n\n## 近期结论\n- **eval_gsm8k_grpo_alpha4_20_v2** (killed): α=4.0 GRPO maintains reward 0.15-0.26 (vs α=1.0 collapse to ~0.008), predicting GSM8K accuracy significantly above α=1.0 baseline. v1 timed out at 774/1319 showing 62.93% interim — full eval needed to confirm α-dependent collapse hypothesis. ← 基于 eval_gsm8k_grpo_alpha4_20\n\n## 趋势\n成功 273 / 负向 23 / 失败 84 / 共 422\naccuracy: 0.268 →（近 3 次 success）\navg_response_length: 1110.462 ↑（近 3
…[truncated 1815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-25T21:13:37.831484+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-25T21:13:38.785443+00:00_

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
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{algorithm}
17	\usepackage[noend]{algpseudocode}
18	\usepackage{enumitem}
19	
20	\newcommand{\rasp}{\textsc{Rasp}}
21	
22	\title{How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	
39	\section*{Limitations}
40	\input{limitations}
41	
42	\section*{Ethics Statement}
43	\input{ethics}
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-25T21:13:38.785764+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 641 · 2026-05-25T21:13:40.242185+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 642 · 2026-05-25T21:13:40.744455+00:00_

-rw-r--r-- 1 ubuntu ubuntu 4663523 May 25 21:11 /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 643 · 2026-05-25T21:13:40.895453+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml 2>/dev/null && echo \"ISSUES_EXIST\" || echo \"NO_ISSUES\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml 2>/dev/null && echo \"ISSUES_EXIST\" || echo \"NO_ISSUES\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 644 · 2026-05-25T21:13:40.996335+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml
ISSUES_EXIST

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-25T21:13:45.261344+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found relevant information about ACL conference submission guidelines and ARR (ACL Rolling Review) procedures, though the search results
…[truncated 1415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 6475
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-25T21:13:51.359144+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 call for papers submission format guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 call for papers submission format guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 647 · 2026-05-25T21:13:51.578732+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 conference dates venue commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 conference dates venue commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-25T21:13:52.593497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-25T21:13:53.141543+00:00_

1	Reinforcement learning with verifiable rewards (RLVR) is widely regarded as essential for recovering pruned reasoning models, substantially outperforming supervised fine-tuning (SFT). We find that this advantage vanishes under fine-grained structured pruning: across four criteria applied to a 7B reasoning model at moderate sparsity, SFT and RL recover to near-identical accuracy for each criterion tested. We term this \emph{reward-accuracy decoupling}.
2	What the pruning criterion does control is RL training dynamics. To study this, we introduce Recovery-Aware Structured Pruning (\rasp{}), a scoring function that balances gradient importance with representational diversity via Centered Kernel Alignment (CKA). The resulting \emph{recovery capacity spectrum} shows that diversity-preserving criteria sustain RL optimization while importance-dominated criteria exhibit reward collapse, yet none of these differences translate into accuracy gains over SFT.
3	These findings reframe the role of RL in pruning recovery: SFT warmup captures most recoverable reasoning capacity, while RL serves as a diagnostic that reveals structural deficiencies invisible to accuracy. Directional trends hold across three benchmarks, with preliminary cross-scale and cross-model evidence\footnote{Code and data are available at \url{https://anonymous.4open.science/r/recovery_aware_struct_prune-5FA5/}.}.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 548
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-25T21:13:53.166567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-25T21:13:53.599545+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	Structured pruning compresses reasoning Large Language Models (LLMs) by removing entire channel groups, but the pruned model must recover through fine-tuning.
5	\citet{selfhealing2025} show that reinforcement learning with verifiable rewards (RLVR) substantially outperforms supervised fine-tuning (SFT) for this recovery.
6	This positions RLVR as the dominant paradigm and creates a testable prediction: a pruning criterion that preserves the model's capacity for RL exploration should yield higher final accuracy.
7	The evidence, however, comes from unstructured magnitude pruning at 96.5\% parameter retention; whether the RLVR advantage holds under structural compression, which removes entire computational units and alters the architecture, remains untested.
8	
9	Our experiments reveal that it does not.
10	On DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} pruned to 20\% MLP channel sparsity, one criterion achieves 4.4 times the peak RL reward of another (CKA-only vs.\ Standard) under GRPO~\citep{shao2024grpo}, yet for each criterion individually, SFT and GRPO recover the model to within 1 percentage point of each other.
11	The pruning criterion determines whether RL training succeeds or collapses, but this stark difference leaves almost no trace in final accuracy.
12	We term this pattern \emph{reward-accuracy decoupling}.
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{figures/paper/fig1_dose_response.pdf}
17	\caption{Dose-response of CKA coefficient $\alpha$ on GSM8K at 20\% sparsity. SFT and GRPO curves nearly overlap ($|\Delta| \leq 1.14$\,pp): reward-accuracy decoupling.}
18	\label{fig:dose_response}
19	\end{figure}
20	
21	This disconnect is surprising in light of recent mechanistic work.
22	RL compresses incorrect reasoning paths while SFT expands correct ones~\citep{rlsqueezes2026}.
23	These asymmetric pressures predict that the two paradigms should complement each other, not conv
…[truncated 3047 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 432
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-25T21:13:53.636702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-25T21:13:53.662915+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Structured pruning of LLMs.}
5	Width pruning (LLM-Pruner~\citep{llmpruner2023}, Bonsai~\citep{bonsai2025}, GRASPrune~\citep{graspprune2026}) removes heads or MLP channels; depth pruning~\citep{shortgpt2024,slicegpt2024} removes entire layers but causes severe reasoning degradation~\citep{shrestha2026layerpruninglimits,llms2lrms2026}.
6	For reasoning models, RESP~\citep{resp2025}, RAC~\citep{rac2025}, and SSGR~\citep{ssgr2025} refine calibration data but retain gradient-based importance scoring.
7	Functional-structure-guided methods cluster neurons~\citep{fang_2025}, apply ICA~\citep{funcnet_2025}, or use inter-layer CKA for depth pruning~\citep{mpruner2024,kornblith2019cka}; we differ in using \emph{intra-layer} CKA between individual structures, optimizing for RL recovery.
8	
9	\paragraph{Pruning-aware recovery.}
10	\citet{selfhealing2025} show RLVR restores pruned reasoning models, outperforming SFT, but evaluate only unstructured pruning at 96.5\% retention; our results suggest this advantage diminishes under fine-grained structural pruning that preserves diversity.
11	Complementary axes include post-pruning scaling~\citep{p2law2025}, recovery data selection~\citep{paser2025}, joint pruning-tuning~\citep{pat2025}, post-hoc compensation~\citep{restorelcc_2025}, iterative prune-tune loops~\citep{boiling_frog_2026}, and post-RLVR compression~\citep{opsd2026}; none study which \emph{pruning criterion} enables RL-based recovery.
12	Concurrent benchmarks~\citep{li2025reasoning_compression,canpruning2025} also do not isolate this variable.
13	
14	\paragraph{RLVR training dynamics.}
15	\citet{rlsqueezes2026} show RLVR \emph{compresses} incorrect trajectories while SFT \emph{expands} correct ones, with training evolving linearly by amplifying early trends~\citep{wang2026linearity}; our results qualify this: the asymmetry manifests as a recovery capacity difference, but the expected accuracy gap vanishes when p
…[truncated 681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 26
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-25T21:13:54.040442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-25T21:13:54.161869+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	To isolate how the pruning criterion affects post-RLVR recovery, we hold everything else constant: a shared structural analysis computes importance and functional overlap scores for all prunable structures, four scoring criteria combine these scores differently to select structures for removal, and an identical two-stage recovery pipeline is applied to every pruned model.
5	The only variable across conditions is which structures are removed (Figure~\ref{fig:method_framework}).
6	
7	\subsection{Preliminaries and Notation}
8	\label{sec:prelim}
9	
10	\paragraph{Structured pruning.}
11	Given a pretrained transformer $\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units (attention heads or MLP channels) to reduce model size while maintaining hardware-friendly dense computation.
12	We denote the set of prunable structures as $\mathcal{H} = \{h_1, h_2, \ldots, h_N\}$.
13	In this work, we focus exclusively on MLP channel group pruning; the formalism below covers attention heads for completeness, but all experiments remove only MLP groups.
14	
15	\paragraph{Grouped Query Attention (GQA).}
16	In GQA architectures~\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads ($G = n_Q / n_{KV}$ per group).
17	For DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$, $G{=}7$), we treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit.
18	
19	\paragraph{RLVR and GRPO.}
20	Reinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.
21	We use Group Relative Policy Optimization (GRPO;~\citealp{shao2024grpo}) as the recovery algorithm.
22	
23	\subsection{Structural Analysis}
24	\label{sec:structural_analysis}
25	
26	\begin{figure}[t]
27	    \centering
28	    \includegraphics[width=\columnwidth]{figures/paper/fig_intra_layer_cka.pdf}
29	    \caption{Intra-layer pairwise CKA similarity betwe
…[truncated 9161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 121
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-25T21:13:56.123245+00:00_

Web search results for query: "EMNLP 2026 conference dates venue commitment deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"Empirical Methods in Natural Language Processing - Wikipedia","url":"https://en.wikipedia.org/wiki/Empirical_Methods_in_Natural_Language_Processing"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP (@emnlpmeeting.bsky.social) — Bluesky","url":"https://bsky.app/profile/emnlpmeeting.bsky.social"},{"title":"EMNLP 2026: Conference on Empirical Methods in Natural Language Processing","url":"https://www.myhuiban.com/conference/424?lang=en_us"}]

Based on the search results, here's the information about EMNLP 2026:

**Conference Dates and Venue:**
The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026) will be held in Budapest, Hungary from October 24th to October 29th, 2026.

**Commitment Deadline:**
The EMNLP commitment deadline is August 2, 2026. This is the deadline for authors to commit their reviewed articles to the conference through the Open Review platform.

**Related Importan
…[truncated 239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 4544
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-25T21:13:57.557176+00:00_

Web search results for query: "ACL Rolling Review 2026 call for papers submission format guidelines page limit"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here are the key submission format guidelines and page limits for ACL Rolling Review 2026:

## Page Limits

Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices. Short papers may consist of up to 4 pages of content, plus unlimited references and appendices. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Formatting Guidelines

All long, short, and theme papers must follow the ACL Author Guidelines. Paper submissions must use the official ACL style template.

## Other Important Requirements

- Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities must be avoided.
- The paper has a section titled "Limitations" placed as follows: ACL forma
…[truncated 453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "WebSearch",
  "elapsed_ms": 6198
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-25T21:14:05.839030+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-25T21:14:06.542174+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\begin{figure*}[t]
6	    \centering
7	    \begin{minipage}[t]{0.38\textwidth}
8	        \centering
9	        \includegraphics[width=\textwidth]{figures/paper/fig2_reward_trajectories.pdf}
10	        \centerline{\small (a) Reward trajectories}
11	    \end{minipage}
12	    \hfill
13	    \begin{minipage}[t]{0.58\textwidth}
14	        \centering
15	        \includegraphics[width=\textwidth]{figures/paper/fig3_collapse_dynamics.pdf}
16	        \centerline{\small (b) $f_0$ and gradient norm diagnostics}
17	    \end{minipage}
18	    \caption{GRPO training dynamics at 20\% sparsity. (a)~Reward trajectories. (b)~$f_0$ (zero-variance batch fraction) and gradient norm diagnostics.}
19	    \label{fig:training_dynamics}
20	\end{figure*}
21	
22	\subsection{Experimental Setup}
23	\label{sec:exp_setup}
24	
25	\input{tables/tab1_recovery_gradient}
26	
27	\paragraph{Base model and evaluation.}
28	We evaluate on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with GQA~\citep{ainslie2023gqa} (Section~\ref{sec:prelim}).
29	Our primary benchmark is GSM8K~\citep{cobbe2021gsm8k} ($N{=}1{,}319$ grade-school math problems; exact-match accuracy).
30	The unpruned model achieves 90.83\% (greedy decoding).
31	
32	\paragraph{Pruning methods.}
33	We compare four pruning criteria at 20\% structured sparsity, all removing 200 of 784 MLP channel groups across 28 layers (${\sim}$1.45B parameters) with identical per-layer capacity floors (${\ge}$40\% retention): \textbf{CKA-only} (Eq.~\ref{eq:cka_only}), \textbf{Standard} (Eq.~\ref{eq:standard}; LLM-Pruner~\citep{llmpruner2023}), \textbf{\rasp{}} at $\alpha{=}1.0$ (Eq.~\ref{eq:score}), and \textbf{Random} (uniform selection; uses TRL's default 512-token generation limit vs.\ 1{,}024 for other methods).
34	See Section~\ref{sec:scoring} and Figure~\ref{fig:pruning_decisions} for scoring details.
35	
36	\paragraph{
…[truncated 10098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-25T21:14:06.592784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-25T21:14:06.593201+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Whether RLVR outperforms SFT for recovering pruned reasoning models appears to depend on how the model was pruned.
5	Under diversity-preserving pruning at 20--25\% MLP sparsity on Qwen2.5-family models, the two paradigms produce near-identical accuracy (mean $|\Delta| {=} 0.54$\,pp for the four main criteria on GSM8K at 20\%; max $1.8$\,pp across benchmarks and $\alpha$ variants), yet the pruning criterion creates a 4.4$\times$ peak reward gap.
6	At 20\% sparsity, SFT warmup recovers the bulk of accuracy (from $<$2\% post-prune to 51--64\%); GRPO exposes structural capacity differences but contributes minimal additional accuracy, a pattern that persists at 300 steps (Appendix~\ref{sec:appendix_extended}).
7	The non-monotonic $\alpha$ dose-response argues against a layer-distribution confound.
8	A practical implication is that GRPO reward trajectories and $f_0$ diagnostics can serve as probes for evaluating pruning quality, surfacing structural deficiencies that accuracy alone would miss.
9	Rather than running full RL recovery to estimate final accuracy (which our results show remains constant across criteria), a short GRPO probe of ${\sim}$100 steps suffices to diagnose whether a pruned model retains the structural diversity needed for downstream RL fine-tuning or task-specific RL alignment.
10	We discuss broader implications in Appendix~\ref{sec:appendix_discussion}.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-25T21:14:06.944788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-25T21:14:07.447087+00:00_

1	% Limitations --- required by ACL/EMNLP
2	
3	Our results are validated on two Qwen2.5-family models (7B and 1.5B); generalization to other architecture families (e.g., LLaMA, Mistral) and larger scales remains open.
4	We evaluate on three benchmarks (GSM8K, MATH-500, MBPP); logical, commonsense, and multi-modal reasoning are not covered.
5	\rasp{} $\alpha$ variants and Random use single GRPO seeds, so fine-grained ranking among these should be interpreted with caution.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-25T21:14:07.447436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-25T21:14:08.050861+00:00_

1	\section{Training Details}
2	\label{sec:appendix_training}
3	
4	Table~\ref{tab:hyperparams} lists the full hyperparameter configurations for both recovery stages described in Section~\ref{sec:exp_setup}. All four pruning criteria share identical SFT and GRPO settings; the only difference is Random's shorter generation limit, inherited from the TRL library default.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Hyperparameter details for SFT warmup and GRPO recovery stages. All methods share the same GRPO configuration; Random uses the TRL default generation limit (marked with $^\dagger$).}
10	\label{tab:hyperparams}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}lll@{}}
13	\toprule
14	Parameter & SFT & GRPO \\
15	\midrule
16	Learning rate & $2 \times 10^{-5}$ & $1 \times 10^{-6}$ \\
17	Batch size & 1 & 1 \\
18	Gradient accumulation & 8 & 1 \\
19	Max sequence length & 2{,}048 & -- \\
20	Max new tokens & -- & 1{,}024\,$^\dagger$512 \\
21	Optimizer & AdamW & AdamW \\
22	Epochs / Steps & 2 epochs & 100 steps \\
23	KL coefficient $\beta$ & -- & 0.01 \\
24	Sampling temperature & -- & 0.4 \\
25	Num generations per prompt & -- & 8 \\
26	Reward & -- & Binary (exact match) \\
27	Loss formulation & Cross-entropy & DAPO-style clipped \\
28	\texttt{reward\_desert\_patience} & -- & 50 \\
29	\bottomrule
30	\multicolumn{3}{l}{\footnotesize $^\dagger$Random uses TRL default of 512 tokens; all other methods use 1{,}024.} \\
31	\end{tabular}}
32	\end{table}
33	
34	\section{Algorithm}
35	\label{sec:appendix_algo}
36	
37	Algorithm~\ref{alg:rasp} summarizes the complete pruning comparison procedure from Section~\ref{sec:method}: shared structural analysis (importance and CKA overlap computation), criterion-specific scoring (Eqs.~\ref{eq:standard}--\ref{eq:cka_only}), and two-stage recovery (SFT warmup followed by GRPO).
38	
39	\begin{algorithm}[h]
40	\caption{Controlled Pruning Comparison Framework}
41	\label{alg:rasp}
42	\begin{algorithmic}[1]
43	\Require Model $\mathc
…[truncated 26391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-25T21:14:08.051355+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml",
  "description": "Read review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml",
    "description": "Read review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-25T21:14:08.152367+00:00_

&lt;persisted-output>
Output too large (35KB). Full output saved to: /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune--claude-sessions-review-director-0d7cc07d/3203ea6e-31da-4bd3-bd3f-a386371d6b78/tool-results/b2uwd7uy0.txt

Preview (first 2KB):
# ============================================================
# Round 1-3 Issues — All Resolved
# ============================================================

- id: "R1-C1"
  summary: "CKA-recovery link 仅相关性, 无因果干预"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证"
  resolution_round: 3

- id: "R1-C2"
  summary: "Single-seed GRPO 无统计显著性"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "3-seed GRPO CKA-only, Welch's t-test p=0.0009"
  resolution_round: 3

- id: "R1-C3"
  summary: "仅 GSM8K 单基准"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "MATH-500 OOD 验证 + MBPP 代码基准"
  resolution_round: 3

- id: "R1-W1"
  summary: "Title overclaim 'determines'"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Title 改为 'shapes'"
  resolution_round: 3

- id: "R1-W2"
  summary: "Abstract 'universally determines' overclaim"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "改为 'significantly shapes'"
  resolution_round: 3

- id: "R1-W3"
  summary: "仅 DeepSeek-R1-7B 单模型"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Qwen2.5-Math-7B cross-arch + 1.5B cross-scale"
  resolution_round: 3

- id: "R1-M1"
  summary: "GRPO 超参未报告"
  category: experiment
  severity: info
  status: resolved
  first_raise
…[truncated 343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-25T21:14:13.336475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune--claude-sessions-review-director-0d7cc07d/3203ea6e-31da-4bd3-bd3f-a386371d6b78/tool-results/b2uwd7uy0.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune--claude-sessions-review-director-0d7cc07d/3203ea6e-31da-4bd3-bd3f-a386371d6b78/tool-results/b2uwd7uy0.txt"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-25T21:14:14.390988+00:00_

1	
2	# ============================================================
3	# Round 1-3 Issues — All Resolved
4	# ============================================================
5	
6	- id: "R1-C1"
7	  summary: "CKA-recovery link 仅相关性, 无因果干预"
8	  category: method
9	  severity: critical
10	  status: resolved
11	  first_raised_round: 1
12	  last_seen_round: 3
13	  resolution: "Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证"
14	  resolution_round: 3
15	
16	- id: "R1-C2"
17	  summary: "Single-seed GRPO 无统计显著性"
18	  category: experiment
19	  severity: critical
20	  status: resolved
21	  first_raised_round: 1
22	  last_seen_round: 3
23	  resolution: "3-seed GRPO CKA-only, Welch's t-test p=0.0009"
24	  resolution_round: 3
25	
26	- id: "R1-C3"
27	  summary: "仅 GSM8K 单基准"
28	  category: experiment
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 1
32	  last_seen_round: 3
33	  resolution: "MATH-500 OOD 验证 + MBPP 代码基准"
34	  resolution_round: 3
35	
36	- id: "R1-W1"
37	  summary: "Title overclaim 'determines'"
38	  category: framing
39	  severity: warning
40	  status: resolved
41	  first_raised_round: 1
42	  last_seen_round: 3
43	  resolution: "Title 改为 'shapes'"
44	  resolution_round: 3
45	
46	- id: "R1-W2"
47	  summary: "Abstract 'universally determines' overclaim"
48	  category: framing
49	  severity: warning
50	  status: resolved
51	  first_raised_round: 1
52	  last_seen_round: 3
53	  resolution: "改为 'significantly shapes'"
54	  resolution_round: 3
55	
56	- id: "R1-W3"
57	  summary: "仅 DeepSeek-R1-7B 单模型"
58	  category: experiment
59	  severity: warning
60	  status: resolved
61	  first_raised_round: 1
62	  last_seen_round: 3
63	  resolution: "Qwen2.5-Math-7B cross-arch + 1.5B cross-scale"
64	  resolution_round: 3
65	
66	- id: "R1-M1"
67	  summary: "GRPO 超参未报告"
68	  category: experiment
69	  severity: info
70	  status: resolved
71	  first_raised_round: 1
72	  last_seen_round: 3
73	  resolution: "Appendix 完整超参表"
74	  resolution_round: 3
75	
76	- id: "R1-M2"
77	  sum
…[truncated 33237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-25T21:14:14.642042+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-25T21:14:14.642398+00:00_

1	This work uses publicly available models (DeepSeek-R1-Distill-Qwen, Qwen2.5-Math) and established benchmarks (GSM8K, MATH-500, MBPP); no private data or human subjects are involved.
2	Structured pruning reduces model size and inference memory, which can lower the computational cost and energy consumption of deploying large language models.
3	Our research focuses on the technical analysis of pruning criteria and their interaction with reinforcement learning recovery; we do not foresee direct negative societal impacts from this work.
4	All models and datasets used in this work are publicly available under permissive licenses: DeepSeek-R1-Distill-Qwen (MIT), Qwen2.5-Math (Apache 2.0), GSM8K (MIT), MATH (MIT), and MBPP (CC-BY-4.0).
5	We disclose our use of AI assistants in Appendix~\ref{sec:appendix_ai_assistants}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-25T21:14:14.692838+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "tables/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "tables/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-25T21:14:14.793727+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-25T21:14:19.460964+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/tab*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/tab*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-25T21:14:19.511734+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/_deprecated/table2_recovery.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/_deprecated/table5_inference.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/_deprecated/table1_postprune.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-25T21:14:25.131940+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-25T21:14:25.734475+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Recovery capacity spectrum at 20\% sparsity. $f_0$: zero-variance batch fraction. Best in \textbf{bold}.}
5	\label{tab:recovery_gradient}
6	\setlength{\tabcolsep}{5pt}
7	\begin{tabular}{@{}lccc@{}}
8	\toprule
9	Method & Peak Rew.\,$\uparrow$ & Mean Rew.\,$\uparrow$ & Min $f_0$\,$\downarrow$ \\
10	\midrule
11	CKA-only & \textbf{0.354} & \textbf{0.285} & \textbf{0.125} \\
12	Random & 0.190 & 0.164 & 0.300 \\
13	Standard & 0.081 & 0.050 & 0.500 \\
14	\rasp{} ($\alpha{=}1.0$) & 0.061 & 0.031 & 0.675 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-25T21:14:25.785003+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-25T21:14:26.563914+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Reward-accuracy decoupling on GSM8K ($N{=}1{,}319$) at 20\% sparsity. $\pm$: multi-seed std. Best in \textbf{bold}.}
5	\label{tab:decoupling}
6	\setlength{\tabcolsep}{4pt}
7	\begin{tabular}{@{}lcccc@{}}
8	\toprule
9	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) & Peak Rew. \\
10	\midrule
11	Unpruned & \textbf{81.27} & \textbf{81.27} & $\phantom{-}$0.00 & \textbf{0.669} \\
12	\rasp{} ($\alpha{=}2.0$) & 64.97 & 66.11 & $+$1.14 & -- \\
13	CKA-only & 63.91 & 64.39{\scriptsize$\pm$0.19} & $+$0.48 & 0.354 \\
14	Standard & 59.29 & 59.84{\scriptsize$\pm$0.38} & $+$0.55 & 0.081 \\
15	\rasp{} ($\alpha{=}1.0$) & 61.49 & 60.88 & $-$0.61 & 0.061 \\
16	Random & 51.25 & 50.72{\scriptsize$\pm$0.15} & $-$0.53 & 0.190 \\
17	\midrule
18	ShortGPT & 44.73 & 43.37 & $-$1.36 & -- \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 778
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-25T21:14:26.564380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-25T21:14:26.564659+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Dose-response analysis: effect of CKA coefficient $\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\% MLP channel sparsity. $\alpha{=}0$ reduces to Standard (importance-only); higher $\alpha$ weights representational diversity. Best in \textbf{bold}.}
5	\label{tab:alpha}
6	\begin{tabular}{@{}cccc@{}}
7	\toprule
8	$\alpha$ & SFT Acc.\,(\%) & GRPO Acc.\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	0.5 & 60.73 & 61.18 & $+$0.45 \\
11	1.0 & 61.49 & 60.88 & $-$0.61 \\
12	\textbf{2.0} & \textbf{64.97} & \textbf{66.11} & $+$1.14 \\
13	3.0 & 64.14 & 63.46 & $-$0.68 \\
14	4.0 & 61.94 & 62.77 & $+$0.83 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-25T21:14:27.016596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-25T21:14:27.368426+00:00_

1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \texttt{max\_new\_tokens=2048}). CKA-only and Standard both outperform \rasp{} and Random; the CKA-only--Standard GRPO gap is 0.6\,pp (vs.\ 4.6\,pp on GSM8K), consistent with difficulty and truncation compressing scores toward a floor. Best per section in \textbf{bold}.}
5	\label{tab:math500}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & \multicolumn{3}{c}{53.0\,$^\dagger$} \\
11	\midrule
12	\multicolumn{4}{l}{\textit{20\% sparsity --- method comparison}} \\
13	CKA-only & \textbf{27.4} & \textbf{27.6} & $+$0.2 \\
14	Standard & 25.6 & 27.0 & $+$1.4 \\
15	\rasp{} ($\alpha{=}1.0$) & 21.6 & 23.0 & $+$1.4 \\
16	Random & 16.6 & 15.0 & $-$1.6 \\
17	\midrule
18	\multicolumn{4}{l}{\textit{20\% sparsity --- $\alpha$ dose-response}} \\
19	$\alpha{=}0.5$ & 26.8 & 26.8 & $+$0.0 \\
20	$\alpha{=}2.0$ & 25.6 & \textbf{27.4} & $+$1.8 \\
21	$\alpha{=}3.0$ & 23.6 & -- & -- \\
22	$\alpha{=}4.0$ & \textbf{27.8} & 27.2 & $-$0.6 \\
23	\midrule
24	\multicolumn{4}{l}{\textit{25\% sparsity}} \\
25	CKA-only & 18.8 & 17.6 & $-$1.2 \\
26	Standard & 15.4 & -- & -- \\
27	\bottomrule
28	\multicolumn{4}{p{0.85\columnwidth}}{\footnotesize $^\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\% at 4096); all pruned models evaluated under the same constraint.}
29	\end{tabular}
30	\end{table}
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-25T21:14:27.770360+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-25T21:14:27.821013+00:00_

1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MBPP code generation accuracy ($N{=}374$, greedy decoding). All fine-grained pruning methods converge near a capability floor (${\sim}$75\% code capability loss vs Dense), limiting differentiation (${\sim}$1\,pp range, within stderr). ShortGPT shows a larger GRPO delta ($+$4.01\,pp) but at the 95\% CI boundary (stderr ${\approx}$1.55\,pp).}
5	\label{tab:mbpp}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & -- & 53.48 & -- \\
11	\midrule
12	CKA-only 20\% & 12.83 & 14.17 & $+$1.34 \\
13	Standard 20\% & 12.03 & 13.10 & $+$1.07 \\
14	\rasp{} ($\alpha{=}1.0$) 20\% & 11.76 & 13.10 & $+$1.34 \\
15	\midrule
16	ShortGPT 20\%$^\dagger$ & 10.43 & 14.44 & $+$4.01 \\
17	\bottomrule
18	\multicolumn{4}{l}{\footnotesize $^\dagger$Depth pruning; removes entire layers.}
19	\end{tabular}
20	\end{table}
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-25T21:14:51.003150+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool call

_source line 687 · 2026-05-25T21:14:51.605573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 688 · 2026-05-25T21:14:52.057548+00:00_

{"result":"# 项目 recovery_aware_struct_prune 概况\n\n## 实验状态 (462 个)\n\n- **grpo_stage2_rasp_20_v2**: DONE (negative) — \n- **grpo_stage2_standard_20**: DONE (killed) — \n- **grpo_stage2_rasp_20**: DONE (killed) — \n- **sft_standard_20**: DONE (success) — \n- **sft_rasp_20**: DONE (success) — \n- **grpo_rasp_20_4096**: DONE (failed) — \n- **grpo_standard_20_4096**: DONE (negative) — \n- **grpo_standard_20_fast**: DONE (negative) — \n- **grpo_rasp_20_fast**: DONE (negative) — \n- **mvp_rasp_pipeline_v4**: PREPARING — \n- **grpo_standard_20**: DONE (killed) — \n- **grpo_rasp_20**: DONE (killed) — \n- **mvp_rasp_pipeline_v3**: DONE (negative) — \n- **mvp_rasp_pipeline_v2**: DONE (failed) — \n- **mvp_rasp_pipeline**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- floor_ablation_0p3_cka_only_20: Floor ratio ablation: lowering the MLP floor from 0.4 to 0.3 allows more aggressive pruning of unimportant layers while CKA-only criterion preserves critical structure. If floor=0.3 maintains GSM8K accuracy within 2pp of floor=0.4 baseline, it demonstrates robustness of CKA-guided pruning to floor choice.（已分配 ? GPU:?，等待提交）\n- floor_ablation_0p5_cka_only_20: Floor ratio ablation: raising the MLP floor from 0.4 to 0.5 constrains pruning to be more conservative. If floor=0.5 improves GSM8K accuracy over floor=0.4, it suggests CKA-only criterion benefits from a higher minimum layer size. Maps the sensitivity curve of floor parameter on recovery quality.（已分配 ? GPU:?，等待提交）\n- …另有 38 项\n\n## 近期结论\n- **eval_gsm8k_grpo_alpha4_20_v2** (killed): α=4.0 GRPO maintains reward 0.15-0.26 (vs α=1.0 collapse to ~0.008), predicting GSM8K accuracy significantly above α=1.0 baseline. v1 timed out at 774/1319 showing 62.93% interim — full eval needed to confirm α-dependent collapse hypothesis. ← 基于 eval_gsm8k_grpo_alpha4_20\n\n## 趋势\n成功 273 / 负向 23 / 失败 84 / 共 422\naccuracy: 0.268 →（近 3 次 success）\navg_response_length: 1110.462 ↑（近 3
…[truncated 1815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-25T21:14:52.058053+00:00_

1	@article{austin2021mbpp,
2	  title={Program Synthesis with Large Language Models},
3	  author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michalewski, Henryk and Dohan, David and Jiang, Ellen and Cai, Carrie and Terry, Michael and Le, Quoc and Sutton, Charles},
4	  journal={arXiv preprint arXiv:2108.07732},
5	  year={2021},
6	}
7	
8	@article{deepseek2025r1,
9	  title={DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},
10	  author={{DeepSeek-AI}},
11	  journal={arXiv preprint arXiv:2501.12948},
12	  year={2025},
13	  url={https://arxiv.org/abs/2501.12948}
14	}
15	
16	@article{qwen2.5,
17	  title={Qwen2.5 Technical Report},
18	  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and others},
19	  journal={arXiv preprint arXiv:2412.15115},
20	  year={2024},
21	  url={https://arxiv.org/abs/2412.15115}
22	}
23	
24	@article{cobbe2021gsm8k,
25	  title={Training Verifiers to Solve Math Word Problems},
26	  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
27	  journal={arXiv preprint arXiv:2110.14168},
28	  year={2021},
29	  url={https://arxiv.org/abs/2110.14168}
30	}
31	
32	@article{shao2024grpo,
33	  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
34	  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
35	  journal={arXiv preprint arXiv:2402.03300},
36	  year={2024},
37	  url={https://arxiv.org/abs/2402.03300}
38	}
39	
40	@inproceedings{llmpruner2023,
41	  title={LLM-Pruner: On the Structural Pruning of Large Language Models},
42	  author={Ma, Xinyin and Fang, Gongfan and Wang, Xinchao},
43	  booktitle={Advances in Neu
…[truncated 12200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-25T21:15:29.964587+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
  }
}
```

</details>

---


### Tool call

_source line 691 · 2026-05-25T21:15:30.516782+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 692 · 2026-05-25T21:15:58.963449+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 28998
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-25T21:15:58.963941+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 28447
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-25T21:15:59.014468+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recovery_aware_struct_prune",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## 论文信息\n- 标题: \"How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM\"\n- 目标 venue: **EMNLP 2026**（通过 ARR 统一审稿）\n- 截止日期: 2026-05-25\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf`\n\n## Venue 格式要求\n- **页数限制**: 正文 8 页，参考文献无限制\n- **模板**: ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（ARR 政策）\n- **Limitations**: 必须包含，不计入页数\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. RASP 方法论\n- Eq.2 乘法形式 I(h)×(1-F(h))^α 的理论动机是否充分？\n- α=1.0 collapse 是否可能由函数形式（而非 diversity-importance tradeoff）导致？I(h)=0 时 score=0 的行为是否合理？\n- 与加法替代形式 βI(h)+(1-β)(1-F(h)) 的对比是否缺失？\n- CKA-only（Eq.3）本质上忽略 importance，为何比 RASP \"平衡\"方案更优？这对方法贡献意味着什么？\n\n### 2. 统计严谨性\n- Decoupling claim: TOST ε=2pp 的选择是否有 post-hoc selection 嫌疑？justify 是否充分？\n- RASP α=2.0 vs CKA-only 仅 1.72pp 差距（单 seed）——统计可靠性？\n- Random baseline 的 max_completion_length=512 vs 其他方法 1024——这一不一致对 spectrum 排序有何影响？\n- 15% sparsity 下 GRPO amplifies gap（与 20-25% decoupling 矛盾）——作者如何解释 boundary condition？\n- Cross-seed 验证：CKA-only 和 Standard 3-seed，但 RASP α variants 和 Random 单 seed——不对称\n\n### 3. 实验控制\n- 300-step extended training 是否报告了 accuracy（而非仅 reward）？\n- Calibration data M=512 的选择依据？\n- Floor ablation τ∈{0.3,0.4,0.5,0.6} 的结果是否充分支持 τ=0.4 选择？\n- Dose-response 中 max_completion_length 不一致（R5-W4/R7-N1 类问题）是否已解决？\n\n### 4. Decoupling 核心论点\n- SFT warmup 恢复 ~60pp（从 <2% 到 51-64%），GRPO 增量 <1pp——\"reward-accuracy decoupling\" 是否可能是训练不足的 artifact？\n- 15% sparsity 下 GRPO amplifies CKA advantage (+1.51pp) 的事实是否 undermines decoupling 的普遍性？\n\n请严格、不留情面地评审。输出格式：\n```\n## Strengths (逐条)\n## Weaknesses (逐条，标注严重程度 Critical/Warning/Minor)\n## Questions (需要作者回答的)\n## Missing References\n## Overall Assessment (评分 + 简短理由)\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recovery_aware_struct_prune",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## 论文信息\n- 标题: \"How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM\"\n- 目标 venue: **EMNLP 2026**（通过 ARR 统一审稿）\n- 截止日期: 2026-05-25\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf`\n\n## Venue 格式要求\n- **页数限制**: 正文 8 页，参考文献无限制\n- **模板**: ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（ARR 政策）\n- **Limitations**: 必须包含，不计入页数\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. RASP 方法论\n- Eq.2 乘法形式 I(h)×(1-F(h))^α 的理论动机是否充分？\n- α=1.0 collapse 是否可能由函数形式（而非 diversity-importance tradeoff）导致？I(h)=0 时 score=0 的行为是否合理？\n- 与加法替代形式 βI(h)+(1-β)(1-F(h)) 的对比是否缺失？\n- CKA-only（Eq.3）本质上忽略 importance，为何比 RASP \"平衡\"方案更优？这对方法贡献意味着什么？\n\n### 2. 统计严谨性\n- Decoupling claim: TOST ε=2pp 的选择是否有 post-hoc selection 嫌疑？justify 是否充分？\n- RASP α=2.0 vs CKA-only 仅 1.72pp 差距（单 seed）——统计可靠性？\n- Random baseline 的 max_completion_length=512 vs 其他方法 1024——这一不一致对 spectrum 排序有何影响？\n- 15% sparsity 下 GRPO amplifies gap（与 20-25% decoupling 矛盾）——作者如何解释 boundary condition？\n- Cross-seed 验证：CKA-only 和 Standard 3-seed，但 RASP α variants 和 Random 单 seed——不对称\n\n### 3. 实验控制\n- 300-step extended training 是否报告了 accuracy（而非仅 reward）？\n- Calibration data M=512 的选择依据？\n- Floor ablation τ∈{0.3,0.4,0.5,0.6} 的结果是否充分支持 τ=0.4 选择？\n- Dose-response 中 max_completion_length 不一致（R5-W4/R7-N1 类问题）是否已解决？\n\n### 4. Decoupling 核心论点\n- SFT warmup 恢复 ~60pp（从 <2% 到 51-64%），GRPO 增量 <1pp——\"reward-accuracy decoupling\" 是否可能是训练不足的 artifact？\n- 15% sparsity 下 GRPO amplifies CKA advantage (+1.51pp) 的事实是否 undermines decoupling 的普遍性？\n\n请严格、不留情面地评审。输出格式：\n```\n## Strengths (逐条)\n## Weaknesses (逐条，标注严重程度 Critical/Warning/Minor)\n## Questions (需要作者回答的)\n## Missing References\n## Overall Assessment (评分 + 简短理由)\n```"
  }
}
````

</details>

---


### Tool result

_source line 695 · 2026-05-25T21:16:21.717750+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22703
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-25T21:16:21.868621+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recovery_aware_struct_prune",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性**审查。\n\n## 论文信息\n- 标题: \"How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM\"\n- 目标 venue: **EMNLP 2026**（通过 ARR 统一审稿）\n- 截止日期: 2026-05-25\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf`\n\n## Venue 格式要求\n- **页数限制**: 正文 8 页，参考文献无限制\n- **模板**: ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（ARR 政策）\n- **Limitations**: 必须包含，不计入页数\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献\n- \"Reward-accuracy decoupling\" 是否是一个真正新颖的发现？还是 SFT 训练不足/GRPO 训练不足的 artifact？\n- RASP 作为方法贡献的价值：α=2.0（最佳）本质上是 CKA-dominant（diversity 权重 >> importance 权重），这是否 undermines \"balancing importance and diversity\" 的叙事？\n- \"Recovery capacity spectrum\" 的实用价值——如果所有方法最终 accuracy 差不多，这个 spectrum 的意义何在？\n- GRPO 作为 diagnostic probe 的 claim 是否有 actionable value？\n\n### 2. 相关工作与定位\n- 检查以下文献是否被引用和充分讨论：\n  * Li et al. (2025, arXiv:2504.02010) \"When Reasoning Meets Compression\"\n  * \"Can Pruning Improve Reasoning?\" (arXiv:2505.14582)\n  * 其他结构化剪枝 + reasoning model 的近期工作\n- Self-Healing (Ji et al., 2025) 的定位：本文声称 \"RLVR > SFT advantage vanishes under structured pruning\"——但 Ji et al. 研究的是 unstructured pruning at 96.5% retention，两者的 setting 差异是否被充分讨论？\n- 与 Mukherjee et al. (2025, RL Finetunes Small Subnetworks) 的关系\n\n### 3. Framing 准确性\n- Title 中 \"a Reasoning LLM\"（单数）vs 论文覆盖多个模型——是否准确？\n- Abstract 中 \"moderate sparsity\" 是否精确限定了 20-25% 窗口？\n- 30% sparsity 全面 collapse 的事实是否被适当讨论？有效窗口 20-25% 是否过窄？\n- Contribution 3 \"SFT warmup as the dominant recovery mechanism\"——如果这是主要发现，为何 Title 和叙事聚焦于 RLVR/GRPO？\n- 论文是否存在 overclaiming？（检查 Abstract、Conclusion、Contribution list）\n\n### 4. 写作质量\n- Section 5 (Conclusion) 是否过于简短？Discussion 是否充分？\n- \"recovery capacity spectrum\"、\"reward-accuracy decoupling\"、\"dose-response\" 等术语是否被清晰定义？\n- 概念先用后定义的问题（如 \"recovery capacity\" 在 Section 1 使用但 Section 3.4 才定义）\n- Limitations section 是否覆盖了关键局限？\n\n### 5. 泛化性\n- 所有实验基于 Qwen2.5 架构族——Title 是否 overclaim？\n- Qwen2.5-Math-7B 仅有 SFT 验证，GRPO 缺失（脚注提供 preliminary 48.60% 但 83.8% truncated）\n- 仅 MLP channel pruning，不包含 attention head pruning——scope 是否被正确限定？\n\n请严格、不留情面地评审。输出格式：\n```\n## Strengths (逐条)\n## Weaknesses (逐条，标注严重程度 Critical/Warning/Minor)\n## Questions (需要作者回答的)\n## Missing References\n## Overall Assessment (评分 + 简短理由)\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recovery_aware_struct_prune",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性**审查。\n\n## 论文信息\n- 标题: \"How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM\"\n- 目标 venue: **EMNLP 2026**（通过 ARR 统一审稿）\n- 截止日期: 2026-05-25\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf`\n\n## Venue 格式要求\n- **页数限制**: 正文 8 页，参考文献无限制\n- **模板**: ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（ARR 政策）\n- **Limitations**: 必须包含，不计入页数\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献\n- \"Reward-accuracy decoupling\" 是否是一个真正新颖的发现？还是 SFT 训练不足/GRPO 训练不足的 artifact？\n- RASP 作为方法贡献的价值：α=2.0（最佳）本质上是 CKA-dominant（diversity 权重 >> importance 权重），这是否 undermines \"balancing importance and diversity\" 的叙事？\n- \"Recovery capacity spectrum\" 的实用价值——如果所有方法最终 accuracy 差不多，这个 spectrum 的意义何在？\n- GRPO 作为 diagnostic probe 的 claim 是否有 actionable value？\n\n### 2. 相关工作与定位\n- 检查以下文献是否被引用和充分讨论：\n  * Li et al. (2025, arXiv:2504.02010) \"When Reasoning Meets Compression\"\n  * \"Can Pruning Improve Reasoning?\" (arXiv:2505.14582)\n  * 其他结构化剪枝 + reasoning model 的近期工作\n- Self-Healing (Ji et al., 2025) 的定位：本文声称 \"RLVR > SFT advantage vanishes under structured pruning\"——但 Ji et al. 研究的是 unstructured pruning at 96.5% retention，两者的 setting 差异是否被充分讨论？\n- 与 Mukherjee et al. (2025, RL Finetunes Small Subnetworks) 的关系\n\n### 3. Framing 准确性\n- Title 中 \"a Reasoning LLM\"（单数）vs 论文覆盖多个模型——是否准确？\n- Abstract 中 \"moderate sparsity\" 是否精确限定了 20-25% 窗口？\n- 30% sparsity 全面 collapse 的事实是否被适当讨论？有效窗口 20-25% 是否过窄？\n- Contribution 3 \"SFT warmup as the dominant recovery mechanism\"——如果这是主要发现，为何 Title 和叙事聚焦于 RLVR/GRPO？\n- 论文是否存在 overclaiming？（检查 Abstract、Conclusion、Contribution list）\n\n### 4. 写作质量\n- Section 5 (Conclusion) 是否过于简短？Discussion 是否充分？\n- \"recovery capacity spectrum\"、\"reward-accuracy decoupling\"、\"dose-response\" 等术语是否被清晰定义？\n- 概念先用后定义的问题（如 \"recovery capacity\" 在 Section 1 使用但 Section 3.4 才定义）\n- Limitations section 是否覆盖了关键局限？\n\n### 5. 泛化性\n- 所有实验基于 Qwen2.5 架构族——Title 是否 overclaim？\n- Qwen2.5-Math-7B 仅有 SFT 验证，GRPO 缺失（脚注提供 preliminary 48.60% 但 83.8% truncated）\n- 仅 MLP channel pruning，不包含 attention head pruning——scope 是否被正确限定？\n\n请严格、不留情面地评审。输出格式：\n```\n## Strengths (逐条)\n## Weaknesses (逐条，标注严重程度 Critical/Warning/Minor)\n## Questions (需要作者回答的)\n## Missing References\n## Overall Assessment (评分 + 简短理由)\n```"
  }
}
````

</details>

---


### Tool result

_source line 697 · 2026-05-25T21:16:23.282457+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1413
}
```

</details>

---


### Assistant

_source line 698 · 2026-05-25T21:16:33.459625+00:00_

Round 9 审稿圆桌会议已启动。

**编排**：
- **Reviewer 1**（方法严谨性 + 实验设计）→ 已派发
- **Reviewer 2**（新颖性 + 完整性）→ 已派发
- **视觉审查 Agent** → 已启动（并行，不阻塞）
- **外部审稿（Stanford Agentic Reviewer）** → 未配置，跳过

**Venue 确认**：EMNLP 2026 via ARR，长文 8 页限制，ACL 模板，double-blind。ARR 提交截止 2026-05-25（今日），commitment deadline 2026-08-02。

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 699 · 2026-05-25T21:22:47.101190+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见（Round 1）：新颖性 + 完整性

**论文**: "How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM"
**Venue**: EMNLP 2026 (ARR)

---

## 总体评分

**Overall Assessment**: 3.0 / 5 — Findings
**一句话总结**: 实验设计严谨、控制变量干净，但核心新颖性不足——"reward-accuracy decoupling"很可能是 SFT 天花板效应的 artifact 而非独立发现，RASP 方法贡献被 α=2.0 (CKA-dominant) 的最优点 undermined，有效剪枝窗口仅 20–25% 严重限制实用价值。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 控制变量设计好，TOST 等统计检验到位，但核心 claim ("decoupling") 存在未排除的混淆因素 |
| Excitement | 2.5/5 | 研究问题有意义，但主要发现是 "SFT 做了大部分工作，GRPO 贡献边际"——这个结论的 actionable value 有限 |
| Overall | 3.0/5 | Findings 水平：实证贡献扎实但新颖性和影响力不足以支撑主会议接收 |
| Confidence | 4/5 | 熟悉 LLM 剪枝和 RL fine-tuning 领域 |

---

## Strengths（优势）

**S1. 干净的控制变量实验设计。** 四种剪枝标准共享同一结构分析流程（importance + CKA），仅改变组合方式，然后经历完全相同的两阶段恢复（SFT → GRPO）。这是剪枝文献中罕见的严谨对比，能有效隔离剪枝标准本身的效应。Algorithm 1（Appendix B）清晰形式化了这一框架。

**S2. 统计严谨性远超同领域平均水平。** TOST 等价检验（Appendix T）、多种子 GRPO 验证（Appendix L，3 seeds ×4 methods）、paired Two One-Sided Tests、cross-seed 标准差报告（Section 4.5, σ=0.19 pp）——这些在剪枝实证论文中不常见。

**S3. 丰富的 Appendix 系统。** 从 A 到 V 共 22 个 appendix，覆盖 CKA 稳定性（H）、梯度信号分析（I）、30% 剪枝崩塌（K）、深度优先基线（R）、per-layer capacity floor（S）等。显示了对审稿人可能质疑的全面预判。

**S4. Recovery capacity spectrum 概念有启发性。** 用 GRPO 训练动态（peak reward, f₀, gradient norm, KL divergence）作为剪枝结构质量的诊断信号（Section 3.5, Figure 5），虽然目前主要是 correlational，但提供了一个有趣的视角。

**S5. 跨尺度验证初步覆盖。** DeepSeek-R1-Distill-Qwen-1.5B（Appendix N）和 Qwen2.5-Math-7B（Appendix O）的初步验证显示 recovery capacity spectrum ordering 在不同模型上基本一致。

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] **"Reward-accuracy decoupling" 极可能是 SFT 天花板效应的 artifact，而非独立发现**
- 具体位置：Section 4.3, Table 2, Figure 6
- 问题：论文声称 GRPO 产生高 reward 但几乎不改变 accuracy，称之为 "decoupling"。但数据显示 SFT warmup 已将 accuracy 恢复到 51–64%（取决于剪枝标准），而 dense model 为 90.83%（Table 2, "Unpruned" 行）。在 20% 结构化剪枝下，模型的有效天花板显著低于 dense model——SFT 阶段已消耗了大部分可恢复空间。GRPO 仅增加 |Δ|≤1pp（Section 4.3）更可能反映的是该剪枝级别下的 accuracy ceiling，而非 reward 与 accuracy 的本质性解耦。
- 论文未排除的关键混淆因素：(a) SFT 已用尽 recoverable accuracy headroom；(b) 二值 reward 信号在 f₀ > 0.5 时自然饱和（Section 3.5 自己承认 "GRPO's group-relative advantage is zero for uniform-reward batches"）；(c) 更长的 GRPO 训练是否能打破 decoupling（Appendix E 的 300 步扩展仍不充分——真实 RLVR 常训练数千步）。
- 为什么影响接收：这是论文的核心 contribution 之一（Contribution 1）。如果 decoupling 只是 SFT 接近天花板后的自然现象，那么这个 "发现" 就缺乏新颖性——它是任何充分 SFT warmup 后都会出现的预期行为。
- 建议修改方向：(1) 设计消融实验——减少 SFT 步数（如从 2 epochs 减到 0.5 epoch），在 SFT 未充分恢复时观察 GRPO 是否仍然 decouple；(2) 在不同 SFT recovery 水平（如 post-SFT acc = 40%, 50%, 60%）下测量 GRPO 的 accuracy gain，看是否存在系统性的 headroom 效应；(3) 至少在 Discussion 中承认并讨论这一替代解释。

**N2** [Critical] **RASP 的最优 α=2.0 实质是 CKA-dominant，undermines "balancing importance and diversity" 的核心叙事**
- 具体位置：Section 3.3 Eq. 5, Section 4.4, Table 1, Appendix D
- 问题：RASP 被 framed 为 "a scoring function that balances gradient importance with CKA-based representational diversity"（Abstract）。但 dose-response 分析（Section 4.4）显示最佳 α=2.0，此时 diversity term $(1-F(h))^2$ 远大于 importance term $I(h)$，使得 RASP 实际行为接近 CKA-only。Appendix D 进一步确认 α=2.0 时 peak reward 0.354，接近 CKA-only 的 0.354（Table 1 也显示两者 peak reward 和 mean reward 非常接近）。这意味着 "balancing" 叙事与最优解不一致——最优策略实际上是几乎完全依赖 diversity。
- 为什么影响接收：RASP 是论文的主要方法贡献。如果最优解是 CKA-dominant，那么 RASP 作为一个 parametric family 的贡献就退化为 "在 CKA-only 基础上加了一个几乎不起作用的 importance 项"，方法新颖性大打折扣。
- 建议修改方向：(1) 诚实地将 RASP 重新 frame 为一个 interpolation family，并强调 dose-response 分析本身是贡献（揭示 diversity >> importance 的不对称性），而非 "balancing"；(2) 讨论为什么 importance 在 CKA overlap 存在时变得冗余。

**N3** [Critical] **有效剪枝窗口仅 20–25%，30% 全面崩塌——实用价值严重受限但论文 framing 不够坦诚**
- 具体位置：Section 4.1（"All methods collapse at 30% sparsity"），Appendix K（Table 10）
- 问题：论文在 abstract 中使用 "moderate sparsity" 一词，但实际有效窗口仅为 20–25% MLP channel sparsity（Appendix K: 30% 时 accuracy 降至 4–5%，EOS rate < 6%）。对于一个 7B 模型，20–25% MLP 通道剪枝 仅约去除整体参数的约 12-15%（因为 attention 层未被剪枝），实际压缩效果非常有限。Appendix C 报告推理延迟仅减少 18%。在模型压缩文献中，这个操作范围过窄，难以证明方法的实用价值。
- 论文处理方式：30% collapse 被放在 Appendix K 中，主文仅在 Section 4.1 一句话提及。Abstract 和 Introduction 均未明确限定有效窗口的上限。
- 为什么影响接收：如果一个关于 "pruning criteria" 的研究只在非常窄的窗口内有效，读者需要在最前面就了解这个限制。将其弱化为 "moderate sparsity" 并将 collapse 分析放到 appendix，构成 framing 上的不坦诚。
- 建议修改方向：(1) Abstract 和 Introduction 中明确写出 "20–25% MLP channel sparsity (approximately 12–15% total parameter reduction)"；(2) 将 30% collapse 分析从 Appendix K 提升到主文 Discussion 中；(3) 讨论为什么结构化剪枝在 reasoning LLM 上的耐受度如此低，这本身可以是一个有价值的发现。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Warning] **Title 和叙事聚焦 RLVR/GRPO，但主要发现是 SFT dominates——存在 framing 错位**
- 具体位置：Title, Abstract, Contribution 3
- 问题：Title 为 "How Pruning Criteria Shape Post-RLVR Recovery"，叙事围绕 RLVR 展开。但 Contribution 3 明确指出 "SFT warmup as the dominant recovery mechanism"，Section 4.3 承认 GRPO 仅增加 |Δ|≤1pp。如果 SFT 才是 dominant mechanism，为什么论文不是关于 "How Pruning Criteria Shape Post-SFT Recovery"？GRPO 在这里更像是一个 afterthought 而非核心。
- 建议：要么 (a) 重新组织叙事，将 "SFT dominates, GRPO serves only as diagnostic" 作为核心 takeaway 而非第三贡献；要么 (b) 提供证据说明在何种条件下 GRPO 贡献是实质性的（如更高剪枝率、不同 reward signal）。

**W2** [Warning] **Ji et al. (2025, Self-Healing) 对比设置差异过大，论文的 "advantage vanishes" claim 过强**
- 具体位置：Section 2 (Related Work), Abstract 第 2-3 句
- 问题：Abstract 声称 "this advantage vanishes under fine-grained structured pruning"，暗示推翻了 Ji et al. 的发现。但两者设置差异巨大：Ji et al. 研究的是 unstructured pruning at 96.5% retention（仅移除 3.5% 权重），本文研究 structured MLP channel pruning at 75–80% retention（移除 20–25%）。Unstructured vs. structured 是根本不同的剪枝范式，直接对比并声称 "vanishes" 是 overclaiming。
- 建议：(1) 弱化措辞为 "does not straightforwardly extend to structured pruning"；(2) 在 Related Work 中更明确地讨论两种范式差异对恢复的影响。

**W3** [Warning] **单一架构族（Qwen2.5）且 Title 暗示泛化性**
- 具体位置：Title ("a Reasoning LLM"), Limitations (page 9)
- 问题：所有实验模型均基于 Qwen2.5 架构——主模型 DeepSeek-R1-Distill-Qwen-7B（Qwen2.5-7B 蒸馏版）、验证模型 DeepSeek-R1-Distill-Qwen-1.5B 和 Qwen2.5-Math-7B。Title 中 "a Reasoning LLM" 在技术上正确（指主模型），但给读者的印象是结论对 reasoning LLM 普遍成立。Limitations section 承认了这一点，但未讨论为什么选择了同一架构族的三个变体而非跨架构验证（如 LLaMA-based reasoning models）。
- 建议：Title 改为 "...in Qwen2.5-Family Reasoning Models" 或在 abstract 中更早明确架构限制。

**W4** [Warning] **Qwen2.5-Math-7B 的 GRPO 验证缺失**
- 具体位置：Appendix O, 脚注（page 15）
- 问题：Qwen2.5-Math-7B 仅有 SFT 阶段验证。脚注提到 "Preliminary GRPO evaluations: 48.60% (2/4500), but 83.8% of responses were truncated at 2048 tokens"。83.8% truncation rate 意味着 GRPO 结果完全不可靠。对于声称 "recovery capacity spectrum generalizes across models" 的论文，在一个验证模型上缺少完整的两阶段验证是显著空白。
- 建议：要么 (a) 完成 GRPO 验证（增加 max generation length）；要么 (b) 明确将 Qwen2.5-Math-7B 的结论限制在 SFT 阶段，并在 Limitations 中讨论。

**W5** [Warning] **Discussion 被放在 Appendix U 而非主文——削弱了论文的完整性**
- 具体位置：Section 5 (Conclusion, page 8), Appendix U (page 16)
- 问题：Section 5 仅有 ~15 行的 conclusion，没有独立的 Discussion section。关于 implications for deployment pipelines 和 GRPO diagnostics 的讨论被放在 Appendix U。对于一篇以 empirical findings 为核心的论文，Discussion 是读者理解 findings 意义的关键部分，不应放在 appendix 中。
- 建议：将 Appendix U 的核心内容（至少 "Implications" 段落）移回主文，可以压缩其他部分（如 Section 4.5 的 representational diversity evidence 部分细节可以移到 appendix）。

**W6** [Warning] **Recovery capacity spectrum 的实用价值不清晰**
- 具体位置：Section 4.2, Table 1
- 问题：论文定义了 recovery capacity 作为 GRPO 训练中的 max batch-mean reward（Section 3.5），并据此建立了方法排序（CKA-only > Random > Standard > RASP(α→1)）。但 Table 1 显示 post-SFT+GRPO 的最终 accuracy 差异很小（CKA-only 64.39% vs Standard 59.84%, 主要差异来自 SFT 阶段）。如果最终 accuracy 差异可以通过 post-SFT accuracy 直接观察到，recovery capacity spectrum 作为 GRPO-based diagnostic 的附加价值何在？论文未论证在什么场景下 GRPO probe 比直接评估 post-SFT accuracy 更有信息量。
- 建议：给出一个 GRPO diagnostic 比 SFT accuracy 更有价值的具体场景（如 GRPO 能揭示 SFT accuracy 无法区分的结构差异），或弱化此 claim。

---

## 小问题（不影响接收）

**M1** [Minor] **概念前向引用**：recovery capacity 在 Section 1（Contribution 2）中使用，但直到 Section 3.5 才正式定义。"Reward-accuracy decoupling" 在 Introduction 出现但 Section 4.3 才解释。建议在 Introduction 首次使用时给出简短定义。

**M2** [Minor] **"dose-response" 术语借用**：该术语源自药理学/毒理学，在 ML 文献中不常见。Section 4.4 使用但未解释其隐喻意义。对不熟悉该术语的读者可能造成困惑。

**M3** [Minor] **Figure 4 scatter plot 可读性差**：四个子图中的颜色/符号区分度不够，尤其在灰度打印时。建议使用不同形状标记。

**M4** [Minor] **Limitations 遗漏了 MLP-only 限制**：Limitations section 提到了单一架构族和有限 benchmark，但未提及实验仅覆盖 MLP channel pruning 而未包含 attention head pruning。鉴于 attention head pruning 在结构化剪枝文献中同等重要，这应被列为 limitation。

**M5** [Minor] **Figure 1 在 abstract 之前引用**：Page 1 的 Introduction 在 abstract 之后立即引用 Figure 1（"the dose-response curve (Figure 1)"），但这个 figure 的上下文在 Section 4.4 才充分展开，对首次阅读的读者来说跳跃较大。

---

## Questions（需要作者回答）

**Q1**: 如果将 SFT warmup 从 2 epochs 减少到 0.5 epochs，使得 post-SFT accuracy 显著低于当前水平，GRPO 阶段是否会产生更大的 accuracy gain？如果是，"reward-accuracy decoupling" 是否只是 SFT 充分恢复后的天花板效应？

**Q2**: RASP(α=2.0) 和 CKA-only 的实际剪枝决策在多大程度上重叠？即在 20% sparsity 下，两者移除的 MLP channel groups 有多少比例相同？如果重叠度很高（>80%），RASP 的独立方法贡献就非常有限。

**Q3**: 论文声称 GRPO 可以作为 "diagnostic probe"（~100 步即可），但 Table 1 中 post-SFT accuracy 已经能区分不同剪枝标准的恢复质量（CKA-only 64.39% vs Standard 59.84%）。在什么具体场景下，~100 步 GRPO probe 比直接评估 post-SFT accuracy 更有诊断价值？

**Q4**: 30% sparsity 下所有方法崩塌，accuracy 降至 4–5%（Appendix K）。是否尝试过在 25%–30% 之间更细粒度的 sparsity level（如 26%, 27%, 28%）来找到确切的 cliff 位置？这对理解为什么结构化剪枝在 reasoning model 上如此脆弱很有价值。

**Q5**: Extended GRPO training（Appendix E, 300 步）仍然没有改变 ordering 或打破 decoupling。是否考虑过训练更长（如 1000–3000 步，接近文献中常见的 RLVR 训练预算）？

---

## Missing References / 引用讨论不足

**R1**: **Zhang et al. (2025, arXiv:2504.02010) "When Reasoning Meets Compression"** — 已出现在参考文献中，但在 Related Work 主文中仅作为 bundled citation 出现，未被单独讨论。该文研究了量化、蒸馏和剪枝对 reasoning LLM 的影响，直接相关——应在 Related Work 中讨论其发现与本文的异同（特别是他们发现的 compression 对不同 reasoning 能力的差异化影响）。

**R2**: **Zhao et al. (2025, arXiv:2505.14582) "Can Pruning Improve Reasoning?"** — 已引用，但应在 Related Work 中明确区分：该文研究的是 reasoning trace pruning（Long-CoT token-level），而本文研究的是 model structure pruning。两者使用相同的 "pruning" 术语但含义完全不同，需要明确讨论以避免读者混淆。

**R3**: **Mukherjee et al. (2025, arXiv:2505.11711) "Reinforcement Learning Finetunes Small Subnetworks"** — 已引用并在 Related Work 中简要讨论。但该文发现 RL 只更新 5–30% 参数的 subnetwork——这与本文 GRPO 阶段 accuracy 增益极小的发现高度相关。建议在 Discussion 中更深入连接：如果 GRPO 只更新一个小 subnetwork，而结构化剪枝可能恰好破坏了该 subnetwork 的关键部分，这是否解释了 criterion-dependent 的 reward 差异？

---

## Overall Assessment

**评分：3.0 / 5 — Findings**

**理由**：这是一篇实验设计严谨、统计方法规范的实证研究，控制变量范式值得肯定。但存在三个核心问题削弱了其主会议接收的竞争力：

1. **新颖性不足**：最核心的 "reward-accuracy decoupling" 发现很可能是 SFT 天花板效应的 artifact，而非独立的科学发现。RASP 的方法贡献被 α=2.0 (CKA-dominant) 最优解所 undermined。

2. **Framing 问题**：论文围绕 RLVR/GRPO 组织叙事，但实际主要发现是 SFT 才是 dominant recovery mechanism。Title 和 narrative 的焦点与实际发现不匹配。

3. **实用性受限**：有效窗口仅 20–25% MLP sparsity（~12–15% 总参数压缩），30% 即全面崩塌。这个操作范围过窄，限制了方法的实际应用价值。

如果作者能 (a) 通过消融实验排除天花板效应作为 decoupling 的解释，(b) 诚实地重新 frame RASP 和叙事焦点，(c) 将有效窗口的局限性上提到主文——论文有潜力达到 3.5（Borderline Conference）。当前状态更适合 Findings track。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 700 · 2026-05-25T21:22:54.277671+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 55

## Round 55

12 recorded events


### User

_source line 701 · 2026-05-25T21:23:17.600368+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**评分：Overall 3.0/5（Findings）**，三个 Critical 问题：

1. **Reward-accuracy decoupling 可能是 SFT 天花板效应的 artifact**——SFT 已恢复大部分 accuracy，GRPO 无 headroom，需要消融实验排除
2. **RASP 最优 α=2.0 本质是 CKA-dominant**——undermines "balancing importance and diversity" 的叙事，方法新颖性打折扣
3. **有效窗口仅 20–25% MLP sparsity，30% 全面崩塌**——Abstract 用 "moderate sparsity" 模糊处理，实际压缩比约 12–15%，实用价值受限

另有 6 个 Warning（Title/叙事与 SFT-dominant 发现的错位、Ji et al. 对比 overclaiming、单一架构族、Math-7B GRPO 缺失、Discussion 被放 Appendix、spectrum 实用价值不清）和 5 个 Minor 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-25T21:23:36.647541+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-25T21:23:36.698176+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-25T21:23:41.164193+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-25T21:23:41.214773+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-25T21:23:44.275174+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-25T21:23:45.380136+00:00_

{"result":"# 项目 recovery_aware_struct_prune 概况\n\n## 实验状态 (462 个)\n\n- **grpo_stage2_rasp_20_v2**: DONE (negative) — \n- **grpo_stage2_standard_20**: DONE (killed) — \n- **grpo_stage2_rasp_20**: DONE (killed) — \n- **sft_standard_20**: DONE (success) — \n- **sft_rasp_20**: DONE (success) — \n- **grpo_rasp_20_4096**: DONE (failed) — \n- **grpo_standard_20_4096**: DONE (negative) — \n- **grpo_standard_20_fast**: DONE (negative) — \n- **grpo_rasp_20_fast**: DONE (negative) — \n- **mvp_rasp_pipeline_v4**: PREPARING — \n- **grpo_standard_20**: DONE (killed) — \n- **grpo_rasp_20**: DONE (killed) — \n- **mvp_rasp_pipeline_v3**: DONE (negative) — \n- **mvp_rasp_pipeline_v2**: DONE (failed) — \n- **mvp_rasp_pipeline**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- floor_ablation_0p3_cka_only_20: Floor ratio ablation: lowering the MLP floor from 0.4 to 0.3 allows more aggressive pruning of unimportant layers while CKA-only criterion preserves critical structure. If floor=0.3 maintains GSM8K accuracy within 2pp of floor=0.4 baseline, it demonstrates robustness of CKA-guided pruning to floor choice.（已分配 ? GPU:?，等待提交）\n- floor_ablation_0p5_cka_only_20: Floor ratio ablation: raising the MLP floor from 0.4 to 0.5 constrains pruning to be more conservative. If floor=0.5 improves GSM8K accuracy over floor=0.4, it suggests CKA-only criterion benefits from a higher minimum layer size. Maps the sensitivity curve of floor parameter on recovery quality.（已分配 ? GPU:?，等待提交）\n- …另有 38 项\n\n## 近期结论\n- **eval_gsm8k_grpo_alpha4_20_v2** (killed): α=4.0 GRPO maintains reward 0.15-0.26 (vs α=1.0 collapse to ~0.008), predicting GSM8K accuracy significantly above α=1.0 baseline. v1 timed out at 774/1319 showing 62.93% interim — full eval needed to confirm α-dependent collapse hypothesis. ← 基于 eval_gsm8k_grpo_alpha4_20\n\n## 趋势\n成功 273 / 负向 23 / 失败 84 / 共 422\naccuracy: 0.268 →（近 3 次 success）\navg_response_length: 1110.462 ↑（近 3
…[truncated 1815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-25T21:24:16.950430+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-25T21:24:17.151462+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-25T21:24:17.151887+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-25T21:24:17.252602+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:15:33.342911+00:00\", \"completed_at\": \"2026-05-25T21:15:37.175385+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 12am (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 712 · 2026-05-25T21:24:37.905597+00:00_

**Reviewer 2 初审收到。** 评分 3.0/5，3 个 Critical + 6 个 Warning。

当前状态：
- Reviewer 1：等待中（未收到初审结果）
- Reviewer 2：✅ 已完成初审
- 外部审稿：未请求
- 视觉审查：❌ Agent 因配额限制未能执行（rate limit hit）

**下一步**：收到 Reviewer 1 的初审结果后，进入交叉分享阶段——将两位 Reviewer 的完整审稿原文互相转发，要求逐条回应 `[AGREE]` / `[REBUT]`，再进入报告合成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 56

## Round 56

8 recorded events


### User

_source line 713 · 2026-05-25T21:25:08.205872+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（Round 1）：方法严谨性 + 实验设计

### 总体评分
**Overall**: 3.0 (Findings)
**Confidence**: 4/5
**一句话总结**: 受控实验设计和 reward-accuracy decoupling 发现有价值，但核心方法 RASP 被自身消融实验否定，关键实验存在未解决的控制变量问题。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | Random baseline 的 max_completion_length 不一致违反受控设计；RASP α 变体仅单 seed；TOST ε=2pp 选择存在 post-hoc 嫌疑 |
| Excitement | 3/5 | Decoupling 发现新颖，但 RASP 被 CKA-only（其极端情况）超越，方法 novelty 弱 |
| Reproducibility | 4/5 | 超参数详尽、算法伪代码清晰、代码已匿名开源 |

---

### Must-Fix 问题

**N1** [critical] RASP 作为方法贡献被自身消融否定
- 位置：Eq.5 (Section 3.3), Table 5 (Appendix D), Table 2
- RASP 在默认 α=1.0 时 reward collapse（Table 1: Peak Rew 0.061，四方法最差）；CKA-only（Eq.6, α→∞ 极限，完全忽略 importance）在 recovery capacity spectrum 排第一（Peak Rew 0.354）。RASP α=2.0 达 66.11%（+1.72pp over CKA-only）但为单 seed。论文最终推荐 CKA-only 而非 RASP——当提出的方法被其自身消融特例超越时，方法贡献不成立。
- 建议：重新定位为 empirical study；补充 additive baseline β·I(h)+(1-β)·(1-F(h)) 对比。

**N2** [critical] 乘法形式 I(h)=0 退化行为未与加法替代对比
- 位置：Eq.5, "The multiplicative form ensures zero-importance structures are always pruned (S=0)"
- 论文将 I(h)=0⟹S=0 描述为 feature，但这恰恰是 RASP 败给 CKA-only 的原因。加法形式不存在此退化。α=1.0 collapse 可能主要源于此数值 artifact 而非 tradeoff 本质。缺少加法对照无法区分两个解释。
- 建议：跑 additive combination baseline（成本低）。

**N3** [critical] Random baseline max_completion_length 不一致违反受控实验设计
- 位置：Section 4.1, Table 3 (Appendix A)
- Random 的 GRPO max_completion_length=512 vs 其他方法 1024。论文自称 "we hold everything else constant" 但此处不一致。Random 是唯一 uninformed baseline，其表现直接影响 spectrum 解读。
- 建议：使用 1024 token 重跑 Random GRPO（成本低）。

**N4** [critical] RASP α 变体全部单 seed，dose-response 曲线不可靠
- 位置：Table 5, Table 11
- CKA-only/Standard/Random 各 3 seeds，但 RASP 全部 α 值（0.5-4.0）均单 seed。Inverted-U 结论完全基于单次运行。α=2.0 的 66.11% vs CKA-only 64.39±0.19% 的 1.72pp 差距，RASP 方差未知。
- 建议：至少 α=2.0 和 α=1.0 各跑 3 seeds。

### Should-Fix 问题

**W1** [warning] TOST ε=2pp 缺乏 a priori justification
- 位置：Appendix T, Section 4.3
- Cross-seed σ 衡量 training noise 不是 practical significance。7/8 pass（Standard seed 456 borderline p=0.069）。需先验论证 2pp 的实际意义。

**W2** [warning] 15% sparsity 下 GRPO 放大 CKA 优势（+1.51pp），Standard Δ=-0.93pp 接近 1pp 边界
- 位置：Section 4.3, Table cross_sparsity
- 论文标题暗示 decoupling 是普遍规律，但实际仅在 20-25% fine-grained MLP sparsity 下成立。

**W3** [warning] 25% sparsity 单 seed，Standard Δ=+0.99pp 恰在 1pp 边界
- 位置：Table cross_sparsity
- 多 seed 可能超过 1pp 阈值。

**W4** [warning] 300-step extended training 未报告 step-by-step accuracy 曲线
- 位置：Section 4.5, Appendix E
- 仅报告终值（step 300），缺少 100-300 步间的 accuracy 变化趋势。

**W5** [warning] Limitations 关于 Random seed 的表述与正文矛盾
- Limitations 写 "RASP α variants and Random use single GRPO seeds" 但 Random 实际有 3 seeds（Section 4.1, Table 11）。

**W6** [warning] Calibration M=512 的 importance score 稳定性未验证
- Table 8 验证了 CKA ranking 稳定性，但未验证 importance score I(h) 的 calibration sensitivity。

### 主要优势

- **S1**: 受控实验设计理念优秀——isolation 设计在 pruning 文献中罕见
- **S2**: Reward-accuracy decoupling 是 genuinely surprising 的发现
- **S3**: f₀/gradient norm/KL 等多维训练动态分析工具有价值
- **S4**: 跨模型/跨尺度/跨 benchmark 验证展示了系统性 validation 意识
- **S5**: 写作清晰，Figure 2 有效传达实验设计

### Questions

Q1: α=1.0 collapse 是乘法 I(h)≈0 退化还是 diversity-importance 平衡失败？additive baseline 结果会如何？
Q2: 为什么不统一 Random 的 max_completion_length 为 1024？
Q3: 如果 α=2.0 补跑 3 seeds 仍优于 CKA-only，结论是否需根本性修改？
Q4: 15% sparsity 下 Standard 更多 seeds 可能超过 1pp 吗？
Q5: Extended training 中间步数有无评估 accuracy？
Q6: Floor ablation 仅对 CKA-only 做了，Standard 在不同 τ 下表现如何？

### Missing References
- Molchanov et al. (2019) "Importance Estimation for Neural Network Pruning"——加法形式多标准组合先例

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-25T21:25:21.429480+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-25T21:25:21.436895+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 7
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-25T21:25:36.981642+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见，对每个点标注 `[AGREE]` 或 `[REBUT]`（附理由）。\n\n---\n\n**Reviewer 2 评分：Overall 3.0/5（Findings）**\n\n### Critical 问题\n\n**C1**: Reward-accuracy decoupling 可能是 SFT 天花板效应的 artifact——SFT 已恢复大部分 accuracy，GRPO 无 headroom，需要消融实验排除\n\n**C2**: RASP 最优 α=2.0 本质是 CKA-dominant——undermines \"balancing importance and diversity\" 的叙事，方法新颖性打折扣\n\n**C3**: 有效窗口仅 20–25% MLP sparsity，30% 全面崩塌——Abstract 用 \"moderate sparsity\" 模糊处理，实际压缩比约 12–15%，实用价值受限\n\n### Warning 问题\n\n**W1**: Title/叙事与 SFT-dominant 发现的错位\n**W2**: Ji et al. 对比 overclaiming\n**W3**: 单一架构族（Qwen2.5 系列）\n**W4**: Math-7B GRPO 缺失\n**W5**: Discussion 被放 Appendix\n**W6**: Spectrum 实用价值不清\n\n### Minor 问题（5 个）\n涉及格式、表述等细节。\n\n---\n\n请对 C1-C3 和 W1-W6 逐条给出 [AGREE] 或 [REBUT]，重点关注：\n1. C1 的 SFT 天花板解释与你发现的 RASP 方法问题之间的关系\n2. C3 的实用价值限制是否构成 reject 级别的问题",
  "reviewer_id": "1",
  "project": "recovery_aware_struct_prune",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见，对每个点标注 `[AGREE]` 或 `[REBUT]`（附理由）。\n\n---\n\n**Reviewer 2 评分：Overall 3.0/5（Findings）**\n\n### Critical 问题\n\n**C1**: Reward-accuracy decoupling 可能是 SFT 天花板效应的 artifact——SFT 已恢复大部分 accuracy，GRPO 无 headroom，需要消融实验排除\n\n**C2**: RASP 最优 α=2.0 本质是 CKA-dominant——undermines \"balancing importance and diversity\" 的叙事，方法新颖性打折扣\n\n**C3**: 有效窗口仅 20–25% MLP sparsity，30% 全面崩塌——Abstract 用 \"moderate sparsity\" 模糊处理，实际压缩比约 12–15%，实用价值受限\n\n### Warning 问题\n\n**W1**: Title/叙事与 SFT-dominant 发现的错位\n**W2**: Ji et al. 对比 overclaiming\n**W3**: 单一架构族（Qwen2.5 系列）\n**W4**: Math-7B GRPO 缺失\n**W5**: Discussion 被放 Appendix\n**W6**: Spectrum 实用价值不清\n\n### Minor 问题（5 个）\n涉及格式、表述等细节。\n\n---\n\n请对 C1-C3 和 W1-W6 逐条给出 [AGREE] 或 [REBUT]，重点关注：\n1. C1 的 SFT 天花板解释与你发现的 RASP 方法问题之间的关系\n2. C3 的实用价值限制是否构成 reject 级别的问题",
    "reviewer_id": "1",
    "project": "recovery_aware_struct_prune",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-25T21:25:47.029049+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 10047
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-25T21:25:47.430954+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见，对每个点标注 `[AGREE]` 或 `[REBUT]`（附理由）。\n\n---\n\n**Reviewer 1 评分：Overall 3.0/5（Findings）**\n\n### Critical 问题\n\n**N1**: RASP 作为方法贡献被自身消融否定——CKA-only（α→∞ 极限）在 recovery capacity spectrum 排第一（Peak Rew 0.354），RASP 默认 α=1.0 reward collapse（Peak Rew 0.061）。论文最终推荐 CKA-only 而非 RASP，方法贡献不成立。\n\n**N2**: 乘法形式 I(h)=0 退化行为未与加法替代对比——I(h)=0⟹S=0 是 RASP 败给 CKA-only 的原因，加法形式不存在此退化。缺少加法对照无法区分乘法 artifact 与 tradeoff 本质。\n\n**N3**: Random baseline max_completion_length 不一致违反受控实验设计——Random GRPO 用 512 vs 其他 1024，论文自称 \"hold everything else constant\" 但此处不一致。\n\n**N4**: RASP α 变体全部单 seed，dose-response 曲线不可靠——α=2.0 的 66.11% vs CKA-only 64.39±0.19% 的 1.72pp 差距在方差未知时不可信。\n\n### Warning 问题\n\n**W1**: TOST ε=2pp 缺乏 a priori justification\n**W2**: 15% sparsity 下 GRPO 放大 CKA 优势（+1.51pp），Standard Δ=-0.93pp 接近 1pp 边界\n**W3**: 25% sparsity 单 seed，Standard Δ=+0.99pp 恰在 1pp 边界\n**W4**: 300-step extended training 未报告 step-by-step accuracy 曲线\n**W5**: Limitations 关于 Random seed 的表述与正文矛盾\n**W6**: Calibration M=512 importance score 稳定性未验证\n\n### Questions\n\nQ1: α=1.0 collapse 是乘法 I(h)≈0 退化还是 diversity-importance 平衡失败？\nQ2: 为什么不统一 Random 的 max_completion_length 为 1024？\nQ3: 如果 α=2.0 补跑 3 seeds 仍优于 CKA-only，结论是否需根本性修改？\n\n---\n\n请对 N1-N4 和 W1-W6 逐条给出 [AGREE] 或 [REBUT]，重点关注：\n1. N1/N2 与你的 C2（α=2.0 本质 CKA-dominant）是否指向同一根本问题\n2. N3 的控制变量问题对你的 spectrum 有效窗口判断有无影响\n3. N4 的单 seed 问题是否加剧了你对方法新颖性的质疑",
  "reviewer_id": "2",
  "project": "recovery_aware_struct_prune",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见，对每个点标注 `[AGREE]` 或 `[REBUT]`（附理由）。\n\n---\n\n**Reviewer 1 评分：Overall 3.0/5（Findings）**\n\n### Critical 问题\n\n**N1**: RASP 作为方法贡献被自身消融否定——CKA-only（α→∞ 极限）在 recovery capacity spectrum 排第一（Peak Rew 0.354），RASP 默认 α=1.0 reward collapse（Peak Rew 0.061）。论文最终推荐 CKA-only 而非 RASP，方法贡献不成立。\n\n**N2**: 乘法形式 I(h)=0 退化行为未与加法替代对比——I(h)=0⟹S=0 是 RASP 败给 CKA-only 的原因，加法形式不存在此退化。缺少加法对照无法区分乘法 artifact 与 tradeoff 本质。\n\n**N3**: Random baseline max_completion_length 不一致违反受控实验设计——Random GRPO 用 512 vs 其他 1024，论文自称 \"hold everything else constant\" 但此处不一致。\n\n**N4**: RASP α 变体全部单 seed，dose-response 曲线不可靠——α=2.0 的 66.11% vs CKA-only 64.39±0.19% 的 1.72pp 差距在方差未知时不可信。\n\n### Warning 问题\n\n**W1**: TOST ε=2pp 缺乏 a priori justification\n**W2**: 15% sparsity 下 GRPO 放大 CKA 优势（+1.51pp），Standard Δ=-0.93pp 接近 1pp 边界\n**W3**: 25% sparsity 单 seed，Standard Δ=+0.99pp 恰在 1pp 边界\n**W4**: 300-step extended training 未报告 step-by-step accuracy 曲线\n**W5**: Limitations 关于 Random seed 的表述与正文矛盾\n**W6**: Calibration M=512 importance score 稳定性未验证\n\n### Questions\n\nQ1: α=1.0 collapse 是乘法 I(h)≈0 退化还是 diversity-importance 平衡失败？\nQ2: 为什么不统一 Random 的 max_completion_length 为 1024？\nQ3: 如果 α=2.0 补跑 3 seeds 仍优于 CKA-only，结论是否需根本性修改？\n\n---\n\n请对 N1-N4 和 W1-W6 逐条给出 [AGREE] 或 [REBUT]，重点关注：\n1. N1/N2 与你的 C2（α=2.0 本质 CKA-dominant）是否指向同一根本问题\n2. N3 的控制变量问题对你的 spectrum 有效窗口判断有无影响\n3. N4 的单 seed 问题是否加剧了你对方法新颖性的质疑",
    "reviewer_id": "2",
    "project": "recovery_aware_struct_prune",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-25T21:25:48.745012+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1314
}
```

</details>

---


### Assistant

_source line 720 · 2026-05-25T21:25:54.211491+00:00_

交叉分享已派发。两位 Reviewer 正在逐条回应对方意见，等待交叉回应结果返回后判断收敛性。

当前状态汇总：
- **内部审稿**：Round 1 初审完成，交叉分享进行中
- **外部审稿**：未请求（项目配置未启用）
- **视觉审查**：Agent 因额度耗尽未执行（将在报告中标注）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 57

## Round 57

2 recorded events


### User

_source line 721 · 2026-05-25T21:25:56.721982+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：给出 **Overall 3.0 (Findings)**。核心问题有四个 critical：(1) RASP 被自身消融特例 CKA-only 超越，方法贡献不成立；(2) 乘法形式的 I(h)=0 退化行为缺少加法替代对比；(3) Random baseline 的 max_completion_length 不一致（512 vs 1024）违反受控实验设计；(4) RASP 全部 α 变体仅单 seed，dose-response 曲线不可靠。此外有 6 个 warning 级问题涉及 TOST ε 选择、decoupling 普适性边界、25% sparsity 单 seed 等。论文的优势在于受控实验设计理念、reward-accuracy decoupling 的新颖发现、以及多维训练动态诊断工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 722 · 2026-05-25T21:26:07.075479+00:00_

Reviewer 1 交叉回应已收到，维持 3.0 (Findings)。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 58

## Round 58

14 recorded events


### User

_source line 723 · 2026-05-25T21:27:17.748719+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应：逐条回应 Reviewer 1 的审稿意见

---

## Critical 问题

**[AGREE] R1-N1: RASP 方法贡献被自身消融否定**

同意，且与我的 N2 指向同一根本问题。我的 N2 从 "α=2.0 最优意味着 CKA-dominant，undermines balancing 叙事" 角度论述，R1-N1 从 "论文最终推荐 CKA-only 而非 RASP" 角度论述——本质一致：RASP 作为独立方法贡献不成立。

补充一点 R1 未提及的：Table 1 数据显示 RASP(α=2.0) Peak Rew = 0.354，CKA-only Peak Rew = 0.354，两者完全相同。这比 R1 的论证更直接——在最优配置下 RASP 与 CKA-only 的 recovery capacity 指标无差异，RASP 框架的额外 parametric 复杂性没有带来任何增益。如果作者声称 α=2.0 时 accuracy (66.11%) 优于 CKA-only (64.39%)，这个 1.72pp 差异恰好落在 R1-N4 指出的单 seed 不可信区间内。

**[AGREE] R1-N2: 乘法形式退化行为未与加法替代对比**

同意，这是一个我未覆盖的有价值技术点。RASP 的乘法形式 $S_{RASP}(h) = I(h) \times (1-F(h))^\alpha$（Eq. 5）意味着 $I(h)=0$ 的结构无论 diversity 多高都被零化。加法替代（如 $S = \beta \cdot I(h) + (1-\beta) \cdot (1-F(h))$）不存在此退化，是合理的 ablation 对照。缺少这个对照，无法判断 α=1.0 collapse（Table 1, Peak Rew 0.061）是乘法形式的 pathological artifact 还是 importance-diversity tradeoff 在该配置下的真实行为。这一遗漏与我的 N2 构成互补——我关注 α=2.0 端（CKA-dominant），R1 关注 α=1.0 端（collapse），合在一起说明 RASP 的整个 parametric 空间都有问题：一端退化，另一端等价于 CKA-only。

**[AGREE with nuance] R1-N3: Random baseline max_completion_length 不一致**

同意这违反了受控实验设计原则，论文自称 "hold everything else constant"（Section 3）但此处不一致。但我对严重程度的评估略低于 R1：

- Random 是四种方法中最弱的 baseline，用于 "控制 informative scoring 的效应"
- max_completion_length 512 vs 1024 可能导致 Random 的 GRPO reward 被低估（因为 reasoning trace 更容易截断），但 Random 在 recovery capacity spectrum 中已经排在 Standard 之上（Peak Rew 0.125 vs 0.060, Table 1），如果统一到 1024 可能进一步拉大这个差距
- 关键影响：如果 Random 在 1024 设置下 accuracy 和 reward 都更高，那 Standard（唯一一个低于 Random 的 informative method）的表现就更显尴尬，这反而强化了论文关于 "importance-only 不如 diversity-preserving" 的结论

所以不一致是真实问题，应报告并修复，但不太可能翻转核心 spectrum ordering。对我的有效窗口判断（N3）无直接影响——30% collapse 是所有方法共享的架构限制，与 Random 的超参数无关。

**[AGREE] R1-N4: RASP α 变体全部单 seed，dose-response 曲线不可靠**

强烈同意，且与我的 N2 直接相关。我的 N2 指出 "α=2.0 CKA-dominant undermines balancing narrative"，R1-N4 进一步指出这个 α=2.0 的优势本身在统计上就不可信。两个问题叠加：

1. (我的 N2) 即使 α=2.0 真的更好，它也只是 CKA-only 的近似
2. (R1-N4) α=2.0 是否真的更好，在单 seed 下无法确认

Appendix J 报告 CKA-only 的 3-seed 标准差为 0.19pp（Section 4.5）。α=2.0 的 66.11% vs CKA-only 64.39% 差距为 1.72pp，看似显著，但 α=2.0 自身方差未知。如果 α=2.0 的标准差与 CKA-only 相当（~0.19pp），则 1.72pp 可能显著；但如果 α=2.0 方差更大（考虑到 RASP 在不同 α 下表现差异巨大——从 collapse 到 66%——variance 可能更高），则 1.72pp 不可信。

这加剧了我对方法新颖性的质疑：RASP 不仅在最优配置下等价于 CKA-only（我的 N2），而且连 "是否真的优于 CKA-only" 这个前提都未被统计验证（R1-N4）。

---

## Warning 问题

**[AGREE] R1-W1: TOST ε=2pp 缺乏 a priori justification**

同意。TOST 的 equivalence margin 是结论成立与否的关键参数。ε=2pp 对于 GSM8K（~1300 题，准确率 60-65%）意味着约 26 题的差异，这在教育评测中算实质性差异还是噪音？论文选择 2pp 但未引用文献或给出统计 power 分析来证明这个选择。如果 ε=1pp，部分 "等价" 结论可能不成立。

**[AGREE] R1-W2: 15% sparsity 下 CKA-only 优势被 GRPO 放大**

同意这削弱了 "SFT+GRPO 抹平差异" 的叙事。Appendix M 的 15% 数据（CKA-only vs Standard: +1.51pp post-GRPO，而 post-SFT 差距更小）表明 GRPO 在低剪枝率下并非纯粹的 diagnostic——它可以放大方法间差异。这与我的 N1（decoupling 可能是天花板效应）一致：在 15% sparsity 下 accuracy headroom 更大，GRPO 开始产生实质性差异，进一步暗示 20% 下的 "decoupling" 是 headroom 耗尽的 artifact。

**[REBUT] R1-W3: 25% sparsity 单 seed，Standard Δ=+0.99pp 恰在 1pp 边界**

部分反驳。R1 的担忧合理——单 seed 下 0.99pp 恰在边界确实不够稳健。但这个数据点不是论文核心 claim 的支撑：25% sparsity 主要作为 "collapse 前的边界条件" 出现（Section 4.1, "All methods collapse at 30%"），而非核心 spectrum 分析的基础。论文的核心 spectrum 结论建立在 20% sparsity 数据上（Table 1, 3 seeds for CKA-only/Standard/Random）。25% 数据的不确定性是真实问题，但严重程度低于 R1 隐含的判断。

**[AGREE] R1-W4: 300-step extended training 未报告 step-by-step accuracy 曲线**

同意。Appendix E 只报告了 100 步和 300 步的 checkpoint accuracy，但没有中间步骤的 accuracy trajectory。这是一个遗漏——如果 CKA-only 在 150-200 步时 accuracy 仍在上升，而 Standard 在 100 步后就 plateau 了，这将是非常有信息量的。更重要的是，300 步仍然远少于 RLVR 文献中常见的训练预算（通常 1000-5000 步），这与我的 Q5 一致。

**[AGREE] R1-W5: Limitations 关于 Random seed 的表述与正文矛盾**

同意这是写作问题。如果 Limitations 说 "RASP α variants and Random use single GRPO seeds" 但 Appendix L (Table 11) 显示 Random 有 3 seeds（42, 123, 456），则存在矛盾。这类不一致会降低审稿人对其他声称的信任度。

**[REBUT] R1-W6: Calibration M=512 importance score 稳定性未验证**

部分反驳。R1 关心 M=512 样本量是否足够计算稳定的 importance score。但 Appendix H（Table 8）报告了 CKA scoring 在不同 calibration set sizes（256/512/1024）下的 Spearman ρ 稳定性（ρ=0.964-0.979），虽然这只验证了 CKA ranking 的稳定性而非 importance score 的稳定性，但暗示 512 样本量对 structure ranking 的计算已经足够稳定。更直接的反驳：importance score 基于 Taylor expansion（一阶梯度×激活），这在剪枝文献中是标准做法，M=512 远超 LLM-Pruner（Ma et al., 2023）使用的 calibration 规模。

---

## 综合评估

R1 的审稿意见整体高质量，与我的评审高度互补：

| 问题域 | R1 视角 | R2 视角 | 关系 |
|--------|---------|---------|------|
| RASP 贡献 | N1: 推荐 CKA-only 否定 RASP | N2: α=2.0 CKA-dominant 否定 balancing | 同一问题的两面 |
| 乘法退化 | N2: 缺加法对照 | 未覆盖 | R1 独有贡献 |
| 实验控制 | N3: Random 超参不一致 | 未覆盖 | R1 独有贡献 |
| 统计可靠性 | N4: α 变体单 seed | Q2: RASP vs CKA-only 重叠度 | 互补 |
| Decoupling 本质 | 未深入讨论 | N1: SFT 天花板效应 | R2 独有贡献 |
| 有效窗口 | 未直接讨论 | N3: 20-25% 过窄 | R2 独有贡献 |
| Framing 错位 | 未直接讨论 | W1: Title vs 实际发现 | R2 独有贡献 |

两份审稿合在一起对 RASP 方法贡献形成了全面否定：从 α→0（Standard 退化）到 α=1.0（乘法 collapse）到 α=2.0（CKA-only 等价且单 seed 不可信）到 α→∞（CKA-only 本身）。RASP 作为 parametric family 在整个参数空间都不优于其端点。

我维持 Overall 3.0（Findings）评分。R1 的技术细节问题（N2 乘法 vs 加法、N3 超参不一致）加强了我对方法贡献不足的判断，但未改变总体评估——论文的控制变量实验设计和实证发现（尤其 SFT dominance 和 criterion-dependent training dynamics）仍然有 Findings 级别的价值。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-25T21:27:37.383033+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-25T21:27:37.438980+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-25T21:27:40.436328+00:00_

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
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
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

_source line 727 · 2026-05-25T21:27:40.575215+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "ToolSearch",
  "elapsed_ms": 138
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-25T21:27:43.769720+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-25T21:27:43.870505+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-25T21:27:48.337445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-25T21:27:48.639740+00:00_

1	
2	# ============================================================
3	# Round 1-3 Issues — All Resolved
4	# ============================================================
5	
6	- id: "R1-C1"
7	  summary: "CKA-recovery link 仅相关性, 无因果干预"
8	  category: method
9	  severity: critical
10	  status: resolved
11	  first_raised_round: 1
12	  last_seen_round: 3
13	  resolution: "Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证"
14	  resolution_round: 3
15	
16	- id: "R1-C2"
17	  summary: "Single-seed GRPO 无统计显著性"
18	  category: experiment
19	  severity: critical
20	  status: resolved
21	  first_raised_round: 1
22	  last_seen_round: 3
23	  resolution: "3-seed GRPO CKA-only, Welch's t-test p=0.0009"
24	  resolution_round: 3
25	
26	- id: "R1-C3"
27	  summary: "仅 GSM8K 单基准"
28	  category: experiment
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 1
32	  last_seen_round: 3
33	  resolution: "MATH-500 OOD 验证 + MBPP 代码基准"
34	  resolution_round: 3
35	
36	- id: "R1-W1"
37	  summary: "Title overclaim 'determines'"
38	  category: framing
39	  severity: warning
40	  status: resolved
41	  first_raised_round: 1
42	  last_seen_round: 3
43	  resolution: "Title 改为 'shapes'"
44	  resolution_round: 3
45	
46	- id: "R1-W2"
47	  summary: "Abstract 'universally determines' overclaim"
48	  category: framing
49	  severity: warning
50	  status: resolved
51	  first_raised_round: 1
52	  last_seen_round: 3
53	  resolution: "改为 'significantly shapes'"
54	  resolution_round: 3
55	
56	- id: "R1-W3"
57	  summary: "仅 DeepSeek-R1-7B 单模型"
58	  category: experiment
59	  severity: warning
60	  status: resolved
61	  first_raised_round: 1
62	  last_seen_round: 3
63	  resolution: "Qwen2.5-Math-7B cross-arch + 1.5B cross-scale"
64	  resolution_round: 3
65	
66	- id: "R1-M1"
67	  summary: "GRPO 超参未报告"
68	  category: experiment
69	  severity: info
70	  status: resolved
71	  first_raised_round: 1
72	  last_seen_round: 3
73	  resolution: "Appendix 完整超参表"
74	  resolution_round: 3
75	
76	- id: "R1-M2"
77	  sum
…[truncated 33237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-25T21:32:02.910376+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "issues_yaml": "# ============================================================\n# Round 1-3 Issues — All Resolved\n# ============================================================\n\n- id: \"R1-C1\"\n  summary: \"CKA-recovery link 仅相关性, 无因果干预\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Single-seed GRPO 无统计显著性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"3-seed GRPO CKA-only, Welch's t-test p=0.0009\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"仅 GSM8K 单基准\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"MATH-500 OOD 验证 + MBPP 代码基准\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"Title overclaim 'determines'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Title 改为 'shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"Abstract 'universally determines' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"改为 'significantly shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"仅 DeepSeek-R1-7B 单模型\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Qwen2.5-Math-7B cross-arch + 1.5B cross-scale\"\n  resolution_round: 3\n\n- id: \"R1-M1\"\n  summary: \"GRPO 超参未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Appendix 完整超参表\"\n  resolution_round: 3\n\n- id: \"R1-M2\"\n  summary: \"Table 1 缺 Random baseline\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Table 1 加入 Random 行\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C1\"\n  summary: \"GRPO 准确率几乎不变,为何要用 GRPO\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Dual-layer reframe: SFT(accuracy) + GRPO(reward signal)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C2\"\n  summary: \"Cross-architecture 仅 SFT 验证,GRPO 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"1.5B GRPO 补充 + Abstract 区分表述\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W1\"\n  summary: \"SFT recovery 被忽视,过度聚焦 GRPO\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注解释 SFT catastrophic forgetting\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W2\"\n  summary: \"Qwen-Math 跨架构验证仅 SFT，Abstract overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 区分 GRPO(DeepSeek) vs SFT(Qwen-Math)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W3\"\n  summary: \"GRPO 准确率改变 < 1pp — 实际效用存疑\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"300-step accuracy + reward-accuracy decoupling 论证\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W4\"\n  summary: \"RASP/Random 仍为单种子\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注透明标注 + Limitations 披露\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W5\"\n  summary: \"Random baseline SFT/GRPO Acc 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Table 2 脚注标注 checkpoint not preserved\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W6\"\n  summary: \"正文 5 处 'determines' 残留\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"全部替换为 shapes/significantly influences\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M1\"\n  summary: \"GRPO batch size / rollouts 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M2\"\n  summary: \"SFT lr/batch/optimizer 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-VIS-1\"\n  summary: \"末页 Figure 6 仅占 30%，70% 空白\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 重排\"\n  resolution_round: 3\n\n- id: \"R2-VIS-2\"\n  summary: \"Appendix page 12 过度拥挤\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 拆分到多页\"\n  resolution_round: 3\n\n- id: \"R3-S5\"\n  summary: \"Qwen-Math 'strongest evidence' 措辞仍略强\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"strongest → additional evidence in §4.5\"\n  resolution_round: 3\n\n- id: \"R3-M2\"\n  summary: \"300-step accuracy 未标注 seed\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"(single seed) 标注已添加到 §4.3\"\n  resolution_round: 3\n\n- id: \"R3-M3\"\n  summary: \"无代码/checkpoint 发布声明\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Code and checkpoints release statement in Conclusion\"\n  resolution_round: 3\n\n# ============================================================\n# Round 5-7 Issues — Carried forward\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Reward-accuracy decoupling 叙事薄弱（GRPO 增量 <1pp，可能是 SFT 天花板效应 artifact）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。SYSTEMIC_ISSUE #1 核心。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W4 和 R2-W2 再次提出，增加新角度：需区分 format compliance vs reasoning quality。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-N3 升级为 critical。R1 完全同意。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 升为本文最关键问题（Critical），R1 维持 Warning。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-C1 再次提出：SFT 已恢复大部分 accuracy（~60pp），GRPO 无 headroom。R1 虽未直接提但在交叉回应中认为 15% sparsity 数据（GRPO amplifies gap）支持天花板解释。连续 5 轮 Critical 未解决。\"\n  action_items:\n    - round: 5\n      action: \"D098 dual-layer reframe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 9\n      action: \"需要消融实验：在 SFT 恢复不充分的条件下（如更少 SFT steps 或更高 sparsity）验证 GRPO 是否产生 accuracy 差异\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"Cross-architecture/scale 泛化严重不足，所有模型共享 Qwen2.5 base\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前不可行（需全 pipeline ~50h GPU）。但 1.5B GRPO 数据已有。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识。Appendix O 'Cross-Architecture Validation' 标题误导。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识 Critical。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W3 再次提出单一架构族（Qwen2.5 系列）。R1 未直接复述但在 Q6 中暗示 Standard 在不同设置下行为未知。连续 5 轮 Critical。\"\n  action_items:\n    - round: 8\n      action: \"Title 改为更精确范围或补充至少一个非 Qwen 架构 GRPO 结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"RASP 单 seed 验证不足——方法贡献可靠性存疑\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"核心比较 CKA vs Standard 有 3-seed p=0.0009。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 升级为 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识 critical。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Director 判定 Critical。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N4 再次明确提出：全部 α 变体（0.5-4.0）均单 seed，dose-response inverted-U 不可靠。R2 交叉回应强烈同意——α=2.0 方差未知时 1.72pp 不可信。连续 5 轮 Critical 未解决。\"\n  action_items:\n    - round: 9\n      action: \"至少 α=2.0 和 α=1.0 各跑 3 seeds；如无法完成则降级 RASP 为 exploratory\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"因果语言系统性过强——'causal driver' 超出 quasi-experimental 证据\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"SYSTEMIC_ISSUE #2 成员。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N3 详细论证。R2 补充 metrics diversity 不足。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未单独复现为独立问题。可能已部分修复（论文已改用 'shapes'）。\"\n  action_items:\n    - round: 7\n      action: \"全文语言审计：'causal driver' → 'key determinant'；decoupling claims 加限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Per-layer capacity floor (40%) 未消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前不可行（需全 pipeline ~50h GPU）。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W3 再次提出。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-Q6 问到 Floor ablation 仅对 CKA-only 做了，Standard 在不同 τ 下表现未知。\"\n  action_items:\n    - round: 5\n      action: \"Limitations 讨论 + rebuttal 论点准备\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Floor ablation τ∈{0.3,0.4,0.5,0.6} experiments running; appendix table added\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"α dose-response 存在 generation length 混杂变量\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"高 ROI 实验。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出。R2-W1 扩展为 κ 消融缺失。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"升级为 critical。α=1.0 用 1024 tokens，其他用 512 tokens。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 在 W2（Random baseline）中再次确认。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N3 再次明确提出：Random GRPO 用 512 vs 其他 1024，违反受控设计。R2 交叉回应 AGREE with nuance——核心 CKA vs Standard 比较未受影响，但 Random spectrum 排序不可信。连续 5 轮未修复。\"\n  action_items:\n    - round: 7\n      action: \"统一所有方法 max_completion_length=1024 重跑\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"'Recovery capacity gradient' 术语与 gradient descent 混淆\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"全文替换为 'recovery capacity spectrum'\"\n  resolution_round: 7\n\n- id: \"R5-M1\"\n  summary: \"Section 5 末尾溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 7\n      reviewers: []\n      note: \"R7 确认格式合规\"\n  resolution: \"格式合规（R7/R8/R9 均未报告溢出）\"\n  resolution_round: 9\n\n- id: \"R5-M2\"\n  summary: \"Abstract p<0.001 未说明统计检验方法\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Abstract 标注 Welch's t-test\"\n  resolution_round: 6\n\n- id: \"R5-M3\"\n  summary: \"Page 7 display items 过度拥挤\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Figure 3 + Figure 4 + Table 2 挤在同一页\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M2 再次提出 Figure 2 信息密度过高。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 5\n      action: \"Figure 前移平衡视觉节奏\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M4\"\n  summary: \"bib key 年份误导 + 引用错误\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"lachance2024cka→2022, klabunde→2023\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 修正 bib 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M5\"\n  summary: \"Figure 2 标注字体偏小 / 颜色区分度不足\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M2 指出 Figure 2 信息密度过高。视觉审查标记 page 7-8 figure panel axis labels 偏小。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 5\n      action: \"增大字号 + 添加不同 line style\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N1\"\n  summary: \"GSM8K 单基准 GRPO 主实验，Title/Abstract 做一般性声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未单独提及——MATH-500 和 MBPP 已存在。\"\n  action_items:\n    - round: 6\n      action: \"MF1: MBPP probe eval\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"CKA-only layer 分布混杂——72.5% 剪枝集中 early layers，优势可能来自 layer 分布而非 diversity\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-N3 提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 详细展开。granularity 不匹配无法解耦。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未直接复现\"\n  action_items:\n    - round: 7\n      action: \"创建 same-granularity layer-biased baseline\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"缺失高度相关文献：RL Finetunes Small Subnetworks (2505.11711)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 添加引用并在 Related Work/Discussion 讨论\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"Reward-accuracy decoupling 未区分 format compliance vs reasoning quality\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"需报告 EOS rate 和 format compliance rate\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未直接提及\"\n  action_items:\n    - round: 6\n      action: \"Agent 从 eval logs 提取 format compliance / EOS rate\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"实验仅覆盖 MLP channel pruning，Title/Abstract 未限定 scope\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Title 改为 'How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs'\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"遗漏 3 篇相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 验证并添加引用\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Welch's t-test at N=3 统计功效极低，缺 effect size 和 CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Cohen's d + 95% CI 已加入正文\"\n  resolution_round: 7\n\n- id: \"R6-W5\"\n  summary: \"15%/25% sparsity 实验为 single-seed\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W5 交叉回应提出。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W2/W3 再次提出 15% 和 25% 单 seed 问题。R2 交叉回应对 W3 部分反驳（25% 非核心 claim）。\"\n  action_items:\n    - round: 6\n      action: \"15%/25% 在 Limitations 标注\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"RASP 表现差于 Standard 缺乏充分解释——乘法形式 artifact\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"需分析 importance 和 CKA overlap 的相关性\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W3 详细论证：α=1.0 collapse + α=2.0 本质 CKA-dominant。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N2 正式升为 Critical：乘法形式 I(h)=0 退化未与加法替代对比。R2 交叉回应完全同意——两个 Reviewer 互补论证 RASP 整个参数空间的问题：一端退化(α=1.0)，另一端等价 CKA-only(α=2.0)。缺少加法形式无法判断 collapse 原因。\"\n  action_items:\n    - round: 9\n      action: \"跑 additive combination baseline β·I(h)+(1-β)·(1-F(h))；最低限度在论文中讨论乘法 vs 加法选择理由\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Table 1 脚注 'Only redundancy-based pruning sustains RL recovery' 与 Random 排第二矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"脚注措辞已修改\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Section 5 Discussion 偏薄（仅半页）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议讨论 CKA 与 RL exploration 关系\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W6 再次提出。Section 5 仅约 7-8 行。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W5 再次提出 Discussion 被放 Appendix，spectrum 实用价值不清。R1 Q6 暗示 floor ablation 缺乏 Standard 对照。\"\n  action_items:\n    - round: 8\n      action: \"扩充 Discussion 至少半栏\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M1\"\n  summary: \"Reward-accuracy decoupling 首次使用时无正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"首次使用处添加正式定义\"\n  resolution_round: 6\n\n- id: \"R6-M2\"\n  summary: \"Figure 2 y 轴未标注 mean vs peak reward\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 6\n      action: \"修改 Figure 2 y-axis label\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M3\"\n  summary: \"Eq.1 未写出 Taylor expansion 完整数学形式\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 补充 Eq.1 完整数学形式\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 7 Issues — Carried forward\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"Dose-response 中 max_completion_length 不一致（Random: 512, 其他: 1024）构成关键混杂变量\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 独立提出。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"再次确认。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N3 明确提出'violates controlled experiment design'。R2 交叉回应 AGREE with nuance（核心 CKA vs Standard 比较不受影响，但 spectrum ordering 含 Random 部分不可信）。合并到 R5-W4 统一追踪。\"\n  action_items:\n    - round: 7\n      action: \"统一所有方法 max_completion_length=1024 重跑\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N2\"\n  summary: \"Abstract overclaiming 'holds across sparsity levels'——仅 20-25% 窗口成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N4 提出，R2 完全同意。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-C3 再次提出：有效窗口仅 20-25%，30% 全面崩塌，Abstract 用 'moderate sparsity' 模糊处理，实际压缩比约 12-15%。R1 交叉回应隐含同意（W2/W3 讨论 15%/25% 边界条件）。\"\n  action_items:\n    - round: 7\n      action: \"Abstract 改为 'at moderate sparsity (20-25%)' 限定\"\n      assigned_to: paper_agent\n      status: open\n    - round: 9\n      action: \"正文和 Abstract 必须明确标注实际有效压缩比（~12-15%）而非仅报告 sparsity 百分比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"Decoupling 缺少形式化等价性检验（TOST ε=2pp post-hoc）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 同意。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"论文已包含 TOST 但 ε=2pp 选择需 justify。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 再次提出 ε=2pp 缺乏 a priori justification。R2 交叉回应同意——ε=1pp 部分结论不成立。\"\n  action_items:\n    - round: 8\n      action: \"justify ε=2pp 选择（引用 GSM8K 文献中 meaningful difference threshold）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"MBPP 结果统计不显著却被用作 decoupling 支持证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未直接提及\"\n  action_items:\n    - round: 7\n      action: \"正文引用 MBPP 时加注 'not statistically significant'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Calibration 数据量 M 在正文中未明确指定\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 同意。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W6 再次提出 Calibration M=512 importance score 稳定性未验证。R2 交叉回应部分反驳（Taylor expansion 是标准做法，M=512 已超 LLM-Pruner）。\"\n  action_items:\n    - round: 7\n      action: \"在 Section 3.2 或 4.1 明确指定 M 及选择依据\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W4\"\n  summary: \"Throughput regression（-19%）未在 Limitations 讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 7\n      action: \"在 Limitations 添加 throughput regression 讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Title/叙事焦点与实际恢复来源错位——SFT 贡献 ~60pp 而 GRPO <1pp\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 交叉回应 [NEW FINDING]\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"双 Reviewer 详细论证。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W1 再次提出 Title/叙事与 SFT-dominant 发现的错位。R1 交叉回应隐含同意。\"\n  action_items:\n    - round: 8\n      action: \"Discussion 显式讨论 'SFT 主导恢复' 的含义及 GRPO 实际贡献的定位\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 8 Issues — Carried forward\n# ============================================================\n\n- id: \"R8-N1\"\n  summary: \"RASP 方法贡献叙事自相矛盾——α=2.0 本质 CKA-dominant，'平衡 importance 与 diversity' 不准确\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W3 详细论证。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N1 和 R2-C2 同时独立提出。R2 交叉回应补充：Table 1 中 RASP(α=2.0) Peak Rew = CKA-only Peak Rew = 0.354（完全相同），RASP 框架的额外 parametric 复杂性未带来任何 recovery capacity 增益。accuracy 差 1.72pp 落在单 seed 不可信区间。双 Reviewer 合力否定 RASP 全参数空间。\"\n  action_items:\n    - round: 9\n      action: \"重新定位论文：从 'RASP as method contribution' 改为 'empirical study of criterion effects'；RASP 降级为 exploratory analysis 之一\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N2\"\n  summary: \"Random baseline max_completion_length=512（vs 其他方法 1024）构成不公平比较\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 列 Warning。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"合并追踪于 R7-N1/R5-W4。\"\n  action_items:\n    - round: 8\n      action: \"统一 Random 的 max_completion_length=1024 重跑\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N3\"\n  summary: \"RASP 函数形式（乘法）缺乏理论推导，可能人为导致 α=1.0 collapse\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 同意。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N2 升为 Critical：I(h)=0 退化是 RASP 败给 CKA-only 的根本原因，加法形式不存在此退化。R2 交叉回应完全同意——补充两个维度互补：R1 关注 α=1.0 端（collapse），R2 关注 α=2.0 端（CKA 等价），合证 RASP 全空间有问题。\"\n  action_items:\n    - round: 9\n      action: \"跑 additive baseline β·I(h)+(1-β)·(1-F(h))（低成本实验）；或至少在论文中详细讨论乘法选择的理由和 I(h)=0 退化的含义\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N4\"\n  summary: \"TOST ε=2pp margin post-hoc selection 嫌疑\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Director 判定 Info。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W1 再次明确提出。合并追踪于 R7-W1。\"\n  action_items:\n    - round: 8\n      action: \"justify ε=2pp 选择\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N5\"\n  summary: \"30% sparsity 全面 collapse 限制方法实用窗口（仅 20-25%）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W7 提出。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-C3 升为 Critical：实际压缩比约 12-15%，实用价值受限。R1 在 W2/W3 中讨论了 15%/25% 边界但对实用价值限制的判断不如 R2 强硬——R1 认为论文定位 controlled study 而非 practical tool。Director 判定升为 Warning（非 reject 级别但需在论文中诚实面对）。\"\n  action_items:\n    - round: 9\n      action: \"Abstract/正文必须诚实标注实际有效压缩比；Discussion 讨论突破方向\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N6\"\n  summary: \"缺失高度相关文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 识别 3 篇缺失。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1 提出新缺失：Molchanov et al. (2019) 'Importance Estimation for Neural Network Pruning'——加法形式多标准组合先例。\"\n  action_items:\n    - round: 8\n      action: \"验证并添加 Li et al. (2504.02010) 和 'Can Pruning Improve Reasoning?' (2505.14582)\"\n      assigned_to: paper_agent\n      status: open\n    - round: 9\n      action: \"添加 Molchanov et al. (2019) 作为加法形式 multi-criteria 组合的先例引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M1\"\n  summary: \"Recovery capacity 概念先用后定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M2\"\n  summary: \"无代码/checkpoint 发布承诺\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 8\n      action: \"在 Conclusion 或 Abstract 添加代码/checkpoint 发布承诺\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M3\"\n  summary: \"Lottery Ticket Hypothesis 联系过于表面\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 8\n      action: \"弱化 LTH 类比或加说明两者的本质区别\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 9 New Issues\n# ============================================================\n\n- id: \"R9-N1\"\n  summary: \"RASP 被全参数空间否定——α=1.0 乘法退化 collapse，α=2.0 等价 CKA-only（Peak Rew 相同），α→∞ 即 CKA-only\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-C2 独立提出，交叉回应中双方完全同意。R2 补充关键数据：Table 1 RASP(α=2.0) Peak Rew = CKA-only Peak Rew = 0.354。这是本轮最核心共识——RASP 作为方法贡献在整个参数空间都不优于其端点。\"\n  action_items:\n    - round: 9\n      action: \"论文重新定位为 empirical study；RASP 降级为 exploratory analysis；核心贡献改为 controlled comparison framework + decoupling 发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-N2\"\n  summary: \"乘法形式 I(h)×(1-F(h))^α 的 I(h)=0 退化缺少加法形式对照——无法区分 artifact vs 真实 tradeoff\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N2 首次作为独立 Critical 提出。R2 交叉回应完全同意——两人互补：R1 关注 α=1.0 端（collapse 可能是数值 artifact），R2 关注 α=2.0 端（CKA 等价）。合证 RASP 函数形式的选择缺乏 justification。引用 Molchanov et al. (2019) 作为加法先例。\"\n  action_items:\n    - round: 9\n      action: \"跑 additive baseline（成本低，单 seed 即可初步验证）；如加法下 α=1.0 不 collapse，则乘法形式选择需重大修改\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-N3\"\n  summary: \"Random baseline max_completion_length=512 违反受控实验自称的 'hold everything else constant'\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1 列 Critical（直接影响 spectrum），R2 AGREE with nuance（核心 CKA vs Standard 比较不受影响，Random 非核心对照）。Director 判定 Warning——不太可能翻转核心 spectrum ordering，但违反论文自身声明。合并追踪于 R5-W4/R7-N1。\"\n  action_items:\n    - round: 9\n      action: \"统一 Random max_completion_length=1024 重跑；或正文明确标注此偏差并讨论影响\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W1\"\n  summary: \"300-step extended training 未报告 step-by-step accuracy 曲线（仅报 100 和 300 终值）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 交叉回应同意。如 CKA-only 在 150-200 步仍上升而 Standard plateau，这是有信息量的。且 300 步远少于 RLVR 文献常见预算（1000-5000 步）。\"\n  action_items:\n    - round: 9\n      action: \"报告 100/150/200/250/300 步 accuracy trajectory；或在 Limitations 讨论为何 300 步足够\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"Limitations 关于 Random seed 的表述与正文矛盾（Limitations 称单 seed 但实际 3 seeds）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 交叉回应同意。此类不一致降低审稿人对其他声称的信任度。\"\n  action_items:\n    - round: 9\n      action: \"修正 Limitations section 关于 Random seed 数量的表述\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W3\"\n  summary: \"Ji et al. (2026) 对比 overclaiming\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W2 提出。R1 在交叉回应中未直接评论。\"\n  action_items:\n    - round: 9\n      action: \"弱化与 Ji et al. 的对比措辞，承认实验设置差异\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W4\"\n  summary: \"Qwen2.5-Math-7B GRPO 验证缺失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W4 提出。跨架构验证仅 SFT，GRPO 结论无法泛化。与 R5-N2 相关。\"\n  action_items:\n    - round: 9\n      action: \"补充 Qwen2.5-Math-7B GRPO 或在论文中明确限定 GRPO claim 仅适用于 DeepSeek-R1-Distill-Qwen-7B\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M1\"\n  summary: \"缺失引用：Molchanov et al. (2019) 'Importance Estimation for Neural Network Pruning'——加法形式多标准组合先例\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1 Missing References 提出。加法形式 multi-criteria 组合的重要先例。\"\n  action_items:\n    - round: 9\n      action: \"验证并添加 Molchanov et al. (2019)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "issues_yaml": "# ============================================================\n# Round 1-3 Issues — All Resolved\n# ============================================================\n\n- id: \"R1-C1\"\n  summary: \"CKA-recovery link 仅相关性, 无因果干预\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Jaccard overlap 分析 + Limitations 承认 + 多种子统计验证\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Single-seed GRPO 无统计显著性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"3-seed GRPO CKA-only, Welch's t-test p=0.0009\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"仅 GSM8K 单基准\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"MATH-500 OOD 验证 + MBPP 代码基准\"\n  resolution_round: 3\n\n- id: \"R1-W1\"\n  summary: \"Title overclaim 'determines'\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Title 改为 'shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W2\"\n  summary: \"Abstract 'universally determines' overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"改为 'significantly shapes'\"\n  resolution_round: 3\n\n- id: \"R1-W3\"\n  summary: \"仅 DeepSeek-R1-7B 单模型\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Qwen2.5-Math-7B cross-arch + 1.5B cross-scale\"\n  resolution_round: 3\n\n- id: \"R1-M1\"\n  summary: \"GRPO 超参未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Appendix 完整超参表\"\n  resolution_round: 3\n\n- id: \"R1-M2\"\n  summary: \"Table 1 缺 Random baseline\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Table 1 加入 Random 行\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C1\"\n  summary: \"GRPO 准确率几乎不变,为何要用 GRPO\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Dual-layer reframe: SFT(accuracy) + GRPO(reward signal)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-C2\"\n  summary: \"Cross-architecture 仅 SFT 验证,GRPO 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"1.5B GRPO 补充 + Abstract 区分表述\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W1\"\n  summary: \"SFT recovery 被忽视,过度聚焦 GRPO\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注解释 SFT catastrophic forgetting\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W2\"\n  summary: \"Qwen-Math 跨架构验证仅 SFT，Abstract overclaim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 区分 GRPO(DeepSeek) vs SFT(Qwen-Math)\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W3\"\n  summary: \"GRPO 准确率改变 < 1pp — 实际效用存疑\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"300-step accuracy + reward-accuracy decoupling 论证\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W4\"\n  summary: \"RASP/Random 仍为单种子\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"脚注透明标注 + Limitations 披露\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W5\"\n  summary: \"Random baseline SFT/GRPO Acc 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Table 2 脚注标注 checkpoint not preserved\"\n  resolution_round: 3\n\n- id: \"R2-NEW-W6\"\n  summary: \"正文 5 处 'determines' 残留\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"全部替换为 shapes/significantly influences\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M1\"\n  summary: \"GRPO batch size / rollouts 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-NEW-M2\"\n  summary: \"SFT lr/batch/optimizer 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 超参表完整覆盖\"\n  resolution_round: 3\n\n- id: \"R2-VIS-1\"\n  summary: \"末页 Figure 6 仅占 30%，70% 空白\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 重排\"\n  resolution_round: 3\n\n- id: \"R2-VIS-2\"\n  summary: \"Appendix page 12 过度拥挤\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Appendix 拆分到多页\"\n  resolution_round: 3\n\n- id: \"R3-S5\"\n  summary: \"Qwen-Math 'strongest evidence' 措辞仍略强\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"strongest → additional evidence in §4.5\"\n  resolution_round: 3\n\n- id: \"R3-M2\"\n  summary: \"300-step accuracy 未标注 seed\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"(single seed) 标注已添加到 §4.3\"\n  resolution_round: 3\n\n- id: \"R3-M3\"\n  summary: \"无代码/checkpoint 发布声明\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"Code and checkpoints release statement in Conclusion\"\n  resolution_round: 3\n\n# ============================================================\n# Round 5-7 Issues — Carried forward\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Reward-accuracy decoupling 叙事薄弱（GRPO 增量 <1pp，可能是 SFT 天花板效应 artifact）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。SYSTEMIC_ISSUE #1 核心。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W4 和 R2-W2 再次提出，增加新角度：需区分 format compliance vs reasoning quality。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2-N3 升级为 critical。R1 完全同意。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 升为本文最关键问题（Critical），R1 维持 Warning。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-C1 再次提出：SFT 已恢复大部分 accuracy（~60pp），GRPO 无 headroom。R1 虽未直接提但在交叉回应中认为 15% sparsity 数据（GRPO amplifies gap）支持天花板解释。连续 5 轮 Critical 未解决。\"\n  action_items:\n    - round: 5\n      action: \"D098 dual-layer reframe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 9\n      action: \"需要消融实验：在 SFT 恢复不充分的条件下（如更少 SFT steps 或更高 sparsity）验证 GRPO 是否产生 accuracy 差异\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N2\"\n  summary: \"Cross-architecture/scale 泛化严重不足，所有模型共享 Qwen2.5 base\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前不可行（需全 pipeline ~50h GPU）。但 1.5B GRPO 数据已有。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识。Appendix O 'Cross-Architecture Validation' 标题误导。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识 Critical。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W3 再次提出单一架构族（Qwen2.5 系列）。R1 未直接复述但在 Q6 中暗示 Standard 在不同设置下行为未知。连续 5 轮 Critical。\"\n  action_items:\n    - round: 8\n      action: \"Title 改为更精确范围或补充至少一个非 Qwen 架构 GRPO 结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"RASP 单 seed 验证不足——方法贡献可靠性存疑\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"核心比较 CKA vs Standard 有 3-seed p=0.0009。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 升级为 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 再次共识 critical。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Director 判定 Critical。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N4 再次明确提出：全部 α 变体（0.5-4.0）均单 seed，dose-response inverted-U 不可靠。R2 交叉回应强烈同意——α=2.0 方差未知时 1.72pp 不可信。连续 5 轮 Critical 未解决。\"\n  action_items:\n    - round: 9\n      action: \"至少 α=2.0 和 α=1.0 各跑 3 seeds；如无法完成则降级 RASP 为 exploratory\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"因果语言系统性过强——'causal driver' 超出 quasi-experimental 证据\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"SYSTEMIC_ISSUE #2 成员。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N3 详细论证。R2 补充 metrics diversity 不足。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未单独复现为独立问题。可能已部分修复（论文已改用 'shapes'）。\"\n  action_items:\n    - round: 7\n      action: \"全文语言审计：'causal driver' → 'key determinant'；decoupling claims 加限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Per-layer capacity floor (40%) 未消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DDL 前不可行（需全 pipeline ~50h GPU）。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-W3 再次提出。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-Q6 问到 Floor ablation 仅对 CKA-only 做了，Standard 在不同 τ 下表现未知。\"\n  action_items:\n    - round: 5\n      action: \"Limitations 讨论 + rebuttal 论点准备\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Floor ablation τ∈{0.3,0.4,0.5,0.6} experiments running; appendix table added\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"α dose-response 存在 generation length 混杂变量\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"高 ROI 实验。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出。R2-W1 扩展为 κ 消融缺失。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"升级为 critical。α=1.0 用 1024 tokens，其他用 512 tokens。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 在 W2（Random baseline）中再次确认。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N3 再次明确提出：Random GRPO 用 512 vs 其他 1024，违反受控设计。R2 交叉回应 AGREE with nuance——核心 CKA vs Standard 比较未受影响，但 Random spectrum 排序不可信。连续 5 轮未修复。\"\n  action_items:\n    - round: 7\n      action: \"统一所有方法 max_completion_length=1024 重跑\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"'Recovery capacity gradient' 术语与 gradient descent 混淆\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"全文替换为 'recovery capacity spectrum'\"\n  resolution_round: 7\n\n- id: \"R5-M1\"\n  summary: \"Section 5 末尾溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 7\n      reviewers: []\n      note: \"R7 确认格式合规\"\n  resolution: \"格式合规（R7/R8/R9 均未报告溢出）\"\n  resolution_round: 9\n\n- id: \"R5-M2\"\n  summary: \"Abstract p<0.001 未说明统计检验方法\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Abstract 标注 Welch's t-test\"\n  resolution_round: 6\n\n- id: \"R5-M3\"\n  summary: \"Page 7 display items 过度拥挤\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Figure 3 + Figure 4 + Table 2 挤在同一页\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M2 再次提出 Figure 2 信息密度过高。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 5\n      action: \"Figure 前移平衡视觉节奏\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M4\"\n  summary: \"bib key 年份误导 + 引用错误\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"lachance2024cka→2022, klabunde→2023\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 5\n      action: \"Paper Agent 修正 bib 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-M5\"\n  summary: \"Figure 2 标注字体偏小 / 颜色区分度不足\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M2 指出 Figure 2 信息密度过高。视觉审查标记 page 7-8 figure panel axis labels 偏小。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 5\n      action: \"增大字号 + 添加不同 line style\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N1\"\n  summary: \"GSM8K 单基准 GRPO 主实验，Title/Abstract 做一般性声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"双 Reviewer 共识 critical。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未单独提及——MATH-500 和 MBPP 已存在。\"\n  action_items:\n    - round: 6\n      action: \"MF1: MBPP probe eval\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"CKA-only layer 分布混杂——72.5% 剪枝集中 early layers，优势可能来自 layer 分布而非 diversity\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-N3 提出。\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 详细展开。granularity 不匹配无法解耦。\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未直接复现\"\n  action_items:\n    - round: 7\n      action: \"创建 same-granularity layer-biased baseline\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N3\"\n  summary: \"缺失高度相关文献：RL Finetunes Small Subnetworks (2505.11711)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 添加引用并在 Related Work/Discussion 讨论\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"Reward-accuracy decoupling 未区分 format compliance vs reasoning quality\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"需报告 EOS rate 和 format compliance rate\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未直接提及\"\n  action_items:\n    - round: 6\n      action: \"Agent 从 eval logs 提取 format compliance / EOS rate\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"实验仅覆盖 MLP channel pruning，Title/Abstract 未限定 scope\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Title 改为 'How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs'\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"遗漏 3 篇相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent 验证并添加引用\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Welch's t-test at N=3 统计功效极低，缺 effect size 和 CI\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Cohen's d + 95% CI 已加入正文\"\n  resolution_round: 7\n\n- id: \"R6-W5\"\n  summary: \"15%/25% sparsity 实验为 single-seed\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2-W5 交叉回应提出。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W2/W3 再次提出 15% 和 25% 单 seed 问题。R2 交叉回应对 W3 部分反驳（25% 非核心 claim）。\"\n  action_items:\n    - round: 6\n      action: \"15%/25% 在 Limitations 标注\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"RASP 表现差于 Standard 缺乏充分解释——乘法形式 artifact\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"需分析 importance 和 CKA overlap 的相关性\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W3 详细论证：α=1.0 collapse + α=2.0 本质 CKA-dominant。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N2 正式升为 Critical：乘法形式 I(h)=0 退化未与加法替代对比。R2 交叉回应完全同意——两个 Reviewer 互补论证 RASP 整个参数空间的问题：一端退化(α=1.0)，另一端等价 CKA-only(α=2.0)。缺少加法形式无法判断 collapse 原因。\"\n  action_items:\n    - round: 9\n      action: \"跑 additive combination baseline β·I(h)+(1-β)·(1-F(h))；最低限度在论文中讨论乘法 vs 加法选择理由\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Table 1 脚注 'Only redundancy-based pruning sustains RL recovery' 与 Random 排第二矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"脚注措辞已修改\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Section 5 Discussion 偏薄（仅半页）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"建议讨论 CKA 与 RL exploration 关系\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W6 再次提出。Section 5 仅约 7-8 行。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W5 再次提出 Discussion 被放 Appendix，spectrum 实用价值不清。R1 Q6 暗示 floor ablation 缺乏 Standard 对照。\"\n  action_items:\n    - round: 8\n      action: \"扩充 Discussion 至少半栏\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M1\"\n  summary: \"Reward-accuracy decoupling 首次使用时无正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"首次使用处添加正式定义\"\n  resolution_round: 6\n\n- id: \"R6-M2\"\n  summary: \"Figure 2 y 轴未标注 mean vs peak reward\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 6\n      action: \"修改 Figure 2 y-axis label\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-M3\"\n  summary: \"Eq.1 未写出 Taylor expansion 完整数学形式\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 6\n      action: \"Paper Agent 补充 Eq.1 完整数学形式\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 7 Issues — Carried forward\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"Dose-response 中 max_completion_length 不一致（Random: 512, 其他: 1024）构成关键混杂变量\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"双 Reviewer 独立提出。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"再次确认。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N3 明确提出'violates controlled experiment design'。R2 交叉回应 AGREE with nuance（核心 CKA vs Standard 比较不受影响，但 spectrum ordering 含 Random 部分不可信）。合并到 R5-W4 统一追踪。\"\n  action_items:\n    - round: 7\n      action: \"统一所有方法 max_completion_length=1024 重跑\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N2\"\n  summary: \"Abstract overclaiming 'holds across sparsity levels'——仅 20-25% 窗口成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-N4 提出，R2 完全同意。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-C3 再次提出：有效窗口仅 20-25%，30% 全面崩塌，Abstract 用 'moderate sparsity' 模糊处理，实际压缩比约 12-15%。R1 交叉回应隐含同意（W2/W3 讨论 15%/25% 边界条件）。\"\n  action_items:\n    - round: 7\n      action: \"Abstract 改为 'at moderate sparsity (20-25%)' 限定\"\n      assigned_to: paper_agent\n      status: open\n    - round: 9\n      action: \"正文和 Abstract 必须明确标注实际有效压缩比（~12-15%）而非仅报告 sparsity 百分比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"Decoupling 缺少形式化等价性检验（TOST ε=2pp post-hoc）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W3 提出，R2 同意。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"论文已包含 TOST 但 ε=2pp 选择需 justify。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 再次提出 ε=2pp 缺乏 a priori justification。R2 交叉回应同意——ε=1pp 部分结论不成立。\"\n  action_items:\n    - round: 8\n      action: \"justify ε=2pp 选择（引用 GSM8K 文献中 meaningful difference threshold）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"MBPP 结果统计不显著却被用作 decoupling 支持证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未直接提及\"\n  action_items:\n    - round: 7\n      action: \"正文引用 MBPP 时加注 'not statistically significant'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Calibration 数据量 M 在正文中未明确指定\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 同意。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W6 再次提出 Calibration M=512 importance score 稳定性未验证。R2 交叉回应部分反驳（Taylor expansion 是标准做法，M=512 已超 LLM-Pruner）。\"\n  action_items:\n    - round: 7\n      action: \"在 Section 3.2 或 4.1 明确指定 M 及选择依据\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W4\"\n  summary: \"Throughput regression（-19%）未在 Limitations 讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 7\n      action: \"在 Limitations 添加 throughput regression 讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Title/叙事焦点与实际恢复来源错位——SFT 贡献 ~60pp 而 GRPO <1pp\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 交叉回应 [NEW FINDING]\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"双 Reviewer 详细论证。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W1 再次提出 Title/叙事与 SFT-dominant 发现的错位。R1 交叉回应隐含同意。\"\n  action_items:\n    - round: 8\n      action: \"Discussion 显式讨论 'SFT 主导恢复' 的含义及 GRPO 实际贡献的定位\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 8 Issues — Carried forward\n# ============================================================\n\n- id: \"R8-N1\"\n  summary: \"RASP 方法贡献叙事自相矛盾——α=2.0 本质 CKA-dominant，'平衡 importance 与 diversity' 不准确\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W3 详细论证。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N1 和 R2-C2 同时独立提出。R2 交叉回应补充：Table 1 中 RASP(α=2.0) Peak Rew = CKA-only Peak Rew = 0.354（完全相同），RASP 框架的额外 parametric 复杂性未带来任何 recovery capacity 增益。accuracy 差 1.72pp 落在单 seed 不可信区间。双 Reviewer 合力否定 RASP 全参数空间。\"\n  action_items:\n    - round: 9\n      action: \"重新定位论文：从 'RASP as method contribution' 改为 'empirical study of criterion effects'；RASP 降级为 exploratory analysis 之一\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N2\"\n  summary: \"Random baseline max_completion_length=512（vs 其他方法 1024）构成不公平比较\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 列 Warning。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"合并追踪于 R7-N1/R5-W4。\"\n  action_items:\n    - round: 8\n      action: \"统一 Random 的 max_completion_length=1024 重跑\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N3\"\n  summary: \"RASP 函数形式（乘法）缺乏理论推导，可能人为导致 α=1.0 collapse\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 同意。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N2 升为 Critical：I(h)=0 退化是 RASP 败给 CKA-only 的根本原因，加法形式不存在此退化。R2 交叉回应完全同意——补充两个维度互补：R1 关注 α=1.0 端（collapse），R2 关注 α=2.0 端（CKA 等价），合证 RASP 全空间有问题。\"\n  action_items:\n    - round: 9\n      action: \"跑 additive baseline β·I(h)+(1-β)·(1-F(h))（低成本实验）；或至少在论文中详细讨论乘法选择的理由和 I(h)=0 退化的含义\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N4\"\n  summary: \"TOST ε=2pp margin post-hoc selection 嫌疑\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Director 判定 Info。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W1 再次明确提出。合并追踪于 R7-W1。\"\n  action_items:\n    - round: 8\n      action: \"justify ε=2pp 选择\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N5\"\n  summary: \"30% sparsity 全面 collapse 限制方法实用窗口（仅 20-25%）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W7 提出。\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-C3 升为 Critical：实际压缩比约 12-15%，实用价值受限。R1 在 W2/W3 中讨论了 15%/25% 边界但对实用价值限制的判断不如 R2 强硬——R1 认为论文定位 controlled study 而非 practical tool。Director 判定升为 Warning（非 reject 级别但需在论文中诚实面对）。\"\n  action_items:\n    - round: 9\n      action: \"Abstract/正文必须诚实标注实际有效压缩比；Discussion 讨论突破方向\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N6\"\n  summary: \"缺失高度相关文献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 识别 3 篇缺失。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1 提出新缺失：Molchanov et al. (2019) 'Importance Estimation for Neural Network Pruning'——加法形式多标准组合先例。\"\n  action_items:\n    - round: 8\n      action: \"验证并添加 Li et al. (2504.02010) 和 'Can Pruning Improve Reasoning?' (2505.14582)\"\n      assigned_to: paper_agent\n      status: open\n    - round: 9\n      action: \"添加 Molchanov et al. (2019) 作为加法形式 multi-criteria 组合的先例引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M1\"\n  summary: \"Recovery capacity 概念先用后定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M2\"\n  summary: \"无代码/checkpoint 发布承诺\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 8\n      action: \"在 Conclusion 或 Abstract 添加代码/checkpoint 发布承诺\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M3\"\n  summary: \"Lottery Ticket Hypothesis 联系过于表面\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提及\"\n  action_items:\n    - round: 8\n      action: \"弱化 LTH 类比或加说明两者的本质区别\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 9 New Issues\n# ============================================================\n\n- id: \"R9-N1\"\n  summary: \"RASP 被全参数空间否定——α=1.0 乘法退化 collapse，α=2.0 等价 CKA-only（Peak Rew 相同），α→∞ 即 CKA-only\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-C2 独立提出，交叉回应中双方完全同意。R2 补充关键数据：Table 1 RASP(α=2.0) Peak Rew = CKA-only Peak Rew = 0.354。这是本轮最核心共识——RASP 作为方法贡献在整个参数空间都不优于其端点。\"\n  action_items:\n    - round: 9\n      action: \"论文重新定位为 empirical study；RASP 降级为 exploratory analysis；核心贡献改为 controlled comparison framework + decoupling 发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-N2\"\n  summary: \"乘法形式 I(h)×(1-F(h))^α 的 I(h)=0 退化缺少加法形式对照——无法区分 artifact vs 真实 tradeoff\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-N2 首次作为独立 Critical 提出。R2 交叉回应完全同意——两人互补：R1 关注 α=1.0 端（collapse 可能是数值 artifact），R2 关注 α=2.0 端（CKA 等价）。合证 RASP 函数形式的选择缺乏 justification。引用 Molchanov et al. (2019) 作为加法先例。\"\n  action_items:\n    - round: 9\n      action: \"跑 additive baseline（成本低，单 seed 即可初步验证）；如加法下 α=1.0 不 collapse，则乘法形式选择需重大修改\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-N3\"\n  summary: \"Random baseline max_completion_length=512 违反受控实验自称的 'hold everything else constant'\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1 列 Critical（直接影响 spectrum），R2 AGREE with nuance（核心 CKA vs Standard 比较不受影响，Random 非核心对照）。Director 判定 Warning——不太可能翻转核心 spectrum ordering，但违反论文自身声明。合并追踪于 R5-W4/R7-N1。\"\n  action_items:\n    - round: 9\n      action: \"统一 Random max_completion_length=1024 重跑；或正文明确标注此偏差并讨论影响\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W1\"\n  summary: \"300-step extended training 未报告 step-by-step accuracy 曲线（仅报 100 和 300 终值）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 交叉回应同意。如 CKA-only 在 150-200 步仍上升而 Standard plateau，这是有信息量的。且 300 步远少于 RLVR 文献常见预算（1000-5000 步）。\"\n  action_items:\n    - round: 9\n      action: \"报告 100/150/200/250/300 步 accuracy trajectory；或在 Limitations 讨论为何 300 步足够\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"Limitations 关于 Random seed 的表述与正文矛盾（Limitations 称单 seed 但实际 3 seeds）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W5 提出，R2 交叉回应同意。此类不一致降低审稿人对其他声称的信任度。\"\n  action_items:\n    - round: 9\n      action: \"修正 Limitations section 关于 Random seed 数量的表述\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W3\"\n  summary: \"Ji et al. (2026) 对比 overclaiming\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W2 提出。R1 在交叉回应中未直接评论。\"\n  action_items:\n    - round: 9\n      action: \"弱化与 Ji et al. 的对比措辞，承认实验设置差异\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W4\"\n  summary: \"Qwen2.5-Math-7B GRPO 验证缺失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W4 提出。跨架构验证仅 SFT，GRPO 结论无法泛化。与 R5-N2 相关。\"\n  action_items:\n    - round: 9\n      action: \"补充 Qwen2.5-Math-7B GRPO 或在论文中明确限定 GRPO claim 仅适用于 DeepSeek-R1-Distill-Qwen-7B\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M1\"\n  summary: \"缺失引用：Molchanov et al. (2019) 'Importance Estimation for Neural Network Pruning'——加法形式多标准组合先例\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1 Missing References 提出。加法形式 multi-criteria 组合的重要先例。\"\n  action_items:\n    - round: 9\n      action: \"验证并添加 Molchanov et al. (2019)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-25T21:32:03.061934+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_issues.yaml\", \"bytes\": 33008}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-25T21:33:48.269840+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 9 审稿报告\n\n**Venue**: EMNLP 2026 (via ARR)\n**论文**: \"How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs\"\n**评审人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性）\n**模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文提出 RASP（Recovery-Aware Structured Pruning），通过乘法形式结合 importance score 和 CKA-based diversity score 进行 MLP 结构化剪枝，并系统研究不同剪枝标准对 GRPO 恢复训练的影响。核心发现是 \"recovery capacity spectrum\"（CKA-only > RASP > Random > Standard）和 \"reward-accuracy decoupling\"（GRPO 提升 reward 但 accuracy 改变 <1pp）。\n\n然而，RASP 方法被自身消融实验否定：CKA-only（RASP 的 α→∞ 极端情况）在 recovery capacity 上与 RASP 最优配置（α=2.0）完全相同（Peak Rew = 0.354），而 accuracy 差异仅 1.72pp（单 seed，不可信）。论文最终推荐 CKA-only 而非 RASP——方法贡献不成立。\n\n---\n\n## Strengths\n\n**S1** [双 Reviewer 共识] 受控实验设计理念在 pruning 文献中罕见——isolation design 使得 criterion effect 可比较。实验设计哲学值得推广。\n\n**S2** [双 Reviewer 共识] Reward-accuracy decoupling 是 genuinely surprising 的实证发现，对 RLVR 社区理解 post-pruning RL recovery 有参考价值。\n\n**S3** [Reviewer 1] f₀/gradient norm/KL divergence 等多维训练动态分析工具有独立价值，提供了比 final accuracy 更丰富的诊断视角。\n\n**S4** [Reviewer 1] 跨模型（Qwen2.5-Math-7B SFT）、跨尺度（1.5B）验证展示了系统性 validation 意识，即使覆盖面有限。\n\n**S5** [Reviewer 2] Recovery capacity spectrum 作为描述性框架有参考价值（即使 RASP 贡献不成立）。\n\n**S6** [双 Reviewer 共识] 写作清晰，Figure 2 有效传达实验设计，超参数报告详尽，代码已匿名开源。Reproducibility 评 4/5。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**C1** [双 Reviewer 共识] **RASP 方法贡献被全参数空间否定**\n- α=1.0（名义\"平衡\"点）：reward collapse（Peak Rew 0.061，四方法最差）\n- α=2.0（最优配置）：Peak Rew = CKA-only Peak Rew = 0.354（完全相同）；accuracy +1.72pp 为单 seed 不可信\n- α→∞：即 CKA-only 本身\n- 论文最终推荐 CKA-only 而非 RASP——当提出的方法被其自身特例超越时，方法贡献不成立\n- **影响**: 论文定位需从 \"method paper\" 转为 \"empirical study\"\n\n**C2** [双 Reviewer 共识] **乘法形式 I(h)=0 退化未与加法替代对比**\n- $S_{RASP}(h) = I(h) \\times (1-F(h))^\\alpha$ 意味着 $I(h)=0$ 的结构无论 diversity 多高都被零化\n- 这恰恰是 α=1.0 collapse 的可能机制——高 diversity 但低 importance 的结构被不当移除\n- 加法形式 $S = \\beta \\cdot I(h) + (1-\\beta) \\cdot (1-F(h))$ 不存在此退化，是自然的 ablation 对照\n- 缺少此对照无法判断 collapse 是乘法 artifact 还是 tradeoff 本质\n- 先例存在：Molchanov et al. (2019) \"Importance Estimation for Neural Network Pruning\"\n\n**C3** [双 Reviewer 共识] **RASP 全部 α 变体仅单 seed，dose-response 曲线不可靠**\n- CKA-only/Standard/Random 各 3 seeds，但 RASP 全部 α 值（0.5-4.0）均单 seed\n- Inverted-U 结论完全基于单次运行\n- α=2.0 的 66.11% vs CKA-only 64.39±0.19% 的 1.72pp 差距：RASP 方差未知\n- 如果 RASP 方差与 CKA-only 相当（~0.19pp），1.72pp 可能显著；但 RASP 跨 α 表现巨变（从 collapse 到 66%）暗示高方差\n- **连续 5 轮 Critical 未解决**（Round 5 至今）\n\n**C4** [Reviewer 2, R1 部分同意] **Reward-accuracy decoupling 可能是 SFT 天花板效应 artifact**\n- SFT 已恢复 ~60pp accuracy（从 post-prune ~4% 到 ~64%），GRPO 无 headroom\n- 15% sparsity 数据自相矛盾：GRPO amplifies CKA-only vs Standard gap (+1.51pp)，说明低 sparsity 下 GRPO 确实能放大差异——暗示 20% 下的 \"decoupling\" 是 headroom 耗尽\n- 需消融实验：在 SFT 恢复不充分条件下验证 GRPO 是否产生 accuracy 差异\n\n**C5** [双 Reviewer 共识] **Cross-architecture 泛化严重不足——所有模型共享 Qwen2.5 base**\n- Title 用 \"Reasoning LLMs\"（复数）但仅验证 Qwen2.5 架构族\n- Qwen2.5-Math-7B 仅有 SFT 验证，GRPO 缺失\n- 1.5B 同属 Qwen2.5 family（跨尺度但非跨架构）\n- **连续 5 轮 Critical 未解决**（Round 5 至今）\n\n### Warning\n\n**W1** [双 Reviewer 共识] Random baseline max_completion_length=512 vs 其他方法 1024，违反受控设计自称的 \"hold everything else constant\"。核心 CKA vs Standard 比较不受影响，但 spectrum 含 Random 的排序不可信。\n\n**W2** [双 Reviewer 共识] TOST ε=2pp 缺乏 a priori justification。如果 ε=1pp，部分 \"等价\" 结论不成立。需引用文献或 power analysis 论证 2pp 的实际意义。\n\n**W3** [Reviewer 1, R2 同意] 15% sparsity 下 GRPO 放大 CKA 优势（+1.51pp），Standard Δ=-0.93pp 接近 1pp 边界——decoupling 并非在所有 \"moderate sparsity\" 下普遍成立。\n\n**W4** [Reviewer 1, R2 同意] 300-step extended training 仅报告终值（100 步和 300 步），缺少中间步骤 accuracy trajectory。300 步远少于 RLVR 文献常见预算（1000-5000 步）。\n\n**W5** [Reviewer 2] Title/叙事焦点与 SFT-dominant 发现错位——SFT 贡献 ~60pp 恢复而 GRPO <1pp，但叙事聚焦 GRPO。\n\n**W6** [Reviewer 2] Ji et al. (2026) 对比 overclaiming——实验设置差异未充分讨论。\n\n**W7** [Reviewer 2] Discussion 被放 Appendix，正文 Section 5 仅约 7-8 行，缺少 spectrum 部署指导意义和机制解释。\n\n**W8** [Reviewer 1, R2 同意] Limitations 关于 Random seed 的表述（称 \"单 seed\"）与正文矛盾（实际 3 seeds）。此类不一致降低审稿人对其他声称的信任度。\n\n**W9** [Reviewer 2] 有效窗口仅 20-25% MLP sparsity（实际压缩比约 12-15%），30% 全面崩塌。Abstract 用 \"moderate sparsity\" 模糊处理。论文定位 controlled study 可接受，但需诚实面对实用限制。\n\n### Minor\n\n**M1** [Reviewer 1, R2 同意] Recovery capacity 概念先用后定义——Section 1 使用该术语但 Section 3 才定义。\n\n**M2** [Reviewer 1] Calibration M=512 importance score 稳定性未独立验证（CKA ranking 稳定性已验证但 importance 未验证）。R2 部分反驳：Taylor expansion 是标准做法，M=512 超过 LLM-Pruner 的 calibration 规模。\n\n**M3** [Reviewer 1, R2 同意] 25% sparsity 单 seed，Standard Δ=+0.99pp 恰在 1pp 边界。R2 反驳严重程度：25% 非核心 claim 支撑。\n\n---\n\n## Questions\n\nQ1: 如果跑 additive baseline $S = \\beta \\cdot I(h) + (1-\\beta) \\cdot (1-F(h))$，α=1.0 对应配置是否仍 collapse？这将判定 collapse 归因于乘法 artifact 还是 tradeoff 本质。\n\nQ2: 如果 α=2.0 补跑 3 seeds 方差很大（e.g., σ>1pp），RASP 相关叙事是否需要全部删除？\n\nQ3: 在 SFT 步数减少（如仅 50% SFT steps）的条件下，GRPO 是否能产生显著 accuracy 差异？这将验证 decoupling 是否为天花板效应。\n\nQ4: 为什么不统一 Random 的 max_completion_length 为 1024？成本极低（单 seed 约几小时 GPU）。\n\nQ5: 15% sparsity 下 GRPO 放大差异与 20% 下 decoupling 的矛盾如何解释？\n\nQ6: Extended training 150-200 步的 accuracy 曲线是否可用？\n\n---\n\n## Missing References\n\n1. **Molchanov et al. (2019)** \"Importance Estimation for Neural Network Pruning\" — 加法形式多标准组合先例，直接相关于 RASP vs additive 对比\n2. **Li et al. (2025, arXiv:2504.02010)** \"When Reasoning Meets Compression\" — 直接 benchmark 剪枝对 DeepSeek-R1 推理影响（Round 8 已提出，仍缺失）\n3. **\"Can Pruning Improve Reasoning?\" (2025, arXiv:2505.14582)** — 剪枝与推理能力关系（Round 8 已提出，仍缺失）\n\n---\n\n## External Review\n\n**状态**: 未请求（not_requested）\n\n---\n\n## Visual Layout Check\n\n**状态**: Agent 错误（rate limit hit）\n- 视觉审查 Agent 因 rate limit 退出，未产出有效 findings\n- 建议后续手动检查或重试\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 (Findings)**\n**Confidence: 4/5**\n**双 Reviewer 一致**\n\n### 评分理由\n\n**为什么不是 3.5+ (Conference)**:\n- 核心方法贡献 RASP 被自身消融否定——论文的方法新颖性基本为零\n- 乘法形式缺少加法对照，无法判断核心消融结论的归因\n- RASP 全部 α 变体单 seed，dose-response 结论统计不可靠\n- 跨架构泛化严重不足（连续 5 轮未解决）\n- Decoupling 可能是 SFT 天花板 artifact（未排除）\n\n**为什么不是 2.5 (Borderline Findings)**:\n- 受控实验设计哲学在 pruning 文献中有方法论价值\n- Reward-accuracy decoupling 即使是初步发现也对 RLVR 社区有参考价值\n- 核心比较（CKA-only vs Standard）有 3-seed 统计验证\n- 写作质量高，再现性好\n- Training dynamics 多维分析工具有独立价值\n\n### 修改路径建议（如目标 Findings 接收）\n\n1. **必做**: 重新定位为 empirical study；RASP 降级为 exploratory analysis\n2. **必做**: Title 限定为具体架构或加 \"A Case Study\"\n3. **强烈建议**: 跑 additive baseline（成本低），α=2.0 至少 3 seeds\n4. **强烈建议**: 统一 Random max_completion_length=1024\n5. **建议**: 正文 Discussion 扩充；诚实标注 12-15% 实际压缩比\n\n---\n\n## Detailed Comments\n\n### 给作者的核心建议\n\n本文最大的问题不是实验不够多，而是**定位错误**。当前论文试图同时作为 method paper（RASP）和 empirical study（spectrum + decoupling），但数据明确否定了 RASP 的方法贡献。如果重新定位为纯 empirical study——\"受控实验揭示 CKA-based diversity preservation 是 RLVR recovery 的关键因素，且 reward 信号与 accuracy 解耦\"——现有数据足以支撑 Findings 级别的贡献。\n\n具体来说：\n- Section 3.3 的 RASP 公式推导可保留但作为 \"exploration of criterion combination\" 而非核心方法贡献\n- Abstract 的第一句应改为 empirical finding 而非 method proposal\n- 核心贡献列表应以 controlled experiment framework 和 decoupling finding 为主\n\n### Reviewer 交叉共识度\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| RASP 全空间否定 | Critical (N1) | Critical (C2) | 完全一致 |\n| 乘法 vs 加法 | Critical (N2) | AGREE | 完全一致 |\n| 单 seed 不可靠 | Critical (N4) | Critical (强烈同意) | 完全一致 |\n| Random 超参不一致 | Critical (N3) | Warning (nuance) | 方向一致，严重程度小分歧 |\n| SFT 天花板 | Warning (隐含) | Critical (C1) | 方向一致，R2 更强硬 |\n| 有效窗口窄 | Warning (W2/W3) | Critical (C3) | 方向一致，R2 更强硬 |\n| TOST ε=2pp | Warning (W1) | AGREE | 一致 |\n| 25% sparsity | Warning (W3) | REBUT (非核心) | 小分歧 |\n| Calibration M=512 | Warning (W6) | REBUT (标准做法) | 小分歧 |\n\n交叉回应后无未解决的重大矛盾。",
  "project": "recovery_aware_struct_prune",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 Findings",
  "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 9 审稿报告\n\n**Venue**: EMNLP 2026 (via ARR)\n**论文**: \"How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs\"\n**评审人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性）\n**模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文提出 RASP（Recovery-Aware Structured Pruning），通过乘法形式结合 importance score 和 CKA-based diversity score 进行 MLP 结构化剪枝，并系统研究不同剪枝标准对 GRPO 恢复训练的影响。核心发现是 \"recovery capacity spectrum\"（CKA-only > RASP > Random > Standard）和 \"reward-accuracy decoupling\"（GRPO 提升 reward 但 accuracy 改变 <1pp）。\n\n然而，RASP 方法被自身消融实验否定：CKA-only（RASP 的 α→∞ 极端情况）在 recovery capacity 上与 RASP 最优配置（α=2.0）完全相同（Peak Rew = 0.354），而 accuracy 差异仅 1.72pp（单 seed，不可信）。论文最终推荐 CKA-only 而非 RASP——方法贡献不成立。\n\n---\n\n## Strengths\n\n**S1** [双 Reviewer 共识] 受控实验设计理念在 pruning 文献中罕见——isolation design 使得 criterion effect 可比较。实验设计哲学值得推广。\n\n**S2** [双 Reviewer 共识] Reward-accuracy decoupling 是 genuinely surprising 的实证发现，对 RLVR 社区理解 post-pruning RL recovery 有参考价值。\n\n**S3** [Reviewer 1] f₀/gradient norm/KL divergence 等多维训练动态分析工具有独立价值，提供了比 final accuracy 更丰富的诊断视角。\n\n**S4** [Reviewer 1] 跨模型（Qwen2.5-Math-7B SFT）、跨尺度（1.5B）验证展示了系统性 validation 意识，即使覆盖面有限。\n\n**S5** [Reviewer 2] Recovery capacity spectrum 作为描述性框架有参考价值（即使 RASP 贡献不成立）。\n\n**S6** [双 Reviewer 共识] 写作清晰，Figure 2 有效传达实验设计，超参数报告详尽，代码已匿名开源。Reproducibility 评 4/5。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**C1** [双 Reviewer 共识] **RASP 方法贡献被全参数空间否定**\n- α=1.0（名义\"平衡\"点）：reward collapse（Peak Rew 0.061，四方法最差）\n- α=2.0（最优配置）：Peak Rew = CKA-only Peak Rew = 0.354（完全相同）；accuracy +1.72pp 为单 seed 不可信\n- α→∞：即 CKA-only 本身\n- 论文最终推荐 CKA-only 而非 RASP——当提出的方法被其自身特例超越时，方法贡献不成立\n- **影响**: 论文定位需从 \"method paper\" 转为 \"empirical study\"\n\n**C2** [双 Reviewer 共识] **乘法形式 I(h)=0 退化未与加法替代对比**\n- $S_{RASP}(h) = I(h) \\times (1-F(h))^\\alpha$ 意味着 $I(h)=0$ 的结构无论 diversity 多高都被零化\n- 这恰恰是 α=1.0 collapse 的可能机制——高 diversity 但低 importance 的结构被不当移除\n- 加法形式 $S = \\beta \\cdot I(h) + (1-\\beta) \\cdot (1-F(h))$ 不存在此退化，是自然的 ablation 对照\n- 缺少此对照无法判断 collapse 是乘法 artifact 还是 tradeoff 本质\n- 先例存在：Molchanov et al. (2019) \"Importance Estimation for Neural Network Pruning\"\n\n**C3** [双 Reviewer 共识] **RASP 全部 α 变体仅单 seed，dose-response 曲线不可靠**\n- CKA-only/Standard/Random 各 3 seeds，但 RASP 全部 α 值（0.5-4.0）均单 seed\n- Inverted-U 结论完全基于单次运行\n- α=2.0 的 66.11% vs CKA-only 64.39±0.19% 的 1.72pp 差距：RASP 方差未知\n- 如果 RASP 方差与 CKA-only 相当（~0.19pp），1.72pp 可能显著；但 RASP 跨 α 表现巨变（从 collapse 到 66%）暗示高方差\n- **连续 5 轮 Critical 未解决**（Round 5 至今）\n\n**C4** [Reviewer 2, R1 部分同意] **Reward-accuracy decoupling 可能是 SFT 天花板效应 artifact**\n- SFT 已恢复 ~60pp accuracy（从 post-prune ~4% 到 ~64%），GRPO 无 headroom\n- 15% sparsity 数据自相矛盾：GRPO amplifies CKA-only vs Standard gap (+1.51pp)，说明低 sparsity 下 GRPO 确实能放大差异——暗示 20% 下的 \"decoupling\" 是 headroom 耗尽\n- 需消融实验：在 SFT 恢复不充分条件下验证 GRPO 是否产生 accuracy 差异\n\n**C5** [双 Reviewer 共识] **Cross-architecture 泛化严重不足——所有模型共享 Qwen2.5 base**\n- Title 用 \"Reasoning LLMs\"（复数）但仅验证 Qwen2.5 架构族\n- Qwen2.5-Math-7B 仅有 SFT 验证，GRPO 缺失\n- 1.5B 同属 Qwen2.5 family（跨尺度但非跨架构）\n- **连续 5 轮 Critical 未解决**（Round 5 至今）\n\n### Warning\n\n**W1** [双 Reviewer 共识] Random baseline max_completion_length=512 vs 其他方法 1024，违反受控设计自称的 \"hold everything else constant\"。核心 CKA vs Standard 比较不受影响，但 spectrum 含 Random 的排序不可信。\n\n**W2** [双 Reviewer 共识] TOST ε=2pp 缺乏 a priori justification。如果 ε=1pp，部分 \"等价\" 结论不成立。需引用文献或 power analysis 论证 2pp 的实际意义。\n\n**W3** [Reviewer 1, R2 同意] 15% sparsity 下 GRPO 放大 CKA 优势（+1.51pp），Standard Δ=-0.93pp 接近 1pp 边界——decoupling 并非在所有 \"moderate sparsity\" 下普遍成立。\n\n**W4** [Reviewer 1, R2 同意] 300-step extended training 仅报告终值（100 步和 300 步），缺少中间步骤 accuracy trajectory。300 步远少于 RLVR 文献常见预算（1000-5000 步）。\n\n**W5** [Reviewer 2] Title/叙事焦点与 SFT-dominant 发现错位——SFT 贡献 ~60pp 恢复而 GRPO <1pp，但叙事聚焦 GRPO。\n\n**W6** [Reviewer 2] Ji et al. (2026) 对比 overclaiming——实验设置差异未充分讨论。\n\n**W7** [Reviewer 2] Discussion 被放 Appendix，正文 Section 5 仅约 7-8 行，缺少 spectrum 部署指导意义和机制解释。\n\n**W8** [Reviewer 1, R2 同意] Limitations 关于 Random seed 的表述（称 \"单 seed\"）与正文矛盾（实际 3 seeds）。此类不一致降低审稿人对其他声称的信任度。\n\n**W9** [Reviewer 2] 有效窗口仅 20-25% MLP sparsity（实际压缩比约 12-15%），30% 全面崩塌。Abstract 用 \"moderate sparsity\" 模糊处理。论文定位 controlled study 可接受，但需诚实面对实用限制。\n\n### Minor\n\n**M1** [Reviewer 1, R2 同意] Recovery capacity 概念先用后定义——Section 1 使用该术语但 Section 3 才定义。\n\n**M2** [Reviewer 1] Calibration M=512 importance score 稳定性未独立验证（CKA ranking 稳定性已验证但 importance 未验证）。R2 部分反驳：Taylor expansion 是标准做法，M=512 超过 LLM-Pruner 的 calibration 规模。\n\n**M3** [Reviewer 1, R2 同意] 25% sparsity 单 seed，Standard Δ=+0.99pp 恰在 1pp 边界。R2 反驳严重程度：25% 非核心 claim 支撑。\n\n---\n\n## Questions\n\nQ1: 如果跑 additive baseline $S = \\beta \\cdot I(h) + (1-\\beta) \\cdot (1-F(h))$，α=1.0 对应配置是否仍 collapse？这将判定 collapse 归因于乘法 artifact 还是 tradeoff 本质。\n\nQ2: 如果 α=2.0 补跑 3 seeds 方差很大（e.g., σ>1pp），RASP 相关叙事是否需要全部删除？\n\nQ3: 在 SFT 步数减少（如仅 50% SFT steps）的条件下，GRPO 是否能产生显著 accuracy 差异？这将验证 decoupling 是否为天花板效应。\n\nQ4: 为什么不统一 Random 的 max_completion_length 为 1024？成本极低（单 seed 约几小时 GPU）。\n\nQ5: 15% sparsity 下 GRPO 放大差异与 20% 下 decoupling 的矛盾如何解释？\n\nQ6: Extended training 150-200 步的 accuracy 曲线是否可用？\n\n---\n\n## Missing References\n\n1. **Molchanov et al. (2019)** \"Importance Estimation for Neural Network Pruning\" — 加法形式多标准组合先例，直接相关于 RASP vs additive 对比\n2. **Li et al. (2025, arXiv:2504.02010)** \"When Reasoning Meets Compression\" — 直接 benchmark 剪枝对 DeepSeek-R1 推理影响（Round 8 已提出，仍缺失）\n3. **\"Can Pruning Improve Reasoning?\" (2025, arXiv:2505.14582)** — 剪枝与推理能力关系（Round 8 已提出，仍缺失）\n\n---\n\n## External Review\n\n**状态**: 未请求（not_requested）\n\n---\n\n## Visual Layout Check\n\n**状态**: Agent 错误（rate limit hit）\n- 视觉审查 Agent 因 rate limit 退出，未产出有效 findings\n- 建议后续手动检查或重试\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 (Findings)**\n**Confidence: 4/5**\n**双 Reviewer 一致**\n\n### 评分理由\n\n**为什么不是 3.5+ (Conference)**:\n- 核心方法贡献 RASP 被自身消融否定——论文的方法新颖性基本为零\n- 乘法形式缺少加法对照，无法判断核心消融结论的归因\n- RASP 全部 α 变体单 seed，dose-response 结论统计不可靠\n- 跨架构泛化严重不足（连续 5 轮未解决）\n- Decoupling 可能是 SFT 天花板 artifact（未排除）\n\n**为什么不是 2.5 (Borderline Findings)**:\n- 受控实验设计哲学在 pruning 文献中有方法论价值\n- Reward-accuracy decoupling 即使是初步发现也对 RLVR 社区有参考价值\n- 核心比较（CKA-only vs Standard）有 3-seed 统计验证\n- 写作质量高，再现性好\n- Training dynamics 多维分析工具有独立价值\n\n### 修改路径建议（如目标 Findings 接收）\n\n1. **必做**: 重新定位为 empirical study；RASP 降级为 exploratory analysis\n2. **必做**: Title 限定为具体架构或加 \"A Case Study\"\n3. **强烈建议**: 跑 additive baseline（成本低），α=2.0 至少 3 seeds\n4. **强烈建议**: 统一 Random max_completion_length=1024\n5. **建议**: 正文 Discussion 扩充；诚实标注 12-15% 实际压缩比\n\n---\n\n## Detailed Comments\n\n### 给作者的核心建议\n\n本文最大的问题不是实验不够多，而是**定位错误**。当前论文试图同时作为 method paper（RASP）和 empirical study（spectrum + decoupling），但数据明确否定了 RASP 的方法贡献。如果重新定位为纯 empirical study——\"受控实验揭示 CKA-based diversity preservation 是 RLVR recovery 的关键因素，且 reward 信号与 accuracy 解耦\"——现有数据足以支撑 Findings 级别的贡献。\n\n具体来说：\n- Section 3.3 的 RASP 公式推导可保留但作为 \"exploration of criterion combination\" 而非核心方法贡献\n- Abstract 的第一句应改为 empirical finding 而非 method proposal\n- 核心贡献列表应以 controlled experiment framework 和 decoupling finding 为主\n\n### Reviewer 交叉共识度\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| RASP 全空间否定 | Critical (N1) | Critical (C2) | 完全一致 |\n| 乘法 vs 加法 | Critical (N2) | AGREE | 完全一致 |\n| 单 seed 不可靠 | Critical (N4) | Critical (强烈同意) | 完全一致 |\n| Random 超参不一致 | Critical (N3) | Warning (nuance) | 方向一致，严重程度小分歧 |\n| SFT 天花板 | Warning (隐含) | Critical (C1) | 方向一致，R2 更强硬 |\n| 有效窗口窄 | Warning (W2/W3) | Critical (C3) | 方向一致，R2 更强硬 |\n| TOST ε=2pp | Warning (W1) | AGREE | 一致 |\n| 25% sparsity | Warning (W3) | REBUT (非核心) | 小分歧 |\n| Calibration M=512 | Warning (W6) | REBUT (标准做法) | 小分歧 |\n\n交叉回应后无未解决的重大矛盾。",
    "project": "recovery_aware_struct_prune",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 Findings",
    "review_chat_id": "oc_40839c097b00df44480b45ab767f59cf"
  }
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-25T21:33:52.033691+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_04e6cf8fe41be27a49d5657e80962f12:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3763
}
```

</details>

---


### Assistant

_source line 736 · 2026-05-25T21:33:59.912527+00:00_

Round 9 审稿完成。

**最终评分：3.0 (Findings)**，双 Reviewer 一致。

核心判定：
- RASP 方法贡献被全参数空间否定（5 个 Critical 中 3 个直接针对 RASP）
- 论文需从 method paper 重新定位为 empirical study
- 受控实验框架和 decoupling 发现仍有 Findings 级别价值

报告已投递给 Research Director，Issue Tracker 已同步更新（新增 R9-N1~N3, R9-W1~W4, R9-M1；多个历史 issue 更新 last_seen_round=9）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 737 · 2026-05-25T21:34:00.948313+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。逐条回应了 R1 的 N1-N4 和 W1-W6：

- **N1/N2/N4**：全部 AGREE，与我的 N2 形成互补——R1 从 "论文推荐 CKA-only 否定 RASP" 和 "乘法退化" 角度，我从 "α=2.0 CKA-dominant" 角度，共同否定 RASP 的方法贡献
- **N3**（Random 超参不一致）：AGREE with nuance——违反控制原则但不太可能翻转 spectrum ordering
- **W3**：REBUT——25% 单 seed 问题真实但非核心 claim 支撑
- **W6**：REBUT——Appendix H 的 CKA 稳定性数据和 Taylor expansion 文献标准提供了间接支持

维持 Overall 3.0（Findings）不变。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

### Critical 问题

**[AGREE with nuance] R2-C1: Decoupling 可能是 SFT 天花板效应的 artifact**
- 同意需要排除此替代解释，但 CKA-only reward 从 0.15 升至 0.354 说明模型在 RL 意义上 IS learning，只是不反映在 accuracy 上——这超出简单 ceiling 能解释的范围
- 与我的 N1/N2 互补：C1 质疑 decoupling 是否真实，N1/N2 质疑 RASP 是否有贡献
- 建议作者做 "SFT under-trained + GRPO" 消融（如 0.5 epoch SFT 后接 GRPO），观察有 headroom 时 GRPO 能否提升 accuracy

**[AGREE] R2-C2: RASP α=2.0 本质是 CKA-dominant**
- 完全同意，与我的 N1 一致。α=0.5→1.0→2.0 的趋势（Table 5）说明只有 diversity overwhelm importance 时才恢复——这不是"平衡"，是 importance 在拖后腿
- 强化了我 N2 的论点：additive baseline 可能证实 importance 的贡献是 marginal 的

**[PARTIALLY AGREE] R2-C3: 有效窗口仅 20-25%，实用价值受限**
- R2 的压缩比估计偏低：论文报告 19% 参数减少、28% 显存减少（非 12-15%）
- 不构成 reject 级别问题——如果论文定位为 scientific study（理解 pruning→RL 交互），压缩比不是核心评判标准
- 但 Abstract 的 "moderate sparsity" 确实应明确标注

### Warning 问题

**[AGREE] R2-W1**: Title/叙事错位——核心发现是 SFT-dominant 但标题暗示 RLVR-centric
**[CANNOT FULLY EVALUATE] R2-W2**: 需 R2 指出具体 overclaiming 句子
**[AGREE] R2-W3**: 三个模型均为 Qwen2.5 家族，generalization 受限
**[AGREE] R2-W4**: Math-7B GRPO 缺失，与我的观察一致
**[PARTIALLY AGREE] R2-W5**: Discussion 放 Appendix 常见但本文反直觉发现需更多主文讨论
**[PARTIALLY AGREE] R2-W6**: Spectrum 的诊断工具价值未被充分阐述

### 综合评估

R2 与我评分一致（3.0），critical issues 互补——我聚焦方法设计和实验控制，R2 聚焦解释层面和 impact。共同指向：empirical finding 有价值但需更强证据，method contribution 不成立，应定位为 controlled empirical study。

如果作者能 (1) 补 additive baseline, (2) 修 Random max_len, (3) α=2.0 补 3 seeds, (4) 做 SFT under-trained 消融——有潜力升至 3.5，当前 3.0。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：R2 和我从不同角度审查，结论高度一致——**Overall 3.0 (Findings)**。我的 N1-N4 指出方法和实验控制缺陷，R2 的 C1/C3 指出解释和 impact 限制。两组问题互补，共同指向论文应重新定位为 empirical study 而非 method paper。最大分歧在 C3（实用价值）：R2 担忧压缩比过低，我认为 scientific study 不应以压缩比为主要标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 738 · 2026-05-25T21:34:11.000514+00:00_

Round 9 审稿流程已完成。报告已投递至 Research Director。

**最终结论**: 双 Reviewer 一致 3.0 (Findings)，核心共识是 RASP 方法贡献不成立（全参数空间否定），论文应重新定位为 empirical study。唯一轻微分歧在 C3 实用价值（R2 更担忧压缩比，R1 认为 scientific study 不以此为标准）——不影响最终评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:director"
}
```

</details>

---
