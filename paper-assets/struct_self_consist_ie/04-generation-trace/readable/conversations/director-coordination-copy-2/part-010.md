# Director coordination — Part 10 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 9](part-009.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 11 →](part-011.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 216

### Tool call

_source line 2845 · 2026-05-21T04:51:24.085058+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ===== 历史 resolved issues (保留) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3-old\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-9 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"scope 声明在 Introduction 和 Limitations 中已存在。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"仅2个~8B fine-tuned + 1个72B zero-shot。缺closed-source模型。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review: R1一句话总结提到'范围局限于NER + 2个~8B模型系列'。Limitations未提closed-source API degeneracy profile差异(R2-M5)。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7）。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26视觉审查再次确认p7 display items过密。\"\n      - round: 27\n        reviewers: [2]\n        note: \"R27-R2-M2: Figure 2 bar chart灰度打印时颜色难区分，建议用hatching patterns。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 27\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"construction不应作为standalone contribution。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review: R1-W1效果量边际(≤+1.39pp)，R2-W4 cost-benefit未讨论(8x推理换~1pp)。R1交叉AGREE，R2交叉同意实用价值有限但认为对negative result论文边际escape route恰当。\"\n    action_items:\n      - round: 26\n        action: \"确认construction在正文中已降级为diagnostic-motivated ablation而非contribution。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction（framing tautology）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 26\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 必须重构Abstract/Intro将structural/empirical二分法前置。\"\n    action_items:\n      - round: 26\n        action: \"重构Abstract和Introduction前置structural/empirical二分法。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Reduced to 4 key numbers.\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  # ===== Round 24 issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 公式删除，改为定性叙述。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"method.tex 加定义。\"\n    resolution_round: 24\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  # ===== Round 25 issues =====\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"n=23 power 仅约 50% for ρ=0.4。结论过强。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及此 specific null finding。\"\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"cross-model仅1数据集1对模型。§5.3 SCD不再出现。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"'first systematic characterization'过强，应限定为'for NER'。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review: R1-W2标题'Structured Generation'范围过宽(实验仅NER+1 exploratory RE)。R2-W3 RE extension单数据集单模型不足以支撑'structured IE' scope。交叉后两人完全共识。\"\n    action_items:\n      - round: 27\n        action: \"标题从'Structured Generation'缩窄为'Named Entity Recognition'或'Structured Information Extraction'。Abstract/Intro scope相应调整。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni；4 数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"CoNLL 增益为负 (−0.29pp)。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"p_adj矛盾(§1: 0.20 vs Table 13: 0.038)。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1-W1效果量最大+1.39pp与标注噪声量级相当。R2-W4 +1.09pp的cost-benefit存疑(8x推理开销)。R1交叉AGREE；R2 partial rebut(negative result论文的escape routes不需要大效果)。\"\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"脚注9报告k=38但Table 13列k=57，差异k=19来源不明。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"fine-tuning/scale/architecture混淆。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及此specific混淆。\"\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    resolution_round: null\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"SciERC single-seed用于detailed diagnostic。bootstrap CI有缓解但不够。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review R1-N2 [critical]: SciERC 3-seed vs 其他 1-seed不对称。Few-NERD(最强正面信号+1.39pp)无法验证跨seed稳定性。R2交叉AGREE(略降严重度，引用Table 11和Table 20作为缓解证据)。共识: 至少Few-NERD补3-seed。\"\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"嵌套NER场景何时violated未讨论。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"bound仅解释3-12%的gap。共识: 可降级为analysis tool。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review R1-N1 [critical]: θ_crit=0.70嵌入SciERC经验参数(G_gap=14.8pp,ε=0.068)，非普适阈值。CoNLL(D=61.7%<0.70)上LP仍失效。R2交叉AGREE并补充Figure 9标题未标注data-specific。共识: 标注为data-dependent经验近似+多数据集敏感性分析。\"\n    action_items:\n      - round: 27\n        action: \"§6.3 θ_crit明确标注为data-dependent经验近似(非universal threshold)。增加CoNLL和Few-NERD的dataset-specific θ_crit估算。Figure 9标题标注SciERC-specific。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"未直接提及。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27-R2-W1: 与Yun et al. (2025) 'Price of Format: Diversity Collapse'差异化不够——其diversity collapse发现与本文degeneracy(82.9%输出一致)高度相关。R1交叉AGREE。建议§8/§9用3-4句明确区分: Yun关注diversity本身，本文关注diversity collapse对selection的功能性影响。\"\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 未找到/元数据不匹配/orphan bib\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"hobelsberger2025systematic疑似虚构，17 orphan bib entries。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review: 81 bib entries, 45 cited, 36 orphan(uncited)。两位Reviewer独立发现并共识清理。R2-N1额外发现5篇高度相关论文在bib中但未引用(Chen 'Two Failures', USC, Adaptive-Consistency, Atomic SC, Semantic Entropy)。R1交叉完全同意这是严重遗漏。\"\n    action_items:\n      - round: 27\n        action: \"清理36条orphan bib entries。确保5篇关键论文(Chen Two Failures, USC, Adaptive-Consistency, Atomic SC, Semantic Entropy)在§8中被引用和讨论。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 标注为descriptive diagnostic而非causal chain。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review R1-N3+R2-N2 [both critical]: cascade四阶段'Why'标题和Figure 1箭头暗示因果链，但证据全部是描述性/相关性(Spearman ρ, subgroup对比, AUROC)。§7.3自承'degeneracy alone does not predict LP direction'与§4因果叙事矛盾。R1建议'Why'→'Where and How'。两人交叉后强烈共识——这是本轮最需修改的问题。\"\n    action_items:\n      - round: 27\n        action: \"§3标题'Why Self-Verification Fails'→'Where Self-Verification Fails'或'How'。§4同理。全文软化因果语言为association/correlation。Figure 1箭头改为描述性标注。加一句显式声明cascade是descriptive diagnostic。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: EL4NER, Self-Certainty BoN 等\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"EL4NER必须引用。\"\n      - round: 27\n        reviewers: [2]\n        note: \"R27-R2额外提出8篇missing references: Chen Two Failures (TMLR), USC (ICML WS), Adaptive-Consistency (EMNLP), Atomic SC (EMNLP), Semantic Entropy (Nature), PASC 2025 (conformal prediction), SC failure for simple tasks (2025), Kuleshov & Liang 2015 (NeurIPS)。其中前5篇在bib中但未cite——R2认为这'尤其令人困惑'。R1交叉完全同意。\"\n    action_items:\n      - round: 27\n        action: \"优先补引并讨论: (1) Chen 'Two Failures' TMLR — 直接分析SC failure modes; (2) USC ICML WS; (3) Adaptive-Consistency EMNLP; (4) Atomic SC EMNLP; (5) Semantic Entropy Nature。酌情补引: PASC 2025, Kuleshov & Liang 2015。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"Oracle Scaling figure 已生成并集成。\"\n    resolution_round: 26\n\n  # ===== Round 26 issues (更新状态) =====\n\n  - id: \"R26-N1\"\n    summary: \"N=8/16对test-time compute scaling研究范围过窄\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"建议至少补N=32或论证N=8的cost-efficiency。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及N range。\"\n\n  - id: \"R26-N2\"\n    summary: \"Trained verifier (LightGBM AUC=0.923) 负面结果scope有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R26-W1\"\n    summary: \"论文同时做4件事，每项深度不够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及scope breadth，但R2评Excitement 3/5部分原因是novelty分散。\"\n\n  - id: \"R26-VIS1\"\n    summary: \"Page 7 display items严重过密（4表+1图）\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查agent超时未产出findings。\"\n\n  - id: \"R26-VIS2\"\n    summary: \"Figure 6 heatmap红绿色阶对色盲不友好\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查agent超时。\"\n\n  # ===== Round 27 新发现 =====\n\n  - id: \"R27-N1\"\n    summary: \"§8 Related Work 仅~0.5页，覆盖严重不足\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R2-N1 [critical] + R2-W2 [warning]: §8仅~0.5页，缺少conformal prediction(PASC 2025)、SC code generation failure、entity-level hallucination detection方向。5篇直接相关论文在bib中未引用。R1交叉完全同意扩充至~1页。\"\n    action_items:\n      - round: 27\n        action: \"§8扩充至0.75-1页: 新增SC failure modes方向(Chen Two Failures)、fine-grained SC变体(USC, Atomic SC, Adaptive-Consistency)、sample-based不确定性(Semantic Entropy)、conformal prediction(PASC 2025)、与Yun et al. 2025差异化讨论。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R27-W1\"\n    summary: \"LODO transfer 分析不充分\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"R1-W3: 未识别transfer-critical特征，'introspection boundary'论证不完整。R2交叉REBUT: 论文claim是'transfer fails'而非'we can do transfer'，§4/§9/Appendix h.3逻辑链完整，额外要求超出claim支撑范围(ARR H13)。\"\n\n  - id: \"R27-W2\"\n    summary: \"缺少 structured MBR baseline 实验对比\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W4: §6.1引用Eikema et al. 2025但未实验对比。R2交叉AGREE: 至少应实现standard MBR with token-level F1 utility或对比不同utility function下的MBR表现。这是验证Proposition 1实际有效性的必要步骤。\"\n    action_items:\n      - round: 27\n        action: \"考虑添加MBR baseline(token-level F1 utility)或在Discussion中解释为何entity-level MBR形式化已足够，standard MBR不适用于NER的原因。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R27-M1\"\n    summary: \"per-sample signal 定义完全defer到Appendix\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"R2-M1: §2.1首次使用时应给简要定义，不应完全defer到Appendix a。R1未回应此点。\"\n\n  - id: \"R27-M2\"\n    summary: \"§6.2 inverse scaling 机制解释不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"R2-M4: SciERC converges more slowly的具体机制仅一句带过。R1交叉AGREE。\"\n\n  - id: \"R27-M3\"\n    summary: \"Limitations 未讨论closed-source API模型的degeneracy profile差异\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"R2-M5: 现有Limitations仅提LP signal不可用，未讨论这些模型是否有不同的degeneracy特征。R1交叉AGREE。\""
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
    "issues_yaml": "issues:\n  # ===== 历史 resolved issues (保留) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3-old\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-9 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"scope 声明在 Introduction 和 Limitations 中已存在。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"仅2个~8B fine-tuned + 1个72B zero-shot。缺closed-source模型。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review: R1一句话总结提到'范围局限于NER + 2个~8B模型系列'。Limitations未提closed-source API degeneracy profile差异(R2-M5)。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7）。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26视觉审查再次确认p7 display items过密。\"\n      - round: 27\n        reviewers: [2]\n        note: \"R27-R2-M2: Figure 2 bar chart灰度打印时颜色难区分，建议用hatching patterns。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 27\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"construction不应作为standalone contribution。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review: R1-W1效果量边际(≤+1.39pp)，R2-W4 cost-benefit未讨论(8x推理换~1pp)。R1交叉AGREE，R2交叉同意实用价值有限但认为对negative result论文边际escape route恰当。\"\n    action_items:\n      - round: 26\n        action: \"确认construction在正文中已降级为diagnostic-motivated ablation而非contribution。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction（framing tautology）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 26\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 必须重构Abstract/Intro将structural/empirical二分法前置。\"\n    action_items:\n      - round: 26\n        action: \"重构Abstract和Introduction前置structural/empirical二分法。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Reduced to 4 key numbers.\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  # ===== Round 24 issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 公式删除，改为定性叙述。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"method.tex 加定义。\"\n    resolution_round: 24\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  # ===== Round 25 issues =====\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"n=23 power 仅约 50% for ρ=0.4。结论过强。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及此 specific null finding。\"\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"cross-model仅1数据集1对模型。§5.3 SCD不再出现。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"'first systematic characterization'过强，应限定为'for NER'。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review: R1-W2标题'Structured Generation'范围过宽(实验仅NER+1 exploratory RE)。R2-W3 RE extension单数据集单模型不足以支撑'structured IE' scope。交叉后两人完全共识。\"\n    action_items:\n      - round: 27\n        action: \"标题从'Structured Generation'缩窄为'Named Entity Recognition'或'Structured Information Extraction'。Abstract/Intro scope相应调整。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni；4 数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"CoNLL 增益为负 (−0.29pp)。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"p_adj矛盾(§1: 0.20 vs Table 13: 0.038)。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1-W1效果量最大+1.39pp与标注噪声量级相当。R2-W4 +1.09pp的cost-benefit存疑(8x推理开销)。R1交叉AGREE；R2 partial rebut(negative result论文的escape routes不需要大效果)。\"\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"脚注9报告k=38但Table 13列k=57，差异k=19来源不明。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"fine-tuning/scale/architecture混淆。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及此specific混淆。\"\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    resolution_round: null\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"SciERC single-seed用于detailed diagnostic。bootstrap CI有缓解但不够。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review R1-N2 [critical]: SciERC 3-seed vs 其他 1-seed不对称。Few-NERD(最强正面信号+1.39pp)无法验证跨seed稳定性。R2交叉AGREE(略降严重度，引用Table 11和Table 20作为缓解证据)。共识: 至少Few-NERD补3-seed。\"\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"嵌套NER场景何时violated未讨论。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"bound仅解释3-12%的gap。共识: 可降级为analysis tool。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review R1-N1 [critical]: θ_crit=0.70嵌入SciERC经验参数(G_gap=14.8pp,ε=0.068)，非普适阈值。CoNLL(D=61.7%<0.70)上LP仍失效。R2交叉AGREE并补充Figure 9标题未标注data-specific。共识: 标注为data-dependent经验近似+多数据集敏感性分析。\"\n    action_items:\n      - round: 27\n        action: \"§6.3 θ_crit明确标注为data-dependent经验近似(非universal threshold)。增加CoNLL和Few-NERD的dataset-specific θ_crit估算。Figure 9标题标注SciERC-specific。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"未直接提及。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27-R2-W1: 与Yun et al. (2025) 'Price of Format: Diversity Collapse'差异化不够——其diversity collapse发现与本文degeneracy(82.9%输出一致)高度相关。R1交叉AGREE。建议§8/§9用3-4句明确区分: Yun关注diversity本身，本文关注diversity collapse对selection的功能性影响。\"\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 未找到/元数据不匹配/orphan bib\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"hobelsberger2025systematic疑似虚构，17 orphan bib entries。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review: 81 bib entries, 45 cited, 36 orphan(uncited)。两位Reviewer独立发现并共识清理。R2-N1额外发现5篇高度相关论文在bib中但未引用(Chen 'Two Failures', USC, Adaptive-Consistency, Atomic SC, Semantic Entropy)。R1交叉完全同意这是严重遗漏。\"\n    action_items:\n      - round: 27\n        action: \"清理36条orphan bib entries。确保5篇关键论文(Chen Two Failures, USC, Adaptive-Consistency, Atomic SC, Semantic Entropy)在§8中被引用和讨论。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 标注为descriptive diagnostic而非causal chain。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh review R1-N3+R2-N2 [both critical]: cascade四阶段'Why'标题和Figure 1箭头暗示因果链，但证据全部是描述性/相关性(Spearman ρ, subgroup对比, AUROC)。§7.3自承'degeneracy alone does not predict LP direction'与§4因果叙事矛盾。R1建议'Why'→'Where and How'。两人交叉后强烈共识——这是本轮最需修改的问题。\"\n    action_items:\n      - round: 27\n        action: \"§3标题'Why Self-Verification Fails'→'Where Self-Verification Fails'或'How'。§4同理。全文软化因果语言为association/correlation。Figure 1箭头改为描述性标注。加一句显式声明cascade是descriptive diagnostic。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: EL4NER, Self-Certainty BoN 等\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"EL4NER必须引用。\"\n      - round: 27\n        reviewers: [2]\n        note: \"R27-R2额外提出8篇missing references: Chen Two Failures (TMLR), USC (ICML WS), Adaptive-Consistency (EMNLP), Atomic SC (EMNLP), Semantic Entropy (Nature), PASC 2025 (conformal prediction), SC failure for simple tasks (2025), Kuleshov & Liang 2015 (NeurIPS)。其中前5篇在bib中但未cite——R2认为这'尤其令人困惑'。R1交叉完全同意。\"\n    action_items:\n      - round: 27\n        action: \"优先补引并讨论: (1) Chen 'Two Failures' TMLR — 直接分析SC failure modes; (2) USC ICML WS; (3) Adaptive-Consistency EMNLP; (4) Atomic SC EMNLP; (5) Semantic Entropy Nature。酌情补引: PASC 2025, Kuleshov & Liang 2015。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"Oracle Scaling figure 已生成并集成。\"\n    resolution_round: 26\n\n  # ===== Round 26 issues (更新状态) =====\n\n  - id: \"R26-N1\"\n    summary: \"N=8/16对test-time compute scaling研究范围过窄\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"建议至少补N=32或论证N=8的cost-efficiency。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及N range。\"\n\n  - id: \"R26-N2\"\n    summary: \"Trained verifier (LightGBM AUC=0.923) 负面结果scope有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R26-W1\"\n    summary: \"论文同时做4件事，每项深度不够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及scope breadth，但R2评Excitement 3/5部分原因是novelty分散。\"\n\n  - id: \"R26-VIS1\"\n    summary: \"Page 7 display items严重过密（4表+1图）\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查agent超时未产出findings。\"\n\n  - id: \"R26-VIS2\"\n    summary: \"Figure 6 heatmap红绿色阶对色盲不友好\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查agent超时。\"\n\n  # ===== Round 27 新发现 =====\n\n  - id: \"R27-N1\"\n    summary: \"§8 Related Work 仅~0.5页，覆盖严重不足\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R2-N1 [critical] + R2-W2 [warning]: §8仅~0.5页，缺少conformal prediction(PASC 2025)、SC code generation failure、entity-level hallucination detection方向。5篇直接相关论文在bib中未引用。R1交叉完全同意扩充至~1页。\"\n    action_items:\n      - round: 27\n        action: \"§8扩充至0.75-1页: 新增SC failure modes方向(Chen Two Failures)、fine-grained SC变体(USC, Atomic SC, Adaptive-Consistency)、sample-based不确定性(Semantic Entropy)、conformal prediction(PASC 2025)、与Yun et al. 2025差异化讨论。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R27-W1\"\n    summary: \"LODO transfer 分析不充分\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"R1-W3: 未识别transfer-critical特征，'introspection boundary'论证不完整。R2交叉REBUT: 论文claim是'transfer fails'而非'we can do transfer'，§4/§9/Appendix h.3逻辑链完整，额外要求超出claim支撑范围(ARR H13)。\"\n\n  - id: \"R27-W2\"\n    summary: \"缺少 structured MBR baseline 实验对比\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W4: §6.1引用Eikema et al. 2025但未实验对比。R2交叉AGREE: 至少应实现standard MBR with token-level F1 utility或对比不同utility function下的MBR表现。这是验证Proposition 1实际有效性的必要步骤。\"\n    action_items:\n      - round: 27\n        action: \"考虑添加MBR baseline(token-level F1 utility)或在Discussion中解释为何entity-level MBR形式化已足够，standard MBR不适用于NER的原因。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R27-M1\"\n    summary: \"per-sample signal 定义完全defer到Appendix\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"R2-M1: §2.1首次使用时应给简要定义，不应完全defer到Appendix a。R1未回应此点。\"\n\n  - id: \"R27-M2\"\n    summary: \"§6.2 inverse scaling 机制解释不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"R2-M4: SciERC converges more slowly的具体机制仅一句带过。R1交叉AGREE。\"\n\n  - id: \"R27-M3\"\n    summary: \"Limitations 未讨论closed-source API模型的degeneracy profile差异\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"R2-M5: 现有Limitations仅提LP signal不可用，未讨论这些模型是否有不同的degeneracy特征。R1交叉AGREE。\""
  }
}
```

</details>

---


### Tool result

_source line 2846 · 2026-05-21T04:51:24.187892+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 34012}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2847 · 2026-05-21T04:53:32.246646+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 27 (Fresh Review)\n\n**论文**: The Capability Ceiling of Self-Consistency: Why Entity-Level Self-Verification Fails in Structured Generation\n**Venue**: EMNLP 2026 Main Conference (Long Paper), ARR May cycle\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（无历史轮次记忆）\n**Reviewer**: R1（方法严谨性）+ R2（新颖性/完整性）\n**轮次**: Round 1 初审 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文系统研究了 self-consistency (SC) 在结构化信息抽取（主要是 NER）中的能力天花板。通过四阶段诊断框架（QE → degeneracy → agreement fidelity → LP compression），论文揭示了一个 \"correlation-selection gap\"：虽然 entity-level agreement signals（如 SJ, VC）与质量存在正相关，但无法有效转化为 sample selection 增益。核心原因是 instance degeneracy——在 fine-tuned 模型上 82.9%（SciERC）的输出完全一致，selection 无从下手。论文测试了七种 entity-level self-verification 方法均告失败，并提出 entity-level construction 和 cross-model ensemble 作为 escape routes。理论贡献包括将 NER SC 形式化为 entity-level MBR decoding 和 degeneracy decomposition 上界。\n\n---\n\n## Strengths\n\n**S1. 实验规模和统计严谨性出色。** 4 个 NER 数据集（SciERC, Few-NERD, CoNLL, WNUT-17）、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）、N∈{2,...,32}、3 seeds（部分）。统计检验完备：Holm-Bonferroni 多重校正、paired bootstrap CI、permutation tests、TOST 等价性检验。42 页附录覆盖几乎所有合理 ablation。[共识]\n\n**S2. Diagnostic cascade 框架有独立工具价值。** 四阶段分解将模糊问题（\"为什么 SC 不 work\"）转化为可操作的诊断步骤。Figure 1 概括力强。对 instance degeneracy 的量化（82.9% identical outputs, Table 2）提供了有力的失效解释。[共识]\n\n**S3. 七种 entity-level self-verification 方法的系统性 negative result。** ESJ, MRSC, LSC, hidden-state probe, ASB, SCD, supervised classifier 逐一测试均 fail，形成令人信服的 negative result。Hidden-state probe AUROC 0.63-0.88 但无法转化为 selection gain——说明质量信号存在但无法 operationalize。[共识]\n\n**S4. MBR 理论联系。** Proposition 1（majority-vote 是 balanced set-overlap utility 下的 MBR optimal）和 Degeneracy Decomposition（E[ΔF1] ≤ (1-D)·G_nd）提供理论基础。[共识]\n\n**S5. 诚实报告负面结果 + prescriptive protocol。** Entity construction (+1.09pp Few-NERD), LP-weighted construction, cross-model ensemble 具实用价值。[共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，共 4 个）\n\n**MF1. [critical] Cascade 因果声称与相关性证据不匹配** [R1-N3 + R2-N2, 强共识]\n- §3 \"Why Self-Verification Fails\"、§4 \"Why Single-Signal Selection Fails\" 的 \"Why\" 标题和 Figure 1 箭头暗示因果链\n- 实际证据全部是描述性/相关性：Spearman ρ、subgroup 对比、AUROC\n- §7.3 自承 \"degeneracy alone does not predict LP direction\"，与 §4 因果叙事存在内部矛盾\n- **建议**: \"Why\" → \"Where and How\"；全文软化因果语言为 association/correlation；加显式声明 cascade 是 descriptive diagnostic 而非 causal model\n\n**MF2. [critical] Related Work 严重不足** [R2-N1 + R2-W2, R1 交叉完全同意]\n- §8 仅 ~0.5 页\n- 5 篇高度相关论文在 .bib 中但未在正文引用：Chen et al. (2024) \"Two Failures of SC\" (TMLR)、Chen et al. (2024) \"Universal SC\" (ICML WS)、Aggarwal et al. (2023) \"Adaptive-Consistency\" (EMNLP)、Thirukovalluru et al. (2024) \"Atomic SC\" (EMNLP)、Farquhar et al. (2024) \"Semantic Entropy\" (Nature)\n- 缺乏对 conformal prediction、SC code generation failure、entity-level hallucination detection 方向的覆盖\n- Chen \"Two Failures\" 从 reasoning 角度分析 SC failure modes，不讨论会让审稿人质疑 novelty claim\n- **建议**: §8 扩充至 0.75-1 页；补引上述论文并讨论差异化贡献\n\n**MF3. [critical] θ_crit=0.70 半经验推导但呈现为理论结果** [R1-N1, R2 交叉完全同意]\n- §6.3 / Appendix p.3 / Figure 9: θ_crit 公式嵌入 SciERC 经验参数（G_gap=14.8pp, ε=0.068）\n- CoNLL（D=61.7% < 0.70）上 LP 选择也失效，说明该阈值非普适\n- Figure 9 标题未标注 data-specific\n- **建议**: 明确标注为 data-dependent 经验近似；增加 CoNLL/Few-NERD 的 dataset-specific θ_crit 敏感性分析\n\n**MF4. [critical] 种子数不对称影响统计效力均衡性** [R1-N2, R2 交叉同意但略降严重度]\n- SciERC 3 seeds vs. Few-NERD/CoNLL 1 seed\n- Few-NERD（最强正面信号 +1.39pp）无法验证跨 seed 稳定性\n- 核心负面结论在 3/4 数据集上依赖单次运行\n- 缓解因素：Table 11 (3-seed mean)、Table 20 (multi-seed stability)、bootstrap CI 部分覆盖\n- **建议**: 至少为 Few-NERD 补做 3-seed 实验\n\n### Should-Fix（影响评分但不一票否决，共 6 个）\n\n**SF1. [warning] 标题 \"Structured Generation\" 范围过宽** [R1-W2 + R2-W3, 强共识]\n- 实验仅覆盖 NER（4 datasets）+ 1 个 exploratory RE（单数据集单模型）\n- \"Structured Generation\" 在 NLP 社区涵盖 code/SQL/JSON 等\n- **建议**: 标题缩窄为 \"Named Entity Recognition\" 或 \"Structured Information Extraction\"\n\n**SF2. [warning] Escape routes 效果量边际 + cost-benefit 缺失** [R1-W1 + R2-W4, 共识但有 nuance]\n- 最大增益 +1.39pp（Few-NERD LP selection），entity construction +1.09pp\n- 8x 推理开销换 ~1pp F1，实用价值存疑\n- R2 partial rebut: 对 negative result 论文，边际 escape routes 恰好强化负面结论\n- R1 rebut R2: entity construction 是 post-hoc aggregation，边际成本为零（已有 N 个样本时）\n- **建议**: §9 增加 cost-benefit 分析框架\n\n**SF3. [warning] 与 Yun et al. (2025) \"Diversity Collapse\" 差异化不够** [R2-W1, R1 交叉同意]\n- Yun et al. 已证明 constrained decoding 导致 diversity collapse，与本文 degeneracy 发现高度相关\n- §8 仅一句引用\n- **建议**: 明确区分——Yun 关注 diversity 本身，本文关注 diversity collapse 对 downstream selection 的功能性影响\n\n**SF4. [warning] 缺少 structured MBR baseline 实验对比** [R1-W4, R2 交叉同意]\n- §6.1 引用 Eikema et al. (2025) 但未实验对比\n- 至少应实现 standard MBR with token-level F1 utility，或对比不同 utility function\n- 验证 Proposition 1 实际有效性的必要步骤\n\n**SF5. [warning] 36 orphan bib entries** [R1 + R2 均发现]\n- 81 bib entries 中仅 45 被引用\n- 应清理未使用条目\n\n**SF6. [warning] Seed 不对称的统计影响** [与 MF4 关联但 severity 不同]\n- SciERC 是 primary test bed 但样本量小（n=529），MDE ≈ 1.5pp\n- Few-NERD 作为 \"definitive test\" 但仅 1 seed\n- Bootstrap CI (B=10000) 部分缓解但不替代 cross-seed validation\n\n### Minor（不影响接收，共 6 个）\n\n**M1.** per-sample signal 定义完全 defer 到 Appendix（§2.1 首次使用时应给简要定义）\n**M2.** Figure 2 bar chart 灰度打印时颜色难区分（建议 hatching patterns）\n**M3.** Table 1 \"One score per input\" 列缺乏正文解释\n**M4.** §6.2 inverse scaling 机制（SciERC converges more slowly）仅一句带过\n**M5.** Limitations 未讨论 closed-source API 模型的 degeneracy profile 差异\n**M6.** 36 orphan bib entries 应清理\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全一致（交叉后无分歧）：\n\n1. **因果声称过强**（R1-N3 = R2-N2）— 最核心问题，§3/§4 的 \"Why\" 标题和 Figure 1 箭头必须修改\n2. **Related Work 严重不足**（R2-N1）— 5 篇直接相关论文在 bib 中未引用，§8 需大幅扩充\n3. **θ_crit 呈现方式误导**（R1-N1）— 必须标注为 data-dependent 经验近似\n4. **Scope overclaim**（R1-W2 = R2-W3）— 标题和 scope 需缩窄至 NER\n5. **Orphan bib entries**（R1 + R2）— 36 条未引用条目需清理\n6. **MBR baseline 缺失**（R1-W4）— Proposition 1 应有实验验证\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在温和分歧（不影响整体判断）：\n\n1. **LODO transfer 分析充分性**（R1-W3 vs R2 REBUT）— R1 认为不充分，R2 认为论文 claim 是 \"transfer fails\" 而非 \"we can do transfer\"，要求额外分析超出 claim 支撑范围（ARR H13）。**Director 判断**: R2 论证有理，transfer 分析充分度维持为 minor concern。\n\n2. **Cost-benefit 论证**（R2-W4 vs R1 partial REBUT）— R2 要求讨论 8x 推理开销的 cost-benefit，R1 指出 entity construction 是 post-hoc aggregation（边际成本为零）。**Director 判断**: 两者都有道理，建议添加简短 cost-benefit 讨论但不阻塞。\n\n3. **Table 1 列标签**（R2-M3 vs R1 REBUT）— R1 认为 §2.2 已定义，属常规做法。**Director 判断**: minor，不要求修改。\n\n4. **AUROC→selection gap 瓶颈**（R2-Q3 vs R1 REBUT）— R2 问是否 bottleneck 在 aggregation，R1 认为论文已解释为 degeneracy 限制可优化空间。**Director 判断**: 建议增加一句显式说明。\n\n---\n\n## Questions for Authors\n\n**Q1.** [R2] T>1.2 是否能 recover diversity 改善 selection？Appendix 温度分析仅到 T=1.2。\n**Q2.** [R2] 本文 failure mode 与 Chen et al. (2024) \"Two Failures\" 识别的 hypothetical/compositional consistency failure 的关系？\n**Q3.** [R2] Hidden-state probe AUROC 0.63-0.88 但 selection gain 有限——bottleneck 在 quality estimation 还是 aggregation？\n**Q4.** [R2] 是否考虑过 entity-level filtering（high-consistency select, low-consistency abstain）作为中间方案？\n\n---\n\n## Missing References\n\n**优先补引（在 .bib 中但未引用）**:\n1. Chen et al. (2024) \"Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs\" (TMLR)\n2. Chen et al. (2024) \"Universal Self-Consistency for Large Language Model Generation\" (ICML Workshop)\n3. Aggarwal et al. (2023) \"Let's Sample Step by Step: Adaptive-Consistency\" (EMNLP)\n4. Thirukovalluru et al. (2024) \"Atomic Self-Consistency for Better Long Form Generations\" (EMNLP)\n5. Farquhar et al. (2024) \"Detecting Hallucinations in LLMs Using Semantic Entropy\" (Nature)\n6. Kuleshov & Liang (2015) \"Calibrated Structured Prediction\" (NeurIPS) — 在 bib 中未引用\n\n**建议补引（可能不在 .bib 中）**:\n7. PASC (2025) \"Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP Pipelines\"\n8. \"Existing LLMs Are Not Self-Consistent For Simple Tasks\" (2025)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: pending（已于 2026-05-21T04:34 发送请求，尚未返回）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: agent 超时（300s timeout），无实际 findings。\n用户可选择重新触发视觉审查。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3 | 3 | 3 |\n| Reproducibility | 4 | 4 | 4 |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4 | 4 | 4 |\n\n**评价**: 实验质量出色，diagnostic cascade 有工具价值，负面结果对 practitioner 有直接 actionable 意义。但四个 Must-Fix 问题（因果声称、Related Work 缺口、θ_crit 呈现、seed 不对称）限制了当前版本的接收可能性。核心 insight（degeneracy 导致 SC 失效）novelty 有限——与 Yun et al. (2025) diversity collapse 发现存在重叠，增量贡献主要在于量化 diversity collapse 对 selection 的功能性影响。\n\n**修改后预期**: 如果 4 个 Must-Fix 全部解决（因果语言软化、§8 扩充、θ_crit 标注、seed 补充），论文可达 **3.0-3.5**（Findings 至 Borderline Conference）。是否能冲击 Main Conference 取决于 novelty argument 的改善——需要更清晰地回答 \"beyond Yun et al., what is new?\"。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Why\" framing 需全面软化为描述性语言\n- Scope claim 需限定为 NER 而非 structured generation\n\n### §2 Diagnostic Framework\n- per-sample signal 定义不应完全 defer 到 Appendix\n\n### §3 Why Self-Verification Fails → 建议改为 \"Where/How\"\n- Hidden-state probe AUROC 0.63-0.88 vs selection gain gap 可增加一句解释\n\n### §4 Why Single-Signal Selection Fails → 建议改为 \"Where/How\"\n- \"degeneracy alone does not predict LP direction\" (§7.3) 与本节因果叙事的张力需要显式 reconcile\n\n### §5 Adaptive Methods / Escape Routes\n- Cost-benefit 分析缺失\n- Cross-model SC 仅 1 数据集 1 对模型，需扩展或缩减\n\n### §6 Theory\n- §6.3 θ_crit 必须标注为 data-dependent；增加敏感性分析\n- Degeneracy decomposition 定位为 diagnostic tool 而非 tight bound\n\n### §7 Experiments\n- Seed 不对称需要解释和缓解（至少 Few-NERD 3-seed）\n- Holm-Bonferroni k 的 family 定义需透明化\n\n### §8 Related Work\n- 从 ~0.5 页扩充至 0.75-1 页\n- 必须覆盖：SC failure modes、fine-grained SC 变体、sample-based 不确定性、conformal prediction、Yun et al. 差异化\n\n### §9 Discussion\n- 增加 cost-benefit 分析\n- 增加 closed-source API 模型的 degeneracy 讨论\n\n### Limitations\n- 增加 closed-source API degeneracy profile 差异的讨论\n\n### References\n- 清理 36 orphan bib entries\n- 引用并讨论 5 篇在 bib 中但未引用的高度相关论文",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
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
    "report": "# 审稿报告 — Round 27 (Fresh Review)\n\n**论文**: The Capability Ceiling of Self-Consistency: Why Entity-Level Self-Verification Fails in Structured Generation\n**Venue**: EMNLP 2026 Main Conference (Long Paper), ARR May cycle\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（无历史轮次记忆）\n**Reviewer**: R1（方法严谨性）+ R2（新颖性/完整性）\n**轮次**: Round 1 初审 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文系统研究了 self-consistency (SC) 在结构化信息抽取（主要是 NER）中的能力天花板。通过四阶段诊断框架（QE → degeneracy → agreement fidelity → LP compression），论文揭示了一个 \"correlation-selection gap\"：虽然 entity-level agreement signals（如 SJ, VC）与质量存在正相关，但无法有效转化为 sample selection 增益。核心原因是 instance degeneracy——在 fine-tuned 模型上 82.9%（SciERC）的输出完全一致，selection 无从下手。论文测试了七种 entity-level self-verification 方法均告失败，并提出 entity-level construction 和 cross-model ensemble 作为 escape routes。理论贡献包括将 NER SC 形式化为 entity-level MBR decoding 和 degeneracy decomposition 上界。\n\n---\n\n## Strengths\n\n**S1. 实验规模和统计严谨性出色。** 4 个 NER 数据集（SciERC, Few-NERD, CoNLL, WNUT-17）、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）、N∈{2,...,32}、3 seeds（部分）。统计检验完备：Holm-Bonferroni 多重校正、paired bootstrap CI、permutation tests、TOST 等价性检验。42 页附录覆盖几乎所有合理 ablation。[共识]\n\n**S2. Diagnostic cascade 框架有独立工具价值。** 四阶段分解将模糊问题（\"为什么 SC 不 work\"）转化为可操作的诊断步骤。Figure 1 概括力强。对 instance degeneracy 的量化（82.9% identical outputs, Table 2）提供了有力的失效解释。[共识]\n\n**S3. 七种 entity-level self-verification 方法的系统性 negative result。** ESJ, MRSC, LSC, hidden-state probe, ASB, SCD, supervised classifier 逐一测试均 fail，形成令人信服的 negative result。Hidden-state probe AUROC 0.63-0.88 但无法转化为 selection gain——说明质量信号存在但无法 operationalize。[共识]\n\n**S4. MBR 理论联系。** Proposition 1（majority-vote 是 balanced set-overlap utility 下的 MBR optimal）和 Degeneracy Decomposition（E[ΔF1] ≤ (1-D)·G_nd）提供理论基础。[共识]\n\n**S5. 诚实报告负面结果 + prescriptive protocol。** Entity construction (+1.09pp Few-NERD), LP-weighted construction, cross-model ensemble 具实用价值。[共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，共 4 个）\n\n**MF1. [critical] Cascade 因果声称与相关性证据不匹配** [R1-N3 + R2-N2, 强共识]\n- §3 \"Why Self-Verification Fails\"、§4 \"Why Single-Signal Selection Fails\" 的 \"Why\" 标题和 Figure 1 箭头暗示因果链\n- 实际证据全部是描述性/相关性：Spearman ρ、subgroup 对比、AUROC\n- §7.3 自承 \"degeneracy alone does not predict LP direction\"，与 §4 因果叙事存在内部矛盾\n- **建议**: \"Why\" → \"Where and How\"；全文软化因果语言为 association/correlation；加显式声明 cascade 是 descriptive diagnostic 而非 causal model\n\n**MF2. [critical] Related Work 严重不足** [R2-N1 + R2-W2, R1 交叉完全同意]\n- §8 仅 ~0.5 页\n- 5 篇高度相关论文在 .bib 中但未在正文引用：Chen et al. (2024) \"Two Failures of SC\" (TMLR)、Chen et al. (2024) \"Universal SC\" (ICML WS)、Aggarwal et al. (2023) \"Adaptive-Consistency\" (EMNLP)、Thirukovalluru et al. (2024) \"Atomic SC\" (EMNLP)、Farquhar et al. (2024) \"Semantic Entropy\" (Nature)\n- 缺乏对 conformal prediction、SC code generation failure、entity-level hallucination detection 方向的覆盖\n- Chen \"Two Failures\" 从 reasoning 角度分析 SC failure modes，不讨论会让审稿人质疑 novelty claim\n- **建议**: §8 扩充至 0.75-1 页；补引上述论文并讨论差异化贡献\n\n**MF3. [critical] θ_crit=0.70 半经验推导但呈现为理论结果** [R1-N1, R2 交叉完全同意]\n- §6.3 / Appendix p.3 / Figure 9: θ_crit 公式嵌入 SciERC 经验参数（G_gap=14.8pp, ε=0.068）\n- CoNLL（D=61.7% < 0.70）上 LP 选择也失效，说明该阈值非普适\n- Figure 9 标题未标注 data-specific\n- **建议**: 明确标注为 data-dependent 经验近似；增加 CoNLL/Few-NERD 的 dataset-specific θ_crit 敏感性分析\n\n**MF4. [critical] 种子数不对称影响统计效力均衡性** [R1-N2, R2 交叉同意但略降严重度]\n- SciERC 3 seeds vs. Few-NERD/CoNLL 1 seed\n- Few-NERD（最强正面信号 +1.39pp）无法验证跨 seed 稳定性\n- 核心负面结论在 3/4 数据集上依赖单次运行\n- 缓解因素：Table 11 (3-seed mean)、Table 20 (multi-seed stability)、bootstrap CI 部分覆盖\n- **建议**: 至少为 Few-NERD 补做 3-seed 实验\n\n### Should-Fix（影响评分但不一票否决，共 6 个）\n\n**SF1. [warning] 标题 \"Structured Generation\" 范围过宽** [R1-W2 + R2-W3, 强共识]\n- 实验仅覆盖 NER（4 datasets）+ 1 个 exploratory RE（单数据集单模型）\n- \"Structured Generation\" 在 NLP 社区涵盖 code/SQL/JSON 等\n- **建议**: 标题缩窄为 \"Named Entity Recognition\" 或 \"Structured Information Extraction\"\n\n**SF2. [warning] Escape routes 效果量边际 + cost-benefit 缺失** [R1-W1 + R2-W4, 共识但有 nuance]\n- 最大增益 +1.39pp（Few-NERD LP selection），entity construction +1.09pp\n- 8x 推理开销换 ~1pp F1，实用价值存疑\n- R2 partial rebut: 对 negative result 论文，边际 escape routes 恰好强化负面结论\n- R1 rebut R2: entity construction 是 post-hoc aggregation，边际成本为零（已有 N 个样本时）\n- **建议**: §9 增加 cost-benefit 分析框架\n\n**SF3. [warning] 与 Yun et al. (2025) \"Diversity Collapse\" 差异化不够** [R2-W1, R1 交叉同意]\n- Yun et al. 已证明 constrained decoding 导致 diversity collapse，与本文 degeneracy 发现高度相关\n- §8 仅一句引用\n- **建议**: 明确区分——Yun 关注 diversity 本身，本文关注 diversity collapse 对 downstream selection 的功能性影响\n\n**SF4. [warning] 缺少 structured MBR baseline 实验对比** [R1-W4, R2 交叉同意]\n- §6.1 引用 Eikema et al. (2025) 但未实验对比\n- 至少应实现 standard MBR with token-level F1 utility，或对比不同 utility function\n- 验证 Proposition 1 实际有效性的必要步骤\n\n**SF5. [warning] 36 orphan bib entries** [R1 + R2 均发现]\n- 81 bib entries 中仅 45 被引用\n- 应清理未使用条目\n\n**SF6. [warning] Seed 不对称的统计影响** [与 MF4 关联但 severity 不同]\n- SciERC 是 primary test bed 但样本量小（n=529），MDE ≈ 1.5pp\n- Few-NERD 作为 \"definitive test\" 但仅 1 seed\n- Bootstrap CI (B=10000) 部分缓解但不替代 cross-seed validation\n\n### Minor（不影响接收，共 6 个）\n\n**M1.** per-sample signal 定义完全 defer 到 Appendix（§2.1 首次使用时应给简要定义）\n**M2.** Figure 2 bar chart 灰度打印时颜色难区分（建议 hatching patterns）\n**M3.** Table 1 \"One score per input\" 列缺乏正文解释\n**M4.** §6.2 inverse scaling 机制（SciERC converges more slowly）仅一句带过\n**M5.** Limitations 未讨论 closed-source API 模型的 degeneracy profile 差异\n**M6.** 36 orphan bib entries 应清理\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 完全一致（交叉后无分歧）：\n\n1. **因果声称过强**（R1-N3 = R2-N2）— 最核心问题，§3/§4 的 \"Why\" 标题和 Figure 1 箭头必须修改\n2. **Related Work 严重不足**（R2-N1）— 5 篇直接相关论文在 bib 中未引用，§8 需大幅扩充\n3. **θ_crit 呈现方式误导**（R1-N1）— 必须标注为 data-dependent 经验近似\n4. **Scope overclaim**（R1-W2 = R2-W3）— 标题和 scope 需缩窄至 NER\n5. **Orphan bib entries**（R1 + R2）— 36 条未引用条目需清理\n6. **MBR baseline 缺失**（R1-W4）— Proposition 1 应有实验验证\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在温和分歧（不影响整体判断）：\n\n1. **LODO transfer 分析充分性**（R1-W3 vs R2 REBUT）— R1 认为不充分，R2 认为论文 claim 是 \"transfer fails\" 而非 \"we can do transfer\"，要求额外分析超出 claim 支撑范围（ARR H13）。**Director 判断**: R2 论证有理，transfer 分析充分度维持为 minor concern。\n\n2. **Cost-benefit 论证**（R2-W4 vs R1 partial REBUT）— R2 要求讨论 8x 推理开销的 cost-benefit，R1 指出 entity construction 是 post-hoc aggregation（边际成本为零）。**Director 判断**: 两者都有道理，建议添加简短 cost-benefit 讨论但不阻塞。\n\n3. **Table 1 列标签**（R2-M3 vs R1 REBUT）— R1 认为 §2.2 已定义，属常规做法。**Director 判断**: minor，不要求修改。\n\n4. **AUROC→selection gap 瓶颈**（R2-Q3 vs R1 REBUT）— R2 问是否 bottleneck 在 aggregation，R1 认为论文已解释为 degeneracy 限制可优化空间。**Director 判断**: 建议增加一句显式说明。\n\n---\n\n## Questions for Authors\n\n**Q1.** [R2] T>1.2 是否能 recover diversity 改善 selection？Appendix 温度分析仅到 T=1.2。\n**Q2.** [R2] 本文 failure mode 与 Chen et al. (2024) \"Two Failures\" 识别的 hypothetical/compositional consistency failure 的关系？\n**Q3.** [R2] Hidden-state probe AUROC 0.63-0.88 但 selection gain 有限——bottleneck 在 quality estimation 还是 aggregation？\n**Q4.** [R2] 是否考虑过 entity-level filtering（high-consistency select, low-consistency abstain）作为中间方案？\n\n---\n\n## Missing References\n\n**优先补引（在 .bib 中但未引用）**:\n1. Chen et al. (2024) \"Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs\" (TMLR)\n2. Chen et al. (2024) \"Universal Self-Consistency for Large Language Model Generation\" (ICML Workshop)\n3. Aggarwal et al. (2023) \"Let's Sample Step by Step: Adaptive-Consistency\" (EMNLP)\n4. Thirukovalluru et al. (2024) \"Atomic Self-Consistency for Better Long Form Generations\" (EMNLP)\n5. Farquhar et al. (2024) \"Detecting Hallucinations in LLMs Using Semantic Entropy\" (Nature)\n6. Kuleshov & Liang (2015) \"Calibrated Structured Prediction\" (NeurIPS) — 在 bib 中未引用\n\n**建议补引（可能不在 .bib 中）**:\n7. PASC (2025) \"Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP Pipelines\"\n8. \"Existing LLMs Are Not Self-Consistent For Simple Tasks\" (2025)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: pending（已于 2026-05-21T04:34 发送请求，尚未返回）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: agent 超时（300s timeout），无实际 findings。\n用户可选择重新触发视觉审查。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3 | 3 | 3 |\n| Reproducibility | 4 | 4 | 4 |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4 | 4 | 4 |\n\n**评价**: 实验质量出色，diagnostic cascade 有工具价值，负面结果对 practitioner 有直接 actionable 意义。但四个 Must-Fix 问题（因果声称、Related Work 缺口、θ_crit 呈现、seed 不对称）限制了当前版本的接收可能性。核心 insight（degeneracy 导致 SC 失效）novelty 有限——与 Yun et al. (2025) diversity collapse 发现存在重叠，增量贡献主要在于量化 diversity collapse 对 selection 的功能性影响。\n\n**修改后预期**: 如果 4 个 Must-Fix 全部解决（因果语言软化、§8 扩充、θ_crit 标注、seed 补充），论文可达 **3.0-3.5**（Findings 至 Borderline Conference）。是否能冲击 Main Conference 取决于 novelty argument 的改善——需要更清晰地回答 \"beyond Yun et al., what is new?\"。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Why\" framing 需全面软化为描述性语言\n- Scope claim 需限定为 NER 而非 structured generation\n\n### §2 Diagnostic Framework\n- per-sample signal 定义不应完全 defer 到 Appendix\n\n### §3 Why Self-Verification Fails → 建议改为 \"Where/How\"\n- Hidden-state probe AUROC 0.63-0.88 vs selection gain gap 可增加一句解释\n\n### §4 Why Single-Signal Selection Fails → 建议改为 \"Where/How\"\n- \"degeneracy alone does not predict LP direction\" (§7.3) 与本节因果叙事的张力需要显式 reconcile\n\n### §5 Adaptive Methods / Escape Routes\n- Cost-benefit 分析缺失\n- Cross-model SC 仅 1 数据集 1 对模型，需扩展或缩减\n\n### §6 Theory\n- §6.3 θ_crit 必须标注为 data-dependent；增加敏感性分析\n- Degeneracy decomposition 定位为 diagnostic tool 而非 tight bound\n\n### §7 Experiments\n- Seed 不对称需要解释和缓解（至少 Few-NERD 3-seed）\n- Holm-Bonferroni k 的 family 定义需透明化\n\n### §8 Related Work\n- 从 ~0.5 页扩充至 0.75-1 页\n- 必须覆盖：SC failure modes、fine-grained SC 变体、sample-based 不确定性、conformal prediction、Yun et al. 差异化\n\n### §9 Discussion\n- 增加 cost-benefit 分析\n- 增加 closed-source API 模型的 degeneracy 讨论\n\n### Limitations\n- 增加 closed-source API degeneracy profile 差异的讨论\n\n### References\n- 清理 36 orphan bib entries\n- 引用并讨论 5 篇在 bib 中但未引用的高度相关论文",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 2848 · 2026-05-21T04:53:37.223293+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4976
}
```

</details>

---


### Assistant

_source line 2849 · 2026-05-21T04:53:46.004895+00:00_

审稿报告已投递至 Research Director。

---

**Round 27 审稿完成汇总**：

- **Overall Score**: 3.5 (Borderline Conference)
- **Reviewer**: R1 (3.5) + R2 (3.5)，1 轮收敛
- **4 个 Must-Fix**:
  1. Cascade 因果声称与相关性证据不匹配（§3/§4 "Why" 需改为描述性）
  2. Related Work 严重不足（§8 仅 0.5 页，5 篇关键论文在 bib 中未引用）
  3. θ_crit=0.70 半经验推导但呈现为理论结果
  4. 种子数不对称（SciERC 3-seed vs 其他 1-seed）
- **6 个 Should-Fix**: 标题 scope 过宽、escape routes 缺 cost-benefit、Yun et al. 差异化不清、缺 MBR baseline、36 orphan bib、seed 统计影响
- **外部审稿**: pending（未返回）
- **视觉审查**: agent 超时，无 findings
- **Issue tracker**: 已更新至 Round 27

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 217

## Round 217

2 recorded events


### User

_source line 2850 · 2026-05-21T04:53:47.293190+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

总结：对 R1 的 7 条意见中，我在 6 条上给出 [AGREE]（N1 θ_crit 半经验性、N2 种子不对称、N3 因果语言、W1 边际效果、W2 scope 过宽、W4 缺 MBR baseline），仅对 W3（LODO transfer 分析）给出 [REBUT]——认为论文的 claim 是 "transfer 失败" 而非 "能做好 transfer"，要求识别 transfer-critical 特征属于超出 claim 范围的额外实验要求。两位 reviewer 的核心共识集中在因果语言修正、scope 缩窄和 Related Work 补充上。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。

总结：在 R2 的 2 个 Must-Fix、4 个 Should-Fix、6 个 Minor、4 个 Questions 中，我 **AGREE 14 条，REBUT 3 条**（W4 部分反驳、M3 反驳、Q3 反驳）。两位 Reviewer 在因果声称过强、scope 过宽、Related Work 不足、效果量边际这四个核心问题上形成共识。总体评分维持 3.5 Borderline Conference。

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

_source line 2851 · 2026-05-21T04:53:57.517341+00:00_

审稿报告已于上一轮提交完毕（Overall 3.5 Borderline Conference），issue tracker 已同步更新。本轮圆桌审稿流程全部完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 218

## Round 218

80 recorded events


### User

_source line 2852 · 2026-05-21T11:16:59.075969+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (Long Paper)
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

_source line 2853 · 2026-05-21T11:17:10.825322+00:00_

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

_source line 2854 · 2026-05-21T11:17:10.876461+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2855 · 2026-05-21T11:17:16.674722+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2856 · 2026-05-21T11:17:16.725327+00:00_



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

_source line 2857 · 2026-05-21T11:17:19.541481+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
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
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2858 · 2026-05-21T11:17:19.592010+00:00_



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

_source line 2859 · 2026-05-21T11:17:25.268289+00:00_

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

_source line 2860 · 2026-05-21T11:17:26.625429+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (278 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_14b_inference_conll_v2 | 14B CoNLL rerun: Qwen2.5-14B fine-tuned model (qwen25-14b-fewnerd-merged-final) on CoNLL NER inference N=8 T=1.0. Previous run (exp_14b_inference_conll) crashed at 55% with EngineDeadError on 5090-b. Tests whether 14B scale preserves correlation-selection gap pattern on CoNLL. | — | — | — |\n| exp_fewnerd_mf4v2_s123 | — | — | — | — |\n| exp_fewnerd_mf4v2_s42 | — | — | — | — |\n\n## 待处理\n- exp_fewnerd_mf4_s456: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=456 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.（排队等待 GPU）\n- exp_fewnerd_mf4_s123: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=123 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.（排队等待 GPU）\n- exp_fewnerd_mf4_s42: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=42 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statisti
…[truncated 1744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool call

_source line 2861 · 2026-05-21T11:17:26.625874+00:00_

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

_source line 2862 · 2026-05-21T11:17:27.179750+00:00_

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
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{The Capability Ceiling of Self-Consistency:\\ How Entity-Level Self-Verification Fails in Structured Generation}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/diagnostic}
38	\input{sections/mechanistic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/background}
44	\input{sections/discussion}
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\section*{Ethics Statement}
51	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
52	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
53	No new human data was collected or annotated for this study.
54	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
55	Code and data will be released upon acceptance at [anonymized URL].
56	
57	\section*{Responsible NLP Research Checklist}
58	\input
…[truncated 183 chars]

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

_source line 2863 · 2026-05-21T11:17:28.187434+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 2864 · 2026-05-21T11:17:28.288272+00:00_

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

_source line 2865 · 2026-05-21T11:17:38.072939+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 papers with information about ARR:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using
…[truncated 1031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 9885
}
```

</details>

---


### Tool result

_source line 2866 · 2026-05-21T11:17:38.073327+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 9785
}
```

</details>

---


### Tool call

_source line 2867 · 2026-05-21T11:17:42.504496+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline page limit format requirements long paper"
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
    "query": "EMNLP 2026 submission deadline page limit format requirements long paper"
  }
}
```

</details>

---


### Tool call

_source line 2868 · 2026-05-21T11:17:43.408479+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
  "description": "List paper sections directory"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
    "description": "List paper sections directory"
  }
}
```

</details>

---


### Tool result

_source line 2869 · 2026-05-21T11:17:44.353568+00:00_

abstract.tex
adaptive.tex
appendix.tex
background.tex
checklist.tex
conclusion.tex
diagnostic.tex
discussion.tex
experiments.tex
experiments_main.tex
introduction.tex
limitations.tex
mechanistic.tex
method.tex
related_work.tex
single_signal.tex
theoretical.tex
theory.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 945
}
```

</details>

---


### Tool call

_source line 2870 · 2026-05-21T11:17:44.829214+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review reports and issues"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review reports and issues"
  }
}
```

</details>

---


### Tool result

_source line 2871 · 2026-05-21T11:17:45.281248+00:00_

data_integrity_audit_v2.md
round_0.md
round_1.md
round_10.md
round_11.md
round_12.md
round_13.md
round_14.md
round_15.md
round_16.md
round_17.md
round_18.md
round_19.md
round_2.md
round_20.md
round_21.md
round_22.md
round_23.md
round_24.md
round_25.md
round_26.md
round_3.md
round_4.md
round_5.md
round_6.md
round_7.md
round_7_consistency.md
round_9.md
---
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2872 · 2026-05-21T11:17:45.733320+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if PDF exists"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2873 · 2026-05-21T11:17:46.259057+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 525
}
```

</details>

---


### Tool call

_source line 2874 · 2026-05-21T11:17:46.359711+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "report.md",
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
    "file": "report.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2875 · 2026-05-21T11:17:48.216273+00:00_

Web search results for query: "EMNLP 2026 submission deadline page limit format requirements long paper"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here are the key submission details for EMNLP 2026:

## Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Page Limit for Long Papers

Long papers have an 8-
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5711
}
```

</details>

---


### Tool result

_source line 2876 · 2026-05-21T11:17:48.216858+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_14b_inference_conll_v2 | 14B CoNLL rerun: Qwen2.5-14B fine-tuned model (qwen25-14b-fewnerd-merged-final) on CoNLL NER inference N=8 T=1.0. Previous run (exp_14b_inference_conll) crashed at 55% with EngineDeadError on 5090-b. Tests whether 14B scale preserves correlation-selection gap pattern on CoNLL. | — | — | — |\\n| exp_fewnerd_mf4v2_s123 | — | — | — | — |\\n| exp_fewnerd_mf4v2_s42 | — | — | — | — |\\n\\n## 待处理\\n- exp_fewnerd_mf4_s456: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=456 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.（排队等待 GPU）\\n- exp_fewnerd_mf4_s123: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=123 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.（排队等待 GPU）\\n- exp_fewnerd_mf4_s42: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=42 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.（排队等待 GPU）\\n- eval_scd_fewnerd_fallback（准备中）\\n- exp_a1_spider_sql_sc: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.（准备中）\\n- exp_b2_v4_inverse_frequency: Inverse-frequency weighting of entity features (agreement_count, vc, sj normal
…[truncated 1334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 2877 · 2026-05-21T11:17:55.461713+00:00_

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

_source line 2878 · 2026-05-21T11:17:55.462181+00:00_

1	\begin{abstract}
2	Test-time compute scaling through repeated sampling yields large gains on discrete-answer reasoning and code generation, yet for structured information extraction (IE), where outputs are entity sets with partial overlap, a persistent gap separates quality estimation from sample selection.
3	We ask whether entity-level agreement signals can bridge this gap.
4	Across seven methods spanning self-judgment, self-refinement, latent consistency, heterogeneous verification, adaptive budgeting, distillation, and supervised classification, we find that no entity-level agreement signal reliably improves selection for named entity recognition (NER), relation extraction (RE), or Text-to-SQL.
5	Quality estimation signals correlate with oracle F1 ($\rho$ up to 0.45, AUROC up to 0.82) yet no signal selects better than greedy decoding.
6	The failure is systematic: a four-stage diagnostic cascade (quality estimation $\to$ degeneracy $\to$ agreement fidelity $\to$ log-probability compression) localizes where and why selection breaks down, with cross-task validation on SQL parsing (87.2\% output degeneracy).
7	A hidden-state linear probe achieves entity-level discrimination (area under the ROC curve [AUROC] $0.63$\textendash$0.88$, dataset-dependent) from a single forward pass, consistently exceeding prompt-based self-evaluation (AUROC 0.51) but matching multi-sample agreement ($0.87$) only on the simplest task.
8	These negative results delineate where self-consistency (SC) does succeed for IE: through paths that bypass entity-level agreement.
9	Log-probability selection improves F1 by $+1.39$\,pp on Few-NERD (Holm-adjusted $p{=}0.019$, selection family $k{=}19$), entity-level construction via weighted voting gains $+1.02$\textendash$1.40$\,pp, and cross-model ensembles add $+0.42$\,pp on Few-NERD.
10	Each exploits sequence-level or cross-model signals rather than entity-level self-verification.
11	A degeneracy decomposition confirms SC gain vanishes once output de
…[truncated 110 chars]

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

_source line 2879 · 2026-05-21T11:17:55.512707+00:00_

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

_source line 2880 · 2026-05-21T11:17:55.615392+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling complements model scaling \cite{snell2025scaling}: repeated sampling with majority voting \cite{wang2023selfconsistency}, best-of-$N$ with learned verifiers \cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \cite{muennighoff2025s1} produce large gains on reasoning and code generation.
4	These successes share a structural prerequisite: the output space admits either exact equivalence classes (multiple-choice, numeric answers) or execution-based verification (code).
5	Named entity recognition (NER) breaks both assumptions.
6	The output is a set of typed entities; two samples from the same input routinely extract overlapping but non-identical sets, and no external oracle can adjudicate correctness at test time.
7	Without equivalence classes, majority voting reduces to heuristic frequency counting; without a verifier, best-of-$N$ requires a reliable proxy signal.
8	This structural mismatch raises a concrete question: can self-consistency signals that estimate quality well for reasoning tasks also \textit{select} better outputs or \textit{construct} better entity sets for structured generation?
9	We investigate this question for NER and validate the core findings on SQL parsing, treating NER as a representative instance of the broader set-valued generation problem.
10	
11	The question has practical stakes beyond information extraction.
12	Hallucination detection methods such as SelfCheckGPT \cite{manakul2023selfcheckgpt} and FActScore \cite{min2023factscore} rely on cross-sample consistency to verify individual claims: if a model's outputs agree, the shared content is presumed factual.
13	This reasoning assumes entity-level self-verification works, that a model can reliably distinguish correct extractions from incorrect ones through self-judgment or re-prompting.
14	We show this assumption fails.
15	Three independent probes (entity self-judgment, multi-round re-prompt
…[truncated 5640 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2881 · 2026-05-21T11:17:55.615863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 2882 · 2026-05-21T11:17:55.867512+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
8	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
9	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
10	
11	\subsection{Confidence Signals}\label{sec:signals}
12	
13	Entity matching uses exact span and type match.
14	We evaluate four \textit{consistency signals}---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal}, per-sample signal.
15	
16	\paragraph{Log-probability (per-sample).}
17	$c_{\text{lp}}(y_i) = |y_i|^{-1} \sum_{j} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)$.
18	
19	\paragraph{Soft Jaccard (structural, instance-level).}
20	For samples $y_i, y_j$, we group by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU):
21	\begin{equation}\label{eq:sj}
22	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
23	\end{equation}
24	Instance-level QE averages over all pairs: $c_{\text{sj}}(x) = \binom{N}{2}^{-1} \sum_{i<j} \text{SJ}(y_i, y_
…[truncated 1482 chars]

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

_source line 2883 · 2026-05-21T11:17:55.968361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
  }
}
```

</details>

---


### Tool result

_source line 2884 · 2026-05-21T11:17:55.968726+00:00_

1	\section{How Self-Verification Fails}\label{sec:mechanistic}
2	
3	The diagnostic cascade (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
4	We evaluate self-verification and diagnostic probes on Qwen2.5-7B (a separate model family from the primary Qwen3-8B) fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Appendix~\ref{app:self_verification}).
5	
6	\paragraph{Entity Self-Judgment (ESJ).}
7	For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
8	Entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.
9	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$).
10	
11	\paragraph{Multi-Round Self-Consistency (MRSC).}
12	Re-prompting on disputed entities (agreement ${<}0.6$) with focused verification yields P(yes) separation of $0.0006$ between gold and non-gold entities ($0.5003$ vs.\ $0.4997$).
13	MRSC best F1 ($0.763$) falls below greedy.
14	
15	\paragraph{Latent Self-Consistency (LSC).}
16	Mean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.
17	Centroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms majority vote ($0.792$) but does not close the oracle gap ($0.882$).
18	
19	\paragraph{Hidden-state probe.}
20	A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
21	All three exceed ESJ ($0.51$); only CoNLL approaches frequency agreement ($0.868$).
22	Cross-dataset transfer is weak: leave-one-dataset-out AUROC drops to $0.559$ (Few-NERD${\to}$C
…[truncated 875 chars]

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

_source line 2885 · 2026-05-21T11:17:56.323291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 2886 · 2026-05-21T11:17:56.774888+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK           & $0.646 \pm 0.001$ & .79 \\
24	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
25	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
26	\midrule
27	Random       & $0.610 \pm 0.003$ & --- \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32
…[truncated 2007 chars]

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

_source line 2887 · 2026-05-21T11:17:56.775442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 2888 · 2026-05-21T11:17:56.826351+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield an unconditional positive result.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond the seven verification methods in \S\ref{sec:mechanistic}--\S\ref{sec:adaptive}). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & \ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & \ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & \ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally distinct models can partially bypass within-model degeneracy.
33	Combining 4 samples each from Qwen3-8B and
…[truncated 764 chars]

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

_source line 2889 · 2026-05-21T11:18:02.045454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 2890 · 2026-05-21T11:18:02.496849+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Following the MBR framework (Appendix~\ref{app:mbr_proof}), entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers the majority-vote threshold $\hat{p}(e) > \tfrac{1}{2}$ used throughout (Proposition~\ref{prop:construction_mbr}; empirical validation: Table~\ref{tab:entity_construction}).
6	Thus majority vote is MBR decoding under set-overlap utility.
7	Signal-derived weights $w_i$ yield quality-weighted MBR (LP-weighted construction): $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$.
8	Weighted MBR improves when $w_i$ correlates with $u(y_i, y^*)$ within instances; when this correlation is weak (LP on SciERC: $\rho{\approx}0.2$; few-shot: \S\ref{sec:scaling}), weighting degrades (\S\ref{sec:prescriptive}).
9	
10	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
11	
12	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; empirical fit in Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, while SciERC converges more slowly ($c{\approx}0.35$).
13	The ceiling grows, but confidence-based aggregation recovers ${<}1$\,pp---a persistent aggregation gap.
14	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{10.1\% of GPT-5.5 samples produced unparseable output; these are excluded from all metrics. See Appendix~\ref{app:frontier_sc}.}
15	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen
…[truncated 2081 chars]

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

_source line 2891 · 2026-05-21T11:18:02.497227+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2892 · 2026-05-21T11:18:02.948608+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N{=}16$ for scaling (Appendix~\ref{app:n_scaling}).
15	
16	%% ============================================================
17	\subsection{Quality Estimation Results}\label{sec:qe_results}
18	
19	\begin{table*}[t]
20	\centering
21	\small
22	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
23	\label{tab:quality_estimation}
24	\begin{tabular}{ll cc cc cc}
25	\toprule
26	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
27	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}

…[truncated 6871 chars]

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

_source line 2893 · 2026-05-21T11:18:02.949113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 2894 · 2026-05-21T11:18:04.052102+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, adaptive allocation \cite{aggarwal2023adaptive}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} all target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes and fine-grained variants.}
8	\citet{chen2023twofailures} identify SC failures in reasoning (hypothetical, compositional) where consistent outputs are systematically wrong; our correlation-selection gap is a distinct structured-generation failure where signals \textit{correlate} with quality yet fail to \textit{select}.
9	\citet{chen2024usc} extend SC to free-form tasks via universal matching; our diagnostic framework shows such extensions face limits under constrained decoding (\S\ref{sec:selection_gap}). \citet{thirukovalluru2024atomic} decompose claims into atomic units; our entity-level decomposition reveals that sub-output agreement does not translate to selection gain.
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{yao2026consistency} show consistency correlates with NER/RE accuracy; we diagnose degeneracy and LP compression as mechanisms that prevent this correlation from yielding selection gains.
13	\citet{xie2023zeroshot} propose entity voting for zero-shot NER; our approach aggregates stochastic samples from a fine-tuned model, building on generative IE \cite{zhou2024uniner, sainz2024gollie} and constrained decoding \cite{willard2023guided, dong2024xgrammar}.
14	
15	\paragraph{Uncertainty estimation and MBR.}
16	Our selection instantiates MBR decoding \cite{eikema2022sampling}; \citet{eikema2025structured} find 
…[truncated 1312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1102
}
```

</details>

---


### Tool call

_source line 2895 · 2026-05-21T11:18:04.253003+00:00_

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

_source line 2896 · 2026-05-21T11:18:04.253370+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	NER exhibits oracle scaling ($c{\approx}0.5$; \S\ref{sec:scaling}), but degeneracy (17.8--67.9\%) and LP-quality alignment ($\rho$ 0.043--0.667) constrain aggregation; temperature disentangles these at $T{=}1.2$ (Table~\ref{tab:t_degeneracy}).
4	
5	\paragraph{Degeneracy governs the selection gap across model families.}
6	Across four frontier models on Few-NERD, degeneracy and the selection gap (oracle${-}$MV) are negatively correlated (5.5--74\% degen $\to$ 0.290--0.032 gap; Table~\ref{tab:frontier_sc_cross}), confirming the degeneracy bound (\S\ref{sec:theory}) is structural, not model-specific.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms at zero marginal cost (reusing the $N$ samples already drawn for QE), with gains positive when degeneracy ${<}22$\% and absent when ${>}31$\% ($p{<}0.01$; Appendix~\ref{app:epoch_confound}); alternative strategies (DALS, DGS, supervised mixtures) fail to beat greedy (Appendix~\ref{app:dals}, \ref{app:supervised_combination}, \ref{app:when_selection_works}).
10	A cost-benefit analysis (Table~\ref{tab:cost_benefit}) confirms construction as the only consistently positive strategy.
11	LP compression (median 0.041 nats) connects to calibration challenges \cite{kadavath2022language, xiong2024verbalized}; per-sample alternatives \cite{kang2025selfcertainty, kadavath2022language} remain untested.
12	

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

_source line 2897 · 2026-05-21T11:18:04.454122+00:00_

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

_source line 2898 · 2026-05-21T11:18:04.605059+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	NER exhibits oracle scaling ($c{\approx}0.5$) but aggregation fails above $\theta_{\text{crit}}{=}0.70$; entity construction and LP selection ($+0.4$\textendash$1.4$\,pp) bypass the introspection boundary (AUROC $0.63$\textendash$0.88$ vs.\ ESJ $0.51$) rather than resolve it.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2899 · 2026-05-21T11:18:04.655654+00:00_

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

_source line 2900 · 2026-05-21T11:18:04.706299+00:00_

1	Scope: structured IE (NER primary, RE and SQL exploratory), English only, open-weight (Qwen and LLaMA) and closed-source (GPT-5.5) families, fine-tuned (4B--14B) and zero-shot (72B, GPT-5.5) regimes, sample budget $N{\leq}32$.
2	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
3	All experiments use English-language datasets; cross-lingual generalization remains untested.
4	Cross-model consistency results (\S\ref{sec:cross_model}) are limited to one dataset (Few-NERD) and one model pair (Qwen3-8B + LLaMA-3.1-8B).
5	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
6	We cover 4B\textendash 14B fine-tuned, 72B zero-shot, and GPT-5.5 zero-shot; the gap persists across all but behavior with 72B fine-tuning is untested.
7	The 72B zero-shot comparison simultaneously varies model family (Qwen3$\to$Qwen2.5), training regime (fine-tuned$\to$zero-shot), and quantization (FP16$\to$AWQ 4-bit); these factors cannot be fully disentangled.
8	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
9	
10	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
11	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
12	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
13	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach
…[truncated 2722 chars]

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

_source line 2901 · 2026-05-21T11:18:11.878525+00:00_

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


### Tool call

_source line 2902 · 2026-05-21T11:18:12.430877+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 2903 · 2026-05-21T11:18:12.882425+00:00_

File content (60760 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool result

_source line 2904 · 2026-05-21T11:18:12.882834+00:00_

1	% Responsible NLP Research Checklist
2	% Following the ACL Rolling Review guidelines:
3	% https://aclrollingreview.org/responsibleNLPresearch/
4	
5	\subsection*{A\hspace{0.5em} For Every Submission}
6	
7	\begin{enumerate}
8	\item[A1.] \textbf{Did you discuss the limitations of your work?}\\
9	Yes. See the Limitations section after the Conclusion.
10	
11	\item[A2.] \textbf{Did you discuss any potential risks of your work?}\\
12	Yes. See the Ethics Statement. This work analyzes existing confidence signals for NER and identifies when they fail; the findings reduce risk of deploying unreliable confidence-based selection in production systems. No dual-use concerns.
13	
14	\item[A3.] \textbf{Do the abstract and introduction summarize the paper's main claims?}\\
15	Yes. The Abstract and Section~\ref{sec:introduction} (3 enumerated contributions) summarize all main claims with supporting evidence pointers.
16	\end{enumerate}
17	
18	\subsection*{B\hspace{0.5em} Did you use or create scientific artifacts?}
19	
20	Yes. We use existing datasets and pre-trained models.
21	
22	\begin{enumerate}
23	\item[B1.] \textbf{Did you cite the creators of artifacts you used?}\\
24	Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
25	
26	\item[B2.] \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\\
27	Partially. The Ethics Statement notes that CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their r
…[truncated 4168 chars]

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

_source line 2905 · 2026-05-21T11:18:13.386307+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null | head -100",
  "description": "Read project config for external review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null | head -100",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2906 · 2026-05-21T11:18:13.738152+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2907 · 2026-05-21T11:18:13.738574+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2908 · 2026-05-21T11:18:13.789206+00:00_

1	issues:
2	  # ===== 历史 resolved issues (保留) =====
3	  - id: "R1-W1"
4	    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
5	    category: experiment
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 19
10	    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
11	    resolution_round: 19
12	
13	  - id: "R1-W2"
14	    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
15	    category: framing
16	    severity: critical
17	    status: resolved
18	    first_raised_round: 1
19	    last_seen_round: 21
20	    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
21	    resolution_round: 21
22	
23	  - id: "R2-N1-old"
24	    summary: "Contribution 1 'methodological premise' 是定义推论"
25	    category: framing
26	    severity: critical
27	    status: resolved
28	    first_raised_round: 1
29	    last_seen_round: 19
30	    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
31	    resolution_round: 19
32	
33	  - id: "R2-N2-old"
34	    summary: "与 MBR 文献差异化定位不够锐利"
35	    category: framing
36	    severity: warning
37	    status: resolved
38	    first_raised_round: 1
39	    last_seen_round: 19
40	    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
41	    resolution_round: 19
42	
43	  - id: "R2-N4-old"
44	    summary: "模型规模 3B-8B，70B+ 未知"
45	    category: experiment
46	    severity: info
47	    status: resolved
48	    first_raised_round: 1
49	    last_seen_round: 19
50	    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
51	    resolution_round: 19
52	
53	  - id: "R1-W3-old"
54	    summary: "2-seed 统计效力不足"
55	    category: experiment
56	    severity: warning
57	    status: resolved
58	    first_raised_round: 1
59	    last_seen_round: 19
60	    resolution: "Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。"
61	    resolution_round: 19
62	
63	  - id: "R1-W4-old
…[truncated 1126 chars]

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

_source line 2909 · 2026-05-21T11:18:17.770640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "200"
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
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2910 · 2026-05-21T11:18:18.874304+00:00_

100	    resolution: "Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。"
101	    resolution_round: 19
102	
103	  - id: "R2-W1-old"
104	    summary: "Abstract 数字过载"
105	    category: writing
106	    severity: warning
107	    status: resolved
108	    first_raised_round: 1
109	    last_seen_round: 19
110	    resolution: "Reviewer PASS: Abstract 含 3 个数字 (≤3)。"
111	    resolution_round: 19
112	
113	  - id: "R2-W2-old"
114	    summary: "Actionable contribution 偏薄"
115	    category: framing
116	    severity: warning
117	    status: resolved
118	    first_raised_round: 1
119	    last_seen_round: 21
120	    resolution: "Conclusion 新增 practitioner guidance。"
121	    resolution_round: 21
122	
123	  - id: "R2-W3-old"
124	    summary: "Discussion 过于碎片化"
125	    category: writing
126	    severity: info
127	    status: resolved
128	    first_raised_round: 1
129	    last_seen_round: 19
130	    resolution: "5 段合并完成。"
131	    resolution_round: 19
132	
133	  - id: "R2-W5-old"
134	    summary: "核心数字跨 section 重复"
135	    category: writing
136	    severity: info
137	    status: resolved
138	    first_raised_round: 1
139	    last_seen_round: 19
140	    resolution: "属正常范围。"
141	    resolution_round: 19
142	
143	  - id: "R2-W4-baseline"
144	    summary: "缺少 baseline signals"
145	    category: experiment
146	    severity: warning
147	    status: resolved
148	    first_raised_round: 1
149	    last_seen_round: 19
150	    resolution: "Round 20 检查 PASS。"
151	    resolution_round: 19
152	
153	  - id: "R2-W4-re"
154	    summary: "RE extension preliminary 但引用频繁"
155	    category: framing
156	    severity: info
157	    status: resolved
158	    first_raised_round: 1
159	    last_seen_round: 19
160	    resolution: "Round 20 检查 PASS。"
161	    resolution_round: 19
162	
163	  - id: "R1-MR1"
164	    summary: "缺失引用: Geifman & El-Yaniv 2017, XGrammar 等"
165	    category: format
166	    severity: warning
167	    status: resolved
168	    first_raised_round: 1
169	    last_seen_round: 20
170	    resolution: "Pape
…[truncated 3775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1103
}
```

</details>

---


### Tool call

_source line 2911 · 2026-05-21T11:18:19.175691+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null; echo \"===\"; find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ -name \"config*\" -type f 2>/dev/null",
  "description": "Find project config files"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null; echo \"===\"; find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ -name \"config*\" -type f 2>/dev/null",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2912 · 2026-05-21T11:18:19.627594+00:00_

===
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/datasets/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/datasets/config.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/util/config.h
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/config.h
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/python/config.h
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval
…[truncated 14057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2913 · 2026-05-21T11:18:19.828656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "0",
  "limit": "200"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2914 · 2026-05-21T11:18:19.879389+00:00_

0	\section{Notation}\label{app:notation}
1	
2	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{cl}
8	\toprule
9	Symbol & Meaning \\
10	\midrule
11	$\mathcal{M}$ & Language model \\
12	$x$ & Input instance \\
13	$y_i$ & $i$-th stochastic sample \\
14	$N$ & Number of samples \\
15	$T$ & Sampling temperature \\
16	$c(\cdot)$ & Confidence signal \\
17	SJ & Soft Jaccard similarity \\
18	FK & Fleiss' $\kappa$ \\
19	EM & Exact-match voting rate \\
20	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
21	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
22	\bottomrule
23	\end{tabular}
24	\caption{Notation used throughout the paper.}
25	\label{tab:notation}
26	\end{table}
27	
28	\section{Robustness Analysis}\label{app:robustness}
29	
30	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
31	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
32	
33	\begin{table}[t]
34	\centering
35	\small
36	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
37	\label{tab:robustness}
38	\begin{tabular}{llcc}
39	\toprule
40	& & NER $\rho$ & RE $\rho$ \\
41	\midrule
42	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
43	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
44	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
45	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
46	\quad FK & $T
…[truncated 13208 chars]

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

_source line 2915 · 2026-05-21T11:18:26.654586+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -20",
  "description": "Find project agent config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -20",
    "description": "Find project agent config files"
  }
}
```

</details>

---


### Tool result

_source line 2916 · 2026-05-21T11:18:27.056324+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2917 · 2026-05-21T11:18:27.307495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2918 · 2026-05-21T11:18:27.408353+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{min2023factscore,
4	  title = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},
5	  author = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},
6	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
7	  year = {2023},
8	  url = {https://aclanthology.org/2023.emnlp-main.741/},
9	}
10	
11	@article{holm1979simple,
12	  title = {A Simple Sequentially Rejective Multiple Test Procedure},
13	  author = {Holm, Sture},
14	  journal = {Scandinavian Journal of Statistics},
15	  volume = {6},
16	  number = {2},
17	  pages = {65--70},
18	  year = {1979},
19	}
20	
21	@inproceedings{xiong2024verbalized,
22	  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},
23	  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},
24	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},
25	  year = {2024},
26	  url = {https://arxiv.org/abs/2306.13063},
27	}
28	
29	@article{brown2024monkeys,
30	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
31	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
32	  journal = {arXiv preprint arXiv:2407.21787},
33	  year = {2024},
34	  url = {https://arxiv.org/abs/2407.21787}
35	}
36	
37	@inproceedings{chen2024usc,
38	  title = {Universal Self-Consistency for Large Language Model Generation},
39	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
40	  bo
…[truncated 586 chars]

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

_source line 2919 · 2026-05-21T11:18:31.620874+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ -maxdepth 3 -name \"*.yaml\" -not -path \"*/.venv/*\" -not -path \"*/node_modules/*\" -not -path \"*/artifacts/experiments/*\" 2>/dev/null | grep -v review_issues",
  "description": "Find project YAML configs"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ -maxdepth 3 -name \"*.yaml\" -not -path \"*/.venv/*\" -not -path \"*/node_modules/*\" -not -path \"*/artifacts/experiments/*\" 2>/dev/null | grep -v review_issues",
    "description": "Find project YAML configs"
  }
}
```

</details>

---


### Tool result

_source line 2920 · 2026-05-21T11:18:31.671488+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml

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

_source line 2921 · 2026-05-21T11:18:34.857291+00:00_

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

_source line 2922 · 2026-05-21T11:18:34.857629+00:00_

1	execution:
2	  account: root
3	  gpu_constraint:
4	    autodl-5090:
5	    - cuda:0
6	    - cuda:1
7	    - cuda:2
8	    - cuda:3
9	    autodl-5090-c:
10	    - cuda:0
11	    - cuda:1
12	    - cuda:2
13	    - cuda:3
14	  gpu_ids:
15	  - cuda:0
16	  - cuda:1
17	  - cuda:2
18	  - cuda:3
19	  project_path: /root/autodl-tmp/struct_self_consist_ie
20	  servers:
21	  - autodl-5090
22	  - autodl-5090-c
23	feishu:
24	  chat_id: oc_1b56445332d8ca2b4964b30f300f0e00
25	  operational_chat_id: oc_523053f5a039428dc15666668fa856b3
26	  review_mode: fresh
27	  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
28	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf
29	  review_round: 27
30	  review_supplementary_paths: ''
31	  submission_chat_id: oc_3897c2857f11615119e277e820eae311
32	project:
33	  created_at: '2026-05-14T04:20:56.331Z'
34	  description: When Does Test-Time Scaling Help Structured Prediction? Adaptive Structural
35	    Self-Consistency with Learned Aggregation
36	  name: struct_self_consist_ie
37	  phase: research
38	  source_idea_id: idea_010
39	venue: emnlp-2026
40	

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

_source line 2923 · 2026-05-21T11:18:34.958319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/emnlp-2026.yaml"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2924 · 2026-05-21T11:18:35.059241+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  - created_at: '2026-05-19T12:23:13Z'
12	    id: bd0516
13	    text: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for
14	      main text, with unlimited space for references. Mandatory limitations and optional
15	      ethical considerations do not count towards this page limit, provided they do
16	      not contain excessive additional content.
17	  writing:
18	  - created_at: '2026-05-21T06:49:14Z'
19	    id: 2468a8
20	    text: Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
21	

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

_source line 2925 · 2026-05-21T11:19:17.016144+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 2926 · 2026-05-21T11:19:35.916087+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18899
}
```

</details>

---


### Tool call

_source line 2927 · 2026-05-21T11:19:36.016944+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验充分性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Main Conference (Long Paper)\n- **审稿系统**: ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板，正文 8 页限制，参考文献不限；Limitations 必须（不计页数）；Ethics 可选（不计页数）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 诊断框架 (Diagnostic Cascade) 的方法论有效性\n- 四阶段级联 (QE → degeneracy → agreement fidelity → LP compression) 是否逻辑自洽？\n- 各阶段之间的因果/相关性声明是否有充分证据支持？\n- degeneracy decomposition 的理论推导 (bound) 是否正确、是否 tight？\n\n### 2. 统计方法与报告\n- 多重比较校正 (Holm-Bonferroni) 的使用是否正确？k 值设定是否合理？\n- 显著性声明 ($p$ 值、CI、MDE) 是否一致且保守？\n- 多 seed 实验设计是否足够？SciERC 单 seed 是否构成实质性问题？\n- Bootstrap 检验的技术细节是否完整？\n\n### 3. 实验覆盖面与充分性\n- 7 种 entity-level 方法的测试是否全面？各方法是否在足够多的 dataset × model 配置下测试？\n- 跨模型 (Qwen vs LLaMA)、跨规模 (4B/8B/14B/72B)、跨任务 (NER/RE/SQL) 的覆盖是否足够支持论文的通用性声明？\n- Few-NERD 3-epoch vs 其他 5-epoch 的 epoch confound 是否被充分控制？\n- GPT-5.5 和 72B 的零样本实验规模 (200 instances, 50 instances) 是否足够？\n\n### 4. 核心数值一致性\n- 跨表格引用的关键数字 (greedy F1, LP ρ, degeneracy%, Δpp) 是否一致？\n- Abstract/Introduction 中的数字是否与正文表格精确对应？\n\n### 5. 格式合规性\n- 正文是否在 8 页以内？\n- 匿名规则是否遵守？\n- Checklist 是否完整？\n\n请输出完整审稿报告，结构：Summary → Strengths → Weaknesses (逐条，区分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (用 EMNLP 2026 评分标准) → Confidence。"
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验充分性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Main Conference (Long Paper)\n- **审稿系统**: ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板，正文 8 页限制，参考文献不限；Limitations 必须（不计页数）；Ethics 可选（不计页数）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 诊断框架 (Diagnostic Cascade) 的方法论有效性\n- 四阶段级联 (QE → degeneracy → agreement fidelity → LP compression) 是否逻辑自洽？\n- 各阶段之间的因果/相关性声明是否有充分证据支持？\n- degeneracy decomposition 的理论推导 (bound) 是否正确、是否 tight？\n\n### 2. 统计方法与报告\n- 多重比较校正 (Holm-Bonferroni) 的使用是否正确？k 值设定是否合理？\n- 显著性声明 ($p$ 值、CI、MDE) 是否一致且保守？\n- 多 seed 实验设计是否足够？SciERC 单 seed 是否构成实质性问题？\n- Bootstrap 检验的技术细节是否完整？\n\n### 3. 实验覆盖面与充分性\n- 7 种 entity-level 方法的测试是否全面？各方法是否在足够多的 dataset × model 配置下测试？\n- 跨模型 (Qwen vs LLaMA)、跨规模 (4B/8B/14B/72B)、跨任务 (NER/RE/SQL) 的覆盖是否足够支持论文的通用性声明？\n- Few-NERD 3-epoch vs 其他 5-epoch 的 epoch confound 是否被充分控制？\n- GPT-5.5 和 72B 的零样本实验规模 (200 instances, 50 instances) 是否足够？\n\n### 4. 核心数值一致性\n- 跨表格引用的关键数字 (greedy F1, LP ρ, degeneracy%, Δpp) 是否一致？\n- Abstract/Introduction 中的数字是否与正文表格精确对应？\n\n### 5. 格式合规性\n- 正文是否在 8 页以内？\n- 匿名规则是否遵守？\n- Checklist 是否完整？\n\n请输出完整审稿报告，结构：Summary → Strengths → Weaknesses (逐条，区分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (用 EMNLP 2026 评分标准) → Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 2928 · 2026-05-21T11:19:55.584215+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19567
}
```

</details>

---


### Tool call

_source line 2929 · 2026-05-21T11:19:55.688456+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 论文完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Main Conference (Long Paper)\n- **审稿系统**: ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板，正文 8 页限制，参考文献不限；Limitations 必须（不计页数）；Ethics 可选（不计页数）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- \"Correlation-selection gap\" 这个概念是否真正新颖？与 MBR 文献 (Eikema & Aziz 2022, Eikema et al. 2025)、SC failure modes (Chen et al. 2023) 的差异是否足够大？\n- 负面结果 (7 种方法全部失败) 作为论文核心贡献，对 EMNLP 社区的价值和影响力如何？\n- Prescriptive results (+1.0~1.4pp) 是否太小以至于缺乏实践意义？\n- 与 Yun et al. 2025 (\"diversity collapse\") 和 Yao et al. 2026 的差异化是否清晰？\n\n### 2. Related Work 完整性\n- 是否遗漏了重要的相关工作？特别关注：\n  - Test-time compute scaling 方向的最新进展\n  - NER/IE 领域使用 SC 的其他工作\n  - Uncertainty quantification 和 calibration 的相关文献\n  - MBR decoding for structured prediction\n- 引用格式和完整性是否符合 ACL 标准？\n\n### 3. 论文结构与叙事\n- 章节安排是否合理？当前结构 (Intro → Diagnostic → Mechanistic → Single-Signal → Adaptive → Theory → Experiments → Related Work → Discussion → Conclusion) 是否清晰？\n- Related Work 放在 Experiments 之后是否影响可读性？\n- 论文作为 \"negative results + prescriptive escape routes\" 的叙事框架是否有效？\n- Abstract 的信息密度是否过高（数字过多）？\n\n### 4. 写作质量\n- 学术英语是否规范？是否有语法、拼写错误？\n- 术语使用是否一致？(e.g., \"degeneracy\", \"correlation-selection gap\" 等关键概念是否有清晰定义并一致使用？)\n- 表格/图表的可读性如何？Caption 是否自含？\n- Limitations 是否充分但不过长（EMNLP 规则：一小段，~3 个点）？\n- Conclusion 是否简洁有效？\n\n### 5. Scope 与 Generalizability 声明\n- 标题 \"Structured Generation\" 与实际范围 (主要是 NER，RE/SQL 为探索性) 是否匹配？\n- 对 \"capability ceiling\" 的声明是否过强？是否有足够 caveat？\n- Cross-task validation (SQL) 的深度是否足以支持泛化声明？\n\n请输出完整审稿报告，结构：Summary → Strengths → Weaknesses (逐条，区分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (用 EMNLP 2026 评分标准) → Confidence。"
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
    "text": "你是 Reviewer 2，负责**新颖性 + 论文完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Main Conference (Long Paper)\n- **审稿系统**: ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板，正文 8 页限制，参考文献不限；Limitations 必须（不计页数）；Ethics 可选（不计页数）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- \"Correlation-selection gap\" 这个概念是否真正新颖？与 MBR 文献 (Eikema & Aziz 2022, Eikema et al. 2025)、SC failure modes (Chen et al. 2023) 的差异是否足够大？\n- 负面结果 (7 种方法全部失败) 作为论文核心贡献，对 EMNLP 社区的价值和影响力如何？\n- Prescriptive results (+1.0~1.4pp) 是否太小以至于缺乏实践意义？\n- 与 Yun et al. 2025 (\"diversity collapse\") 和 Yao et al. 2026 的差异化是否清晰？\n\n### 2. Related Work 完整性\n- 是否遗漏了重要的相关工作？特别关注：\n  - Test-time compute scaling 方向的最新进展\n  - NER/IE 领域使用 SC 的其他工作\n  - Uncertainty quantification 和 calibration 的相关文献\n  - MBR decoding for structured prediction\n- 引用格式和完整性是否符合 ACL 标准？\n\n### 3. 论文结构与叙事\n- 章节安排是否合理？当前结构 (Intro → Diagnostic → Mechanistic → Single-Signal → Adaptive → Theory → Experiments → Related Work → Discussion → Conclusion) 是否清晰？\n- Related Work 放在 Experiments 之后是否影响可读性？\n- 论文作为 \"negative results + prescriptive escape routes\" 的叙事框架是否有效？\n- Abstract 的信息密度是否过高（数字过多）？\n\n### 4. 写作质量\n- 学术英语是否规范？是否有语法、拼写错误？\n- 术语使用是否一致？(e.g., \"degeneracy\", \"correlation-selection gap\" 等关键概念是否有清晰定义并一致使用？)\n- 表格/图表的可读性如何？Caption 是否自含？\n- Limitations 是否充分但不过长（EMNLP 规则：一小段，~3 个点）？\n- Conclusion 是否简洁有效？\n\n### 5. Scope 与 Generalizability 声明\n- 标题 \"Structured Generation\" 与实际范围 (主要是 NER，RE/SQL 为探索性) 是否匹配？\n- 对 \"capability ceiling\" 的声明是否过强？是否有足够 caveat？\n- Cross-task validation (SQL) 的深度是否足以支持泛化声明？\n\n请输出完整审稿报告，结构：Summary → Strengths → Weaknesses (逐条，区分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (用 EMNLP 2026 评分标准) → Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 2930 · 2026-05-21T11:19:57.304640+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1616
}
```

</details>

---


### Assistant

_source line 2931 · 2026-05-21T11:20:05.488849+00:00_

Round 1 已启动：

- **视觉审查 Agent**：已派发（fire-and-forget，不阻塞）
- **Reviewer 1**（方法严谨性 + 实验充分性）：已分配
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：已分配

等待两位 Reviewer 返回初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 219

## Round 219

2 recorded events


### User

_source line 2932 · 2026-05-21T11:27:54.798028+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性 + 论文完整性 + 写作质量

### 总体评分
**Overall**: 3.0 — Findings（可被 Findings 接收）
**一句话总结**: 扎实的负面结果实证研究，诊断框架设计精巧，但标题与实际实验范围不匹配、prescriptive gains 边际化且依赖数据集，加上主体结构混乱，限制了主会议接收的竞争力。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 诊断级联方法论完善，统计检验充分（bootstrap CI, Holm-Bonferroni），但 claim scope 超出证据支撑范围 |
| Excitement | 2.5/5 | 负面结果对社区有警示价值，但 set-valued output 的 SC 失败并非完全出人意料；prescriptive gains 太小 |
| Reproducibility | 4/5 | 公开数据集、承诺释放代码、训练/推理细节详尽 |
| Overall Assessment | 3.0/5 | Findings 水平 |

### Must-Fix 问题（3 个 critical）

**N1** [critical] 标题与实验范围严重不匹配
- 标题 "Structured Generation" 极其宽泛，但实际实验以 NER 为绝对主体（4 datasets × 2 model families）。RE 仅 1 个数据集探索性扩展（Appendix o），SQL 仅 post-hoc validation。ARR guidelines 要求 "evaluation samples must represent the populations discussed in conclusions"——当前标题构成 overclaiming。
- 建议：收窄为 "Named Entity Recognition" 或 "Structured Information Extraction"，或大幅扩充 RE/SQL 实验。

**N2** [critical] Prescriptive gains 边际化且依赖数据集
- LP-weighted entity construction +1.02–1.40pp 仅在 Few-NERD 上显著，SciERC/CoNLL 不一致。Cross-model ensemble 需 2N× cost 仅 +0.42pp。Table 61 显示唯一 unconditionally positive 的方法（SC+construction）最佳也仅 +1.4pp/8× cost。
- 论文将 prescriptive results 定位为第四项核心贡献，但增益接近噪声水平，严重削弱实用价值。
- 建议：降低 prescriptive results 宣传权重，重新定位为 analysis paper。

**N3** [critical] 主体结构混乱：诊断/方法/结果交织
- Sections 3–5 在介绍方法时嵌入 SciERC 初步结果，Section 7 又展开"完整实验"，大量重叠。读者难以分辨 preliminary diagnostic 和 main experiment。
- 建议：统一放结果到 Section 7，或明确标注 Sections 3–5 为 diagnostic pilot。

### Should-Fix 问题（5 个 warning）

**W1** "Capability ceiling" 措辞过于绝对——仅测试 3B–8B 开源模型，更大模型可能改变结论
**W2** 模型多样性不足——缺 70B+、闭源 API 模型、instruction-tuned vs base 对比
**W3** RE 分析的混合证据削弱泛化声明——RE 失败机制与 NER 不同（span error vs degeneracy），统一归因于 correlation-selection gap 过度简化
**W4** Abstract 信息密度过高——250 词内塞入 ρ≤0.45、AUROC≤0.82、87.2% degeneracy 等大量数字
**W5** Related Work 后置（Section 8）影响阅读——读者需提前理解 SC 在 reasoning 中为何有效才能理解在 IE 中的失败

### 小问题（6 个）
- M1: 2 个 orphan bib entries 未引用
- M2: Figure 2 caption "oracle gap" 未自含定义
- M3: "VotConsLogProb" 在 Table 3 突然出现未正式定义
- M4: Table 61 (cost-benefit) 被埋在 45 页附录中，应提到主文
- M5: "degeneracy" 首次使用缺括号解释
- M6: "Inverse Scaling" 标题与实际内容（scaling 变慢）不完全对应

### 主要优势
- S1: 4 阶段诊断级联是最有价值的贡献，从现象到机制定位精准
- S2: 9 大类方法 × 4 数据集 × 2 模型族覆盖面极广
- S3: MBR 等价性证明 + degeneracy bound + scaling law 提供理论支撑
- S4: Bootstrap CI + Holm-Bonferroni 统计严谨性远超同类论文
- S5: ~35 页附录可追溯性极高
- S6: Table 62 与先前工作差异化清晰

### Missing References
1. "Uncertainty Quantification and Confidence Calibration in LLMs: A Survey" (KDD 2025)
2. "A Simple but Effective Approach to Improve Structured LLM Output for IE" (Aronica et al., 2024)
3. "Test-time Scaling of LLMs: A Survey" (2025, arXiv:2511.14772)

### 引用验证结果
- 51 bib entries, 49 cited, 2 orphan, 0 missing
- 46/51 online verified, 2 not found (lightman2024verify, aggarwal2023adaptive — 均为真实论文但 OpenAlex 未索引), 3 minor mismatches (LaTeX encoding issues)
- 无虚假引用

### Confidence: 4/5

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

_source line 2933 · 2026-05-21T11:28:01.053562+00:00_

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


## Round 220

## Round 220

2 recorded events


### User

_source line 2934 · 2026-05-21T11:28:06.520749+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。三个 critical 问题：(1) "Structured Generation" 标题严重超出 NER-centric 实验范围；(2) prescriptive gains 仅 +1.0–1.4pp 且仅在 Few-NERD 上显著；(3) Sections 3–7 结构交织导致阅读困难。主要优势在于诊断框架的精巧设计和统计严谨性。引用验证通过，无虚假引用。

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

_source line 2935 · 2026-05-21T11:28:14.648220+00:00_

Reviewer 2 报告已收到（Overall 3.0 Findings）。等待 Reviewer 1 完成初审后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 221

## Round 221

6 recorded events


### User

_source line 2936 · 2026-05-21T11:31:45.564644+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：方法严谨性 + 实验充分性

**论文**: "The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Structured Generation"
**Venue**: EMNLP 2026 Main Conference (Long Paper, via ARR)

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 对 NER 领域 self-consistency 失败机制的诊断非常透彻，但泛化性声明（RE/SQL）严重超出证据支撑范围，且理论贡献（degeneracy bound）过于松散，正面贡献（entity construction ~1pp 增益）的实际影响有限。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | NER 实验方法论扎实（Holm-Bonferroni k=57, bootstrap CI, 3-seed），但因果语言与相关性证据不匹配，RE/SQL 泛化声明证据不足，degeneracy bound 极松（仅捕获 4.7–12.1% 的实际增益） |
| Excitement | 3/5 | 研究问题有价值（SC 为何在结构化生成中失败），诊断框架新颖，但正面贡献有限（entity construction 仅 +1–1.4pp），主要是 negative results |
| Reproducibility | 4/5 | 附录极其详尽（60+ 表格），训练配置、超参数、prompt 模板均给出，承诺开源代码和数据。SciERC 部分分析仅 seed=42 |
| Overall Assessment | 3.5/5 | Borderline Conference — 若收窄泛化声明至 NER 则为 solid Findings，当前 scope 与证据不匹配 |
| Confidence | 4/5 | 对统计方法、IE 任务设计和 SC 文献较为熟悉，仔细审读了全部 46 页 |

---

## Must-Fix 问题（影响接收决定）

### N1 [critical] 泛化性声明严重超出证据范围：标题说 "Structured Generation" 但证据几乎全是 NER

- **具体位置**: Title, Abstract ("NER, Text-to-SQL, or RE"), Section 9 (p.8), Section 10 (p.8)
- **问题**:
  - **RE 证据**：仅 SciERC 一个数据集，且 Appendix d (p.15) 承认 55.5% 的 RE 实例因 entity span errors 获得 zero F1。这意味着 RE 分析实际测量的是 NER 错误在 RE pipeline 中的传播，而非 RE 本身的 self-consistency 失败。Table 3 conditional set 中 LP 在 RE 上 ρ=−0.026，近乎无信号。Section 7.6 (p.7) 也承认 RE 的 LP 选择不转移。RE 被 Limitations (p.9) 标记为 "exploratory"，但标题和摘要未反映这一限定。
  - **SQL 证据**：仅一句话——"Cross-task validation on Spider SQL parsing (GPT-5.5, n=196) confirms the diagnostic cascade: degeneracy reaches 87.2%" (p.2)。无详细表格、无多模型对比、无统计检验、无 entity-level 信号分析。n=196 仅一个模型一个数据集，不足以支撑 "Text-to-SQL" 这一任务类别的泛化声明。
  - 论文 60+ 张表格中，RE 专属表格仅 3 张（Tables 28-29 in Appendix o, Table 3 partial），SQL 无任何表格。证据密度与 NER（~55 张表格）严重不对称。
- **为什么影响接收**: Reviewer 和 AC 会根据标题和摘要建立期望。当证据仅覆盖 NER 时，以 "Structured Generation" 为标题构成 overclaiming，这在 ARR 审稿中是常见的 soundness 扣分点。
- **建议修改方向**: (a) 将标题和摘要收窄为 NER-specific（如 "How Entity-Level Self-Verification Fails in Named Entity Recognition"），RE/SQL 作为 "preliminary observations" 在 Discussion 中简述；或 (b) 补充 RE 和 SQL 的完整实验（多数据集、多模型、完整信号分析），使其与 NER 的证据密度可比。方案 (a) 更务实。

### N2 [critical] 因果语言与相关性证据不匹配

- **具体位置**: Section 9 (p.8): "Degeneracy **governs** the selection gap across model families"; Abstract: "the failure **is** systematic: a four-stage diagnostic **cascade**"; Introduction (p.2): "our diagnostic framework **fills** this gap: four failure modes (degeneracy, low agreement, false agreement, LP compression) **explaining** where and why..."
- **问题**: Figure 1 caption 正确标注 "correlation sequence, not causal claims"，但论文主体在多处使用因果动词（"governs", "explaining", "fills"），暗示四阶段级联是因果机制而非相关模式。论文实际做的是：(1) 观察高 degeneracy 与小增益共现，(2) 观察 LP 压缩与选择失败共现。这是 correlational diagnosis，不是 causal mechanism。
  - 关键区分：Appendix ae (p.34) 的 prescriptive recommendations（如 "Step 1: Measure instance degeneracy... >30% indicates limited headroom"）隐含因果假设——即 degeneracy *导致*增益受限，而非仅与之共现。如果关系仅是相关的，则降低 degeneracy（如换 prompt、提高温度）不一定能提升增益。
  - 论文未提供干预实验（intervention）来验证因果方向。Table 7 的温度扫描 (p.14) 接近干预，但其结果恰恰显示温度对 ρ 影响不大（SJ ρ 从 T=0.7 的 0.360 到 T=1.0 的 0.364），表明操纵 degeneracy 的前因并不能线性改善信号质量。
- **为什么影响接收**: 因果推断是 soundness 的核心维度。如果四阶段级联仅是描述性的相关模式，则其诊断价值和处方价值均需降级。
- **建议修改方向**: (a) 在 Section 2.1 或 Figure 1 caption 附近增加一段明确的 scope statement，说明 cascade 是 "diagnostic correlation framework" 而非 causal model；(b) 将 Section 9 和 Abstract 中的因果动词统一替换为相关性语言（"is associated with", "co-occurs with", "predicts"）；(c) 在 Discussion 中明确讨论因果推断的局限。

### N3 [critical] Holm-Bonferroni k 值与 Table 13 不一致，影响核心统计声明的可复现性

- **具体位置**: Abstract (p.1): "Holm p_adj=0.010, selection family k=19"; Table 13 (p.37)
- **问题**: Abstract 声称 LP 选择增益的 Holm 校正使用 "selection family k=19"。但 Table 13 列出的 selection family（rows 1–21）共有 **21** 项测试，而非 19 项。差异为 2 项。论文未解释哪 2 项被排除或为何 k=19。
  - 这直接影响 p_adj 的计算：Holm-Bonferroni 校正中 k 值越大，p_adj 越保守。如果实际 k=21，则 p_adj=0.010 可能变为 p_adj≈0.011（仍显著），但如果 k 有误，可能影响边界情况的其他测试。
  - 更重要的是，这影响**可复现性**：读者无法从 Table 13 独立验证 Abstract 中的数字。
- **为什么影响接收**: 统计报告的精确性是 empirical paper 的基本要求。ARR checklist 明确要求 "report relevant statistics like... significance tests."
- **建议修改方向**: (a) 核实 k=19 还是 k=21，修正 Abstract 中的数字；(b) 如果有测试被排除，在 Appendix f 中说明排除理由；(c) 提供完整的 Holm correction computation trace（如补充表格显示每个测试的 raw p、rank、adjusted p）。

---

## Should-Fix 问题（影响评分但不一票否决）

### W1 [warning] Degeneracy bound (Table 30) 极松且单向，但被作为主要理论贡献呈现

- **具体位置**: Proposition 1 (Appendix p.1, p.25), Table 30 (p.40), Introduction contribution #4 (p.2)
- **问题**: Table 30 显示 bound $(1-D) \cdot G_{\text{nd}} \cdot \alpha$ 仅捕获实际增益的 4.7–12.1%（低 degeneracy 配置），且 bound ≥ 0 恒成立，无法预测负增益方向（CoN s123: actual Δ=−0.42, bound≈0）。这意味着：
  - Bound 作为上界极松（off by ~10×）
  - Bound 无法区分"无增益"和"负增益"
  - Bound 的实际预测能力有限——知道 D, G_nd, α 后，对实际 Δ 的预测区间极宽
  - Table 30 header 自己标注 "actual/weak bound"，但 Introduction (p.2) 和 Abstract 将其作为主要贡献之一呈现
- **建议**: (a) 在主文中明确讨论 bound 的 tightness（如 "captures ~10% of actual gain"），而非仅在 Table 30 header 中用 "weak" 一词带过；(b) 讨论 bound 松散的原因（entity-wise independence 假设？balanced set-overlap utility？）；(c) 考虑将 Proposition 1 的 MBR 等价性（较强的结论）与 degeneracy bound（较弱的推论）区分呈现。

### W2 [warning] SciERC RE 分析被 entity span error 严重混淆

- **具体位置**: Appendix d (p.15), Appendix o (p.24), Table 3 RE columns
- **问题**: Appendix d 明确指出 RE 的主要错误源是 entity span error（55.5% 的实例 F1=0），这意味着 RE 分析本质上在测量 NER-to-RE 的错误传播。在 entity span error 占主导的情况下，self-consistency 信号反映的是 NER 级别的不确定性而非 RE 级别的。
  - FEATURE-OF 关系 ρ≈0（p=0.001 反方向）vs HYPONYM-OF ρ=0.646，说明信号质量高度依赖关系类型
  - Limitations (p.9) 承认 RE 是 "exploratory"，但 Section 7.6 (p.7) 和 Table 3 中 RE 与 NER 并列呈现，未充分标注这一混淆
- **建议**: 在 Section 7.6 首段明确声明 RE 结果受 entity span error 混淆，建议读者谨慎解读；在 Table 3 的 RE 列添加脚注标注混淆因素。

### W3 [warning] k=57 全局 Holm 校正与中等样本量结合，统计功效不足

- **具体位置**: Table 13 (p.37), Table 55 (p.44), Section 7.2 (p.6)
- **问题**: Table 55 的 post-hoc power analysis 显示：在 n=23（RE 分析）时，仅 ρ≥0.3 的大效应量可被检测到（power=0.80）。结合 k=57 的全局 Holm 校正，大多数比较的统计功效不足。
  - 这意味着论文的核心结论——"no entity-level signal reliably improves selection"——可能反映的是 **insufficient power to detect moderate effects** 而非 **true null**。
  - 对 NER 数据集（n=529–37,648），功效较充足。但对 RE (n≈397) 和小配置，功效显著不足。
  - 论文承认了这一点（Table 55），但未在主文结论中充分 hedge。
- **建议**: 在 Section 9 或 Conclusion 中明确表述："our non-significant findings for RE and smaller configurations may reflect insufficient statistical power rather than true absence of signal utility"。报告 minimum detectable effect (MDE) 以帮助读者判断。

### W4 [warning] 7 种方法的分类边界模糊

- **具体位置**: Abstract (p.1): "seven methods spanning self-judgment, self-refinement, latent consistency, heterogeneous temperature sampling, adaptive budgeting, distillation, and supervised classification"
- **问题**: 这 7 种方法中，部分是**诊断探针**（ESJ, MRSC, LSC — 测试模型是否能 self-verify），部分是**选择/构造方法**（DALS, SCD — 试图利用信号改善输出）。Abstract 将两类混为一体（"we evaluated seven approaches"），但它们的功能和评价标准不同。
  - "Heterogeneous temperature sampling" 在 Table 2 中无对应行。它似乎对应 Table 7 的温度敏感性分析（一种实验条件变化，而非独立方法）。
  - Table 2 列出 9 个 method categories，与 Abstract 的 7 methods 不完全对齐。
- **建议**: 在 Section 1 或 Section 3 开头明确区分 "diagnostic probes" 和 "aggregation/selection methods"，并说明 Abstract 中 7 种方法的分类逻辑。

### W5 [warning] Entity construction 的正面增益虽一致但幅度有限

- **具体位置**: Table 2 (p.5), Table 61 (p.45), Section 6.1 (p.5)
- **问题**: Entity construction 是论文唯一 consistently positive 的推荐策略，但：
  - 增益幅度：+1.02–1.40 pp（Few-NERD），+0.71 pp（SciERC），CoNLL 负增益（Table 61: ΔF1≈0 pp）
  - 推理成本：N× inference（N=8 时成本 8 倍）
  - Table 61 verdict: "positive" 但仅在 SciERC 和 Few-NERD 上；CoNLL 和 WNUT-17 上 "dataset-dep."
  - 相比之下，cross-model SC 增益 +0.42 pp 但成本 2N×，性价比更低
  - 这使得论文的 prescriptive value 有限：实践者是否值得为 ~1pp 增益付出 8× 推理成本？
- **建议**: 在 Section 10 或 Discussion 中直接 address cost-effectiveness question，而非仅在 Table 61 隐式呈现。

---

## 小问题（不影响接收）

1. **Orphan bib entries**: `holm1979simple` 和 `xia2025survey` 在 .bib 中存在但似乎未被 `\cite` 引用（verify_references 工具检测）。Holm (1979) 在文中被频繁提及但可能仅作为方法名（"Holm-Bonferroni"）而未显式 \cite。建议补充 \cite 或移除 orphan entry。

2. **Abstract 中 "ρ up to 0.45" 精度**: 我在所有表格中找到的最高 ρ 值为 ~0.427（LP on SciERC full set, Table 3）和 ~0.472（EM on LLaMA CoNLL, Table 7）。0.45 作为概括数字尚可接受，但若 EM 0.472 是最大值，则 "up to 0.47" 更精确；若 LP 0.427 是主要参考，则 "up to 0.43" 更准确。建议核实并统一。

3. **Table 30 中 "Ratio" 列在 Δ<0 时显示 "—"**: 建议说明 "—" 代表 bound 不适用（actual gain negative, bound non-negative），而非数据缺失。

4. **Appendix 编号系统复杂**: 附录从 a 到 ag（33 个子附录），编号到 ab.9, ae 等。虽然内容丰富，但导航困难。建议增加附录目录（Table of Contents for Appendix）。

5. **Figure 3 (p.7)**: Y 轴标签 "Instance degeneracy ρ and LP selection gain across..." 不够清晰，应分别标注左右 Y 轴。

---

## 主要优势

1. **研究问题重要且定位精准**: Self-consistency 在 reasoning 任务上被广泛研究，但在 structured generation（尤其是 entity-level IE）上的失败机制是一个真实且未被探索的 gap。论文准确识别了 "correlation-selection gap"（信号与 oracle 相关但选择无效）这一核心矛盾。

2. **四阶段诊断框架逻辑清晰**: QE → degeneracy → agreement fidelity → LP compression 的递进式诊断结构合理，每个阶段都有对应的 metric 和实验验证。Figure 1 的 overview 图和 Table 2 的方法总结使复杂实验结构可读性强。

3. **实验覆盖度在 NER 范围内堪称典范**: 4 个 NER 数据集（SciERC, Few-NERD, CoNLL-2003, WNUT-17）覆盖不同难度梯度；2 个模型家族（Qwen, LLaMA）；4B–72B 规模范围；5 种信号（SJ, FK, EM, VC, LP）；60+ 张实验表格。这一覆盖度远超同领域多数论文。

4. **统计方法论严谨**: 全局 Holm-Bonferroni 校正 (k=57) 而非仅报告 raw p-values；paired bootstrap tests (B=10,000)；bootstrap 95% CI；multi-seed design (3 seeds on most datasets)；post-hoc power analysis (Table 55)。这种统计严谨度在 NLP 实验论文中不常见。

5. **MBR 等价性 (Proposition 1)**: 将 entity construction 与 minimum Bayes risk decoding 联系起来是一个 clean 的理论贡献，为诊断框架提供了概率论基础。虽然 degeneracy bound 较松，但等价性本身是精确的。

6. **三个独立诊断探针 (ESJ, MRSC, LSC)**: 从不同角度（prompt-based self-evaluation、multi-round refinement、hidden-state analysis）收敛到相同结论（entity-level self-verification 失败），提供了 converging evidence 而非单一证据线。

7. **Prescriptive output (Table 61, Appendix ae)**: 在诊断之上提供了实用的决策框架，告诉实践者在什么条件下该用什么策略，这在分析型论文中不常见。

---

## Questions to Authors

1. **关于 k=19 vs k=21**: 请确认 Abstract 中 "selection family k=19" 的 k 值来源。Table 13 的 selection family 含 21 行测试。如果有 2 项被排除，请说明理由。

2. **关于 RE 的 entity span error 混淆**: 是否考虑过先用 oracle entity spans 再评估 RE 信号质量？这可以隔离 RE-specific 的 self-consistency 失败（如果存在）与 NER 错误传播。

3. **关于因果推断**: 是否有任何干预实验（如通过 prompt engineering 降低 degeneracy 后观察增益变化）来支持 degeneracy → selection failure 的因果方向？Table 7 的温度实验接近干预，但结果显示温度变化对信号质量影响不大。

4. **关于 bound tightness**: Proposition 1 的 entity-wise independence 假设在 NER 中是否合理？相邻 entity mentions 的预测往往相关（如 "Barack Obama" 后更可能出现 "United States"）。这一相关性是否解释了 bound 的松散度？

5. **关于 GPT-5.5 SQL 实验**: n=196 instances 是否有具体的统计功效计算？在该样本量下，能检测到的最小效应量 (MDE) 是多少？

---

## Missing References

论文引用覆盖面总体良好（51 篇，OpenAlex 验证 46 篇 verified），但可能遗漏以下相关工作：

1. **Structured prediction 中的 MBR decoding**: 论文引用了 Eikema et al. (2025) 的 structure-conditional MBR，但未引用 DeNero et al. (2009) 关于 MT 中 consensus decoding 的经典工作，该工作与 entity construction 的 MBR 等价性直接相关。

2. **NER 中的 calibration**: 论文讨论了 calibration（Appendix c），但未引用 Desai & Durrett (2020) "Calibration of Pre-trained Transformers" 中关于 sequence labeling calibration 的发现。

3. **Self-consistency 的 failure mode 分类**: Chen et al. (2024a) 和 Yun et al. (2025) 已被引用，但 Huang et al. (2024) "Large Language Models Cannot Self-Correct Reasoning Yet" 也讨论了 self-verification 失败，可能值得在 Related Work (Section 8) 中讨论。

---

## Confidence 说明

**Confidence: 4/5** — 我对 NER/IE 评估方法论、self-consistency 文献、以及统计检验方法（Holm-Bonferroni, bootstrap）较为熟悉。我仔细审读了全部 46 页（包括所有附录表格和理论推导）。对 MBR decoding 的理论细节（Proposition 1 的 proof）的审查是 moderate-depth 而非 expert-level，因为结构化预测中的 MBR 不是我的核心专长。


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

_source line 2937 · 2026-05-21T11:32:34.856459+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性 + 论文完整性 + 写作质量\n\n### 总体评分\n**Overall**: 3.0 — Findings（可被 Findings 接收）\n\n### Must-Fix 问题（3 个 critical）\n\n**N1** [critical] 标题与实验范围严重不匹配\n- 标题 \"Structured Generation\" 极其宽泛，但实际实验以 NER 为绝对主体（4 datasets × 2 model families）。RE 仅 1 个数据集探索性扩展（Appendix o），SQL 仅 post-hoc validation。ARR guidelines 要求 \"evaluation samples must represent the populations discussed in conclusions\"——当前标题构成 overclaiming。\n\n**N2** [critical] Prescriptive gains 边际化且依赖数据集\n- LP-weighted entity construction +1.02–1.40pp 仅在 Few-NERD 上显著，SciERC/CoNLL 不一致。Cross-model ensemble 需 2N× cost 仅 +0.42pp。Table 61 显示唯一 unconditionally positive 的方法（SC+construction）最佳也仅 +1.4pp/8× cost。\n- 论文将 prescriptive results 定位为第四项核心贡献，但增益接近噪声水平，严重削弱实用价值。\n\n**N3** [critical] 主体结构混乱：诊断/方法/结果交织\n- Sections 3–5 在介绍方法时嵌入 SciERC 初步结果，Section 7 又展开\"完整实验\"，大量重叠。读者难以分辨 preliminary diagnostic 和 main experiment。\n\n### Should-Fix 问题（5 个 warning）\n\n**W1** \"Capability ceiling\" 措辞过于绝对——仅测试 3B–8B 开源模型，更大模型可能改变结论\n**W2** 模型多样性不足——缺 70B+、闭源 API 模型、instruction-tuned vs base 对比\n**W3** RE 分析的混合证据削弱泛化声明——RE 失败机制与 NER 不同（span error vs degeneracy），统一归因于 correlation-selection gap 过度简化\n**W4** Abstract 信息密度过高——250 词内塞入 ρ≤0.45、AUROC≤0.82、87.2% degeneracy 等大量数字\n**W5** Related Work 后置（Section 8）影响阅读——读者需提前理解 SC 在 reasoning 中为何有效才能理解在 IE 中的失败\n\n### 小问题（6 个）\n- M1: 2 个 orphan bib entries 未引用\n- M2: Figure 2 caption \"oracle gap\" 未自含定义\n- M3: \"VotConsLogProb\" 在 Table 3 突然出现未正式定义\n- M4: Table 61 (cost-benefit) 被埋在 45 页附录中，应提到主文\n- M5: \"degeneracy\" 首次使用缺括号解释\n- M6: \"Inverse Scaling\" 标题与实际内容（scaling 变慢）不完全对应\n\n### 主要优势\n- S1: 4 阶段诊断级联是最有价值的贡献\n- S2: 9 大类方法 × 4 数据集 × 2 模型族覆盖面极广\n- S3: MBR 等价性证明 + degeneracy bound + scaling law 提供理论支撑\n- S4: Bootstrap CI + Holm-Bonferroni 统计严谨性远超同类论文\n- S5: ~35 页附录可追溯性极高\n- S6: Table 62 与先前工作差异化清晰\n\n### Missing References\n1. \"Uncertainty Quantification and Confidence Calibration in LLMs: A Survey\" (KDD 2025)\n2. \"A Simple but Effective Approach to Improve Structured LLM Output for IE\" (Aronica et al., 2024)\n3. \"Test-time Scaling of LLMs: A Survey\" (2025, arXiv:2511.14772)\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor 和 Missing References，标注 [AGREE] 或 [REBUT]。"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性 + 论文完整性 + 写作质量\n\n### 总体评分\n**Overall**: 3.0 — Findings（可被 Findings 接收）\n\n### Must-Fix 问题（3 个 critical）\n\n**N1** [critical] 标题与实验范围严重不匹配\n- 标题 \"Structured Generation\" 极其宽泛，但实际实验以 NER 为绝对主体（4 datasets × 2 model families）。RE 仅 1 个数据集探索性扩展（Appendix o），SQL 仅 post-hoc validation。ARR guidelines 要求 \"evaluation samples must represent the populations discussed in conclusions\"——当前标题构成 overclaiming。\n\n**N2** [critical] Prescriptive gains 边际化且依赖数据集\n- LP-weighted entity construction +1.02–1.40pp 仅在 Few-NERD 上显著，SciERC/CoNLL 不一致。Cross-model ensemble 需 2N× cost 仅 +0.42pp。Table 61 显示唯一 unconditionally positive 的方法（SC+construction）最佳也仅 +1.4pp/8× cost。\n- 论文将 prescriptive results 定位为第四项核心贡献，但增益接近噪声水平，严重削弱实用价值。\n\n**N3** [critical] 主体结构混乱：诊断/方法/结果交织\n- Sections 3–5 在介绍方法时嵌入 SciERC 初步结果，Section 7 又展开\"完整实验\"，大量重叠。读者难以分辨 preliminary diagnostic 和 main experiment。\n\n### Should-Fix 问题（5 个 warning）\n\n**W1** \"Capability ceiling\" 措辞过于绝对——仅测试 3B–8B 开源模型，更大模型可能改变结论\n**W2** 模型多样性不足——缺 70B+、闭源 API 模型、instruction-tuned vs base 对比\n**W3** RE 分析的混合证据削弱泛化声明——RE 失败机制与 NER 不同（span error vs degeneracy），统一归因于 correlation-selection gap 过度简化\n**W4** Abstract 信息密度过高——250 词内塞入 ρ≤0.45、AUROC≤0.82、87.2% degeneracy 等大量数字\n**W5** Related Work 后置（Section 8）影响阅读——读者需提前理解 SC 在 reasoning 中为何有效才能理解在 IE 中的失败\n\n### 小问题（6 个）\n- M1: 2 个 orphan bib entries 未引用\n- M2: Figure 2 caption \"oracle gap\" 未自含定义\n- M3: \"VotConsLogProb\" 在 Table 3 突然出现未正式定义\n- M4: Table 61 (cost-benefit) 被埋在 45 页附录中，应提到主文\n- M5: \"degeneracy\" 首次使用缺括号解释\n- M6: \"Inverse Scaling\" 标题与实际内容（scaling 变慢）不完全对应\n\n### 主要优势\n- S1: 4 阶段诊断级联是最有价值的贡献\n- S2: 9 大类方法 × 4 数据集 × 2 模型族覆盖面极广\n- S3: MBR 等价性证明 + degeneracy bound + scaling law 提供理论支撑\n- S4: Bootstrap CI + Holm-Bonferroni 统计严谨性远超同类论文\n- S5: ~35 页附录可追溯性极高\n- S6: Table 62 与先前工作差异化清晰\n\n### Missing References\n1. \"Uncertainty Quantification and Confidence Calibration in LLMs: A Survey\" (KDD 2025)\n2. \"A Simple but Effective Approach to Improve Structured LLM Output for IE\" (Aronica et al., 2024)\n3. \"Test-time Scaling of LLMs: A Survey\" (2025, arXiv:2511.14772)\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor 和 Missing References，标注 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2938 · 2026-05-21T11:32:56.207945+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21351
}
```

</details>

---


### Tool call

_source line 2939 · 2026-05-21T11:32:56.359027+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性 + 实验充分性\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 泛化性声明严重超出证据范围：标题说 \"Structured Generation\" 但证据几乎全是 NER\n- RE 仅 SciERC 1 个数据集，55.5% F1=0 因 entity span errors。SQL 仅 n=196 一句话描述。论文 60+ 表格中 RE 专属仅 3 张，SQL 无表格。\n\n**N2** [critical] 因果语言与相关性证据不匹配\n- Section 9 \"Degeneracy governs the selection gap\"；Abstract \"the failure is systematic: a four-stage diagnostic cascade\"——但论文实际做的是相关性诊断而非因果机制。Figure 1 caption 正确标注 \"not causal claims\"，但主体多处使用因果动词。无干预实验验证因果方向。\n\n**N3** [critical] Holm-Bonferroni k=19 vs Table 13 k=21 不一致\n- Abstract 声称 \"selection family k=19\"，但 Table 13 selection family 共 21 项测试。差异 2 项未解释。影响 p_adj 可复现性。\n\n### Should-Fix 问题\n\n**W1** Degeneracy bound 极松（仅捕获 4.7–12.1% 实际增益），且无法预测负增益方向\n**W2** SciERC RE 分析被 entity span error 严重混淆（55.5% zero F1），本质测量 NER→RE 错误传播\n**W3** k=57 全局 Holm + 中等样本量，RE/小配置统计功效不足，负面结论可能是 power 问题\n**W4** 7 种方法分类边界模糊——diagnostic probes vs selection methods 未区分；Het-T 在 Table 2 无对应行\n**W5** Entity construction 正面增益一致但幅度有限 (+1.0–1.4pp at 8× cost)\n\n### 小问题\n1. Orphan bib entries: holm1979simple, xia2025survey\n2. Abstract \"ρ up to 0.45\" 精度待核实（最高 EM 0.472）\n3. Table 30 Ratio 列 \"—\" 含义未说明\n4. 附录编号到 ag，导航困难，建议增加 TOC\n5. Figure 3 Y 轴标签不够清晰\n\n### 主要优势\n1. 研究问题重要且定位精准（SC 在 structured generation 的失败机制）\n2. 四阶段诊断框架逻辑清晰\n3. NER 范围内实验覆盖度堪称典范\n4. 统计方法论严谨（Holm k=57, bootstrap B=10000, multi-seed）\n5. MBR 等价性是 clean 的理论贡献\n6. 三个独立诊断探针收敛同一结论\n7. Prescriptive output (Table 61, Appendix ae) 在分析型论文中少见\n\n### Questions to Authors\n1. k=19 vs k=21 来源？\n2. 是否考虑用 oracle entity spans 隔离 RE-specific 失败？\n3. 是否有干预实验支持 degeneracy→selection failure 因果方向？\n4. Entity-wise independence 假设在 NER 中是否合理？\n5. GPT-5.5 SQL n=196 的 MDE 是多少？\n\n### Missing References\n1. DeNero et al. (2009) — consensus decoding in MT\n2. Desai & Durrett (2020) — calibration of pre-trained transformers for sequence labeling\n3. Huang et al. (2024) — \"LLMs Cannot Self-Correct Reasoning Yet\"\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor、Questions 和 Missing References，标注 [AGREE] 或 [REBUT]。"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性 + 实验充分性\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 泛化性声明严重超出证据范围：标题说 \"Structured Generation\" 但证据几乎全是 NER\n- RE 仅 SciERC 1 个数据集，55.5% F1=0 因 entity span errors。SQL 仅 n=196 一句话描述。论文 60+ 表格中 RE 专属仅 3 张，SQL 无表格。\n\n**N2** [critical] 因果语言与相关性证据不匹配\n- Section 9 \"Degeneracy governs the selection gap\"；Abstract \"the failure is systematic: a four-stage diagnostic cascade\"——但论文实际做的是相关性诊断而非因果机制。Figure 1 caption 正确标注 \"not causal claims\"，但主体多处使用因果动词。无干预实验验证因果方向。\n\n**N3** [critical] Holm-Bonferroni k=19 vs Table 13 k=21 不一致\n- Abstract 声称 \"selection family k=19\"，但 Table 13 selection family 共 21 项测试。差异 2 项未解释。影响 p_adj 可复现性。\n\n### Should-Fix 问题\n\n**W1** Degeneracy bound 极松（仅捕获 4.7–12.1% 实际增益），且无法预测负增益方向\n**W2** SciERC RE 分析被 entity span error 严重混淆（55.5% zero F1），本质测量 NER→RE 错误传播\n**W3** k=57 全局 Holm + 中等样本量，RE/小配置统计功效不足，负面结论可能是 power 问题\n**W4** 7 种方法分类边界模糊——diagnostic probes vs selection methods 未区分；Het-T 在 Table 2 无对应行\n**W5** Entity construction 正面增益一致但幅度有限 (+1.0–1.4pp at 8× cost)\n\n### 小问题\n1. Orphan bib entries: holm1979simple, xia2025survey\n2. Abstract \"ρ up to 0.45\" 精度待核实（最高 EM 0.472）\n3. Table 30 Ratio 列 \"—\" 含义未说明\n4. 附录编号到 ag，导航困难，建议增加 TOC\n5. Figure 3 Y 轴标签不够清晰\n\n### 主要优势\n1. 研究问题重要且定位精准（SC 在 structured generation 的失败机制）\n2. 四阶段诊断框架逻辑清晰\n3. NER 范围内实验覆盖度堪称典范\n4. 统计方法论严谨（Holm k=57, bootstrap B=10000, multi-seed）\n5. MBR 等价性是 clean 的理论贡献\n6. 三个独立诊断探针收敛同一结论\n7. Prescriptive output (Table 61, Appendix ae) 在分析型论文中少见\n\n### Questions to Authors\n1. k=19 vs k=21 来源？\n2. 是否考虑用 oracle entity spans 隔离 RE-specific 失败？\n3. 是否有干预实验支持 degeneracy→selection failure 因果方向？\n4. Entity-wise independence 假设在 NER 中是否合理？\n5. GPT-5.5 SQL n=196 的 MDE 是多少？\n\n### Missing References\n1. DeNero et al. (2009) — consensus decoding in MT\n2. Desai & Durrett (2020) — calibration of pre-trained transformers for sequence labeling\n3. Huang et al. (2024) — \"LLMs Cannot Self-Correct Reasoning Yet\"\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor、Questions 和 Missing References，标注 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2940 · 2026-05-21T11:32:57.972428+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1613
}
```

</details>

---


### Assistant

_source line 2941 · 2026-05-21T11:33:01.249624+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 222

## Round 222

2 recorded events


### User

_source line 2942 · 2026-05-21T11:33:04.022451+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心结论**: Overall 3.5 (Borderline Conference)。

**3 个 Must-Fix**:
1. 泛化性 overclaiming——标题说 "Structured Generation" 但证据 ~95% 是 NER，RE 受 entity span error 混淆，SQL 仅 1 句话 (n=196)
2. 因果语言与相关性证据不匹配——Figure 1 caption 说 "not causal" 但 Section 9 用 "governs" 等因果动词
3. Holm-Bonferroni k=19 vs Table 13 中 k=21 不一致，影响核心统计声明可复现性

**5 个 Should-Fix**: degeneracy bound 极松 (4.7–12.1%)、RE 的 entity span error 混淆、k=57 全局校正导致统计功效不足、7 种方法分类边界模糊、entity construction 增益虽一致但仅 ~1pp 且需 8× 推理成本。

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

_source line 2943 · 2026-05-21T11:33:08.845431+00:00_

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


## Round 223

## Round 223

2 recorded events


### User

_source line 2944 · 2026-05-21T11:37:01.517294+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1

### 回应总结
R1 的 17 个具体问题中，15 个标注 [AGREE]，1 个标注 [REBUT]（R1-Q3 干预实验的可行性），1 个 [AGREE with nuance]（R1-N2 因果语言，同意问题存在但承认论文有部分准因果证据缓解）。

### 两位 Reviewer 独立收敛的 Critical Issues
1. **标题-范围不匹配**（R1-N1 = R2-N1）：标题 "Structured Generation" 显著超出 NER-centric 实验范围。最高优先级修订。
2. **Prescriptive gains 边际化**（R1-W5 = R2-N2）：+1.0–1.4pp at 8× cost 缺乏实践吸引力，且依赖数据集。

### R1 额外贡献的重要问题（R2 未充分覆盖）
3. **因果语言不当**（R1-N2）：Section 9 "governs"、Abstract "why" 等因果动词与相关性证据不匹配。Figure 1 caption 正确标注 "not causal" 但未贯彻全文。[AGREE，建议替换因果动词，保留仅在理论支撑处的机制性语言]
4. **k 值不一致**（R1-N3）：Abstract k=19 vs Table 13 实际行数不匹配，影响 p_adj 可复现性。[AGREE，需作者逐行核对]

### 唯一 REBUT：R1-Q3（干预实验）
R1 要求正式干预实验验证 degeneracy→selection failure 因果链。标准合理，但完全干预不可行：degeneracy 是 emergent property 而非可独立操控的 treatment。论文已提供三条准因果证据：(a) MBR 理论机制 (Proposition 1)；(b) 非退化子集条件分析 (Table 14)；(c) 温度扫描调节 degeneracy (Table 43)。建议作者在 Discussion 中明确承认缺乏正式因果实验，同时列出准因果证据链。

### 综合判断
R1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。分歧主要在：
- R1 对 NER 范围内实验质量的认可度更高（称之为"典范"），这点我同意
- 但我认为 prescriptive gains 的边际化程度构成更严重的 impact 问题（我将其列为 critical N2，R1 仅列为 W5）
- 如果作者能修复标题范围、因果语言、k 值不一致三个问题，并将 prescriptive results 降级为 secondary contribution，我愿意上调至 3.5

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

_source line 2945 · 2026-05-21T11:37:13.883994+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 224

## Round 224

20 recorded events


### User

_source line 2946 · 2026-05-21T11:37:15.107689+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题回应

### [AGREE] R2-N1: 标题与实验范围严重不匹配

同意，这与我自己的 R1-N1 一致。证据：

- NER 有 4 数据集 × 2 模型族 × 多 seed × 60+ 张表格。RE 仅 SciERC 一个数据集（Appendix o），且受 entity span error 严重混淆（Appendix d, p.15 承认 55.5% RE 实例 F1=0）。SQL 仅一句话提及 GPT-5.5 on Spider (n=196, p.2)。
- 标题 "Structured Generation" 与 Limitations (p.9) 自己承认的 "exploratory RE extension" 和有限 SQL 证据矛盾。

补充 R2 未提到的一点：RE 分析中 FEATURE-OF 关系 ρ≈0（反方向）而 HYPONYM-OF ρ=0.646（Appendix d），说明 RE 信号质量高度关系类型依赖，不能泛化为 "RE task" 级别的结论。

**结论**: 两位 Reviewer 对此问题完全一致，应被视为 consensus critical issue。

### [AGREE with nuance] R2-N2: Prescriptive gains 边际化且依赖数据集

部分同意，但认为 R2 对其严重程度的判断略偏高。

**同意的部分**:
- Entity construction +1.02–1.40pp 确实幅度有限（Table 2, p.5）。Cross-model SC +0.42pp at 2N× cost 性价比低（Table 61, p.45）。
- Table 61 显示多数策略的 verdict 是 "dataset-dep." 或 "no gain"，仅 SC+construction 为 "positive"，但最佳也仅 +1.4pp。
- 这与我的 R1-W5 一致。

**不同意上升到 Must-Fix 的理由**:
- 论文的主要贡献是**诊断框架**（四阶段级联），而非 prescriptive methods。R2 自己在 S1 中承认 "4 阶段诊断级联是最有价值的贡献"。
- Prescriptive results 在 Introduction (p.2) 被明确列为 **contribution #4**（四个贡献中的最后一个），不是 primary claim。
- **Negative results 本身有价值**: 论文系统性地证明了 7 种 entity-level 方法在 NER 上均不 work（Section 3, Table 2），这对 NLP 社区有重要参考意义——避免后续研究者重复尝试已被证伪的方向。
- 将此定为 Must-Fix 等于要求论文产生大幅正面增益才能被接收，这对 diagnostic/negative-result 论文不公平。

**我的建议**: 保持 Should-Fix 级别。建议作者在 Section 10 中更坦诚地讨论 cost-effectiveness（当前仅 Table 61 隐式呈现），并降低 prescriptive contribution 的 framing 强度。

### [REBUT] R2-N3: 主体结构混乱——Sections 3–5 诊断/方法/结果交织

**不同意此为 critical issue，理由如下：**

1. **Sections 3–5 的结构是 diagnostic cascade 的逻辑必然**。论文的 framing 是一个四阶段诊断流程——每个阶段提出假设、介绍测量工具、在 SciERC 上验证、得出阶段性结论后进入下一阶段。这是 **hypothesis-driven diagnostic narrative**，不是 methods-then-results 的标准结构。
   - Section 3 "How Self-Verification Fails": 假设（模型能 self-verify）→ 三个探针（ESJ, MRSC, LSC）→ SciERC 结果（均失败）→ 结论（self-verification 不可靠）
   - Section 4 "Where Single-Signal Selection Fails": 分解 correlation-selection gap → SciERC 初步证据 → 识别 degeneracy 和 LP compression 两个因素
   - Section 5 "Adaptive Methods": 在 Section 3–4 的诊断基础上提出补救策略
   - Section 7 "Experiments": 将 SciERC 上的 preliminary findings 扩展到全部 4 datasets × 2 models 验证

2. **SciERC 的 preliminary 角色是明确的**。Section 5 第一段 (p.5): "Since instance-level selection fails (§4), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking." Section 7.1 (p.6): "We evaluate on four English NER benchmarks spanning a difficulty gradient." 从单数据集诊断到多数据集验证的逻辑跃迁是清晰的。

3. **替代结构的问题**。如果严格分离 methods 和 results，读者需要先读 ~3 页纯方法描述（7 种方法 + 3 种探针 + 诊断框架定义），再读 ~3 页纯结果，两部分之间的逻辑联系会断裂。当前结构让读者能 **incrementally build understanding**，这对一篇有 7+ 方法的复杂实验论文是合理的设计选择。

4. **ACL/EMNLP 先例**。Chen et al. (2024a) "Two Failures of Self-Consistency" 同样在方法介绍中嵌入初步实验结果，被 TMLR 接收。Yun et al. (2025) "The Price of Format" 在 Findings of EMNLP 2025 发表，同样采用 diagnostic-interleaved 结构。

**我的建议**: 这是写作风格而非结构缺陷。建议在 Section 3 开头增加一句 roadmap 说明（"We first diagnose on SciERC (§3–4), then validate across datasets (§7)"），帮助读者建立预期。但不应要求重构全文。

---

## Should-Fix 问题回应

### [REBUT] R2-W1: "Capability ceiling" 措辞过于绝对——仅测试 3B–8B 开源模型

**R2 的事实前提有误**。论文测试的模型远不止 3B–8B：

- **Qwen2.5-72B-Instruct-AWQ**: Appendix ab.9 (p.34), Table 60 (p.45) 提供了完整的 zero-shot vs few-shot 对比，覆盖 SciERC, CoNLL, Few-NERD 三个数据集。72B 模型 degeneracy 仍达 46.2%–70.0%（Table 60）。
- **Qwen2.5-14B**: 14B scale ablation 在 Appendix l.1 (Table 15) 中报告。
- **Qwen2.5-4B**: 4B scale ablation 同在 Table 15。
- **GPT-5.5**: 闭源模型，200 Few-NERD instances (p.6), 50% degeneracy, SJ ρ=0.340。
- **Figure 10** (p.28) 明确展示了从 4B 到 72B 的 scaling curve，显示 oracle F1 ceiling 持续增长但 correlation-selection gap 不收敛。

因此论文覆盖了 **4B → 72B 开源 + 闭源 GPT-5.5**，"Capability ceiling" 的措辞有跨规模和跨模型族的证据支撑。

"Ceiling" 指的是 **self-consistency 机制本身的能力上限**（degeneracy + agreement infidelity + LP compression 共同造成的结构性瓶颈），而非 "当前最大模型的极限"。这一概念在论文中有明确定义（Section 1, p.1; Section 6.2, p.5-6）。

**部分同意**: instruction-tuned vs base 的对比确实缺失，Limitations (p.9) 也承认这一点。但这不影响 "capability ceiling" 措辞的合理性。

### [AGREE] R2-W2: 模型多样性——instruction-tuned vs base 对比缺失

**部分同意，但需修正 R2 的事实错误**:

- R2 称 "缺 70B+" — 事实上 Qwen2.5-72B 已被测试（Table 60, Appendix ab.9），72B > 70B。
- R2 称 "缺闭源 API 模型" — GPT-5.5 已被测试（p.6），虽然规模有限（200 instances, 仅 Few-NERD）。
- **真正缺失的是 instruction-tuned vs base 对比**。当前所有 fine-tuned 模型都基于 Instruct 版本（Qwen3-8B-Instruct, LLaMA-3.1-8B-Instruct via LlamaFactory, p.6），zero-shot 模型也是 Instruct-AWQ。Base model 的 degeneracy 特征可能不同（base model 通常更 diverse）。这一对比确实值得补充。
- Limitations (p.9) 承认了这一点。

### [AGREE] R2-W3: RE 分析的混合证据削弱泛化声明

同意，这与我的 R1-W2 一致。RE 的 entity span error 混淆（Appendix d: 55.5% F1=0）使得 RE 分析测量的主要是 NER-to-RE 错误传播而非 RE 本身的 self-consistency 失败。论文在 Limitations (p.9) 和 Appendix o 开头标注了 "exploratory"，但主文 Section 7.6 (p.7) 和 Table 3 中 RE 与 NER 并列呈现时未充分标注混淆因素。

### [REBUT mildly] R2-W4: Abstract 信息密度过高

**不太同意这是一个需要修改的问题**:

- Abstract 中的数字（ρ≤0.45, AUROC≤0.82, 87.2% degeneracy, +1.39pp, k=19）每个都对应一个具体的实验结论。对于一篇 46 页、60+ 表格的 comprehensive empirical study，Abstract 需要足够的数字来 anchor 关键发现。
- 对比同类 diagnostic 论文：Chen et al. (2024a) "Two Failures" 的 abstract 同样包含多个数字，Yun et al. (2025) "The Price of Format" 也类似。这是 empirical NLP 论文的常见做法。
- 删减数字会使 Abstract 变得空泛（"signals correlate but don't help" 缺乏 quantitative backing）。

**小建议**: 可以将部分数字（如 k=19）移入正文，在 Abstract 中保留最核心的 3–4 个数字。但不认为这是 Should-Fix 级别。

### [REBUT] R2-W5: Related Work 后置（Section 8）影响阅读

**不同意**:

- ACL/EMNLP 对 Related Work 位置无硬性要求。后置 Related Work 是 empirical NLP 论文的常见选择，尤其当论文需要先建立自己的方法论框架后才能有效地与先前工作做对比。
- 本论文的 Related Work 需要读者先理解 "correlation-selection gap"、"degeneracy"、"LP compression" 等论文自定义概念，才能理解与 Yun et al. (2025)、Chen et al. (2024a)、Farquhar et al. (2024) 的区分。前置 Related Work 会迫使读者在概念尚未建立时阅读对比讨论。
- Section 2 (Background, p.2-3) 已经提供了足够的 prerequisite context（SC 在 reasoning 中的成功、entity-level IE 的定义、constrained decoding 的基础），使读者能理解 Sections 3–7 的内容。
- Table 62 (p.46) 的 differentiation matrix 放在附录末尾恰好说明 Related Work 需要读者已经理解全文后才能充分 appreciate。

---

## Minor 问题回应

### [AGREE] R2-M1: 2 个 orphan bib entries 未引用

同意，我的 verify_references 也检测到 `holm1979simple` 和 `xia2025survey` 在 .bib 中存在但未被 `\cite` 显式引用。`holm1979simple` 在文中被频繁提及（"Holm-Bonferroni correction"），应补充 `\cite{holm1979simple}`。`xia2025survey` 若不引用则应从 .bib 移除。

### [AGREE] R2-M2: Figure 2 caption "oracle gap" 未自含定义

同意。Figure 2 caption (p.5) 用 "Dashed green: oracle (+1.13pp)" 标注了 oracle 参考线，但 "oracle gap"（greedy F1 与 oracle F1 之差）作为关键概念未在 caption 中自含定义。建议在 caption 中添加 "(oracle headroom = best-of-N F1 − greedy F1)"。

### [AGREE] R2-M3: "VotConsLogProb" 在 Figure 6 / 表格中未正式定义

同意。Table 6 (p.13) 定义了 LP 和 VC 等简称，但 Figure 6 heatmap (p.17) 使用 "VotConsLogProb" 这一全称，未在任何地方建立与 LP 的对应关系。读者可能困惑这是一个新信号还是 LP 的别名。建议统一术语。

### [AGREE] R2-M4: Table 61 (cost-benefit) 应在主文中引用

同意。Table 61 (p.45) 是论文最有实用价值的产出之一（方法 × 成本 × 增益 × verdict），但被埋在 Appendix ae 第 45 页。Section 10 (Conclusion, p.8) 或 Section 5 应明确引用此表，或将其简化版纳入主文。这与我 R1-W5 的建议一致。

### [REBUT mildly] R2-M5: "degeneracy" 首次使用缺括号解释

**部分同意但不认为严重**:

- Abstract 首次使用 "output degeneracy" 时未给括号定义，但 "output degeneracy" 的字面含义（输出退化/简并）对 NLP 读者是可理解的。
- Section 2.3 (p.3) 在正式引入时有明确定义："Instance **degeneracy**: fraction of instances where all N samples produce identical outputs"（注释形式，page 3, 第一列底部）。
- 建议在 Abstract 中 "87.2% output degeneracy" 后加括号 "(identical outputs across all N samples)"，但这是 cosmetic fix。

### [REBUT] R2-M6: "Inverse Scaling" 标题与内容不符

**不同意**:

- Section 6.2 (p.5-6) 讨论了两个 scaling 行为：(a) oracle F1 的正向 scaling（F₁(N) = a − b·N⁻ᶜ），(b) entity construction 在 adaptive threshold 下的**逆向 scaling**——"Increasing N decreases construction F1 in 40 of 58 transitions (p<0.05, Appendix s)" (p.6)。
- 这正是 "inverse scaling" 的标准含义：更多 inference compute → 更差的 performance。这与 Wei et al. (2022) 定义的 inverse scaling 一致。
- R2 将其解读为 "scaling 变慢" 是误读。论文明确描述的是 **performance degradation with increased N**，不是 diminishing returns。

---

## Missing References 回应

### [AGREE partially] "Uncertainty Quantification and Confidence Calibration in LLMs: A Survey" (KDD 2025)

论文已引用两篇相关 survey：Geng et al. (2024) "A Survey of Confidence Estimation and Calibration in Large Language Models" (NAACL 2024) 和 Xia et al. (2025) "A Survey of Uncertainty Estimation Methods on Large Language Models" (ACL Findings 2025)。第三篇 KDD survey 可作为 supplementary reference，但非必要——两篇已覆盖 calibration 和 uncertainty estimation 的综述需求。建议在 camera-ready 中补充。

### [AGREE] "A Simple but Effective Approach to Improve Structured LLM Output for IE" (Aronica et al., 2024)

如果该论文提出了改善 structured IE output 质量的方法，且与本文的 entity construction / constrained decoding 方向直接相关，应在 Related Work (Section 8) 或 Section 5 中引用和讨论。需要作者确认 overlap 程度。

### [AGREE partially] "Test-time Scaling of LLMs: A Survey" (2025, arXiv:2511.14772)

论文已引用 test-time scaling 的核心文献（Snell et al., 2025; Brown et al., 2024; Muennighoff et al., 2025），一篇 2025 年的 survey 可在 camera-ready 中补充以增强完整性，但不影响当前论文的引用覆盖面。

---

## 总结

| R2 Issue | R1 判断 | 理由 |
|----------|--------|------|
| N1 标题 overclaiming | **AGREE** | 与 R1-N1 一致，consensus critical |
| N2 Prescriptive 增益弱 | **AGREE 降为 Should-Fix** | 论文主要贡献是诊断框架；negative results 有独立价值 |
| N3 结构混乱 | **REBUT** | Diagnostic narrative 需要 interleaved 结构；有 ACL/EMNLP 先例 |
| W1 Ceiling 措辞绝对 | **REBUT** | R2 事实前提有误，论文测至 72B + GPT-5.5 |
| W2 模型多样性 | **部分 AGREE** | 缺 instruction vs base 对比，但 R2 称 "缺 70B+" 事实有误 |
| W3 RE 混合证据 | **AGREE** | 与 R1-W2 一致 |
| W4 Abstract 密度 | **REBUT mildly** | 符合 empirical NLP 论文惯例 |
| W5 Related Work 后置 | **REBUT** | 标准做法，概念依赖决定了后置更合理 |
| M1–M4 | **AGREE** | 均为合理的 minor fixes |
| M5 degeneracy 定义 | **部分 AGREE** | Section 2.3 有定义，Abstract 可补充 |
| M6 Inverse Scaling | **REBUT** | R2 误读，论文描述的确是 performance degradation |


---

[Reviewer 2 审稿结果]:
交叉回应已提交。17 个问题中 15 个 [AGREE]、1 个 [REBUT]（干预实验可行性）、1 个 [AGREE with nuance]（因果语言）。两位 Reviewer 在标题-范围不匹配和 prescriptive gains 边际化上独立收敛，这两个应作为修订最高优先级。

---

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部意见的逐条回应，已提交给 Review Director。

核心判断：
- **R2-N1（标题 overclaiming）**: 与我的 R1-N1 一致，**AGREE**，两位 Reviewer 形成 consensus
- **R2-N2（增益弱）**: 同意事实但**降级为 Should-Fix**——论文主贡献是诊断框架，非 prescriptive methods
- **R2-N3（结构混乱）**: **REBUT**——diagnostic narrative 需要 interleaved 结构，有先例支持
- **R2-W1（仅 3B-8B）**: **REBUT**——R2 事实前提错误，论文测至 72B + GPT-5.5
- **R2-M6（Inverse Scaling）**: **REBUT**——R2 误读，论文描述的确是 performance degradation with increased N

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

_source line 2947 · 2026-05-21T11:37:38.778561+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

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
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 2948 · 2026-05-21T11:37:38.779001+00:00_

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

_source line 2949 · 2026-05-21T11:37:40.184581+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T11:19:20.690230+00:00\", \"completed_at\": \"2026-05-21T11:23:15.937825+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前两页为连续纯文本（Title/Abstract/Introduction），无任何 display item。第一个视觉锚点 Figure 1 出现在第 3 页。对于实证为主的论文，前 2 页缺乏视觉锚点会削弱审稿人的第一印象。建议在第 1 页底部或第 2 页加入 teaser figure 或将 Figure 1 提前\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（概览图）信息密度高、颜色编码清晰，能有效传达论文核心框架（correlation-selection gap 的四阶段诊断级联）。Caption 自包含。但部分面板内文字偏小（约正文字号 60-65%），打印后可能难以阅读\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 使用 booktabs 风格，最优值加粗，精度统一——排版规范。右栏 float 位置合理\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 + Table 2 同页，视觉节奏好。Figure 2 bar chart 颜色区分度好（绿色虚线 oracle 清晰可辨），Table 2 紧凑但可读\"}, {\"severity\": \"info\", \"dimension\": \"page 6-7\", \"message\": \"Display items 密度非常高（Tables 3-5 + Figure 3 + Tables 6-8），文字与图表交替紧凑。页面略显拥挤但信息承载量高，适合实证论文的 Experiments 段\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Section 8 \\\"Related Work\\\" + Section 9 \\\"Discussion\\\" 整页纯文本，与前两页（6-7）的高密度形成较大反差。Related Work 段本身无 display item 是常规做法，但若 Discussion 能附一个总结性 figure/table 会改善布局节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段简洁（约半栏），符合 EMNLP 2026 规范。Ethics Statement 和 Checklist 从此页开始\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Figure 4（温度/样本量鲁棒性）和 Table 7 同页，附录排版节奏好\"}, {\"severity\": \"info\", \"dimension\": \"page 16\", \"message\": \"Figure 5（reliability diagrams）双面板 NER/RE 对比，清晰可读。使用对角线参考线是好的 calibration 可视化实践\"}, {\"severity\": \"warning\", \"dimension\": \"page 17\", \"message\": \"Figure 6 heatmaps 使用单色渐变（黄→深绿），虽有数值标注辅助阅读，但色盲读者可能难以区分中间梯度。建议使用双色发散色板（如 blue-white-red）以增强对比度\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 7（output length vs. LP）清晰，正/负相关
…[truncated 1501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool result

_source line 2950 · 2026-05-21T11:37:40.235302+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 2951 · 2026-05-21T11:37:40.386232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "290",
  "limit": "200"
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
    "offset": "290",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2952 · 2026-05-21T11:37:40.487254+00:00_

290	    resolution: "7→2 脚注。"
291	    resolution_round: 21
292	
293	  - id: "R21-W7"
294	    summary: "Greedy F1 多表数值不一致 (4 values)"
295	    category: experiment
296	    severity: warning
297	    status: resolved
298	    first_raised_round: 21
299	    last_seen_round: 21
300	    resolution: "Method §3.3 列出 4 值 + 3 类 protocol variants。"
301	    resolution_round: 21
302	
303	  - id: "R21-I1"
304	    summary: "Appendix 残留实验标识"
305	    category: format
306	    severity: info
307	    status: resolved
308	    first_raised_round: 21
309	    last_seen_round: 21
310	    resolution: "全文搜索确认无残留。"
311	    resolution_round: 21
312	
313	  - id: "R21-I2"
314	    summary: "'Capability trap' 措辞过强"
315	    category: writing
316	    severity: info
317	    status: resolved
318	    first_raised_round: 21
319	    last_seen_round: 21
320	    resolution: "统一使用 'capability-diversity tension'。"
321	    resolution_round: 21
322	
323	  - id: "R21-I3"
324	    summary: "3 处 -ing 短语残留"
325	    category: writing
326	    severity: info
327	    status: resolved
328	    first_raised_round: 21
329	    last_seen_round: 21
330	    resolution: "3 处改写完成。"
331	    resolution_round: 21
332	
333	  - id: "R21-MR1"
334	    summary: "缺失引用: Farquhar et al., Chen et al. pass@k"
335	    category: format
336	    severity: warning
337	    status: resolved
338	    first_raised_round: 21
339	    last_seen_round: 21
340	    resolution: "已补入 Related Work。"
341	    resolution_round: 21
342	
343	  - id: "R21-Q3"
344	    summary: "Per-entity-type ρ=-0.881 effective df 问题"
345	    category: experiment
346	    severity: info
347	    status: resolved
348	    first_raised_round: 21
349	    last_seen_round: 21
350	    resolution: "Appendix 已有 df=4 adjustment。"
351	    resolution_round: 21
352	
353	  - id: "R22-N1"
354	    summary: "正文再次超页约 2 页"
355	    category: format
356	    severity: critical
357	    status: resolved
358	    first_raised_round: 22
359	    last_seen_round: 23
360	    resolution: "Multiple compression rounds c
…[truncated 4143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2953 · 2026-05-21T11:37:45.857495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "485",
  "limit": "200"
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
    "offset": "485",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2954 · 2026-05-21T11:37:45.958475+00:00_

485	  - id: "R22-I3"
486	    summary: "Figure 3 scatter plot 标签在打印尺寸下可能难辨"
487	    category: format
488	    severity: info
489	    status: open
490	    first_raised_round: 22
491	    last_seen_round: 27
492	    mentions:
493	      - round: 25
494	        reviewers: [1, 2]
495	        note: "视觉审查确认 Figure 3 过小（p7）。"
496	      - round: 26
497	        reviewers: [1]
498	        note: "R26视觉审查再次确认p7 display items过密。"
499	      - round: 27
500	        reviewers: [2]
501	        note: "R27-R2-M2: Figure 2 bar chart灰度打印时颜色难区分，建议用hatching patterns。"
502	
503	  - id: "R22-MR1"
504	    summary: "缺失引用: ensemble-based IE, Xie et al. 2023"
505	    category: format
506	    severity: warning
507	    status: resolved
508	    first_raised_round: 22
509	    last_seen_round: 24
510	    resolution: "Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。"
511	    resolution_round: 24
512	
513	  - id: "R22-FIG1"
514	    summary: "fig_overview 缺少 Construction 贡献 + 残留 RE 文字"
515	    category: format
516	    severity: warning
517	    status: resolved
518	    first_raised_round: 22
519	    last_seen_round: 23
520	    resolution: "fig_overview regenerated as three-column layout."
521	    resolution_round: 23
522	
523	  - id: "R22-FIG2"
524	    summary: "fig_selection_gap caption 仍引用旧双面板格式"
525	    category: format
526	    severity: info
527	    status: resolved
528	    first_raised_round: 22
529	    last_seen_round: 23
530	    resolution: "Regenerated as single-panel NER-only."
531	    resolution_round: 23
532	
533	  - id: "R23-N1"
534	    summary: "Entity-level construction 新颖性不足"
535	    category: framing
536	    severity: critical
537	    status: in_progress
538	    first_raised_round: 23
539	    last_seen_round: 27
540	    mentions:
541	      - round: 23
542	        reviewers: [1, 2]
543	        note: "两位 Reviewer 独立列为 critical。"
544	      - round: 24
545	        reviewers: [1, 2]
546	        note: "降级为 diagnostic-motivated mitigation。"
547	      - round: 25
548	  
…[truncated 4279 chars]

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

_source line 2955 · 2026-05-21T11:37:49.519864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "684",
  "limit": "300"
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
    "offset": "684",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 2956 · 2026-05-21T11:37:49.570681+00:00_

684	    first_raised_round: 24
685	    last_seen_round: 24
686	    resolution: "Bootstrap CI 完成。"
687	    resolution_round: 24
688	
689	  - id: "R24-W1"
690	    summary: "'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom"
691	    category: framing
692	    severity: warning
693	    status: resolved
694	    first_raised_round: 24
695	    last_seen_round: 24
696	    resolution: "Title 'Resolving' → 'Addressing', Contribution 3 降级。"
697	    resolution_round: 24
698	
699	  - id: "R24-W2"
700	    summary: "SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)"
701	    category: experiment
702	    severity: warning
703	    status: resolved
704	    first_raised_round: 24
705	    last_seen_round: 24
706	    resolution: "加 detection threshold caveat。"
707	    resolution_round: 24
708	
709	  - id: "R24-W3"
710	    summary: "Related Work 缺少与 CISC/Self-Certainty 技术差异对比"
711	    category: writing
712	    severity: warning
713	    status: resolved
714	    first_raised_round: 24
715	    last_seen_round: 24
716	    resolution: "RW 增加 2 句技术差异。"
717	    resolution_round: 24
718	
719	  - id: "R24-W4"
720	    summary: "English-only + NER-heavy 泛化局限未在 Limitations 讨论"
721	    category: writing
722	    severity: warning
723	    status: resolved
724	    first_raised_round: 24
725	    last_seen_round: 24
726	    resolution: "Limitations 增加 1 句。"
727	    resolution_round: 24
728	
729	  - id: "R24-W5"
730	    summary: "Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试"
731	    category: experiment
732	    severity: warning
733	    status: wont_fix
734	    first_raised_round: 24
735	    last_seen_round: 26
736	    resolution: "DDL 前无法新增 signal 实验。已在 Limitations 列出。"
737	
738	  - id: "R24-W6"
739	    summary: "Appendix D 'as a reviewer correctly noted' 暗示审稿历史"
740	    category: writing
741	    severity: warning
742	    status: resolved
743	    first_raised_round: 24
744	    last_seen_round: 24
745	    resolution: "删除，改为直接陈述。"
746	    resolution_round: 24
747	
748	  - id: 
…[truncated 8040 chars]

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

_source line 2957 · 2026-05-21T11:37:54.322632+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "983",
  "limit": "200"
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
    "offset": "983",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2958 · 2026-05-21T11:37:54.373403+00:00_

983	      - round: 27
984	        reviewers: [1, 2]
985	        note: "R27 fresh review: 81 bib entries, 45 cited, 36 orphan(uncited)。两位Reviewer独立发现并共识清理。R2-N1额外发现5篇高度相关论文在bib中但未引用(Chen 'Two Failures', USC, Adaptive-Consistency, Atomic SC, Semantic Entropy)。R1交叉完全同意这是严重遗漏。"
986	    action_items:
987	      - round: 27
988	        action: "清理36条orphan bib entries。确保5篇关键论文(Chen Two Failures, USC, Adaptive-Consistency, Atomic SC, Semantic Entropy)在§8中被引用和讨论。Paper Agent已派发。"
989	        assigned_to: paper_agent
990	        status: in_progress
991	
992	  - id: "R25-W9"
993	    summary: "LP compression 缺与 LLM 校准文献的机制性对接"
994	    category: writing
995	    severity: warning
996	    status: in_progress
997	    first_raised_round: 25
998	    last_seen_round: 26
999	    mentions:
1000	      - round: 27
1001	        reviewers: []
1002	        note: "R27 fresh review 未直接提及。"
1003	
1004	  - id: "R25-W10"
1005	    summary: "三种故障模式呈 cascade 而非正交关系"
1006	    category: framing
1007	    severity: warning
1008	    status: in_progress
1009	    first_raised_round: 25
1010	    last_seen_round: 27
1011	    mentions:
1012	      - round: 26
1013	        reviewers: [1, 2]
1014	        note: "共识: 标注为descriptive diagnostic而非causal chain。"
1015	      - round: 27
1016	        reviewers: [1, 2]
1017	        note: "R27 fresh review R1-N3+R2-N2 [both critical]: cascade四阶段'Why'标题和Figure 1箭头暗示因果链，但证据全部是描述性/相关性(Spearman ρ, subgroup对比, AUROC)。§7.3自承'degeneracy alone does not predict LP direction'与§4因果叙事矛盾。R1建议'Why'→'Where and How'。两人交叉后强烈共识——这是本轮最需修改的问题。"
1018	    action_items:
1019	      - round: 27
1020	        action: "§3标题'Why Self-Verification Fails'→'How Self-Verification Fails'。§4→'Where Single-Signal Selection Fails'。全文软化因果语言。Figure 1加注descriptive diagnostic。Paper Agent已派发(MF1)。"
1021	        assigned_to: paper_agent
1022	        status: in_progress
1023	
1024	  - id: "R25-MR1"
1025	    summary: "缺失引用: EL4NER, Self-Certainty BoN 等"
1026	    category: format
1027	    severity: warning
1028	    sta
…[truncated 5619 chars]

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

_source line 2959 · 2026-05-21T11:37:58.237731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "1180",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "1180",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2960 · 2026-05-21T11:37:58.289336+00:00_

1180	    summary: "§6.2 inverse scaling 机制解释不足"
1181	    category: writing
1182	    severity: info
1183	    status: open
1184	    first_raised_round: 27
1185	    last_seen_round: 27
1186	    mentions:
1187	      - round: 27
1188	        reviewers: [2]
1189	        note: "R2-M4: SciERC converges more slowly的具体机制仅一句带过。R1交叉AGREE。"
1190	
1191	  - id: "R27-M3"
1192	    summary: "Limitations 未讨论closed-source API模型的degeneracy profile差异"
1193	    category: writing
1194	    severity: info
1195	    status: open
1196	    first_raised_round: 27
1197	    last_seen_round: 27
1198	    mentions:
1199	      - round: 27
1200	        reviewers: [2]
1201	        note: "R2-M5: 现有Limitations仅提LP signal不可用，未讨论这些模型是否有不同的degeneracy特征。R1交叉AGREE。"

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

_source line 2961 · 2026-05-21T11:42:51.678317+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ===== 历史 resolved issues (保留) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3-old\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-9 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"scope 声明在 Introduction 和 Limitations 中已存在。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"仅2个~8B fine-tuned + 1个72B zero-shot。缺closed-source模型。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R1 REBUT R2-W1(事实前提错误:论文已测72B+GPT-5.5)。R2确认事实错误但仍指出缺instruction-tuned vs base对比。共识:模型覆盖度合理但缺base model对比。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7）。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26视觉审查再次确认p7 display items过密。\"\n      - round: 27\n        reviewers: [2]\n        note: \"R27视觉审查: p6-7 display items密度高但可接受。Figure 1 部分面板文字偏小(约正文60-65%)。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 27\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"construction不应作为standalone contribution。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R2-N2列prescriptive gains为critical(+1.0-1.4pp at 8x cost)。R1降为should-fix(主贡献是诊断框架)。R1交叉回应: negative results有独立价值，prescriptive是contribution #4非primary。R2同意若修复其他问题可降级。\"\n    action_items:\n      - round: 26\n        action: \"确认construction在正文中已降级为diagnostic-motivated ablation而非contribution。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction（framing tautology）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 27\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 必须重构Abstract/Intro将structural/empirical二分法前置。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: Section 4明确区分了definitional vs empirical层面。R1-N2关注的是因果语言而非tautology本身。论文已有改善但主体仍用'governs'等因果动词。\"\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 27\n    resolution: \"R23: Reduced to 4 key numbers. R27 fresh: R2再次提出W4但R1 REBUT(empirical NLP论文惯例)。共识: 当前密度尚可接受。\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  # ===== Round 24 issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 公式删除，改为定性叙述。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"method.tex 加定义。\"\n    resolution_round: 24\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1 minor #2: 最高ρ为EM 0.472(LLaMA CoNLL)，'up to 0.45'略低。建议核实。\"\n\n  # ===== Round 25 issues =====\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"n=23 power 仅约 50% for ρ=0.4。结论过强。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及此 specific null finding。\"\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"cross-model仅1数据集1对模型。§5.3 SCD不再出现。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"'first systematic characterization'过强，应限定为'for NER'。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: 两位Reviewer独立列为consensus critical。R1-N1=R2-N1: 标题'Structured Generation'与NER-centric证据严重不匹配。RE仅1数据集(55.5% F1=0受span error混淆)，SQL仅n=196一句话。\"\n    action_items:\n      - round: 27\n        action: \"标题从'Structured Generation'缩窄为NER-specific或'Structured Information Extraction'。Abstract/Intro scope相应调整。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni；4 数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"CoNLL 增益为负 (−0.29pp)。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"p_adj矛盾(§1: 0.20 vs Table 13: 0.038)。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R2-N2 prescriptive gains边际(+1.0-1.4pp at 8x cost)。R1-W5同意事实但降为should-fix。交叉后共识: gains有限但对diagnostic论文可接受。\"\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"脚注9报告k=38但Table 13列k=57，差异k=19来源不明。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-N3 [critical]: Abstract k=19 vs Table 13实际21行。两位Reviewer交叉后共识需作者核实。\"\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"fine-tuning/scale/architecture混淆。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。Limitations已承认。\"\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"SciERC single-seed用于detailed diagnostic。bootstrap CI有缓解但不够。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh: 论文已改为3-seed(Few-NERD/CoNLL)。SciERC仍σ=0.48pp但已标注。\"\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"嵌套NER场景何时violated未讨论。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-Q4: entity-wise independence在NER中是否合理——相邻entity预测常相关。\"\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"bound仅解释3-12%的gap。共识: 可降级为analysis tool。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 R1-W1: bound仅捕获4.7-12.1%实际增益且无法预测负增益。交叉后两人共识: 在主文中明确讨论tightness而非仅Table 30 header标'weak'。\"\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"未直接提及。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: 与Yun et al. (2025) diversity collapse差异化需强化。两人交叉共识: §8/§9用3-4句明确区分。\"\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 未找到/元数据不匹配/orphan bib\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"hobelsberger2025systematic疑似虚构，17 orphan bib entries。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1 minor #1发现holm1979simple和xia2025survey orphan。R2引用验证: 51 bib, 49 cited, 2 orphan, 0 fake。较之前有改善(从17降至2)。\"\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 标注为descriptive diagnostic而非causal chain。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 R1-N2 [critical]: 因果语言('governs','explaining')与相关性证据不匹配。Figure 1标'not causal'但主体未贯彻。两人交叉强烈共识——需统一替换为相关性语言。\"\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: EL4NER, Self-Certainty BoN 等\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"EL4NER必须引用。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1建议补DeNero et al. 2009, Desai & Durrett 2020, Huang et al. 2024。R2建议补KDD 2025 survey, Aronica et al. 2024, test-time scaling survey。\"\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"Oracle Scaling figure 已生成并集成。\"\n    resolution_round: 26\n\n  # ===== Round 26 issues =====\n\n  - id: \"R26-N1\"\n    summary: \"N=8/16对test-time compute scaling研究范围过窄\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"建议至少补N=32或论证N=8的cost-efficiency。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及N range。\"\n\n  - id: \"R26-N2\"\n    summary: \"Trained verifier (LightGBM AUC=0.923) 负面结果scope有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R26-W1\"\n    summary: \"论文同时做4件事，每项深度不够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 R2 Excitement=2.5/5部分原因是novelty分散。\"\n\n  - id: \"R26-VIS1\"\n    summary: \"Page 7 display items严重过密（4表+1图）\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: p6-7 '略显拥挤但信息承载量高，适合实证论文'。降低严重性。\"\n\n  - id: \"R26-VIS2\"\n    summary: \"Figure 6 heatmap红绿色阶对色盲不友好\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: Figure 6 heatmap单色渐变(黄→深绿)，建议双色发散色板。\"\n\n  # ===== Round 27 新发现 =====\n\n  - id: \"R27-N1\"\n    summary: \"因果语言与相关性证据不匹配——Section 9 'governs'、Abstract 'explaining why'\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-N2 [critical]: Figure 1 caption标'not causal'但§9用'governs'，Abstract用'explaining where and why'，Intro用'fills this gap'。无干预实验验证因果方向。R2 AGREE with nuance(论文有准因果证据:MBR理论/条件分析/温度扫描，但仍需全文统一语言)。交叉后强烈共识。\"\n    action_items:\n      - round: 27\n        action: \"全文统一将因果动词替换为相关性语言('governs'→'is associated with','explaining'→'characterizing')。Discussion加段讨论因果推断局限。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R27-N2\"\n    summary: \"Holm-Bonferroni k=19(Abstract) vs Table 13实际21行——影响p_adj可复现性\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-N3 [critical]: Abstract 'selection family k=19'但Table 13 selection family有21项测试。差异2项未解释。若k=21则p_adj需重算。R2 AGREE。交叉共识: 需作者核实并修正。\"\n    action_items:\n      - round: 27\n        action: \"核实k=19 vs k=21来源。修正Abstract数字。在Appendix f提供完整Holm correction trace。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R27-W1\"\n    summary: \"7种方法分类边界模糊——diagnostic probes vs selection methods未区分\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"R1-W4: Abstract '7 methods'含diagnostic probes(ESJ/MRSC/LSC)和selection methods(DALS/SCD)混为一体。Het-T在Table 2无对应行。Table 2列9 categories与Abstract 7 methods不对齐。\"\n\n  - id: \"R27-W2\"\n    summary: \"RE分析受entity span error混淆(55.5% F1=0)——测量NER→RE错误传播而非RE本身\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W2+R2-W3: RE FEATURE-OF ρ≈0 vs HYPONYM-OF ρ=0.646。Table 3 RE列与NER并列但未标注混淆。两人交叉共识。\"\n\n  - id: \"R27-W3\"\n    summary: \"k=57全局Holm + RE/小配置样本量→统计功效不足，负面结论可能是power问题\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"R1-W3: RE n≈397时仅大效应量可检测。论文核心结论'no signal improves selection'可能反映insufficient power。需在Conclusion加hedge。R2 AGREE。\"\n\n  - id: \"R27-W4\"\n    summary: \"Entity construction +1.0-1.4pp at 8x cost——cost-effectiveness未在主文讨论\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W5+R2-N2: Table 61在Appendix p45但主文未引用。实践者是否值得8x推理成本换~1pp？R1建议Section 10直接address。R2降为should-fix(若其他问题修复)。\"\n\n  - id: \"R27-M1\"\n    summary: \"2个orphan bib entries: holm1979simple, xia2025survey\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1+R2独立发现。holm1979simple应补\\\\cite，xia2025survey若不引用应删除。\"\n\n  - id: \"R27-M2\"\n    summary: \"Figure 2 caption 'oracle gap'未自含定义\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R2-M2: 建议caption加'(oracle headroom = best-of-N F1 − greedy F1)'。R1 AGREE。\"\n\n  - id: \"R27-M3\"\n    summary: \"Limitations 未讨论closed-source API模型的degeneracy profile差异\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"R2-M5: 现有Limitations仅提LP signal不可用，未讨论degeneracy特征差异。R1 AGREE。\"\n\n  - id: \"R27-MR1\"\n    summary: \"缺失引用: DeNero 2009, Desai & Durrett 2020, Huang 2024, KDD 2025 survey, Aronica 2024\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1: DeNero et al. 2009(consensus decoding MT), Desai & Durrett 2020(calibration seq labeling), Huang et al. 2024(LLMs cannot self-correct)。R2: KDD 2025 UQ survey, Aronica et al. 2024(structured IE), test-time scaling survey 2025。交叉后部分AGREE——核心3篇(DeNero, Huang, Aronica)应补，surveys可选。\""
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
    "issues_yaml": "issues:\n  # ===== 历史 resolved issues (保留) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3-old\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-9 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"scope 声明在 Introduction 和 Limitations 中已存在。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"仅2个~8B fine-tuned + 1个72B zero-shot。缺closed-source模型。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R1 REBUT R2-W1(事实前提错误:论文已测72B+GPT-5.5)。R2确认事实错误但仍指出缺instruction-tuned vs base对比。共识:模型覆盖度合理但缺base model对比。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7）。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26视觉审查再次确认p7 display items过密。\"\n      - round: 27\n        reviewers: [2]\n        note: \"R27视觉审查: p6-7 display items密度高但可接受。Figure 1 部分面板文字偏小(约正文60-65%)。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 27\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"construction不应作为standalone contribution。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R2-N2列prescriptive gains为critical(+1.0-1.4pp at 8x cost)。R1降为should-fix(主贡献是诊断框架)。R1交叉回应: negative results有独立价值，prescriptive是contribution #4非primary。R2同意若修复其他问题可降级。\"\n    action_items:\n      - round: 26\n        action: \"确认construction在正文中已降级为diagnostic-motivated ablation而非contribution。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction（framing tautology）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 27\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 必须重构Abstract/Intro将structural/empirical二分法前置。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: Section 4明确区分了definitional vs empirical层面。R1-N2关注的是因果语言而非tautology本身。论文已有改善但主体仍用'governs'等因果动词。\"\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 27\n    resolution: \"R23: Reduced to 4 key numbers. R27 fresh: R2再次提出W4但R1 REBUT(empirical NLP论文惯例)。共识: 当前密度尚可接受。\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  # ===== Round 24 issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 公式删除，改为定性叙述。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"method.tex 加定义。\"\n    resolution_round: 24\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1 minor #2: 最高ρ为EM 0.472(LLaMA CoNLL)，'up to 0.45'略低。建议核实。\"\n\n  # ===== Round 25 issues =====\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"n=23 power 仅约 50% for ρ=0.4。结论过强。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及此 specific null finding。\"\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"cross-model仅1数据集1对模型。§5.3 SCD不再出现。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"'first systematic characterization'过强，应限定为'for NER'。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: 两位Reviewer独立列为consensus critical。R1-N1=R2-N1: 标题'Structured Generation'与NER-centric证据严重不匹配。RE仅1数据集(55.5% F1=0受span error混淆)，SQL仅n=196一句话。\"\n    action_items:\n      - round: 27\n        action: \"标题从'Structured Generation'缩窄为NER-specific或'Structured Information Extraction'。Abstract/Intro scope相应调整。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni；4 数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"CoNLL 增益为负 (−0.29pp)。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"p_adj矛盾(§1: 0.20 vs Table 13: 0.038)。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R2-N2 prescriptive gains边际(+1.0-1.4pp at 8x cost)。R1-W5同意事实但降为should-fix。交叉后共识: gains有限但对diagnostic论文可接受。\"\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"脚注9报告k=38但Table 13列k=57，差异k=19来源不明。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-N3 [critical]: Abstract k=19 vs Table 13实际21行。两位Reviewer交叉后共识需作者核实。\"\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"fine-tuning/scale/architecture混淆。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。Limitations已承认。\"\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"SciERC single-seed用于detailed diagnostic。bootstrap CI有缓解但不够。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh: 论文已改为3-seed(Few-NERD/CoNLL)。SciERC仍σ=0.48pp但已标注。\"\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"嵌套NER场景何时violated未讨论。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-Q4: entity-wise independence在NER中是否合理——相邻entity预测常相关。\"\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"bound仅解释3-12%的gap。共识: 可降级为analysis tool。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 R1-W1: bound仅捕获4.7-12.1%实际增益且无法预测负增益。交叉后两人共识: 在主文中明确讨论tightness而非仅Table 30 header标'weak'。\"\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"未直接提及。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: 与Yun et al. (2025) diversity collapse差异化需强化。两人交叉共识: §8/§9用3-4句明确区分。\"\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 未找到/元数据不匹配/orphan bib\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"hobelsberger2025systematic疑似虚构，17 orphan bib entries。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1 minor #1发现holm1979simple和xia2025survey orphan。R2引用验证: 51 bib, 49 cited, 2 orphan, 0 fake。较之前有改善(从17降至2)。\"\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 标注为descriptive diagnostic而非causal chain。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 R1-N2 [critical]: 因果语言('governs','explaining')与相关性证据不匹配。Figure 1标'not causal'但主体未贯彻。两人交叉强烈共识——需统一替换为相关性语言。\"\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: EL4NER, Self-Certainty BoN 等\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"EL4NER必须引用。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1建议补DeNero et al. 2009, Desai & Durrett 2020, Huang et al. 2024。R2建议补KDD 2025 survey, Aronica et al. 2024, test-time scaling survey。\"\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"Oracle Scaling figure 已生成并集成。\"\n    resolution_round: 26\n\n  # ===== Round 26 issues =====\n\n  - id: \"R26-N1\"\n    summary: \"N=8/16对test-time compute scaling研究范围过窄\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"建议至少补N=32或论证N=8的cost-efficiency。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及N range。\"\n\n  - id: \"R26-N2\"\n    summary: \"Trained verifier (LightGBM AUC=0.923) 负面结果scope有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R26-W1\"\n    summary: \"论文同时做4件事，每项深度不够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 R2 Excitement=2.5/5部分原因是novelty分散。\"\n\n  - id: \"R26-VIS1\"\n    summary: \"Page 7 display items严重过密（4表+1图）\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: p6-7 '略显拥挤但信息承载量高，适合实证论文'。降低严重性。\"\n\n  - id: \"R26-VIS2\"\n    summary: \"Figure 6 heatmap红绿色阶对色盲不友好\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: Figure 6 heatmap单色渐变(黄→深绿)，建议双色发散色板。\"\n\n  # ===== Round 27 新发现 =====\n\n  - id: \"R27-N1\"\n    summary: \"因果语言与相关性证据不匹配——Section 9 'governs'、Abstract 'explaining why'\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-N2 [critical]: Figure 1 caption标'not causal'但§9用'governs'，Abstract用'explaining where and why'，Intro用'fills this gap'。无干预实验验证因果方向。R2 AGREE with nuance(论文有准因果证据:MBR理论/条件分析/温度扫描，但仍需全文统一语言)。交叉后强烈共识。\"\n    action_items:\n      - round: 27\n        action: \"全文统一将因果动词替换为相关性语言('governs'→'is associated with','explaining'→'characterizing')。Discussion加段讨论因果推断局限。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R27-N2\"\n    summary: \"Holm-Bonferroni k=19(Abstract) vs Table 13实际21行——影响p_adj可复现性\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-N3 [critical]: Abstract 'selection family k=19'但Table 13 selection family有21项测试。差异2项未解释。若k=21则p_adj需重算。R2 AGREE。交叉共识: 需作者核实并修正。\"\n    action_items:\n      - round: 27\n        action: \"核实k=19 vs k=21来源。修正Abstract数字。在Appendix f提供完整Holm correction trace。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R27-W1\"\n    summary: \"7种方法分类边界模糊——diagnostic probes vs selection methods未区分\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"R1-W4: Abstract '7 methods'含diagnostic probes(ESJ/MRSC/LSC)和selection methods(DALS/SCD)混为一体。Het-T在Table 2无对应行。Table 2列9 categories与Abstract 7 methods不对齐。\"\n\n  - id: \"R27-W2\"\n    summary: \"RE分析受entity span error混淆(55.5% F1=0)——测量NER→RE错误传播而非RE本身\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W2+R2-W3: RE FEATURE-OF ρ≈0 vs HYPONYM-OF ρ=0.646。Table 3 RE列与NER并列但未标注混淆。两人交叉共识。\"\n\n  - id: \"R27-W3\"\n    summary: \"k=57全局Holm + RE/小配置样本量→统计功效不足，负面结论可能是power问题\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"R1-W3: RE n≈397时仅大效应量可检测。论文核心结论'no signal improves selection'可能反映insufficient power。需在Conclusion加hedge。R2 AGREE。\"\n\n  - id: \"R27-W4\"\n    summary: \"Entity construction +1.0-1.4pp at 8x cost——cost-effectiveness未在主文讨论\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W5+R2-N2: Table 61在Appendix p45但主文未引用。实践者是否值得8x推理成本换~1pp？R1建议Section 10直接address。R2降为should-fix(若其他问题修复)。\"\n\n  - id: \"R27-M1\"\n    summary: \"2个orphan bib entries: holm1979simple, xia2025survey\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1+R2独立发现。holm1979simple应补\\\\cite，xia2025survey若不引用应删除。\"\n\n  - id: \"R27-M2\"\n    summary: \"Figure 2 caption 'oracle gap'未自含定义\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R2-M2: 建议caption加'(oracle headroom = best-of-N F1 − greedy F1)'。R1 AGREE。\"\n\n  - id: \"R27-M3\"\n    summary: \"Limitations 未讨论closed-source API模型的degeneracy profile差异\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"R2-M5: 现有Limitations仅提LP signal不可用，未讨论degeneracy特征差异。R1 AGREE。\"\n\n  - id: \"R27-MR1\"\n    summary: \"缺失引用: DeNero 2009, Desai & Durrett 2020, Huang 2024, KDD 2025 survey, Aronica 2024\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1: DeNero et al. 2009(consensus decoding MT), Desai & Durrett 2020(calibration seq labeling), Huang et al. 2024(LLMs cannot self-correct)。R2: KDD 2025 UQ survey, Aronica et al. 2024(structured IE), test-time scaling survey 2025。交叉后部分AGREE——核心3篇(DeNero, Huang, Aronica)应补，surveys可选。\""
  }
}
```

</details>

---


### Tool result

_source line 2962 · 2026-05-21T11:42:51.779638+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 34142}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2963 · 2026-05-21T11:45:08.948220+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# 审稿报告 — Round 27 (Fresh Review)\n\n**论文**: \"The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Structured Generation\"\n**Venue**: EMNLP 2026 Main Conference (Long Paper, via ARR)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验充分性; R2: 新颖性+完整性+写作质量）\n**交叉分享**: 完成（R1→R2, R2→R1，逐条[AGREE]/[REBUT]回应）\n\n---\n\n## Summary\n\n本文调查 self-consistency (SC) 在结构化信息抽取（主要是 NER）中为何失败。核心发现是 \"correlation-selection gap\"：质量估计信号与 oracle F1 相关（ρ up to 0.45, AUROC up to 0.82），但无法选出比 greedy decoding 更好的样本。论文提出四阶段诊断级联（QE → degeneracy → agreement fidelity → LP compression）来定位失败机制，测试了 7 种 entity-level 方法（ESJ, MRSC, LSC, Het-T, ASB, SCD, supervised verifier），均未能弥合 gap。处方性结果包括 LP-weighted entity construction (+1.02–1.40pp on Few-NERD)、cross-model ensemble (+0.42pp) 和 regime-specific LP selection (+1.39pp on Few-NERD)。实验跨 4 个 NER 数据集、2 个模型族（Qwen/LLaMA）、4B–72B 规模和 GPT-5.5。\n\n---\n\n## Strengths\n\n**S1 [Consensus]** 四阶段诊断级联是论文最有价值的贡献。从质量估计到 degeneracy 到 agreement fidelity 到 LP compression 的递进式诊断结构，每个阶段都有对应的 metric 和实验验证。\n\n**S2 [Consensus]** NER 范围内的实验覆盖度堪称典范。4 个数据集（SciERC, Few-NERD, CoNLL-2003, WNUT-17）覆盖不同难度梯度；2 个模型族；4B–72B 规模范围；5 种信号；60+ 张表格。\n\n**S3 [Consensus]** 统计方法论严谨性远超同类论文。全局 Holm-Bonferroni 校正（k=57）、paired bootstrap tests（B=10,000）、bootstrap 95% CI、multi-seed 设计（3 seeds on key datasets）、post-hoc power analysis。\n\n**S4 [R1]** MBR 等价性证明（Proposition 1）将 entity construction 与 MBR decoding 联系，提供了概率论基础。\n\n**S5 [R1]** 三个独立诊断探针（ESJ, MRSC, LSC）从不同角度收敛到相同结论——entity-level self-verification 失败——构成 converging evidence。\n\n**S6 [R2]** ~35 页附录提供极高可追溯性。Table 62 与先前工作的差异化矩阵清晰。\n\n**S7 [Consensus]** 引用验证通过：51 bib entries, 49 cited, 2 orphan, 0 虚假引用。\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 个 critical，两位 Reviewer 完全共识）\n\n**C1 [CONSENSUS CRITICAL] 标题 \"Structured Generation\" 与实验范围严重不匹配**\n- R1-N1 + R2-N1 独立提出，交叉后完全一致\n- NER 有 4 数据集 × 2 模型族 × 60+ 表格。RE 仅 SciERC 1 个数据集（Appendix o），且 55.5% 实例因 entity span error 获 F1=0。SQL 仅 GPT-5.5 on Spider (n=196) 一句话描述，无详细表格。\n- RE 中 FEATURE-OF ρ≈0 vs HYPONYM-OF ρ=0.646，信号质量高度关系类型依赖\n- 建议: 标题和 Abstract 收窄为 NER-specific（如 \"Named Entity Recognition\" 或 \"Structured Information Extraction\"），RE/SQL 降为 \"preliminary observations\"\n\n**C2 [CONSENSUS CRITICAL] 因果语言与相关性证据不匹配**\n- R1-N2 提出，R2 AGREE with nuance\n- Figure 1 caption 正确标注 \"diagnostic sequence, not causal chain\"，但 Section 9 用 \"Degeneracy **governs** the selection gap\"，Abstract 用 \"**explaining** where and why\"，Introduction 用 \"fills this gap\"\n- 论文实际做的是相关性诊断（Spearman ρ, subgroup 对比, AUROC），无干预实验验证因果方向\n- R2 认为论文有准因果证据缓解（MBR 理论机制、非退化子集条件分析、温度扫描），但全文语言仍需统一\n- 建议: 全文替换因果动词为相关性语言；Discussion 加段讨论因果推断局限\n\n**C3 [CONSENSUS CRITICAL] Holm-Bonferroni k=19 (Abstract) vs Table 13 实际 21 行——影响核心统计声明可复现性**\n- R1-N3 提出，R2 AGREE\n- Abstract 声称 \"selection family k=19\"，但 Table 13 的 selection family 共 21 项测试，差异 2 项未解释\n- 直接影响 p_adj 计算和读者独立验证\n- 建议: 核实 k 值来源，修正 Abstract，在 Appendix f 提供完整 Holm correction trace\n\n### Should-Fix（7 个 warning）\n\n**W1 [Consensus]** Degeneracy bound 极松且被过度呈现。Table 30 显示 bound 仅捕获实际增益 4.7–12.1%，且无法预测负增益方向。Introduction 将其作为主要贡献之一呈现，但 bound 的实际预测能力有限。建议: 在主文讨论 tightness。\n\n**W2 [Consensus]** RE 分析被 entity span error 严重混淆。RE 本质上测量 NER→RE 错误传播而非 RE 本身的 SC 失败。Table 3 RE 列与 NER 并列但未充分标注混淆因素。建议: Section 7.6 首段明确声明。\n\n**W3 [R1, R2 AGREE]** k=57 全局 Holm + RE/小配置样本量导致统计功效不足。核心结论 \"no signal improves selection\" 在 RE 和小配置上可能反映 insufficient power 而非 true null。建议: Conclusion 加 hedge。\n\n**W4 [R1, R2 partially AGREE]** 7 种方法分类边界模糊。Abstract \"7 methods\" 含 diagnostic probes (ESJ/MRSC/LSC) 和 selection methods (DALS/SCD) 但未区分。Het-T 在 Table 2 无对应行。Table 2 列 9 categories 与 Abstract 7 methods 不对齐。\n\n**W5 [R2→R1 降级]** Prescriptive gains 边际化 (+1.0–1.4pp at 8× cost)。R2 列为 critical，R1 降为 should-fix——论文主贡献是诊断框架而非 prescriptive methods，negative results 有独立价值。交叉后共识: 保持 should-fix，建议在 Section 10 或 Discussion 直接 address cost-effectiveness。\n\n**W6 [R1, partially]** Entity-wise independence 假设（Proposition 1）未经验验证。相邻 entity 预测常相关，可能解释 bound 松散度。\n\n**W7 [Consensus]** 与 Yun et al. (2025) \"diversity collapse\" 差异化需强化。§8/§9 需 3–4 句明确区分。\n\n### Minor（8 个 info）\n\n- M1: 2 个 orphan bib entries（holm1979simple 应补 \\cite，xia2025survey 应删除）\n- M2: Figure 2 caption \"oracle gap\" 未自含定义\n- M3: \"VotConsLogProb\" 在 Figure 6 突然出现未正式定义\n- M4: Table 61 (cost-benefit) 在 Appendix p45 但主文未引用\n- M5: Abstract \"ρ up to 0.45\"——最高值为 EM 0.472 (LLaMA CoNLL)，建议核实\n- M6: Table 30 Ratio 列 \"—\" 含义未说明\n- M7: Limitations 未讨论 closed-source API 模型的 degeneracy profile 差异\n- M8: 附录 a–ag（33 个子附录）导航困难，建议增加 TOC\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成**完全共识**：\n\n1. **[AGREE] 标题-范围不匹配**（C1）：最高优先级修订。标题 \"Structured Generation\" 与 NER-centric 证据严重不匹配。\n2. **[AGREE] 因果语言不当**（C2）：全文因果动词需统一替换为相关性语言。\n3. **[AGREE] k 值不一致**（C3）：Abstract k=19 需核实修正。\n4. **[AGREE] 诊断框架是核心贡献**：四阶段级联设计精巧，NER 实验覆盖度典范。\n5. **[AGREE] 统计严谨性优秀**：Holm-Bonferroni + bootstrap + multi-seed 远超同类论文。\n6. **[AGREE] RE 混淆**（W2）：span error 使 RE 分析测量的是 NER 错误传播。\n7. **[AGREE] Prescriptive gains 有限但可接受**（W5）：对 diagnostic 论文，~1pp escape route 不需大效果量。\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分析 |\n|------|----|----|------|\n| Prescriptive gains 严重度 | Should-Fix (W5) | Critical (N2) | R1 论点更有说服力——论文主贡献是诊断框架，negative results 有独立价值。R2 同意若其他问题修复可降级。**采纳 R1: Should-Fix。** |\n| 论文结构 (§3–7 交织) | REBUT（diagnostic narrative 合理） | Critical (N3) | R1 引用 ACL/EMNLP 先例（Chen 2024a, Yun 2025）论证 interleaved 结构有据可循。论文的 hypothesis-driven diagnostic 叙事需要在方法中嵌入初步结果。**采纳 R1: 非缺陷，建议加 roadmap 句。** |\n| \"Capability ceiling\" 措辞 | REBUT（72B+GPT-5.5 已测） | W1（3B–8B 仅） | R2 事实前提有误——论文已测 4B→72B + GPT-5.5。R1 纠正有据。**R2 W1 撤销。** |\n| Abstract 信息密度 | REBUT（empirical NLP 惯例） | W4 | R1 引用同类论文先例。当前数字密度尚可接受。**采纳 R1: 非缺陷。** |\n| Related Work 后置 | REBUT（标准做法） | W5 | ACL/EMNLP 无硬性要求。概念依赖决定后置更合理。**采纳 R1: 非缺陷。** |\n| \"Inverse Scaling\" 标题 | REBUT（R2 误读） | M6 | 论文描述的确是 performance degradation with increased N，符合 inverse scaling 定义。**R2 M6 撤销。** |\n| 干预实验 (R1-Q3) | 要求 | REBUT（不可行） | R2 正确指出 degeneracy 是 emergent property，完全干预不可行。准因果证据链（MBR 理论/条件分析/温度扫描）部分缓解。**采纳 R2: 不要求正式干预，但需在 Discussion 讨论局限。** |\n\n---\n\n## Questions（需作者澄清）\n\n1. **k=19 vs k=21**: 请确认 Abstract \"selection family k=19\" 的来源。Table 13 有 21 行。\n2. **RE oracle entity spans**: 是否考虑过先用 oracle entity spans 隔离 RE-specific 的 SC 失败？\n3. **Degeneracy 因果方向**: 是否有任何证据（超出温度扫描）支持 degeneracy→selection failure 的因果方向？\n4. **Entity-wise independence**: Proposition 1 的 independence 假设在 NER 中是否合理？相邻 entity 预测常相关。\n5. **GPT-5.5 SQL MDE**: n=196 instances 能检测到的最小效应量是多少？\n\n---\n\n## Missing References\n\n两位 Reviewer 共同建议补充：\n1. **DeNero et al. (2009)** — consensus decoding in MT，与 entity construction 的 MBR 等价性直接相关\n2. **Huang et al. (2024)** — \"Large Language Models Cannot Self-Correct Reasoning Yet\"，self-verification 失败的相关讨论\n3. **Desai & Durrett (2020)** — calibration of pre-trained transformers for sequence labeling\n4. **Aronica et al. (2024)** — structured IE output improvement（如与 entity construction 方向相关）\n\n可选补充：\n5. KDD 2025 UQ & Calibration survey\n6. Test-time Scaling of LLMs survey (arXiv:2511.14772)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用（项目配置中 external_review.paperreview_ai.enabled 不存在）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（耗时 ~4 分钟）\n**结果**: 0 critical, 6 warning, 16 info\n\n主要 findings：\n- **[warning] Pages 1–2**: 前两页纯文本无 display item，第一个视觉锚点 Figure 1 在 page 3。建议提前或加 teaser figure。\n- **[warning] Page 8**: Section 8 (Related Work) + Section 9 (Discussion) 整页纯文本，与 pages 6–7 高密度形成反差。\n- **[warning] Page 17**: Figure 6 heatmap 单色渐变（黄→深绿），色盲读者可能难以区分。建议双色发散色板。\n- **[warning] Pages 40, 45, 46**: 附录表格后大面积空白（>2/3 页），可重新排列。\n- **[info]** 主文 8 页含 3 Figure + ~8 Table = 11 display items，密度充足。所有表格 booktabs 风格统一。无 margin 溢出、未解析引用或 LaTeX 错误。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | 综合评分 | 说明 |\n|------|---------|------|\n| Soundness | 3.5/5 | NER 诊断方法论扎实，但 claim scope 超出证据（RE/SQL），因果语言与证据不匹配，k 值不一致 |\n| Excitement | 2.5/5 | 负面结果有警示价值，诊断框架新颖，但 prescriptive gains 边际化，set-valued SC 失败非完全出人意料 |\n| Reproducibility | 4/5 | 附录极详尽，公开数据集，承诺代码释放 |\n\n**判断依据**:\n\nR1 给 3.5 (Borderline Conference), R2 给 3.0 (Findings)。三个 consensus critical 问题（标题 overclaiming、因果语言、k 值）中，C1 和 C2 是系统性问题——标题和全文的 scope 声明与证据不匹配，因果语言贯穿全文多处。这些不是局部修补可解决的，需要重新定位论文 scope 并统一语言。C3 是技术性问题但影响可复现性。\n\n论文在 NER 范围内的诊断深度和统计严谨性是其核心竞争力，足以达到 Findings 水平。但 \"Structured Generation\" 的宏大标题与 NER-centric 证据之间的 gap，以及 prescriptive results 的边际增益，限制了 Main Conference 的竞争力。\n\n**如果作者能修复**：(1) 标题收窄为 NER-specific，(2) 全文统一相关性语言，(3) 核实 k 值——评分可上调至 **3.5 (Borderline Conference)**。\n\n**Confidence: 4/5** — 两位 Reviewer 均仔细审读全文 46 页（含附录），对 NER/IE、SC 文献和统计方法熟悉。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度当前可接受（交叉后共识），但 \"ρ up to 0.45\" 需核实（最高 EM 0.472）\n- \"selection family k=19\" 需修正为实际值\n- \"structured generation\" scope 需收窄\n\n### Introduction (§1)\n- Contribution #1–#3 定位准确；Contribution #4 (prescriptive) 应降低 framing 强度\n- \"our diagnostic framework fills this gap\" → 应改为 \"characterizes\" 或 \"identifies\"\n- \"four failure modes explaining where and why\" → \"characterizing where and how\"\n\n### Diagnostic Framework (§2)\n- 方法论完善：5 信号定义清晰、evaluation protocol 明确\n- per-sample vs instance-level 区分是重要概念贡献\n\n### How Self-Verification Fails (§3)\n- ESJ/MRSC/LSC 三个探针的 converging evidence 是强项\n- Hidden-state probe (AUROC 0.63–0.88) 提供了 introspection boundary 的定量证据\n\n### Where Single-Signal Selection Fails (§4)\n- Definitional vs empirical 二分法处理得当\n- LP compression (median 0.041 nats) 是重要发现\n- Table 1 清晰展示 selection gap\n\n### Adaptive Methods (§5)\n- Table 2 方法总结有效\n- Cross-model SC (+0.42pp) 有趣但仅 1 数据集 1 模型对\n- Supervised verifier AUC=0.923 → +0.30pp 的 disconnect 是重要 negative result\n\n### Threshold Regime Analysis (§6)\n- MBR 等价性（Proposition 1）是 clean 的理论贡献\n- Degeneracy bound 松散需在主文讨论（W1）\n- Inverse scaling (40/58 transitions negative) 是值得注意的发现\n\n### Experiments (§7)\n- Setup 详尽；QE results (Table 3) 清晰\n- Few-NERD contrast (Table 4) 是最有说服力的实验\n- Entity construction (Table 5) 结果 dataset-dependent，CoNLL 负增益\n\n### Related Work (§8)\n- 后置位置合理（交叉后共识）\n- §8.1 与 Yun et al. 差异化需强化\n- 缺 DeNero 2009, Huang 2024 等引用\n\n### Discussion (§9)\n- \"Degeneracy governs\" 需改为相关性语言\n- 实用建议（construction when D<22%）有价值但应标注为 empirical pattern\n\n### Conclusion (§10)\n- 简洁有效\n- 缺 cost-effectiveness 讨论（Table 61 应在此引用）\n\n### Limitations\n- 覆盖面合理，长度符合 EMNLP 规范\n- 缺 closed-source API degeneracy profile 讨论\n\n### Appendix\n- 60+ 表格极详尽，可追溯性高\n- 导航困难（a–ag），建议加 TOC",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
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
    "project": "struct_self_consist_ie",
    "report": "# 审稿报告 — Round 27 (Fresh Review)\n\n**论文**: \"The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Structured Generation\"\n**Venue**: EMNLP 2026 Main Conference (Long Paper, via ARR)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验充分性; R2: 新颖性+完整性+写作质量）\n**交叉分享**: 完成（R1→R2, R2→R1，逐条[AGREE]/[REBUT]回应）\n\n---\n\n## Summary\n\n本文调查 self-consistency (SC) 在结构化信息抽取（主要是 NER）中为何失败。核心发现是 \"correlation-selection gap\"：质量估计信号与 oracle F1 相关（ρ up to 0.45, AUROC up to 0.82），但无法选出比 greedy decoding 更好的样本。论文提出四阶段诊断级联（QE → degeneracy → agreement fidelity → LP compression）来定位失败机制，测试了 7 种 entity-level 方法（ESJ, MRSC, LSC, Het-T, ASB, SCD, supervised verifier），均未能弥合 gap。处方性结果包括 LP-weighted entity construction (+1.02–1.40pp on Few-NERD)、cross-model ensemble (+0.42pp) 和 regime-specific LP selection (+1.39pp on Few-NERD)。实验跨 4 个 NER 数据集、2 个模型族（Qwen/LLaMA）、4B–72B 规模和 GPT-5.5。\n\n---\n\n## Strengths\n\n**S1 [Consensus]** 四阶段诊断级联是论文最有价值的贡献。从质量估计到 degeneracy 到 agreement fidelity 到 LP compression 的递进式诊断结构，每个阶段都有对应的 metric 和实验验证。\n\n**S2 [Consensus]** NER 范围内的实验覆盖度堪称典范。4 个数据集（SciERC, Few-NERD, CoNLL-2003, WNUT-17）覆盖不同难度梯度；2 个模型族；4B–72B 规模范围；5 种信号；60+ 张表格。\n\n**S3 [Consensus]** 统计方法论严谨性远超同类论文。全局 Holm-Bonferroni 校正（k=57）、paired bootstrap tests（B=10,000）、bootstrap 95% CI、multi-seed 设计（3 seeds on key datasets）、post-hoc power analysis。\n\n**S4 [R1]** MBR 等价性证明（Proposition 1）将 entity construction 与 MBR decoding 联系，提供了概率论基础。\n\n**S5 [R1]** 三个独立诊断探针（ESJ, MRSC, LSC）从不同角度收敛到相同结论——entity-level self-verification 失败——构成 converging evidence。\n\n**S6 [R2]** ~35 页附录提供极高可追溯性。Table 62 与先前工作的差异化矩阵清晰。\n\n**S7 [Consensus]** 引用验证通过：51 bib entries, 49 cited, 2 orphan, 0 虚假引用。\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 个 critical，两位 Reviewer 完全共识）\n\n**C1 [CONSENSUS CRITICAL] 标题 \"Structured Generation\" 与实验范围严重不匹配**\n- R1-N1 + R2-N1 独立提出，交叉后完全一致\n- NER 有 4 数据集 × 2 模型族 × 60+ 表格。RE 仅 SciERC 1 个数据集（Appendix o），且 55.5% 实例因 entity span error 获 F1=0。SQL 仅 GPT-5.5 on Spider (n=196) 一句话描述，无详细表格。\n- RE 中 FEATURE-OF ρ≈0 vs HYPONYM-OF ρ=0.646，信号质量高度关系类型依赖\n- 建议: 标题和 Abstract 收窄为 NER-specific（如 \"Named Entity Recognition\" 或 \"Structured Information Extraction\"），RE/SQL 降为 \"preliminary observations\"\n\n**C2 [CONSENSUS CRITICAL] 因果语言与相关性证据不匹配**\n- R1-N2 提出，R2 AGREE with nuance\n- Figure 1 caption 正确标注 \"diagnostic sequence, not causal chain\"，但 Section 9 用 \"Degeneracy **governs** the selection gap\"，Abstract 用 \"**explaining** where and why\"，Introduction 用 \"fills this gap\"\n- 论文实际做的是相关性诊断（Spearman ρ, subgroup 对比, AUROC），无干预实验验证因果方向\n- R2 认为论文有准因果证据缓解（MBR 理论机制、非退化子集条件分析、温度扫描），但全文语言仍需统一\n- 建议: 全文替换因果动词为相关性语言；Discussion 加段讨论因果推断局限\n\n**C3 [CONSENSUS CRITICAL] Holm-Bonferroni k=19 (Abstract) vs Table 13 实际 21 行——影响核心统计声明可复现性**\n- R1-N3 提出，R2 AGREE\n- Abstract 声称 \"selection family k=19\"，但 Table 13 的 selection family 共 21 项测试，差异 2 项未解释\n- 直接影响 p_adj 计算和读者独立验证\n- 建议: 核实 k 值来源，修正 Abstract，在 Appendix f 提供完整 Holm correction trace\n\n### Should-Fix（7 个 warning）\n\n**W1 [Consensus]** Degeneracy bound 极松且被过度呈现。Table 30 显示 bound 仅捕获实际增益 4.7–12.1%，且无法预测负增益方向。Introduction 将其作为主要贡献之一呈现，但 bound 的实际预测能力有限。建议: 在主文讨论 tightness。\n\n**W2 [Consensus]** RE 分析被 entity span error 严重混淆。RE 本质上测量 NER→RE 错误传播而非 RE 本身的 SC 失败。Table 3 RE 列与 NER 并列但未充分标注混淆因素。建议: Section 7.6 首段明确声明。\n\n**W3 [R1, R2 AGREE]** k=57 全局 Holm + RE/小配置样本量导致统计功效不足。核心结论 \"no signal improves selection\" 在 RE 和小配置上可能反映 insufficient power 而非 true null。建议: Conclusion 加 hedge。\n\n**W4 [R1, R2 partially AGREE]** 7 种方法分类边界模糊。Abstract \"7 methods\" 含 diagnostic probes (ESJ/MRSC/LSC) 和 selection methods (DALS/SCD) 但未区分。Het-T 在 Table 2 无对应行。Table 2 列 9 categories 与 Abstract 7 methods 不对齐。\n\n**W5 [R2→R1 降级]** Prescriptive gains 边际化 (+1.0–1.4pp at 8× cost)。R2 列为 critical，R1 降为 should-fix——论文主贡献是诊断框架而非 prescriptive methods，negative results 有独立价值。交叉后共识: 保持 should-fix，建议在 Section 10 或 Discussion 直接 address cost-effectiveness。\n\n**W6 [R1, partially]** Entity-wise independence 假设（Proposition 1）未经验验证。相邻 entity 预测常相关，可能解释 bound 松散度。\n\n**W7 [Consensus]** 与 Yun et al. (2025) \"diversity collapse\" 差异化需强化。§8/§9 需 3–4 句明确区分。\n\n### Minor（8 个 info）\n\n- M1: 2 个 orphan bib entries（holm1979simple 应补 \\cite，xia2025survey 应删除）\n- M2: Figure 2 caption \"oracle gap\" 未自含定义\n- M3: \"VotConsLogProb\" 在 Figure 6 突然出现未正式定义\n- M4: Table 61 (cost-benefit) 在 Appendix p45 但主文未引用\n- M5: Abstract \"ρ up to 0.45\"——最高值为 EM 0.472 (LLaMA CoNLL)，建议核实\n- M6: Table 30 Ratio 列 \"—\" 含义未说明\n- M7: Limitations 未讨论 closed-source API 模型的 degeneracy profile 差异\n- M8: 附录 a–ag（33 个子附录）导航困难，建议增加 TOC\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成**完全共识**：\n\n1. **[AGREE] 标题-范围不匹配**（C1）：最高优先级修订。标题 \"Structured Generation\" 与 NER-centric 证据严重不匹配。\n2. **[AGREE] 因果语言不当**（C2）：全文因果动词需统一替换为相关性语言。\n3. **[AGREE] k 值不一致**（C3）：Abstract k=19 需核实修正。\n4. **[AGREE] 诊断框架是核心贡献**：四阶段级联设计精巧，NER 实验覆盖度典范。\n5. **[AGREE] 统计严谨性优秀**：Holm-Bonferroni + bootstrap + multi-seed 远超同类论文。\n6. **[AGREE] RE 混淆**（W2）：span error 使 RE 分析测量的是 NER 错误传播。\n7. **[AGREE] Prescriptive gains 有限但可接受**（W5）：对 diagnostic 论文，~1pp escape route 不需大效果量。\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分析 |\n|------|----|----|------|\n| Prescriptive gains 严重度 | Should-Fix (W5) | Critical (N2) | R1 论点更有说服力——论文主贡献是诊断框架，negative results 有独立价值。R2 同意若其他问题修复可降级。**采纳 R1: Should-Fix。** |\n| 论文结构 (§3–7 交织) | REBUT（diagnostic narrative 合理） | Critical (N3) | R1 引用 ACL/EMNLP 先例（Chen 2024a, Yun 2025）论证 interleaved 结构有据可循。论文的 hypothesis-driven diagnostic 叙事需要在方法中嵌入初步结果。**采纳 R1: 非缺陷，建议加 roadmap 句。** |\n| \"Capability ceiling\" 措辞 | REBUT（72B+GPT-5.5 已测） | W1（3B–8B 仅） | R2 事实前提有误——论文已测 4B→72B + GPT-5.5。R1 纠正有据。**R2 W1 撤销。** |\n| Abstract 信息密度 | REBUT（empirical NLP 惯例） | W4 | R1 引用同类论文先例。当前数字密度尚可接受。**采纳 R1: 非缺陷。** |\n| Related Work 后置 | REBUT（标准做法） | W5 | ACL/EMNLP 无硬性要求。概念依赖决定后置更合理。**采纳 R1: 非缺陷。** |\n| \"Inverse Scaling\" 标题 | REBUT（R2 误读） | M6 | 论文描述的确是 performance degradation with increased N，符合 inverse scaling 定义。**R2 M6 撤销。** |\n| 干预实验 (R1-Q3) | 要求 | REBUT（不可行） | R2 正确指出 degeneracy 是 emergent property，完全干预不可行。准因果证据链（MBR 理论/条件分析/温度扫描）部分缓解。**采纳 R2: 不要求正式干预，但需在 Discussion 讨论局限。** |\n\n---\n\n## Questions（需作者澄清）\n\n1. **k=19 vs k=21**: 请确认 Abstract \"selection family k=19\" 的来源。Table 13 有 21 行。\n2. **RE oracle entity spans**: 是否考虑过先用 oracle entity spans 隔离 RE-specific 的 SC 失败？\n3. **Degeneracy 因果方向**: 是否有任何证据（超出温度扫描）支持 degeneracy→selection failure 的因果方向？\n4. **Entity-wise independence**: Proposition 1 的 independence 假设在 NER 中是否合理？相邻 entity 预测常相关。\n5. **GPT-5.5 SQL MDE**: n=196 instances 能检测到的最小效应量是多少？\n\n---\n\n## Missing References\n\n两位 Reviewer 共同建议补充：\n1. **DeNero et al. (2009)** — consensus decoding in MT，与 entity construction 的 MBR 等价性直接相关\n2. **Huang et al. (2024)** — \"Large Language Models Cannot Self-Correct Reasoning Yet\"，self-verification 失败的相关讨论\n3. **Desai & Durrett (2020)** — calibration of pre-trained transformers for sequence labeling\n4. **Aronica et al. (2024)** — structured IE output improvement（如与 entity construction 方向相关）\n\n可选补充：\n5. KDD 2025 UQ & Calibration survey\n6. Test-time Scaling of LLMs survey (arXiv:2511.14772)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用（项目配置中 external_review.paperreview_ai.enabled 不存在）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（耗时 ~4 分钟）\n**结果**: 0 critical, 6 warning, 16 info\n\n主要 findings：\n- **[warning] Pages 1–2**: 前两页纯文本无 display item，第一个视觉锚点 Figure 1 在 page 3。建议提前或加 teaser figure。\n- **[warning] Page 8**: Section 8 (Related Work) + Section 9 (Discussion) 整页纯文本，与 pages 6–7 高密度形成反差。\n- **[warning] Page 17**: Figure 6 heatmap 单色渐变（黄→深绿），色盲读者可能难以区分。建议双色发散色板。\n- **[warning] Pages 40, 45, 46**: 附录表格后大面积空白（>2/3 页），可重新排列。\n- **[info]** 主文 8 页含 3 Figure + ~8 Table = 11 display items，密度充足。所有表格 booktabs 风格统一。无 margin 溢出、未解析引用或 LaTeX 错误。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | 综合评分 | 说明 |\n|------|---------|------|\n| Soundness | 3.5/5 | NER 诊断方法论扎实，但 claim scope 超出证据（RE/SQL），因果语言与证据不匹配，k 值不一致 |\n| Excitement | 2.5/5 | 负面结果有警示价值，诊断框架新颖，但 prescriptive gains 边际化，set-valued SC 失败非完全出人意料 |\n| Reproducibility | 4/5 | 附录极详尽，公开数据集，承诺代码释放 |\n\n**判断依据**:\n\nR1 给 3.5 (Borderline Conference), R2 给 3.0 (Findings)。三个 consensus critical 问题（标题 overclaiming、因果语言、k 值）中，C1 和 C2 是系统性问题——标题和全文的 scope 声明与证据不匹配，因果语言贯穿全文多处。这些不是局部修补可解决的，需要重新定位论文 scope 并统一语言。C3 是技术性问题但影响可复现性。\n\n论文在 NER 范围内的诊断深度和统计严谨性是其核心竞争力，足以达到 Findings 水平。但 \"Structured Generation\" 的宏大标题与 NER-centric 证据之间的 gap，以及 prescriptive results 的边际增益，限制了 Main Conference 的竞争力。\n\n**如果作者能修复**：(1) 标题收窄为 NER-specific，(2) 全文统一相关性语言，(3) 核实 k 值——评分可上调至 **3.5 (Borderline Conference)**。\n\n**Confidence: 4/5** — 两位 Reviewer 均仔细审读全文 46 页（含附录），对 NER/IE、SC 文献和统计方法熟悉。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度当前可接受（交叉后共识），但 \"ρ up to 0.45\" 需核实（最高 EM 0.472）\n- \"selection family k=19\" 需修正为实际值\n- \"structured generation\" scope 需收窄\n\n### Introduction (§1)\n- Contribution #1–#3 定位准确；Contribution #4 (prescriptive) 应降低 framing 强度\n- \"our diagnostic framework fills this gap\" → 应改为 \"characterizes\" 或 \"identifies\"\n- \"four failure modes explaining where and why\" → \"characterizing where and how\"\n\n### Diagnostic Framework (§2)\n- 方法论完善：5 信号定义清晰、evaluation protocol 明确\n- per-sample vs instance-level 区分是重要概念贡献\n\n### How Self-Verification Fails (§3)\n- ESJ/MRSC/LSC 三个探针的 converging evidence 是强项\n- Hidden-state probe (AUROC 0.63–0.88) 提供了 introspection boundary 的定量证据\n\n### Where Single-Signal Selection Fails (§4)\n- Definitional vs empirical 二分法处理得当\n- LP compression (median 0.041 nats) 是重要发现\n- Table 1 清晰展示 selection gap\n\n### Adaptive Methods (§5)\n- Table 2 方法总结有效\n- Cross-model SC (+0.42pp) 有趣但仅 1 数据集 1 模型对\n- Supervised verifier AUC=0.923 → +0.30pp 的 disconnect 是重要 negative result\n\n### Threshold Regime Analysis (§6)\n- MBR 等价性（Proposition 1）是 clean 的理论贡献\n- Degeneracy bound 松散需在主文讨论（W1）\n- Inverse scaling (40/58 transitions negative) 是值得注意的发现\n\n### Experiments (§7)\n- Setup 详尽；QE results (Table 3) 清晰\n- Few-NERD contrast (Table 4) 是最有说服力的实验\n- Entity construction (Table 5) 结果 dataset-dependent，CoNLL 负增益\n\n### Related Work (§8)\n- 后置位置合理（交叉后共识）\n- §8.1 与 Yun et al. 差异化需强化\n- 缺 DeNero 2009, Huang 2024 等引用\n\n### Discussion (§9)\n- \"Degeneracy governs\" 需改为相关性语言\n- 实用建议（construction when D<22%）有价值但应标注为 empirical pattern\n\n### Conclusion (§10)\n- 简洁有效\n- 缺 cost-effectiveness 讨论（Table 61 应在此引用）\n\n### Limitations\n- 覆盖面合理，长度符合 EMNLP 规范\n- 缺 closed-source API degeneracy profile 讨论\n\n### Appendix\n- 60+ 表格极详尽，可追溯性高\n- 导航困难（a–ag），建议加 TOC",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 2964 · 2026-05-21T11:45:13.214507+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4266
}
```

</details>

---


### Assistant

_source line 2965 · 2026-05-21T11:45:21.939492+00:00_

审稿报告已投递至 Research Director。

**Round 27 审稿完成**。核心结论：

**Overall: 3.0 (Findings)**

三个 Consensus Critical：
1. **标题 "Structured Generation" 与 NER-centric 证据严重不匹配**——RE 仅 1 数据集且受 span error 混淆，SQL 仅 n=196 一句话
2. **因果语言与相关性证据不匹配**——"governs"、"explaining why" 等因果动词贯穿全文，但实验仅为相关性诊断
3. **Holm k=19 vs Table 13 k=21 不一致**——影响核心统计声明可复现性

主要优势：诊断框架设计精巧、NER 实验覆盖度典范、统计方法论严谨（Holm k=57, bootstrap, multi-seed）。

**升级路径**：修复标题 scope、统一语言、核实 k 值后可达 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 225

## Round 225

80 recorded events


### User

_source line 2966 · 2026-05-21T12:25:27.820263+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
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

_source line 2967 · 2026-05-21T12:25:34.660450+00:00_

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

_source line 2968 · 2026-05-21T12:25:34.711408+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2969 · 2026-05-21T12:25:40.225206+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
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
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2970 · 2026-05-21T12:25:40.225646+00:00_

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

_source line 2971 · 2026-05-21T12:25:43.892964+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2972 · 2026-05-21T12:25:43.943705+00:00_



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

_source line 2973 · 2026-05-21T12:25:47.757864+00:00_

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

_source line 2974 · 2026-05-21T12:25:49.164210+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (280 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_scierc_n16_s42 | SciERC N=16 seed=42: tests whether doubling samples from N=8 to N=16 on SciERC increases oracle headroom and whether MV aggregation gap widens. SciERC has lowest base F1 (~0.66) and moderate degeneracy (~12%), so additional samples may provide more diverse entity candidates for MV to select from. | — | — | — |\n| exp_fewnerd_n16_s123 | FewNERD N=16 seed=123: second seed for N=16 scaling analysis. Tests whether doubling samples from N=8 to N=16 increases oracle headroom consistently across seeds, and whether MV aggregation gap widens or narrows. | — | — | — |\n| exp_fewnerd_n16_s42_v2 | FewNERD N=16 scaling: doubling sample count from N=8 to N=16 increases oracle headroom and tests whether additional samples improve MV aggregation or only expand the correlation-selection gap. | — | — | — |\n\n## 待处理\n- exp_fewnerd_mf4_s456: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=456 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.（排队等待 GPU）\n- exp_fewnerd_mf4_s123: MF4 pipeline fix: F
…[truncated 1744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 2975 · 2026-05-21T12:25:49.164573+00:00_

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

_source line 2976 · 2026-05-21T12:25:49.465982+00:00_

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
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{The Capability Ceiling of Self-Consistency:\\ How Entity-Level Self-Verification Fails in Named Entity Recognition}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/diagnostic}
38	\input{sections/mechanistic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/background}
44	\input{sections/discussion}
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\section*{Ethics Statement}
51	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
52	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
53	No new human data was collected or annotated for this study.
54	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
55	Code and data will be released upon acceptance at [anonymized URL].
56	
57	\section*{Responsible NLP Research Checklist}
58	\in
…[truncated 186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2977 · 2026-05-21T12:25:49.516686+00:00_

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

_source line 2978 · 2026-05-21T12:25:49.567321+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

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

_source line 2979 · 2026-05-21T12:25:55.447240+00:00_

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

_source line 2980 · 2026-05-21T12:25:55.547800+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2981 · 2026-05-21T12:25:58.911194+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 2982 · 2026-05-21T12:25:59.916933+00:00_

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

_source line 2983 · 2026-05-21T12:26:00.370248+00:00_

1	\begin{abstract}
2	Test-time compute scaling through repeated sampling yields large gains on discrete-answer reasoning and code generation, yet for named entity recognition (NER), where outputs are entity sets with partial overlap, a persistent gap separates quality estimation from sample selection.
3	We ask whether entity-level agreement signals can bridge this gap.
4	Across nine method categories spanning diagnostic probes, selection/construction strategies, and learning-based approaches, we find that no entity-level agreement signal reliably improves selection.
5	Quality estimation signals correlate with oracle F1 ($\rho$ up to 0.47, AUROC up to 0.82) yet no signal selects better than greedy decoding.
6	The failure is systematic: a four-stage diagnostic cascade (quality estimation $\to$ degeneracy $\to$ agreement fidelity $\to$ log-probability compression) localizes where and how selection breaks down, with cross-task validation on RE and SQL parsing (87.2\% output degeneracy).
7	A hidden-state linear probe achieves entity-level discrimination (area under the ROC curve [AUROC] $0.63$\textendash$0.88$, dataset-dependent) from a single forward pass, consistently exceeding prompt-based self-evaluation (AUROC 0.51) but matching multi-sample agreement ($0.87$) only on the simplest task.
8	These negative results delineate where self-consistency (SC) does succeed for IE: through paths that bypass entity-level agreement.
9	Log-probability selection improves F1 by $+1.39$\,pp on Few-NERD (Holm-adjusted $p{=}0.021$, selection family $k{=}21$), entity-level construction via weighted voting gains $+1.02$\textendash$1.40$\,pp, and cross-model ensembles add $+0.42$\,pp on Few-NERD.
10	Each exploits sequence-level or cross-model signals rather than entity-level self-verification.
11	A degeneracy decomposition confirms SC gain vanishes once output degeneracy exceeds 70\%.
12	\end{abstract}
13	%% REFRAME: scope precision + empirical exhaustion methodology
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2984 · 2026-05-21T12:26:00.370685+00:00_

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

_source line 2985 · 2026-05-21T12:26:00.825500+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling complements model scaling \cite{snell2025scaling}: repeated sampling with majority voting \cite{wang2023selfconsistency}, best-of-$N$ with learned verifiers \cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \cite{muennighoff2025s1} produce large gains on reasoning and code generation.
4	These successes share a structural prerequisite: the output space admits either exact equivalence classes (multiple-choice, numeric answers) or execution-based verification (code).
5	Named entity recognition (NER) breaks both assumptions.
6	The output is a set of typed entities; two samples from the same input routinely extract overlapping but non-identical sets, and no external oracle can adjudicate correctness at test time.
7	Without equivalence classes, majority voting reduces to heuristic frequency counting; without a verifier, best-of-$N$ requires a reliable proxy signal.
8	This structural mismatch raises a concrete question: can self-consistency signals that estimate quality well for reasoning tasks also \textit{select} better outputs or \textit{construct} better entity sets for NER?
9	We investigate this question for NER and validate the core findings on SQL parsing, treating NER as a representative instance of the broader set-valued generation problem.
10	
11	The question has practical stakes beyond information extraction.
12	Hallucination detection methods such as SelfCheckGPT \cite{manakul2023selfcheckgpt} and FActScore \cite{min2023factscore} rely on cross-sample consistency to verify individual claims: if a model's outputs agree, the shared content is presumed factual.
13	This reasoning assumes entity-level self-verification works, that a model can reliably distinguish correct extractions from incorrect ones through self-judgment or re-prompting.
14	We show this assumption fails.
15	Three independent probes (entity self-judgment, multi-round re-prompting, latent-space 
…[truncated 4688 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 2986 · 2026-05-21T12:26:00.825952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 2987 · 2026-05-21T12:26:01.333710+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
8	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
9	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
10	
11	\subsection{Confidence Signals}\label{sec:signals}
12	
13	Entity matching uses exact span and type match.
14	We evaluate four \textit{consistency signals}---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal}, per-sample signal.
15	
16	\paragraph{Log-probability (per-sample).}
17	$c_{\text{lp}}(y_i) = |y_i|^{-1} \sum_{j} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)$.
18	
19	\paragraph{Soft Jaccard (structural, instance-level).}
20	For samples $y_i, y_j$, we group by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU):
21	\begin{equation}\label{eq:sj}
22	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
23	\end{equation}
24	Instance-level QE averages over all pairs: $c_{\text{sj}}(x) = \binom{N}{2}^{-1} \sum_{i<j} \text{SJ}(y_i, y_
…[truncated 1482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 2988 · 2026-05-21T12:26:01.334235+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
  }
}
```

</details>

---


### Tool result

_source line 2989 · 2026-05-21T12:26:01.687028+00:00_

1	\section{How Self-Verification Fails}\label{sec:mechanistic}
2	
3	The diagnostic cascade (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
4	We evaluate self-verification and diagnostic probes on Qwen2.5-7B (a separate model family from the primary Qwen3-8B) fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Appendix~\ref{app:self_verification}).
5	
6	\paragraph{Entity Self-Judgment (ESJ).}
7	For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
8	Entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.
9	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$).
10	
11	\paragraph{Multi-Round Self-Consistency (MRSC).}
12	Re-prompting on disputed entities (agreement ${<}0.6$) with focused verification yields P(yes) separation of $0.0006$ between gold and non-gold entities ($0.5003$ vs.\ $0.4997$).
13	MRSC best F1 ($0.763$) falls below greedy.
14	
15	\paragraph{Latent Self-Consistency (LSC).}
16	Mean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.
17	Centroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms majority vote ($0.792$) but does not close the oracle gap ($0.882$).
18	
19	\paragraph{Hidden-state probe.}
20	A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
21	All three exceed ESJ ($0.51$); only CoNLL approaches frequency agreement ($0.868$).
22	Cross-dataset transfer is weak: leave-one-dataset-out AUROC drops to $0.559$ (Few-NERD${\to}$C
…[truncated 875 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2990 · 2026-05-21T12:26:01.742287+00:00_

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

_source line 2991 · 2026-05-21T12:26:01.792871+00:00_

No matching deferred tools found

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


### Tool result

_source line 2992 · 2026-05-21T12:26:06.249729+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 call for papers:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. In addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel lingui
…[truncated 1067 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7338
}
```

</details>

---


### Tool call

_source line 2993 · 2026-05-21T12:26:13.727285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 2994 · 2026-05-21T12:26:14.129014+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK           & $0.646 \pm 0.001$ & .79 \\
24	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
25	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
26	\midrule
27	Random       & $0.610 \pm 0.003$ & --- \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32
…[truncated 2066 chars]

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

_source line 2995 · 2026-05-21T12:26:14.129473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 2996 · 2026-05-21T12:26:14.881898+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield an unconditional positive result.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond the seven verification methods in \S\ref{sec:mechanistic}--\S\ref{sec:adaptive}). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & \ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & \ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & \ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally distinct models can partially bypass within-model degeneracy.
33	Combining 4 samples each from Qwen3-8B and
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 2997 · 2026-05-21T12:26:14.982914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 2998 · 2026-05-21T12:26:14.983553+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Following the MBR framework (Appendix~\ref{app:mbr_proof}), entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers the majority-vote threshold $\hat{p}(e) > \tfrac{1}{2}$ used throughout (Proposition~\ref{prop:construction_mbr}; empirical validation: Table~\ref{tab:entity_construction}).
6	Thus majority vote is MBR decoding under set-overlap utility.
7	Signal-derived weights $w_i$ yield quality-weighted MBR (LP-weighted construction): $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$.
8	Weighted MBR improves when $w_i$ correlates with $u(y_i, y^*)$ within instances; when this correlation is weak (LP on SciERC: $\rho{\approx}0.2$; few-shot: \S\ref{sec:scaling}), weighting degrades (\S\ref{sec:prescriptive}).
9	
10	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
11	
12	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; empirical fit in Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, while SciERC converges more slowly ($c{\approx}0.35$).
13	The ceiling grows, but confidence-based aggregation recovers ${<}1$\,pp---a persistent aggregation gap.
14	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{10.1\% of GPT-5.5 samples produced unparseable output; these are excluded from all metrics. See Appendix~\ref{app:frontier_sc}.}
15	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen
…[truncated 3131 chars]

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

_source line 2999 · 2026-05-21T12:26:15.385243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3000 · 2026-05-21T12:26:15.888170+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N{=}16$ for scaling (Appendix~\ref{app:n_scaling}).
15	
16	%% ============================================================
17	\subsection{Quality Estimation Results}\label{sec:qe_results}
18	
19	\begin{table*}[t]
20	\centering
21	\small
22	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
23	\label{tab:quality_estimation}
24	\begin{tabular}{ll cc cc cc}
25	\toprule
26	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
27	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}

…[truncated 6893 chars]

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

_source line 3001 · 2026-05-21T12:26:15.888615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 3002 · 2026-05-21T12:26:15.888924+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, adaptive allocation \cite{aggarwal2023adaptive}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} all target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes and fine-grained variants.}
8	\citet{chen2023twofailures} identify SC failures where consistent outputs are systematically wrong; \citet{huang2024large} show LLMs cannot self-correct reasoning without external feedback. Our correlation-selection gap is a distinct failure where signals \textit{correlate} with quality yet fail to \textit{select}.
9	\citet{chen2024usc} extend SC to free-form tasks; our diagnostic shows such extensions face limits under constrained decoding (\S\ref{sec:selection_gap}). \citet{thirukovalluru2024atomic} decompose claims atomically; our entity-level decomposition reveals sub-output agreement does not translate to selection gain.
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{yao2026consistency} show consistency correlates with NER/RE accuracy; we diagnose degeneracy and LP compression as mechanisms that prevent this correlation from yielding selection gains.
13	\citet{xie2023zeroshot} propose entity voting for zero-shot NER and \citet{li2024simple} improve structured output formatting; our approach diagnoses why entity-level agreement fails to improve selection, building on generative IE \cite{zhou2024uniner, sainz2024gollie} and constrained decoding \cite{willard2023guided, dong2024xgrammar}.
14	
15	\paragraph{Uncertainty estimation and MBR.}
16	Our selection instantiates MBR decoding \cite{eik
…[truncated 1152 chars]

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

_source line 3003 · 2026-05-21T12:26:16.440862+00:00_

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

_source line 3004 · 2026-05-21T12:26:17.445063+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	NER exhibits oracle scaling ($c{\approx}0.5$; \S\ref{sec:scaling}), but degeneracy (17.8--67.9\%) and LP-quality alignment ($\rho$ 0.043--0.667) constrain aggregation; temperature disentangles these at $T{=}1.2$ (Table~\ref{tab:t_degeneracy}).
4	
5	\paragraph{Degeneracy correlates with the selection gap across model families.}
6	Across four frontier models on Few-NERD, degeneracy and the selection gap (oracle${-}$MV) are negatively correlated (5.5--74\% degen $\to$ 0.290--0.032 gap; Table~\ref{tab:frontier_sc_cross}), consistent with the degeneracy bound (\S\ref{sec:theory}) being structural rather than model-specific.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms at zero marginal cost, with gains positive when degeneracy ${<}22$\% and absent when ${>}31$\% ($p{<}0.01$; Appendix~\ref{app:epoch_confound}); alternative strategies fail to beat greedy (Appendix~\ref{app:dals}, \ref{app:supervised_combination}).
10	Construction is the only consistently positive strategy (Table~\ref{tab:cost_benefit}), though the trade-off ($N{\times}$ inference cost for ${\approx}1$\,pp) may only be justified in safety-critical settings.
11	LP compression (median 0.041 nats) connects to calibration challenges \cite{kadavath2022language, xiong2024verbalized}; per-sample alternatives \cite{kang2025selfcertainty} remain untested.
12	
13	\paragraph{Limitations of causal interpretation.}
14	Our evidence is correlational and theoretical (MBR framework, conditional decomposition), not interventional: we have not performed controlled interventions (e.g., artificially varying degeneracy while holding other factors constant), and the cascade stages interact in ways that resist decomposition into independent causal effects ($R^2{<}0$; \S\ref{sec:selection_gap}).
15	Our contribution is characterization of the phenomenon; causal claims require future intervention e
…[truncated 15 chars]

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

_source line 3005 · 2026-05-21T12:26:17.445519+00:00_

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

_source line 3006 · 2026-05-21T12:26:17.647826+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	NER exhibits oracle scaling ($c{\approx}0.5$) but aggregation fails above $\theta_{\text{crit}}{=}0.70$; entity construction and LP selection ($+0.4$\textendash$1.4$\,pp) bypass the introspection boundary (AUROC $0.63$\textendash$0.88$ vs.\ ESJ $0.51$) rather than resolve it.
4	For configurations with small sample sizes (e.g., SQL $n{=}196$), absence of significant improvement may reflect insufficient statistical power rather than true absence of effect.
5	

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

_source line 3007 · 2026-05-21T12:26:17.649072+00:00_

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

_source line 3008 · 2026-05-21T12:26:17.701510+00:00_

1	Scope: structured IE (NER primary, RE and SQL exploratory), English only, open-weight (Qwen and LLaMA) and closed-source (GPT-5.5) families, fine-tuned (4B--14B) and zero-shot (72B, GPT-5.5) regimes, sample budget $N{\leq}32$.
2	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
3	All experiments use English-language datasets; cross-lingual generalization remains untested.
4	Cross-model consistency results (\S\ref{sec:cross_model}) are limited to one dataset (Few-NERD) and one model pair (Qwen3-8B + LLaMA-3.1-8B).
5	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
6	We cover 4B\textendash 14B fine-tuned, 72B zero-shot, and GPT-5.5 zero-shot; the gap persists across all but behavior with 72B fine-tuning is untested.
7	Frontier API models exhibit markedly different degeneracy profiles (e.g., Claude Sonnet~4 at 74\% vs.\ DeepSeek Chat at 5.5\%; Table~\ref{tab:frontier_sc_cross}), suggesting that our findings from fine-tuned open-weight models may not fully generalize to proprietary systems.
8	The 72B zero-shot comparison simultaneously varies model family (Qwen3$\to$Qwen2.5), training regime (fine-tuned$\to$zero-shot), and quantization (FP16$\to$AWQ 4-bit); these factors cannot be fully disentangled.
9	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
10	
11	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
12	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appe
…[truncated 3001 chars]

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

_source line 3009 · 2026-05-21T12:26:24.268227+00:00_

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

_source line 3010 · 2026-05-21T12:26:25.071731+00:00_

File content (61818 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 3011 · 2026-05-21T12:26:25.072164+00:00_

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

_source line 3012 · 2026-05-21T12:26:25.674676+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{min2023factscore,
4	  title = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},
5	  author = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},
6	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
7	  year = {2023},
8	  url = {https://aclanthology.org/2023.emnlp-main.741/},
9	}
10	
11	@article{holm1979simple,
12	  title = {A Simple Sequentially Rejective Multiple Test Procedure},
13	  author = {Holm, Sture},
14	  journal = {Scandinavian Journal of Statistics},
15	  volume = {6},
16	  number = {2},
17	  pages = {65--70},
18	  year = {1979},
19	}
20	
21	@inproceedings{xiong2024verbalized,
22	  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},
23	  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},
24	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},
25	  year = {2024},
26	  url = {https://arxiv.org/abs/2306.13063},
27	}
28	
29	@article{brown2024monkeys,
30	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
31	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
32	  journal = {arXiv preprint arXiv:2407.21787},
33	  year = {2024},
34	  url = {https://arxiv.org/abs/2407.21787}
35	}
36	
37	@inproceedings{chen2024usc,
38	  title = {Universal Self-Consistency for Large Language Model Generation},
39	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
40	  bo
…[truncated 2906 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 3013 · 2026-05-21T12:26:25.675011+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": "5000"
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
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 3014 · 2026-05-21T12:26:26.126435+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 226\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 3531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 3015 · 2026-05-21T12:26:26.278772+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
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
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3016 · 2026-05-21T12:26:26.380267+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3017 · 2026-05-21T12:26:30.600542+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent"
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
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent"
  }
}
```

</details>

---


### Tool result

_source line 3018 · 2026-05-21T12:26:30.651109+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3019 · 2026-05-21T12:26:31.555800+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config*.yaml",
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
    "pattern": "**/project_config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 3020 · 2026-05-21T12:26:32.031769+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 475
}
```

</details>

---


### Tool call

_source line 3021 · 2026-05-21T12:26:32.134418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "0",
  "limit": "200"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 3022 · 2026-05-21T12:26:32.235577+00:00_

0	\section{Notation}\label{app:notation}
1	
2	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{cl}
8	\toprule
9	Symbol & Meaning \\
10	\midrule
11	$\mathcal{M}$ & Language model \\
12	$x$ & Input instance \\
13	$y_i$ & $i$-th stochastic sample \\
14	$N$ & Number of samples \\
15	$T$ & Sampling temperature \\
16	$c(\cdot)$ & Confidence signal \\
17	SJ & Soft Jaccard similarity \\
18	FK & Fleiss' $\kappa$ \\
19	EM & Exact-match voting rate \\
20	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
21	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
22	\bottomrule
23	\end{tabular}
24	\caption{Notation used throughout the paper.}
25	\label{tab:notation}
26	\end{table}
27	
28	\section{Robustness Analysis}\label{app:robustness}
29	
30	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
31	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
32	
33	\begin{table}[t]
34	\centering
35	\small
36	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
37	\label{tab:robustness}
38	\begin{tabular}{llcc}
39	\toprule
40	& & NER $\rho$ & RE $\rho$ \\
41	\midrule
42	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
43	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
44	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
45	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
46	\quad FK & $T
…[truncated 13208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3023 · 2026-05-21T12:26:38.405002+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
    "output_mode": "content",
    "glob": "*.yaml",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 3024 · 2026-05-21T12:26:39.308537+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 3025 · 2026-05-21T12:26:39.810313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "300"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 3026 · 2026-05-21T12:26:40.212777+00:00_

200	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
201	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
202	EM ranks first across all four tested conditional configurations: SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$). This holds despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
203	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
204	On the conditional set, where the model demonstrably produces varied outputs, exact agreement becomes the strongest quality signal.
205	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
206	
207	\paragraph{WNUT-17 full signal analysis.}
208	Table~\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\rho$.
209	
210	\begin{table}[t]
211	\centering
212	\small
213	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
214	\label{tab:wnut}
215	\begin{tabular}{lcccc}
216	\toprule
217	Signal & $\rho$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
218	\midrule
219	VC      & .724 & .913 & .038 & .487 \\
220	FK      & .125 & .555 & .169 & .00
…[truncated 21529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 3027 · 2026-05-21T12:26:40.213523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 3028 · 2026-05-21T12:26:40.282498+00:00_

1	% Responsible NLP Research Checklist
2	% Following the ACL Rolling Review guidelines:
3	% https://aclrollingreview.org/responsibleNLPresearch/
4	
5	\subsection*{A\hspace{0.5em} For Every Submission}
6	
7	\begin{enumerate}
8	\item[A1.] \textbf{Did you discuss the limitations of your work?}\\
9	Yes. See the Limitations section after the Conclusion.
10	
11	\item[A2.] \textbf{Did you discuss any potential risks of your work?}\\
12	Yes. See the Ethics Statement. This work analyzes existing confidence signals for NER and identifies when they fail; the findings reduce risk of deploying unreliable confidence-based selection in production systems. No dual-use concerns.
13	
14	\item[A3.] \textbf{Do the abstract and introduction summarize the paper's main claims?}\\
15	Yes. The Abstract and Section~\ref{sec:introduction} (3 enumerated contributions) summarize all main claims with supporting evidence pointers.
16	\end{enumerate}
17	
18	\subsection*{B\hspace{0.5em} Did you use or create scientific artifacts?}
19	
20	Yes. We use existing datasets and pre-trained models.
21	
22	\begin{enumerate}
23	\item[B1.] \textbf{Did you cite the creators of artifacts you used?}\\
24	Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
25	
26	\item[B2.] \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\\
27	Partially. The Ethics Statement notes that CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their r
…[truncated 4168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 68
}
```

</details>

---


### Tool call

_source line 3029 · 2026-05-21T12:26:46.177091+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "paperreview_ai|external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "output_mode": "content",
  "glob": "*.{yaml,yml,json,toml}",
  "head_limit": "20"
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
    "pattern": "paperreview_ai|external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
    "output_mode": "content",
    "glob": "*.{yaml,yml,json,toml}",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 3030 · 2026-05-21T12:26:47.135841+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 3031 · 2026-05-21T12:26:47.688193+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
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
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3032 · 2026-05-21T12:26:47.839199+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 3033 · 2026-05-21T12:26:48.491996+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission guidelines page limit anonymity double blind 2026"
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
    "query": "EMNLP 2026 ARR submission guidelines page limit anonymity double blind 2026"
  }
}
```

</details>

---


### Tool result

_source line 3034 · 2026-05-21T12:26:54.724592+00:00_

Web search results for query: "EMNLP 2026 ARR submission guidelines page limit anonymity double blind 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Policies for Review and Citation - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"}]

Based on the search results, here are the key EMNLP 2026 submission guidelines regarding page limits, anonymity, and double-blind review:

## Double-Blind Review

The reviewing process will continue to be double-blind. Reviewers will not see authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible.

## Anonymity Requirements

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" must be avoided. Supplementary materials, including any links to repositories, should also be anonymized.

…[truncated 684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6232
}
```

</details>

---


### Tool call

_source line 3035 · 2026-05-21T12:26:58.238485+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 call for papers long paper short paper page limit",
  "allowed_domains": "['aclrollingreview.org']"
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
    "query": "ACL Rolling Review 2026 call for papers long paper short paper page limit",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 3036 · 2026-05-21T12:26:58.489778+00:00_

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

_source line 3037 · 2026-05-21T12:26:58.792047+00:00_

1	issues:
2	  # ===== 历史 resolved issues (保留) =====
3	  - id: "R1-W1"
4	    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
5	    category: experiment
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 19
10	    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
11	    resolution_round: 19
12	
13	  - id: "R1-W2"
14	    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
15	    category: framing
16	    severity: critical
17	    status: resolved
18	    first_raised_round: 1
19	    last_seen_round: 21
20	    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
21	    resolution_round: 21
22	
23	  - id: "R2-N1-old"
24	    summary: "Contribution 1 'methodological premise' 是定义推论"
25	    category: framing
26	    severity: critical
27	    status: resolved
28	    first_raised_round: 1
29	    last_seen_round: 19
30	    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
31	    resolution_round: 19
32	
33	  - id: "R2-N2-old"
34	    summary: "与 MBR 文献差异化定位不够锐利"
35	    category: framing
36	    severity: warning
37	    status: resolved
38	    first_raised_round: 1
39	    last_seen_round: 19
40	    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
41	    resolution_round: 19
42	
43	  - id: "R2-N4-old"
44	    summary: "模型规模 3B-8B，70B+ 未知"
45	    category: experiment
46	    severity: info
47	    status: resolved
48	    first_raised_round: 1
49	    last_seen_round: 19
50	    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
51	    resolution_round: 19
52	
53	  - id: "R1-W3-old"
54	    summary: "2-seed 统计效力不足"
55	    category: experiment
56	    severity: warning
57	    status: resolved
58	    first_raised_round: 1
59	    last_seen_round: 19
60	    resolution: "Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。"
61	    resolution_round: 19
62	
63	  - id: "R1-W4-old
…[truncated 39063 chars]

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


### Tool result

_source line 3038 · 2026-05-21T12:27:02.003024+00:00_

Web search results for query: "ACL Rolling Review 2026 call for papers long paper short paper page limit"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's the information about ACL Rolling Review 2026 page limits:

ACL Rolling Review submissions are in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

Additionally, discussions of ethical impact do not count towards the page limit, as long as they are placed at the end of the paper, and ethics sections will not count towards the page limit.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 3764
}
```

</details>

---


### Tool call

_source line 3039 · 2026-05-21T12:27:33.426106+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3040 · 2026-05-21T12:27:55.352069+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21925
}
```

</details>

---


### Tool call

_source line 3041 · 2026-05-21T12:27:55.731604+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查方法严谨性与实验设计。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤ 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**: ACL (review mode)\n- **匿名规则**: Double-blind，无 anonymity period\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点关注：\n\n1. **Diagnostic Framework 合理性**\n   - 四阶段 cascade（QE → degeneracy → agreement fidelity → LP compression）是否逻辑自洽？\n   - 各阶段是否有充分的实验证据支撑？\n   - \"correlation-selection gap\" 概念是否有 tautological 成分（instance-level signals 天然无法做 per-sample selection）？\n\n2. **统计方法论**\n   - Holm-Bonferroni 多重比较校正：family 定义是否合理？k=57 是否过于保守？\n   - Bootstrap CI、paired bootstrap p-values 的使用是否恰当？\n   - 样本量是否足够（SciERC n=529、RE n≈397）？负面结论是否可能是 power 不足？\n   - Multi-seed 报告是否充分？\n\n3. **实验覆盖度与控制**\n   - 4 个 NER 数据集 + RE + SQL 的覆盖是否支撑论文 claim？\n   - 模型覆盖：2 个 8B fine-tuned + 4B/14B 消融 + 72B zero-shot + GPT-5.5——是否充分？\n   - N=8/16 的 sample budget 是否对 test-time compute scaling 研究足够？\n   - Epoch confound（Few-NERD 3 epochs vs others 5 epochs）的处理是否充分？\n   - Cross-model ensemble 仅 1 个数据集 1 对模型——可靠性如何？\n\n4. **理论分析**\n   - Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 的 tightness（仅 3-12% 实际增益）\n   - Proposition 1 的 entity-wise independence 假设在 NER 中是否合理？\n   - MBR 框架的推导是否严谨？\n\n5. **因果 vs 相关性语言**\n   - 正文是否存在因果性措辞（\"governs\"、\"explaining why\"）与实际相关性证据的不匹配？\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → Overall Assessment（评分 + 置信度）→ Detailed Comments。\n\n**评审立场**：像顶会最严格的审稿人。不留情面，严正客观。",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311"
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
    "text": "你是 Reviewer 1，负责审查方法严谨性与实验设计。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤ 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**: ACL (review mode)\n- **匿名规则**: Double-blind，无 anonymity period\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点关注：\n\n1. **Diagnostic Framework 合理性**\n   - 四阶段 cascade（QE → degeneracy → agreement fidelity → LP compression）是否逻辑自洽？\n   - 各阶段是否有充分的实验证据支撑？\n   - \"correlation-selection gap\" 概念是否有 tautological 成分（instance-level signals 天然无法做 per-sample selection）？\n\n2. **统计方法论**\n   - Holm-Bonferroni 多重比较校正：family 定义是否合理？k=57 是否过于保守？\n   - Bootstrap CI、paired bootstrap p-values 的使用是否恰当？\n   - 样本量是否足够（SciERC n=529、RE n≈397）？负面结论是否可能是 power 不足？\n   - Multi-seed 报告是否充分？\n\n3. **实验覆盖度与控制**\n   - 4 个 NER 数据集 + RE + SQL 的覆盖是否支撑论文 claim？\n   - 模型覆盖：2 个 8B fine-tuned + 4B/14B 消融 + 72B zero-shot + GPT-5.5——是否充分？\n   - N=8/16 的 sample budget 是否对 test-time compute scaling 研究足够？\n   - Epoch confound（Few-NERD 3 epochs vs others 5 epochs）的处理是否充分？\n   - Cross-model ensemble 仅 1 个数据集 1 对模型——可靠性如何？\n\n4. **理论分析**\n   - Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 的 tightness（仅 3-12% 实际增益）\n   - Proposition 1 的 entity-wise independence 假设在 NER 中是否合理？\n   - MBR 框架的推导是否严谨？\n\n5. **因果 vs 相关性语言**\n   - 正文是否存在因果性措辞（\"governs\"、\"explaining why\"）与实际相关性证据的不匹配？\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → Overall Assessment（评分 + 置信度）→ Detailed Comments。\n\n**评审立场**：像顶会最严格的审稿人。不留情面，严正客观。",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3042 · 2026-05-21T12:28:12.246363+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16514
}
```

</details>

---


### Tool call

_source line 3043 · 2026-05-21T12:28:12.751642+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查新颖性、完整性与写作质量。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤ 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**: ACL (review mode)\n- **匿名规则**: Double-blind，无 anonymity period\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**，重点关注：\n\n1. **新颖性评估**\n   - \"Correlation-selection gap\" 作为核心概念的原创性——与 MBR 文献、SC failure modes (Chen et al. 2023)、diversity collapse (Yun et al. 2025) 的差异化是否足够？\n   - 9 种方法类别的 negative results 是否有足够的独立贡献价值？\n   - Entity construction（MV 作为 MBR 解码的特例）是否过于 incremental？\n   - Hidden-state probe 结果的 introspection boundary 概念是否有新意？\n\n2. **Framing 清晰度**\n   - 标题 \"The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\" 是否准确反映论文内容？\n   - Abstract 信息密度是否过高？数字是否过多？\n   - 4 个 contributions 的层次是否清晰？diagnostic framework vs. negative results vs. positive escape routes 的叙事逻辑？\n   - \"Structured IE\" / \"structured prediction\" framing 与实际 NER-centric 证据是否匹配？\n\n3. **Related Work 覆盖**\n   - 与 Yao et al. (2026) 的差异化是否充分？\n   - 与 Yun et al. (2025) diversity collapse 的关系是否清楚？\n   - MBR decoding 文献（DeNero et al. 2009, Freitag et al. 2022 等）是否充分讨论？\n   - 是否遗漏重要相关工作？\n   - 引用质量：是否有 orphan bib entries？引用格式是否一致？\n\n4. **写作质量**\n   - 章节组织是否合理（Diagnostic → Mechanistic → Single Signal → Adaptive → Theory → Experiments → Related Work → Discussion → Conclusion）？\n   - 段落衔接是否流畅？\n   - 术语定义是否一致（F1 metric 类型、degeneracy 等）？\n   - Limitations 是否覆盖关键弱点？\n\n5. **跨任务泛化声明**\n   - RE extension（55.5% zero-F1 instances, span error confound）的可靠性\n   - SQL parsing（n=196, 87.2% degeneracy）作为 cross-task validation 的充分性\n   - 正文的泛化声明是否 overclaimed？\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → Overall Assessment（评分 + 置信度）→ Detailed Comments。\n\n**评审立场**：像顶会最严格的审稿人。不留情面，严正客观。",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311"
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
    "text": "你是 Reviewer 2，负责审查新颖性、完整性与写作质量。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤ 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**: ACL (review mode)\n- **匿名规则**: Double-blind，无 anonymity period\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**，重点关注：\n\n1. **新颖性评估**\n   - \"Correlation-selection gap\" 作为核心概念的原创性——与 MBR 文献、SC failure modes (Chen et al. 2023)、diversity collapse (Yun et al. 2025) 的差异化是否足够？\n   - 9 种方法类别的 negative results 是否有足够的独立贡献价值？\n   - Entity construction（MV 作为 MBR 解码的特例）是否过于 incremental？\n   - Hidden-state probe 结果的 introspection boundary 概念是否有新意？\n\n2. **Framing 清晰度**\n   - 标题 \"The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\" 是否准确反映论文内容？\n   - Abstract 信息密度是否过高？数字是否过多？\n   - 4 个 contributions 的层次是否清晰？diagnostic framework vs. negative results vs. positive escape routes 的叙事逻辑？\n   - \"Structured IE\" / \"structured prediction\" framing 与实际 NER-centric 证据是否匹配？\n\n3. **Related Work 覆盖**\n   - 与 Yao et al. (2026) 的差异化是否充分？\n   - 与 Yun et al. (2025) diversity collapse 的关系是否清楚？\n   - MBR decoding 文献（DeNero et al. 2009, Freitag et al. 2022 等）是否充分讨论？\n   - 是否遗漏重要相关工作？\n   - 引用质量：是否有 orphan bib entries？引用格式是否一致？\n\n4. **写作质量**\n   - 章节组织是否合理（Diagnostic → Mechanistic → Single Signal → Adaptive → Theory → Experiments → Related Work → Discussion → Conclusion）？\n   - 段落衔接是否流畅？\n   - 术语定义是否一致（F1 metric 类型、degeneracy 等）？\n   - Limitations 是否覆盖关键弱点？\n\n5. **跨任务泛化声明**\n   - RE extension（55.5% zero-F1 instances, span error confound）的可靠性\n   - SQL parsing（n=196, 87.2% degeneracy）作为 cross-task validation 的充分性\n   - 正文的泛化声明是否 overclaimed？\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → Overall Assessment（评分 + 置信度）→ Detailed Comments。\n\n**评审立场**：像顶会最严格的审稿人。不留情面，严正客观。",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3044 · 2026-05-21T12:28:14.360485+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1608
}
```

</details>

---


### Assistant

_source line 3045 · 2026-05-21T12:28:31.444345+00:00_

视觉审查已派发，两名 Reviewer 已收到 Round 1 任务。

- **视觉审查**：已启动（fire-and-forget，不阻塞）
- **Reviewer 1**（方法严谨性 + 实验设计）：已分配
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：已分配

等待两名 Reviewer 独立初审结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 226

## Round 226

8 recorded events


### User

_source line 3046 · 2026-05-21T12:48:01.212083+00:00_

[Reviewer 1 审稿结果]:
读取最后的关键附录页（SQL 验证、failure gallery 等）。

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

_source line 3047 · 2026-05-21T12:49:19.654803+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3048 · 2026-05-21T12:49:44.470242+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24815
}
```

</details>

---


### Tool call

_source line 3049 · 2026-05-21T12:49:46.026608+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (ACL Rolling Review May 2026 cycle)\n- **投稿类别**: Long Paper (ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**: ACL (使用 \\usepackage[review]{acl})\n- **匿名规则**: Double-blind（无匿名期要求）\n- **评分标准**: ARR Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文信息\n- **标题**: The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\n- **论文文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Diagnostic cascade（4 阶段）的逻辑是否自洽？各阶段之间的关系是 descriptive 还是 causal？论文的语言是否与证据强度匹配？\n- Confidence signals（SJ, FK, EM, VC, LP）的定义和使用是否严谨？\n- Entity construction 的 MBR 框架推导是否正确？\n- Degeneracy decomposition（Proposition 1）的假设是否合理？证明是否正确？\n\n### 2. 实验设计\n- 4 个 NER 数据集的选择是否合理？覆盖度是否足够？\n- 2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）+ scale ablations（4B, 14B, 72B zero-shot, GPT-5.5）是否充分？\n- RE extension（SciERC 单数据集）和 SQL parsing validation 是否足以支撑 cross-task claims？\n- N=8 (primary) + N=16 (scaling) 的样本预算是否足够？\n- 训练设置（LoRA fine-tuning, 3 vs 5 epochs）是否引入混淆？\n\n### 3. 统计分析\n- Holm-Bonferroni 多重比较校正：k=57 global family 的定义是否透明？Abstract 中报告的 family-wise k 值是否与 Appendix 一致？\n- 核心 positive results（Few-NERD LP selection +1.39pp, LP-weighted construction +1.40pp）在不同校正层级下的显著性\n- Negative results 的统计功效：SciERC n=529, SQL n=196 的 MDE 是否足以排除有意义的效应？\n- Multi-seed reporting（3 seeds for Few-NERD/CoNLL, 1 seed for SciERC）是否充分？\n- Bootstrap CI、TOST equivalence testing 的使用是否恰当？\n\n### 4. 审稿报告格式\n请按以下格式提交审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths**: 逐条列出优点\n- **Weaknesses**: 逐条列出缺点（标注 [critical] / [should-fix] / [minor]）\n- **Questions**: 需要作者回答的问题\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 基于 ARR 评分标准的初步评分 + 置信度\n- **Detailed Comments**: 逐节评论",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311",
  "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
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
    "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (ACL Rolling Review May 2026 cycle)\n- **投稿类别**: Long Paper (ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**: ACL (使用 \\usepackage[review]{acl})\n- **匿名规则**: Double-blind（无匿名期要求）\n- **评分标准**: ARR Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文信息\n- **标题**: The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\n- **论文文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Diagnostic cascade（4 阶段）的逻辑是否自洽？各阶段之间的关系是 descriptive 还是 causal？论文的语言是否与证据强度匹配？\n- Confidence signals（SJ, FK, EM, VC, LP）的定义和使用是否严谨？\n- Entity construction 的 MBR 框架推导是否正确？\n- Degeneracy decomposition（Proposition 1）的假设是否合理？证明是否正确？\n\n### 2. 实验设计\n- 4 个 NER 数据集的选择是否合理？覆盖度是否足够？\n- 2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）+ scale ablations（4B, 14B, 72B zero-shot, GPT-5.5）是否充分？\n- RE extension（SciERC 单数据集）和 SQL parsing validation 是否足以支撑 cross-task claims？\n- N=8 (primary) + N=16 (scaling) 的样本预算是否足够？\n- 训练设置（LoRA fine-tuning, 3 vs 5 epochs）是否引入混淆？\n\n### 3. 统计分析\n- Holm-Bonferroni 多重比较校正：k=57 global family 的定义是否透明？Abstract 中报告的 family-wise k 值是否与 Appendix 一致？\n- 核心 positive results（Few-NERD LP selection +1.39pp, LP-weighted construction +1.40pp）在不同校正层级下的显著性\n- Negative results 的统计功效：SciERC n=529, SQL n=196 的 MDE 是否足以排除有意义的效应？\n- Multi-seed reporting（3 seeds for Few-NERD/CoNLL, 1 seed for SciERC）是否充分？\n- Bootstrap CI、TOST equivalence testing 的使用是否恰当？\n\n### 4. 审稿报告格式\n请按以下格式提交审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths**: 逐条列出优点\n- **Weaknesses**: 逐条列出缺点（标注 [critical] / [should-fix] / [minor]）\n- **Questions**: 需要作者回答的问题\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 基于 ARR 评分标准的初步评分 + 置信度\n- **Detailed Comments**: 逐节评论",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311",
    "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
  }
}
```

</details>

---


### Tool result

_source line 3050 · 2026-05-21T12:50:07.998453+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21971
}
```

</details>

---


### Tool call

_source line 3051 · 2026-05-21T12:50:08.501522+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查新颖性、相关工作完整性、写作质量和格式合规。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (ACL Rolling Review May 2026 cycle)\n- **投稿类别**: Long Paper (ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**: ACL (使用 \\usepackage[review]{acl})\n- **匿名规则**: Double-blind（无匿名期要求）\n- **评分标准**: ARR Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文信息\n- **标题**: The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\n- **论文文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- \"Correlation-selection gap\" 概念的新颖性：是否为已知现象的重新包装？与 MBR decoding 文献的区别？\n- Diagnostic cascade（QE → degeneracy → agreement fidelity → LP compression）作为分析框架的贡献度\n- 9 种方法的覆盖度：是否遗漏了重要的方法类别（如 Self-Certainty, P(True), 其他 per-sample scoring methods）？\n- Hidden-state probe 的 \"introspection boundary\" 概念是否有独立贡献？\n- Entity construction 作为 prescriptive contribution 的新颖性（vs. 已有 entity voting 工作如 Xie et al. 2023）\n- Cross-task validation（RE + SQL）对论文 scope claims 的支撑力度\n\n### 2. 相关工作完整性\n- Test-time compute scaling 文献覆盖度\n- SC failure modes（Chen et al. 2023, Huang et al. 2024）引用和差异化是否充分\n- MBR decoding 文献（Eikema & Aziz 2022, DeNero et al. 2009 等）\n- NER-specific SC 工作（Yao et al. 2026, Xie et al. 2023）\n- Diversity collapse（Yun et al. 2025）差异化是否充分\n- Uncertainty estimation / calibration 文献\n- 是否有遗漏的关键引用（特别是 2025-2026 年的新工作）\n- Bib 文件质量：是否有 orphan entries、虚构引用、元数据错误？\n\n### 3. 写作质量\n- Abstract 信息密度是否适当？是否清晰传达了 4 个 contributions？\n- Introduction 的叙事结构：问题定义 → 方法 → 结果 → 贡献是否连贯？\n- 各 section 之间的逻辑流是否顺畅？\n- 术语一致性（如 F1 metric 的定义和使用、degeneracy 的定义）\n- 因果语言 vs 相关性语言的使用是否与证据强度匹配\n- Table/Figure 的设计和 caption 质量\n- Limitations section 是否充分覆盖主要局限\n\n### 4. 格式合规\n- 正文是否在 8 页限制内？\n- 匿名化是否完整（无作者信息泄露、无自引暴露身份）？\n- 引用格式是否符合 ACL 标准？\n- Responsible NLP Research Checklist 是否完整？\n- 附录引用是否正确？\n\n### 5. 审稿报告格式\n请按以下格式提交审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths**: 逐条列出优点\n- **Weaknesses**: 逐条列出缺点（标注 [critical] / [should-fix] / [minor]）\n- **Questions**: 需要作者回答的问题\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 基于 ARR 评分标准的初步评分 + 置信度\n- **Detailed Comments**: 逐节评论",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311",
  "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
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
    "text": "你是 Reviewer 2，负责审查新颖性、相关工作完整性、写作质量和格式合规。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (ACL Rolling Review May 2026 cycle)\n- **投稿类别**: Long Paper (ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**: ACL (使用 \\usepackage[review]{acl})\n- **匿名规则**: Double-blind（无匿名期要求）\n- **评分标准**: ARR Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文信息\n- **标题**: The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\n- **论文文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- \"Correlation-selection gap\" 概念的新颖性：是否为已知现象的重新包装？与 MBR decoding 文献的区别？\n- Diagnostic cascade（QE → degeneracy → agreement fidelity → LP compression）作为分析框架的贡献度\n- 9 种方法的覆盖度：是否遗漏了重要的方法类别（如 Self-Certainty, P(True), 其他 per-sample scoring methods）？\n- Hidden-state probe 的 \"introspection boundary\" 概念是否有独立贡献？\n- Entity construction 作为 prescriptive contribution 的新颖性（vs. 已有 entity voting 工作如 Xie et al. 2023）\n- Cross-task validation（RE + SQL）对论文 scope claims 的支撑力度\n\n### 2. 相关工作完整性\n- Test-time compute scaling 文献覆盖度\n- SC failure modes（Chen et al. 2023, Huang et al. 2024）引用和差异化是否充分\n- MBR decoding 文献（Eikema & Aziz 2022, DeNero et al. 2009 等）\n- NER-specific SC 工作（Yao et al. 2026, Xie et al. 2023）\n- Diversity collapse（Yun et al. 2025）差异化是否充分\n- Uncertainty estimation / calibration 文献\n- 是否有遗漏的关键引用（特别是 2025-2026 年的新工作）\n- Bib 文件质量：是否有 orphan entries、虚构引用、元数据错误？\n\n### 3. 写作质量\n- Abstract 信息密度是否适当？是否清晰传达了 4 个 contributions？\n- Introduction 的叙事结构：问题定义 → 方法 → 结果 → 贡献是否连贯？\n- 各 section 之间的逻辑流是否顺畅？\n- 术语一致性（如 F1 metric 的定义和使用、degeneracy 的定义）\n- 因果语言 vs 相关性语言的使用是否与证据强度匹配\n- Table/Figure 的设计和 caption 质量\n- Limitations section 是否充分覆盖主要局限\n\n### 4. 格式合规\n- 正文是否在 8 页限制内？\n- 匿名化是否完整（无作者信息泄露、无自引暴露身份）？\n- 引用格式是否符合 ACL 标准？\n- Responsible NLP Research Checklist 是否完整？\n- 附录引用是否正确？\n\n### 5. 审稿报告格式\n请按以下格式提交审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths**: 逐条列出优点\n- **Weaknesses**: 逐条列出缺点（标注 [critical] / [should-fix] / [minor]）\n- **Questions**: 需要作者回答的问题\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 基于 ARR 评分标准的初步评分 + 置信度\n- **Detailed Comments**: 逐节评论",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311",
    "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
  }
}
```

</details>

---


### Tool result

_source line 3052 · 2026-05-21T12:50:10.941499+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2439
}
```

</details>

---


### Assistant

_source line 3053 · 2026-05-21T12:50:16.608416+00:00_

已全部派发：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已启动（fire-and-forget） |
| Reviewer 1（方法/实验/统计） | ✅ 已分配 |
| Reviewer 2（新颖性/相关工作/写作/格式） | ✅ 已分配 |

等待两位 Reviewer 的 Round 1 独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 227

## Round 227

2 recorded events


### User

_source line 3054 · 2026-05-21T12:50:18.120809+00:00_

[Reviewer 2 审稿结果]:
继续读取 RE 扩展、SQL parsing 和理论部分的附录页。

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

_source line 3055 · 2026-05-21T12:50:26.744178+00:00_

两位 Reviewer 均在读取附录细节中，尚未提交完整审稿意见。视觉审查已派发。等待所有结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 228

## Round 228

2 recorded events


### User

_source line 3056 · 2026-05-21T13:09:38.851120+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告

**论文**: The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition
**Venue**: EMNLP 2026 (ARR May 2026 cycle), Long Paper

---

## Summary

本文研究 self-consistency（SC）在 NER 任务上的失败机制。作者提出一个 4 阶段诊断级联（quality estimation → degeneracy → agreement fidelity → LP compression），在 4 个 NER 数据集、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）及多个模型规模（4B–72B, GPT-5.5）上系统评估了 9 类方法。核心发现是负面的：无 entity-level agreement signal 能可靠改善 sample selection；仅 sequence-level LP selection（+1.39pp on Few-NERD）和 entity-level weighted construction（+1.02–1.40pp）提供有限增益。论文还通过 MBR 框架连接 entity construction 与 majority vote，并提出 degeneracy decomposition bound。

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 方法论严谨的系统性负面结果研究，诊断框架和统计分析质量高，但跨任务泛化声明支撑不足，核心理论贡献（Proposition 1）过于松弛，positive findings 效应量有限且数据集特异。

---

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | NER 主实验设计严谨，Holm-Bonferroni 多重校正、bootstrap CI、TOST 等统计工具使用恰当；但 RE 单数据集 + SQL 196 样本的跨任务声明证据薄弱，Proposition 1 bound 过松（自承仅覆盖 3–12% actual gains） |
| **Excitement** | 2.5/5 | 负面结果对社区有参考价值，但 SC 在结构化输出上因高 degeneracy 而失效并非意外发现；positive results（+1.39pp）效应量有限且 dataset-specific；诊断级联框架有一定方法论贡献但未形成可复用的工具 |
| **Reproducibility** | 4/5 | 实验细节充分（47 页 appendix），LoRA 配置、prompt template、超参数均有报告；代码承诺 acceptance 后释放；主要扣分：部分 seed 数不足（CoNLL 2 seeds, WNUT-17 部分配置 1 seed） |
| **Overall Assessment** | 3.0/5 | Findings 级别——统计方法论扎实，诊断框架有价值，但跨任务泛化不足、理论贡献薄弱、核心发现的新颖性有限 |
| **Reviewer Confidence** | 4/5 | 熟悉 NER、self-consistency、MBR decoding、统计检验方法论；对 hidden-state probing 部分有一定不确定性 |

---

## Strengths

**S1. 系统性和全面性出色。** 9 类方法（diagnostic probes, selection, construction, cross-model, supervised, verifier 等）× 4 数据集 × 多模型规模的全因子实验设计，是目前 SC 用于 IE 的最全面研究。Table 2（Section 5）的方法分类学和 Table 62（Appendix）的 differentiation matrix 清晰定位了本文的贡献边界。

**S2. 统计方法论严谨。** Holm-Bonferroni 多重校正覆盖 k=57 个检验（Table 13），TOST equivalence testing 用于支撑负面结果（Table 16），FK independence permutation test（Table 8）验证信号假设，bootstrap CI 报告置信区间而非单一 p 值。这在 *ACL 投稿中属上乘水准。特别是 Table 13 完整列出所有 57 个检验的 raw p 和 adjusted p，透明度很高。

**S3. MBR 理论连接新颖且正确。** 将 entity-level majority vote 连接到 MBR decoding under set-overlap utility（Proposition 2, Appendix p）是本文最有价值的理论贡献。这个连接不仅解释了为什么 α=1 对应 majority-vote threshold 1/2，还为 LP-weighted construction 提供了 principled motivation。

**S4. 诊断级联概念有实用价值。** 4 阶段框架（QE → degeneracy → agreement fidelity → LP compression）为其他结构化生成任务提供了可借鉴的分析模板。Figure 1 的可视化有效传达了核心论点。

**S5. 负面结果的呈现方式诚实且有建设性。** 论文没有回避负面结果，而是系统分析失败原因并给出明确的实践建议（Section 9: "From diagnosis to practice"），包括何时该用 SC、何时不该用。Table 61（cost-benefit summary）直接给出了每种方法的性价比判断。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 跨任务泛化声明缺乏充分证据

- **具体位置**: Abstract ("cross-task validation on RE and SQL parsing"), Section 6.3, Section 7.5 (RE), Appendix o (SQL)
- **问题**: RE extension 仅在 SciERC 一个数据集上评估（n=529 non-zero F1 instances, 单 seed），SQL validation 仅在 Spider 上评估（n=196, 87.2% degeneracy → 有效非退化样本约 25 个）。Abstract 中 "cross-task validation" 的表述暗示了跨任务泛化，但单数据集 + 极小样本无法支撑此声明。
- **为什么影响接收**: 如果去掉跨任务泛化声明，论文的 scope 从 "structured IE general" 缩小到 "NER-specific"。这本身可以接受，但目前的表述与证据强度不匹配。Table 55（Appendix, page 45）的 post-hoc power analysis 显示 n=23 时仅 ρ≥0.5 的 correlation 有足够 power 被检测到——这意味着 SQL 上的负面结果可能是 power 不足而非真正的 null effect。
- **建议**: (1) 将 Abstract 和 Introduction 中的 "cross-task validation" 改为 "exploratory cross-task extension"；(2) 增加至少一个 RE 数据集（如 TACRED 或 DocRED）或明确声明 RE 结论仅为 preliminary；(3) 对 SQL 结果加入 minimum detectable effect (MDE) 讨论——当前 n=196 能排除多大效应？

**N2** [critical] Holm-Bonferroni 家族定义在 Abstract 与 Appendix 间存在不一致，可能误导评分

- **具体位置**: Abstract ("Holm-adjusted p=0.021, selection family k=21"), Table 13 (Appendix, k=57 global family)
- **问题**: Abstract 报告的 p=0.021 使用的是 selection family 内的 k=21 校正。但 Table 13 的 global family 包含 k=57 个检验。如果 Few-NERD LP selection 的 raw p ≈ 0.001，全局校正后 p_adj ≈ 0.057，不再显著（α=0.05）。Abstract 仅报告 within-family correction 而不提及 global correction 的结果，存在 selective reporting 风险。
- **为什么影响接收**: 论文最重要的 positive result (+1.39pp) 的显著性依赖于使用哪个 correction family。如果全局校正下不显著，核心 positive finding 的统计支撑会大幅削弱。
- **建议**: (1) 在 Abstract 和 Section 7 中同时报告 within-family 和 global correction 的 p 值；(2) 明确说明选择 k=21 family 的理论依据（为什么 selection tests 构成独立 family？它们与 construction tests 是否真正独立？）；(3) 如果 global correction 下不显著，应诚实陈述并调整 claim 强度。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [should-fix] 训练 epoch 差异与 degeneracy 的混淆

- **具体位置**: Section 7.1 (Experimental Setup), Appendix aa (Epoch Confound Analysis), Table 21
- **问题**: SciERC 训练 3 epochs，Few-NERD/CoNLL 训练 5 epochs。Appendix aa 明确显示 degeneracy 随 epoch 单调递增。这意味着 SciERC 较低的 degeneracy 率部分归因于较少的训练轮数，而非任务本身的特性。跨数据集的 degeneracy 比较（如 Section 4 中 SciERC 17.8% vs. CoNLL 61.0% vs. Few-NERD 46.2%）因此被混淆。
- **建议**: 在所有数据集上使用相同 epoch 数重新训练（或至少在 3 epoch 检查点上对齐比较），或在主文中明确讨论此混淆并量化其影响。

**W2** [should-fix] Proposition 1 (Degeneracy Decomposition) 的贡献过于朴素

- **具体位置**: Section 6.3, Appendix p.4
- **问题**: Proposition 1 的核心内容：(a) degenerate instances 上 MV=greedy（定义即得）；(b) E[ΔF1] = (1-δ)·E[ΔF1|non-deg]（全期望公式）；(c) ΔF1>0 需要 precision > F1_greedy/2（F1 公式的代数推导）。这三个结论都是相当直接的数学事实。更关键的是，"Degeneracy Decomposition" bound E[ΔF1(A)] ≤ (1-D)·G_nd 作者自己承认仅覆盖 3–12% of actual gains（Section 6.3），说明它既非 tight 也非 informative。
- **为什么影响评分**: 论文将此作为理论贡献（Table 62 中 "Theoretical contrib: MBR equivalence, degeneracy bound, scaling laws"），但 bound 的松弛程度限制了其实际意义。与 Proposition 2（MBR connection）相比，Proposition 1 的贡献微弱。
- **建议**: 降低 Proposition 1 在正文中的呈现权重，或提供 tighter bound（例如考虑 signal alignment α 的分布而非仅用 upper bound）。

**W3** [should-fix] 诊断级联的 descriptive vs. causal 语言不一致

- **具体位置**: Figure 1 caption ("diagnostic sequence, not causal chain"), Abstract ("localizes where and how selection breaks down"), Section 9 ("Limitations of causal interpretation")
- **问题**: Figure 1 caption 明确声明级联是 descriptive 的，Section 9 也承认 causal interpretation 的局限。但 Abstract 中 "localizes where and how selection breaks down" 以及 Introduction 中 "The failure is systematic: a four-stage diagnostic cascade..." 的表述暗示了因果关系。级联的 4 个阶段（QE → degeneracy → agreement fidelity → LP compression）在不同数据集上可能并非按此顺序 "break down"——例如 SciERC 的主要瓶颈是 agreement fidelity（而非 degeneracy），而 CoNLL 的主要瓶颈是 degeneracy。
- **建议**: 统一语言——要么一致使用 "diagnostic decomposition" 而非 "cascade"（cascade 暗示序列依赖），要么明确说明该序列是在 Few-NERD 上观察到的主要模式，而非普遍规律。

**W4** [should-fix] LoRA fine-tuning 对 degeneracy 的影响未被讨论

- **具体位置**: Section 7.1, Table 21
- **问题**: 所有 fine-tuned 模型使用 LoRA（rank=16, alpha=32）。LoRA 的低秩约束可能本身就倾向于产生更窄的输出分布，从而人为提高 degeneracy。论文报告了 zero-shot 72B 模型的 degeneracy（Few-NERD 50%），但没有与同规模 full fine-tuning 比较。如果 LoRA 本身是 degeneracy 的部分原因，则论文的一般性结论（"SC fails for NER"）需要加限定词。
- **建议**: 至少讨论 LoRA vs. full fine-tuning 对 output diversity 的理论影响，或引用相关文献。如果有 full fine-tuning baseline（即使只在一个小数据集上），将大大加强论点。

**W5** [should-fix] Temperature exploration 不充分

- **具体位置**: Section 7.1 (T=1.0 primary), Appendix b (Table 7, only Qwen SciERC)
- **问题**: Temperature 直接控制 output diversity 进而影响 degeneracy——这是论文核心变量之一。但 temperature ablation 仅在 Qwen SciERC 上系统测试（Table 7: T=0.7, 1.0, 1.2）。Table 7 显示 LP 在 T=0.8 时 ρ 达到峰值，而 SJ 在 T=1.0 时较好——不同 signal 对 temperature 的敏感度不同。仅用 T=1.0 作为 primary setting 可能对某些 signal 不公平。
- **建议**: 至少在 Few-NERD（论文最重要的 positive result 所在数据集）上补充 T=0.7 和 T=1.2 的完整实验。

---

## Questions（需要作者回答）

**Q1.** Table 13 中 Few-NERD LP selection 的 raw p 是多少？全局 Holm 校正（k=57）后的 adjusted p 是多少？如果全局校正后 p>0.05，作者如何论证 within-family k=21 是合适的 family 定义？

**Q2.** Appendix aa 显示 SciERC 3-epoch model 的 degeneracy 显著低于 5-epoch。如果 SciERC 也训练到 5 epochs，degeneracy 率会上升多少？这是否会改变 SciERC 上 LP selection 的有效性结论？

**Q3.** LoRA rank=16 的选择依据是什么？是否测试过更高 rank（如 64 或 128）对 output diversity 的影响？

**Q4.** 论文声称 "no entity-level agreement signal reliably improves selection"，但 Table 2 中 cross-model SC 在 Few-NERD 上取得了 +0.42pp（p<0.001）。这是否属于 entity-level agreement signal 的成功案例？如果不是，如何区分 cross-model agreement 与 within-model entity-level agreement？

**Q5.** SQL parsing validation（Appendix o）中 87.2% degeneracy → 有效非退化样本约 25 个。在 n=25 下，TOST equivalence testing 的 equivalence margin 是多少？能排除多大的真实效应？

---

## Missing References

- **Wang et al. (2023) "GPT-NER: Named Entity Recognition via Large Language Models"** — 直接相关的 LLM-based NER 基线工作，应在 Related Work 中引用。
- **Jiang et al. (2023) "LLM-Blender: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion"** — 与 cross-model ensemble (Section 5.1) 直接相关。
- **Ye et al. (2023) "Self-Refine: Iterative Refinement with Self-Feedback"** — 论文讨论了 self-verification 的局限性，Self-Refine 是另一种 self-improvement 范式，应在 Discussion 中对比。

---

## 小问题（不影响接收）

- **M1.** Abstract 信息密度过高——包含 ρ 值、AUROC、pp、k 值等大量数字，建议精简到核心 message + 1-2 个支撑数字。
- **M2.** Related Work（Section 8）放在 Experiments（Section 7）之后——虽然 ACL 允许，但建议考虑前置，因为 MBR 和 SC 的背景对理解实验设计很重要。
- **M3.** Table 1（Section 4, page 4）的 caption 说 "SciERC" 但结果包含多个数据集的引用——caption 应更精确。
- **M4.** 引用验证发现 2 个 "not_found"（lightman2024verify, aggarwal2023adaptive）和 3 个 "mismatch"（snell2025scaling, muller2021understanding, dembczynski2011exact）——后 3 个可能是 LaTeX encoding 问题（如 ü vs. \"u），但前 2 个应确认 OpenAlex 覆盖。
- **M5.** Limitations 章节提到 "cross-model consistency results (§5.1) are limited to one dataset (Few-NERD)"——这个限制值得更突出地在主文中提及。

---

## 主要优势总结

1. *ACL 投稿中少见的统计严谨度（k=57 Holm-Bonferroni, TOST, permutation tests）
2. 全面的 9 类方法 × 4 数据集 × 多模型规模实验矩阵
3. MBR-majority vote 等价性是新颖且正确的理论贡献
4. 诊断级联框架对未来结构化生成研究有方法论价值
5. 47 页 appendix 的透明度和可复现性

---

**最终评分**: Overall 3.0 / Soundness 3.5 / Excitement 2.5 / Reproducibility 4 / Confidence 4

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

_source line 3057 · 2026-05-21T13:09:48.861238+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 229

## Round 229

2 recorded events


### User

_source line 3058 · 2026-05-21T13:09:51.524514+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

清理 PDF 渲染缓存。

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

_source line 3059 · 2026-05-21T13:09:56.835310+00:00_

Reviewer 1 报告已确认收录。继续等待 Reviewer 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 230

## Round 230

2 recorded events


### User

_source line 3060 · 2026-05-21T13:10:13.725458+00:00_

[Reviewer 2 审稿结果]:
正文恰好 8 页，格式合规。现在搜索可能遗漏的关键引用，并检查附录中的 SQL cross-task validation。

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

_source line 3061 · 2026-05-21T13:10:19.704294+00:00_

Reviewer 2 仍在进行引用搜索和附录验证，等待其完整报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 231

## Round 231

56 recorded events


### User

_source line 3062 · 2026-05-21T14:55:21.830586+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (Long Paper, via ARR)
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

_source line 3063 · 2026-05-21T14:55:40.276924+00:00_

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

_source line 3064 · 2026-05-21T14:55:40.378541+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3065 · 2026-05-21T14:55:46.044023+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3066 · 2026-05-21T14:55:46.094742+00:00_



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

_source line 3067 · 2026-05-21T14:56:11.956342+00:00_

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

_source line 3068 · 2026-05-21T14:56:12.910558+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (291 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_fewnerd_n16_s123 | FewNERD N=16 seed=123: second seed for N=16 scaling analysis. Tests whether doubling samples from N=8 to N=16 increases oracle headroom consistently across seeds, and whether MV aggregation gap widens or narrows. | — | — | — |\n| exp_fewnerd_n16_s42_v2 | FewNERD N=16 scaling: doubling sample count from N=8 to N=16 increases oracle headroom and tests whether additional samples improve MV aggregation or only expand the correlation-selection gap. | — | — | — |\n| exp_e2_pretrained_fewnerd_s123 | E2 pre-trained baseline seed 123: Qwen2.5-7B-Instruct (unfinetuned) on FewNERD SC pipeline N=8 T=1.0. Additional seed for E2 pre-trained baseline statistical power. If correlation-selection gap persists without fine-tuning → phenomenon is model-intrinsic. | — | — | — |\n\n## 待处理\n- exp_fewnerd_mf4_s456: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=456 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.（排队等待 GPU）\n- exp_fewnerd_mf4_s123: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=123 usin
…[truncated 1745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 3069 · 2026-05-21T14:56:12.910902+00:00_

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

_source line 3070 · 2026-05-21T14:56:12.911075+00:00_



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

_source line 3071 · 2026-05-21T14:56:14.314889+00:00_

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

_source line 3072 · 2026-05-21T14:56:14.366395+00:00_

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
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{The Capability Ceiling of Self-Consistency:\\ How Entity-Level Self-Verification Fails in Named Entity Recognition}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/diagnostic}
38	\input{sections/mechanistic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/background}
44	\input{sections/discussion}
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\section*{Ethics Statement}
51	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
52	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
53	No new human data was collected or annotated for this study.
54	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
55	Code and data will be released upon acceptance at [anonymized URL].
56	
57	\section*{Responsible NLP Research Checklist}
58	\in
…[truncated 186 chars]

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

_source line 3073 · 2026-05-21T14:56:23.400110+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 3074 · 2026-05-21T14:56:23.851541+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "5000"
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
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 3075 · 2026-05-21T14:56:30.442452+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

I've found relevant information about EMNLP 2026 call for papers and submission guidelines related to ARR. Here are the key findings:

## EMNLP 2026 Paper Submissions

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic
…[truncated 1005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7042
}
```

</details>

---


### Tool result

_source line 3076 · 2026-05-21T14:56:30.493504+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Experiment Memory\\n\\n## exp_e2_pretrained_fewnerd — Analysis (2026-05-21)\\n\\n### Setup\\n- Model: Qwen2.5-7B-Instruct (pretrained, no fine-tuning)\\n- Dataset: FewNERD (37,648 instances)\\n- SC pipeline: N=8, T=1.0, seed=42\\n\\n### Key Metrics\\n\\n| Metric | FewNERD | CoNLL (ref) |\\n|--------|---------|-------------|\\n| Greedy F1 | 0.5121 | 0.5385 |\\n| Oracle F1 | 0.6175 | 0.6275 |\\n| Oracle headroom | +0.1054 | +0.0890 |\\n| Fleiss κ (mean) | 0.4501 | 0.5470 |\\n| Soft Jaccard (mean) | 0.6881 | 0.7764 |\\n| Sample F1 (mean±std) | 0.523±0.332 | 0.581±0.384 |\\n| Sample F1=0 (%) | 18.2% | 23.4% |\\n| Full ρ(κ,F1) | +0.383 | +0.377 |\\n| Full ρ(SJ,F1) | +0.433 | +0.392 |\\n| Cond ρ(κ,F1) | +0.371 | +0.435 |\\n| Cond ρ(SJ,F1) | +0.440 | +0.467 |\\n| Structural > Surface | YES (+0.050) | YES (+0.015) |\\n| LP full ρ | +0.189 | -0.020 (ns) |\\n| LP full AUROC | 0.596 | 0.538 |\\n| LP cond ρ | +0.176 | +0.210 |\\n| LP cond AUROC | 0.593 | 0.580 |\\n| Verdict | PASS | MARGINAL |\\n\\n### Conclusion: SUCCESS\\n\\n**Correlation-selection gap confirmed on pretrained model.**\\n\\n1. **Gap exists**: Oracle F1 (0.618) exceeds Greedy F1 (0.512) by 10.5pp — substantial untapped selection potential in the 8 samples\\n2. **Agreement correlates with correctness**: ρ(SJ,F1) = +0.43 (p≈0), but this correlation does NOT close the gap via naive MV → classic correlation-selection gap\\n3. **Structural > Surface**: Soft Jaccard beats Fleiss κ as quality signal by +0.050 ρ — consistent across both datasets\\n4. **Logprob weak**: LP correlation exists (ρ=0.19) but much weaker than agreement-based signals — LP alone insufficient for selection\\n5. **Cross-dataset consistency**: Gap pattern replicates across FewNERD (37.6K instances) and CoNLL (3.5K instances), with FewNERD showing larger headroom and stronger structural 
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6641
}
```

</details>

---


### Tool call

_source line 3077 · 2026-05-21T14:56:35.518817+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline May ARR cycle page limit format"
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
    "query": "EMNLP 2026 submission deadline May ARR cycle page limit format"
  }
}
```

</details>

---


### Tool result

_source line 3078 · 2026-05-21T14:56:43.359575+00:00_

Web search results for query: "EMNLP 2026 submission deadline May ARR cycle page limit format"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"}]

Now let me search for the page limit and format information:

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underl
…[truncated 2537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7840
}
```

</details>

---


### Tool call

_source line 3079 · 2026-05-21T14:56:52.403289+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 3080 · 2026-05-21T14:56:52.496753+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 93
}
```

</details>

---


### Tool call

_source line 3081 · 2026-05-21T14:56:56.933680+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/docs/paper/sections/*.tex",
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
    "pattern": "**/struct_self_consist_ie/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 3082 · 2026-05-21T14:56:57.440791+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theoretical.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_ge
…[truncated 71 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 3083 · 2026-05-21T14:56:57.644799+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml",
  "limit": "80"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 3084 · 2026-05-21T14:56:57.695453+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.

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

_source line 3085 · 2026-05-21T14:57:01.659967+00:00_

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

_source line 3086 · 2026-05-21T14:57:02.111915+00:00_

1	\begin{abstract}
2	Test-time compute scaling through repeated sampling yields large gains on discrete-answer reasoning and code generation, yet for named entity recognition (NER), where outputs are entity sets with partial overlap, a persistent gap separates quality estimation from sample selection.
3	We ask whether entity-level agreement signals can bridge this gap.
4	Across nine method categories spanning diagnostic probes, selection/construction strategies, and learning-based approaches, we find that no entity-level agreement signal reliably improves selection.
5	Quality estimation signals correlate with oracle F1 ($\rho$ up to 0.47, AUROC up to 0.82) yet no signal selects better than greedy decoding.
6	The failure is systematic: a four-stage diagnostic cascade (quality estimation $\to$ degeneracy $\to$ agreement fidelity $\to$ log-probability compression) localizes where and how selection breaks down, with cross-task validation on RE and SQL parsing (87.2\% output degeneracy).
7	A hidden-state linear probe achieves entity-level discrimination (area under the ROC curve [AUROC] $0.63$\textendash$0.88$, dataset-dependent) from a single forward pass, consistently exceeding prompt-based self-evaluation (AUROC 0.51) but matching multi-sample agreement ($0.87$) only on the simplest task.
8	These negative results delineate where self-consistency (SC) does succeed for IE: through paths that bypass entity-level agreement.
9	Log-probability selection improves F1 by $+1.39$\,pp on Few-NERD (Holm-adjusted $p{=}0.021$, selection family $k{=}21$), entity-level construction via weighted voting gains $+1.02$\textendash$1.40$\,pp, and cross-model ensembles add $+0.42$\,pp on Few-NERD.
10	Each exploits sequence-level or cross-model signals rather than entity-level self-verification.
11	Strict majority vote fails to improve F1 on any dataset ($\Delta$ from $-2.7$ to ${\approx}0$\,pp); a degeneracy decomposition confirms gain vanishes once output degeneracy exceeds 70\%.
12	\end{a
…[truncated 78 chars]

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

_source line 3087 · 2026-05-21T14:57:02.112421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "limit": "80"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 3088 · 2026-05-21T14:57:02.112826+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling complements model scaling \cite{snell2025scaling}: repeated sampling with majority voting \cite{wang2023selfconsistency}, best-of-$N$ with learned verifiers \cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \cite{muennighoff2025s1} produce large gains on reasoning and code generation.
4	These successes share a structural prerequisite: the output space admits either exact equivalence classes (multiple-choice, numeric answers) or execution-based verification (code).
5	Named entity recognition (NER) breaks both assumptions.
6	The output is a set of typed entities; two samples from the same input routinely extract overlapping but non-identical sets, and no external oracle can adjudicate correctness at test time.
7	Without equivalence classes, majority voting reduces to heuristic frequency counting; without a verifier, best-of-$N$ requires a reliable proxy signal.
8	This structural mismatch raises a concrete question: can self-consistency signals that estimate quality well for reasoning tasks also \textit{select} better outputs or \textit{construct} better entity sets for NER?
9	We investigate this question for NER and validate the core findings on SQL parsing, treating NER as a representative instance of the broader set-valued generation problem.
10	
11	The question has practical stakes beyond information extraction.
12	Hallucination detection methods such as SelfCheckGPT \cite{manakul2023selfcheckgpt} and FActScore \cite{min2023factscore} rely on cross-sample consistency to verify individual claims: if a model's outputs agree, the shared content is presumed factual.
13	This reasoning assumes entity-level self-verification works, that a model can reliably distinguish correct extractions from incorrect ones through self-judgment or re-prompting.
14	We show this assumption fails.
15	Three independent probes (entity self-judgment, multi-round re-prompting, latent-space 
…[truncated 4688 chars]

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

_source line 3089 · 2026-05-21T14:57:02.816314+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/agent/*.yaml",
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
    "pattern": "**/struct_self_consist_ie/agent/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 3090 · 2026-05-21T14:57:02.917070+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3091 · 2026-05-21T14:57:09.042677+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/config*.yaml",
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
    "pattern": "**/struct_self_consist_ie/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 3092 · 2026-05-21T14:57:09.143435+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3093 · 2026-05-21T14:57:12.959281+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/config*",
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
    "pattern": "**/struct_self_consist_ie/**/config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 3094 · 2026-05-21T14:57:13.210656+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/pygments/lexers/configs.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_
…[truncated 14053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 3095 · 2026-05-21T14:57:19.232334+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "*.yaml",
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
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "glob": "*.yaml",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 3096 · 2026-05-21T14:57:19.693455+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 461
}
```

</details>

---


### Tool call

_source line 3097 · 2026-05-21T14:57:19.844377+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/projects.yaml",
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
    "pattern": "**/projects.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 3098 · 2026-05-21T14:57:19.998655+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 154
}
```

</details>

---


### Tool call

_source line 3099 · 2026-05-21T14:57:24.213499+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
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
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3100 · 2026-05-21T14:57:24.315108+00:00_

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
…[truncated 12109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3101 · 2026-05-21T14:57:29.864455+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/constraints.yaml",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/constraints.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 3102 · 2026-05-21T14:57:30.320911+00:00_

1	_next_id: 2
2	constraints:
3	- id: C001
4	  added: 2026-05-16 03:03 UTC
5	  summary: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/
6	    下的 tex 文件
7	  scope: worker
8	  reason: 两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker
9	    + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 3103 · 2026-05-21T14:57:30.321333+00:00_

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

_source line 3104 · 2026-05-21T14:57:30.775015+00:00_

1	issues:
2	  # ===== 历史 resolved issues (保留) =====
3	  - id: "R1-W1"
4	    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
5	    category: experiment
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 19
10	    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
11	    resolution_round: 19
12	
13	  - id: "R1-W2"
14	    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
15	    category: framing
16	    severity: critical
17	    status: resolved
18	    first_raised_round: 1
19	    last_seen_round: 21
20	    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
21	    resolution_round: 21
22	
23	  - id: "R2-N1-old"
24	    summary: "Contribution 1 'methodological premise' 是定义推论"
25	    category: framing
26	    severity: critical
27	    status: resolved
28	    first_raised_round: 1
29	    last_seen_round: 19
30	    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
31	    resolution_round: 19
32	
33	  - id: "R2-N2-old"
34	    summary: "与 MBR 文献差异化定位不够锐利"
35	    category: framing
36	    severity: warning
37	    status: resolved
38	    first_raised_round: 1
39	    last_seen_round: 19
40	    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
41	    resolution_round: 19
42	
43	  - id: "R2-N4-old"
44	    summary: "模型规模 3B-8B，70B+ 未知"
45	    category: experiment
46	    severity: info
47	    status: resolved
48	    first_raised_round: 1
49	    last_seen_round: 19
50	    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 3105 · 2026-05-21T14:57:31.076303+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
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
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3106 · 2026-05-21T14:57:31.279807+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7_consistency.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_16.md
/home/ubu
…[truncated 1277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 3107 · 2026-05-21T14:57:45.561236+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "glob": "*.yaml",
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
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
    "glob": "*.yaml",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 3108 · 2026-05-21T14:57:45.785623+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 224
}
```

</details>

---


### Tool call

_source line 3109 · 2026-05-21T14:57:49.891481+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview\"",
  "path": "/home/ubuntu/agent-ml-research",
  "glob": "*.yaml",
  "output_mode": "files_with_matches",
  "head_limit": "5"
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
    "pattern": "external_review|paperreview\"",
    "path": "/home/ubuntu/agent-ml-research",
    "glob": "*.yaml",
    "output_mode": "files_with_matches",
    "head_limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 3110 · 2026-05-21T14:57:49.942732+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3111 · 2026-05-21T14:58:37.024911+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "你是 Reviewer 1，负责审查方法严谨性和实验设计。\n\n## 论文信息\n- 标题: \"The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\"\n- 目标 venue: EMNLP 2026（通过 ARR 统一审稿）\n- 投稿类别: Main Conference, Long Paper\n- Deadline: 2026-05-25\n- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex\n- PDF 路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\n\n## Venue 格式要求\n- 页数限制: 正文 8 页（不含 references），Limitations 和 Ethics 不计入页数（但不得包含过多额外内容）\n- 模板: ACL 2-column (acl.sty, review mode)\n- 匿名规则: Double-blind\n- 引用格式: natbib\n- 附录: 允许，但不保证审稿人会阅读\n- 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点关注：\n\n1. **诊断框架逻辑**：四阶段级联（QE → degeneracy → agreement fidelity → LP compression）是否逻辑自洽，每个阶段的因果推断是否站得住脚\n2. **统计检验**：所有 p 值、Holm 校正、置信区间是否正确使用，多重比较是否充分控制\n3. **实验覆盖度**：4 个 NER 数据集 × 2 个模型族 × 不同 N 值是否充分；cross-task validation（RE, SQL）是否有说服力\n4. **表格/数字一致性**：正文中引用的数字是否与表格一致，表格之间是否互相矛盾\n5. **消融设计**：9 种方法类别的消融是否公平、完整，是否有遗漏的 baseline\n6. **Hidden-state probe**：GroupKFold CV 设计是否存在数据泄露风险，AUROC 0.63-0.88 的 variance 来源是否充分解释\n7. **负面结果的说服力**：声称 \"no method works\" 需要极高的证据标准——是否穷尽了合理的方法空间\n8. **Prescriptive escape routes**：LP-weighted construction +1.02-1.40pp、cross-model ensemble +0.42pp 的效果量是否有实际意义\n\n请提供完整的结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues。每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
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
    "text": "你是 Reviewer 1，负责审查方法严谨性和实验设计。\n\n## 论文信息\n- 标题: \"The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\"\n- 目标 venue: EMNLP 2026（通过 ARR 统一审稿）\n- 投稿类别: Main Conference, Long Paper\n- Deadline: 2026-05-25\n- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex\n- PDF 路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\n\n## Venue 格式要求\n- 页数限制: 正文 8 页（不含 references），Limitations 和 Ethics 不计入页数（但不得包含过多额外内容）\n- 模板: ACL 2-column (acl.sty, review mode)\n- 匿名规则: Double-blind\n- 引用格式: natbib\n- 附录: 允许，但不保证审稿人会阅读\n- 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点关注：\n\n1. **诊断框架逻辑**：四阶段级联（QE → degeneracy → agreement fidelity → LP compression）是否逻辑自洽，每个阶段的因果推断是否站得住脚\n2. **统计检验**：所有 p 值、Holm 校正、置信区间是否正确使用，多重比较是否充分控制\n3. **实验覆盖度**：4 个 NER 数据集 × 2 个模型族 × 不同 N 值是否充分；cross-task validation（RE, SQL）是否有说服力\n4. **表格/数字一致性**：正文中引用的数字是否与表格一致，表格之间是否互相矛盾\n5. **消融设计**：9 种方法类别的消融是否公平、完整，是否有遗漏的 baseline\n6. **Hidden-state probe**：GroupKFold CV 设计是否存在数据泄露风险，AUROC 0.63-0.88 的 variance 来源是否充分解释\n7. **负面结果的说服力**：声称 \"no method works\" 需要极高的证据标准——是否穷尽了合理的方法空间\n8. **Prescriptive escape routes**：LP-weighted construction +1.02-1.40pp、cross-model ensemble +0.42pp 的效果量是否有实际意义\n\n请提供完整的结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues。每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
  }
}
```

</details>

---


### Tool result

_source line 3112 · 2026-05-21T14:58:50.038161+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13013
}
```

</details>

---


### Tool call

_source line 3113 · 2026-05-21T14:58:52.851487+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "你是 Reviewer 2，负责审查新颖性和完整性。\n\n## 论文信息\n- 标题: \"The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\"\n- 目标 venue: EMNLP 2026（通过 ARR 统一审稿）\n- 投稿类别: Main Conference, Long Paper\n- Deadline: 2026-05-25\n- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex\n- PDF 路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\n\n## Venue 格式要求\n- 页数限制: 正文 8 页（不含 references），Limitations 和 Ethics 不计入页数（但不得包含过多额外内容）\n- 模板: ACL 2-column (acl.sty, review mode)\n- 匿名规则: Double-blind\n- 引用格式: natbib\n- 附录: 允许，但不保证审稿人会阅读\n- 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**新颖性 + 完整性**，重点关注：\n\n1. **贡献定位**：4 个 contribution 是否真正新颖？\"correlation-selection gap\" 概念在 MBR/self-consistency 文献中是否已有类似发现？\n2. **Related Work 覆盖**：是否遗漏了 key references？特别是：\n   - MBR decoding for structured prediction\n   - Self-verification / self-evaluation in LLMs（SelfCheckGPT, FActScore 之外）\n   - Entity-level confidence estimation\n   - Test-time compute scaling 最新工作\n   - Structured output generation with LLMs\n3. **叙事逻辑**：论文从 \"SC fails for NER\" 到 \"prescriptive escape routes\" 的叙事弧是否流畅？Introduction 的 claim 是否被后续实验充分支持？\n4. **负面结果论文的价值**：对 EMNLP community 的启发性如何？是否仅仅是 \"X doesn't work\" 还是提供了深层理解？\n5. **格式合规**：\n   - 正文是否超过 8 页限制？\n   - Double-blind 匿名是否完整（无作者信息泄露、无 GitHub 链接、无 \"our previous work\" 等）？\n   - Limitations section 是否存在且内容充分？\n   - References 格式是否一致（会议名 vs 缩写、年份、页码）？\n6. **写作质量**：术语一致性、图表标注清晰度、符号使用规范性\n7. **Missing references**：列出你认为应该引用但未引用的重要工作\n\n请提供完整的结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
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
    "text": "你是 Reviewer 2，负责审查新颖性和完整性。\n\n## 论文信息\n- 标题: \"The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\"\n- 目标 venue: EMNLP 2026（通过 ARR 统一审稿）\n- 投稿类别: Main Conference, Long Paper\n- Deadline: 2026-05-25\n- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex\n- PDF 路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\n\n## Venue 格式要求\n- 页数限制: 正文 8 页（不含 references），Limitations 和 Ethics 不计入页数（但不得包含过多额外内容）\n- 模板: ACL 2-column (acl.sty, review mode)\n- 匿名规则: Double-blind\n- 引用格式: natbib\n- 附录: 允许，但不保证审稿人会阅读\n- 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**新颖性 + 完整性**，重点关注：\n\n1. **贡献定位**：4 个 contribution 是否真正新颖？\"correlation-selection gap\" 概念在 MBR/self-consistency 文献中是否已有类似发现？\n2. **Related Work 覆盖**：是否遗漏了 key references？特别是：\n   - MBR decoding for structured prediction\n   - Self-verification / self-evaluation in LLMs（SelfCheckGPT, FActScore 之外）\n   - Entity-level confidence estimation\n   - Test-time compute scaling 最新工作\n   - Structured output generation with LLMs\n3. **叙事逻辑**：论文从 \"SC fails for NER\" 到 \"prescriptive escape routes\" 的叙事弧是否流畅？Introduction 的 claim 是否被后续实验充分支持？\n4. **负面结果论文的价值**：对 EMNLP community 的启发性如何？是否仅仅是 \"X doesn't work\" 还是提供了深层理解？\n5. **格式合规**：\n   - 正文是否超过 8 页限制？\n   - Double-blind 匿名是否完整（无作者信息泄露、无 GitHub 链接、无 \"our previous work\" 等）？\n   - Limitations section 是否存在且内容充分？\n   - References 格式是否一致（会议名 vs 缩写、年份、页码）？\n6. **写作质量**：术语一致性、图表标注清晰度、符号使用规范性\n7. **Missing references**：列出你认为应该引用但未引用的重要工作\n\n请提供完整的结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
  }
}
```

</details>

---


### Tool call

_source line 3114 · 2026-05-21T14:58:53.152867+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3115 · 2026-05-21T14:58:54.309176+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool result

_source line 3116 · 2026-05-21T14:58:56.077795+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2924
}
```

</details>

---


### Assistant

_source line 3117 · 2026-05-21T14:59:01.656656+00:00_

圆桌审稿已启动：

- **Reviewer 1**（方法严谨性 + 实验设计）：已派发 ✓
- **Reviewer 2**（新颖性 + 完整性）：已派发 ✓
- **视觉审查 Agent**：已启动 ✓
- **外部审稿**：未配置，跳过

等待 Reviewer 返回初审报告。收到后将进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 232

## Round 232

2 recorded events


### User

_source line 3118 · 2026-05-21T15:09:20.287641+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性 + 完整性

**论文**: "The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition"
**Venue**: EMNLP 2026 (ARR)
**类别**: Main Conference, Long Paper

---

## 总体评分

**Overall**: 3.5 — Borderline Conference
**一句话总结**: 一篇执行扎实的负面结果诊断研究，提出了有用的"correlation-selection gap"概念框架，但核心发现的新颖性有限（SC 对结构化预测效果差在 MBR 文献中已有先兆），且关键统计结果在严格多重比较校正下未能存活。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论整体严谨（Holm-Bonferroni 校正、bootstrap CI、TOST 等价检验），但核心 claim 在全局校正下 p_adj=0.055 未达显著；SciERC 仅 n=529 且 seed 敏感性 σ=0.48 pp；部分 escape route 增益在噪声范围内 |
| Excitement | 3/5 | 诊断框架（4-stage cascade）是有用的概念贡献，但"SC 对结构化输出效果差"对熟悉 MBR 文献的读者并不意外；escape routes 增益微弱（+1.0–1.4 pp）；负面结果价值中等 |
| Reproducibility | 4/5 | 实验细节充分，checklist 完整，承诺代码开源；超参数、训练配置、评估协议均有记录 |
| Overall Assessment | 3.5/5 | Borderline Conference — 执行质量高但新颖性中等，更适合 Findings |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心统计 claim 的稳健性不足
- 具体位置：Section 7.5 (Table 5)、Appendix f (Table 13)
- 问题：论文承认在全局 Holm-Bonferroni 校正（k=57）下，"no core NER claim survives"（p_adj=0.055 for Few-NERD LP selection and construction）。论文转而报告 per-family 校正（selection k=21, construction k=10），但 per-family 分割本身是事后决定，削弱了统计严谨性。Few-NERD LP selection 的 per-family p_adj=0.021 是唯一正面结果，而 SciERC construction 的 p_adj=0.20 不显著。
- 为什么影响接收：论文 4 个 contribution 中的第 4 个（"prescriptive escape routes"）依赖这些统计结果。如果核心正面结果在合理的多重比较校正下不显著，那么"escape routes"的贡献就被大幅削弱，论文变成纯负面结果 + 诊断框架。
- 建议修改方向：(1) 在正文中明确讨论全局 vs per-family 校正的取舍，而非仅在 Appendix f 披露；(2) 预注册 hypothesis families 或提供更强的 justification；(3) 考虑用 permutation test 或 Bayesian 方法补充频率主义检验。

**N2** [critical] "Correlation-selection gap" 概念的新颖性定位不够精准
- 具体位置：Section 1 (lines 94–95)、Section 4、Section 8
- 问题：论文将 "correlation-selection gap" 作为核心概念贡献，但未充分区分与 MBR 文献中已知发现的关系。Eikema & Aziz (2020, 2022) 已经证明 MAP decoding 的不足，Eikema et al. (2025) 明确指出 MBR utilities 在结构化输出上表现退化。论文的 Related Work (Section 8, lines 533–548) 讨论了 MBR 但主要聚焦于 utility function 选择，未明确论证 "correlation-selection gap" 相比 "MBR utility degrade on structured outputs" 的增量贡献。Instance-level signal 的设计性局限（4/5 信号是 instance-level 因此无法区分 per-sample 候选，Section 2.1 lines 162–173）更像是方法设计问题而非深层发现。
- 为什么影响接收：新颖性是论文能否从 Findings 升级到 Main Conference 的关键判据。如果核心概念在先行工作中已有类似表述，贡献定位就需要更精确。
- 建议修改方向：(1) 在 Related Work 中增加一段 explicit comparison，说明 MBR utility degradation (Eikema et al., 2025) 与 correlation-selection gap 的区别和联系；(2) 强调诊断 cascade 的增量价值——MBR 文献指出问题存在，本文定位问题在哪个环节发生（degeneracy vs. LP compression），这是真正的新贡献。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 模型覆盖范围有限，泛化性声明过度
- 具体位置：Section 7.1 (lines 425–431)、Limitations (lines 600–618)
- 问题：完整实验仅覆盖 Qwen3-8B 和 LLaMA-3.1-8B（均为 LoRA 微调）。72B zero-shot 扩展仅在 Few-NERD 上进行，GPT-5.5 仅 200 实例。论文在 Limitations 中承认 frontier API models（Claude Sonnet 4, DeepSeek Chat）表现出不同的 degeneracy profiles（4% vs 5.5%），"findings from fine-tuned open-weight models may not fully generalize to proprietary systems"（lines 619–624）。但 Introduction 和 Conclusion 的措辞（如 "persistent gap"、"capability ceiling"）暗示普遍性结论。
- 建议：弱化泛化性措辞，明确区分 "fine-tuned open-weight models under constrained decoding" 和一般性结论；或增加至少一个 proprietary model 的完整实验。

**W2** [warning] Cross-task validation 较薄弱
- 具体位置：Section 1 (lines 125–126)、Appendix o
- 问题：RE 验证仅在 SciERC 一个数据集上进行，且 RE F1 被 entity span errors 严重干扰（55.5% 的 zero-F1 RE instances 来自 span 错误，footnote 1）。SQL parsing 仅提到 87.2% degeneracy 但缺乏系统分析。论文声称 NER 是 "broader set-valued generation problem" 的代表（line 68），但跨任务证据不够支撑这一定位。
- 建议：(1) 如果 RE 数据受 span 错误污染严重，应讨论这对 cross-task validation 的影响；(2) SQL parsing 需更详细的分析或降低 cross-task generalization 的 claim。

**W3** [warning] 遗漏直接相关的参考文献
- 具体位置：Section 8 (Related Work)
- 问题：以下工作与本文高度相关但未被引用：
  1. **Ma et al. (2024) "Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models" (NAACL 2024)** — 直接使用 self-consistency 进行 NER annotation selection，是对 SC 在 NER 上应用的直接先行工作，论文应讨论其发现与本文的关系
  2. **Madaan et al. (2023) "Self-Refine: Iterative Refinement with Self-Feedback" (NeurIPS 2023)** — 论文测试了 Multi-Round Self-Consistency (MRSC, Section 3)，但未引用最相关的 iterative self-refinement 基准工作
- 为什么重要：Ma et al. (2024) 在 zero-shot NER 中使用 SC 获得正面结果，与本文负面结果形成有意义的对比（zero-shot vs fine-tuned、annotation selection vs output selection），遗漏可能被 reviewer 视为 related work 不完整。
- 建议：在 Section 8 "Consistency for structured IE" 段中加入讨论。

**W4** [warning] Escape routes 的实用价值定位模糊
- 具体位置：Section 7.5 (Table 5)、Section 9 (Discussion, lines 569–580)
- 问题：Entity-level construction 的最佳结果是 +1.40 pp on Few-NERD（但 cost 是 N×），cross-model ensemble 是 +0.42 pp。Discussion 中论文承认 "the trade-off (N× cost for ≈1 pp) may only justify safety-critical use"（lines 575–576）。对于 EMNLP 社区，≈1 pp 的改进在多数应用场景下可忽略不计，且 entity-level construction 前提（degeneracy < 22%）限制了适用范围。论文应更清楚地定位这些 escape routes 是理论洞见（证明问题可解）还是实用方案。
- 建议：明确区分 "proof of concept"（degeneracy 是瓶颈，绕过它可以获得增益）和 "practical recommendation"。

---

## 小问题（不影响接收）

1. **Table 1 标注不一致**：LP 标注为 "per-sample" 而其他为 "consensus-proximity"，但 ρ 列对 EM 和 VC 标注 "n/a†" 而 footnote † 解释 "One score per input"——与 Section 2.1 的 instance-level vs per-sample 区分重复，建议统一措辞。

2. **Proposition 1 的 notation**：M⁺ = ŷ_MV \ ŷ_gr 的定义假设 MV 结果是 greedy 的超集加上额外实体，但 MV 也可能删除 greedy 中的实体（频率 < θ 的实体被移除）。Proposition 1(a) 只讨论了 degenerate instances (Δ F1 = 0) 而未讨论 MV 删除正确实体的负面场景。

3. **Figure 1 信息密度过高**：三个 panel 各包含多个概念层次，caption 需要 4 行才能解释。建议拆分或简化，使 key message 更直观。

4. **Appendix 体量**：附录从第 14 页延伸到第 47 页（约 34 页），远超正文。部分分析（如 Appendix g diversity analysis、Appendix e bootstrap CI）对支撑核心 claim 至关重要，建议将最关键的证据整合到正文。

5. **引用格式小问题**：verify_references 工具检测到 snell2025scaling 的 bib key 用姓氏 "snell" 但 API 匹配到 first name "charlie"，这是 bib 格式常见问题，不影响正确性。

---

## 主要优势

1. **诊断框架设计优秀**：四阶段 cascade（QE → degeneracy → agreement fidelity → LP compression）提供了系统化的诊断路径，超越了简单的 "X doesn't work" 负面结果。Proposition 1 的 degeneracy decomposition 给出了理论上界，实验验证了 bound 的 tightness（3–12% of actual gains, Section 6.3, Figure 9）。

2. **实验设计全面且统计处理严谨**：4 个 NER benchmarks 覆盖不同难度梯度，9 种方法类别的系统比较，TOST 等价检验（Appendix g）、Holm-Bonferroni 校正（Appendix f）、bootstrap CI（Appendix e）等统计工具的使用体现了高标准的实证研究。

3. **Introspection gap 是有趣的发现**：hidden-state probe（AUROC 0.63–0.88）超越 prompt-based self-judgment（0.51）但低于 multi-sample agreement（0.87, 仅在最简单的 CoNLL 上），揭示了模型内部表示包含 prompt 接口无法访问的质量信息（Section 3, lines 241–267）。

4. **写作质量高**：术语一致，叙事逻辑清晰（从问题定义 → 诊断 → 失败分析 → 逃逸路径），信息密度大但不混乱。Limitations 坦诚且具体。

5. **对社区的实际指导价值**：论文明确了在何种条件下 SC 可能有效（degeneracy < 22%、足够的 oracle headroom）、何种条件下注定失败（degeneracy > 70%），这对从业者选择推理策略有直接参考价值。

---

## Missing References（建议引用）

1. **Ma, Wang, Sun & Li (2024). "Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models." NAACL 2024.** — 直接使用 SC 进行 NER，获得正面结果，是本文最相关的先行工作之一。

2. **Madaan, Tandon, Gupta et al. (2023). "Self-Refine: Iterative Refinement with Self-Feedback." NeurIPS 2023.** — 本文的 MRSC 方法与 Self-Refine 的 iterative refinement 范式直接相关。

3. **Wei, Wang, Schuurmans et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." NeurIPS 2022.** — SC 的前置工作（CoT），虽然 Wang et al. 2023 已引用，但 CoT 作为 SC 的基础应被 acknowledge。

4. **Survey: "Test-time Scaling of LLMs: A Survey from A Subproblem Structure Perspective" (2025, arXiv:2511.14772)** — 本文的 §6.2 讨论了 scaling behavior，该 survey 提供了更完整的 TTS 分类框架，有助于定位本文的 inverse scaling 发现。

---

## 总结

这是一篇执行质量高的诊断性研究，提出了有用的 correlation-selection gap 概念和四阶段诊断框架。主要弱点在于：(1) 核心统计结果在严格校正下不稳健；(2) 概念新颖性相对 MBR 文献的增量定位不够清晰；(3) escape routes 的实用价值有限。论文适合 Findings 级别发表，如果能加强 N1（统计稳健性）和 N2（新颖性定位）的论证，有可能提升到 Borderline Conference。

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

_source line 3119 · 2026-05-21T15:09:30.197320+00:00_

Reviewer 2 报告已收到（3.5 Borderline Conference）。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 233

## Round 233

2 recorded events


### User

_source line 3120 · 2026-05-21T15:09:43.001405+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**评分摘要**：
- **Overall**: 3.5（Borderline Conference）
- **Soundness**: 3.5/5 — 方法论严谨但核心 claim 在全局 Holm-Bonferroni 校正下 p_adj=0.055 未达显著
- **Excitement**: 3/5 — 诊断框架有价值但核心发现对 MBR 领域不意外，escape routes 增益微弱

**2 个 Must-Fix**：
1. 核心统计结果（escape routes）在严格多重比较校正下不稳健，正文应正面讨论而非仅 Appendix 披露
2. "Correlation-selection gap" 与 MBR 文献已知发现的增量新颖性需要更精确定位

**4 个 Should-Fix**：模型覆盖有限（仅 8B fine-tuned）、cross-task validation 薄弱（RE 受 span 错误污染）、遗漏关键参考文献（Ma et al. NAACL 2024, Madaan et al. NeurIPS 2023）、escape routes 实用价值定位模糊

**主要优势**：四阶段诊断 cascade 设计优秀、统计处理全面（TOST/bootstrap/Holm-Bonferroni）、introspection gap 是有趣发现、写作质量高。

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

_source line 3121 · 2026-05-21T15:09:48.186498+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 234

## Round 234

6 recorded events


### User

_source line 3122 · 2026-05-21T15:11:42.301799+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：方法严谨性与实验设计

**论文**: "The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition"
**Venue**: EMNLP 2026 (via ACL ARR)
**审查侧重**: 方法严谨性 + 实验设计

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 一项方法论扎实、覆盖极其全面的诊断性实证研究，对 NER 领域 self-consistency 的局限性提供了系统性解释，但负面结果的实际影响有限，理论贡献的实际预测力偏弱，"escape routes"效果量小。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 (Strong) | 方法论严谨，核心 claims 有充分实验支撑；四阶段级联逻辑自洽；统计检验规范（Holm-Bonferroni 57 项、bootstrap CI、TOST 等量性检验）；但因果推断力度不足（承认为 correlational，非 interventional） |
| Excitement | 3/5 (Interesting) | 对社区有价值的负面结果——系统性地证明了9类方法都无法在 NER 上让 SC 超越 greedy；MBR 理论联系有新意；但实际可操作建议有限，escape routes 效果量 1-1.4pp |
| Overall | 3.5 | Borderline Conference：工作质量高于一般 Findings 论文，但负面结果的影响力和建设性贡献使其难以达到主会议 "4" 的水准 |
| Reproducibility | 5/5 | 极优：Appendix Table 21 列出全部超参数，47页附录含62张表，承诺释放代码和数据，NLP Checklist 完整填写 |
| Reviewer Confidence | 4/5 | 对 self-consistency、NER evaluation、统计方法论有充分了解；已通读全部47页 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **诊断级联的因果推断力度不足，与标题"Capability Ceiling"的强 claim 不匹配**
- 具体位置：§3-4 (诊断框架)，Limitations (p.8)
- 问题：四阶段级联 (QE → degeneracy → agreement fidelity → LP compression) 基于观察性关联建立，但标题声称发现了"capability ceiling"。论文在 Figure 1 caption 中谨慎标注"diagnostic sequence, not causal chain"，但正文叙事 (e.g., §4 "Where Single-Sample Selection Fails", §6.3 degeneracy decomposition) 隐含因果方向性。Limitations 承认"not interventional: we have not performed controlled interventions"，但这一关键限制被埋在第8页末尾，与标题的强 claim 形成张力。
- 为什么影响接收：审稿人和读者可能将诊断结论误读为因果结论。如果 degeneracy 和 LP compression 只是相关而非因果，则"ceiling"的说法缺乏根基——可能存在未测试的干预（如 diversity-encouraging decoding、contrastive sampling）能同时降低 degeneracy 和拓宽 LP range。
- 建议修改方向：(1) 在 §1 或 §3 引言处明确声明诊断框架是 observational 而非 causal；(2) 将标题从"Capability Ceiling"改为更准确的表述（如"Diagnostic Analysis of Self-Consistency Failure"），或在正文中提供至少一个 controlled intervention 来支撑"ceiling"的 claim（如人工注入 diversity 看是否打破 ceiling）。

**N2** [critical] **Free-form decoding 消融实验覆盖不完整，削弱了 LP compression 作为独立瓶颈的论证**
- 具体位置：Appendix q (p.27), Table 47-48
- 问题：LP compression 被诊断为第四阶段瓶颈，但 free-form decoding 消融仅在 CoNLL NER 和 Few-NERD INTRA 上执行，**未覆盖论文主要基准 SciERC**。SciERC 是论文中 construction gain 最大的数据集 (+1.40pp, Table 2)，也是大部分诊断分析的主场景。论文在 Table 22 (p.23) 报告 SciERC 的 within-instance LP range 仅 0.041 nats（主要在 constrained decoding 下测量），但未验证 SciERC 在 free-form 下 LP range 是否确实拓宽、以及拓宽后 selection 是否仍然失败。
- 为什么影响接收：如果 SciERC 在 free-form decoding 下 selection 能够改善，则"LP compression is the bottleneck"的结论对这个关键数据集不成立，整个级联的普适性受到质疑。
- 建议修改方向：补充 SciERC 的 free-form decoding 实验（至少 single-seed），报告 LP range、selection Δ 和 construction Δ。这是可以在短期内完成的实验。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **理论贡献（MBR 等价、degeneracy bound）的实际预测力有限**
- 具体位置：§6.3, Corollary 1, Table 30 (p.26/41)
- 问题：Corollary 1 给出 SC gain 的必要条件 (D > threshold → Δ < 0)，Table 30 验证了16个配置。但 bound 仅捕获实际 gain 的 5-12%（actual/bound ratio 3-12×），论文归因于"α (signal alignment) is the bottleneck: the best signal recovers only 6.8% of the non-degenerate oracle gap"。这意味着 MBR 框架虽然提供了 qualitative insight，但 quantitative bound 过松，对实际决策（e.g., 给定 D 和 α 能否预测 SC 是否有效）指导有限。
- 建议：(1) 在 §6.3 讨论 bound 的 tightness 和失败条件；(2) 讨论是否存在更紧的 bound（例如通过条件化 entity 类型或 dataset 特征）。

**W2** [warning] **Hidden-state probe 的跨数据集方差未充分解释**
- 具体位置：§3 (p.3-4), Appendix h.3 (p.21)
- 问题：Hidden-state probe AUROC 从 SciERC 的 0.63 到 CoNLL 的 0.88 变化剧烈。论文将此归因为"dataset-specific rather than universal encoding"（p.21），且 cross-dataset transfer drops（Few-NERD→CoNLL=0.759, CoNLL→Few-NERD=0.671）。但未深入分析是什么让 CoNLL 的 hidden states 更加可分（entity 类型粒度？类型数量？数据分布？）。如果 probe 在某些条件下表现良好 (AUROC=0.88)，那么"ceiling"是条件性的而非绝对的——高 AUROC 理论上应该能转化为 selection gain，但论文报告 CoNLL 上 probe 仍然不能改善 selection（Table 17, p.39 shows hidden-state probe ρ, but no selection Δ for CoNLL probe specifically）。
- 建议：(1) 提供 CoNLL 上 hidden-state probe 的 selection Δ 以及与 AUROC 0.88 的对照分析；(2) 讨论为什么高 AUROC 不能转化为 selection gain（是因为 AUROC→ranking quality 的gap，还是 ranking→selection 的gap？）。

**W3** [warning] **Escape routes 的效果量可能缺乏实际意义**
- 具体位置：§5 (p.5), Table 2, Table 61 (p.46)
- 问题：三个 escape routes 的效果量：LP-weighted construction +1.02-1.40pp, cross-model ensemble +0.42pp, LP selection +1.39pp（仅 Few-NERD）。考虑到这些方法需要 N× 到 2N× 的推理成本，以及 SciERC greedy F1 仅 ~0.529，+1.40pp 将其提升到 ~0.543——这在实际应用中是否 justify 了 8× 的推理开销？Table 61 的 cost-benefit 分析列出了每种方法的 verdict，但未量化 compute-accuracy Pareto 曲线。
- 建议：(1) 添加 cost-effectiveness 的定量分析（如 pp/dollar 或 pp/FLOP）；(2) 讨论在什么应用场景下 +1.4pp 是有实际价值的（如 high-stakes medical NER vs. commodity extraction）。

**W4** [warning] **N-scaling 范围对负面结论的支撑力有限**
- 具体位置：§6.1 (p.6), Appendix s (p.28), Figure 10 (p.28)
- 问题：主实验使用 N=8，scaling 分析扩展到 N=32。论文引用 Brown et al. (2024) "Large Language Monkeys" 证明在 reasoning 任务上 N 可以极大提升 coverage，但 NER 的 N-scaling 分析止步于 N=32。Figure 10 显示 oracle F1 follows F₁(N) = a - b·N^(-c) with R²>0.999，但 degeneracy 在 N=32 时仍为 ~13% (SciERC)。如果将 N 扩大到 100+（在 Brown et al. 的 setting 下 coverage 提升显著），degeneracy 是否会显著下降？论文在 Appendix s 承认"additional samples stabilize structural signals but capture less than 5% of the available improvement"，但这是在 N≤32 范围内的观察。
- 建议：即使不做 N=100 的实验，也应在 §6.1 讨论 Figure 10 的 scaling law 外推到 N=100 时 degeneracy 的预测值，并分析是否存在 regime change 的可能。

**W5** [warning] **Cross-model ensemble 仅测试了2个模型族，结论可能偏保守**
- 具体位置：§5.1 (p.5), Table 2
- 问题：Cross-model SC 仅测试 Qwen3-8B + LLaMA-3.1-8B 的组合，gain +0.42pp。这两个模型都是在相同协议下 fine-tune 的（LoRA via LLaMA Factory, Table 21），共享训练流程可能限制了 diversity 的上限。如果使用架构差异更大的模型组合（如 encoder-decoder vs. decoder-only，或不同 fine-tuning 方法如 full fine-tune vs. LoRA），diversity 可能更高，从而突破当前 +0.42pp 的 ceiling。
- 建议：讨论 model diversity 的上限问题——当前 +0.42pp 是由于模型数量不够（2个）还是由于 NER 任务本身限制了 diversity？引用 Yun et al. (2025) "Price of Format" 的 diversity collapse 论证是否也适用于 cross-model 场景。

---

## 小问题（不影响接收）

- **M1**: Table 1 (p.4) 的 caption 说"One score per input"，但 LP row 的 footnote 说"LP is per-sample"——应在 caption 中直接说明而不是依赖 footnote。
- **M2**: §2.2 (p.3) 定义了4种 confidence signals (SJ, FK, EM, VC)，但 LP 作为第5种直到 §2.3 才引入且标注为"the sole model-internal, per-sample signal"。建议在 §2.2 统一介绍所有5种信号。
- **M3**: Appendix f (p.18) 的 Holm-Bonferroni 全局校正导致核心 claims 均不显著（"no core NER claim survives"），但正文 §7.5 使用 per-family 校正。这一差异在正文中未充分说明——读者可能只看正文而得到"statistically significant"的印象，看到附录后又发现全局校正不显著。建议在 §7.5 添加一句指向 Appendix f 的说明。
- **M4**: 引用验证发现 `lightman2024verify` ("Let's Verify Step by Step") 和 `aggarwal2023adaptive` ("Let's Sample Step by Step") 在 OpenAlex 上未匹配——前者可能是索引问题，但建议确认 bib 条目正确。`snell2025scaling` 存在 first_author mismatch（bib=snell vs api=charlie），以及 `dembczynski2011exact` 和 `muller2021understanding` 的 LaTeX encoding 导致的 author name mismatch——这些是小问题但建议修正。
- **M5**: Figure 1 (p.3) 右侧面板显示"+1.4 pp (Few-NERD, $7.5)"——但 Table 2 (p.5) 显示 Few-NERD 上 entity construction 的 gain 是 +1.02pp 而非 +1.4pp（+1.40pp 是 SciERC 上的结果）。Figure 1 可能混淆了数据集，请核实数据来源一致性。
- **M6**: 论文 47 页（含附录），虽然 review guidelines 不要求审阅附录，但如此大量的附录材料如果核心 findings 高度依赖其中的表格，应考虑在正文中提供更自包含的数字摘要。

---

## 主要优势

1. **实验覆盖的深度和广度是该领域最全面的**：4个 NER 数据集 × 2个模型族 × 多个 N 值 × 9类方法（含16+配置变体）× 温度消融 × scale 消融 (4B/8B/14B/72B) × free-form vs. constrained × epoch 曲线 × per-entity-type 分析 × cross-task (RE+SQL)。62张表构成了一个极其详尽的证据网络。Table 62 (p.47) 的 differentiation matrix 清晰定位了本文相对于4篇先行工作的独特贡献。

2. **统计方法论远高于 NLP 论文平均水平**：Holm-Bonferroni 多重比较校正、bootstrap 95% CI (Table 12)、TOST 等量性检验 (p.20, external anchors)、permutation tests (calibration)、GroupKFold CV (hidden-state probe)。这为负面结果提供了可信的证据基础。

3. **MBR 理论联系具有原创性**：将 entity-level construction 形式化为 MBR decoding under entity-wise independence (Proposition 1-2) 在文献中是新颖的。虽然 bound 偏松，但 Corollary 1 给出了 SC gain 的 closed-form 必要条件，具有理论价值。

4. **诊断框架的结构性洞察有持久价值**：degeneracy → agreement fidelity → LP compression 的层次分解为未来研究提供了 operationalizable 的诊断工具。特别是"correlation-selection gap"这个概念（QE 信号与 quality 相关但不能转化为 selection gain）对理解 SC 在结构化任务上的行为非常有启发性。

5. **Cross-task 验证增强了普适性**：RE 扩展 (Appendix o, p.24-26) 显示相同的 degeneracy + LP compression pattern；SQL 扩展 (Appendix p, Table 5/§7.3 referenced) 通过 contrast（free-form decoding 在 SQL 上有效）强化了 constrained structured output 是 NER failure 的核心条件这一结论。

6. **Failure mode gallery (Appendix ag, p.36-37)** 提供了具体的定性示例，展示了 LP confidence failures、consensus-based verification failures 和 confidence-based extraction failures 的真实案例——这对理解定量结果背后的机制非常有帮助。

---

## 对 Director 指定审查重点的逐项回应

1. **诊断框架逻辑**：四阶段级联在 observational 层面逻辑自洽。每阶段有明确的操作化定义和可测量指标。但因果推断力度不足——级联各阶段之间的交互未通过 controlled interventions 验证（见 N1）。

2. **统计检验**：Holm 校正、bootstrap CI、TOST 均正确使用。57 项全局 Holm 校正过于保守（已承认），per-family 校正是合理的标准做法。唯一concern 是正文与附录校正结果的差异未在正文中显式说明（见 M3）。

3. **实验覆盖度**：4 NER + RE + SQL + 2 模型族 + 4B/8B/14B/72B + GPT-5.5 = 覆盖度在该领域属于顶级。N≤32 是一个限制（见 W4）。

4. **表格/数字一致性**：未发现明显的表格间矛盾。Figure 1 右侧面板的"+1.4pp (Few-NERD, §7.5)"可能与 Table 2 不一致（见 M5），需要作者核实。

5. **消融设计**：9类方法 × 16+配置变体的消融是全面的。缺失的 baseline 是 diversity-encouraging decoding strategies 和 trained external verifiers（超出论文定义的 self-verification 范围，但会影响"ceiling"claim 的普适性）。

6. **Hidden-state probe**：GroupKFold CV 设计正确（group=source instance, 5-fold, 3 seeds），不存在显式的数据泄露。AUROC 0.63-0.88 的 variance 来源未充分解释（见 W2）。

7. **负面结果的说服力**：在论文定义的 self-verification 范围内，证据标准高。但"capability ceiling"的措辞暗示了超越 self-verification 的普适性，这一更强 claim 未被充分支撑（见 N1）。

8. **Prescriptive escape routes**：效果量 +1.02-1.40pp (construction) 和 +0.42pp (cross-model) 统计显著但实际意义有限（见 W3）。LP selection +1.39pp 仅在 Few-NERD 上有效，不具普适性。


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

_source line 3123 · 2026-05-21T15:12:26.061187+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Must-Fix 问题\n\n**N1** [critical] 核心统计 claim 的稳健性不足\n- Section 7.5 (Table 5)、Appendix f (Table 13)\n- 论文承认在全局 Holm-Bonferroni 校正（k=57）下，\"no core NER claim survives\"（p_adj=0.055 for Few-NERD LP selection and construction）。论文转而报告 per-family 校正（selection k=21, construction k=10），但 per-family 分割本身是事后决定，削弱了统计严谨性。Few-NERD LP selection 的 per-family p_adj=0.021 是唯一正面结果，而 SciERC construction 的 p_adj=0.20 不显著。\n- 论文 4 个 contribution 中的第 4 个（\"prescriptive escape routes\"）依赖这些统计结果。如果核心正面结果在合理的多重比较校正下不显著，\"escape routes\"的贡献被大幅削弱。\n- 建议：(1) 正文中明确讨论全局 vs per-family 校正；(2) 预注册 hypothesis families 或提供更强 justification；(3) 用 permutation test 或 Bayesian 方法补充。\n\n**N2** [critical] \"Correlation-selection gap\" 概念的新颖性定位不够精准\n- Section 1 (lines 94–95)、Section 4、Section 8\n- 未充分区分与 MBR 文献已知发现的关系。Eikema & Aziz (2020, 2022) 已证明 MAP decoding 不足，Eikema et al. (2025) 指出 MBR utilities 在结构化输出上退化。Related Work (Section 8, lines 533–548) 主要聚焦 utility function 选择，未明确论证增量贡献。Instance-level signal 的设计性局限更像方法设计问题而非深层发现。\n- 建议：增加 explicit comparison 说明 MBR utility degradation 与 correlation-selection gap 的区别。\n\n## Reviewer 2 的 Should-Fix 问题\n\n**W1** [warning] 模型覆盖范围有限，泛化性声明过度\n- 完整实验仅 Qwen3-8B 和 LLaMA-3.1-8B（LoRA 微调）。72B zero-shot 仅 Few-NERD，GPT-5.5 仅 200 实例。Limitations 承认 frontier API models 表现出不同 degeneracy profiles（4% vs 5.5%）。但 Introduction/Conclusion 措辞暗示普遍性结论。\n\n**W2** [warning] Cross-task validation 较薄弱\n- RE 仅 SciERC 一个数据集，55.5% zero-F1 来自 span 错误。SQL 仅提到 87.2% degeneracy 缺乏系统分析。\n\n**W3** [warning] 遗漏直接相关参考文献\n- Ma et al. (2024) \"Self-Improving for Zero-Shot NER with LLMs\" (NAACL 2024) — 直接使用 SC 进行 NER 获正面结果\n- Madaan et al. (2023) \"Self-Refine\" (NeurIPS 2023) — MRSC 方法的直接先行工作\n\n**W4** [warning] Escape routes 实用价值定位模糊\n- +1.40pp 需 N× 推理成本，Discussion 承认 \"trade-off may only justify safety-critical use\"。应明确区分 proof of concept vs practical recommendation。\n\n## Reviewer 2 的小问题\n1. Table 1 标注不一致（LP \"per-sample\" vs 其他信号）\n2. Proposition 1 notation: M⁺ = ŷ_MV \\ ŷ_gr 未讨论 MV 删除正确实体的场景\n3. Figure 1 信息密度过高\n4. Appendix 34 页远超正文\n5. 引用格式小问题\n\n## Reviewer 2 的 Missing References\n1. Ma, Wang, Sun & Li (2024). NAACL 2024 — SC for zero-shot NER\n2. Madaan et al. (2023). NeurIPS 2023 — Self-Refine\n3. Wei et al. (2022). NeurIPS 2022 — Chain-of-Thought\n4. Survey: \"Test-time Scaling of LLMs\" (2025, arXiv:2511.14772)\n\n---\n\n请对以上每个问题逐条回应 [AGREE] 或 [REBUT]，如有补充发现请一并提出。"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Must-Fix 问题\n\n**N1** [critical] 核心统计 claim 的稳健性不足\n- Section 7.5 (Table 5)、Appendix f (Table 13)\n- 论文承认在全局 Holm-Bonferroni 校正（k=57）下，\"no core NER claim survives\"（p_adj=0.055 for Few-NERD LP selection and construction）。论文转而报告 per-family 校正（selection k=21, construction k=10），但 per-family 分割本身是事后决定，削弱了统计严谨性。Few-NERD LP selection 的 per-family p_adj=0.021 是唯一正面结果，而 SciERC construction 的 p_adj=0.20 不显著。\n- 论文 4 个 contribution 中的第 4 个（\"prescriptive escape routes\"）依赖这些统计结果。如果核心正面结果在合理的多重比较校正下不显著，\"escape routes\"的贡献被大幅削弱。\n- 建议：(1) 正文中明确讨论全局 vs per-family 校正；(2) 预注册 hypothesis families 或提供更强 justification；(3) 用 permutation test 或 Bayesian 方法补充。\n\n**N2** [critical] \"Correlation-selection gap\" 概念的新颖性定位不够精准\n- Section 1 (lines 94–95)、Section 4、Section 8\n- 未充分区分与 MBR 文献已知发现的关系。Eikema & Aziz (2020, 2022) 已证明 MAP decoding 不足，Eikema et al. (2025) 指出 MBR utilities 在结构化输出上退化。Related Work (Section 8, lines 533–548) 主要聚焦 utility function 选择，未明确论证增量贡献。Instance-level signal 的设计性局限更像方法设计问题而非深层发现。\n- 建议：增加 explicit comparison 说明 MBR utility degradation 与 correlation-selection gap 的区别。\n\n## Reviewer 2 的 Should-Fix 问题\n\n**W1** [warning] 模型覆盖范围有限，泛化性声明过度\n- 完整实验仅 Qwen3-8B 和 LLaMA-3.1-8B（LoRA 微调）。72B zero-shot 仅 Few-NERD，GPT-5.5 仅 200 实例。Limitations 承认 frontier API models 表现出不同 degeneracy profiles（4% vs 5.5%）。但 Introduction/Conclusion 措辞暗示普遍性结论。\n\n**W2** [warning] Cross-task validation 较薄弱\n- RE 仅 SciERC 一个数据集，55.5% zero-F1 来自 span 错误。SQL 仅提到 87.2% degeneracy 缺乏系统分析。\n\n**W3** [warning] 遗漏直接相关参考文献\n- Ma et al. (2024) \"Self-Improving for Zero-Shot NER with LLMs\" (NAACL 2024) — 直接使用 SC 进行 NER 获正面结果\n- Madaan et al. (2023) \"Self-Refine\" (NeurIPS 2023) — MRSC 方法的直接先行工作\n\n**W4** [warning] Escape routes 实用价值定位模糊\n- +1.40pp 需 N× 推理成本，Discussion 承认 \"trade-off may only justify safety-critical use\"。应明确区分 proof of concept vs practical recommendation。\n\n## Reviewer 2 的小问题\n1. Table 1 标注不一致（LP \"per-sample\" vs 其他信号）\n2. Proposition 1 notation: M⁺ = ŷ_MV \\ ŷ_gr 未讨论 MV 删除正确实体的场景\n3. Figure 1 信息密度过高\n4. Appendix 34 页远超正文\n5. 引用格式小问题\n\n## Reviewer 2 的 Missing References\n1. Ma, Wang, Sun & Li (2024). NAACL 2024 — SC for zero-shot NER\n2. Madaan et al. (2023). NeurIPS 2023 — Self-Refine\n3. Wei et al. (2022). NeurIPS 2022 — Chain-of-Thought\n4. Survey: \"Test-time Scaling of LLMs\" (2025, arXiv:2511.14772)\n\n---\n\n请对以上每个问题逐条回应 [AGREE] 或 [REBUT]，如有补充发现请一并提出。"
  }
}
```

</details>

---


### Tool result

_source line 3124 · 2026-05-21T15:12:53.555052+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27493
}
```

</details>

---


### Tool call

_source line 3125 · 2026-05-21T15:12:53.756347+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题\n\n**N1** [critical] 诊断级联的因果推断力度不足，与标题\"Capability Ceiling\"的强 claim 不匹配\n- §3-4 (诊断框架), Limitations (p.8)\n- 四阶段级联基于观察性关联建立，但标题声称\"capability ceiling\"。Figure 1 caption 标注\"diagnostic sequence, not causal chain\"，但正文叙事隐含因果方向性。Limitations 承认\"not interventional\"，但被埋在末尾。\n- 可能存在未测试的干预（diversity-encouraging decoding、contrastive sampling）能同时降低 degeneracy 和拓宽 LP range。\n- 建议：(1) 在 §1/§3 明确声明 observational 而非 causal；(2) 改标题或提供 controlled intervention。\n\n**N2** [critical] Free-form decoding 消融实验覆盖不完整，削弱 LP compression 作为独立瓶颈的论证\n- Appendix q (p.27), Table 47-48\n- LP compression 被诊断为第四阶段瓶颈，但 free-form decoding 消融仅在 CoNLL 和 Few-NERD INTRA 上执行，未覆盖 SciERC。SciERC 是 construction gain 最大的数据集 (+1.40pp, Table 2)。Table 22 (p.23) 报告 SciERC LP range 仅 0.041 nats（constrained decoding 下）。\n- 如果 SciERC 在 free-form 下 selection 能改善，则 LP compression 结论对该关键数据集不成立。\n- 建议：补充 SciERC free-form decoding 实验。\n\n## Reviewer 1 的 Should-Fix 问题\n\n**W1** [warning] 理论贡献（MBR 等价、degeneracy bound）实际预测力有限\n- §6.3, Corollary 1, Table 30 (p.26/41)\n- Bound 仅捕获实际 gain 的 5-12%（actual/bound ratio 3-12×），signal alignment α 是瓶颈（best signal 仅恢复 6.8% of non-degenerate oracle gap）。MBR 框架提供 qualitative insight 但 quantitative bound 过松。\n\n**W2** [warning] Hidden-state probe 跨数据集方差未充分解释\n- §3 (p.3-4), Appendix h.3 (p.21)\n- AUROC 从 SciERC 0.63 到 CoNLL 0.88 变化剧烈。Cross-dataset transfer drops。未分析什么让 CoNLL hidden states 更可分。CoNLL 上 AUROC=0.88 但似乎仍不能改善 selection——需解释为什么高 AUROC 不转化为 selection gain。\n\n**W3** [warning] Escape routes 效果量可能缺乏实际意义\n- §5, Table 2, Table 61 (p.46)\n- +1.02-1.40pp 需 N× 推理成本，SciERC greedy F1 ~0.529 提升到 ~0.543。未量化 compute-accuracy Pareto 曲线。\n\n**W4** [warning] N-scaling 范围对负面结论支撑力有限\n- §6.1 (p.6), Appendix s (p.28), Figure 10\n- N 止步于 32。引用 Brown et al. (2024) 但未讨论 N=100+ 时 degeneracy 是否显著下降。应基于 scaling law 外推讨论。\n\n**W5** [warning] Cross-model ensemble 仅测试 2 个模型族\n- §5.1, Table 2\n- Qwen3-8B + LLaMA-3.1-8B 共享 LoRA 训练流程，可能限制 diversity 上限。未讨论架构差异更大的组合。\n\n## Reviewer 1 的小问题\n- M1: Table 1 caption \"One score per input\" 与 LP footnote 矛盾\n- M2: §2.2 定义4种信号但 LP 在 §2.3 才引入，应统一\n- M3: Appendix f 全局校正导致 claims 不显著但正文 §7.5 用 per-family 校正，差异未充分说明\n- M4: 引用验证问题（lightman2024verify, aggarwal2023adaptive 等）\n- M5: Figure 1 右面板 \"+1.4pp (Few-NERD)\" 可能与 Table 2 不一致（+1.40pp 是 SciERC）\n- M6: 47 页附录，核心 findings 依赖附录表格\n\n## Reviewer 1 的主要优势评价\n1. 实验覆盖深度和广度是该领域最全面的\n2. 统计方法论远高于 NLP 论文平均水平\n3. MBR 理论联系具有原创性\n4. 诊断框架结构性洞察有持久价值\n5. Cross-task 验证增强普适性\n6. Failure mode gallery 提供定性理解\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 问题逐条回应 [AGREE] 或 [REBUT]，如有补充发现请一并提出。"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题\n\n**N1** [critical] 诊断级联的因果推断力度不足，与标题\"Capability Ceiling\"的强 claim 不匹配\n- §3-4 (诊断框架), Limitations (p.8)\n- 四阶段级联基于观察性关联建立，但标题声称\"capability ceiling\"。Figure 1 caption 标注\"diagnostic sequence, not causal chain\"，但正文叙事隐含因果方向性。Limitations 承认\"not interventional\"，但被埋在末尾。\n- 可能存在未测试的干预（diversity-encouraging decoding、contrastive sampling）能同时降低 degeneracy 和拓宽 LP range。\n- 建议：(1) 在 §1/§3 明确声明 observational 而非 causal；(2) 改标题或提供 controlled intervention。\n\n**N2** [critical] Free-form decoding 消融实验覆盖不完整，削弱 LP compression 作为独立瓶颈的论证\n- Appendix q (p.27), Table 47-48\n- LP compression 被诊断为第四阶段瓶颈，但 free-form decoding 消融仅在 CoNLL 和 Few-NERD INTRA 上执行，未覆盖 SciERC。SciERC 是 construction gain 最大的数据集 (+1.40pp, Table 2)。Table 22 (p.23) 报告 SciERC LP range 仅 0.041 nats（constrained decoding 下）。\n- 如果 SciERC 在 free-form 下 selection 能改善，则 LP compression 结论对该关键数据集不成立。\n- 建议：补充 SciERC free-form decoding 实验。\n\n## Reviewer 1 的 Should-Fix 问题\n\n**W1** [warning] 理论贡献（MBR 等价、degeneracy bound）实际预测力有限\n- §6.3, Corollary 1, Table 30 (p.26/41)\n- Bound 仅捕获实际 gain 的 5-12%（actual/bound ratio 3-12×），signal alignment α 是瓶颈（best signal 仅恢复 6.8% of non-degenerate oracle gap）。MBR 框架提供 qualitative insight 但 quantitative bound 过松。\n\n**W2** [warning] Hidden-state probe 跨数据集方差未充分解释\n- §3 (p.3-4), Appendix h.3 (p.21)\n- AUROC 从 SciERC 0.63 到 CoNLL 0.88 变化剧烈。Cross-dataset transfer drops。未分析什么让 CoNLL hidden states 更可分。CoNLL 上 AUROC=0.88 但似乎仍不能改善 selection——需解释为什么高 AUROC 不转化为 selection gain。\n\n**W3** [warning] Escape routes 效果量可能缺乏实际意义\n- §5, Table 2, Table 61 (p.46)\n- +1.02-1.40pp 需 N× 推理成本，SciERC greedy F1 ~0.529 提升到 ~0.543。未量化 compute-accuracy Pareto 曲线。\n\n**W4** [warning] N-scaling 范围对负面结论支撑力有限\n- §6.1 (p.6), Appendix s (p.28), Figure 10\n- N 止步于 32。引用 Brown et al. (2024) 但未讨论 N=100+ 时 degeneracy 是否显著下降。应基于 scaling law 外推讨论。\n\n**W5** [warning] Cross-model ensemble 仅测试 2 个模型族\n- §5.1, Table 2\n- Qwen3-8B + LLaMA-3.1-8B 共享 LoRA 训练流程，可能限制 diversity 上限。未讨论架构差异更大的组合。\n\n## Reviewer 1 的小问题\n- M1: Table 1 caption \"One score per input\" 与 LP footnote 矛盾\n- M2: §2.2 定义4种信号但 LP 在 §2.3 才引入，应统一\n- M3: Appendix f 全局校正导致 claims 不显著但正文 §7.5 用 per-family 校正，差异未充分说明\n- M4: 引用验证问题（lightman2024verify, aggarwal2023adaptive 等）\n- M5: Figure 1 右面板 \"+1.4pp (Few-NERD)\" 可能与 Table 2 不一致（+1.40pp 是 SciERC）\n- M6: 47 页附录，核心 findings 依赖附录表格\n\n## Reviewer 1 的主要优势评价\n1. 实验覆盖深度和广度是该领域最全面的\n2. 统计方法论远高于 NLP 论文平均水平\n3. MBR 理论联系具有原创性\n4. 诊断框架结构性洞察有持久价值\n5. Cross-task 验证增强普适性\n6. Failure mode gallery 提供定性理解\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 问题逐条回应 [AGREE] 或 [REBUT]，如有补充发现请一并提出。"
  }
}
```

</details>

---


### Tool result

_source line 3126 · 2026-05-21T15:12:55.213600+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1457
}
```

</details>

---


### Assistant

_source line 3127 · 2026-05-21T15:12:58.018573+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 235

## Round 235

2 recorded events


### User

_source line 3128 · 2026-05-21T15:13:00.642324+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心评价**：Overall 3.5 (Borderline Conference)，Soundness 4/5，Excitement 3/5，Reproducibility 5/5。

**两个 Must-Fix**：
1. 诊断级联是 observational 而非 causal，但标题"Capability Ceiling"暗示了过强的因果 claim——需要明确声明或降低 claim 强度
2. Free-form decoding 消融未覆盖主要基准 SciERC，削弱了 LP compression 作为独立瓶颈的普适性论证

**五个 Should-Fix**：理论 bound 过松（5-12%）、hidden-state probe 跨数据集方差未充分解释、escape routes 效果量偏小缺少 cost-effectiveness 量化、N-scaling 止步于 32、cross-model ensemble 仅测2个模型族。

**主要优势**：实验覆盖深度属该领域顶级（62张表），统计方法论远超 NLP 平均水准，MBR 理论联系有原创性，诊断框架有持久工具价值。

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

_source line 3129 · 2026-05-21T15:13:08.494704+00:00_

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


## Round 236

## Round 236

28 recorded events


### User

_source line 3130 · 2026-05-21T15:16:12.416282+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 诊断级联的因果推断力度不足，与标题"Capability Ceiling"的强 claim 不匹配**

同意这是一个需要处理的问题。论文在 Figure 1 caption 明确标注 "diagnostic sequence, not causal chain"，Limitations（lines 590–598）也承认 "Our evidence is correlational and theoretical (MBR framework, conditional decomposition), not interventional: we have not performed controlled interventions (e.g., artificially varying degeneracy while holding other factors constant), and the cascade stages interact in ways that resist decomposition into independent causal effects (R²<0; §4)"。

但正如 R1 所指出，这些 caveat 与标题 "Capability Ceiling" 的强断言之间存在张力。"Ceiling" 暗示一个硬性的、被证明的上界，而论文实际提供的是 observational diagnostics + loose theoretical bound（actual/bound ratio 仅 3–12%，Table 30）。建议作者在 Section 1 的 contribution 列表中明确标注诊断框架的 observational 性质，而非仅在 Limitations 中披露。

不过，我认为 R1 建议的 "provide controlled intervention" 对本文来说可能过于苛刻——人为控制 degeneracy 同时保持其他因素不变在 LLM 实验中极难实现。论文的 LoRA-rank ablation（§7.4，将 degeneracy 从 17.8% 降至 7.2%）和 temperature ablation（Appendix u，Table 43：degeneracy 从 41.4% 到 14.9%）已经提供了有限的 quasi-interventional 证据。标题修改或措辞弱化是更可行的修改方向。

**严重程度判断**：同意为 Must-Fix，但建议修改路径以标题/措辞调整为主，不需要新实验。

---

**[REBUT] R1-N2: Free-form decoding 消融实验覆盖不完整，未覆盖 SciERC**

R1 的事实判断有误。Appendix q（p.27）的 Table 32 明确标题为 "Comparison of constrained vs. free-form decoding **on SciERC** (Qwen3-8B, N=8, T=1.0, seed=42; RE selection gap replicates across 4 seeds: +1.84±0.12 pp)"。该表包含四个 Panel：

- **Panel A**（LP 分布）：constrained tied fraction 59.7% vs free-form 57.7%，Δ = −2.0 pp
- **Panel B**（Selection F1）：NER LP-selected 0.6241 (constrained) vs 0.6222 (free-form)，selection gap 分别为 −0.0059 和 −0.0041——两种解码方式下 NER selection 均无法改善
- **Panel C**（QE ρ）：所有信号在 free-form 下均有微弱提升（SJ +0.018, FK +0.053），但 LP 提升仅 +0.008
- **Panel D**（Parse rate）：free-form 解析率 99.95%

论文正文 Appendix q 进一步在 lines 2184–2200 补充了 CoNLL 的 free-form 结果作为扩展验证。因此，SciERC 是 free-form ablation 的**首要**数据集，而非被遗漏。

此外，lines 2056–2073 讨论了 SciERC free-form 下的 non-tied subset reshuffling：87 instances 新获 LP discrimination 但 "aggregate NER selection gains remain negligible"（line 2066），明确回应了 "如果 SciERC 在 free-form 下 selection 能改善" 的假设——答案是不能。

**结论**：R1-N2 基于对论文内容的误读，不构成有效的 Must-Fix 问题。论文在 SciERC 上的 free-form 消融是完整的，且结果支持 LP compression 作为独立瓶颈的论证（tied fraction 仅减少 2 pp，selection 依然无效）。

---

### Should-Fix 问题

**[AGREE] R1-W1: 理论贡献（MBR 等价、degeneracy bound）实际预测力有限**

同意。Table 30 显示 actual/bound ratio 仅 3–12%，α（signal alignment）是真正的瓶颈（best signal 恢复非退化 oracle gap 的 6.8%），而非 degeneracy D。论文自身在 lines 389–392 承认 "α—not D—is the bottleneck...the bound cannot be tightened by signal combination (§5.2) or verifier-based construction (§5.2)"。

然而，我认为理论贡献的价值不完全在于 bound 的 tightness。Corollary 1 的 θ_crit = 0.70 预测了 degeneracy 超过何种水平时增益消失（§6.3），Table 30 验证了所有正增益配置的 D < θ_crit。这提供了**定性的预测力**——告诉从业者在什么条件下不值得尝试 SC，即使 bound 本身很松。

**补充发现**：我在 Round 1 审稿中也指出了类似问题——bound 松弛意味着 escape routes 的理论基础薄弱。建议作者在正文中明确将 degeneracy bound 定位为 **necessary condition**（D < θ_crit 是必要条件）而非 sufficient condition，避免读者误解为紧界。

---

**[AGREE] R1-W2: Hidden-state probe 跨数据集方差未充分解释**

同意这是一个值得补充解释的问题。AUROC 从 SciERC 0.630 到 CoNLL 0.882 的变化确实需要更多分析。论文在 lines 248–267 讨论了 cross-dataset transfer 下降（LODO AUROC 0.56–0.67），并指出 "even direct hidden-state access would not yield a universal quality signal"（lines 265–266），但未解释**为什么** CoNLL 的 hidden states 更可分。

可能的解释方向（论文未提供）：CoNLL 任务更简单（greedy F1 ≈ 91%），错误实体在 hidden space 中可能表现为更明显的 outlier；SciERC 有 6 种实体类型且 F1 仅 ≈ 65%，错误模式更多样化，增加了 hidden-state 分类难度。这与论文在 Appendix d 中发现的 "structural signals scale with structural complexity"（SciERC 6+ entities: ρ=0.547 vs 1–2 entities: ρ=0.415）一致。

关于 "为什么高 AUROC 不转化为 selection gain"：这在 Section 2.1（lines 162–173）中有结构性解释——hidden-state probe 是 instance-level signal（对同一 input 的所有 N 个 candidate 产生相同 score），因此无法 discriminate per-sample candidates。但 R1 的关切更深层：即使在 CoNLL 上 AUROC=0.88 使 quality estimation 非常准确，instance-level 的设计限制仍然阻止了 selection 改善，这恰恰印证了 correlation-selection gap 的核心论点。建议作者在 §3 补充这一点作为 hidden-state probe 结果的 explicit takeaway。

---

**[AGREE] R1-W3: Escape routes 效果量可能缺乏实际意义**

同意，且这与我在 Round 1 的 W4 一致。Table 61（p.46）提供了成本-效益汇总：SC + construction（N×成本）仅获 +1.02–1.40 pp，cross-model SC（2N×成本）获 +0.42 pp。论文在 Discussion（lines 575–576）承认 "the trade-off (N× cost for ≈1 pp) may only justify safety-critical use"。

缺少的是 Pareto 曲线：在什么 N 值下达到边际收益拐点？Table 37（p.28）的 N-scaling 数据（N=2 到 32）可以绘制 cost-accuracy trade-off，但论文未这样呈现。建议作者补充这一视觉化。

---

**[AGREE] R1-W4: N-scaling 范围对负面结论支撑力有限**

部分同意。Table 37 显示在 N=32 时 degeneracy 降至 4%、oracle headroom 达 +20.0 pp，但 best selection Δ 仅 +0.95 pp（LP, p=0.091）。这已经是一个很强的论据：**即使 degeneracy 几乎被消除，selection 依然失败**。

然而，R1 关于 N=100+ 的 concern 有一定道理。论文引用了 Brown et al. (2024) 的 scaling law F₁(N) = a − b·N^{−c}，Figure 10 拟合了 R² > 0.999 的曲线。SciERC c ≈ 0.35 意味着 oracle headroom 的增长是 sublinear 的（从 N=32 到 N=128 oracle headroom 可能从 +20 pp 增至约 +25 pp），但论文未讨论 selection gap 是否会在更大 N 下因为候选池质量提升而缩小。

**补充证据**：Table 38（N=32 bootstrap significance test）显示 LP p_greedy = 0.091，CI [−0.41, +2.34]——95% CI 跨零，即使在 N=32 时也无法排除零效应。如果 selection gap 在 N=32 时都无法达到显著，继续增大 N 改善 selection 的概率很低（因为瓶颈是 signal alignment α 而非 candidate pool size）。建议论文在 Appendix s 增加基于 scaling law 的 extrapolation 讨论。

---

**[AGREE] R1-W5: Cross-model ensemble 仅测试 2 个模型族**

同意，且与我的 W1 一致。Qwen3-8B 和 LLaMA-3.1-8B 共享相同的 LoRA 训练流程（LLaMA Factory），可能限制了 diversity 上限。论文的 frontier model 实验（Table 41）显示不同架构间 degeneracy 差异巨大（Claude Sonnet 4: 74%, DeepSeek: 5.5%），暗示更多样化的 ensemble 可能产生更大的增益，但这未被验证。

---

### 小问题回应

**[AGREE] R1-M1**: Table 1 caption 的 "†One score per input" 确实容易与 per-sample/instance-level 区分混淆。

**[AGREE] R1-M2**: §2.2 先定义 4 种信号再在 §2.3 引入 LP，结构上可以改善。

**[AGREE] R1-M3**: Appendix f 全局校正 vs §7.5 per-family 校正的差异——这也是我 Round 1 审稿的 N1。

**[REBUT] R1-M4**: 引用验证工具检测到 lightman2024verify、wang2023selfconsistency、aggarwal2023adaptive 为 "not_found"，但这是 OpenAlex API 的覆盖局限（这三篇都是知名且真实的论文），不构成引用问题。snell2025scaling 和 dembczynski2011exact 的 "mismatch" 是 LaTeX 编码导致的姓氏格式差异（Müller vs M\"uller, Dembczyński vs Dembczy\'nski），属于 bib 文件的正常现象。

**[REBUT] R1-M5**: R1 称 "Figure 1 右面板 '+1.4pp (Few-NERD)' 可能与 Table 2 不一致（+1.40pp 是 SciERC）"。实际上 Table 5 明确显示 **Few-NERD** construction Δ = +1.40±0.51 pp，**SciERC** 为 +1.02±0.49 pp。Figure 1 的 "+1.4 pp (Few-NERD; §7.5)" 与 Table 5 完全一致。R1 混淆了两个数据集的数字。

**[AGREE] R1-M6**: 47 页附录体量过大——与我 Round 1 小问题第 4 条一致。

---

### 综合评估

R1 的审稿整体质量高，对诊断框架的因果推断局限性（N1）和理论 bound 的松弛性（W1）的指出均有价值。但 **N2（free-form decoding 缺失 SciERC）是一个事实性错误**——Table 32 明确在 SciERC 上执行了 free-form ablation，结果支持论文的结论。M5 同样是事实性误读。

去除 N2 后，R1 的 Must-Fix 仅剩 N1（因果性/标题措辞），这可以通过修改标题和增加 Section 1 的 caveat 来解决，不需要新实验。R1 的 Should-Fix 问题（W1–W5）与我 Round 1 的发现高度一致，支持论文处于 **3.5 Borderline Conference** 的评分区间。

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

_source line 3131 · 2026-05-21T15:16:31.500343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 3132 · 2026-05-21T15:16:31.601537+00:00_

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
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
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
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3133 · 2026-05-21T15:16:36.219148+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "free.form|Free.form|freeform",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "context": "3",
  "head_limit": "40"
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
    "pattern": "free.form|Free.form|freeform",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "context": "3",
    "head_limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 3134 · 2026-05-21T15:16:36.269836+00:00_

314-\section{Holm--Bonferroni Enumeration}\label{app:holm}
315-
316-Table~\ref{tab:holm_family} enumerates all $k{=}57$ statistical tests reported in this paper under a single global Holm--Bonferroni correction.
317:Under this most conservative family, no core NER claim survives ($p_{\text{adj}}{=}0.055$ for Few-NERD LP selection and construction); only two peripheral tests reach significance (CoNLL few-shot entity entropy, RE LP selection reversal under free-form decoding).
318-We report per-family corrections in the main text (\S\ref{sec:prescriptive}); the global enumeration is provided here for transparency.
319-
320-\begin{table*}[t]
--
393-\addlinespace
394-\multicolumn{6}{l}{\textit{Other}} \\
395-54 & & LP distribution seed 42 vs 456 (Mann--Whitney) & $0.550$ & $1.0$ &  \\
396:55 & & RE LP selection reversal (free-form, 4-seed) & ${<}.001$ & $0.006$ & $\dagger$ \\
397-56 & & WNUT-17 conditional $\rho$ VC ($p$-value) & $0.487$ & $1.0$ &  \\
398-57 & & WNUT-17 conditional $\rho$ FK ($p$-value) & $0.002$ & $0.094$ &  \\
399-\bottomrule
--
786-\paragraph{Non-tied subset.}
787-Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
788-As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability. LP carries information, but compression limits its exploitation.
789:A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
790-
791-\paragraph{$\va
…[truncated 1959 chars]

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

_source line 3135 · 2026-05-21T15:16:40.784883+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "freeform_ablation|free.form.*ablation|\\\\\\\\label\\\\{app:freeform\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "context": "10",
  "head_limit": "60"
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
    "pattern": "freeform_ablation|free.form.*ablation|\\\\\\\\label\\\\{app:freeform\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "context": "10",
    "head_limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 3136 · 2026-05-21T15:16:40.835500+00:00_

No matches found

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

_source line 3137 · 2026-05-21T15:16:44.207287+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "freeform|free_form",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "context": "3"
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
    "pattern": "freeform|free_form",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "context": "3"
  }
}
```

</details>

---


### Tool result

_source line 3138 · 2026-05-21T15:16:44.258085+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-786-\paragraph{Non-tied subset.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-787-Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-788-As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability. LP carries information, but compression limits its exploitation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:789:A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-790-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-791-\paragraph{$\varepsilon$ sensitivity sweep (post-hoc exploratory).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-792-Table~\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.
--
/home
…[truncated 4299 chars]

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

_source line 3139 · 2026-05-21T15:16:53.661316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1154",
  "limit": "80"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1154",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 3140 · 2026-05-21T15:16:53.817368+00:00_

1154	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
1155	
1156	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).
1157	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
1158	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
1159	RE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\ $-0.68$~pp constrained.
1160	The constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.
1161	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
1162	
1163	\begin{table*}[t]
1164	\centering
1165	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
1166	\label{tab:freeform_ablation}
1167	
1168	\vspace{2pt}
1169	{\small\textsc{Panel A: Logprob Distribution}}
1170	\vspace{2pt}
1171	
1172	\begin{tabular}{lccc}
1173	\toprule
1174	Metric & Constrained & Free-form & $\Delta$ \\
1175	\midrule
1176	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
1177	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
1178	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
1179	\bottomrule
1180	\end{tabular}
1181	
1182	\vspace{8pt}
1183	
1184	{\small\textsc{Panel B: Selection F1}}
1185	\vspace{2pt}
1186	
1187	\begin{tabular}{llccc}
1188	\toprule
1189	Task & Method & Constrained & Free-
…[truncated 1556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 156
}
```

</details>

---


### Tool call

_source line 3141 · 2026-05-21T15:17:06.262252+00:00_

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


### Tool call

_source line 3142 · 2026-05-21T15:17:06.312839+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

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
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3143 · 2026-05-21T15:17:06.313248+00:00_

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


### Tool result

_source line 3144 · 2026-05-21T15:17:06.364521+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T14:58:55.635241+00:00\", \"completed_at\": \"2026-05-21T15:03:04.713623+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续两页纯文本（Title/Abstract/Introduction/Contributions），第一个 display item（Figure 1）直到第 3 页才出现。对于实证为主的诊断论文，在前两页缺少视觉锚点会削弱审稿人第一印象。建议将 Figure 1（或其简化版）提前至第 2 页。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Author/Abstract 排版整洁，符合 ACL 匿名投稿格式，无拥挤感。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 作为首个 display item 信息传达有效：三阶段诊断级联（Quality Estimation → Sample Selection → Entity-Level Construction）清晰展示核心 message，含 AUROC/ρ 数值标注，caption 自包含。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 ≥2 页无任何 figure/table/equation 穿插。此处非理论推导密集段，属于可改进的节奏问题。\"}, {\"severity\": \"info\", \"dimension\": \"page 3-7\", \"message\": \"中段视觉节奏良好：Figure 1 (p3) → Table 1 + Figure 2 (p4) → Table 2 (p5) → Table 3 + Figure 3 (p6) → Tables + Figure 4 (p7)，text-table-figure 三重奏交替频繁。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"最后一页主文（Related Work/Discussion/Conclusion/Limitations）为纯文本，但这些 section 纯文本属于常规做法，无需调整。页面填充率 >90%，空间利用充分。\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页内含 4 figures + 5-6 tables ≈ 9-10 个 display items。对于实证诊断类论文，这是理想密度，每个 display item 传达明确且不可替代的 message。\"}, {\"severity\": \"info\", \"dimension\": \"page 14-47\", \"message\": \"附录 34 页，包含大量补充 tables（至少 Tables 7-62）和 Figures 5-8。附录与主文比约 4:1，体现了充分的实验覆盖。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 使用绿色（✓ Effective）和红色（✗ Fails）对比。绿-红配色对红绿色盲不友好（~8% 男性），但图中同时有 ✓/✗ 符号和文字标签作为冗余编码，影响有限。建议将红色替换为橙色以提升色盲友好度。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（Temperature Robustness，4 子图面板）面板较小，图内 axis label 和 legend 文字接近可读性下限（约正文字号的 65-70%）。建议适当增大字号或改用 figure* 全宽排版。\"}, {\"severity\": 
…[truncated 1546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3145 · 2026-05-21T15:18:00.251699+00:00_

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

_source line 3146 · 2026-05-21T15:18:00.955259+00:00_

1	issues:
2	  # ===== 历史 resolved issues (保留) =====
3	  - id: "R1-W1"
4	    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
5	    category: experiment
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 19
10	    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
11	    resolution_round: 19
12	
13	  - id: "R1-W2"
14	    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
15	    category: framing
16	    severity: critical
17	    status: resolved
18	    first_raised_round: 1
19	    last_seen_round: 21
20	    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
21	    resolution_round: 21
22	
23	  - id: "R2-N1-old"
24	    summary: "Contribution 1 'methodological premise' 是定义推论"
25	    category: framing
26	    severity: critical
27	    status: resolved
28	    first_raised_round: 1
29	    last_seen_round: 19
30	    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
31	    resolution_round: 19
32	
33	  - id: "R2-N2-old"
34	    summary: "与 MBR 文献差异化定位不够锐利"
35	    category: framing
36	    severity: warning
37	    status: resolved
38	    first_raised_round: 1
39	    last_seen_round: 19
40	    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
41	    resolution_round: 19
42	
43	  - id: "R2-N4-old"
44	    summary: "模型规模 3B-8B，70B+ 未知"
45	    category: experiment
46	    severity: info
47	    status: resolved
48	    first_raised_round: 1
49	    last_seen_round: 19
50	    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
51	    resolution_round: 19
52	
53	  - id: "R1-W3-old"
54	    summary: "2-seed 统计效力不足"
55	    category: experiment
56	    severity: warning
57	    status: resolved
58	    first_raised_round: 1
59	    last_seen_round: 19
60	    resolution: "Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。"
61	    resolution_round: 19
62	
63	  - id: "R1-W4-old
…[truncated 39063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 3147 · 2026-05-21T15:18:37.333091+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\\\.40.*Few|Few.*1\\\\.40|construction.*Few.*\\\\+1",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "context": "2",
  "head_limit": "20"
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
    "pattern": "1\\\\.40.*Few|Few.*1\\\\.40|construction.*Few.*\\\\+1",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "context": "2",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 3148 · 2026-05-21T15:18:37.684628+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 3149 · 2026-05-21T15:18:41.547666+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\\\.40|\\\\+1\\\\.40\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
  "output_mode": "content",
  "context": "3"
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
    "pattern": "1\\\\.40|\\\\+1\\\\.40\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
    "output_mode": "content",
    "context": "3"
  }
}
```

</details>

---


### Tool result

_source line 3150 · 2026-05-21T15:18:41.598287+00:00_

No matches found

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

_source line 3151 · 2026-05-21T15:18:45.667930+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\\\.40|construction.*gain|prescriptive\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "context": "2",
  "glob": "*.tex",
  "head_limit": "30"
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
    "pattern": "1\\\\.40|construction.*gain|prescriptive\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "context": "2",
    "glob": "*.tex",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 3152 · 2026-05-21T15:18:45.718700+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-242-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-243-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:244:LP-weighted construction improves on Few-NERD ($+1.40{\pm}0.51$\,pp, $p{<}0.001$; survives Holm--Bonferroni at $k{=}57$) and SciERC ($+1.02{\pm}0.49$\,pp, $p{=}0.004$, $p_{\text{adj}}{=}0.20$; Table~\ref{tab:entity_construction}), recovering 8--11\% of oracle headroom. CoNLL shows no gain ($-0.39$\,pp), consistent with high degeneracy ($N$-scaling in Appendix~\ref{app:n_scaling}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-245-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-246-\paragraph{LP-alignment gating.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-7-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-8-\paragraph{From diagnosis to practice.}\label{sec:selection_method}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:9:Entity-level construction bypasses both failure mechanisms, with gains when degeneracy ${<}22$\% and absent when ${>}31$\% ($p{<}0.01$; Appendix~\ref{app:epoch_confound}); no alternative strategy beats greedy (Appendix~\ref{app:dals}, \ref{app:supervised_combination}), making construction the only consistently positive approach (Table~\ref{tab:cost_benefit})---though the trade-off ($N{\times}$ cost for ${\approx}1$\,pp) may only justify safety-critical use.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs
…[truncated 4662 chars]

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
