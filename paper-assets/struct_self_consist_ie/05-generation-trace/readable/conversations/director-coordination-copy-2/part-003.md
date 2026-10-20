# Director coordination — Part 3 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 55

### Tool call

_source line 657 · 2026-05-15T09:03:11.851390+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues (all resolved)\n  # ============================================================\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B）\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"model-agnostic 与 Limitations 矛盾\"\n    action_items:\n      - round: 1\n        action: \"全文替换 model-agnostic → consistent across tested model families\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 确认措辞修正到位，无再提\"\n    resolution_round: 2\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"新遗漏：Optimal SC, Difficulty-Adaptive SC\"\n    action_items:\n      - round: 1\n        action: \"补充 6 篇引用到 Related Work\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏\"\n    resolution_round: 2\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 4\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"需跨数据集验证或降级措辞\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Abstract RE 措辞需修正\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\"\n    action_items:\n      - round: 1\n        action: \"降级措辞 universal → observed in SciERC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"Abstract 改为 NER (three datasets) and RE (SciERC)\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议\"\n    resolution_round: 4\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Nedellec 增量贡献论证不足 + 引用错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强增量贡献论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认三点差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams\"\n    action_items: []\n    resolution: \"论文已包含 6 个 figures\"\n    resolution_round: 1\n\n  - id: \"R0-C6\"\n    summary: \"成本分析 negligible 误导\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8-16× 推理开销不应描述为 negligible\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"互补性已证明但未尝试组合\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Bootstrap 细节不足\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n    resolution_round: 2\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling +0.018 与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"+0.018 实际为 -0.080\"\n    action_items:\n      - round: 0\n        action: \"修正声明\"\n        assigned_to: \"Main Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 1 issues (all resolved)\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"p=0.39 支撑核心结论但细节缺失\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价统计规范达到高标准\"\n    resolution_round: 2\n\n  - id: \"R1-N2\"\n    summary: \"Gap 解释力不足 + logprob 失败未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"4/5 定义性 + logprob 机制缺失\"\n    action_items:\n      - round: 1\n        action: \"区分 by-design vs empirical + logprob failure 分析段\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 logprob failure analysis 充分\"\n    resolution_round: 2\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 单薄\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"consensus-proximity = LOO-SJ 是表述问题\"\n    action_items:\n      - round: 1\n        action: \"显式说明等价关系\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 consensus-proximity = LOO-SJ 已明确\"\n    resolution_round: 2\n\n  - id: \"R1-N4\"\n    summary: \"Nedellec 引用错误 + 增量贡献弱\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Yao vs Nédellec 事实错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"SJ 形式化有歧义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Hungarian threshold + max denominator 需补充\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R3-R1 再次指出 Hungarian cost function 未明确 maximize/minimize 方向, zero-IoU pairs 处理方式缺失\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 Round 4 确认 SJ 形式化已完善 [RESOLVED]\"\n    action_items:\n      - round: 1\n        action: \"补全 Eq(4) 定义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"补 threshold 说明 + max vs union 设计理由\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"补 Hungarian optimization objective (max-weight matching on IoU) + zero-IoU pairs handling\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: R2 确认 SJ 形式化已完善，Hungarian matching 描述清晰\"\n    resolution_round: 4\n\n  - id: \"R1-W2\"\n    summary: \"Voting-SJ 冗余度未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"instance-level correlation 未报告\"\n    action_items:\n      - round: 1\n        action: \"报告 Voting-SJ ρ=0.659/0.605\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"中等相关数据已报告\"\n    resolution_round: 2\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 缺 contextualization\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 cross-method footnote\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote: semantic entropy AUROC comparison + cross-task caveat\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度数据缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"robustness 结论需限定\"\n    action_items:\n      - round: 1\n        action: \"限定为 consistency-based signals robust; logprob uncharacterized\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞限定到位\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 establishing 措辞过度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"fail to reject ≠ accept\"\n    action_items:\n      - round: 1\n        action: \"establishing → consistent with/suggests\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R1-W6\"\n    summary: \"LLaMA 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"LLaMA fine-tuning 状态未说明\"\n    action_items:\n      - round: 1\n        action: \"明确两模型 identical LoRA 配置\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 未再提及\"\n    resolution_round: 2\n\n  - id: \"R1-W7\"\n    summary: \"约束解码 diversity 影响\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展为全局 confound + Limitations 条目\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 新增条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已扩展为全局 confound 讨论\"\n    resolution_round: 2\n\n  - id: \"R1-W8\"\n    summary: \"first systematic 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"需收窄 scope\"\n    action_items:\n      - round: 1\n        action: \"first multi-family\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 无再提\"\n    resolution_round: 2\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Optimal SC, Difficulty-Adaptive SC 等\"\n    action_items:\n      - round: 1\n        action: \"补充引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认无遗漏\"\n    resolution_round: 2\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 分析浅\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"EM=1 压缩效应需主文提及\"\n    action_items:\n      - round: 1\n        action: \"Section 5 简述 + 引导 Appendix\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 dissociation 分析为 actionable finding\"\n    resolution_round: 2\n\n  - id: \"R1-M1\"\n    summary: \"Logistic regression proxy 无结果\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"展示结果或删除\"\n    action_items:\n      - round: 1\n        action: \"删除提及\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已删除\"\n    resolution_round: 2\n\n  - id: \"R1-M2\"\n    summary: \"GSM8K +18pp 未注明模型\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"补注 PaLM-540B\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告 CI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"within 3-seed σ≈0.007\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 2 issues (all resolved)\n  # ============================================================\n  - id: \"R2-C1\"\n    summary: \"Selection 证据面过窄——仅 1 dataset × 1 model\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需补 LLaMA SciERC + CoNLL selection\"\n    action_items:\n      - round: 2\n        action: \"补 4 配置 selection 分析 + Appendix Table 6\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"6 configurations 全部补齐，无 signal 显著超越 greedy\"\n    resolution_round: 2\n\n  - id: \"R2-C2\"\n    summary: \"WNUT-17 仅报告 1 个信号\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"5 signals 中仅 SJ 一个数据点\"\n    action_items:\n      - round: 2\n        action: \"补全 5 信号 full/conditional ρ + AUROC + Appendix Table 5\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"WNUT-17 全信号表完整，叙事修正为区分 full-set vs conditional\"\n    resolution_round: 2\n\n  - id: \"R2-W1\"\n    summary: \"ρ=0.38 缺 cross-method 对比\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 footnote 引用 semantic entropy AUROC\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R2-W2\"\n    summary: \"N=8 QE ρ 无 uncertainty\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap CIs\"\n    action_items:\n      - round: 2\n        action: \"计算 B=10,000 bootstrap CI + Appendix 表\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Bootstrap CI 表已加入 Appendix，SJ-logprob 显著\"\n    resolution_round: 2\n\n  - id: \"R2-W3\"\n    summary: \"SJ Hungarian threshold + max denominator\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"无 threshold 声明需验证\"\n    action_items:\n      - round: 2\n        action: \"代码验证 + method.tex 补充\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"无 threshold, 96.6% pairs sim≥0.5, max denominator 已解释\"\n    resolution_round: 2\n\n  - id: \"R2-W4\"\n    summary: \"RE selection 无统计检验\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap p-value\"\n    action_items:\n      - round: 2\n        action: \"RE bootstrap + 补 p=0.80 到论文\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"RE logprob p=0.80, all signals below greedy\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Constrained decoding 全局 confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展到全局 + Limitations\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已处理\"\n    resolution_round: 2\n\n  - id: \"R2-W6\"\n    summary: \"Abstract RE 措辞误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"NER (three datasets) and RE (SciERC)\"\n    action_items:\n      - round: 2\n        action: \"修正 Abstract\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R2-W7\"\n    summary: \"n=529 vs 551 未解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"22 instances filtering criteria\"\n    action_items:\n      - round: 2\n        action: \"补一句说明\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已说明 gold-empty filtering\"\n    resolution_round: 2\n\n  - id: \"R2-DATA\"\n    summary: \"RE selection 数据矛盾 (Table 2 vs L129)\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"Table 2 logprob=0.395 (-0.9pp) vs L129 logprob=0.410 (+0.6pp)\"\n    action_items:\n      - round: 2\n        action: \"Agent 确认 Table 2 正确 → Paper Agent 修正 L129\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"L129 统一为 logprob=0.395, -0.9pp, p=0.80\"\n    resolution_round: 2\n\n  - id: \"R2-AUROC\"\n    summary: \"L64 AUROC 归属错误 (Voting ρ 配 EM AUROC)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"corresponding 暗示同一信号\"\n    action_items:\n      - round: 2\n        action: \"分别标注 Voting ρ 和 EM AUROC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已拆分归属\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3+ issues (updated with Round 6 status)\n  # ============================================================\n  - id: \"R3-C1\"\n    summary: \"Constrained decoding 是 correlation-selection gap 的未控制混淆变量\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均独立提出。Outlines/vLLM constrained decoding 可能压缩 per-sample diversity，使 gap 成为实验设置 artifact。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决（承认但未量化）。R1 仍列 critical（需 logprob 分布分析）。共识：elevated should-fix，量化 logprob 分布而非增加 free-form 实验。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Round 5 两位 Reviewer 再次独立提出为 critical。Appendix F 已有 logprob tie 分析（60% instances range<0.05），但论文 claim scope（title/abstract/conclusion）仍未限定为 constrained decoding setting。Non-tied subset +2.9pp p=0.01 结果被两位 Reviewer 一致解读为 gap 主因是 score compression 而非 IE 固有属性。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 列 critical（要求 free-form 对照或 scope 限定）。R2 rebut 降为 should-fix：Layer 1 definitional gap 与 decoding 策略无关；free-form IE 实用性存疑。共识：论文 Title 已含 'under Constrained Decoding'，但 Introduction/Discussion 仍暗示 gap 是 IE 固有属性。需在 Introduction 和 Discussion 收紧 scope。\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 diversity；Paper Agent 写入论文 + 限定 scope\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"量化 logprob 分布（tie 定义 Δlogprob<ε, non-tie 子集 selection 能力）+ Discussion 中讨论 grammar compliance 如何压缩区分度\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"(a) Title/Abstract/Conclusion 限定 claim scope 为 constrained decoding setting；(b) 提升 Appendix F non-tied analysis 至主文 Discussion；(c) 明确承认 non-tied evidence 对 claim 普适性的影响\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Introduction 和 Discussion 末尾各加 1 句明确声明 gap 发现 specific to constrained decoding regime；勿暗示为 IE 固有属性\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C2\"\n    summary: \"Failure-to-reject 不等于 evidence of absence，selection gap 统计论证不完整\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需修改措辞或补充等价性检验\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：TOST 已补充，措辞修正到位\"\n    action_items:\n      - round: 3\n        action: \"修改措辞 + 6/6 cumulative evidence 论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: TOST 等价检验已补充，措辞修正为 'no significant evidence'，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-C3\"\n    summary: \"N=8 核心结果 single seed (seed=42)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 1 N=8 和 Table 2 selection 全部 single seed\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：3-seed 验证已补充\"\n    action_items:\n      - round: 3\n        action: \"Limitations 中明确 single-seed 风险并引用 N=16 stability\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 3-seed 稳定性验证已补充，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"多重比较校正缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"SJ-EM CI lower bound +0.003 在 Bonferroni 下不会 survive\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：Bonferroni 声明已加\"\n    action_items:\n      - round: 3\n        action: \"声明未做多重比较校正 + SJ-EM 改为 suggestive\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: Bonferroni 声明已加，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需在 Discussion 中分离两层论证\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 两位 Reviewer 独立再次提出：Introduction 未正面论证 why not obvious a priori\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 认为 gap 被两头夹击（instance-level=tautological, logprob=artifact），整体 contribution 空心化。R1 rebut：consensus-proximity/MBR failure 是 non-trivial empirical finding，但同意 logprob artifact 是 real concern。共识：gap 不完全 tautological（MBR 在 MT 成功 IE 失败是非平凡的），但 C2 应以 logprob+MBR failure 为重心。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次达成共识：Abstract/Introduction 仍将 '4/5 signals fail' 与 logprob failure 并列呈现。应先一句话 dismiss instance-level 信号（by definition），然后聚焦 consensus-proximity failure 和 logprob score compression 作为论文的真正实证贡献。\"\n    action_items:\n      - round: 3\n        action: \"Discussion 中分离两层论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"(a) Introduction 正面论证 why gap is not obvious (MBR MT vs IE 对比); (b) Discussion 明确分离定义性局限 vs 经验性失败\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"Reframe C2: 以 logprob score compression + MBR/consensus-proximity empirical failure 为中心，弱化 '5 signals all fail' 叙事\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Abstract 和 Introduction 重构：先 dismiss instance-level selection（definitional, 1 句），然后聚焦 consensus-proximity/MBR failure + logprob compression 作为核心贡献\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"MBR decoding 是成熟替代方案但未讨论\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：MBR 连接已补充\"\n    action_items:\n      - round: 3\n        action: \"明确 consensus-proximity 与 MBR 联系 + 引用 MBR 文献\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: §5 MBR decoding 连接段已写入\"\n    resolution_round: 4\n\n  - id: \"R3-W4\"\n    summary: \"FK 独立性假设 justification 不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"§3.2 一句 hand-wave。需报告 inter-sample correlation\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：excess agreement 数据已补充\"\n      - round: 5\n        reviewers: [1]\n        note: \"R1 重新提出：excess agreement (-0.4% to -4.0%) 未注明在哪个 configuration 测量，未提供所有配置数据，未引用 FK 在非独立 rater 下的行为分析文献。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 再提 excess agreement 无显著性检验（permutation test / bootstrap CI）。R2 同意但认为 FK 非核心 contribution，severity 偏低。当前论文措辞 'sufficient response diversity' 不准确，应改为 'mild negative dependence'。\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 inter-sample correlation；Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"(a) 注明 excess agreement 的 configuration；(b) 补充所有配置数据或至少说明范围；(c) 引用 FK 在非独立 rater 下的行为文献\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"将 'sufficient response diversity' 改为 'mild negative dependence'；注明 excess agreement 覆盖的 configurations\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"Cross-model 实为 cross-architecture at fixed 8B scale\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两模型均 8B，措辞过度外推\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：cross-architecture 措辞已统一\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出：Conclusion 仍用 'across model families' 而非限定 'at 8B scale'。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍未修复。Section 1, Section 4.1, Conclusion 多处使用 'cross-model' 或 'across models' 无 scale 限定。两位 Reviewer 共识改为 'across two model families at 8B scale'。\"\n    action_items:\n      - round: 5\n        action: \"Conclusion 和 Abstract 统一加 'at 8B scale' 限定\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"全文统一：'cross-model' → 'across two model families at 8B scale'\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W6\"\n    summary: \"'First multi-family comparison' claim scope 过宽\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需限定为 structured IE 的 QE + selection\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认部分解决：Conclusion 有 hedge 但 Introduction 仍断言式\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"通过堆叠修饰词确保 'first' 成立属于 scope engineering。建议改为描述性表述。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 将此列为 must-fix N1 的一部分：Contribution 1 本质是 engineering benchmark，应降级为 setup/methodology。R1 agree。共识：去掉 'first' claim，将 Contribution 1 降级，以 gap + logprob 诊断为核心。\"\n    action_items:\n      - round: 5\n        action: \"Introduction 和 Conclusion 去掉 'first' claim，改为描述性表述\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Contribution 1 降级为 methodology/setup；Contribution 2 (gap + logprob compression) 提升为核心\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"confidence signal vs consistency signal 混用；VC vs Voting Conf.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决：表格缩写 VC/Voting Conf. 仍不统一\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"仍未解决。Table 1 'Voting Conf.'，Table 4/7 'VC'，正文 'entity voting'。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"第 4 轮仍未解决。还发现 LP/Log-prob/logprob 三种写法。两位 Reviewer 共识：统一为一套缩写（VC, SJ, FK, EM, LP），全文表格/正文一致。\"\n    action_items:\n      - round: 5\n        action: \"全文统一表格缩写（建议全部用 VC）+ 正文首次出现时写全称\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"全文统一：VC / SJ / FK / EM / LP 五个缩写，表格和正文一致使用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"遗漏引用：VerifiNER, RASC, MBR decoding, Malinin & Gales\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"VerifiNER, MBR decoding 等高度相关\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：引用已补全\"\n    action_items:\n      - round: 3\n        action: \"补充引用并在 Related Work 中讨论\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 引用已补全，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"WNUT-17 '54% zero F1' 与 Table 7 数据不一致 (51.5%)\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"355/689 ≈ 51.5% vs 正文 54%\"\n    action_items:\n      - round: 3\n        action: \"Agent 核实实际数字 → Paper Agent 统一\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"54% → 52% 已修正，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"EM selection exclusion 缺乏经验支持\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"'probability negligible' 需报告 exact match pairs 频率\"\n    action_items:\n      - round: 3\n        action: \"Agent 计算 exact match pairs 频率 → Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"EM 已加入 Table 2，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Ethics Statement 缺失\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"共识降为 minor\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 Ethics Statement 已存在但位于 Limitations section 内\"\n      - round: 5\n        reviewers: [2]\n        note: \"Ethics Statement 现为独立 section，格式合规\"\n    action_items:\n      - round: 4\n        action: \"将 Ethics Statement 从 Limitations 内移出为独立 section\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: Ethics Statement 已为独立 section，格式合规\"\n    resolution_round: 5\n\n  - id: \"R3-M4\"\n    summary: \"ρ-AUROC dissociation 作为独立发现过度强调\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议承认统计预期性后聚焦实践含义\"\n    action_items:\n      - round: 3\n        action: \"§4.2 承认 dissociation 的统计预期性\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已承认统计预期性，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M5\"\n    summary: \"对 Nedellec (2026) 措辞偏 adversarial\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议用更 neutral 语气\"\n    action_items:\n      - round: 3\n        action: \"Introduction 中改为更 neutral 的语气\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Nedellec 措辞已改为 neutral，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M6\"\n    summary: \"LOO-SJ 验证中 Δρ 和 per-instance Δρ 量纲混淆\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"Δρ=−0.014 vs per-instance max Δρ=3.1×10⁻⁴ 量纲不同\"\n    action_items:\n      - round: 3\n        action: \"澄清 per-instance Δρ 具体含义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"LOO-SJ Δρ 含义已澄清，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M7\"\n    summary: \"Figure 1 caption 引入未直接可视化的 p=0.39\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"建议加 '(Table 2)' 交叉引用\"\n    action_items:\n      - round: 3\n        action: \"补 '(Table 2)' 交叉引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Figure 1 caption 交叉引用已补，Round 4 未再提及\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (updated with Round 6)\n  # ============================================================\n  - id: \"R4-C1\"\n    summary: \"训练配置和 prompt template 缺失，影响独立复现\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"§4.1 仅报告 LoRA rank=32, α=64, 5 epochs, LLaMA Factory，缺少 lr, batch size 等\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Appendix E 已包含完整 Table 8 + prompt template。两位 Reviewer 均给 Reproducibility 4/5。\"\n    action_items:\n      - round: 4\n        action: \"附录补充完整训练配置表 + NER/RE prompt template 示例\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: Appendix E Table 8 完整，Reproducibility 4/5\"\n    resolution_round: 5\n\n  - id: \"R4-W1\"\n    summary: \"RE 证据需进一步加强（conditional analysis 或降级）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"claim 降级已完成，但两位 Reviewer 仍认为 RE 证据薄弱\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Abstract 标注 '(SciERC, preliminary)' 但后续 Table 1/2, Discussion 大量使用 RE 结果无 preliminary 限定。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍存在。238 个 non-zero F1 instances，per-relation 变异极大（Feature-Of ρ=0.004 vs Hyponym-Of ρ=0.646）。Discussion/Conclusion 引用 RE 结论时缺少一致的 preliminary 标注。R1 建议将 RE 更多移入 Appendix；R2 建议每次引用 RE 结论时加 '(preliminary, single benchmark)' 后缀。\"\n    action_items:\n      - round: 5\n        action: \"(a) 所有 RE 分析处一致标注 single-benchmark preliminary；(b) Contribution #3 加 RE 限定；(c) Future work 明确列出 RE 多数据集验证\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Discussion/Conclusion 中每次引用 RE 结论时一致标注 '(preliminary, single benchmark)'；考虑将 RE selection results 移入 Appendix\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W2\"\n    summary: \"SJ vs EM 优势叙事应改为 difficulty-dependent complementarity\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"SJ vs EM Δρ=+0.065, Bonferroni 下不显著\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§4.2 已使用 complementarity 措辞\"\n    action_items:\n      - round: 4\n        action: \"Contribution #1 弱化 structural advantage，改为 difficulty-dependent complementarity\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: §4.2 已用 complementarity 措辞\"\n    resolution_round: 5\n\n  - id: \"R4-W3\"\n    summary: \"Abstract 过于密集，第 4 行超长句子需拆分\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"多层嵌套括号和分号的超长句子\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"仍未修改。9 行含 5 signal/3 family/4 metric/3 dataset/2 model + gap 概念。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"第 3 轮仍未解决。两位 Reviewer 共识：减少具体数字，将 signal family 名称移到正文；abstract 聚焦问题-发现-意义三段式。\"\n    action_items:\n      - round: 5\n        action: \"Abstract 拆分为 2-3 句核心 claim，将具体信号名/数字/family 移入 Introduction\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Abstract 精简为问题-发现-意义三段式，移除大部分具体数字和信号名\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W4\"\n    summary: \"缺少 Xiong et al. (2024) 'Can LLMs Express Their Uncertainty?' ICLR 2024\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"系统评估 LLM 置信度获取方法\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Related Work §2 已引用 Xiong et al.\"\n    action_items:\n      - round: 4\n        action: \"Related Work 引用 Xiong et al.\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: 已引用，§2 第三段\"\n    resolution_round: 5\n\n  - id: \"R4-M1\"\n    summary: \"SJ normalizer 选择（max vs union）缺乏对比\"\n    category: method\n    severity: info\n    status: wont_fix\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"max(|g_i|,|g_j|) vs |g_i∪g_j| 未比较\"\n    action_items:\n      - round: 4\n        action: \"附录补 union normalizer 结果或提供理论依据\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: wont_fix\n    resolution: \"max normalizer 设计已在 method.tex 有理由，超出 scope\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"TOST δ 选择（±2/3/5 pp）缺乏实践意义论证\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"δ 选择直接影响等价结论\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再提：与 IAA 关联无引用。R2 认为多水平 δ 已构成 sensitivity analysis。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 升级为 must-fix：IAA 变异 ≠ selector 预期增益，概念不匹配。δ=5pp 在 13pp oracle headroom 中 = 放弃 38%。R2 agree，建议报告 breakpoint δ* 和直接报告 effect size/bootstrap CI（已部分有 d=0.038 和 CI [-3.0, +4.2]pp）。\"\n    action_items:\n      - round: 5\n        action: \"引用 1-2 篇 IE benchmark IAA 数据来锚定 δ 选择\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"(a) 用 SESOI 框架或 oracle headroom 比例来论证 δ；(b) 报告 breakpoint δ*（使结论翻转的最小 δ）；(c) 强化 effect size (Cohen's d) + bootstrap CI 作为主要证据\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-M3\"\n    summary: \"Table 1 N=16 block 大面积空白\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"N=16 仅填 LLaMA CoNLL，SciERC 空白\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"已加脚注但格式可能异常\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍建议将 N=16 行移入 Appendix Table 3，简化 Table 1\"\n    action_items:\n      - round: 6\n        action: \"Table 1 删除 N=16 行，合并到 Appendix Table 3\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 5 issues (updated with Round 6)\n  # ============================================================\n  - id: \"R5-N1\"\n    summary: \"与 Nédellec et al. (2026) 的增量贡献不充分\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"三个增量均偏弱。共识：Findings-worthy 但非 ground-breaking。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 再提为 N1 的一部分（Contribution 1 framing）。R1 agree。共识：增量贡献本身存在但论文过度强调。应更诚实地量化增量；强调 WNUT-17 conditional collapse 和 logprob negative correlation 作为 non-obvious findings。\"\n    action_items:\n      - round: 5\n        action: \"更诚实地量化增量大小\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Introduction 中降低 Contribution 1 的 claim 强度；将 WNUT-17 conditional collapse + logprob ρ=-0.410 提升为显式 non-obvious finding\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W1\"\n    summary: \"Qwen3-8B thinking token 训练不一致（SciERC vs CoNLL/WNUT）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"SciERC 未显式禁用 enable_thinking，CoNLL/WNUT 显式设 false。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次独立提出。R1 指出 thinking token 可能影响 SciERC logprob 分布，进而影响 score compression 诊断。R2 补充：如果 thinking tokens 改变了 logprob scale，'60% instances tied' 这个数字可能在 thinking-disabled 训练下不同。共识：在 Experiments Setup 中 prominently 声明此 confound（非仅脚注/Limitations），让 reader 在解读 cross-dataset 比较时有背景。\"\n    action_items:\n      - round: 5\n        action: \"Limitations 讨论此不一致性\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Experiments Setup §4.1 中显著声明 Qwen3 thinking token 训练不一致（非仅脚注）；Limitations 中扩展讨论其对 logprob 分布的潜在影响\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W2\"\n    summary: \"Semantic entropy 脚注比较可能误导\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 建议删除或缩短；R2 认为意图合理但执行可能误导。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 agree 删除；R2 rebut（认为脚注作为 scale context 有价值）。分歧：R1 无用 vs R2 有用。共识：缩短脚注，去掉具体数字。\"\n    action_items:\n      - round: 6\n        action: \"缩短脚注，保留 'comparable AUROC on discrete-answer QA' 但去掉具体 0.75-0.85 数字\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W3\"\n    summary: \"he2024uncertainty bib entry 与引用上下文不匹配\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1]\n        note: \"bib 标题是 sequential labeling 论文，但引用上下文是 LLM UQ survey\"\n    action_items:\n      - round: 5\n        action: \"修正引用上下文描述，或替换为正确的 LLM UQ survey 引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M1\"\n    summary: \"缺少 test-time scaling verification survey 引用\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 建议补 verification survey，R1 同意\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 具体指出 Zhang et al. (2025) 'A Survey on Test-Time Scaling in LLMs'。R1 rebut：survey 引用非 critical（已引用原始工作），降为 minor。共识：should-fix，camera-ready 补充。\"\n    action_items:\n      - round: 6\n        action: \"Related Work §2 ¶1 补充 Zhang et al. (2025) TTS survey 引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M2\"\n    summary: \"缺少 MBR 在非 MT 任务中的应用引用\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Discussion §5 将方法与 MBR 对接但只引用 MT 领域。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 具体指出 Eikema, Rutkiewicz & Giulianelli (EMNLP 2025) 'Structure-Conditional MBR Decoding'——直接研究 MBR 在结构化输出上的问题。R1 agree 为 should-fix。\"\n    action_items:\n      - round: 6\n        action: \"Discussion §5 MBR 段补充 Eikema et al. (EMNLP 2025) 并讨论其 utility function 在结构化输出上不适用的发现与本文 MBR failure 的互证\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M3\"\n    summary: \"Consensus-proximity = LOO-SJ 等价性缺少推导\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§3.3 声称数学等价但未给出推导。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Appendix D 已包含完整等价性证明（constant factor 1/(N-1) argument + self-comparison constant），并报告 empirical Δρ=-0.014 和 max per-instance diff 3.1×10⁻⁴。Round 6 未再提出。\"\n    action_items:\n      - round: 5\n        action: \"附录补简要推导\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Appendix D 已包含完整等价性证明，Round 6 未再提出\"\n    resolution_round: 6\n\n  - id: \"R5-C1\"\n    summary: \"Constrained decoding 混淆变量未隔离，claim scope 与 evidence 不匹配\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Title/Abstract/Conclusion 需限定 constrained decoding scope。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"与 R3-C1 合并追踪。Title 已含 'under Constrained Decoding'，但 Introduction/Discussion 仍暗示 gap 是 IE 固有属性。\"\n    action_items:\n      - round: 5\n        action: \"Title 加 'under Constrained Decoding'; scope 限定\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 6\n        action: \"见 R3-C1 Round 6 action\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-C2\"\n    summary: \"Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"4/5 instance-level failure = tautological; logprob failure = artifact。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"与 R3-W2 合并追踪。共识：重构叙事以 logprob compression + MBR failure 为中心。\"\n    action_items:\n      - round: 5\n        action: \"Reframe C2 聚焦 logprob compression + MBR failure\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"见 R3-W2 Round 6 action\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W4\"\n    summary: \"'First multi-family comparison' claim = scope engineering\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"建议改为描述性表述\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"与 R3-W6 合并追踪。\"\n    action_items:\n      - round: 5\n        action: \"'first' → 'a systematic'\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"见 R3-W6 Round 6 action\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W5\"\n    summary: \"'Cross-architecture' 用词过度（两个 8B decoder-only）\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"改为 'across two model families at 8B scale'\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"与 R3-W5 合并追踪。\"\n    action_items:\n      - round: 5\n        action: \"全文替换 cross-architecture\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"见 R3-W5 Round 6 action\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W6\"\n    summary: \"FK independence justification 不够严格\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Excess agreement 未注明 configuration，未引用文献\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"与 R3-W4 合并追踪。\"\n    action_items:\n      - round: 5\n        action: \"补 configuration 信息 + 引用文献\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"见 R3-W4 Round 6 action\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W7\"\n    summary: \"SJ 方法论新颖性有限，'core structural signal' 过度宣传\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"R2 认为标准技术组合。共识: application novelty 但不应过度宣传。\"\n    action_items:\n      - round: 5\n        action: \"'core structural signal' → 'primary structural signal'\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M4\"\n    summary: \"部分 bib entries 在 OpenAlex 未找到或 author name 有 variant\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"hobelsberger2025systematic, lightman2024verify 未找到; feng2025optimal, ye2025uncertainty author name 可能有 variant\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 补充：snell2024scaling key 标 2024 但 venue 为 ICLR 2025。ye2025uncertainty 第一作者可能为 Heo。两位 Reviewer 均同意需核实。\"\n    action_items:\n      - round: 6\n        action: \"(a) ye2025uncertainty 核实第一作者 Ye vs Heo；(b) snell2024scaling 统一 key/year 为 2025；(c) feng2025optimal 核实 author 顺序；(d) hobelsberger2025systematic, venktesh2025trust 确认 arXiv ID\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M5\"\n    summary: \"Ethics Statement 仅 2 句，内容偏简\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"格式合规但内容偏简\"\n      - round: 6\n        reviewers: [2]\n        note: \"R2 补充：应注明 CoNLL-2003 基于 Reuters 语料的 license 限制。R1 agree。\"\n    action_items:\n      - round: 6\n        action: \"Ethics Statement 补充 CoNLL-2003 Reuters license 注明\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-Q4\"\n    summary: \"WNUT-17 logprob 负相关 (ρ=-0.410) 机制未解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"capability boundary 下 logprob 反映 fluency 而非 accuracy。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§4.2 已加机制假设（overconfidence on OOD inputs, Xiong et al. 引用），解释 logprob 在 capability boundary 处与 accuracy 反相关。Round 6 未再单独提出。\"\n    action_items:\n      - round: 5\n        action: \"§4 加机制解释\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"§4.2 已包含 overconfidence 假设，引用 Xiong et al.\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 new issues\n  # ============================================================\n  - id: \"R6-W1\"\n    summary: \"VC 公式（Eq.6）与实现不一致：无阈值 vs majority threshold\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Equation 6 定义为所有 entity 平均频率（无阈值），但 Footnote 2 承认实现使用 majority threshold (>N/2)。两者数学上不等价。Footnote 说 'slightly different absolute values but identical qualitative conclusions' 但未提供量化差异（如两种实现的 ρ 对比）。影响可复现性。\"\n    action_items:\n      - round: 6\n        action: \"(a) 统一公式和实现——改公式反映 threshold，或改实现匹配公式；(b) 报告两种实现的 ρ 差值；(c) 明确 Table 1 报告的是哪种实现\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W2\"\n    summary: \"Figure 1 caption 冗余——重复 Section 4.2/4.3 内容\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Figure 1 caption 引入 p=0.39、Table 2 引用、详细数字等——与正文重复。应更简洁。\"\n    action_items:\n      - round: 6\n        action: \"精简 Figure 1 caption，保留图表要传达的核心信息\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues (all resolved)\n  # ============================================================\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B）\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"model-agnostic 与 Limitations 矛盾\"\n    action_items:\n      - round: 1\n        action: \"全文替换 model-agnostic → consistent across tested model families\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 确认措辞修正到位，无再提\"\n    resolution_round: 2\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"新遗漏：Optimal SC, Difficulty-Adaptive SC\"\n    action_items:\n      - round: 1\n        action: \"补充 6 篇引用到 Related Work\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏\"\n    resolution_round: 2\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 4\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"需跨数据集验证或降级措辞\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Abstract RE 措辞需修正\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\"\n    action_items:\n      - round: 1\n        action: \"降级措辞 universal → observed in SciERC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"Abstract 改为 NER (three datasets) and RE (SciERC)\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议\"\n    resolution_round: 4\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Nedellec 增量贡献论证不足 + 引用错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强增量贡献论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认三点差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams\"\n    action_items: []\n    resolution: \"论文已包含 6 个 figures\"\n    resolution_round: 1\n\n  - id: \"R0-C6\"\n    summary: \"成本分析 negligible 误导\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8-16× 推理开销不应描述为 negligible\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"互补性已证明但未尝试组合\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Bootstrap 细节不足\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n    resolution_round: 2\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling +0.018 与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"+0.018 实际为 -0.080\"\n    action_items:\n      - round: 0\n        action: \"修正声明\"\n        assigned_to: \"Main Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 1 issues (all resolved)\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"p=0.39 支撑核心结论但细节缺失\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价统计规范达到高标准\"\n    resolution_round: 2\n\n  - id: \"R1-N2\"\n    summary: \"Gap 解释力不足 + logprob 失败未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"4/5 定义性 + logprob 机制缺失\"\n    action_items:\n      - round: 1\n        action: \"区分 by-design vs empirical + logprob failure 分析段\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 logprob failure analysis 充分\"\n    resolution_round: 2\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 单薄\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"consensus-proximity = LOO-SJ 是表述问题\"\n    action_items:\n      - round: 1\n        action: \"显式说明等价关系\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 consensus-proximity = LOO-SJ 已明确\"\n    resolution_round: 2\n\n  - id: \"R1-N4\"\n    summary: \"Nedellec 引用错误 + 增量贡献弱\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Yao vs Nédellec 事实错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"SJ 形式化有歧义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Hungarian threshold + max denominator 需补充\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R3-R1 再次指出 Hungarian cost function 未明确 maximize/minimize 方向, zero-IoU pairs 处理方式缺失\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 Round 4 确认 SJ 形式化已完善 [RESOLVED]\"\n    action_items:\n      - round: 1\n        action: \"补全 Eq(4) 定义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"补 threshold 说明 + max vs union 设计理由\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"补 Hungarian optimization objective (max-weight matching on IoU) + zero-IoU pairs handling\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: R2 确认 SJ 形式化已完善，Hungarian matching 描述清晰\"\n    resolution_round: 4\n\n  - id: \"R1-W2\"\n    summary: \"Voting-SJ 冗余度未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"instance-level correlation 未报告\"\n    action_items:\n      - round: 1\n        action: \"报告 Voting-SJ ρ=0.659/0.605\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"中等相关数据已报告\"\n    resolution_round: 2\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 缺 contextualization\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 cross-method footnote\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote: semantic entropy AUROC comparison + cross-task caveat\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度数据缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"robustness 结论需限定\"\n    action_items:\n      - round: 1\n        action: \"限定为 consistency-based signals robust; logprob uncharacterized\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞限定到位\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 establishing 措辞过度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"fail to reject ≠ accept\"\n    action_items:\n      - round: 1\n        action: \"establishing → consistent with/suggests\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R1-W6\"\n    summary: \"LLaMA 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"LLaMA fine-tuning 状态未说明\"\n    action_items:\n      - round: 1\n        action: \"明确两模型 identical LoRA 配置\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 未再提及\"\n    resolution_round: 2\n\n  - id: \"R1-W7\"\n    summary: \"约束解码 diversity 影响\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展为全局 confound + Limitations 条目\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 新增条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已扩展为全局 confound 讨论\"\n    resolution_round: 2\n\n  - id: \"R1-W8\"\n    summary: \"first systematic 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"需收窄 scope\"\n    action_items:\n      - round: 1\n        action: \"first multi-family\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 无再提\"\n    resolution_round: 2\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Optimal SC, Difficulty-Adaptive SC 等\"\n    action_items:\n      - round: 1\n        action: \"补充引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认无遗漏\"\n    resolution_round: 2\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 分析浅\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"EM=1 压缩效应需主文提及\"\n    action_items:\n      - round: 1\n        action: \"Section 5 简述 + 引导 Appendix\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 dissociation 分析为 actionable finding\"\n    resolution_round: 2\n\n  - id: \"R1-M1\"\n    summary: \"Logistic regression proxy 无结果\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"展示结果或删除\"\n    action_items:\n      - round: 1\n        action: \"删除提及\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已删除\"\n    resolution_round: 2\n\n  - id: \"R1-M2\"\n    summary: \"GSM8K +18pp 未注明模型\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"补注 PaLM-540B\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告 CI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"within 3-seed σ≈0.007\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 2 issues (all resolved)\n  # ============================================================\n  - id: \"R2-C1\"\n    summary: \"Selection 证据面过窄——仅 1 dataset × 1 model\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需补 LLaMA SciERC + CoNLL selection\"\n    action_items:\n      - round: 2\n        action: \"补 4 配置 selection 分析 + Appendix Table 6\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"6 configurations 全部补齐，无 signal 显著超越 greedy\"\n    resolution_round: 2\n\n  - id: \"R2-C2\"\n    summary: \"WNUT-17 仅报告 1 个信号\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"5 signals 中仅 SJ 一个数据点\"\n    action_items:\n      - round: 2\n        action: \"补全 5 信号 full/conditional ρ + AUROC + Appendix Table 5\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"WNUT-17 全信号表完整，叙事修正为区分 full-set vs conditional\"\n    resolution_round: 2\n\n  - id: \"R2-W1\"\n    summary: \"ρ=0.38 缺 cross-method 对比\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 footnote 引用 semantic entropy AUROC\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R2-W2\"\n    summary: \"N=8 QE ρ 无 uncertainty\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap CIs\"\n    action_items:\n      - round: 2\n        action: \"计算 B=10,000 bootstrap CI + Appendix 表\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Bootstrap CI 表已加入 Appendix，SJ-logprob 显著\"\n    resolution_round: 2\n\n  - id: \"R2-W3\"\n    summary: \"SJ Hungarian threshold + max denominator\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"无 threshold 声明需验证\"\n    action_items:\n      - round: 2\n        action: \"代码验证 + method.tex 补充\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"无 threshold, 96.6% pairs sim≥0.5, max denominator 已解释\"\n    resolution_round: 2\n\n  - id: \"R2-W4\"\n    summary: \"RE selection 无统计检验\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap p-value\"\n    action_items:\n      - round: 2\n        action: \"RE bootstrap + 补 p=0.80 到论文\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"RE logprob p=0.80, all signals below greedy\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Constrained decoding 全局 confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展到全局 + Limitations\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已处理\"\n    resolution_round: 2\n\n  - id: \"R2-W6\"\n    summary: \"Abstract RE 措辞误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"NER (three datasets) and RE (SciERC)\"\n    action_items:\n      - round: 2\n        action: \"修正 Abstract\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R2-W7\"\n    summary: \"n=529 vs 551 未解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"22 instances filtering criteria\"\n    action_items:\n      - round: 2\n        action: \"补一句说明\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已说明 gold-empty filtering\"\n    resolution_round: 2\n\n  - id: \"R2-DATA\"\n    summary: \"RE selection 数据矛盾 (Table 2 vs L129)\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"Table 2 logprob=0.395 (-0.9pp) vs L129 logprob=0.410 (+0.6pp)\"\n    action_items:\n      - round: 2\n        action: \"Agent 确认 Table 2 正确 → Paper Agent 修正 L129\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"L129 统一为 logprob=0.395, -0.9pp, p=0.80\"\n    resolution_round: 2\n\n  - id: \"R2-AUROC\"\n    summary: \"L64 AUROC 归属错误 (Voting ρ 配 EM AUROC)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"corresponding 暗示同一信号\"\n    action_items:\n      - round: 2\n        action: \"分别标注 Voting ρ 和 EM AUROC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已拆分归属\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3+ issues (updated with Round 6 status)\n  # ============================================================\n  - id: \"R3-C1\"\n    summary: \"Constrained decoding 是 correlation-selection gap 的未控制混淆变量\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均独立提出。Outlines/vLLM constrained decoding 可能压缩 per-sample diversity，使 gap 成为实验设置 artifact。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决（承认但未量化）。R1 仍列 critical（需 logprob 分布分析）。共识：elevated should-fix，量化 logprob 分布而非增加 free-form 实验。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Round 5 两位 Reviewer 再次独立提出为 critical。Appendix F 已有 logprob tie 分析（60% instances range<0.05），但论文 claim scope（title/abstract/conclusion）仍未限定为 constrained decoding setting。Non-tied subset +2.9pp p=0.01 结果被两位 Reviewer 一致解读为 gap 主因是 score compression 而非 IE 固有属性。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 列 critical（要求 free-form 对照或 scope 限定）。R2 rebut 降为 should-fix：Layer 1 definitional gap 与 decoding 策略无关；free-form IE 实用性存疑。共识：论文 Title 已含 'under Constrained Decoding'，但 Introduction/Discussion 仍暗示 gap 是 IE 固有属性。需在 Introduction 和 Discussion 收紧 scope。\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 diversity；Paper Agent 写入论文 + 限定 scope\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"量化 logprob 分布（tie 定义 Δlogprob<ε, non-tie 子集 selection 能力）+ Discussion 中讨论 grammar compliance 如何压缩区分度\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"(a) Title/Abstract/Conclusion 限定 claim scope 为 constrained decoding setting；(b) 提升 Appendix F non-tied analysis 至主文 Discussion；(c) 明确承认 non-tied evidence 对 claim 普适性的影响\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Introduction 和 Discussion 末尾各加 1 句明确声明 gap 发现 specific to constrained decoding regime；勿暗示为 IE 固有属性\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C2\"\n    summary: \"Failure-to-reject 不等于 evidence of absence，selection gap 统计论证不完整\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需修改措辞或补充等价性检验\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：TOST 已补充，措辞修正到位\"\n    action_items:\n      - round: 3\n        action: \"修改措辞 + 6/6 cumulative evidence 论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: TOST 等价检验已补充，措辞修正为 'no significant evidence'，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-C3\"\n    summary: \"N=8 核心结果 single seed (seed=42)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 1 N=8 和 Table 2 selection 全部 single seed\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：3-seed 验证已补充\"\n    action_items:\n      - round: 3\n        action: \"Limitations 中明确 single-seed 风险并引用 N=16 stability\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 3-seed 稳定性验证已补充，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"多重比较校正缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"SJ-EM CI lower bound +0.003 在 Bonferroni 下不会 survive\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：Bonferroni 声明已加\"\n    action_items:\n      - round: 3\n        action: \"声明未做多重比较校正 + SJ-EM 改为 suggestive\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: Bonferroni 声明已加，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需在 Discussion 中分离两层论证\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 两位 Reviewer 独立再次提出：Introduction 未正面论证 why not obvious a priori\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 认为 gap 被两头夹击（instance-level=tautological, logprob=artifact），整体 contribution 空心化。R1 rebut：consensus-proximity/MBR failure 是 non-trivial empirical finding，但同意 logprob artifact 是 real concern。共识：gap 不完全 tautological（MBR 在 MT 成功 IE 失败是非平凡的），但 C2 应以 logprob+MBR failure 为重心。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次达成共识：Abstract/Introduction 仍将 '4/5 signals fail' 与 logprob failure 并列呈现。应先一句话 dismiss instance-level 信号（by definition），然后聚焦 consensus-proximity failure 和 logprob score compression 作为论文的真正实证贡献。\"\n    action_items:\n      - round: 3\n        action: \"Discussion 中分离两层论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"(a) Introduction 正面论证 why gap is not obvious (MBR MT vs IE 对比); (b) Discussion 明确分离定义性局限 vs 经验性失败\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"Reframe C2: 以 logprob score compression + MBR/consensus-proximity empirical failure 为中心，弱化 '5 signals all fail' 叙事\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Abstract 和 Introduction 重构：先 dismiss instance-level selection（definitional, 1 句），然后聚焦 consensus-proximity/MBR failure + logprob compression 作为核心贡献\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"MBR decoding 是成熟替代方案但未讨论\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：MBR 连接已补充\"\n    action_items:\n      - round: 3\n        action: \"明确 consensus-proximity 与 MBR 联系 + 引用 MBR 文献\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: §5 MBR decoding 连接段已写入\"\n    resolution_round: 4\n\n  - id: \"R3-W4\"\n    summary: \"FK 独立性假设 justification 不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"§3.2 一句 hand-wave。需报告 inter-sample correlation\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：excess agreement 数据已补充\"\n      - round: 5\n        reviewers: [1]\n        note: \"R1 重新提出：excess agreement (-0.4% to -4.0%) 未注明在哪个 configuration 测量，未提供所有配置数据，未引用 FK 在非独立 rater 下的行为分析文献。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 再提 excess agreement 无显著性检验（permutation test / bootstrap CI）。R2 同意但认为 FK 非核心 contribution，severity 偏低。当前论文措辞 'sufficient response diversity' 不准确，应改为 'mild negative dependence'。\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 inter-sample correlation；Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"(a) 注明 excess agreement 的 configuration；(b) 补充所有配置数据或至少说明范围；(c) 引用 FK 在非独立 rater 下的行为文献\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"将 'sufficient response diversity' 改为 'mild negative dependence'；注明 excess agreement 覆盖的 configurations\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"Cross-model 实为 cross-architecture at fixed 8B scale\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两模型均 8B，措辞过度外推\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：cross-architecture 措辞已统一\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出：Conclusion 仍用 'across model families' 而非限定 'at 8B scale'。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍未修复。Section 1, Section 4.1, Conclusion 多处使用 'cross-model' 或 'across models' 无 scale 限定。两位 Reviewer 共识改为 'across two model families at 8B scale'。\"\n    action_items:\n      - round: 5\n        action: \"Conclusion 和 Abstract 统一加 'at 8B scale' 限定\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"全文统一：'cross-model' → 'across two model families at 8B scale'\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W6\"\n    summary: \"'First multi-family comparison' claim scope 过宽\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需限定为 structured IE 的 QE + selection\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认部分解决：Conclusion 有 hedge 但 Introduction 仍断言式\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"通过堆叠修饰词确保 'first' 成立属于 scope engineering。建议改为描述性表述。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 将此列为 must-fix N1 的一部分：Contribution 1 本质是 engineering benchmark，应降级为 setup/methodology。R1 agree。共识：去掉 'first' claim，将 Contribution 1 降级，以 gap + logprob 诊断为核心。\"\n    action_items:\n      - round: 5\n        action: \"Introduction 和 Conclusion 去掉 'first' claim，改为描述性表述\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Contribution 1 降级为 methodology/setup；Contribution 2 (gap + logprob compression) 提升为核心\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 6\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"confidence signal vs consistency signal 混用；VC vs Voting Conf.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决：表格缩写 VC/Voting Conf. 仍不统一\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"仍未解决。Table 1 'Voting Conf.'，Table 4/7 'VC'，正文 'entity voting'。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"第 4 轮仍未解决。还发现 LP/Log-prob/logprob 三种写法。两位 Reviewer 共识：统一为一套缩写（VC, SJ, FK, EM, LP），全文表格/正文一致。\"\n    action_items:\n      - round: 5\n        action: \"全文统一表格缩写（建议全部用 VC）+ 正文首次出现时写全称\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"全文统一：VC / SJ / FK / EM / LP 五个缩写，表格和正文一致使用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"遗漏引用：VerifiNER, RASC, MBR decoding, Malinin & Gales\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"VerifiNER, MBR decoding 等高度相关\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：引用已补全\"\n    action_items:\n      - round: 3\n        action: \"补充引用并在 Related Work 中讨论\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 引用已补全，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"WNUT-17 '54% zero F1' 与 Table 7 数据不一致 (51.5%)\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"355/689 ≈ 51.5% vs 正文 54%\"\n    action_items:\n      - round: 3\n        action: \"Agent 核实实际数字 → Paper Agent 统一\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"54% → 52% 已修正，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"EM selection exclusion 缺乏经验支持\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"'probability negligible' 需报告 exact match pairs 频率\"\n    action_items:\n      - round: 3\n        action: \"Agent 计算 exact match pairs 频率 → Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"EM 已加入 Table 2，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Ethics Statement 缺失\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"共识降为 minor\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 Ethics Statement 已存在但位于 Limitations section 内\"\n      - round: 5\n        reviewers: [2]\n        note: \"Ethics Statement 现为独立 section，格式合规\"\n    action_items:\n      - round: 4\n        action: \"将 Ethics Statement 从 Limitations 内移出为独立 section\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: Ethics Statement 已为独立 section，格式合规\"\n    resolution_round: 5\n\n  - id: \"R3-M4\"\n    summary: \"ρ-AUROC dissociation 作为独立发现过度强调\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议承认统计预期性后聚焦实践含义\"\n    action_items:\n      - round: 3\n        action: \"§4.2 承认 dissociation 的统计预期性\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已承认统计预期性，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M5\"\n    summary: \"对 Nedellec (2026) 措辞偏 adversarial\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议用更 neutral 语气\"\n    action_items:\n      - round: 3\n        action: \"Introduction 中改为更 neutral 的语气\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Nedellec 措辞已改为 neutral，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M6\"\n    summary: \"LOO-SJ 验证中 Δρ 和 per-instance Δρ 量纲混淆\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"Δρ=−0.014 vs per-instance max Δρ=3.1×10⁻⁴ 量纲不同\"\n    action_items:\n      - round: 3\n        action: \"澄清 per-instance Δρ 具体含义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"LOO-SJ Δρ 含义已澄清，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M7\"\n    summary: \"Figure 1 caption 引入未直接可视化的 p=0.39\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"建议加 '(Table 2)' 交叉引用\"\n    action_items:\n      - round: 3\n        action: \"补 '(Table 2)' 交叉引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Figure 1 caption 交叉引用已补，Round 4 未再提及\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (updated with Round 6)\n  # ============================================================\n  - id: \"R4-C1\"\n    summary: \"训练配置和 prompt template 缺失，影响独立复现\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"§4.1 仅报告 LoRA rank=32, α=64, 5 epochs, LLaMA Factory，缺少 lr, batch size 等\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Appendix E 已包含完整 Table 8 + prompt template。两位 Reviewer 均给 Reproducibility 4/5。\"\n    action_items:\n      - round: 4\n        action: \"附录补充完整训练配置表 + NER/RE prompt template 示例\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: Appendix E Table 8 完整，Reproducibility 4/5\"\n    resolution_round: 5\n\n  - id: \"R4-W1\"\n    summary: \"RE 证据需进一步加强（conditional analysis 或降级）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"claim 降级已完成，但两位 Reviewer 仍认为 RE 证据薄弱\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Abstract 标注 '(SciERC, preliminary)' 但后续 Table 1/2, Discussion 大量使用 RE 结果无 preliminary 限定。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍存在。238 个 non-zero F1 instances，per-relation 变异极大（Feature-Of ρ=0.004 vs Hyponym-Of ρ=0.646）。Discussion/Conclusion 引用 RE 结论时缺少一致的 preliminary 标注。R1 建议将 RE 更多移入 Appendix；R2 建议每次引用 RE 结论时加 '(preliminary, single benchmark)' 后缀。\"\n    action_items:\n      - round: 5\n        action: \"(a) 所有 RE 分析处一致标注 single-benchmark preliminary；(b) Contribution #3 加 RE 限定；(c) Future work 明确列出 RE 多数据集验证\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Discussion/Conclusion 中每次引用 RE 结论时一致标注 '(preliminary, single benchmark)'；考虑将 RE selection results 移入 Appendix\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W2\"\n    summary: \"SJ vs EM 优势叙事应改为 difficulty-dependent complementarity\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"SJ vs EM Δρ=+0.065, Bonferroni 下不显著\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§4.2 已使用 complementarity 措辞\"\n    action_items:\n      - round: 4\n        action: \"Contribution #1 弱化 structural advantage，改为 difficulty-dependent complementarity\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: §4.2 已用 complementarity 措辞\"\n    resolution_round: 5\n\n  - id: \"R4-W3\"\n    summary: \"Abstract 过于密集，第 4 行超长句子需拆分\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"多层嵌套括号和分号的超长句子\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"仍未修改。9 行含 5 signal/3 family/4 metric/3 dataset/2 model + gap 概念。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"第 3 轮仍未解决。两位 Reviewer 共识：减少具体数字，将 signal family 名称移到正文；abstract 聚焦问题-发现-意义三段式。\"\n    action_items:\n      - round: 5\n        action: \"Abstract 拆分为 2-3 句核心 claim，将具体信号名/数字/family 移入 Introduction\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Abstract 精简为问题-发现-意义三段式，移除大部分具体数字和信号名\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W4\"\n    summary: \"缺少 Xiong et al. (2024) 'Can LLMs Express Their Uncertainty?' ICLR 2024\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"系统评估 LLM 置信度获取方法\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Related Work §2 已引用 Xiong et al.\"\n    action_items:\n      - round: 4\n        action: \"Related Work 引用 Xiong et al.\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: 已引用，§2 第三段\"\n    resolution_round: 5\n\n  - id: \"R4-M1\"\n    summary: \"SJ normalizer 选择（max vs union）缺乏对比\"\n    category: method\n    severity: info\n    status: wont_fix\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"max(|g_i|,|g_j|) vs |g_i∪g_j| 未比较\"\n    action_items:\n      - round: 4\n        action: \"附录补 union normalizer 结果或提供理论依据\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: wont_fix\n    resolution: \"max normalizer 设计已在 method.tex 有理由，超出 scope\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"TOST δ 选择（±2/3/5 pp）缺乏实践意义论证\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"δ 选择直接影响等价结论\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再提：与 IAA 关联无引用。R2 认为多水平 δ 已构成 sensitivity analysis。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 升级为 must-fix：IAA 变异 ≠ selector 预期增益，概念不匹配。δ=5pp 在 13pp oracle headroom 中 = 放弃 38%。R2 agree，建议报告 breakpoint δ* 和直接报告 effect size/bootstrap CI（已部分有 d=0.038 和 CI [-3.0, +4.2]pp）。\"\n    action_items:\n      - round: 5\n        action: \"引用 1-2 篇 IE benchmark IAA 数据来锚定 δ 选择\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"(a) 用 SESOI 框架或 oracle headroom 比例来论证 δ；(b) 报告 breakpoint δ*（使结论翻转的最小 δ）；(c) 强化 effect size (Cohen's d) + bootstrap CI 作为主要证据\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-M3\"\n    summary: \"Table 1 N=16 block 大面积空白\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"N=16 仅填 LLaMA CoNLL，SciERC 空白\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"已加脚注但格式可能异常\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍建议将 N=16 行移入 Appendix Table 3，简化 Table 1\"\n    action_items:\n      - round: 6\n        action: \"Table 1 删除 N=16 行，合并到 Appendix Table 3\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 5 issues (updated with Round 6)\n  # ============================================================\n  - id: \"R5-N1\"\n    summary: \"与 Nédellec et al. (2026) 的增量贡献不充分\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"三个增量均偏弱。共识：Findings-worthy 但非 ground-breaking。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 再提为 N1 的一部分（Contribution 1 framing）。R1 agree。共识：增量贡献本身存在但论文过度强调。应更诚实地量化增量；强调 WNUT-17 conditional collapse 和 logprob negative correlation 作为 non-obvious findings。\"\n    action_items:\n      - round: 5\n        action: \"更诚实地量化增量大小\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Introduction 中降低 Contribution 1 的 claim 强度；将 WNUT-17 conditional collapse + logprob ρ=-0.410 提升为显式 non-obvious finding\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W1\"\n    summary: \"Qwen3-8B thinking token 训练不一致（SciERC vs CoNLL/WNUT）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"SciERC 未显式禁用 enable_thinking，CoNLL/WNUT 显式设 false。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次独立提出。R1 指出 thinking token 可能影响 SciERC logprob 分布，进而影响 score compression 诊断。R2 补充：如果 thinking tokens 改变了 logprob scale，'60% instances tied' 这个数字可能在 thinking-disabled 训练下不同。共识：在 Experiments Setup 中 prominently 声明此 confound（非仅脚注/Limitations），让 reader 在解读 cross-dataset 比较时有背景。\"\n    action_items:\n      - round: 5\n        action: \"Limitations 讨论此不一致性\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"Experiments Setup §4.1 中显著声明 Qwen3 thinking token 训练不一致（非仅脚注）；Limitations 中扩展讨论其对 logprob 分布的潜在影响\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W2\"\n    summary: \"Semantic entropy 脚注比较可能误导\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 建议删除或缩短；R2 认为意图合理但执行可能误导。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 agree 删除；R2 rebut（认为脚注作为 scale context 有价值）。分歧：R1 无用 vs R2 有用。共识：缩短脚注，去掉具体数字。\"\n    action_items:\n      - round: 6\n        action: \"缩短脚注，保留 'comparable AUROC on discrete-answer QA' 但去掉具体 0.75-0.85 数字\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W3\"\n    summary: \"he2024uncertainty bib entry 与引用上下文不匹配\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1]\n        note: \"bib 标题是 sequential labeling 论文，但引用上下文是 LLM UQ survey\"\n    action_items:\n      - round: 5\n        action: \"修正引用上下文描述，或替换为正确的 LLM UQ survey 引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M1\"\n    summary: \"缺少 test-time scaling verification survey 引用\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 建议补 verification survey，R1 同意\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 具体指出 Zhang et al. (2025) 'A Survey on Test-Time Scaling in LLMs'。R1 rebut：survey 引用非 critical（已引用原始工作），降为 minor。共识：should-fix，camera-ready 补充。\"\n    action_items:\n      - round: 6\n        action: \"Related Work §2 ¶1 补充 Zhang et al. (2025) TTS survey 引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M2\"\n    summary: \"缺少 MBR 在非 MT 任务中的应用引用\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Discussion §5 将方法与 MBR 对接但只引用 MT 领域。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 具体指出 Eikema, Rutkiewicz & Giulianelli (EMNLP 2025) 'Structure-Conditional MBR Decoding'——直接研究 MBR 在结构化输出上的问题。R1 agree 为 should-fix。\"\n    action_items:\n      - round: 6\n        action: \"Discussion §5 MBR 段补充 Eikema et al. (EMNLP 2025) 并讨论其 utility function 在结构化输出上不适用的发现与本文 MBR failure 的互证\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M3\"\n    summary: \"Consensus-proximity = LOO-SJ 等价性缺少推导\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§3.3 声称数学等价但未给出推导。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Appendix D 已包含完整等价性证明（constant factor 1/(N-1) argument + self-comparison constant），并报告 empirical Δρ=-0.014 和 max per-instance diff 3.1×10⁻⁴。Round 6 未再提出。\"\n    action_items:\n      - round: 5\n        action: \"附录补简要推导\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Appendix D 已包含完整等价性证明，Round 6 未再提出\"\n    resolution_round: 6\n\n  - id: \"R5-C1\"\n    summary: \"Constrained decoding 混淆变量未隔离，claim scope 与 evidence 不匹配\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Title/Abstract/Conclusion 需限定 constrained decoding scope。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"与 R3-C1 合并追踪。Title 已含 'under Constrained Decoding'，但 Introduction/Discussion 仍暗示 gap 是 IE 固有属性。\"\n    action_items:\n      - round: 5\n        action: \"Title 加 'under Constrained Decoding'; scope 限定\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 6\n        action: \"见 R3-C1 Round 6 action\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-C2\"\n    summary: \"Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"4/5 instance-level failure = tautological; logprob failure = artifact。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"与 R3-W2 合并追踪。共识：重构叙事以 logprob compression + MBR failure 为中心。\"\n    action_items:\n      - round: 5\n        action: \"Reframe C2 聚焦 logprob compression + MBR failure\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"见 R3-W2 Round 6 action\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W4\"\n    summary: \"'First multi-family comparison' claim = scope engineering\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"建议改为描述性表述\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"与 R3-W6 合并追踪。\"\n    action_items:\n      - round: 5\n        action: \"'first' → 'a systematic'\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"见 R3-W6 Round 6 action\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W5\"\n    summary: \"'Cross-architecture' 用词过度（两个 8B decoder-only）\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"改为 'across two model families at 8B scale'\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"与 R3-W5 合并追踪。\"\n    action_items:\n      - round: 5\n        action: \"全文替换 cross-architecture\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"见 R3-W5 Round 6 action\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W6\"\n    summary: \"FK independence justification 不够严格\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Excess agreement 未注明 configuration，未引用文献\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"与 R3-W4 合并追踪。\"\n    action_items:\n      - round: 5\n        action: \"补 configuration 信息 + 引用文献\"\n        assigned_to: \"Paper Agent\"\n        status: open\n      - round: 6\n        action: \"见 R3-W4 Round 6 action\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W7\"\n    summary: \"SJ 方法论新颖性有限，'core structural signal' 过度宣传\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"R2 认为标准技术组合。共识: application novelty 但不应过度宣传。\"\n    action_items:\n      - round: 5\n        action: \"'core structural signal' → 'primary structural signal'\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M4\"\n    summary: \"部分 bib entries 在 OpenAlex 未找到或 author name 有 variant\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"hobelsberger2025systematic, lightman2024verify 未找到; feng2025optimal, ye2025uncertainty author name 可能有 variant\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 补充：snell2024scaling key 标 2024 但 venue 为 ICLR 2025。ye2025uncertainty 第一作者可能为 Heo。两位 Reviewer 均同意需核实。\"\n    action_items:\n      - round: 6\n        action: \"(a) ye2025uncertainty 核实第一作者 Ye vs Heo；(b) snell2024scaling 统一 key/year 为 2025；(c) feng2025optimal 核实 author 顺序；(d) hobelsberger2025systematic, venktesh2025trust 确认 arXiv ID\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M5\"\n    summary: \"Ethics Statement 仅 2 句，内容偏简\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"格式合规但内容偏简\"\n      - round: 6\n        reviewers: [2]\n        note: \"R2 补充：应注明 CoNLL-2003 基于 Reuters 语料的 license 限制。R1 agree。\"\n    action_items:\n      - round: 6\n        action: \"Ethics Statement 补充 CoNLL-2003 Reuters license 注明\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-Q4\"\n    summary: \"WNUT-17 logprob 负相关 (ρ=-0.410) 机制未解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"capability boundary 下 logprob 反映 fluency 而非 accuracy。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"§4.2 已加机制假设（overconfidence on OOD inputs, Xiong et al. 引用），解释 logprob 在 capability boundary 处与 accuracy 反相关。Round 6 未再单独提出。\"\n    action_items:\n      - round: 5\n        action: \"§4 加机制解释\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"§4.2 已包含 overconfidence 假设，引用 Xiong et al.\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 new issues\n  # ============================================================\n  - id: \"R6-W1\"\n    summary: \"VC 公式（Eq.6）与实现不一致：无阈值 vs majority threshold\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Equation 6 定义为所有 entity 平均频率（无阈值），但 Footnote 2 承认实现使用 majority threshold (>N/2)。两者数学上不等价。Footnote 说 'slightly different absolute values but identical qualitative conclusions' 但未提供量化差异（如两种实现的 ρ 对比）。影响可复现性。\"\n    action_items:\n      - round: 6\n        action: \"(a) 统一公式和实现——改公式反映 threshold，或改实现匹配公式；(b) 报告两种实现的 ρ 差值；(c) 明确 Table 1 报告的是哪种实现\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W2\"\n    summary: \"Figure 1 caption 冗余——重复 Section 4.2/4.3 内容\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Figure 1 caption 引入 p=0.39、Table 2 引用、详细数字等——与正文重复。应更简洁。\"\n    action_items:\n      - round: 6\n        action: \"精简 Figure 1 caption，保留图表要传达的核心信息\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-15T09:03:12.055670+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 53653}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 204
}
```

</details>

---


### Tool call

_source line 659 · 2026-05-15T09:05:31.185488+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 合并审稿报告 — Round 6\n\n**论文**: Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding\n**目标 Venue**: EMNLP 2026 Findings\n**Reviewer 1 侧重**: 方法严谨性 + 实验设计 | **Reviewer 2 侧重**: 新颖性 + 完整性 + 相关工作\n**Reviewer 1 评分**: 3.0/5 | **Reviewer 2 评分**: 3.0/5\n\n---\n\n## Summary\n\n论文在 constrained decoding 下系统比较了 5 种 confidence signals（VC, SJ, FK, EM, logprob）用于 structured IE（NER + RE）的 quality estimation 和 sample selection。核心发现是 correlation-selection gap：信号是有效的 quality estimator（ρ=0.38, AUROC=0.75），但无法做 best-of-N selection（p>0.39）。机制诊断追溯到 constrained decoding 下的 logprob score compression。\n\n---\n\n## Strengths\n\n1. **统计分析严谨度远超同类论文**：Bootstrap CI、TOST 等价检验、Cohen's d、multi-seed stability analysis、diversity stratification、conditional filtering——两位 Reviewer 独立给出 4/5 Reproducibility，一致认为统计实践为 IE 领域少见的高标准。[AGREE R1+R2]\n\n2. **Logprob 压缩诊断是论文最有价值的贡献**：Non-tied subset analysis（+2.9pp, p=0.01, within-instance ρ: 0.08→0.39）不仅报告了 selection failure，还提供了 actionable 的机制解释——constrained decoding 压缩 logprob resolution 是主要瓶颈。两位 Reviewer 一致认为这是论文的核心洞察。[AGREE R1+R2]\n\n3. **Quality estimation vs. sample selection 的概念区分**：此前 IE 文献经常混淆这两个目标。论文清晰分离了 instance-level quality prediction 和 per-sample candidate ranking，为后续研究提供了有价值的框架。[AGREE R1+R2]\n\n4. **Difficulty gradient 设计合理**：三个 NER 数据集跨越 easy (CoNLL, 91% F1) → hard (SciERC) → boundary (WNUT-17, 52% zero F1)。WNUT-17 的 logprob 负相关（ρ=−0.410）和 conditional collapse（ρ=0.038, n.s.）是非显然发现。[AGREE R1+R2]\n\n5. **Limitations 的诚实程度值得肯定**：覆盖 RE 单数据集、模型规模限制、N-scaling 范围、thinking mode confound、logprob temperature gap。[AGREE R1+R2]\n\n---\n\n## Weaknesses（按严重度排序）\n\n### Must-Fix（影响接收决定）\n\n**[MF-1] Correlation-selection gap 的叙事结构需根本性重构** [共识 R1+R2]\n- **问题**：论文将 \"4/5 signals fail at selection\" 与 logprob failure 并列呈现为同一现象（gap）。但 4/5 信号的 selection failure 是 **定义的直接推论**（instance-level 信号给同一 input 的所有 N 个 sample 相同分数），不需要实验验证。Discussion Section 5 自己承认了 \"Layer 1 (definitional)\"，但 Abstract 和 Introduction 仍将其包装为实证发现。\n- **真正的实证贡献**是两个点：(a) consensus-proximity / MBR selection 也失败（Table 2: SJ selection 0.645 vs greedy 0.644）；(b) logprob（唯一 per-sample signal）因 score compression 失败。当前 framing 用 \"5 signals all fail\" 的统一叙事掩盖了这两个更有深度的发现。\n- **修改要求**：Abstract 和 Introduction 重构——先一句话 dismiss instance-level 信号的 selection potential（\"by definition, not empirically\"），然后聚焦 consensus-proximity/MBR failure 和 logprob compression 作为核心贡献。Contribution 2 应以 logprob compression + MBR failure 为重心。\n\n**[MF-2] Contribution 1 framing 过度——benchmark 应用研究被呈现为 primary contribution** [共识 R1+R2]\n- **问题**：将 \"systematic multi-family comparison of 5 signals\" 列为第一条 Contribution，给读者印象是论文的主要贡献。但本质是将已知 confidence signals（logprob, exact match, Fleiss' κ 等）应用于新任务设置——engineering benchmark 而非 new principle discovery。SJ 的 type-aware bipartite matching 有方法新意，但应被呈现为 methodology 而非独立 contribution。\n- **修改要求**：Contribution 1 降级为 setup/methodology；Contribution 2（gap + logprob 压缩诊断）提升为核心。去掉 \"first\" claim（通过堆叠修饰词确保 \"first\" 成立属于 scope engineering）。\n\n**[MF-3] TOST δ 选择的理据概念错配** [共识 R1+R2，R1 列 must-fix，R2 agree]\n- **问题**：δ 取值 ±2/3/5pp 的唯一理由是 IAA 变异（\"well-annotated NER benchmarks typically achieve inter-annotator F1 above 95%\"），但 IAA 测量标注噪声天花板，与 \"selector 预期增益\" 是不同概念。Oracle headroom = 13-18pp，δ=5pp 意味着放弃 ~38% 的可能增益仍算\"等价\"。\n- **修改要求**：(a) 用 SESOI 框架或 oracle headroom 比例来论证 δ；(b) 报告 breakpoint δ*（使结论翻转的最小 δ）；(c) 更突出 effect size (Cohen's d=0.038) 和 bootstrap CI [−3.0, +4.2]pp 作为主要证据，TOST 作为补充。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[SF-1] Constrained decoding scope 限定仍不充分** [共识方向一致，严重度分歧]\n- Title 已含 \"under Constrained Decoding\"，但 Introduction 和 Discussion 中部分措辞仍暗示 gap 是 structured IE 的固有属性。Non-tied subset +2.9pp (p=0.01) 表明 gap 主要源于 score compression 而非 IE 固有属性。\n- R1 要求 free-form 对照实验（listed critical）；R2 rebut：Layer 1 definitional gap 与 decoding 策略无关，free-form IE 实用性存疑。共识：不要求 free-form 实验，但 Introduction 和 Discussion 需各加 1 句明确声明 gap 发现 specific to constrained decoding regime。\n\n**[SF-2] Qwen3 thinking token 训练不一致** [共识 R1+R2]\n- SciERC 未禁用 enable_thinking，CoNLL/WNUT 禁用。Thinking tokens 训练时影响 learned representations 可能改变 logprob 分布，进而影响 score compression 诊断（\"60% instances tied\" 可能在 thinking-disabled 下不同）。当前仅在 Limitations 脚注中提及。\n- 修改要求：Experiments Setup §4.1 中显著声明此 confound。\n\n**[SF-3] RE 证据标注全文不一致** [共识 R1+R2]\n- Abstract 标注 \"(SciERC, preliminary)\" 但 Table 1/2、Figure 2-3、Discussion 大量使用 RE 结果无 preliminary 限定。238 个 non-zero F1 instances，per-relation 变异极大（Feature-Of ρ=0.004 vs Hyponym-Of ρ=0.646）。\n- 修改要求：Discussion/Conclusion 每次引用 RE 结论时标注 \"(preliminary, single benchmark)\"；考虑将 RE selection 移入 Appendix。\n\n**[SF-4] \"cross-model\" 措辞过度外推** [共识 R1+R2]\n- 仅测试 2 个同规模 (8B) 模型。全文改为 \"across two model families at 8B scale\"。\n\n**[SF-5] Abstract 信息密度过高** [共识 R1+R2]\n- 9 行含 5 signal/3 family/4 metric/3 dataset/2 model + 新术语。精简为问题-发现-意义三段式，移除大部分具体数字和信号名。\n\n**[SF-6] 术语不一致** [共识 R1+R2，Round 3 以来持续存在]\n- VC / Voting Conf. / entity voting confidence / $c_{\\text{vote}}$；LP / Log-prob / logprob / $c_{\\text{lp}}$。全文统一为 VC/SJ/FK/EM/LP 五个缩写。\n\n**[SF-7] VC 公式（Eq.6）与实现不一致** [共识 R1+R2，Round 6 新发现]\n- Equation 6 无阈值（所有 entity 平均频率），但 Footnote 2 承认实现使用 majority threshold (>N/2)。两者数学不等价。\"Slightly different\" 但无量化。\n- 修改要求：统一公式和实现；报告两种实现的 ρ 差值。\n\n**[SF-8] 遗漏 Eikema et al. (EMNLP 2025) Structure-Conditional MBR** [R2 提出，R1 降为 should-fix]\n- Discussion §5 讨论 MBR failure 但缺少结构化输出上 MBR 的最直接相关工作。应引用并讨论差异。\n\n**[SF-9] Nédellec et al. (2026) 增量贡献应更诚实量化** [共识 R1+R2]\n- 三个增量均偏弱：SJ vs EM Bonferroni 不显著，selection analysis 部分 tautological，difficulty gradient 直觉上不意外。应降低 claim 强度，强调 WNUT-17 conditional collapse + logprob ρ=−0.410 作为 non-obvious findings。\n\n### Minor（不影响接收）\n\n- Figure 1 caption 冗余，重复 Section 4.2/4.3 内容\n- Table 1 N=16 行空白过多，建议移入 Appendix\n- FK excess agreement (-0.4% to -4.0%) 未做显著性检验\n- N=8 primary results 使用单一 seed=42，与 σ≤0.025 在同量级\n- Semantic entropy 脚注去掉具体数字\n- he2024uncertainty 引用上下文与实际论文不匹配\n- Ethics Statement 应注明 CoNLL-2003 Reuters license\n- Notation Table 缺 LP 缩写\n- 5 处 bib 条目需核实/修正（ye2025uncertainty author, snell2024scaling year, feng2025optimal author order, hobelsberger/venktesh 确认 arXiv ID）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **论文适合 Findings track**（3/5），但 framing 需要根本性修正——当前叙事夸大了贡献新颖性\n2. **Logprob 压缩诊断是真正的核心贡献**，应取代 \"multi-family comparison\" 成为论文重心\n3. **4/5 selection failure 是 definitional**，应与 empirical findings（MBR failure + logprob compression）明确分离\n4. **统计实践是显著优势**，远超同类工作\n5. **RE 证据薄弱**（单数据集、per-relation 高变异），需全文一致标注 preliminary\n6. **Qwen3 thinking token 训练不一致**是未控制 confound\n7. **\"cross-model\" 措辞过度外推**，实际仅 2 个 8B 模型\n8. **术语不一致**持续 4 轮未解决\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **Free-form decoding 对照实验**：R1 列 must-fix（gap 可能是 constrained decoding artifact），R2 rebut 降为 should-fix（Layer 1 definitional gap 与 decoding 策略无关；free-form IE 实用性存疑）。**Director 判断**：降为 should-fix——论文 Title 已限定 constrained decoding，且 free-form 对照引入新 confounds（不可解析样本处理），但 Introduction/Discussion 的 scope 声明需收紧。\n\n2. **Missing references 严重度**：R2 列 critical（Zhang et al. TTS survey + Eikema et al. Structure-Conditional MBR），R1 rebut（survey 非 critical，Eikema 降为 should-fix）。**Director 判断**：Eikema et al. 为 should-fix（与 MBR failure 直接相关），Zhang et al. 为 minor（camera-ready 补充）。\n\n3. **Supervised verifier baseline**：R2 列 should-fix，R1 rebut（超出论文 scope，已在 Future Work 讨论）。**Director 判断**：不列为 should-fix——论文 scope 是 unsupervised signals，要求 supervised baseline 改变论文定位。\n\n---\n\n## Questions（需作者澄清）\n\n1. VC 实现使用的是 Equation 6（无阈值）还是 Footnote 2 描述的 majority threshold？Table 1 报告的是哪种？\n2. Qwen3 SciERC 训练时 thinking tokens 是否实际被激活？是否可以确认 SciERC checkpoint 训练日志中有/无 thinking token outputs？\n3. TOST breakpoint δ*（使等价结论翻转的最小 δ）是多少？\n\n---\n\n## Missing References\n\n1. **Eikema, Rutkiewicz & Giulianelli (EMNLP 2025)** \"Structure-Conditional Minimum Bayes Risk Decoding\"——直接研究 MBR 在结构化输出上的 utility function 失效问题，与 Discussion §5 MBR failure 高度互证 [should-fix]\n2. **Zhang et al. (2025)** \"A Survey on Test-Time Scaling in Large Language Models\"——最全面的 TTS survey [minor, camera-ready]\n\n---\n\n## Overall Assessment\n\n**评分：borderline（3/5）**\n**建议：Conditional Accept for Findings（需完成 Must-Fix 修改）**\n**置信度：4/5**\n\n论文是一项方法论扎实、统计实践严谨的实证研究，对 structured IE 的 test-time scaling 提供了有价值的实证警告。Logprob 压缩诊断和 difficulty-dependent signal ranking 是实用的贡献。\n\n但当前 framing 存在系统性问题：(a) 将定义性事实（instance-level 信号不能做 per-sample selection）包装为实证发现；(b) 将 engineering benchmark（5 信号对比）包装为 primary contribution；(c) 核心发现的 scope 未充分限定为 constrained decoding 设置。这些 framing 问题不影响实验结论的正确性，但显著降低了论文的可信度和 perceived novelty。\n\n如果作者完成 3 项 Must-Fix 修改（叙事重构、Contribution 重排、TOST δ 理据），论文的 presentation 质量将大幅提升，适合 EMNLP 2026 Findings 接收。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高（9 行含全部技术细节），需精简为问题-发现-意义三段式\n- \"four of five signals are instance-level by construction\" 应一笔带过而非作为 finding 呈现\n\n### Section 1 (Introduction)\n- Contribution 1 需降级为 methodology；Contribution 2 提升为核心\n- \"first multi-family comparison\" → 描述性表述\n- MBR 在 MT 成功但 IE 失败的对比已有（line 26-27），但应更 prominently 作为 gap non-obviousness 的论证\n\n### Section 3 (Method)\n- Equation 6 (VC) 与 Footnote 2 实现不一致——统一\n- FK \"sufficient response diversity\" → \"mild negative dependence\"，注明 excess agreement 的 configurations\n- SJ 的 \"primary structural signal\" 措辞适当（非 \"core\"）\n\n### Section 4 (Experiments)\n- §4.1 需 prominently 声明 Qwen3 thinking token confound\n- Table 1 删除 N=16 行移入 Appendix\n- TOST 分析需 SESOI 论证 + breakpoint δ* 报告\n\n### Section 5 (Discussion)\n- \"Layer 1 (definitional)\" 已有但 Introduction/Abstract 未同步——需全文一致\n- 补充 Eikema et al. (EMNLP 2025) MBR 互证\n- 收紧 gap 的 scope 声明（specific to constrained decoding）\n\n### Section 6 (Conclusion)\n- \"across model families\" → \"across two model families at 8B scale\"\n- RE 限定句 \"RE findings rest on SciERC alone\" 已有但 Discussion 中引用 RE 时缺同等标注\n\n### Section 7 (Limitations)\n- WNUT-17 logprob 负相关机制假设已加入 §4.2，Limitations 可交叉引用\n- Thinking token confound 需从脚注级别提升\n\n### References\n- 5 处 bib 条目需核实修正\n- 补充 Eikema et al. (EMNLP 2025)\n\n### 术语统一（全文）\n- VC / SJ / FK / EM / LP 五个缩写，表格和正文一致",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 合并审稿报告 — Round 6\n\n**论文**: Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding\n**目标 Venue**: EMNLP 2026 Findings\n**Reviewer 1 侧重**: 方法严谨性 + 实验设计 | **Reviewer 2 侧重**: 新颖性 + 完整性 + 相关工作\n**Reviewer 1 评分**: 3.0/5 | **Reviewer 2 评分**: 3.0/5\n\n---\n\n## Summary\n\n论文在 constrained decoding 下系统比较了 5 种 confidence signals（VC, SJ, FK, EM, logprob）用于 structured IE（NER + RE）的 quality estimation 和 sample selection。核心发现是 correlation-selection gap：信号是有效的 quality estimator（ρ=0.38, AUROC=0.75），但无法做 best-of-N selection（p>0.39）。机制诊断追溯到 constrained decoding 下的 logprob score compression。\n\n---\n\n## Strengths\n\n1. **统计分析严谨度远超同类论文**：Bootstrap CI、TOST 等价检验、Cohen's d、multi-seed stability analysis、diversity stratification、conditional filtering——两位 Reviewer 独立给出 4/5 Reproducibility，一致认为统计实践为 IE 领域少见的高标准。[AGREE R1+R2]\n\n2. **Logprob 压缩诊断是论文最有价值的贡献**：Non-tied subset analysis（+2.9pp, p=0.01, within-instance ρ: 0.08→0.39）不仅报告了 selection failure，还提供了 actionable 的机制解释——constrained decoding 压缩 logprob resolution 是主要瓶颈。两位 Reviewer 一致认为这是论文的核心洞察。[AGREE R1+R2]\n\n3. **Quality estimation vs. sample selection 的概念区分**：此前 IE 文献经常混淆这两个目标。论文清晰分离了 instance-level quality prediction 和 per-sample candidate ranking，为后续研究提供了有价值的框架。[AGREE R1+R2]\n\n4. **Difficulty gradient 设计合理**：三个 NER 数据集跨越 easy (CoNLL, 91% F1) → hard (SciERC) → boundary (WNUT-17, 52% zero F1)。WNUT-17 的 logprob 负相关（ρ=−0.410）和 conditional collapse（ρ=0.038, n.s.）是非显然发现。[AGREE R1+R2]\n\n5. **Limitations 的诚实程度值得肯定**：覆盖 RE 单数据集、模型规模限制、N-scaling 范围、thinking mode confound、logprob temperature gap。[AGREE R1+R2]\n\n---\n\n## Weaknesses（按严重度排序）\n\n### Must-Fix（影响接收决定）\n\n**[MF-1] Correlation-selection gap 的叙事结构需根本性重构** [共识 R1+R2]\n- **问题**：论文将 \"4/5 signals fail at selection\" 与 logprob failure 并列呈现为同一现象（gap）。但 4/5 信号的 selection failure 是 **定义的直接推论**（instance-level 信号给同一 input 的所有 N 个 sample 相同分数），不需要实验验证。Discussion Section 5 自己承认了 \"Layer 1 (definitional)\"，但 Abstract 和 Introduction 仍将其包装为实证发现。\n- **真正的实证贡献**是两个点：(a) consensus-proximity / MBR selection 也失败（Table 2: SJ selection 0.645 vs greedy 0.644）；(b) logprob（唯一 per-sample signal）因 score compression 失败。当前 framing 用 \"5 signals all fail\" 的统一叙事掩盖了这两个更有深度的发现。\n- **修改要求**：Abstract 和 Introduction 重构——先一句话 dismiss instance-level 信号的 selection potential（\"by definition, not empirically\"），然后聚焦 consensus-proximity/MBR failure 和 logprob compression 作为核心贡献。Contribution 2 应以 logprob compression + MBR failure 为重心。\n\n**[MF-2] Contribution 1 framing 过度——benchmark 应用研究被呈现为 primary contribution** [共识 R1+R2]\n- **问题**：将 \"systematic multi-family comparison of 5 signals\" 列为第一条 Contribution，给读者印象是论文的主要贡献。但本质是将已知 confidence signals（logprob, exact match, Fleiss' κ 等）应用于新任务设置——engineering benchmark 而非 new principle discovery。SJ 的 type-aware bipartite matching 有方法新意，但应被呈现为 methodology 而非独立 contribution。\n- **修改要求**：Contribution 1 降级为 setup/methodology；Contribution 2（gap + logprob 压缩诊断）提升为核心。去掉 \"first\" claim（通过堆叠修饰词确保 \"first\" 成立属于 scope engineering）。\n\n**[MF-3] TOST δ 选择的理据概念错配** [共识 R1+R2，R1 列 must-fix，R2 agree]\n- **问题**：δ 取值 ±2/3/5pp 的唯一理由是 IAA 变异（\"well-annotated NER benchmarks typically achieve inter-annotator F1 above 95%\"），但 IAA 测量标注噪声天花板，与 \"selector 预期增益\" 是不同概念。Oracle headroom = 13-18pp，δ=5pp 意味着放弃 ~38% 的可能增益仍算\"等价\"。\n- **修改要求**：(a) 用 SESOI 框架或 oracle headroom 比例来论证 δ；(b) 报告 breakpoint δ*（使结论翻转的最小 δ）；(c) 更突出 effect size (Cohen's d=0.038) 和 bootstrap CI [−3.0, +4.2]pp 作为主要证据，TOST 作为补充。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[SF-1] Constrained decoding scope 限定仍不充分** [共识方向一致，严重度分歧]\n- Title 已含 \"under Constrained Decoding\"，但 Introduction 和 Discussion 中部分措辞仍暗示 gap 是 structured IE 的固有属性。Non-tied subset +2.9pp (p=0.01) 表明 gap 主要源于 score compression 而非 IE 固有属性。\n- R1 要求 free-form 对照实验（listed critical）；R2 rebut：Layer 1 definitional gap 与 decoding 策略无关，free-form IE 实用性存疑。共识：不要求 free-form 实验，但 Introduction 和 Discussion 需各加 1 句明确声明 gap 发现 specific to constrained decoding regime。\n\n**[SF-2] Qwen3 thinking token 训练不一致** [共识 R1+R2]\n- SciERC 未禁用 enable_thinking，CoNLL/WNUT 禁用。Thinking tokens 训练时影响 learned representations 可能改变 logprob 分布，进而影响 score compression 诊断（\"60% instances tied\" 可能在 thinking-disabled 下不同）。当前仅在 Limitations 脚注中提及。\n- 修改要求：Experiments Setup §4.1 中显著声明此 confound。\n\n**[SF-3] RE 证据标注全文不一致** [共识 R1+R2]\n- Abstract 标注 \"(SciERC, preliminary)\" 但 Table 1/2、Figure 2-3、Discussion 大量使用 RE 结果无 preliminary 限定。238 个 non-zero F1 instances，per-relation 变异极大（Feature-Of ρ=0.004 vs Hyponym-Of ρ=0.646）。\n- 修改要求：Discussion/Conclusion 每次引用 RE 结论时标注 \"(preliminary, single benchmark)\"；考虑将 RE selection 移入 Appendix。\n\n**[SF-4] \"cross-model\" 措辞过度外推** [共识 R1+R2]\n- 仅测试 2 个同规模 (8B) 模型。全文改为 \"across two model families at 8B scale\"。\n\n**[SF-5] Abstract 信息密度过高** [共识 R1+R2]\n- 9 行含 5 signal/3 family/4 metric/3 dataset/2 model + 新术语。精简为问题-发现-意义三段式，移除大部分具体数字和信号名。\n\n**[SF-6] 术语不一致** [共识 R1+R2，Round 3 以来持续存在]\n- VC / Voting Conf. / entity voting confidence / $c_{\\text{vote}}$；LP / Log-prob / logprob / $c_{\\text{lp}}$。全文统一为 VC/SJ/FK/EM/LP 五个缩写。\n\n**[SF-7] VC 公式（Eq.6）与实现不一致** [共识 R1+R2，Round 6 新发现]\n- Equation 6 无阈值（所有 entity 平均频率），但 Footnote 2 承认实现使用 majority threshold (>N/2)。两者数学不等价。\"Slightly different\" 但无量化。\n- 修改要求：统一公式和实现；报告两种实现的 ρ 差值。\n\n**[SF-8] 遗漏 Eikema et al. (EMNLP 2025) Structure-Conditional MBR** [R2 提出，R1 降为 should-fix]\n- Discussion §5 讨论 MBR failure 但缺少结构化输出上 MBR 的最直接相关工作。应引用并讨论差异。\n\n**[SF-9] Nédellec et al. (2026) 增量贡献应更诚实量化** [共识 R1+R2]\n- 三个增量均偏弱：SJ vs EM Bonferroni 不显著，selection analysis 部分 tautological，difficulty gradient 直觉上不意外。应降低 claim 强度，强调 WNUT-17 conditional collapse + logprob ρ=−0.410 作为 non-obvious findings。\n\n### Minor（不影响接收）\n\n- Figure 1 caption 冗余，重复 Section 4.2/4.3 内容\n- Table 1 N=16 行空白过多，建议移入 Appendix\n- FK excess agreement (-0.4% to -4.0%) 未做显著性检验\n- N=8 primary results 使用单一 seed=42，与 σ≤0.025 在同量级\n- Semantic entropy 脚注去掉具体数字\n- he2024uncertainty 引用上下文与实际论文不匹配\n- Ethics Statement 应注明 CoNLL-2003 Reuters license\n- Notation Table 缺 LP 缩写\n- 5 处 bib 条目需核实/修正（ye2025uncertainty author, snell2024scaling year, feng2025optimal author order, hobelsberger/venktesh 确认 arXiv ID）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **论文适合 Findings track**（3/5），但 framing 需要根本性修正——当前叙事夸大了贡献新颖性\n2. **Logprob 压缩诊断是真正的核心贡献**，应取代 \"multi-family comparison\" 成为论文重心\n3. **4/5 selection failure 是 definitional**，应与 empirical findings（MBR failure + logprob compression）明确分离\n4. **统计实践是显著优势**，远超同类工作\n5. **RE 证据薄弱**（单数据集、per-relation 高变异），需全文一致标注 preliminary\n6. **Qwen3 thinking token 训练不一致**是未控制 confound\n7. **\"cross-model\" 措辞过度外推**，实际仅 2 个 8B 模型\n8. **术语不一致**持续 4 轮未解决\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **Free-form decoding 对照实验**：R1 列 must-fix（gap 可能是 constrained decoding artifact），R2 rebut 降为 should-fix（Layer 1 definitional gap 与 decoding 策略无关；free-form IE 实用性存疑）。**Director 判断**：降为 should-fix——论文 Title 已限定 constrained decoding，且 free-form 对照引入新 confounds（不可解析样本处理），但 Introduction/Discussion 的 scope 声明需收紧。\n\n2. **Missing references 严重度**：R2 列 critical（Zhang et al. TTS survey + Eikema et al. Structure-Conditional MBR），R1 rebut（survey 非 critical，Eikema 降为 should-fix）。**Director 判断**：Eikema et al. 为 should-fix（与 MBR failure 直接相关），Zhang et al. 为 minor（camera-ready 补充）。\n\n3. **Supervised verifier baseline**：R2 列 should-fix，R1 rebut（超出论文 scope，已在 Future Work 讨论）。**Director 判断**：不列为 should-fix——论文 scope 是 unsupervised signals，要求 supervised baseline 改变论文定位。\n\n---\n\n## Questions（需作者澄清）\n\n1. VC 实现使用的是 Equation 6（无阈值）还是 Footnote 2 描述的 majority threshold？Table 1 报告的是哪种？\n2. Qwen3 SciERC 训练时 thinking tokens 是否实际被激活？是否可以确认 SciERC checkpoint 训练日志中有/无 thinking token outputs？\n3. TOST breakpoint δ*（使等价结论翻转的最小 δ）是多少？\n\n---\n\n## Missing References\n\n1. **Eikema, Rutkiewicz & Giulianelli (EMNLP 2025)** \"Structure-Conditional Minimum Bayes Risk Decoding\"——直接研究 MBR 在结构化输出上的 utility function 失效问题，与 Discussion §5 MBR failure 高度互证 [should-fix]\n2. **Zhang et al. (2025)** \"A Survey on Test-Time Scaling in Large Language Models\"——最全面的 TTS survey [minor, camera-ready]\n\n---\n\n## Overall Assessment\n\n**评分：borderline（3/5）**\n**建议：Conditional Accept for Findings（需完成 Must-Fix 修改）**\n**置信度：4/5**\n\n论文是一项方法论扎实、统计实践严谨的实证研究，对 structured IE 的 test-time scaling 提供了有价值的实证警告。Logprob 压缩诊断和 difficulty-dependent signal ranking 是实用的贡献。\n\n但当前 framing 存在系统性问题：(a) 将定义性事实（instance-level 信号不能做 per-sample selection）包装为实证发现；(b) 将 engineering benchmark（5 信号对比）包装为 primary contribution；(c) 核心发现的 scope 未充分限定为 constrained decoding 设置。这些 framing 问题不影响实验结论的正确性，但显著降低了论文的可信度和 perceived novelty。\n\n如果作者完成 3 项 Must-Fix 修改（叙事重构、Contribution 重排、TOST δ 理据），论文的 presentation 质量将大幅提升，适合 EMNLP 2026 Findings 接收。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高（9 行含全部技术细节），需精简为问题-发现-意义三段式\n- \"four of five signals are instance-level by construction\" 应一笔带过而非作为 finding 呈现\n\n### Section 1 (Introduction)\n- Contribution 1 需降级为 methodology；Contribution 2 提升为核心\n- \"first multi-family comparison\" → 描述性表述\n- MBR 在 MT 成功但 IE 失败的对比已有（line 26-27），但应更 prominently 作为 gap non-obviousness 的论证\n\n### Section 3 (Method)\n- Equation 6 (VC) 与 Footnote 2 实现不一致——统一\n- FK \"sufficient response diversity\" → \"mild negative dependence\"，注明 excess agreement 的 configurations\n- SJ 的 \"primary structural signal\" 措辞适当（非 \"core\"）\n\n### Section 4 (Experiments)\n- §4.1 需 prominently 声明 Qwen3 thinking token confound\n- Table 1 删除 N=16 行移入 Appendix\n- TOST 分析需 SESOI 论证 + breakpoint δ* 报告\n\n### Section 5 (Discussion)\n- \"Layer 1 (definitional)\" 已有但 Introduction/Abstract 未同步——需全文一致\n- 补充 Eikema et al. (EMNLP 2025) MBR 互证\n- 收紧 gap 的 scope 声明（specific to constrained decoding）\n\n### Section 6 (Conclusion)\n- \"across model families\" → \"across two model families at 8B scale\"\n- RE 限定句 \"RE findings rest on SciERC alone\" 已有但 Discussion 中引用 RE 时缺同等标注\n\n### Section 7 (Limitations)\n- WNUT-17 logprob 负相关机制假设已加入 §4.2，Limitations 可交叉引用\n- Thinking token confound 需从脚注级别提升\n\n### References\n- 5 处 bib 条目需核实修正\n- 补充 Eikema et al. (EMNLP 2025)\n\n### 术语统一（全文）\n- VC / SJ / FK / EM / LP 五个缩写，表格和正文一致",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline"
  }
}
```

</details>

---


### Tool result

_source line 660 · 2026-05-15T09:05:35.914960+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4729
}
```

</details>

---


### Assistant

_source line 661 · 2026-05-15T09:05:47.395224+00:00_

审稿完成。

**Round 6 审稿报告已投递给 Research Director。**

| 项目 | 结果 |
|------|------|
| 评分 | **borderline (3/5)** — Conditional Accept for Findings |
| Reviewer 1 | 3.0/5 |
| Reviewer 2 | 3.0/5 |
| 轮次 | 1 轮（交叉分享后达成共识，无需追加轮次） |

**3 项 Must-Fix：**
1. **叙事重构**：4/5 selection failure 是定义性事实而非实证发现，需与 logprob compression/MBR failure 明确分离
2. **Contribution 重排**：C1（multi-family comparison）降级为 methodology，C2（gap + logprob 诊断）提升为核心
3. **TOST δ 理据**：IAA 变异 ≠ selector 预期增益，需 SESOI 框架 + breakpoint 分析

**9 项 Should-Fix** 涵盖 scope 限定、thinking token confound、RE 标注、cross-model 措辞、Abstract 密度、术语一致性、VC 公式-实现不一致、遗漏引用、Nédellec 增量量化。

**Issue Tracker** 已同步更新至 Round 6（`review_issues.yaml`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 56

## Round 56

58 recorded events


### User

_source line 662 · 2026-05-15T12:11:39.432342+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 663 · 2026-05-15T12:11:46.662028+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 664 · 2026-05-15T12:11:46.713399+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 665 · 2026-05-15T12:11:51.534396+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 666 · 2026-05-15T12:11:51.534878+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 667 · 2026-05-15T12:11:57.832784+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 668 · 2026-05-15T12:11:58.385941+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (83 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_019_supervised_verifier（等待人工审批）\n- exp_002_merge_conll2003（准备中）\n- exp_007_ner_llama（准备中）\n- exp008_re_n16（准备中）\n- exp_001_n16_seed123_full（准备中）\n- exp_001_n16_seed456_full（准备中）\n- exp001_seed123（准备中）\n- exp001_seed456（准备中）\n\n## 近期结论\n- **exp_011_ood_conll_to_scierc** (success): —\n- **exp_011_ood_scierc_to_conll** (success): —\n- **exp_017_llama_conll_n16_s456_r1024** (success): —\n\n## 趋势\n成功 47 / 负向 19 / 失败 1 / 共 75\nauroc_em_ner: 0.6294 ↓（近 3 次 success）\nauroc_fk_ner: 0.9059 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_018_llama_scierc_seed456: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 669 · 2026-05-15T12:11:58.838152+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 670 · 2026-05-15T12:12:00.294853+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 671 · 2026-05-15T12:12:00.798701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 672 · 2026-05-15T12:12:01.000042+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Do Not Scale Structured Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 673 · 2026-05-15T12:12:01.000536+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 674 · 2026-05-15T12:12:01.000782+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 675 · 2026-05-15T12:12:08.136280+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 676 · 2026-05-15T12:12:08.186921+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 677 · 2026-05-15T12:12:10.244430+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 678 · 2026-05-15T12:12:10.596347+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 679 · 2026-05-15T12:12:10.596762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 680 · 2026-05-15T12:12:11.149915+00:00_

1	issues:
2	- id: R0-C1
3	  summary: 模型规模单一（仅 8B）
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 1
9	  mentions:
10	  - round: 0
11	    reviewers:
12	    - 1
13	    - 2
14	    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性
15	  - round: 1
16	    reviewers:
17	    - 1
18	    - 2
19	    note: model-agnostic 与 Limitations 矛盾
20	  action_items:
21	  - round: 1
22	    action: 全文替换 model-agnostic → consistent across tested model families
23	    assigned_to: Paper Agent
24	    status: resolved
25	  resolution: Round 2 Reviewer 确认措辞修正到位，无再提
26	  resolution_round: 2
27	- id: R0-C2
28	  summary: 相关工作显著遗漏
29	  category: framing
30	  severity: warning
31	  status: resolved
32	  first_raised_round: 0
33	  last_seen_round: 1
34	  mentions:
35	  - round: 0
36	    reviewers:
37	    - 1
38	    - 2
39	    note: 5 篇核心文献缺失
40	  - round: 1
41	    reviewers:
42	    - 1
43	    - 2
44	    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC
45	  action_items:
46	  - round: 1
47	    action: 补充 6 篇引用到 Related Work
48	    assigned_to: Paper Agent
49	    status: resolved
50	  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'
51	  resolution_round: 2
52	- id: R0-C3
53	  summary: RE 结论仅基于 SciERC 单数据集
54	  category: experiment
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 0
58	  last_seen_round: 4
59	  mentions:
60	  - round: 0
61	    reviewers:
62	    - 1
63	    - 2
64	    note: 需跨数据集验证或降级措辞
65	  - round: 2
66	    reviewers:
67	    - 1
68	    - 2
69	    note: Abstract RE 措辞需修正
70	  - round: 3
71	    reviewers:
72	    - 1
73	    - 2
74	    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围
75	  - round: 4
76	    reviewers:
77	    - 1
78	    - 2
79	    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪
80	  action_items:
81	  - round: 1
82	    action: 降级措辞 universal → observed in SciERC
83	    assigned_to: Paper Agent
84	    status: resolved
85	  - ro
…[truncated 54894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 681 · 2026-05-15T12:12:11.301019+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 682 · 2026-05-15T12:12:11.351766+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## Registry 清理备注 (2026-05-15)\\n- 9 个 PREPARING+killed 实验因状态机限制无法推进到 DONE，实质已废弃\\n- 包括：exp_017_llama_conll_n16_s456_r1024, exp_017_llama_conll_n16_r1024, exp_001_n16_seed123_full, exp_001_n16_seed456_full, exp001_seed123, exp001_seed456, exp_007_ner_llama, exp_002_merge_conll2003, exp008_re_n16\\n\", \"total_chars\": 1740,
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 683 · 2026-05-15T12:12:22.419793+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-15T12:12:24.377190+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-15T12:12:24.678775+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-15T12:12:24.980296+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-15T12:12:35.085059+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's a summary of the EMNLP 2026 call for papers submission guidelines and author instructions:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, a
…[truncated 1829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 12665
}
```

</details>

---


### Tool result

_source line 688 · 2026-05-15T12:12:35.136059+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 76\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发现
…[truncated 1439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10155
}
```

</details>

---


### Tool call

_source line 689 · 2026-05-15T12:12:46.500116+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR May 2026 page limit format requirements long paper short paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR May 2026 page limit format requirements long paper short paper"
  }
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-15T12:12:46.651056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-15T12:12:46.651465+00:00_

1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.
3	We compare five confidence signals across NER and relation extraction on three benchmarks with two 8B-parameter model families and uncover a \textit{correlation-selection gap}: signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom.
4	Most signals are instance-level by construction and cannot rank candidates; the empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection (MBR decoding) can bridge the gap.
5	Neither succeeds: log-probability scores are compressed into effective ties, while MBR utility correlates with quality across instances but not within them.
6	A controlled ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.
7	Signal rankings depend on task complexity, with findings consistent across two model families at 8B scale.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-15T12:12:47.203601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-15T12:12:47.254355+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2025scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-15T12:12:47.606324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-15T12:12:47.657212+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in T
…[truncated 11585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 696 · 2026-05-15T12:12:54.695384+00:00_

Web search results for query: "EMNLP 2026 ARR May 2026 page limit format requirements long paper short paper"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"}]

Based on the search results, here are the EMNLP 2026 page limit and format requirements for the ARR May 2026 cycle:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Format Requirements

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL co
…[truncated 700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 8195
}
```

</details>

---


### Tool call

_source line 697 · 2026-05-15T12:13:08.116679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 698 · 2026-05-15T12:13:08.117482+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface
…[truncated 4871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 699 · 2026-05-15T12:13:09.073339+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 700 · 2026-05-15T12:13:09.073883+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2025scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selec
…[truncated 2915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 701 · 2026-05-15T12:13:09.425486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 702 · 2026-05-15T12:13:09.476261+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.
6	At higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) with lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).
7	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
8	
9	\paragraph{Why the gap exists: two layers.}
10	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
11	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
12	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
13	LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
14	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
15	This diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.
16	A cont
…[truncated 4640 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 703 · 2026-05-15T12:13:10.680616+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 704 · 2026-05-15T12:13:10.934325+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) for LLM-based structured IE, but fail at sample selection---the \textit{correlation-selection gap}.
4	By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to score compression.
5	Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.
6	A controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding.
7	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
8	RE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.
9	Trained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 705 · 2026-05-15T12:13:15.514587+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 706 · 2026-05-15T12:13:15.916428+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 707 · 2026-05-15T12:13:15.916923+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 708 · 2026-05-15T12:13:16.420460+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.010$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as population standard deviation.}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.4
…[truncated 34442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 709 · 2026-05-15T12:13:16.420827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 710 · 2026-05-15T12:13:16.471461+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 2459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 711 · 2026-05-15T12:13:45.617641+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml",
    "max_chars": "500"
  }
}
```

</details>

---


### Tool result

_source line 712 · 2026-05-15T12:13:46.070221+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 76\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric\\n\\n... [截断: 省略 59865 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 60365, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 713 · 2026-05-15T12:13:47.175305+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 714 · 2026-05-15T12:13:47.377749+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md:163:外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md:156:外部审稿：未配置（项目未启用 `external_review.paperreview_ai.enabled`）。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T102033_395761.jsonl:2106:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T102033_395761.jsonl:2207:[Omitted long 
…[truncated 17480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 715 · 2026-05-15T12:14:46.503680+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。\n\n## 论文信息\n- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子目录各章节）\n- **目标 Venue**: EMNLP 2026 Main Conference\n- **Track**: Main Conference (Long Paper)\n- **Deadline**: 2026-05-25 (ARR May 2026 cycle)\n\n## Venue 格式要求\n- ACL 模板，8 页正文 + 引用不限 + 附录\n- Double-blind（匿名审稿）\n- Limitations section 必需\n- 提交时必须选择 EMNLP（绑定选择）\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- 五个 confidence signal 的定义是否数学严谨、无歧义\n- Soft Jaccard（Eq.4-5）的 Hungarian matching 描述是否完整（目标函数、zero-IoU 处理、threshold）\n- VC（Eq.6）的公式定义与脚注中描述的实际实现（majority threshold）是否一致\n- FK 的独立性假设：excess agreement 数据是否充分支撑（configuration 覆盖、显著性检验）\n- Consensus-proximity = LOO-SJ 等价性推导是否充分\n\n### 2. 统计检验\n- Bootstrap resampling 的参数设置（B=10,000, n=529）是否充分\n- TOST 等价检验的 δ 选择（±2/3/5 pp）的合理性论证——δ 是否有实践锚定\n- 多重比较校正（Bonferroni）的处理是否到位\n- Effect size (Cohen's d=0.038) 和 CI 的报告是否完整\n- \"60% instances effectively tied\" 的 ε=0.05 阈值选择是否有依据\n\n### 3. 实验设计\n- 训练配置（LoRA rank=32, α=64, 5 epochs）是否完整可复现\n- Qwen3-8B SciERC thinking token 训练不一致是否充分讨论\n- N=8 single seed (seed=42) 作为核心结果的局限性\n- Free-form ablation 仅 1 个 dataset × 1 个 model 的充分性\n- RE 证据仅基于 SciERC 单数据集的措辞限定是否一致\n\n### 4. 可复现性\n- 附录是否包含完整训练配置、prompt template\n- 数据集 split 信息\n- Constrained decoding 的具体工具和参数\n\n请严格按照 EMNLP 审稿标准评审，不留情面。输出格式：Summary → Strengths → Weaknesses (Critical/Warning/Minor 分级) → Questions → Missing References → Scores (Soundness/Presentation/Contribution/Overall 1-5) → Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。\n\n## 论文信息\n- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子目录各章节）\n- **目标 Venue**: EMNLP 2026 Main Conference\n- **Track**: Main Conference (Long Paper)\n- **Deadline**: 2026-05-25 (ARR May 2026 cycle)\n\n## Venue 格式要求\n- ACL 模板，8 页正文 + 引用不限 + 附录\n- Double-blind（匿名审稿）\n- Limitations section 必需\n- 提交时必须选择 EMNLP（绑定选择）\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- 五个 confidence signal 的定义是否数学严谨、无歧义\n- Soft Jaccard（Eq.4-5）的 Hungarian matching 描述是否完整（目标函数、zero-IoU 处理、threshold）\n- VC（Eq.6）的公式定义与脚注中描述的实际实现（majority threshold）是否一致\n- FK 的独立性假设：excess agreement 数据是否充分支撑（configuration 覆盖、显著性检验）\n- Consensus-proximity = LOO-SJ 等价性推导是否充分\n\n### 2. 统计检验\n- Bootstrap resampling 的参数设置（B=10,000, n=529）是否充分\n- TOST 等价检验的 δ 选择（±2/3/5 pp）的合理性论证——δ 是否有实践锚定\n- 多重比较校正（Bonferroni）的处理是否到位\n- Effect size (Cohen's d=0.038) 和 CI 的报告是否完整\n- \"60% instances effectively tied\" 的 ε=0.05 阈值选择是否有依据\n\n### 3. 实验设计\n- 训练配置（LoRA rank=32, α=64, 5 epochs）是否完整可复现\n- Qwen3-8B SciERC thinking token 训练不一致是否充分讨论\n- N=8 single seed (seed=42) 作为核心结果的局限性\n- Free-form ablation 仅 1 个 dataset × 1 个 model 的充分性\n- RE 证据仅基于 SciERC 单数据集的措辞限定是否一致\n\n### 4. 可复现性\n- 附录是否包含完整训练配置、prompt template\n- 数据集 split 信息\n- Constrained decoding 的具体工具和参数\n\n请严格按照 EMNLP 审稿标准评审，不留情面。输出格式：Summary → Strengths → Weaknesses (Critical/Warning/Minor 分级) → Questions → Missing References → Scores (Soundness/Presentation/Contribution/Overall 1-5) → Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 716 · 2026-05-15T12:15:06.162371+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19658
}
```

</details>

---


### Tool call

_source line 717 · 2026-05-15T12:15:07.119313+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 的审查。\n\n## 论文信息\n- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子目录各章节）\n- **目标 Venue**: EMNLP 2026 Main Conference\n- **Track**: Main Conference (Long Paper)\n- **Deadline**: 2026-05-25 (ARR May 2026 cycle)\n\n## Venue 格式要求\n- ACL 模板，8 页正文 + 引用不限 + 附录\n- Double-blind（匿名审稿）\n- Limitations section 必需\n- 提交时必须选择 EMNLP（绑定选择）\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- 论文的三个 contributions 是否清晰、non-trivial\n- Contribution 1（evaluation framework）：是否本质是 engineering benchmark 而非 methodological contribution？是否应降级？\n- Contribution 2（correlation-selection gap）：4/5 instance-level signals 无法 rank candidates 是 by construction——论文是否充分区分了 definitional limitation 和 empirical finding？\n- Contribution 3（task-complexity boundary）：是否充分展示了 non-obvious findings（WNUT-17 conditional collapse, LP negative correlation）？\n- 与 Nédellec et al. (2026) 的增量贡献是否充分量化？三个增量方向是否偏弱？\n- SJ（Soft Jaccard）方法论本身是否过度宣传？是否只是标准技术组合？\n\n### 2. Related Work 完整性\n- 是否遗漏重要相关工作（test-time scaling surveys, MBR in non-MT tasks, verification surveys）\n- 引用是否准确——特别关注 bib entries 的 author name、venue、year 一致性\n- 与 concurrent work 的定位是否公平\n\n### 3. 写作质量与 Framing\n- Abstract 是否过于密集（具体数字、signal 名称过多）？是否适合三段式精简？\n- 术语一致性：VC/Voting Conf./entity voting 是否统一？LP/Log-prob/logprob？\n- \"Cross-model\" 措辞是否过度（实为 cross-architecture at fixed 8B scale）？\n- \"First multi-family comparison\" 是否为 scope engineering？应改为描述性表述？\n- RE 结论在各处引用时是否一致标注 \"preliminary, single benchmark\"？\n- Figure/Table captions 是否简洁有效？\n- Ethics Statement 内容是否充分？\n\n### 4. 格式合规\n- 页数是否在 8 页正文限制内\n- Limitations section 是否存在且充分\n- 匿名是否完整（无作者信息泄露）\n- 引用格式是否符合 ACL natbib 规范\n\n请严格按照 EMNLP 审稿标准评审，不留情面。输出格式：Summary → Strengths → Weaknesses (Critical/Warning/Minor 分级) → Questions → Missing References → Scores (Soundness/Presentation/Contribution/Overall 1-5) → Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 的审查。\n\n## 论文信息\n- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子目录各章节）\n- **目标 Venue**: EMNLP 2026 Main Conference\n- **Track**: Main Conference (Long Paper)\n- **Deadline**: 2026-05-25 (ARR May 2026 cycle)\n\n## Venue 格式要求\n- ACL 模板，8 页正文 + 引用不限 + 附录\n- Double-blind（匿名审稿）\n- Limitations section 必需\n- 提交时必须选择 EMNLP（绑定选择）\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- 论文的三个 contributions 是否清晰、non-trivial\n- Contribution 1（evaluation framework）：是否本质是 engineering benchmark 而非 methodological contribution？是否应降级？\n- Contribution 2（correlation-selection gap）：4/5 instance-level signals 无法 rank candidates 是 by construction——论文是否充分区分了 definitional limitation 和 empirical finding？\n- Contribution 3（task-complexity boundary）：是否充分展示了 non-obvious findings（WNUT-17 conditional collapse, LP negative correlation）？\n- 与 Nédellec et al. (2026) 的增量贡献是否充分量化？三个增量方向是否偏弱？\n- SJ（Soft Jaccard）方法论本身是否过度宣传？是否只是标准技术组合？\n\n### 2. Related Work 完整性\n- 是否遗漏重要相关工作（test-time scaling surveys, MBR in non-MT tasks, verification surveys）\n- 引用是否准确——特别关注 bib entries 的 author name、venue、year 一致性\n- 与 concurrent work 的定位是否公平\n\n### 3. 写作质量与 Framing\n- Abstract 是否过于密集（具体数字、signal 名称过多）？是否适合三段式精简？\n- 术语一致性：VC/Voting Conf./entity voting 是否统一？LP/Log-prob/logprob？\n- \"Cross-model\" 措辞是否过度（实为 cross-architecture at fixed 8B scale）？\n- \"First multi-family comparison\" 是否为 scope engineering？应改为描述性表述？\n- RE 结论在各处引用时是否一致标注 \"preliminary, single benchmark\"？\n- Figure/Table captions 是否简洁有效？\n- Ethics Statement 内容是否充分？\n\n### 4. 格式合规\n- 页数是否在 8 页正文限制内\n- Limitations section 是否存在且充分\n- 匿名是否完整（无作者信息泄露）\n- 引用格式是否符合 ACL natbib 规范\n\n请严格按照 EMNLP 审稿标准评审，不留情面。输出格式：Summary → Strengths → Weaknesses (Critical/Warning/Minor 分级) → Questions → Missing References → Scores (Soundness/Presentation/Contribution/Overall 1-5) → Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 718 · 2026-05-15T12:15:08.646329+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1527
}
```

</details>

---


### Assistant

_source line 719 · 2026-05-15T12:15:19.116508+00:00_

两位 Reviewer 已派发，Round 1 独立审稿进行中。

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| **R1** | 方法严谨性 + 实验设计 + 统计检验 + 可复现性 | 审稿中 |
| **R2** | 新颖性 + 贡献定位 + Related Work + 写作质量 + 格式合规 | 审稿中 |

等待两位 Reviewer 提交初审报告后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 57

## Round 57

2 recorded events


### User

_source line 720 · 2026-05-15T12:20:35.144985+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验设计

**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction
**Venue**: EMNLP 2026 Main Conference (Long Paper)

---

### 总体评分

**Overall**: 3/5 (Findings of the ACL)
**一句话总结**: 论文提出了有价值的 correlation-selection gap 概念并提供了扎实的 quality estimation 分析，但核心 selection failure 结论建立在 single-seed 分析上、ε=0.05 阈值缺乏论证、free-form ablation 范围过窄却支撑了过强的泛化声称。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 方法定义清晰，QE 分析可靠；但 selection gap 的统计支撑不足（single seed）、关键阈值未论证、ablation 泛化过度 |
| Excitement | 3.5/5 | Correlation-selection gap 概念对 IE + test-time scaling 社区有实际指导意义；MBR 连接有洞察力 |
| Overall | 3/5 | 贡献真实但 selection 分析——论文的核心卖点——统计论证最弱；补充多种子 selection 分析后可达 Findings |
| Confidence | 4/5 | 仔细阅读全文含附录，核查公式推导和引用 |
| Reproducibility | 3.5/5 | 训练配置完整（Table 7），但核心实验 single seed 限制复现可信度 |

---

### Must-Fix 问题（3个 Critical）

**N1** [critical] Selection gap 分析缺乏多种子验证
- 位置：Section 4.3 / Table 3
- 核心 selection failure（LP NER +0.6pp, p=0.39）仅使用 seed=42。3-seed 分析（Table 10）仅覆盖 QE，未覆盖 selection F1。p=0.39 的 single-seed 结果不足以支撑论文的 headline finding。
- 建议：将 3-seed 分析扩展至 Table 3，报告跨种子 selection F1 的 mean±σ 和 p-value 范围。

**N2** [critical] ε=0.05 "effectively tied" 阈值缺乏论证
- 位置：Section 5 / Appendix H (Table 12)
- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59×跳变），说明阈值处于分布陡峭区域。"60% effectively tied" 出现在 abstract 中但 0.05 的依据未给出。
- 建议：提供 LP range 完整 CDF；或用连续度量（within-instance LP-F1 correlation）替代二元划分。

**N3** [critical] Free-form ablation 范围过窄但结论过强
- 位置：Section 5 §4 / Discussion
- 1 dataset × 1 model × 1 seed 的 ablation 支撑了 "fundamental challenge" 的声称。且 RE LP selection 在 free-form 下翻转（−0.68pp→+1.69pp），与 "not an artifact of decoding strategy" 矛盾。
- 建议：降级 "fundamental" 为 "observed in our setting"；明确承认 RE 翻转。

### Should-Fix 问题（5个 Warning）

**W1** FK 独立性检验功效极低（n=5 configurations 的 t-test）
**W2** VC 在 QE 和 selection 中使用不同计算但 Table 3 标注不清
**W3** TOST δ 值循环锚定于 oracle headroom，缺乏外部标准
**W4** LP 温度敏感性完全缺失（核心诊断对象却无 T=0.7 数据）
**W5** 标题/摘要暗示 NER+RE 均有多 benchmark 支持，实际 RE 仅单数据集

### 主要优势

- Correlation-selection gap 概念清晰且有社区价值
- 五信号三家族的系统化 taxonomy 是理论贡献
- RE "preliminary" 标注诚实，Limitations 详尽
- MBR decoding 连接是对 MBR 文献的有意义扩展
- 附录深度出色（12个补充分析章节）

### 引用验证

62篇引用全部 cross-check 通过，56篇 OpenAlex 确认，无伪造引用问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 721 · 2026-05-15T12:20:43.723468+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 58

## Round 58

2 recorded events


### User

_source line 722 · 2026-05-15T12:20:46.314335+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：论文在 quality estimation 层面做得扎实（5 signal × 3 dataset × 2 model 的系统比较，统计分析较完整），但其核心卖点——correlation-selection gap——的统计支撑存在三个 critical 级别问题：(1) selection 分析仅 single seed；(2) "60% effectively tied" 的 ε 阈值未论证；(3) free-form ablation 过窄但支撑了过强的泛化声称。建议 Overall 3/5（Findings 水平），补充多种子 selection 分析后有望提升。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 723 · 2026-05-15T12:20:55.389591+00:00_

Reviewer 1 审稿已收到。核心发现：3 个 critical（selection 单种子、ε 阈值无依据、ablation 泛化过度）+ 5 个 warning。Overall 3/5。

等待 Reviewer 2 完成审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 59

## Round 59

6 recorded events


### User

_source line 724 · 2026-05-15T12:22:43.010521+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告完成

**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction
**审查侧重**: 新颖性 + 完整性 + 写作质量

### 总体判断: 3/5 (Findings track)

实验工作量大、设计严谨，但核心 contribution framing 有根本性问题。

### 3 个 Critical Issues

**N1: Correlation-selection gap 大部分是 definitional，非 empirical**
4/5 signals 按设计对同一 instance 的所有 candidates 赋相同分数——论文 §5 自己承认这是 "Layer 1 (definitional)"，但 abstract/intro 将其包装为 empirical discovery。实际的 empirical finding 更窄：LP compression。需要根本性 reframing。

**N2: 模型规模同质性（仅 8B）无法支撑标题中 "Do Not Scale" 的 broad claim**
两个模型均为 8B 参数。论文自身发现 task difficulty × model capability 存在交互效应，但只测了一个 scale 点。标题/abstract 需要 scope down。

**N3: RE 结论过度前置但证据不足**
仅 SciERC RE 单 benchmark + Qwen only（preliminary），但 LP 负相关数字出现在 abstract 中。应从 abstract 移除或补充实验。

### 4 个 Warning Issues
- W1: Abstract 信息密度过高
- W2: "First multi-family comparison" 是 scope engineering
- W3: Evaluation framework (Contribution 1) 是 engineering benchmark 而非 methodological contribution
- W4: LP 的 temperature sensitivity 未表征（被排除在 T comparison 之外）
- W5: Conditional set 排除最难实例的 selection bias 未充分讨论
- W6: Eikema et al. (2025) structure-conditional MBR 仅在 Discussion 出现，应在 Related Work 中定位

### 主要优势
- 问题定位精准，负面结论有实用价值
- 实验设计远超平均水平（seed stability, bootstrap CI, TOST, free-form ablation）
- Quality estimation vs. sample selection 的 conceptual distinction 有价值
- 引用全面准确（62 篇，verify_references 无 orphan/missing）

### 引用验证结果
62 bib entries, 93 citations, 0 orphan, 0 missing, 56 online verified, 3 not found (recent preprints, normal), 3 mismatch (all false positives from encoding/name format)

### Scores
Soundness 3/5 | Excitement 3/5 | Overall 3/5 | Confidence 4/5

完整审稿意见已在对话中输出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 725 · 2026-05-15T12:23:13.220463+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Critical/Warning 级别的问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n**Overall**: 3/5\n\n### Must-Fix (Critical)\n\n**N1** [critical] Selection gap 分析缺乏多种子验证\n- Section 4.3 / Table 3 的核心 selection failure（LP NER +0.6pp, p=0.39）仅使用 seed=42。3-seed 分析（Table 10）仅覆盖 QE，未覆盖 selection F1。p=0.39 的 single-seed 结果不足以支撑论文的 headline finding。\n\n**N2** [critical] ε=0.05 \"effectively tied\" 阈值缺乏论证\n- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59×跳变），说明阈值处于分布陡峭区域。\"60% effectively tied\" 出现在 abstract 中但 0.05 的依据未给出。\n\n**N3** [critical] Free-form ablation 范围过窄但结论过强\n- 1 dataset × 1 model × 1 seed 的 ablation 支撑了 \"fundamental challenge\" 的声称。且 RE LP selection 在 free-form 下翻转（−0.68pp→+1.69pp），与 \"not an artifact of decoding strategy\" 矛盾。\n\n### Should-Fix (Warning)\n\n**W1** FK 独立性检验功效极低（n=5 configurations 的 t-test）\n**W2** VC 在 QE 和 selection 中使用不同计算但 Table 3 标注不清\n**W3** TOST δ 值循环锚定于 oracle headroom，缺乏外部标准\n**W4** LP 温度敏感性完全缺失（核心诊断对象却无 T=0.7 数据）\n**W5** 标题/摘要暗示 NER+RE 均有多 benchmark 支持，实际 RE 仅单数据集\n\n### 优势\n- Correlation-selection gap 概念清晰且有社区价值\n- 五信号三家族的系统化 taxonomy 是理论贡献\n- MBR decoding 连接有意义\n- 附录深度出色\n\n---\n\n请逐条（N1-N3, W1-W5）给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Critical/Warning 级别的问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n**Overall**: 3/5\n\n### Must-Fix (Critical)\n\n**N1** [critical] Selection gap 分析缺乏多种子验证\n- Section 4.3 / Table 3 的核心 selection failure（LP NER +0.6pp, p=0.39）仅使用 seed=42。3-seed 分析（Table 10）仅覆盖 QE，未覆盖 selection F1。p=0.39 的 single-seed 结果不足以支撑论文的 headline finding。\n\n**N2** [critical] ε=0.05 \"effectively tied\" 阈值缺乏论证\n- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59×跳变），说明阈值处于分布陡峭区域。\"60% effectively tied\" 出现在 abstract 中但 0.05 的依据未给出。\n\n**N3** [critical] Free-form ablation 范围过窄但结论过强\n- 1 dataset × 1 model × 1 seed 的 ablation 支撑了 \"fundamental challenge\" 的声称。且 RE LP selection 在 free-form 下翻转（−0.68pp→+1.69pp），与 \"not an artifact of decoding strategy\" 矛盾。\n\n### Should-Fix (Warning)\n\n**W1** FK 独立性检验功效极低（n=5 configurations 的 t-test）\n**W2** VC 在 QE 和 selection 中使用不同计算但 Table 3 标注不清\n**W3** TOST δ 值循环锚定于 oracle headroom，缺乏外部标准\n**W4** LP 温度敏感性完全缺失（核心诊断对象却无 T=0.7 数据）\n**W5** 标题/摘要暗示 NER+RE 均有多 benchmark 支持，实际 RE 仅单数据集\n\n### 优势\n- Correlation-selection gap 概念清晰且有社区价值\n- 五信号三家族的系统化 taxonomy 是理论贡献\n- MBR decoding 连接有意义\n- 附录深度出色\n\n---\n\n请逐条（N1-N3, W1-W5）给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 726 · 2026-05-15T12:23:18.705246+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 5484
}
```

</details>

---


### Tool call

_source line 727 · 2026-05-15T12:23:18.857511+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Critical/Warning 级别的问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n**Overall**: 3/5\n\n### Critical Issues\n\n**N1**: Correlation-selection gap 大部分是 definitional，非 empirical\n- 4/5 signals 按设计对同一 instance 的所有 candidates 赋相同分数——论文 §5 自己承认这是 \"Layer 1 (definitional)\"，但 abstract/intro 将其包装为 empirical discovery。实际的 empirical finding 更窄：LP compression。需要根本性 reframing。\n\n**N2**: 模型规模同质性（仅 8B）无法支撑标题中 \"Do Not Scale\" 的 broad claim\n- 两个模型均为 8B 参数。论文自身发现 task difficulty × model capability 存在交互效应，但只测了一个 scale 点。标题/abstract 需要 scope down。\n\n**N3**: RE 结论过度前置但证据不足\n- 仅 SciERC RE 单 benchmark + Qwen only（preliminary），但 LP 负相关数字出现在 abstract 中。应从 abstract 移除或补充实验。\n\n### Warning Issues\n\n**W1**: Abstract 信息密度过高\n**W2**: \"First multi-family comparison\" 是 scope engineering\n**W3**: Evaluation framework (Contribution 1) 是 engineering benchmark 而非 methodological contribution\n**W4**: LP 的 temperature sensitivity 未表征\n**W5**: Conditional set 排除最难实例的 selection bias 未充分讨论\n**W6**: Eikema et al. (2025) structure-conditional MBR 仅在 Discussion 出现，应在 Related Work 中定位\n\n### 优势\n- 问题定位精准，负面结论有实用价值\n- 实验设计远超平均水平\n- Quality estimation vs. sample selection 的 conceptual distinction 有价值\n- 引用全面准确\n\n---\n\n请逐条（N1-N3, W1-W6）给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Critical/Warning 级别的问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n**Overall**: 3/5\n\n### Critical Issues\n\n**N1**: Correlation-selection gap 大部分是 definitional，非 empirical\n- 4/5 signals 按设计对同一 instance 的所有 candidates 赋相同分数——论文 §5 自己承认这是 \"Layer 1 (definitional)\"，但 abstract/intro 将其包装为 empirical discovery。实际的 empirical finding 更窄：LP compression。需要根本性 reframing。\n\n**N2**: 模型规模同质性（仅 8B）无法支撑标题中 \"Do Not Scale\" 的 broad claim\n- 两个模型均为 8B 参数。论文自身发现 task difficulty × model capability 存在交互效应，但只测了一个 scale 点。标题/abstract 需要 scope down。\n\n**N3**: RE 结论过度前置但证据不足\n- 仅 SciERC RE 单 benchmark + Qwen only（preliminary），但 LP 负相关数字出现在 abstract 中。应从 abstract 移除或补充实验。\n\n### Warning Issues\n\n**W1**: Abstract 信息密度过高\n**W2**: \"First multi-family comparison\" 是 scope engineering\n**W3**: Evaluation framework (Contribution 1) 是 engineering benchmark 而非 methodological contribution\n**W4**: LP 的 temperature sensitivity 未表征\n**W5**: Conditional set 排除最难实例的 selection bias 未充分讨论\n**W6**: Eikema et al. (2025) structure-conditional MBR 仅在 Discussion 出现，应在 Related Work 中定位\n\n### 优势\n- 问题定位精准，负面结论有实用价值\n- 实验设计远超平均水平\n- Quality estimation vs. sample selection 的 conceptual distinction 有价值\n- 引用全面准确\n\n---\n\n请逐条（N1-N3, W1-W6）给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 728 · 2026-05-15T12:23:20.323483+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1465
}
```

</details>

---


### Assistant

_source line 729 · 2026-05-15T12:23:23.846357+00:00_

交叉分享已派发。等待两位 Reviewer 返回 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 60

## Round 60

2 recorded events


### User

_source line 730 · 2026-05-15T12:23:26.492469+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：论文实验工作扎实，但 3 个 critical issue（gap 的 definitional nature、scale 同质性、RE 证据不足）需要在 resubmission 前解决。Overall 3/5，建议 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 731 · 2026-05-15T12:23:31.299712+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 61

## Round 61

2 recorded events


### User

_source line 732 · 2026-05-15T12:25:12.947208+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

### Critical Issues

**[AGREE] R2-N1**: Correlation-selection gap 确实大部分是 definitional。论文 §5 自己承认 "Layer 1 (definitional)"，但 abstract/intro 将整个 gap 包装为统一的 empirical finding。实际 empirical contribution 更窄：LP compression 诊断 + MBR utility-quality misalignment + non-tied subset 分析。需要 reframing。

**[AGREE] R2-N2**: 仅 8B × 2 models 不足以支撑 "Do Not Scale" 的 universal claim。论文自身发现的 task difficulty × model capability 交互效应说明 model capability 是关键调节变量。标题需要 scope down。

**[REBUT] R2-N3**: R2 声称 "LP 负相关数字出现在 abstract 中"——这是误读。Abstract 中没有 RE 负相关数字。Introduction 中的 ρ=−0.410 是 WNUT-17 NER（非 RE）。但 R2 的 underlying concern（RE 证据不足被前置）与我的 W5 一致——问题在于 abstract 措辞暗示了比实际更广的 RE 覆盖度。建议 R2 修正 factual error。

### Warning Issues

**[AGREE] R2-W1**: Abstract 信息密度过高，8句话覆盖过多发现。
**[REBUT] R2-W2**: 论文未声称 "first multi-family comparison"。Contribution 1 的核心是三个 metrics 的 decouple（ρ-AUROC dissociation, Table 1），不是 priority claim。
**[REBUT] R2-W3**: Contribution 1 核心是三个 metrics decouple 的 empirical finding（EM leads AUROC=0.749 but ranks third in ρ=0.295），有实践意义。同意降级为 "finding" 比 "contribution" 更准确。
**[AGREE] R2-W4**: 与我的 W4 完全一致。LP 温度敏感性缺失是核心诊断对象的数据缺口。
**[REBUT] R2-W5**: Conditional filtering 是分离 binary detection 与 quality gradation 的 methodological 必要步骤，不是 selection bias。Table 5 显示 full-set ρ=0.724 完全由 zero/non-zero boundary 驱动。
**[AGREE] R2-W6**: eikema2025structured 应在 Related Work 的 MBR 段落中定位。

### 汇总

R2 的 N1（definitional reframing）和 N2（scale scope down）与我自己的评估一致，是需要作者解决的实质问题。N3 有 factual error 但 underlying concern 成立。W2/W3/W5 我持不同意见，已提供具体证据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 733 · 2026-05-15T12:25:17.965863+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 62

## Round 62

2 recorded events


### User

_source line 734 · 2026-05-15T12:25:20.585235+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。汇总：

- **3 个 AGREE**（R2-N1 definitional reframing、R2-N2 scale scope down、R2-W1/W4/W6）
- **3 个 REBUT**（R2-N3 的 factual error、R2-W2/W3 的 contribution 定性、R2-W5 的 conditional filtering）

R2 与我的评审在以下问题上形成共识：abstract/title 泛化过度、LP 温度数据缺失、RE 单 benchmark 不足。分歧主要在 evaluation framework 是否构成 contribution 以及 conditional filtering 是否引入 selection bias。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 735 · 2026-05-15T12:25:26.416605+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 63

## Round 63

8 recorded events


### User

_source line 736 · 2026-05-15T12:26:09.392387+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应完成（对 Reviewer 1）

**结果：8/8 全部 [AGREE]**

### Critical Issues (N1-N3): 全部同意
- **N1 (multi-seed selection)**: 同意。Table 10 仅覆盖 QE，selection F1 的 p=0.39 来自单 seed。补充观察：Table 6 中 LLaMA CoNLL SJ Δ_best=+1.0pp 在换种子后可能越过 significance。
- **N2 (ε=0.05 阈值)**: 同意。Table 12 的 59× 跳变（1.1%→60.3%）说明 abstract 中的 "60%" 高度依赖 arbitrary cutoff。建议报告完整 CDF。
- **N3 (free-form ablation)**: 同意。Table 14 Panel B 中 RE LP selection gap 从 −0.68pp 翻转为 +1.69pp，直接反驳 "task-inherent" claim。但 NER 的 compression 在 free-form 下持续存在。

### Warning Issues (W1-W5): 全部同意
- W1: n=5 t-test 无统计功效
- W2: VC 做 selection 实质是 random-among-tied，应明确标注。与我的 N1（definitional limitation）一致。
- W3: δ 循环锚定需外部标准（建议 ~1pp F1）
- W4: 强烈同意，与我的 W4 完全一致
- W5: 强烈同意，与我的 N3 完全一致

### 两份审稿的交集
核心问题归结为：(a) reframe definitional vs. empirical 部分；(b) multi-seed selection CI；(c) 收窄 RE scope；(d) ε threshold justification。

两份审稿互补性强——R1 聚焦方法/统计严谨性，R2 聚焦 framing/novelty/completeness。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 737 · 2026-05-15T12:27:07.193300+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 738 · 2026-05-15T12:27:07.244036+00:00_

1	issues:
2	- id: R0-C1
3	  summary: 模型规模单一（仅 8B）
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 1
9	  mentions:
10	  - round: 0
11	    reviewers:
12	    - 1
13	    - 2
14	    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性
15	  - round: 1
16	    reviewers:
17	    - 1
18	    - 2
19	    note: model-agnostic 与 Limitations 矛盾
20	  action_items:
21	  - round: 1
22	    action: 全文替换 model-agnostic → consistent across tested model families
23	    assigned_to: Paper Agent
24	    status: resolved
25	  resolution: Round 2 Reviewer 确认措辞修正到位，无再提
26	  resolution_round: 2
27	- id: R0-C2
28	  summary: 相关工作显著遗漏
29	  category: framing
30	  severity: warning
31	  status: resolved
32	  first_raised_round: 0
33	  last_seen_round: 1
34	  mentions:
35	  - round: 0
36	    reviewers:
37	    - 1
38	    - 2
39	    note: 5 篇核心文献缺失
40	  - round: 1
41	    reviewers:
42	    - 1
43	    - 2
44	    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC
45	  action_items:
46	  - round: 1
47	    action: 补充 6 篇引用到 Related Work
48	    assigned_to: Paper Agent
49	    status: resolved
50	  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 739 · 2026-05-15T12:35:42.274978+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确 maximize/minimize 方向, zero-IoU pairs 处理方式缺失\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善 [RESOLVED]\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective (max-weight matching on IoU) + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善，Hungarian matching 描述清晰'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison + cross-task caveat'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust; logprob uncharacterized\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄——仅 1 dataset × 1 model\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析 + Appendix Table 6\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐，无 signal 显著超越 greedy\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ 一个数据点\n  action_items:\n  - round: 2\n    action: 补全 5 信号 full/conditional ρ + AUROC + Appendix Table 5\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整，叙事修正为区分 full-set vs conditional\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI + Appendix 表\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix，SJ-logprob 显著\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, 96.6% pairs sim≥0.5, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap + 补 p=0.80 到论文\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80, all signals below greedy\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾 (Table 2 vs L129)\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 logprob=0.395 (-0.9pp) vs L129 logprob=0.410 (+0.6pp)\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确 → Paper Agent 修正 L129\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: L129 统一为 logprob=0.395, -0.9pp, p=0.80\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误 (Voting ρ 配 EM AUROC)\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注 Voting ρ 和 EM AUROC\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 两位 Reviewer 均独立提出。Outlines/vLLM constrained decoding 可能压缩 per-sample diversity，使 gap 成为实验设置 artifact。\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决（承认但未量化）。R1 仍列 critical（需 logprob 分布分析）。\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出为 critical。Appendix F 已有 logprob tie 分析。\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix。共识：需在 Introduction 和 Discussion 收紧 scope。\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity；Paper Agent 写入论文 + 限定 scope\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope 为 constrained decoding setting\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 末尾各加 1 句明确声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: 'exp-018 free-form ablation 证明 gap 是 task-intrinsic 而非 decoding artifact。D075 决策记录。'\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence，selection gap 统计论证不完整\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：TOST 已补充，措辞修正到位\n  action_items:\n  - round: 3\n    action: 修改措辞 + 6/6 cumulative evidence 论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: TOST 等价检验已补充，措辞修正为 no significant evidence'\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed (seed=42)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 selection 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：3-seed 验证已补充\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险并引用 N=16 stability\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: 3-seed 稳定性验证已补充'\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM CI lower bound +0.003 在 Bonferroni 下不会 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：Bonferroni 声明已加\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正 + SJ-EM 改为 suggestive\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: Bonferroni 声明已加'\n  resolution_round: 4\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: R4 两位 Reviewer 独立再次提出：Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial。共识：gap 不完全 tautological。\n  - round: 6\n    reviewers: [1, 2]\n    note: 两位 Reviewer 再次达成共识：Abstract/Introduction 仍将 4/5 signals fail 与 logprob failure 并列呈现。应先 dismiss instance-level，然后聚焦 consensus-proximity failure 和 logprob score compression。\n  - round: 7\n    reviewers: [1, 2]\n    note: 'Round 7 fresh review 两位 Reviewer 独立再次提出为 critical（R2-N1）。论文 §5 自己承认 Layer 1 (definitional)，但 abstract/intro 仍将整个 gap 包装为统一 empirical discovery。R1 agree。共识：需根本性 reframing——dismiss instance-level failure in one sentence，聚焦 LP compression + MBR failure 作为核心 empirical contribution。'\n  action_items:\n  - round: 3\n    action: Discussion 中分离两层论证\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 4\n    action: Introduction 正面论证 why gap is not obvious\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 5\n    action: 'Reframe C2: 以 logprob score compression + MBR failure 为中心'\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: Abstract 和 Introduction 重构：先 dismiss instance-level selection\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 根本性 reframing——Abstract/Introduction/Contribution 2 以 LP compression 诊断 + MBR utility-quality misalignment 为核心 empirical finding，instance-level failure 用 1 句 dismiss\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W3\n  summary: Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR decoding 是成熟替代方案但未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：MBR 连接已补充\n  action_items:\n  - round: 3\n    action: 明确 consensus-proximity 与 MBR 联系 + 引用 MBR 文献\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: §5 MBR decoding 连接段已写入'\n  resolution_round: 4\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: §3.2 一句 hand-wave。需报告 inter-sample correlation\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：excess agreement 数据已补充\n  - round: 5\n    reviewers: [1]\n    note: R1 重新提出：excess agreement 未注明 configuration\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 再提 excess agreement 无显著性检验。R2 同意但认为 severity 偏低。\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1 列 warning（R1-W1）：n=5 configurations 的 one-sample t-test 功效极低，基本无统计意义。R2 agree。论文现已报告 excess agreement (-0.4% to -4.0%) 和 p<0.05，但 n=5 的 t-test 本身不可信。需 permutation test 或 bootstrap CI，或在论文中承认此局限性。'\n  action_items:\n  - round: 3\n    action: Agent 量化 inter-sample correlation；Paper Agent 写入\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: 注明 excess agreement 的 configuration；补充所有配置数据\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 将 sufficient response diversity 改为 mild negative dependence\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 承认 n=5 t-test 功效不足；改用 per-instance permutation test 或 bootstrap CI；或降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 两模型均 8B，措辞过度外推\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：cross-architecture 措辞已统一\n  - round: 5\n    reviewers: [1, 2]\n    note: R1 再次提出：Conclusion 仍用 across model families 而非限定 at 8B scale\n  - round: 6\n    reviewers: [1, 2]\n    note: 仍未修复。多处使用 cross-model 或 across models 无 scale 限定。\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R2-N2 升级为 critical：标题 \"Do Not Scale\" 暗示 universal negative result，但仅 8B × 2 models。R1 agree。论文 Conclusion L7 写 \"consistent ordering across two model families at 8B scale\" 但标题和 abstract 不含此限定。'\n  action_items:\n  - round: 5\n    action: Conclusion 和 Abstract 统一加 at 8B scale 限定\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 全文统一 cross-model → across two model families at 8B scale\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 标题 scope down（加 at 8B Scale 或类似限定）；全文 cross-model → across two 8B model families\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W6\n  summary: '''First multi-family comparison'' claim scope 过宽'\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE 的 QE + selection\n  - round: 4\n    reviewers: [2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: scope engineering\n  - round: 6\n    reviewers: [1, 2]\n    note: 共识：去掉 first claim，将 Contribution 1 降级\n  - round: 7\n    reviewers: [1]\n    note: 'R1 rebut R2-W2：论文当前版本未声称 first multi-family comparison。Contribution 1 核心是三个 metrics 的 decouple（ρ-AUROC dissociation）。Round 7 R2 亦未在独立审稿中提及 first claim。可能已修复。'\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: Contribution 1 降级为 methodology/setup\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 待 Research Director 确认当前论文是否仍含 first claim；如已移除则标记 resolved\n    assigned_to: Research Director\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: confidence signal vs consistency signal 混用；VC vs Voting Conf.\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决：表格缩写仍不统一\n  - round: 5\n    reviewers: [1, 2]\n    note: 仍未解决。Table 1 Voting Conf.，Table 4/7 VC\n  - round: 6\n    reviewers: [1, 2]\n    note: 还发现 LP/Log-prob/logprob 三种写法\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文当前 Table 1 使用 VC/SJ/FK/EM/LP；Notation table 定义一致。可能已修复，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: 全文统一 VC/SJ/FK/EM/LP 五个缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W8\n  summary: 遗漏引用：VerifiNER, RASC, MBR decoding, Malinin & Gales\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: VerifiNER, MBR decoding 等高度相关\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用并在 Related Work 中讨论\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: 引用已补全'\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% zero F1 与 Table 7 数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 正文 54%\n  action_items:\n  - round: 3\n    action: Agent 核实实际数字 → Paper Agent 统一\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏经验支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: probability negligible 需报告 exact match pairs 频率\n  action_items:\n  - round: 3\n    action: Agent 计算 exact match pairs 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 3\n    reviewers: [2]\n    note: 共识降为 minor\n  - round: 4\n    reviewers: [2]\n    note: Ethics Statement 位于 Limitations section 内\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section，格式合规\n  action_items:\n  - round: 4\n    action: 将 Ethics Statement 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 5: Ethics Statement 已为独立 section'\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 作为独立发现过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 建议承认统计预期性后聚焦实践含义\n  action_items:\n  - round: 3\n    action: §4.2 承认 dissociation 的统计预期性\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: 对 Nedellec (2026) 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 建议用更 neutral 语气\n  action_items:\n  - round: 3\n    action: Introduction 中改为更 neutral 的语气\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Nedellec 措辞已改为 neutral\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ 验证中 Δρ 和 per-instance Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ=−0.014 vs per-instance max Δρ=3.1×10⁻⁴ 量纲不同\n  action_items:\n  - round: 3\n    action: 澄清 per-instance Δρ 具体含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: LOO-SJ Δρ 含义已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 建议加 (Table 2) 交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Figure 1 caption 交叉引用已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: §4.1 缺少 lr, batch size 等\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含完整 Table 8 + prompt template\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 5: Appendix E Table 8 完整，Reproducibility 4/5'\n  resolution_round: 5\n- id: R4-W1\n  summary: RE 证据需进一步加强（conditional analysis 或降级）\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: claim 降级已完成，但两位 Reviewer 仍认为 RE 证据薄弱\n  - round: 5\n    reviewers: [1, 2]\n    note: Abstract 标注 (SciERC, preliminary) 但后续引用无限定\n  - round: 6\n    reviewers: [1, 2]\n    note: 仍存在。Discussion/Conclusion 引用 RE 结论时缺少一致的 preliminary 标注\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R2-N3 列 critical（RE 过度前置）+ R1-W5（RE scope 措辞过度）。R1 纠正 R2 事实错误（LP 负相关是 WNUT-17 NER 非 RE）但同意 underlying concern。Abstract 当前提到 RE 但未含 negative correlation 数字。论文各处 RE 标注不一致：有些写 preliminary，有些不写。'\n  action_items:\n  - round: 5\n    action: 所有 RE 分析处一致标注 single-benchmark preliminary\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: Discussion/Conclusion 中每次引用 RE 结论时一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 全文 RE 引用一致标注 (preliminary, single benchmark)；考虑从 abstract 移除 RE 具体数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W2\n  summary: SJ vs EM 优势叙事应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: SJ vs EM Δρ=+0.065, Bonferroni 下不显著\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage，改为 difficulty-dependent complementarity\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 5: §4.2 已用 complementarity 措辞'\n  resolution_round: 5\n- id: R4-W3\n  summary: Abstract 过于密集，超长句子需拆分\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: 多层嵌套括号和分号的超长句子\n  - round: 5\n    reviewers: [1, 2]\n    note: 仍未修改\n  - round: 6\n    reviewers: [1, 2]\n    note: 第 3 轮仍未解决。共识：减少具体数字，abstract 聚焦问题-发现-意义三段式\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R2-W1 再次提出。R1 agree。Abstract 仍含 5 signal family 名称、3 datasets、2 models、4 metrics + gap 概念。共识：精简为问题-发现-意义三段式，将具体信号名和数字移到 Introduction。'\n  action_items:\n  - round: 5\n    action: Abstract 拆分为 2-3 句核心 claim\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: Abstract 精简为问题-发现-意义三段式\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: Abstract 精简为问题-发现-意义三段式，移除大部分具体数字和信号名到 Introduction\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: 系统评估 LLM 置信度获取方法\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work §2 已引用 Xiong et al.\n  action_items:\n  - round: 4\n    action: Related Work 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 5: 已引用'\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: max(|g_i|,|g_j|) vs |g_i∪g_j| 未比较\n  action_items:\n  - round: 4\n    action: 附录补 union normalizer 结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已在 method.tex 有理由，超出 scope\n  resolution_round: 4\n- id: R4-M2\n  summary: TOST δ 选择（±2/3/5 pp）缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: δ 选择直接影响等价结论\n  - round: 5\n    reviewers: [1, 2]\n    note: R1 再提：与 IAA 关联无引用。R2 认为多水平 δ 已构成 sensitivity analysis。\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 升级为 must-fix。R2 agree。建议报告 breakpoint δ*。\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-W3 再次提出：δ 循环锚定于 oracle headroom（δ=5pp = forgoing 28-38% of headroom），但 oracle headroom 正是被调查量，构成循环论证。R2 agree。建议用外部标准（IAA 变异、deployment threshold）或更突出 breakpoint δ*。'\n  action_items:\n  - round: 5\n    action: 引用 IE benchmark IAA 数据来锚定 δ 选择\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 报告 breakpoint δ*；强化 effect size + bootstrap CI\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 用外部标准（SESOI 框架或 deployment F1 threshold）替代 oracle headroom 锚定；将 breakpoint δ* 和 Cohen's d + CI 作为主要证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-M3\n  summary: Table 1 N=16 block 大面积空白\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: N=16 仅填 LLaMA CoNLL，SciERC 空白\n  - round: 5\n    reviewers: [1, 2]\n    note: 已加脚注但格式可能异常\n  - round: 6\n    reviewers: [1, 2]\n    note: 仍建议将 N=16 行移入 Appendix Table 3\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文当前 Table 1 仅含 N=8，N=16 在脚注引向 Appendix。可能已修复，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行，合并到 Appendix Table 3\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: 三个增量均偏弱\n  - round: 6\n    reviewers: [1, 2]\n    note: R2 再提。共识：增量贡献存在但论文过度强调\n  - round: 7\n    reviewers: []\n    note: 本轮未直接提及。R2-N1 的 reframing 要求间接涵盖此问题——如果核心贡献 reframe 为 LP compression + MBR failure（而非 gap 本身），Nédellec 增量问题将自然缓解。\n  action_items:\n  - round: 5\n    action: 更诚实地量化增量大小\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致（SciERC vs CoNLL/WNUT）\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: SciERC 未显式禁用 enable_thinking\n  - round: 6\n    reviewers: [1, 2]\n    note: 两位 Reviewer 再次独立提出。共识：在 Experiments Setup 中 prominently 声明\n  - round: 7\n    reviewers: []\n    note: 本轮未提及为 issue。论文 §4.1 现已显式声明 thinking token confound（3 句话），Limitations 中也有讨论。R1 Reproducibility 评 3.5/5 未提及此问题。可能已充分解决，待 Research Director 确认。\n  action_items:\n  - round: 5\n    action: Limitations 讨论此不一致性\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: Experiments Setup §4.1 中显著声明\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: R1 建议删除或缩短；R2 认为意图合理但执行可能误导\n  - round: 6\n    reviewers: [1, 2]\n    note: 共识：缩短脚注，去掉具体数字\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文脚注已缩短为 comparable AUROC on discrete-answer QA 并加 cross-task caveat。可能已修复，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: 缩短脚注，保留 comparable AUROC 但去掉具体数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W3\n  summary: he2024uncertainty bib entry 与引用上下文不匹配\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1]\n    note: bib 标题是 sequential labeling 论文，但引用上下文是 LLM UQ survey\n  - round: 7\n    reviewers: []\n    note: 本轮 R1 验证 62 篇引用全部通过，未再提及此问题。可能已修正，待 Research Director 确认。\n  action_items:\n  - round: 5\n    action: 修正引用上下文描述\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling verification survey 引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 建议补 verification survey\n  - round: 6\n    reviewers: [1, 2]\n    note: R2 具体指出 Zhang et al. (2025) TTS survey。共识 should-fix。\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文 Related Work 已引用 zhang2025tts (test-time scaling)。R1 验证引用完整。可能已修复，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: Related Work §2 补充 Zhang et al. (2025) TTS survey 引用\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Discussion §5 将方法与 MBR 对接但只引用 MT 领域\n  - round: 6\n    reviewers: [1, 2]\n    note: R2 具体指出 Eikema et al. (EMNLP 2025)\n  - round: 7\n    reviewers: [2]\n    note: 'R2-W6 再次提出（rebrand）：Eikema et al. (2025) structure-conditional MBR 仅在 Discussion 出现，应在 Related Work 中定位。R1 agree。论文 Discussion 已引用 eikema2025structured，但应前移到 Related Work §2 的 MBR 段落。'\n  action_items:\n  - round: 6\n    action: Discussion §5 MBR 段补充 Eikema et al.\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 将 eikema2025structured 的讨论从 Discussion 前移到 Related Work §2 MBR 段落\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M3\n  summary: Consensus-proximity = LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §3.3 声称数学等价但未给出推导\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含完整等价性证明\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 已包含完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到或 author name 有 variant\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: hobelsberger2025systematic, lightman2024verify 未找到\n  - round: 6\n    reviewers: [1, 2]\n    note: snell2024scaling key 标 2024 但 venue 为 ICLR 2025\n  - round: 7\n    reviewers: []\n    note: 'R1 Round 7 验证 62 篇引用全部通过（56 online verified, 3 not found = recent preprints, 3 mismatch = encoding false positives）。R2 同样报告 0 orphan, 0 missing, 3 not found (normal)。未再提及具体 bib 问题。可能已修正或属于正常范围。'\n  action_items:\n  - round: 6\n    action: 核实 ye2025uncertainty, snell2024scaling, feng2025optimal, hobelsberger2025systematic\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句，内容偏简\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: 格式合规但内容偏简\n  - round: 6\n    reviewers: [2]\n    note: 应注明 CoNLL-2003 Reuters license 限制\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文 Ethics Statement 现已包含 CoNLL-2003 Reuters RCV1 corpus 和 NIST agreement 说明。可能已充分解决，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: Ethics Statement 补充 CoNLL-2003 Reuters license 注明\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C1\n  summary: Constrained decoding 混淆变量未隔离，claim scope 与 evidence 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Title/Abstract/Conclusion 需限定 constrained decoding scope\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并追踪\n  action_items:\n  - round: 5\n    action: Title 加 under Constrained Decoding\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: 见 R3-C1 Round 6 action\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: 与 R3-C1 合并。exp-018 free-form ablation 证明 gap task-intrinsic。D075。\n  resolution_round: 7\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: 4/5 instance-level failure = tautological\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。共识：重构叙事以 logprob compression + MBR failure 为中心。\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并。Round 7 fresh review 两位 Reviewer 独立再次提出。见 R3-W2 Round 7 mention。\n  action_items:\n  - round: 5\n    action: Reframe C2 聚焦 logprob compression + MBR failure\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 见 R3-W2 Round 6 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: '''First multi-family comparison'' claim = scope engineering'\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: 建议改为描述性表述\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-W6 合并追踪\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。Round 7 R1 rebut 论文当前版本未含 first claim。见 R3-W6 Round 7 mention。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 见 R3-W6 Round 6 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W5\n  summary: '''Cross-architecture'' 用词过度（两个 8B decoder-only）'\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: 改为 across two model families at 8B scale\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并。Round 7 R2-N2 升级为 critical（标题 scope）。见 R3-W5 Round 7 mention。\n  action_items:\n  - round: 5\n    action: 全文替换 cross-architecture\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 见 R3-W5 Round 6 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Excess agreement 未注明 configuration\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并。见 R3-W4 Round 7 mention。\n  action_items:\n  - round: 5\n    action: 补 configuration 信息 + 引用文献\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 见 R3-W4 Round 6 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限，core structural signal 过度宣传\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: R2 认为标准技术组合\n  - round: 7\n    reviewers: []\n    note: 本轮未直接提及。R2 Round 7 未在独立审稿中重新提出 SJ novelty 问题。可能已通过 complementarity 措辞缓解，待 Research Director 确认。\n  action_items:\n  - round: 5\n    action: core structural signal → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关 (ρ=-0.410) 机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: capability boundary 下 logprob 反映 fluency 而非 accuracy\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: §4 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设，引用 Xiong et al.\n  resolution_round: 6\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致：无阈值 vs majority threshold\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Equation 6 定义为所有 entity 平均频率（无阈值），但 Footnote 2 承认实现使用 majority threshold (>N/2)。两者数学上不等价。\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-W2 再次提出：VC 在 QE（Eq.6 连续）和 selection（majority threshold）中使用不同计算，但 Table 3 标注不清。Footnote 2 报告了 ρ 差异（threshold ρ=0.252 vs Eq.6 ρ=0.379），但表格未标明使用的是哪种实现。R2 agree（通过 W2 response）。'\n  action_items:\n  - round: 6\n    action: 统一公式和实现；报告两种实现的 ρ 差值；明确 Table 1 使用哪种实现\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: Table 3 caption 或脚注明确标注 VC selection 使用 majority threshold（非 Eq.6 连续值）；保持 QE 和 selection 的分离但标注更清晰\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W2\n  summary: Figure 1 caption 冗余——重复 Section 4.2/4.3 内容\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Figure 1 caption 引入 p=0.39、Table 2 引用等与正文重复\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文 Figure 1 caption 当前仅含核心信息（Left/Right 描述）。可能已精简，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: 精简 Figure 1 caption\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证——核心 headline finding 仅 single seed\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-N1: 核心 selection failure（LP NER +0.6pp, p=0.39, Table 3）仅使用 seed=42。3-seed 分析（Table 10）仅覆盖 QE 而非 selection F1。p=0.39 来自单种子不足以支撑论文 headline finding。R2 agree 并补充：Table 6 中 LLaMA CoNLL SJ Δ_best=+1.0pp 在换种子后可能越过 significance。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3（selection F1），报告跨种子 selection F1 mean±σ 和 p-value range\n    assigned_to: Agent + Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 \"effectively tied\" 阈值缺乏论证——abstract 数字依赖 arbitrary cutoff\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-N2: Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59× 跳变），说明阈值处于分布陡峭区域。\"60% effectively tied\" 出现在 abstract 中但 0.05 的依据未给出。R2 agree（abstract 数字高度依赖 arbitrary cutoff）。建议提供 LP range 完整 CDF 或用连续度量（within-instance LP-F1 correlation）替代二元划分。'\n  action_items:\n  - round: 7\n    action: (a) 提供 LP range 完整 CDF 图或表；(b) 论证 ε=0.05 的选择依据或改用连续度量；(c) abstract 中避免依赖单一 arbitrary cutoff 的数字\n    assigned_to: Agent + Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑了过强的泛化声称\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-N3: 1 dataset × 1 model × 1 seed 的 ablation 支撑了 \"fundamental challenge\" 和 \"intrinsic to the model and task\" 声称。RE LP selection 在 free-form 下翻转（−0.68pp→+1.69pp, Table 14 Panel B），部分反驳 \"not an artifact of decoding strategy\"。R2 agree 但补充 NER compression 在 free-form 下持续存在。共识：NER 结论可保留但需降级措辞；RE 翻转必须明确承认。'\n  action_items:\n  - round: 7\n    action: (a) 降级 \"fundamental\"/\"intrinsic\" 为 \"observed in our NER setting\"；(b) 明确承认 RE LP selection 在 free-form 下的翻转；(c) 区分 NER（compression 持续）和 RE（翻转）的 ablation 结论\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失——核心诊断对象无 T=0.7 数据\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-W4 + R2-W4: LP 是论文核心诊断对象（score compression, per-sample discrimination），但被排除在温度比较（T=0.7 vs T=1.0）之外。Limitations 提到但未解释为何缺失。score compression 可能是 T-dependent（T=0.7 下 logit 分布更集中可能加剧或缓解 compression），而温度正是影响 LP 分布的关键参数。两位 Reviewer 均列 warning。'\n  action_items:\n  - round: 7\n    action: (a) 补充 T=0.7 LP 数据（如可获得）；(b) 如数据不可获得，在 Limitations 中更充分讨论 LP 温度敏感性未知的影响\n    assigned_to: Agent + Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 (evaluation framework) 定性有分歧——engineering benchmark vs methodological contribution\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R2-W3 认为 Contribution 1 本质是 engineering benchmark 而非 methodological contribution，应降级。R1 rebut：核心是三个 metrics 的 decouple（ρ-AUROC dissociation, EM leads AUROC=0.749 but ranks third in ρ=0.295）有实践意义。但 R1 同意 \"contribution\" framing 可能 overstate，\"finding\" 更准确。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 \"contribution\" 降级为 \"setup/methodology\"，以 ρ-AUROC dissociation 作为 secondary finding\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) structure-conditional MBR 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R2-W6: eikema2025structured 仅在 Discussion 出现（§5 MBR decoding 连接段），应在 Related Work §2 的 MBR 段落中定位以建立 prior awareness。R1 agree。与 R5-M2 合并追踪——R5-M2 要求补引用（已完成），R7-W3 要求调整引用位置。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 的引用从 Discussion 前移（或同时在）Related Work §2 MBR 段\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确 maximize/minimize 方向, zero-IoU pairs 处理方式缺失\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善 [RESOLVED]\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective (max-weight matching on IoU) + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善，Hungarian matching 描述清晰'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison + cross-task caveat'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust; logprob uncharacterized\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄——仅 1 dataset × 1 model\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析 + Appendix Table 6\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐，无 signal 显著超越 greedy\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ 一个数据点\n  action_items:\n  - round: 2\n    action: 补全 5 信号 full/conditional ρ + AUROC + Appendix Table 5\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整，叙事修正为区分 full-set vs conditional\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI + Appendix 表\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix，SJ-logprob 显著\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, 96.6% pairs sim≥0.5, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap + 补 p=0.80 到论文\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80, all signals below greedy\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾 (Table 2 vs L129)\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 logprob=0.395 (-0.9pp) vs L129 logprob=0.410 (+0.6pp)\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确 → Paper Agent 修正 L129\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: L129 统一为 logprob=0.395, -0.9pp, p=0.80\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误 (Voting ρ 配 EM AUROC)\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注 Voting ρ 和 EM AUROC\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 两位 Reviewer 均独立提出。Outlines/vLLM constrained decoding 可能压缩 per-sample diversity，使 gap 成为实验设置 artifact。\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决（承认但未量化）。R1 仍列 critical（需 logprob 分布分析）。\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出为 critical。Appendix F 已有 logprob tie 分析。\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix。共识：需在 Introduction 和 Discussion 收紧 scope。\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity；Paper Agent 写入论文 + 限定 scope\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope 为 constrained decoding setting\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 末尾各加 1 句明确声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: 'exp-018 free-form ablation 证明 gap 是 task-intrinsic 而非 decoding artifact。D075 决策记录。'\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence，selection gap 统计论证不完整\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：TOST 已补充，措辞修正到位\n  action_items:\n  - round: 3\n    action: 修改措辞 + 6/6 cumulative evidence 论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: TOST 等价检验已补充，措辞修正为 no significant evidence'\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed (seed=42)\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 selection 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：3-seed 验证已补充\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险并引用 N=16 stability\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: 3-seed 稳定性验证已补充'\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM CI lower bound +0.003 在 Bonferroni 下不会 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：Bonferroni 声明已加\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正 + SJ-EM 改为 suggestive\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: Bonferroni 声明已加'\n  resolution_round: 4\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: R4 两位 Reviewer 独立再次提出：Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial。共识：gap 不完全 tautological。\n  - round: 6\n    reviewers: [1, 2]\n    note: 两位 Reviewer 再次达成共识：Abstract/Introduction 仍将 4/5 signals fail 与 logprob failure 并列呈现。应先 dismiss instance-level，然后聚焦 consensus-proximity failure 和 logprob score compression。\n  - round: 7\n    reviewers: [1, 2]\n    note: 'Round 7 fresh review 两位 Reviewer 独立再次提出为 critical（R2-N1）。论文 §5 自己承认 Layer 1 (definitional)，但 abstract/intro 仍将整个 gap 包装为统一 empirical discovery。R1 agree。共识：需根本性 reframing——dismiss instance-level failure in one sentence，聚焦 LP compression + MBR failure 作为核心 empirical contribution。'\n  action_items:\n  - round: 3\n    action: Discussion 中分离两层论证\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 4\n    action: Introduction 正面论证 why gap is not obvious\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 5\n    action: 'Reframe C2: 以 logprob score compression + MBR failure 为中心'\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: Abstract 和 Introduction 重构：先 dismiss instance-level selection\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 根本性 reframing——Abstract/Introduction/Contribution 2 以 LP compression 诊断 + MBR utility-quality misalignment 为核心 empirical finding，instance-level failure 用 1 句 dismiss\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W3\n  summary: Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR decoding 是成熟替代方案但未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：MBR 连接已补充\n  action_items:\n  - round: 3\n    action: 明确 consensus-proximity 与 MBR 联系 + 引用 MBR 文献\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: §5 MBR decoding 连接段已写入'\n  resolution_round: 4\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: §3.2 一句 hand-wave。需报告 inter-sample correlation\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：excess agreement 数据已补充\n  - round: 5\n    reviewers: [1]\n    note: R1 重新提出：excess agreement 未注明 configuration\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 再提 excess agreement 无显著性检验。R2 同意但认为 severity 偏低。\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1 列 warning（R1-W1）：n=5 configurations 的 one-sample t-test 功效极低，基本无统计意义。R2 agree。论文现已报告 excess agreement (-0.4% to -4.0%) 和 p<0.05，但 n=5 的 t-test 本身不可信。需 permutation test 或 bootstrap CI，或在论文中承认此局限性。'\n  action_items:\n  - round: 3\n    action: Agent 量化 inter-sample correlation；Paper Agent 写入\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: 注明 excess agreement 的 configuration；补充所有配置数据\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 将 sufficient response diversity 改为 mild negative dependence\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 承认 n=5 t-test 功效不足；改用 per-instance permutation test 或 bootstrap CI；或降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 两模型均 8B，措辞过度外推\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED：cross-architecture 措辞已统一\n  - round: 5\n    reviewers: [1, 2]\n    note: R1 再次提出：Conclusion 仍用 across model families 而非限定 at 8B scale\n  - round: 6\n    reviewers: [1, 2]\n    note: 仍未修复。多处使用 cross-model 或 across models 无 scale 限定。\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R2-N2 升级为 critical：标题 \"Do Not Scale\" 暗示 universal negative result，但仅 8B × 2 models。R1 agree。论文 Conclusion L7 写 \"consistent ordering across two model families at 8B scale\" 但标题和 abstract 不含此限定。'\n  action_items:\n  - round: 5\n    action: Conclusion 和 Abstract 统一加 at 8B scale 限定\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 全文统一 cross-model → across two model families at 8B scale\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 标题 scope down（加 at 8B Scale 或类似限定）；全文 cross-model → across two 8B model families\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W6\n  summary: '''First multi-family comparison'' claim scope 过宽'\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE 的 QE + selection\n  - round: 4\n    reviewers: [2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: scope engineering\n  - round: 6\n    reviewers: [1, 2]\n    note: 共识：去掉 first claim，将 Contribution 1 降级\n  - round: 7\n    reviewers: [1]\n    note: 'R1 rebut R2-W2：论文当前版本未声称 first multi-family comparison。Contribution 1 核心是三个 metrics 的 decouple（ρ-AUROC dissociation）。Round 7 R2 亦未在独立审稿中提及 first claim。可能已修复。'\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: Contribution 1 降级为 methodology/setup\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 待 Research Director 确认当前论文是否仍含 first claim；如已移除则标记 resolved\n    assigned_to: Research Director\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: confidence signal vs consistency signal 混用；VC vs Voting Conf.\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决：表格缩写仍不统一\n  - round: 5\n    reviewers: [1, 2]\n    note: 仍未解决。Table 1 Voting Conf.，Table 4/7 VC\n  - round: 6\n    reviewers: [1, 2]\n    note: 还发现 LP/Log-prob/logprob 三种写法\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文当前 Table 1 使用 VC/SJ/FK/EM/LP；Notation table 定义一致。可能已修复，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: 全文统一 VC/SJ/FK/EM/LP 五个缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W8\n  summary: 遗漏引用：VerifiNER, RASC, MBR decoding, Malinin & Gales\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: VerifiNER, MBR decoding 等高度相关\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用并在 Related Work 中讨论\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: 引用已补全'\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% zero F1 与 Table 7 数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 正文 54%\n  action_items:\n  - round: 3\n    action: Agent 核实实际数字 → Paper Agent 统一\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏经验支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: probability negligible 需报告 exact match pairs 频率\n  action_items:\n  - round: 3\n    action: Agent 计算 exact match pairs 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 3\n    reviewers: [2]\n    note: 共识降为 minor\n  - round: 4\n    reviewers: [2]\n    note: Ethics Statement 位于 Limitations section 内\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section，格式合规\n  action_items:\n  - round: 4\n    action: 将 Ethics Statement 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 5: Ethics Statement 已为独立 section'\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 作为独立发现过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 建议承认统计预期性后聚焦实践含义\n  action_items:\n  - round: 3\n    action: §4.2 承认 dissociation 的统计预期性\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: 对 Nedellec (2026) 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 建议用更 neutral 语气\n  action_items:\n  - round: 3\n    action: Introduction 中改为更 neutral 的语气\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Nedellec 措辞已改为 neutral\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ 验证中 Δρ 和 per-instance Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ=−0.014 vs per-instance max Δρ=3.1×10⁻⁴ 量纲不同\n  action_items:\n  - round: 3\n    action: 澄清 per-instance Δρ 具体含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: LOO-SJ Δρ 含义已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 建议加 (Table 2) 交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Figure 1 caption 交叉引用已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: §4.1 缺少 lr, batch size 等\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含完整 Table 8 + prompt template\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 5: Appendix E Table 8 完整，Reproducibility 4/5'\n  resolution_round: 5\n- id: R4-W1\n  summary: RE 证据需进一步加强（conditional analysis 或降级）\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: claim 降级已完成，但两位 Reviewer 仍认为 RE 证据薄弱\n  - round: 5\n    reviewers: [1, 2]\n    note: Abstract 标注 (SciERC, preliminary) 但后续引用无限定\n  - round: 6\n    reviewers: [1, 2]\n    note: 仍存在。Discussion/Conclusion 引用 RE 结论时缺少一致的 preliminary 标注\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R2-N3 列 critical（RE 过度前置）+ R1-W5（RE scope 措辞过度）。R1 纠正 R2 事实错误（LP 负相关是 WNUT-17 NER 非 RE）但同意 underlying concern。Abstract 当前提到 RE 但未含 negative correlation 数字。论文各处 RE 标注不一致：有些写 preliminary，有些不写。'\n  action_items:\n  - round: 5\n    action: 所有 RE 分析处一致标注 single-benchmark preliminary\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: Discussion/Conclusion 中每次引用 RE 结论时一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 全文 RE 引用一致标注 (preliminary, single benchmark)；考虑从 abstract 移除 RE 具体数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W2\n  summary: SJ vs EM 优势叙事应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: SJ vs EM Δρ=+0.065, Bonferroni 下不显著\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage，改为 difficulty-dependent complementarity\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 5: §4.2 已用 complementarity 措辞'\n  resolution_round: 5\n- id: R4-W3\n  summary: Abstract 过于密集，超长句子需拆分\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: 多层嵌套括号和分号的超长句子\n  - round: 5\n    reviewers: [1, 2]\n    note: 仍未修改\n  - round: 6\n    reviewers: [1, 2]\n    note: 第 3 轮仍未解决。共识：减少具体数字，abstract 聚焦问题-发现-意义三段式\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R2-W1 再次提出。R1 agree。Abstract 仍含 5 signal family 名称、3 datasets、2 models、4 metrics + gap 概念。共识：精简为问题-发现-意义三段式，将具体信号名和数字移到 Introduction。'\n  action_items:\n  - round: 5\n    action: Abstract 拆分为 2-3 句核心 claim\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: Abstract 精简为问题-发现-意义三段式\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: Abstract 精简为问题-发现-意义三段式，移除大部分具体数字和信号名到 Introduction\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: 系统评估 LLM 置信度获取方法\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work §2 已引用 Xiong et al.\n  action_items:\n  - round: 4\n    action: Related Work 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 5: 已引用'\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: max(|g_i|,|g_j|) vs |g_i∪g_j| 未比较\n  action_items:\n  - round: 4\n    action: 附录补 union normalizer 结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已在 method.tex 有理由，超出 scope\n  resolution_round: 4\n- id: R4-M2\n  summary: TOST δ 选择（±2/3/5 pp）缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: δ 选择直接影响等价结论\n  - round: 5\n    reviewers: [1, 2]\n    note: R1 再提：与 IAA 关联无引用。R2 认为多水平 δ 已构成 sensitivity analysis。\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 升级为 must-fix。R2 agree。建议报告 breakpoint δ*。\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-W3 再次提出：δ 循环锚定于 oracle headroom（δ=5pp = forgoing 28-38% of headroom），但 oracle headroom 正是被调查量，构成循环论证。R2 agree。建议用外部标准（IAA 变异、deployment threshold）或更突出 breakpoint δ*。'\n  action_items:\n  - round: 5\n    action: 引用 IE benchmark IAA 数据来锚定 δ 选择\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 报告 breakpoint δ*；强化 effect size + bootstrap CI\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 用外部标准（SESOI 框架或 deployment F1 threshold）替代 oracle headroom 锚定；将 breakpoint δ* 和 Cohen's d + CI 作为主要证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-M3\n  summary: Table 1 N=16 block 大面积空白\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 4\n    reviewers: [1, 2]\n    note: N=16 仅填 LLaMA CoNLL，SciERC 空白\n  - round: 5\n    reviewers: [1, 2]\n    note: 已加脚注但格式可能异常\n  - round: 6\n    reviewers: [1, 2]\n    note: 仍建议将 N=16 行移入 Appendix Table 3\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文当前 Table 1 仅含 N=8，N=16 在脚注引向 Appendix。可能已修复，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行，合并到 Appendix Table 3\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: 三个增量均偏弱\n  - round: 6\n    reviewers: [1, 2]\n    note: R2 再提。共识：增量贡献存在但论文过度强调\n  - round: 7\n    reviewers: []\n    note: 本轮未直接提及。R2-N1 的 reframing 要求间接涵盖此问题——如果核心贡献 reframe 为 LP compression + MBR failure（而非 gap 本身），Nédellec 增量问题将自然缓解。\n  action_items:\n  - round: 5\n    action: 更诚实地量化增量大小\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致（SciERC vs CoNLL/WNUT）\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: SciERC 未显式禁用 enable_thinking\n  - round: 6\n    reviewers: [1, 2]\n    note: 两位 Reviewer 再次独立提出。共识：在 Experiments Setup 中 prominently 声明\n  - round: 7\n    reviewers: []\n    note: 本轮未提及为 issue。论文 §4.1 现已显式声明 thinking token confound（3 句话），Limitations 中也有讨论。R1 Reproducibility 评 3.5/5 未提及此问题。可能已充分解决，待 Research Director 确认。\n  action_items:\n  - round: 5\n    action: Limitations 讨论此不一致性\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: Experiments Setup §4.1 中显著声明\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: R1 建议删除或缩短；R2 认为意图合理但执行可能误导\n  - round: 6\n    reviewers: [1, 2]\n    note: 共识：缩短脚注，去掉具体数字\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文脚注已缩短为 comparable AUROC on discrete-answer QA 并加 cross-task caveat。可能已修复，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: 缩短脚注，保留 comparable AUROC 但去掉具体数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W3\n  summary: he2024uncertainty bib entry 与引用上下文不匹配\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1]\n    note: bib 标题是 sequential labeling 论文，但引用上下文是 LLM UQ survey\n  - round: 7\n    reviewers: []\n    note: 本轮 R1 验证 62 篇引用全部通过，未再提及此问题。可能已修正，待 Research Director 确认。\n  action_items:\n  - round: 5\n    action: 修正引用上下文描述\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling verification survey 引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 建议补 verification survey\n  - round: 6\n    reviewers: [1, 2]\n    note: R2 具体指出 Zhang et al. (2025) TTS survey。共识 should-fix。\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文 Related Work 已引用 zhang2025tts (test-time scaling)。R1 验证引用完整。可能已修复，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: Related Work §2 补充 Zhang et al. (2025) TTS survey 引用\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Discussion §5 将方法与 MBR 对接但只引用 MT 领域\n  - round: 6\n    reviewers: [1, 2]\n    note: R2 具体指出 Eikema et al. (EMNLP 2025)\n  - round: 7\n    reviewers: [2]\n    note: 'R2-W6 再次提出（rebrand）：Eikema et al. (2025) structure-conditional MBR 仅在 Discussion 出现，应在 Related Work 中定位。R1 agree。论文 Discussion 已引用 eikema2025structured，但应前移到 Related Work §2 的 MBR 段落。'\n  action_items:\n  - round: 6\n    action: Discussion §5 MBR 段补充 Eikema et al.\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: 将 eikema2025structured 的讨论从 Discussion 前移到 Related Work §2 MBR 段落\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M3\n  summary: Consensus-proximity = LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §3.3 声称数学等价但未给出推导\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含完整等价性证明\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 已包含完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到或 author name 有 variant\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: hobelsberger2025systematic, lightman2024verify 未找到\n  - round: 6\n    reviewers: [1, 2]\n    note: snell2024scaling key 标 2024 但 venue 为 ICLR 2025\n  - round: 7\n    reviewers: []\n    note: 'R1 Round 7 验证 62 篇引用全部通过（56 online verified, 3 not found = recent preprints, 3 mismatch = encoding false positives）。R2 同样报告 0 orphan, 0 missing, 3 not found (normal)。未再提及具体 bib 问题。可能已修正或属于正常范围。'\n  action_items:\n  - round: 6\n    action: 核实 ye2025uncertainty, snell2024scaling, feng2025optimal, hobelsberger2025systematic\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句，内容偏简\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: 格式合规但内容偏简\n  - round: 6\n    reviewers: [2]\n    note: 应注明 CoNLL-2003 Reuters license 限制\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文 Ethics Statement 现已包含 CoNLL-2003 Reuters RCV1 corpus 和 NIST agreement 说明。可能已充分解决，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: Ethics Statement 补充 CoNLL-2003 Reuters license 注明\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C1\n  summary: Constrained decoding 混淆变量未隔离，claim scope 与 evidence 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Title/Abstract/Conclusion 需限定 constrained decoding scope\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并追踪\n  action_items:\n  - round: 5\n    action: Title 加 under Constrained Decoding\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: 见 R3-C1 Round 6 action\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: 与 R3-C1 合并。exp-018 free-form ablation 证明 gap task-intrinsic。D075。\n  resolution_round: 7\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: 4/5 instance-level failure = tautological\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。共识：重构叙事以 logprob compression + MBR failure 为中心。\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并。Round 7 fresh review 两位 Reviewer 独立再次提出。见 R3-W2 Round 7 mention。\n  action_items:\n  - round: 5\n    action: Reframe C2 聚焦 logprob compression + MBR failure\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 见 R3-W2 Round 6 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: '''First multi-family comparison'' claim = scope engineering'\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: 建议改为描述性表述\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-W6 合并追踪\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。Round 7 R1 rebut 论文当前版本未含 first claim。见 R3-W6 Round 7 mention。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 见 R3-W6 Round 6 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W5\n  summary: '''Cross-architecture'' 用词过度（两个 8B decoder-only）'\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: 改为 across two model families at 8B scale\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并。Round 7 R2-N2 升级为 critical（标题 scope）。见 R3-W5 Round 7 mention。\n  action_items:\n  - round: 5\n    action: 全文替换 cross-architecture\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 见 R3-W5 Round 6 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Excess agreement 未注明 configuration\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并。见 R3-W4 Round 7 mention。\n  action_items:\n  - round: 5\n    action: 补 configuration 信息 + 引用文献\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 6\n    action: 见 R3-W4 Round 6 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限，core structural signal 过度宣传\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: R2 认为标准技术组合\n  - round: 7\n    reviewers: []\n    note: 本轮未直接提及。R2 Round 7 未在独立审稿中重新提出 SJ novelty 问题。可能已通过 complementarity 措辞缓解，待 Research Director 确认。\n  action_items:\n  - round: 5\n    action: core structural signal → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关 (ρ=-0.410) 机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: capability boundary 下 logprob 反映 fluency 而非 accuracy\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: §4 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设，引用 Xiong et al.\n  resolution_round: 6\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致：无阈值 vs majority threshold\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Equation 6 定义为所有 entity 平均频率（无阈值），但 Footnote 2 承认实现使用 majority threshold (>N/2)。两者数学上不等价。\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-W2 再次提出：VC 在 QE（Eq.6 连续）和 selection（majority threshold）中使用不同计算，但 Table 3 标注不清。Footnote 2 报告了 ρ 差异（threshold ρ=0.252 vs Eq.6 ρ=0.379），但表格未标明使用的是哪种实现。R2 agree（通过 W2 response）。'\n  action_items:\n  - round: 6\n    action: 统一公式和实现；报告两种实现的 ρ 差值；明确 Table 1 使用哪种实现\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 7\n    action: Table 3 caption 或脚注明确标注 VC selection 使用 majority threshold（非 Eq.6 连续值）；保持 QE 和 selection 的分离但标注更清晰\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W2\n  summary: Figure 1 caption 冗余——重复 Section 4.2/4.3 内容\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Figure 1 caption 引入 p=0.39、Table 2 引用等与正文重复\n  - round: 7\n    reviewers: []\n    note: 本轮未提及。论文 Figure 1 caption 当前仅含核心信息（Left/Right 描述）。可能已精简，待 Research Director 确认。\n  action_items:\n  - round: 6\n    action: 精简 Figure 1 caption\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证——核心 headline finding 仅 single seed\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-N1: 核心 selection failure（LP NER +0.6pp, p=0.39, Table 3）仅使用 seed=42。3-seed 分析（Table 10）仅覆盖 QE 而非 selection F1。p=0.39 来自单种子不足以支撑论文 headline finding。R2 agree 并补充：Table 6 中 LLaMA CoNLL SJ Δ_best=+1.0pp 在换种子后可能越过 significance。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3（selection F1），报告跨种子 selection F1 mean±σ 和 p-value range\n    assigned_to: Agent + Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 \"effectively tied\" 阈值缺乏论证——abstract 数字依赖 arbitrary cutoff\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-N2: Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59× 跳变），说明阈值处于分布陡峭区域。\"60% effectively tied\" 出现在 abstract 中但 0.05 的依据未给出。R2 agree（abstract 数字高度依赖 arbitrary cutoff）。建议提供 LP range 完整 CDF 或用连续度量（within-instance LP-F1 correlation）替代二元划分。'\n  action_items:\n  - round: 7\n    action: (a) 提供 LP range 完整 CDF 图或表；(b) 论证 ε=0.05 的选择依据或改用连续度量；(c) abstract 中避免依赖单一 arbitrary cutoff 的数字\n    assigned_to: Agent + Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑了过强的泛化声称\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-N3: 1 dataset × 1 model × 1 seed 的 ablation 支撑了 \"fundamental challenge\" 和 \"intrinsic to the model and task\" 声称。RE LP selection 在 free-form 下翻转（−0.68pp→+1.69pp, Table 14 Panel B），部分反驳 \"not an artifact of decoding strategy\"。R2 agree 但补充 NER compression 在 free-form 下持续存在。共识：NER 结论可保留但需降级措辞；RE 翻转必须明确承认。'\n  action_items:\n  - round: 7\n    action: (a) 降级 \"fundamental\"/\"intrinsic\" 为 \"observed in our NER setting\"；(b) 明确承认 RE LP selection 在 free-form 下的翻转；(c) 区分 NER（compression 持续）和 RE（翻转）的 ablation 结论\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失——核心诊断对象无 T=0.7 数据\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R1-W4 + R2-W4: LP 是论文核心诊断对象（score compression, per-sample discrimination），但被排除在温度比较（T=0.7 vs T=1.0）之外。Limitations 提到但未解释为何缺失。score compression 可能是 T-dependent（T=0.7 下 logit 分布更集中可能加剧或缓解 compression），而温度正是影响 LP 分布的关键参数。两位 Reviewer 均列 warning。'\n  action_items:\n  - round: 7\n    action: (a) 补充 T=0.7 LP 数据（如可获得）；(b) 如数据不可获得，在 Limitations 中更充分讨论 LP 温度敏感性未知的影响\n    assigned_to: Agent + Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 (evaluation framework) 定性有分歧——engineering benchmark vs methodological contribution\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R2-W3 认为 Contribution 1 本质是 engineering benchmark 而非 methodological contribution，应降级。R1 rebut：核心是三个 metrics 的 decouple（ρ-AUROC dissociation, EM leads AUROC=0.749 but ranks third in ρ=0.295）有实践意义。但 R1 同意 \"contribution\" framing 可能 overstate，\"finding\" 更准确。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 \"contribution\" 降级为 \"setup/methodology\"，以 ρ-AUROC dissociation 作为 secondary finding\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) structure-conditional MBR 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 'R2-W6: eikema2025structured 仅在 Discussion 出现（§5 MBR decoding 连接段），应在 Related Work §2 的 MBR 段落中定位以建立 prior awareness。R1 agree。与 R5-M2 合并追踪——R5-M2 要求补引用（已完成），R7-W3 要求调整引用位置。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 的引用从 Discussion 前移（或同时在）Related Work §2 MBR 段\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 740 · 2026-05-15T12:35:42.684723+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 51846}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 409
}
```

</details>

---


### Tool call

_source line 741 · 2026-05-15T12:37:15.039914+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "report": "# Consolidated Review Report — Round 7\n\n**Paper**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**Reviewers**: 2 (R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性 + 写作质量)\n**Rounds**: 1 (converged after cross-sharing; all critical issues consensual)\n\n---\n\n## Summary\n\nThe paper investigates whether confidence signals can identify the best output among multiple LLM-generated candidates for structured IE tasks (NER, RE). It compares five signals from three families—structural (VC, SJ), surface (EM, FK), and model-internal (LP)—across three benchmarks with two 8B-parameter model families. The central finding is the \"correlation-selection gap\": signals achieve strong quality estimation (ρ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13–18 pp oracle headroom. A free-form decoding ablation suggests LP score compression is intrinsic rather than a constrained decoding artifact.\n\nThe experimental work is extensive and the conceptual distinction between quality estimation and sample selection has genuine value. However, the core contribution framing conflates definitional limitations with empirical findings, key statistical analyses lack multi-seed validation, and the paper's broadest claims (title, abstract) exceed the evidence scope.\n\n---\n\n## Strengths\n\n1. **Conceptual clarity**: The quality estimation vs. sample selection distinction is well-articulated and has practical implications for IE deployment and test-time scaling.\n\n2. **Experimental breadth**: 5 signals × 3 datasets × 2 models with comprehensive ablations (temperature, sample size, free-form decoding, multi-seed QE, diversity stratification, calibration analysis).\n\n3. **Statistical rigor in QE**: Bootstrap CIs (B=10,000), TOST equivalence testing, Bonferroni corrections, 3-seed stability analysis—the quality estimation analysis meets high statistical standards.\n\n4. **Honest hedging**: RE results consistently marked \"preliminary, single benchmark\" in most locations; Limitations section is thorough and self-aware (7 paragraphs covering scope, scale, ablation limitations).\n\n5. **MBR connection**: Linking consensus-proximity selection to MBR decoding and diagnosing why MBR fails (utility correlates across but not within instances) is insightful and connects to a mature literature. The Eikema et al. (2025) structure-conditional MBR finding corroborates this.\n\n6. **Appendix depth**: 12 supplementary sections with per-relation diagnostics, diversity stratification, LP failure stability analysis, LOO-SJ equivalence proof, calibration reliability diagrams.\n\n7. **Citation integrity**: Both reviewers independently verified all 62 bib entries; 56 confirmed via OpenAlex, no fabricated citations detected.\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix) — 5 issues, all consensual\n\n**C1. Gap framing conflates definitional and empirical contributions** [Consensus]\nAbstract and Introduction present the correlation-selection gap as a unified empirical discovery, but §5 explicitly acknowledges that 4/5 signals fail at selection \"by construction\" (Layer 1: definitional). The actual empirical contributions are narrower: (a) LP score compression diagnosis (60% instances with range < 0.05), (b) MBR utility-quality misalignment at per-sample level, (c) non-tied subset analysis showing LP becomes significant when compression is mitigated (+2.9 pp, p=0.01). **Action**: Reframe Abstract/Introduction/Contribution 2 — dismiss instance-level failure in one sentence (definitional), then center LP compression + MBR failure as core empirical findings.\n\n**C2. Selection gap lacks multi-seed validation** [Consensus]\nThe headline finding (LP NER +0.6 pp, p=0.39; Table 3) uses seed=42 only. The 3-seed analysis (Table 10) covers QE metrics but not selection F1. A p=0.39 from a single seed is insufficient to support the paper's central claim. **Action**: Extend 3-seed analysis to Table 3 selection F1; report cross-seed mean±σ and p-value range.\n\n**C3. ε=0.05 \"effectively tied\" threshold lacks justification** [Consensus]\nTable 12 shows a 59× jump from ε=0.01 (1.1%) to ε=0.05 (60.3%), indicating the threshold sits on a steep distribution cliff. \"60% of instances effectively tied\" appears in the abstract but the 0.05 cutoff has no stated basis. **Action**: Provide LP range CDF; justify ε or replace with continuous measure (within-instance LP-F1 correlation).\n\n**C4. Free-form ablation scope too narrow for claims** [Consensus]\n1 dataset × 1 model × 1 seed supports \"fundamental challenge\" and \"intrinsic to the model and task.\" RE LP selection flips from −0.68 pp (constrained) to +1.69 pp (free-form, Table 14 Panel B), partially contradicting \"not an artifact of decoding strategy.\" NER compression persists. **Action**: Downgrade \"fundamental/intrinsic\" to \"observed in our NER setting\"; explicitly acknowledge RE reversal; differentiate NER and RE ablation conclusions.\n\n**C5. Title \"Do Not Scale\" exceeds evidence scope** [Consensus]\nBoth models are 8B parameters. The paper's own findings show task difficulty × model capability interaction effects, but only one scale point is tested. The title implies a universal negative result. **Action**: Scope title to \"at 8B Scale\" or equivalent qualification.\n\n### Warning (Should-Fix) — 8 issues\n\n**W1. RE conclusions inconsistently qualified** [Consensus]\nRE analysis uses SciERC alone (preliminary). Abstract and some Discussion passages reference RE results without consistent \"preliminary, single benchmark\" qualification. R1 corrected R2's factual error (LP negative correlation ρ=−0.410 is WNUT-17 NER, not RE) but agrees with the underlying concern. **Action**: All RE citations carry \"(preliminary, single benchmark)\" consistently.\n\n**W2. Abstract information density too high** [Consensus]\nAbstract packs 5 signal families, 3 datasets, 2 models, 4 metrics, and the gap concept into ~8 sentences. **Action**: Simplify to problem-finding-implication three-paragraph structure; move specific signal names and numbers to Introduction.\n\n**W3. FK independence test near-zero power** [Consensus]\nOne-sample t-test over n=5 configurations has essentially no statistical power. **Action**: Add permutation test/bootstrap CI, or acknowledge the limitation explicitly.\n\n**W4. VC formula-implementation inconsistency** [Consensus]\nEq. 6 defines continuous QE signal; selection uses majority threshold (>N/2). Table 3 doesn't clarify which. Footnote reports ρ difference (0.252 vs 0.379) but table labeling is ambiguous. **Action**: Clearly label both variants in table captions.\n\n**W5. TOST δ circularly anchored** [Consensus]\nδ values anchored to oracle headroom, but oracle headroom is the quantity under investigation. **Action**: Use external standard (IAA variation, deployment threshold) or prominently report breakpoint δ*.\n\n**W6. LP temperature sensitivity missing** [Consensus]\nLP—the paper's primary diagnostic target—excluded from temperature comparison (T=0.7 vs T=1.0). Score compression may be temperature-dependent. **Action**: Obtain T=0.7 LP data or discuss this gap more prominently in Limitations.\n\n**W7. Eikema et al. (2025) positioning** [Consensus]\nStructure-conditional MBR paper cited only in Discussion; should also appear in Related Work §2 MBR paragraph. **Action**: Add reference in Related Work.\n\n**W8. Contribution 1 framing** [Divergence]\nR2: evaluation framework is engineering benchmark, not contribution. R1: ρ-AUROC dissociation finding has genuine value, but agrees \"finding\" is more accurate than \"contribution.\" **Action**: Consider presenting as methodology/setup with dissociation as secondary finding.\n\n### Minor — 1 issue\n\n**M1. Conditional filtering** [Divergence]\nR2: excluding zero-F1 instances introduces selection bias. R1: methodologically necessary to separate binary detection from quality gradation (Table 5 confirms). **Action**: Brief discussion of what filtering controls and doesn't.\n\n---\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | Status |\n|-------|----|----|--------|\n| C1 (definitional reframing) | AGREE | Raised | Consensus |\n| C2 (multi-seed selection) | Raised | AGREE | Consensus |\n| C3 (ε threshold) | Raised | AGREE | Consensus |\n| C4 (ablation scope) | Raised | AGREE | Consensus |\n| C5 (title scope) | AGREE | Raised | Consensus |\n| W1–W7 | Various | Various | Consensus |\n| W8 (Contribution 1) | Partial REBUT | Raised | Divergence recorded |\n| M1 (conditional filtering) | REBUT | Raised | Divergence recorded |\n\n---\n\n## Reviewer Divergence Detail\n\n**W8**: R1 argues Contribution 1's core is the ρ-AUROC dissociation finding (EM leads AUROC=0.749 but ranks third in ρ=0.295), which has genuine practical value. R2 argues the evaluation framework is an engineering benchmark. Both agree \"contribution\" may overstate; \"finding\" is more accurate.\n\n**M1**: R1 argues conditional filtering is a standard methodological step to separate binary detection from quality gradation, supported by Table 5 (full-set ρ=0.724 entirely boundary-driven). R2 argues excluding the hardest instances introduces selection bias. R1's position is stronger—the paper's claim structure requires this decomposition.\n\n---\n\n## Questions for Authors\n\n1. Can you provide multi-seed selection F1 (mean±σ, p-value range) for at least SciERC NER LP?\n2. What is the justification for ε=0.05 as the tied/non-tied boundary? Can you show the full CDF?\n3. How do you reconcile the RE LP selection reversal under free-form decoding with the \"intrinsic compression\" claim?\n4. Would you consider scoping the title to include \"at 8B Scale\"?\n5. Can LP temperature data (T=0.7) be obtained, or is this a permanent data gap?\n\n---\n\n## Missing References\n\nNone identified. Both reviewers independently verified all 62 bib entries (56 OpenAlex-confirmed, 3 recent preprints not indexed, 3 encoding-related false positive mismatches). No fabricated or orphan citations.\n\n---\n\n## External Review\n\nExternal review not configured (paperreview_ai.enabled not set). Status: not_requested.\n\n---\n\n## Overall Assessment\n\n**Score: Borderline**\n\nThe paper identifies a real and practically important phenomenon (quality estimation ≠ sample selection for structured IE) and provides extensive experimental evidence. The conceptual distinction has genuine community value, and the diagnostic analysis (LP compression, MBR failure, non-tied subset) contains non-trivial empirical findings.\n\nHowever, the core framing issue (C1) is fundamental: readers are led to believe all five signals empirically fail, when four fail by mathematical construction. The actual empirical contribution is narrower but genuinely interesting. The statistical gaps (C2: single-seed selection, C3: unjustified ε threshold), scope-evidence mismatch (C4-C5: \"fundamental\"/\"Do Not Scale\" from narrow ablation and 8B-only experiments), and persistent writing issues (W2: abstract density, W4: VC labeling) compound the framing problem.\n\nWith reframing (C1), multi-seed selection data (C2), ε justification (C3), claim scope corrections (C4-C5), and writing fixes (W1-W8), this would be a solid EMNLP Findings paper. The current version is not ready for main conference acceptance.\n\n**Confidence: 4/5** (both reviewers independently assessed; thorough reading including all appendices)\n\n---\n\n## Scores Summary\n\n| Dimension | R1 | R2 | Consensus |\n|-----------|----|----|-----------|\n| Soundness | 3/5 | 3/5 | 3/5 |\n| Excitement | 3.5/5 | 3/5 | 3/5 |\n| Overall | 3/5 | 3/5 | 3/5 (Borderline) |\n| Confidence | 4/5 | 4/5 | 4/5 |\n| Reproducibility | 3.5/5 | — | 3.5/5 |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "report": "# Consolidated Review Report — Round 7\n\n**Paper**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**Reviewers**: 2 (R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性 + 写作质量)\n**Rounds**: 1 (converged after cross-sharing; all critical issues consensual)\n\n---\n\n## Summary\n\nThe paper investigates whether confidence signals can identify the best output among multiple LLM-generated candidates for structured IE tasks (NER, RE). It compares five signals from three families—structural (VC, SJ), surface (EM, FK), and model-internal (LP)—across three benchmarks with two 8B-parameter model families. The central finding is the \"correlation-selection gap\": signals achieve strong quality estimation (ρ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13–18 pp oracle headroom. A free-form decoding ablation suggests LP score compression is intrinsic rather than a constrained decoding artifact.\n\nThe experimental work is extensive and the conceptual distinction between quality estimation and sample selection has genuine value. However, the core contribution framing conflates definitional limitations with empirical findings, key statistical analyses lack multi-seed validation, and the paper's broadest claims (title, abstract) exceed the evidence scope.\n\n---\n\n## Strengths\n\n1. **Conceptual clarity**: The quality estimation vs. sample selection distinction is well-articulated and has practical implications for IE deployment and test-time scaling.\n\n2. **Experimental breadth**: 5 signals × 3 datasets × 2 models with comprehensive ablations (temperature, sample size, free-form decoding, multi-seed QE, diversity stratification, calibration analysis).\n\n3. **Statistical rigor in QE**: Bootstrap CIs (B=10,000), TOST equivalence testing, Bonferroni corrections, 3-seed stability analysis—the quality estimation analysis meets high statistical standards.\n\n4. **Honest hedging**: RE results consistently marked \"preliminary, single benchmark\" in most locations; Limitations section is thorough and self-aware (7 paragraphs covering scope, scale, ablation limitations).\n\n5. **MBR connection**: Linking consensus-proximity selection to MBR decoding and diagnosing why MBR fails (utility correlates across but not within instances) is insightful and connects to a mature literature. The Eikema et al. (2025) structure-conditional MBR finding corroborates this.\n\n6. **Appendix depth**: 12 supplementary sections with per-relation diagnostics, diversity stratification, LP failure stability analysis, LOO-SJ equivalence proof, calibration reliability diagrams.\n\n7. **Citation integrity**: Both reviewers independently verified all 62 bib entries; 56 confirmed via OpenAlex, no fabricated citations detected.\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix) — 5 issues, all consensual\n\n**C1. Gap framing conflates definitional and empirical contributions** [Consensus]\nAbstract and Introduction present the correlation-selection gap as a unified empirical discovery, but §5 explicitly acknowledges that 4/5 signals fail at selection \"by construction\" (Layer 1: definitional). The actual empirical contributions are narrower: (a) LP score compression diagnosis (60% instances with range < 0.05), (b) MBR utility-quality misalignment at per-sample level, (c) non-tied subset analysis showing LP becomes significant when compression is mitigated (+2.9 pp, p=0.01). **Action**: Reframe Abstract/Introduction/Contribution 2 — dismiss instance-level failure in one sentence (definitional), then center LP compression + MBR failure as core empirical findings.\n\n**C2. Selection gap lacks multi-seed validation** [Consensus]\nThe headline finding (LP NER +0.6 pp, p=0.39; Table 3) uses seed=42 only. The 3-seed analysis (Table 10) covers QE metrics but not selection F1. A p=0.39 from a single seed is insufficient to support the paper's central claim. **Action**: Extend 3-seed analysis to Table 3 selection F1; report cross-seed mean±σ and p-value range.\n\n**C3. ε=0.05 \"effectively tied\" threshold lacks justification** [Consensus]\nTable 12 shows a 59× jump from ε=0.01 (1.1%) to ε=0.05 (60.3%), indicating the threshold sits on a steep distribution cliff. \"60% of instances effectively tied\" appears in the abstract but the 0.05 cutoff has no stated basis. **Action**: Provide LP range CDF; justify ε or replace with continuous measure (within-instance LP-F1 correlation).\n\n**C4. Free-form ablation scope too narrow for claims** [Consensus]\n1 dataset × 1 model × 1 seed supports \"fundamental challenge\" and \"intrinsic to the model and task.\" RE LP selection flips from −0.68 pp (constrained) to +1.69 pp (free-form, Table 14 Panel B), partially contradicting \"not an artifact of decoding strategy.\" NER compression persists. **Action**: Downgrade \"fundamental/intrinsic\" to \"observed in our NER setting\"; explicitly acknowledge RE reversal; differentiate NER and RE ablation conclusions.\n\n**C5. Title \"Do Not Scale\" exceeds evidence scope** [Consensus]\nBoth models are 8B parameters. The paper's own findings show task difficulty × model capability interaction effects, but only one scale point is tested. The title implies a universal negative result. **Action**: Scope title to \"at 8B Scale\" or equivalent qualification.\n\n### Warning (Should-Fix) — 8 issues\n\n**W1. RE conclusions inconsistently qualified** [Consensus]\nRE analysis uses SciERC alone (preliminary). Abstract and some Discussion passages reference RE results without consistent \"preliminary, single benchmark\" qualification. R1 corrected R2's factual error (LP negative correlation ρ=−0.410 is WNUT-17 NER, not RE) but agrees with the underlying concern. **Action**: All RE citations carry \"(preliminary, single benchmark)\" consistently.\n\n**W2. Abstract information density too high** [Consensus]\nAbstract packs 5 signal families, 3 datasets, 2 models, 4 metrics, and the gap concept into ~8 sentences. **Action**: Simplify to problem-finding-implication three-paragraph structure; move specific signal names and numbers to Introduction.\n\n**W3. FK independence test near-zero power** [Consensus]\nOne-sample t-test over n=5 configurations has essentially no statistical power. **Action**: Add permutation test/bootstrap CI, or acknowledge the limitation explicitly.\n\n**W4. VC formula-implementation inconsistency** [Consensus]\nEq. 6 defines continuous QE signal; selection uses majority threshold (>N/2). Table 3 doesn't clarify which. Footnote reports ρ difference (0.252 vs 0.379) but table labeling is ambiguous. **Action**: Clearly label both variants in table captions.\n\n**W5. TOST δ circularly anchored** [Consensus]\nδ values anchored to oracle headroom, but oracle headroom is the quantity under investigation. **Action**: Use external standard (IAA variation, deployment threshold) or prominently report breakpoint δ*.\n\n**W6. LP temperature sensitivity missing** [Consensus]\nLP—the paper's primary diagnostic target—excluded from temperature comparison (T=0.7 vs T=1.0). Score compression may be temperature-dependent. **Action**: Obtain T=0.7 LP data or discuss this gap more prominently in Limitations.\n\n**W7. Eikema et al. (2025) positioning** [Consensus]\nStructure-conditional MBR paper cited only in Discussion; should also appear in Related Work §2 MBR paragraph. **Action**: Add reference in Related Work.\n\n**W8. Contribution 1 framing** [Divergence]\nR2: evaluation framework is engineering benchmark, not contribution. R1: ρ-AUROC dissociation finding has genuine value, but agrees \"finding\" is more accurate than \"contribution.\" **Action**: Consider presenting as methodology/setup with dissociation as secondary finding.\n\n### Minor — 1 issue\n\n**M1. Conditional filtering** [Divergence]\nR2: excluding zero-F1 instances introduces selection bias. R1: methodologically necessary to separate binary detection from quality gradation (Table 5 confirms). **Action**: Brief discussion of what filtering controls and doesn't.\n\n---\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | Status |\n|-------|----|----|--------|\n| C1 (definitional reframing) | AGREE | Raised | Consensus |\n| C2 (multi-seed selection) | Raised | AGREE | Consensus |\n| C3 (ε threshold) | Raised | AGREE | Consensus |\n| C4 (ablation scope) | Raised | AGREE | Consensus |\n| C5 (title scope) | AGREE | Raised | Consensus |\n| W1–W7 | Various | Various | Consensus |\n| W8 (Contribution 1) | Partial REBUT | Raised | Divergence recorded |\n| M1 (conditional filtering) | REBUT | Raised | Divergence recorded |\n\n---\n\n## Reviewer Divergence Detail\n\n**W8**: R1 argues Contribution 1's core is the ρ-AUROC dissociation finding (EM leads AUROC=0.749 but ranks third in ρ=0.295), which has genuine practical value. R2 argues the evaluation framework is an engineering benchmark. Both agree \"contribution\" may overstate; \"finding\" is more accurate.\n\n**M1**: R1 argues conditional filtering is a standard methodological step to separate binary detection from quality gradation, supported by Table 5 (full-set ρ=0.724 entirely boundary-driven). R2 argues excluding the hardest instances introduces selection bias. R1's position is stronger—the paper's claim structure requires this decomposition.\n\n---\n\n## Questions for Authors\n\n1. Can you provide multi-seed selection F1 (mean±σ, p-value range) for at least SciERC NER LP?\n2. What is the justification for ε=0.05 as the tied/non-tied boundary? Can you show the full CDF?\n3. How do you reconcile the RE LP selection reversal under free-form decoding with the \"intrinsic compression\" claim?\n4. Would you consider scoping the title to include \"at 8B Scale\"?\n5. Can LP temperature data (T=0.7) be obtained, or is this a permanent data gap?\n\n---\n\n## Missing References\n\nNone identified. Both reviewers independently verified all 62 bib entries (56 OpenAlex-confirmed, 3 recent preprints not indexed, 3 encoding-related false positive mismatches). No fabricated or orphan citations.\n\n---\n\n## External Review\n\nExternal review not configured (paperreview_ai.enabled not set). Status: not_requested.\n\n---\n\n## Overall Assessment\n\n**Score: Borderline**\n\nThe paper identifies a real and practically important phenomenon (quality estimation ≠ sample selection for structured IE) and provides extensive experimental evidence. The conceptual distinction has genuine community value, and the diagnostic analysis (LP compression, MBR failure, non-tied subset) contains non-trivial empirical findings.\n\nHowever, the core framing issue (C1) is fundamental: readers are led to believe all five signals empirically fail, when four fail by mathematical construction. The actual empirical contribution is narrower but genuinely interesting. The statistical gaps (C2: single-seed selection, C3: unjustified ε threshold), scope-evidence mismatch (C4-C5: \"fundamental\"/\"Do Not Scale\" from narrow ablation and 8B-only experiments), and persistent writing issues (W2: abstract density, W4: VC labeling) compound the framing problem.\n\nWith reframing (C1), multi-seed selection data (C2), ε justification (C3), claim scope corrections (C4-C5), and writing fixes (W1-W8), this would be a solid EMNLP Findings paper. The current version is not ready for main conference acceptance.\n\n**Confidence: 4/5** (both reviewers independently assessed; thorough reading including all appendices)\n\n---\n\n## Scores Summary\n\n| Dimension | R1 | R2 | Consensus |\n|-----------|----|----|-----------|\n| Soundness | 3/5 | 3/5 | 3/5 |\n| Excitement | 3.5/5 | 3/5 | 3/5 |\n| Overall | 3/5 | 3/5 | 3/5 (Borderline) |\n| Confidence | 4/5 | 4/5 | 4/5 |\n| Reproducibility | 3.5/5 | — | 3.5/5 |\n"
  }
}
```

</details>

---


### Tool result

_source line 742 · 2026-05-15T12:37:19.296689+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4256
}
```

</details>

---


### Assistant

_source line 743 · 2026-05-15T12:37:32.481658+00:00_

---

**Round 7 审稿完成。**

汇总：

- **评分**：Borderline (3/5)，建议 Findings track
- **5 个 Critical（全部共识）**：
  1. Gap framing 混淆 definitional 与 empirical（需根本性 reframe）
  2. Selection gap 缺多种子验证（p=0.39 仅 single seed）
  3. ε=0.05 阈值无论证（abstract "60%" 依赖 arbitrary cutoff）
  4. Free-form ablation 过窄但声称 "fundamental"（RE 翻转未承认）
  5. 标题 "Do Not Scale" 超出 8B-only 证据范围
- **8 个 Warning**：RE 标注不一致、Abstract 密度、FK 统计功效、VC 标注、TOST δ 循环锚定、LP 温度缺失、Eikema 定位、Contribution 1 定性
- **分歧**：Contribution 1 是否为 contribution（R1 认为有价值，R2 认为应降级）；conditional filtering 是否引入 bias（R1 否认，R2 认为需讨论）

审稿报告已投递 Research Director，Issue Tracker 已同步更新（新增 3 个 open issue，更新 15+ 个 existing issue 的 Round 7 mention）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 64

## Round 64

2 recorded events


### User

_source line 744 · 2026-05-15T12:37:35.091859+00:00_

[Reviewer 2 审稿结果]:
交叉回应完成并已提交。对 Reviewer 1 的 8 条意见全部 [AGREE]，两份审稿在 selection evidence quality、RE 证据不足、LP temperature 缺口三个方向上高度一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 745 · 2026-05-15T12:37:46.981582+00:00_

Round 7 审稿已全部完成。

**汇总**：

- 2 位 Reviewer 独立初审 → 交叉分享 → 1 轮收敛
- **Overall: Borderline (3/5)**，建议 Findings track
- **5 个 Critical** 全部达成共识：(1) gap framing 需 reframe definitional vs empirical；(2) selection gap 需多种子验证；(3) ε=0.05 阈值需论证；(4) free-form ablation 范围过窄但声称过强；(5) 标题 "Do Not Scale" 超出 8B-only 证据范围
- **8 个 Warning**、**1 个 Minor** 分歧已记录
- Issue Tracker 已同步更新（3 个新 critical issue + 现有 issue Round 7 mentions）
- 审稿报告已投递给 Research Director

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 65

## Round 65

76 recorded events


### User

_source line 746 · 2026-05-15T14:54:02.897677+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: findings
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 747 · 2026-05-15T14:54:09.164948+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 748 · 2026-05-15T14:54:09.166118+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 749 · 2026-05-15T14:54:13.939329+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 750 · 2026-05-15T14:54:13.939778+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 751 · 2026-05-15T14:54:18.108071+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 752 · 2026-05-15T14:54:18.610336+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (83 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp008_re_n16** (killed): —\n- **exp001_seed456** (killed): —\n- **exp001_seed123** (killed): —\n\n## 趋势\n成功 46 / 负向 20 / 失败 1 / 共 83\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_007_ner_llama: 已被终止 — unknown\n- exp001_seed123: 已被终止 — unknown\n- exp001_seed456: 已被终止 — unknown\n- exp008_re_n16: 已被终止 — unknown\n- exp_002_merge_conll2003: 已被终止 — unknown\n- exp_001_n16_seed123_full: 已被终止 — unknown\n- exp_001_n16_seed456_full: 已被终止 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\n- exp_019_supervised_verifier: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 753 · 2026-05-15T14:54:18.610803+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 754 · 2026-05-15T14:54:19.525524+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## ρ 一致性审计 (2026-05-15) — 关键管道 bug\\n- **根因**：旧管道 `compute_metrics.py` 包含 gold-empty 实例 + FK 对全空 sample 返回 0（应为 1.0）\\n- CoNLL 697/3453 (20%) gold-empty 实例导致 FK ρ 膨胀 0.48→0.81，SJ ρ 压低 0.48→0.18，排名反转\\n- **统一标准**：排除 gold-empty 实例。CoNLL n=2756，SciERC n=551（或 n=529 排除空 gold NER）\\n- 论文所有 ρ 值必须来自 gold-filtered 管道（`rho_audit.py
…[truncated 1052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 914
}
```

</details>

---


### Tool call

_source line 755 · 2026-05-15T14:54:19.727904+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 756 · 2026-05-15T14:54:19.780284+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 757 · 2026-05-15T14:54:24.000458+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 758 · 2026-05-15T14:54:24.201854+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex
/home/ubuntu/.agent-
…[truncated 2776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 759 · 2026-05-15T14:54:24.302779+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 760 · 2026-05-15T14:54:24.354467+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_gap.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_curves.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figure
…[truncated 6818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 761 · 2026-05-15T14:54:30.782674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 762 · 2026-05-15T14:54:31.234908+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 763 · 2026-05-15T14:54:31.235338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 764 · 2026-05-15T14:54:31.687565+00:00_

1	\begin{abstract}
2	Self-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote exists.
3	Can consistency signals nonetheless select the best among $N$ candidates?
4	
5	Across three NER and one RE benchmark with two 8B-parameter models, all signals achieve strong quality estimation yet none significantly improves sample selection despite 12--18~pp of oracle headroom---the \textit{correlation-selection gap}.
6	Instance-level signals fail by construction; the two mechanisms that \textit{could} bridge the gap also fail: log-probability scores are compressed into effective ties (60\% of instances), and consensus-proximity selection (MBR decoding) correlates with quality across but not within instances.
7	Signal rankings are difficulty-dependent and collapse at the capability boundary.
8	
9	The gap widens with sample size; closing it likely requires per-sample scoring such as trained verifiers.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 765 · 2026-05-15T14:54:31.738308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 766 · 2026-05-15T14:54:32.190429+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2025scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a structurally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumpt
…[truncated 5489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 767 · 2026-05-15T14:54:32.190926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 768 · 2026-05-15T14:54:32.592639+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface
…[truncated 5477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 769 · 2026-05-15T14:54:32.593280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 770 · 2026-05-15T14:54:33.597632+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in T
…[truncated 13735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 771 · 2026-05-15T14:54:33.598020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 772 · 2026-05-15T14:54:34.100459+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2025scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selec
…[truncated 3089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 773 · 2026-05-15T14:54:34.100841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 774 · 2026-05-15T14:54:34.553374+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.
6	At higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) with lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).
7	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
8	
9	\paragraph{Why the gap exists: two layers.}
10	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
11	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
12	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 12--18~pp oracle headroom.
13	LP scores are severely compressed: the median within-instance LP range is only 0.041 nats, below the $\varepsilon{=}0.05$ threshold at which 60\% of instances are effectively tied, and 75\% of pairwise comparisons fall within $|\Delta|{<}0.026$ (Appendix~\ref{app:logprob_ties}).
14	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
15	This diagnostic confirms that LP carries useful per-sample qualit
…[truncated 6757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 775 · 2026-05-15T14:54:34.553753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 776 · 2026-05-15T14:54:35.005734+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.
4	All signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection on SciERC despite 12--18~pp oracle headroom---the \textit{correlation-selection gap}.
5	The instance-level failure of four signals is definitional; the empirical finding is that neither consensus-proximity selection (MBR decoding) nor log-probability bridges the gap.
6	MBR utility correlates with quality across instances but not within them; LP scores are compressed into effective ties (60\% of instances), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
7	A controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), indicating task-dependent interaction with decoding regime.
8	Signal rankings shift with task difficulty---EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude; at the capability boundary (WNUT-17), all signals collapse to non-significance.
9	RE findings rest on SciERC alone (preliminary) and warrant multi-benchmark validation.
10	Trained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 777 · 2026-05-15T14:54:35.056468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 778 · 2026-05-15T14:54:35.508596+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists
…[truncated 2611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 779 · 2026-05-15T14:54:35.509123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 780 · 2026-05-15T14:54:35.973765+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
47	\quad FK & 
…[truncated 47137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 464
}
```

</details>

---


### Tool call

_source line 781 · 2026-05-15T14:54:35.974283+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 782 · 2026-05-15T14:54:36.024828+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 783 · 2026-05-15T14:54:44.875594+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-15T14:54:46.187321+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 findings track submission requirements page limit template",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'softconf.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 findings track submission requirements page limit template",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'softconf.com']"
  }
}
```

</details>

---


### Tool call

_source line 785 · 2026-05-15T14:54:47.845825+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-15T14:54:48.197969+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-15T14:54:48.198425+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 788 · 2026-05-15T14:54:54.450197+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the search results, here's the information about EMNLP 2026:

## Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

#
…[truncated 1560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 9574
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-15T14:54:59.974400+00:00_

Web search results for query: "EMNLP 2026 findings track submission requirements page limit template"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"LM Playschool: Improving Language Models through Learning from Dialogue Interaction | ACL Member Portal","url":"https://www.aclweb.org/portal/content/lm-playschool-improving-language-models-through-learning-dialogue-game-interaction"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Final Call for Papers - 4th Multilingual Representation Learning (MRL) Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/final-call-papers-4th-multilingual-representation-learning-mrl-workshop"},{"title":"[Call for participation] Present your Findings of EMNLP paper at the NLP4MusA (NLP for Music and Audio) workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-present-your-findings-emnlp-paper-nlp4musa-nlp-music-and-audio-workshop"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"DEADLINE EXTENSION: FINAL CALL FOR PAPERS: THE 4TH MULTILINGUAL REPRESENTATION LEARNING (MRL) WORKSHOP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/deadline-extension-final-call
…[truncated 5186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 13787
}
```

</details>

---


### Tool result

_source line 790 · 2026-05-15T14:54:59.974862+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 12129
}
```

</details>

---


### Tool call

_source line 791 · 2026-05-15T14:55:04.718301+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 792 · 2026-05-15T14:55:04.718722+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 793 · 2026-05-15T14:55:06.100393+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" 2026 submission format page limit long paper short paper template anonymization",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" 2026 submission format page limit long paper short paper template anonymization",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-15T14:55:07.024998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-15T14:55:07.440254+00:00_

1	issues:
2	- id: R0-C1
3	  summary: 模型规模单一（仅 8B）
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 1
9	  mentions:
10	  - round: 0
11	    reviewers: [1, 2]
12	    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性
13	  - round: 1
14	    reviewers: [1, 2]
15	    note: model-agnostic 与 Limitations 矛盾
16	  action_items:
17	  - round: 1
18	    action: 全文替换 model-agnostic → consistent across tested model families
19	    assigned_to: Paper Agent
20	    status: resolved
21	  resolution: Round 2 Reviewer 确认措辞修正到位，无再提
22	  resolution_round: 2
23	- id: R0-C2
24	  summary: 相关工作显著遗漏
25	  category: framing
26	  severity: warning
27	  status: resolved
28	  first_raised_round: 0
29	  last_seen_round: 1
30	  mentions:
31	  - round: 0
32	    reviewers: [1, 2]
33	    note: 5 篇核心文献缺失
34	  - round: 1
35	    reviewers: [1, 2]
36	    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC
37	  action_items:
38	  - round: 1
39	    action: 补充 6 篇引用到 Related Work
40	    assigned_to: Paper Agent
41	    status: resolved
42	  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'
43	  resolution_round: 2
44	- id: R0-C3
45	  summary: RE 结论仅基于 SciERC 单数据集
46	  category: experiment
47	  severity: critical
48	  status: resolved
49	  first_raised_round: 0
50	  last_seen_round: 4
51	  mentions:
52	  - round: 0
53	    reviewers: [1, 2]
54	    note: 需跨数据集验证或降级措辞
55	  - round: 2
56	    reviewers: [1, 2]
57	    note: Abstract RE 措辞需修正
58	  - round: 3
59	    reviewers: [1, 2]
60	    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围
61	  - round: 4
62	    reviewers: [1, 2]
63	    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪
64	  action_items:
65	  - round: 1
66	    action: 降级措辞 universal → observed in SciERC
67	    assigned_to: Paper Agent
68	    status: resolved
69	  - round: 2
70	    action: Abstract 改为 NER (three datasets) and RE (SciERC)
71	    assigned_to: Paper Agent
72	    status: re
…[truncated 59820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 415
}
```

</details>

---


### Tool result

_source line 796 · 2026-05-15T14:55:14.647411+00:00_

Web search results for query: ""ACL Rolling Review" 2026 submission format page limit long paper short paper template anonymization"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"The 6th International Conference on Natural Language Processing for the Digital Humanities | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-international-conference-natural-language-processing-digital-humanities"}]

Based on the search results for ACL Rolling Review 2026 submission format requirements, here's what I found:

## Page Limits

Long papers should follow page limits of 8 pages for long papers
…[truncated 1317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 8547
}
```

</details>

---


### Tool call

_source line 797 · 2026-05-15T14:56:06.434482+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 798 · 2026-05-15T14:56:06.887896+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 799 · 2026-05-15T14:56:07.040414+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/ | wc -l",
  "description": "Count paper PDF pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/ | wc -l",
    "description": "Count paper PDF pages"
  }
}
```

</details>

---


### Tool result

_source line 800 · 2026-05-15T14:56:07.242494+00:00_

20

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 801 · 2026-05-15T14:56:16.331754+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 802 · 2026-05-15T14:56:16.786274+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 803 · 2026-05-15T14:56:16.836852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 804 · 2026-05-15T14:56:17.038957+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 805 · 2026-05-15T14:56:21.667320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 806 · 2026-05-15T14:56:22.221623+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 807 · 2026-05-15T14:56:22.272323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 808 · 2026-05-15T14:56:22.475118+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 809 · 2026-05-15T14:56:26.643019+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 810 · 2026-05-15T14:56:26.845452+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 811 · 2026-05-15T14:56:30.359660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 812 · 2026-05-15T14:56:31.064995+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 813 · 2026-05-15T14:57:18.599491+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 814 · 2026-05-15T14:57:18.650207+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 815 · 2026-05-15T14:58:06.274328+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**：方法严谨性 + 实验可靠性\n\n### 投稿信息\n- **目标 venue**: EMNLP 2026 Findings (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template, 长文 8 页正文 + unlimited Limitations/Ethics/References/Appendix\n- **匿名**: Double-blind\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（多文件结构，sections 在 `sections/` 子目录）\n\n### 论文概要\n本文研究 LLM 结构化信息抽取（NER/RE）中，自一致性信号能否用于质量估计和样本选择。比较 5 个置信度信号（VC, SJ, FK, EM, LP），在 3 个 NER 数据集 + 1 个 RE 数据集、2 个 8B 模型上系统评估。核心发现：所有信号实现强质量估计（ρ 至 0.38, AUROC 至 0.75），但无一显著改善样本选择——\"correlation-selection gap\"。机制解释：LP score compression + MBR utility-quality misalignment。\n\n### 审查要点（不限于此）\n\n1. **统计检验严谨性**\n   - Bootstrap resampling 方法是否规范（B=10,000, Fisher combination, n=551）\n   - TOST 等价检验的 δ 选择是否有充分论证（论文用 ±2/3/5 pp，锚定于 oracle headroom）\n   - 多重比较校正是否充分（Bonferroni 声明）\n   - 单种子 vs 多种子：核心 selection failure（Table 3, seed=42）是否需要多种子验证\n\n2. **信号形式化**\n   - SJ（Eq. 4-5）：Hungarian matching 目标函数、zero-IoU pairs 处理、max normalizer vs union normalizer 选择\n   - VC（Eq. 6）：QE 用连续公式 vs selection 用 majority threshold——Table 3 是否清楚标注\n   - FK（Eq. 3）：独立性假设的 justification（excess agreement -0.4% to -4.0%, n=5 t-test 功效是否足够）\n   - LP（Eq. 1）：ε=0.05 \"effectively tied\" 阈值的 arbitrary 程度（Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%，59× 跳变）\n\n3. **实验设计**\n   - RE 结论仅基于 SciERC 单数据集——\"preliminary\" 标注是否全文一致\n   - Free-form ablation 范围（1 dataset × 1 model × 1 seed）是否支撑 \"task-intrinsic\" 声称\n   - LP 温度数据缺失（T=0.7 无 LP 数据）——核心诊断对象的关键参数\n   - N=8 核心结果单种子，N=16 有 3-seed——是否存在不对称\n   - Qwen3-8B SciERC 的 enable_thinking confound\n\n4. **可复现性**\n   - 训练配置（Appendix Table 8）完整度\n   - Prompt template 是否充分\n   - 数据集 filtering 标准（n=529 vs 551, gold-empty 排除）是否清晰\n\n请按 EMNLP 标准进行严格审查，输出完整审稿报告。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**：方法严谨性 + 实验可靠性\n\n### 投稿信息\n- **目标 venue**: EMNLP 2026 Findings (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template, 长文 8 页正文 + unlimited Limitations/Ethics/References/Appendix\n- **匿名**: Double-blind\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（多文件结构，sections 在 `sections/` 子目录）\n\n### 论文概要\n本文研究 LLM 结构化信息抽取（NER/RE）中，自一致性信号能否用于质量估计和样本选择。比较 5 个置信度信号（VC, SJ, FK, EM, LP），在 3 个 NER 数据集 + 1 个 RE 数据集、2 个 8B 模型上系统评估。核心发现：所有信号实现强质量估计（ρ 至 0.38, AUROC 至 0.75），但无一显著改善样本选择——\"correlation-selection gap\"。机制解释：LP score compression + MBR utility-quality misalignment。\n\n### 审查要点（不限于此）\n\n1. **统计检验严谨性**\n   - Bootstrap resampling 方法是否规范（B=10,000, Fisher combination, n=551）\n   - TOST 等价检验的 δ 选择是否有充分论证（论文用 ±2/3/5 pp，锚定于 oracle headroom）\n   - 多重比较校正是否充分（Bonferroni 声明）\n   - 单种子 vs 多种子：核心 selection failure（Table 3, seed=42）是否需要多种子验证\n\n2. **信号形式化**\n   - SJ（Eq. 4-5）：Hungarian matching 目标函数、zero-IoU pairs 处理、max normalizer vs union normalizer 选择\n   - VC（Eq. 6）：QE 用连续公式 vs selection 用 majority threshold——Table 3 是否清楚标注\n   - FK（Eq. 3）：独立性假设的 justification（excess agreement -0.4% to -4.0%, n=5 t-test 功效是否足够）\n   - LP（Eq. 1）：ε=0.05 \"effectively tied\" 阈值的 arbitrary 程度（Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%，59× 跳变）\n\n3. **实验设计**\n   - RE 结论仅基于 SciERC 单数据集——\"preliminary\" 标注是否全文一致\n   - Free-form ablation 范围（1 dataset × 1 model × 1 seed）是否支撑 \"task-intrinsic\" 声称\n   - LP 温度数据缺失（T=0.7 无 LP 数据）——核心诊断对象的关键参数\n   - N=8 核心结果单种子，N=16 有 3-seed——是否存在不对称\n   - Qwen3-8B SciERC 的 enable_thinking confound\n\n4. **可复现性**\n   - 训练配置（Appendix Table 8）完整度\n   - Prompt template 是否充分\n   - 数据集 filtering 标准（n=529 vs 551, gold-empty 排除）是否清晰\n\n请按 EMNLP 标准进行严格审查，输出完整审稿报告。"
  }
}
```

</details>

---


### Tool result

_source line 816 · 2026-05-15T14:58:28.739029+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22464
}
```

</details>

---


### Tool call

_source line 817 · 2026-05-15T14:58:28.890554+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**：新颖性 + 定位完整性 + 写作质量 + 格式合规\n\n### 投稿信息\n- **目标 venue**: EMNLP 2026 Findings (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template, 长文 8 页正文 + unlimited Limitations/Ethics/References/Appendix\n- **匿名**: Double-blind\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（多文件结构，sections 在 `sections/` 子目录）\n\n### 论文概要\n本文研究 LLM 结构化信息抽取（NER/RE）中，自一致性信号能否用于质量估计和样本选择。比较 5 个置信度信号（VC, SJ, FK, EM, LP），在 3 个 NER 数据集 + 1 个 RE 数据集、2 个 8B 模型上系统评估。核心发现：所有信号实现强质量估计（ρ 至 0.38, AUROC 至 0.75），但无一显著改善样本选择——\"correlation-selection gap\"。机制解释：LP score compression + MBR utility-quality misalignment。\n\n### 审查要点（不限于此）\n\n1. **新颖性与贡献评估**\n   - Correlation-selection gap 是否为真正的 empirical discovery？4/5 信号是 instance-level——无法 select 是定义必然。论文自承 \"Layer 1 (definitional)\"。核心贡献应聚焦 LP compression 诊断 + MBR failure，而非整个 gap\n   - 与 Nédellec et al. (2026) 的增量贡献：structural matching、selection analysis、difficulty gradient 三点增量是否足够\n   - Contribution 1（multi-metric evaluation）是 methodological contribution 还是 engineering benchmark？\n   - SJ 方法新颖性：Hungarian matching + token-level IoU 的组合是否属于标准技术应用\n\n2. **Related Work 覆盖与定位**\n   - 引用完整性检查：62 篇 bib entry 是否均被正文引用（orphan check）\n   - Eikema et al. (2025) structure-conditional MBR 是否应前移到 Related Work（当前仅在 Discussion）\n   - MBR decoding 在非 MT 任务中的应用引用是否充分\n   - Test-time scaling survey (Zhang et al. 2025) 引用位置是否合适\n   - 与 concurrent work 的差异化是否清晰（USC, CISC, Self-Certainty, RASC 等）\n\n3. **写作质量**\n   - Abstract 密度：是否过于拥挤（5 signal names, 3 datasets, 2 models, 4 metrics + gap 概念）——是否适合精简为问题-发现-意义三段式\n   - Claim scope：标题 \"8B-Scale\" 是否充分限定规模泛化；\"Do Not Select\" 是否过强（仅 2 个 8B 模型）\n   - 术语一致性：VC/SJ/FK/EM/LP 在全文表格和正文中是否统一\n   - RE 结论的 \"preliminary\" 标注是否全文一致（Abstract, Experiments, Discussion, Conclusion 各处）\n   - Figure/Table caption 信息量和准确性\n\n4. **格式合规（关键）**\n   - **页数检查**：论文正文（Abstract 至 Conclusion）是否 ≤ 8 页（初步估计约 11 页，严重超限）\n   - Limitations section 位置和内容\n   - Ethics Statement 是否独立且有实质内容\n   - 匿名合规：是否有身份泄露（代码链接、致谢、自引方式）\n   - ACL template 使用是否正确（`\\usepackage[review]{acl}`）\n   - References 格式（natbib + acl_natbib.bst）\n\n5. **Reproducibility checklist**\n   - 代码和数据是否承诺发布\n   - 实验配置是否完整\n   - 随机种子报告\n\n请按 EMNLP 标准进行严格审查，输出完整审稿报告。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**：新颖性 + 定位完整性 + 写作质量 + 格式合规\n\n### 投稿信息\n- **目标 venue**: EMNLP 2026 Findings (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template, 长文 8 页正文 + unlimited Limitations/Ethics/References/Appendix\n- **匿名**: Double-blind\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（多文件结构，sections 在 `sections/` 子目录）\n\n### 论文概要\n本文研究 LLM 结构化信息抽取（NER/RE）中，自一致性信号能否用于质量估计和样本选择。比较 5 个置信度信号（VC, SJ, FK, EM, LP），在 3 个 NER 数据集 + 1 个 RE 数据集、2 个 8B 模型上系统评估。核心发现：所有信号实现强质量估计（ρ 至 0.38, AUROC 至 0.75），但无一显著改善样本选择——\"correlation-selection gap\"。机制解释：LP score compression + MBR utility-quality misalignment。\n\n### 审查要点（不限于此）\n\n1. **新颖性与贡献评估**\n   - Correlation-selection gap 是否为真正的 empirical discovery？4/5 信号是 instance-level——无法 select 是定义必然。论文自承 \"Layer 1 (definitional)\"。核心贡献应聚焦 LP compression 诊断 + MBR failure，而非整个 gap\n   - 与 Nédellec et al. (2026) 的增量贡献：structural matching、selection analysis、difficulty gradient 三点增量是否足够\n   - Contribution 1（multi-metric evaluation）是 methodological contribution 还是 engineering benchmark？\n   - SJ 方法新颖性：Hungarian matching + token-level IoU 的组合是否属于标准技术应用\n\n2. **Related Work 覆盖与定位**\n   - 引用完整性检查：62 篇 bib entry 是否均被正文引用（orphan check）\n   - Eikema et al. (2025) structure-conditional MBR 是否应前移到 Related Work（当前仅在 Discussion）\n   - MBR decoding 在非 MT 任务中的应用引用是否充分\n   - Test-time scaling survey (Zhang et al. 2025) 引用位置是否合适\n   - 与 concurrent work 的差异化是否清晰（USC, CISC, Self-Certainty, RASC 等）\n\n3. **写作质量**\n   - Abstract 密度：是否过于拥挤（5 signal names, 3 datasets, 2 models, 4 metrics + gap 概念）——是否适合精简为问题-发现-意义三段式\n   - Claim scope：标题 \"8B-Scale\" 是否充分限定规模泛化；\"Do Not Select\" 是否过强（仅 2 个 8B 模型）\n   - 术语一致性：VC/SJ/FK/EM/LP 在全文表格和正文中是否统一\n   - RE 结论的 \"preliminary\" 标注是否全文一致（Abstract, Experiments, Discussion, Conclusion 各处）\n   - Figure/Table caption 信息量和准确性\n\n4. **格式合规（关键）**\n   - **页数检查**：论文正文（Abstract 至 Conclusion）是否 ≤ 8 页（初步估计约 11 页，严重超限）\n   - Limitations section 位置和内容\n   - Ethics Statement 是否独立且有实质内容\n   - 匿名合规：是否有身份泄露（代码链接、致谢、自引方式）\n   - ACL template 使用是否正确（`\\usepackage[review]{acl}`）\n   - References 格式（natbib + acl_natbib.bst）\n\n5. **Reproducibility checklist**\n   - 代码和数据是否承诺发布\n   - 实验配置是否完整\n   - 随机种子报告\n\n请按 EMNLP 标准进行严格审查，输出完整审稿报告。"
  }
}
```

</details>

---


### Tool result

_source line 818 · 2026-05-15T14:58:30.400319+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1509
}
```

</details>

---


### Tool call

_source line 819 · 2026-05-15T14:58:30.400757+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "struct_self_consist_ie",
  "paper_pdf_path": "projects/struct_self_consist_ie/docs/paper/main.pdf",
  "venue": "EMNLP 2026 Findings",
  "note": "Round 8 fresh review。论文已有 7 轮内部审稿历史，本轮为独立评审。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "paper_pdf_path": "projects/struct_self_consist_ie/docs/paper/main.pdf",
    "venue": "EMNLP 2026 Findings",
    "note": "Round 8 fresh review。论文已有 7 轮内部审稿历史，本轮为独立评审。"
  }
}
```

</details>

---


### Tool result

_source line 820 · 2026-05-15T14:58:31.107362+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 706
}
```

</details>

---


### Assistant

_source line 821 · 2026-05-15T14:58:41.463216+00:00_

**Round 1 已启动**：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | 已分配 | 方法严谨性 + 实验可靠性 |
| Reviewer 2 | 已分配 | 新颖性 + 定位 + 写作 + 格式 |
| 外部审稿（Stanford Agentic Reviewer） | 已请求，pending | 异步，不阻塞内部流程 |

等待两位 Reviewer 返回 Round 1 独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 66

## Round 66

2 recorded events


### User

_source line 822 · 2026-05-15T15:04:23.434429+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: Strong Predictors, Weak Selectors: Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction
**目标 venue**: EMNLP 2026 Findings (ARR May cycle)
**审查侧重**: 新颖性 + 定位完整性 + 写作质量 + 格式合规

---

## 总体评分
**Overall**: 2.5/5（介于 Resubmit next cycle 和 Findings acceptance 之间）
**一句话总结**: 方法论扎实、统计分析严谨的负面结果论文，但核心 framing 存在问题——"correlation-selection gap" 中 4/5 信号的 selection 失败是定义必然而非经验发现，真正的经验贡献（LP compression 诊断 + MBR utility-quality misalignment）被过度包装的 gap 叙事稀释；加上正文极可能严重超过 8 页限制，当前版本不宜接收。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法论优秀（3-seed, bootstrap CI, TOST, Fisher combination），但核心 framing 将定义性质的观察与经验发现混为一体，夸大了 empirical contribution 的范围 |
| Excitement | 2.5/5 | LP compression 诊断和 MBR 在 structured IE 上的失败是有价值的负面结果，但 4/5 信号 definitionally 无法 select 的事实削弱了"所有信号都失败"这一叙事的冲击力；整体贡献对 NLP 社区的启发性有限 |
| Overall | 2.5/5 | 页数严重超限是硬伤（可能触发 desk-reject），需要实质性压缩；即使页数合规，contribution framing 也需要重新聚焦 |
| Reproducibility | 4/5 | 训练配置完整（Table 8），prompt 模板、超参数、随机种子均已报告；缺少代码/数据发布承诺 |
| Confidence | 4/5 | 对 self-consistency、MBR decoding、IE 评估均有扎实了解 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文页数极可能严重超过 8 页限制
- 具体位置：main.tex（Abstract → Conclusion 的全部 sections）
- 问题：正文包含 7 个 section（Abstract, Introduction, Related Work, Method, Experiments, Discussion, Conclusion），其中 Introduction 含 1 个 figure*（全宽），Experiments 含 2 个 figure*、1 个 table*（全宽）、1 个 table，Method 含 6 个 displayed equation，Discussion 含 1 个 ablation subsection。保守估计正文约 10-11 页，超限 2-3 页。
- 为什么影响接收：ARR CFP 明确规定长文正文 ≤8 页，超页是 desk-rejection 理由（ARR reviewer guidelines 的 desk-rejection checklist 中列有 format/length violations）。
- 建议修改方向：(1) Discussion §sec:ablation（free-form ablation 详述）可移至 Appendix，正文仅保留 1-2 句结论；(2) Robustness (§5.4) 的大部分数字可移至 Appendix；(3) Experiments 中 seed variability 和 conditional filtering 段落可精简；(4) 压缩 Introduction 的 3 个 contribution bullet——当前每个 contribution 包含过多实验细节（具体数字、p-value），这些应留在 Experiments 中。

**N2** [critical] 核心 framing "correlation-selection gap" 混淆了定义性观察与经验发现
- 具体位置：Abstract line 5-6, Introduction §1 Contributions, Section 5.2 标题, Discussion 全篇
- 问题：论文框架暗示 "5 个信号都在 selection 上失败" 是一个统一的经验发现。但论文自身承认（Introduction line 23: "Four of five signals are instance-level by construction—this is definitional, not empirical"；Discussion Layer 1）4/5 信号是 instance-level aggregates，它们无法 select 是数学上的必然，与"gap"无关。将这 4 个信号纳入 selection table（Table 2）并展示它们"失败"，在方法论上是有效的（通过 consensus-proximity 转化为 per-sample），但在叙事上容易误导读者，因为读者的第一印象是"所有 5 个信号都经验性地失败了"。
- 真正的经验贡献仅限于：(a) LP score compression 诊断（60% tied, 非 tied 子集 +2.9pp p=0.01），(b) MBR utility-quality misalignment 在 structured IE 上的首次证实。这两点足以构成一篇有价值的 Findings 论文，但当前 framing 让它们淹没在过度宏大的"gap"叙事中。
- 为什么影响接收：Reviewer 和 AC 可能认为论文过度包装了一个部分 trivial 的发现（ARR guidelines H1 提到不应因 "unsurprising" 拒稿，但这里的问题不是 surprising 与否，而是定义性观察被包装为经验发现）。
- 建议修改方向：重新聚焦 framing。标题和 abstract 应明确：核心问题是 "为什么 LP（唯一的 per-sample 信号）和 MBR（将 instance-level 转化为 per-sample 的唯一机制）都无法 bridge quality estimation 到 selection"。4 个 instance-level 信号的 definitional failure 可以作为 background/motivation，而非核心 finding。Contribution 1 ("multi-metric evaluation") 更像是 methodology/benchmark 而非 conceptual contribution。

**N3** [critical] 标题 claim 过强："Do Not Select" + "8B-Scale" 的泛化暗示
- 具体位置：标题 "Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction"
- 问题："Do Not Select" 是一个绝对性否定，但论文实际发现 LP 在非 tied 子集上 significantly selects (+2.9pp, p=0.01, §Discussion)，RE 在 free-form decoding 下 LP 也翻转为正（+1.69pp, preliminary）。即在论文自身的实验中，selection 并非完全不可能——只是在 primary setting 下未达显著性。此外，仅基于 2 个 8B 模型，标题使用 "8B-Scale" 暗示了这一规模下的普遍性。Limitations section 正确指出了 70B+ 和 closed-source API 未测试，但标题未反映这一限定。
- 为什么影响接收：标题 overclaim 是 ARR review form 中 Results issues (R5: "Overclaiming or misleading framing") 的评审要点。
- 建议修改方向："Do Not Select" → "Struggle to Select" 或 "Fail to Select Under Score Compression"；考虑移除 "8B-Scale" 或改为 "Two 8B Models"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 信息密度过高，关键 message 被淹没
- 具体位置：Abstract (sections/abstract.tex)
- 问题：10 行 abstract 中包含：5 个信号缩写（VC, SJ, FK, EM, LP）、3 个 NER 数据集 + 1 个 RE 数据集、2 个 8B 模型、4 个评估维度（ρ, AUROC, best-of-N F1, oracle headroom）、"correlation-selection gap" 概念、LP compression 机制（60%）、MBR utility-quality misalignment、difficulty-dependent collapse、trained verifiers 作为 future direction。一般 EMNLP 读者在 abstract 中无法消化这么多具体数字和缩写。
- 建议：精简为"问题—方法—核心发现—implications"四段式。具体数字和信号缩写留给 Introduction。

**W2** [warning] Contribution 1 ("multi-metric evaluation revealing metric dissociation") 的贡献性质模糊
- 具体位置：Introduction, Contribution 1 (line 38-40)
- 问题：该 contribution 声称"EM leads AUROC (0.749) but ranks third in ρ (0.295), so single-metric evaluation risks selecting the wrong signal"。这是有效的实验观察，但它更接近于 methodological recommendation（"应该评估多个指标"）而非 conceptual contribution。在 EMNLP/ARR 评审标准下，这类 benchmark-level 发现通常不被视为独立的核心贡献——除非伴随新方法或新 benchmark release。
- 建议：将其降级为 experimental finding，而非与 Contribution 2/3 并列为核心贡献。

**W3** [warning] SJ（Soft Jaccard）方法新颖性有限
- 具体位置：Method §3.2, Eq. 4-5
- 问题：SJ 的核心组件——Hungarian algorithm 做 bipartite matching + token-level IoU 作为 similarity——均为标准技术。Hungarian matching 在 NER/RE 评估中已有应用（如 entity alignment 文献），token-level IoU 也是常规 span overlap metric。论文将 SJ 作为 "our primary structural signal" 和 "structural matching beyond surface-level agreement"（Introduction line 17, (i)），但未明确说明这一组合相对于已有工作的技术新颖性。
- 建议：明确 SJ 是已有技术的组合应用，而非方法论贡献；或 cite 相关 entity alignment 文献以定位 SJ 的增量。

**W4** [warning] Eikema et al. (2025) structure-conditional MBR 应提前到 Related Work
- 具体位置：Related Work §2 最后一句引用了 eikema2025structured，但主要讨论在 Discussion §6 (line 30)
- 问题：Eikema et al. (2025) 的 structure-conditional MBR decoding 发现 "standard utility functions degrade on structured outputs" 与本文核心发现高度相关。当前仅在 Discussion 中用 1 句带过，在 Related Work 最后 1 句提及。这一工作应该在 Related Work 中被更充分地讨论，并明确本文与之的差异化定位（他们研究 MT structured outputs，本文研究 IE structured outputs；他们提出 structure-conditional 方案，本文诊断失败原因）。
- 建议：在 Related Work 的 MBR 段落中增加 2-3 句讨论 Eikema et al. (2025)，明确两者的互补关系。

**W5** [warning] RE 结论的 "preliminary" 标注在各 section 中不一致
- 具体位置：Abstract 未标注 preliminary；Introduction Contribution 2 line 47 标注 "preliminary"；Introduction Contribution 3 line 52 标注 "preliminary"；Table 1 caption 标注；Discussion 多处标注；Conclusion line 9 标注
- 问题：Abstract（论文最高可见度的部分）完全未提及 RE 结果是 preliminary（基于单一 RE benchmark）。读者如果只读 abstract，会误以为 RE 结论与 NER 同等稳健。考虑到 RE 只有 SciERC 一个数据集（40% zero F1），且 RE selection 在 free-form 下出现 direction reversal，RE 结论的 preliminary 性质应在 abstract 中有所体现。
- 建议：Abstract 中增加一句类似 "RE findings rest on a single benchmark and are preliminary"。

**W6** [warning] 缺少代码/数据发布承诺
- 具体位置：全文（Ethics Statement, Limitations, 均未提及）
- 问题：ARR reproducibility checklist 通常要求作者说明是否会发布代码和数据。论文报告了完整的训练配置和实验参数，但未承诺发布代码、训练好的模型、或实验 artifacts。对于一篇以 empirical benchmark 为核心的论文，缺少复现资源会显著降低实际影响力。
- 建议：在 Ethics Statement 或 Limitations 后添加 "Code and Data" 段，说明发布计划。

**W7** [warning] enable_thinking 训练 confound 的影响评估不充分
- 具体位置：Experiments §5.1 line 15-18, Limitations line 18-21
- 问题：Qwen3-8B 的 SciERC checkpoint 使用 enable_thinking=True 训练（注入空 `&lt;think>&lt;/think>` blocks），而 CoNLL 和 WNUT 未使用。论文辩称影响小（<0.3% of 2048-token window, no reasoning content, constrained decoding suppresses），但未提供任何定量证据对比 thinking vs non-thinking 训练的 LP 分布差异。论文的核心发现之一是 LP score compression——如果 thinking tokens 在训练时偏移了 first-token probability distributions（论文自身在 Limitations 中承认这一可能），这恰好可能影响 LP compression 行为。
- 建议：提供 SciERC vs CoNLL/WNUT 的 LP variance 对比数据，或运行一个 ablation（同一数据集两种 thinking 设置）来排除 confound。

---

## 小问题（不影响接收）

- **M1**: Table 1 caption 中 "SciERC RE" 列标注为 "single benchmark—preliminary"，但 SciERC NER 也是 single benchmark（尽管有 CoNLL + WNUT-17 作为补充）。建议统一 "preliminary" 标注标准或解释为何 NER 不标注。
- **M2**: Eq. 4 中 $\sum_{g} \max(|g_i|, |g_j|)$ 的 normalizer 解释（"penalize length asymmetry"）与标准 Jaccard 的 union normalizer 不同，但论文未讨论这一选择对结果的影响。是否做过 sensitivity analysis？
- **M3**: 引用格式小问题——feng2025optimal 的 bib entry 中 author 字段为 "Feng, Austin"，但 OpenAlex 匹配到的 first author 是 "Austin"（非姓氏），可能需要检查作者顺序。snell2025scaling 类似。
- **M4**: Discussion 中 free-form ablation 段落（§sec:ablation）使用 `\paragraph` 标签但实际是一个完整的 subsection（约 17 行），与 Discussion 其他 paragraph 的粒度不一致。
- **M5**: Appendix 中 Table 3 (tab:robustness) 的 footnote $\dagger$ 解释 "$\sigma=0.013$"，但表格正文中未出现 $\pm 0.013$（表格显示的是单点值 0.411$^\dagger$），容易混淆。
- **M6**: nedellec2026consistency 在 bib 中的 author 字段以 "Yao, Xinzhi" 开头，但 key 用了 "nedellec2026"；虽然不影响编译，但 key 与实际第一作者不一致可能造成混淆。

---

## 主要优势

1. **统计严谨性**: 3-seed analysis, bootstrap CI, TOST equivalence testing, Fisher combined p-values — 远超 IE/NLP 领域的典型论文水准。这种 "negative result done right" 的方法论值得认可。
2. **诚实的 hedging**: RE 结论在 Experiments/Discussion/Conclusion 中一致标注 "preliminary"，训练 confound 在 Limitations 中坦诚披露，seed 456 的 --subtask joint 不一致也被报告。这种透明度在投稿论文中罕见。
3. **LP compression 诊断的机制清晰度**: 60% tied fraction → non-tied subset 显著 select (+2.9pp) → 确认 compression 是 bottleneck 而非 LP 本身无信息——这一逻辑链是论文最强的贡献。
4. **Difficulty gradient 发现**: EM→SJ crossover 在 easy→hard 任务上的切换，以及 WNUT-17 capability boundary 的识别，对 practitioners 有直接指导意义。
5. **引用完整**: 62 篇引用无 orphan 无 missing，覆盖 self-consistency、MBR、uncertainty estimation、IE 等全部相关方向；concurrent work（CISC, Self-Certainty, RASC, LatentSC, Ranked Voting 等）均已讨论。

---

## Reviewer 2 建议的 action items（优先级排序）

1. **[必须]** 压缩正文至 ≤8 页（当前估计 10-11 页）
2. **[必须]** 重新聚焦 contribution framing：核心问题是 LP compression + MBR misalignment，而非 "5 个信号都在 selection 上失败"
3. **[必须]** 修改标题，softening "Do Not Select" claim
4. **[建议]** 精简 abstract，移除大部分具体数字和缩写
5. **[建议]** Abstract 中标注 RE preliminary
6. **[建议]** 扩展 Eikema et al. (2025) 在 Related Work 中的讨论
7. **[建议]** 添加代码/数据发布承诺

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 823 · 2026-05-15T15:04:30.452675+00:00_

Reviewer 2 审稿报告已收到。等待 Reviewer 1 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 67

## Round 67

2 recorded events


### User

_source line 824 · 2026-05-15T15:04:35.138470+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：

**Overall 2.5/5**（Soundness 3.5, Excitement 2.5）。三个 critical 问题：

1. **页数严重超限**（估计 10-11 页 vs 限制 8 页）— 可能触发 desk-reject
2. **Framing 问题** — "correlation-selection gap" 中 4/5 信号的 selection 失败是定义必然，论文自承 "definitional, not empirical"，但 framing 将其包装为统一的经验发现。真正的经验贡献（LP compression 诊断 + MBR misalignment）被稀释
3. **标题 overclaim** — "Do Not Select" 是绝对否定，但论文自身数据显示 LP 在非 tied 子集上 significantly selects (+2.9pp, p=0.01)

主要优势：统计方法论极为严谨（3-seed, bootstrap CI, TOST），LP compression 的机制诊断逻辑清晰，引用完整（62/62，0 orphan/missing），作者对 limitations 的披露非常诚实。引用验证全部通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 825 · 2026-05-15T15:04:41.311869+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 68

## Round 68

6 recorded events


### User

_source line 826 · 2026-05-15T15:04:46.711447+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告

**侧重**：方法严谨性 + 实验可靠性

### 总体评分
- **Overall**: 3.5/5（Findings 边缘接受，需修改后可接收）
- **Soundness**: 3.5/5
- **Excitement**: 3/5
- **Reproducibility**: 3/5
- **Confidence**: 4/5

**一句话总结**: NER 上 correlation-selection gap 的发现和机制分析扎实可信，但 RE 证据薄弱（单数据集+核心 Table 3 单种子）、LP 温度敏感性数据缺失、ε=0.05 阈值论证循环，整体构成一篇值得发表但需补强的实证研究。

### Must-Fix 问题（3 个 critical）

**N1** [critical] ε=0.05 "effectively tied" 阈值论证循环性
- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59× 跳变），阈值选择对核心 "60% effectively tied" 叙事有决定性影响
- ε=0.05 选在中位数附近（median LP range=0.041），保证≥50% tied 是 by construction 非 empirical finding
- 建议报告完整 ε 梯度 + 提供外部基准（QA/MT 上同模型 LP range 作参照）

**N2** [critical] LP 温度数据缺失
- 核心诊断对象 LP 在 T=0.7 无数据（Appendix B 明确标注），但论文在 Section 4.4 声称 "robust performance across T∈{0.7, 1.0}" 易误读为包含 LP
- T<1.0 是常用部署温度，LP compression 在该条件下是否成立完全未知

**N3** [critical] RE 结论基础薄弱
- 仅 SciERC 单数据集；Table 3 RE 仅 seed=42 单种子
- "preliminary" 标注不一致：Abstract 未标 preliminary，Conclusion 合并引用 NER/RE headroom
- 建议补数据集或统一降级 RE 为 pilot study

### Should-Fix 问题（6 个 warning）

**W1** Free-form ablation 仅 1 dataset × 1 model × 1 seed，RE LP 翻转需 3-seed 验证
**W2** FK 独立性检验 n=5 t-test 功效极低，应改用 instance-level 检验（n=529+）
**W3** Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为
**W4** TOST δ 锚定于内部 oracle headroom，缺乏外部实际意义基准
**W5** SJ max normalizer 非标准设计未 ablate
**W6** N=8 QE 主表单种子 vs N=16 多种子，设计不对称

### 主要优势
- Correlation-selection gap 概念和两层机制解释逻辑自洽
- 统计分析远超同类工作（bootstrap + Fisher + TOST + effect size + CI）
- 限制披露透明（enable_thinking、seed 456、LP T=0.7 等逐一讨论）
- NER 跨模型一致性强（Kendall's W=1.000）
- 难度梯度设计揭示信号排名翻转等非显然现象

### 引用核查
62 条引用全部通过交叉验证，无虚假引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 827 · 2026-05-15T15:05:18.375482+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 总体评分\nOverall: 2.5/5, Soundness: 3.5/5, Excitement: 2.5/5, Reproducibility: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 正文页数极可能严重超过 8 页限制\n- 正文包含 7 个 section（Abstract 至 Conclusion），含 1 个 figure*、2 个 figure*、1 个 table*、1 个 table、6 个 displayed equation、1 个 ablation subsection。保守估计正文约 10-11 页，超限 2-3 页。\n- ARR 超页是 desk-rejection 理由。\n- 建议：Discussion §ablation 移至 Appendix；Robustness 大部分移至 Appendix；精简 contribution bullets。\n\n**N2** [critical] 核心 framing \"correlation-selection gap\" 混淆定义性观察与经验发现\n- 论文自承 4/5 信号 \"definitional, not empirical\"（Introduction line 23），但将 5 个信号纳入 selection table 展示\"失败\"，叙事上误导读者。\n- 真正经验贡献仅限：(a) LP score compression 诊断，(b) MBR utility-quality misalignment。\n- 建议：重新聚焦 framing，核心问题改为\"为什么 LP 和 MBR 都无法 bridge quality estimation 到 selection\"。\n\n**N3** [critical] 标题 claim 过强：\"Do Not Select\" + \"8B-Scale\" 的泛化暗示\n- \"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集上 significantly selects (+2.9pp, p=0.01)，RE 在 free-form 下也翻转为正。\n- 仅 2 个 8B 模型，标题暗示规模普遍性。\n- 建议：\"Do Not Select\" → \"Struggle to Select\"；移除或限定 \"8B-Scale\"。\n\n### Should-Fix 问题\n\n**W1** Abstract 信息密度过高\n**W2** Contribution 1 (\"multi-metric evaluation\") 更像 methodology 而非 conceptual contribution\n**W3** SJ 方法新颖性有限（标准技术组合）\n**W4** Eikema et al. (2025) structure-conditional MBR 应前移到 Related Work\n**W5** RE \"preliminary\" 标注各 section 不一致（Abstract 未标注）\n**W6** 缺少代码/数据发布承诺\n**W7** enable_thinking 训练 confound 影响评估不充分\n\n### 小问题\nM1: NER 也是 single benchmark 但未标 preliminary\nM2: SJ max normalizer 无 sensitivity analysis\nM3: bib entry 作者顺序问题（feng2025optimal, snell2025scaling）\nM4: Discussion ablation 段落粒度不一致\nM5: Appendix Table 3 footnote 与表格数字不匹配\nM6: nedellec2026 bib key 与实际第一作者不一致\n\n### Reviewer 2 主要优势评价\n1. 统计严谨性远超典型 NLP 论文\n2. 对 limitations 的诚实 hedging\n3. LP compression 诊断的机制清晰度\n4. Difficulty gradient 的实践指导价值\n5. 引用完整（62/62）\n\n---\n\n请对以上每个 N/W/M 级别问题给出你的 [AGREE] 或 [REBUT] 判断，并说明理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 总体评分\nOverall: 2.5/5, Soundness: 3.5/5, Excitement: 2.5/5, Reproducibility: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 正文页数极可能严重超过 8 页限制\n- 正文包含 7 个 section（Abstract 至 Conclusion），含 1 个 figure*、2 个 figure*、1 个 table*、1 个 table、6 个 displayed equation、1 个 ablation subsection。保守估计正文约 10-11 页，超限 2-3 页。\n- ARR 超页是 desk-rejection 理由。\n- 建议：Discussion §ablation 移至 Appendix；Robustness 大部分移至 Appendix；精简 contribution bullets。\n\n**N2** [critical] 核心 framing \"correlation-selection gap\" 混淆定义性观察与经验发现\n- 论文自承 4/5 信号 \"definitional, not empirical\"（Introduction line 23），但将 5 个信号纳入 selection table 展示\"失败\"，叙事上误导读者。\n- 真正经验贡献仅限：(a) LP score compression 诊断，(b) MBR utility-quality misalignment。\n- 建议：重新聚焦 framing，核心问题改为\"为什么 LP 和 MBR 都无法 bridge quality estimation 到 selection\"。\n\n**N3** [critical] 标题 claim 过强：\"Do Not Select\" + \"8B-Scale\" 的泛化暗示\n- \"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集上 significantly selects (+2.9pp, p=0.01)，RE 在 free-form 下也翻转为正。\n- 仅 2 个 8B 模型，标题暗示规模普遍性。\n- 建议：\"Do Not Select\" → \"Struggle to Select\"；移除或限定 \"8B-Scale\"。\n\n### Should-Fix 问题\n\n**W1** Abstract 信息密度过高\n**W2** Contribution 1 (\"multi-metric evaluation\") 更像 methodology 而非 conceptual contribution\n**W3** SJ 方法新颖性有限（标准技术组合）\n**W4** Eikema et al. (2025) structure-conditional MBR 应前移到 Related Work\n**W5** RE \"preliminary\" 标注各 section 不一致（Abstract 未标注）\n**W6** 缺少代码/数据发布承诺\n**W7** enable_thinking 训练 confound 影响评估不充分\n\n### 小问题\nM1: NER 也是 single benchmark 但未标 preliminary\nM2: SJ max normalizer 无 sensitivity analysis\nM3: bib entry 作者顺序问题（feng2025optimal, snell2025scaling）\nM4: Discussion ablation 段落粒度不一致\nM5: Appendix Table 3 footnote 与表格数字不匹配\nM6: nedellec2026 bib key 与实际第一作者不一致\n\n### Reviewer 2 主要优势评价\n1. 统计严谨性远超典型 NLP 论文\n2. 对 limitations 的诚实 hedging\n3. LP compression 诊断的机制清晰度\n4. Difficulty gradient 的实践指导价值\n5. 引用完整（62/62）\n\n---\n\n请对以上每个 N/W/M 级别问题给出你的 [AGREE] 或 [REBUT] 判断，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 828 · 2026-05-15T15:05:27.565879+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 9190
}
```

</details>

---


### Tool call

_source line 829 · 2026-05-15T15:05:27.667434+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 总体评分\nOverall: 3.5/5, Soundness: 3.5/5, Excitement: 3/5, Reproducibility: 3/5\n\n### Must-Fix 问题\n\n**N1** [critical] ε=0.05 \"effectively tied\" 阈值论证循环性\n- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59× 跳变），阈值处于 CDF 陡峭区域\n- ε=0.05 选在中位数附近（median LP range=0.041），保证≥50% tied 是 by construction\n- 建议报告完整 ε 梯度 + 提供外部基准（QA/MT 上同模型 LP range 作参照）\n\n**N2** [critical] LP 温度数据缺失\n- 核心诊断对象 LP 在 T=0.7 无数据（Appendix B 明确标注），但论文在 Section 4.4 声称 \"robust performance across T∈{0.7, 1.0}\" 易误读为包含 LP\n- T<1.0 是常用部署温度，LP compression 行为完全未知\n\n**N3** [critical] RE 结论基础薄弱\n- 仅 SciERC 单数据集；Table 3 RE 仅 seed=42 单种子\n- \"preliminary\" 标注不一致：Abstract 未标 preliminary\n- 建议补数据集或统一降级 RE 为 pilot study\n\n### Should-Fix 问题\n\n**W1** Free-form ablation 仅 1 dataset × 1 model × 1 seed，RE LP 翻转需 3-seed 验证\n**W2** FK 独立性检验 n=5 t-test 功效极低，应改用 instance-level 检验（n=529+）\n**W3** Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n**W4** TOST δ 锚定于内部 oracle headroom，缺乏外部实际意义基准\n**W5** SJ max normalizer 非标准设计未 ablate\n**W6** N=8 QE 主表单种子 vs N=16 多种子，设计不对称\n\n### Reviewer 1 主要优势评价\n1. Correlation-selection gap 概念和两层机制解释逻辑自洽\n2. 统计分析远超同类工作\n3. 限制披露透明\n4. NER 跨模型一致性强（Kendall's W=1.000）\n5. 难度梯度设计揭示非显然现象\n\n### 引用核查\n62 条引用全部通过，无虚假引用。\n\n---\n\n请对以上每个 N/W 级别问题给出你的 [AGREE] 或 [REBUT] 判断，并说明理由。特别是：你是否同意 R1 关于 ε=0.05 循环论证的判断？LP 温度缺失的 severity 你如何评估？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 总体评分\nOverall: 3.5/5, Soundness: 3.5/5, Excitement: 3/5, Reproducibility: 3/5\n\n### Must-Fix 问题\n\n**N1** [critical] ε=0.05 \"effectively tied\" 阈值论证循环性\n- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59× 跳变），阈值处于 CDF 陡峭区域\n- ε=0.05 选在中位数附近（median LP range=0.041），保证≥50% tied 是 by construction\n- 建议报告完整 ε 梯度 + 提供外部基准（QA/MT 上同模型 LP range 作参照）\n\n**N2** [critical] LP 温度数据缺失\n- 核心诊断对象 LP 在 T=0.7 无数据（Appendix B 明确标注），但论文在 Section 4.4 声称 \"robust performance across T∈{0.7, 1.0}\" 易误读为包含 LP\n- T<1.0 是常用部署温度，LP compression 行为完全未知\n\n**N3** [critical] RE 结论基础薄弱\n- 仅 SciERC 单数据集；Table 3 RE 仅 seed=42 单种子\n- \"preliminary\" 标注不一致：Abstract 未标 preliminary\n- 建议补数据集或统一降级 RE 为 pilot study\n\n### Should-Fix 问题\n\n**W1** Free-form ablation 仅 1 dataset × 1 model × 1 seed，RE LP 翻转需 3-seed 验证\n**W2** FK 独立性检验 n=5 t-test 功效极低，应改用 instance-level 检验（n=529+）\n**W3** Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n**W4** TOST δ 锚定于内部 oracle headroom，缺乏外部实际意义基准\n**W5** SJ max normalizer 非标准设计未 ablate\n**W6** N=8 QE 主表单种子 vs N=16 多种子，设计不对称\n\n### Reviewer 1 主要优势评价\n1. Correlation-selection gap 概念和两层机制解释逻辑自洽\n2. 统计分析远超同类工作\n3. 限制披露透明\n4. NER 跨模型一致性强（Kendall's W=1.000）\n5. 难度梯度设计揭示非显然现象\n\n### 引用核查\n62 条引用全部通过，无虚假引用。\n\n---\n\n请对以上每个 N/W 级别问题给出你的 [AGREE] 或 [REBUT] 判断，并说明理由。特别是：你是否同意 R1 关于 ε=0.05 循环论证的判断？LP 温度缺失的 severity 你如何评估？"
  }
}
```

</details>

---


### Tool result

_source line 830 · 2026-05-15T15:05:29.076290+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1408
}
```

</details>

---


### Assistant

_source line 831 · 2026-05-15T15:05:32.385500+00:00_

交叉分享已发送。两位 Reviewer 正在逐条回应对方意见，等待返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 69

## Round 69

2 recorded events


### User

_source line 832 · 2026-05-15T15:05:34.919544+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：论文在 NER 上的核心发现（correlation-selection gap + LP compression 机制）有充分统计支撑，论文写作透明度高于同类工作。3 个 critical 问题集中在：(1) ε=0.05 阈值的循环论证需补外部基准，(2) LP 在 T=0.7 下缺失数据是核心机制的关键盲区，(3) RE 仅单数据集+单种子需补强或降级。6 个 should-fix 问题涉及 ablation 范围、FK 检验功效、seed 456 confound 等方法论细节。整体评分 3.5/5，适合 EMNLP Findings 但需一轮修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 833 · 2026-05-15T15:05:43.106929+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 70

## Round 70

2 recorded events


### User

_source line 834 · 2026-05-15T15:07:20.149501+00:00_

[Reviewer 1 审稿结果]:
## 交叉回应：Reviewer 2 审稿意见

---

### Must-Fix 问题

**[AGREE] R2-N1: 正文页数可能超限**
同意这是一个需要确认的风险。正文包含 Introduction（含 figure*）、Related Work、Method（6 个 displayed equation）、Experiments（2 个 figure*、1 个 table*、1 个 table）、Discussion（含完整 ablation 段落）、Conclusion，内容体量确实接近或超过 8 页。Discussion 中的 "Score compression under free-form decoding" 段落（§5 lines 33-49）和 "Task-specific decoding interactions" 段落（lines 42-49）合计约 1 页，移至 Appendix 不会损失核心论证。R2 的建议（Discussion ablation 移至 Appendix、Robustness 精简、contribution bullets 压缩）可操作。但需注意：我无法从 .tex 源码精确判定编译后页数，建议 Director 确认实际编译页数。

**[REBUT] R2-N2: 核心 framing 混淆定义性 vs 经验性**
R2 认为将 4 个 instance-level 信号纳入 Table 3 构成叙事误导。我不同意这个判断的严重程度。

理由：(1) 论文在 Introduction line 23 明确标注 "definitional, not empirical"，在 Section 4.3 line 119 再次强调 "they cannot rank candidates by construction"，在 Conclusion line 5 第三次重申——三处一致的透明声明不构成"误导"。(2) Table 3 的完整比较（5 信号 + oracle + greedy + random）为读者提供了 apples-to-apples 的全景视图；如果省略 4 个信号，反而会导致读者质疑为什么不测试它们。(3) 论文的核心 framing 准确地说是："gap 的存在是多层次的——Layer 1 是 definitional（4 个信号），Layer 2 是 empirical（LP compression + MBR misalignment）"。这个两层结构是有信息量的，因为它解释了为什么 consensus-proximity selection（将 instance-level 信号转化为 per-sample ranking 的尝试）也失败了。

但 R2 有一个合理的子观点：论文可以更早、更醒目地区分 definitional vs empirical，例如在 Table 3 中用视觉分组（水平线分隔 instance-level 和 per-sample 信号）。这是一个呈现改进建议，而非 framing 错误。

**[AGREE with qualification] R2-N3: 标题 claim 过强**
部分同意。"Do Not Select" 确实与非 tied 子集的显著选择结果（$+2.9$ pp, $p=0.01$; Section 5, Discussion）矛盾——论文自己证明了在 40% 的实例上 LP *does* select。R2 建议 "Struggle to Select" 是更准确的描述。

但关于 "8B-Scale" 我不同意 R2 的判断。标题中 "8B-Scale" 是 **描述性限定**（specifying what was tested），而非泛化声明。如果去掉 "8B-Scale"，反而会让读者认为结论适用于所有模型规模，这更具误导性。论文在 Limitations (line 6) 明确说 "whether our findings hold for larger models (70B+) remains untested"，标题的 "8B-Scale" 恰好与这个限定一致。建议保留 "8B-Scale"，仅将 "Do Not Select" 修改为更 hedged 的表述。

---

### Should-Fix 问题

**[AGREE] R2-W1: Abstract 信息密度过高**
同意。10 行 abstract 包含 5 个信号名称、3+1 数据集、2 模型、ρ/AUROC 具体数值、LP compression 百分比、MBR misalignment、difficulty-dependence、未来方向。建议删减具体数值（如 "ρ 至 0.38, AUROC 至 0.75" 可简化为 "strong quality estimation"），将信号名称移至正文。

**[REBUT] R2-W2: Contribution 1 是 methodology 而非 conceptual contribution**
不同意。Contribution 1 的核心发现是 **metric dissociation**——EM 在 AUROC 领先 (0.749) 但在 ρ 仅排第三 (0.295)（Table 2）。这不是"我们用了多个指标"的方法论声明，而是一个 empirical finding：单指标评估会选错信号。这个发现对 practitioners 有直接实用价值（质量分流用 EM，细粒度排名用 VC/SJ），不应降格为方法论细节。当然，Contribution 1 的措辞 ("Multi-metric evaluation revealing metric dissociation") 确实不够锐利，建议改为以发现为主语的表述。

**[REBUT] R2-W3: SJ 方法新颖性有限**
论文并未将 SJ 作为方法论贡献（Contribution list 中无 "novel signal design"）。SJ 是分析工具而非论文贡献，因此 "新颖性有限" 的批评对象不成立。论文的贡献在于系统比较，而非发明信号。且 SJ 的具体设计选择（type-aware bipartite matching + token-level IoU + max normalizer; Eq. 4-5）在 IE 自一致性文献中未见先例——Nédellec et al. (2026) 只用 surface-level agreement，论文自身在 Introduction line 17 和 Related Work lines 13-15 明确对比了这一改进。

**[AGREE] R2-W4: Eikema et al. (2025) 应前移**
同意。Eikema et al. (2025) 的 structure-conditional MBR 发现（"standard utility functions degrade on structured outputs"）与本文核心发现直接相关。当前仅在 Related Work line 27 和 Discussion line 30 简短提及，建议在 Related Work 中扩展讨论，明确本文与其互补关系。

**[AGREE] R2-W5: RE "preliminary" 标注不一致**
完全同意，与我自己 N3 中的发现一致。Abstract 未标注 preliminary，Conclusion 合并引用 NER/RE headroom (12-18 pp)。需全文统一。

**[AGREE] R2-W6: 缺少代码/数据发布承诺**
同意。对于 EMNLP Findings 论文，ARR 评审标准明确考察 reproducibility。论文使用公开数据集和开源模型（Qwen3-8B, LLaMA-3.1-8B），但自定义代码（SJ matching、bootstrap testing pipeline、constrained decoding schema）未提及发布计划。即使只声明 "code will be released upon acceptance" 也能改善评分。

**[AGREE with qualification] R2-W7: enable_thinking confound 影响评估不充分**
部分同意。论文的辩护逻辑是合理的（CoNLL/WNUT 无此 confound 但 LP 同样失败→confound 非 gap 主因；Section 4.1 lines 15-17, Limitations lines 18-21）。但 R2 的 "不充分" 指向一个具体缺口：论文未量化 enable_thinking 对 LP score distribution 的影响。即使 <0.3% token window，first-token probability shift 可能对 LP range（本就极窄，median 0.041 nats）产生 non-negligible 的影响。建议补充 SciERC 上 enable_thinking=False 的 LP 分布对比（至少在 Appendix 中），或明确论证 4-5 个 empty thinking tokens 的 LP 贡献在 mean token log-prob 中被 1500+ 个其他 token 稀释到可忽略。

---

### 小问题

**[REBUT] R2-M1: NER 也是 single benchmark 但未标 preliminary**
不正确。NER 在 **3 个数据集**上评估：SciERC (Table 2), CoNLL-2003 (Table 2), WNUT-17 (Table 7)。RE 之所以标 preliminary 是因为仅 SciERC 一个 RE benchmark，而 NER 的 3 数据集覆盖了 easy→hard 难度梯度，不属于 single-benchmark 问题。

**[AGREE] R2-M2: SJ max normalizer 无 sensitivity analysis**
同意，与我自己 W5 一致。

**[REBUT] R2-M3: bib entry 作者顺序问题**
引用核查结果显示 feng2025optimal 和 snell2025scaling 的 "mismatch" 仅为 OpenAlex API 返回 first name vs bib 使用 last name 的格式差异（bib=feng vs api=austin → Austin Feng; bib=snell vs api=charlie → Charlie Snell）。bib 中实际 author field 排列正确，不存在作者顺序错误。

**[AGREE] R2-M4: Discussion ablation 段落粒度不一致**
同意。"Score compression under free-form decoding" 和 "Task-specific decoding interactions" 两段的细节程度（win/loss ratio, Jaccard similarity 0.472, selective variance reallocation p<0.0001）更适合 Appendix 而非 Discussion 正文。

**[REBUT with uncertainty] R2-M5: Appendix Table 3 footnote 与表格数字不匹配**
无法从 .tex 源码确认 R2 所指的具体不匹配。Table 3 (selection table) footnote 关于 VC majority-threshold voting 和 greedy baseline 的说明与正文数字一致（VC NER 0.595, greedy 0.620, Δ=-2.5 pp; Section 4.3 line 129）。如 R2 指的是编译后的表格渲染问题，需要查看 PDF 才能确认。

**[AGREE] R2-M6: nedellec2026 bib key 与实际第一作者不一致**
确认。bib 条目 `nedellec2026consistency` 的实际第一作者是 "Yao, Xinzhi"，而非 Nédellec。bib key 使用了第二作者姓氏，属于 bib 卫生问题，应修正为 `yao2026consistency`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 835 · 2026-05-15T15:07:27.665500+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 71

## Round 71

12 recorded events


### User

_source line 836 · 2026-05-15T15:07:49.215104+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 回应 Reviewer 1 审稿意见

### 概要

R1 的 6 个 Must/Should-Fix 问题中，我 **AGREE** 5 个（N2, N3, W1, W4, W5），**AGREE with nuance** 3 个（N1, W2, W3, W6）。无 REBUT。

### 关键判断

**ε=0.05 circularity（R1-N1）**: 表面论证正确（中位数附近选阈值保证 ≥50% tied），但非 tied 子集的 conditional diagnostic (+2.9pp, p=0.01) 不依赖于具体 tied fraction 百分比。建议补充完整 ε 梯度和外部基准，但不影响 LP compression 核心诊断的有效性。

**LP 温度缺失（R1-N2）**: 评估为 **high severity**，与 R1 一致。LP 是唯一 per-sample 信号，score compression 在部署温度下的行为完全未知。这是仅次于页数超限的第二大方法论问题。

**RE preliminary（R1-N3）**: 完全同意。补充指出 Table 2 RE 列缺少 3-seed 统计（NER 有 mean±σ + Fisher p，RE 仅 seed=42 单点值），进一步削弱 RE 结论基础。

### 与 R1 的主要分歧

Overall 评分差异（R1: 3.5 vs R2: 2.5），原因：
1. 我识别了 **页数严重超限**（估计 10-11 页，超限 2-3 页）——R1 未提及此问题
2. 我认为 **contribution framing** 存在根本问题（4/5 信号的 selection 失败是定义必然，被包装为经验发现）——R1 虽在 N1 中触及了方法论层面，但未挑战 framing 本身
3. 我认为标题 "Do Not Select" **overclaim**（论文自身发现 LP 在非 tied 子集上 significantly selects）

如果页数合规 + framing 重新聚焦 + 标题 softened，我的评分可上调至 3/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 837 · 2026-05-15T15:09:05.237288+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 838 · 2026-05-15T15:09:05.388353+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"projects/struct_self_consist_ie/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026 Findings\", \"requested_at\": \"2026-05-15T14:58:31.045041+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_1b56445332d8ca2b4964b30f300f0e00\", \"skipped_at\": \"2026-05-15T14:58:58.728344+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 839 · 2026-05-15T15:15:53.602557+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-7) =====\n- id: R0-C1\n  summary: 模型规模单一（仅 8B）\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性\n  - round: 1\n    reviewers: [1, 2]\n    note: model-agnostic 与 Limitations 矛盾\n  action_items:\n  - round: 1\n    action: 全文替换 model-agnostic → consistent across tested model families\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 确认措辞修正到位，无再提\n  resolution_round: 2\n- id: R0-C2\n  summary: 相关工作显著遗漏\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 5 篇核心文献缺失\n  - round: 1\n    reviewers: [1, 2]\n    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC\n  action_items:\n  - round: 1\n    action: 补充 6 篇引用到 Related Work\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'\n  resolution_round: 2\n- id: R0-C3\n  summary: RE 结论仅基于 SciERC 单数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 4\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 需跨数据集验证或降级措辞\n  - round: 2\n    reviewers: [1, 2]\n    note: Abstract RE 措辞需修正\n  - round: 3\n    reviewers: [1, 2]\n    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\n  action_items:\n  - round: 1\n    action: 降级措辞 universal → observed in SciERC\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: Abstract 改为 NER (three datasets) and RE (SciERC)\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 'Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议'\n  resolution_round: 4\n- id: R0-C4\n  summary: SJ 方法新颖性有限\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [2]\n    note: Nedellec 增量贡献论证不足 + 引用错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强增量贡献论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认三点差异化清晰\n  resolution_round: 2\n- id: R0-C5\n  summary: 全文零图表\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 缺少 selection curves、reliability diagrams\n  action_items: []\n  resolution: 论文已包含 6 个 figures\n  resolution_round: 1\n- id: R0-C6\n  summary: 成本分析 negligible 误导\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 8-16× 推理开销不应描述为 negligible\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W1\n  summary: 未探索 signal combination\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: 互补性已证明但未尝试组合\n  action_items: []\n  resolution: Round 1+ 未再提及\n  resolution_round: 1\n- id: R0-W4\n  summary: 统计检验不系统\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Bootstrap 细节不足\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 bootstrap 达到高标准\n  resolution_round: 2\n- id: R0-RR-D1\n  summary: Voting Conf N-scaling +0.018 与数据矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  mentions:\n  - round: 0\n    reviewers: [Research Reviewer]\n    note: +0.018 实际为 -0.080\n  action_items:\n  - round: 0\n    action: 修正声明\n    assigned_to: Main Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 1\n- id: R1-N1\n  summary: Bootstrap 检验细节不足\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: p=0.39 支撑核心结论但细节缺失\n  action_items:\n  - round: 1\n    action: 补完整 bootstrap 规范\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价统计规范达到高标准\n  resolution_round: 2\n- id: R1-N2\n  summary: Gap 解释力不足 + logprob 失败未分析\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 4/5 定义性 + logprob 机制缺失\n  action_items:\n  - round: 1\n    action: 区分 by-design vs empirical + logprob failure 分析段\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 Reviewer 评价 logprob failure analysis 充分\n  resolution_round: 2\n- id: R1-N3\n  summary: Per-sample signal 单薄\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: consensus-proximity = LOO-SJ 是表述问题\n  action_items:\n  - round: 1\n    action: 显式说明等价关系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 consensus-proximity = LOO-SJ 已明确\n  resolution_round: 2\n- id: R1-N4\n  summary: Nedellec 引用错误 + 增量贡献弱\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Yao vs Nédellec 事实错误\n  action_items:\n  - round: 1\n    action: 修正 bib + 加强论证\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认差异化清晰\n  resolution_round: 2\n- id: R1-W1\n  summary: SJ 形式化有歧义\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: Hungarian threshold + max denominator 需补充\n  - round: 3\n    reviewers: [1, 2]\n    note: R3-R1 再次指出 Hungarian cost function 未明确\n  - round: 4\n    reviewers: [2]\n    note: R2 Round 4 确认 SJ 形式化已完善\n  action_items:\n  - round: 1\n    action: 补全 Eq(4) 定义\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 2\n    action: 补 threshold 说明 + max vs union 设计理由\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 3\n    action: 补 Hungarian optimization objective + zero-IoU pairs handling\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 'Round 4: R2 确认 SJ 形式化已完善'\n  resolution_round: 4\n- id: R1-W2\n  summary: Voting-SJ 冗余度未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: instance-level correlation 未报告\n  action_items:\n  - round: 1\n    action: 报告 Voting-SJ ρ=0.659/0.605\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 中等相关数据已报告\n  resolution_round: 2\n- id: R1-W3\n  summary: ρ=0.38 缺 contextualization\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 cross-method footnote\n  action_items:\n  - round: 2\n    action: '§5 footnote: semantic entropy AUROC comparison'\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R1-W4\n  summary: Logprob 温度数据缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: robustness 结论需限定\n  action_items:\n  - round: 1\n    action: 限定为 consistency-based signals robust\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 措辞限定到位\n  resolution_round: 2\n- id: R1-W5\n  summary: WNUT-17 establishing 措辞过度\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: fail to reject ≠ accept\n  action_items:\n  - round: 1\n    action: establishing → consistent with/suggests\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R1-W6\n  summary: LLaMA 训练设置不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: LLaMA fine-tuning 状态未说明\n  action_items:\n  - round: 1\n    action: 明确两模型 identical LoRA 配置\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 未再提及\n  resolution_round: 2\n- id: R1-W7\n  summary: 约束解码 diversity 影响\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展为全局 confound + Limitations 条目\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 新增条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已扩展为全局 confound 讨论\n  resolution_round: 2\n- id: R1-W8\n  summary: first systematic 过强\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 需收窄 scope\n  action_items:\n  - round: 1\n    action: first multi-family\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 无再提\n  resolution_round: 2\n- id: R1-W9\n  summary: 遗漏引用\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: Optimal SC, Difficulty-Adaptive SC 等\n  action_items:\n  - round: 1\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认无遗漏\n  resolution_round: 2\n- id: R1-W10\n  summary: ρ-AUROC dissociation 分析浅\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: EM=1 压缩效应需主文提及\n  action_items:\n  - round: 1\n    action: Section 5 简述 + 引导 Appendix\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Round 2 确认 dissociation 分析为 actionable finding\n  resolution_round: 2\n- id: R1-M1\n  summary: Logistic regression proxy 无结果\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 展示结果或删除\n  action_items:\n  - round: 1\n    action: 删除提及\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已删除\n  resolution_round: 2\n- id: R1-M2\n  summary: GSM8K +18pp 未注明模型\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: 补注 PaLM-540B\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R1-M3\n  summary: Cross-model Δ=0.005 未报告 CI\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n  - round: 1\n    reviewers: [1, 2]\n    note: within 3-seed σ≈0.007\n  action_items:\n  - round: 1\n    action: 补注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补注\n  resolution_round: 2\n- id: R2-C1\n  summary: Selection 证据面过窄\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需补 LLaMA SciERC + CoNLL selection\n  action_items:\n  - round: 2\n    action: 补 4 配置 selection 分析\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 6 configurations 全部补齐\n  resolution_round: 2\n- id: R2-C2\n  summary: WNUT-17 仅报告 1 个信号\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 5 signals 中仅 SJ\n  action_items:\n  - round: 2\n    action: 补全 5 信号\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: WNUT-17 全信号表完整\n  resolution_round: 2\n- id: R2-W1\n  summary: ρ=0.38 缺 cross-method 对比\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 footnote 引用 semantic entropy AUROC\n  action_items:\n  - round: 2\n    action: §5 footnote\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Footnote 已加\n  resolution_round: 2\n- id: R2-W2\n  summary: N=8 QE ρ 无 uncertainty\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap CIs\n  action_items:\n  - round: 2\n    action: 计算 B=10,000 bootstrap CI\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: Bootstrap CI 表已加入 Appendix\n  resolution_round: 2\n- id: R2-W3\n  summary: SJ Hungarian threshold + max denominator\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 无 threshold 声明需验证\n  action_items:\n  - round: 2\n    action: 代码验证 + method.tex 补充\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 无 threshold, max denominator 已解释\n  resolution_round: 2\n- id: R2-W4\n  summary: RE selection 无统计检验\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需 bootstrap p-value\n  action_items:\n  - round: 2\n    action: RE bootstrap\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: RE logprob p=0.80\n  resolution_round: 2\n- id: R2-W5\n  summary: Constrained decoding 全局 confound\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 需扩展到全局 + Limitations\n  action_items:\n  - round: 2\n    action: Discussion 扩展 + Limitations 条目\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已处理\n  resolution_round: 2\n- id: R2-W6\n  summary: Abstract RE 措辞误导\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: NER (three datasets) and RE (SciERC)\n  action_items:\n  - round: 2\n    action: 修正 Abstract\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 2\n- id: R2-W7\n  summary: n=529 vs 551 未解释\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [1, 2]\n    note: 22 instances filtering criteria\n  action_items:\n  - round: 2\n    action: 补一句说明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已说明 gold-empty filtering\n  resolution_round: 2\n- id: R2-DATA\n  summary: RE selection 数据矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: Table 2 vs L129 矛盾\n  action_items:\n  - round: 2\n    action: Agent 确认 Table 2 正确\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 数据已统一\n  resolution_round: 2\n- id: R2-AUROC\n  summary: L64 AUROC 归属错误\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n  - round: 2\n    reviewers: [Research Reviewer]\n    note: corresponding 暗示同一信号\n  action_items:\n  - round: 2\n    action: 分别标注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已拆分归属\n  resolution_round: 2\n- id: R3-C1\n  summary: Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: constrained decoding 可能压缩 per-sample diversity\n  - round: 4\n    reviewers: [1, 2]\n    note: R2 确认部分解决\n  - round: 5\n    reviewers: [1, 2]\n    note: Round 5 两位 Reviewer 再次独立提出\n  - round: 6\n    reviewers: [1, 2]\n    note: R1 列 critical。R2 rebut 降为 should-fix\n  action_items:\n  - round: 3\n    action: Agent 量化 diversity\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 4\n    action: 量化 logprob 分布\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  - round: 5\n    action: Title/Abstract/Conclusion 限定 claim scope\n    assigned_to: Paper Agent\n    status: resolved\n  - round: 6\n    action: Introduction 和 Discussion 声明\n    assigned_to: Paper Agent\n    status: superseded\n  resolution: exp-018 free-form ablation 证明 gap task-intrinsic\n  resolution_round: 7\n- id: R3-C2\n  summary: Failure-to-reject 不等于 evidence of absence\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需修改措辞或补充等价性检验\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 修改措辞 + TOST\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: TOST 等价检验已补充\n  resolution_round: 4\n- id: R3-C3\n  summary: N=8 核心结果 single seed\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: Table 1 N=8 和 Table 2 全部 single seed\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: Limitations 中明确 single-seed 风险\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 3-seed 稳定性验证已补充\n  resolution_round: 4\n- id: R3-W1\n  summary: 多重比较校正缺失\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: SJ-EM 在 Bonferroni 下不 survive\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 声明未做多重比较校正\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Bonferroni 声明已加\n  resolution_round: 4\n- id: R3-W3\n  summary: Consensus-proximity 未与 MBR 建立联系\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: MBR 未讨论\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 明确与 MBR 联系\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §5 MBR decoding 连接段已写入\n  resolution_round: 4\n- id: R3-W6\n  summary: First multi-family comparison claim scope 过宽\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需限定为 structured IE\n  - round: 7\n    reviewers: [1]\n    note: 论文当前版本未声称 first\n  action_items:\n  - round: 5\n    action: 去掉 first claim\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: introduction.tex 无 first claim\n  resolution_round: 7\n- id: R3-W7\n  summary: 术语不一致\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 本轮未提及，全文一致使用 VC/SJ/FK/EM/LP\n  action_items:\n  - round: 6\n    action: 全文统一缩写\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 全文一致\n  resolution_round: 7\n- id: R3-W8\n  summary: 遗漏引用 VerifiNER, RASC, MBR, Malinin\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [2]\n    note: R2 确认 RESOLVED\n  action_items:\n  - round: 3\n    action: 补充引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 引用已补全\n  resolution_round: 4\n- id: R3-M1\n  summary: WNUT-17 54% 与数据不一致\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 355/689 ≈ 51.5% vs 54%\n  action_items:\n  - round: 3\n    action: Agent 核实\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: 54% → 52% 已修正\n  resolution_round: 4\n- id: R3-M2\n  summary: EM selection exclusion 缺乏支持\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告频率\n  action_items:\n  - round: 3\n    action: 计算 exact match 频率\n    assigned_to: Agent + Paper Agent\n    status: resolved\n  resolution: EM 已加入 Table 2\n  resolution_round: 4\n- id: R3-M3\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [2]\n    note: Ethics Statement 现为独立 section\n  action_items:\n  - round: 4\n    action: 移出为独立 section\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Ethics Statement 已为独立 section\n  resolution_round: 5\n- id: R3-M4\n  summary: ρ-AUROC dissociation 过度强调\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 承认统计预期性\n  action_items:\n  - round: 3\n    action: §4.2 承认\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已承认\n  resolution_round: 4\n- id: R3-M5\n  summary: Nedellec 措辞偏 adversarial\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 用更 neutral 语气\n  action_items:\n  - round: 3\n    action: 改为 neutral\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已修正\n  resolution_round: 4\n- id: R3-M6\n  summary: LOO-SJ Δρ 量纲混淆\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: Δρ vs per-instance max\n  action_items:\n  - round: 3\n    action: 澄清含义\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已澄清\n  resolution_round: 4\n- id: R3-M7\n  summary: Figure 1 caption 引入未直接可视化的 p=0.39\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n  - round: 3\n    reviewers: [1]\n    note: 补交叉引用\n  action_items:\n  - round: 3\n    action: 补 (Table 2) 交叉引用\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已补\n  resolution_round: 4\n- id: R4-C1\n  summary: 训练配置和 prompt template 缺失\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Appendix E 已包含 Table 8\n  action_items:\n  - round: 4\n    action: 附录补充完整训练配置表\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix E Table 8 完整\n  resolution_round: 5\n- id: R4-M1\n  summary: SJ normalizer 选择（max vs union）缺乏对比\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n  - round: 4\n    reviewers: [1]\n    note: 未比较\n  action_items:\n  - round: 4\n    action: 附录补结果或提供理论依据\n    assigned_to: Agent + Paper Agent\n    status: wont_fix\n  resolution: max normalizer 设计已有理由，超出 scope\n  resolution_round: 4\n- id: R4-M3\n  summary: Table 1 N=16 block 空白\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: Table 1 仅含 N=8，N=16 在 Appendix\n  action_items:\n  - round: 6\n    action: Table 1 删除 N=16 行\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: N=16 委托至 Appendix\n  resolution_round: 7\n- id: R4-W2\n  summary: SJ vs EM 应改为 difficulty-dependent complementarity\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: §4.2 已使用 complementarity 措辞\n  action_items:\n  - round: 4\n    action: 弱化 structural advantage\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: complementarity 措辞到位\n  resolution_round: 5\n- id: R4-W4\n  summary: 缺少 Xiong et al. (2024)\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n  - round: 5\n    reviewers: [1, 2]\n    note: Related Work 已引用\n  action_items:\n  - round: 4\n    action: 引用 Xiong et al.\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 已引用\n  resolution_round: 5\n- id: R5-W1\n  summary: Qwen3-8B thinking token 训练不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: §4.1 现已显式声明，Limitations 讨论\n  action_items:\n  - round: 6\n    action: Experiments Setup 中显著声明\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: experiments.tex 明确声明 + limitations.tex 讨论\n  resolution_round: 7\n- id: R5-W2\n  summary: Semantic entropy 脚注比较可能误导\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 脚注已缩短\n  action_items:\n  - round: 6\n    action: 缩短脚注\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 脚注已缩短\n  resolution_round: 7\n- id: R5-W3\n  summary: he2024uncertainty bib entry 不匹配\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: R1 验证通过\n  action_items:\n  - round: 5\n    action: 修正引用上下文\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 正确指向 Findings of NAACL 2024\n  resolution_round: 7\n- id: R5-M3\n  summary: LOO-SJ 等价性缺少推导\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: Appendix D 已包含\n  action_items:\n  - round: 5\n    action: 附录补简要推导\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Appendix D 完整等价性证明\n  resolution_round: 6\n- id: R5-M4\n  summary: 部分 bib entries 在 OpenAlex 未找到\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 62 篇全部通过验证\n  action_items:\n  - round: 6\n    action: 核实 bib entries\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 62 篇引用全部通过验证\n  resolution_round: 7\n- id: R5-M5\n  summary: Ethics Statement 仅 2 句\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 包含 CoNLL Reuters 出处\n  action_items:\n  - round: 6\n    action: 补充 CoNLL Reuters license\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 实质性内容完整\n  resolution_round: 7\n- id: R5-Q4\n  summary: WNUT-17 logprob 负相关机制未解释\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: §4.2 已加机制假设\n  action_items:\n  - round: 5\n    action: 加机制解释\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: §4.2 已包含 overconfidence 假设\n  resolution_round: 6\n- id: R5-C1\n  summary: Constrained decoding 混淆变量 claim scope 不匹配\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n  - round: 6\n    reviewers: [1, 2]\n    note: 与 R3-C1 合并\n  action_items:\n  - round: 5\n    action: Title 加限定\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-C1 合并。Free-form ablation 证明 task-intrinsic\n  resolution_round: 7\n- id: R6-W2\n  summary: Figure 1 caption 冗余\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 2 句简洁 caption\n  action_items:\n  - round: 6\n    action: 精简 caption\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 2 句简洁 caption\n  resolution_round: 7\n\n# ===== IN-PROGRESS ISSUES (updated with Round 8) =====\n- id: R3-W2\n  summary: Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需在 Discussion 中分离两层论证\n  - round: 4\n    reviewers: [1, 2]\n    note: Introduction 未正面论证 why not obvious a priori\n  - round: 5\n    reviewers: [1, 2]\n    note: R2 认为 gap 被两头夹击。R1 rebut：consensus-proximity/MBR failure 是 non-trivial\n  - round: 6\n    reviewers: [1, 2]\n    note: 应先 dismiss instance-level，聚焦 consensus-proximity failure 和 logprob score compression\n  - round: 7\n    reviewers: [1, 2]\n    note: 需根本性 reframing——dismiss instance-level failure in one sentence\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N2（论文将 4/5 definitional failure 与 LP/MBR empirical failure 混为统一 finding）。R1 rebut（三处透明声明不构成误导，两层结构有信息量），但 agree 可改善呈现（如 Table 3 用水平线分隔 instance-level 和 per-sample）。分歧记录：R2 认为根本 framing 错误，R1 认为呈现改进问题。'\n  action_items:\n  - round: 7\n    action: 根本性 reframing——以 LP compression + MBR failure 为核心\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少在 Table 3 中用视觉分组区分 instance-level 和 per-sample 信号；考虑 Abstract/Introduction 更突出两层区分\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W4\n  summary: FK 独立性假设 justification 不足\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: 需报告 inter-sample correlation\n  - round: 7\n    reviewers: [1, 2]\n    note: n=5 t-test 功效极低\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W2 再次提出（n=5 t-test 应改用 instance-level 检验 n=529+）。R2 agree with nuance。共识：当前 justification 不足。'\n  action_items:\n  - round: 7\n    action: 改用 permutation test 或 bootstrap CI\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 改用 instance-level 检验（n=529+），或在论文中降级 FK 独立性声称为 approximate justification\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R3-W5\n  summary: Cross-model 实为 cross-architecture at fixed 8B scale\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope 问题\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 N3 标题 \"8B-Scale\" 过度泛化暗示。R1 rebut：8B-Scale 是描述性限定非泛化声明，去掉反而更误导。共识：保留 8B-Scale，修改 Do Not Select。'\n  action_items:\n  - round: 7\n    action: 标题 scope down\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 保留 8B-Scale 限定；修改 Do Not Select 为更 hedged 表述（如 Struggle to Select）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-M2\n  summary: TOST δ 选择缺乏实践意义论证\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: δ 循环锚定于 oracle headroom\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W4 再次提出（需外部实际意义基准）。R2 agree。\n  action_items:\n  - round: 7\n    action: 用外部标准替代 oracle headroom 锚定\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W1\n  summary: RE 证据需进一步加强（consistent preliminary 标注）\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: RE 标注不一致\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 列 critical：Table 3 RE 仅 seed=42 单种子，Abstract 未标 preliminary。R2 W5 同意 + 补充 Table 2 RE 缺 3-seed。共识：Abstract 必须标注 RE preliminary。'\n  action_items:\n  - round: 7\n    action: 全文 RE 引用一致标注\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: Abstract 增加 RE preliminary 标注；Table 3 RE 补 3-seed 或明确标注 single seed\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R4-W3\n  summary: Abstract 过于密集\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 精简为问题-发现-意义三段式\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W1 再次提出（5 signal names + 3 datasets + 4 metrics 过多）。R1 agree。共识：删减具体数值，信号名称移至 Introduction。'\n  action_items:\n  - round: 8\n    action: Abstract 精简为 问题-发现-意义，移除大部分具体数字和信号缩写\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-N1\n  summary: 与 Nédellec et al. (2026) 的增量贡献不充分\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 如果核心贡献 reframe 为 LP compression + MBR failure，此问题自然缓解\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。可能通过 R3-W2 reframing 间接缓解。\n  action_items:\n  - round: 6\n    action: 降低 Contribution 1 claim 强度\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-C2\n  summary: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W2 合并追踪。见 R3-W2 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W2 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W4\n  summary: First multi-family comparison claim = scope engineering\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 与 R3-W6 合并。论文当前版本未含 first claim。\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。R3-W6 已 resolved。\n  action_items:\n  - round: 5\n    action: first → a systematic\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: 与 R3-W6 合并。论文当前版本无 first claim。\n  resolution_round: 7\n- id: R5-W5\n  summary: Cross-architecture 用词过度\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 标题 scope\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W5 合并追踪。见 R3-W5 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W5 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W6\n  summary: FK independence justification 不够严格\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 与 R3-W4 合并追踪。见 R3-W4 Round 8 mention。\n  action_items:\n  - round: 6\n    action: 见 R3-W4 action\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-W7\n  summary: SJ 方法论新颖性有限\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 未直接提及\n  - round: 8\n    reviewers: [2]\n    note: 'R2 W3 再次提出（标准技术组合）。R1 rebut：论文未将 SJ 作为方法论贡献，且 type-aware bipartite matching + IoU 在 IE 一致性文献中未见先例。分歧记录。'\n  action_items:\n  - round: 5\n    action: core → primary structural signal\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R5-M1\n  summary: 缺少 test-time scaling survey 引用\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: []\n    note: 论文 Related Work 已引用 zhang2025tts\n  - round: 8\n    reviewers: []\n    note: 本轮未提及。已引用。\n  action_items:\n  - round: 6\n    action: 补充 Zhang et al. (2025)\n    assigned_to: Paper Agent\n    status: resolved\n  resolution: Related Work 已引用 zhang2025tts\n  resolution_round: 8\n- id: R5-M2\n  summary: 缺少 MBR 在非 MT 任务中的应用引用\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [2]\n    note: Eikema 仅在 Discussion\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4（Eikema 应前移到 Related Work）。R1 agree。共识。与 R7-W3 合并追踪。'\n  action_items:\n  - round: 7\n    action: 将 eikema2025structured 前移到 Related Work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R6-W1\n  summary: VC 公式（Eq.6）与实现不一致\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: Table 3 标注不清\n  - round: 8\n    reviewers: []\n    note: 本轮未直接提及。论文 Footnote 2 报告了两种实现的 ρ 差异。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: Table 3 caption 明确标注 VC selection 使用 majority threshold\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C1\n  summary: Selection gap 分析缺乏多种子验证\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 核心 selection failure 仅 seed=42\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N3 间接触及（Table 3 RE 仅 seed=42）。R2 补充 Table 2 RE 也缺 3-seed。两位 Reviewer 未将 NER selection multi-seed 作为独立 critical 提出——论文已有 3-seed NER selection data（Table 3 mean±σ + Fisher p），焦点转移到 RE 单种子问题。'\n  action_items:\n  - round: 7\n    action: 将 3-seed 分析扩展至 Table 3\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C2\n  summary: ε=0.05 effectively tied 阈值缺乏论证\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 59× 跳变，abstract 数字依赖 arbitrary cutoff\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N1 列 critical：ε=0.05 选在中位数附近 (0.041) by construction 保证 ≥50% tied。R2 agree with nuance：循环论证成立但不影响 non-tied subset conditional diagnostic (+2.9pp, p=0.01)。共识：需补充完整 ε 梯度 + 外部基准。论文 Appendix G 已有 CDF 图和 Table 12。'\n  action_items:\n  - round: 7\n    action: 提供 LP range 完整 CDF 或连续度量替代二元划分\n    assigned_to: Agent + Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 突出已有 CDF（Appendix G）；(b) 正文用连续度量（median LP range + IQR）补充二元划分；(c) 提供外部基准（QA/MT LP range）；(d) abstract 避免依赖单一 cutoff 的数字\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-C3\n  summary: Free-form ablation 范围过窄但支撑过强泛化声称\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 1 dataset × 1 model × 1 seed\n  - round: 8\n    reviewers: [1, 2]\n    note: R1 W1 再次提出（RE LP 翻转需 3-seed）。R2 agree（NER 结论可保留，RE 翻转需承认）。\n  action_items:\n  - round: 7\n    action: 降级 fundamental/intrinsic 措辞\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) 明确承认 RE LP 翻转 + CI；(b) RE free-form 行为列为 future work\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W1\n  summary: LP 温度敏感性完全缺失\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: LP 是核心诊断对象但无 T=0.7 数据\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 N2 列 critical：Section 4.4 \"robust across T\" 易误读为含 LP。R2 agree (high severity)。共识：仅次于页数超限的第二大方法论问题。'\n  action_items:\n  - round: 7\n    action: Limitations 中充分讨论\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: (a) Section 4.4 robustness 声明明确排除 LP；(b) Limitations 扩展 LP 温度讨论；(c) 引用 free-form ablation std ratio 0.97 作为间接证据\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W2\n  summary: Contribution 1 定性有分歧\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: engineering benchmark vs methodological contribution\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W2 再次提出（methodology 非 conceptual contribution）。R1 rebut：metric dissociation（EM AUROC 0.749 but ρ #3）是 empirical finding 对 practitioners 有价值。共识未达成：R2 建议降格为 finding，R1 认为措辞可改但不应降格。分歧记录。'\n  action_items:\n  - round: 7\n    action: 考虑将 Contribution 1 从 contribution 降级\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 8\n    action: 至少改措辞为以发现为主语的表述（如 \"We find that metrics decouple\" 而非 \"Multi-metric evaluation revealing...\"）\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W3\n  summary: Eikema et al. (2025) 应前移到 Related Work\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: 仅在 Discussion 出现\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W4 再次提出。R1 agree。共识：在 Related Work MBR 段扩展讨论。'\n  action_items:\n  - round: 8\n    action: Related Work §2 MBR 段增加 2-3 句讨论 Eikema et al. (2025) 并明确互补关系\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n- id: R7-W4\n  summary: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n  - round: 7\n    reviewers: [Research Reviewer]\n    note: Appendix 模型名错误\n  - round: 8\n    reviewers: []\n    note: 本轮未检查。待 Research Director 确认。\n  action_items:\n  - round: 7\n    action: 全文搜索替换\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 8) =====\n- id: R8-N1\n  summary: 正文页数严重超过 8 页限制（估计 10-11 页）\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N1：正文 7 个 section + 3 个 figure* + 1 个 table* + 6 equations，估计 10-11 页超限 2-3 页。R1 agree：Discussion ablation 和 decoding interaction 段落（合计约 1 页）可移至 Appendix。ARR 超页是 desk-rejection 理由。'\n  action_items:\n  - round: 8\n    action: '压缩至 ≤8 页：(1) Discussion free-form ablation 详述移至 Appendix；(2) Robustness 数字精简；(3) Introduction contribution bullets 压缩具体数字；(4) Experiments seed variability 段落精简'\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-N2\n  summary: 标题 \"Do Not Select\" overclaim——论文自身数据显示 LP 在子集上 significantly selects\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 列 critical N3：\"Do Not Select\" 是绝对否定，但 LP 在非 tied 子集 +2.9pp (p=0.01)，RE 在 free-form 下翻转为正。R1 agree with qualification：Do Not Select 需 softening，但 8B-Scale 是描述性限定应保留。共识：修改 Do Not Select。'\n  action_items:\n  - round: 8\n    action: '标题修改：Do Not Select → Struggle to Select / Fail to Select Under Score Compression 或类似 hedged 表述；保留 8B-Scale'\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-W1\n  summary: 缺少代码/数据发布承诺\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W6 提出。R1 agree。ARR reproducibility checklist 要求。论文使用公开数据集 + 开源模型但未承诺发布自定义代码。'\n  action_items:\n  - round: 8\n    action: 添加 Code and Data 段落说明发布计划\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-W2\n  summary: enable_thinking 对 LP score distribution 的影响未量化\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 W7 提出。R1 agree with qualification：论文辩护逻辑合理（CoNLL/WNUT 无 confound 但 LP 同样失败），但未量化 thinking tokens 对 LP range 的影响。median LP range 仅 0.041 nats，4-5 个 empty tokens 的 LP 贡献可能 non-negligible。'\n  action_items:\n  - round: 8\n    action: 补充 SciERC LP 分布对比（thinking vs non-thinking），或论证 4-5 tokens 在 1500+ tokens 中被稀释到可忽略\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-W3\n  summary: SJ max normalizer 未做 sensitivity analysis / ablation\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R1 W5 和 R2 M2 均提出。max(|g_i|,|g_j|) vs |g_i∪g_j| 对结果影响未知。R4-M1 (wont_fix) 仅提供设计理由但无对比数据。'\n  action_items:\n  - round: 8\n    action: 至少在 Appendix 报告 union normalizer 的 ρ 对比，或解释为何差异可忽略\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-W4\n  summary: Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W3：Limitations 提到 <0.3pp F1 差异但未讨论对 LP distribution 的影响。joint decoding 生成更长输出（含 RE），可能改变 LP range。'\n  action_items:\n  - round: 8\n    action: 报告 seed 456 的 LP range 对比数据或论证影响可忽略\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-W5\n  summary: N=8 QE 主表单种子 vs N=16 多种子设计不对称\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1]\n    note: 'R1 W6：Table 1 N=8 仅 seed=42，Table 10 multi-seed 仅覆盖 QE 非 selection。设计不对称。'\n  action_items:\n  - round: 8\n    action: 说明 N=8 单种子 + N=16 多种子的设计理由，或补充 N=8 multi-seed QE 数据\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: R8-M1\n  summary: nedellec2026 bib key 与实际第一作者不一致\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n  - round: 8\n    reviewers: [1, 2]\n    note: 'R2 M6 提出，R1 agree：bib key nedellec2026 但第一作者 Yao, Xinzhi。应修正为 yao2026consistency。'\n  action_items:\n  - round: 8\n    action: 修正 bib key\n    assigned_to: Paper Agent\n    status: open\n  resolution: ''\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 840 · 2026-05-15T15:15:53.856318+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 45806}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 841 · 2026-05-15T15:17:58.482317+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:submit_review_report_to_research_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 842 · 2026-05-15T15:17:58.533539+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 843 · 2026-05-15T15:18:01.299818+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 844 · 2026-05-15T15:18:01.350720+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 845 · 2026-05-15T15:19:33.134908+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 8 Consolidated Review Report\n\n**Paper**: \"Strong Predictors, Weak Selectors: Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction\"\n**Venue**: EMNLP 2026 Findings (ARR May cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法+实验), R2 (新颖性+写作+格式)\n**Protocol**: 独立初审 → 交叉分享 → 收敛（1轮达成共识，无需第2轮）\n\n---\n\n## Summary\n\n本文系统评估了五种置信度信号（VC、SJ、FK、EM、LP）在 LLM 结构化信息抽取中的质量估计、二元判别和样本选择三个维度上的表现。核心发现为\"correlation-selection gap\"——所有信号在质量估计上表现良好（ρ 最高 0.38，AUROC 最高 0.75），但在样本选择上均未能显著优于 greedy baseline，尽管存在 12-18pp 的 oracle headroom。论文提出两层解释：(1) 四个信号为 instance-level 聚合，定义上无法排序候选；(2) LP 分数严重压缩（60% 实例有效并列）。实验覆盖 2 个模型族（Qwen3-8B, LLaMA-3.1-8B）、3 个数据集（SciERC, CoNLL-2003, WNUT-17）、N=8/16 两个采样规模。\n\n---\n\n## Strengths\n\n**S1. 系统性实验设计（两位 Reviewer 共识）**\n5 信号 × 3 维度 × 3 数据集 × 2 模型的全因子设计，覆盖面在同类工作中罕见。bootstrapped CI、paired permutation test、3-seed 稳定性分析等统计方法规范。\n\n**S2. 核心发现具有实用价值**\nCorrelation-selection gap 的发现对 self-consistency 方法的实际部署有直接指导意义——警示从业者不能仅凭 rank correlation 选择信号。\n\n**S3. 多层次诊断分析**\n从定义层（instance-level 信号无法排序候选）到机制层（LP 压缩、MBR 效用-质量错位）的分层解释，提供了比单纯报告现象更深的理解。\n\n**S4. 透明的局限性讨论**\nLimitations 部分涵盖 RE 单基准、模型规模限制、温度未测试、enable_thinking 不一致等，展现了诚实的自我评估。\n\n**S5. Ablation 设计有价值**\nFree-form ablation 排除了 constrained decoding 作为 LP 压缩的唯一来源，non-tied LP 子集的显著性分析（+2.9pp, p=0.01）为机制解释提供了关键证据。\n\n---\n\n## Weaknesses\n\n### Critical（必须修复）\n\n**C1. 页数严重超限 [R1+R2 共识]**\n正文（Abstract 至 Conclusion）估计为 10-11 页，超出 ARR/EMNLP 8 页限制 2-3 页。这是格式硬性要求，desk reject 风险极高。\n- R1: 需要大幅压缩 experiments 和 discussion\n- R2: 必须砍到 8 页，建议将 free-form ablation 详情、N-scaling 细节、部分表格移入 appendix\n\n**C2. ε=0.05 \"effectively tied\" 阈值循环论证 [R1 提出, R2 同意]**\nLP 压缩的核心量化依赖 ε=0.05 阈值，但该阈值缺乏独立于数据的 justification。论文未提供 ε sensitivity analysis（不同 ε 下 tied fraction 如何变化），使\"60% tied\"这一关键数字的可信度受损。R1 建议补充 ε sweep 图表。\n\n**C3. LP 温度 T=0.7 数据缺失 [R1 提出, R2 同意]**\n温度比较实验（T=0.7 vs T=1.0）中 LP 被排除（因缺少 T=0.7 LP 数据）。这恰好是 LP 压缩与温度交互效应的关键缺失——practitioners 通常在 T<1.0 部署，LP 在低温下的表现直接影响论文结论的实用性。Limitations 已提及但仅作为\"unknown\"处理，不足以弥补。\n\n**C4. RE 结论基于单基准+单 seed（部分场景）[R1+R2 共识]**\nRE 仅在 SciERC 上评估（且 40% 实例 F1=0），free-form ablation RE 选择方向逆转基于单 seed。论文在多处声称 RE 为 \"preliminary\"，但标注不一致——abstract 和部分正文中未标注。所有 RE claim 必须统一标注 preliminary。\n\n### Major（强烈建议修复）\n\n**M1. 标题 \"Do Not Select\" 过度断言 [R2 提出, R1 部分同意]**\n标题断言信号\"不能选择\"，但 non-tied LP 子集确实能选择（+2.9pp, p=0.01），且论文仅测试了 unsupervised 信号。R1 认为当前标题可接受但可改进为更精确的表述。R2 认为标题与论文自己的证据矛盾。建议修改为反映条件性失败的表述。\n\n**M2. Abstract 信息过载 [R1+R2 共识]**\n10 行 abstract 塞入 5 个信号名、3 个数据集、2 个模型、4 个指标的具体数值，first-pass 可读性差。建议精简到核心 narrative：gap 存在 → 诊断原因 → 实用影响。\n\n**M3. Framing 问题：贡献 C1 的性质 [R1、R2 分歧，见下]**\nR2 认为 C1（instance-level 信号无法排序候选）是定义推导而非实证贡献，将其列为\"贡献\"存在 framing 误导；R1 认为 definition-level 诊断本身有价值但同意措辞可改进。论文需要更清晰地区分 definitional vs empirical 贡献。\n\n**M4. Eikema & Aziz (2022) MBR 讨论位置不当 [R1+R2 共识]**\nMBR decoding 连接出现在 Discussion 而非 Related Work，使读者在 §5 才发现这一重要理论关联。建议在 Related Work 中增加 MBR/utility-based selection 子节。\n\n**M5. 缺少代码/数据发布声明 [R2 提出, R1 同意]**\n论文未包含代码或数据发布声明。ARR review form 明确询问 reproducibility resources。即使匿名期无法提供链接，也应声明提交时或录用后会发布。\n\n### Minor\n\n**W1. enable_thinking 对 LP 的潜在影响**\nQwen3-8B SciERC checkpoint 训练时有空 `&lt;think>&lt;/think>` 块，可能影响 first-token 概率分布。虽然 Limitations 中已讨论，但未定量评估影响大小。\n\n**W2. Free-form ablation 范围窄**\n仅在 SciERC + Qwen3-8B 上进行，泛化性未验证。\n\n**W3. FK t-test 统计功效不足**\nSciERC RE 的 FK t-test 可能样本量不足，p 值接近临界值时可信度受限。\n\n**W4. TOST δ 锚定**\n等价性检验的 δ 选择缺乏先验 justification。\n\n**W5. SJ 的 Hungarian 算法匹配**\nSJ 使用 Hungarian 算法做 token-level IoU 匹配，计算复杂度 O(n³)，论文未讨论 scalability。\n\n---\n\n## Reviewer Consensus（共识区）\n\n以下问题两位 Reviewer 完全一致：\n1. **页数超限是 desk reject 级问题**，必须在提交前解决\n2. **ε=0.05 需要 sensitivity analysis** 或独立于数据的 justification\n3. **LP T=0.7 缺失**是对实用性的重大限制\n4. **RE preliminary 标注必须全文一致**\n5. **Abstract 需精简**，减少具体数值堆砌\n6. **Eikema MBR 讨论应前移到 Related Work**\n7. **需要代码发布声明**\n8. **核心实验设计和统计方法扎实**\n\n---\n\n## Reviewer Divergence（分歧区）\n\n**D1. Framing 严重程度**\n- R2 (2.5/5): 认为 framing 存在根本性问题——将定义推导包装为实证贡献，标题与证据矛盾，整体叙事需要重构\n- R1 (3.5/5): 认为是表述改进问题而非根本缺陷，核心发现的价值不受 framing 影响\n\n**D2. 贡献 C1 的性质**\n- R2: 属于方法论层面的定义问题，不应列为论文贡献\n- R1: Definitional 诊断本身具有实证价值（因为社区此前未明确意识到这一点）\n\n**D3. SJ Hungarian matching 的新颖性**\n- R2: 技术新颖性有限，且 scalability 未讨论\n- R1: 论文未将其声称为贡献，不应作为弱点评判\n\n---\n\n## Questions for Authors\n\nQ1. ε=0.05 的选择依据是什么？能否提供 ε ∈ {0.01, 0.02, 0.05, 0.10, 0.20} 下 tied fraction 和 LP selection Δ 的 sensitivity curve？\n\nQ2. LP 在 T=0.7 下的压缩行为是否可从现有数据推断？是否有技术障碍阻止收集 T=0.7 LP 数据？\n\nQ3. Non-tied LP 子集（40%, n=210）的 instance 特征是什么？它们是否对应特定难度区间或 schema 复杂度？\n\nQ4. 如果 C1 是 definitional（如论文 Introduction L23 所述），为何将其列为论文的第一个 contribution 而非 background/preliminary？\n\nQ5. Free-form ablation 中 RE LP selection 方向逆转（-0.68→+1.69pp）的机制解释是什么？这是否暗示 constrained decoding 而非 LP 本身是 RE selection 失败的原因？\n\nQ6. 论文是否计划发布代码、模型 checkpoint 或实验数据？\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现关键缺失引用。引用列表（62 条）经核查真实完整。\n\n建议补充（非必须）：\n- MBR decoding 在 NLP 中的更多近期工作（如 Bertsch et al. 2023 等）\n- Conformal prediction for NLP（论文 Conclusion 中提到但未引用具体工作）\n\n---\n\n## External Review\n\n本轮未获得外部审稿结果（用户跳过）。\n\n---\n\n## Overall Assessment\n\n**综合评分: Borderline（边界线）**\n\n**R1 评分: 3.5/5** — 方法扎实、发现有价值，但 ε 循环论证和 LP 温度缺失削弱了核心 claim 的可信度\n**R2 评分: 2.5/5** — 实验设计严谨但页数超限+framing 问题构成提交障碍；R2 表示若页数+framing+标题修复可升至 3.0/5\n\n**录用建议: Borderline Reject → Borderline Accept（取决于修改质量）**\n\n论文的核心发现（correlation-selection gap）具有实际价值，实验设计系统严谨，统计方法规范。但当前版本存在以下提交障碍：\n\n1. **Blocking**: 页数超限 2-3 页（desk reject 风险）\n2. **Blocking**: ε=0.05 缺乏独立 justification（核心量化可信度）\n3. **High priority**: 标题过度断言、RE preliminary 标注不一致、abstract 可读性\n\n如果作者能在 deadline 前（2026-05-25）完成：压缩至 8 页、补充 ε sensitivity analysis、统一 RE preliminary 标注、修改标题、精简 abstract，论文有望达到 EMNLP Findings 的录用标准。否则建议推迟至下一 cycle。\n\n---\n\n## Detailed Comments\n\n### 页数压缩建议（优先级排序）\n1. Discussion §5 的 free-form ablation 详情（¶4）→ 移入 Appendix，正文仅保留一句结论\n2. Table 2 的 N=16 行 → 移入 Appendix，正文讨论 N=8 为主\n3. Experiments 中 WNUT-17 的详细讨论 → 压缩为 1 段，作为 capability boundary 验证\n4. Figure 3 → 考虑是否可与 Figure 2 合并或移入 Appendix\n\n### RE 处理建议\n- 所有 RE 相关 claim 统一添加 \"(preliminary; single benchmark)\" 标注\n- Abstract 中 RE 相关数值可删除或移入括号注释\n- 考虑将 RE 定位为 \"exploratory analysis\" 而非与 NER 并列的主要结果\n\n### Framing 调整建议\n- C1 重新措辞：从 \"contribution\" 改为 \"observation/finding\"，或明确区分 \"definitional analysis\" 与 \"empirical contribution\"\n- 标题选项：\"Confidence Signals Predict but Struggle to Select\" 或 \"The Correlation-Selection Gap in ...\"",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 8 Consolidated Review Report\n\n**Paper**: \"Strong Predictors, Weak Selectors: Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction\"\n**Venue**: EMNLP 2026 Findings (ARR May cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法+实验), R2 (新颖性+写作+格式)\n**Protocol**: 独立初审 → 交叉分享 → 收敛（1轮达成共识，无需第2轮）\n\n---\n\n## Summary\n\n本文系统评估了五种置信度信号（VC、SJ、FK、EM、LP）在 LLM 结构化信息抽取中的质量估计、二元判别和样本选择三个维度上的表现。核心发现为\"correlation-selection gap\"——所有信号在质量估计上表现良好（ρ 最高 0.38，AUROC 最高 0.75），但在样本选择上均未能显著优于 greedy baseline，尽管存在 12-18pp 的 oracle headroom。论文提出两层解释：(1) 四个信号为 instance-level 聚合，定义上无法排序候选；(2) LP 分数严重压缩（60% 实例有效并列）。实验覆盖 2 个模型族（Qwen3-8B, LLaMA-3.1-8B）、3 个数据集（SciERC, CoNLL-2003, WNUT-17）、N=8/16 两个采样规模。\n\n---\n\n## Strengths\n\n**S1. 系统性实验设计（两位 Reviewer 共识）**\n5 信号 × 3 维度 × 3 数据集 × 2 模型的全因子设计，覆盖面在同类工作中罕见。bootstrapped CI、paired permutation test、3-seed 稳定性分析等统计方法规范。\n\n**S2. 核心发现具有实用价值**\nCorrelation-selection gap 的发现对 self-consistency 方法的实际部署有直接指导意义——警示从业者不能仅凭 rank correlation 选择信号。\n\n**S3. 多层次诊断分析**\n从定义层（instance-level 信号无法排序候选）到机制层（LP 压缩、MBR 效用-质量错位）的分层解释，提供了比单纯报告现象更深的理解。\n\n**S4. 透明的局限性讨论**\nLimitations 部分涵盖 RE 单基准、模型规模限制、温度未测试、enable_thinking 不一致等，展现了诚实的自我评估。\n\n**S5. Ablation 设计有价值**\nFree-form ablation 排除了 constrained decoding 作为 LP 压缩的唯一来源，non-tied LP 子集的显著性分析（+2.9pp, p=0.01）为机制解释提供了关键证据。\n\n---\n\n## Weaknesses\n\n### Critical（必须修复）\n\n**C1. 页数严重超限 [R1+R2 共识]**\n正文（Abstract 至 Conclusion）估计为 10-11 页，超出 ARR/EMNLP 8 页限制 2-3 页。这是格式硬性要求，desk reject 风险极高。\n- R1: 需要大幅压缩 experiments 和 discussion\n- R2: 必须砍到 8 页，建议将 free-form ablation 详情、N-scaling 细节、部分表格移入 appendix\n\n**C2. ε=0.05 \"effectively tied\" 阈值循环论证 [R1 提出, R2 同意]**\nLP 压缩的核心量化依赖 ε=0.05 阈值，但该阈值缺乏独立于数据的 justification。论文未提供 ε sensitivity analysis（不同 ε 下 tied fraction 如何变化），使\"60% tied\"这一关键数字的可信度受损。R1 建议补充 ε sweep 图表。\n\n**C3. LP 温度 T=0.7 数据缺失 [R1 提出, R2 同意]**\n温度比较实验（T=0.7 vs T=1.0）中 LP 被排除（因缺少 T=0.7 LP 数据）。这恰好是 LP 压缩与温度交互效应的关键缺失——practitioners 通常在 T<1.0 部署，LP 在低温下的表现直接影响论文结论的实用性。Limitations 已提及但仅作为\"unknown\"处理，不足以弥补。\n\n**C4. RE 结论基于单基准+单 seed（部分场景）[R1+R2 共识]**\nRE 仅在 SciERC 上评估（且 40% 实例 F1=0），free-form ablation RE 选择方向逆转基于单 seed。论文在多处声称 RE 为 \"preliminary\"，但标注不一致——abstract 和部分正文中未标注。所有 RE claim 必须统一标注 preliminary。\n\n### Major（强烈建议修复）\n\n**M1. 标题 \"Do Not Select\" 过度断言 [R2 提出, R1 部分同意]**\n标题断言信号\"不能选择\"，但 non-tied LP 子集确实能选择（+2.9pp, p=0.01），且论文仅测试了 unsupervised 信号。R1 认为当前标题可接受但可改进为更精确的表述。R2 认为标题与论文自己的证据矛盾。建议修改为反映条件性失败的表述。\n\n**M2. Abstract 信息过载 [R1+R2 共识]**\n10 行 abstract 塞入 5 个信号名、3 个数据集、2 个模型、4 个指标的具体数值，first-pass 可读性差。建议精简到核心 narrative：gap 存在 → 诊断原因 → 实用影响。\n\n**M3. Framing 问题：贡献 C1 的性质 [R1、R2 分歧，见下]**\nR2 认为 C1（instance-level 信号无法排序候选）是定义推导而非实证贡献，将其列为\"贡献\"存在 framing 误导；R1 认为 definition-level 诊断本身有价值但同意措辞可改进。论文需要更清晰地区分 definitional vs empirical 贡献。\n\n**M4. Eikema & Aziz (2022) MBR 讨论位置不当 [R1+R2 共识]**\nMBR decoding 连接出现在 Discussion 而非 Related Work，使读者在 §5 才发现这一重要理论关联。建议在 Related Work 中增加 MBR/utility-based selection 子节。\n\n**M5. 缺少代码/数据发布声明 [R2 提出, R1 同意]**\n论文未包含代码或数据发布声明。ARR review form 明确询问 reproducibility resources。即使匿名期无法提供链接，也应声明提交时或录用后会发布。\n\n### Minor\n\n**W1. enable_thinking 对 LP 的潜在影响**\nQwen3-8B SciERC checkpoint 训练时有空 `&lt;think>&lt;/think>` 块，可能影响 first-token 概率分布。虽然 Limitations 中已讨论，但未定量评估影响大小。\n\n**W2. Free-form ablation 范围窄**\n仅在 SciERC + Qwen3-8B 上进行，泛化性未验证。\n\n**W3. FK t-test 统计功效不足**\nSciERC RE 的 FK t-test 可能样本量不足，p 值接近临界值时可信度受限。\n\n**W4. TOST δ 锚定**\n等价性检验的 δ 选择缺乏先验 justification。\n\n**W5. SJ 的 Hungarian 算法匹配**\nSJ 使用 Hungarian 算法做 token-level IoU 匹配，计算复杂度 O(n³)，论文未讨论 scalability。\n\n---\n\n## Reviewer Consensus（共识区）\n\n以下问题两位 Reviewer 完全一致：\n1. **页数超限是 desk reject 级问题**，必须在提交前解决\n2. **ε=0.05 需要 sensitivity analysis** 或独立于数据的 justification\n3. **LP T=0.7 缺失**是对实用性的重大限制\n4. **RE preliminary 标注必须全文一致**\n5. **Abstract 需精简**，减少具体数值堆砌\n6. **Eikema MBR 讨论应前移到 Related Work**\n7. **需要代码发布声明**\n8. **核心实验设计和统计方法扎实**\n\n---\n\n## Reviewer Divergence（分歧区）\n\n**D1. Framing 严重程度**\n- R2 (2.5/5): 认为 framing 存在根本性问题——将定义推导包装为实证贡献，标题与证据矛盾，整体叙事需要重构\n- R1 (3.5/5): 认为是表述改进问题而非根本缺陷，核心发现的价值不受 framing 影响\n\n**D2. 贡献 C1 的性质**\n- R2: 属于方法论层面的定义问题，不应列为论文贡献\n- R1: Definitional 诊断本身具有实证价值（因为社区此前未明确意识到这一点）\n\n**D3. SJ Hungarian matching 的新颖性**\n- R2: 技术新颖性有限，且 scalability 未讨论\n- R1: 论文未将其声称为贡献，不应作为弱点评判\n\n---\n\n## Questions for Authors\n\nQ1. ε=0.05 的选择依据是什么？能否提供 ε ∈ {0.01, 0.02, 0.05, 0.10, 0.20} 下 tied fraction 和 LP selection Δ 的 sensitivity curve？\n\nQ2. LP 在 T=0.7 下的压缩行为是否可从现有数据推断？是否有技术障碍阻止收集 T=0.7 LP 数据？\n\nQ3. Non-tied LP 子集（40%, n=210）的 instance 特征是什么？它们是否对应特定难度区间或 schema 复杂度？\n\nQ4. 如果 C1 是 definitional（如论文 Introduction L23 所述），为何将其列为论文的第一个 contribution 而非 background/preliminary？\n\nQ5. Free-form ablation 中 RE LP selection 方向逆转（-0.68→+1.69pp）的机制解释是什么？这是否暗示 constrained decoding 而非 LP 本身是 RE selection 失败的原因？\n\nQ6. 论文是否计划发布代码、模型 checkpoint 或实验数据？\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现关键缺失引用。引用列表（62 条）经核查真实完整。\n\n建议补充（非必须）：\n- MBR decoding 在 NLP 中的更多近期工作（如 Bertsch et al. 2023 等）\n- Conformal prediction for NLP（论文 Conclusion 中提到但未引用具体工作）\n\n---\n\n## External Review\n\n本轮未获得外部审稿结果（用户跳过）。\n\n---\n\n## Overall Assessment\n\n**综合评分: Borderline（边界线）**\n\n**R1 评分: 3.5/5** — 方法扎实、发现有价值，但 ε 循环论证和 LP 温度缺失削弱了核心 claim 的可信度\n**R2 评分: 2.5/5** — 实验设计严谨但页数超限+framing 问题构成提交障碍；R2 表示若页数+framing+标题修复可升至 3.0/5\n\n**录用建议: Borderline Reject → Borderline Accept（取决于修改质量）**\n\n论文的核心发现（correlation-selection gap）具有实际价值，实验设计系统严谨，统计方法规范。但当前版本存在以下提交障碍：\n\n1. **Blocking**: 页数超限 2-3 页（desk reject 风险）\n2. **Blocking**: ε=0.05 缺乏独立 justification（核心量化可信度）\n3. **High priority**: 标题过度断言、RE preliminary 标注不一致、abstract 可读性\n\n如果作者能在 deadline 前（2026-05-25）完成：压缩至 8 页、补充 ε sensitivity analysis、统一 RE preliminary 标注、修改标题、精简 abstract，论文有望达到 EMNLP Findings 的录用标准。否则建议推迟至下一 cycle。\n\n---\n\n## Detailed Comments\n\n### 页数压缩建议（优先级排序）\n1. Discussion §5 的 free-form ablation 详情（¶4）→ 移入 Appendix，正文仅保留一句结论\n2. Table 2 的 N=16 行 → 移入 Appendix，正文讨论 N=8 为主\n3. Experiments 中 WNUT-17 的详细讨论 → 压缩为 1 段，作为 capability boundary 验证\n4. Figure 3 → 考虑是否可与 Figure 2 合并或移入 Appendix\n\n### RE 处理建议\n- 所有 RE 相关 claim 统一添加 \"(preliminary; single benchmark)\" 标注\n- Abstract 中 RE 相关数值可删除或移入括号注释\n- 考虑将 RE 定位为 \"exploratory analysis\" 而非与 NER 并列的主要结果\n\n### Framing 调整建议\n- C1 重新措辞：从 \"contribution\" 改为 \"observation/finding\"，或明确区分 \"definitional analysis\" 与 \"empirical contribution\"\n- 标题选项：\"Confidence Signals Predict but Struggle to Select\" 或 \"The Correlation-Selection Gap in ...\"",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 846 · 2026-05-15T15:19:36.851363+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3716
}
```

</details>

---


### Assistant

_source line 847 · 2026-05-15T15:19:43.295460+00:00_

审稿报告已投递至 Research Director。

**Round 8 审稿完成。** 两位 Reviewer 独立初审 + 交叉分享，1 轮收敛。综合评分 **Borderline**（R1: 3.5/5, R2: 2.5/5）。

关键发现：
- **2 个 blocking issue**：页数超限 2-3 页（desk reject 风险）、ε=0.05 阈值缺乏独立 justification
- **3 个 high priority**：标题过度断言、RE preliminary 标注不一致、abstract 信息过载
- **3 个分歧点**：framing 严重程度、C1 贡献性质、SJ 新颖性——已如实记录在报告中
- Issue tracker 已同步更新（22 条 in_progress 更新 + 7 条新增）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 72

## Round 72

72 recorded events


### User

_source line 848 · 2026-05-15T15:19:44.339928+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

R1 的 6 个问题中我无一 REBUT，全部 AGREE（3 个有 nuance 限定）。两位 reviewer 的核心共识：LP 温度缺失 severity 高、RE 结论基础薄弱、统计严谨性是论文主要优势。

主要分歧在 overall 评分（3.5 vs 2.5）——差异源于我额外识别的页数超限和 contribution framing 问题，R1 未涉及这两点。

---

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 849 · 2026-05-15T15:19:50.318414+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 850 · 2026-05-15T15:19:50.369381+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 851 · 2026-05-15T15:20:04.446404+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 852 · 2026-05-15T15:20:04.497342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 853 · 2026-05-15T15:20:09.370312+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 854 · 2026-05-15T15:20:09.823979+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (83 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp008_re_n16** (killed): —\n- **exp001_seed456** (killed): —\n- **exp001_seed123** (killed): —\n\n## 趋势\n成功 46 / 负向 20 / 失败 1 / 共 83\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_007_ner_llama: 已被终止 — unknown\n- exp001_seed123: 已被终止 — unknown\n- exp001_seed456: 已被终止 — unknown\n- exp008_re_n16: 已被终止 — unknown\n- exp_002_merge_conll2003: 已被终止 — unknown\n- exp_001_n16_seed123_full: 已被终止 — unknown\n- exp_001_n16_seed456_full: 已被终止 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\n- exp_019_supervised_verifier: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 855 · 2026-05-15T15:20:10.377493+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 856 · 2026-05-15T15:20:10.679315+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 857 · 2026-05-15T15:20:10.730471+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 858 · 2026-05-15T15:20:10.833719+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 859 · 2026-05-15T15:20:14.654251+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-15T15:20:15.658900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-15T15:20:15.910273+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-15T15:20:15.910788+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-15T15:20:15.911039+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 864 · 2026-05-15T15:20:23.148230+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the search results, here's comprehensive information about EMNLP 2026's call for papers:

## Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026. All deadlines are 11:59PM UTC-12:
…[truncated 1885 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 8493
}
```

</details>

---


### Tool call

_source line 865 · 2026-05-15T15:20:28.118397+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 866 · 2026-05-15T15:20:29.022583+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex
/home/ubuntu/.agent-
…[truncated 2776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 867 · 2026-05-15T15:20:29.022953+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 page limit format template double blind anonymity ACL rolling review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 page limit format template double blind anonymity ACL rolling review"
  }
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-15T15:20:29.123551+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-15T15:20:40.192396+00:00_

Web search results for query: "EMNLP 2026 page limit format template double blind anonymity ACL rolling review"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/ojs/index.php/tacl/about/submissions"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"}]

Based on my search results, here's information about EMNLP 2026 submission requirements:

## Page Limits and Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Anonymity and Double-Blind Review

Industry Track submissions must neither include the authors
…[truncated 959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 11169
}
```

</details>

---


### Tool result

_source line 870 · 2026-05-15T15:20:40.192799+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 11069
}
```

</details>

---


### Tool call

_source line 871 · 2026-05-15T15:20:45.564842+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 872 · 2026-05-15T15:20:45.615642+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 873 · 2026-05-15T15:20:46.218460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 874 · 2026-05-15T15:20:46.521338+00:00_

1	issues:
2	# ===== RESOLVED ISSUES (Rounds 0-7) =====
3	- id: R0-C1
4	  summary: 模型规模单一（仅 8B）
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 1
10	  mentions:
11	  - round: 0
12	    reviewers: [1, 2]
13	    note: 8B→8B 仅验证架构鲁棒性非规模鲁棒性
14	  - round: 1
15	    reviewers: [1, 2]
16	    note: model-agnostic 与 Limitations 矛盾
17	  action_items:
18	  - round: 1
19	    action: 全文替换 model-agnostic → consistent across tested model families
20	    assigned_to: Paper Agent
21	    status: resolved
22	  resolution: Round 2 Reviewer 确认措辞修正到位，无再提
23	  resolution_round: 2
24	- id: R0-C2
25	  summary: 相关工作显著遗漏
26	  category: framing
27	  severity: warning
28	  status: resolved
29	  first_raised_round: 0
30	  last_seen_round: 1
31	  mentions:
32	  - round: 0
33	    reviewers: [1, 2]
34	    note: 5 篇核心文献缺失
35	  - round: 1
36	    reviewers: [1, 2]
37	    note: 新遗漏：Optimal SC, Difficulty-Adaptive SC
38	  action_items:
39	  - round: 1
40	    action: 补充 6 篇引用到 Related Work
41	    assigned_to: Paper Agent
42	    status: resolved
43	  resolution: 'Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏'
44	  resolution_round: 2
45	- id: R0-C3
46	  summary: RE 结论仅基于 SciERC 单数据集
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 0
51	  last_seen_round: 4
52	  mentions:
53	  - round: 0
54	    reviewers: [1, 2]
55	    note: 需跨数据集验证或降级措辞
56	  - round: 2
57	    reviewers: [1, 2]
58	    note: Abstract RE 措辞需修正
59	  - round: 3
60	    reviewers: [1, 2]
61	    note: Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围
62	  - round: 4
63	    reviewers: [1, 2]
64	    note: R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪
65	  action_items:
66	  - round: 1
67	    action: 降级措辞 universal → observed in SciERC
68	    assigned_to: Paper Agent
69	    status: resolved
70	  - round: 2
71	    action: Abstract 改为 NER (three datasets) and RE (SciERC)
72	
…[truncated 52229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 875 · 2026-05-15T15:20:46.672405+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "writing_plan.yaml"
  }
}
```

</details>

---


### Tool result

_source line 876 · 2026-05-15T15:20:47.125182+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026 Main (via ARR May)\\n  track: main\\n  template: null  # ARR/ACL format — need to download acl2023.sty or latest ARR template\\n  template_note: \\\"No local template found. Worker should download latest ARR LaTeX template from ACL Rolling Review.\\\"\\n  page_limit: 8  # + unlimited references\\n  deadline: 2026-05-25\\n  core_claim: >\\n    Structural consistency signals are the strongest unsupervised quality estimators for LLM-based IE —\\n    entity voting leads ρ (0.38) while EM leads AUROC (0.75), with soft Jaccard as complementary robust signal\\n    (temperature-stable: NER Δρ=0.028; conditional filtering ρ=0.31). A correlation-selection gap means\\n    this does not translate to best-of-N selection — no signal reliably surpasses greedy on either task\\n    (p>0.39, bootstrap). Signal effectiveness is task-difficulty-dependent: easy tasks favor exact-match,\\n    hard tasks favor structural consistency, and SJ strength scales with both sample size (N=8→16 ρ +0.052)\\n    and instance complexity (entity count 6+ ρ=0.55). RE reveals a capability boundary: when compound\\n    error propagation dominates (~44% zero-F1), all signals weaken (ρ=0.134-0.350) — conditional filtering restores\\n    structural signal advantage (SJ ρ=0.31) while logprob collapses (ρ=-0.03).\\n  created_at: 2026-05-14T13:00:00Z\\n  selected_title: \\\"Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\\\"\\n  director_approval: \\\"2026-05-14 approved with modifications: title #2 selected, RE must distinguish joint vs RE-only protocol (D023), 3 tables confirmed (tab_robustness kept), exp_003/exp_007 pending — Director will notify for Patch\\\"\\n  re_protocol_note: \\\"D023: Joint RE SJ ρ=0.267 < FK ρ=0.315; RE-only 
…[truncated 10793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 877 · 2026-05-15T15:21:18.979669+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 878 · 2026-05-15T15:21:19.031245+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No constraints.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 879 · 2026-05-15T15:21:28.686085+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find external review config",
  "subagent_type": "Explore",
  "prompt": "Search in /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ for any YAML or config file that mentions \"external_review\" or \"paperreview\". Check files like config.yaml, project.yaml, settings.yaml, etc. Report the relevant section content. Quick search."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Find external review config",
    "subagent_type": "Explore",
    "prompt": "Search in /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ for any YAML or config file that mentions \"external_review\" or \"paperreview\". Check files like config.yaml, project.yaml, settings.yaml, etc. Report the relevant section content. Quick search."
  }
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-15T15:21:30.445494+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/**/*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/**/*.yaml"
  }
}
```

</details>

---


### Tool call

_source line 881 · 2026-05-15T15:21:30.445931+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/**/*.yml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/**/*.yml"
  }
}
```

</details>

---


### Tool result

_source line 882 · 2026-05-15T15:21:30.446240+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/review_context.yaml
/hom
…[truncated 3166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-15T15:21:30.497010+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-15T15:21:32.153075+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "**/*.yaml",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "glob": "**/*.yaml",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-15T15:21:32.203795+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-15T15:21:33.909398+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 2 -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 2 -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-15T15:21:34.060321+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-15T15:21:35.568359+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-15T15:21:35.619067+00:00_

total 44
drwxrwxr-x  9 ubuntu ubuntu 4096 May 14 04:20 .
drwxr-x--- 16 ubuntu ubuntu 4096 May 15 13:00 ..
drwxr-xr-x  2 ubuntu ubuntu 4096 May 14 04:20 .claude
-rw-r--r--  1 ubuntu ubuntu  355 May 15 15:19 AGENTS.md
drwxrwxr-x  4 ubuntu ubuntu 4096 May 15 09:34 config
drwxr-xr-x  3 ubuntu ubuntu 4096 May 15 15:10 global
drwxr-xr-x  2 ubuntu ubuntu 4096 May 14 04:20 idea_generator
drwxrwxr-x  4 ubuntu ubuntu 4096 May 14 04:20 projects
drwxr-xr-x  3 ubuntu ubuntu 4096 May 14 03:29 skills
drwxr-xr-x  2 ubuntu ubuntu 4096 May 15 15:21 state
-rw-r--r--  1 ubuntu ubuntu   13 May 14 03:29 workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-15T15:21:37.027877+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config -type f \\( -name \"*.yaml\" -o -name \"*.yml\" \\) 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config -type f \\( -name \"*.yaml\" -o -name \"*.yml\" \\) 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-15T15:21:37.078640+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/secrets/struct_self_consist_ie/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-15T15:21:38.885743+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config",
  "glob": "**/*.yaml",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config",
    "glob": "**/*.yaml",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-15T15:21:38.886248+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-15T15:21:40.362467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml"
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-15T15:21:40.362912+00:00_

1	execution:
2	  account: root
3	  gpu_ids:
4	  - cuda:0
5	  - cuda:1
6	  - cuda:2
7	  - cuda:3
8	  project_path: /root/autodl-tmp/struct_self_consist_ie
9	  servers:
10	  - account: root
11	    aliases:
12	    - bjb1-21071
13	    server: autodl-5090
14	feishu:
15	  chat_id: oc_1b56445332d8ca2b4964b30f300f0e00
16	  operational_chat_id: oc_523053f5a039428dc15666668fa856b3
17	  review_paper_path: projects/struct_self_consist_ie/paper/main.tex
18	  review_round: 9
19	  review_supplementary_paths: ''
20	  submission_chat_id: oc_3897c2857f11615119e277e820eae311
21	project:
22	  created_at: '2026-05-14T04:20:56.331Z'
23	  description: When Does Test-Time Scaling Help Structured Prediction? Adaptive Structural
24	    Self-Consistency with Learned Aggregation
25	  name: struct_self_consist_ie
26	  phase: research
27	  source_idea_id: idea_010
28	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-15T15:21:41.718619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/resources.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/resources.yaml"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-15T15:21:41.869856+00:00_

1	default_model: claude-opus-4-6
2	default_model_claude_code: claude-opus-4-6
3	idea_model: claude-opus-4-6
4	servers:
5	  autodl-5090:
6	    accounts:
7	    - env_activate: ''
8	      user: root
9	      work_dir: /root/autodl-tmp
10	    detected_image:
11	      detected: false
12	      image: ''
13	      status: unknown
14	      version: ''
15	    gpus:
16	    - available: true
17	      id: cuda:0
18	      vram_gb: 32
19	    - available: true
20	      id: cuda:1
21	      vram_gb: 32
22	    - available: true
23	      id: cuda:2
24	      vram_gb: 32
25	    - available: true
26	      id: cuda:3
27	      vram_gb: 32
28	    hardware:
29	      cpu_cores: 0
30	      disk_avail_gb: 0
31	      disk_total_gb: 0
32	      probed_at: '2026-05-14T04:46:16.427Z'
33	      ram_total_gb: 0
34	    host: connect.bjb1.seetacloud.com
35	    port: 21071
36	  bjb1-21071:
37	    accounts:
38	    - env_activate: ''
39	      user: root
40	      work_dir: /root
41	    detected_image:
42	      detected: false
43	      image: ''
44	      status: unknown
45	      version: ''
46	    gpus:
47	    - available: true
48	      id: cuda:0
49	      vram_gb: 32
50	    - available: true
51	      id: cuda:1
52	      vram_gb: 32
53	    - available: true
54	      id: cuda:2
55	      vram_gb: 32
56	    - available: true
57	      id: cuda:3
58	      vram_gb: 32
59	    hardware:
60	      cgroup_memory_limit_gb: 360
61	      cpu_cores: 208
62	      disk_avail_gb: 20
63	      disk_total_gb: 30
64	      probed_at: '2026-05-14T13:33:13.562Z'
65	      ram_total_gb: 755
66	    host: connect.bjb1.seetacloud.com
67	    port: 21071
68	user_rules: []
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-15T15:21:41.870362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/approvals.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/approvals.yaml"
  }
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-15T15:21:41.870679+00:00_

1	# 审批类型注册表
2	# 此文件位于 WORKSPACE_ROOT/config/approvals.yaml
3	# hook 名由 Python (core/approvals/hooks.py) 绑定，不在此文件里定义
4	
5	approval_types:
6	
7	  experiment:
8	    display_name: "实验审批"
9	    description: "高风险实验变更，需要人工审批后才能提交训练"
10	    always_require: false
11	    auto_approve_rule: "all_not_high"   # 枚举：all_low | all_not_high | always | never
12	    risk_dimensions:
13	      - name: gpu_hours
14	        label: "GPU 时长（小时）"
15	        type: numeric
16	        thresholds: { low: 2.0, medium: 8.0 }
17	        hard_limit: 4.0            # 超过直接触发审批，无视其他维度
18	      - name: change_scope
19	        label: "代码变更文件数"
20	        type: numeric
21	        thresholds: { low: 1, medium: 3 }
22	      - name: history_success
23	        label: "历史成功次数"
24	        type: numeric
25	        thresholds: { low: 2, medium: 1 }   # 0 次 → medium（不再是 high）
26	        invert: true                         # 数值越大风险越低
27	    pending_timeout_hours: 48
28	
29	  worker:
30	    display_name: "Worker 任务审批"
31	    description: "高风险后台任务需要确认后才启动"
32	    always_require: false
33	    auto_approve_rule: "all_low"
34	    risk_dimensions:
35	      - name: task_type
36	        label: "任务类型"
37	        type: enum
38	        high_values: ["code_rewrite", "bulk_delete"]
39	        medium_values: ["code_modify"]
40	        low_values: ["doc_gen", "analysis", "exploration"]
41	      - name: file_scope
42	        label: "涉及文件数"
43	        type: numeric
44	        thresholds: { low: 3, medium: 10 }
45	    pending_timeout_hours: 24
46	
47	  deployment:
48	    display_name: "部署审批"
49	    description: "生产部署不可逆，必须人工确认"
50	    always_require: true
51	    auto_approve_rule: "never"
52	    risk_dimensions:
53	      - name: service_tier
54	        label: "服务等级"
55	        type: enum
56	        high_values: ["production"]
57	        medium_values: ["staging"]
58	        low_values: ["dev"]
59	    pending_timeout_hours: 24
60	
61	  submission:
62	    display_name: "投稿审批"
63	    description: "Director 提交审稿请求后，发卡片到 A 群让用户选择审稿模式（co
…[truncated 626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-15T15:21:43.729209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-15T15:21:43.830012+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-idea-gen-0514
5	  my_token: 97c92b1c3bd6eb7ae960060e7b95906c2ffa08a3120431259b3eaac3a322c220
6	  ingest_token: e1dc1e287cb57d2e8411481f152c3cfb22d694b1bc8043b04a543cc7f0e08b82
7	  api:
8	    listen_host: 0.0.0.0
9	    listen_port: 8420
10	    allowed_source_cidrs:
11	    - 10.0.0.0/8
12	    - 192.168.0.0/16
13	    - 172.16.0.0/12
14	    - 127.0.0.0/8
15	  capabilities:
16	    read: true
17	    bootstrap_project: true
18	    archive_project: true
19	    allocate_gpus: true
20	    release_gpus: true
21	    read_chat_history: true
22	    claude_account_login: true
23	    read_claude_pool: true
24	  local_approvals:
25	    bootstrap_project: false
26	    archive_project: false
27	    allocate_gpus: false
28	  heartbeat:
29	    enabled: true
30	    interval_sec: 60
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-15T15:21:43.930819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml"
  }
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-15T15:21:43.931197+00:00_

1	app_id: cli_a97ee92a41b81cb1
2	app_secret: mlARg4oP9AVEWECTLUaEEgG0ivekqJg2
3	bot_name: Auto Research Prod15
4	chats: {}
5	policy:
6	  require_mention: true
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 904 · 2026-05-15T15:21:45.638353+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -type f -name \"*review*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -type f -name \"*review*\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-15T15:21:45.739334+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_paper_integrate_review_data_20260515T031735.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_review_round7_consistency_20260515T124330_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_paper_reviewer_consistency_check_20260515T031759_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_review_round7_consistency_20260515T124330.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_paper_integrate_review_data_20260515T031735_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_paper_reviewer_consistency_check_20260515T031759.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_review_round7_consistency_20260515T124330.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_reviewer_2.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.lock
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_reviewer_2.lock
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_review_round7_consistency_20260515T124330.lock
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_reviewer_1.lock
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer_20260514T08
…[truncated 1259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-15T15:21:47.095789+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/state -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/state -type f 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-15T15:21:47.147460+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/state/pool_state_last.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-15T15:21:48.503436+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-15T15:21:48.654583+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log:2026-05-15 01:47:44 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log:2026-05-15 02:38:36 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log:2026-05-15 03:55:06 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log:2026-05-15 06:38:12 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log:2026-05-15 07:48:49 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log:2026-05-15 08:42:35 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log:2026-05-15 12:11:37 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log:2026-05-15 14:54:01 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log:2026-05-15 15:10:38 INFO     [EXTERN] [external_review] reset state for project=struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log:2026-05-15 15:10:38 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:{"ts": "2026-05-15T12:39:44.11061
…[truncated 22895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-15T15:21:51.269914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log",
  "limit": "100",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log",
    "limit": "100",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-15T15:21:51.320802+00:00_

0	2026-05-14 03:29:46 INFO     [SESSION] [session_server] wrote /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/mcp_config.json
1	2026-05-14 03:29:46 INFO     [SESSION] [session_server] started (loop=135555280795168)
2	2026-05-14 03:29:46 INFO     [__MAIN] [startup] watchdog started pid=2794 (bash=/usr/bin/bash)
3	2026-05-14 03:29:46 INFO     [FEISHU] Feishu WebSocket started in background thread
4	2026-05-14 03:29:47 INFO     [GPU_MO] GPU monitor daemon starting (interval=60s)
5	2026-05-14 03:29:47 INFO     [CRON] Polling loop started (default interval 120s)
6	2026-05-14 03:29:47 INFO     [DIRECT] [keepalive] Loaded 0 project states
7	2026-05-14 03:29:51 INFO     [POOL_S] pool_state_watcher scheduled
8	2026-05-14 03:29:51 INFO     [POOL_S] pool_state_watcher: no manager target in backend.yaml; watcher will not emit events
9	2026-05-14 03:29:56 INFO     [HTTP] HTTP Request: GET https://autoresearch.claude-code-manager.com/api/health "HTTP/1.1 502 Bad Gateway"
10	2026-05-14 03:29:56 WARNING  [__MAIN] Public URL check failed: https://autoresearch.claude-code-manager.com 返回 502
11	2026-05-14 03:30:02 INFO     [SESSION] [session_server] cron_poller started
12	2026-05-14 03:30:02 INFO     [FEISHU] [WS-PATCH] Monkey-patched WSClient._handle_message for CARD frame support
13	2026-05-14 03:30:02 INFO     [LARK] connected to wss://msg-frontier.feishu.cn/ws/v2?fpid=493&aid=552564&device_id=7639584580949363649&access_key=[REDACTED] [conn_id=7639584580949363649]
14	2026-05-14 04:04:39 INFO     [CRON] Polling loop cancelled
15	2026-05-14 04:04:41 INFO     [SESSION] [session_server] started (loop=126120147040112)
16	2026-05-14 04:04:41 INFO     [__MAIN] [startup] watchdog already running (pid=4681, status 19s old), skipping restart
17	2026-05-14 04:04:41 INFO     [FEISHU] Feishu WebSocket started in background thread
18	2026-05-14 04:04:41 INFO     [GPU_MO] GPU monitor daemon starting (in
…[truncated 8769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-15T15:21:53.180110+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log"
  }
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-15T15:21:53.230795+00:00_

5199:2026-05-15 01:47:44 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
5347:2026-05-15 02:38:36 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
5736:2026-05-15 03:55:06 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
6574:2026-05-15 06:38:12 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
6793:2026-05-15 07:48:49 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
6964:2026-05-15 08:42:35 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
7843:2026-05-15 12:11:37 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
8992:2026-05-15 14:54:01 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
9133:2026-05-15 15:10:38 INFO     [EXTERN] [external_review] reset state for project=struct_self_consist_ie
9134:2026-05-15 15:10:38 INFO     [HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 914 · 2026-05-15T15:22:00.660941+00:00_

Perfect. Now I have all the information I need. Let me compile the final report.

## Report: YAML/Config Files Mentioning "external_review" or "paperreview"

After a comprehensive search of the project directory and configuration files, here are my findings:

### Files Checked
- All YAML files in `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/` (no matches)
- Config files in `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/` directory
- Main project config: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml`

### Key Findings

**1. No YAML/Config File Mentions**
There are no YAML configuration files in the project directory that explicitly mention "external_review" or "paperreview" settings.

**2. System Log Evidence**
The system logs at `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log` contain relevant information:

Multiple entries show:
```
[HOOKS] [review] external_review_enabled=False for project=struct_self_consist_ie
```

And a state reset entry:
```
2026-05-15 15:10:38 INFO     [EXTERN] [external_review] reset state for project=struct_self_consist_ie
```

**3. External Review Status**
Based on the Review Director session logs in the project chat history and the MCP tool call results:
- Status: `not_requested`
- Message: "No external review requested."
- The tool `get_external_review_status(project="struct_self_consist_ie")` returns this status

**4. Project Configuration Context**
From `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml`:
```yaml
feishu:
  chat_id: oc_1b56445332d8ca2b4964b30f300f0e00
  operational_chat_id: oc_523053f5a039428dc15666668fa856b3
  review_paper_path: projects/struct_self_consist_ie/paper/main.tex
  review_round: 9
  review_supplementary_paths: ''
  submission_chat_id: oc_3897c2857f11615119e277e820eae311
```

No `external_review` or `paperreview_ai` configuration block exists in this fi
…[truncated 277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Agent",
  "elapsed_ms": 31974
}
```

</details>

---


### Tool call

_source line 915 · 2026-05-15T15:22:54.067882+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "9",
  "project": "struct_self_consist_ie",
  "text": "## Round 9 审稿任务 — Reviewer 1\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页（双栏 ACL 模板），参考文献不限页，Limitations 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各 section 在 `projects/struct_self_consist_ie/docs/paper/sections/` 下\n- Appendix: `projects/struct_self_consist_ie/docs/paper/sections/appendix.tex`\n\n### 审查重点（方法严谨性 + 实验设计）\n\n请重点审查以下方面：\n\n1. **统计方法论**：\n   - Bootstrap 检验、TOST 等价检验的实施是否正确\n   - 多重比较校正是否充分\n   - p 值解读是否准确（failure-to-reject ≠ evidence of absence）\n   - Fleiss' Kappa 独立性假设的 justification\n\n2. **实验设计完整性**：\n   - 多种子验证覆盖率（哪些结果有 3-seed，哪些仅 single seed）\n   - N=8 vs N=16 设计是否对称\n   - Cross-model/cross-dataset 证据面是否支撑所述 claim\n   - Free-form ablation 的范围是否足以支撑其结论\n\n3. **数据完整性**：\n   - 表格数据是否自洽（cross-reference 检查）\n   - LP（logprob）温度敏感性数据是否缺失\n   - RE 证据标注是否一致（preliminary vs established）\n\n4. **可复现性**：\n   - 训练配置和 prompt template 是否完整\n   - 代码/数据发布承诺\n   - 超参数选择的 justification（如 ε=0.05 阈值）\n\n5. **页数**：请估算正文页数是否符合 ≤8 页限制\n\n### 参考：Issue Tracker 中与你审查范围相关的 open/in_progress 问题\n\n- R7-C1: Selection gap 分析缺乏多种子验证（critical）\n- R7-C2: ε=0.05 effectively tied 阈值缺乏论证（critical）\n- R7-C3: Free-form ablation 范围过窄但支撑过强泛化声称（critical）\n- R7-W1: LP 温度敏感性完全缺失（critical）\n- R4-W1: RE 证据需进一步加强（critical）\n- R3-W4: FK 独立性假设 justification 不足（warning）\n- R4-M2: TOST δ 选择缺乏实践意义论证（warning）\n- R8-N1: 正文页数严重超过 8 页限制（critical）\n- R8-W2: enable_thinking 对 LP score distribution 的影响未量化（warning）\n- R8-W3: SJ max normalizer 未做 sensitivity analysis（warning）\n- R8-W4: Seed 456 使用 --subtask joint 而非 --subtask ner（warning）\n- R8-W5: N=8 QE 主表单种子 vs N=16 多种子设计不对称（warning）\n\n请独立审稿，不受上述 issue 列表局限——如有新发现请完整报告。\n\n### 输出格式\n```\n## Summary\n## Strengths（逐条）\n## Weaknesses（逐条，标注 severity: critical/warning/info）\n## Questions（需作者澄清的问题）\n## Missing References\n## Overall Assessment（评分 + 置信度）\n## Detailed Comments（逐节）\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "9",
    "project": "struct_self_consist_ie",
    "text": "## Round 9 审稿任务 — Reviewer 1\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页（双栏 ACL 模板），参考文献不限页，Limitations 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各 section 在 `projects/struct_self_consist_ie/docs/paper/sections/` 下\n- Appendix: `projects/struct_self_consist_ie/docs/paper/sections/appendix.tex`\n\n### 审查重点（方法严谨性 + 实验设计）\n\n请重点审查以下方面：\n\n1. **统计方法论**：\n   - Bootstrap 检验、TOST 等价检验的实施是否正确\n   - 多重比较校正是否充分\n   - p 值解读是否准确（failure-to-reject ≠ evidence of absence）\n   - Fleiss' Kappa 独立性假设的 justification\n\n2. **实验设计完整性**：\n   - 多种子验证覆盖率（哪些结果有 3-seed，哪些仅 single seed）\n   - N=8 vs N=16 设计是否对称\n   - Cross-model/cross-dataset 证据面是否支撑所述 claim\n   - Free-form ablation 的范围是否足以支撑其结论\n\n3. **数据完整性**：\n   - 表格数据是否自洽（cross-reference 检查）\n   - LP（logprob）温度敏感性数据是否缺失\n   - RE 证据标注是否一致（preliminary vs established）\n\n4. **可复现性**：\n   - 训练配置和 prompt template 是否完整\n   - 代码/数据发布承诺\n   - 超参数选择的 justification（如 ε=0.05 阈值）\n\n5. **页数**：请估算正文页数是否符合 ≤8 页限制\n\n### 参考：Issue Tracker 中与你审查范围相关的 open/in_progress 问题\n\n- R7-C1: Selection gap 分析缺乏多种子验证（critical）\n- R7-C2: ε=0.05 effectively tied 阈值缺乏论证（critical）\n- R7-C3: Free-form ablation 范围过窄但支撑过强泛化声称（critical）\n- R7-W1: LP 温度敏感性完全缺失（critical）\n- R4-W1: RE 证据需进一步加强（critical）\n- R3-W4: FK 独立性假设 justification 不足（warning）\n- R4-M2: TOST δ 选择缺乏实践意义论证（warning）\n- R8-N1: 正文页数严重超过 8 页限制（critical）\n- R8-W2: enable_thinking 对 LP score distribution 的影响未量化（warning）\n- R8-W3: SJ max normalizer 未做 sensitivity analysis（warning）\n- R8-W4: Seed 456 使用 --subtask joint 而非 --subtask ner（warning）\n- R8-W5: N=8 QE 主表单种子 vs N=16 多种子设计不对称（warning）\n\n请独立审稿，不受上述 issue 列表局限——如有新发现请完整报告。\n\n### 输出格式\n```\n## Summary\n## Strengths（逐条）\n## Weaknesses（逐条，标注 severity: critical/warning/info）\n## Questions（需作者澄清的问题）\n## Missing References\n## Overall Assessment（评分 + 置信度）\n## Detailed Comments（逐节）\n```"
  }
}
````

</details>

---


### Tool result

_source line 916 · 2026-05-15T15:23:17.384265+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23316
}
```

</details>

---


### Tool call

_source line 917 · 2026-05-15T15:23:17.535433+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "9",
  "project": "struct_self_consist_ie",
  "text": "## Round 9 审稿任务 — Reviewer 2\n\n### 你的审查侧重：新颖性 + 完整性 + 格式合规\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页（双栏 ACL 模板），参考文献不限页，Limitations 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各 section 在 `projects/struct_self_consist_ie/docs/paper/sections/` 下\n- Appendix: `projects/struct_self_consist_ie/docs/paper/sections/appendix.tex`\n\n### 审查重点（新颖性 + 完整性 + 格式合规）\n\n请重点审查以下方面：\n\n1. **核心贡献新颖性**：\n   - Correlation-selection gap 是否是 genuine finding 还是 tautological（instance-level 信号无法 select 是否是定义必然）\n   - 与 Nédellec et al. (2026) 的增量贡献是否充分\n   - SJ (Soft Jaccard) 方法论新颖性\n   - Contribution 1（multi-metric evaluation）是否应为 contribution 还是 finding\n\n2. **Framing 与 Claim Scope**：\n   - 标题 \"Do Not Select\" 是否 overclaim（LP 在子集上 significantly selects，RE free-form 下翻转为正）\n   - \"8B-Scale\" 是否过度暗示泛化性\n   - Cross-architecture 用词是否准确（实为 fixed 8B scale 两架构）\n   - Abstract 信息密度是否适当\n\n3. **Related Work 覆盖**：\n   - 关键引用是否齐全\n   - Eikema et al. (2025) 是否应从 Discussion 前移到 Related Work\n   - MBR decoding 在非 MT 任务中的应用文献\n   - 引用格式和 bib 条目准确性（如 nedellec2026 bib key 与实际第一作者不一致）\n\n4. **格式合规（ARR/EMNLP 要求）**：\n   - **页数限制**：正文是否 ≤8 页（这是最高优先级检查项，超页 = desk rejection）\n   - Limitations section 是否存在且实质\n   - Ethics Statement 是否存在\n   - 匿名性检查（作者信息、自引暴露）\n   - 引用格式是否符合 ACL style\n\n5. **写作质量**：\n   - 术语一致性\n   - 表格/图表的可读性和 caption 质量\n   - VC 公式与实现是否一致（Table 3 标注）\n\n### 参考：Issue Tracker 中与你审查范围相关的 open/in_progress 问题\n\n- R3-W2/R5-C2: Gap 概念部分 tautological（critical）\n- R3-W5/R5-W5: Cross-model 实为 cross-architecture at fixed 8B（warning）\n- R4-W3: Abstract 过于密集（warning）\n- R5-N1: 与 Nédellec et al. (2026) 增量贡献不充分（warning）\n- R5-W7: SJ 方法论新颖性有限（warning）\n- R7-W2: Contribution 1 定性有分歧（warning）\n- R7-W3/R5-M2: Eikema et al. (2025) 应前移到 Related Work（warning）\n- R6-W1: VC 公式与实现不一致（warning）\n- R8-N1: 正文页数严重超过 8 页限制（critical）\n- R8-N2: 标题 \"Do Not Select\" overclaim（critical）\n- R8-W1: 缺少代码/数据发布承诺（warning）\n- R8-M1: nedellec2026 bib key 与实际第一作者不一致（info）\n- R7-W4: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B（critical）\n\n请独立审稿，不受上述 issue 列表局限——如有新发现请完整报告。\n\n### 输出格式\n```\n## Summary\n## Strengths（逐条）\n## Weaknesses（逐条，标注 severity: critical/warning/info）\n## Questions（需作者澄清的问题）\n## Missing References\n## Overall Assessment（评分 + 置信度）\n## Detailed Comments（逐节）\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "9",
    "project": "struct_self_consist_ie",
    "text": "## Round 9 审稿任务 — Reviewer 2\n\n### 你的审查侧重：新颖性 + 完整性 + 格式合规\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页（双栏 ACL 模板），参考文献不限页，Limitations 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各 section 在 `projects/struct_self_consist_ie/docs/paper/sections/` 下\n- Appendix: `projects/struct_self_consist_ie/docs/paper/sections/appendix.tex`\n\n### 审查重点（新颖性 + 完整性 + 格式合规）\n\n请重点审查以下方面：\n\n1. **核心贡献新颖性**：\n   - Correlation-selection gap 是否是 genuine finding 还是 tautological（instance-level 信号无法 select 是否是定义必然）\n   - 与 Nédellec et al. (2026) 的增量贡献是否充分\n   - SJ (Soft Jaccard) 方法论新颖性\n   - Contribution 1（multi-metric evaluation）是否应为 contribution 还是 finding\n\n2. **Framing 与 Claim Scope**：\n   - 标题 \"Do Not Select\" 是否 overclaim（LP 在子集上 significantly selects，RE free-form 下翻转为正）\n   - \"8B-Scale\" 是否过度暗示泛化性\n   - Cross-architecture 用词是否准确（实为 fixed 8B scale 两架构）\n   - Abstract 信息密度是否适当\n\n3. **Related Work 覆盖**：\n   - 关键引用是否齐全\n   - Eikema et al. (2025) 是否应从 Discussion 前移到 Related Work\n   - MBR decoding 在非 MT 任务中的应用文献\n   - 引用格式和 bib 条目准确性（如 nedellec2026 bib key 与实际第一作者不一致）\n\n4. **格式合规（ARR/EMNLP 要求）**：\n   - **页数限制**：正文是否 ≤8 页（这是最高优先级检查项，超页 = desk rejection）\n   - Limitations section 是否存在且实质\n   - Ethics Statement 是否存在\n   - 匿名性检查（作者信息、自引暴露）\n   - 引用格式是否符合 ACL style\n\n5. **写作质量**：\n   - 术语一致性\n   - 表格/图表的可读性和 caption 质量\n   - VC 公式与实现是否一致（Table 3 标注）\n\n### 参考：Issue Tracker 中与你审查范围相关的 open/in_progress 问题\n\n- R3-W2/R5-C2: Gap 概念部分 tautological（critical）\n- R3-W5/R5-W5: Cross-model 实为 cross-architecture at fixed 8B（warning）\n- R4-W3: Abstract 过于密集（warning）\n- R5-N1: 与 Nédellec et al. (2026) 增量贡献不充分（warning）\n- R5-W7: SJ 方法论新颖性有限（warning）\n- R7-W2: Contribution 1 定性有分歧（warning）\n- R7-W3/R5-M2: Eikema et al. (2025) 应前移到 Related Work（warning）\n- R6-W1: VC 公式与实现不一致（warning）\n- R8-N1: 正文页数严重超过 8 页限制（critical）\n- R8-N2: 标题 \"Do Not Select\" overclaim（critical）\n- R8-W1: 缺少代码/数据发布承诺（warning）\n- R8-M1: nedellec2026 bib key 与实际第一作者不一致（info）\n- R7-W4: Appendix 表格模型名 Qwen 2.5-7B 应为 Qwen3-8B（critical）\n\n请独立审稿，不受上述 issue 列表局限——如有新发现请完整报告。\n\n### 输出格式\n```\n## Summary\n## Strengths（逐条）\n## Weaknesses（逐条，标注 severity: critical/warning/info）\n## Questions（需作者澄清的问题）\n## Missing References\n## Overall Assessment（评分 + 置信度）\n## Detailed Comments（逐节）\n```"
  }
}
````

</details>

---


### Tool result

_source line 918 · 2026-05-15T15:23:19.098197+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1562
}
```

</details>

---


### Assistant

_source line 919 · 2026-05-15T15:23:24.636083+00:00_

两位 Reviewer 已分配：

- **Reviewer 1**（方法严谨性 + 实验设计）→ 已触发
- **Reviewer 2**（新颖性 + 完整性 + 格式合规）→ 已触发

每位 Reviewer 收到了完整的 venue 信息（EMNLP 2026, 8 页限制, double-blind, ARR May cycle）、论文路径、审查侧重指引，以及 Issue Tracker 中对应领域的 open/in_progress 问题清单供参考。

等待两位 Reviewer 提交独立初审报告，收到后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 73

## Round 73

2 recorded events


### User

_source line 920 · 2026-05-15T15:30:15.371008+00:00_

[Reviewer 2 审稿意见]:
## Round 9 — Reviewer 2 审稿报告（新颖性 + 完整性 + 格式合规）

### Summary

本文系统评估五种信心信号在 LLM 结构化 IE 中的质量估计和样本选择能力，发现 correlation-selection gap：所有信号在 QE 上表现良好但无法显著改善 best-of-N 选择。实验设计严谨、统计方法论扎实，但核心发现的新颖性受限于 tautological framing。

### Overall: 3/5 — Findings（非 Main Conference）

| 维度 | 分数 |
|------|------|
| Soundness | 3.5/5 |
| Excitement | 2.5/5 |
| Reproducibility | 3/5 |
| Confidence | 4/5 |

---

### Strengths（5 条）

- **S1**: 质量估计 vs 样本选择的概念区分清晰且有实际指导意义
- **S2**: 统计方法论（3-seed, TOST, Fisher combination, bootstrap CI, diversity-stratified）远超领域平均
- **S3**: 透明度突出——坦诚报告 enable_thinking confound、seed 456 混用、RE 单 benchmark 等限制
- **S4**: LP 压缩因果分析有说服力（non-tied subset +2.9pp p=0.01 + free-form 消融）
- **S5**: difficulty-dependent signal ranking 交叉现象有实用价值

---

### Critical Issues（3 条）

**W1 [critical] Correlation-selection gap 部分 tautological**
- §1 line 23 自述 "definitional, not empirical"；§5 Layer 1 确认 4/5 信号 by construction 无法选择
- 论文将 definitional 部分与 genuine empirical finding（LP 压缩、MBR misalignment）混合呈现，膨胀贡献感
- 建议：将 instance-level 失败一句话带过，叙事重心转移到 LP 压缩和 MBR misalignment

**W2 [critical] 标题 "Do Not Select" overclaim**
- 论文自身报告三处 significant selection：(1) LP non-tied subset +2.9pp p=0.01; (2) CoNLL N=16 VC +0.28pp p<0.03; (3) RE free-form LP +1.69pp
- 建议改为 "Rarely Select" 或 "Predict Better Than They Select"

**W3 [critical] 正文可能超 8 页限制**
- 无法编译确认精确页数，但根据内容体量（Introduction 含 full-width figure + Experiments 含 3 full-width figures/tables + Method 含 6 公式 + Discussion + Conclusion）估算正文约 9-9.5 页
- ARR 超页 = desk rejection，需立即编译确认

---

### Warning Issues（5 条）

**W4 [warning]** 与 Nédellec et al. (2026) 增量有限——QE 结果是 corroboration（论文自述），SJ-EM gap 仅 borderline significant (Appendix E CI 下界 +0.003)

**W5 [warning]** "8B-Scale" / "cross-architecture" 暗示过度泛化——实为 fixed 8B 两架构，未测试 70B+ 或 closed-source

**W6 [warning]** Contribution 1（multi-metric evaluation）是 empirical finding 非 methodological contribution

**W7 [warning]** 缺少代码/数据发布承诺，ARR Reproducibility 和 Software 维度受影响

**W8 [warning]** Abstract 信息密度过高，核心 message 被淹没

---

### Info Issues（2 条）

**W9 [info]** `nedellec2026` bib key 第一作者实际为 Yao——渲染正确但 key 误导

**W10 [info]** VC notation 不一致——Eq.6 为连续 QE，选择时用 majority threshold，同一缩写两种计算

---

### 引用验证

- 62 entries, 0 orphan, 0 missing bib
- OpenAlex: 56 verified, 3 not found (hobelsberger2025/lightman2024/venktesh2025, 均为真实论文, 索引延迟), 3 minor format mismatch (非实际错误)
- Eikema et al. (2025) 已在 Related Work §2 line 27 出现，处理得当
- 整体引用质量良好，覆盖充分

---

### 与 Issue Tracker 的交叉对照

| Issue | 我的独立判断 |
|-------|-------------|
| R3-W2/R5-C2 Gap tautological | **AGREE** — 确认 4/5 信号 definitional failure (W1) |
| R8-N2 标题 overclaim | **AGREE** — 三处 significant selection 反例 (W2) |
| R8-N1 超页 | **AGREE** — 内容体量估算超 8 页 (W3) |
| R5-N1 增量不充分 | **AGREE** — QE 是 corroboration (W4) |
| R3-W5/R5-W5 cross-architecture | **AGREE** — fixed 8B 两架构 (W5) |
| R7-W2 Contribution 1 | **AGREE** — finding 非 contribution (W6) |
| R8-W1 缺代码发布 | **AGREE** (W7) |
| R4-W3 Abstract 密集 | **AGREE** (W8) |
| R8-M1 nedellec bib key | **AGREE** (W9) |
| R6-W1 VC 公式不一致 | **AGREE** — notation 双重含义 (W10) |
| R5-W7 SJ 新颖性有限 | **AGREE** — 标准 engineering 组合，非方法论创新 |
| R7-W3/R5-M2 Eikema 前移 | **已解决** — Eikema 已在 §2 Related Work 中出现 |
| R7-W4 Appendix 模型名错误 | **无法独立确认** — Appendix 统一使用 "Qwen" 简称，未见 "Qwen 2.5-7B" |

### 新发现（未在 Issue Tracker 中）

**NEW-1 [warning]**: §5 Ablation 使用 `\label{sec:ablation}` 但嵌套在 Discussion §5 内而非独立 section，从 Abstract 和 §1 引用 "§Ablation" 可能让读者找不到位置。

**NEW-2 [info]**: Q2 提出 meta-signal 思路——LP range 可作为是否 apply LP selection 的门控信号——这是论文未探索但可能有价值的方向，可加入 future work。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 921 · 2026-05-15T15:30:22.316486+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 74

## Round 74

2 recorded events


### User

_source line 922 · 2026-05-15T15:30:24.865937+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已汇报给 Review Director。

**审稿结论：Overall 3/5 (Findings)**

关键发现：
- **3 个 critical issues**：(1) correlation-selection gap 对 4/5 信号是 tautological 而非经验发现；(2) 标题 "Do Not Select" overclaim（论文自身有三处 significant selection 反例）；(3) 正文可能超 8 页限制
- **5 个 warning issues**：增量贡献有限、"8B-Scale" 泛化性暗示、Contribution 1 定性偏差、缺代码发布承诺、Abstract 过密
- **2 个新发现**：Ablation section label 嵌套问题；LP range 可作为 meta-signal 的未探索方向
- **引用质量良好**：62 entries 全部匹配，无 orphan/missing，OpenAlex 验证 56/62 通过

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 923 · 2026-05-15T15:30:31.956094+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 完成独立初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 75

## Round 75

2 recorded events


### User

_source line 924 · 2026-05-15T15:43:00.813149+00:00_

[Reviewer 1 审稿结果]:
全部论文材料已读完。现在进行系统性审查。

让我先验证引用，同时撰写审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 925 · 2026-05-15T15:43:09.100461+00:00_

等待 Reviewer 1 完成审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 76

## Round 76

74 recorded events


### User

_source line 926 · 2026-05-16T02:14:16.128468+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 927 · 2026-05-16T02:14:22.770260+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 928 · 2026-05-16T02:14:22.821269+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 929 · 2026-05-16T02:14:27.189262+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 930 · 2026-05-16T02:14:27.189610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 931 · 2026-05-16T02:14:31.859311+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 932 · 2026-05-16T02:14:32.311442+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (104 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_qwen3_4b_scierc_merge_inference** (killed): SciERC 4B best checkpoint merge + SCS inference. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\n- **exp_qwen3_4b_conll_merge_inference_v2** (killed): CoNLL 4B checkpoint-4200 (best from resume training) merge + SCS inference. Replaces v1 which used checkpoint-3800 merged model. Cross-scale evidence for correlation-selection gap.\n- **exp_qwen3_4b_scierc_scs_inference** (success): SciERC 4B SCS inference after v4 finetune merge. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\n\n## 趋势\n成功 58 / 负向 22 / 失败 4 / 共 104\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_007_ner_llama: 已被终止 — unknown\n- exp001_seed123: 已被终止 — unknown\n- exp001_seed456: 已被终止 — unknown\n- exp008_re_n16: 已被终止 — unknown\n- exp_002_merge_conll2003: 已被终止 — unknown\n- exp_001_n16_seed123_full: 已被终止 — unknown\n- exp_001_n16_seed456_full: 已被终止 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp
…[truncated 653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 933 · 2026-05-16T02:14:32.813970+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md"
  }
}
```

</details>

---
