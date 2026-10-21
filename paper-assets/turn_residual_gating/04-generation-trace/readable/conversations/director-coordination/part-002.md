# Director coordination — Part 2 of 2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination.md) · [Structured JSON](../../../sessions/1a/1ad2ecd083aa9ebb6dd0.json)

## Round 23

### Tool call

_source line 288 · 2026-05-22T23:09:51.603103+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 4 (Fresh Re-Review)\n\n**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\n**目标 venue**：EMNLP 2026 (ARR May cycle, Long paper)\n**Reviewer 编排**：2 人（R1: 方法严谨性+实验设计 / R2: 新颖性+写作完整性）\n**审稿模式**：Fresh（无上轮记忆）\n\n---\n\n## Summary\n\n本文提出 ThreadGate，一种在 transformer 每层残差路径上添加 content-and-turn-conditioned MLP gate 的方法，目标是恢复多轮对话中衰减的 system prompt 注意力（GAR）。通过五路对照实验（ThreadGate / +PCGrad / Uniform Gate / LoRA-only / Base），作者发现 teacher-forced GAR 收敛至 0.50，但自回归生成时坍塌至 0.015–0.025（20–33× gap）。论文通过 PCGrad 排除梯度方向冲突、gate 值分析排除架构缺陷，将失败归因于 exposure bias。β-steering（β=5）在推理时恢复 GAR 至 0.727，scheduled sampling（单 seed）将 gap 从 31× 压缩至 1.57×。跨模型验证在 Llama-3.1-8B 上确认了 27× gap。\n\n---\n\n## Strengths\n\n**S1. 实验设计严谨的五路对照框架。** 每对配置精确隔离一个因素（turn conditioning / gating mechanism / gradient conflict / fine-tuning），逻辑链条清晰。PCGrad 排除实验遵循 modus tollens 推理范式。[R1, R2 共识]\n\n**S2. 负面结果的诚实报告与深入诊断。** 论文系统追溯失败机制：gate 值反转（§5.1, 27/28 layers, Wilcoxon p=3.73×10⁻⁸）→ 排除梯度冲突（§5.2）→ 分布偏移归因（§5.3）→ 机制特异性确认（§5.4）→ 跨模型泛化（§5.5）。诊断深度在负面结果论文中少见。[R1, R2 共识]\n\n**S3. Exposure bias 对辅助注意力损失的选择性破坏是有价值的发现。** 先前 exposure bias 文献聚焦于主生成目标的质量退化。本文展示 exposure bias 可选择性摧毁辅助注意力目标（GAR 20–33× 坍塌），同时保留主任务（NTP/PPL 不变）。[R2 强调新颖性；R1 认为可预见性较强——见 Divergence]\n\n**S4. β-steering 实验提供建设性证据。** 通过直接操控注意力 logits 恢复 GAR（0.064→0.727），有效区分\"表征退化\"和\"注意力路由失败\"。N=50 验证增强可信度。[R1, R2 共识]\n\n**S5. 写作中 scoping hedges 使用得当。** 频繁使用 \"under the tested conditions\", \"consistent with our evidence\", \"proximal cause\" 等限定语。Limitations 章节全面诚实。[R2 正面评价]\n\n**S6. β steering phase transition（β=2→3 跳变）是有趣发现。** [R1 正面评价]\n\n---\n\n## Weaknesses\n\n### Critical Must-Fix（3 项，影响接收决定）\n\n**C1. 自回归评估样本量严重不足（N=5）** [R1-N1, R2 确认]\n- 核心发现（TF GAR 0.50 → AR GAR 0.015-0.025）完全基于 Qwen 上 5 条自回归对话。N=5 无法提供有意义的统计推断力。0.015 vs 0.025（ThreadGate vs LoRA-only）的差异无法判断统计显著性。Llama AR 评估同样使用 N=5 pilot（§5.5 提到 N=20 mid-turn 但含义模糊）。\n- **要求**：AR 评估扩展到 N≥50；报告 bootstrap 95% CI；条件间做成对显著性检验。\n\n**C2. Scheduled sampling 结果承载过重但仅单 seed** [R1-N3/W3, R2-N2]\n- SS 是论文中唯一展示 training-time mitigation 可行性的证据，在 abstract、contribution (2)、discussion、conclusion 中均被引用。但仅基于单 seed，且两个 seed（GAR 0.318 vs 0.418，即 gap 1.57× vs 1.20×）差异达 31%，说明方差极高。Abstract 以确定性语气呈现（\"compresses the gap to 1.57×\"）存在 overclaim。\n- **要求**：至少 3 seeds + mean±std；abstract/conclusion 标注 \"preliminary\" 或弱化措辞。\n\n**C3. GAR 指标与下游任务性能缺乏因果验证** [R2-N1, R1-W4]\n- 论文核心叙事建立在 GAR 之上，但从未验证 GAR 提升是否改善指令遵循质量。唯一下游评估（Appendix C instruction retention）McNemar p=0.077 不显著、r=0.200。β=10 时 PPL 退化到 4.22 说明 GAR 极端提升可能有害。所有 fine-tuned variants PPL≈2.78 且残差流 AUC≈0.98，GAR 改善与生成质量脱节。\n- R1 认为 GAR-PPL 脱节是 Should-Fix，R2 将其升级为 Critical——Director 裁定为 **Critical**，因为这影响论文核心 claim 的实际意义。\n- **要求**：在 β=0/3/5 条件下评估实际指令遵循质量（IFEval/MT-Bench/自定义 compliance metric）；若无法完成，需在论文中明确承认局限并显著降低 claim 强度。\n\n### Should-Fix（7 项，影响评分但不一票否决）\n\n**S1. Exposure bias 归因缺乏替代假说排除** [R1-N2 Critical, R2-M4 Minor → Director 裁定 Should-Fix]\n- §6 承认 KV cache drift 未排除，§8 留给 future work。对宣称 \"mechanistic analysis\" 的论文，将核心替代假说完全留给 future work 不够充分。但论文已使用 \"proximal cause\" 等 hedging 语言，且 R2 认为在 scoping 存在的情况下可接受。\n- **建议**：设计 TF→AR 切换实验（teacher-forced prefix 到第 k 轮后切换 AR，观察 GAR 退化转折点），或在 §6 用 2-3 句话更充分讨论为什么当前证据倾向 exposure bias 而非 KV cache drift。\n\n**S2. 标题误导 + 副标题 overclaim** [R2-W1, R1-W2]\n- 标题 \"Why Per-Layer Residual Gating Fails\" 暗示 gating 固有失败，但 LoRA-only（无 gate）表现完全相同——真正的发现是 TF 辅助损失在 AR 下通用失效。\"Mechanistic Analysis\" 副标题与实际分析深度（宏观层面而非 circuit-level）不匹配。\n- **建议**：标题更准确反映 exposure bias 核心发现；副标题改为 \"Diagnostic Analysis\"。\n\n**S3. 跨模型验证不完整** [R1-W1, R2-W4]\n- Llama 仅覆盖 3/5 条件（缺 PCGrad + Uniform Gate）。仅两个 7-8B 模型家族。§5.5 使用 median 而主实验使用 mean，有 metric selection 之嫌。§5.5 标题 \"Cross-Model Generality\" 暗示过强。\n- **建议**：补齐 Llama 5-way；mean/median 双报；标题改为 \"Cross-Model Replication\"。\n\n**S4. 缺少与直接竞争者的实验对比** [R2-W2]\n- Split-softmax (Li et al. 2024) 和 Rhea (Hong et al. 2025) 在 related work 中被讨论但无实验对比。论文声称它们 \"cannot address exposure bias\" 但缺乏实验验证。\n- **建议**：至少在一个模型上运行 split-softmax baseline，或明确承认缺乏对比是局限。\n\n**S5. \"To our knowledge, the first\" 声称不可证伪** [R2-W3]\n- Contribution (2) 的 \"first\" 声称过于狭窄（niche 太窄导致不可证伪），不增加实际新颖性论证。\n- **建议**：删除 \"first\" 修饰语，直接陈述贡献内容。\n\n**S6. 关键数字重复过多** [R2-W5]\n- \"20-33× gap\" 在论文中出现至少 7 次，\"0.064 to 0.727\" 出现 4+ 次。降低信息密度，给人 padding 感。\n- **建议**：abstract/核心结果保留精确数字，后续用 \"the TF-AR gap (Table 1)\" 回指。\n\n**S7. 无代码/数据发布承诺** [R1, R2]\n- 负面结果论文可复现性是最后防线。ARR reproducibility 评分受影响。\n- **建议**：投稿时附匿名 GitHub repo。\n\n### Minor（8 项）\n\n- **M1**: GAR-D 全条件接近零（TF 下 ThreadGate GAR-D = 0.02），干预仅在 τ-masked last token 成功，泛化性未讨论 [R1-W5]\n- **M2**: Table 1 精度与正文不一致——§4.2 称 spread 0.75pp 但表格两位小数显示 1pp [R2-W6]\n- **M3**: r_min 数值正文未报告 [R1-M1]\n- **M4**: Table 1 AR 列缺 GAR-D 和 PPL [R1-M2]\n- **M5**: Abstract 过密（约 180 词），首次阅读难以消化 [R2-M1]\n- **M6**: §7 Conclusion 仅 3 句话，可能过于简短 [R2-M5]\n- **M7**: Bib 格式不一致——Raposo et al. 2024 应更新为 ICML @inproceedings；Gromov et al. 年份需确认 [R2-M3]\n- **M8**: Figure 4/6 双栏打印尺寸下辨认困难，Figure 5 (c)(d) y 轴标签重叠 [R1-M4, 视觉审查]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **N=5 AR 样本量不可接受**——两位 Reviewer 独立列为 Critical Must-Fix，无分歧\n2. **Scheduled sampling 单 seed 不可靠**——两位 Reviewer 均列为 Critical/高优先 Warning\n3. **五路对照设计原则上严谨**——两位 Reviewer 均列为核心 Strength\n4. **诊断链完整性**——两位 Reviewer 均认可 gate reversal → PCGrad exclusion → distribution shift → TRC 证据链\n5. **跨模型验证不完整**——两位均指出 Llama 3/5 条件是弱点\n6. **代码未发布**——两位均提出\n7. **关键数字重复过多**——两位均注意到 \"20-33×\" 出现过多次\n\n## Reviewer Divergence [REBUT]\n\n1. **Exposure bias 新颖性**：R1 认为 \"可预见性较强\"（Excitement 3/5），R2 认为 \"真正新颖的发现——先前文献未系统研究 exposure bias 对辅助注意力损失的选择性破坏\"（Excitement 3/5，但 S3 强调了具体贡献）。\n   - **Director 裁定**：R2 的论证更有说服力——虽然 exposure bias 本身是已知现象，但对辅助注意力损失的选择性破坏（主任务 PPL 不变而 GAR 坍塌 20-33×）确实是文献中未被系统研究的方面。但新颖性受限于缺乏下游验证（C3）。\n\n2. **KV cache drift 严重性**：R1 列 Critical（核心因果声明漏洞），R2 列 Minor（scoping hedges 存在即可）。\n   - **Director 裁定**：Should-Fix（S1）。论文已使用 \"proximal cause\" 等 hedging 语言，但对自称 \"mechanistic analysis\" 的论文，完全不排除替代假说仍是弱点。需要更充分讨论，但不必强制要求新实验。\n\n3. **GAR 下游验证严重性**：R2 列 Critical，R1 列 Should-Fix。\n   - **Director 裁定**：Critical（C3）。GAR 是整个论文的核心指标，缺乏下游验证影响论文实际意义。\n\n---\n\n## Questions to Authors\n\n1. Table 1 中 LoRA-only AR GAR (0.025) 高于所有 gating variants (0.015-0.016)。这是否意味着 gate 在推理时略微有害？多 seed 下是否稳定？\n2. β-steering 中 N=5 baseline GAR=0.028 vs N=50 baseline GAR=0.064，差异超过 2×。GAR 对对话长度是否高度敏感？这是否削弱跨设置可比性？\n3. Scheduled sampling 两 seed 间 AR GAR 相差 31%（0.318 vs 0.418）。方差来源是什么？是否暗示效果对初始化敏感？\n4. 是否尝试过更高 LoRA rank（64/128）？gate 无效性是否可能部分归因于 LoRA 容量已饱和？\n5. Teacher-forced prefix 到第 k 轮后切换 AR，GAR 退化临界 k 是多少？这一实验可区分 exposure bias 和 KV cache drift。\n6. r_min 具体数值是多少？\n7. 是否计划开源代码？\n\n---\n\n## Missing References\n\n1. **Zhang et al. (2024) \"Tell Your Model Where to Attend\"** — 推理时注意力操控方法，与 β-steering 思路相似，应在 §2 讨论 [R2]\n2. **Multi-turn instruction following benchmarks** (IFEval multi-turn variant, MT-Bench) — 论文缺少标准化下游评估 [R2]\n3. **Raposo et al. (2024)** Mixture-of-Depths — bib 条目应更新为 ICML 2024 正式版本 [R2]\n4. 需核实 Dongre et al. GAR 全称——论文使用 \"Goal Attention Ratio\"，arXiv 原文应为 \"Goal Accessibility Ratio\"（跨轮遗留问题） [历史追踪]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未请求。本轮未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（0 critical, 3 warning, 10 info）\n\n主要发现：\n- **[warning]** Page 3-4 连续两页无 figure/table，纯文本感较强\n- **[warning]** Page 7 视觉密度最高——Figure 5 (c)(d) y 轴标签重叠或过于密集，在 150dpi 下已显拥挤\n- **[warning]** Page 13 Figure 10 caption 与 Table 3 之间有约 1/3 页空白\n- **[info]** Figure 1 右侧 \"Mechanism analysis\" 区域文字偏小（约 6-7pt），打印/低分辨率下难辨认\n- **[info]** Figure 4 bar chart 层号标签字号极小（约 5-6pt）\n- **[info]** 无 [?] 未解析引用，色彩语义一致性好，booktabs 风格表格专业\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings**\n\n**Reviewer 评分**：R1 = 3.0 (Findings) / R2 = 3.5 (Borderline Conference)\n**Director 综合评分**：3.0 (Findings)\n\n**理由**：\n\n论文在实验设计上表现出色——五路对照框架、PCGrad 排除、多维度诊断链的完整性在该领域论文中少见。Exposure bias 对辅助注意力损失的选择性破坏（主任务 PPL 不变而 GAR 坍塌 20-33×）是有理论价值的发现。\n\n但论文存在三个 Critical 级别的方法论缺陷阻碍其达到 Conference 水平：\n\n1. **统计基础薄弱**：核心量化证据基于 N=5 AR 评估和单种子实验。5 路对比中仅 ThreadGate 有 2 seeds，其余条件单 seed。Scheduled sampling 两 seed 方差 31%。这些共同导致核心结论（\"gating produces no measurable benefit\"、\"all variants collapse equally\"）缺乏统计可靠性。\n\n2. **GAR 指标未经验证**：整篇论文围绕一个注意力统计量（GAR）展开，但从未证明 GAR 改善对用户可感知的对话质量有意义。唯一的下游评估不显著（p=0.077）。这使得 \"GAR 坍塌 = 失败\" 的核心叙事基础不稳固。\n\n3. **Scheduled sampling 作为独立贡献不成立**：单 seed、高方差、确定性语气呈现。\n\n**修改后预期**：如果补充 (1) N≥50 AR 评估 + 3 seeds 全条件覆盖 + 统计检验，(2) β-steering 条件下的下游指令遵循评估，(3) SS 多 seed 结果，论文可达 3.5–4.0（Borderline Conference 至 Conference）水平。当前状态适合 Findings 接收。\n\n**置信度**：4/5——两位 Reviewer 均有高置信度（4/5），核心问题（统计不足）明确且可操作。\n\n---\n\n## Detailed Comments（逐节）\n\n**Title & Abstract**：标题暗示 gating 固有失败但实际发现是 exposure bias 对 TF 辅助损失的通用问题，存在误导。Abstract 约 180 词，信息密度极高但首次阅读难消化。\"compresses the gap to 1.57×\" 以确定性语气呈现单 seed 结果。\n\n**§1 Introduction**：贡献罗列清晰但 \"to our knowledge, the first\" 声称过于狭窄。关键数字重复从此处开始。\n\n**§2 Related Work**：覆盖较全面，但缺 Zhang et al. (2024) 推理时注意力操控方法。Split-softmax 和 Rhea 仅定性讨论，无实验对比。\n\n**§3 Method**：ThreadGate 设计描述清晰，Eq. 1-7 技术上正确。r_min 数值未报告。UG（Uniform Gate）描述不够清晰——未说明仍为可学习 MLP。\n\n**§4 Experiments**：五路对照设计原则上严谨，但 N=5 AR 评估和单种子严重削弱定量证据。Table 1 精度与正文不一致（spread 0.75pp vs 表格显示 1pp）。AR 列缺 GAR-D 和 PPL。\n\n**§4.3 β-steering**：Phase transition（β=2→3）是有趣发现。N=50 验证增强可信度。但 β=0 baseline GAR 在不同 N 下差异大（0.028 vs 0.064），引发 GAR 对对话长度敏感性的问题。\n\n**§5 Analysis**：诊断链逻辑清晰。§5.1 gate reversal（Wilcoxon p=3.73×10⁻⁸）有说服力。§5.2 PCGrad 排除合理但仅排除 directional conflict（未排除 magnitude imbalance）。§5.3 exposure bias 归因在 hedging 存在时可接受，但 KV cache drift 替代假说讨论不足。§5.5 Llama 仅 3/5 条件，median/mean 混用。\n\n**§6 Discussion**：KV cache drift 仅一句话讨论，不够充分。Instruction retention 段落占篇幅但结果不显著（p=0.077），建议移入 Appendix。\n\n**§7 Conclusion**：仅 3 句话，可适当扩展 future directions。\n\n**§8 Limitations**：全面诚实，符合 EMNLP 规范。\n\n**Format**：页数合规（8 页正文）。匿名性合规。Bib 格式需统一（Raposo et al. 应更新为 ICML 版本）。",
  "project": "turn_residual_gating",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 4 (Fresh Re-Review)\n\n**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\n**目标 venue**：EMNLP 2026 (ARR May cycle, Long paper)\n**Reviewer 编排**：2 人（R1: 方法严谨性+实验设计 / R2: 新颖性+写作完整性）\n**审稿模式**：Fresh（无上轮记忆）\n\n---\n\n## Summary\n\n本文提出 ThreadGate，一种在 transformer 每层残差路径上添加 content-and-turn-conditioned MLP gate 的方法，目标是恢复多轮对话中衰减的 system prompt 注意力（GAR）。通过五路对照实验（ThreadGate / +PCGrad / Uniform Gate / LoRA-only / Base），作者发现 teacher-forced GAR 收敛至 0.50，但自回归生成时坍塌至 0.015–0.025（20–33× gap）。论文通过 PCGrad 排除梯度方向冲突、gate 值分析排除架构缺陷，将失败归因于 exposure bias。β-steering（β=5）在推理时恢复 GAR 至 0.727，scheduled sampling（单 seed）将 gap 从 31× 压缩至 1.57×。跨模型验证在 Llama-3.1-8B 上确认了 27× gap。\n\n---\n\n## Strengths\n\n**S1. 实验设计严谨的五路对照框架。** 每对配置精确隔离一个因素（turn conditioning / gating mechanism / gradient conflict / fine-tuning），逻辑链条清晰。PCGrad 排除实验遵循 modus tollens 推理范式。[R1, R2 共识]\n\n**S2. 负面结果的诚实报告与深入诊断。** 论文系统追溯失败机制：gate 值反转（§5.1, 27/28 layers, Wilcoxon p=3.73×10⁻⁸）→ 排除梯度冲突（§5.2）→ 分布偏移归因（§5.3）→ 机制特异性确认（§5.4）→ 跨模型泛化（§5.5）。诊断深度在负面结果论文中少见。[R1, R2 共识]\n\n**S3. Exposure bias 对辅助注意力损失的选择性破坏是有价值的发现。** 先前 exposure bias 文献聚焦于主生成目标的质量退化。本文展示 exposure bias 可选择性摧毁辅助注意力目标（GAR 20–33× 坍塌），同时保留主任务（NTP/PPL 不变）。[R2 强调新颖性；R1 认为可预见性较强——见 Divergence]\n\n**S4. β-steering 实验提供建设性证据。** 通过直接操控注意力 logits 恢复 GAR（0.064→0.727），有效区分\"表征退化\"和\"注意力路由失败\"。N=50 验证增强可信度。[R1, R2 共识]\n\n**S5. 写作中 scoping hedges 使用得当。** 频繁使用 \"under the tested conditions\", \"consistent with our evidence\", \"proximal cause\" 等限定语。Limitations 章节全面诚实。[R2 正面评价]\n\n**S6. β steering phase transition（β=2→3 跳变）是有趣发现。** [R1 正面评价]\n\n---\n\n## Weaknesses\n\n### Critical Must-Fix（3 项，影响接收决定）\n\n**C1. 自回归评估样本量严重不足（N=5）** [R1-N1, R2 确认]\n- 核心发现（TF GAR 0.50 → AR GAR 0.015-0.025）完全基于 Qwen 上 5 条自回归对话。N=5 无法提供有意义的统计推断力。0.015 vs 0.025（ThreadGate vs LoRA-only）的差异无法判断统计显著性。Llama AR 评估同样使用 N=5 pilot（§5.5 提到 N=20 mid-turn 但含义模糊）。\n- **要求**：AR 评估扩展到 N≥50；报告 bootstrap 95% CI；条件间做成对显著性检验。\n\n**C2. Scheduled sampling 结果承载过重但仅单 seed** [R1-N3/W3, R2-N2]\n- SS 是论文中唯一展示 training-time mitigation 可行性的证据，在 abstract、contribution (2)、discussion、conclusion 中均被引用。但仅基于单 seed，且两个 seed（GAR 0.318 vs 0.418，即 gap 1.57× vs 1.20×）差异达 31%，说明方差极高。Abstract 以确定性语气呈现（\"compresses the gap to 1.57×\"）存在 overclaim。\n- **要求**：至少 3 seeds + mean±std；abstract/conclusion 标注 \"preliminary\" 或弱化措辞。\n\n**C3. GAR 指标与下游任务性能缺乏因果验证** [R2-N1, R1-W4]\n- 论文核心叙事建立在 GAR 之上，但从未验证 GAR 提升是否改善指令遵循质量。唯一下游评估（Appendix C instruction retention）McNemar p=0.077 不显著、r=0.200。β=10 时 PPL 退化到 4.22 说明 GAR 极端提升可能有害。所有 fine-tuned variants PPL≈2.78 且残差流 AUC≈0.98，GAR 改善与生成质量脱节。\n- R1 认为 GAR-PPL 脱节是 Should-Fix，R2 将其升级为 Critical——Director 裁定为 **Critical**，因为这影响论文核心 claim 的实际意义。\n- **要求**：在 β=0/3/5 条件下评估实际指令遵循质量（IFEval/MT-Bench/自定义 compliance metric）；若无法完成，需在论文中明确承认局限并显著降低 claim 强度。\n\n### Should-Fix（7 项，影响评分但不一票否决）\n\n**S1. Exposure bias 归因缺乏替代假说排除** [R1-N2 Critical, R2-M4 Minor → Director 裁定 Should-Fix]\n- §6 承认 KV cache drift 未排除，§8 留给 future work。对宣称 \"mechanistic analysis\" 的论文，将核心替代假说完全留给 future work 不够充分。但论文已使用 \"proximal cause\" 等 hedging 语言，且 R2 认为在 scoping 存在的情况下可接受。\n- **建议**：设计 TF→AR 切换实验（teacher-forced prefix 到第 k 轮后切换 AR，观察 GAR 退化转折点），或在 §6 用 2-3 句话更充分讨论为什么当前证据倾向 exposure bias 而非 KV cache drift。\n\n**S2. 标题误导 + 副标题 overclaim** [R2-W1, R1-W2]\n- 标题 \"Why Per-Layer Residual Gating Fails\" 暗示 gating 固有失败，但 LoRA-only（无 gate）表现完全相同——真正的发现是 TF 辅助损失在 AR 下通用失效。\"Mechanistic Analysis\" 副标题与实际分析深度（宏观层面而非 circuit-level）不匹配。\n- **建议**：标题更准确反映 exposure bias 核心发现；副标题改为 \"Diagnostic Analysis\"。\n\n**S3. 跨模型验证不完整** [R1-W1, R2-W4]\n- Llama 仅覆盖 3/5 条件（缺 PCGrad + Uniform Gate）。仅两个 7-8B 模型家族。§5.5 使用 median 而主实验使用 mean，有 metric selection 之嫌。§5.5 标题 \"Cross-Model Generality\" 暗示过强。\n- **建议**：补齐 Llama 5-way；mean/median 双报；标题改为 \"Cross-Model Replication\"。\n\n**S4. 缺少与直接竞争者的实验对比** [R2-W2]\n- Split-softmax (Li et al. 2024) 和 Rhea (Hong et al. 2025) 在 related work 中被讨论但无实验对比。论文声称它们 \"cannot address exposure bias\" 但缺乏实验验证。\n- **建议**：至少在一个模型上运行 split-softmax baseline，或明确承认缺乏对比是局限。\n\n**S5. \"To our knowledge, the first\" 声称不可证伪** [R2-W3]\n- Contribution (2) 的 \"first\" 声称过于狭窄（niche 太窄导致不可证伪），不增加实际新颖性论证。\n- **建议**：删除 \"first\" 修饰语，直接陈述贡献内容。\n\n**S6. 关键数字重复过多** [R2-W5]\n- \"20-33× gap\" 在论文中出现至少 7 次，\"0.064 to 0.727\" 出现 4+ 次。降低信息密度，给人 padding 感。\n- **建议**：abstract/核心结果保留精确数字，后续用 \"the TF-AR gap (Table 1)\" 回指。\n\n**S7. 无代码/数据发布承诺** [R1, R2]\n- 负面结果论文可复现性是最后防线。ARR reproducibility 评分受影响。\n- **建议**：投稿时附匿名 GitHub repo。\n\n### Minor（8 项）\n\n- **M1**: GAR-D 全条件接近零（TF 下 ThreadGate GAR-D = 0.02），干预仅在 τ-masked last token 成功，泛化性未讨论 [R1-W5]\n- **M2**: Table 1 精度与正文不一致——§4.2 称 spread 0.75pp 但表格两位小数显示 1pp [R2-W6]\n- **M3**: r_min 数值正文未报告 [R1-M1]\n- **M4**: Table 1 AR 列缺 GAR-D 和 PPL [R1-M2]\n- **M5**: Abstract 过密（约 180 词），首次阅读难以消化 [R2-M1]\n- **M6**: §7 Conclusion 仅 3 句话，可能过于简短 [R2-M5]\n- **M7**: Bib 格式不一致——Raposo et al. 2024 应更新为 ICML @inproceedings；Gromov et al. 年份需确认 [R2-M3]\n- **M8**: Figure 4/6 双栏打印尺寸下辨认困难，Figure 5 (c)(d) y 轴标签重叠 [R1-M4, 视觉审查]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **N=5 AR 样本量不可接受**——两位 Reviewer 独立列为 Critical Must-Fix，无分歧\n2. **Scheduled sampling 单 seed 不可靠**——两位 Reviewer 均列为 Critical/高优先 Warning\n3. **五路对照设计原则上严谨**——两位 Reviewer 均列为核心 Strength\n4. **诊断链完整性**——两位 Reviewer 均认可 gate reversal → PCGrad exclusion → distribution shift → TRC 证据链\n5. **跨模型验证不完整**——两位均指出 Llama 3/5 条件是弱点\n6. **代码未发布**——两位均提出\n7. **关键数字重复过多**——两位均注意到 \"20-33×\" 出现过多次\n\n## Reviewer Divergence [REBUT]\n\n1. **Exposure bias 新颖性**：R1 认为 \"可预见性较强\"（Excitement 3/5），R2 认为 \"真正新颖的发现——先前文献未系统研究 exposure bias 对辅助注意力损失的选择性破坏\"（Excitement 3/5，但 S3 强调了具体贡献）。\n   - **Director 裁定**：R2 的论证更有说服力——虽然 exposure bias 本身是已知现象，但对辅助注意力损失的选择性破坏（主任务 PPL 不变而 GAR 坍塌 20-33×）确实是文献中未被系统研究的方面。但新颖性受限于缺乏下游验证（C3）。\n\n2. **KV cache drift 严重性**：R1 列 Critical（核心因果声明漏洞），R2 列 Minor（scoping hedges 存在即可）。\n   - **Director 裁定**：Should-Fix（S1）。论文已使用 \"proximal cause\" 等 hedging 语言，但对自称 \"mechanistic analysis\" 的论文，完全不排除替代假说仍是弱点。需要更充分讨论，但不必强制要求新实验。\n\n3. **GAR 下游验证严重性**：R2 列 Critical，R1 列 Should-Fix。\n   - **Director 裁定**：Critical（C3）。GAR 是整个论文的核心指标，缺乏下游验证影响论文实际意义。\n\n---\n\n## Questions to Authors\n\n1. Table 1 中 LoRA-only AR GAR (0.025) 高于所有 gating variants (0.015-0.016)。这是否意味着 gate 在推理时略微有害？多 seed 下是否稳定？\n2. β-steering 中 N=5 baseline GAR=0.028 vs N=50 baseline GAR=0.064，差异超过 2×。GAR 对对话长度是否高度敏感？这是否削弱跨设置可比性？\n3. Scheduled sampling 两 seed 间 AR GAR 相差 31%（0.318 vs 0.418）。方差来源是什么？是否暗示效果对初始化敏感？\n4. 是否尝试过更高 LoRA rank（64/128）？gate 无效性是否可能部分归因于 LoRA 容量已饱和？\n5. Teacher-forced prefix 到第 k 轮后切换 AR，GAR 退化临界 k 是多少？这一实验可区分 exposure bias 和 KV cache drift。\n6. r_min 具体数值是多少？\n7. 是否计划开源代码？\n\n---\n\n## Missing References\n\n1. **Zhang et al. (2024) \"Tell Your Model Where to Attend\"** — 推理时注意力操控方法，与 β-steering 思路相似，应在 §2 讨论 [R2]\n2. **Multi-turn instruction following benchmarks** (IFEval multi-turn variant, MT-Bench) — 论文缺少标准化下游评估 [R2]\n3. **Raposo et al. (2024)** Mixture-of-Depths — bib 条目应更新为 ICML 2024 正式版本 [R2]\n4. 需核实 Dongre et al. GAR 全称——论文使用 \"Goal Attention Ratio\"，arXiv 原文应为 \"Goal Accessibility Ratio\"（跨轮遗留问题） [历史追踪]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未请求。本轮未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（0 critical, 3 warning, 10 info）\n\n主要发现：\n- **[warning]** Page 3-4 连续两页无 figure/table，纯文本感较强\n- **[warning]** Page 7 视觉密度最高——Figure 5 (c)(d) y 轴标签重叠或过于密集，在 150dpi 下已显拥挤\n- **[warning]** Page 13 Figure 10 caption 与 Table 3 之间有约 1/3 页空白\n- **[info]** Figure 1 右侧 \"Mechanism analysis\" 区域文字偏小（约 6-7pt），打印/低分辨率下难辨认\n- **[info]** Figure 4 bar chart 层号标签字号极小（约 5-6pt）\n- **[info]** 无 [?] 未解析引用，色彩语义一致性好，booktabs 风格表格专业\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings**\n\n**Reviewer 评分**：R1 = 3.0 (Findings) / R2 = 3.5 (Borderline Conference)\n**Director 综合评分**：3.0 (Findings)\n\n**理由**：\n\n论文在实验设计上表现出色——五路对照框架、PCGrad 排除、多维度诊断链的完整性在该领域论文中少见。Exposure bias 对辅助注意力损失的选择性破坏（主任务 PPL 不变而 GAR 坍塌 20-33×）是有理论价值的发现。\n\n但论文存在三个 Critical 级别的方法论缺陷阻碍其达到 Conference 水平：\n\n1. **统计基础薄弱**：核心量化证据基于 N=5 AR 评估和单种子实验。5 路对比中仅 ThreadGate 有 2 seeds，其余条件单 seed。Scheduled sampling 两 seed 方差 31%。这些共同导致核心结论（\"gating produces no measurable benefit\"、\"all variants collapse equally\"）缺乏统计可靠性。\n\n2. **GAR 指标未经验证**：整篇论文围绕一个注意力统计量（GAR）展开，但从未证明 GAR 改善对用户可感知的对话质量有意义。唯一的下游评估不显著（p=0.077）。这使得 \"GAR 坍塌 = 失败\" 的核心叙事基础不稳固。\n\n3. **Scheduled sampling 作为独立贡献不成立**：单 seed、高方差、确定性语气呈现。\n\n**修改后预期**：如果补充 (1) N≥50 AR 评估 + 3 seeds 全条件覆盖 + 统计检验，(2) β-steering 条件下的下游指令遵循评估，(3) SS 多 seed 结果，论文可达 3.5–4.0（Borderline Conference 至 Conference）水平。当前状态适合 Findings 接收。\n\n**置信度**：4/5——两位 Reviewer 均有高置信度（4/5），核心问题（统计不足）明确且可操作。\n\n---\n\n## Detailed Comments（逐节）\n\n**Title & Abstract**：标题暗示 gating 固有失败但实际发现是 exposure bias 对 TF 辅助损失的通用问题，存在误导。Abstract 约 180 词，信息密度极高但首次阅读难消化。\"compresses the gap to 1.57×\" 以确定性语气呈现单 seed 结果。\n\n**§1 Introduction**：贡献罗列清晰但 \"to our knowledge, the first\" 声称过于狭窄。关键数字重复从此处开始。\n\n**§2 Related Work**：覆盖较全面，但缺 Zhang et al. (2024) 推理时注意力操控方法。Split-softmax 和 Rhea 仅定性讨论，无实验对比。\n\n**§3 Method**：ThreadGate 设计描述清晰，Eq. 1-7 技术上正确。r_min 数值未报告。UG（Uniform Gate）描述不够清晰——未说明仍为可学习 MLP。\n\n**§4 Experiments**：五路对照设计原则上严谨，但 N=5 AR 评估和单种子严重削弱定量证据。Table 1 精度与正文不一致（spread 0.75pp vs 表格显示 1pp）。AR 列缺 GAR-D 和 PPL。\n\n**§4.3 β-steering**：Phase transition（β=2→3）是有趣发现。N=50 验证增强可信度。但 β=0 baseline GAR 在不同 N 下差异大（0.028 vs 0.064），引发 GAR 对对话长度敏感性的问题。\n\n**§5 Analysis**：诊断链逻辑清晰。§5.1 gate reversal（Wilcoxon p=3.73×10⁻⁸）有说服力。§5.2 PCGrad 排除合理但仅排除 directional conflict（未排除 magnitude imbalance）。§5.3 exposure bias 归因在 hedging 存在时可接受，但 KV cache drift 替代假说讨论不足。§5.5 Llama 仅 3/5 条件，median/mean 混用。\n\n**§6 Discussion**：KV cache drift 仅一句话讨论，不够充分。Instruction retention 段落占篇幅但结果不显著（p=0.077），建议移入 Appendix。\n\n**§7 Conclusion**：仅 3 句话，可适当扩展 future directions。\n\n**§8 Limitations**：全面诚实，符合 EMNLP 规范。\n\n**Format**：页数合规（8 页正文）。匿名性合规。Bib 格式需统一（Raposo et al. 应更新为 ICML 版本）。",
    "project": "turn_residual_gating",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-22T23:09:55.641965+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4038
}
```

</details>

---


### Assistant

_source line 290 · 2026-05-22T23:10:09.937280+00:00_

审稿报告已投递。

**审稿完成总结：**

- **Overall: 3.0/5 — Findings**（R1: 3.0, R2: 3.5, Director 综合: 3.0）
- **3 个 Critical Must-Fix**：
  1. AR 评估 N=5 统计功效不足——需扩至 N≥50 + 3 seeds 全条件覆盖
  2. Scheduled sampling 单 seed 高方差（两 seed GAR 差 31%）——需 3+ seeds + 弱化 abstract 措辞
  3. GAR 指标缺乏下游任务验证——需 β-steering 条件下的指令遵循评估
- **7 个 Should-Fix**：KV cache drift 排除不足、标题误导、跨模型不完整、缺竞争者对比、"first" 声称不可证伪、数字重复、无代码发布
- **核心判断**：方法论设计严谨的负面结果论文，exposure bias 对辅助注意力目标的选择性破坏有理论价值，但统计基础和 GAR 下游验证是根本弱点。补充统计证据和下游评估后可达 3.5–4.0。

Issue Tracker 已同步更新（Round 4，35 个 issues，13 open / 10 in_progress / 12 resolved）。视觉审查已完成（0 critical, 3 warning）。外部审稿未请求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events


### User

_source line 291 · 2026-05-22T23:10:09.953558+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 交叉回应 Reviewer 2

### Must-Fix

[AGREE] R2-N1 (GAR 缺乏下游验证): 同意且认为比我原本的 W4 更严重。R2 直接引用 Appendix C 的 McNemar p=0.077 和 r=0.200——论文自己的下游验证不显著。如果 GAR 坍塌不等于实际质量下降，整个诊断的动机被削弱。我同意升级为 critical。

[AGREE] R2-N2 (Scheduled sampling 证据不足): 完全同意，与我的 W3 一致。两种子 GAR 差异超 70% 是不可接受的。

### Should-Fix

[AGREE] R2-W1 (标题暗示 gating 特异性失败): 同意，与我的 W2 互补。标题将通用 exposure bias 问题归咎于特定架构。

[REBUT] R2-W2 (缺少 Split-softmax/Rhea 实验对比): 部分不同意。论文是诊断性而非竞争性研究，五路对比隔离自身架构因素已足够。Split-softmax 是推理时方法，Rhea 操作注意力内部——干预层面不同，不构成直接 baseline。加入为 nice-to-have，不应 should-fix。

[AGREE] R2-W3 ("to our knowledge, the first" 不可证伪): 同意。

[REBUT] R2-W4 (仅两个模型家族): 部分不同意。Qwen-2.5-7B 和 Llama-3.1-8B 架构差异显著，两个模型对诊断性论文已构成合理初步证据。更多模型属 future work。但我维持我的 W1（Llama 仅 3/5 条件）——问题不在模型数量而在消融不完整。

[AGREE] R2-W5 (数字重复过多): 同意。
[AGREE] R2-W6 (四舍五入不一致): 同意。

### Minor

R2-M4 (KV cache drift): R2 列为 minor，但我认为应为 critical（我的 N2）。对因果归因论文，未排除的主要替代假说不是小问题。

其余 M1-M3, M5-M6: 全部 AGREE。

### 三个分歧点

**评分差异 (3.5 vs 3.0)**: 差距来自三个问题的严重性判断：(1) N=5 样本量——R2 未列为独立 must-fix，我列为 N1 critical；(2) KV cache drift——R2 列为 minor，我列为 critical；(3) 三个统计弱点叠加后因果声明可信度降至 Findings 水平。我维持 3.0。

**R2-N1 vs R1-W4**: 同一问题，R2 论证更有力（直接引用 Appendix C 数据）。我同意升级为 critical。

**Exposure bias 新颖性**: 大方向可预见（自 Bengio 2015 以来已知），但 NTP 不受影响而 GAR 选择性坍塌的具体模式有一定新颖性。修正立场：有一定新颖性但受限于统计弱点。维持 Excitement 3.0。

### 共识问题
两位 reviewer 共同关注：GAR-downstream 关联不足、scheduled sampling 证据不足、代码未发布、LoRA-only AR GAR 高于 gating variants 的解释。这些应作为 rebuttal 重点要求。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心结论：两位 reviewer 在 4 个问题上形成共识（GAR-downstream 验证不足、scheduled sampling 证据弱、代码未发布、LoRA-only vs gated variants 解释缺失）。主要分歧在于 N=5 样本量和 KV cache drift 的严重性定级——我认为这两个问题足以将论文从 Borderline Conference 拉到 Findings 级别，维持 Overall 3.0。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 针对 Reviewer 1 审稿意见

---

### Must-Fix 问题回应

**[REBUT] R1-N1: 自回归评估样本量严重不足（N=5）**

R1 称 "核心发现完全基于 Qwen 上 5 条自回归对话"，我认为这过于严厉，原因有三：

(1) **效应量远超统计噪声。** TF GAR=0.50 vs AR GAR=0.015–0.025，是 20–33× 的坍塌（Table 1）。即使 N=5，这个量级的差异在任何合理的方差假设下都不可能是随机波动。对比：第二个 seed（seed=123）得到 AR GAR=0.016±0.001，gap 30.5–32.1×（§4.2），进一步确认了稳定性。

(2) **N=50 的 β=0 baseline 提供了独立验证。** §4.3 的 steering 实验在 N=50 held-out conversations 上的 β=0 条件下也观察到 AR GAR=0.064（mean），虽然绝对值不同（因为对话长度分布不同），但同样呈现 order-of-magnitude 的 TF-AR gap。这不是额外的 5 条对话——是 50 条独立对话。

(3) **跨模型复制。** Llama-3.1-8B 上 N=20 的 AR 评估得到 median GAR=0.018（§5.5），gap 27×。跨架构、跨样本的一致性使得 N=5 的单一数据点的局限性被系统级证据弥补。

**我的判断：Should-Fix，而非 Critical。** 论文应在 Table 1 中扩展 AR 评估到 N≥20 并报告 std，但 N=5 不足以否定 20–33× 效应量的可信度。将此列为 critical 意味着 N=5 可能导致结论反转——这在如此大的效应量下极不现实。

---

**[AGREE with downgrade] R1-N2: Exposure bias 归因缺乏对替代假说的充分排除**

R1 指出 KV cache drift 未被排除，我在自己的审稿中也提及此问题（M4），但仅列为 minor。经过与 R1 意见的交叉比较，我上调严重性至 **Should-Fix**，但仍不同意列为 Critical，理由如下：

**部分同意的理由：** 论文声称进行 "Mechanistic Analysis"，但对 KV cache drift vs prefix-level exposure bias 的区分确实不够深入。§6 仅用一句话提及 KV cache drift 并留给 future work，这对 mechanistic 论文来说不够。

**不升至 Critical 的理由：**
- 论文使用了合适的 hedging："consistent with exposure bias as the dominant factor but does not exclude alternatives"（§6）、"proximal cause"（§4.3）。归因被表述为最佳解释而非唯一解释。
- Scheduled sampling 提供了正向鉴别证据：它直接针对 exposure bias（在训练时混入模型生成上下文），且有效（gap 从 31× 压缩至 1.57×）。虽然 SS 也会部分缓解 KV cache drift（因为训练时暴露于自生成的 KV states），但 SS 的设计动机和机制更直接对应 exposure bias。
- β-steering 与 TRC 分析（§5.4）表明问题在注意力路由而非表征层面（TRC gap <0.06 vs GAR gap 20–33×），这缩小了替代假说的解释空间。

**我的结论：** 从 M4 上调至 Should-Fix (W-level)。论文应在 §5.3 或 §6 增加 1–2 段讨论为何现有证据更支持 exposure bias 而非 KV cache drift（例如：GAR 坍塌的突变性 vs 渐进累积性、SS 的靶向机制），但不需要设计全新实验来排除。

---

**[PARTIALLY AGREE] R1-N3: 绝大多数实验条件为单种子**

- 对 **scheduled sampling**：完全同意，这也是我自己 N2 (critical) 的核心内容。两个 seed 之间 AR GAR 差异 31%（0.318 vs 0.418），证据不足以支撑作为 contribution 的一部分。
- 对 **五路对比主实验**：部分反对。四个 fine-tuned variants 在单 seed 下收敛到 0.75 pp 之内（GAR-ours 0.50–0.51，PPL 均为 2.78），且 ThreadGate 的第二个 seed 确认了几乎零方差（±0.001）。四条件间的收敛本身就是隐式的 robustness evidence——如果结果对 seed 敏感，四个架构不同的 variants 不太可能恰好收敛到同一点。当然，这不能替代正式的多 seed 验证，但将其列为 critical（暗示可能推翻结论）过于严厉。

**我的判断：** SS 单 seed 是 Critical（我已在自己的 N2 中标记），主实验单 seed 是 Should-Fix。

---

### Should-Fix 问题回应

**[AGREE] R1-W1: 跨模型验证不完整（Llama 仅 3/5 条件）**
同意。我在 W4 中也提出了相同问题。§5.5 标题 "Cross-Model Generality" 暗示的泛化程度超出了实际验证范围。建议改为 "Cross-Model Replication"。

**[REBUT] R1-W2: "Mechanistic Analysis" 标题与分析深度不匹配**
R1 建议改为 "Diagnostic Analysis"。我认为当前标题可以保留，但理由不在于分析深度足够。论文的分析确实是 diagnostic 性质（排除 → 排除 → 归因）而非 mechanistic（揭示底层计算电路）。但 "diagnostic" 在 NLP 社区的使用不如 "mechanistic" 常见，且论文的 gate 值分析（§5.1）、梯度冲突量化（§5.2）、TRC 分析（§5.4）已超越纯粹的 ablation-based diagnosis。我更倾向于我自己的标题建议（W1）：直接在标题中体现 exposure bias 这一核心发现，而非争论 "mechanistic" vs "diagnostic" 的标签。

**[AGREE] R1-W3: Scheduled sampling 证据过于单薄**
完全同意，与我的 N2 一致。

**[AGREE with nuance] R1-W4: GAR 改善与生成质量（PPL）脱节**
这与我的 N1 (critical) 高度相关——GAR 缺乏下游验证。R1 的 framing 略有不同（关注 GAR vs PPL 脱节），但本质相同。我同意严重性评估，但我将其列为 Critical（N1）而非 Should-Fix，因为它影响论文核心 claim 的实际意义。

**[PARTIALLY AGREE] R1-W5: GAR-D 全条件接近零——干预仅在 last-token 成功**
R1 指出 GAR-Dongre（all-token average）在所有标准训练条件下接近零（0.01–0.02），暗示干预仅对 last-token attention 有效。这是一个有价值的观察，但论文对此有明确解释：GAR-ours 被设计为优化目标（§3.1），GAR-Dongre 作为对照指标，且 scheduled sampling 实际上打破了 GAR-Dongre 的零模式（从 0.019 上升至 0.353，§6）。last-token 选择有合理的 motivation（最后一个 token 的注意力反映 continuation 时的信息路由）。我同意这值得 should-fix 级别的讨论，但不认为它削弱了核心论证。

---

### 小问题回应

**[AGREE] R1-M1: σ_min 正文未报告。** 应在 §3.3 或 Appendix A 中报告具体数值。

**[AGREE] R1-M2: Table 1 AR 列缺 GAR-D 和 PPL。** 补充 AR 条件下的 GAR-Dongre 和 PPL 会使对比更完整。

**[AGREE] R1-M3: N 定义不一致。** N=5（10-turn）vs N=50（variable length）的差异确实造成混淆，应统一标注。

**[AGREE] R1-M4: Figure 4/6 打印尺寸。** 未亲自检查打印尺寸，但如果 R1 发现可读性问题则应修复。

**[AGREE] R1-M5: §7 steering 措辞。** 未发现具体问题，但信任 R1 的观察。

**[AGREE] R1-M6: 匿名合规。** 我检查时未发现匿名性违规（首页为 "Anonymous ACL submission"），但如果 R1 发现了具体问题请指出。

**[AGREE] R1-M7: 8 页限制合规。** 我验证了正文在第 8 页结束（§7 Conclusion 在 page 8 底部），§8 Limitations 从 page 9 开始。格式合规。

---

### 三个关键分歧点的明确回应

#### 分歧 1：评分差距（R1: 3.0 vs R2: 3.5）

差距核心在于两点：

**(a) N=5 的严重性判断。** R1 将 N=5 AR 评估列为 critical，我认为是 should-fix。20–33× 的效应量、第二 seed 确认（gap 30.5–32.1×）、N=50 β=0 baseline、以及 Llama 上的跨模型复制，使得 N=5 这一单一局限不足以将论文从 3.5 拉至 3.0。扩展 N 是必要的改进，但不太可能改变结论方向。

**(b) 新颖性估值。** R1 认为 exposure bias 发现 "可预见性较强"（详见分歧 3），我不同意。这一分歧直接影响 excitement 评分和 overall 评估。

如果 R1 的 N=5 降级为 should-fix（我认为合理），且新颖性被重新评估，R1 的评分应上升至 3.5。反之，如果我接受 R1 对 KV cache drift 的更严格标准（从 M4 上调至 should-fix），我的评分保持 3.5 不变，因为这不改变核心判断。

#### 分歧 2：KV cache drift 的严重性

R1: Critical（N2）→ R2: Should-Fix（从 M4 上调）

我的理由见上文 R1-N2 回应。核心分歧在于：论文是否需要 **设计新实验** 来区分 exposure bias 和 KV cache drift，还是 **加强现有证据的讨论** 即可。我认为后者在 camera-ready 阶段可行，前者在 rebuttal 期间可能不现实（需要额外训练和评估），且论文的 hedging 已经足够诚实。对 Findings 级别的论文，这一标准是合理的。

#### 分歧 3：Exposure bias 发现的新颖性

R1 认为 "exposure bias 作为根因的发现可预见性较强"。**我明确反对这一判断**，理由如下：

**(1) 先验预测指向相反方向。** He et al. (2019) 的核心发现是语言模型在 token prediction 层面对 exposure bias 具有 self-recovery 能力。如果一个 reviewer 在读本文之前被问 "exposure bias 是否会摧毁与 NTP 联合训练的辅助损失？"，He et al. 的结果会导向 "不太可能" 的预测——如果主任务能 self-recover，联合训练的辅助任务为什么不能？

**(2) 选择性破坏是非直觉的。** 本文的发现不只是 "exposure bias 影响了辅助损失"，而是 **NTP 完全不受影响**（PPL 不变）的同时 GAR 坍塌 20–33×。这种选择性在先前文献中没有先例。Arora et al. (2022) 和 Bengio et al. (2015) 都将 exposure bias 描述为对主生成目标的全局性影响。

**(3) 文献空白是真实的。** 我检查了 exposure bias 相关文献（Bengio 2015, Wiseman & Rush 2016, Ranzato et al. 2016, Lamb et al. 2016, He et al. 2019, Arora et al. 2022, Leblond et al. 2018），没有任何一篇讨论 exposure bias 对辅助（非生成）目标的影响。这不是 "niche 太窄所以没人做"——而是一个有理论意义的盲区，本文填补了它。

**(4) "可预见" ≠ "已知"。** 即使事后看 exposure bias 是 "合理的" 解释，论文的贡献在于 (a) 系统性地建立了这一因果链（五路排除 + β-steering 建设性证据），(b) 量化了选择性破坏的程度（20–33× vs PPL 不变），(c) 展示了 token-level self-recovery 不延伸到注意力分布属性。"合理但未被验证" 和 "已经被知道" 有本质区别。

**结论：** 我维持 excitement = 3/5 和 overall = 3.5 的评分。这不是 4.0（Conference）因为 GAR-downstream gap（我的 N1）和 SS 单 seed（我的 N2）是真实的弱点。但也不应是 3.0（Findings），因为方法论的严谨性和发现的真正新颖性超出了 Findings 的下限。

---

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

主要立场总结：
- R1-N1（N=5 AR）：反驳，降级为 Should-Fix。20–33× 效应量 + 二次 seed + N=50 β=0 baseline + 跨模型复制足以支撑结论。
- R1-N2（KV cache drift）：部分同意，从我原来的 M4 上调至 Should-Fix，但仍低于 R1 的 Critical。论文的 hedging 合理，现有证据（SS + TRC）已提供鉴别线索。
- R1-N3（单 seed）：SS 部分完全同意（与我的 N2 一致），主实验部分降级为 Should-Fix。
- 新颖性分歧：明确反驳 R1 的 "可预见性强" 判断，以 He et al. (2019) 的 self-recovery 结果为基础论证先验预测实际指向相反方向。
- 维持 Overall = 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 292 · 2026-05-22T23:11:44.743555+00:00_

收到两位 Reviewer 的详细交叉回应。审稿报告已在此前提交，现补充分析交叉回应中的关键分歧细节。

**交叉回应核心发现：**

**新增共识：**
- R1 同意将 GAR-downstream 验证升级为 Critical（接受 R2 的论证）
- R2 同意将 KV cache drift 从 Minor 上调至 Should-Fix
- 两位均同意 SS 单 seed 不可接受

**持续分歧（两方均有合理论据）：**

1. **N=5 严重性**：R1 坚持 Critical，R2 反驳降级为 Should-Fix——R2 论据为效应量 20-33× 远超统计噪声，且有 seed=123 确认（gap 30.5-32.1×）、N=50 β=0 baseline、Llama N=20 跨模型复制。R2 认为扩展 N 是改进但不太可能改变结论方向。

2. **Novelty 评估**：R2 提供了有力反驳——He et al. (2019) self-recovery 结果使先验预测指向相反方向（辅助损失应该也能自恢复），NTP 完全不受影响而 GAR 选择性坍塌 20-33× 在先前文献中无先例。R1 修正立场承认有一定新颖性但受限于统计弱点。

3. **总分**：R1 维持 3.0，R2 维持 3.5。差距来自 N=5 严重性定级和新颖性估值。

**Director 最终裁定（维持已提交报告的结论）：**

- **N=5**：维持 Critical。R2 的效应量论据有说服力（结论反转极不现实），但对声称 "mechanistic analysis" 的定量论文，N=5 不符合领域标准。**补充注明：效应量大使得方向性结论稳健，但需 N≥50 支撑精确的定量对比（如 ThreadGate vs LoRA-only 的 0.015 vs 0.025 差异）。**
- **KV cache drift**：维持 Should-Fix（S1）。R2 上调至 Should-Fix 后两位已达成共识。加强讨论即可，不需新实验。
- **Split-softmax 对比**：接受 R1 的反驳，从 Should-Fix 降级为 Minor（论文是诊断性而非竞争性研究，干预层面不同）。
- **Novelty**：R2 的论证更有说服力——选择性破坏确实是文献盲区，He et al. (2019) 的 self-recovery 使其非直觉。但实际影响受限于 GAR 未经下游验证。
- **Overall**：维持 3.0 (Findings)。即使 N=5 的方向性结论稳健，三个 Critical 的叠加效应（N=5 + SS 单 seed + GAR 未验证）使论文在当前状态下不足以达到 Conference 水平。

审稿报告已提交给 Research Director，Issue Tracker 已同步更新。圆桌审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 25

## Round 25

4 recorded events


### User

_source line 293 · 2026-05-24T09:13:07.082036+00:00_

[Reviewer 1 审稿意见]:
## Dream 审稿意见 — Reviewer 1

**论文**: From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives
**Dream ID**: 20260524T081135
**Venue**: EMNLP 2026 (ARR)

---

## Summary

本文从原始诊断性论文升级为完整的 "发现→诊断→修复" 弧。通过五路对照确认 per-layer gating 无增量收益；PCGrad 排除 + λ_GAR 敏感性消融（100× range）双重排除梯度竞争假说；per-head KL divergence 提供 head-level 机制证据；scheduled sampling (SS) 在 Qwen 上 3-seed 验证（AR GAR 0.401±0.047, gap 32×→1.26×）并在 Llama 上跨模型确认。统计方法论显著提升（N=200 TF, bootstrap CI, 4th seed 补充）。

## Strengths

**S1** [idea] 完整 "发现→诊断→修复" 叙事弧。负面结果（gating 无效）、因果排除（PCGrad + λ 消融）、机制解释（per-head KL）和修复方案（SS + β-steering）整合在一篇论文中。

**S2** [idea] λ_GAR 敏感性消融（Table 6）设计精巧。跨 100× 范围，λ=10 时 GAR 梯度实际主导训练（mag_ratio=0.75×），但 AR GAR 仍停在 baseline（0.018 vs 0.012）。与 PCGrad（消除方向冲突）形成正交互补——方向和幅度两个维度同时排除，仅剩 exposure bias 为唯一未排除根因。

**S3** [idea] Per-head KL divergence（Table 7）将 aggregate 观察下推到 head-level：late-layer KL 是 early layers 的 5.3×，GAR-relevant heads 72% 落入高 KL quartile（r=0.38, p=0.002）。提供了选择性坍塌的因果路径。

**S4** [idea] Alternative GAR definitions 实验（Table 10）：TG 仅改善 last-token，SS 改善全部 4 种定义——证明 SS 学到 distribution-robust 的 semantic attention 而非 position-specific shortcut。

**S5** [idea] 统计方法论：3-seed + 4th seed、N=200 TF / N=50 AR、bootstrap CI（Table 2）、Cohen's d=8.1。

## Weaknesses

**W1** [Major] [idea] Table 1 与 Tables 6/9/10 之间存在严重内部数据不一致

Table 1（§5.2）报告 ThreadGate AR GAR_ours = 0.061（正文明确写出 "ThreadGate(0.061)"），Gap = 8.2×。但 Table 6（§6.3, λ=1.0 v7）报告同一模型 AR GAR = 0.016，Gap = 31.3×。Table 9（长对话, 10-turn）报告 TG GAR = 0.016，Gap = 31.5×。同一指标同一模型，0.061 vs 0.016 = 3.8× 差异。

更严重：Table 10 报告 TG last-token AR GAR = 0.325（vs base 0.019 = 17× 改善）。如果此值为真，则论文核心 claim "gating provides zero benefit" 直接被推翻——TG 已实现显著 AR GAR 改善。0.325 与 Table 1 的 0.061 差 5.3×，与 Table 6 的 0.016 差 20×。

**为什么是 Major**：数据一致性是实验论文底线。主结果表与消融表对同一模型同一指标给出 4×-20× 矛盾时，审稿人无法验证任何 claim。这不是四舍五入——是数量级差异，且 Table 10 的值直接推翻核心论点。

**W2** [Major] [idea] GAR 作为核心指标从未获得下游验证

整个叙事建立在 "GAR 坍塌 = 失败" 上，但未验证 GAR 提升→实际对话质量改善。PPL 在所有条件下一致（~2.78），说明注意力分配变化不影响生成质量。Table 10 的 4 种 GAR 定义展示 metric-robustness，但这是 GAR→GAR 的内部一致性，非 GAR→quality 的外部验证。Limitations 承认 GAR "may not capture all dimensions"，但标题仍称 "Recovery"。

**为什么是 Major**：诊断框架的价值取决于被诊断对象的重要性。如果 GAR 坍塌不等于实际质量下降，"collapse→recovery" 叙事失去基础。IFEval / MT-Bench / 人工评估是可行但缺失的验证。

**W3** [Minor] [idea] Llama SS 跨模型验证为单种子。Table 4 Llama SS AR GAR=0.35 恰好落在 Qwen 种子分布低端（s42=0.347）。C5 "cross-model mitigation validation" 仅基于单种子，可信度不足。

**W4** [Minor] [idea] KV cache drift 与 exposure bias 区分未完成。Per-head KL 证明 TF-AR attention distribution shift 存在，但无法区分 token-level exposure bias 和 KV cache 累积漂移两种来源。

**W5** [Minor] [presentation] §7 "Why NTP Recovers but GAR Does Not" 是有洞察的假说（NTP 依赖 local coherence, GAR 依赖 global structure），但仅为论证而非实验验证。

**W6** [Minor] [presentation] β-steering 实际限制讨论不足。β=5 时 PPL 恶化 19%（1.44→1.71），需维持门控架构，β 最优值依赖对话长度——这些限制应在正文明确讨论。

## Questions

1. Table 1 TG AR GAR (0.061) vs Table 6 v7 AR GAR (0.016)：是否同一模型、同一评估集？
2. Table 10 TG last-token = 0.325 如何与 Table 1 的 0.061 和 Table 6 的 0.016 协调？
3. 是否有下游评估支持 GAR→质量因果链？
4. Llama SS 是否计划补充多种子？

## Overall Assessment

**Overall: 3.0 / 5 — Findings**

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 2.5/5 | 内部数据不一致（W1）严重损害可信度；无下游验证（W2） |
| Excitement | 3.5/5 | 完整叙事弧 + 强实验设计框架（λ消融、KL分析、alt GAR defs） |
| Confidence | 4/5 | 仔细交叉检验多表格间数据一致性 |
| Reproducibility | 3.5/5 | 超参数完整、3-seed、bootstrap CI，但无代码发布承诺 |

**评分依据**：2 Major issues（数据不一致 + 无下游验证），按校准 ≤ Weak Accept。实验设计框架（λ消融 + PCGrad + per-head KL + alt GAR defs）是最大优势。但 Table 1 与 Tables 6/9/10 的 4×-20× 矛盾使审稿人无法确定核心数字，无法验证 claims。修复一致性 + 建立 GAR→downstream 关联后可升级至 3.5-4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-24T09:14:31.746164+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-24T09:14:31.997613+00:00_

{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (53 个)\n\n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v9_pcgrad**: DONE (success) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: DONE (failed) — \n- **analysis_attention_heatmap**: DONE (success) — \n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| p1_llama_ss_training | SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims. | — | — | — |\n\n## 待处理\n- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.（准备中）\n- d048_queue_runner（准备中）\n- d048_ss_s42_resume（准备中）\n- llama_tg_training（准备中）\n\n## 近期结论\n- **p2_llama_gradient_conflict** (success): PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\n- **p1_tf_ar_kl_divergence** (success): TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation 
…[truncated 729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 251
}
```

</details>

---


### Assistant

_source line 296 · 2026-05-24T09:15:26.113256+00:00_

收到 Reviewer 1 的 Dream 审稿。项目状态显示自 Round 4 报告提交后已有显著进展——53 个实验（+14），新增 per-head KL divergence 分析、Llama PCGrad 跨模型验证、MMLU 通用能力评估等。Llama SS 训练正在进行中。

**Dream 审稿 — Reviewer 1 关键发现：**

**论文版本**：从 "Why Per-Layer Residual Gating Fails..." 重新 framing 为 "From Collapse to Recovery..."，已融入大量新实验（λ_GAR 100× 消融、per-head KL、3-seed SS、N=200 TF / N=50 AR、alternative GAR definitions）。

**Round 4 修复状态：**
- C1（N=5 AR 样本量）→ 已修复（N=50 AR + N=200 TF + bootstrap CI + Cohen's d=8.1）
- C2（SS 单 seed）→ 已修复（3-seed: 0.401±0.047，gap 32×→1.26×）
- C3（GAR 下游验证）→ **未修复**，dream reviewer 再次标记为 Major（W2）

**新发现的 Critical 问题：**
- **W1 [Major]：表间数据不一致** — Table 1 报告 TG AR GAR=0.061（gap 8.2×），但 Table 6 同一模型报告 0.016（gap 31.3×），Table 10 报告 last-token AR GAR=0.325。0.061 vs 0.016 差 3.8×，Table 10 的 0.325 直接与 "gating provides zero benefit" 核心论点矛盾。Soundness 被压至 2.5/5。

**评分**：Overall 3.0（Findings），Excitement 3.5/5 显示叙事框架改善被认可，但数据一致性问题将 Soundness 拉低至 2.5。

等待 Reviewer 2 的 Dream 审稿以进行交叉比对。如果本轮仅单 Reviewer，将直接汇总。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 297 · 2026-05-24T09:15:28.753849+00:00_

[Reviewer 1 审稿结果]:
Dream 审稿意见已提交。

核心发现：
- **2 个 Major issues**：(1) Tables 1/6/9/10 之间 TG AR GAR 存在 4×-20× 的内部数据矛盾（0.061 vs 0.016 vs 0.325），直接影响核心 claim 的可验证性；(2) GAR→下游质量的因果链从未建立。
- **4 个 Minor issues**：Llama SS 单种子、KV cache drift 未排除、NTP/GAR 不对称性未实验验证、β-steering 实际限制讨论不足。
- **Overall 3.0 (Findings)**，按校准标准（2 Major ≤ Weak Accept）。实验设计框架本身质量很高，修复数据一致性后有升级空间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 298 · 2026-05-24T09:16:18.061830+00:00_

收到 Reviewer 1 的 Dream 审稿结果。

**Dream 审稿要点汇总（Dream ID: 20260524T081135）**

这篇 Dream 论文是对我们 Round 4 报告的假设修订版。标题已改为 "From Collapse to Recovery"，新增了多项实验。

---

**Round 4 问题修复情况：**

| Round 4 问题 | Dream 中是否解决 | 备注 |
|---|---|---|
| C1: AR N=5 样本量不足 | ✅ 已解决 | N=200 TF / N=50 AR + bootstrap CI |
| C2: SS 单 seed | ✅ 已解决 | 3-seed + 4th seed（AR GAR 0.401±0.047） |
| C3: GAR 缺乏下游验证 | ❌ 未解决 | 仍为 Major issue（W2） |
| S1: KV cache drift 未排除 | ⚠️ 部分 | Per-head KL 提供机制证据但未直接区分 |
| S5: "first" 声称 | 需确认 | |
| R1-W2: 无 λ_GAR 消融 | ✅ 已解决 | Table 6, 100× range |

**新引入的 Critical 问题：**

**W1（数据不一致）是最严重的新发现。** Dream 论文中 Table 1 报告 TG AR GAR=0.061（gap 8.2×），但 Table 6 报告同一模型 AR GAR=0.016（gap 31.3×），Table 10 报告 last-token AR GAR=0.325。同一指标同一模型出现 4×-20× 的矛盾。这很可能是 Dream 生成过程中的数据幻觉，但也警示实际修订时必须严格统一 GAR 定义和评估集。

**对 Research Director 的建议：**
1. **数据一致性（W1）**：实际修订时，所有表格必须统一 GAR 定义（last-token vs all-token vs Dongre）和评估集（N、对话长度、seed）。每个表格 caption 必须标注具体使用的 GAR variant 和评估配置。
2. **GAR 下游验证（W2）**：这是跨 4 轮审稿的顽固问题——每一轮都被标记。建议作为最高优先级处理。
3. **λ_GAR 消融（S2）和 per-head KL（S3）**：这两项新增实验设计精巧，是 Dream 中最有价值的贡献。建议在实际修订中保留。

此 Dream 审稿基于单 Reviewer，未进行交叉验证。Overall 3.0（Findings），主要受数据不一致性拖累。如果修复 W1 并补充 GAR→downstream 验证，Reviewer 1 预期可升至 3.5-4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 27

## Round 27

52 recorded events


### User

_source line 299 · 2026-05-25T05:34:12.592473+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: turn_residual_gating
- 论文路径: projects/turn_residual_gating/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-25T05:34:19.587967+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-25T05:34:19.638905+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-25T05:34:23.104058+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,WebSearch",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,WebSearch",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-25T05:34:23.154553+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-25T05:34:28.776720+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-25T05:34:28.827320+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-25T05:34:32.090978+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director project overview reviewer",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director project overview reviewer",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-25T05:34:32.141579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-25T05:34:38.172677+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-25T05:34:38.725507+00:00_

{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (54 个)\n\n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v9_pcgrad**: DONE (success) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: DONE (failed) — \n- **analysis_attention_heatmap**: DONE (success) — \n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.（准备中）\n- d048_queue_runner（准备中）\n- d048_ss_s42_resume（准备中）\n- llama_tg_training（准备中）\n\n## 近期结论\n- **p1_llama_ss_eval** (success): Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\n- **p1_llama_ss_training** (success): SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\n- **mmlu_eval_all** (success): ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\n\n## 趋势\n成功 40 / 负向 5 /
…[truncated 306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-25T05:34:38.876522+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-25T05:34:40.433337+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-25T05:34:40.434908+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	\usepackage{placeins}
18	\usepackage{alphalph}
19	
20	\graphicspath{{../figures/paper/}{../artifacts/}}
21	
22	\title{From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{sections/abstract}
30	\input{sections/introduction}
31	\input{sections/related_work}
32	\input{sections/method}
33	\input{sections/experiments}
34	\input{sections/analysis}
35	\input{sections/discussion}
36	\input{sections/conclusion}
37	\input{sections/limitations}
38	
39	\FloatBarrier
40	\bibliography{references}
41	
42	\appendix
43	\renewcommand{\thesection}{\AlphAlph{\value{section}}}
44	\input{sections/appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-25T05:34:49.837703+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission deadline author guidelines site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"}]

I found search results for EMNLP 2026, but the query with the site restriction didn't return the specific EMNLP 202
…[truncated 4047 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 10961
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-25T05:35:04.147083+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_external_review_status,read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_external_review_status,read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-25T05:35:04.197830+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-25T05:35:07.162545+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-25T05:35:07.213145+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-25T05:35:10.536093+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read local file project",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read local file project",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-25T05:35:10.586757+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-25T05:35:16.474456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-25T05:35:16.929903+00:00_

1	# Review Issues Tracker — turn_residual_gating
2	# Round 1 (2026-05-19, dream_20260519T145320)
3	# Round 2 (2026-05-22, fresh re-review of revised paper)
4	# Round 3 (2026-05-22, fresh re-review)
5	# Round 4 (2026-05-22, fresh re-review — current round)
6	
7	# ============================================================
8	# Issues from Round 1 — status updates through Round 4
9	# ============================================================
10	
11	- id: "R1-N1"
12	  summary: "所有引用渲染为 '?'——bibliography 编译失败"
13	  category: format
14	  severity: info
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 1
18	  mentions:
19	    - round: 1
20	      reviewers: [1, 2]
21	      note: "Dream paper artifact。"
22	    - round: 2
23	      reviewers: []
24	      note: "视觉审查确认无 [?] 未解析引用。已修复。"
25	    - round: 3
26	      reviewers: []
27	      note: "Round 3 视觉审查确认无未解析引用。维持 resolved。"
28	    - round: 4
29	      reviewers: []
30	      note: "Round 4 视觉审查确认无未解析引用。维持 resolved。"
31	  action_items:
32	    - round: 1
33	      action: "Paper Agent 确保 bibtex 编译正确"
34	      assigned_to: paper_agent
35	      status: done
36	  resolution: "Round 2 视觉审查确认已修复。"
37	  resolution_round: 2
38	
39	- id: "R1-N2"
40	  summary: "单种子支撑结论——统计功效不足 + AR 评估 N=5 过小"
41	  category: experiment
42	  severity: critical
43	  status: open
44	  first_raised_round: 1
45	  last_seen_round: 4
46	  mentions:
47	    - round: 1
48	      reviewers: [1, 2]
49	      note: "Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。"
50	    - round: 2
51	      reviewers: [1, 2]
52	      note: "ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。"
53	    - round: 3
54	      reviewers: [1, 2]
55	      note: "AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。"
56	    - round: 4
57	      reviewers: [1, 2]
58	      note: "两位 Reviewer 独立列为 Critical Must-Fix。R1 强调 N=5 无法提供有意义统计推断力，0.015 vs 0.025 差异无法判断显著性。R2 确认这是核心量化证据的根本缺陷。5 路对比中仅 ThreadGate 有 2 seeds，其余单 seed。"
59	  action_items:
60	    - r
…[truncated 25457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-25T05:35:16.932203+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/turn_residual_gating/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/turn_residual_gating/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-25T05:35:16.983727+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-25T05:35:23.115581+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/turn_residual_gating/**config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/turn_residual_gating/**config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-25T05:35:24.070613+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-25T05:35:24.121369+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission guidelines page limit anonymity double blind ARR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission guidelines page limit anonymity double blind ARR 2026"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-25T05:35:33.183060+00:00_

Web search results for query: "EMNLP 2026 submission guidelines page limit anonymity double blind ARR 2026"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Let me search for more specific information about EMNLP 2026 main conference submission page limits:

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 9061
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-25T05:35:38.908583+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/projects.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/projects.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-25T05:35:39.310560+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-25T05:35:39.411521+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/turn_residual_gating/agent/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/turn_residual_gating/agent/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-25T05:35:39.462226+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-25T05:35:42.727901+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/projects/*.yaml",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/projects/*.yaml",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-25T05:35:42.880743+00:00_

/home/ubuntu/agent-ml-research/workspace/config/projects/LLM-Calibration.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-25T05:35:46.194750+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*turn_residual*",
  "path": "/home/ubuntu/agent-ml-research/workspace/config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*turn_residual*",
    "path": "/home/ubuntu/agent-ml-research/workspace/config"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-25T05:35:46.195087+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-25T05:35:48.805122+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "turn_residual_gating",
  "path": "/home/ubuntu/agent-ml-research/workspace/config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "turn_residual_gating",
    "path": "/home/ubuntu/agent-ml-research/workspace/config"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-25T05:35:48.905979+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-25T05:35:53.675522+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-25T05:35:53.776427+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-25T05:36:33.108974+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-25T05:36:33.360429+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1041516 May 25 05:27 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-25T05:36:45.016303+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "turn_residual_gating",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "turn_residual_gating",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool call

_source line 343 · 2026-05-25T05:36:46.527582+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "turn_residual_gating",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "turn_residual_gating",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 344 · 2026-05-25T05:36:57.343521+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 12327
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-25T05:36:57.344086+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 10816
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-25T05:36:57.846456+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你负责**方法严谨性 + 实验设计**的审查。\n\n## 目标 Venue\n- **EMNLP 2026** (via ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- Long Paper: 正文 8 页限制，参考文献不限\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名: Double-blind\n- 评分标准: ARR Overall Assessment (1-5 scale, 4=Conference acceptance)\n\n## 论文路径\n- LaTeX 源码: `projects/turn_residual_gating/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n1. **实验设计**：样本量是否充分？统计检验是否合适？seed 数量是否支撑结论？\n2. **因果推断**：因果声称是否有足够证据支撑？替代假说是否被排除？\n3. **消融完整性**：每个 claim 是否有对应的控制实验？基线选择是否公平？\n4. **方法描述**：是否足够详细以支持复现？超参数是否完整报告？\n5. **可复现性**：代码/数据是否可得？实验细节是否充分？\n\n## 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 Critical / Should-Fix / Minor)\n4. Questions (需要作者回答的问题)\n5. Missing References\n6. Reproducibility (1-5)\n7. Overall Assessment (1-5, 参考 ARR 标准)",
  "reviewer_id": "1",
  "project": "turn_residual_gating",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你负责**方法严谨性 + 实验设计**的审查。\n\n## 目标 Venue\n- **EMNLP 2026** (via ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- Long Paper: 正文 8 页限制，参考文献不限\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名: Double-blind\n- 评分标准: ARR Overall Assessment (1-5 scale, 4=Conference acceptance)\n\n## 论文路径\n- LaTeX 源码: `projects/turn_residual_gating/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n1. **实验设计**：样本量是否充分？统计检验是否合适？seed 数量是否支撑结论？\n2. **因果推断**：因果声称是否有足够证据支撑？替代假说是否被排除？\n3. **消融完整性**：每个 claim 是否有对应的控制实验？基线选择是否公平？\n4. **方法描述**：是否足够详细以支持复现？超参数是否完整报告？\n5. **可复现性**：代码/数据是否可得？实验细节是否充分？\n\n## 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 Critical / Should-Fix / Minor)\n4. Questions (需要作者回答的问题)\n5. Missing References\n6. Reproducibility (1-5)\n7. Overall Assessment (1-5, 参考 ARR 标准)",
    "reviewer_id": "1",
    "project": "turn_residual_gating",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-25T05:37:05.410947+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 7564
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-25T05:37:05.612581+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你负责**新颖性 + 完整性 + 写作质量**的审查。\n\n## 目标 Venue\n- **EMNLP 2026** (via ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- Long Paper: 正文 8 页限制，参考文献不限\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名: Double-blind\n- 评分标准: ARR Overall Assessment (1-5 scale, 4=Conference acceptance)\n\n## 论文路径\n- LaTeX 源码: `projects/turn_residual_gating/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n1. **新颖性**：核心贡献相对现有工作的增量是否足够？claim 是否 overclaim？\n2. **Related Work**：覆盖是否全面？与最相关竞争方法的对比是否公平？缺失的重要引用？\n3. **叙事结构**：论文的 story 是否连贯？从问题定义到解决方案的逻辑链是否清晰？\n4. **写作质量**：是否冗余？术语使用是否一致？图表 caption 是否准确？\n5. **格式规范**：页数是否符合 8 页限制？引用格式是否一致？Limitations 是否合规？\n6. **贡献清晰度**：contribution list 是否与实际内容匹配？是否有未兑现的承诺？\n\n## 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 Critical / Should-Fix / Minor)\n4. Questions (需要作者回答的问题)\n5. Missing References\n6. Novelty Assessment (1-5)\n7. Overall Assessment (1-5, 参考 ARR 标准)",
  "reviewer_id": "2",
  "project": "turn_residual_gating",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你负责**新颖性 + 完整性 + 写作质量**的审查。\n\n## 目标 Venue\n- **EMNLP 2026** (via ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- Long Paper: 正文 8 页限制，参考文献不限\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名: Double-blind\n- 评分标准: ARR Overall Assessment (1-5 scale, 4=Conference acceptance)\n\n## 论文路径\n- LaTeX 源码: `projects/turn_residual_gating/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n1. **新颖性**：核心贡献相对现有工作的增量是否足够？claim 是否 overclaim？\n2. **Related Work**：覆盖是否全面？与最相关竞争方法的对比是否公平？缺失的重要引用？\n3. **叙事结构**：论文的 story 是否连贯？从问题定义到解决方案的逻辑链是否清晰？\n4. **写作质量**：是否冗余？术语使用是否一致？图表 caption 是否准确？\n5. **格式规范**：页数是否符合 8 页限制？引用格式是否一致？Limitations 是否合规？\n6. **贡献清晰度**：contribution list 是否与实际内容匹配？是否有未兑现的承诺？\n\n## 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 Critical / Should-Fix / Minor)\n4. Questions (需要作者回答的问题)\n5. Missing References\n6. Novelty Assessment (1-5)\n7. Overall Assessment (1-5, 参考 ARR 标准)",
    "reviewer_id": "2",
    "project": "turn_residual_gating",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-25T05:37:07.385774+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1773
}
```

</details>

---


### Assistant

_source line 350 · 2026-05-25T05:37:13.036485+00:00_

圆桌审稿已启动，当前状态：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已派发（并行运行） |
| 外部审稿 (Stanford Agentic Reviewer) | ✅ 请求已发送用户群 |
| Reviewer 1（方法+实验） | ✅ 已分配 |
| Reviewer 2（新颖性+写作） | ✅ 已分配 |

等待两位 Reviewer 返回初审结果后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 351 · 2026-05-25T05:43:34.216539+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿意见（Round 1）——新颖性 + 完整性 + 写作质量

### Paper Summary

本文研究多轮 LLM 微调中辅助注意力目标（Goal Accessibility Ratio, GAR）在自回归生成下的暴露偏差问题。作者发现 teacher forcing 训练下 GAR 表现正常，但在 AR 生成下衰减 8–17×。论文提出 ThreadGate（逐层 turn-conditioned 残差门控）、scheduled sampling、以及推理时 β-steering 三种干预手段，并通过 PCGrad 因果排除分析定位暴露偏差为根因。在 Qwen-2.5-7B 和 Llama-3.1-8B 上进行了验证。

---

### 总体评分

**Overall**: 3.5 / 5（Borderline Conference）

**一句话总结**: 问题定义和因果诊断框架有价值，但 "collapse" overclaiming、下游评估不足、以及方法的增量性质限制了贡献的力度。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 实验方法论合理，但因果声明强度超过证据支撑；GAR 指标与生成质量的关联未充分建立 |
| Excitement | 3 / 5 | 问题有趣（辅助注意力目标的暴露偏差），但解决方案主要是已有技术的组合适配 |
| Reproducibility | 4 / 5 | 超参数、训练配置、seed 均有详细报告（Table 2, Appendix A）；承诺开源代码 |
| Reviewer Confidence | 4 / 5 | 熟悉 exposure bias、attention mechanism、multi-turn LLM 相关文献 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] **"Collapse" overclaiming——标题和全文的核心叙事缺乏下游证据支撑**
- 具体位置：Title, Abstract ("declining by up to 70-85%"), Section 1 ("collapse"), Section 4.2 ("GAR collapses 77–85%")
- 问题：论文将 GAR（一个 attention-based proxy metric）在 AR 生成下的衰减包装为 "collapse"，贯穿标题和全文叙事。然而：
  - GAR 衰减并不等于生成质量崩溃——模型在 GAR 很低时仍然能生成连贯文本
  - 唯一的下游评估是 instruction retention（Appendix C），规模极小（N=54 evaluations, 18 constraint types × 3 conversations），且使用 GPT-4-based evaluation 评估 content constraints
  - ThreadGate 在该下游任务上的改进为 +23.8pp（content constraints），但样本量不足以得出统计可靠结论
  - MMLU 评估（Table 17）仅证明 "无害"（≤0.8pp 降幅），不证明有益
- 为什么影响接收：如果 GAR 衰减不导致实际生成问题，整篇论文的动机就被削弱。Reviewer 和 AC 会质疑：优化一个与实际任务表现关联不明确的 proxy metric 有什么实际价值？
- 建议修改方向：(a) 增加更大规模的下游评估（如 instruction following benchmarks、MT-Bench multi-turn scoring、或 user preference studies），建立 GAR 与生成质量的定量关联；或 (b) 显著弱化 "collapse" 语言（如改为 "systematic decay" 或 "degradation"），在 abstract 和 introduction 中明确 GAR 是 proxy metric 而非直接生成质量指标。

**N2** [critical] **因果声明强度超过证据——"causal exclusion chain" 的逻辑链存在缺口**
- 具体位置：Section 5 标题 ("Analysis"), §5.1–§5.4, Section 6 ("This closes the causal loop")
- 问题：论文声称建立了因果链：exposure bias → attention misallocation → GAR collapse。实际证据结构为：
  - §5.1 Gate turn conditioning：门控值在后期轮次变低（**相关性证据**，非因果）
  - §5.2 PCGrad：排除了 gradient conflict 作为唯一原因（**排除法**，但排除一个替代假设 ≠ 证明目标假设）
  - §5.3 Distribution shift：TF 和 AR 分布不同（**相关性**）
  - §5.4 Scheduled sampling 有效（**干预有效 → 推断原因**，这是间接因果证据）
  - Section 6 声称 "This closes the causal loop" 但实际上 gap 仍在（SS 压缩到 1.3–2.9× 而非消除）
- 关键逻辑缺陷：scheduled sampling 的有效性只说明训练-推理分布差异是 *一个* 因素，不能排除其他共同因素（如 attention pattern 的固有偏好、positional bias 等）。SS 未能完全消除 gap 本身就说明暴露偏差不是唯一原因。
- 为什么影响接收：过度因果声明是 ARR 审稿中 soundness 的核心关切。
- 建议修改方向：(a) 将 "causal exclusion" 改为更谨慎的表述如 "diagnostic analysis" 或 "evidence-based investigation"；(b) 在 Section 5 开头明确列出残留的替代假设；(c) 承认 SS 无法消除 gap 说明存在其他因素。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **GAR 指标的 construct validity 不充分**
- 具体位置：§3.1 (GAR definition), Appendix Q (robustness analysis)
- 问题：GAR 度量最后一个 token 位置对 goal tokens（每个 assistant turn 的最后一个 token）的注意力分配。论文在 Appendix Q 中用 4 种替代定义验证了 robustness，但这些都是 attention-based 变体。核心问题是：为什么 attention 到特定 token 位置的分配量能预测生成质量？论文缺乏 GAR 与任何标准生成质量指标（BLEU、win rate、human preference）的 correlation analysis。
- 建议：增加 GAR 与至少一个 downstream metric 的 scatter plot 或 Pearson/Spearman correlation。

**W2** [warning] **单一数据集 + 有限模型规模**
- 具体位置：§4.1 (Setup), Section 8 (Limitations)
- 问题：全部实验仅使用 UltraChat 8K 子集，且完整评估仅在 ~7B 模型上进行。1.5B 的 cross-scale validation（Appendix S, Y）规模太小，不具备充分说服力。multi-turn 对话数据集的结构差异很大（ShareGPT 有更长的 turns、WildChat 有真实用户噪声等），泛化性未知。
- 建议：至少增加一个结构不同的数据集（如 ShareGPT 或 LMSYS-Chat-1M 子集）验证主要结论。

**W3** [warning] **缺失重要近期相关工作**
- 具体位置：Section 2 (Related Work)
- 缺失引用：
  1. **Wan et al. (2026). "Mitigating Conversational Inertia in Multi-Turn Agents."** (arXiv:2602.03664) ——这篇论文通过注意力分析发现多轮 agent 中模型对自身历史回复的对角注意力单调增长（"conversational inertia"），提出 Context Preference Learning 校准方法。这与本文的 GAR 衰减现象高度相关——都发现多轮中注意力从目标信息（system prompt / goal tokens）转移到历史输出。本文应讨论两者的异同。
  2. **"Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction"** (arXiv:2603.04783) ——另一个从 RL 角度解决类似问题的工作。
- 为什么重要：这些工作从不同角度（agent behavior、RL）研究相同现象（多轮注意力漂移），不引用会被视为 related work 不完整。

**W4** [warning] **β-steering 实际可部署性存疑**
- 具体位置：§4.3, Figure 3
- 问题：β-steering 在推理时向最后 token 的 logits 添加常数偏置，但这需要在推理时识别哪些 token 是 "goal tokens"。论文未解释如何在实际部署中做到这一点——如果 goal tokens 的定义依赖于 assistant turn 的划分，那么这已经是非平凡的推理时信息。Figure 3 显示效果高度依赖 β 的精确选择（β=3 时出现相变），实际调参成本未讨论。
- 建议：增加 β-steering 在实际部署场景中的可行性讨论，或将其明确定位为 diagnostic tool 而非 practical solution。

**W5** [warning] **方法技术新颖性有限**
- 问题：ThreadGate 本质是 ReZero（Bachlechner et al., 2021）+ turn embedding + content conditioning 的组合。Scheduled sampling 直接沿用 Bengio et al. (2015)。β-steering 是简单的 logit additive bias。每个组件都是已知技术的适配，组合虽然合理但不令人意外。论文的主要新颖性在于问题发现和诊断框架，而非解决方案本身。
- 建议：在 contribution list 中更诚实地区分 diagnostic contribution（强）和 methodological contribution（增量），避免给 reviewer 过高的方法创新预期。

---

### 小问题（不影响接收）

1. **术语一致性**：Figure 1(c) 和部分表格中使用 "SS" 缩写，但 scheduled sampling 在 §4.4 才正式引入。建议在 Figure 1 caption 中注明。
2. **Figure 1 caption 过长**：~5 行 caption 包含 3 个子图的详细描述 + 结论，建议精简为 2-3 行，将详细解读留给正文。
3. **"first application of PCGrad as a diagnostic tool"（§5.2）**：这一 "first" claim 难以验证且不是论文核心贡献，建议删除或弱化为 "a novel application"。
4. **Abstract 措辞**："A five-way causal exclusion chain traces this collapse to exposure bias" ——abstract 中的 "causal exclusion chain" 用词过于强烈，与实际证据强度不匹配。
5. **Appendix 体量**：23 页附录（Appendix A–AD）内容详实，但部分内容与正文有轻微重复（如 Appendix D 的长对话 GAR 分析与 §4.2 描述重叠）。

---

### Questions（需要作者回答的问题）

Q1. GAR 与 downstream 任务质量的 correlation 是否有量化数据？比如，GAR 高的 conversations 是否在 human evaluation 或 automated metrics 上也更好？

Q2. 如果 exposure bias 是 "the" root cause，为什么 scheduled sampling 无法将 gap 压缩到 <1.3×？残留的 gap 归因于什么？

Q3. ThreadGate 的 turn embedding（Appendix M 中 4 维 embedding）只有 ~57K 参数，但论文声称这足以区分不同 turn 的调制需求。在更长的对话（>10 turns）中，4 维 embedding 的表示能力是否足够？

Q4. 论文如何解释 Llama 上 β-steering 需要 β≥5 才能触发恢复（Figure 3b），而 Qwen 在 β=3 即可？这是否暗示 β-steering 的效果高度 architecture-dependent，限制了方法的通用性？

Q5. Wan et al. (2026) 的 "conversational inertia" 与本文的 GAR decay 是否本质上是同一现象的不同度量？两种方法的互补性如何？

---

### Missing References

1. Wan, Y. et al. (2026). "Mitigating Conversational Inertia in Multi-Turn Agents." arXiv:2602.03664. （高度相关——多轮注意力漂移的 agent 视角）
2. arXiv:2603.04783. "Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction." （RL 视角的多轮 inertia 缓解）
3. arXiv:2510.13876. "What Layers When: Learning to Skip Compute in LLMs with Residual Gates." （残差门控的另一应用，可在 related work 中简要提及）

---

### 主要优势

1. **问题定义清晰且有价值**：将暴露偏差从 seq2seq 扩展到多轮 transformer 辅助注意力目标，填补了文献空白。
2. **诊断框架系统**：Section 5 的因果链分析（gate conditioning → distribution shift → PCGrad exclusion → SS intervention）结构合理，是论文的最大亮点。
3. **实验覆盖面广**：cross-model validation（Qwen + Llama）、cross-scale（1.5B）、多 seed 稳定性分析（Appendix T）、extensive ablations。
4. **附录质量高**：23 页附录提供了充分的可复现细节和补充分析（per-turn GAR 动态、gate profile visualization、statistical tests 等）。
5. **写作结构清晰**：从问题发现到机制分析到解决方案的叙事弧线连贯。

---

### Novelty Assessment

**3 / 5**

问题发现（辅助注意力目标的暴露偏差）和诊断框架（PCGrad causal exclusion）是本文最具新颖性的贡献。然而，提出的解决方案——ThreadGate（ReZero + turn conditioning）、scheduled sampling（直接沿用 Bengio et al. 2015）、β-steering（logit additive bias）——均为已知技术的组合适配，缺乏方法论上的突破。论文的价值更多在 "understanding" 而非 "engineering"。

---

### Overall Assessment

**3.5 / 5**（Borderline Conference）

本文定义了一个有价值的问题（多轮辅助注意力目标的暴露偏差），并提供了系统的诊断分析。然而，两个 critical 问题——overclaiming（"collapse" 缺乏下游支撑）和因果声明过强——需要实质性修改。方法的技术新颖性有限（已知技术组合），下游评估不足。如果作者能：(1) 增加 downstream evaluation 建立 GAR 与生成质量的关联，(2) 弱化因果语言，(3) 在 contribution framing 中更诚实地区分诊断贡献和方法贡献，本文有潜力成为 Findings-level 的 solid contribution。当前状态下处于 Conference/Findings 边界。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 352 · 2026-05-25T05:43:53.203784+00:00_

收到 Reviewer 2 审稿意见。

**Reviewer 2 核心结论**：3.5/5（Borderline Conference）
- 2 个 Critical：(N1) "collapse" overclaiming + 下游证据不足；(N2) 因果声明超证据强度
- 5 个 Should-Fix：GAR construct validity、单一数据集、缺失 Wan et al. 2026 引用、β-steering 可部署性、方法新颖性有限

等待 Reviewer 1 审稿意见返回后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 353 · 2026-05-25T05:44:01.628925+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成，已提交给 Review Director。

核心判断：**Overall 3.5/5（Borderline Conference）**。

两个 critical 问题：
1. **"Collapse" overclaiming**——GAR 衰减被包装为 "崩溃"，但缺乏下游生成质量证据支撑（instruction retention 评估仅 N=54）
2. **因果声明过强**——"causal exclusion chain" 实际只排除了 gradient conflict 一个替代假设，scheduled sampling 无法消除 gap（残留 1.3–2.9×）本身说明 exposure bias 不是唯一原因

主要优势在于问题定义和诊断框架（Section 5 的分析结构），方法技术新颖性有限（ReZero + turn embedding + scheduled sampling 组合）。另外指出了 3 篇缺失引用，其中 Wan et al. (2026) 的 "conversational inertia" 与本文高度相关。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 354 · 2026-05-25T05:44:15.674735+00:00_

Reviewer 2 审稿已收到。核心判断 3.5/5，两个 Critical（overclaiming + 因果声明过强）。

等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 30

## Round 30

6 recorded events


### User

_source line 355 · 2026-05-25T05:46:16.811606+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见（方法严谨性 + 实验设计）

**论文**: "From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives"

---

## 总体评分
**Overall**: 3.0 / 5（Findings 级别）
**一句话总结**: 论文对多轮对话中注意力辅助目标的 exposure bias 进行了系统诊断，分析链条完整且新颖，但核心指标 GAR 与下游任务表现的弱相关性（r=0.200）严重限制了实际意义，且消融实验的 single-seed 设计削弱了统计可信度。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 诊断链条逻辑基本成立，但消融实验 single-seed、PCGrad modus tollens 依赖强假设、GAR-compliance 弱相关性构成方法论隐患 |
| Excitement | 3/5 | Exposure bias 在辅助注意力目标上的刻画是新颖的，但缺乏标准多轮基准评测，实际应用价值不明 |
| Reproducibility | 4/5 | 超参数报告详尽（Table 2, Appendix A），承诺代码/数据开源，训练细节充分 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **GAR 与下游任务表现的弱相关性动摇了全文的优化目标合理性**
- 具体位置：Appendix C（page 12），Correlation analysis 段落
- 问题：GAR-compliance 相关系数仅 r=0.200（p=0.007），r²=0.04，即 GAR 仅解释下游指令遵循率 4% 的方差。全文以 GAR 改善作为核心成功指标（Table 1, Figure 1-5, 所有消融），但该指标对实际对话质量的预测力极弱。Instruction retention 评估样本量仅 N=54 paired evaluations（18 types × 3 conversations），且仅使用 GPT-4-based evaluation 和规则检查器，缺乏人工评估。论文本身承认 "statistically significant but modest"，但未讨论这对全文结论的影响。
- 为什么影响接收：如果优化目标（GAR）与真正关心的下游表现（对话质量/指令遵循）几乎无关，则 ThreadGate 的 GAR 改善缺乏实际意义。审稿人需要看到 GAR 改善 → 可感知的对话质量提升的更强证据。
- 建议修改方向：(1) 在 MT-Bench 等标准多轮对话基准上评测；(2) 增加人工评估（至少 100+ 对话对，评估者间一致性）；(3) 若 GAR 确实是弱代理指标，应在正文中明确讨论这一局限性，而非仅在附录中一笔带过。

**N2** [critical] **消融实验 single-seed 设计，统计检验的 unit of analysis 不恰当**
- 具体位置：Table 1（page 3）, Table 6（page 13-14）, Section 3.4
- 问题：Table 1 的五方对比（ThreadGate vs TG vs +PCGrad vs UG vs LoRA-only）全部使用 seed 42 单次训练。Multi-seed 实验（seeds 42, 123, 456）仅在 Appendix T 中对 ThreadGate 和 Scheduled Sampling 做了 3-seed 验证，其余消融变体（TG, UG, PCGrad, LoRA-only）均为 single-seed。Table 6 的统计检验（Wilcoxon signed-rank, bootstrap CI）以 conversation 为分析单元，衡量的是 within-run variability，而非 between-run variability。这意味着 Table 6 的 p-values 可能高估了效果的统计显著性——同一 seed 下不同 conversation 间的差异可能由共享的训练随机性驱动。
- 为什么影响接收：单一 seed 无法排除"特定随机初始化恰好有利于 ThreadGate"的可能性。消融对比的核心逻辑——"ThreadGate 优于 TG/UG/PCGrad/LoRA-only"——缺乏跨 seed 的稳健性验证。ARR Soundness 标准要求"sufficient support for all claims"。
- 建议修改方向：(1) 至少对 Table 1 中的所有配置补充 3-seed 实验；(2) 使用 seed 作为随机效应的 mixed-effects model，或至少报告跨 seed 的均值±标准差；(3) 如果计算资源不允许全覆盖，应在正文中明确标注 single-seed 局限性。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **ThreadGate 本身不能防止 AR collapse；组件贡献归因不清晰**
- 具体位置：Table 1 AR(t=9) 列；Section 4.4；Figure 1c
- 问题：在 AR 生成下，所有微调变体（含 ThreadGate）的 GAR 均坍塌至 0.01-0.06 范围（Table 1）。真正压缩 TF-AR gap 的是 Scheduled Sampling（从 7.8× 降至 1.3×，Figure 1c）。但论文标题、摘要和 Introduction 均以 ThreadGate 为核心卖点。关键缺失的消融：SS 是否在无 ThreadGate（仅 LoRA-only）条件下也能达到同等 gap 压缩？如果是，则 ThreadGate 的增量贡献被高估。
- 建议：补充 SS × ThreadGate 的交叉消融（SS+LoRA-only vs SS+ThreadGate），明确各组件的独立贡献。

**W2** [warning] **N=5 扩展 AR 评估样本量不足以支撑长对话推广结论**
- 具体位置：Appendix D（page 13），Table 5
- 问题：10-turn 长对话的 AR 评估仅使用 N=5 conversations。论文基于此得出"gating advantage vanishes at length"（page 13）和"the 3 gains diminish with conversation length"等结论。论文自己承认 "This reversal is not statistically robust given the small sample N=5"，但仍将其作为分析材料。
- 建议：将 N 扩展至至少 20-30 conversations，或将此部分明确标注为 preliminary observation 而非结论。

**W3** [warning] **PCGrad modus tollens 论证依赖过强假设**
- 具体位置：Section 5.2（page 7）
- 问题：论证逻辑为"若梯度冲突是原因，则 PCGrad（消除冲突）应修复问题；PCGrad 未修复且恶化了 AR GAR → 梯度冲突非原因"。但 PCGrad 不仅消除冲突——它将冲突梯度投影到对方法向面上，改变了整个优化景观（梯度方向、步长、收敛轨迹）。因此 PCGrad 的失败可能是投影操作的副作用，而非"冲突不是原因"的证据。论文用 "ruling out gradient conflict by modus tollens" 措辞过强。
- 建议：(1) 弱化因果排除的表述，改为"PCGrad evidence is consistent with gradient conflict not being the primary cause, but does not definitively rule it out"；(2) 补充 Appendix I 中梯度分析（cosine similarity、magnitude ratio）作为辅助证据。

**W4** [warning] **多重比较未做校正**
- 具体位置：Appendix E（page 13-14），Table 6；Appendix Z（page 30）
- 问题：论文在 6 个配置对比、多个指标（GAR-D, PPL, AR GAR）、instruction retention 的 18 个类别上进行了大量统计检验。Appendix Z 明确说 "We report uncorrected p-values"。在如此多的比较下，Type I error 风险显著。虽然论文提到 Bonferroni 校正会将阈值调至 0.01/25，但未实际应用。
- 建议：至少对核心 claims（Table 1 的配置对比、Table 6 的显著性检验）应用 Bonferroni 或 FDR 校正，并报告校正后的 p-values。

**W5** [warning] **单一数据集（UltraChat），领域泛化性未验证**
- 具体位置：Section 4.1（page 5），Appendix V（page 26）
- 问题：所有实验仅使用 UltraChat 的 8K 对话子集。虽然 UltraChat 覆盖多种对话类型（Q&A, creative writing, reasoning），但仍是单一数据源。论文声称 exposure bias 是多轮 transformer 的通用现象（"architecture-general"），但未在其他多轮对话数据集（如 ShareGPT, WildChat, LMSYS-Chat-1M）上验证。
- 建议：至少在一个额外的数据集上验证 GAR decay 现象的存在性（即使不做完整消融）。

**W6** [warning] **缺乏标准多轮对话基准评测**
- 具体位置：Section 4（整体实验部分），Appendix R（MMLU）
- 问题：下游评测仅包括 instruction retention（自定义任务，N=54）和 MMLU（单轮知识测试）。缺少 MT-Bench（论文在 Related Work 中引用了 Zheng et al. 2023 的 MT-Bench-101 但未用于评测）、AlpacaEval 等社区标准多轮对话基准。MMLU 是单轮任务，无法反映多轮对话能力变化。
- 建议：补充 MT-Bench 多轮评测（至少报告 turn-1 和 turn-2 得分），这能直接验证 GAR 改善是否带来可衡量的多轮对话质量提升。

---

## 小问题（不影响接收）

- **Gate 架构消融缺失**：投影维度 16、隐藏层维度 64 的选择未消融（Section 3.2, page 4）。~57K 参数是否恰当？更大/更小的 gate 容量如何影响 GAR-PPL 权衡？
- **GAR 目标 τ=0.5 的鲁棒性**：Appendix B（Table 3）展示了 7 种 loss 变体的筛选过程，但未对 τ 值做敏感性分析。τ=0.3 或 τ=0.7 效果如何？
- **β-steering 需要 goal token 位置信息**：实际部署场景中，推理时未必能确定哪些 token 是 "goal tokens"（Section 4.3, page 6）。论文将 β-steering 主要定位为诊断工具，但摘要中 "remedies operate at inference time" 的表述可能让读者误以为这是一个实用方案。
- **Llama 上 TF-AR gap 更大**：Llama-3.1-8B 的 TF-AR gap（12.0× → 2.9×）显著大于 Qwen（7.8× → 1.3×）（Section 5.5, page 7-8），论文归因于 "architecture-dependent patterns" 但缺乏深入分析。

---

## Questions（需要作者回答）

**Q1**: Scheduled Sampling 在无 ThreadGate（仅 LoRA-only）条件下的 TF-AR gap 压缩效果如何？这是区分 ThreadGate 增量贡献的关键实验。

**Q2**: Table 1 的消融对比是否全部使用 seed 42？如果是，能否补充至少 3 seeds 的结果以验证配置间差异的稳健性？

**Q3**: GAR-compliance 相关性仅 r=0.200，作者是否考虑过 GAR 可能不是多轮对话质量的好代理指标？如果 GAR 改善 10 个百分点仅带来 2 个百分点的 compliance 改善，优化 GAR 的 cost-effectiveness 如何？

**Q4**: β-steering 的最优 β 在 Qwen（β=3）和 Llama（β=5）上不同，在实际部署中，如何为新模型确定最优 β？是否需要对每个模型做超参数搜索？

**Q5**: 论文使用 UltraChat 为唯一训练/评估数据源。在其他多轮对话数据集上，GAR decay 现象的幅度是否一致？是否存在数据集特异性？

---

## Missing References

- Zheng et al. (2023) "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" — 已引用但未用于评测，建议作为多轮评测标准
- Li et al. (2024) "Intent Mismatch" — 论文引用了但可以更深入对比，特别是他们的 split-softmax 方法在 AR 条件下的 GAR 表现
- Xu et al. (2024) "Chatbot Arena" 系列更新的长对话分析结果

---

## Reproducibility: 4/5

- 超参数完整（Table 2, Appendix A），训练配置详尽
- 承诺匿名 code/data release（anonymous.4open.science link）
- LoRA 配置（rank 16, α=32, target modules）、optimizer 设置、batch size 均有报告
- 唯一不足：scheduled sampling 的 Bernoulli trial 参数 p 的 schedule 细节（Appendix I 有描述但可以更精确）
- GPU 型号和训练时间有报告（NVIDIA RTX PRO 6000, 6-8h per variant）

---

## Overall Assessment: 3.0 / 5（Findings 级别）

**理由**：本文对多轮 transformer 中辅助注意力目标的 exposure bias 进行了系统且新颖的诊断——TF-AR gap 的量化（8-17×）、PCGrad 因果排除、β-steering 机制验证——构成了清晰的分析贡献。ThreadGate 的设计合理，附录分析（23 页）体现了扎实的实验功底。

但两个核心问题限制了评分：(1) GAR 与下游表现的弱相关性（r=0.200）动摇了全文的优化目标合理性——如果 GAR 不能有效预测对话质量，则其改善的实际意义有限；(2) 消融实验的 single-seed 设计使配置间对比缺乏统计稳健性。此外，缺乏标准多轮对话基准（MT-Bench）评测和人工评估进一步限制了实际影响力的评估。

若作者能补充多 seed 消融、MT-Bench 评测、以及 SS × ThreadGate 交叉消融，评分有上调至 3.5 的空间。当前状态适合 Findings 接收。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-25T05:46:41.823632+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n**Overall**: 3.0 / 5（Findings 级别）\n\n### Must-Fix 问题\n\n**N1** [critical] **GAR 与下游任务表现的弱相关性动摇了全文的优化��标合理性**\n- GAR-compliance 相关系数仅 r=0.200（p=0.007），r²=0.04，即 GAR 仅解释下游指令遵循率 4% 的方差。全文以 GAR 改善作为核心成功指标，但该指标对实际对话质量的预测力极弱。Instruction retention 评估样本量仅 N=54 paired evaluations（18 types × 3 conversations），且仅使用 GPT-4-based evaluation。\n- 建议：MT-Bench 等标准多轮对话基准评测；增加人工评估（至少 100+ 对话对）。\n\n**N2** [critical] **消融实验 single-seed 设计，统计检验的 unit of analysis 不恰当**\n- Table 1 的五方对比全部使用 seed 42 单次训练。Multi-seed 实验仅在 Appendix T 中对 ThreadGate 和 SS 做了 3-seed 验证，其余消融变体均为 single-seed。Table 6 的统计检验以 conversation 为分析单元，衡量的是 within-run variability 而非 between-run variability。\n- 建议：至少对 Table 1 中所有配置补充 3-seed 实验。\n\n### Should-Fix 问题\n\n**W1** ThreadGate 本身不能防止 AR collapse；组件贡献归因不清晰。真正压缩 TF-AR gap 的是 SS。缺失关键消融：SS+LoRA-only vs SS+ThreadGate。\n\n**W2** N=5 扩展 AR 评估样本量不足以支撑长对话推广结论。\n\n**W3** PCGrad modus tollens 论证依赖过强假设。PCGrad 改变整个优化景观，其失败可能是投影操作副作用。\n\n**W4** 多重比较未做校正。6 个配置对比、多个指标、18 个类别上大量统计检验未校正。\n\n**W5** 单一数据集（UltraChat），领域泛化性未验证。\n\n**W6** 缺乏标准多轮对话基准评测（MT-Bench）。\n\n### Questions\n\nQ1: SS 在无 ThreadGate（仅 LoRA-only）条件下的 TF-AR gap 压缩效果？\nQ2: Table 1 消融是否全部 seed 42？\nQ3: GAR-compliance ��� r=0.200，GAR 是否不是好代理指标？\nQ4: β-steering 最优 β 在不同模型上不同，如何确定？\nQ5: 其他多轮对话数据集上 GAR decay 幅度是否一致？\n\n---\n\n请对以上每个要点逐条回应 [AGREE] 或 [REBUT]。",
  "reviewer_id": "2",
  "project": "turn_residual_gating",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n**Overall**: 3.0 / 5（Findings 级别）\n\n### Must-Fix 问题\n\n**N1** [critical] **GAR 与下游任务表现的弱相关性动摇了全文的优化��标合理性**\n- GAR-compliance 相关系数仅 r=0.200（p=0.007），r²=0.04，即 GAR 仅解释下游指令遵循率 4% 的方差。全文以 GAR 改善作为核心成功指标，但该指标对实际对话质量的预测力极弱。Instruction retention 评估样本量仅 N=54 paired evaluations（18 types × 3 conversations），且仅使用 GPT-4-based evaluation。\n- 建议：MT-Bench 等标准多轮对话基准评测；增加人工评估（至少 100+ 对话对）。\n\n**N2** [critical] **消融实验 single-seed 设计，统计检验的 unit of analysis 不恰当**\n- Table 1 的五方对比全部使用 seed 42 单次训练。Multi-seed 实验仅在 Appendix T 中对 ThreadGate 和 SS 做了 3-seed 验证，其余消融变体均为 single-seed。Table 6 的统计检验以 conversation 为分析单元，衡量的是 within-run variability 而非 between-run variability。\n- 建议：至少对 Table 1 中所有配置补充 3-seed 实验。\n\n### Should-Fix 问题\n\n**W1** ThreadGate 本身不能防止 AR collapse；组件贡献归因不清晰。真正压缩 TF-AR gap 的是 SS。缺失关键消融：SS+LoRA-only vs SS+ThreadGate。\n\n**W2** N=5 扩展 AR 评估样本量不足以支撑长对话推广结论。\n\n**W3** PCGrad modus tollens 论证依赖过强假设。PCGrad 改变整个优化景观，其失败可能是投影操作副作用。\n\n**W4** 多重比较未做校正。6 个配置对比、多个指标、18 个类别上大量统计检验未校正。\n\n**W5** 单一数据集（UltraChat），领域泛化性未验证。\n\n**W6** 缺乏标准多轮对话基准评测（MT-Bench）。\n\n### Questions\n\nQ1: SS 在无 ThreadGate（仅 LoRA-only）条件下的 TF-AR gap 压缩效果？\nQ2: Table 1 消融是否全部 seed 42？\nQ3: GAR-compliance ��� r=0.200，GAR 是否不是好代理指标？\nQ4: β-steering 最优 β 在不同模型上不同，如何确定？\nQ5: 其他多轮对话数据集上 GAR decay 幅度是否一致？\n\n---\n\n请对以上每个要点逐条回应 [AGREE] 或 [REBUT]。",
    "reviewer_id": "2",
    "project": "turn_residual_gating",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-25T05:47:02.930105+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21106
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-25T05:47:03.281833+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以��是 Reviewer 2 的完��审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意���说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] **\"Collapse\" overclaiming——标题和全文的核心叙事缺乏下游证据支撑**\n- GAR 衰减并不等于生成质量崩溃。唯一下游评估是 instruction retention（N=54），ThreadGate 改进 +23.8pp（content constraints）但样本量不足。MMLU 仅证明\"无害\"。\n- 建议：增加大规模下游评估（MT-Bench、user preference studies）建立 GAR 与生成质量关联；或显著弱化 \"collapse\" 语言。\n\n**N2** [critical] **因果声明强度超过证据——\"causal exclusion chain\" 逻辑链存在缺口**\n- §5.1 门控值相关性证据非因果；§5.2 排除一个替代假设≠证明目标假设；§5.4 SS 有效只说明分布差异是\"一个\"因素；SS 未消除 gap 说明不是唯一原因。\n- 建议：将 \"causal exclusion\" 改为 \"diagnostic analysis\"；承认 SS 无法消除 gap 说明存在其他因素。\n\n### Should-Fix 问题\n\n**W1** GAR 指标的 construct validity 不充分。缺乏 GAR 与标准生成质量指标的 correlation analysis。\n\n**W2** 单一数据集 + 有限模型规模。仅 UltraChat 8K + ~7B 模型。\n\n**W3** 缺失重要近期相关工作：Wan et al. (2026) \"Conversational Inertia\"（arXiv:2602.03664）、arXiv:2603.04783。\n\n**W4** β-steering 实际可部署性存疑。需要推理时识别 goal tokens，β 选择高度依赖超参搜索。\n\n**W5** 方法技术新颖性有限。ThreadGate=ReZero+turn embedding，SS 沿用 Bengio et al. 2015，β-steering 是简单 logit bias。\n\n### Questions\n\nQ1: GAR 与 downstream 质量的 correlation 是否有量化数据？\nQ2: SS 无法将 gap 压缩到 <1.3×，残留 gap 归因于什么？\nQ3: 4 维 turn embedding 在 >10 turns 中表示能力是否足够？\nQ4: Llama 需要 β≥5 而 Qwen β=3 即可，方法通用性如何？\nQ5: Wan et al. (2026) 的 \"conversational inertia\" 与本文 GAR decay 是否同一现象？\n\n---\n\n请对以上每个要点逐条回应 [AGREE] 或 [REBUT]。",
  "reviewer_id": "1",
  "project": "turn_residual_gating",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以��是 Reviewer 2 的完��审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意���说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] **\"Collapse\" overclaiming——标题和全文的核心叙事缺乏下游证据支撑**\n- GAR 衰减并不等于生成质量崩溃。唯一下游评估是 instruction retention（N=54），ThreadGate 改进 +23.8pp（content constraints）但样本量不足。MMLU 仅证明\"无害\"。\n- 建议：增加大规模下游评估（MT-Bench、user preference studies）建立 GAR 与生成质量关联；或显著弱化 \"collapse\" 语言。\n\n**N2** [critical] **因果声明强度超过证据——\"causal exclusion chain\" 逻辑链存在缺口**\n- §5.1 门控值相关性证据非因果；§5.2 排除一个替代假设≠证明目标假设；§5.4 SS 有效只说明分布差异是\"一个\"因素；SS 未消除 gap 说明不是唯一原因。\n- 建议：将 \"causal exclusion\" 改为 \"diagnostic analysis\"；承认 SS 无法消除 gap 说明存在其他因素。\n\n### Should-Fix 问题\n\n**W1** GAR 指标的 construct validity 不充分。缺乏 GAR 与标准生成质量指标的 correlation analysis。\n\n**W2** 单一数据集 + 有限模型规模。仅 UltraChat 8K + ~7B 模型。\n\n**W3** 缺失重要近期相关工作：Wan et al. (2026) \"Conversational Inertia\"（arXiv:2602.03664）、arXiv:2603.04783。\n\n**W4** β-steering 实际可部署性存疑。需要推理时识别 goal tokens，β 选择高度依赖超参搜索。\n\n**W5** 方法技术新颖性有限。ThreadGate=ReZero+turn embedding，SS 沿用 Bengio et al. 2015，β-steering 是简单 logit bias。\n\n### Questions\n\nQ1: GAR 与 downstream 质量的 correlation 是否有量化数据？\nQ2: SS 无法将 gap 压缩到 <1.3×，残留 gap 归因于什么？\nQ3: 4 维 turn embedding 在 >10 turns 中表示能力是否足够？\nQ4: Llama 需要 β≥5 而 Qwen β=3 即可，方法通用性如何？\nQ5: Wan et al. (2026) 的 \"conversational inertia\" 与本文 GAR decay 是否同一现象？\n\n---\n\n请对以上每个要点逐条回应 [AGREE] 或 [REBUT]。",
    "reviewer_id": "1",
    "project": "turn_residual_gating",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-25T05:47:04.942881+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1661
}
```

</details>

---


### Assistant

_source line 360 · 2026-05-25T05:47:09.132712+00:00_

交叉分享已派发。两位 Reviewer 正在互相审阅对方意见并准备 [AGREE]/[REBUT] 回应。等待交叉回应返回后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 361 · 2026-05-25T05:47:11.884079+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿总结**：Overall 3.0（Findings 级别）。

两个 Critical 问题：
1. **GAR 与下游表现弱相关**（r=0.200，仅解释 4% 方差）——全文优化的核心指标对实际对话质量的预测力不足，缺乏 MT-Bench 等标准基准评测和人工评估
2. **消融实验 single-seed**——Table 1 五方对比仅 seed 42，统计检验以 conversation 为单元（衡量 within-run 而非 between-run variability），无法排除特定随机初始化的偶然性

6 个 Should-Fix：ThreadGate 本身不防 AR collapse（SS 才是关键）但 credit assignment 不清晰、N=5 长对话评估样本不足、PCGrad modus tollens 假设过强、多重比较未校正、单一数据集、缺标准多轮基准。

诊断贡献（TF-AR gap 8-17× 量化、因果排除链）是新颖且扎实的，附录分析体现了良好的实验功底。若补充多 seed 消融 + MT-Bench + SS×ThreadGate 交叉消融，有上调至 3.5 的空间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 362 · 2026-05-25T05:47:17.294086+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 32

## Round 32

20 recorded events


### User

_source line 363 · 2026-05-25T05:48:49.898317+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: GAR 与下游任务表现的弱相关性动摇优化目标合理性**

完全同意。这与我在 R2-N1 中提出的 "collapse overclaiming" 问题一致。R1 提供了更具体的量化论据：r=0.200, r²=0.04。论文自身在 Appendix B 中承认 GAR-compliance 相关性 "statistically significant but modest"，并列举了其他影响因素（procedural memory、constraint specificity、conversation-topic interaction）。然而，全文从 Title 到 Conclusion 都以 GAR 改善作为核心成功叙事，这与 4% 解释方差的现实严重脱节。

补充一个 R1 未提到的问题：即使 r=0.200 的 p=0.007 统计显著，这只在 McNemar's test 的 N=54 paired 样本（18 types × 3 conversations）上得出。这个样本量下，任何 modest correlation 的置信区间都会非常宽（粗略估计 95% CI: ~[0.05, 0.35]），进一步削弱了将 GAR 作为核心指标的合理性。

R1 建议的 MT-Bench 评测和 100+ 对话人工评估是必要的。

---

**[AGREE] R1-N2: 消融实验 single-seed 设计，统计检验 unit of analysis 不恰当**

同意核心关切，但有细微补充。

论文确实在 Appendix T 中对 ThreadGate 和 Scheduled Sampling 做了 3-seed 验证（seeds 42, 123, 456），结果显示 cross-seed variance 较低（AR GAR std=0.004 for ThreadGate, 对应 CoV=9%）。但 R1 的关键观察是正确的：**Table 1 中 Base、PCGrad、Uniform Gate 三个重要消融变体仅有 seed 42 单次结果。** 这使得这些变体之间的对比（尤其是 PCGrad vs Base, UG vs TG）无法排除 seed-level variance 的混淆。

R1 关于 unit of analysis 的问题也很重要：Table 6 的 Wilcoxon signed-rank test 以 conversation 为单元（N=50），衡量的是 within-run variability。论文需要的是 between-run variability 来支撑配置间的对比结论。即使只看 Appendix T 的数据：ThreadGate 3 seeds 的 AR GAR 分别为 0.047/0.043/0.047，这种低方差在 3 个 seed 上是否足够可靠，值得质疑。

---

### Should-Fix 问题

**[AGREE] R1-W1: ThreadGate 本身不能防止 AR collapse；SS+LoRA-only 消融缺失**

这是非常关键的消融缺失。从论文数据看：
- ThreadGate (TG) 的 AR GAR ≈ 0.047（Table 1），与 Base 的 0.018 相比仅 ~2.6× 改善
- Scheduled Sampling (SS) 的 AR GAR ≈ 0.401（Figure 5），相比 TG 提升 ~8.5×

这意味着 **SS 是压缩 TF-AR gap 的主要贡献者，ThreadGate 的贡献相对边际**。论文缺少 SS+LoRA-only 这一关键消融——如果 SS+LoRA-only 能达到与 SS+ThreadGate 相似的 GAR 水平，那么 ThreadGate 作为架构贡献的价值将大幅降低，全文的 contribution framing 需要根本性调整。

Section 6 Discussion 中论文轻描淡写地提到 "SS provides training-time mitigation with no inference cost"，但没有直面 ThreadGate vs SS 的贡献归因问题。

---

**[AGREE] R1-W2: N=5 扩展 AR 评估样本量不足**

同意。N=5 conversations 对于长对话泛化结论（§4.2, Appendix D）远远不够。论文在 Appendix D 中报告了 per-turn GAR 动态和 gap scaling 趋势，但基于 5 个对话的趋势外推（"gap would exceed 100× at 20 turns"）缺乏统计基础。建议至少 N≥20。

---

**[AGREE] R1-W3: PCGrad modus tollens 论证依赖过强假设**

同意，这与我在 R2-N2 中的因果声明过强问题一致。R1 的论述比我更精确：PCGrad 不仅测试 gradient conflict 假设，它还改变了整个优化景观（将梯度投影到对方梯度的法平面上）。如果投影操作本身引入了新的优化问题（如 §5.2 中报告的 "effect reverses" 和 NTP magnitude 增长 7.5× to 14.7×），那么 PCGrad 的失败可能反映的是投影副作用，而非 gradient conflict 不存在。

论文用 Appendix L 中的 gradient statistics 部分回应了这一点（full gradient statistics in Appendix L.1），但那些数据本身也是 PCGrad 条件下的，不能作为独立验证。

---

**[REBUT] R1-W4: 多重比较未做校正**

部分反驳。论文在 Appendix E（page 30）明确声明："All reported significant results (p ≤ 0.05) survive Holm-Bonferroni correction for the 4 primary comparisons within each f level." 因此，**主要对比的多重比较校正已经完成。**

但 R1 的担忧对 instruction retention 分析（18 categories, Appendix C）仍然成立——per-category 的 McNemar's test 未报告多重比较校正。论文在 Appendix C 中提到 "reflecting the small sample size (18 constraint types)"，但没有对 18 个分类的多重比较做 FDR 或 Bonferroni 校正。

结论：R1 的关切**对主要实验部分不成立**（已有 Holm-Bonferroni），但**对 Appendix C 的 instruction retention 分析成立**。

---

**[AGREE] R1-W5: 单一数据集（UltraChat）**

完全同意，与我在 R2-W2 中的观点一致。

---

**[AGREE] R1-W6: 缺乏标准多轮对话基准评测**

同意，与我在 R2-N1 中强调的下游评估不足一致。MT-Bench 是最直接的补充方向。

---

### Questions

**[AGREE] R1-Q1: SS+LoRA-only 的 TF-AR gap？**
同 W1，这是关键缺失消融。

**[AGREE] R1-Q2: Table 1 消融是否全部 seed 42？**
论文应在 Table 1 或 §4.1 中明确标注。Appendix A (Table 2) 似乎只列出了通用超参数，未逐配置标注 seed。

**[AGREE] R1-Q3: GAR 是否不是好代理指标？**
同 N1。r²=0.04 的 proxy metric 难以支撑全文叙事。但我补充一点：GAR 的价值可能不在于预测下游任务表现，而在于作为 *diagnostic probe* 揭示注意力分配的系统性偏移。论文如果将 GAR 重新定位为诊断工具而非优化目标，N1 的严重性会降低。

**[AGREE] R1-Q4: β-steering 最优 β 的 architecture dependence**
与我在 R2-W4 和 R2-Q4 中的观点一致。Qwen β=3 vs Llama β≥5 的差异暗示该方法需要 per-model tuning，限制实用性。

**[AGREE] R1-Q5: 其他数据集上 GAR decay 是否一致？**
同 W5 / R2-W2。

---

### 综合评价

R1 的审稿聚焦方法严谨性和实验设计，与我聚焦新颖性和写作质量形成互补。我们在以下核心问题上高度一致：

1. **GAR 的下游预测力不足**（R1-N1 ≈ R2-N1）——这是最影响接收决定的问题
2. **因果声明过强**（R1-W3 ≈ R2-N2）
3. **单一数据集**（R1-W5 ≈ R2-W2）
4. **下游评估不足**（R1-W6 ≈ R2-N1）

R1 额外识别了两个重要问题我未重点覆盖：
- **single-seed 消融设计**（R1-N2）：合理的统计方法论关切
- **SS vs ThreadGate 贡献归因不清**（R1-W1）：我在 R2-W5 中提到方法新颖性有限，但 R1 更精确地指出了缺失的关键消融

R1 唯一我部分反驳的是 **W4（多重比较）**：主要实验已有 Holm-Bonferroni 校正，但 instruction retention 分析确实缺少校正。

R1 给出 3.0（Findings），我给出 3.5（Borderline Conference）。差异主要在于我认为论文的**诊断框架和问题发现**本身有独立价值，即使方法贡献是增量的。但如果 GAR 的 construct validity 问题（r²=0.04）得不到解决，我愿意将评分下调至 3.0。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-25T05:49:36.706584+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_project_file,update_review_issues,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_project_file,update_review_issues,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-25T05:49:36.757233+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-25T05:49:44.892132+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-25T05:49:44.943338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-25T05:49:48.558100+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
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

_source line 369 · 2026-05-25T05:49:48.608750+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-25T05:49:51.471578+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-25T05:49:51.522169+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-25T05:49:57.798835+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-25T05:49:57.799272+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-25T05:49:58.151508+00:00_

1	# Review Issues Tracker — turn_residual_gating
2	# Round 1 (2026-05-19, dream_20260519T145320)
3	# Round 2 (2026-05-22, fresh re-review of revised paper)
4	# Round 3 (2026-05-22, fresh re-review)
5	# Round 4 (2026-05-22, fresh re-review — current round)
6	
7	# ============================================================
8	# Issues from Round 1 — status updates through Round 4
9	# ============================================================
10	
11	- id: "R1-N1"
12	  summary: "所有引用渲染为 '?'——bibliography 编译失败"
13	  category: format
14	  severity: info
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 1
18	  mentions:
19	    - round: 1
20	      reviewers: [1, 2]
21	      note: "Dream paper artifact。"
22	    - round: 2
23	      reviewers: []
24	      note: "视觉审查确认无 [?] 未解析引用。已修复。"
25	    - round: 3
26	      reviewers: []
27	      note: "Round 3 视觉审查确认无未解析引用。维持 resolved。"
28	    - round: 4
29	      reviewers: []
30	      note: "Round 4 视觉审查确认无未解析引用。维持 resolved。"
31	  action_items:
32	    - round: 1
33	      action: "Paper Agent 确保 bibtex 编译正确"
34	      assigned_to: paper_agent
35	      status: done
36	  resolution: "Round 2 视觉审查确认已修复。"
37	  resolution_round: 2
38	
39	- id: "R1-N2"
40	  summary: "单种子支撑结论——统计功效不足 + AR 评估 N=5 过小"
41	  category: experiment
42	  severity: critical
43	  status: open
44	  first_raised_round: 1
45	  last_seen_round: 4
46	  mentions:
47	    - round: 1
48	      reviewers: [1, 2]
49	      note: "Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。"
50	    - round: 2
51	      reviewers: [1, 2]
52	      note: "ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。"
53	    - round: 3
54	      reviewers: [1, 2]
55	      note: "AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。"
56	    - round: 4
57	      reviewers: [1, 2]
58	      note: "两位 Reviewer 独立列为 Critical Must-Fix。R1 强调 N=5 无法提供有意义统计推断力，0.015 vs 0.025 差异无法判断显著性。R2 确认这是核心量化证据的根本缺陷。5 路对比中仅 ThreadGate 有 2 seeds，其余单 seed。"
59	  action_items:
60	    - r
…[truncated 25457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-25T05:49:58.151904+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-25T05:36:50.020878+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_640e53b6afbbd5e34eb7273cd5a707a0\", \"skipped_at\": \"2026-05-25T05:44:29.434298+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-25T05:49:58.152073+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-25T05:49:58.202545+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T05:36:49.054039+00:00\", \"completed_at\": \"2026-05-25T05:41:11.177086+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"Figure 4（Scheduled sampling compression）尺寸偏小，柱状图条形窄、标签字号小，审稿人在屏幕上可能难以区分各 training condition 的差异\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 6a（per-layer gate values）将 28 层的逐层数据压缩在单栏宽度内，个别柱体过窄（<2px），建议改用折线图或放大为 figure* 全宽\"}, {\"severity\": \"warning\", \"dimension\": \"pages 5,7,8\", \"message\": \"多个 bar chart（Figures 3/5/6b）使用高饱和度配色（亮橙+亮蓝+亮绿），对比强烈但美观度偏低；与用户规则\\\"配色饱和度对比别太高\\\"不符\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item——Figure 1 出现在 Page 2，仍在前 3 页内，符合要求。若能将 Figure 1 提前到首页底部（如缩小为单栏预览），审稿人锚定更快\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 caption 较长（~7 行），内容自包含（好），但视觉上偏密集\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 5 只有两根柱子（β=0 vs β=5），信息密度偏低——可考虑与其他相关数据合并为多面板图\"}, {\"severity\": \"info\", \"dimension\": \"page 30\", \"message\": \"Appendix 中出现整页纯文本（Extended Training Dynamics 讨论段），无 display item。因为是统计方法论讨论，可以接受\"}, {\"severity\": \"info\", \"dimension\": \"pages 25-26\", \"message\": \"Tables 19-22（per-seed / per-turn results）列数较多，数据密集，但字号尚可辨认\"}, {\"severity\": \"info\", \"dimension\": \"pages 16,18,19\", \"message\": \"部分 Appendix 图表（Figures 8/10/13）的 axis label 和 legend 字号偏小（约正文 60-65%），建议统一到 ≥70%\"}], \"counts\": {\"critical\": 0, \"warning\": 3, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-25T05:53:45.252635+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "turn_residual_gating",
  "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review)\n# Round 4 (2026-05-25, fresh re-review — current round)\n# Cross-response phase completed: R1↔R2 high convergence\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 4\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 视觉审查确认无未解析引用。维持 resolved。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足 + AR 评估 N=5 过小\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立列为 Critical Must-Fix。交叉回应 R2 完全同意 R1 论证。R2 补充：Appendix T 3-seed CoV=9% 仅覆盖 TG，Table 1 Base/PCGrad/UG 仍为单 seed。Appendix T N=3 能否可靠估计 between-run variance 也值得质疑。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"D048: 6 条件 × 3 seeds from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"AR 评估扩大至 N=50 + bootstrap 95% CI + 条件间成对检验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件 + 显著性检验 + CI\"\n      assigned_to: agent\n      status: in_progress\n      note: \"N=50 code fix underway; multi-seed queue running.\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。未再被提出。\"\n    - round: 4\n      reviewers: []\n      note: \"TF 评估样本量已充分。AR N=5 问题在 R1-N2 中追踪。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。AR N=5 问题移至 R1-N2 追踪。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。维持 resolved。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"额外问题：mean/median 未双报，AR/TF 样本量不匹配，attention spikes 未解释。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Should-Fix（仅 3/5 条件削弱 cross-model generality 声明）。R2 建议标题改为 'Cross-Model Replication'。R2-M2 指出 median vs mean 切换有 metric selection 之嫌。交叉回应 R2 同意 R1 观点。\"\n  action_items:\n    - round: 2\n      action: \"D048: 补充 Llama PCGrad+UG 训练+评估\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"Llama 5-way GPU 实验无法在 DDL 内完成；写作降级：§5.5 标题→Cross-Model Replication + mean/median 双报\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2/3/4 未被独立提出。论文核心 claim 已转向 exposure bias。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"双种子差异大（GAR 0.318 vs 0.418）且策略不同。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应确认完全一致。R2 同意 R1 关于 SS 是压缩 TF-AR gap 的主要贡献者而 ThreadGate 贡献边际的分析。SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047，SS 贡献 ~8.5× 提升。\"\n  action_items:\n    - round: 2\n      action: \"D048: SS 3-seed from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"3 seeds (s42/s123/s456) + mean±std；abstract/conclusion 弱化措辞\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2 — status updates through Round 4\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——contribution 措辞需调整\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"删除 'in principle applicable'。'first' → 'to our knowledge, the first'。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W3: 'to our knowledge, the first' 仍被质疑。交叉回应 R2 进一步指出即使 GAR 不适合做优化目标，作为 diagnostic probe 仍有价值——如果论文重新定位 GAR 为诊断工具而非优化目标，overclaim 严重性可降低。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 4\n      action: \"删除 'to our knowledge, the first' 修饰语，将 GAR 重新定位为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 过宽。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 仍有异议但 R1 反驳有理。Director 裁定当前标题可接受。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意 R1 关于 'Mechanistic' → 'Diagnostic' 的建议。\"\n  action_items:\n    - round: 2\n      action: \"标题改为 'Per-Layer Residual Gating'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"标题改为反映 exposure bias 核心发现；副标题 'Mechanistic' → 'Diagnostic'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"原文为 'Goal Accessibility Ratio'。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"arXiv 原文验证确认。Critical Must-Fix。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮 Reviewer 未独立提出。待确认是否已修复。\"\n  action_items:\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因——替代假说讨论不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 降 Should-Fix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意 R1（W3）：PCGrad 失败可能反映投影副作用（NTP magnitude 增长 7.5×-14.7×），而非 gradient conflict 不存在。Appendix L 数据在 PCGrad 条件下获得，不能作为独立验证。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"§6 扩展 exposure bias 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标——instruction retention 不显著但占页过多\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"McNemar p=0.077 不显著。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"占 Discussion 过多篇幅。建议移入 Appendix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 补充：r=0.200 的 95% CI ≈ [0.05, 0.35]（N=54 paired samples），置信区间过宽。R2 建议将 GAR 重新定位为 diagnostic probe 而非优化目标可缓解此问题。\"\n  action_items:\n    - round: 2\n      action: \"D048: N=200 扩容指令保持实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"提升已有显著数据至主文 + 重新定位 GAR 为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。待确认。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"orphan 条目。\"\n    - round: 2\n      reviewers: [2]\n      note: \"'and others' vs 完整作者列表不一致。\"\n    - round: 3\n      reviewers: [2]\n      note: \"grattafiori2024llama3 格式不一致。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-M3: Raposo et al. 2024 → ICML 2024；Gromov et al. 年份一致性。交叉回应未新增。\"\n  action_items:\n    - round: 4\n      action: \"统一 bib 格式\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"Reproducibility 3.0/5。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 AR 列需扩容\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现未在表格中呈现。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 列存在但仅 N=5。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M2: Table 1 AR 列缺 GAR-D 和 PPL。与 R1-N2 联动。\"\n  action_items:\n    - round: 4\n      action: \"AR 列更新为 N≥50 数据 + CI + GAR-D + PPL\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字重复 8+ 次\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 多章节重复。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"出现 8+ 次。\"\n    - round: 4\n      reviewers: [2]\n      note: \"交叉回应 R2 同意应去冗。\"\n  action_items:\n    - round: 4\n      action: \"Abstract/§4.2 保留完整数字，其余改用回指\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 泛化声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable' 未验证。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-N1。\"\n  action_items:\n    - round: 4\n      action: \"删除泛化声称，合并至 R2-N1\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. split-softmax 缺实验对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争方法。R1 认为超 scope。\"\n    - round: 4\n      reviewers: [2]\n      note: \"交叉回应 R2 维持观点。\"\n  action_items:\n    - round: 4\n      action: \"Related Work 加强理论论证 + Limitations 承认\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure/Table caption overclaim + 重复句\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Figure caption 可能有 overclaim。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Figure 4 caption 重复句。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 3\n      action: \"修正 Fig 3b/Table 1/Fig 4 caption 的 overclaim + 删除 Fig 4 重复句\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后数字更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Abstract/Intro gap 数字需从单 seed 更新为 mean±std。\"\n    - round: 4\n      reviewers: []\n      note: \"仍待 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后统一更新\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"SS 3-seed variance 极大时需应急 framing。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 两 seed 差异 31% 进一步增加应急计划紧迫性。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance\"\n      assigned_to: director\n      status: open\n\n# ============================================================\n# Issues from Round 3 — status updates through Round 4\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"约 8.4 页。Paper Agent 已压缩至 8.0 页。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M7: 页数符合 8 页限制。\"\n  resolution: \"Round 4 确认页数合规。\"\n  resolution_round: 4\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad scope 过度概括\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"'gradient conflict' 未加 'directional' 限定。\"\n    - round: 4\n      reviewers: []\n      note: \"交叉回应 R2 同意 R1（W3）：PCGrad 失败可能反映投影副作用，限定 scope 必要。\"\n  action_items:\n    - round: 3\n      action: \"'gradient conflict' → 'gradient direction conflict'；结论提及 magnitude imbalance 未排除\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869) 引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Rhea: Role-aware Heuristic Episodic Attention。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-W7-new 追踪。\"\n  action_items:\n    - round: 3\n      action: \"添加 bib 条目 + §2/§6 引用对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出，R2 反驳（不影响 TF-AR gap）。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-Q4: LoRA rank 16 是否影响结论？交叉回应 R2 同意 R1（Q4）。\"\n  action_items:\n    - round: 4\n      action: \"§4.2 或 Limitations 加一句 acknowledge LoRA rank 可能影响 gate 效用上界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"'NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)' 待确认。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"确认准确性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R3-NEW-1\"\n  summary: \"UG 描述不清——未说明仍为可学习 MLP\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"UG 描述仅说 'gates without turn embedding'，未明确仍是可学习的 content-conditioned MLP。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"§4.1 或 §3 加一句说明\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-NEW-2\"\n  summary: \"Contribution (4) 混淆开发迭代与系统消融\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"'seven loss formulations and four training configurations' 混淆了 v1-v7 loss iteration 和五路系统消融。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"拆分为 'loss design iterations (Appendix A)' + 'systematic conditions comparison (Table 1)'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# New issues from Round 4\n# ============================================================\n\n- id: \"R4-N1\"\n  summary: \"GAR 指标与下游任务性能之间缺乏因果验证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 完全同意 R1：r=0.200, r²=0.04。R2 补充 N=54 下 95% CI ≈ [0.05, 0.35] 过宽。R2 建议重新定位 GAR 为 diagnostic probe 可缓解但不消除该问题。两位 Reviewer 一致认为这是最影响接收决定的问题。\"\n  action_items:\n    - round: 4\n      action: \"已有数据提升至主文 + GAR 重定位为 diagnostic probe + 补充 MT-Bench 或其他下游评估\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-N2\"\n  summary: \"SS+LoRA-only 消融缺失——ThreadGate 独立贡献不清\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 完全同意 R1（W1）：SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。SS 是压缩 TF-AR gap 的主要贡献者（~8.5× vs TG ~2.6×）。如果 SS+LoRA-only 达到相似水平，ThreadGate 架构贡献将大幅降低。关键缺失消融。\"\n  action_items:\n    - round: 4\n      action: \"需要 SS+LoRA-only 实验数据，或在论文中明确承认 ThreadGate 贡献相对于 SS 是边际的\"\n      assigned_to: agent\n      status: open\n\n- id: \"R4-W1\"\n  summary: \"GAR-D 全条件接近零——干预仅在 last token 成功\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-W5: 即使 TF 下 ThreadGate GAR-D = 0.02。干预仅在 τ-masked last token 成功，泛化性问题未讨论。\"\n  action_items:\n    - round: 4\n      action: \"讨论 GAR-ours vs GAR-D 差异的含义\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W2\"\n  summary: \"Table 1 四舍五入与正文数字精度不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W6: §4.2 称 spread 为 0.75pp 但 Table 1 两位小数显示 1pp。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 增加一位小数，或正文使用与 table 一致的精度\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W3\"\n  summary: \"r_min 数值正文未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M1: r_min 数值在正文中未报告，影响可复现性。\"\n  action_items:\n    - round: 4\n      action: \"在 §3 或 Appendix A 中报告 r_min 数值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-MR1\"\n  summary: \"缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"与 β-steering 思路相似的推理时注意力操控方法，应在 §2 讨论。\"\n  action_items:\n    - round: 4\n      action: \"确认引用存在性并在 §2 引用对比\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W4\"\n  summary: \"Appendix C instruction retention 多重比较未校正\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 部分反驳 R1（W4）：主实验已有 Holm-Bonferroni 校正（Appendix E p30），但 Appendix C 18-category McNemar's test 未做 FDR/Bonferroni 校正。R1 关切对主实验不成立，对 Appendix C 成立。\"\n  action_items:\n    - round: 4\n      action: \"Appendix C per-category 分析补充 Holm-Bonferroni 或 FDR 校正\"\n      assigned_to: paper_agent\n      status: open\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "turn_residual_gating",
    "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review)\n# Round 4 (2026-05-25, fresh re-review — current round)\n# Cross-response phase completed: R1↔R2 high convergence\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 4\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 视觉审查确认无未解析引用。维持 resolved。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足 + AR 评估 N=5 过小\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立列为 Critical Must-Fix。交叉回应 R2 完全同意 R1 论证。R2 补充：Appendix T 3-seed CoV=9% 仅覆盖 TG，Table 1 Base/PCGrad/UG 仍为单 seed。Appendix T N=3 能否可靠估计 between-run variance 也值得质疑。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"D048: 6 条件 × 3 seeds from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"AR 评估扩大至 N=50 + bootstrap 95% CI + 条件间成对检验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件 + 显著性检验 + CI\"\n      assigned_to: agent\n      status: in_progress\n      note: \"N=50 code fix underway; multi-seed queue running.\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。未再被提出。\"\n    - round: 4\n      reviewers: []\n      note: \"TF 评估样本量已充分。AR N=5 问题在 R1-N2 中追踪。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。AR N=5 问题移至 R1-N2 追踪。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。维持 resolved。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"额外问题：mean/median 未双报，AR/TF 样本量不匹配，attention spikes 未解释。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Should-Fix（仅 3/5 条件削弱 cross-model generality 声明）。R2 建议标题改为 'Cross-Model Replication'。R2-M2 指出 median vs mean 切换有 metric selection 之嫌。交叉回应 R2 同意 R1 观点。\"\n  action_items:\n    - round: 2\n      action: \"D048: 补充 Llama PCGrad+UG 训练+评估\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"Llama 5-way GPU 实验无法在 DDL 内完成；写作降级：§5.5 标题→Cross-Model Replication + mean/median 双报\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2/3/4 未被独立提出。论文核心 claim 已转向 exposure bias。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"双种子差异大（GAR 0.318 vs 0.418）且策略不同。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应确认完全一致。R2 同意 R1 关于 SS 是压缩 TF-AR gap 的主要贡献者而 ThreadGate 贡献边际的分析。SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047，SS 贡献 ~8.5× 提升。\"\n  action_items:\n    - round: 2\n      action: \"D048: SS 3-seed from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"3 seeds (s42/s123/s456) + mean±std；abstract/conclusion 弱化措辞\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2 — status updates through Round 4\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——contribution 措辞需调整\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"删除 'in principle applicable'。'first' → 'to our knowledge, the first'。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W3: 'to our knowledge, the first' 仍被质疑。交叉回应 R2 进一步指出即使 GAR 不适合做优化目标，作为 diagnostic probe 仍有价值——如果论文重新定位 GAR 为诊断工具而非优化目标，overclaim 严重性可降低。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 4\n      action: \"删除 'to our knowledge, the first' 修饰语，将 GAR 重新定位为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 过宽。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 仍有异议但 R1 反驳有理。Director 裁定当前标题可接受。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意 R1 关于 'Mechanistic' → 'Diagnostic' 的建议。\"\n  action_items:\n    - round: 2\n      action: \"标题改为 'Per-Layer Residual Gating'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"标题改为反映 exposure bias 核心发现；副标题 'Mechanistic' → 'Diagnostic'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"原文为 'Goal Accessibility Ratio'。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"arXiv 原文验证确认。Critical Must-Fix。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮 Reviewer 未独立提出。待确认是否已修复。\"\n  action_items:\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因——替代假说讨论不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 降 Should-Fix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意 R1（W3）：PCGrad 失败可能反映投影副作用（NTP magnitude 增长 7.5×-14.7×），而非 gradient conflict 不存在。Appendix L 数据在 PCGrad 条件下获得，不能作为独立验证。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"§6 扩展 exposure bias 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标——instruction retention 不显著但占页过多\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"McNemar p=0.077 不显著。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"占 Discussion 过多篇幅。建议移入 Appendix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 补充：r=0.200 的 95% CI ≈ [0.05, 0.35]（N=54 paired samples），置信区间过宽。R2 建议将 GAR 重新定位为 diagnostic probe 而非优化目标可缓解此问题。\"\n  action_items:\n    - round: 2\n      action: \"D048: N=200 扩容指令保持实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"提升已有显著数据至主文 + 重新定位 GAR 为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。待确认。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"orphan 条目。\"\n    - round: 2\n      reviewers: [2]\n      note: \"'and others' vs 完整作者列表不一致。\"\n    - round: 3\n      reviewers: [2]\n      note: \"grattafiori2024llama3 格式不一致。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-M3: Raposo et al. 2024 → ICML 2024；Gromov et al. 年份一致性。交叉回应未新增。\"\n  action_items:\n    - round: 4\n      action: \"统一 bib 格式\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"Reproducibility 3.0/5。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 AR 列需扩容\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现未在表格中呈现。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 列存在但仅 N=5。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M2: Table 1 AR 列缺 GAR-D 和 PPL。与 R1-N2 联动。\"\n  action_items:\n    - round: 4\n      action: \"AR 列更新为 N≥50 数据 + CI + GAR-D + PPL\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字重复 8+ 次\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 多章节重复。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"出现 8+ 次。\"\n    - round: 4\n      reviewers: [2]\n      note: \"交叉回应 R2 同意应去冗。\"\n  action_items:\n    - round: 4\n      action: \"Abstract/§4.2 保留完整数字，其余改用回指\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 泛化声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable' 未验证。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-N1。\"\n  action_items:\n    - round: 4\n      action: \"删除泛化声称，合并至 R2-N1\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. split-softmax 缺实验对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争方法。R1 认为超 scope。\"\n    - round: 4\n      reviewers: [2]\n      note: \"交叉回应 R2 维持观点。\"\n  action_items:\n    - round: 4\n      action: \"Related Work 加强理论论证 + Limitations 承认\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure/Table caption overclaim + 重复句\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Figure caption 可能有 overclaim。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Figure 4 caption 重复句。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 3\n      action: \"修正 Fig 3b/Table 1/Fig 4 caption 的 overclaim + 删除 Fig 4 重复句\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后数字更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Abstract/Intro gap 数字需从单 seed 更新为 mean±std。\"\n    - round: 4\n      reviewers: []\n      note: \"仍待 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后统一更新\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"SS 3-seed variance 极大时需应急 framing。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 两 seed 差异 31% 进一步增加应急计划紧迫性。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance\"\n      assigned_to: director\n      status: open\n\n# ============================================================\n# Issues from Round 3 — status updates through Round 4\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"约 8.4 页。Paper Agent 已压缩至 8.0 页。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M7: 页数符合 8 页限制。\"\n  resolution: \"Round 4 确认页数合规。\"\n  resolution_round: 4\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad scope 过度概括\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"'gradient conflict' 未加 'directional' 限定。\"\n    - round: 4\n      reviewers: []\n      note: \"交叉回应 R2 同意 R1（W3）：PCGrad 失败可能反映投影副作用，限定 scope 必要。\"\n  action_items:\n    - round: 3\n      action: \"'gradient conflict' → 'gradient direction conflict'；结论提及 magnitude imbalance 未排除\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869) 引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Rhea: Role-aware Heuristic Episodic Attention。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-W7-new 追踪。\"\n  action_items:\n    - round: 3\n      action: \"添加 bib 条目 + §2/§6 引用对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出，R2 反驳（不影响 TF-AR gap）。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-Q4: LoRA rank 16 是否影响结论？交叉回应 R2 同意 R1（Q4）。\"\n  action_items:\n    - round: 4\n      action: \"§4.2 或 Limitations 加一句 acknowledge LoRA rank 可能影响 gate 效用上界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"'NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)' 待确认。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"确认准确性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R3-NEW-1\"\n  summary: \"UG 描述不清——未说明仍为可学习 MLP\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"UG 描述仅说 'gates without turn embedding'，未明确仍是可学习的 content-conditioned MLP。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"§4.1 或 §3 加一句说明\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-NEW-2\"\n  summary: \"Contribution (4) 混淆开发迭代与系统消融\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"'seven loss formulations and four training configurations' 混淆了 v1-v7 loss iteration 和五路系统消融。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"拆分为 'loss design iterations (Appendix A)' + 'systematic conditions comparison (Table 1)'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# New issues from Round 4\n# ============================================================\n\n- id: \"R4-N1\"\n  summary: \"GAR 指标与下游任务性能之间缺乏因果验证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 完全同意 R1：r=0.200, r²=0.04。R2 补充 N=54 下 95% CI ≈ [0.05, 0.35] 过宽。R2 建议重新定位 GAR 为 diagnostic probe 可缓解但不消除该问题。两位 Reviewer 一致认为这是最影响接收决定的问题。\"\n  action_items:\n    - round: 4\n      action: \"已有数据提升至主文 + GAR 重定位为 diagnostic probe + 补充 MT-Bench 或其他下游评估\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-N2\"\n  summary: \"SS+LoRA-only 消融缺失——ThreadGate 独立贡献不清\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 完全同意 R1（W1）：SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。SS 是压缩 TF-AR gap 的主要贡献者（~8.5× vs TG ~2.6×）。如果 SS+LoRA-only 达到相似水平，ThreadGate 架构贡献将大幅降低。关键缺失消融。\"\n  action_items:\n    - round: 4\n      action: \"需要 SS+LoRA-only 实验数据，或在论文中明确承认 ThreadGate 贡献相对于 SS 是边际的\"\n      assigned_to: agent\n      status: open\n\n- id: \"R4-W1\"\n  summary: \"GAR-D 全条件接近零——干预仅在 last token 成功\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-W5: 即使 TF 下 ThreadGate GAR-D = 0.02。干预仅在 τ-masked last token 成功，泛化性问题未讨论。\"\n  action_items:\n    - round: 4\n      action: \"讨论 GAR-ours vs GAR-D 差异的含义\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W2\"\n  summary: \"Table 1 四舍五入与正文数字精度不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W6: §4.2 称 spread 为 0.75pp 但 Table 1 两位小数显示 1pp。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 增加一位小数，或正文使用与 table 一致的精度\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W3\"\n  summary: \"r_min 数值正文未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M1: r_min 数值在正文中未报告，影响可复现性。\"\n  action_items:\n    - round: 4\n      action: \"在 §3 或 Appendix A 中报告 r_min 数值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-MR1\"\n  summary: \"缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"与 β-steering 思路相似的推理时注意力操控方法，应在 §2 讨论。\"\n  action_items:\n    - round: 4\n      action: \"确认引用存在性并在 §2 引用对比\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W4\"\n  summary: \"Appendix C instruction retention 多重比较未校正\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 部分反驳 R1（W4）：主实验已有 Holm-Bonferroni 校正（Appendix E p30），但 Appendix C 18-category McNemar's test 未做 FDR/Bonferroni 校正。R1 关切对主实验不成立，对 Appendix C 成立。\"\n  action_items:\n    - round: 4\n      action: \"Appendix C per-category 分析补充 Holm-Bonferroni 或 FDR 校正\"\n      assigned_to: paper_agent\n      status: open\n"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-25T05:53:45.404880+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml\", \"bytes\": 23329}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-25T05:56:02.257039+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 4\n\n**Paper**: Turn-Residual Gating for Multi-Turn Dialogue (working title)\n**Venue**: EMNLP 2026 (ARR submission)\n**Reviewers**: R1 (方法严谨性/实验设计), R2 (新颖性/写作质量)\n**Cross-response convergence**: 高度收敛。R2 对 R1 几乎全部 [AGREE]，唯一 [REBUT] 为 W4（多重比较），且仅部分成立。\n\n---\n\n## Summary\n\n本文研究多轮对话中辅助注意力损失（auxiliary attention loss）在自回归推理时的效能退化问题。作者提出 Goal Attention Ratio（GAR）指标量化注意力衰减，设计 ThreadGate（基于对话轮次的残差门控）和 Scheduled Sampling（SS）两种缓解方案，在 Qwen2.5-3B + LoRA 上进行五路对比实验（Base, PCGrad, Uniform Gate, ThreadGate, ThreadGate+SS）。核心发现：所有 teacher-forcing 训练的变体在自回归推理时 GAR 均大幅退化（20-33× gap），Scheduled Sampling 是唯一有效压缩该 gap 的方案，ThreadGate 本身贡献边际。论文将此归因于 exposure bias。Llama-3.1-8B 上做了部分跨模型验证（3/5 条件）。\n\n论文提出了一个有意义的研究问题，实验设计在消融维度上较为完整，SS 的实用发现有价值。但核心指标（GAR）的 construct validity 严重不足（r²=0.04），统计支撑薄弱（多条件单 seed，SS 跨 seed 方差 31%），因果声明超出证据范围，下游任务评估完全缺失。\n\n---\n\n## Strengths\n\n**S1. 重要且未被充分研究的问题。** 多轮对话中辅助注意力损失在推理时失效是一个实际且重要的现象。现有文献对此的系统性量化几乎空白。论文正确识别了这个 gap 并试图填补。\n\n**S2. 系统性五路消融设计。** Base / PCGrad / Uniform Gate / ThreadGate / ThreadGate+SS 的五路对比在方法维度上覆盖了主要假设（梯度冲突、架构设计、训练策略），结构化程度高于该领域多数工作。\n\n**S3. Scheduled Sampling 的实用发现。** SS 显著压缩 TF-AR gap（从 20-33× 降至 ~1.3×）且无推理成本，这一发现对该领域的实践者有直接参考价值。\n\n**S4. 详尽的 Appendix 和可追溯性。** 论文提供了大量补充材料（v1-v7 loss 迭代历史、per-turn 动态、gradient statistics、per-seed 结果），展现了研究过程的透明性。\n\n**S5. β-steering 作为轻量推理时干预。** 无需重训练即可调控注意力分布的方案，有工程实用价值。跨模型（Qwen β=3, Llama β≥5）差异也提供了有价值的 negative signal。\n\n---\n\n## Weaknesses\n\n### Critical（必须修复，否则影响接收）\n\n**C1. GAR 指标的 construct validity 严重不足。** [R1-N1, R2-N1, 交叉一致]\n- GAR 与下游指令保持率的相关性 r=0.200, r²=0.04。全文从标题到结论以 GAR 改善为核心叙事，但 GAR 仅解释 4% 的下游方差。\n- N=54 paired samples 下 95% CI ≈ [0.05, 0.35]，置信区间过宽。\n- β=10 时 PPL 退化至 4.22，表明 GAR 极端提升可能有害，进一步质疑其作为优化目标的合理性。\n- 所有 variants PPL ≈ 2.78, AUC ≈ 0.98——GAR 的巨大差异未映射到任何下游性能差异。\n- **缺少任何标准多轮对话基准评测**（MT-Bench、AlpacaEval 等）。论文的全部评估建立在 GAR 这个未经外部验证的内部指标上。\n- **建议**：补充 MT-Bench 等下游评测（≥100 对话人工评估），或将 GAR 重新定位为 diagnostic probe 而非优化目标/成功指标。\n\n**C2. 单 seed 消融 + SS 跨 seed 方差 31%。** [R1-N2, R1-W5, R2 交叉一致]\n- Table 1 中 Base, PCGrad, Uniform Gate 三个重要条件**仅有 seed=42 单次结果**。ThreadGate 有 2 seeds，SS 有 2 seeds 但策略不同不可直接比较。\n- SS 两 seed AR GAR: 0.318 vs 0.418（相差 31%），说明 between-run variance 极高。Abstract 以确定性语气呈现这些结果（\"compresses the gap to 1.29×\"）构成 overclaim。\n- Appendix T 的 3-seed 验证仅覆盖 ThreadGate（CoV=9%），不能替代全条件多 seed 验证。\n- Table 6 Wilcoxon signed-rank test 以 conversation 为单元（N=50），衡量 within-run variability，无法支撑 between-run 对比结论。\n- **建议**：全部 5 条件 × 3 seeds 完整实验，报告 mean±std。当前单 seed 数据仅能作为 pilot study。\n\n**C3. Exposure bias 因果归因超出证据。** [R2-C3, R1-W3, 交叉一致]\n- 论文将 TF-AR gap 归因于 exposure bias，但未实验排除 KV cache drift 假说（§6 承认，§8 留给 future work）。\n- PCGrad 失败被用作 modus tollens 否定 gradient conflict 假说，但 PCGrad 的投影操作本身引入副作用（NTP magnitude 增长 7.5×-14.7×），失败可能反映投影副作用而非 gradient conflict 不存在。\n- Appendix L 的 gradient statistics 在 PCGrad 条件下获得，不构成独立验证。\n- 对一篇以 \"mechanistic/diagnostic analysis\" 自居的论文，留下核心因果链的最关键环节未验证是不可接受的。\n- **建议**：设计 TF→AR 切换实验区分 prefix-level exposure bias 和 cache-level drift；或大幅弱化因果声称。\n\n### Should-Fix（应修复，影响评分但不单独构成拒稿理由）\n\n**W1. SS+LoRA-only 关键消融缺失。** [R1-W1, R2 交叉一致]\n- TG AR GAR ≈ 0.047（相比 Base ~2.6× 改善），SS AR GAR ≈ 0.401（相比 TG ~8.5× 改善）。SS 是压缩 TF-AR gap 的主要贡献者。\n- 缺少 SS+LoRA-only（不加 ThreadGate）的消融。如果该配置效果相似，ThreadGate 作为架构贡献的价值将大幅降低。\n- §6 未直面 ThreadGate vs SS 的贡献归因问题。\n\n**W2. 单一数据集（UltraChat）。** [R1-W5, R2-W2, 交叉一致]\n- 所有实验仅在 UltraChat 上进行，无法评估 GAR decay 是否为 UltraChat 特异现象。\n- 缺少 ShareGPT、LMSYS-Chat-1M 等替代数据集验证。\n\n**W3. Llama 跨模型验证不完整。** [R1-W1, R2-M2, 交叉一致]\n- 仅 3/5 条件（Base, TG, TG+SS），缺 PCGrad 和 Uniform Gate。\n- Median vs mean 切换在 Qwen→Llama 间不一致，有 metric selection 之嫌。\n- §5.5 标题 \"Cross-Model Validation\" 过度概括，建议改为 \"Cross-Model Replication\"。\n\n**W4. 标题与副标题 overclaim。** [R2-N2, R1-W2, 交叉一致]\n- 标题暗示 gating 固有失败，但实际发现是 exposure bias 的通用问题（LoRA-only 无 gate 表现相同）。\n- \"Mechanistic Analysis\" 副标题与分析深度不匹配——宏观层面非 circuit-level。建议改为 \"Diagnostic Analysis\"。\n\n**W5. Li et al. split-softmax / Rhea 缺实验对比。** [R2-W7-new, R2-W2]\n- 论文声称 split-softmax \"cannot address exposure bias\" 但未实验验证。\n- 作为最直接竞争方法，至少需要理论论证或承认未验证。\n\n**W6. Appendix C instruction retention 多重比较未校正。** [R1-W4, R2 部分反驳]\n- 主实验已有 Holm-Bonferroni 校正（Appendix E p30），此关切对主实验不成立。\n- 但 Appendix C 18-category McNemar's test 未做 FDR/Bonferroni 校正。\n\n**W7. 写作冗余。** [R2-W4-new]\n- '20-33× gap' 至少出现 7 次，'0.064 to 0.727' 出现 4+ 次。\n\n### Minor\n\n**M1.** r_min 数值正文未报告，影响可复现性。[R1-M1]\n**M2.** GAR-D 全条件接近零（ThreadGate TF下仅0.02），说明干预仅在 τ-masked last token 成功，泛化性未讨论。[R1-W5]\n**M3.** Table 1 四舍五入与正文数字精度不一致（0.75pp vs 1pp）。[R2-W6]\n**M4.** LoRA rank=16 是否影响结论未讨论。[R2-Q4]\n**M5.** 无代码/数据发布承诺。[R1-M6, R2-M6]\n**M6.** Bib 格式：Raposo et al. 2024 应更新为 ICML 2024 @inproceedings；Gromov et al. 年份一致性。[R2-M3]\n\n---\n\n## Questions\n\n**Q1.** SS+LoRA-only（不加 ThreadGate）的 TF-AR gap 是多少？如果与 SS+ThreadGate 相似，ThreadGate 的独立贡献是什么？[R1, R2 一致]\n\n**Q2.** Table 1 中 Base, PCGrad, Uniform Gate 是否均为 seed=42？请明确标注。[R1]\n\n**Q3.** 如果 GAR 与下游任务的 r²=0.04，作者是否考虑 GAR 可能不是指令遵循的可靠代理指标？将 GAR 重新定位为 diagnostic probe 而非优化目标是否更准确？[R1, R2 一致]\n\n**Q4.** β-steering 最优 β 的 architecture dependence（Qwen β=3 vs Llama β≥5）意味着什么？该方法是否需要 per-model tuning？[R1, R2 一致]\n\n**Q5.** 其他数据集（ShareGPT, LMSYS-Chat-1M）上 GAR decay 是否一致？[R1, R2 一致]\n\n**Q6.** 是否尝试过更高 LoRA rank（32, 64）？rank=16 下的结论是否因 capacity saturation 被低估？[R2]\n\n---\n\n## Missing References\n\n1. **Zhang et al. 2024** — \"Tell Your Model Where to Attend\"：与 β-steering 思路相似的推理时注意力操控方法，应在 §2 讨论。[R2]\n2. **Rhea (arXiv:2512.06869)** — Role-aware Heuristic Episodic Attention：§2 已讨论但缺实验对比。[R1, R2 跨轮追踪]\n3. **Li et al. 2024** — Split-softmax：最直接竞争方法，需加强理论对比。[R2]\n\n---\n\n## External Review\n\n**状态**：已跳过（skipped at 2026-05-25T05:44:29）。未获得外部审稿数据。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成 (0 critical, 3 warning, 6 info)\n\n**Warning:**\n- Page 6: Figure 4（Scheduled sampling compression）尺寸偏小，柱状图条形窄、标签字号小\n- Page 8: Figure 6a（per-layer gate values）28 层数据压缩在单栏宽度内，个别柱体 <2px，建议改用折线图或全宽\n- Pages 5/7/8: 多个 bar chart 使用高饱和度配色（亮橙+亮蓝+亮绿），与用户规则\"配色饱和度对比别太高\"不符\n\n**Info:**\n- Page 1: 首页无 display item，Figure 1 在 Page 2\n- Page 2: Figure 1 caption ~7 行，偏密集\n- Page 7: Figure 5 仅两根柱子，信息密度低\n- Page 30: Appendix 整页纯文本（可接受）\n- Pages 25-26: Tables 19-22 列数多但字号可辨\n- Pages 16/18/19: Appendix 图表 axis label 约正文 60-65%\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Overall | 3.0 (Findings) | 3.5→3.0 (Findings) | **3.0 (Findings)** |\n| Soundness | 3/5 | 3/5 | 3/5 |\n| Novelty | 2/5 | 2.5/5 | 2/5 |\n| Reproducibility | 3/5 | 4/5 | 3/5 |\n\n### 综合评价\n\n**Overall Score: 3.0 — Findings**\n\n论文识别了一个重要且未被充分研究的问题（多轮对话辅助注意力损失在 AR 推理时的效能退化），五路消融设计系统性较好，SS 的实用发现有直接价值。\n\n然而，三个 Critical 问题共同构成了接收的主要障碍：\n\n1. **GAR construct validity**（r²=0.04）——全文核心叙事建立在一个仅解释 4% 下游方差的指标上，且无任何标准多轮对话基准评测。这不是精度问题，而是整个评估框架的根基问题。\n\n2. **统计不可靠**——多条件单 seed，SS 跨 seed 方差 31%，AR 评估 N=5。当前数据本质上是 pilot study 级别，不足以支撑论文的定量结论。\n\n3. **因果 overclaiming**——exposure bias 归因未排除 KV cache drift，PCGrad modus tollens 论证依赖过强假设。\"Mechanistic analysis\" 的定位与实际分析深度不匹配。\n\nR2 指出论文的**诊断框架和问题发现**本身有独立价值，即使方法贡献是增量的。如果 GAR 被重新定位为 diagnostic probe（而非优化目标），因果声称被大幅弱化，统计问题被修复（全条件 3-seed + N≥50 AR 评估），论文可达到 Findings 水准。当前状态距此仍有实质性 gap。\n\n### 修改优先级\n\n1. **[实验]** 全条件 3-seed × N≥50 AR 评估 + mean±std → 解决 C2\n2. **[实验]** SS+LoRA-only 消融 → 解决 W1\n3. **[评估]** MT-Bench 或等价下游评测 → 部分解决 C1\n4. **[写作]** GAR 重新定位为 diagnostic probe + 因果声称弱化 → 部分解决 C1, C3\n5. **[写作]** 标题/副标题调整 → 解决 W4\n6. **[实验]** 第二数据集验证 → 解决 W2\n\n---\n\n## Detailed Comments\n\n### 交叉回应分歧记录\n\n仅一项分歧，已在报告中体现：\n\n- **R1-W4（多重比较）**：R2 部分反驳——主实验已有 Holm-Bonferroni 校正（Appendix E p30），R1 关切对主实验不成立。但对 Appendix C 18-category McNemar's test 成立。报告中记录为 W6（Should-Fix，限定于 Appendix C）。\n\n### 评分调整说明\n\nR2 初始评分 3.5（Borderline Conference），交叉回应后表示\"如果 GAR 的 construct validity 问题（r²=0.04）得不到解决，愿意将评分下调至 3.0\"。鉴于 C1 目前未解决，R2 有效评分调整为 3.0。两位 Reviewer 共识为 3.0（Findings）。\n\n### 跨轮次追踪\n\n本轮为 Round 4（fresh re-review）。Issue tracker 中有 5 个 Critical 级别未解决问题（R1-N2, R1-W5, R2-C3, R4-N1, R2-N3），12 个 Warning 级别未解决问题，6 个 Info 级别未解决问题。详见 `artifacts/review_issues.yaml`。\n",
  "project": "turn_residual_gating",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Round 4\n\n**Paper**: Turn-Residual Gating for Multi-Turn Dialogue (working title)\n**Venue**: EMNLP 2026 (ARR submission)\n**Reviewers**: R1 (方法严谨性/实验设计), R2 (新颖性/写作质量)\n**Cross-response convergence**: 高度收敛。R2 对 R1 几乎全部 [AGREE]，唯一 [REBUT] 为 W4（多重比较），且仅部分成立。\n\n---\n\n## Summary\n\n本文研究多轮对话中辅助注意力损失（auxiliary attention loss）在自回归推理时的效能退化问题。作者提出 Goal Attention Ratio（GAR）指标量化注意力衰减，设计 ThreadGate（基于对话轮次的残差门控）和 Scheduled Sampling（SS）两种缓解方案，在 Qwen2.5-3B + LoRA 上进行五路对比实验（Base, PCGrad, Uniform Gate, ThreadGate, ThreadGate+SS）。核心发现：所有 teacher-forcing 训练的变体在自回归推理时 GAR 均大幅退化（20-33× gap），Scheduled Sampling 是唯一有效压缩该 gap 的方案，ThreadGate 本身贡献边际。论文将此归因于 exposure bias。Llama-3.1-8B 上做了部分跨模型验证（3/5 条件）。\n\n论文提出了一个有意义的研究问题，实验设计在消融维度上较为完整，SS 的实用发现有价值。但核心指标（GAR）的 construct validity 严重不足（r²=0.04），统计支撑薄弱（多条件单 seed，SS 跨 seed 方差 31%），因果声明超出证据范围，下游任务评估完全缺失。\n\n---\n\n## Strengths\n\n**S1. 重要且未被充分研究的问题。** 多轮对话中辅助注意力损失在推理时失效是一个实际且重要的现象。现有文献对此的系统性量化几乎空白。论文正确识别了这个 gap 并试图填补。\n\n**S2. 系统性五路消融设计。** Base / PCGrad / Uniform Gate / ThreadGate / ThreadGate+SS 的五路对比在方法维度上覆盖了主要假设（梯度冲突、架构设计、训练策略），结构化程度高于该领域多数工作。\n\n**S3. Scheduled Sampling 的实用发现。** SS 显著压缩 TF-AR gap（从 20-33× 降至 ~1.3×）且无推理成本，这一发现对该领域的实践者有直接参考价值。\n\n**S4. 详尽的 Appendix 和可追溯性。** 论文提供了大量补充材料（v1-v7 loss 迭代历史、per-turn 动态、gradient statistics、per-seed 结果），展现了研究过程的透明性。\n\n**S5. β-steering 作为轻量推理时干预。** 无需重训练即可调控注意力分布的方案，有工程实用价值。跨模型（Qwen β=3, Llama β≥5）差异也提供了有价值的 negative signal。\n\n---\n\n## Weaknesses\n\n### Critical（必须修复，否则影响接收）\n\n**C1. GAR 指标的 construct validity 严重不足。** [R1-N1, R2-N1, 交叉一致]\n- GAR 与下游指令保持率的相关性 r=0.200, r²=0.04。全文从标题到结论以 GAR 改善为核心叙事，但 GAR 仅解释 4% 的下游方差。\n- N=54 paired samples 下 95% CI ≈ [0.05, 0.35]，置信区间过宽。\n- β=10 时 PPL 退化至 4.22，表明 GAR 极端提升可能有害，进一步质疑其作为优化目标的合理性。\n- 所有 variants PPL ≈ 2.78, AUC ≈ 0.98——GAR 的巨大差异未映射到任何下游性能差异。\n- **缺少任何标准多轮对话基准评测**（MT-Bench、AlpacaEval 等）。论文的全部评估建立在 GAR 这个未经外部验证的内部指标上。\n- **建议**：补充 MT-Bench 等下游评测（≥100 对话人工评估），或将 GAR 重新定位为 diagnostic probe 而非优化目标/成功指标。\n\n**C2. 单 seed 消融 + SS 跨 seed 方差 31%。** [R1-N2, R1-W5, R2 交叉一致]\n- Table 1 中 Base, PCGrad, Uniform Gate 三个重要条件**仅有 seed=42 单次结果**。ThreadGate 有 2 seeds，SS 有 2 seeds 但策略不同不可直接比较。\n- SS 两 seed AR GAR: 0.318 vs 0.418（相差 31%），说明 between-run variance 极高。Abstract 以确定性语气呈现这些结果（\"compresses the gap to 1.29×\"）构成 overclaim。\n- Appendix T 的 3-seed 验证仅覆盖 ThreadGate（CoV=9%），不能替代全条件多 seed 验证。\n- Table 6 Wilcoxon signed-rank test 以 conversation 为单元（N=50），衡量 within-run variability，无法支撑 between-run 对比结论。\n- **建议**：全部 5 条件 × 3 seeds 完整实验，报告 mean±std。当前单 seed 数据仅能作为 pilot study。\n\n**C3. Exposure bias 因果归因超出证据。** [R2-C3, R1-W3, 交叉一致]\n- 论文将 TF-AR gap 归因于 exposure bias，但未实验排除 KV cache drift 假说（§6 承认，§8 留给 future work）。\n- PCGrad 失败被用作 modus tollens 否定 gradient conflict 假说，但 PCGrad 的投影操作本身引入副作用（NTP magnitude 增长 7.5×-14.7×），失败可能反映投影副作用而非 gradient conflict 不存在。\n- Appendix L 的 gradient statistics 在 PCGrad 条件下获得，不构成独立验证。\n- 对一篇以 \"mechanistic/diagnostic analysis\" 自居的论文，留下核心因果链的最关键环节未验证是不可接受的。\n- **建议**：设计 TF→AR 切换实验区分 prefix-level exposure bias 和 cache-level drift；或大幅弱化因果声称。\n\n### Should-Fix（应修复，影响评分但不单独构成拒稿理由）\n\n**W1. SS+LoRA-only 关键消融缺失。** [R1-W1, R2 交叉一致]\n- TG AR GAR ≈ 0.047（相比 Base ~2.6× 改善），SS AR GAR ≈ 0.401（相比 TG ~8.5× 改善）。SS 是压缩 TF-AR gap 的主要贡献者。\n- 缺少 SS+LoRA-only（不加 ThreadGate）的消融。如果该配置效果相似，ThreadGate 作为架构贡献的价值将大幅降低。\n- §6 未直面 ThreadGate vs SS 的贡献归因问题。\n\n**W2. 单一数据集（UltraChat）。** [R1-W5, R2-W2, 交叉一致]\n- 所有实验仅在 UltraChat 上进行，无法评估 GAR decay 是否为 UltraChat 特异现象。\n- 缺少 ShareGPT、LMSYS-Chat-1M 等替代数据集验证。\n\n**W3. Llama 跨模型验证不完整。** [R1-W1, R2-M2, 交叉一致]\n- 仅 3/5 条件（Base, TG, TG+SS），缺 PCGrad 和 Uniform Gate。\n- Median vs mean 切换在 Qwen→Llama 间不一致，有 metric selection 之嫌。\n- §5.5 标题 \"Cross-Model Validation\" 过度概括，建议改为 \"Cross-Model Replication\"。\n\n**W4. 标题与副标题 overclaim。** [R2-N2, R1-W2, 交叉一致]\n- 标题暗示 gating 固有失败，但实际发现是 exposure bias 的通用问题（LoRA-only 无 gate 表现相同）。\n- \"Mechanistic Analysis\" 副标题与分析深度不匹配——宏观层面非 circuit-level。建议改为 \"Diagnostic Analysis\"。\n\n**W5. Li et al. split-softmax / Rhea 缺实验对比。** [R2-W7-new, R2-W2]\n- 论文声称 split-softmax \"cannot address exposure bias\" 但未实验验证。\n- 作为最直接竞争方法，至少需要理论论证或承认未验证。\n\n**W6. Appendix C instruction retention 多重比较未校正。** [R1-W4, R2 部分反驳]\n- 主实验已有 Holm-Bonferroni 校正（Appendix E p30），此关切对主实验不成立。\n- 但 Appendix C 18-category McNemar's test 未做 FDR/Bonferroni 校正。\n\n**W7. 写作冗余。** [R2-W4-new]\n- '20-33× gap' 至少出现 7 次，'0.064 to 0.727' 出现 4+ 次。\n\n### Minor\n\n**M1.** r_min 数值正文未报告，影响可复现性。[R1-M1]\n**M2.** GAR-D 全条件接近零（ThreadGate TF下仅0.02），说明干预仅在 τ-masked last token 成功，泛化性未讨论。[R1-W5]\n**M3.** Table 1 四舍五入与正文数字精度不一致（0.75pp vs 1pp）。[R2-W6]\n**M4.** LoRA rank=16 是否影响结论未讨论。[R2-Q4]\n**M5.** 无代码/数据发布承诺。[R1-M6, R2-M6]\n**M6.** Bib 格式：Raposo et al. 2024 应更新为 ICML 2024 @inproceedings；Gromov et al. 年份一致性。[R2-M3]\n\n---\n\n## Questions\n\n**Q1.** SS+LoRA-only（不加 ThreadGate）的 TF-AR gap 是多少？如果与 SS+ThreadGate 相似，ThreadGate 的独立贡献是什么？[R1, R2 一致]\n\n**Q2.** Table 1 中 Base, PCGrad, Uniform Gate 是否均为 seed=42？请明确标注。[R1]\n\n**Q3.** 如果 GAR 与下游任务的 r²=0.04，作者是否考虑 GAR 可能不是指令遵循的可靠代理指标？将 GAR 重新定位为 diagnostic probe 而非优化目标是否更准确？[R1, R2 一致]\n\n**Q4.** β-steering 最优 β 的 architecture dependence（Qwen β=3 vs Llama β≥5）意味着什么？该方法是否需要 per-model tuning？[R1, R2 一致]\n\n**Q5.** 其他数据集（ShareGPT, LMSYS-Chat-1M）上 GAR decay 是否一致？[R1, R2 一致]\n\n**Q6.** 是否尝试过更高 LoRA rank（32, 64）？rank=16 下的结论是否因 capacity saturation 被低估？[R2]\n\n---\n\n## Missing References\n\n1. **Zhang et al. 2024** — \"Tell Your Model Where to Attend\"：与 β-steering 思路相似的推理时注意力操控方法，应在 §2 讨论。[R2]\n2. **Rhea (arXiv:2512.06869)** — Role-aware Heuristic Episodic Attention：§2 已讨论但缺实验对比。[R1, R2 跨轮追踪]\n3. **Li et al. 2024** — Split-softmax：最直接竞争方法，需加强理论对比。[R2]\n\n---\n\n## External Review\n\n**状态**：已跳过（skipped at 2026-05-25T05:44:29）。未获得外部审稿数据。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成 (0 critical, 3 warning, 6 info)\n\n**Warning:**\n- Page 6: Figure 4（Scheduled sampling compression）尺寸偏小，柱状图条形窄、标签字号小\n- Page 8: Figure 6a（per-layer gate values）28 层数据压缩在单栏宽度内，个别柱体 <2px，建议改用折线图或全宽\n- Pages 5/7/8: 多个 bar chart 使用高饱和度配色（亮橙+亮蓝+亮绿），与用户规则\"配色饱和度对比别太高\"不符\n\n**Info:**\n- Page 1: 首页无 display item，Figure 1 在 Page 2\n- Page 2: Figure 1 caption ~7 行，偏密集\n- Page 7: Figure 5 仅两根柱子，信息密度低\n- Page 30: Appendix 整页纯文本（可接受）\n- Pages 25-26: Tables 19-22 列数多但字号可辨\n- Pages 16/18/19: Appendix 图表 axis label 约正文 60-65%\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Overall | 3.0 (Findings) | 3.5→3.0 (Findings) | **3.0 (Findings)** |\n| Soundness | 3/5 | 3/5 | 3/5 |\n| Novelty | 2/5 | 2.5/5 | 2/5 |\n| Reproducibility | 3/5 | 4/5 | 3/5 |\n\n### 综合评价\n\n**Overall Score: 3.0 — Findings**\n\n论文识别了一个重要且未被充分研究的问题（多轮对话辅助注意力损失在 AR 推理时的效能退化），五路消融设计系统性较好，SS 的实用发现有直接价值。\n\n然而，三个 Critical 问题共同构成了接收的主要障碍：\n\n1. **GAR construct validity**（r²=0.04）——全文核心叙事建立在一个仅解释 4% 下游方差的指标上，且无任何标准多轮对话基准评测。这不是精度问题，而是整个评估框架的根基问题。\n\n2. **统计不可靠**——多条件单 seed，SS 跨 seed 方差 31%，AR 评估 N=5。当前数据本质上是 pilot study 级别，不足以支撑论文的定量结论。\n\n3. **因果 overclaiming**——exposure bias 归因未排除 KV cache drift，PCGrad modus tollens 论证依赖过强假设。\"Mechanistic analysis\" 的定位与实际分析深度不匹配。\n\nR2 指出论文的**诊断框架和问题发现**本身有独立价值，即使方法贡献是增量的。如果 GAR 被重新定位为 diagnostic probe（而非优化目标），因果声称被大幅弱化，统计问题被修复（全条件 3-seed + N≥50 AR 评估），论文可达到 Findings 水准。当前状态距此仍有实质性 gap。\n\n### 修改优先级\n\n1. **[实验]** 全条件 3-seed × N≥50 AR 评估 + mean±std → 解决 C2\n2. **[实验]** SS+LoRA-only 消融 → 解决 W1\n3. **[评估]** MT-Bench 或等价下游评测 → 部分解决 C1\n4. **[写作]** GAR 重新定位为 diagnostic probe + 因果声称弱化 → 部分解决 C1, C3\n5. **[写作]** 标题/副标题调整 → 解决 W4\n6. **[实验]** 第二数据集验证 → 解决 W2\n\n---\n\n## Detailed Comments\n\n### 交叉回应分歧记录\n\n仅一项分歧，已在报告中体现：\n\n- **R1-W4（多重比较）**：R2 部分反驳——主实验已有 Holm-Bonferroni 校正（Appendix E p30），R1 关切对主实验不成立。但对 Appendix C 18-category McNemar's test 成立。报告中记录为 W6（Should-Fix，限定于 Appendix C）。\n\n### 评分调整说明\n\nR2 初始评分 3.5（Borderline Conference），交叉回应后表示\"如果 GAR 的 construct validity 问题（r²=0.04）得不到解决，愿意将评分下调至 3.0\"。鉴于 C1 目前未解决，R2 有效评分调整为 3.0。两位 Reviewer 共识为 3.0（Findings）。\n\n### 跨轮次追踪\n\n本轮为 Round 4（fresh re-review）。Issue tracker 中有 5 个 Critical 级别未解决问题（R1-N2, R1-W5, R2-C3, R4-N1, R2-N3），12 个 Warning 级别未解决问题，6 个 Info 级别未解决问题。详见 `artifacts/review_issues.yaml`。\n",
    "project": "turn_residual_gating",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-25T05:56:06.584899+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4327
}
```

</details>

---


### Assistant

_source line 382 · 2026-05-25T05:56:14.888713+00:00_

Round 4 审稿报告已投递。

**最终评分：3.0（Findings）**，两位 Reviewer 高度共识。

三个 Critical 问题是主会议接收的核心障碍：
1. GAR construct validity（r²=0.04，无下游基准评测）
2. 统计不可靠（多条件单 seed，SS 跨 seed 方差 31%）
3. Exposure bias 因果归因超出证据

修改优先级：全条件 3-seed 实验 > SS+LoRA-only 消融 > MT-Bench 下游评测 > GAR 重定位 + 因果声称弱化 > 标题调整。Issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 33

## Round 33

2 recorded events


### User

_source line 383 · 2026-05-25T05:56:16.163005+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- 对 R1 的 14 个要点中 **13 个标注 [AGREE]**，1 个 **[REBUT]**（W4 多重比较——主要实验已有 Holm-Bonferroni 校正，但 instruction retention 分析确实缺少）
- 两位 Reviewer 在核心问题上高度一致：GAR 下游预测力弱（r²=0.04）、因果声明过强、单一数据集、下游评估不足
- R1 额外贡献了 single-seed 消融设计和 SS vs ThreadGate 归因不清两个重要发现
- 如果 GAR construct validity 问题得不到解决，我愿意将评分从 3.5 下调至 3.0

---

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: "Collapse" overclaiming——标题叙事缺乏下游证据**

完全同意，这与我自己的 N1（GAR-compliance 弱相关性）指向同一核心问题。补充证据：

1. **Appendix C（page 12）明确报告 GAR-compliance 相关系数仅 r=0.200（p=0.007）**，r²=0.04，即 GAR 仅解释 4% 的指令遵循率方差。这直接支持 R2 的判断——GAR 衰减不等于生成质量"崩溃"。
2. **McNemar's test p=0.077**（page 12），仅 marginally significant，即使在最有利的类别（content constraints +23.8pp），样本量也仅 N=54（18 types × 3 conversations）。
3. 论文的 MMLU 评测（Appendix R）确实只证明"无害"——所有变体在 MMLU 上差异 ≤0.8pp，但 MMLU 是单轮知识测试，与多轮对话质量无关。

标题中 "From Collapse to Recovery" 暗示了一个严重的实际问题及其解决，但论文实际展示的是**内部指标（GAR）的衰减与恢复**，缺乏充分的下游证据证明这一衰减对用户可感知的对话质量有实际影响。R2 的建议（增加 MT-Bench 评测或弱化 "collapse" 语言）是恰当的。

---

**[AGREE] R2-N2: 因果声明强度超过证据——"causal exclusion chain" 有逻辑缺口**

同意，我在自己的 W3 中也对 PCGrad modus tollens 提出了类似质疑。R2 的分解比我更系统，逐环分析如下：

1. **§5.1 门控值相关性**：R2 正确指出这是 correlational evidence。论文展示了 "27/28 layers, gate values are lower at turn 1 than turn 21"（page 7），但 gate value 与 turn index 的 correlation 不等于 gate → GAR 的因果关系。
2. **§5.2 PCGrad 排除**：我在 W3 中已指出，PCGrad 不仅消除梯度冲突，还改变优化景观（投影到法向面上）。R2 进一步指出"排除一个替代假设 ≠ 证明目标假设"——逻辑上完全正确。即使梯度冲突不是原因，也不能直接推出 exposure bias 就是原因。
3. **§5.4 SS 有效性**：R2 观察到 SS 将 gap 从 7.8× 压缩到 1.3× 但**未消除**——这是关键。如果 exposure bias 是唯一原因，理论上 SS 应该能将 gap 压缩到 ~1.0×。残留的 1.3× gap 说明存在其他因素（如表示漂移、累积误差），但论文未充分讨论。

R2 建议将 "causal exclusion" 改为 "diagnostic analysis" 是合理的。这不会削弱论文的分析贡献，但能避免逻辑 overstatement。

---

### Should-Fix 问题

**[AGREE] R2-W1: GAR construct validity 不充分**

与我的 N1 一致。论文 Appendix C 提供了唯一的 construct validity 证据（r=0.200），这远不足以支撑 GAR 作为核心优化目标的合理性。论文缺少 GAR 与标准生成质量指标（human preference, coherence, fluency）的系统 correlation analysis。如果 GAR 是一个 weak proxy，则全文围绕 GAR 改善构建的叙事根基不稳。

---

**[AGREE] R2-W2: 单一数据集 + 有限模型规模**

与我的 W5 一致。补充：论文的 cross-scale 验证（Qwen-2.5-1.5B, Appendix Y, page 28）一定程度上扩展了模型覆盖，但 1.5B 与 7B 属同一架构家族，不能替代跨架构的广泛验证。跨模型验证（Llama-3.1-8B）更有价值，但仍是同一数据集（UltraChat）上的同一实验流程。

---

**[AGREE] R2-W3: 缺失近期相关工作**

我无法独立验证 R2 引用的具体 arXiv papers（Wan et al. 2026, arXiv:2602.03664; arXiv:2603.04783）的存在性和相关性。但如果 "Conversational Inertia" 确实研究了多轮对话中注意力/信息衰减的同类现象，那么它应该被讨论。作者应在 camera-ready 中验证并引用这些工作（如果确实相关）。

---

**[AGREE] R2-W4: β-steering 实际可部署性存疑**

与我的 minor point 一致，但我认同 R2 将其升级为 should-fix 的判断。具体问题：
1. **Goal token 识别**：推理时需要知道哪些 token 是 "goal tokens"（system prompt 中的任务指令），这在实际部署中并非总是可用的——例如在 streaming 场景下或当 system prompt 被加密时。
2. **β 超参搜索**：Qwen 需 β=3（page 6, §4.3 "phase transition at β≥3"），Llama 需 β≥5（page 8），且 β 过大导致 PPL 恶化（"PPL remains below 1.8 while GAR reaches 0.727"）。每个新模型需要单独搜索。
3. 论文在 Discussion（page 8）中将 β-steering 主要定位为 "inference-time recovery"，但 Abstract 的 "Existing remedies operate at inference time" 表述容易误导读者以为这是一个 production-ready 方案。

---

**[REBUT] R2-W5: 方法技术新颖性有限**

部分反驳。R2 将 ThreadGate 简化为 "ReZero + turn embedding"、SS 归结为 "Bengio et al. 2015"、β-steering 归结为 "simple logit bias"，我认为这低估了论文的贡献定位：

1. **论文的核心贡献是诊断性/分析性的，不是方法论的**。Abstract 的四个 contributions 中，前三个是诊断发现（exposure bias 刻画、PCGrad 排除、β-steering 机制验证），只有第四个（SS 应用）是方法论贡献。对于诊断性论文，insight 新颖性比 method 新颖性更关键。
2. **"首次将 exposure bias 框架应用于多轮辅助注意力目标"** 这一洞察本身是新颖的。Bengio et al. 2015 的 SS 是为 RNN sequence models 设计的，论文首次验证了它在 transformer 多轮注意力训练中的有效性（Section 4.4），这不是简单的照搬。
3. **系统性排除方法论**：五方对比 + PCGrad 因果排除 + β-steering 机制验证 + SS 分布桥接，构成了完整的诊断链条，整体设计有新颖性。

但 R2 的批评有合理之处：**如果只看 method 部分（Section 3），确实没有根本性的技术突破**。ThreadGate 的具体架构（投影+MLP+sigmoid gate）在 gating 文献中是标准设计。论文的价值在于 **问题的发现和系统的验证**，而非提出新算法。建议作者在 Introduction 中更明确地定位论文为 "diagnostic + mitigation" 而非 "new method"。

---

### Questions 回应

**[AGREE] R2-Q1**: GAR-downstream 相关性有量化数据——Appendix C（page 12）报告 r=0.200（p=0.007）。这是全文唯一的 construct validity 证据，且相关性弱。我在 N1 中已详细讨论。

**[AGREE] R2-Q2**: SS 残留 gap（1.3×）的归因确实是论文未充分讨论的问题。从论文现有分析推测，可能的因素包括：(1) SS 的线性 schedule（ratio 0→0.3）可能不够激进；(2) model-generated tokens 来自训练早期，与真实 AR 分布仍有差距；(3) 累积漂移（Appendix O 的 length-dependent compounding 分析，page 21，gap 与 turn 数近似线性增长）超出 SS 的校正能力。但这些都是推测——论文应提供实验证据。

**[AGREE] R2-Q3**: 4 维 turn embedding（2-dim t_s + 2-dim t_r）在 >10 turns 场景下的表示能力确实值得关注。论文主要在 5-turn 对话上评测（Table 14, page 20），extended 评测仅到 10 turns（N=5, Appendix D）。对于更长对话（如 20+ turns，实际部署场景），4-dim embedding 可能不足以捕捉 fine-grained 的 turn-specific modulation。但当前评测范围内（5-10 turns），这不是紧迫问题。

**[AGREE] R2-Q4**: β 的架构依赖性（Qwen β=3, Llama β≥5）限制了方法的开箱即用性。我在 minor point 和 Q4 中也提出了同样的问题。论文未提供确定最优 β 的系统方法——目前是 grid search（Figure 3, page 5），但未讨论如何在新模型上高效搜索。

**[AGREE] R2-Q5**: 我无法独立验证 Wan et al. (2026) "Conversational Inertia" 的存在。如果该论文确实描述了类似的多轮注意力衰减现象，则 R2 的关切成立——本文需要讨论两者的异同。作者应在修改中验证并回应。

---

### 总结

R2 的审稿意见与我的评估高度一致，尤其在核心问题上：
- **GAR 下游验证不足**（R2-N1 ≈ R1-N1）
- **因果声明过强**（R2-N2 ≈ R1-W3）
- **单一数据集**（R2-W2 ≈ R1-W5）
- **β-steering 部署性**（R2-W4 ≈ R1-minor）

唯一分歧在 **R2-W5（技术新颖性）**：我认为论文的诊断贡献足以构成 novelty，但同意 method 部分本身缺乏技术突破。

两位 Reviewer 的 Overall 评分（R1: 3.0, R2: 3.5）差异可能反映了对"诊断性贡献 vs 方法论贡献"的权重不同。如果以 diagnostic paper 标准评价，3.5 合理；如果以 method paper 标准评价，3.0 更准确。


---

[Reviewer 1 审稿结果]:
交叉回应已提交。

要点：对 R2 的 7 个 Must-Fix/Should-Fix 中的 6 个标注了 [AGREE]（N1 下游验证不足、N2 因果声明过强、W1-W4），唯一 [REBUT] 的是 W5（技术新颖性有限）——我认为论文的核心贡献是诊断性的而非方法论的，insight novelty 足以构成贡献，但同意 method 部分本身无技术突破。R2 的 5 个 Questions 全部 [AGREE]，其中 Q1 我补充了 Appendix C 的 r=0.200 量化数据。两位 Reviewer 的核心关切高度一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 384 · 2026-05-25T05:56:25.319018+00:00_

审稿报告已在上一轮提交完成（Overall Score: 3.0 — Findings）。R1 的交叉回应进一步确认了高度收敛——R1 对 R2 的 6/7 [AGREE]，唯一 [REBUT]（W5 技术新颖性）与 R2 对 R1 的唯一 [REBUT]（W4 多重比较）形成互补，且双方 rebut 都附带了部分认同。

报告已投递至 Research Director，无需额外操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 34

## Round 34

42 recorded events


### User

_source line 385 · 2026-05-25T08:16:00.918655+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: turn_residual_gating
- 论文路径: projects/turn_residual_gating/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR August 2026
- 截止日期: 2026-08-03
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-25T08:16:07.082017+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-25T08:16:07.183493+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-25T08:16:12.355038+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,read_project_file,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,read_project_file,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-25T08:16:12.505987+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-25T08:16:16.224610+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-25T08:16:16.225135+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-25T08:16:19.391666+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-25T08:16:19.844078+00:00_

{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (58 个)\n\n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v9_pcgrad**: DONE (success) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: DONE (failed) — \n- **analysis_attention_heatmap**: DONE (success) — \n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| phase1a_multiseed_qwen | Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds. | — | — | — |\n\n## 待处理\n- phase2_tf_ar_switching: TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.（排队等待 GPU）\n- phase1a_multiseed_8runs（准备中）\n- phase1b_llama_complement: Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.（准备中）\n- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack
…[truncated 1211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-25T08:16:19.996922+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-25T08:16:19.997362+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-25T08:16:25.675234+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions",
  "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions",
    "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 397 · 2026-05-25T08:16:27.483001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 398 · 2026-05-25T08:16:27.533612+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	\usepackage{placeins}
18	\usepackage{alphalph}
19	
20	\graphicspath{{../figures/paper/}{../artifacts/}}
21	
22	\title{Exposure Bias Destroys Auxiliary Attention Losses in Multi-Turn Dialogue}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{sections/abstract}
30	\input{sections/introduction}
31	\input{sections/related_work}
32	\input{sections/method}
33	\input{sections/experiments}
34	\input{sections/analysis}
35	\input{sections/discussion}
36	\input{sections/conclusion}
37	\input{sections/limitations}
38	
39	\FloatBarrier
40	\bibliography{references}
41	
42	\appendix
43	\renewcommand{\thesection}{\AlphAlph{\value{section}}}
44	\input{sections/appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 399 · 2026-05-25T08:16:27.684599+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
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

_source line 400 · 2026-05-25T08:16:27.785351+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-25T08:16:33.658696+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"}]

Based on the search results, here's information about EMNLP 2026 ARR submission guidelines:

## Key Policy Information

Given that the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026—ARR submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to
…[truncated 651 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 7983
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-25T08:16:40.740447+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR August 2026 submission deadline page limit format requirements",
  "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR August 2026 submission deadline page limit format requirements",
    "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 403 · 2026-05-25T08:16:41.343729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-25T08:16:41.344652+00:00_

1	# Review Issues Tracker — turn_residual_gating
2	# Round 1 (2026-05-19, dream_20260519T145320)
3	# Round 2 (2026-05-22, fresh re-review of revised paper)
4	# Round 3 (2026-05-22, fresh re-review)
5	# Round 4 (2026-05-25, fresh re-review — current round)
6	# Cross-response phase completed: R1↔R2 high convergence
7	
8	# ============================================================
9	# Issues from Round 1 — status updates through Round 4
10	# ============================================================
11	
12	- id: "R1-N1"
13	  summary: "所有引用渲染为 '?'——bibliography 编译失败"
14	  category: format
15	  severity: info
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  mentions:
20	    - round: 1
21	      reviewers: [1, 2]
22	      note: "Dream paper artifact。"
23	    - round: 2
24	      reviewers: []
25	      note: "视觉审查确认无 [?] 未解析引用。已修复。"
26	    - round: 3
27	      reviewers: []
28	      note: "Round 3 视觉审查确认无未解析引用。维持 resolved。"
29	    - round: 4
30	      reviewers: []
31	      note: "Round 4 视觉审查确认无未解析引用。维持 resolved。"
32	  action_items:
33	    - round: 1
34	      action: "Paper Agent 确保 bibtex 编译正确"
35	      assigned_to: paper_agent
36	      status: done
37	  resolution: "Round 2 视觉审查确认已修复。"
38	  resolution_round: 2
39	
40	- id: "R1-N2"
41	  summary: "单种子支撑结论——统计功效不足 + AR 评估 N=5 过小"
42	  category: experiment
43	  severity: critical
44	  status: open
45	  first_raised_round: 1
46	  last_seen_round: 4
47	  mentions:
48	    - round: 1
49	      reviewers: [1, 2]
50	      note: "Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。"
51	    - round: 2
52	      reviewers: [1, 2]
53	      note: "ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。"
54	    - round: 3
55	      reviewers: [1, 2]
56	      note: "AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。"
57	    - round: 4
58	      reviewers: [1, 2]
59	      note: "两位 Reviewer 独立列为 Critical Must-Fix。交叉回应 R2 完全同意 R1 论证。R2 补充：Appendix T 3-seed CoV=9% 仅覆盖 TG，Table 1 Base/PCGrad
…[truncated 24833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-25T08:16:41.746526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf"
  }
}
```

</details>

---


### Tool result

_source line 406 · 2026-05-25T08:16:41.797133+00:00_

This PDF has 33 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-25T08:16:46.365929+00:00_

Web search results for query: "ARR August 2026 submission deadline page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here are the key details for ARR submissions:

## Page Limit Requirements

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

## Format Requirements

The submission must adhere to the formatting in the submission templates, which is available as an Overleaf template.

## August 2026 Submission Deadline

The search results don't contain specific information about an August 2026 submission deadline for ARR. The results indicate that the new schedule started in May 2025 cycle with 10-week cycles, meaning there are generally 5 submission deadlines per year rather than 6. However, the exact dates for the August 2026 cycle are not detailed in these search results.

For the most current and specific information about the August 2026 ARR submission dead
…[truncated 268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 5625
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-25T08:16:52.288447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-25T08:16:53.746453+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf (1015.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 1458
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-25T08:16:53.755506+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 August cycle submission deadline dates",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 August cycle submission deadline dates",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-25T08:16:54.257609+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "turn_residual_gating",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-25T08:17:04.789216+00:00_

Web search results for query: "ACL Rolling Review 2026 August cycle submission deadline dates"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Dates – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/some-important-dates/"},{"title":"ARR Dashboard","url":"http://stats.aclrollingreview.org/"},{"title":"Submission dates and process for 2024 Conferences – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submission-dates-for-2024/"}]

Based on the search results, I found information about ACL Rolling Review's schedule and deadline structure:

ACL switched to 10-week review cycles starting in May 2025, and the submission deadline is always the 15th of the month.

However, the search results do
…[truncated 838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 11033
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-25T08:17:04.789890+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/decisions.yaml\", \"content\": \"_next_id: 56\\ndecisions:\\n- id: D001\\n  date: 2026-05-18 04:48 UTC\\n  summary: MVP Phase 2 中间场景处置：条件1通过+条件2失败 = partial pass\\n  rationale: 如果 ThreadGate GAR recovery 显著优于 Uniform Gate（验证 Cesaro 理论预测）但下游任务无改善，说明核心机制成立但\\n    GAR explanation ceiling 有限。处置：视为 partial pass 进入 research，但 framing 必须从\\\"提升多轮性能的方法\\\"转向\\\"理论验证+首个\\n    principled 干预框架\\\"，实用价值作为 secondary contribution。如果连条件1都不满足则仍为 kill。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-18 04:59 UTC\\n  summary: MVP 使用残差缩放公式 x + g·f(x) 代替 IDEA_BRIEF 插值公式\\n  rationale: IDEA_BRIEF 的插值公式 g·x + (1-g)·f(x) 无法通过任何 g 值恢复正常模型行为 x+f(x)，导致初始化困难。改用\\n    x + g·f(x)（g=1 为正常，g→0 为跳过层），保证模型可从正常状态开始学习。核心对比（turn-conditional vs uniform）不受公式影响——两种公式下\\n    uniform gating 都无法选择性修改特定位置的 GAR。理论对齐留到 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-18 06:05 UTC\\n  summary: Phase 2 增加归一化 GAR 作为诊断指标，pass 标准仍基于 raw GAR\\n  rationale: Reviewer 发现 Phase 1 的 70.8% raw GAR 衰减大部分由序列增长稀释驱动，归一化后结构性下降仅 ~21%。normalized\\n    GAR 能区分\\\"稀释补偿\\\"vs\\\"结构性修复\\\"，直接影响论文 Cesaro 理论 story 的可信度。但 raw GAR 衰减是功能上真实有害的，方法即使只补偿稀释也有实用价值，因此\\n    MVP pass 标准不变。\\n  related_experiments:\\n  - exp_id: phase1_gar_diag\\n    role: evidence\\n    result: GAR衰减70.8%但归一化后仅~21%\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-18 13:37 UTC\\n  summary: Kill v3, run v3b (λ=10, gate_lr=10x, init_bias=0.0) as GAR-driven gating的最终验证。500步内gate无分化则GAR→gate梯度路径判定失败。\\n  rationale: v1/v2/v3 三个版本全部无法驱动gate学习选择性干预：v1 epsilon过高(L_GAR=0)，v2 hinge退化平衡点，v3\\n    maximize模式梯度太弱(gate冻结在0.876±0.001)。根因一致：GAR→attention→hidden→gate间接梯度路径太弱。v3b同时最大化三个信号强度维度(λ=10,\\n    gate_lr=10x, init_bias=0.0给sigmoid最大梯度区间)，如果仍然失败则排除\\\"信号不够强\\\"的解释，确认是梯度路径结构性问题。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v1\\n    role: evidence\\n    result: L_G
…[truncated 1476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10532
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-25T08:17:22.460589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
  "pages": "11-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
    "pages": "11-20"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-25T08:17:23.367780+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf (1015.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-25T08:17:23.431642+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "output_mode": "content",
  "glob": "*.yaml",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
    "output_mode": "content",
    "glob": "*.yaml",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-25T08:17:23.482308+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-25T08:17:30.715076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
  "pages": "21-33"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
    "pages": "21-33"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-25T08:17:31.519485+00:00_

PDF pages extracted: 13 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf (1015.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-25T08:18:02.855598+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "turn_residual_gating",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "turn_residual_gating",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-25T08:18:27.954923+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 25099
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-25T08:18:28.206331+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "turn_residual_gating",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性** 审查。\n\n## 论文信息\n- **标题**: Exposure Bias Destroys Auxiliary Attention Losses in Multi-Turn Dialogue\n- **论文路径**: projects/turn_residual_gating/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf\n- **目标 venue**: EMNLP 2026（通过 ARR August 2026 投稿）\n- **截止日期**: 2026-08-03\n\n## Venue 格式要求\n- **页数限制**: Long paper 正文严格 8 页，参考文献不限页数\n- **模板**: ACL 模板（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind（Anonymous ACL submission）\n- **附录**: 允许，但附录参与审稿\n- **Limitations**: 必须有，不计入 8 页限制\n- **评分标准**: ARR Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 你的审查重点\n\n### 1. 实验设计与统计有效性\n- Table 1 的五路对比实验设计是否合理？各条件之间是否真正 isolate 单一因素？\n- 统计检验（Wilcoxon, bootstrap CI, McNemar）的选择和使用是否恰当？\n- AR 评估的样本量（N=50 held-out, N=5 长对话）是否足够支撑结论？\n- 多种子实验（SS 3 seeds, TG 2 seeds）覆盖是否充分？其余条件单种子是否削弱结论？\n- 效应量（r=0.802, r=0.454 等）的报告和解读是否准确？\n\n### 2. 因果推理链\n- §3.4 的因果排除链（turn conditioning → gating → gradient conflict → exposure bias）逻辑是否严密？\n- PCGrad \"modus tollens\" 论证是否成立？是否有替代解释（如 magnitude imbalance）未被排除？\n- β-steering 恢复 GAR 是否真正确认 attention misallocation 而非其他机制？是否存在循环论证风险？\n- Exposure bias 归因是否过强？KV cache drift 等替代假说是否被充分讨论？\n\n### 3. 指标有效性\n- GAR-ours vs GAR-Dongre 的区别和选择是否有充分理由？\n- GAR 与下游任务（instruction retention）的相关性 r=0.200 很弱，这对论文核心 claim 意味什么？\n- GAR-D 在所有条件下接近零（Table 1），而 GAR-ours 有显著差异——这说明什么？\n\n### 4. 可复现性\n- 超参数报告是否完整（Table 2, Appendix A）？\n- 代码/数据是否承诺发布？\n- 训练细节（GPU 型号、训练时间等）是否准确？\n\n### 5. 格式合规性\n- 正文是否严格 ≤8 页？\n- Limitations section 是否存在且内容充分？\n- 匿名性是否保持？（检查是否有去匿名化信息）\n\n请按 ARR 标准出具完整审稿意见，结构为：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "turn_residual_gating",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性** 审查。\n\n## 论文信息\n- **标题**: Exposure Bias Destroys Auxiliary Attention Losses in Multi-Turn Dialogue\n- **论文路径**: projects/turn_residual_gating/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf\n- **目标 venue**: EMNLP 2026（通过 ARR August 2026 投稿）\n- **截止日期**: 2026-08-03\n\n## Venue 格式要求\n- **页数限制**: Long paper 正文严格 8 页，参考文献不限页数\n- **模板**: ACL 模板（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind（Anonymous ACL submission）\n- **附录**: 允许，但附录参与审稿\n- **Limitations**: 必须有，不计入 8 页限制\n- **评分标准**: ARR Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 你的审查重点\n\n### 1. 实验设计与统计有效性\n- Table 1 的五路对比实验设计是否合理？各条件之间是否真正 isolate 单一因素？\n- 统计检验（Wilcoxon, bootstrap CI, McNemar）的选择和使用是否恰当？\n- AR 评估的样本量（N=50 held-out, N=5 长对话）是否足够支撑结论？\n- 多种子实验（SS 3 seeds, TG 2 seeds）覆盖是否充分？其余条件单种子是否削弱结论？\n- 效应量（r=0.802, r=0.454 等）的报告和解读是否准确？\n\n### 2. 因果推理链\n- §3.4 的因果排除链（turn conditioning → gating → gradient conflict → exposure bias）逻辑是否严密？\n- PCGrad \"modus tollens\" 论证是否成立？是否有替代解释（如 magnitude imbalance）未被排除？\n- β-steering 恢复 GAR 是否真正确认 attention misallocation 而非其他机制？是否存在循环论证风险？\n- Exposure bias 归因是否过强？KV cache drift 等替代假说是否被充分讨论？\n\n### 3. 指标有效性\n- GAR-ours vs GAR-Dongre 的区别和选择是否有充分理由？\n- GAR 与下游任务（instruction retention）的相关性 r=0.200 很弱，这对论文核心 claim 意味什么？\n- GAR-D 在所有条件下接近零（Table 1），而 GAR-ours 有显著差异——这说明什么？\n\n### 4. 可复现性\n- 超参数报告是否完整（Table 2, Appendix A）？\n- 代码/数据是否承诺发布？\n- 训练细节（GPU 型号、训练时间等）是否准确？\n\n### 5. 格式合规性\n- 正文是否严格 ≤8 页？\n- Limitations section 是否存在且内容充分？\n- 匿名性是否保持？（检查是否有去匿名化信息）\n\n请按 ARR 标准出具完整审稿意见，结构为：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-25T08:18:51.876354+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23670
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-25T08:18:52.278204+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "turn_residual_gating",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## 论文信息\n- **标题**: Exposure Bias Destroys Auxiliary Attention Losses in Multi-Turn Dialogue\n- **论文路径**: projects/turn_residual_gating/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf\n- **目标 venue**: EMNLP 2026（通过 ARR August 2026 投稿）\n- **截止日期**: 2026-08-03\n\n## Venue 格式要求\n- **页数限制**: Long paper 正文严格 8 页，参考文献不限页数\n- **模板**: ACL 模板（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind（Anonymous ACL submission）\n- **附录**: 允许，但附录参与审稿\n- **Limitations**: 必须有，不计入 8 页限制\n- **评分标准**: ARR Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 你的审查重点\n\n### 1. 新颖性与贡献评估\n- 论文声称的四项贡献（exposure bias 表征、诊断 testbed、β-steering 确认、scheduled sampling 迁移）是否确实新颖？\n- 与 Dongre et al. (2026) 的关系：是增量贡献还是独立贡献？论文是否正确定位了自己与 Dongre 的区别？\n- 与 Li et al. (2024) split-softmax 的关系：是否充分讨论？缺少实验对比是否削弱贡献？\n- 与 Hong et al. (Rhea, arXiv:2512.06869) 的关系是否被恰当讨论？\n- \"first transfer of time-scheduled sampling to auxiliary attention objectives in multi-turn transformers\" 这一声称是否过强？\n\n### 2. Related Work 覆盖度\n- Multi-turn dialogue 文献覆盖是否充分？\n- Exposure bias 文献（RNN → Transformer）的覆盖是否完整？\n- Gating/attention manipulation 文献是否遗漏重要工作？\n- 是否有近期（2025-2026）相关工作被遗漏？特别注意检查：\n  - Zhang et al. 2024 \"Tell Your Model Where to Attend\"（推理时注意力操控）\n  - 其他 multi-turn attention 相关工作\n\n### 3. Framing 与声称强度\n- 标题 \"Exposure Bias Destroys Auxiliary Attention Losses\" 是否过度声称？\"Destroys\" 是否准确反映实验发现？\n- Abstract 是否准确概括了论文发现？是否有 overclaim？字数是否 ≤200 words？\n- Contribution 列表中是否有泛化声称超出实验证据的范围？\n- \"causal exclusion chain\" 的措辞是否恰当？实验设计是否真正支持因果声称？\n- GAR 作为 \"diagnostic probe\" 的定位是否一致且令人信服？\n\n### 4. 写作质量\n- 论文结构是否清晰、逻辑流畅？\n- 关键数字（如 \"8-17× gap\"）是否在多章节过度重复？\n- Figure/Table caption 是否准确？是否有 overclaim？\n- 行文是否有 AI 写作痕迹（过度使用 \"crucially\", \"notably\", \"importantly\" 等）？\n- Discussion (§6) 是否平衡讨论了 limitations 和 alternative explanations？\n\n### 5. 跨模型泛化\n- Llama 实验仅覆盖 3/5 条件（Base, TG, LoRA-only），缺 PCGrad 和 UG——这对 \"cross-architecture generalization\" 声称意味什么？\n- Llama 使用 median 而非 mean 报告——是否有 metric selection 之嫌？\n- §5.5 标题 \"Cross-Model Replication\" vs \"Cross-Model Generalization\"——哪个更准确？\n\n### 6. 引用格式与准确性\n- Bib 格式是否一致？（作者列表、venue 名称、年份）\n- Dongre et al. GAR 的全称是否正确？（\"Goal Accessibility Ratio\" vs \"Goal Attention Ratio\"）\n- 所有引用是否真实存在？是否有错配引用？\n\n请按 ARR 标准出具完整审稿意见，结构为：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "turn_residual_gating",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## 论文信息\n- **标题**: Exposure Bias Destroys Auxiliary Attention Losses in Multi-Turn Dialogue\n- **论文路径**: projects/turn_residual_gating/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf\n- **目标 venue**: EMNLP 2026（通过 ARR August 2026 投稿）\n- **截止日期**: 2026-08-03\n\n## Venue 格式要求\n- **页数限制**: Long paper 正文严格 8 页，参考文献不限页数\n- **模板**: ACL 模板（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind（Anonymous ACL submission）\n- **附录**: 允许，但附录参与审稿\n- **Limitations**: 必须有，不计入 8 页限制\n- **评分标准**: ARR Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 你的审查重点\n\n### 1. 新颖性与贡献评估\n- 论文声称的四项贡献（exposure bias 表征、诊断 testbed、β-steering 确认、scheduled sampling 迁移）是否确实新颖？\n- 与 Dongre et al. (2026) 的关系：是增量贡献还是独立贡献？论文是否正确定位了自己与 Dongre 的区别？\n- 与 Li et al. (2024) split-softmax 的关系：是否充分讨论？缺少实验对比是否削弱贡献？\n- 与 Hong et al. (Rhea, arXiv:2512.06869) 的关系是否被恰当讨论？\n- \"first transfer of time-scheduled sampling to auxiliary attention objectives in multi-turn transformers\" 这一声称是否过强？\n\n### 2. Related Work 覆盖度\n- Multi-turn dialogue 文献覆盖是否充分？\n- Exposure bias 文献（RNN → Transformer）的覆盖是否完整？\n- Gating/attention manipulation 文献是否遗漏重要工作？\n- 是否有近期（2025-2026）相关工作被遗漏？特别注意检查：\n  - Zhang et al. 2024 \"Tell Your Model Where to Attend\"（推理时注意力操控）\n  - 其他 multi-turn attention 相关工作\n\n### 3. Framing 与声称强度\n- 标题 \"Exposure Bias Destroys Auxiliary Attention Losses\" 是否过度声称？\"Destroys\" 是否准确反映实验发现？\n- Abstract 是否准确概括了论文发现？是否有 overclaim？字数是否 ≤200 words？\n- Contribution 列表中是否有泛化声称超出实验证据的范围？\n- \"causal exclusion chain\" 的措辞是否恰当？实验设计是否真正支持因果声称？\n- GAR 作为 \"diagnostic probe\" 的定位是否一致且令人信服？\n\n### 4. 写作质量\n- 论文结构是否清晰、逻辑流畅？\n- 关键数字（如 \"8-17× gap\"）是否在多章节过度重复？\n- Figure/Table caption 是否准确？是否有 overclaim？\n- 行文是否有 AI 写作痕迹（过度使用 \"crucially\", \"notably\", \"importantly\" 等）？\n- Discussion (§6) 是否平衡讨论了 limitations 和 alternative explanations？\n\n### 5. 跨模型泛化\n- Llama 实验仅覆盖 3/5 条件（Base, TG, LoRA-only），缺 PCGrad 和 UG——这对 \"cross-architecture generalization\" 声称意味什么？\n- Llama 使用 median 而非 mean 报告——是否有 metric selection 之嫌？\n- §5.5 标题 \"Cross-Model Replication\" vs \"Cross-Model Generalization\"——哪个更准确？\n\n### 6. 引用格式与准确性\n- Bib 格式是否一致？（作者列表、venue 名称、年份）\n- Dongre et al. GAR 的全称是否正确？（\"Goal Accessibility Ratio\" vs \"Goal Attention Ratio\"）\n- 所有引用是否真实存在？是否有错配引用？\n\n请按 ARR 标准出具完整审稿意见，结构为：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-25T08:18:54.141951+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1863
}
```

</details>

---


### Assistant

_source line 426 · 2026-05-25T08:19:01.626503+00:00_

Round 5 审稿圆桌已启动：

- **视觉审查 Agent**：已派发，与 Reviewer 并行运行
- **Reviewer 1**（方法严谨性 + 实验有效性）：已分配，重点审查因果推理链、统计检验、GAR 指标有效性、多种子覆盖
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：已分配，重点审查贡献新颖性、Related Work 覆盖、Framing 声称强度、跨模型泛化

等待两位 Reviewer 返回独立初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 35

## Round 35

2 recorded events


### User

_source line 427 · 2026-05-25T08:26:17.300798+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性 + 实验有效性）

### 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**Confidence**: 4 / 5（Quite sure — 完整阅读全部 33 页含附录）

**一句话总结**: 五路受控对比设计精巧、负面结果报告诚实，但因果排除链不完整（未测试 KV cache drift 和 magnitude imbalance），GAR 与下游任务相关性极弱（r=0.200, r²=0.04）削弱了实际意义。

### 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 五路对比+统计检验规范（Wilcoxon+bootstrap+Bonferroni），但因果链有缺口，大部分条件单种子存在伪重复 |
| Excitement | 3.0/5 | 负面结果有警示价值，但影响范围窄（仅 GAR 族+UltraChat），GAR 弱相关下游 |
| Reproducibility | 4.0/5 | 匿名代码仓库+完整超参数+详细训练信息 |

---

### Must-Fix 问题

**N1** [critical] GAR 与下游任务相关性极弱（r=0.200, r²=0.04），削弱论文实际意义
- 位置：§6, §3.1
- GAR 仅解释 4% 的 instruction retention 方差。β-steering 下游改善 +11.1pp 未达显著（p=0.077, Table 4）。若 GAR 崩溃不影响实际任务，"Exposure Bias Destroys" 的标题暗示的实际危害存疑。
- 建议：扩大下游评估（MT-Bench-101 等），或明确定位为纯方法论贡献。

**N2** [critical] 因果排除链不完整——exposure bias 归因过强
- 位置：§5, §6, Title
- 仅排除 turn conditioning 和 gradient direction conflict。KV cache drift（§6 自己承认未测试）和 magnitude imbalance（NTP 主导 7.5–14.7×, §6 承认 PCGrad 不解决幅度问题）均未实验验证。标题 "Destroys" 过于确定。
- 建议：弱化因果措辞为 "consistent with"；增加 GradNorm 实验或 KV cache drift 区分实验。

**N3** [critical] 大部分实验条件仅单种子，伪重复问题
- 位置：§4.1, Table 1
- Base/LoRA-only/UG/PCGrad 均为单种子。Wilcoxon 以 N=50 对话为样本，但共享同一模型权重，是伪重复。无法区分实验效果与种子伪影。
- 建议：至少为 LoRA-only 和 PCGrad 增加 2-3 种子（因果排除链关键比较）。

---

### Should-Fix 问题

**W1** [warning] β-steering 恢复 GAR 存在部分循环论证——GAR 就是 goal token 注意力，β-steering 机械提升之。PPL 合理仅排除了表征退化，不唯一确认注意力错配。

**W2** [warning] 单数据集（UltraChat）限制泛化性——未做跨领域验证。

**W3** [warning] 缺失与 split-softmax (Li et al. 2024) 和 Rhea (Hong et al. 2025) 的实验对比。

**W4** [warning] GAR-Dongre 近零可能是 averaging artifact 而非选择性分布偏移的证据。

---

### 主要优势
1. 五路对比设计精良，每组隔离单一因素
2. 负面结果诚实报告（ThreadGate 在 AR 下失败）
3. 统计实践规范（Wilcoxon + bootstrap CI + Bonferroni + 效应量）
4. 跨架构（Qwen + Llama）+ 跨尺度（1.5B）验证
5. 丰富附录（23 页）
6. β-steering 提供可操作的推理时干预方案

### 格式合规
正文 ≤8 页 ✓ | Limitations ✓ | 匿名性 ✓ | ACL 模板 ✓ | AI 声明 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 428 · 2026-05-25T08:26:28.489601+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成独立审稿后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 429 · 2026-05-25T08:26:31.354917+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **Overall 3.5**（Borderline Conference）：分析质量在 Findings 之上，但存在三个 critical 问题阻碍稳进主会议
- **3 个 Must-Fix**：(1) GAR-compliance 弱相关（r=0.200）削弱实际意义；(2) 因果排除不完整（KV cache drift、magnitude imbalance 未测试）但标题措辞过强；(3) 单种子伪重复影响统计可靠性
- **4 个 Should-Fix**：β-steering 部分循环论证、单数据集、缺关键 baseline 对比、GAR-Dongre 解释可能有替代
- **主要优势**：实验设计精良、负面结果诚实、统计规范、跨架构验证充分、附录材料丰富

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 430 · 2026-05-25T08:26:38.719960+00:00_

收到 Reviewer 1 的完整审稿意见。等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 37

## Round 37

6 recorded events


### User

_source line 431 · 2026-05-25T08:26:44.840953+00:00_

[Reviewer 2 审稿意见]:
# Reviewer 2 审稿意见（Round 1）——新颖性 + 完整性 + 写作质量

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**Confidence**: 4 / 5
**一句话总结**: 系统的诊断性实验设计揭示了一个有价值的发现（exposure bias 导致辅助注意力损失在 AR 生成中失效），但实验范围狭窄（单数据集、双模型且 Llama 不完整）、因果声称过强、缺少与关键竞争方法的实验对比，制约了贡献的完整性和影响力。

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 五路对比设计合理，统计分析严谨（Wilcoxon、Bootstrap CI、Bonferroni 校正），但"causal exclusion chain"的因果声称超出了观测性对比实验所能支撑的程度；Llama 仅覆盖 3/5 条件削弱跨架构泛化论证 |
| Excitement | 3/5 | 诊断性贡献有实用价值（揭示 TF→AR gap 的机制），但核心结论（exposure bias 导致 attention 训练-推理不匹配）从既有文献可预期；范围窄、无方法突破限制了更广泛的兴奋度 |
| Reproducibility | 3.5/5 | 附录提供了详尽的超参数和统计细节，但未提供代码链接或开源承诺 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Causal exclusion chain"的因果声称过强，实验设计不支持严格因果推断
- 具体位置：§1 第2段、§5 开头、§7 Conclusion
- 问题：论文将五路对比描述为"causal exclusion chain"，声称每个子实验"kills one alternative hypothesis"。但本质上是观测性对比实验（不同训练配置下的性能比较），而非严格因果干预。+PCGrad vs. TG 的对比同时改变了梯度处理和可能的训练动态，不能干净地隔离单一因素。
- 为什么影响接收：因果声称是论文核心叙事支柱。如果降级为 differential diagnosis，贡献定位需重新校准。
- 建议：将"causal exclusion"改为"systematic diagnostic comparison"；删除"kills one alternative hypothesis"措辞。

**N2** [critical] 缺少与 Li et al. (2024) split-softmax 和 Hong et al. (Rhea) 的实验对比
- 具体位置：§2 Related Work（仅文字讨论），§8 Limitations（未提及）
- 问题：split-softmax 在推理时分离 instruction 与 conversation tokens，直接针对同一问题。β-steering（§4.3）已经证明推理时注意力操控可恢复 GAR，但 split-softmax 作为更实际的推理时方案未被比较。读者无法判断 scheduled sampling 相对于已有推理时方案的 cost-benefit。
- 建议：至少添加 split-softmax 实验对比，或在 Discussion 中定量讨论与 β-steering 的关系。

**N3** [critical] Llama 实验不完整（3/5 条件），削弱"cross-architecture generalization"声称
- 具体位置：§5.5 Cross-Model Replication、Table 7（Appendix F）
- 问题：Llama 缺 PCGrad 和 UG，而这两个条件是 exclusion chain 排除 gradient conflict 和 turn conditioning 假设的关键。此外 Llama 用 median、Qwen 用 mean 报告 AR GAR，构成 metric selection 不一致。
- 建议：补充 Llama PCGrad/UG 实验，或将声称降级为"partial replication"；统一报告指标（同时报告 mean 和 median）。

---

## Should-Fix 问题

**W1** [warning] 标题"Destroys"过度声称——AR GAR 降至 0.01-0.06 而非零，"Collapses"更准确
**W2** [warning] 单数据集（UltraChat 8K）、单领域（多轮对话）——泛化性未验证
**W3** [warning] 质量评估仅依赖 PPL——缺少 MT-Bench、AlpacaEval 等对话质量评估
**W4** [warning] AR 评估 N=50 偏小，长对话评估 N=5 更小
**W5** [warning] "8-17×"数字在全文重复 6+ 次，造成循环论证感
**W6** [warning] 未提供代码链接或开源承诺，影响 reproducibility 评估

---

## 小问题
- M1：参考文献中 Mihaylova 拼为 Mikhaylova（对照 ACL Anthology: P19-2049）
- M2：Abstract 接近 200 词上限
- M3：Figure 1(b) log scale 在 caption 中未明确标注
- M4：GAR-Dongre vs GAR-ours 的数值差异（Table 1 中 GAR-D 极低 0.00-0.02）未充分解释
- M5：§5.2 "first application of PCGrad as a diagnostic tool" 的 first claim 难以验证，建议删除
- M6：Appendix AD 披露 AI 辅助——透明度良好

---

## 主要优势
- S1：五路对比实验设计系统清晰，每对相邻对比仅改变一个因素（§3.4）
- S2：β-steering（§4.3）是巧妙的确认性测试（常数偏置恢复 GAR 从 0.064→0.727）
- S3：统计分析异常严谨（非参数检验、bootstrap CI、Bonferroni 校正、effect size），NLP 论文中属上乘
- S4：25 页附录覆盖 loss formulation search、instruction retention、per-seed results 等多方面
- S5：Scheduled sampling 迁移证明实用的 partial mitigation（gap 7.8×→1.3×，无 PPL cost）

---

## 提问
1. 如果 split-softmax 在推理时能恢复 GAR，scheduled sampling（训练时干预）的必要性是否被削弱？
2. Last-token GAR 能否代表整个回复的 goal adherence？
3. Appendix Q 的 4 种 GAR 替代定义结果差异较大——核心发现是否依赖特定定义？
4. 为什么未设计实验排除 KV cache drift（§7 中承认的替代解释）？
5. Dongre 报告 12 模型 27-48% GAR 衰减/50 turns vs 本文 70.8%/5 turns——差异是否完全由定义不同解释？

---

## 可能遗漏的参考文献
- PASTA (Zhang et al. 2024) 已引用但与 β-steering 的方法论重叠可以讨论更深入
- StreamingLLM attention sink 现象与 GAR 衰减的机制区别可以更明确

---

**总结**：论文有潜力——如果 rebuttal 中（a）降低因果声称，（b）补充 split-softmax 对比，（c）完善 Llama 实验，可升至 4 分（Conference）。当前适合 Findings 或 Borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-25T08:27:07.213525+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "turn_residual_gating",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（方法严谨性 + 实验有效性）的完整审稿原文。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 评分\n**Overall**: 3.5 / 5（Borderline Conference）| **Confidence**: 4 / 5\n\n### Must-Fix 问题\n\n**N1** [critical] GAR 与下游任务相关性极弱（r=0.200, r²=0.04），削弱论文实际意义\n- GAR 仅解释 4% 的 instruction retention 方差。β-steering 下游改善 +11.1pp 未达显著（p=0.077, Table 4）。若 GAR 崩溃不影响实际任务，\"Exposure Bias Destroys\" 的标题暗示的实际危害存疑。\n\n**N2** [critical] 因果排除链不完整——exposure bias 归因过强\n- 仅排除 turn conditioning 和 gradient direction conflict。KV cache drift（§6 自己承认未测试）和 magnitude imbalance（NTP 主导 7.5–14.7×）均未实验验证。标题 \"Destroys\" 过于确定。\n\n**N3** [critical] 大部分实验条件仅单种子，伪重复问题\n- Base/LoRA-only/UG/PCGrad 均为单种子。Wilcoxon 以 N=50 对话为样本，但共享同一模型权重，是伪重复。\n\n### Should-Fix 问题\n\n**W1** β-steering 恢复 GAR 存在部分循环论证\n**W2** 单数据集（UltraChat）限制泛化性\n**W3** 缺失与 split-softmax (Li et al. 2024) 和 Rhea (Hong et al. 2025) 的实验对比\n**W4** GAR-Dongre 近零可能是 averaging artifact\n\n### 主要优势\n1. 五路对比设计精良\n2. 负面结果诚实报告\n3. 统计实践规范\n4. 跨架构+跨尺度验证\n5. 丰富附录（23页）\n6. β-steering 提供可操作推理时干预方案\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应，特别关注你自己审查视角（新颖性/完整性/写作）与 Reviewer 1 发现的一致性或差异。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "turn_residual_gating",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（方法严谨性 + 实验有效性）的完整审稿原文。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 评分\n**Overall**: 3.5 / 5（Borderline Conference）| **Confidence**: 4 / 5\n\n### Must-Fix 问题\n\n**N1** [critical] GAR 与下游任务相关性极弱（r=0.200, r²=0.04），削弱论文实际意义\n- GAR 仅解释 4% 的 instruction retention 方差。β-steering 下游改善 +11.1pp 未达显著（p=0.077, Table 4）。若 GAR 崩溃不影响实际任务，\"Exposure Bias Destroys\" 的标题暗示的实际危害存疑。\n\n**N2** [critical] 因果排除链不完整——exposure bias 归因过强\n- 仅排除 turn conditioning 和 gradient direction conflict。KV cache drift（§6 自己承认未测试）和 magnitude imbalance（NTP 主导 7.5–14.7×）均未实验验证。标题 \"Destroys\" 过于确定。\n\n**N3** [critical] 大部分实验条件仅单种子，伪重复问题\n- Base/LoRA-only/UG/PCGrad 均为单种子。Wilcoxon 以 N=50 对话为样本，但共享同一模型权重，是伪重复。\n\n### Should-Fix 问题\n\n**W1** β-steering 恢复 GAR 存在部分循环论证\n**W2** 单数据集（UltraChat）限制泛化性\n**W3** 缺失与 split-softmax (Li et al. 2024) 和 Rhea (Hong et al. 2025) 的实验对比\n**W4** GAR-Dongre 近零可能是 averaging artifact\n\n### 主要优势\n1. 五路对比设计精良\n2. 负面结果诚实报告\n3. 统计实践规范\n4. 跨架构+跨尺度验证\n5. 丰富附录（23页）\n6. β-steering 提供可操作推理时干预方案\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应，特别关注你自己审查视角（新颖性/完整性/写作）与 Reviewer 1 发现的一致性或差异。"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-25T08:27:19.135272+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11921
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-25T08:27:19.487783+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "turn_residual_gating",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（新颖性 + 完整性 + 写作质量）的完整审稿原文。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 评分\n**Overall**: 3.5 / 5（Borderline Conference）| **Confidence**: 4 / 5\n\n### Must-Fix 问题\n\n**R2-N1** [critical] \"Causal exclusion chain\"的因果声称过强，实验设计不支持严格因果推断\n- 论文将五路对比描述为\"causal exclusion chain\"，声称每个子实验\"kills one alternative hypothesis\"。但本质上是观测性对比实验，不能干净地隔离单一因素。+PCGrad vs. TG 同时改变了梯度处理和训练动态。\n- 建议改为\"systematic diagnostic comparison\"。\n\n**R2-N2** [critical] 缺少与 Li et al. (2024) split-softmax 和 Hong et al. (Rhea) 的实验对比\n- split-softmax 在推理时分离 instruction 与 conversation tokens，直接针对同一问题。读者无法判断 scheduled sampling 相对于已有推理时方案的 cost-benefit。\n\n**R2-N3** [critical] Llama 实验不完整（3/5 条件），削弱\"cross-architecture generalization\"声称\n- Llama 缺 PCGrad 和 UG。Llama 用 median、Qwen 用 mean，metric selection 不一致。\n- 建议补充实验或将声称降级为\"partial replication\"。\n\n### Should-Fix 问题\n\n**R2-W1** 标题\"Destroys\"过度声称——\"Collapses\"更准确\n**R2-W2** 单数据集（UltraChat 8K）限制泛化\n**R2-W3** 质量评估仅依赖 PPL——缺少 MT-Bench、AlpacaEval 等\n**R2-W4** AR 评估 N=50 偏小，长对话 N=5 更小\n**R2-W5** \"8-17×\"数字全文重复 6+ 次，循环论证感\n**R2-W6** 未提供代码链接或开源承诺\n\n### 小问题\n- M1：Mihaylova 拼写可能有误\n- M2：Abstract 接近 200 词上限\n- M3：Figure 1(b) log scale 未在 caption 中标注\n- M4：GAR-Dongre vs GAR-ours 差异未充分解释\n- M5：§5.2 \"first application of PCGrad as a diagnostic tool\" 难以验证\n\n### 主要优势\n- S1：五路对比实验设计系统清晰\n- S2：β-steering 巧妙确认性测试\n- S3：统计分析异常严谨\n- S4：25页附录多方面覆盖\n- S5：Scheduled sampling 迁移实用\n\n### Reviewer 2 关键提问\n1. split-softmax 如能推理时恢复 GAR，scheduled sampling 必要性是否削弱？\n2. Last-token GAR 能否代表整个回复？\n3. Appendix Q 的 4 种 GAR 替代定义结果差异——核心发现依赖特定定义？\n4. 为什么未排除 KV cache drift？\n5. Dongre 12模型 27-48%/50turns vs 本文 70.8%/5turns——差异完全由定义不同解释？\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应，特别关注你自己审查视角（方法/统计/因果推理）与 Reviewer 2 发现的一致性或差异。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "turn_residual_gating",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（新颖性 + 完整性 + 写作质量）的完整审稿原文。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 评分\n**Overall**: 3.5 / 5（Borderline Conference）| **Confidence**: 4 / 5\n\n### Must-Fix 问题\n\n**R2-N1** [critical] \"Causal exclusion chain\"的因果声称过强，实验设计不支持严格因果推断\n- 论文将五路对比描述为\"causal exclusion chain\"，声称每个子实验\"kills one alternative hypothesis\"。但本质上是观测性对比实验，不能干净地隔离单一因素。+PCGrad vs. TG 同时改变了梯度处理和训练动态。\n- 建议改为\"systematic diagnostic comparison\"。\n\n**R2-N2** [critical] 缺少与 Li et al. (2024) split-softmax 和 Hong et al. (Rhea) 的实验对比\n- split-softmax 在推理时分离 instruction 与 conversation tokens，直接针对同一问题。读者无法判断 scheduled sampling 相对于已有推理时方案的 cost-benefit。\n\n**R2-N3** [critical] Llama 实验不完整（3/5 条件），削弱\"cross-architecture generalization\"声称\n- Llama 缺 PCGrad 和 UG。Llama 用 median、Qwen 用 mean，metric selection 不一致。\n- 建议补充实验或将声称降级为\"partial replication\"。\n\n### Should-Fix 问题\n\n**R2-W1** 标题\"Destroys\"过度声称——\"Collapses\"更准确\n**R2-W2** 单数据集（UltraChat 8K）限制泛化\n**R2-W3** 质量评估仅依赖 PPL——缺少 MT-Bench、AlpacaEval 等\n**R2-W4** AR 评估 N=50 偏小，长对话 N=5 更小\n**R2-W5** \"8-17×\"数字全文重复 6+ 次，循环论证感\n**R2-W6** 未提供代码链接或开源承诺\n\n### 小问题\n- M1：Mihaylova 拼写可能有误\n- M2：Abstract 接近 200 词上限\n- M3：Figure 1(b) log scale 未在 caption 中标注\n- M4：GAR-Dongre vs GAR-ours 差异未充分解释\n- M5：§5.2 \"first application of PCGrad as a diagnostic tool\" 难以验证\n\n### 主要优势\n- S1：五路对比实验设计系统清晰\n- S2：β-steering 巧妙确认性测试\n- S3：统计分析异常严谨\n- S4：25页附录多方面覆盖\n- S5：Scheduled sampling 迁移实用\n\n### Reviewer 2 关键提问\n1. split-softmax 如能推理时恢复 GAR，scheduled sampling 必要性是否削弱？\n2. Last-token GAR 能否代表整个回复？\n3. Appendix Q 的 4 种 GAR 替代定义结果差异——核心发现依赖特定定义？\n4. 为什么未排除 KV cache drift？\n5. Dongre 12模型 27-48%/50turns vs 本文 70.8%/5turns——差异完全由定义不同解释？\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应，特别关注你自己审查视角（方法/统计/因果推理）与 Reviewer 2 发现的一致性或差异。"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-25T08:27:21.197620+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1709
}
```

</details>

---


### Assistant

_source line 436 · 2026-05-25T08:27:27.416684+00:00_

交叉分享已派发，等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 437 · 2026-05-25T08:27:30.311933+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall: 3.5/5 (Borderline Conference)**，Soundness 3/5，Excitement 3/5
- **3 个 Must-Fix**：(N1) "causal exclusion chain" 因果声称过强——实际是观测性对比而非严格因果干预；(N2) 缺少与 split-softmax / Rhea 的实验对比；(N3) Llama 仅覆盖 3/5 条件且 mean/median 报告不一致
- **6 个 Should-Fix**：标题 "Destroys" 过强、单数据集单领域、PPL-only 质量评估、N=50 样本偏小、"8-17×" 过度重复、无代码开源
- **主要优势**：五路对比设计系统、β-steering 确认实验巧妙、统计分析严谨、附录充实、scheduled sampling 迁移有实用价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 438 · 2026-05-25T08:27:36.684927+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 39

## Round 39

18 recorded events


### User

_source line 439 · 2026-05-25T08:30:13.436283+00:00_

[Reviewer 2 审稿意见]:
# Reviewer 2 交叉回应（对 Reviewer 1 审稿意见）

## 逐条回应

### Must-Fix

**[AGREE with nuance] R1-N1: GAR与下游弱相关（r²=0.04）**
数据引用准确（§6 p.8, Table 4）。但 R1 解读过严——论文一致将 GAR 定位为 diagnostic probe（§3.1, §6），弱下游相关性不等于无诊断价值。**核心问题在于标题"Destroys"暗示的实际危害与 4% 解释方差不匹配**，与我的 W1（标题 overclaim）一致。建议降为 Should-Fix。

**[AGREE] R1-N2: 因果排除链不完整**
完全同意，与我的 N1 高度一致。R1 补充了两个重要缺口：(1) KV cache drift（§7 自己承认未排除），(2) NTP magnitude imbalance 7.5-14.7×（§5.2）——PCGrad 仅消除方向冲突，未解决量级碾压。**两位 Reviewer 强共识：causal exclusion 声称需降级。**

**[REBUT, 降级为 Should-Fix] R1-N3: 单种子伪重复**
技术上正确但过于严厉：(1) NLP 领域标准做法；(2) 关键条件 ThreadGate 有 2-3 种子（Appendix T p.25），SS 有 2 种子（Table 19）；(3) 效应量 8-17× 远超种子方差（种子间 AR GAR: 0.064 vs 0.055）；(4) Bootstrap CI 部分缓解。建议降为 Should-Fix。

### Should-Fix

**[AGREE] R1-W1: β-steering 部分循环论证** — GAR 恢复是同义反复（boost attention → attention metric recovers），非循环部分（下游 +11.1pp）统计上弱（p=0.077）。论文应解耦两个声称。

**[AGREE] R1-W2: 单数据集** — 与我的 W2 一致。

**[AGREE, 但我评级更高] R1-W3: 缺 split-softmax/Rhea 对比** — 我将此列为 N2 (Must-Fix)。β-steering 已证明推理时干预可恢复 GAR，split-softmax 是更实际的已发表方案，诊断论文不与已有方案对比是完整性缺陷。

**[AGREE] R1-W4: GAR-Dongre 近零是 averaging artifact** — Table 1 所有条件 GAR-D ≈ 0.00-0.02 证实了这点。§3.1 对选择 GAR-ours 的讨论不充分。

## 两位 Reviewer 共识

| 问题 | R1 | R2 | 共识 |
|------|-----|-----|------|
| 因果声称过强 | N2 Must-Fix | N1 Must-Fix | **强共识** |
| 缺 split-softmax 对比 | W3 Should-Fix | N2 Must-Fix | R2 更严重 |
| 标题 overclaim | implicit | W1 Should-Fix | 共识 |
| 单数据集 | W2 | W2 | 一致 |
| Llama 不完整 | 未提 | N3 Must-Fix | 仅 R2 |
| GAR 弱相关 | N1 Must-Fix | — | R2 同意降为 Should-Fix |
| 单种子伪重复 | N3 Must-Fix | — | R2 认为降为 Should-Fix |

**评分维持 3.5/5 (Borderline Conference)**。两位 Reviewer 视角互补（R1 偏统计方法论，R2 偏学术完整性），对核心问题达成共识。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-25T08:30:46.658185+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-25T08:30:47.262652+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-25T08:30:48.772618+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-25T08:30:48.823285+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-25T08:31:33.933306+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
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

_source line 445 · 2026-05-25T08:31:33.984170+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-25T08:31:37.098567+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-25T08:31:37.602025+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T08:18:06.713244+00:00\", \"completed_at\": \"2026-05-25T08:22:11.820091+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，仅 Abstract + Introduction 文本。Figure 1 在 page 2 出现，仍在前 3 页内，属可接受范围，但若能将 Figure 1 提前至 page 1 底部（如压缩 Abstract/Intro 段落）会进一步强化审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（Per-turn GAR under AR）仅占左栏约 1/4 高度，整体偏小；legend 文字（\\\"Qwen TG\\\" / \\\"Llama TG\\\" 等）在打印尺寸下可能偏小，建议适当放大或移到 caption 中说明\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 4 使用 5 种柱状颜色区分训练条件（Base/TG/+PCGrad/UG/LoRA），灰度打印时可区分度下降，建议添加 hatching pattern 辅助区分\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 6(a) 柱状图中多个 variant 的颜色标签较密，图内文字（gate value 数值标注）字号偏小，建议确保 ≥8pt\"}, {\"severity\": \"info\", \"dimension\": \"page 19\", \"message\": \"Appendix Figures 13-14 在同一页密集排列（gate value distribution + NTP/GAR loss），Figure 14 的 4 子图线条较多且颜色相近，辨认度中等\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"Figures 15-17 共 3 张图挤在一页，每张尺寸较小（约 1/3 栏高），建议检查图内文字可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 33\", \"message\": \"最后一页（附录末页）内容约占页面 65%，Figure 27 四子图 + AD 节开头。附录末页不影响审稿印象，可接受\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"全文配色以红/蓝双色为主调，饱和度适中，色盲友好（非纯红绿对比）；同一 method 在不同图中颜色一致，语义连贯性好\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 8}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-25T08:31:37.602399+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-25T08:31:38.557617+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-25T08:31:38.659653+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-25T08:31:38.660838+00:00_

1	# Review Issues Tracker — turn_residual_gating
2	# Round 1 (2026-05-19, dream_20260519T145320)
3	# Round 2 (2026-05-22, fresh re-review of revised paper)
4	# Round 3 (2026-05-22, fresh re-review)
5	# Round 4 (2026-05-25, fresh re-review — current round)
6	# Cross-response phase completed: R1↔R2 high convergence
7	
8	# ============================================================
9	# Issues from Round 1 — status updates through Round 4
10	# ============================================================
11	
12	- id: "R1-N1"
13	  summary: "所有引用渲染为 '?'——bibliography 编译失败"
14	  category: format
15	  severity: info
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  mentions:
20	    - round: 1
21	      reviewers: [1, 2]
22	      note: "Dream paper artifact。"
23	    - round: 2
24	      reviewers: []
25	      note: "视觉审查确认无 [?] 未解析引用。已修复。"
26	    - round: 3
27	      reviewers: []
28	      note: "Round 3 视觉审查确认无未解析引用。维持 resolved。"
29	    - round: 4
30	      reviewers: []
31	      note: "Round 4 视觉审查确认无未解析引用。维持 resolved。"
32	  action_items:
33	    - round: 1
34	      action: "Paper Agent 确保 bibtex 编译正确"
35	      assigned_to: paper_agent
36	      status: done
37	  resolution: "Round 2 视觉审查确认已修复。"
38	  resolution_round: 2
39	
40	- id: "R1-N2"
41	  summary: "单种子支撑结论——统计功效不足 + AR 评估 N=5 过小"
42	  category: experiment
43	  severity: critical
44	  status: open
45	  first_raised_round: 1
46	  last_seen_round: 4
47	  mentions:
48	    - round: 1
49	      reviewers: [1, 2]
50	      note: "Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。"
51	    - round: 2
52	      reviewers: [1, 2]
53	      note: "ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。"
54	    - round: 3
55	      reviewers: [1, 2]
56	      note: "AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。"
57	    - round: 4
58	      reviewers: [1, 2]
59	      note: "两位 Reviewer 独立列为 Critical Must-Fix。交叉回应 R2 完全同意 R1 论证。R2 补充：Appendix T 3-seed CoV=9% 仅覆盖 TG，Table 1 Base/PCGrad
…[truncated 24833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-25T08:39:16.544489+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "turn_residual_gating",
  "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review)\n# Round 4 (2026-05-25, fresh re-review)\n# Round 5 (2026-05-25, fresh re-review — current round)\n# Cross-response phase completed: R1↔R2 convergence reached\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 5\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足 + AR 评估 N=5 过小\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立列为 Critical Must-Fix。交叉回应 R2 完全同意 R1 论证。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N3 Must-Fix。R2 建议降为 Should-Fix：效应量 8-17× 远超种子方差（AR GAR 0.064 vs 0.055），Bootstrap CI 部分缓解。Director 裁定 Should-Fix。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"D048: 6 条件 × 3 seeds from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"AR 评估扩大至 N=50 + bootstrap 95% CI + 条件间成对检验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件 + 显著性检验 + CI\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。未再被提出。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。TF 评估样本量充分。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。AR N=5 问题移至 R1-N2 追踪。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"额外问题：mean/median 未双报，AR/TF 样本量不匹配，attention spikes 未解释。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Should-Fix。R2 建议标题改为 'Cross-Model Replication'。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1。仅 3/5 条件削弱 cross-model generality 声明。\"\n  action_items:\n    - round: 2\n      action: \"D048: 补充 Llama PCGrad+UG 训练+评估\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"写作降级：§5.5 标题→Cross-Model Replication + mean/median 双报\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2/3/4/5 未被独立提出。论文核心 claim 已转向 exposure bias。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"双种子差异大（GAR 0.318 vs 0.418）且策略不同。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047，SS 贡献 ~8.5× 提升。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1 关于 SS 是压缩 TF-AR gap 主要贡献者的分析。ThreadGate 贡献边际。\"\n  action_items:\n    - round: 2\n      action: \"D048: SS 3-seed from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"3 seeds (s42/s123/s456) + mean±std；abstract/conclusion 弱化措辞\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2 — status updates through Round 5\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——contribution 措辞需调整\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"删除 'in principle applicable'。'first' → 'to our knowledge, the first'。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W3: 'to our knowledge, the first' 仍被质疑。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N2 因果排除链不完整（KV cache drift + NTP magnitude imbalance 未排除）与 R2-N1 合并为 Round 5 核心 Must-Fix。两位 Reviewer 强共识。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 4\n      action: \"删除 'to our knowledge, the first' 修饰语，将 GAR 重新定位为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"exposure bias 降级为 'a proximal cause consistent with evidence'；讨论 KV cache drift + magnitude imbalance 替代假说\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 过宽。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 仍有异议但 R1 反驳有理。Director 裁定当前标题可接受。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意 R1 关于 'Mechanistic' → 'Diagnostic' 的建议。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-W1: 'Destroys' 暗示的实际危害与 r²=0.04 不匹配。两位 Reviewer 共识需降调。\"\n  action_items:\n    - round: 2\n      action: \"标题改为 'Per-Layer Residual Gating'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"标题改为反映 exposure bias 核心发现；副标题 'Mechanistic' → 'Diagnostic'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"原文为 'Goal Accessibility Ratio'。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"arXiv 原文验证确认。Critical Must-Fix。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮 Reviewer 未独立提出。待确认是否已修复。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。待确认修复状态。\"\n  action_items:\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因——替代假说讨论不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 降 Should-Fix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"PCGrad 失败可能反映投影副作用（NTP magnitude 增长 7.5×-14.7×）。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 完全同意 R1-N2。补充：Appendix L 数据在 PCGrad 条件下获得不能作为独立验证。两位 Reviewer 强共识此为最关键问题之一。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"§6 扩展 exposure bias 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标——instruction retention 不显著但占页过多\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"McNemar p=0.077 不显著。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"占 Discussion 过多篇幅。建议移入 Appendix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200 的 95% CI ≈ [0.05, 0.35]（N=54）过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"升级为核心问题：r²=0.04 意味着 GAR 仅解释 4% 下游方差。R1 列 Must-Fix (R1-N1)，R2 同意数据但建议 GAR 重定位为 diagnostic probe 可缓解。Director 裁定 Must-Fix。\"\n  action_items:\n    - round: 2\n      action: \"D048: N=200 扩容指令保持实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"提升已有显著数据至主文 + 重新定位 GAR 为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"orphan 条目。\"\n    - round: 2\n      reviewers: [2]\n      note: \"'and others' vs 完整作者列表不一致。\"\n    - round: 3\n      reviewers: [2]\n      note: \"grattafiori2024llama3 格式不一致。\"\n    - round: 4\n      reviewers: [2]\n      note: \"Raposo et al. 2024 → ICML 2024；Gromov et al. 年份一致性。\"\n    - round: 5\n      reviewers: [2]\n      note: \"R2-M3 继续指出 bib 格式问题。\"\n  action_items:\n    - round: 4\n      action: \"统一 bib 格式\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"Reproducibility 3.0/5。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍未解决。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 AR 列需扩容\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现未在表格中呈现。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 列存在但仅 N=5。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M2: Table 1 AR 列缺 GAR-D 和 PPL。\"\n    - round: 5\n      reviewers: [1]\n      note: \"与 R1-N2 联动，AR 列需 N≥50 + CI。\"\n  action_items:\n    - round: 4\n      action: \"AR 列更新为 N≥50 数据 + CI + GAR-D + PPL\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字重复 8+ 次\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 多章节重复。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"出现 8+ 次。\"\n    - round: 4\n      reviewers: [2]\n      note: \"交叉回应 R2 同意应去冗。\"\n    - round: 5\n      reviewers: [2]\n      note: \"仍存在。\"\n  action_items:\n    - round: 4\n      action: \"Abstract/§4.2 保留完整数字，其余改用回指\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 泛化声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable' 未验证。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-N1。\"\n    - round: 5\n      reviewers: [2]\n      note: \"R2-W3: 'to our knowledge, the first' 仍被质疑。合并至 R2-N1 追踪。\"\n  action_items:\n    - round: 4\n      action: \"删除泛化声称，合并至 R2-N1\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. split-softmax 缺实验对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争方法。R1 认为超 scope。\"\n    - round: 4\n      reviewers: [2]\n      note: \"交叉回应 R2 维持观点。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 列 N2 Must-Fix，R1 列 W3 Should-Fix。Director 裁定 Must-Fix：β-steering 已开推理时干预先河，不与已发表推理时方案对比不合理。\"\n  action_items:\n    - round: 4\n      action: \"Related Work 加强理论论证 + Limitations 承认\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"考虑补充 split-softmax 实验对比，或在 Limitations 充分论证不对比的理由\"\n      assigned_to: paper_agent\n      status: open\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure/Table caption overclaim + 重复句\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Figure caption 可能有 overclaim。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Figure 4 caption 重复句。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 3\n      action: \"修正 Fig 3b/Table 1/Fig 4 caption 的 overclaim + 删除 Fig 4 重复句\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后数字更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Abstract/Intro gap 数字需从单 seed 更新为 mean±std。\"\n    - round: 5\n      reviewers: []\n      note: \"仍待 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后统一更新\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"SS 3-seed variance 极大时需应急 framing。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 两 seed 差异 31% 进一步增加应急计划紧迫性。\"\n    - round: 5\n      reviewers: []\n      note: \"SS 统计支撑仍为核心问题。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance\"\n      assigned_to: director\n      status: open\n\n# ============================================================\n# Issues from Round 3 — status updates through Round 5\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"约 8.4 页。Paper Agent 已压缩至 8.0 页。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M7: 页数符合 8 页限制。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  resolution: \"Round 4 确认页数合规。\"\n  resolution_round: 4\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad scope 过度概括\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"'gradient conflict' 未加 'directional' 限定。\"\n    - round: 4\n      reviewers: []\n      note: \"交叉回应 R2 同意 R1（W3）：PCGrad 失败可能反映投影副作用。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1: NTP magnitude imbalance 7.5-14.7× 是 PCGrad 失败的替代解释，需限定 scope。\"\n  action_items:\n    - round: 3\n      action: \"'gradient conflict' → 'gradient direction conflict'；结论提及 magnitude imbalance 未排除\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869) 引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Rhea: Role-aware Heuristic Episodic Attention。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-W7-new 追踪。\"\n    - round: 5\n      reviewers: [2]\n      note: \"与 split-softmax 一并作为缺失对比方案。\"\n  action_items:\n    - round: 3\n      action: \"添加 bib 条目 + §2/§6 引用对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出，R2 反驳（不影响 TF-AR gap）。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-Q4: LoRA rank 16 是否影响结论？\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1 (Q4)。\"\n  action_items:\n    - round: 4\n      action: \"§4.2 或 Limitations 加一句 acknowledge LoRA rank 可能影响 gate 效用上界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"'NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)' 待确认。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"确认准确性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R3-NEW-1\"\n  summary: \"UG 描述不清——未说明仍为可学习 MLP\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"UG 描述仅说 'gates without turn embedding'，未明确仍是可学习的 content-conditioned MLP。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"§4.1 或 §3 加一句说明\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-NEW-2\"\n  summary: \"Contribution (4) 混淆开发迭代与系统消融\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"'seven loss formulations and four training configurations' 混淆了 v1-v7 loss iteration 和五路系统消融。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"拆分为 'loss design iterations (Appendix A)' + 'systematic conditions comparison (Table 1)'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Issues from Round 4 — status updates through Round 5\n# ============================================================\n\n- id: \"R4-N1\"\n  summary: \"GAR 指标与下游任务性能之间缺乏因果验证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200, r²=0.04。R2 补充 N=54 下 95% CI ≈ [0.05, 0.35] 过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N1 Must-Fix，R2 同意数据但建议降级。Director 裁定 Must-Fix：4% 解释方差不足以支撑核心叙事。与 R2-W3 合并追踪。\"\n  action_items:\n    - round: 4\n      action: \"已有数据提升至主文 + GAR 重定位为 diagnostic probe + 补充 MT-Bench 或其他下游评估\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-N2\"\n  summary: \"SS+LoRA-only 消融缺失——ThreadGate 独立贡献不清\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。SS 贡献 ~8.5× vs TG ~2.6×。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 完全同意 R1 (W1)。如果 SS+LoRA-only 达相似水平，ThreadGate 架构贡献大幅降低。关键缺失消融。\"\n  action_items:\n    - round: 4\n      action: \"需要 SS+LoRA-only 实验数据，或在论文中明确承认 ThreadGate 贡献相对于 SS 是边际的\"\n      assigned_to: agent\n      status: open\n\n- id: \"R4-W1\"\n  summary: \"GAR-D 全条件接近零——干预仅在 last token 成功\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-W5: 即使 TF 下 ThreadGate GAR-D = 0.02。\"\n    - round: 5\n      reviewers: [1]\n      note: \"R1-W4: Table 1 所有条件 GAR-D ≈ 0.00-0.02。§3.1 对 GAR-ours vs GAR-D 选择讨论不充分。R2 同意。\"\n  action_items:\n    - round: 4\n      action: \"讨论 GAR-ours vs GAR-D 差异的含义\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W2\"\n  summary: \"Table 1 四舍五入与正文数字精度不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W6: §4.2 称 spread 为 0.75pp 但 Table 1 两位小数显示 1pp。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提及。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 增加一位小数，或正文使用与 table 一致的精度\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W3\"\n  summary: \"r_min 数值正文未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M1: r_min 数值在正文中未报告，影响可复现性。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提及。\"\n  action_items:\n    - round: 4\n      action: \"在 §3 或 Appendix A 中报告 r_min 数值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-MR1\"\n  summary: \"缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"与 β-steering 思路相似的推理时注意力操控方法，应在 §2 讨论。\"\n    - round: 5\n      reviewers: [2]\n      note: \"仍缺失。\"\n  action_items:\n    - round: 4\n      action: \"确认引用存在性并在 §2 引用对比\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W4\"\n  summary: \"Appendix C instruction retention 多重比较未校正\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"主实验已有 Holm-Bonferroni 校正（Appendix E p30），但 Appendix C 18-category McNemar's test 未做 FDR/Bonferroni 校正。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 部分反驳 R1：主实验校正已有，Appendix C 仍缺。共识：Appendix C 需补校正。\"\n  action_items:\n    - round: 4\n      action: \"Appendix C per-category 分析补充 Holm-Bonferroni 或 FDR 校正\"\n      assigned_to: paper_agent\n      status: open"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "turn_residual_gating",
    "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review)\n# Round 4 (2026-05-25, fresh re-review)\n# Round 5 (2026-05-25, fresh re-review — current round)\n# Cross-response phase completed: R1↔R2 convergence reached\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 5\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足 + AR 评估 N=5 过小\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立列为 Critical Must-Fix。交叉回应 R2 完全同意 R1 论证。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N3 Must-Fix。R2 建议降为 Should-Fix：效应量 8-17× 远超种子方差（AR GAR 0.064 vs 0.055），Bootstrap CI 部分缓解。Director 裁定 Should-Fix。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"D048: 6 条件 × 3 seeds from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"AR 评估扩大至 N=50 + bootstrap 95% CI + 条件间成对检验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件 + 显著性检验 + CI\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。未再被提出。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。TF 评估样本量充分。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。AR N=5 问题移至 R1-N2 追踪。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"额外问题：mean/median 未双报，AR/TF 样本量不匹配，attention spikes 未解释。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Should-Fix。R2 建议标题改为 'Cross-Model Replication'。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1。仅 3/5 条件削弱 cross-model generality 声明。\"\n  action_items:\n    - round: 2\n      action: \"D048: 补充 Llama PCGrad+UG 训练+评估\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"写作降级：§5.5 标题→Cross-Model Replication + mean/median 双报\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2/3/4/5 未被独立提出。论文核心 claim 已转向 exposure bias。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"双种子差异大（GAR 0.318 vs 0.418）且策略不同。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047，SS 贡献 ~8.5× 提升。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1 关于 SS 是压缩 TF-AR gap 主要贡献者的分析。ThreadGate 贡献边际。\"\n  action_items:\n    - round: 2\n      action: \"D048: SS 3-seed from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"3 seeds (s42/s123/s456) + mean±std；abstract/conclusion 弱化措辞\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2 — status updates through Round 5\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——contribution 措辞需调整\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"删除 'in principle applicable'。'first' → 'to our knowledge, the first'。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W3: 'to our knowledge, the first' 仍被质疑。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N2 因果排除链不完整（KV cache drift + NTP magnitude imbalance 未排除）与 R2-N1 合并为 Round 5 核心 Must-Fix。两位 Reviewer 强共识。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 4\n      action: \"删除 'to our knowledge, the first' 修饰语，将 GAR 重新定位为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"exposure bias 降级为 'a proximal cause consistent with evidence'；讨论 KV cache drift + magnitude imbalance 替代假说\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 过宽。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 仍有异议但 R1 反驳有理。Director 裁定当前标题可接受。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意 R1 关于 'Mechanistic' → 'Diagnostic' 的建议。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-W1: 'Destroys' 暗示的实际危害与 r²=0.04 不匹配。两位 Reviewer 共识需降调。\"\n  action_items:\n    - round: 2\n      action: \"标题改为 'Per-Layer Residual Gating'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"标题改为反映 exposure bias 核心发现；副标题 'Mechanistic' → 'Diagnostic'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"原文为 'Goal Accessibility Ratio'。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"arXiv 原文验证确认。Critical Must-Fix。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮 Reviewer 未独立提出。待确认是否已修复。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。待确认修复状态。\"\n  action_items:\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因——替代假说讨论不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 降 Should-Fix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"PCGrad 失败可能反映投影副作用（NTP magnitude 增长 7.5×-14.7×）。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 完全同意 R1-N2。补充：Appendix L 数据在 PCGrad 条件下获得不能作为独立验证。两位 Reviewer 强共识此为最关键问题之一。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"§6 扩展 exposure bias 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标——instruction retention 不显著但占页过多\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"McNemar p=0.077 不显著。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"占 Discussion 过多篇幅。建议移入 Appendix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200 的 95% CI ≈ [0.05, 0.35]（N=54）过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"升级为核心问题：r²=0.04 意味着 GAR 仅解释 4% 下游方差。R1 列 Must-Fix (R1-N1)，R2 同意数据但建议 GAR 重定位为 diagnostic probe 可缓解。Director 裁定 Must-Fix。\"\n  action_items:\n    - round: 2\n      action: \"D048: N=200 扩容指令保持实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"提升已有显著数据至主文 + 重新定位 GAR 为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"orphan 条目。\"\n    - round: 2\n      reviewers: [2]\n      note: \"'and others' vs 完整作者列表不一致。\"\n    - round: 3\n      reviewers: [2]\n      note: \"grattafiori2024llama3 格式不一致。\"\n    - round: 4\n      reviewers: [2]\n      note: \"Raposo et al. 2024 → ICML 2024；Gromov et al. 年份一致性。\"\n    - round: 5\n      reviewers: [2]\n      note: \"R2-M3 继续指出 bib 格式问题。\"\n  action_items:\n    - round: 4\n      action: \"统一 bib 格式\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"Reproducibility 3.0/5。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仍未解决。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 AR 列需扩容\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现未在表格中呈现。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 列存在但仅 N=5。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M2: Table 1 AR 列缺 GAR-D 和 PPL。\"\n    - round: 5\n      reviewers: [1]\n      note: \"与 R1-N2 联动，AR 列需 N≥50 + CI。\"\n  action_items:\n    - round: 4\n      action: \"AR 列更新为 N≥50 数据 + CI + GAR-D + PPL\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字重复 8+ 次\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 多章节重复。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"出现 8+ 次。\"\n    - round: 4\n      reviewers: [2]\n      note: \"交叉回应 R2 同意应去冗。\"\n    - round: 5\n      reviewers: [2]\n      note: \"仍存在。\"\n  action_items:\n    - round: 4\n      action: \"Abstract/§4.2 保留完整数字，其余改用回指\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 泛化声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable' 未验证。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-N1。\"\n    - round: 5\n      reviewers: [2]\n      note: \"R2-W3: 'to our knowledge, the first' 仍被质疑。合并至 R2-N1 追踪。\"\n  action_items:\n    - round: 4\n      action: \"删除泛化声称，合并至 R2-N1\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. split-softmax 缺实验对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争方法。R1 认为超 scope。\"\n    - round: 4\n      reviewers: [2]\n      note: \"交叉回应 R2 维持观点。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 列 N2 Must-Fix，R1 列 W3 Should-Fix。Director 裁定 Must-Fix：β-steering 已开推理时干预先河，不与已发表推理时方案对比不合理。\"\n  action_items:\n    - round: 4\n      action: \"Related Work 加强理论论证 + Limitations 承认\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"考虑补充 split-softmax 实验对比，或在 Limitations 充分论证不对比的理由\"\n      assigned_to: paper_agent\n      status: open\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure/Table caption overclaim + 重复句\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Figure caption 可能有 overclaim。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Figure 4 caption 重复句。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 3\n      action: \"修正 Fig 3b/Table 1/Fig 4 caption 的 overclaim + 删除 Fig 4 重复句\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后数字更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Abstract/Intro gap 数字需从单 seed 更新为 mean±std。\"\n    - round: 5\n      reviewers: []\n      note: \"仍待 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后统一更新\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"SS 3-seed variance 极大时需应急 framing。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 两 seed 差异 31% 进一步增加应急计划紧迫性。\"\n    - round: 5\n      reviewers: []\n      note: \"SS 统计支撑仍为核心问题。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance\"\n      assigned_to: director\n      status: open\n\n# ============================================================\n# Issues from Round 3 — status updates through Round 5\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"约 8.4 页。Paper Agent 已压缩至 8.0 页。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M7: 页数符合 8 页限制。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  resolution: \"Round 4 确认页数合规。\"\n  resolution_round: 4\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad scope 过度概括\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"'gradient conflict' 未加 'directional' 限定。\"\n    - round: 4\n      reviewers: []\n      note: \"交叉回应 R2 同意 R1（W3）：PCGrad 失败可能反映投影副作用。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1: NTP magnitude imbalance 7.5-14.7× 是 PCGrad 失败的替代解释，需限定 scope。\"\n  action_items:\n    - round: 3\n      action: \"'gradient conflict' → 'gradient direction conflict'；结论提及 magnitude imbalance 未排除\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869) 引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Rhea: Role-aware Heuristic Episodic Attention。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-W7-new 追踪。\"\n    - round: 5\n      reviewers: [2]\n      note: \"与 split-softmax 一并作为缺失对比方案。\"\n  action_items:\n    - round: 3\n      action: \"添加 bib 条目 + §2/§6 引用对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出，R2 反驳（不影响 TF-AR gap）。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-Q4: LoRA rank 16 是否影响结论？\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1 (Q4)。\"\n  action_items:\n    - round: 4\n      action: \"§4.2 或 Limitations 加一句 acknowledge LoRA rank 可能影响 gate 效用上界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"'NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)' 待确认。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"确认准确性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R3-NEW-1\"\n  summary: \"UG 描述不清——未说明仍为可学习 MLP\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"UG 描述仅说 'gates without turn embedding'，未明确仍是可学习的 content-conditioned MLP。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"§4.1 或 §3 加一句说明\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-NEW-2\"\n  summary: \"Contribution (4) 混淆开发迭代与系统消融\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"'seven loss formulations and four training configurations' 混淆了 v1-v7 loss iteration 和五路系统消融。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"拆分为 'loss design iterations (Appendix A)' + 'systematic conditions comparison (Table 1)'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Issues from Round 4 — status updates through Round 5\n# ============================================================\n\n- id: \"R4-N1\"\n  summary: \"GAR 指标与下游任务性能之间缺乏因果验证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200, r²=0.04。R2 补充 N=54 下 95% CI ≈ [0.05, 0.35] 过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N1 Must-Fix，R2 同意数据但建议降级。Director 裁定 Must-Fix：4% 解释方差不足以支撑核心叙事。与 R2-W3 合并追踪。\"\n  action_items:\n    - round: 4\n      action: \"已有数据提升至主文 + GAR 重定位为 diagnostic probe + 补充 MT-Bench 或其他下游评估\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-N2\"\n  summary: \"SS+LoRA-only 消融缺失——ThreadGate 独立贡献不清\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。SS 贡献 ~8.5× vs TG ~2.6×。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 完全同意 R1 (W1)。如果 SS+LoRA-only 达相似水平，ThreadGate 架构贡献大幅降低。关键缺失消融。\"\n  action_items:\n    - round: 4\n      action: \"需要 SS+LoRA-only 实验数据，或在论文中明确承认 ThreadGate 贡献相对于 SS 是边际的\"\n      assigned_to: agent\n      status: open\n\n- id: \"R4-W1\"\n  summary: \"GAR-D 全条件接近零——干预仅在 last token 成功\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-W5: 即使 TF 下 ThreadGate GAR-D = 0.02。\"\n    - round: 5\n      reviewers: [1]\n      note: \"R1-W4: Table 1 所有条件 GAR-D ≈ 0.00-0.02。§3.1 对 GAR-ours vs GAR-D 选择讨论不充分。R2 同意。\"\n  action_items:\n    - round: 4\n      action: \"讨论 GAR-ours vs GAR-D 差异的含义\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W2\"\n  summary: \"Table 1 四舍五入与正文数字精度不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W6: §4.2 称 spread 为 0.75pp 但 Table 1 两位小数显示 1pp。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提及。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 增加一位小数，或正文使用与 table 一致的精度\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W3\"\n  summary: \"r_min 数值正文未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M1: r_min 数值在正文中未报告，影响可复现性。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提及。\"\n  action_items:\n    - round: 4\n      action: \"在 §3 或 Appendix A 中报告 r_min 数值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-MR1\"\n  summary: \"缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"与 β-steering 思路相似的推理时注意力操控方法，应在 §2 讨论。\"\n    - round: 5\n      reviewers: [2]\n      note: \"仍缺失。\"\n  action_items:\n    - round: 4\n      action: \"确认引用存在性并在 §2 引用对比\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W4\"\n  summary: \"Appendix C instruction retention 多重比较未校正\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"主实验已有 Holm-Bonferroni 校正（Appendix E p30），但 Appendix C 18-category McNemar's test 未做 FDR/Bonferroni 校正。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 部分反驳 R1：主实验校正已有，Appendix C 仍缺。共识：Appendix C 需补校正。\"\n  action_items:\n    - round: 4\n      action: \"Appendix C per-category 分析补充 Holm-Bonferroni 或 FDR 校正\"\n      assigned_to: paper_agent\n      status: open"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-25T08:39:16.645686+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml\", \"bytes\": 25445}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-25T08:41:39.231731+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 5 (Fresh Re-Review)\n\n**论文**: Turn-Residual Gating for Multi-Turn LLMs\n**目标 Venue**: EMNLP 2026 (via ARR)\n**审稿日期**: 2026-05-25\n**Reviewer**: R1 (方法严谨性) + R2 (新颖性/完整性)\n**模式**: 圆桌审稿 Round 1，交叉回应后收敛\n\n---\n\n## Summary\n\n本文研究 per-layer residual gating (ThreadGate) 能否缓解多轮 LLM 在自回归解码中的 per-turn grounding 损失。通过 Qwen2.5-7B + ShareGPT 上五种训练条件（Base, ThreadGate, TG+PCGrad, Uniform Gate, LoRA-only）的系统对比，论文报告所有 gating 变体均无法弥合 teacher-forcing 与 autoregressive 模式下 20-33× 的 GAR 差距，将此归因于 exposure bias 而非 gradient conflict。Llama-3.1-8B 上仅 3/5 条件的跨模型复制部分支持该发现。诊断性 β-steering 干预可部分恢复 GAR 但下游改善微弱（p=0.077）。\n\n---\n\n## Strengths\n\n**S1. 系统的五路条件对比**\nBase / ThreadGate / TG+PCGrad / Uniform Gate / LoRA-only 覆盖了从无干预到 gradient conflict 缓解的合理消融范围。五路设计使每个条件的贡献可分离，实验逻辑清晰。\n\n**S2. 有价值的负面结果**\n证明 lightweight per-layer gating 无法解决 TF-AR grounding gap，对社区有实际意义——避免后续研究重复尝试类似方案。负面结果论文在 ACL venue 中有其独特价值。\n\n**S3. Exposure bias 假说具启发性**\n将 multi-turn grounding 失败从架构层面转向训练范式层面（exposure bias），为社区提供了新的研究方向。SS 条件下 GAR 改善约 8.5× 间接支持这一假说。\n\n**S4. β-steering 诊断工具**\n推理时注意力操控作为诊断手段具有方法论创新性。通过操控注意力权重验证 grounding 机制，为理解 LLM 内部 attention dynamics 提供了可复用工具。\n\n**S5. 丰富的实验材料**\n35 页附录包含 loss formulation iterations (v1-v7)、gate value distributions、per-turn breakdowns、bootstrap CIs 等详尽材料。主文 5 figures + 多 tables，可视化质量可接受。\n\n---\n\n## Weaknesses\n\n### Must-Fix (阻碍接收的关键问题)\n\n**MF1. 因果排除链不完整——exposure bias 声称过强** [R1-N2 + R2-N1, 强共识]\n\n论文将 exposure bias 定位为 TF-AR gap 的根因（\"the proximal cause\"），但因果排除链存在关键缺口：\n- **KV cache drift 未排除**：TF 使用 ground-truth prefix，AR 使用模型生成 prefix，两者 KV cache 内容本质不同。§7 Limitations 自己承认未排除这一混淆变量。\n- **NTP magnitude imbalance**：§5.2 显示 NTP loss magnitude 碾压 GAR loss 7.5-14.7×。PCGrad 仅消除方向冲突（cosine < 0），不处理量级碾压——PCGrad 失败可能反映投影副作用而非 gradient direction conflict 不存在。\n- **Appendix L 非独立验证**：gradient cosine 数据在 PCGrad 条件下获得，不能作为 exposure bias 假说的独立证据。\n- 需要至少排除 KV cache drift（如 AR+oracle-prefix 实验）和明确讨论 magnitude imbalance 后，exposure bias 才能被确立为 proximal cause。\n\n**MF2. GAR 指标与下游任务弱相关——核心叙事基础不稳** [R1-N1 Must-Fix, R2 同意数据但建议降级]\n\nTable 4 / §6 显示 GAR 与 instruction retention rate 的相关性：r ≈ 0.200, r² = 0.04（N=54 paired samples, 95% CI ≈ [0.05, 0.35]）。\n- 标题 \"Destroys\" 暗示 catastrophic downstream impact，但 GAR 仅解释 4% 下游方差\n- CI 跨越近零，统计说服力不足\n- 论文将 GAR 同时用作诊断指标和核心 claim 的支撑——如果 GAR collapse 不能预测下游表现，\"Destroys\" 的叙事需要根本性重构\n- R2 建议重新定位 GAR 为 diagnostic probe（非 optimization target/performance indicator），这可部分缓解但不消除问题——即使作为 diagnostic probe，4% 解释方差仍质疑其诊断价值\n- 建议补充至少一个 established 下游评估（如 MT-Bench multi-turn subset）建立 GAR 与实际性能的桥梁\n\n**MF3. 缺少推理时方案实验对比** [R2-N2 Must-Fix, R1-W3 Should-Fix, Director 裁定 Must-Fix]\n\nβ-steering 已证明推理时注意力干预可恢复 GAR，但论文未与已发表的推理时方案做实验对比：\n- **Li et al. 2024 split-softmax**：最直接的竞争方案，通过 softmax 分离解决 multi-turn attention 问题\n- **Rhea (arXiv:2512.06869)**：Role-aware Heuristic Episodic Attention\n- 作为诊断论文，自己做了推理时干预（β-steering）却不与已有推理时方案比较，是实验完整性缺陷\n- 至少需要在 Related Work 中做理论对比，理想情况下应有实验数据\n\n### Should-Fix (影响论文质量但不直接阻碍接收)\n\n**SF1. β-steering 部分循环论证** [R1-W1, R2 同意]\nβ-steering boost attention → GAR（attention metric）recovers 是同义反复。非循环部分（下游 instruction retention +11.1pp）的 McNemar p=0.077 未达 α=0.05 显著水平。论文应解耦 GAR 恢复（自明）与下游改善（需独立统计支撑）两个声称。\n\n**SF2. 单数据集 + 单模型为主** [R1-W2 + R2-W2, 一致]\n核心实验仅在 ShareGPT（8K conversations）+ Qwen2.5-7B 上完成。Llama 跨模型复制仅覆盖 3/5 条件且使用 median 报告（mean/median 未双报，存在 metric selection 之嫌）。对 \"general phenomenon\" 的泛化声称缺乏数据集多样性支撑。\n\n**SF3. 单种子伪重复** [R1-N3 Must-Fix, R2 建议降级, Director 裁定 Should-Fix]\nTable 1 中 Base/PCGrad/UG 为单种子。ThreadGate 有 2-3 种子（Appendix T），SS 有 2 种子但协议不同不可比。\n- R2 反驳降级理由：效应量 8-17× 远超种子间方差（AR GAR seed 42: 0.064 vs seed 123: 0.055），Bootstrap CI 部分缓解\n- Director 裁定 Should-Fix：效应量确实大，但 training variance 完全未覆盖仍是方法论遗憾。至少应在 Limitations 中讨论。\n\n**SF4. Llama 跨模型验证不完整** [R2-N3 Must-Fix, R1 未独立提出, Director 裁定 Should-Fix]\n仅 3/5 条件（Base, TG, LoRA-only），缺 PCGrad 和 Uniform Gate。\"Cross-model generality\" 声称缺乏支撑。\n- 建议标题改为 \"Cross-Model Replication\" 并双报 mean/median\n- Llama cross-model gap 对比需准确：论文对比数字应与 Qwen 结果使用相同 metric 口径\n\n**SF5. 标题 overclaim** [R2-W1, R1 隐含同意]\n\"Destroys\" 暗示 catastrophic downstream failure，但 GAR collapse 仅解释 4% 下游方差。当前标题与证据强度不匹配。建议调整标题反映诊断发现（如 \"collapses\" 或 \"degrades\"）而非灾难性后果。\n\n**SF6. GAR-Dongre 全条件接近零——度量选择讨论不充分** [R1-W4, R2 同意]\nTable 1 所有条件 GAR-D ≈ 0.00-0.02（包括 TF 下 ThreadGate 也仅 0.02）。§3.1 对选择 GAR-ours 而非 Dongre 原始定义的讨论不充分。干预仅在 τ-masked last token 成功，泛化性问题未讨论。\n\n**SF7. SS+LoRA-only 消融缺失** [R1-W1 + R2 交叉共识]\nSS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。SS 贡献 ~8.5× 提升 vs ThreadGate ~2.6×。如果 SS+LoRA-only（无 gating 架构）达到相似水平，ThreadGate 的架构贡献将大幅降低。此消融对论文核心结论有决定性影响——建议补充实验或明确承认 ThreadGate 贡献相对于 SS 是边际的。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 定级 | R2 定级 | Director 裁定 |\n|------|---------|---------|---------------|\n| 因果排除链不完整 | N2 Must-Fix | N1 Must-Fix | **Must-Fix** (强共识) |\n| GAR 弱下游相关 r²=0.04 | N1 Must-Fix | Should-Fix | **Must-Fix** (4% 不足以支撑核心叙事) |\n| 缺 split-softmax/Rhea 对比 | W3 Should-Fix | N2 Must-Fix | **Must-Fix** (诊断论文完整性) |\n| β-steering 循环论证 | W1 Should-Fix | 同意 | **Should-Fix** |\n| 单数据集 | W2 Should-Fix | W2 Should-Fix | **Should-Fix** |\n| 单种子伪重复 | N3 Must-Fix | Should-Fix | **Should-Fix** (效应量大) |\n| Llama 不完整 | 未提 | N3 Must-Fix | **Should-Fix** |\n| 标题 overclaim | 隐含同意 | W1 Should-Fix | **Should-Fix** |\n| GAR-D 近零 artifact | W4 Should-Fix | 同意 | **Should-Fix** |\n| SS+LoRA-only 消融缺失 | W1 | 同意 | **Should-Fix** |\n\n---\n\n## Reviewer Divergence\n\n**1. GAR 弱相关的严重性**\n- R1 视为 Must-Fix：核心指标不可靠，论文基础动摇\n- R2 视为 Should-Fix：若重定位 GAR 为 diagnostic probe，弱下游相关可接受\n- **Director 裁定 Must-Fix**：即使作为 diagnostic probe，4% 解释方差也严重削弱论文叙事的说服力。\"Destroys\" 隐含的 downstream harm 需要更强的下游证据支撑。\n\n**2. 单种子的严重性**\n- R1 视为 Must-Fix：统计方法论问题，训练方差完全未覆盖\n- R2 认为效应量 8-17× 足以缓解，建议降为 Should-Fix\n- **Director 裁定 Should-Fix**：效应量确实远超 seed noise（CoV ~9%），但方法论洁癖要求至少讨论这一限制。\n\n**3. Split-softmax 对比的严重性**\n- R1 视为 Should-Fix：超出论文 scope（诊断 vs 解决方案）\n- R2 视为 Must-Fix：β-steering 已开推理时干预先河，不对比不合理\n- **Director 裁定 Must-Fix**：论文自己做了推理时干预实验，却不与已发表的推理时方案比较，是逻辑不一致。\n\n---\n\n## Questions\n\nQ1. 如果 GAR 与下游 instruction retention 仅 r²=0.04，为什么 GAR 是论文的核心指标？有没有更好的 grounding proxy metric？\n\nQ2. SS 贡献 ~8.5× vs ThreadGate ~2.6×，如果进一步做 SS+LoRA-only 消融，ThreadGate 的独立架构价值还有多少？\n\nQ3. KV cache drift 是否是 TF-AR gap 的另一个 confound？可以设计什么实验排除？（如 AR decoding with oracle-prefix injection）\n\nQ4. LoRA rank 16 是否可能限制了 gate 效用上界？在更高 rank（32/64）下是否会有不同结论？\n\nQ5. GAR-ours 与 GAR-Dongre 的巨大差异（~0.5 vs ~0.01）的根因是什么？这是否意味着 Dongre 原始定义在 multi-turn 场景下更鲁棒（不受 last-token attention 主导）？\n\n---\n\n## Missing References\n\n- **Li et al. 2024** — split-softmax：最直接的推理时 multi-turn attention 解决方案，需在 §2 对比讨论 [R1, R2 共识]\n- **Rhea (arXiv:2512.06869)** — Role-aware Heuristic Episodic Attention：与 β-steering 思路相关 [R1, R2 共识]\n- **Zhang et al. 2024** \"Tell Your Model Where to Attend\" — 推理时注意力操控方法，与 β-steering 高度相关 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**\n\n---\n\n## Visual Layout Check (非评分项)\n\n**状态：已完成** (耗时 ~4 分钟，0 critical / 0 warning / 8 info)\n\n主要发现：\n- **Page 1**：首页无 display item，Figure 1 在 page 2（可接受但非最优——若能将 Figure 1 提前至 page 1 底部会强化第一印象）\n- **Page 4**：Figure 2 偏小，legend 文字在打印尺寸下可能偏小\n- **Page 6**：Figure 4 五种柱状颜色灰度打印可区分度下降，建议添加 hatching pattern\n- **Page 8**：Figure 6(a) 标签密集，图内数值标注字号偏小（建议 ≥8pt）\n- **Pages 19-20**：附录图表密集排列（3 张图挤一页），单图尺寸偏小\n- **全文配色**：红/蓝双色主调，饱和度适中，色盲友好（非纯红绿对比），语义连贯性好\n\n整体排版质量可接受，无影响审稿印象的严重问题。\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | Director |\n|------|-----|-----|----------|\n| Overall | 3.5 | 3.5 | **3.0** |\n\n**Director 综合评分：3.0 / 5 (Findings)**\n\n**置信度：4/5 (High)**\n\n### 评分理由\n\n本文呈现了一个有价值的负面结果——lightweight per-layer gating 无法弥合多轮 LLM 的 TF-AR grounding gap——并提出 exposure bias 作为解释假说。系统的五路条件对比和 β-steering 诊断工具是亮点。\n\n**3 个 Must-Fix 问题严重限制接收前景：**\n1. **因果声称过强**：exposure bias 归因缺少对 KV cache drift 和 NTP magnitude imbalance 的排除，\"root cause\" 声称站不住\n2. **核心指标薄弱**：GAR 与下游仅 r²=0.04，\"Destroys\" 叙事的基础不稳\n3. **缺少推理时方案对比**：β-steering 开了推理时干预的口子但未与 split-softmax 等已发表方案比较\n\n这三个问题跨越方法论（因果推断）、指标有效性、实验完整性三个维度，非单纯写作修改可解决，需要补充实验和重新校准 claims。\n\n**Director 评分低于两位 Reviewer 0.5 分的理由：**\n跨 5 轮审稿，因果排除链（R2-C3, Round 2 首次提出）和 GAR 有效性（R2-W3, Round 1 首次提出）从未被真正解决——每轮只是措辞微调而非补充排除实验。持续未解决的核心问题累积降低了论文在审稿周期内可修复的信心。\n\n**升级路径（→ 3.5 Borderline Conference）：**\n(a) 将 GAR 明确重定位为 diagnostic probe + 补充至少一个 established 下游评估（MT-Bench multi-turn）\n(b) 将 exposure bias 降级为 \"a proximal cause consistent with evidence\" 并充分讨论替代假说\n(c) 补充 SS+LoRA-only 消融以明确 ThreadGate 独立贡献\n(d) 至少与 split-softmax 做理论对比（实验对比更佳）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Destroys\" 标题词与 r²=0.04 不匹配，需降调\n- Contribution (1) \"to our knowledge, the first\" 仍被 R2 质疑——跨 5 轮未解决\n\n### §3 Method / GAR Definition\n- r_min 数值在正文中未报告（仅 Appendix），影响可复现性 [R1-M1]\n- GAR-ours vs GAR-Dongre 选择理由不充分——GAR-D 全条件 ≈ 0.00-0.02，论文未解释为何弃用更稳定的原始定义\n- UG 描述需明确仍为可学习 MLP（当前仅说 \"gates without turn embedding\"）\n\n### §4 Results\n- Table 1 AR 列仍仅 N=5，需扩容至 N≥50 + CI + GAR-D + PPL [R1-M2]\n- 数字精度不一致：§4.2 称 spread 0.75pp 但 Table 1 两位小数显示 1pp\n- \"20-33× gap\" 重复 8+ 次——Abstract/§4.2 保留完整数字，其余用回指\n\n### §5 Analysis\n- PCGrad 失败分析需限定 scope：\"gradient direction conflict\" 而非泛化的 \"gradient conflict\"。NTP magnitude imbalance 7.5-14.7× 是替代解释，必须讨论。\n- β-steering GAR 恢复是同义反复（boost attention → attention metric recovers），需与下游效果解耦报告\n- §5.5 Llama：仅 3/5 条件，标题建议改为 \"Cross-Model Replication\"，mean/median 双报\n\n### §6 Discussion\n- Exposure bias 归因需降级措辞：当前论证不足以支撑 \"root cause\"\n- Instruction retention McNemar p=0.077 未达显著，CI 过宽 [0.05, 0.35]\n- 缺少与 split-softmax / Rhea 的实验或理论对比\n\n### §7 Limitations\n- KV cache drift 已提及但未设计排除实验\n- LoRA rank capacity saturation 未讨论\n\n### Appendix\n- Appendix C per-category McNemar's test（18 categories）未做 FDR/Bonferroni 校正——主实验已有 Holm-Bonferroni（Appendix E p30），但 Appendix C 漏掉了\n- Bib 格式仍有不一致：Raposo et al. 缺 ICML 2024 venue、Gromov et al. 年份问题\n- liu2016attention 引用可能错配（语音识别 vs 注意力引导），需确认\n\n### 复现性\n- 无代码/数据发布承诺——作为负面结果论文，复现材料是可复现性最后防线。跨 5 轮未解决。",
  "project": "turn_residual_gating",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 5 (Fresh Re-Review)\n\n**论文**: Turn-Residual Gating for Multi-Turn LLMs\n**目标 Venue**: EMNLP 2026 (via ARR)\n**审稿日期**: 2026-05-25\n**Reviewer**: R1 (方法严谨性) + R2 (新颖性/完整性)\n**模式**: 圆桌审稿 Round 1，交叉回应后收敛\n\n---\n\n## Summary\n\n本文研究 per-layer residual gating (ThreadGate) 能否缓解多轮 LLM 在自回归解码中的 per-turn grounding 损失。通过 Qwen2.5-7B + ShareGPT 上五种训练条件（Base, ThreadGate, TG+PCGrad, Uniform Gate, LoRA-only）的系统对比，论文报告所有 gating 变体均无法弥合 teacher-forcing 与 autoregressive 模式下 20-33× 的 GAR 差距，将此归因于 exposure bias 而非 gradient conflict。Llama-3.1-8B 上仅 3/5 条件的跨模型复制部分支持该发现。诊断性 β-steering 干预可部分恢复 GAR 但下游改善微弱（p=0.077）。\n\n---\n\n## Strengths\n\n**S1. 系统的五路条件对比**\nBase / ThreadGate / TG+PCGrad / Uniform Gate / LoRA-only 覆盖了从无干预到 gradient conflict 缓解的合理消融范围。五路设计使每个条件的贡献可分离，实验逻辑清晰。\n\n**S2. 有价值的负面结果**\n证明 lightweight per-layer gating 无法解决 TF-AR grounding gap，对社区有实际意义——避免后续研究重复尝试类似方案。负面结果论文在 ACL venue 中有其独特价值。\n\n**S3. Exposure bias 假说具启发性**\n将 multi-turn grounding 失败从架构层面转向训练范式层面（exposure bias），为社区提供了新的研究方向。SS 条件下 GAR 改善约 8.5× 间接支持这一假说。\n\n**S4. β-steering 诊断工具**\n推理时注意力操控作为诊断手段具有方法论创新性。通过操控注意力权重验证 grounding 机制，为理解 LLM 内部 attention dynamics 提供了可复用工具。\n\n**S5. 丰富的实验材料**\n35 页附录包含 loss formulation iterations (v1-v7)、gate value distributions、per-turn breakdowns、bootstrap CIs 等详尽材料。主文 5 figures + 多 tables，可视化质量可接受。\n\n---\n\n## Weaknesses\n\n### Must-Fix (阻碍接收的关键问题)\n\n**MF1. 因果排除链不完整——exposure bias 声称过强** [R1-N2 + R2-N1, 强共识]\n\n论文将 exposure bias 定位为 TF-AR gap 的根因（\"the proximal cause\"），但因果排除链存在关键缺口：\n- **KV cache drift 未排除**：TF 使用 ground-truth prefix，AR 使用模型生成 prefix，两者 KV cache 内容本质不同。§7 Limitations 自己承认未排除这一混淆变量。\n- **NTP magnitude imbalance**：§5.2 显示 NTP loss magnitude 碾压 GAR loss 7.5-14.7×。PCGrad 仅消除方向冲突（cosine < 0），不处理量级碾压——PCGrad 失败可能反映投影副作用而非 gradient direction conflict 不存在。\n- **Appendix L 非独立验证**：gradient cosine 数据在 PCGrad 条件下获得，不能作为 exposure bias 假说的独立证据。\n- 需要至少排除 KV cache drift（如 AR+oracle-prefix 实验）和明确讨论 magnitude imbalance 后，exposure bias 才能被确立为 proximal cause。\n\n**MF2. GAR 指标与下游任务弱相关——核心叙事基础不稳** [R1-N1 Must-Fix, R2 同意数据但建议降级]\n\nTable 4 / §6 显示 GAR 与 instruction retention rate 的相关性：r ≈ 0.200, r² = 0.04（N=54 paired samples, 95% CI ≈ [0.05, 0.35]）。\n- 标题 \"Destroys\" 暗示 catastrophic downstream impact，但 GAR 仅解释 4% 下游方差\n- CI 跨越近零，统计说服力不足\n- 论文将 GAR 同时用作诊断指标和核心 claim 的支撑——如果 GAR collapse 不能预测下游表现，\"Destroys\" 的叙事需要根本性重构\n- R2 建议重新定位 GAR 为 diagnostic probe（非 optimization target/performance indicator），这可部分缓解但不消除问题——即使作为 diagnostic probe，4% 解释方差仍质疑其诊断价值\n- 建议补充至少一个 established 下游评估（如 MT-Bench multi-turn subset）建立 GAR 与实际性能的桥梁\n\n**MF3. 缺少推理时方案实验对比** [R2-N2 Must-Fix, R1-W3 Should-Fix, Director 裁定 Must-Fix]\n\nβ-steering 已证明推理时注意力干预可恢复 GAR，但论文未与已发表的推理时方案做实验对比：\n- **Li et al. 2024 split-softmax**：最直接的竞争方案，通过 softmax 分离解决 multi-turn attention 问题\n- **Rhea (arXiv:2512.06869)**：Role-aware Heuristic Episodic Attention\n- 作为诊断论文，自己做了推理时干预（β-steering）却不与已有推理时方案比较，是实验完整性缺陷\n- 至少需要在 Related Work 中做理论对比，理想情况下应有实验数据\n\n### Should-Fix (影响论文质量但不直接阻碍接收)\n\n**SF1. β-steering 部分循环论证** [R1-W1, R2 同意]\nβ-steering boost attention → GAR（attention metric）recovers 是同义反复。非循环部分（下游 instruction retention +11.1pp）的 McNemar p=0.077 未达 α=0.05 显著水平。论文应解耦 GAR 恢复（自明）与下游改善（需独立统计支撑）两个声称。\n\n**SF2. 单数据集 + 单模型为主** [R1-W2 + R2-W2, 一致]\n核心实验仅在 ShareGPT（8K conversations）+ Qwen2.5-7B 上完成。Llama 跨模型复制仅覆盖 3/5 条件且使用 median 报告（mean/median 未双报，存在 metric selection 之嫌）。对 \"general phenomenon\" 的泛化声称缺乏数据集多样性支撑。\n\n**SF3. 单种子伪重复** [R1-N3 Must-Fix, R2 建议降级, Director 裁定 Should-Fix]\nTable 1 中 Base/PCGrad/UG 为单种子。ThreadGate 有 2-3 种子（Appendix T），SS 有 2 种子但协议不同不可比。\n- R2 反驳降级理由：效应量 8-17× 远超种子间方差（AR GAR seed 42: 0.064 vs seed 123: 0.055），Bootstrap CI 部分缓解\n- Director 裁定 Should-Fix：效应量确实大，但 training variance 完全未覆盖仍是方法论遗憾。至少应在 Limitations 中讨论。\n\n**SF4. Llama 跨模型验证不完整** [R2-N3 Must-Fix, R1 未独立提出, Director 裁定 Should-Fix]\n仅 3/5 条件（Base, TG, LoRA-only），缺 PCGrad 和 Uniform Gate。\"Cross-model generality\" 声称缺乏支撑。\n- 建议标题改为 \"Cross-Model Replication\" 并双报 mean/median\n- Llama cross-model gap 对比需准确：论文对比数字应与 Qwen 结果使用相同 metric 口径\n\n**SF5. 标题 overclaim** [R2-W1, R1 隐含同意]\n\"Destroys\" 暗示 catastrophic downstream failure，但 GAR collapse 仅解释 4% 下游方差。当前标题与证据强度不匹配。建议调整标题反映诊断发现（如 \"collapses\" 或 \"degrades\"）而非灾难性后果。\n\n**SF6. GAR-Dongre 全条件接近零——度量选择讨论不充分** [R1-W4, R2 同意]\nTable 1 所有条件 GAR-D ≈ 0.00-0.02（包括 TF 下 ThreadGate 也仅 0.02）。§3.1 对选择 GAR-ours 而非 Dongre 原始定义的讨论不充分。干预仅在 τ-masked last token 成功，泛化性问题未讨论。\n\n**SF7. SS+LoRA-only 消融缺失** [R1-W1 + R2 交叉共识]\nSS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。SS 贡献 ~8.5× 提升 vs ThreadGate ~2.6×。如果 SS+LoRA-only（无 gating 架构）达到相似水平，ThreadGate 的架构贡献将大幅降低。此消融对论文核心结论有决定性影响——建议补充实验或明确承认 ThreadGate 贡献相对于 SS 是边际的。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 定级 | R2 定级 | Director 裁定 |\n|------|---------|---------|---------------|\n| 因果排除链不完整 | N2 Must-Fix | N1 Must-Fix | **Must-Fix** (强共识) |\n| GAR 弱下游相关 r²=0.04 | N1 Must-Fix | Should-Fix | **Must-Fix** (4% 不足以支撑核心叙事) |\n| 缺 split-softmax/Rhea 对比 | W3 Should-Fix | N2 Must-Fix | **Must-Fix** (诊断论文完整性) |\n| β-steering 循环论证 | W1 Should-Fix | 同意 | **Should-Fix** |\n| 单数据集 | W2 Should-Fix | W2 Should-Fix | **Should-Fix** |\n| 单种子伪重复 | N3 Must-Fix | Should-Fix | **Should-Fix** (效应量大) |\n| Llama 不完整 | 未提 | N3 Must-Fix | **Should-Fix** |\n| 标题 overclaim | 隐含同意 | W1 Should-Fix | **Should-Fix** |\n| GAR-D 近零 artifact | W4 Should-Fix | 同意 | **Should-Fix** |\n| SS+LoRA-only 消融缺失 | W1 | 同意 | **Should-Fix** |\n\n---\n\n## Reviewer Divergence\n\n**1. GAR 弱相关的严重性**\n- R1 视为 Must-Fix：核心指标不可靠，论文基础动摇\n- R2 视为 Should-Fix：若重定位 GAR 为 diagnostic probe，弱下游相关可接受\n- **Director 裁定 Must-Fix**：即使作为 diagnostic probe，4% 解释方差也严重削弱论文叙事的说服力。\"Destroys\" 隐含的 downstream harm 需要更强的下游证据支撑。\n\n**2. 单种子的严重性**\n- R1 视为 Must-Fix：统计方法论问题，训练方差完全未覆盖\n- R2 认为效应量 8-17× 足以缓解，建议降为 Should-Fix\n- **Director 裁定 Should-Fix**：效应量确实远超 seed noise（CoV ~9%），但方法论洁癖要求至少讨论这一限制。\n\n**3. Split-softmax 对比的严重性**\n- R1 视为 Should-Fix：超出论文 scope（诊断 vs 解决方案）\n- R2 视为 Must-Fix：β-steering 已开推理时干预先河，不对比不合理\n- **Director 裁定 Must-Fix**：论文自己做了推理时干预实验，却不与已发表的推理时方案比较，是逻辑不一致。\n\n---\n\n## Questions\n\nQ1. 如果 GAR 与下游 instruction retention 仅 r²=0.04，为什么 GAR 是论文的核心指标？有没有更好的 grounding proxy metric？\n\nQ2. SS 贡献 ~8.5× vs ThreadGate ~2.6×，如果进一步做 SS+LoRA-only 消融，ThreadGate 的独立架构价值还有多少？\n\nQ3. KV cache drift 是否是 TF-AR gap 的另一个 confound？可以设计什么实验排除？（如 AR decoding with oracle-prefix injection）\n\nQ4. LoRA rank 16 是否可能限制了 gate 效用上界？在更高 rank（32/64）下是否会有不同结论？\n\nQ5. GAR-ours 与 GAR-Dongre 的巨大差异（~0.5 vs ~0.01）的根因是什么？这是否意味着 Dongre 原始定义在 multi-turn 场景下更鲁棒（不受 last-token attention 主导）？\n\n---\n\n## Missing References\n\n- **Li et al. 2024** — split-softmax：最直接的推理时 multi-turn attention 解决方案，需在 §2 对比讨论 [R1, R2 共识]\n- **Rhea (arXiv:2512.06869)** — Role-aware Heuristic Episodic Attention：与 β-steering 思路相关 [R1, R2 共识]\n- **Zhang et al. 2024** \"Tell Your Model Where to Attend\" — 推理时注意力操控方法，与 β-steering 高度相关 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**\n\n---\n\n## Visual Layout Check (非评分项)\n\n**状态：已完成** (耗时 ~4 分钟，0 critical / 0 warning / 8 info)\n\n主要发现：\n- **Page 1**：首页无 display item，Figure 1 在 page 2（可接受但非最优——若能将 Figure 1 提前至 page 1 底部会强化第一印象）\n- **Page 4**：Figure 2 偏小，legend 文字在打印尺寸下可能偏小\n- **Page 6**：Figure 4 五种柱状颜色灰度打印可区分度下降，建议添加 hatching pattern\n- **Page 8**：Figure 6(a) 标签密集，图内数值标注字号偏小（建议 ≥8pt）\n- **Pages 19-20**：附录图表密集排列（3 张图挤一页），单图尺寸偏小\n- **全文配色**：红/蓝双色主调，饱和度适中，色盲友好（非纯红绿对比），语义连贯性好\n\n整体排版质量可接受，无影响审稿印象的严重问题。\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | Director |\n|------|-----|-----|----------|\n| Overall | 3.5 | 3.5 | **3.0** |\n\n**Director 综合评分：3.0 / 5 (Findings)**\n\n**置信度：4/5 (High)**\n\n### 评分理由\n\n本文呈现了一个有价值的负面结果——lightweight per-layer gating 无法弥合多轮 LLM 的 TF-AR grounding gap——并提出 exposure bias 作为解释假说。系统的五路条件对比和 β-steering 诊断工具是亮点。\n\n**3 个 Must-Fix 问题严重限制接收前景：**\n1. **因果声称过强**：exposure bias 归因缺少对 KV cache drift 和 NTP magnitude imbalance 的排除，\"root cause\" 声称站不住\n2. **核心指标薄弱**：GAR 与下游仅 r²=0.04，\"Destroys\" 叙事的基础不稳\n3. **缺少推理时方案对比**：β-steering 开了推理时干预的口子但未与 split-softmax 等已发表方案比较\n\n这三个问题跨越方法论（因果推断）、指标有效性、实验完整性三个维度，非单纯写作修改可解决，需要补充实验和重新校准 claims。\n\n**Director 评分低于两位 Reviewer 0.5 分的理由：**\n跨 5 轮审稿，因果排除链（R2-C3, Round 2 首次提出）和 GAR 有效性（R2-W3, Round 1 首次提出）从未被真正解决——每轮只是措辞微调而非补充排除实验。持续未解决的核心问题累积降低了论文在审稿周期内可修复的信心。\n\n**升级路径（→ 3.5 Borderline Conference）：**\n(a) 将 GAR 明确重定位为 diagnostic probe + 补充至少一个 established 下游评估（MT-Bench multi-turn）\n(b) 将 exposure bias 降级为 \"a proximal cause consistent with evidence\" 并充分讨论替代假说\n(c) 补充 SS+LoRA-only 消融以明确 ThreadGate 独立贡献\n(d) 至少与 split-softmax 做理论对比（实验对比更佳）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Destroys\" 标题词与 r²=0.04 不匹配，需降调\n- Contribution (1) \"to our knowledge, the first\" 仍被 R2 质疑——跨 5 轮未解决\n\n### §3 Method / GAR Definition\n- r_min 数值在正文中未报告（仅 Appendix），影响可复现性 [R1-M1]\n- GAR-ours vs GAR-Dongre 选择理由不充分——GAR-D 全条件 ≈ 0.00-0.02，论文未解释为何弃用更稳定的原始定义\n- UG 描述需明确仍为可学习 MLP（当前仅说 \"gates without turn embedding\"）\n\n### §4 Results\n- Table 1 AR 列仍仅 N=5，需扩容至 N≥50 + CI + GAR-D + PPL [R1-M2]\n- 数字精度不一致：§4.2 称 spread 0.75pp 但 Table 1 两位小数显示 1pp\n- \"20-33× gap\" 重复 8+ 次——Abstract/§4.2 保留完整数字，其余用回指\n\n### §5 Analysis\n- PCGrad 失败分析需限定 scope：\"gradient direction conflict\" 而非泛化的 \"gradient conflict\"。NTP magnitude imbalance 7.5-14.7× 是替代解释，必须讨论。\n- β-steering GAR 恢复是同义反复（boost attention → attention metric recovers），需与下游效果解耦报告\n- §5.5 Llama：仅 3/5 条件，标题建议改为 \"Cross-Model Replication\"，mean/median 双报\n\n### §6 Discussion\n- Exposure bias 归因需降级措辞：当前论证不足以支撑 \"root cause\"\n- Instruction retention McNemar p=0.077 未达显著，CI 过宽 [0.05, 0.35]\n- 缺少与 split-softmax / Rhea 的实验或理论对比\n\n### §7 Limitations\n- KV cache drift 已提及但未设计排除实验\n- LoRA rank capacity saturation 未讨论\n\n### Appendix\n- Appendix C per-category McNemar's test（18 categories）未做 FDR/Bonferroni 校正——主实验已有 Holm-Bonferroni（Appendix E p30），但 Appendix C 漏掉了\n- Bib 格式仍有不一致：Raposo et al. 缺 ICML 2024 venue、Gromov et al. 年份问题\n- liu2016attention 引用可能错配（语音识别 vs 注意力引导），需确认\n\n### 复现性\n- 无代码/数据发布承诺——作为负面结果论文，复现材料是可复现性最后防线。跨 5 轮未解决。",
    "project": "turn_residual_gating",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-25T08:41:43.854812+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4623
}
```

</details>

---


### Assistant

_source line 456 · 2026-05-25T08:41:51.893774+00:00_

**Round 5 审稿报告已投递至 Research Director。**

汇总结果：

**评分：3.0 / 5 (Findings)**（R1: 3.5, R2: 3.5, Director 综合: 3.0）

**3 个 Must-Fix：**
1. 因果排除链不完整——exposure bias 声称缺 KV cache drift + NTP magnitude imbalance 排除（R1+R2 强共识）
2. GAR 与下游仅 r²=0.04——核心指标解释 4% 方差，"Destroys" 叙事基础不稳
3. 缺 split-softmax/Rhea 实验对比——自己做了推理时干预却不与已发表方案比较

**7 个 Should-Fix：** β-steering 循环论证、单数据集、单种子、Llama 不完整、标题 overclaim、GAR-D 近零 artifact、SS+LoRA-only 消融缺失

Director 评分低于两位 Reviewer 0.5 分，理由：因果排除链和 GAR 有效性问题自 Round 1-2 起从未通过补充实验真正解决，每轮仅措辞微调。Issue Tracker 已同步更新至 Round 5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 40

## Round 40

6 recorded events


### User

_source line 457 · 2026-05-25T08:41:53.216869+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **R1-N1（GAR 弱相关）**：同意数据但建议降为 Should-Fix——GAR 作为诊断探针不需要强下游相关性，但标题暗示的危害与 r²=0.04 不匹配
- **R1-N2（因果排除不完整）**：完全同意，与我的 N1 强共识
- **R1-N3（单种子伪重复）**：反驳严重性——效应量 8-17× 远超种子方差，NLP 标准做法，建议降为 Should-Fix
- **R1-W1~W4**：均同意，其中 W3（缺 split-softmax 对比）我评级更高（Must-Fix）

两位 Reviewer 核心共识：因果声称需降级、缺关键对比实验、标题 overclaim。评分维持 3.5/5。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2

### 评分维持：Overall 3.5 / 5（Borderline Conference）

### Must-Fix 回应

**[AGREE] R2-N1 因果声称过强**: 与 R1-N2 一致。建议 "systematic diagnostic comparison" 替代 "causal exclusion"。但补充：逐对因素隔离设计本身是精良的，问题在于排除集不完备（KV cache drift + magnitude imbalance 未测试）。

**[AGREE with reservation] R2-N2 缺 split-softmax 对比**: 方向同意但不同意升级为 Must-Fix。论文定位为诊断性贡献，split-softmax 是推理时方案与 SS（训练时方案）不在同一层面竞争。建议在 Discussion 中定性讨论适用场景差异。

**[PARTIALLY AGREE] R2-N3 Llama 不完整**: 核心发现（gap + SS 有效）已完整复现。R2 关于 median vs mean metric inconsistency 的批评不成立——Llama 重尾分布（CoV>100%）使用 median 是统计合理选择，Table 7 同时报告 mean 和 median。建议措辞改为 "cross-architecture replication of the main finding, with partial replication of the exclusion chain"。

### Should-Fix 回应

**[AGREE] R2-W1 标题过强, [AGREE] R2-W2 单数据集**

**[REBUT] R2-W3 仅依赖 PPL**: 事实不符。论文含 instruction retention（Table 4, N=200, 18 constraint 类型, McNemar 检验）+ MMLU 5-shot（Table 17）+ PPL，三层评估。

**[PARTIALLY REBUT] R2-W4 N=50 偏小**: 对 8-17× 效应量，paired Wilcoxon N=50 足够（r=0.802）。真正问题是 R1-N3 的伪重复，而非样本量。

**[REBUT] R2-W5 "8-17×"循环论证**: 在不同语境引用同一数字是引用经验事实，非循环论证。

**[REBUT] R2-W6 无代码链接**: 事实错误。Abstract p.1 明确有 "data and code: https://anonymous.4open.science/r/turn-residual-gating"。

### 小问题
**[REBUT] R2-M3 Figure 1(b) log scale**: 事实错误。Caption 明确标注 "(log scale)"。

### R1-R2 共识
完全一致：因果声称过强、标题过强、单数据集
R1 独立发现：GAR 弱相关下游（N1, Must-Fix）、伪重复（N3, Must-Fix）、β-steering 循环论证（W1）
R2 事实错误：W6 代码链接、M3 log scale 标注

### 最终判断
两位 Reviewer 共识的 Must-Fix 核心问题是**因果声称需要弱化**。R1 额外认为 **GAR 与下游弱相关**（r=0.200）和**伪重复/单种子**是同等重要的 Must-Fix 问题。修改建议明确，作者在一个 resubmission cycle 内可完成。维持 3.5 评分。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **与 R2 一致**：因果声称过强（两人共同的 Must-Fix）、标题"Destroys"过强、单数据集限制
- **R1 独立发现的问题**：GAR 弱相关下游（r=0.200）、伪重复/单种子、β-steering 部分循环论证
- **纠正 R2 事实错误**：代码链接已在 Abstract 提供（R2-W6）、Figure 1(b) caption 已标注 log scale（R2-M3）、论文有 instruction retention + MMLU 评估而非仅 PPL（R2-W3）
- **评分维持 3.5/5**（Borderline Conference）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-25T08:45:52.606214+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "turn_residual_gating",
  "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review)\n# Round 4 (2026-05-25, fresh re-review)\n# Round 5 (2026-05-25, fresh re-review — current round)\n# Cross-response phase completed: R1↔R2 convergence reached\n# Post-cross correction: R1 identified 3 R2 factual errors (code link, log scale, eval layers)\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 5\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足 + AR 评估 N=5 过小\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立列为 Critical Must-Fix。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 维持 Must-Fix。R2 建议降 Should-Fix（效应量 8-17×）。Director 裁定 Should-Fix。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"D048: 6 条件 × 3 seeds from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"AR 评估扩大至 N=50 + bootstrap 95% CI + 条件间成对检验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件 + 显著性检验 + CI\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。R1 交叉回应确认 paired Wilcoxon N=50 对 8-17× 效应量足够（r=0.802）。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"额外问题：mean/median 未双报，AR/TF 样本量不匹配，attention spikes 未解释。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Should-Fix。R2 建议标题改为 'Cross-Model Replication'。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 部分同意 R2-N3 但反驳 median 批评：Llama 重尾分布 CoV>100% 使用 median 统计合理，Table 7 同时报告 mean 和 median。建议措辞 'cross-architecture replication of the main finding, with partial replication of the exclusion chain'。\"\n  action_items:\n    - round: 2\n      action: \"D048: 补充 Llama PCGrad+UG 训练+评估\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"写作降级：§5.5 标题→Cross-Model Replication + mean/median 双报\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2/3/4/5 未被独立提出。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"双种子差异大（GAR 0.318 vs 0.418）且策略不同。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047，SS 贡献 ~8.5× 提升。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 共识 SS 是压缩 TF-AR gap 主要贡献者。\"\n  action_items:\n    - round: 2\n      action: \"D048: SS 3-seed from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"3 seeds (s42/s123/s456) + mean±std；abstract/conclusion 弱化措辞\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2 — status updates through Round 5\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——contribution 措辞需调整\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"删除 'in principle applicable'。'first' → 'to our knowledge, the first'。\"\n    - round: 4\n      reviewers: [2]\n      note: \"'to our knowledge, the first' 仍被质疑。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"强共识。R1 建议 'systematic diagnostic comparison' 替代 'causal exclusion'，但肯定逐对隔离设计本身精良——问题在排除集不完备。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 4\n      action: \"删除 'to our knowledge, the first'，将 GAR 重新定位为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"'causal exclusion' → 'systematic diagnostic comparison'；讨论 KV cache drift + magnitude imbalance\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 过宽。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Director 裁定当前标题可接受。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"'Mechanistic' → 'Diagnostic'。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 共识 'Destroys' 与 r²=0.04 不匹配。\"\n  action_items:\n    - round: 2\n      action: \"标题改为 'Per-Layer Residual Gating'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"标题反映 exposure bias 发现；'Mechanistic' → 'Diagnostic'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"原文为 'Goal Accessibility Ratio'。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"arXiv 原文验证确认。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。待确认修复状态。\"\n  action_items:\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因——替代假说讨论不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 降 Should-Fix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"PCGrad 失败可能反映投影副作用（NTP magnitude 增长 7.5×-14.7×）。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 同意 R2-N1。R1 补充：排除集不完备（KV cache drift + magnitude imbalance 未测试），但肯定逐对因素隔离设计精良。两位 Reviewer 强共识。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"§6 扩展 exposure bias 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标——instruction retention 不显著但占页过多\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"McNemar p=0.077 不显著。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"占 Discussion 过多篇幅。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200, 95% CI ≈ [0.05, 0.35]（N=54）过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N1 Must-Fix，R2 同意数据但建议 diagnostic probe 重定位。R1 交叉回应纠正 R2-W3 事实错误：论文有 instruction retention（N=200, 18 categories, McNemar）+ MMLU 5-shot + PPL 三层评估，非仅 PPL。核心问题仍在：r²=0.04 弱。\"\n  action_items:\n    - round: 2\n      action: \"D048: N=200 扩容指令保持实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"提升已有显著数据至主文 + 重新定位 GAR 为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"orphan 条目。\"\n    - round: 2\n      reviewers: [2]\n      note: \"'and others' vs 完整作者列表不一致。\"\n    - round: 3\n      reviewers: [2]\n      note: \"grattafiori2024llama3 格式不一致。\"\n    - round: 4\n      reviewers: [2]\n      note: \"Raposo et al. 2024 → ICML 2024；Gromov et al. 年份一致性。\"\n    - round: 5\n      reviewers: [2]\n      note: \"R2-M3 继续指出 bib 格式问题。\"\n  action_items:\n    - round: 4\n      action: \"统一 bib 格式\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"Reproducibility 3.0/5。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意。\"\n    - round: 5\n      reviewers: [1]\n      note: \"R1 交叉回应纠正 R2-W6 事实错误：Abstract p.1 明确有匿名代码链接 https://anonymous.4open.science/r/turn-residual-gating。R2 此项声称不成立。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: done\n  resolution: \"Abstract p.1 已提供匿名代码/数据链接。R2 Round 5 W6 为事实错误，由 R1 纠正。\"\n  resolution_round: 5\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 AR 列需扩容\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现未在表格中呈现。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 列存在但仅 N=5。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M2: Table 1 AR 列缺 GAR-D 和 PPL。\"\n    - round: 5\n      reviewers: [1]\n      note: \"与 R1-N2 联动。\"\n  action_items:\n    - round: 4\n      action: \"AR 列更新为 N≥50 数据 + CI + GAR-D + PPL\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字重复 8+ 次\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 多章节重复。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"出现 8+ 次。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2 同意应去冗。\"\n    - round: 5\n      reviewers: [2]\n      note: \"仍存在。R1 交叉回应反驳 R2-W5：在不同语境引用同一数字是引用经验事实非循环论证，但同意适度去冗。\"\n  action_items:\n    - round: 4\n      action: \"Abstract/§4.2 保留完整数字，其余改用回指\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 泛化声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable' 未验证。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-N1。\"\n    - round: 5\n      reviewers: [2]\n      note: \"合并至 R2-N1 追踪。\"\n  action_items:\n    - round: 4\n      action: \"删除泛化声称，合并至 R2-N1\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. split-softmax 缺实验对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争方法。R1 认为超 scope。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2 维持观点。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 列 N2 Must-Fix，R1 明确反对升级（论文定位为诊断，split-softmax 为推理时方案不在同层面竞争）。R1 建议 Discussion 定性讨论。Director 裁定 Should-Fix（divergence 记录在报告中）。\"\n  action_items:\n    - round: 4\n      action: \"Related Work 加强理论论证 + Limitations 承认\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"Discussion 加定性对比 split-softmax/Rhea 适用场景差异\"\n      assigned_to: paper_agent\n      status: open\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure/Table caption overclaim + 重复句\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Figure caption 可能有 overclaim。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Figure 4 caption 重复句。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 3\n      action: \"修正 Fig 3b/Table 1/Fig 4 caption 的 overclaim + 删除 Fig 4 重复句\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后数字更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Abstract/Intro gap 数字需从单 seed 更新为 mean±std。\"\n    - round: 5\n      reviewers: []\n      note: \"仍待 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后统一更新\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"SS 3-seed variance 极大时需应急 framing。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 两 seed 差异 31%。\"\n    - round: 5\n      reviewers: []\n      note: \"SS 统计支撑仍为核心问题。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance\"\n      assigned_to: director\n      status: open\n\n# ============================================================\n# Issues from Round 3 — status updates through Round 5\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"约 8.4 页。Paper Agent 已压缩至 8.0 页。\"\n    - round: 4\n      reviewers: [1]\n      note: \"页数符合 8 页限制。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  resolution: \"Round 4 确认页数合规。\"\n  resolution_round: 4\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad scope 过度概括\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"'gradient conflict' 未加 'directional' 限定。\"\n    - round: 4\n      reviewers: []\n      note: \"PCGrad 失败可能反映投影副作用。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 同意 R2：NTP magnitude imbalance 7.5-14.7× 是 PCGrad 失败替代解释。\"\n  action_items:\n    - round: 3\n      action: \"'gradient conflict' → 'gradient direction conflict'；结论提及 magnitude imbalance 未排除\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869) 引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Rhea: Role-aware Heuristic Episodic Attention。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-W7-new 追踪。\"\n    - round: 5\n      reviewers: [2]\n      note: \"与 split-softmax 一并追踪。\"\n  action_items:\n    - round: 3\n      action: \"添加 bib 条目 + §2/§6 引用对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出，R2 反驳。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-Q4: LoRA rank 16 是否影响结论？\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1。\"\n  action_items:\n    - round: 4\n      action: \"§4.2 或 Limitations acknowledge LoRA rank 可能影响 gate 效用上界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"'NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)' 待确认。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"确认准确性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R3-NEW-1\"\n  summary: \"UG 描述不清——未说明仍为可学习 MLP\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"UG 描述仅说 'gates without turn embedding'。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"§4.1 或 §3 加一句说明\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-NEW-2\"\n  summary: \"Contribution (4) 混淆开发迭代与系统消融\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"'seven loss formulations and four training configurations' 混淆。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"拆分为 'loss design iterations (Appendix A)' + 'systematic conditions comparison (Table 1)'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Issues from Round 4 — status updates through Round 5\n# ============================================================\n\n- id: \"R4-N1\"\n  summary: \"GAR 指标与下游任务性能之间缺乏因果验证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200, r²=0.04。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix，R2 同意数据但建议降级。R1 交叉回应纠正 R2-W3 事实错误：论文有三层评估（instruction retention N=200 + MMLU 5-shot + PPL），非仅 PPL。核心问题仍在：r²=0.04。\"\n  action_items:\n    - round: 4\n      action: \"GAR 重定位为 diagnostic probe + 补充下游评估\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-N2\"\n  summary: \"SS+LoRA-only 消融缺失——ThreadGate 独立贡献不清\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。SS 贡献 ~8.5×。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 共识。关键缺失消融。\"\n  action_items:\n    - round: 4\n      action: \"需 SS+LoRA-only 实验，或明确承认 ThreadGate 贡献边际\"\n      assigned_to: agent\n      status: open\n\n- id: \"R4-W1\"\n  summary: \"GAR-D 全条件接近零——干预仅在 last token 成功\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"即使 TF 下 ThreadGate GAR-D = 0.02。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Table 1 所有条件 GAR-D ≈ 0.00-0.02。R2 同意。\"\n  action_items:\n    - round: 4\n      action: \"讨论 GAR-ours vs GAR-D 差异的含义\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W2\"\n  summary: \"Table 1 四舍五入与正文数字精度不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"§4.2 称 spread 0.75pp 但 Table 1 两位小数显示 1pp。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提及。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 增加一位小数，或正文使用与 table 一致的精度\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W3\"\n  summary: \"r_min 数值正文未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"r_min 数值在正文中未报告。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提及。\"\n  action_items:\n    - round: 4\n      action: \"在 §3 或 Appendix A 中报告 r_min 数值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-MR1\"\n  summary: \"缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"与 β-steering 思路相似。\"\n    - round: 5\n      reviewers: [2]\n      note: \"仍缺失。\"\n  action_items:\n    - round: 4\n      action: \"确认引用存在性并在 §2 引用对比\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W4\"\n  summary: \"Appendix C instruction retention 多重比较未校正\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"主实验有 Holm-Bonferroni（Appendix E），Appendix C 18-category 未校正。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 部分反驳 R1：主实验已有校正。共识：仅 Appendix C 需补。\"\n  action_items:\n    - round: 4\n      action: \"Appendix C per-category 分析补充 Holm-Bonferroni 或 FDR 校正\"\n      assigned_to: paper_agent\n      status: open\n\n# ============================================================\n# R2 factual errors identified by R1 in Round 5 cross-response\n# ============================================================\n\n- id: \"R5-ERRATA\"\n  summary: \"R2 Round 5 三处事实错误（由 R1 交叉回应纠正）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"R2-W6 称无代码链接——事实错误，Abstract p.1 有 anonymous.4open.science 链接。R2-M3 称 Figure 1(b) 缺 log scale 标注——事实错误，caption 已标注。R2-W3 称论文仅用 PPL 评估——事实错误，论文有 instruction retention (N=200) + MMLU 5-shot + PPL 三层评估。这些错误已从最终报告中剔除。\"\n  action_items: []\n  resolution: \"R1 交叉回应已纠正。不影响论文评估。\"\n  resolution_round: 5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "turn_residual_gating",
    "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review)\n# Round 4 (2026-05-25, fresh re-review)\n# Round 5 (2026-05-25, fresh re-review — current round)\n# Cross-response phase completed: R1↔R2 convergence reached\n# Post-cross correction: R1 identified 3 R2 factual errors (code link, log scale, eval layers)\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 5\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足 + AR 评估 N=5 过小\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立列为 Critical Must-Fix。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 维持 Must-Fix。R2 建议降 Should-Fix（效应量 8-17×）。Director 裁定 Should-Fix。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"D048: 6 条件 × 3 seeds from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"AR 评估扩大至 N=50 + bootstrap 95% CI + 条件间成对检验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件 + 显著性检验 + CI\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。R1 交叉回应确认 paired Wilcoxon N=50 对 8-17× 效应量足够（r=0.802）。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"额外问题：mean/median 未双报，AR/TF 样本量不匹配，attention spikes 未解释。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Should-Fix。R2 建议标题改为 'Cross-Model Replication'。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 部分同意 R2-N3 但反驳 median 批评：Llama 重尾分布 CoV>100% 使用 median 统计合理，Table 7 同时报告 mean 和 median。建议措辞 'cross-architecture replication of the main finding, with partial replication of the exclusion chain'。\"\n  action_items:\n    - round: 2\n      action: \"D048: 补充 Llama PCGrad+UG 训练+评估\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"写作降级：§5.5 标题→Cross-Model Replication + mean/median 双报\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2/3/4/5 未被独立提出。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"双种子差异大（GAR 0.318 vs 0.418）且策略不同。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047，SS 贡献 ~8.5× 提升。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 共识 SS 是压缩 TF-AR gap 主要贡献者。\"\n  action_items:\n    - round: 2\n      action: \"D048: SS 3-seed from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"3 seeds (s42/s123/s456) + mean±std；abstract/conclusion 弱化措辞\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2 — status updates through Round 5\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——contribution 措辞需调整\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"删除 'in principle applicable'。'first' → 'to our knowledge, the first'。\"\n    - round: 4\n      reviewers: [2]\n      note: \"'to our knowledge, the first' 仍被质疑。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"强共识。R1 建议 'systematic diagnostic comparison' 替代 'causal exclusion'，但肯定逐对隔离设计本身精良——问题在排除集不完备。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 4\n      action: \"删除 'to our knowledge, the first'，将 GAR 重新定位为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"'causal exclusion' → 'systematic diagnostic comparison'；讨论 KV cache drift + magnitude imbalance\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 过宽。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Director 裁定当前标题可接受。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"'Mechanistic' → 'Diagnostic'。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 共识 'Destroys' 与 r²=0.04 不匹配。\"\n  action_items:\n    - round: 2\n      action: \"标题改为 'Per-Layer Residual Gating'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"标题反映 exposure bias 发现；'Mechanistic' → 'Diagnostic'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"原文为 'Goal Accessibility Ratio'。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"arXiv 原文验证确认。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。待确认修复状态。\"\n  action_items:\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因——替代假说讨论不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 降 Should-Fix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"PCGrad 失败可能反映投影副作用（NTP magnitude 增长 7.5×-14.7×）。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 同意 R2-N1。R1 补充：排除集不完备（KV cache drift + magnitude imbalance 未测试），但肯定逐对因素隔离设计精良。两位 Reviewer 强共识。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"§6 扩展 exposure bias 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标——instruction retention 不显著但占页过多\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"McNemar p=0.077 不显著。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"占 Discussion 过多篇幅。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200, 95% CI ≈ [0.05, 0.35]（N=54）过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N1 Must-Fix，R2 同意数据但建议 diagnostic probe 重定位。R1 交叉回应纠正 R2-W3 事实错误：论文有 instruction retention（N=200, 18 categories, McNemar）+ MMLU 5-shot + PPL 三层评估，非仅 PPL。核心问题仍在：r²=0.04 弱。\"\n  action_items:\n    - round: 2\n      action: \"D048: N=200 扩容指令保持实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"提升已有显著数据至主文 + 重新定位 GAR 为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"orphan 条目。\"\n    - round: 2\n      reviewers: [2]\n      note: \"'and others' vs 完整作者列表不一致。\"\n    - round: 3\n      reviewers: [2]\n      note: \"grattafiori2024llama3 格式不一致。\"\n    - round: 4\n      reviewers: [2]\n      note: \"Raposo et al. 2024 → ICML 2024；Gromov et al. 年份一致性。\"\n    - round: 5\n      reviewers: [2]\n      note: \"R2-M3 继续指出 bib 格式问题。\"\n  action_items:\n    - round: 4\n      action: \"统一 bib 格式\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"Reproducibility 3.0/5。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"交叉回应 R2 同意。\"\n    - round: 5\n      reviewers: [1]\n      note: \"R1 交叉回应纠正 R2-W6 事实错误：Abstract p.1 明确有匿名代码链接 https://anonymous.4open.science/r/turn-residual-gating。R2 此项声称不成立。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: done\n  resolution: \"Abstract p.1 已提供匿名代码/数据链接。R2 Round 5 W6 为事实错误，由 R1 纠正。\"\n  resolution_round: 5\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 AR 列需扩容\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现未在表格中呈现。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 列存在但仅 N=5。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M2: Table 1 AR 列缺 GAR-D 和 PPL。\"\n    - round: 5\n      reviewers: [1]\n      note: \"与 R1-N2 联动。\"\n  action_items:\n    - round: 4\n      action: \"AR 列更新为 N≥50 数据 + CI + GAR-D + PPL\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字重复 8+ 次\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 多章节重复。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"出现 8+ 次。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2 同意应去冗。\"\n    - round: 5\n      reviewers: [2]\n      note: \"仍存在。R1 交叉回应反驳 R2-W5：在不同语境引用同一数字是引用经验事实非循环论证，但同意适度去冗。\"\n  action_items:\n    - round: 4\n      action: \"Abstract/§4.2 保留完整数字，其余改用回指\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 泛化声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable' 未验证。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-N1。\"\n    - round: 5\n      reviewers: [2]\n      note: \"合并至 R2-N1 追踪。\"\n  action_items:\n    - round: 4\n      action: \"删除泛化声称，合并至 R2-N1\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. split-softmax 缺实验对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争方法。R1 认为超 scope。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2 维持观点。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 列 N2 Must-Fix，R1 明确反对升级（论文定位为诊断，split-softmax 为推理时方案不在同层面竞争）。R1 建议 Discussion 定性讨论。Director 裁定 Should-Fix（divergence 记录在报告中）。\"\n  action_items:\n    - round: 4\n      action: \"Related Work 加强理论论证 + Limitations 承认\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"Discussion 加定性对比 split-softmax/Rhea 适用场景差异\"\n      assigned_to: paper_agent\n      status: open\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure/Table caption overclaim + 重复句\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Figure caption 可能有 overclaim。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Figure 4 caption 重复句。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 3\n      action: \"修正 Fig 3b/Table 1/Fig 4 caption 的 overclaim + 删除 Fig 4 重复句\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后数字更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Abstract/Intro gap 数字需从单 seed 更新为 mean±std。\"\n    - round: 5\n      reviewers: []\n      note: \"仍待 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后统一更新\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"SS 3-seed variance 极大时需应急 framing。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 两 seed 差异 31%。\"\n    - round: 5\n      reviewers: []\n      note: \"SS 统计支撑仍为核心问题。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance\"\n      assigned_to: director\n      status: open\n\n# ============================================================\n# Issues from Round 3 — status updates through Round 5\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"约 8.4 页。Paper Agent 已压缩至 8.0 页。\"\n    - round: 4\n      reviewers: [1]\n      note: \"页数符合 8 页限制。\"\n    - round: 5\n      reviewers: []\n      note: \"维持 resolved。\"\n  resolution: \"Round 4 确认页数合规。\"\n  resolution_round: 4\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad scope 过度概括\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"'gradient conflict' 未加 'directional' 限定。\"\n    - round: 4\n      reviewers: []\n      note: \"PCGrad 失败可能反映投影副作用。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 同意 R2：NTP magnitude imbalance 7.5-14.7× 是 PCGrad 失败替代解释。\"\n  action_items:\n    - round: 3\n      action: \"'gradient conflict' → 'gradient direction conflict'；结论提及 magnitude imbalance 未排除\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869) 引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Rhea: Role-aware Heuristic Episodic Attention。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-W7-new 追踪。\"\n    - round: 5\n      reviewers: [2]\n      note: \"与 split-softmax 一并追踪。\"\n  action_items:\n    - round: 3\n      action: \"添加 bib 条目 + §2/§6 引用对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出，R2 反驳。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-Q4: LoRA rank 16 是否影响结论？\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1。\"\n  action_items:\n    - round: 4\n      action: \"§4.2 或 Limitations acknowledge LoRA rank 可能影响 gate 效用上界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"'NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)' 待确认。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"确认准确性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R3-NEW-1\"\n  summary: \"UG 描述不清——未说明仍为可学习 MLP\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"UG 描述仅说 'gates without turn embedding'。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"§4.1 或 §3 加一句说明\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-NEW-2\"\n  summary: \"Contribution (4) 混淆开发迭代与系统消融\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"'seven loss formulations and four training configurations' 混淆。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"拆分为 'loss design iterations (Appendix A)' + 'systematic conditions comparison (Table 1)'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Issues from Round 4 — status updates through Round 5\n# ============================================================\n\n- id: \"R4-N1\"\n  summary: \"GAR 指标与下游任务性能之间缺乏因果验证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200, r²=0.04。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix，R2 同意数据但建议降级。R1 交叉回应纠正 R2-W3 事实错误：论文有三层评估（instruction retention N=200 + MMLU 5-shot + PPL），非仅 PPL。核心问题仍在：r²=0.04。\"\n  action_items:\n    - round: 4\n      action: \"GAR 重定位为 diagnostic probe + 补充下游评估\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-N2\"\n  summary: \"SS+LoRA-only 消融缺失——ThreadGate 独立贡献不清\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。SS 贡献 ~8.5×。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 共识。关键缺失消融。\"\n  action_items:\n    - round: 4\n      action: \"需 SS+LoRA-only 实验，或明确承认 ThreadGate 贡献边际\"\n      assigned_to: agent\n      status: open\n\n- id: \"R4-W1\"\n  summary: \"GAR-D 全条件接近零——干预仅在 last token 成功\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"即使 TF 下 ThreadGate GAR-D = 0.02。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Table 1 所有条件 GAR-D ≈ 0.00-0.02。R2 同意。\"\n  action_items:\n    - round: 4\n      action: \"讨论 GAR-ours vs GAR-D 差异的含义\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W2\"\n  summary: \"Table 1 四舍五入与正文数字精度不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"§4.2 称 spread 0.75pp 但 Table 1 两位小数显示 1pp。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提及。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 增加一位小数，或正文使用与 table 一致的精度\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W3\"\n  summary: \"r_min 数值正文未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"r_min 数值在正文中未报告。\"\n    - round: 5\n      reviewers: []\n      note: \"本轮未独立提及。\"\n  action_items:\n    - round: 4\n      action: \"在 §3 或 Appendix A 中报告 r_min 数值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-MR1\"\n  summary: \"缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"与 β-steering 思路相似。\"\n    - round: 5\n      reviewers: [2]\n      note: \"仍缺失。\"\n  action_items:\n    - round: 4\n      action: \"确认引用存在性并在 §2 引用对比\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W4\"\n  summary: \"Appendix C instruction retention 多重比较未校正\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"主实验有 Holm-Bonferroni（Appendix E），Appendix C 18-category 未校正。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 部分反驳 R1：主实验已有校正。共识：仅 Appendix C 需补。\"\n  action_items:\n    - round: 4\n      action: \"Appendix C per-category 分析补充 Holm-Bonferroni 或 FDR 校正\"\n      assigned_to: paper_agent\n      status: open\n\n# ============================================================\n# R2 factual errors identified by R1 in Round 5 cross-response\n# ============================================================\n\n- id: \"R5-ERRATA\"\n  summary: \"R2 Round 5 三处事实错误（由 R1 交叉回应纠正）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"R2-W6 称无代码链接——事实错误，Abstract p.1 有 anonymous.4open.science 链接。R2-M3 称 Figure 1(b) 缺 log scale 标注——事实错误，caption 已标注。R2-W3 称论文仅用 PPL 评估——事实错误，论文有 instruction retention (N=200) + MMLU 5-shot + PPL 三层评估。这些错误已从最终报告中剔除。\"\n  action_items: []\n  resolution: \"R1 交叉回应已纠正。不影响论文评估。\"\n  resolution_round: 5"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-25T08:45:52.757918+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml\", \"bytes\": 25992}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-25T08:48:24.453058+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 5 (Fresh Re-Review) [修正版]\n\n**论文**: Turn-Residual Gating for Multi-Turn LLMs\n**目标 Venue**: EMNLP 2026 (via ARR)\n**审稿日期**: 2026-05-25\n**Reviewer**: R1 (方法严谨性) + R2 (新颖性/完整性)\n**模式**: 圆桌审稿 Round 1，交叉回应后收敛\n**修正说明**: R1 交叉回应纠正了 R2 三处事实错误（代码链接已存在、Figure 1(b) 已标注 log scale、论文有三层评估非仅 PPL），影响 MF3→SF 降级及代码发布 issue 解决\n\n---\n\n## Summary\n\n本文研究 per-layer residual gating (ThreadGate) 能否缓解多轮 LLM 在自回归解码中的 per-turn grounding 损失。通过 Qwen2.5-7B + ShareGPT 上五种训练条件（Base, ThreadGate, TG+PCGrad, Uniform Gate, LoRA-only）的系统对比，论文报告所有 gating 变体均无法弥合 teacher-forcing 与 autoregressive 模式下 20-33× 的 GAR 差距，将此归因于 exposure bias 而非 gradient conflict。Llama-3.1-8B 上仅 3/5 条件的跨模型复制部分支持该发现。诊断性 β-steering 干预可部分恢复 GAR 但下游改善微弱（p=0.077）。\n\n---\n\n## Strengths\n\n**S1. 系统的五路条件对比**\nBase / ThreadGate / TG+PCGrad / Uniform Gate / LoRA-only 覆盖从无干预到 gradient conflict 缓解的合理消融范围。逐对因素隔离设计精良（R1 肯定），实验逻辑清晰。\n\n**S2. 有价值的负面结果**\n证明 lightweight per-layer gating 无法解决 TF-AR grounding gap，对社区有实际意义——避免后续研究重复尝试类似方案。\n\n**S3. Exposure bias 假说具启发性**\n将 multi-turn grounding 失败从架构层面转向训练范式层面（exposure bias），为社区提供新研究方向。SS 条件下 GAR 改善约 8.5× 间接支持这一假说。\n\n**S4. β-steering 诊断工具**\n推理时注意力操控作为诊断手段具有方法论创新性，为理解 LLM 内部 attention dynamics 提供可复用工具。\n\n**S5. 多层评估 + 丰富附录**\n主文包含 instruction retention（N=200, 18 constraint categories, McNemar 检验）+ MMLU 5-shot + PPL 三层评估。35 页附录覆盖 v1-v7 loss iterations、gate value distributions、per-turn breakdowns、bootstrap CIs 等。代码和数据已通过匿名链接提供。\n\n---\n\n## Weaknesses\n\n### Must-Fix (阻碍接收的关键问题)\n\n**MF1. 因果排除链不完整——exposure bias 声称过强** [R1-N2 + R2-N1, 强共识]\n\n论文将 exposure bias 定位为 TF-AR gap 的根因，但因果排除链存在关键缺口：\n- **KV cache drift 未排除**：TF 使用 ground-truth prefix，AR 使用模型生成 prefix，两者 KV cache 内容本质不同。§7 Limitations 自己承认未排除这一混淆变量。\n- **NTP magnitude imbalance**：§5.2 显示 NTP loss magnitude 碾压 GAR loss 7.5-14.7×。PCGrad 仅消除方向冲突（cosine < 0），不处理量级碾压——PCGrad 失败可能反映投影副作用而非 gradient direction conflict 不存在。\n- **Appendix L 非独立验证**：gradient cosine 数据在 PCGrad 条件下获得，不能作为 exposure bias 假说的独立证据。\n- R1 建议将 \"causal exclusion\" 重新定位为 \"systematic diagnostic comparison\"——肯定设计精良但排除集不完备。\n\n**MF2. GAR 指标与下游任务弱相关——核心叙事基础不稳** [R1-N1 Must-Fix, R2 同意数据但建议降级]\n\nTable 4 / §6 显示 GAR 与 instruction retention rate：r ≈ 0.200, r² = 0.04（N=54 paired samples, 95% CI ≈ [0.05, 0.35]）。\n- 标题 \"Destroys\" 暗示 catastrophic downstream impact，但 GAR 仅解释 4% 下游方差\n- CI 跨越近零，统计说服力不足\n- R2 建议重新定位 GAR 为 diagnostic probe 可部分缓解，但即使作为 diagnostic probe，4% 解释方差仍质疑其诊断价值\n- 建议补充至少一个 established 下游评估（如 MT-Bench multi-turn subset）建立 GAR 与实际性能的桥梁\n\n### Should-Fix (影响论文质量但不直接阻碍接收)\n\n**SF1. β-steering 部分循环论证** [R1-W1, R2 同意]\nβ-steering boost attention → GAR（attention metric）recovers 是同义反复。非循环部分（下游 instruction retention +11.1pp）的 McNemar p=0.077 未达 α=0.05 显著水平。论文应解耦 GAR 恢复（自明）与下游改善（需独立统计支撑）两个声称。\n\n**SF2. 单数据集 + 单模型为主** [R1-W2 + R2-W2, 一致]\n核心实验仅在 ShareGPT（8K conversations）+ Qwen2.5-7B 上完成。Llama 跨模型复制仅覆盖 3/5 条件。对 \"general phenomenon\" 的泛化声称缺乏数据集多样性支撑。\n\n**SF3. 单种子伪重复** [R1-N3 Must-Fix, R2 建议降级, Director 裁定 Should-Fix]\nTable 1 中 Base/PCGrad/UG 为单种子。ThreadGate 有 2-3 种子（Appendix T），SS 有 2 种子但协议不同不可比。\n- R2 反驳降级理由：效应量 8-17× 远超种子间方差（AR GAR seed 42: 0.064 vs seed 123: 0.055），Bootstrap CI 部分缓解\n- R1 反驳 R2-W4：N=50 下 paired Wilcoxon 对 8-17× 效应量足够（r=0.802），真正问题是 training variance 而非 eval 样本量\n- Director 裁定 Should-Fix：效应量大，但 training variance 完全未覆盖仍是方法论遗憾\n\n**SF4. Llama 跨模型验证不完整** [R2-N3 Must-Fix, R1 部分同意, Director 裁定 Should-Fix]\n仅 3/5 条件（Base, TG, LoRA-only），缺 PCGrad 和 Uniform Gate。\n- R1 部分反驳 R2：核心发现（gap + SS 有效）已完整复现；Llama 重尾分布（CoV>100%）使用 median 统计合理；Table 7 同时报告 mean 和 median（R2 关于 metric inconsistency 的批评不成立）\n- R1 建议措辞：\"cross-architecture replication of the main finding, with partial replication of the exclusion chain\"\n- Director 裁定 Should-Fix：3/5 条件削弱完整排除，但核心发现复制成功\n\n**SF5. 标题 overclaim** [R2-W1, R1 同意]\n\"Destroys\" 暗示 catastrophic downstream failure，但 GAR collapse 仅解释 4% 下游方差。当前标题与证据强度不匹配。\n\n**SF6. GAR-Dongre 全条件接近零——度量选择讨论不充分** [R1-W4, R2 同意]\nTable 1 所有条件 GAR-D ≈ 0.00-0.02（包括 TF 下 ThreadGate 也仅 0.02）。§3.1 对选择 GAR-ours 而非 Dongre 原始定义的讨论不充分。\n\n**SF7. SS+LoRA-only 消融缺失** [R1-W1 + R2 交叉共识]\nSS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。SS 贡献 ~8.5× 提升 vs ThreadGate ~2.6×。如果 SS+LoRA-only（无 gating 架构）达到相似水平，ThreadGate 的架构贡献将大幅降低。关键缺失消融。\n\n**SF8. 缺少推理时方案对比** [R2-N2 Must-Fix, R1 Should-Fix, Director 裁定 Should-Fix — divergence]\nβ-steering 已证明推理时注意力干预可恢复 GAR，但论文未与已发表的推理时方案做实验对比（Li et al. 2024 split-softmax, Rhea）。\n- R2 认为 Must-Fix：诊断论文不与最直接替代方案对比是完整性缺陷\n- R1 明确反对升级：论文定位为诊断性贡献，split-softmax 是推理时解决方案，不在同一层面竞争。建议 Discussion 中定性讨论适用场景差异即可。\n- Director 裁定 Should-Fix：R1 的 scope 论证有理——诊断论文不必做方案对比实验，但 Discussion 中应有定性讨论\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 定级 | R2 定级 | Director 裁定 |\n|------|---------|---------|---------------|\n| 因果排除链不完整 | N2 Must-Fix | N1 Must-Fix | **Must-Fix** (强共识) |\n| GAR 弱下游相关 r²=0.04 | N1 Must-Fix | Should-Fix | **Must-Fix** (4% 不足以支撑核心叙事) |\n| 缺 split-softmax/Rhea 对比 | W3 Should-Fix | N2 Must-Fix | **Should-Fix** (见 Divergence) |\n| β-steering 循环论证 | W1 Should-Fix | 同意 | **Should-Fix** |\n| 单数据集 | W2 Should-Fix | W2 Should-Fix | **Should-Fix** |\n| 单种子伪重复 | N3 Must-Fix | Should-Fix | **Should-Fix** (效应量大) |\n| Llama 不完整 | 部分同意 | N3 Must-Fix | **Should-Fix** (核心发现已复制) |\n| 标题 overclaim | 同意 | W1 Should-Fix | **Should-Fix** |\n| GAR-D 近零 artifact | W4 Should-Fix | 同意 | **Should-Fix** |\n| SS+LoRA-only 消融缺失 | W1 | 同意 | **Should-Fix** |\n\n---\n\n## Reviewer Divergence\n\n**1. GAR 弱相关的严重性**\n- R1 视为 Must-Fix：核心指标不可靠，论文基础动摇\n- R2 视为 Should-Fix：若重定位 GAR 为 diagnostic probe，弱下游相关可接受\n- **Director 裁定 Must-Fix**：即使作为 diagnostic probe，4% 解释方差也严重削弱论文叙事说服力\n\n**2. 单种子的严重性**\n- R1 视为 Must-Fix：training variance 完全未覆盖\n- R2 认为效应量 8-17× 足以缓解；R1 确认 eval 样本量（N=50, r=0.802）足够\n- **Director 裁定 Should-Fix**：效应量确实远超 seed noise，但 training variance 仍是遗憾\n\n**3. Split-softmax 对比的严重性**\n- R2 视为 Must-Fix：β-steering 已开推理时干预先河，不对比不合理\n- R1 明确反对升级：论文定位为诊断，split-softmax 为推理时方案不在同层面竞争，Discussion 定性讨论即可\n- **Director 裁定 Should-Fix**：R1 的 scope 论证成立——诊断论文核心贡献是发现问题而非提出解决方案，但 Discussion 应讨论\n\n**4. Llama median vs mean**\n- R2 批评 median 使用有 metric selection 之嫌\n- R1 反驳：Llama 重尾分布 CoV>100%，median 是统计合理选择；Table 7 已双报\n- **Director 裁定**：R1 反驳有理，R2 此项批评不成立\n\n---\n\n## R2 事实错误（由 R1 交叉回应纠正）\n\n| R2 声称 | R1 纠正 | 影响 |\n|---------|---------|------|\n| R2-W6: 无代码/数据链接 | Abstract p.1 有 anonymous.4open.science/r/turn-residual-gating | 该 weakness 撤销 |\n| R2-M3: Figure 1(b) 缺 log scale 标注 | Caption 已明确标注 \"(log scale)\" | 该 minor 撤销 |\n| R2-W3: 仅用 PPL 评估 | 论文有 instruction retention (N=200, 18 categories, McNemar) + MMLU 5-shot + PPL 三层评估 | 评估完整性无问题，但 r²=0.04 弱相关问题仍在 |\n\n---\n\n## Questions\n\nQ1. 如果 GAR 与下游 instruction retention 仅 r²=0.04，为什么 GAR 是论文的核心指标？有没有更好的 grounding proxy metric？\n\nQ2. SS 贡献 ~8.5× vs ThreadGate ~2.6×，如果进一步做 SS+LoRA-only 消融，ThreadGate 的独立架构价值还有多少？\n\nQ3. KV cache drift 是否是 TF-AR gap 的另一个 confound？可以设计什么实验排除？（如 AR decoding with oracle-prefix injection）\n\nQ4. LoRA rank 16 是否可能限制了 gate 效用上界？在更高 rank（32/64）下是否会有不同结论？\n\nQ5. GAR-ours 与 GAR-Dongre 的巨大差异（~0.5 vs ~0.01）的根因是什么？这是否意味着 Dongre 原始定义在 multi-turn 场景下更鲁棒？\n\n---\n\n## Missing References\n\n- **Li et al. 2024** — split-softmax：推理时 multi-turn attention 解决方案，需 §2/Discussion 讨论 [R1, R2 共识]\n- **Rhea (arXiv:2512.06869)** — Role-aware Heuristic Episodic Attention [R1, R2 共识]\n- **Zhang et al. 2024** \"Tell Your Model Where to Attend\" — 推理时注意力操控方法 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**\n\n---\n\n## Visual Layout Check (非评分项)\n\n**状态：已完成** (耗时 ~4 分钟，0 critical / 0 warning / 8 info)\n\n主要发现：\n- **Page 1**：首页无 display item，Figure 1 在 page 2（可接受但非最优）\n- **Page 4**：Figure 2 偏小，legend 文字在打印尺寸下可能偏小\n- **Page 6**：Figure 4 五种柱状颜色灰度打印可区分度下降，建议添加 hatching pattern\n- **Page 8**：Figure 6(a) 标签密集，图内数值标注字号偏小（建议 ≥8pt）\n- **Pages 19-20**：附录图表密集排列，单图尺寸偏小\n- **全文配色**：红/蓝双色主调，饱和度适中，色盲友好，语义连贯性好\n\n整体排版质量可接受，无影响审稿印象的严重问题。\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | Director |\n|------|-----|-----|----------|\n| Overall | 3.5 | 3.5 | **3.0** |\n\n**Director 综合评分：3.0 / 5 (Findings)**\n\n**置信度：4/5 (High)**\n\n### 评分理由\n\n本文呈现了一个有价值的负面结果——lightweight per-layer gating 无法弥合多轮 LLM 的 TF-AR grounding gap——并提出 exposure bias 作为解释假说。系统的五路条件对比（R1 肯定设计精良）和 β-steering 诊断工具是亮点。评估体系完善（instruction retention + MMLU + PPL 三层），代码/数据已匿名发布。\n\n**2 个 Must-Fix 问题限制接收前景：**\n1. **因果声称过强**（强共识）：exposure bias 归因缺少对 KV cache drift 和 NTP magnitude imbalance 的排除，\"root cause\" 声称站不住——R1 建议重新定位为 \"systematic diagnostic comparison\"\n2. **核心指标薄弱**：GAR 与下游仅 r²=0.04，\"Destroys\" 叙事的基础不稳\n\n这两个问题分别涉及方法论（因果推断）和指标有效性，需要实验补充（排除实验 + 下游评估），非纯写作修改可解决。\n\n**8 个 Should-Fix 问题**可在一个 resubmission cycle 内完成修改（R1 明确确认）。\n\n**Director 评分低于两位 Reviewer 0.5 分的理由：**\n因果排除链（Round 2 首次提出）和 GAR 有效性（Round 1 首次提出）跨 5 轮审稿从未被真正解决——每轮只是措辞微调而非补充排除实验。持续未解决的核心问题降低论文在审稿周期内可修复的信心。\n\n**升级路径（→ 3.5 Borderline Conference）：**\n(a) 将 GAR 明确重定位为 diagnostic probe + 补充至少一个 established 下游评估\n(b) 将 exposure bias 降级为 \"a proximal cause consistent with evidence\" 并充分讨论替代假说（KV cache drift, magnitude imbalance）\n(c) 补充 SS+LoRA-only 消融以明确 ThreadGate 独立贡献\n(d) Discussion 中定性讨论 split-softmax/Rhea 适用场景差异\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Destroys\" 标题词与 r²=0.04 不匹配，需降调\n- Contribution (1) \"to our knowledge, the first\" 仍被 R2 质疑\n\n### §3 Method / GAR Definition\n- r_min 数值在正文中未报告（仅 Appendix），影响可复现性 [R1-M1]\n- GAR-ours vs GAR-Dongre 选择理由不充分——GAR-D 全条件 ≈ 0.00-0.02，论文未解释为何弃用原始定义\n- UG 描述需明确仍为可学习 MLP\n\n### §4 Results\n- Table 1 AR 列仍仅 N=5，需扩容至 N≥50 + CI + GAR-D + PPL\n- 数字精度不一致：§4.2 称 spread 0.75pp 但 Table 1 两位小数显示 1pp\n- \"20-33× gap\" 重复 8+ 次——Abstract/§4.2 保留完整数字，其余用回指\n\n### §5 Analysis\n- PCGrad 失败分析需限定 scope：\"gradient direction conflict\" 而非泛化的 \"gradient conflict\"。NTP magnitude imbalance 7.5-14.7× 是替代解释，必须讨论\n- β-steering GAR 恢复是同义反复，需与下游效果解耦报告\n- §5.5 Llama：R1 确认 median 使用合理（CoV>100%），Table 7 已双报——建议正文明确说明选择理由。标题改为 \"Cross-Model Replication\"\n\n### §6 Discussion\n- Exposure bias 归因需降级措辞\n- Instruction retention McNemar p=0.077 未达显著\n- 需定性讨论 split-softmax / Rhea 适用场景差异（R1 建议）\n\n### §7 Limitations\n- KV cache drift 已提及但未设计排除实验\n- LoRA rank capacity saturation 未讨论\n\n### Appendix\n- Appendix C per-category McNemar's test（18 categories）未做 FDR/Bonferroni 校正——主实验已有 Holm-Bonferroni（Appendix E p30），但 Appendix C 漏掉了\n- Bib 格式仍有不一致：Raposo et al. 缺 ICML 2024 venue、Gromov et al. 年份问题\n- liu2016attention 引用可能错配（语音识别 vs 注意力引导），需确认",
  "project": "turn_residual_gating",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 5 (Fresh Re-Review) [修正版]\n\n**论文**: Turn-Residual Gating for Multi-Turn LLMs\n**目标 Venue**: EMNLP 2026 (via ARR)\n**审稿日期**: 2026-05-25\n**Reviewer**: R1 (方法严谨性) + R2 (新颖性/完整性)\n**模式**: 圆桌审稿 Round 1，交叉回应后收敛\n**修正说明**: R1 交叉回应纠正了 R2 三处事实错误（代码链接已存在、Figure 1(b) 已标注 log scale、论文有三层评估非仅 PPL），影响 MF3→SF 降级及代码发布 issue 解决\n\n---\n\n## Summary\n\n本文研究 per-layer residual gating (ThreadGate) 能否缓解多轮 LLM 在自回归解码中的 per-turn grounding 损失。通过 Qwen2.5-7B + ShareGPT 上五种训练条件（Base, ThreadGate, TG+PCGrad, Uniform Gate, LoRA-only）的系统对比，论文报告所有 gating 变体均无法弥合 teacher-forcing 与 autoregressive 模式下 20-33× 的 GAR 差距，将此归因于 exposure bias 而非 gradient conflict。Llama-3.1-8B 上仅 3/5 条件的跨模型复制部分支持该发现。诊断性 β-steering 干预可部分恢复 GAR 但下游改善微弱（p=0.077）。\n\n---\n\n## Strengths\n\n**S1. 系统的五路条件对比**\nBase / ThreadGate / TG+PCGrad / Uniform Gate / LoRA-only 覆盖从无干预到 gradient conflict 缓解的合理消融范围。逐对因素隔离设计精良（R1 肯定），实验逻辑清晰。\n\n**S2. 有价值的负面结果**\n证明 lightweight per-layer gating 无法解决 TF-AR grounding gap，对社区有实际意义——避免后续研究重复尝试类似方案。\n\n**S3. Exposure bias 假说具启发性**\n将 multi-turn grounding 失败从架构层面转向训练范式层面（exposure bias），为社区提供新研究方向。SS 条件下 GAR 改善约 8.5× 间接支持这一假说。\n\n**S4. β-steering 诊断工具**\n推理时注意力操控作为诊断手段具有方法论创新性，为理解 LLM 内部 attention dynamics 提供可复用工具。\n\n**S5. 多层评估 + 丰富附录**\n主文包含 instruction retention（N=200, 18 constraint categories, McNemar 检验）+ MMLU 5-shot + PPL 三层评估。35 页附录覆盖 v1-v7 loss iterations、gate value distributions、per-turn breakdowns、bootstrap CIs 等。代码和数据已通过匿名链接提供。\n\n---\n\n## Weaknesses\n\n### Must-Fix (阻碍接收的关键问题)\n\n**MF1. 因果排除链不完整——exposure bias 声称过强** [R1-N2 + R2-N1, 强共识]\n\n论文将 exposure bias 定位为 TF-AR gap 的根因，但因果排除链存在关键缺口：\n- **KV cache drift 未排除**：TF 使用 ground-truth prefix，AR 使用模型生成 prefix，两者 KV cache 内容本质不同。§7 Limitations 自己承认未排除这一混淆变量。\n- **NTP magnitude imbalance**：§5.2 显示 NTP loss magnitude 碾压 GAR loss 7.5-14.7×。PCGrad 仅消除方向冲突（cosine < 0），不处理量级碾压——PCGrad 失败可能反映投影副作用而非 gradient direction conflict 不存在。\n- **Appendix L 非独立验证**：gradient cosine 数据在 PCGrad 条件下获得，不能作为 exposure bias 假说的独立证据。\n- R1 建议将 \"causal exclusion\" 重新定位为 \"systematic diagnostic comparison\"——肯定设计精良但排除集不完备。\n\n**MF2. GAR 指标与下游任务弱相关——核心叙事基础不稳** [R1-N1 Must-Fix, R2 同意数据但建议降级]\n\nTable 4 / §6 显示 GAR 与 instruction retention rate：r ≈ 0.200, r² = 0.04（N=54 paired samples, 95% CI ≈ [0.05, 0.35]）。\n- 标题 \"Destroys\" 暗示 catastrophic downstream impact，但 GAR 仅解释 4% 下游方差\n- CI 跨越近零，统计说服力不足\n- R2 建议重新定位 GAR 为 diagnostic probe 可部分缓解，但即使作为 diagnostic probe，4% 解释方差仍质疑其诊断价值\n- 建议补充至少一个 established 下游评估（如 MT-Bench multi-turn subset）建立 GAR 与实际性能的桥梁\n\n### Should-Fix (影响论文质量但不直接阻碍接收)\n\n**SF1. β-steering 部分循环论证** [R1-W1, R2 同意]\nβ-steering boost attention → GAR（attention metric）recovers 是同义反复。非循环部分（下游 instruction retention +11.1pp）的 McNemar p=0.077 未达 α=0.05 显著水平。论文应解耦 GAR 恢复（自明）与下游改善（需独立统计支撑）两个声称。\n\n**SF2. 单数据集 + 单模型为主** [R1-W2 + R2-W2, 一致]\n核心实验仅在 ShareGPT（8K conversations）+ Qwen2.5-7B 上完成。Llama 跨模型复制仅覆盖 3/5 条件。对 \"general phenomenon\" 的泛化声称缺乏数据集多样性支撑。\n\n**SF3. 单种子伪重复** [R1-N3 Must-Fix, R2 建议降级, Director 裁定 Should-Fix]\nTable 1 中 Base/PCGrad/UG 为单种子。ThreadGate 有 2-3 种子（Appendix T），SS 有 2 种子但协议不同不可比。\n- R2 反驳降级理由：效应量 8-17× 远超种子间方差（AR GAR seed 42: 0.064 vs seed 123: 0.055），Bootstrap CI 部分缓解\n- R1 反驳 R2-W4：N=50 下 paired Wilcoxon 对 8-17× 效应量足够（r=0.802），真正问题是 training variance 而非 eval 样本量\n- Director 裁定 Should-Fix：效应量大，但 training variance 完全未覆盖仍是方法论遗憾\n\n**SF4. Llama 跨模型验证不完整** [R2-N3 Must-Fix, R1 部分同意, Director 裁定 Should-Fix]\n仅 3/5 条件（Base, TG, LoRA-only），缺 PCGrad 和 Uniform Gate。\n- R1 部分反驳 R2：核心发现（gap + SS 有效）已完整复现；Llama 重尾分布（CoV>100%）使用 median 统计合理；Table 7 同时报告 mean 和 median（R2 关于 metric inconsistency 的批评不成立）\n- R1 建议措辞：\"cross-architecture replication of the main finding, with partial replication of the exclusion chain\"\n- Director 裁定 Should-Fix：3/5 条件削弱完整排除，但核心发现复制成功\n\n**SF5. 标题 overclaim** [R2-W1, R1 同意]\n\"Destroys\" 暗示 catastrophic downstream failure，但 GAR collapse 仅解释 4% 下游方差。当前标题与证据强度不匹配。\n\n**SF6. GAR-Dongre 全条件接近零——度量选择讨论不充分** [R1-W4, R2 同意]\nTable 1 所有条件 GAR-D ≈ 0.00-0.02（包括 TF 下 ThreadGate 也仅 0.02）。§3.1 对选择 GAR-ours 而非 Dongre 原始定义的讨论不充分。\n\n**SF7. SS+LoRA-only 消融缺失** [R1-W1 + R2 交叉共识]\nSS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。SS 贡献 ~8.5× 提升 vs ThreadGate ~2.6×。如果 SS+LoRA-only（无 gating 架构）达到相似水平，ThreadGate 的架构贡献将大幅降低。关键缺失消融。\n\n**SF8. 缺少推理时方案对比** [R2-N2 Must-Fix, R1 Should-Fix, Director 裁定 Should-Fix — divergence]\nβ-steering 已证明推理时注意力干预可恢复 GAR，但论文未与已发表的推理时方案做实验对比（Li et al. 2024 split-softmax, Rhea）。\n- R2 认为 Must-Fix：诊断论文不与最直接替代方案对比是完整性缺陷\n- R1 明确反对升级：论文定位为诊断性贡献，split-softmax 是推理时解决方案，不在同一层面竞争。建议 Discussion 中定性讨论适用场景差异即可。\n- Director 裁定 Should-Fix：R1 的 scope 论证有理——诊断论文不必做方案对比实验，但 Discussion 中应有定性讨论\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 定级 | R2 定级 | Director 裁定 |\n|------|---------|---------|---------------|\n| 因果排除链不完整 | N2 Must-Fix | N1 Must-Fix | **Must-Fix** (强共识) |\n| GAR 弱下游相关 r²=0.04 | N1 Must-Fix | Should-Fix | **Must-Fix** (4% 不足以支撑核心叙事) |\n| 缺 split-softmax/Rhea 对比 | W3 Should-Fix | N2 Must-Fix | **Should-Fix** (见 Divergence) |\n| β-steering 循环论证 | W1 Should-Fix | 同意 | **Should-Fix** |\n| 单数据集 | W2 Should-Fix | W2 Should-Fix | **Should-Fix** |\n| 单种子伪重复 | N3 Must-Fix | Should-Fix | **Should-Fix** (效应量大) |\n| Llama 不完整 | 部分同意 | N3 Must-Fix | **Should-Fix** (核心发现已复制) |\n| 标题 overclaim | 同意 | W1 Should-Fix | **Should-Fix** |\n| GAR-D 近零 artifact | W4 Should-Fix | 同意 | **Should-Fix** |\n| SS+LoRA-only 消融缺失 | W1 | 同意 | **Should-Fix** |\n\n---\n\n## Reviewer Divergence\n\n**1. GAR 弱相关的严重性**\n- R1 视为 Must-Fix：核心指标不可靠，论文基础动摇\n- R2 视为 Should-Fix：若重定位 GAR 为 diagnostic probe，弱下游相关可接受\n- **Director 裁定 Must-Fix**：即使作为 diagnostic probe，4% 解释方差也严重削弱论文叙事说服力\n\n**2. 单种子的严重性**\n- R1 视为 Must-Fix：training variance 完全未覆盖\n- R2 认为效应量 8-17× 足以缓解；R1 确认 eval 样本量（N=50, r=0.802）足够\n- **Director 裁定 Should-Fix**：效应量确实远超 seed noise，但 training variance 仍是遗憾\n\n**3. Split-softmax 对比的严重性**\n- R2 视为 Must-Fix：β-steering 已开推理时干预先河，不对比不合理\n- R1 明确反对升级：论文定位为诊断，split-softmax 为推理时方案不在同层面竞争，Discussion 定性讨论即可\n- **Director 裁定 Should-Fix**：R1 的 scope 论证成立——诊断论文核心贡献是发现问题而非提出解决方案，但 Discussion 应讨论\n\n**4. Llama median vs mean**\n- R2 批评 median 使用有 metric selection 之嫌\n- R1 反驳：Llama 重尾分布 CoV>100%，median 是统计合理选择；Table 7 已双报\n- **Director 裁定**：R1 反驳有理，R2 此项批评不成立\n\n---\n\n## R2 事实错误（由 R1 交叉回应纠正）\n\n| R2 声称 | R1 纠正 | 影响 |\n|---------|---------|------|\n| R2-W6: 无代码/数据链接 | Abstract p.1 有 anonymous.4open.science/r/turn-residual-gating | 该 weakness 撤销 |\n| R2-M3: Figure 1(b) 缺 log scale 标注 | Caption 已明确标注 \"(log scale)\" | 该 minor 撤销 |\n| R2-W3: 仅用 PPL 评估 | 论文有 instruction retention (N=200, 18 categories, McNemar) + MMLU 5-shot + PPL 三层评估 | 评估完整性无问题，但 r²=0.04 弱相关问题仍在 |\n\n---\n\n## Questions\n\nQ1. 如果 GAR 与下游 instruction retention 仅 r²=0.04，为什么 GAR 是论文的核心指标？有没有更好的 grounding proxy metric？\n\nQ2. SS 贡献 ~8.5× vs ThreadGate ~2.6×，如果进一步做 SS+LoRA-only 消融，ThreadGate 的独立架构价值还有多少？\n\nQ3. KV cache drift 是否是 TF-AR gap 的另一个 confound？可以设计什么实验排除？（如 AR decoding with oracle-prefix injection）\n\nQ4. LoRA rank 16 是否可能限制了 gate 效用上界？在更高 rank（32/64）下是否会有不同结论？\n\nQ5. GAR-ours 与 GAR-Dongre 的巨大差异（~0.5 vs ~0.01）的根因是什么？这是否意味着 Dongre 原始定义在 multi-turn 场景下更鲁棒？\n\n---\n\n## Missing References\n\n- **Li et al. 2024** — split-softmax：推理时 multi-turn attention 解决方案，需 §2/Discussion 讨论 [R1, R2 共识]\n- **Rhea (arXiv:2512.06869)** — Role-aware Heuristic Episodic Attention [R1, R2 共识]\n- **Zhang et al. 2024** \"Tell Your Model Where to Attend\" — 推理时注意力操控方法 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**\n\n---\n\n## Visual Layout Check (非评分项)\n\n**状态：已完成** (耗时 ~4 分钟，0 critical / 0 warning / 8 info)\n\n主要发现：\n- **Page 1**：首页无 display item，Figure 1 在 page 2（可接受但非最优）\n- **Page 4**：Figure 2 偏小，legend 文字在打印尺寸下可能偏小\n- **Page 6**：Figure 4 五种柱状颜色灰度打印可区分度下降，建议添加 hatching pattern\n- **Page 8**：Figure 6(a) 标签密集，图内数值标注字号偏小（建议 ≥8pt）\n- **Pages 19-20**：附录图表密集排列，单图尺寸偏小\n- **全文配色**：红/蓝双色主调，饱和度适中，色盲友好，语义连贯性好\n\n整体排版质量可接受，无影响审稿印象的严重问题。\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | Director |\n|------|-----|-----|----------|\n| Overall | 3.5 | 3.5 | **3.0** |\n\n**Director 综合评分：3.0 / 5 (Findings)**\n\n**置信度：4/5 (High)**\n\n### 评分理由\n\n本文呈现了一个有价值的负面结果——lightweight per-layer gating 无法弥合多轮 LLM 的 TF-AR grounding gap——并提出 exposure bias 作为解释假说。系统的五路条件对比（R1 肯定设计精良）和 β-steering 诊断工具是亮点。评估体系完善（instruction retention + MMLU + PPL 三层），代码/数据已匿名发布。\n\n**2 个 Must-Fix 问题限制接收前景：**\n1. **因果声称过强**（强共识）：exposure bias 归因缺少对 KV cache drift 和 NTP magnitude imbalance 的排除，\"root cause\" 声称站不住——R1 建议重新定位为 \"systematic diagnostic comparison\"\n2. **核心指标薄弱**：GAR 与下游仅 r²=0.04，\"Destroys\" 叙事的基础不稳\n\n这两个问题分别涉及方法论（因果推断）和指标有效性，需要实验补充（排除实验 + 下游评估），非纯写作修改可解决。\n\n**8 个 Should-Fix 问题**可在一个 resubmission cycle 内完成修改（R1 明确确认）。\n\n**Director 评分低于两位 Reviewer 0.5 分的理由：**\n因果排除链（Round 2 首次提出）和 GAR 有效性（Round 1 首次提出）跨 5 轮审稿从未被真正解决——每轮只是措辞微调而非补充排除实验。持续未解决的核心问题降低论文在审稿周期内可修复的信心。\n\n**升级路径（→ 3.5 Borderline Conference）：**\n(a) 将 GAR 明确重定位为 diagnostic probe + 补充至少一个 established 下游评估\n(b) 将 exposure bias 降级为 \"a proximal cause consistent with evidence\" 并充分讨论替代假说（KV cache drift, magnitude imbalance）\n(c) 补充 SS+LoRA-only 消融以明确 ThreadGate 独立贡献\n(d) Discussion 中定性讨论 split-softmax/Rhea 适用场景差异\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Destroys\" 标题词与 r²=0.04 不匹配，需降调\n- Contribution (1) \"to our knowledge, the first\" 仍被 R2 质疑\n\n### §3 Method / GAR Definition\n- r_min 数值在正文中未报告（仅 Appendix），影响可复现性 [R1-M1]\n- GAR-ours vs GAR-Dongre 选择理由不充分——GAR-D 全条件 ≈ 0.00-0.02，论文未解释为何弃用原始定义\n- UG 描述需明确仍为可学习 MLP\n\n### §4 Results\n- Table 1 AR 列仍仅 N=5，需扩容至 N≥50 + CI + GAR-D + PPL\n- 数字精度不一致：§4.2 称 spread 0.75pp 但 Table 1 两位小数显示 1pp\n- \"20-33× gap\" 重复 8+ 次——Abstract/§4.2 保留完整数字，其余用回指\n\n### §5 Analysis\n- PCGrad 失败分析需限定 scope：\"gradient direction conflict\" 而非泛化的 \"gradient conflict\"。NTP magnitude imbalance 7.5-14.7× 是替代解释，必须讨论\n- β-steering GAR 恢复是同义反复，需与下游效果解耦报告\n- §5.5 Llama：R1 确认 median 使用合理（CoV>100%），Table 7 已双报——建议正文明确说明选择理由。标题改为 \"Cross-Model Replication\"\n\n### §6 Discussion\n- Exposure bias 归因需降级措辞\n- Instruction retention McNemar p=0.077 未达显著\n- 需定性讨论 split-softmax / Rhea 适用场景差异（R1 建议）\n\n### §7 Limitations\n- KV cache drift 已提及但未设计排除实验\n- LoRA rank capacity saturation 未讨论\n\n### Appendix\n- Appendix C per-category McNemar's test（18 categories）未做 FDR/Bonferroni 校正——主实验已有 Holm-Bonferroni（Appendix E p30），但 Appendix C 漏掉了\n- Bib 格式仍有不一致：Raposo et al. 缺 ICML 2024 venue、Gromov et al. 年份问题\n- liu2016attention 引用可能错配（语音识别 vs 注意力引导），需确认",
    "project": "turn_residual_gating",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-25T08:48:29.076156+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4623
}
```

</details>

---


### Assistant

_source line 462 · 2026-05-25T08:48:38.669187+00:00_

修正版审稿报告已投递至 Research Director。

**修正摘要**：

R1 交叉回应纠正了 R2 三处事实错误后，报告做了以下关键调整：

| 原报告 | 修正后 | 原因 |
|--------|--------|------|
| MF3 split-softmax 对比 (Must-Fix) | → SF8 (Should-Fix) | R1 明确反对升级：诊断论文不在解决方案层面竞争 |
| R1-MISC 无代码发布 (open) | → resolved | R1 确认 Abstract 已有匿名链接 |
| R2-W3 仅 PPL 评估 | → 撤销 | 论文有 instruction retention + MMLU + PPL 三层评估 |
| R2 Llama median 批评 | → 不成立 | CoV>100% 重尾分布用 median 统计合理，Table 7 已双报 |

**最终评分：3.0/5 (Findings)**，2 个 Must-Fix（因果排除链不完整 + GAR 弱下游相关）+ 8 个 Should-Fix。R1 确认修改可在一个 resubmission cycle 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 41

## Round 41

56 recorded events


### User

_source line 463 · 2026-05-25T21:13:31.469542+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: turn_residual_gating
- 论文路径: projects/turn_residual_gating/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main
- 截止日期: 2026-08-03
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-25T21:13:37.724022+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-25T21:13:37.775053+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-25T21:13:44.146955+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-25T21:13:44.247744+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-25T21:13:47.762494+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-25T21:13:47.814896+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-25T21:13:50.524113+00:00_

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
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
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

_source line 471 · 2026-05-25T21:13:50.575566+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-25T21:13:52.884251+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-25T21:13:52.934839+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-25T21:13:55.745085+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read local file project",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read local file project",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-25T21:13:55.845838+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-25T21:14:02.653209+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-25T21:14:04.610322+00:00_

{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (60 个)\n\n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v9_pcgrad**: DONE (success) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: DONE (failed) — \n- **analysis_attention_heatmap**: DONE (success) — \n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- phase2_tf_ar_switching: TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.（排队等待 GPU）\n- phase1a_multiseed_8runs（准备中）\n- phase1b_llama_complement: Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.（准备中）\n- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.（准备中）\n- d048_queue_runner（准备中）\n- d048_ss_s42_resume（准备中）\n- llama_tg_training（准备中）\n\n## 近期结论\n- **phase1a_multiseed_qwen** (killed): Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) 
…[truncated 1242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1957
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-25T21:14:04.610879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-25T21:14:05.614897+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{placeins}
17	\usepackage{float}
18	\usepackage{alphalph}
19	\usepackage{etoolbox}
20	\AtBeginEnvironment{figure}{\nolinenumbers}
21	\AfterEndEnvironment{figure}{\linenumbers}
22	\AtBeginEnvironment{figure*}{\nolinenumbers}
23	\AfterEndEnvironment{figure*}{\linenumbers}
24	\AtBeginEnvironment{table}{\nolinenumbers}
25	\AfterEndEnvironment{table}{\linenumbers}
26	\AtBeginEnvironment{table*}{\nolinenumbers}
27	\AfterEndEnvironment{table*}{\linenumbers}
28	
29	\graphicspath{{../figures/paper/}{../artifacts/}}
30	
31	\title{Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\input{sections/abstract}
39	\input{sections/introduction}
40	\input{sections/related_work}
41	\input{sections/method}
42	\input{sections/experiments}
43	\input{sections/analysis}
44	\FloatBarrier
45	\input{sections/discussion}
46	\input{sections/conclusion}
47	\input{sections/limitations}
48	
49	\bibliography{references}
50	
51	\raggedbottom
52	\appendix
53	\renewcommand{\thesection}{\AlphAlph{\value{section}}}
54	\input{sections/appendix}
55	
56	\end{document}
57	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-25T21:14:05.615253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-25T21:14:05.866902+00:00_

1	# Review Issues Tracker — turn_residual_gating
2	# Round 1 (2026-05-19, dream_20260519T145320)
3	# Round 2 (2026-05-22, fresh re-review of revised paper)
4	# Round 3 (2026-05-22, fresh re-review)
5	# Round 4 (2026-05-25, fresh re-review)
6	# Round 5 (2026-05-25, fresh re-review — current round)
7	# Cross-response phase completed: R1↔R2 convergence reached
8	
9	# ============================================================
10	# Issues from Round 1 — status updates through Round 5
11	# ============================================================
12	
13	- id: "R1-N1"
14	  summary: "所有引用渲染为 '?'——bibliography 编译失败"
15	  category: format
16	  severity: info
17	  status: resolved
18	  first_raised_round: 1
19	  last_seen_round: 1
20	  mentions:
21	    - round: 1
22	      reviewers: [1, 2]
23	      note: "Dream paper artifact。"
24	    - round: 2
25	      reviewers: []
26	      note: "视觉审查确认无 [?] 未解析引用。已修复。"
27	  action_items:
28	    - round: 1
29	      action: "Paper Agent 确保 bibtex 编译正确"
30	      assigned_to: paper_agent
31	      status: done
32	  resolution: "Round 2 视觉审查确认已修复。"
33	  resolution_round: 2
34	
35	- id: "R1-N2"
36	  summary: "单种子支撑结论——统计功效不足 + AR 评估 N=5 过小"
37	  category: experiment
38	  severity: warning
39	  status: in_progress
40	  first_raised_round: 1
41	  last_seen_round: 5
42	  mentions:
43	    - round: 1
44	      reviewers: [1, 2]
45	      note: "Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。"
46	    - round: 2
47	      reviewers: [1, 2]
48	      note: "ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。"
49	    - round: 3
50	      reviewers: [1, 2]
51	      note: "AR 评估仅 N=5，核心 claim 缺统计检验。"
52	    - round: 4
53	      reviewers: [1, 2]
54	      note: "两位 Reviewer 独立列为 Critical Must-Fix。"
55	    - round: 5
56	      reviewers: [1, 2]
57	      note: "Director 裁定降为 Should-Fix（效应量 8-17× 远超种子方差）。Phase 1A multi-seed 训练中。"
58	  action_items:
59	    - round: 1
60	      action: "plan_019: seed=123 extra training"
61	      assigned_to: agent
62	      status: do
…[truncated 22518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-25T21:14:05.867262+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-25T21:14:05.917761+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-25T21:14:21.627695+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 485 · 2026-05-25T21:14:24.037984+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 486 · 2026-05-25T21:14:24.389526+00:00_

1	\begin{abstract}
2	As multi-turn conversations grow longer, large language models progressively lose attention to the system-prompt goals that define their task, even when the underlying goal representations remain intact. Existing remedies operate at inference time, leaving a natural but untested alternative: training auxiliary attention losses alongside next-token prediction to directly optimize goal attention. This strategy assumes that attention patterns learned under teacher forcing will transfer to autoregressive generation, an assumption that classical exposure bias research has challenged for sequence models but that has never been examined for auxiliary attention objectives in multi-turn transformers.
3	We show this assumption fails. On a controlled five-way testbed spanning two architectures (Qwen-2.5-7B, Llama-3.1-8B), goal attention optimized to target under teacher forcing collapses by an order of magnitude under autoregressive generation. A causal exclusion chain traces the failure to exposure bias, ruling out gradient conflict, gating mechanism, and parameter capacity as primary causes. Inference-time attention steering confirms that the collapse reflects attention misallocation rather than representation loss. Scheduled sampling, applied here for the first time to auxiliary attention objectives in multi-turn transformers, compresses the training--inference gap to near parity on Qwen and substantially on Llama, with no perplexity cost\footnote{Code and data are available at \url{https://anonymous.4open.science/r/turn_residual_gating-8703/}.}.
4	\end{abstract}
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 487 · 2026-05-25T21:14:24.389845+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6"
  }
}
```

</details>

---


### Tool result

_source line 488 · 2026-05-25T21:14:24.490343+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-25T21:14:30.270948+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

Based on the search results, here are the key submission guidelines and information for EMNLP 2026:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR and Anonymity Policy

Following the ACL and ARR policies, there is no anonymity period requirement. 

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this cho
…[truncated 557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 8643
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-25T21:14:34.786912+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template double blind review policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit template double blind review policy"
  }
}
```

</details>

---


### Tool call

_source line 491 · 2026-05-25T21:14:35.790982+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR 2026 submission guidelines page limit long paper short paper format requirements",
  "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR 2026 submission guidelines page limit long paper short paper format requirements",
    "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-25T21:14:42.063663+00:00_

Web search results for query: "ARR 2026 submission guidelines page limit long paper short paper format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 1st Workshop on Retrieval Augmented Generation for Report Generation @ ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/1st-workshop-retrieval-augmented-generation-report-generation-acl-2026"}]

Based on the search results, here are the ARR 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Long papers must follow an 8-page limit, and short papers must follow a 4-page limit, not including limitations and ethical considerations.

## Paper Format Requirements

Submissions must adhere to the formatting in the submission templates, which is available as an Overleaf template.

## Additional Requirements

Papers must have a section titled "Limitations" placed according to ACL formatting guidelines. The Limitations section can only include discussion of li
…[truncated 634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 6272
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-25T21:14:43.569728+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template double blind review policy"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Submission Checklist for Original, First Time Submissions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/OriginalSubmissionChecklist"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Now let me search for more specific information about the double-blind review policy for EMNLP 2026 main conference:

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"GroundLM 2026 | EMNLP 2026 Workshop","url":"https://groundlm.github.io/grouplm_emnlp202
…[truncated 1956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 8782
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-25T21:14:58.176255+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-25T21:14:58.681884+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is central to how large language models are deployed, from customer service to tutoring to long-form reasoning. Yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \citet{dongre2026attention} measured significant Goal Accessibility Ratio (GAR) decline across 12 models over extended conversations; in our own evaluation, goal attention drops by over 70\% within just five turns. Crucially, this is not a representation problem: residual stream probes confirm that goal information persists (AUC\,=\,0.98). The model retains the knowledge of what it should attend to; it simply stops attending.
4	
5	Existing remedies address this decay at inference time. Split-softmax \citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \citep{xiao2024streaming} retains anchor tokens; Gated Attention \citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. A natural alternative is to intervene during training: optimize goal attention directly through auxiliary losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption: attention patterns learned under teacher forcing (TF) transfer to autoregressive (AR) generation. Classical exposure bias research \citep{bengio2015scheduled,lamb2016professor} has shown that TF creates a training--inference distribution mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.
6	
7	We test this assumption and find it fails. We introduce a controlled five-way testbed (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, and Base) designed not as competing solutions but as a causal exclusion chain (\S\ref{sec:comparison-design}), where each adjacent pair isolates one cand
…[truncated 2630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-25T21:14:58.719600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-25T21:14:59.057993+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Accessibility Ratio.}
6	Standard metrics such as perplexity and attention entropy capture generation quality but not \emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. To formalize this, we denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation; attention at this position most directly reflects the model's awareness of task specifications. \textbf{GAR-ours} restricts the measurement accordingly:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon fo
…[truncated 6289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 338
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-25T21:14:59.058399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-25T21:14:59.109537+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; training costs in Appendix~\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; dataset statistics in Appendices~\ref{sec:appendix-data} and~\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and perplexity (PPL).
7	
8	\subsection{Main Results}
9	
10	Table~\ref{tab:five-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\leq$1\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, indicating that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\S\ref{subsec:ss}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendices~\ref{sec:appendix-stats} and~\ref{sec:appendix-stats-ext}), yet the gap remains 7.8$\times$. A second seed co
…[truncated 4119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-25T21:15:03.981201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex",
  "offset": "41"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex",
    "offset": "41"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-25T21:15:04.533343+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (41). The file has 41 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-25T21:15:04.533721+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-25T21:15:04.986739+00:00_

1	\section{Analysis}\label{sec:analysis}
2	
3	\begin{figure*}[!t]
4	  \centering
5	  \includegraphics[width=\textwidth]{fig3_gate_shift.pdf}
6	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:five-way}) due to smaller sample size.}
7	  \label{fig:gate-shift}
8	\end{figure*}
9	
10	Each subsection kills one alternative hypothesis via causal exclusion: \S\ref{subsec:gate-conditioning}~turn conditioning, \S\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms selectivity; \S\ref{subsec:cross-model} confirms cross-architecture generalization.
11	
12	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
13	
14	We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\% attenuation; Table~\ref{tab:five-way}; full gate profiles in Appendix~\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\,=\,0.777, L27\,=\,1.000) despite lacking turn conditioning; the structure thus arises from LoRA$+$GAR pressure (Figure~\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict p
…[truncated 4892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-25T21:15:04.987206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-25T21:15:05.490708+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \citep{he2019exposure}; GAR optimizes a \emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\leq}$1.3$\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\,=\,0.743; Appendix~\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.
4	
5	\looseness=-1 Our exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\S\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\times$ NTP dominance; \citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\,=\,0.200; Appendix~\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\beta$-steering is likewise a \emph{diagnostic}, distinct from inference-time remedies such as split-softmax \citep{li2024measuring} and Rhea \citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\beta$\,=\,5 the two converge (SS\,=\,0.717 vs.\ TG\,=\,0.727).
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-25T21:15:05.491066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-25T21:15:05.942963+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\,=\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\sim}$1.3$\times$ (Qwen) and ${\sim}$2.9$\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-25T21:15:05.943297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-25T21:15:06.044055+00:00_

1	\section*{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations); generalization to other architectures and domains (e.g., code, reasoning) is untested. Most configurations use a single seed (scheduled sampling validated on three seeds; \S\ref{subsec:ss}), and quality assessment relies on PPL rather than comprehensive benchmarks \citep{hendrycks2021measuring,lin2022truthfulqa}. We test only one auxiliary loss family (GAR with MSE target $\tau$\,=\,0.5); head-specific or layer-specific losses may exhibit different sensitivity to exposure bias. Our causal exclusion identifies exposure bias as a primary factor but does not rule out KV cache drift as a contributing mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-25T21:15:34.143291+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "turn_residual_gating",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "turn_residual_gating",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-25T21:15:36.554554+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "turn_residual_gating",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6/submitted.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "turn_residual_gating",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6/submitted.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 512 · 2026-05-25T21:15:55.348020+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21204
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-25T21:15:55.348345+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 18793
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-25T21:15:55.549262+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "turn_residual_gating",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long paper (Main Conference)\n- **截止日期**: ARR 提交 2026-05-25，EMNLP Commitment 2026-08-02\n- **格式**: 正文 8 页限制，参考文献不限，Limitations 章节必须有（不计入页数），double-blind，ACL 模板\n- **匿名规则**: Double-blind，无匿名期限制\n\n## 论文路径\n- LaTeX: `projects/turn_residual_gating/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**——重点检查以下方面：\n\n1. **因果排除链逻辑**：五路对比设计是否真正实现了因果排除？每一步排除（gradient conflict、gating mechanism、parameter capacity）的逻辑是否严密？是否存在未排除的替代假说？\n2. **统计有效性**：AR 评估样本量（N=50）是否足够？统计检验选择是否合理？多重比较是否校正？效应量（8-17×）的置信区间？\n3. **Exposure bias 归因**：论文声称 exposure bias 是 primary cause，但因果排除链是否完整？KV cache drift、NTP magnitude imbalance 等替代假说是否被充分讨论？\n4. **Scheduled sampling 证据**：SS 的 gap 压缩（7.8× → 1.3×）是否足够可信？三个种子是否足够？PPL 无损的声称是否有充分证据？\n5. **β-steering 论证**：GAR 恢复是否存在循环论证（boost attention → attention metric recovers）？下游效果（p=0.077）未达显著，这对论文结论有何影响？\n6. **GAR 指标有效性**：GAR-ours vs GAR-Dongre 的选择是否充分论证？r=0.200 的下游相关性意味着什么？GAR 作为 diagnostic probe 的定位是否合理？\n7. **跨模型验证**：Llama 仅覆盖 3/5 条件，N=20，使用 median——这些限制对泛化性声称的影响？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 1-5，参照 EMNLP 2026 评分标准)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "turn_residual_gating",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long paper (Main Conference)\n- **截止日期**: ARR 提交 2026-05-25，EMNLP Commitment 2026-08-02\n- **格式**: 正文 8 页限制，参考文献不限，Limitations 章节必须有（不计入页数），double-blind，ACL 模板\n- **匿名规则**: Double-blind，无匿名期限制\n\n## 论文路径\n- LaTeX: `projects/turn_residual_gating/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**——重点检查以下方面：\n\n1. **因果排除链逻辑**：五路对比设计是否真正实现了因果排除？每一步排除（gradient conflict、gating mechanism、parameter capacity）的逻辑是否严密？是否存在未排除的替代假说？\n2. **统计有效性**：AR 评估样本量（N=50）是否足够？统计检验选择是否合理？多重比较是否校正？效应量（8-17×）的置信区间？\n3. **Exposure bias 归因**：论文声称 exposure bias 是 primary cause，但因果排除链是否完整？KV cache drift、NTP magnitude imbalance 等替代假说是否被充分讨论？\n4. **Scheduled sampling 证据**：SS 的 gap 压缩（7.8× → 1.3×）是否足够可信？三个种子是否足够？PPL 无损的声称是否有充分证据？\n5. **β-steering 论证**：GAR 恢复是否存在循环论证（boost attention → attention metric recovers）？下游效果（p=0.077）未达显著，这对论文结论有何影响？\n6. **GAR 指标有效性**：GAR-ours vs GAR-Dongre 的选择是否充分论证？r=0.200 的下游相关性意味着什么？GAR 作为 diagnostic probe 的定位是否合理？\n7. **跨模型验证**：Llama 仅覆盖 3/5 条件，N=20，使用 median——这些限制对泛化性声称的影响？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 1-5，参照 EMNLP 2026 评分标准)。"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-25T21:16:09.057138+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13507
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-25T21:16:09.207984+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "turn_residual_gating",
  "text": "你是 Reviewer 2，负责**新颖性/完整性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long paper (Main Conference)\n- **截止日期**: ARR 提交 2026-05-25，EMNLP Commitment 2026-08-02\n- **格式**: 正文 8 页限制，参考文献不限，Limitations 章节必须有（不计入页数），double-blind，ACL 模板\n- **匿名规则**: Double-blind，无匿名期限制\n\n## 论文路径\n- LaTeX: `projects/turn_residual_gating/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性/完整性**——重点检查以下方面：\n\n1. **Novelty 定位**：exposure bias 在 multi-turn transformer auxiliary attention losses 上的首次实证——这个 novelty claim 是否成立？是否有已知工作做了类似的事情？\"to our knowledge, the first\" 的措辞是否可接受？\n2. **Related Work 覆盖**：\n   - 是否遗漏了重要的相关工作？特别是 attention steering/loss 方向、multi-turn dialogue 方向、exposure bias 方向\n   - Li et al. (2024) split-softmax、Rhea (Hong et al. 2025) 等竞争方案是否被充分讨论？\n   - Scheduled sampling 在 transformer 上的应用是否已有先例？\n3. **Framing 准确性**：\n   - Contribution 声称是否与实际证据匹配？是否存在过度声称（overclaim）？\n   - \"causal exclusion\" 措辞是否准确？实际是消融研究 + 排除法\n   - GAR 被定位为 \"diagnostic probe\"——这个定位是否自洽？\n4. **写作质量**：\n   - 行文是否清晰、逻辑连贯？\n   - 关键数字（如 8-17×、0.401±0.047）是否重复过多？\n   - Figure/Table 的标题和说明是否准确？\n   - 引用格式是否一致？bib 条目是否完整？\n5. **格式合规**：\n   - 正文是否在 8 页以内？\n   - Limitations 章节是否合规（放在正文、一段覆盖 3 个点左右）？\n   - 匿名化是否彻底？\n   - Abstract 是否在 200 words 以内？\n6. **Appendix 完整性**：附录内容是否与正文互补而非重复？是否有关键信息仅在附录中但应在正文中？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 1-5，参照 EMNLP 2026 评分标准)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "turn_residual_gating",
    "text": "你是 Reviewer 2，负责**新颖性/完整性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long paper (Main Conference)\n- **截止日期**: ARR 提交 2026-05-25，EMNLP Commitment 2026-08-02\n- **格式**: 正文 8 页限制，参考文献不限，Limitations 章节必须有（不计入页数），double-blind，ACL 模板\n- **匿名规则**: Double-blind，无匿名期限制\n\n## 论文路径\n- LaTeX: `projects/turn_residual_gating/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性/完整性**——重点检查以下方面：\n\n1. **Novelty 定位**：exposure bias 在 multi-turn transformer auxiliary attention losses 上的首次实证——这个 novelty claim 是否成立？是否有已知工作做了类似的事情？\"to our knowledge, the first\" 的措辞是否可接受？\n2. **Related Work 覆盖**：\n   - 是否遗漏了重要的相关工作？特别是 attention steering/loss 方向、multi-turn dialogue 方向、exposure bias 方向\n   - Li et al. (2024) split-softmax、Rhea (Hong et al. 2025) 等竞争方案是否被充分讨论？\n   - Scheduled sampling 在 transformer 上的应用是否已有先例？\n3. **Framing 准确性**：\n   - Contribution 声称是否与实际证据匹配？是否存在过度声称（overclaim）？\n   - \"causal exclusion\" 措辞是否准确？实际是消融研究 + 排除法\n   - GAR 被定位为 \"diagnostic probe\"——这个定位是否自洽？\n4. **写作质量**：\n   - 行文是否清晰、逻辑连贯？\n   - 关键数字（如 8-17×、0.401±0.047）是否重复过多？\n   - Figure/Table 的标题和说明是否准确？\n   - 引用格式是否一致？bib 条目是否完整？\n5. **格式合规**：\n   - 正文是否在 8 页以内？\n   - Limitations 章节是否合规（放在正文、一段覆盖 3 个点左右）？\n   - 匿名化是否彻底？\n   - Abstract 是否在 200 words 以内？\n6. **Appendix 完整性**：附录内容是否与正文互补而非重复？是否有关键信息仅在附录中但应在正文中？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 1-5，参照 EMNLP 2026 评分标准)。"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-25T21:16:10.717112+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1509
}
```

</details>

---


### Assistant

_source line 518 · 2026-05-25T21:16:19.298893+00:00_

Round 6 审稿已全面启动：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 已分配，独立审稿中 |
| Reviewer 2（新颖性/完整性） | ✅ 已分配，独立审稿中 |
| 视觉审查 Agent | ✅ 已派发，并行执行 |
| 外部审稿（Stanford Agentic Reviewer） | ✅ 已发送请求，8h 后自动提醒 |

等待两位 Reviewer 返回 Round 1 独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 42

## Round 42

2 recorded events


### User

_source line 519 · 2026-05-25T21:23:17.539794+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性审查

**论文标题**: Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审稿侧重**: 方法严谨性（因果排除链、统计有效性、归因逻辑、跨模型验证）

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 研究问题新颖，五路因果排除设计有创意，核心发现在 Qwen 主实验上基本可信，但因果链存在未封闭的替代假说、下游效果弱（GAR 与 compliance 相关性仅 r=0.200）、跨模型验证不充分，削弱了"exposure bias 是 primary cause"这一核心声称的说服力。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3 / 5 | 主要 claims 有实验支撑但存在明显缺口：因果排除链未封闭（梯度幅值失衡未独立测试）、β-steering 下游效果 p=0.077 未显著、跨模型验证仅覆盖 3/5 条件 |
| **Excitement** | 3.5 / 5 | 首次系统研究 exposure bias 对多轮对话中辅助注意力目标的影响，五路排除设计有方法论贡献，但实际应用场景的指导意义有限（GAR 仅解释 4% 下游方差） |
| **Reproducibility** | 4 / 5 | 超参数完整（Table 2/Appendix A），三种子重复（Seeds 42/123/456），匿名代码链接已提供，统计检验详尽（Appendix E/Z），但 Llama 实验单种子、N=20 难以复现 |
| **Reviewer Confidence** | 4 / 5 | 仔细阅读了全文 34 页（正文 + 全部附录），对 exposure bias、scheduled sampling、注意力分析方法论均有较好理解 |

---

## Must-Fix 问题（影响接收决定）

### N1 [critical] 因果排除链存在未封闭的替代假说——梯度幅值失衡

- **具体位置**: §5.2 PCGrad Gradient Direction Conflict Exclusion；Appendix J（Gradient Conflict Analysis）
- **问题**: 论文用 PCGrad 排除了梯度*方向*冲突（gradient direction conflict），但 Appendix J 明确显示 NTP 梯度幅值压倒 GAR 7.5–14.7×（"NTP gradient magnitude dominates GAR by 7.5× at epoch 0 and 14.7× by epoch 3"）。PCGrad 仅将冲突梯度投影到对方法平面上，不改变幅值比。论文自己也承认"the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor"（§5.2）。
- **关键缺失**: 一个更直接的替代测试是**梯度幅值重缩放**（如增大 λ_GAR 使 GAR 梯度与 NTP 梯度同量级），但论文未测试这一条件。如果简单地增大 λ_GAR 就能压缩 TF-AR gap，那"exposure bias 是 primary cause"的结论就需要大幅修正——primary cause 可能只是 GAR 信号被 NTP 淹没。
- **为什么影响接收**: 论文核心声称是"exposure bias is the primary cause"（Abstract, §1, §6）。因果排除链是支撑这一声称的关键论证结构，如果排除链有未覆盖的可行替代假说，核心结论的可信度受损。
- **建议修改方向**: (1) 增加 λ_GAR 梯度幅值匹配实验（如 λ_GAR ×10 或 ×15）；(2) 若无法补充实验，至少将 NTP 幅值压倒作为与 exposure bias 同等地位的候选假说讨论，而非在 Appendix J 中一笔带过；(3) 将声称从"primary cause"弱化为"a major contributing factor"。

### N2 [critical] GAR-ours 作为核心指标的下游有效性不足——r=0.200 仅解释 4% 方差

- **具体位置**: §3.1（GAR 定义）；§4.3（"correlation with instruction retention is weak: r = 0.200, p = 0.007; §6"）；Appendix C（Instruction Retention Details）
- **问题**: 全文所有实验的核心结果指标是 GAR-ours，但 GAR-ours 与下游 instruction compliance 的相关性仅 r = 0.200（p = 0.007），即 GAR 仅解释 4% 的下游行为方差。这意味着：
  - GAR 从 0.50 坍塌到 0.019（17×）在下游任务上可能影响不大
  - SS 将 GAR gap 压缩到 1.3× 的实际意义不清楚
  - 论文用"diagnostic probe"定位（§3.1: "GAR serves primarily as a diagnostic probe"）来规避这个问题，但同时又在 Abstract、Introduction、Conclusion 中将 GAR collapse 和 SS remedy 作为核心贡献呈现，暗含实际意义
- **为什么影响接收**: 一篇以诊断现象和提出 remedy 为核心贡献的论文，其核心指标与实际效果之间的弱关联严重削弱了 paper 的 impact 论证。读者会问：如果 GAR 坍塌了但下游任务影响不大，这个现象为什么重要？
- **建议修改方向**: (1) 补充更多下游评测（如多轮对话中的 goal completion rate、系统提示遵循率等），用 task-level metric 而非 attention metric 评估 SS 的实际效果；(2) 在 Instruction Retention 评测中增大样本量（当前 N=54 对 paired evaluations，McNemar's test p=0.077 不显著）；(3) 至少在 Introduction 中明确承认 GAR 的下游预测力有限，避免给读者过强的实际影响暗示。

### N3 [critical] 跨模型验证严重不足——Llama 仅覆盖 3/5 条件且统计效力低

- **具体位置**: §5.5 Cross-Model Replication；Table 7/8（Appendix F）；Table 29
- **问题**:
  1. Llama-3.1-8B 仅覆盖 3/5 排除链条件（Base, ThreadGate, LoRA-only），缺少 Uniform Gate 和 +PCGrad——排除链在 Llama 上是断裂的
  2. N=20 conversations，因 AR 分布重尾改用 median（Table 7, §5.5），但 Qwen 用 mean，导致跨模型数值不可直接比较（Qwen baseline gap 7.8× vs Llama 27× (median)）
  3. 单种子（seed 123），无方差估计
  4. 1.5B cross-scale 验证（Appendix Y）也仅覆盖 Qwen，单种子
- **为什么影响接收**: 论文声称"the gap is substantial on both architectures, consistent with exposure bias as architecture-independent"（§5.5），但 Llama 上的排除链不完整：没有 PCGrad → 无法在 Llama 上排除梯度冲突假说；没有 Uniform Gate → 无法排除 gating mechanism 假说。Architecture-independent 的声称没有充分证据支撑。
- **建议修改方向**: (1) 补全 Llama 上至少 PCGrad 条件的实验（这是排除链中最关键的节点）；(2) 增大 N 到至少 50 或统一 mean/median 报告以允许跨模型比较；(3) 如无法补全，将 cross-model 结论明确降级为"preliminary/suggestive evidence"而非"consistent with architecture-independence"。

---

## Should-Fix 问题（影响评分但不一票否决）

### W1 [warning] β-steering 论证存在部分循环性——GAR 恢复是 trivially expected

- **具体位置**: §4.3 Inference-Time Attention Steering；Appendix C；Figure 3
- **问题**: β-steering 直接在 pre-softmax 层给 goal-token 位置加偏置 β → attention weight 增加 → GAR（衡量对 goal-token 的 attention）自然恢复。这部分是 tautological：boosting attention to goal tokens → metric measuring attention to goal tokens improves。
- **非循环的部分**: 如果 goal-token 位置的 hidden states 在 AR 生成中已经降级，那么 boost attention 也不会改善 instruction following。β-steering 的论证逻辑是"representations intact, routing broken"——但下游验证（Appendix C, p=0.077）不显著，无法完成论证闭环。
- **建议**: (1) 更明确地区分"GAR 恢复"（trivially expected）和"instruction compliance 恢复"（non-trivial but unproven at α=0.05）；(2) 增大 Appendix C 的样本量以获得足够统计效力；(3) 考虑加入 random position boosting 对照（boost 非 goal-token 位置的 attention），证明 goal-token 位置的特异性。

### W2 [warning] Scheduled Sampling 有效性的替代解释未排除

- **具体位置**: §4.4；Appendix I（Scheduled Sampling Implementation）；Table 29
- **问题**: SS 在训练中引入 model-generated tokens 替换 ground-truth tokens，论文将其效果归因于"bridging the TF-AR distribution gap"（exposure bias mitigation）。但 SS 同时引入了多种正则化效应：
  - 数据增强（model-generated tokens 增加了输入多样性）
  - 隐式 curriculum learning（随 p 线性增加的难度）
  - Distributional smoothing（平滑了 one-hot teacher signal）
  - Context-dependent regularization（模型必须在自己的前缀上继续生成）
  
  论文未设计实验分离这些效应。如果 SS 的效果主要来自数据增强而非 exposure bias mitigation，论文的因果归因需要调整。
- **建议**: 增加对照实验，如 (1) 随机 token 替换（提供数据增强但不模拟 AR drift）；(2) 固定 p（无 curriculum 效应）的 SS 变体；(3) 仅在 goal-token 附近做 SS（隔离 exposure bias 的空间特异性）。

### W3 [warning] Qwen 和 Llama 结果报告标准不一致

- **具体位置**: Table 1（Qwen, mean）vs Table 7（Llama, median）；Table 29（两模型对比）
- **问题**: Qwen 所有结果用 mean 报告，Llama 因重尾分布改用 median。这导致：
  - Qwen baseline TG gap = 7.8×（mean）vs Llama = 27×（median）——无法判断是架构差异还是统计量选择造成的数值差异
  - Gap compression 比（6.5× vs 9.3×）也不可直接比较
  - 论文在 Limitations 中未提及这一不一致性
- **建议**: 两个模型同时报告 mean 和 median（至少在 Appendix 中），并讨论 Llama 重尾分布的来源（是模型特性还是 N=20 的小样本效应？）。

### W4 [warning] Loss formulation 搜索（7 轮迭代）的过拟合风险

- **具体位置**: Appendix B（Loss Formulation Search）；Table 3
- **问题**: 论文经历了 7 轮 loss formulation 搜索（v1→v7），从 cumulative loss、maximize loss、smooth saturation 等不同方向迭代到最终的 MSE + gate diversity。这个搜索过程使用了与最终评测相同的 GAR 指标。虽然论文透明地报告了搜索过程（appreciated），但这引入了对特定评测设置的过拟合风险——v7 是否在新数据/新模型上同样最优？
- **建议**: 在 Llama 或 1.5B 上验证 v7 仍然是最优或接近最优的 loss formulation（至少与 v5/v6 做简短对比）。

---

## 小问题（不影响接收）

1. **PPL 饱和**: Table 1 中所有 5 个变体的 TF PPL 都是 2.78，AR PPL 都是 ~1.441。如此高度一致暗示 PPL 在此评测集上可能已经饱和，不足以区分变体之间的生成质量差异。考虑补充 distinct-n 或 MAUVE 等生成多样性指标。

2. **Figure 1 信息密度**: Figure 1 尝试在一页内同时展示 GAR decay（1a）、SS 效果（1b）、五路排除结果（Table 1），但 Table 1 的字体极小，影响可读性。建议将 Table 1 独立排版。

3. **匿名 URL**: 脚注 1 使用了 anonymous.4open.science URL。确认匿名链接不泄露作者信息（已检查，URL 格式合规）。

4. **Abstract word count**: 按 EMNLP 2026 要求不超过 200 words。当前 abstract 约 190-195 words，合规。

5. **Appendix J 标题不精确**: "Gradient Conflict Analysis" → 实际内容同时包含方向分析和幅值分析，建议改为 "Gradient Interaction Analysis"。

6. **Gate diversity loss 的消融不足**: §3.3 引入 L_div 但未单独消融其贡献（仅在 Table 3 的 v7 中出现）。建议在 Appendix 中加一个 v7-without-div 对照。

---

## Questions for Authors

**Q1**: NTP 梯度幅值压倒 GAR 7.5–14.7×（Appendix J）。是否测试过直接增大 λ_GAR（如 ×10 或 ×15）来匹配 NTP 幅值？如果 λ_GAR 重缩放能压缩 TF-AR gap，这对 exposure bias 归因有何影响？

**Q2**: Llama 改用 median 报告是因为重尾分布。能否提供 Llama 的 mean GAR 值以及 Qwen 的 median 值，以允许跨模型直接比较？重尾分布是 Llama 的架构特性，还是 N=20 小样本效应？

**Q3**: Table 1 中所有变体的 TF PPL 完全一致（2.78）。这是否意味着 TF evaluation set 对这些模型已经饱和？在更长对话（>5 turns）上 PPL 是否仍然一致？

**Q4**: SS 的效果是否可以通过 oracle-forcing 实验（在 AR generation 的 turn boundary 提供 gold tokens）进一步验证？这能直接测试"training-inference distribution mismatch at turn boundaries"这一特定假说。

**Q5**: GAR-ours 仅衡量 last token 对 goal tokens 的 attention。信息也可通过 residual connections 和中间 token 传播。TRC 分析（§5.4）表明 hidden states 跨轮次变化，但未直接验证 goal information 是否可通过非注意力通路（如 residual stream）到达 last token。对此有何补充证据？

---

## Missing References

论文引用较为完整，但建议补充以下相关工作：

1. **Goyal et al. (2017)** "Differentiable Scheduled Sampling for Credit Assignment" — SS 的可微分变体，与本文的 SS 实现（Bernoulli sampling）是互补方法，应在 §4.4 或 Related Work 中讨论。

2. **Holtzman et al. (2020)** "The Curious Case of Neural Text Degeneration" — 关于 AR 生成中退化现象的经典分析，与本文"AR generation degrades attention patterns"的发现在精神上相关。

3. **Su et al. (2024) 或 Jiang et al. (2023)** — 近期关于 LLM long-context attention 退化的工作（如果存在的话），可以加强 Related Work 中"attention decay over length"的讨论。

---

## 主要优势

1. **研究问题新颖且定义清晰**: 首次系统研究 exposure bias 对多轮对话中辅助注意力训练目标的影响。现有 exposure bias 文献集中在 NMT/text generation，本文将其扩展到多轮对话的注意力分配问题，填补了一个有意义的研究空白。

2. **五路因果排除设计有方法论贡献**: 每个变体精确隔离一个因素（capacity → LoRA-only, direction conflict → PCGrad, gating → Uniform Gate vs ThreadGate, distribution mismatch → SS），这种"causal exclusion chain"的实验设计方法论本身可以被其他诊断性研究借鉴。

3. **附录极为详尽（26 页）**: 涵盖 loss formulation search（B）、instruction retention（C）、long-conversation evaluation（D）、完整统计检验（E/Z）、gate profile analysis（G/H）、bootstrap CIs（G4）、training loss curves（G6）、per-turn GAR decay（O）、per-head KL divergence（P）、scaling analysis（N/Y）、gradient interaction（J）、per-seed results（T）等，展现了扎实的实验工作量。

4. **统计报告规范（主实验）**: Qwen 主实验使用 Wilcoxon signed-rank tests（非参数），bootstrap 95% CIs（10000 resamples），effect sizes（rank-biserial），Bonferroni 校正（4 primary comparisons, all survive），per-seed 分解（Appendix T）——统计分析达到优秀水平。

5. **诚实的 Limitations 讨论**: 明确承认 KV cache drift 未排除、单数据集限制、narrow model coverage，以及 β-steering 下游效果 p=0.077 不显著。这种诚实增强了论文的可信度。

6. **Scheduled Sampling 应用有实际价值**: 首次将 SS 应用于辅助注意力训练目标，gap 压缩比显著（Qwen: 7.8× → 1.3×, PPL 无损），且跨种子稳定（Table 19/20）。即使因果归因有争议，SS 作为一个实用的训练技巧本身有贡献。

---

**总结**: 这是一篇在研究问题和实验设计上有显著亮点的论文，主实验（Qwen 五路排除 + SS）的技术执行质量高。但核心 claim（"exposure bias is the primary cause"）的论证存在三个关键缺口：(1) 梯度幅值替代假说未排除，(2) GAR 指标下游有效性弱，(3) 跨模型验证不完整。如果能在 rebuttal 中补充 λ_GAR rescaling 实验结果并完善 Llama 上的排除链，评分可以考虑提升到 4.0（Conference）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 520 · 2026-05-25T21:23:26.897711+00:00_

Reviewer 1 审稿已收到（3.5/5 Borderline Conference）。等待 Reviewer 2 完成独立初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 43

## Round 43

8 recorded events


### User

_source line 521 · 2026-05-25T21:23:34.270038+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结果摘要**：

- **Overall: 3.5 / 5（Borderline Conference）**
- **Soundness: 3/5 | Excitement: 3.5/5 | Reproducibility: 4/5**

**3 个 Must-Fix**：
1. **因果排除链未封闭**——PCGrad 仅排除梯度方向冲突，未测试梯度幅值重缩放（NTP 幅值压倒 GAR 7.5–14.7×），λ_GAR rescaling 实验缺失
2. **GAR 下游有效性弱**——r=0.200 仅解释 4% 下游方差，β-steering 的 instruction retention 效果 p=0.077 不显著
3. **跨模型验证不足**——Llama 仅 3/5 条件、N=20、单种子、median 报告与 Qwen mean 不可比

**4 个 Should-Fix**：β-steering 部分循环论证、SS 替代解释未排除、Qwen/Llama 报告标准不一致、loss formulation 搜索的过拟合风险

**主要优势**：研究问题新颖、五路排除设计有方法论贡献、26 页附录展现扎实工作量、Qwen 主实验统计分析规范、SS 应用有实用价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-25T21:23:53.252930+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-25T21:23:53.303542+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-25T21:23:56.776696+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,get_external_review_status,get_visual_check_status,dispatch_visual_check,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,get_external_review_status,get_visual_check_status,dispatch_visual_check,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-25T21:23:56.827197+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-25T21:23:59.233084+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director reviewer review mcp agent-ml",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director reviewer review mcp agent-ml",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-25T21:23:59.283693+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 528 · 2026-05-25T21:24:08.073349+00:00_

Reviewer 1 初审已收到，记录其核心发现。现在等待 Reviewer 2 完成初审，收齐后进入交叉分享阶段。

**Reviewer 1 初审摘要**：
- **Overall: 3.5（Borderline Conference）**
- 3 个 Must-Fix：因果排除链未封闭（梯度幅值）、GAR 下游有效性弱（r=0.200）、跨模型验证不足（Llama 条件/种子/统计量不一致）
- 4 个 Should-Fix：β-steering 循环论证、SS 替代解释、报告标准不一致、loss formulation 搜索过拟合风险

等待 Reviewer 2 提交后立即启动 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 44

## Round 44

6 recorded events


### User

_source line 529 · 2026-05-25T21:24:47.546600+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（新颖性/完整性）

---

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 论文提出了一个genuinely novel的实证发现——exposure bias会导致multi-turn transformer中auxiliary attention loss在autoregressive generation下崩塌——实验设计严谨，但单一数据集、LoRA-only评估、以及GAR与下游任务性能之间的弱关联限制了实际影响力。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（五路对比+因果排除），但"因果排除"的措辞过强，实际是消融排除法；SS在Llama上gap仍有2.9×未解决 |
| Excitement | 3.0/5 | 发现本身新颖且有启发性，但本质是诊断性工作而非提出解决方案；实际应用影响不清晰 |
| Reproducibility | 4.0/5 | 附录极为详尽（24页），超参数、统计检验、per-seed结果齐全；匿名代码已提供 |
| Overall Assessment | 3.5/5 | Borderline Conference——发现有价值，实验严谨，但scope有限、实际影响待验证 |
| Confidence | 4/5 | 熟悉exposure bias、multi-turn dialogue、attention manipulation领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Causal exclusion"措辞过强，与实际方法论不匹配
- 具体位置：Abstract第3句、Section 1 Contribution 2、Section 5.2标题
- 问题：论文声称使用"causal exclusion chain"追踪failure到exposure bias。但实际方法是：(1) 消融实验排除gradient conflict（PCGrad）、gating mechanism（Uniform Gate vs ThreadGate）、parameter capacity（LoRA-only）；(2) scheduled sampling（针对exposure bias的intervention）部分修复了问题。这是一个合理的"排除替代解释"方法，但不是严格的因果推断。特别是：
  - PCGrad排除了gradient direction conflict，但没有排除gradient magnitude imbalance的所有形式
  - Limitations自己承认"does not rule out KV cache drift as a contributing mechanism"
  - SS只是部分修复（Llama上gap仍有2.9×），这说明可能还有其他因素
- 为什么影响接收：Reviewer可能认为overclaim，降低论文可信度。"Causal exclusion"在philosophy of mind中有严格含义，在这里使用容易引发误解。
- 建议修改方向：改为"systematic exclusion of alternative explanations"或"diagnostic exclusion chain"。保留方法论，修改措辞。

**N2** [critical] 单一数据集限制了generalizability claim
- 具体位置：所有实验（Section 4-5）、Abstract中"spanning two architectures"的暗示
- 问题：所有实验均在UltraChat 8K conversations上进行，没有在任何其他multi-turn数据集（如MT-Bench、LMSYS-Chat、ShareGPT）上验证。论文的核心claim是关于exposure bias的普遍现象，但单一数据集的evidence难以支撑这种普遍性。Abstract说"spanning two architectures"给人感觉是跨多个设置的验证，但实际上只是同一数据集上的两个模型。
- 为什么影响接收：ARR reviewers通常期望至少2个数据集来支持generalization claims。当前的experimental scope对于一个诊断性/负面结果论文可能不够。
- 建议修改方向：至少在一个额外的multi-turn dataset上验证核心发现（TF-AR gap在不同数据集上是否也存在），或者在claim中明确限定scope。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] GAR与下游任务性能的关联证据不足
- 具体位置：Section 3.1（GAR定义）、Appendix C（Instruction Retention）
- 问题：GAR是本文的核心指标，但论文没有充分论证GAR collapse在实践中的危害。Appendix C的instruction retention评估显示：只有content constraints获得显著改善（+23.8pp），format和count constraints几乎无变化，position constraints接近0。这说明GAR主要捕获的是content-level的attention routing，而非全面的instruction following能力。此外，PPL在所有配置下几乎相同（2.78 for TG/UG/LoRA-only），这进一步削弱了"collapse"的实际影响。
- 建议：在正文中更明确地讨论GAR作为proxy metric的局限性，或提供更多downstream evidence（如GPT-4评分、人工评估）。

**W2** [warning] Scheduled sampling在Llama上效果有限（2.9× gap），但论文表述不够明确
- 具体位置：Abstract（"substantially on Llama"）、Section 4.4、Table 29
- 问题：SS将Qwen的gap从7.8×压缩到1.2×（非常好），但Llama仅从27×（median）到2.9×。2.9×仍然是显著的performance gap。Abstract中"substantially"的措辞模糊了这个事实。Section 5.5讨论了架构差异，但对Llama上SS效果有限的根本原因分析不够深入。
- 建议：Abstract中改为更精确的表述，如"compresses the gap to near parity on Qwen (1.2×) and by 9.3× on Llama (from 27× to 2.9×), though a meaningful gap remains on Llama"。

**W3** [warning] 仅LoRA fine-tuning，未验证full fine-tuning
- 具体位置：Section 4.1、Appendix A（Table 2）
- 问题：所有实验使用LoRA（rank 16/32）。LoRA限制了模型重组attention patterns的capacity。在full fine-tuning下，模型可能有更大的capacity来学习TF下不会在AR下崩塌的attention patterns。Exposure bias的严重程度可能与adapter capacity有关。
- 建议：在Limitations中更prominently讨论这一点，或至少在一个配置上提供full fine-tuning的对照。

**W4** [warning] Dou et al. (2019/2022) attention forcing的区分讨论不够深入
- 具体位置：Section 2（Related Work）第3段
- 问题：Dou et al.的attention forcing直接监督attention distributions以减轻training-inference mismatch——这与本文的auxiliary GAR loss在概念上非常接近。论文列举了三点区别（self-attention vs cross-attention, multi-turn vs NMT, auxiliary vs primary），但没有讨论：(1) Dou et al.是否也观察到了attention forcing在AR下的退化？(2) 本文的发现是否可以retrospectively解释attention forcing的效果或局限？这种deeper engagement会增强novelty positioning。
- 建议：增加1-2句话讨论与attention forcing的deeper conceptual connection。

---

## 小问题（不影响接收）

- **M1**: Figure 1有6个子图（a-d），信息密度很高，print size下文字可能难以阅读。建议简化或分拆。
- **M2**: Abstract的footnote（匿名代码链接）虽然符合惯例，但在abstract正文中放footnote不太常见，考虑移到Introduction。
- **M3**: 论文总长34页（正文8 + 参考文献2 + 附录24），附录篇幅非常大。部分附录内容（如Appendix O: Per-Turn AR GAR Decay, Appendix P: Per-Head KL Divergence Analysis）提供了valuable details，但有些内容可能可以压缩。
- **M4**: Section 3.4的五路对比设计描述清晰，但可以考虑用一个小的示意图来更直观地展示exclusion chain的逻辑。
- **M5**: "8–17×"这个数字在论文中出现多次（Abstract、Introduction、Table 1 caption），略有重复感。

---

## Novelty 验证结果

1. **"To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives"**: 经过文献搜索验证，**这个claim基本成立**。我未找到任何先前工作专门研究auxiliary attention loss在multi-turn transformer AR generation下的exposure bias。UBARv2（2022）研究task-oriented dialogue的exposure bias但使用不同方法。Dou et al.的attention forcing工作（2019/2022）在NMT上监督attention但未分析TF-AR gap。
2. **Scheduled sampling首次应用于auxiliary attention objectives in multi-turn**: 成立。Mihaylova & Martins (2019)将SS扩展到transformer但仅用于single-turn NMT的primary loss。
3. **Li et al. (2024) split-softmax引用**: 经搜索确认为"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs"（arXiv:2402.10962），确实讨论instruction instability。是否提出"split-softmax"作为remedy需要进一步核实。
4. **Qiu et al. (2025) Gated Attention**: 正确引用，NeurIPS 2025 Oral。ThreadGate与之的区别（conditioning on turn position）已充分讨论。
5. **Dongre et al. (2026) GAR metric**: 正确引用，是本文的foundation work。

**潜在遗漏的相关工作**：
- 未发现严重遗漏。论文的Related Work覆盖了dialogue coherence、gating manipulation、exposure bias三个方向的关键工作。
- 可以考虑讨论"Self Forcing"（2025, video generation领域）作为bridging TF-AR gap的最新方法，但这是vision领域的工作，不讨论也完全可以。

---

## 主要优势

1. **研究问题清晰且genuinely novel**：exposure bias是否影响auxiliary attention objectives——这个问题此前未被系统研究过。
2. **实验设计严谨**：五路对比将变量逐一隔离，方法论上优于简单的baseline对比。
3. **统计严谨性高**：bootstrap CI、Wilcoxon signed-rank tests、multi-seed validation（SS）、per-category breakdown。
4. **附录极为详尽**：24页附录提供了完整的reproducibility details，包括loss formulation search history（Appendix B）、per-seed results（Appendix T）、gradient conflict分析（Appendix L）等。
5. **Cross-model validation**：在Qwen和Llama两个架构上验证，虽然只有一个数据集。
6. **写作质量整体良好**：逻辑清晰，claim与evidence的对应关系明确。
7. **Negative result的科学价值**：论文本质上是一个well-characterized negative result（auxiliary attention losses fail under AR），对该领域有warning value。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文页数 | ✅ 8页 | Sections 1-7 + Limitations在第8页结束 |
| Abstract字数 | ✅ ~191词 | 在200词限制内（不含footnote） |
| Limitations章节 | ✅ | 在正文内，一段覆盖4个点（model scale, single dataset, single seed, single loss family） |
| 匿名化 | ✅ | "Anonymous ACL submission"，匿名代码仓库 |
| 引用格式 | ✅ | parenthetical/textual citations使用一致 |
| Appendix无Limitations | ✅ | 附录中无单独Limitations section |
| AI Use声明 | ✅ | Appendix Z（page 33-34）声明使用Claude |

---

**总结**：这是一篇实证基础扎实、发现genuinely novel的诊断性论文。主要顾虑是：(1) "causal exclusion"措辞过强需修正；(2) 单一数据集限制generalizability；(3) GAR与实际downstream impact的link需要更多evidence。如果作者能在rebuttal中提供至少一个额外数据集的验证（即使是pilot scale），并修正overclaim的措辞，论文有潜力达到Conference水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-25T21:25:31.695211+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条阅读 Reviewer 2 的审稿意见，对每个问题用 `[AGREE]` 或 `[REBUT]` 回应，并附简要理由。特别关注你们之间的共识和分歧。\n\n---\n\n以下是 Reviewer 2 的完整审稿：\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] \"Causal exclusion\"措辞过强，与实际方法论不匹配\n- Abstract第3句、Section 1 Contribution 2、Section 5.2标题\n- 实际方法是消融排除法，不是严格因果推断。PCGrad排除了gradient direction conflict但没排除gradient magnitude imbalance的所有形式。Limitations承认未排除KV cache drift。SS只部分修复（Llama 2.9×），说明可能有其他因素。\n- 建议改为\"systematic exclusion of alternative explanations\"或\"diagnostic exclusion chain\"\n\n**N2** [critical] 单一数据集限制了generalizability claim\n- 所有实验在UltraChat 8K上，没有MT-Bench/LMSYS-Chat/ShareGPT验证。Abstract说\"spanning two architectures\"给人跨多设置的感觉，但只是同一数据集两个模型。\n\n### Should-Fix\n\n**W1** GAR与下游任务性能关联不足——instruction retention只有content constraints显著改善(+23.8pp)，format/count/position几乎无变化。PPL在所有配置下几乎相同(2.78)。\n\n**W2** SS在Llama上效果有限(2.9×gap)——Abstract中\"substantially\"模糊了这个事实。\n\n**W3** 仅LoRA fine-tuning，未验证full fine-tuning——LoRA限制了模型重组attention patterns的capacity。\n\n**W4** Dou et al. attention forcing的区分讨论不够深入——未讨论Dou et al.是否也观察到AR下退化，以及本文发现能否解释attention forcing的效果/局限。\n\n### Minor\n\n- M1: Figure 1信息密度过高\n- M2: Abstract中footnote不常见\n- M3: 附录24页偏大\n- M4: 五路对比可加示意图\n- M5: \"8-17×\"数字重复感\n\n### Novelty验证\n- \"首次实证exposure bias崩塌auxiliary attention objectives\"基本成立\n- SS首次应用于auxiliary attention objectives成立\n- 未发现严重相关工作遗漏\n\n### 主要优势\n研究问题novel、实验设计严谨、统计规范、附录详尽、cross-model validation、写作质量好、negative result有科学价值\n\n---\n\n请对以上每个 Must-Fix、Should-Fix、Minor 问题逐条给出 [AGREE] 或 [REBUT]，并说明理由。",
  "reviewer_id": "1",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条阅读 Reviewer 2 的审稿意见，对每个问题用 `[AGREE]` 或 `[REBUT]` 回应，并附简要理由。特别关注你们之间的共识和分歧。\n\n---\n\n以下是 Reviewer 2 的完整审稿：\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] \"Causal exclusion\"措辞过强，与实际方法论不匹配\n- Abstract第3句、Section 1 Contribution 2、Section 5.2标题\n- 实际方法是消融排除法，不是严格因果推断。PCGrad排除了gradient direction conflict但没排除gradient magnitude imbalance的所有形式。Limitations承认未排除KV cache drift。SS只部分修复（Llama 2.9×），说明可能有其他因素。\n- 建议改为\"systematic exclusion of alternative explanations\"或\"diagnostic exclusion chain\"\n\n**N2** [critical] 单一数据集限制了generalizability claim\n- 所有实验在UltraChat 8K上，没有MT-Bench/LMSYS-Chat/ShareGPT验证。Abstract说\"spanning two architectures\"给人跨多设置的感觉，但只是同一数据集两个模型。\n\n### Should-Fix\n\n**W1** GAR与下游任务性能关联不足——instruction retention只有content constraints显著改善(+23.8pp)，format/count/position几乎无变化。PPL在所有配置下几乎相同(2.78)。\n\n**W2** SS在Llama上效果有限(2.9×gap)——Abstract中\"substantially\"模糊了这个事实。\n\n**W3** 仅LoRA fine-tuning，未验证full fine-tuning——LoRA限制了模型重组attention patterns的capacity。\n\n**W4** Dou et al. attention forcing的区分讨论不够深入——未讨论Dou et al.是否也观察到AR下退化，以及本文发现能否解释attention forcing的效果/局限。\n\n### Minor\n\n- M1: Figure 1信息密度过高\n- M2: Abstract中footnote不常见\n- M3: 附录24页偏大\n- M4: 五路对比可加示意图\n- M5: \"8-17×\"数字重复感\n\n### Novelty验证\n- \"首次实证exposure bias崩塌auxiliary attention objectives\"基本成立\n- SS首次应用于auxiliary attention objectives成立\n- 未发现严重相关工作遗漏\n\n### 主要优势\n研究问题novel、实验设计严谨、统计规范、附录详尽、cross-model validation、写作质量好、negative result有科学价值\n\n---\n\n请对以上每个 Must-Fix、Should-Fix、Minor 问题逐条给出 [AGREE] 或 [REBUT]，并说明理由。",
    "reviewer_id": "1",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-25T21:25:44.309518+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12614
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-25T21:25:44.410208+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条阅读 Reviewer 1 的审稿意见，对每个问题用 `[AGREE]` 或 `[REBUT]` 回应，并附简要理由。特别关注你们之间的共识和分歧。\n\n---\n\n以下是 Reviewer 1 的完整审稿：\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness: 3/5 | Excitement: 3.5/5 | Reproducibility: 4/5**\n\n### Must-Fix（3个）\n\n**C1** 因果排除链未封闭——PCGrad仅排除梯度方向冲突，未测试梯度幅值重缩放（NTP幅值压倒GAR 7.5–14.7×），λ_GAR rescaling实验缺失\n\n**C2** GAR下游有效性弱——r=0.200仅解释4%下游方差，β-steering的instruction retention效果p=0.077不显著\n\n**C3** 跨模型验证不足——Llama仅3/5条件、N=20、单种子、median报告与Qwen mean不可比\n\n### Should-Fix（4个）\n\n**S1** β-steering部分循环论证\n\n**S2** SS替代解释未排除\n\n**S3** Qwen/Llama报告标准不一致\n\n**S4** loss formulation搜索的过拟合风险\n\n### 主要优势\n研究问题新颖、五路排除设计有方法论贡献、26页附录扎实、Qwen主实验统计规范、SS应用有实用价值\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 问题逐条给出 [AGREE] 或 [REBUT]，并说明理由。特别注意：\n\n1. R1的C1（gradient magnitude imbalance未排除）与你的N1（causal exclusion措辞过强）是否指向同一根本问题？\n2. R1的C2（GAR下游有效性弱，r=0.200）与你的W1（GAR-downstream link不足）的严重性判断是否一致？\n3. R1的C3（跨模型验证不足）与你的N2（单一数据集）各指向不同维度的scope限制，你如何看待两者的相对重要性？",
  "reviewer_id": "2",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条阅读 Reviewer 1 的审稿意见，对每个问题用 `[AGREE]` 或 `[REBUT]` 回应，并附简要理由。特别关注你们之间的共识和分歧。\n\n---\n\n以下是 Reviewer 1 的完整审稿：\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness: 3/5 | Excitement: 3.5/5 | Reproducibility: 4/5**\n\n### Must-Fix（3个）\n\n**C1** 因果排除链未封闭——PCGrad仅排除梯度方向冲突，未测试梯度幅值重缩放（NTP幅值压倒GAR 7.5–14.7×），λ_GAR rescaling实验缺失\n\n**C2** GAR下游有效性弱——r=0.200仅解释4%下游方差，β-steering的instruction retention效果p=0.077不显著\n\n**C3** 跨模型验证不足——Llama仅3/5条件、N=20、单种子、median报告与Qwen mean不可比\n\n### Should-Fix（4个）\n\n**S1** β-steering部分循环论证\n\n**S2** SS替代解释未排除\n\n**S3** Qwen/Llama报告标准不一致\n\n**S4** loss formulation搜索的过拟合风险\n\n### 主要优势\n研究问题新颖、五路排除设计有方法论贡献、26页附录扎实、Qwen主实验统计规范、SS应用有实用价值\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 问题逐条给出 [AGREE] 或 [REBUT]，并说明理由。特别注意：\n\n1. R1的C1（gradient magnitude imbalance未排除）与你的N1（causal exclusion措辞过强）是否指向同一根本问题？\n2. R1的C2（GAR下游有效性弱，r=0.200）与你的W1（GAR-downstream link不足）的严重性判断是否一致？\n3. R1的C3（跨模型验证不足）与你的N2（单一数据集）各指向不同维度的scope限制，你如何看待两者的相对重要性？",
    "reviewer_id": "2",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-25T21:25:45.821693+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1411
}
```

</details>

---


### Assistant

_source line 534 · 2026-05-25T21:25:55.257747+00:00_

交叉分享已发出。两位 Reviewer 正在审阅对方的意见并准备 [AGREE]/[REBUT] 回应。

初步观察——两位 Reviewer 存在明显共识的区域：
- **因果排除措辞过强**：R1（C1 gradient magnitude未排除）和 R2（N1 "causal exclusion"措辞）指向同一根本问题
- **GAR 下游有效性弱**：R1（C2, r=0.200）和 R2（W1, PPL无差异+instruction retention局部）高度重叠
- **跨模型/跨数据集 scope 不足**：R1（C3 Llama验证不足）和 R2（N2 单一数据集）从不同角度指出 generalizability 限制

等待两位 Reviewer 的交叉回应后，将进入报告合成阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 535 · 2026-05-25T21:25:57.816691+00:00_

[Reviewer 2 审稿结果]:
审稿完成。

**核心结论**：Overall 3.5/5（Borderline Conference）。论文提出了一个genuinely novel的实证发现——exposure bias导致auxiliary attention loss在AR generation下崩塌——实验设计严谨（五路因果排除链），附录详尽（24页）。

**两个Must-Fix**：
1. "Causal exclusion"措辞过强，实际是消融排除法，建议改为"diagnostic exclusion chain"
2. 单一数据集（仅UltraChat）限制了generalizability，需至少一个额外数据集验证

**四个Should-Fix**：GAR与downstream性能的弱关联、Llama上SS仍有2.9×残留gap但表述模糊、仅LoRA未测full fine-tuning、与Dou et al. attention forcing的deeper engagement不足。

审稿意见已提交至 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 536 · 2026-05-25T21:26:05.778708+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 46

## Round 46

14 recorded events


### User

_source line 537 · 2026-05-25T21:27:02.921284+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

## Must-Fix

**[AGREE] R2-N1: "Causal exclusion"措辞过强**

同意。我的 N1 从实质层面提出了相同问题——PCGrad 仅排除梯度方向冲突，未排除梯度幅值失衡（NTP 压倒 GAR 7.5–14.7×, Appendix J）。R2 从术语精确性的角度切入，我从方法论完备性的角度切入，结论一致：论文的排除链不是严格因果推断，不应使用"causal exclusion"这一暗示 interventionist causal inference 的表述。"Diagnostic exclusion chain"或"systematic ablation-based exclusion"更准确。补充一点：即便改措辞，实质问题仍在——λ_GAR rescaling 实验的缺失使得 exposure bias 归因无法与梯度幅值淹没假说区分（详见我的 N1）。

**[REBUT] R2-N2: 单一数据集应为 Must-Fix**

部分同意结论，不同意严重级别。理由：
1. 本文定位是**诊断/分析论文**（diagnosing exposure bias collapse mechanism），不是提出新训练方法要求广泛 benchmark 验证。对于诊断性研究，在一个受控数据集上深入分析比在多个数据集上浅层验证更有价值。
2. UltraChat 覆盖了 18 种对话类型（Table 23, Appendix G），domain diversity 在单数据集内已有一定保障。论文 Appendix D 还有 N=5 的 10-turn 长对话评测，虽然样本小但提供了 length 维度的补充。
3. 跨数据集泛化（MT-Bench/ShareGPT）是有意义的扩展，但对于"exposure bias 导致 TF-AR gap"这一机制性发现，该机制依赖于 training dynamics（teacher forcing vs autoregressive），不太可能因为数据集不同而消失。
4. **建议降级为 Should-Fix**，要求作者在 Limitations 中明确讨论单数据集限制对 generalizability 的影响，并在 future work 中承诺跨数据集验证。

---

## Should-Fix

**[AGREE] R2-W1: GAR 与下游任务关联不足，per-category 分化**

强烈同意，且我认为这个问题的严重程度应该更高。我在自己的审稿中将此列为 **Must-Fix (N2)**。R2 提供了重要的补充细节：Appendix C Table 4 显示只有 content constraints 显著改善（+23.8pp），而 format（+6.7pp）、count（0）、position（0）几乎无变化。这说明 β-steering 的下游效果不仅整体弱（p=0.077），而且高度 category-specific——它只对需要"sustained attention to goal tokens"的约束类型有效，对程序性约束（格式、计数）无效。这进一步削弱了 GAR 作为通用 diagnostic 的有效性论证。

**[AGREE] R2-W2: SS 在 Llama 上残留 2.9× gap，"substantially"模糊**

同意。Abstract 用"substantially"描述 Llama 结果是不精确的。2.9× 的残留 gap 意味着 SS 在 Llama 上**没有**解决问题——如果 exposure bias 是 primary cause 且 SS 直接针对 exposure bias，为什么 Llama 上残留 gap 是 Qwen 的 2.2 倍（2.9× vs 1.3×）？这要么说明 (a) Llama 上有其他因素在起作用（如 GQA/RoPE 等架构差异），要么 (b) SS 的效果依赖于架构特性，不像论文暗示的那样通用。这也与我的 W3（跨模型报告标准不一致）相关——Llama 用 median 报告放大了 baseline gap（27×），可能使 compression ratio 看起来更大。建议 Abstract 改为具体数字："compressing the gap from 7.8× to 1.3× on Qwen and from 27× to 2.9× (median) on Llama"。

**[AGREE] R2-W3: 仅 LoRA fine-tuning，未验证 full fine-tuning**

同意方向，但认为严重程度适中。LoRA 对 7B 模型是标准实践，full fine-tuning 成本高且不一定是必要的。但 R2 的核心洞察是对的：LoRA 限制了模型重组 attention patterns 的 capacity，这可能 confound 因果排除链中的 capacity 排除步骤——Base→LoRA-only 比较本意是排除 parameter capacity，但如果 LoRA 本身就限制了 attention 重组能力，那这个排除步骤测试的不是"更多参数是否有帮助"，而是"LoRA 形式的有限参数是否有帮助"。建议在 Limitations 中讨论。

**[AGREE] R2-W4: Dou et al. attention forcing 讨论不够**

同意。Dou et al. (2024) 的 attention forcing 是最直接的相关工作——都涉及在训练时引导 attention patterns。论文应讨论：(1) Dou et al. 是否在 AR 场景下观察到类似的 attention collapse？(2) 本文的 exposure bias 诊断是否能解释 attention forcing 在 AR 下的效果/局限？(3) ThreadGate 与 attention forcing 的方法论差异和互补性。缺少这个讨论让 Related Work 的完整性打折。

---

## Minor

**[AGREE] R2-M1: Figure 1 信息密度过高**

同意，我在自己的审稿 minor point 2 中也提出了相同意见。Table 1 字体极小，建议独立排版。

**[REBUT] R2-M2: Abstract 中 footnote 不常见**

不同意这是问题。ACL/EMNLP 模板允许 abstract 中使用 footnote，多篇已发表论文有先例（尤其是标注 code/data availability 或 equal contribution 的脚注）。ARR 投稿规则中没有禁止 abstract footnote 的条款。

**[REBUT] R2-M3: 附录 24 页偏大**

不同意。EMNLP 2026 对附录没有页数限制。24 页附录包含完整的统计检验、per-seed 结果、消融实验、梯度分析等，恰恰是方法严谨性的体现。ARR reviewer guidelines 明确指出不应因附录篇幅惩罚作者（reviewer 不被要求阅读全部附录）。我认为详尽的附录是本文的**优势**而非弱点。

**[AGREE] R2-M4: 五路对比可加示意图**

同意。当前五路排除链的逻辑仅通过文字（§3.4）传达，一个简洁的 flow diagram 显示 "Base → (+capacity) → LoRA-only → (+gating) → UG → (+conditioning) → TG → (+PCGrad) → exclude direction conflict → (+SS) → exposure bias" 会大幅提高可读性。

**[REBUT] R2-M5: "8-17×" 数字重复感**

不同意这是问题。"8-17×"是核心结果的 effect size range，在 Abstract、Introduction、Results 中重复是科学写作的正常实践——确保 skim reader 在任何章节都能获取关键数字。重复关键数据不等于冗余。

---

## 共识总结

R1 和 R2 在以下关键判断上一致：
1. **因果排除链不完备**（R1-N1 + R2-N1）：PCGrad 未排除梯度幅值假说，"causal exclusion"措辞过强
2. **GAR 下游有效性弱**（R1-N2 + R2-W1）：r=0.200，per-category 高度分化，p=0.077 不显著
3. **跨模型验证不足**（R1-N3 + R2-W2）：Llama 排除链断裂，SS 残留 2.9× gap
4. **Overall 评分一致**：均为 3.5（Borderline Conference）

## 分歧点

| 问题 | R1 | R2 | 说明 |
|------|----|----|------|
| 单数据集 | Should-Fix | Must-Fix | R1 认为诊断性研究可接受单数据集，R2 认为影响 generalizability claim |
| 附录篇幅 | 优势 | Minor 问题 | R1 认为详尽附录是严谨性体现 |
| Abstract footnote | 合规 | 不常见 | ACL 模板允许 |

## 对 Overall 评分的影响

R2 的审稿意见未改变我的 Overall 判断（3.5）。两位 reviewer 的核心关切高度重合，加强了以下 rebuttal 期望：(1) λ_GAR rescaling 实验结果，(2) Llama 上补全 PCGrad 条件，(3) 措辞从"causal exclusion / primary cause"调整为更审慎的表述。如果 rebuttal 能有效回应这三点，评分可考虑提升至 4.0。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-25T21:27:28.821849+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-25T21:27:29.273814+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6/submitted.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-25T21:15:38.555524+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_640e53b6afbbd5e34eb7273cd5a707a0\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-25T21:27:29.274115+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-25T21:27:29.675944+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:15:37.683613+00:00\", \"completed_at\": \"2026-05-25T21:19:53.815141+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前两页为连续纯文本（Abstract + Introduction + Related Work），无任何 display item。第一个视觉锚点（Figure 1）出现在第 3 页顶部。虽在 3 页限制内，但审稿人翻过两整页纯文字才看到第一张图，第一印象略弱。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 作为首个 display item 传达核心 message 有效：三面板分别展示 GAR 衰减、TF/AR gap 持续存在、SS 压缩 gap，与 Title-Abstract 故事一致。全宽排布合理。Table 1 紧随其下，booktabs 风格，最优值加粗，格式专业。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Table 1 的 95% CI 列格式整洁，数值精度一致（小数点后 2-3 位）。最优结果加粗标注到位。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 为单栏图，面积较小但文字可读。Y 轴标签 \\\"GAR-ours\\\" 和图例清晰。配色使用柔和色调，符合项目要求。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"纯文本+公式页（Sections 3.3-4.1），公式渲染正确，无 LaTeX 残留错误。方程编号连续。训练目标公式排版整洁。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 全宽双面板（β-steering，N=5 和 N=50），线条+置信区间带清晰可读。Figure 4 在右栏，虽小但信息传达完整。两图在同一页形成良好视觉密度。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 5 全宽双面板（gate conditioning），柱状图+散点图组合，配色区分度好。Sections 5.1-5.3 文本穿插合理。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"最后一页主文本。Figure 6（multi-seed bar chart）+ Discussion + Conclusion + Limitations 紧凑排列。Limitations 简短（约一段），符合 EMNLP 要求。页面填充率 >90%，无浪费。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Section 7 Conclusion 和 Limitations 没有孤悬标题问题，每个标题后至少有 2-3 行正文。\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"References 页排版正常，双栏均匀，无 [?] 未解析引用，无明显截断或 overfull。格式统一。\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Appendix 开始。Table 2（超参数表）booktabs 风格，整洁。\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Table 3（Loss formulation i
…[truncated 1489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-25T21:27:29.827758+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "artifacts/review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "turn_residual_gating",
    "file": "artifacts/review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-25T21:27:29.878532+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-25T21:27:33.648084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-25T21:27:33.701179+00:00_

1	# Review Issues Tracker — turn_residual_gating
2	# Round 1 (2026-05-19, dream_20260519T145320)
3	# Round 2 (2026-05-22, fresh re-review of revised paper)
4	# Round 3 (2026-05-22, fresh re-review)
5	# Round 4 (2026-05-25, fresh re-review)
6	# Round 5 (2026-05-25, fresh re-review — current round)
7	# Cross-response phase completed: R1↔R2 convergence reached
8	
9	# ============================================================
10	# Issues from Round 1 — status updates through Round 5
11	# ============================================================
12	
13	- id: "R1-N1"
14	  summary: "所有引用渲染为 '?'——bibliography 编译失败"
15	  category: format
16	  severity: info
17	  status: resolved
18	  first_raised_round: 1
19	  last_seen_round: 1
20	  mentions:
21	    - round: 1
22	      reviewers: [1, 2]
23	      note: "Dream paper artifact。"
24	    - round: 2
25	      reviewers: []
26	      note: "视觉审查确认无 [?] 未解析引用。已修复。"
27	  action_items:
28	    - round: 1
29	      action: "Paper Agent 确保 bibtex 编译正确"
30	      assigned_to: paper_agent
31	      status: done
32	  resolution: "Round 2 视觉审查确认已修复。"
33	  resolution_round: 2
34	
35	- id: "R1-N2"
36	  summary: "单种子支撑结论——统计功效不足 + AR 评估 N=5 过小"
37	  category: experiment
38	  severity: warning
39	  status: in_progress
40	  first_raised_round: 1
41	  last_seen_round: 5
42	  mentions:
43	    - round: 1
44	      reviewers: [1, 2]
45	      note: "Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。"
46	    - round: 2
47	      reviewers: [1, 2]
48	      note: "ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。"
49	    - round: 3
50	      reviewers: [1, 2]
51	      note: "AR 评估仅 N=5，核心 claim 缺统计检验。"
52	    - round: 4
53	      reviewers: [1, 2]
54	      note: "两位 Reviewer 独立列为 Critical Must-Fix。"
55	    - round: 5
56	      reviewers: [1, 2]
57	      note: "Director 裁定降为 Should-Fix（效应量 8-17× 远超种子方差）。Phase 1A multi-seed 训练中。"
58	  action_items:
59	    - round: 1
60	      action: "plan_019: seed=123 extra training"
61	      assigned_to: agent
62	      status: do
…[truncated 22518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-25T21:30:59.602921+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "turn_residual_gating",
  "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review)\n# Round 4 (2026-05-25, fresh re-review)\n# Round 5 (2026-05-25, fresh re-review)\n# Round 6 (2026-05-25, fresh re-review — current round)\n# Cross-response phase completed: R1↔R2 convergence reached\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 6\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足 + AR 评估 N=5 过小\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 评估仅 N=5，核心 claim 缺统计检验。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立列为 Critical Must-Fix。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Director 裁定降为 Should-Fix（效应量 8-17× 远超种子方差）。Phase 1A multi-seed 训练中。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R6 未作为独立 Must-Fix 提出，但 R1-C3 指出 Llama 单种子问题。维持 Should-Fix。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 4\n      action: \"AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件\"\n      assigned_to: agent\n      status: in_progress\n    - round: 5\n      action: \"Phase 1A multi-seed 训练进行中（5 条件 × 3 seeds）\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"额外问题：mean/median 未双报。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Should-Fix。R2 建议标题改为 Cross-Model Replication。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仅 3/5 条件削弱 cross-model generality。Phase 1B Llama PCGrad+UG 排队。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-C3 指出 Llama 仅 3/5 条件、N=20、单种子、median 与 Qwen mean 不可比。R2 交叉同意。\"\n  action_items:\n    - round: 2\n      action: \"补充 Llama PCGrad+UG 训练+评估\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"写作降级：§5.5 标题→Cross-Model Replication + mean/median 双报\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-C1 明确要求 λ_GAR rescaling 实验——NTP 幅值压倒 GAR 7.5-14.7×，未测试 rescaling 使排除链不完整。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"λ_GAR rescaling 实验：测试 λ_GAR 放大至 NTP/GAR magnitude parity\"\n      assigned_to: agent\n      status: open\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n  action_items: []\n  resolution: \"Figure 1-6 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"SS 贡献 ~8.5× 提升。ThreadGate 贡献边际。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"SS Llama 残留 2.9× gap 说明 exposure bias 可能非唯一因素。Abstract 'substantially' 模糊。\"\n  action_items:\n    - round: 4\n      action: \"3 seeds (s42/s123/s456) + mean±std\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2 — status updates through Round 6\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——contribution 措辞需调整\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 4\n      reviewers: [2]\n      note: \"'to our knowledge, the first' 仍被质疑。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"因果排除链不完整（KV cache drift + NTP magnitude imbalance 未排除）。强共识 Must-Fix。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"[复发 ×6 轮] 'causal exclusion' 措辞强共识必须修改。R1 从方法论（magnitude未排除），R2 从术语精确性（非interventionist causal inference）。建议→'diagnostic exclusion chain'/'systematic ablation-based exclusion'。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 4\n      action: \"GAR 重新定位为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"Phase 2 switching 实验 + exposure bias 降级为 'a proximal cause'\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"[复发 ×6 轮] Abstract/§1/§5.2: 'causal exclusion'→'diagnostic exclusion chain' or 'systematic ablation-based exclusion'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"'Destroys' 与 r²=0.04 不匹配。需降调。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"维持 Should-Fix。标题需降调以匹配 evidence 强度。\"\n  action_items:\n    - round: 5\n      action: \"标题 'Destroys' → 'Collapses'（描述 attention 行为而非下游灾难）\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"arXiv 原文验证确认。Critical Must-Fix。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。待确认修复状态。\"\n  action_items:\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因——替代假说讨论不足\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 降 Should-Fix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"PCGrad 失败可能反映投影副作用。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[复发 ×4 轮] 强共识 Must-Fix。KV cache drift + Appendix L 非独立验证。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"[复发 ×5 轮] R1 交叉回应明确：λ_GAR rescaling 缺失使 exposure bias 归因无法与梯度幅值淹没假说区分。SS Llama 2.9× 残留进一步说明可能有其他因素。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"§6 扩展 exposure bias 讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 5\n      action: \"Phase 2 switching 实验区分 exposure bias vs KV cache drift\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"λ_GAR rescaling 实验 + NTP magnitude imbalance 显式讨论 + 'a proximal cause' 降级\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标——instruction retention 不显著但占页过多\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"McNemar p=0.077 不显著。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200 的 95% CI ≈ [0.05, 0.35] 过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[复发 ×5 轮] 升级为 Must-Fix。r²=0.04 仅解释 4% 下游方差。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"[复发 ×6 轮] R2 补充：per-category 高度分化——仅 content constraints +23.8pp 显著，format/count/position 无变化。R1 交叉回应强烈同意并认为应升级。\"\n  action_items:\n    - round: 4\n      action: \"重新定位 GAR 为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"标题 Destroys→Collapses + 叙事重构\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"正文明确讨论 GAR 作为 proxy metric 的局限性（per-category 分化 + r²=0.04）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Raposo et al. 缺 ICML 2024 venue；Gromov et al. 年份问题。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 4\n      action: \"统一 bib 格式\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"论文 p.1 Abstract 已有 anonymous.4open.science 链接。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: done\n  resolution: \"论文 p.1 已有匿名代码链接。\"\n  resolution_round: 5\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 AR 列需扩容\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"与 R1-N2 联动，AR 列需 N≥50 + CI。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 4\n      action: \"AR 列更新为 N≥50 数据 + CI + GAR-D + PPL\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字重复 8+ 次\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"仍存在。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1 交叉回应 rebut——认为核心 effect size 在 Abstract/Intro/Results 重复是正常科学写作。\"\n  action_items:\n    - round: 5\n      action: \"Abstract/§4.2 保留完整数字，其余改用回指\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 泛化声称\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"'to our knowledge, the first' 仍被质疑。合并至 R2-N1 追踪。\"\n  action_items:\n    - round: 4\n      action: \"删除泛化声称，合并至 R2-N1\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. split-softmax 缺实验对比\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Discussion 定性讨论即可，不做实验对比。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 中加强 split-softmax/Rhea 概念对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure/Table caption overclaim + 重复句\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 6\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 3\n      action: \"修正 Fig 3b/Table 1/Fig 4 caption\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后数字更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 6\n      reviewers: []\n      note: \"仍待 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后统一更新\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 6\n      reviewers: []\n      note: \"SS 统计支撑仍为核心问题。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance\"\n      assigned_to: director\n      status: open\n\n# ============================================================\n# Issues from Round 3 — status updates through Round 6\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Round 4 确认页数合规。\"\n  resolution_round: 4\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad scope 过度概括\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"NTP magnitude imbalance 7.5-14.7× 是 PCGrad 失败的替代解释。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 交叉回应：即便改 'causal exclusion' 措辞，λ_GAR rescaling 缺失仍是实质问题。\"\n  action_items:\n    - round: 3\n      action: \"'gradient conflict' → 'gradient direction conflict'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"补充 1 句：PCGrad 不处理 magnitude imbalance\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869) 引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"与 split-softmax 一并作为缺失对比方案。合并至 R2-W7-new。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 概念对比中一并覆盖 Rhea\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 未讨论\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1 (Q4)。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W3 新增：LoRA 限制模型重组 attention patterns capacity，可能 confound capacity 排除步骤。R1 交叉同意。\"\n  action_items:\n    - round: 5\n      action: \"§7 Limitations 加 1 句 acknowledge LoRA rank 16 可能影响 gate 效用上界\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"Limitations 扩展：LoRA-only 实验限制了 capacity 排除步骤的推断力度\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  action_items:\n    - round: 3\n      action: \"确认准确性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R3-NEW-1\"\n  summary: \"UG 描述不清——未说明仍为可学习 MLP\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  action_items:\n    - round: 3\n      action: \"§4.1 或 §3 加一句说明\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-NEW-2\"\n  summary: \"Contribution (4) 混淆开发迭代与系统消融\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  action_items:\n    - round: 3\n      action: \"拆分为 loss design iterations + systematic conditions comparison\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Issues from Round 4 — status updates through Round 6\n# ============================================================\n\n- id: \"R4-N1\"\n  summary: \"GAR 指标与下游任务性能之间缺乏因果验证\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200, r²=0.04。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Director 裁定 Must-Fix。与 R2-W3 合并追踪。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 补充 per-category 分化证据。R1 交叉强烈同意。维持 Must-Fix。\"\n  action_items:\n    - round: 5\n      action: \"标题 Destroys→Collapses + GAR 叙事重构\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"正文讨论 GAR proxy 局限 + per-category 分化\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-N2\"\n  summary: \"SS+LoRA-only 消融缺失——ThreadGate 独立贡献不清\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"关键缺失消融。\"\n  action_items:\n    - round: 5\n      action: \"SS+LoRA-only 实验\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R4-W1\"\n  summary: \"GAR-D 全条件接近零——干预仅在 last token 成功\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"§3.1 补充 GAR-ours vs GAR-D 选择理由\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-W2\"\n  summary: \"Table 1 四舍五入与正文数字精度不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  action_items:\n    - round: 4\n      action: \"Table 1 增加一位小数\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W3\"\n  summary: \"r_min 数值正文未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  action_items:\n    - round: 4\n      action: \"在 §3 或 Appendix A 中报告 r_min 数值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-MR1\"\n  summary: \"缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"合并至 R2-W7-new Discussion 概念对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-W4\"\n  summary: \"Appendix C instruction retention 多重比较未校正\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"18-category McNemar's test 缺 FDR/Bonferroni 校正。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未独立提出，但 per-category 分化进一步削弱未校正结果的可信度。\"\n  action_items:\n    - round: 4\n      action: \"Appendix C per-category 分析补充 Holm-Bonferroni 或 FDR 校正\"\n      assigned_to: paper_agent\n      status: open\n\n# ============================================================\n# Round 5 — status updates through Round 6\n# ============================================================\n\n- id: \"R5-SF1\"\n  summary: \"β-steering 部分循环论证——GAR 恢复 vs 下游效果未解耦\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证首次提出。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"boost attention → attention metric recovers 是同义反复。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-S1 维持循环论证判断。\"\n  action_items:\n    - round: 5\n      action: \"§5.4 拆为两段：GAR 恢复标注 'by construction' + 下游效果单独报告\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Round 6 新增\n# ============================================================\n\n- id: \"R6-SF1\"\n  summary: \"单一数据集（仅 UltraChat）限制 generalizability claim\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 列 Must-Fix，R1 rebut 降为 Should-Fix（诊断性论文单数据集可接受，UltraChat 18 种对话类型提供 domain diversity）。Director 裁定 Should-Fix——机制性发现依赖 training dynamics 而非数据，但 Limitations 需明确讨论。\"\n  action_items:\n    - round: 6\n      action: \"Limitations 明确讨论单数据集对 generalizability 的限制 + future work 承诺跨数据集验证\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R6-SF2\"\n  summary: \"SS Llama 残留 2.9× gap——Abstract 'substantially' 措辞模糊\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"强共识。Qwen 1.3× vs Llama 2.9× 差异显著。Abstract 应报告具体数字。可能暗示 Llama 上有 exposure bias 以外的因素。\"\n  action_items:\n    - round: 6\n      action: \"Abstract 改为具体数字：'compressing the gap from 7.8× to 1.3× on Qwen and from 27× to 2.9× (median) on Llama'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R6-SF3\"\n  summary: \"仅 LoRA fine-tuning，未验证 full fine-tuning\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 交叉同意（严重程度适中）。LoRA capacity 限制可能 confound capacity 排除步骤。\"\n  action_items:\n    - round: 6\n      action: \"Limitations 讨论 LoRA-only 限制，或提供 1 个配置 full FT 对照\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R6-SF4\"\n  summary: \"Dou et al. attention forcing 区分讨论不够深入\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出 3 点缺失讨论（AR 退化、retrospective 解释、方法论互补），R1 交叉同意。\"\n  action_items:\n    - round: 6\n      action: \"Related Work 增加 1-2 句 deeper conceptual connection with Dou et al.\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R6-SF5\"\n  summary: \"Loss formulation 搜索（v1-v9）的过拟合风险\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-S4: 9 次迭代选 loss formulation 可能对 UltraChat 数据集过拟合。\"\n  action_items:\n    - round: 6\n      action: \"Appendix B 或 Limitations 讨论 loss search 可能的 overfitting risk\"\n      assigned_to: paper_agent\n      status: open\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "turn_residual_gating",
    "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review)\n# Round 4 (2026-05-25, fresh re-review)\n# Round 5 (2026-05-25, fresh re-review)\n# Round 6 (2026-05-25, fresh re-review — current round)\n# Cross-response phase completed: R1↔R2 convergence reached\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 6\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足 + AR 评估 N=5 过小\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 评估仅 N=5，核心 claim 缺统计检验。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立列为 Critical Must-Fix。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Director 裁定降为 Should-Fix（效应量 8-17× 远超种子方差）。Phase 1A multi-seed 训练中。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R6 未作为独立 Must-Fix 提出，但 R1-C3 指出 Llama 单种子问题。维持 Should-Fix。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 4\n      action: \"AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件\"\n      assigned_to: agent\n      status: in_progress\n    - round: 5\n      action: \"Phase 1A multi-seed 训练进行中（5 条件 × 3 seeds）\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"额外问题：mean/median 未双报。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Should-Fix。R2 建议标题改为 Cross-Model Replication。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仅 3/5 条件削弱 cross-model generality。Phase 1B Llama PCGrad+UG 排队。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-C3 指出 Llama 仅 3/5 条件、N=20、单种子、median 与 Qwen mean 不可比。R2 交叉同意。\"\n  action_items:\n    - round: 2\n      action: \"补充 Llama PCGrad+UG 训练+评估\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"写作降级：§5.5 标题→Cross-Model Replication + mean/median 双报\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-C1 明确要求 λ_GAR rescaling 实验——NTP 幅值压倒 GAR 7.5-14.7×，未测试 rescaling 使排除链不完整。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"λ_GAR rescaling 实验：测试 λ_GAR 放大至 NTP/GAR magnitude parity\"\n      assigned_to: agent\n      status: open\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n  action_items: []\n  resolution: \"Figure 1-6 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"SS 贡献 ~8.5× 提升。ThreadGate 贡献边际。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"SS Llama 残留 2.9× gap 说明 exposure bias 可能非唯一因素。Abstract 'substantially' 模糊。\"\n  action_items:\n    - round: 4\n      action: \"3 seeds (s42/s123/s456) + mean±std\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2 — status updates through Round 6\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——contribution 措辞需调整\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 4\n      reviewers: [2]\n      note: \"'to our knowledge, the first' 仍被质疑。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"因果排除链不完整（KV cache drift + NTP magnitude imbalance 未排除）。强共识 Must-Fix。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"[复发 ×6 轮] 'causal exclusion' 措辞强共识必须修改。R1 从方法论（magnitude未排除），R2 从术语精确性（非interventionist causal inference）。建议→'diagnostic exclusion chain'/'systematic ablation-based exclusion'。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 4\n      action: \"GAR 重新定位为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"Phase 2 switching 实验 + exposure bias 降级为 'a proximal cause'\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"[复发 ×6 轮] Abstract/§1/§5.2: 'causal exclusion'→'diagnostic exclusion chain' or 'systematic ablation-based exclusion'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"'Destroys' 与 r²=0.04 不匹配。需降调。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"维持 Should-Fix。标题需降调以匹配 evidence 强度。\"\n  action_items:\n    - round: 5\n      action: \"标题 'Destroys' → 'Collapses'（描述 attention 行为而非下游灾难）\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"arXiv 原文验证确认。Critical Must-Fix。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。待确认修复状态。\"\n  action_items:\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因——替代假说讨论不足\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 降 Should-Fix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"PCGrad 失败可能反映投影副作用。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[复发 ×4 轮] 强共识 Must-Fix。KV cache drift + Appendix L 非独立验证。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"[复发 ×5 轮] R1 交叉回应明确：λ_GAR rescaling 缺失使 exposure bias 归因无法与梯度幅值淹没假说区分。SS Llama 2.9× 残留进一步说明可能有其他因素。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"§6 扩展 exposure bias 讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 5\n      action: \"Phase 2 switching 实验区分 exposure bias vs KV cache drift\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"λ_GAR rescaling 实验 + NTP magnitude imbalance 显式讨论 + 'a proximal cause' 降级\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标——instruction retention 不显著但占页过多\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"McNemar p=0.077 不显著。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200 的 95% CI ≈ [0.05, 0.35] 过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[复发 ×5 轮] 升级为 Must-Fix。r²=0.04 仅解释 4% 下游方差。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"[复发 ×6 轮] R2 补充：per-category 高度分化——仅 content constraints +23.8pp 显著，format/count/position 无变化。R1 交叉回应强烈同意并认为应升级。\"\n  action_items:\n    - round: 4\n      action: \"重新定位 GAR 为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"标题 Destroys→Collapses + 叙事重构\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"正文明确讨论 GAR 作为 proxy metric 的局限性（per-category 分化 + r²=0.04）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Raposo et al. 缺 ICML 2024 venue；Gromov et al. 年份问题。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 4\n      action: \"统一 bib 格式\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"论文 p.1 Abstract 已有 anonymous.4open.science 链接。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: done\n  resolution: \"论文 p.1 已有匿名代码链接。\"\n  resolution_round: 5\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 AR 列需扩容\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"与 R1-N2 联动，AR 列需 N≥50 + CI。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 4\n      action: \"AR 列更新为 N≥50 数据 + CI + GAR-D + PPL\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字重复 8+ 次\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"仍存在。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1 交叉回应 rebut——认为核心 effect size 在 Abstract/Intro/Results 重复是正常科学写作。\"\n  action_items:\n    - round: 5\n      action: \"Abstract/§4.2 保留完整数字，其余改用回指\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 泛化声称\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"'to our knowledge, the first' 仍被质疑。合并至 R2-N1 追踪。\"\n  action_items:\n    - round: 4\n      action: \"删除泛化声称，合并至 R2-N1\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. split-softmax 缺实验对比\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Discussion 定性讨论即可，不做实验对比。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 中加强 split-softmax/Rhea 概念对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure/Table caption overclaim + 重复句\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 6\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 3\n      action: \"修正 Fig 3b/Table 1/Fig 4 caption\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后数字更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 6\n      reviewers: []\n      note: \"仍待 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后统一更新\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 6\n      reviewers: []\n      note: \"SS 统计支撑仍为核心问题。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance\"\n      assigned_to: director\n      status: open\n\n# ============================================================\n# Issues from Round 3 — status updates through Round 6\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Round 4 确认页数合规。\"\n  resolution_round: 4\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad scope 过度概括\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"NTP magnitude imbalance 7.5-14.7× 是 PCGrad 失败的替代解释。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 交叉回应：即便改 'causal exclusion' 措辞，λ_GAR rescaling 缺失仍是实质问题。\"\n  action_items:\n    - round: 3\n      action: \"'gradient conflict' → 'gradient direction conflict'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"补充 1 句：PCGrad 不处理 magnitude imbalance\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869) 引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"与 split-softmax 一并作为缺失对比方案。合并至 R2-W7-new。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 概念对比中一并覆盖 Rhea\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 未讨论\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1 (Q4)。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W3 新增：LoRA 限制模型重组 attention patterns capacity，可能 confound capacity 排除步骤。R1 交叉同意。\"\n  action_items:\n    - round: 5\n      action: \"§7 Limitations 加 1 句 acknowledge LoRA rank 16 可能影响 gate 效用上界\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"Limitations 扩展：LoRA-only 实验限制了 capacity 排除步骤的推断力度\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  action_items:\n    - round: 3\n      action: \"确认准确性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R3-NEW-1\"\n  summary: \"UG 描述不清——未说明仍为可学习 MLP\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  action_items:\n    - round: 3\n      action: \"§4.1 或 §3 加一句说明\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-NEW-2\"\n  summary: \"Contribution (4) 混淆开发迭代与系统消融\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  action_items:\n    - round: 3\n      action: \"拆分为 loss design iterations + systematic conditions comparison\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Issues from Round 4 — status updates through Round 6\n# ============================================================\n\n- id: \"R4-N1\"\n  summary: \"GAR 指标与下游任务性能之间缺乏因果验证\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200, r²=0.04。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Director 裁定 Must-Fix。与 R2-W3 合并追踪。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 补充 per-category 分化证据。R1 交叉强烈同意。维持 Must-Fix。\"\n  action_items:\n    - round: 5\n      action: \"标题 Destroys→Collapses + GAR 叙事重构\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"正文讨论 GAR proxy 局限 + per-category 分化\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-N2\"\n  summary: \"SS+LoRA-only 消融缺失——ThreadGate 独立贡献不清\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"关键缺失消融。\"\n  action_items:\n    - round: 5\n      action: \"SS+LoRA-only 实验\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R4-W1\"\n  summary: \"GAR-D 全条件接近零——干预仅在 last token 成功\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"§3.1 补充 GAR-ours vs GAR-D 选择理由\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-W2\"\n  summary: \"Table 1 四舍五入与正文数字精度不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  action_items:\n    - round: 4\n      action: \"Table 1 增加一位小数\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W3\"\n  summary: \"r_min 数值正文未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  action_items:\n    - round: 4\n      action: \"在 §3 或 Appendix A 中报告 r_min 数值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-MR1\"\n  summary: \"缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"合并至 R2-W7-new Discussion 概念对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-W4\"\n  summary: \"Appendix C instruction retention 多重比较未校正\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"18-category McNemar's test 缺 FDR/Bonferroni 校正。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未独立提出，但 per-category 分化进一步削弱未校正结果的可信度。\"\n  action_items:\n    - round: 4\n      action: \"Appendix C per-category 分析补充 Holm-Bonferroni 或 FDR 校正\"\n      assigned_to: paper_agent\n      status: open\n\n# ============================================================\n# Round 5 — status updates through Round 6\n# ============================================================\n\n- id: \"R5-SF1\"\n  summary: \"β-steering 部分循环论证——GAR 恢复 vs 下游效果未解耦\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证首次提出。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"boost attention → attention metric recovers 是同义反复。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-S1 维持循环论证判断。\"\n  action_items:\n    - round: 5\n      action: \"§5.4 拆为两段：GAR 恢复标注 'by construction' + 下游效果单独报告\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Round 6 新增\n# ============================================================\n\n- id: \"R6-SF1\"\n  summary: \"单一数据集（仅 UltraChat）限制 generalizability claim\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 列 Must-Fix，R1 rebut 降为 Should-Fix（诊断性论文单数据集可接受，UltraChat 18 种对话类型提供 domain diversity）。Director 裁定 Should-Fix——机制性发现依赖 training dynamics 而非数据，但 Limitations 需明确讨论。\"\n  action_items:\n    - round: 6\n      action: \"Limitations 明确讨论单数据集对 generalizability 的限制 + future work 承诺跨数据集验证\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R6-SF2\"\n  summary: \"SS Llama 残留 2.9× gap——Abstract 'substantially' 措辞模糊\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"强共识。Qwen 1.3× vs Llama 2.9× 差异显著。Abstract 应报告具体数字。可能暗示 Llama 上有 exposure bias 以外的因素。\"\n  action_items:\n    - round: 6\n      action: \"Abstract 改为具体数字：'compressing the gap from 7.8× to 1.3× on Qwen and from 27× to 2.9× (median) on Llama'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R6-SF3\"\n  summary: \"仅 LoRA fine-tuning，未验证 full fine-tuning\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 交叉同意（严重程度适中）。LoRA capacity 限制可能 confound capacity 排除步骤。\"\n  action_items:\n    - round: 6\n      action: \"Limitations 讨论 LoRA-only 限制，或提供 1 个配置 full FT 对照\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R6-SF4\"\n  summary: \"Dou et al. attention forcing 区分讨论不够深入\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出 3 点缺失讨论（AR 退化、retrospective 解释、方法论互补），R1 交叉同意。\"\n  action_items:\n    - round: 6\n      action: \"Related Work 增加 1-2 句 deeper conceptual connection with Dou et al.\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R6-SF5\"\n  summary: \"Loss formulation 搜索（v1-v9）的过拟合风险\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"R1-S4: 9 次迭代选 loss formulation 可能对 UltraChat 数据集过拟合。\"\n  action_items:\n    - round: 6\n      action: \"Appendix B 或 Limitations 讨论 loss search 可能的 overfitting risk\"\n      assigned_to: paper_agent\n      status: open\n"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-25T21:30:59.755859+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml\", \"bytes\": 24964}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-25T21:33:05.737588+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 6 审稿报告（合并版）\n\n**Target Venue**: EMNLP 2026 (ARR)  \n**Paper**: Turn-Residual Gating  \n**Reviewers**: R1（方法/实验严谨性）、R2（新颖性/完整性）  \n**轮次**: Round 6（fresh re-review，无前轮记忆）  \n**交叉分享**: 完成，R1↔R2 逐条回应  \n\n---\n\n## Summary\n\n论文研究 exposure bias 是否导致 multi-turn transformer 中 auxiliary attention loss（GAR）在 autoregressive generation 下崩塌。通过五路对比设计（Base→LoRA-only→Uniform Gate→ThreadGate→PCGrad）逐步排除替代解释，发现 TF-AR GAR gap 达 8–17×，scheduled sampling 在 Qwen 上压缩至 1.3×、Llama 上压缩至 2.9×。研究问题 genuinely novel，实验设计严谨，附录极为详尽（24 页），但因果归因措辞过强、核心指标（GAR）与下游任务关联薄弱、跨模型验证不完整。\n\n---\n\n## Strengths\n\n1. **研究问题 genuinely novel**：exposure bias 是否影响 auxiliary attention objectives——此前未被系统研究。两位 Reviewer 独立确认 novelty claim 成立。\n2. **五路对比设计有方法论贡献**：逐一隔离变量的排除设计优于简单 baseline 对比，对该领域后续工作有参考价值。\n3. **统计分析规范**（Qwen 主实验）：bootstrap CI、Wilcoxon signed-rank tests、per-category breakdown、N=50 评估。\n4. **附录极为详尽**：24 页涵盖 loss formulation 搜索历史、per-seed 结果、梯度冲突分析、per-turn/per-head 分析。Reproducibility 4/5。\n5. **Scheduled sampling 应用有实用价值**：首次将 SS 应用于 auxiliary attention objectives，Qwen 上效果显著（7.8×→1.3×）。\n6. **写作质量整体良好**：逻辑清晰，claim-evidence 对应关系明确，格式完全合规。\n7. **Negative result 的科学价值**：well-characterized negative result 对该领域有 warning value。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（3 个，影响接收决定）\n\n**MF1** [Critical | R1+R2 强共识] **因果排除链不完整 + \"causal exclusion\" 措辞过强**\n\n两位 Reviewer 从不同角度指向同一根本问题：\n- **R1 角度（方法论）**：PCGrad 仅排除梯度*方向*冲突，未排除梯度*幅值*失衡。Appendix J/L 显示 NTP 梯度幅值压倒 GAR 7.5–14.7×，但论文未测试 λ_GAR rescaling（放大 GAR 权重至与 NTP magnitude parity）。这意味着 exposure bias 归因无法与\"NTP 幅值淹没 GAR 信号\"这一替代假说区分。\n- **R2 角度（术语精确性）**：\"Causal exclusion\" 在 philosophy of mind 中有严格含义（interventionist causal inference），论文实际做的是消融排除法（ablation-based elimination），不是严格因果推断。Limitations 自己承认未排除 KV cache drift。SS 在 Llama 上残留 2.9× gap 进一步说明可能有其他因素。\n- **R1 交叉回应确认**：即便改措辞，实质问题仍在——λ_GAR rescaling 实验缺失。\n\n**要求**：(1) 措辞从 \"causal exclusion chain\" 改为 \"diagnostic exclusion chain\" 或 \"systematic ablation-based exclusion\"（Abstract 第 3 句、§1 Contribution 2、§5.2 标题）；(2) λ_GAR rescaling 实验或在 Discussion 中显式讨论 magnitude imbalance 作为 confound。\n\n**MF2** [Critical | R1+R2 强共识] **GAR 与下游任务性能关联薄弱**\n\n- r=0.200 仅解释 4% 下游方差（r²=0.04），95% CI ≈ [0.05, 0.35] 极宽\n- β-steering instruction retention：McNemar p=0.077 不显著，且高度 category-specific——仅 content constraints 显著改善 (+23.8pp)，format (+6.7pp)、count (0)、position (0) 几乎无变化\n- PPL 在所有配置下几乎相同（2.78）\n- R1 交叉回应：\"强烈同意，应升级严重性\"——GAR collapse 的实际下游危害未得到充分论证\n\n**要求**：(1) 重新定位 GAR 为 attention mechanism collapse 的诊断指标，明确不声称下游因果；(2) 标题从 \"Destroys\" 降调为 \"Collapses\"（描述 attention 行为而非下游灾难）；(3) 正文讨论 GAR 作为 proxy metric 的局限性（per-category 分化 + r²=0.04）。\n\n**MF3** [Critical | R1 主导，R2 认同] **跨模型验证不完整**\n\n- Llama 仅 3/5 条件（缺 PCGrad + Uniform Gate），N=20，单种子\n- Llama 用 median 报告，Qwen 用 mean——统计标准不可比\n- SS Llama 残留 2.9× gap 是 Qwen 1.3× 的 2.2 倍，可能暗示架构差异（GQA/RoPE）带来的其他因素\n- Llama median 报告可能放大 baseline gap（27×），使 compression ratio 视觉效果更大\n\n**要求**：(1) Llama 补全 5/5 条件 + mean/median 双报；(2) Abstract 改为具体数字而非 \"substantially\"；(3) §5.5 标题考虑降级为 \"Cross-Model Replication\"。\n\n### Should-Fix（7 个，影响评分但不一票否决）\n\n**SF1** [Warning | R2 Must-Fix → R1 rebut → Director 裁定 Should-Fix] **单一数据集限制 generalizability**\n- 所有实验仅在 UltraChat 8K 上。R2 认为应 Must-Fix，R1 反驳：诊断性论文的机制发现依赖 training dynamics 而非数据分布，UltraChat 18 种对话类型已提供 domain diversity。Director 裁定：诊断性研究可接受单数据集，但 Limitations 需明确讨论，future work 需承诺跨数据集验证。\n\n**SF2** [Warning | R1+R2 共识] **β-steering 部分循环论证**\n- boost attention → attention metric (GAR) recovers 是 by construction 的同义反复。下游效果（p=0.077）未达显著。§5.4 应拆为两段：GAR 恢复标注 \"by construction\" + 下游效果单独报告。\n\n**SF3** [Warning | R2 提出，R1 交叉同意] **SS Llama 残留 2.9× gap，Abstract \"substantially\" 模糊**\n- Abstract 应报告具体数字：\"compressing the gap from 7.8× to 1.3× on Qwen and from 27× to 2.9× (median) on Llama\"。2.9× 残留需更深入讨论根因（架构差异 vs SS 通用性限制）。\n\n**SF4** [Warning | R2 提出，R1 交叉同意] **仅 LoRA fine-tuning，未验证 full fine-tuning**\n- LoRA 限制模型重组 attention patterns 的 capacity，可能 confound 排除链中的 capacity 排除步骤（Base→LoRA-only 测试的是 \"LoRA 形式的有限参数\" 而非 \"更多参数\"）。Limitations 需讨论。\n\n**SF5** [Warning | R2 提出，R1 交叉同意] **Dou et al. attention forcing 讨论不够深入**\n- 应补充：(1) Dou et al. 是否在 AR 下观察到类似 collapse；(2) 本文发现能否 retrospectively 解释 attention forcing 的效果/局限；(3) 方法论互补性。\n\n**SF6** [Warning | R1 提出] **Loss formulation 搜索（v1-v9）过拟合风险**\n- 9 次迭代在同一数据集（UltraChat）上选择 loss formulation，final choice 可能对该数据集过拟合。\n\n**SF7** [Warning | R1 提出] **SS 替代解释未排除**\n- SS 改变了训练动态（curriculum effect），不仅仅是修复 exposure bias。需讨论 SS 效果的可能替代机制。\n\n### Minor（5 个，不影响接收）\n\n- **m1**: Figure 1 信息密度过高，print size 下文字可能难读（R1+R2 共识）\n- **m2**: §3.4 五路对比可加 flow diagram 提高可读性（R2 提出，R1 同意）\n- **m3**: Appendix C instruction retention 18-category McNemar's test 缺 FDR/Bonferroni 校正（R1+R2 共识）\n- **m4**: 最后一页（p.34）>75% 空白，可压缩（视觉审查）\n- **m5**: 前两页纯文本无 display item，第一个视觉锚点在 p.3（视觉审查）\n\n---\n\n## Questions\n\n1. 如果将 λ_GAR 放大至 NTP/GAR magnitude parity（约 7.5–14.7×），TF-AR gap 是否缩小？这是区分 exposure bias 归因与 magnitude imbalance 假说的关键实验。\n2. SS+LoRA-only（无 ThreadGate）是否达到与 SS+ThreadGate 相似的 GAR recovery？如果是，ThreadGate 的独立贡献为零，论文 story 需要调整。\n3. Llama 上 SS 残留 2.9× gap 的根因是什么？是 GQA/RoPE 架构差异，还是 SS 的 mixing ratio 需要 architecture-specific tuning？\n4. GAR-D（Dongre et al. 原版）在所有条件下接近零，为什么选择 GAR-ours 而非讨论 GAR-D 失败的原因？\n\n---\n\n## Missing References\n\n- **Dou et al. (2024) attention forcing**：论文已引用但讨论不够深入，需补充 AR 退化是否被观察到的讨论（R1+R2 共识）\n- **Zhang et al. 2024 \"Tell Your Model Where to Attend\"**：缺失，应在 Discussion 概念对比中覆盖\n- 其他引用：R2 novelty 验证确认无严重遗漏。Dongre et al. (2026)、Qiu et al. (2025)、Li et al. (2024) 均正确引用。\n\n---\n\n## External Review\n\n**状态**：pending（已发送请求，尚未返回）。Stanford Agentic Reviewer 审稿结果未在本轮报告截止前到达。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (0 critical, 2 warning, 19 info)\n\n**Warnings**:\n1. 前两页纯文本（Abstract + Introduction + Related Work），无 display item，第一个视觉锚点（Figure 1）在 p.3。审稿人翻过两整页纯文字才看到第一张图，第一印象略弱。\n2. 最后一页（p.34）仅顶部 ~20% 有内容，>75% 空白。\n\n**Positive findings**:\n- 主文本 8 页含 6 Figure + 1 Table = 7 个 display items，密度 0.88/页，合理\n- 配色柔和（蓝/橙/绿/灰），饱和度适中，不同 figure 语义连贯\n- Figure/Table 均出现在首次引用附近，无 float 推后\n- Caption 自包含，公式渲染正确，无 margin overflow\n- 格式完全合规：8 页正文、~191 词 Abstract、Limitations 在正文内、匿名化正确\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5（Borderline Conference）**\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 3.5 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**评分理由**：\n\n论文提出了一个 genuinely novel 的研究问题（exposure bias 对 auxiliary attention objectives 的影响），且实验设计（五路排除）在方法论上有贡献。附录 24 页展现了扎实的实验工作量，统计分析（Qwen 主实验）规范。\n\n但三个 Must-Fix 问题阻止了更高评分：\n1. **因果归因不完备**（复发 6 轮）——\"causal exclusion\" 措辞过强，λ_GAR rescaling 实验缺失使归因链有实质缺口\n2. **核心指标与下游脱节**（复发 6 轮）——r²=0.04 + p=0.077 + per-category 高度分化，GAR collapse 的实际危害未论证\n3. **跨模型验证断裂**——Llama 仅 3/5 条件、median/mean 不可比、SS 残留 2.9× gap\n\n**Rebuttal 期望**：如果作者能 (1) 提供 λ_GAR rescaling 实验结果或等效的 magnitude control；(2) 将 GAR 重新定位为诊断指标并降调下游因果声称；(3) 补全 Llama 5/5 条件 + mean/median 双报，评分可考虑提升至 4.0（Conference）。\n\n---\n\n## Detailed Comments\n\n### 交叉分享共识点\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| \"Causal exclusion\" 措辞 | Must-Fix (方法论) | Must-Fix (术语) | **强共识 Must-Fix** |\n| GAR 下游有效性 | Must-Fix (r=0.200) | Should-Fix→升级 | **强共识 Must-Fix** |\n| 跨模型验证 | Must-Fix (3/5条件) | Should-Fix (SS gap) | **合并 Must-Fix** |\n| SS Llama 2.9× gap | Should-Fix | Should-Fix | **共识 Should-Fix** |\n| β-steering 循环论证 | Should-Fix | 未独立提出 | Should-Fix |\n| LoRA-only 限制 | 交叉同意 | Should-Fix | Should-Fix |\n\n### 交叉分享分歧点\n\n| 问题 | R1 | R2 | Director 裁定 |\n|------|----|----|---------------|\n| 单数据集 | Should-Fix（诊断性论文可接受） | Must-Fix（限制 generalizability） | **Should-Fix**——机制性发现依赖 training dynamics 而非数据，但需在 Limitations 明确讨论 |\n| 附录篇幅 | 优势（严谨性体现） | Minor（偏大） | **优势**——EMNLP 无附录页数限制 |\n| Abstract footnote | 合规（ACL 模板允许） | Minor（不常见） | **无需修改**——合规且有先例 |\n| 数字重复 \"8-17×\" | 正常科学写作 | Minor（重复感） | **无需修改**——关键 effect size 重复符合惯例 |\n\n### Novelty 验证\n\nR2 独立确认以下 novelty claims 成立：\n1. \"首次实证 exposure bias 崩塌 auxiliary attention objectives\"——文献搜索未发现先前工作\n2. \"Scheduled sampling 首次应用于 auxiliary attention objectives in multi-turn\"——Mihaylova & Martins (2019) 仅用于 single-turn NMT primary loss\n3. 未发现严重的 related work 遗漏\n\n### Issue Tracker 统计（Round 6）\n\n| 状态 | 数量 |\n|------|------|\n| open | 12 |\n| in_progress | 22 |\n| resolved | 9 |\n| **total** | **43** |\n\n其中 critical severity in_progress/open: 5 个（R2-N1, R2-N3, R2-C3, R2-W3/R4-N1, R1-W5）",
  "project": "turn_residual_gating",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 6 审稿报告（合并版）\n\n**Target Venue**: EMNLP 2026 (ARR)  \n**Paper**: Turn-Residual Gating  \n**Reviewers**: R1（方法/实验严谨性）、R2（新颖性/完整性）  \n**轮次**: Round 6（fresh re-review，无前轮记忆）  \n**交叉分享**: 完成，R1↔R2 逐条回应  \n\n---\n\n## Summary\n\n论文研究 exposure bias 是否导致 multi-turn transformer 中 auxiliary attention loss（GAR）在 autoregressive generation 下崩塌。通过五路对比设计（Base→LoRA-only→Uniform Gate→ThreadGate→PCGrad）逐步排除替代解释，发现 TF-AR GAR gap 达 8–17×，scheduled sampling 在 Qwen 上压缩至 1.3×、Llama 上压缩至 2.9×。研究问题 genuinely novel，实验设计严谨，附录极为详尽（24 页），但因果归因措辞过强、核心指标（GAR）与下游任务关联薄弱、跨模型验证不完整。\n\n---\n\n## Strengths\n\n1. **研究问题 genuinely novel**：exposure bias 是否影响 auxiliary attention objectives——此前未被系统研究。两位 Reviewer 独立确认 novelty claim 成立。\n2. **五路对比设计有方法论贡献**：逐一隔离变量的排除设计优于简单 baseline 对比，对该领域后续工作有参考价值。\n3. **统计分析规范**（Qwen 主实验）：bootstrap CI、Wilcoxon signed-rank tests、per-category breakdown、N=50 评估。\n4. **附录极为详尽**：24 页涵盖 loss formulation 搜索历史、per-seed 结果、梯度冲突分析、per-turn/per-head 分析。Reproducibility 4/5。\n5. **Scheduled sampling 应用有实用价值**：首次将 SS 应用于 auxiliary attention objectives，Qwen 上效果显著（7.8×→1.3×）。\n6. **写作质量整体良好**：逻辑清晰，claim-evidence 对应关系明确，格式完全合规。\n7. **Negative result 的科学价值**：well-characterized negative result 对该领域有 warning value。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（3 个，影响接收决定）\n\n**MF1** [Critical | R1+R2 强共识] **因果排除链不完整 + \"causal exclusion\" 措辞过强**\n\n两位 Reviewer 从不同角度指向同一根本问题：\n- **R1 角度（方法论）**：PCGrad 仅排除梯度*方向*冲突，未排除梯度*幅值*失衡。Appendix J/L 显示 NTP 梯度幅值压倒 GAR 7.5–14.7×，但论文未测试 λ_GAR rescaling（放大 GAR 权重至与 NTP magnitude parity）。这意味着 exposure bias 归因无法与\"NTP 幅值淹没 GAR 信号\"这一替代假说区分。\n- **R2 角度（术语精确性）**：\"Causal exclusion\" 在 philosophy of mind 中有严格含义（interventionist causal inference），论文实际做的是消融排除法（ablation-based elimination），不是严格因果推断。Limitations 自己承认未排除 KV cache drift。SS 在 Llama 上残留 2.9× gap 进一步说明可能有其他因素。\n- **R1 交叉回应确认**：即便改措辞，实质问题仍在——λ_GAR rescaling 实验缺失。\n\n**要求**：(1) 措辞从 \"causal exclusion chain\" 改为 \"diagnostic exclusion chain\" 或 \"systematic ablation-based exclusion\"（Abstract 第 3 句、§1 Contribution 2、§5.2 标题）；(2) λ_GAR rescaling 实验或在 Discussion 中显式讨论 magnitude imbalance 作为 confound。\n\n**MF2** [Critical | R1+R2 强共识] **GAR 与下游任务性能关联薄弱**\n\n- r=0.200 仅解释 4% 下游方差（r²=0.04），95% CI ≈ [0.05, 0.35] 极宽\n- β-steering instruction retention：McNemar p=0.077 不显著，且高度 category-specific——仅 content constraints 显著改善 (+23.8pp)，format (+6.7pp)、count (0)、position (0) 几乎无变化\n- PPL 在所有配置下几乎相同（2.78）\n- R1 交叉回应：\"强烈同意，应升级严重性\"——GAR collapse 的实际下游危害未得到充分论证\n\n**要求**：(1) 重新定位 GAR 为 attention mechanism collapse 的诊断指标，明确不声称下游因果；(2) 标题从 \"Destroys\" 降调为 \"Collapses\"（描述 attention 行为而非下游灾难）；(3) 正文讨论 GAR 作为 proxy metric 的局限性（per-category 分化 + r²=0.04）。\n\n**MF3** [Critical | R1 主导，R2 认同] **跨模型验证不完整**\n\n- Llama 仅 3/5 条件（缺 PCGrad + Uniform Gate），N=20，单种子\n- Llama 用 median 报告，Qwen 用 mean——统计标准不可比\n- SS Llama 残留 2.9× gap 是 Qwen 1.3× 的 2.2 倍，可能暗示架构差异（GQA/RoPE）带来的其他因素\n- Llama median 报告可能放大 baseline gap（27×），使 compression ratio 视觉效果更大\n\n**要求**：(1) Llama 补全 5/5 条件 + mean/median 双报；(2) Abstract 改为具体数字而非 \"substantially\"；(3) §5.5 标题考虑降级为 \"Cross-Model Replication\"。\n\n### Should-Fix（7 个，影响评分但不一票否决）\n\n**SF1** [Warning | R2 Must-Fix → R1 rebut → Director 裁定 Should-Fix] **单一数据集限制 generalizability**\n- 所有实验仅在 UltraChat 8K 上。R2 认为应 Must-Fix，R1 反驳：诊断性论文的机制发现依赖 training dynamics 而非数据分布，UltraChat 18 种对话类型已提供 domain diversity。Director 裁定：诊断性研究可接受单数据集，但 Limitations 需明确讨论，future work 需承诺跨数据集验证。\n\n**SF2** [Warning | R1+R2 共识] **β-steering 部分循环论证**\n- boost attention → attention metric (GAR) recovers 是 by construction 的同义反复。下游效果（p=0.077）未达显著。§5.4 应拆为两段：GAR 恢复标注 \"by construction\" + 下游效果单独报告。\n\n**SF3** [Warning | R2 提出，R1 交叉同意] **SS Llama 残留 2.9× gap，Abstract \"substantially\" 模糊**\n- Abstract 应报告具体数字：\"compressing the gap from 7.8× to 1.3× on Qwen and from 27× to 2.9× (median) on Llama\"。2.9× 残留需更深入讨论根因（架构差异 vs SS 通用性限制）。\n\n**SF4** [Warning | R2 提出，R1 交叉同意] **仅 LoRA fine-tuning，未验证 full fine-tuning**\n- LoRA 限制模型重组 attention patterns 的 capacity，可能 confound 排除链中的 capacity 排除步骤（Base→LoRA-only 测试的是 \"LoRA 形式的有限参数\" 而非 \"更多参数\"）。Limitations 需讨论。\n\n**SF5** [Warning | R2 提出，R1 交叉同意] **Dou et al. attention forcing 讨论不够深入**\n- 应补充：(1) Dou et al. 是否在 AR 下观察到类似 collapse；(2) 本文发现能否 retrospectively 解释 attention forcing 的效果/局限；(3) 方法论互补性。\n\n**SF6** [Warning | R1 提出] **Loss formulation 搜索（v1-v9）过拟合风险**\n- 9 次迭代在同一数据集（UltraChat）上选择 loss formulation，final choice 可能对该数据集过拟合。\n\n**SF7** [Warning | R1 提出] **SS 替代解释未排除**\n- SS 改变了训练动态（curriculum effect），不仅仅是修复 exposure bias。需讨论 SS 效果的可能替代机制。\n\n### Minor（5 个，不影响接收）\n\n- **m1**: Figure 1 信息密度过高，print size 下文字可能难读（R1+R2 共识）\n- **m2**: §3.4 五路对比可加 flow diagram 提高可读性（R2 提出，R1 同意）\n- **m3**: Appendix C instruction retention 18-category McNemar's test 缺 FDR/Bonferroni 校正（R1+R2 共识）\n- **m4**: 最后一页（p.34）>75% 空白，可压缩（视觉审查）\n- **m5**: 前两页纯文本无 display item，第一个视觉锚点在 p.3（视觉审查）\n\n---\n\n## Questions\n\n1. 如果将 λ_GAR 放大至 NTP/GAR magnitude parity（约 7.5–14.7×），TF-AR gap 是否缩小？这是区分 exposure bias 归因与 magnitude imbalance 假说的关键实验。\n2. SS+LoRA-only（无 ThreadGate）是否达到与 SS+ThreadGate 相似的 GAR recovery？如果是，ThreadGate 的独立贡献为零，论文 story 需要调整。\n3. Llama 上 SS 残留 2.9× gap 的根因是什么？是 GQA/RoPE 架构差异，还是 SS 的 mixing ratio 需要 architecture-specific tuning？\n4. GAR-D（Dongre et al. 原版）在所有条件下接近零，为什么选择 GAR-ours 而非讨论 GAR-D 失败的原因？\n\n---\n\n## Missing References\n\n- **Dou et al. (2024) attention forcing**：论文已引用但讨论不够深入，需补充 AR 退化是否被观察到的讨论（R1+R2 共识）\n- **Zhang et al. 2024 \"Tell Your Model Where to Attend\"**：缺失，应在 Discussion 概念对比中覆盖\n- 其他引用：R2 novelty 验证确认无严重遗漏。Dongre et al. (2026)、Qiu et al. (2025)、Li et al. (2024) 均正确引用。\n\n---\n\n## External Review\n\n**状态**：pending（已发送请求，尚未返回）。Stanford Agentic Reviewer 审稿结果未在本轮报告截止前到达。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (0 critical, 2 warning, 19 info)\n\n**Warnings**:\n1. 前两页纯文本（Abstract + Introduction + Related Work），无 display item，第一个视觉锚点（Figure 1）在 p.3。审稿人翻过两整页纯文字才看到第一张图，第一印象略弱。\n2. 最后一页（p.34）仅顶部 ~20% 有内容，>75% 空白。\n\n**Positive findings**:\n- 主文本 8 页含 6 Figure + 1 Table = 7 个 display items，密度 0.88/页，合理\n- 配色柔和（蓝/橙/绿/灰），饱和度适中，不同 figure 语义连贯\n- Figure/Table 均出现在首次引用附近，无 float 推后\n- Caption 自包含，公式渲染正确，无 margin overflow\n- 格式完全合规：8 页正文、~191 词 Abstract、Limitations 在正文内、匿名化正确\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5（Borderline Conference）**\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.0 |\n| Excitement | 3.5 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**评分理由**：\n\n论文提出了一个 genuinely novel 的研究问题（exposure bias 对 auxiliary attention objectives 的影响），且实验设计（五路排除）在方法论上有贡献。附录 24 页展现了扎实的实验工作量，统计分析（Qwen 主实验）规范。\n\n但三个 Must-Fix 问题阻止了更高评分：\n1. **因果归因不完备**（复发 6 轮）——\"causal exclusion\" 措辞过强，λ_GAR rescaling 实验缺失使归因链有实质缺口\n2. **核心指标与下游脱节**（复发 6 轮）——r²=0.04 + p=0.077 + per-category 高度分化，GAR collapse 的实际危害未论证\n3. **跨模型验证断裂**——Llama 仅 3/5 条件、median/mean 不可比、SS 残留 2.9× gap\n\n**Rebuttal 期望**：如果作者能 (1) 提供 λ_GAR rescaling 实验结果或等效的 magnitude control；(2) 将 GAR 重新定位为诊断指标并降调下游因果声称；(3) 补全 Llama 5/5 条件 + mean/median 双报，评分可考虑提升至 4.0（Conference）。\n\n---\n\n## Detailed Comments\n\n### 交叉分享共识点\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| \"Causal exclusion\" 措辞 | Must-Fix (方法论) | Must-Fix (术语) | **强共识 Must-Fix** |\n| GAR 下游有效性 | Must-Fix (r=0.200) | Should-Fix→升级 | **强共识 Must-Fix** |\n| 跨模型验证 | Must-Fix (3/5条件) | Should-Fix (SS gap) | **合并 Must-Fix** |\n| SS Llama 2.9× gap | Should-Fix | Should-Fix | **共识 Should-Fix** |\n| β-steering 循环论证 | Should-Fix | 未独立提出 | Should-Fix |\n| LoRA-only 限制 | 交叉同意 | Should-Fix | Should-Fix |\n\n### 交叉分享分歧点\n\n| 问题 | R1 | R2 | Director 裁定 |\n|------|----|----|---------------|\n| 单数据集 | Should-Fix（诊断性论文可接受） | Must-Fix（限制 generalizability） | **Should-Fix**——机制性发现依赖 training dynamics 而非数据，但需在 Limitations 明确讨论 |\n| 附录篇幅 | 优势（严谨性体现） | Minor（偏大） | **优势**——EMNLP 无附录页数限制 |\n| Abstract footnote | 合规（ACL 模板允许） | Minor（不常见） | **无需修改**——合规且有先例 |\n| 数字重复 \"8-17×\" | 正常科学写作 | Minor（重复感） | **无需修改**——关键 effect size 重复符合惯例 |\n\n### Novelty 验证\n\nR2 独立确认以下 novelty claims 成立：\n1. \"首次实证 exposure bias 崩塌 auxiliary attention objectives\"——文献搜索未发现先前工作\n2. \"Scheduled sampling 首次应用于 auxiliary attention objectives in multi-turn\"——Mihaylova & Martins (2019) 仅用于 single-turn NMT primary loss\n3. 未发现严重的 related work 遗漏\n\n### Issue Tracker 统计（Round 6）\n\n| 状态 | 数量 |\n|------|------|\n| open | 12 |\n| in_progress | 22 |\n| resolved | 9 |\n| **total** | **43** |\n\n其中 critical severity in_progress/open: 5 个（R2-N1, R2-N3, R2-C3, R2-W3/R4-N1, R1-W5）",
    "project": "turn_residual_gating",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-25T21:33:09.816567+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4078
}
```

</details>

---


### Assistant

_source line 550 · 2026-05-25T21:33:22.492170+00:00_

Round 6 审稿完成。

**合并评分：3.5 / 5（Borderline Conference）**

**3 个 Must-Fix**：
1. **因果排除链不完整 + "causal exclusion" 措辞过强**——PCGrad 未排除梯度幅值失衡（NTP 压倒 GAR 7.5–14.7×），λ_GAR rescaling 实验缺失。措辞需改为 "diagnostic exclusion chain"。（复发 6 轮）
2. **GAR 与下游任务关联薄弱**——r²=0.04，p=0.077 不显著，per-category 仅 content constraints 有效。需重新定位为诊断指标，标题 "Destroys"→"Collapses"。（复发 6 轮）
3. **跨模型验证不完整**——Llama 仅 3/5 条件、median/mean 不可比、SS 残留 2.9× gap。

**7 个 Should-Fix** 包括：单数据集（Director 裁定降级）、β-steering 循环论证、SS Llama 措辞模糊、LoRA-only 限制、Dou et al. 讨论不足、loss search 过拟合风险、SS 替代解释。

Issues tracker 已同步更新（43 条，5 个 critical in_progress/open）。审稿报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 551 · 2026-05-25T21:33:23.585302+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：R1 和 R2 在三个关键问题上形成共识——因果排除链不完备（梯度幅值未排除）、GAR 下游有效性弱（r=0.200, per-category 分化）、跨模型验证不足。分歧主要在严重级别判定上（单数据集是 Must-Fix 还是 Should-Fix、附录篇幅是优势还是问题）。两人 Overall 均为 3.5，rebuttal 期望一致：λ_GAR rescaling 实验 + Llama PCGrad 补全 + 措辞审慎化。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 回应

**[AGREE] R1-C1: 因果排除链未封闭——gradient magnitude imbalance未排除**

同意这是一个实质性的gap。论文报告NTP magnitude压倒GAR 7.5–14.7×（Appendix L, Section 5.2），PCGrad仅处理方向冲突而非幅值失衡。缺失λ_GAR rescaling实验意味着无法排除以下假说：**当前magnitude imbalance下，模型只学到了TF下最小满足GAR的脆弱attention patterns，而更高λ_GAR可能产生对distribution shift更鲁棒的patterns**。

不过我要补充一个nuance：论文所有5个配置在TF下均达到GAR≈0.50（Table 1），说明当前λ_GAR在TF学习上已经饱和。问题不在于"没学到"而在于"学到的不迁移"。Magnitude imbalance是一个训练效率问题，而非直接的TF-AR transfer问题。但R1说得对——这仍是exclusion chain的一个未封闭环节。

**与我的N1的关系**：R1-C1和我的N1指向同一根本问题的不同层面。我的N1是terminology层面（"causal exclusion"措辞过强），R1-C1提供了具体的方法论证据（magnitude未排除）来支撑这一判断。两者互补，共同构成对论文核心claim的最重要质疑。建议合并为rebuttal的首要问题。

---

**[AGREE] R1-C2: GAR下游有效性弱（r=0.200, p=0.077）**

同意R1对统计数据的解读。r=0.200仅解释4%下游方差，β-steering的instruction retention改善p=0.077在α=0.05下不显著——这些具体数字比我在W1中的定性描述更有说服力。

我在初审中将此列为Should-Fix（W1），R1列为Must-Fix。反思后，我认为R1的severity判断可能更准确，理由如下：
- 如果GAR collapse对downstream performance的影响negligible，那么论文的核心发现（exposure bias collapses GAR）的practical significance就大打折扣
- 论文的narrative建立在"GAR collapse是一个需要解决的问题"之上，但如果GAR只捕获4%的下游方差，这个前提就不牢固
- Appendix C的instruction retention评估显示只有content constraints受益（+23.8pp），format/count/position几乎无变化

**但我要提供一个partial defense**：论文将GAR定位为"diagnostic probe"而非performance predictor。GAR的价值在于揭示exposure bias对attention routing的影响，而非直接预测任务性能。作为诊断工具，low downstream correlation不等于GAR本身无效——只是说明attention routing只是影响downstream performance的多个因素之一。如果作者能在rebuttal中更清晰地框定GAR的diagnostic（而非predictive）角色，这个问题可以缓解。

**严重性调整**：将我的W1上调至borderline Must-Fix，与R1-C2基本一致。

---

**[AGREE] R1-C3: 跨模型验证不足——Llama实验underpowered**

同意Llama实验在以下方面显著弱于Qwen：
- 仅3/5条件（缺PCGrad和Uniform Gate）
- N=20 vs Qwen的N=50
- 单种子
- Median vs mean报告

这使得cross-model comparison缺乏rigorous对等性。R1正确指出median与mean在heavy-tailed分布下差异显著，而Table 7使用median（"median is more representative due to heavy-tailed AR distributions"）与Table 1使用mean不可直接比较。

**与我的N2的关系**：R1-C3和我的N2指向scope limitation的不同维度：
- R1-C3：同一数据集上的cross-**model**验证质量不足
- 我的N2：cross-**dataset**验证完全缺失

两者各自独立且互不替代。我认为cross-dataset（N2）对generalizability的威胁更大，因为即使Llama实验完全对等，如果finding仅在UltraChat上成立，科学价值仍然有限。但R1-C3对于论文当前的cross-model claim具有直接的undermining效果——论文不能同时声称"spanning two architectures"却在一个架构上提供underpowered evidence。

**相对重要性**：N2（cross-dataset）> C3（cross-model rigor），但两者都应在rebuttal中addressed。

---

### Should-Fix 回应

**[AGREE] R1-S1: β-steering部分循环论证**

部分同意。β-steering增加goal token attention → GAR上升——这本身确实是definitionally true，存在partial circularity。但我要指出论文的argument不完全循环：β-steering在GAR恢复的同时PPL仅modest增长（Table 18: β=3时PPL从~2.78升到~2.80），这证明representations是完整的（如果representation已degraded，β-steering会导致catastrophic PPL）。这一推理链是valid的。

真正的circularity在于instruction retention claim：β-steering → GAR↑ → instruction retention↑ 的链条中，如果GAR-downstream correlation本身就弱（R1-C2, r=0.200），那么β-steering的downstream improvement claim就是建立在weak foundation上的。

---

**[AGREE] R1-S2: SS替代解释未排除**

同意。Scheduled sampling同时改变了：(1) 训练时的input distribution（target exposure bias）；(2) effective training data diversity；(3) optimization landscape。论文将SS的改善归因于(1)，但没有control experiment排除(2)和(3)。例如，一个简单的对照：对input添加random noise（改变distribution但不specifically target TF-AR mismatch）能否也减少gap？如果能，SS的改善就不能uniquely归因于exposure bias mitigation。

不过，SS specifically targets the TF-AR gap by construction（模型在训练时看到自己生成的tokens），所以归因于exposure bias mitigation是reasonable的prior。只是不够definitive。

---

**[AGREE] R1-S3: Qwen/Llama报告标准不一致**

与C3有重叠。这是一个reporting rigor问题——同一论文中对两个架构应使用一致的统计报告标准。即使Llama分布heavy-tailed需要median，也应同时报告mean以便直接比较。

---

**[AGREE] R1-S4: loss formulation搜索的过拟合风险**

同意。Appendix B记录了7次迭代的loss formulation search。虽然这种engineering transparency值得肯定，但7次迭代均在同一UltraChat数据上进行，存在implicit dataset-specific tuning的风险。这与我的N2（单一数据集）互相加强：如果loss design是针对UltraChat特性tune出来的，在其他数据集上可能不work。

---

### 总结：两位Reviewer的共识与分歧

**强共识区域**（两位Reviewer均认为是问题）：
1. ⭐ "Causal exclusion"声称过强（R1-C1 + R2-N1）——最关键的共识
2. ⭐ GAR-downstream link薄弱（R1-C2 + R2-W1→调整至borderline Must-Fix）
3. Cross-model/cross-dataset scope不足（R1-C3 + R2-N2）
4. β-steering有partial circularity（R1-S1，R2未独立提出但同意）
5. SS的归因不够definitive（R1-S2，R2未独立提出但同意）

**独特贡献**：
- R1独有：gradient magnitude imbalance的具体gap（C1中的λ_GAR rescaling缺失）、SS替代解释（S2）、loss search过拟合风险（S4）
- R2独有：cross-dataset validation缺失（N2）、Dou et al. attention forcing的deeper engagement需求（W4）、Llama上SS效果的Abstract措辞模糊（W2）

**severity分歧**：
- GAR下游有效性：R1列Must-Fix，R2初评Should-Fix → 交叉后调整至borderline Must-Fix
- 整体评分一致：均为3.5（Borderline Conference）

**对rebuttal的建议优先级**：
1. 回应causal exclusion overclaim + 提供λ_GAR rescaling实验或理论分析
2. 强化GAR-downstream evidence（额外的downstream evaluation或更大sample size的correlation study）
3. 至少一个额外数据集的pilot验证
4. 统一Llama/Qwen的报告标准（补充Llama的mean + 更多配置）

---

[Reviewer 2 审稿结果]:
交叉回应已提交。

**核心结论**：对 R1 的 7 条意见**全部 [AGREE]**，无 rebut。两位 reviewer 在三个关键问题上形成强共识：

1. **"Causal exclusion" overclaim**（R1-C1 + R2-N1）：最重要的共识，R1 提供了具体的 gap（gradient magnitude），我提供了 terminology 层面的批评
2. **GAR-downstream link 薄弱**（R1-C2 + R2-W1）：R1 的具体数字（r=0.200, p=0.077）说服我将 severity 从 Should-Fix 上调至 borderline Must-Fix
3. **Scope 不足**：R1 聚焦 cross-model rigor（C3），我聚焦 cross-dataset 缺失（N2），两者互补

整体评分两人一致：3.5（Borderline Conference）。Rebuttal 最高优先级应是回应 causal exclusion overclaim 并提供额外数据集验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 552 · 2026-05-25T21:33:40.176679+00:00_

Round 6 审稿圆桌已完成。

R2 详细交叉回应对 R1 全部 7 条意见 **[AGREE]**，无任何 rebut。这与已提交的合并报告结论完全一致——两位 Reviewer 在三个 Must-Fix 上形成强共识，Overall 均为 3.5（Borderline Conference）。报告无需修订。

审稿报告已投递给 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---
