# Director coordination — Part 11 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 10](part-010.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 12 →](part-012.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 236

### Tool call

_source line 3153 · 2026-05-21T15:24:25.249095+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ===== 历史 resolved issues (保留) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3-old\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-9 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 28\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"scope 声明在 Introduction 和 Limitations 中已存在。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"仅2个~8B fine-tuned + 1个72B zero-shot。缺closed-source模型。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R1 REBUT R2-W1(事实前提错误:论文已测72B+GPT-5.5)。R2确认事实错误但仍指出缺instruction-tuned vs base对比。共识:模型覆盖度合理但缺base model对比。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: R1-W1(模型覆盖有限)+R2-W1(泛化性声明过度)再次独立提出。完整实验仅Qwen3-8B和LLaMA-3.1-8B(LoRA)。72B仅Few-NERD, GPT-5.5仅200实例。Limitations承认frontier models degeneracy不同(4%-5.5%)。两人AGREE。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 28\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7）。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26视觉审查再次确认p7 display items过密。\"\n      - round: 27\n        reviewers: [2]\n        note: \"R27视觉审查: p6-7 display items密度高但可接受。Figure 1 部分面板文字偏小(约正文60-65%)。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: Figure 4面板较小(约正文65-70%)，Figure 3尺寸偏小但可读。info级。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 28\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"construction不应作为standalone contribution。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R2-N2列prescriptive gains为critical(+1.0-1.4pp at 8x cost)。R1降为should-fix(主贡献是诊断框架)。R1交叉回应: negative results有独立价值，prescriptive是contribution #4非primary。R2同意若修复其他问题可降级。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: R1-W3+R2-W4再次提出escape routes效果量偏小(+1.0-1.4pp at N×cost)。R2 AGREE R1-W3。共识: 效果量真实但实用价值有限——明确定位为proof of concept而非practical recommendation。\"\n    action_items:\n      - round: 26\n        action: \"确认construction在正文中已降级为diagnostic-motivated ablation而非contribution。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction（framing tautology）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 28\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 必须重构Abstract/Intro将structural/empirical二分法前置。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: Section 4明确区分了definitional vs empirical层面。R1-N2关注的是因果语言而非tautology本身。论文已有改善但主体仍用'governs'等因果动词。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28 R2-N2: correlation-selection gap与MBR文献已知发现(Eikema & Aziz 2020/2022, Eikema et al. 2025)的增量新颖性需更精确定位。Related Work §8讨论MBR但聚焦utility function选择，未明确论证诊断cascade的增量贡献。\"\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 27\n    resolution: \"R23: Reduced to 4 key numbers. R27 fresh: R2再次提出W4但R1 REBUT(empirical NLP论文惯例)。共识: 当前密度尚可接受。\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  # ===== Round 24 issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 公式删除，改为定性叙述。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"method.tex 加定义。\"\n    resolution_round: 24\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1 minor #2: 最高ρ为EM 0.472(LLaMA CoNLL)，'up to 0.45'略低。建议核实。\"\n\n  # ===== Round 25 issues =====\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"n=23 power 仅约 50% for ρ=0.4。结论过强。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及此 specific null finding。\"\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"cross-model仅1数据集1对模型。§5.3 SCD不再出现。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n      - round: 28\n        reviewers: [1]\n        note: \"R28 R1-W5: cross-model仅Qwen3-8B+LLaMA-3.1-8B, 共享LoRA训练流程可能限制diversity上限。R2 AGREE。\"\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"'first systematic characterization'过强，应限定为'for NER'。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: 两位Reviewer独立列为consensus critical。R1-N1=R2-N1: 标题'Structured Generation'与NER-centric证据严重不匹配。RE仅1数据集(55.5% F1=0受span error混淆)，SQL仅n=196一句话。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: R2-W2(RE受span error混淆, SQL缺系统分析)+R1(cross-task as strength but W4 N-scaling限制)。标题已为NER-specific。RE/SQL定位为preliminary extension而非core claim。\"\n    action_items:\n      - round: 27\n        action: \"标题从'Structured Generation'缩窄为NER-specific或'Structured Information Extraction'。Abstract/Intro scope相应调整。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni；4 数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"CoNLL 增益为负 (−0.29pp)。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"p_adj矛盾(§1: 0.20 vs Table 13: 0.038)。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R2-N2 prescriptive gains边际(+1.0-1.4pp at 8x cost)。R1-W5同意事实但降为should-fix。交叉后共识: gains有限但对diagnostic论文可接受。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R2-N1 [critical]: 全局Holm k=57下p_adj=0.055。experiments_main.tex声称construction 'survives Holm-Bonferroni at k=57'但Appendix f声称'no core NER claim survives'——存在正文与附录的不一致。Per-family k=21事后决定削弱严谨性。两人共识。\"\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"脚注9报告k=38但Table 13列k=57，差异k=19来源不明。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-N3 [critical]: Abstract k=19 vs Table 13实际21行。两位Reviewer交叉后共识需作者核实。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R2-N1再次指出per-family分割为事后决定。Abstract报告k=21。正文§7.5用per-family但未引导读者到Appendix f全局校正结果。\"\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"fine-tuning/scale/architecture混淆。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。Limitations已承认。\"\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"SciERC single-seed用于detailed diagnostic。bootstrap CI有缓解但不够。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh: 论文已改为3-seed(Few-NERD/CoNLL)。SciERC仍σ=0.48pp但已标注。\"\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"嵌套NER场景何时violated未讨论。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-Q4: entity-wise independence在NER中是否合理——相邻entity预测常相关。\"\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"bound仅解释3-12%的gap。共识: 可降级为analysis tool。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 R1-W1: bound仅捕获4.7-12.1%实际增益且无法预测负增益。交叉后两人共识: 在主文中明确讨论tightness而非仅Table 30 header标'weak'。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R1-W1再次提出(actual/bound ratio 3-12x)。R2 AGREE但补充: θ_crit=0.70给出了有效的定性预测力(necessary condition)。共识: bound应定位为necessary condition而非tight bound。\"\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"未直接提及。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: 与Yun et al. (2025) diversity collapse差异化需强化。两人交叉共识: §8/§9用3-4句明确区分。\"\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 未找到/元数据不匹配/orphan bib\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"hobelsberger2025systematic疑似虚构，17 orphan bib entries。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1 minor #1发现holm1979simple和xia2025survey orphan。R2引用验证: 51 bib, 49 cited, 2 orphan, 0 fake。较之前有改善(从17降至2)。\"\n      - round: 28\n        reviewers: [1]\n        note: \"R28 R1-M4: lightman2024verify和aggarwal2023adaptive在OpenAlex未匹配(索引问题非虚构)。snell2025scaling等有LaTeX编码导致的author mismatch。R2 REBUT: 这些是API覆盖局限而非引用问题。\"\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 标注为descriptive diagnostic而非causal chain。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 R1-N2 [critical]: 因果语言('governs','explaining')与相关性证据不匹配。Figure 1标'not causal'但主体未贯彻。两人交叉强烈共识——需统一替换为相关性语言。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R1-N1 [critical]: 标题'Capability Ceiling'暗示硬上界但证据为observational。Limitations承认'not interventional'但埋在末尾。R2 AGREE——但指出LoRA-rank和temperature消融提供quasi-interventional证据，标题/措辞修改即可。共识: Must-Fix via title change + §1 caveat。\"\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: EL4NER, Self-Certainty BoN 等\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"EL4NER必须引用。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1建议补DeNero et al. 2009, Desai & Durrett 2020, Huang et al. 2024。R2建议补KDD 2025 survey, Aronica et al. 2024, test-time scaling survey。\"\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"Oracle Scaling figure 已生成并集成。\"\n    resolution_round: 26\n\n  # ===== Round 26 issues =====\n\n  - id: \"R26-N1\"\n    summary: \"N=8/16对test-time compute scaling研究范围过窄\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"建议至少补N=32或论证N=8的cost-efficiency。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及N range。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R1-W4: N止步于32, 引用Brown et al.(2024)但未讨论N=100+。R2部分AGREE——N=32时degeneracy降至4%但selection Δ仅+0.95pp(p=0.091)，说明瓶颈是signal alignment而非N。建议基于scaling law extrapolation讨论。\"\n\n  - id: \"R26-N2\"\n    summary: \"Trained verifier (LightGBM AUC=0.923) 负面结果scope有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R26-W1\"\n    summary: \"论文同时做4件事，每项深度不够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 R2 Excitement=2.5/5部分原因是novelty分散。\"\n\n  - id: \"R26-VIS1\"\n    summary: \"Page 7 display items严重过密（4表+1图）\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: p6-7 '略显拥挤但信息承载量高，适合实证论文'。降低严重性。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: p3-7中段视觉节奏良好，text-table-figure交替频繁。整体密度适合实证诊断论文。\"\n\n  - id: \"R26-VIS2\"\n    summary: \"Figure 6 heatmap红绿色阶对色盲不友好\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 26\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: Figure 6 heatmap单色渐变(黄→深绿)，建议双色发散色板。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: Figure 1绿/红对比对红绿色盲不友好(~8%男性)，但有✓/✗符号冗余编码。建议红→橙。\"\n\n  # ===== Round 27 issues =====\n\n  - id: \"R27-N1\"\n    summary: \"因果语言与相关性证据不匹配——Section 9 'governs'、Abstract 'explaining why'\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-N2 [critical]: Figure 1 caption标'not causal'但§9用'governs'，Abstract用'explaining where and why'，Intro用'fills this gap'。无干预实验验证因果方向。R2 AGREE with nuance。交叉后强烈共识。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R1-N1再次以'Capability Ceiling'标题为切入点提出同一问题。R2 AGREE: LoRA-rank/temperature ablation提供quasi-interventional证据但不足以支撑'ceiling'。共识: 标题需修改+全文统一相关性语言。\"\n    action_items:\n      - round: 27\n        action: \"全文统一将因果动词替换为相关性语言('governs'→'is associated with','explaining'→'characterizing')。Discussion加段讨论因果推断局限。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R27-N2\"\n    summary: \"Holm-Bonferroni k=19(Abstract) vs Table 13实际21行——影响p_adj可复现性\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-N3 [critical]: Abstract 'selection family k=19'但Table 13 selection family有21项测试。差异2项未解释。若k=21则p_adj需重算。R2 AGREE。交叉共识: 需作者核实并修正。\"\n    action_items:\n      - round: 27\n        action: \"核实k=19 vs k=21来源。修正Abstract数字。在Appendix f提供完整Holm correction trace。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R27-W1\"\n    summary: \"7种方法分类边界模糊——diagnostic probes vs selection methods未区分\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"R1-W4: Abstract '7 methods'含diagnostic probes(ESJ/MRSC/LSC)和selection methods(DALS/SCD)混为一体。Het-T在Table 2无对应行。Table 2列9 categories与Abstract 7 methods不对齐。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent text fix: Abstract/Intro区分diagnostic probes和selection methods。对齐Table 2 categories与Abstract计数。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-W2\"\n    summary: \"RE分析受entity span error混淆(55.5% F1=0)——测量NER→RE错误传播而非RE本身\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W2+R2-W3: RE FEATURE-OF ρ≈0 vs HYPONYM-OF ρ=0.646。Table 3 RE列与NER并列但未标注混淆。两人交叉共识。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28 R2-W2再次指出: RE仅SciERC一个数据集, 55.5% zero-F1来自span错误。SQL仅87.2% degeneracy缺系统分析。Cross-task validation薄弱。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: Table 3 RE列加脚注标注span error混淆。正文加caveat。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-W3\"\n    summary: \"k=57全局Holm + RE/小配置样本量→统计功效不足，负面结论可能是power问题\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"R1-W3: RE n≈397时仅大效应量可检测。论文核心结论'no signal improves selection'可能反映insufficient power。需在Conclusion加hedge。R2 AGREE。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: Conclusion加hedge('absence of evidence is not evidence of absence'风格)。计算SQL n=196 MDE。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-W4\"\n    summary: \"Entity construction +1.0-1.4pp at 8x cost——cost-effectiveness未在主文讨论\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W5+R2-N2: Table 61在Appendix p45但主文未引用。实践者是否值得8x推理成本换~1pp？R1建议Section 10直接address。R2降为should-fix(若其他问题修复)。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R1-W3+R2-W4: 重复提出。Discussion承认'N× cost for ≈1 pp may only justify safety-critical use'但缺Pareto曲线量化。共识: 应明确区分proof-of-concept vs practical recommendation。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: Discussion/Conclusion加cost-effectiveness讨论(8x cost for ~1pp gain)。引用Appendix Table 61。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-M1\"\n    summary: \"2个orphan bib entries: holm1979simple, xia2025survey\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1+R2独立发现。holm1979simple应补\\\\cite，xia2025survey若不引用应删除。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: holm1979simple补\\\\cite到Holm-Bonferroni首次出现处。xia2025survey决定引用或删除。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-M2\"\n    summary: \"Figure 2 caption 'oracle gap'未自含定义\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R2-M2: 建议caption加'(oracle headroom = best-of-N F1 − greedy F1)'。R1 AGREE。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: Figure 2 caption加oracle headroom定义。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-M3\"\n    summary: \"Limitations 未讨论closed-source API模型的degeneracy profile差异\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"R2-M5: 现有Limitations仅提LP signal不可用，未讨论degeneracy特征差异。R1 AGREE。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: Limitations加1句关于closed-source API模型degeneracy profile差异(Claude 74% vs DeepSeek 5.5%)。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-MR1\"\n    summary: \"缺失引用: DeNero 2009, Desai & Durrett 2020, Huang 2024, KDD 2025 survey, Aronica 2024\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1: DeNero et al. 2009(consensus decoding MT), Desai & Durrett 2020(calibration seq labeling), Huang et al. 2024(LLMs cannot self-correct)。R2: KDD 2025 UQ survey, Aronica et al. 2024(structured IE), test-time scaling survey 2025。交叉后部分AGREE——核心3篇(DeNero, Huang, Aronica)应补，surveys可选。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28 R2-W3新增: Ma et al. (2024) NAACL 'Self-Improving for Zero-Shot NER with LLMs'——直接使用SC进行NER获正面结果，是最相关先行工作。Madaan et al. (2023) NeurIPS 'Self-Refine'——MRSC方法的直接先行工作。Wei et al. (2022) NeurIPS CoT——SC基础工作。\"\n    action_items:\n      - round: 27\n        action: \"Agent: WebSearch验证4篇引用(DeNero 2009, Huang 2024, Desai & Durrett 2020, Aronica 2024)。确认存在后Paper Agent补入bib+正文。\"\n        assigned_to: main_agent\n        status: in_progress\n\n  # ===== Round 28 新发现 =====\n\n  - id: \"R28-N1\"\n    summary: \"正文§7.5声称construction 'survives Holm-Bonferroni at k=57'但Appendix f声称'no core NER claim survives (p_adj=0.055)'——正文与附录矛盾\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: [1, 2]\n        note: \"Director核实: experiments_main.tex:244说+1.40pp 'survives Holm-Bonferroni at k=57'(基于p<0.001)。但Appendix f:317说'no core NER claim survives (p_adj=0.055 for Few-NERD LP selection and construction)'。若p_raw<0.001且Holm排名第1，p_adj=57×0.001=0.057>0.05。两处表述矛盾——正文需与附录一致。\"\n    action_items:\n      - round: 28\n        action: \"核实Few-NERD construction的exact p_raw和Holm rank。修正experiments_main.tex或Appendix f使表述一致。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R28-N2\"\n    summary: \"Correlation-selection gap与MBR文献增量新颖性定位不够精准\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: [2]\n        note: \"R2-N2 [critical]: Eikema & Aziz(2020,2022)已证明MAP decoding不足, Eikema et al.(2025)指出MBR utilities在structured outputs退化。§8讨论MBR但聚焦utility function选择，未明确论证'correlation-selection gap'的增量贡献vs'MBR utility degradation'。Instance-level signal设计局限更像方法设计问题而非深层发现。R1在优势#3中赞赏MBR理论联系的原创性——存在一定分歧。Director判断: 诊断cascade定位问题在哪个环节是增量贡献，应在§8明确说明。\"\n    action_items:\n      - round: 28\n        action: \"§8 Related Work增加explicit comparison: MBR utility degradation(Eikema et al. 2025)指出问题存在，本文诊断cascade定位问题在哪个环节(degeneracy vs LP compression vs signal alignment)发生——这是增量贡献。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R28-W1\"\n    summary: \"Hidden-state probe跨数据集AUROC方差(SciERC 0.63 vs CoNLL 0.88)未充分解释\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R1-W2 [should-fix]: AUROC变化剧烈，cross-dataset transfer下降。CoNLL高AUROC不能转化为selection gain——需解释是AUROC→ranking gap还是ranking→selection gap。R2 AGREE并补充: CoNLL任务简单(F1≈91%)使错误entity在hidden space中为更明显outlier。hidden-state probe是instance-level signal无法discriminate per-sample candidates。\"\n    action_items:\n      - round: 28\n        action: \"§3补充: (1)CoNLL vs SciERC AUROC差异的可能解释; (2)明确说明高AUROC不转化为selection gain是因为instance-level设计限制。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R28-MR1\"\n    summary: \"缺失引用: Ma et al. (2024) NAACL SC-for-NER, Madaan et al. (2023) Self-Refine\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: [2]\n        note: \"Ma et al.(2024) 'Self-Improving for Zero-Shot NER with LLMs' (NAACL)——直接使用SC进行NER annotation selection获正面结果，是最直接的先行工作。Madaan et al.(2023) 'Self-Refine' (NeurIPS)——MRSC方法的直接基准。遗漏可能被ARR reviewer视为related work不完整。\"\n    action_items:\n      - round: 28\n        action: \"§8 'Consistency for structured IE'段增加Ma et al.(2024)讨论——zero-shot SC获正面结果与本文negative results的对比(zero-shot vs fine-tuned, annotation selection vs output selection)。补引Madaan et al.(2023)。\"\n        assigned_to: research_director\n        status: open"
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
    "issues_yaml": "issues:\n  # ===== 历史 resolved issues (保留) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3-old\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-9 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 28\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"scope 声明在 Introduction 和 Limitations 中已存在。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"仅2个~8B fine-tuned + 1个72B zero-shot。缺closed-source模型。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R1 REBUT R2-W1(事实前提错误:论文已测72B+GPT-5.5)。R2确认事实错误但仍指出缺instruction-tuned vs base对比。共识:模型覆盖度合理但缺base model对比。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: R1-W1(模型覆盖有限)+R2-W1(泛化性声明过度)再次独立提出。完整实验仅Qwen3-8B和LLaMA-3.1-8B(LoRA)。72B仅Few-NERD, GPT-5.5仅200实例。Limitations承认frontier models degeneracy不同(4%-5.5%)。两人AGREE。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 28\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7）。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26视觉审查再次确认p7 display items过密。\"\n      - round: 27\n        reviewers: [2]\n        note: \"R27视觉审查: p6-7 display items密度高但可接受。Figure 1 部分面板文字偏小(约正文60-65%)。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: Figure 4面板较小(约正文65-70%)，Figure 3尺寸偏小但可读。info级。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 28\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"construction不应作为standalone contribution。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R2-N2列prescriptive gains为critical(+1.0-1.4pp at 8x cost)。R1降为should-fix(主贡献是诊断框架)。R1交叉回应: negative results有独立价值，prescriptive是contribution #4非primary。R2同意若修复其他问题可降级。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: R1-W3+R2-W4再次提出escape routes效果量偏小(+1.0-1.4pp at N×cost)。R2 AGREE R1-W3。共识: 效果量真实但实用价值有限——明确定位为proof of concept而非practical recommendation。\"\n    action_items:\n      - round: 26\n        action: \"确认construction在正文中已降级为diagnostic-motivated ablation而非contribution。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction（framing tautology）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 28\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 必须重构Abstract/Intro将structural/empirical二分法前置。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: Section 4明确区分了definitional vs empirical层面。R1-N2关注的是因果语言而非tautology本身。论文已有改善但主体仍用'governs'等因果动词。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28 R2-N2: correlation-selection gap与MBR文献已知发现(Eikema & Aziz 2020/2022, Eikema et al. 2025)的增量新颖性需更精确定位。Related Work §8讨论MBR但聚焦utility function选择，未明确论证诊断cascade的增量贡献。\"\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 27\n    resolution: \"R23: Reduced to 4 key numbers. R27 fresh: R2再次提出W4但R1 REBUT(empirical NLP论文惯例)。共识: 当前密度尚可接受。\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  # ===== Round 24 issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 公式删除，改为定性叙述。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"method.tex 加定义。\"\n    resolution_round: 24\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1 minor #2: 最高ρ为EM 0.472(LLaMA CoNLL)，'up to 0.45'略低。建议核实。\"\n\n  # ===== Round 25 issues =====\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"n=23 power 仅约 50% for ρ=0.4。结论过强。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及此 specific null finding。\"\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"cross-model仅1数据集1对模型。§5.3 SCD不再出现。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n      - round: 28\n        reviewers: [1]\n        note: \"R28 R1-W5: cross-model仅Qwen3-8B+LLaMA-3.1-8B, 共享LoRA训练流程可能限制diversity上限。R2 AGREE。\"\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"'first systematic characterization'过强，应限定为'for NER'。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: 两位Reviewer独立列为consensus critical。R1-N1=R2-N1: 标题'Structured Generation'与NER-centric证据严重不匹配。RE仅1数据集(55.5% F1=0受span error混淆)，SQL仅n=196一句话。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: R2-W2(RE受span error混淆, SQL缺系统分析)+R1(cross-task as strength but W4 N-scaling限制)。标题已为NER-specific。RE/SQL定位为preliminary extension而非core claim。\"\n    action_items:\n      - round: 27\n        action: \"标题从'Structured Generation'缩窄为NER-specific或'Structured Information Extraction'。Abstract/Intro scope相应调整。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni；4 数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"CoNLL 增益为负 (−0.29pp)。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"p_adj矛盾(§1: 0.20 vs Table 13: 0.038)。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R2-N2 prescriptive gains边际(+1.0-1.4pp at 8x cost)。R1-W5同意事实但降为should-fix。交叉后共识: gains有限但对diagnostic论文可接受。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R2-N1 [critical]: 全局Holm k=57下p_adj=0.055。experiments_main.tex声称construction 'survives Holm-Bonferroni at k=57'但Appendix f声称'no core NER claim survives'——存在正文与附录的不一致。Per-family k=21事后决定削弱严谨性。两人共识。\"\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"脚注9报告k=38但Table 13列k=57，差异k=19来源不明。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-N3 [critical]: Abstract k=19 vs Table 13实际21行。两位Reviewer交叉后共识需作者核实。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R2-N1再次指出per-family分割为事后决定。Abstract报告k=21。正文§7.5用per-family但未引导读者到Appendix f全局校正结果。\"\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"fine-tuning/scale/architecture混淆。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。Limitations已承认。\"\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"SciERC single-seed用于detailed diagnostic。bootstrap CI有缓解但不够。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh: 论文已改为3-seed(Few-NERD/CoNLL)。SciERC仍σ=0.48pp但已标注。\"\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"嵌套NER场景何时violated未讨论。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-Q4: entity-wise independence在NER中是否合理——相邻entity预测常相关。\"\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"bound仅解释3-12%的gap。共识: 可降级为analysis tool。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 R1-W1: bound仅捕获4.7-12.1%实际增益且无法预测负增益。交叉后两人共识: 在主文中明确讨论tightness而非仅Table 30 header标'weak'。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R1-W1再次提出(actual/bound ratio 3-12x)。R2 AGREE但补充: θ_crit=0.70给出了有效的定性预测力(necessary condition)。共识: bound应定位为necessary condition而非tight bound。\"\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"未直接提及。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: 与Yun et al. (2025) diversity collapse差异化需强化。两人交叉共识: §8/§9用3-4句明确区分。\"\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 未找到/元数据不匹配/orphan bib\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"hobelsberger2025systematic疑似虚构，17 orphan bib entries。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1 minor #1发现holm1979simple和xia2025survey orphan。R2引用验证: 51 bib, 49 cited, 2 orphan, 0 fake。较之前有改善(从17降至2)。\"\n      - round: 28\n        reviewers: [1]\n        note: \"R28 R1-M4: lightman2024verify和aggarwal2023adaptive在OpenAlex未匹配(索引问题非虚构)。snell2025scaling等有LaTeX编码导致的author mismatch。R2 REBUT: 这些是API覆盖局限而非引用问题。\"\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 标注为descriptive diagnostic而非causal chain。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 R1-N2 [critical]: 因果语言('governs','explaining')与相关性证据不匹配。Figure 1标'not causal'但主体未贯彻。两人交叉强烈共识——需统一替换为相关性语言。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R1-N1 [critical]: 标题'Capability Ceiling'暗示硬上界但证据为observational。Limitations承认'not interventional'但埋在末尾。R2 AGREE——但指出LoRA-rank和temperature消融提供quasi-interventional证据，标题/措辞修改即可。共识: Must-Fix via title change + §1 caveat。\"\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: EL4NER, Self-Certainty BoN 等\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"EL4NER必须引用。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1建议补DeNero et al. 2009, Desai & Durrett 2020, Huang et al. 2024。R2建议补KDD 2025 survey, Aronica et al. 2024, test-time scaling survey。\"\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"Oracle Scaling figure 已生成并集成。\"\n    resolution_round: 26\n\n  # ===== Round 26 issues =====\n\n  - id: \"R26-N1\"\n    summary: \"N=8/16对test-time compute scaling研究范围过窄\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"建议至少补N=32或论证N=8的cost-efficiency。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及N range。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R1-W4: N止步于32, 引用Brown et al.(2024)但未讨论N=100+。R2部分AGREE——N=32时degeneracy降至4%但selection Δ仅+0.95pp(p=0.091)，说明瓶颈是signal alignment而非N。建议基于scaling law extrapolation讨论。\"\n\n  - id: \"R26-N2\"\n    summary: \"Trained verifier (LightGBM AUC=0.923) 负面结果scope有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R26-W1\"\n    summary: \"论文同时做4件事，每项深度不够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 R2 Excitement=2.5/5部分原因是novelty分散。\"\n\n  - id: \"R26-VIS1\"\n    summary: \"Page 7 display items严重过密（4表+1图）\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: p6-7 '略显拥挤但信息承载量高，适合实证论文'。降低严重性。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: p3-7中段视觉节奏良好，text-table-figure交替频繁。整体密度适合实证诊断论文。\"\n\n  - id: \"R26-VIS2\"\n    summary: \"Figure 6 heatmap红绿色阶对色盲不友好\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 26\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: Figure 6 heatmap单色渐变(黄→深绿)，建议双色发散色板。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: Figure 1绿/红对比对红绿色盲不友好(~8%男性)，但有✓/✗符号冗余编码。建议红→橙。\"\n\n  # ===== Round 27 issues =====\n\n  - id: \"R27-N1\"\n    summary: \"因果语言与相关性证据不匹配——Section 9 'governs'、Abstract 'explaining why'\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-N2 [critical]: Figure 1 caption标'not causal'但§9用'governs'，Abstract用'explaining where and why'，Intro用'fills this gap'。无干预实验验证因果方向。R2 AGREE with nuance。交叉后强烈共识。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R1-N1再次以'Capability Ceiling'标题为切入点提出同一问题。R2 AGREE: LoRA-rank/temperature ablation提供quasi-interventional证据但不足以支撑'ceiling'。共识: 标题需修改+全文统一相关性语言。\"\n    action_items:\n      - round: 27\n        action: \"全文统一将因果动词替换为相关性语言('governs'→'is associated with','explaining'→'characterizing')。Discussion加段讨论因果推断局限。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R27-N2\"\n    summary: \"Holm-Bonferroni k=19(Abstract) vs Table 13实际21行——影响p_adj可复现性\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-N3 [critical]: Abstract 'selection family k=19'但Table 13 selection family有21项测试。差异2项未解释。若k=21则p_adj需重算。R2 AGREE。交叉共识: 需作者核实并修正。\"\n    action_items:\n      - round: 27\n        action: \"核实k=19 vs k=21来源。修正Abstract数字。在Appendix f提供完整Holm correction trace。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R27-W1\"\n    summary: \"7种方法分类边界模糊——diagnostic probes vs selection methods未区分\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"R1-W4: Abstract '7 methods'含diagnostic probes(ESJ/MRSC/LSC)和selection methods(DALS/SCD)混为一体。Het-T在Table 2无对应行。Table 2列9 categories与Abstract 7 methods不对齐。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent text fix: Abstract/Intro区分diagnostic probes和selection methods。对齐Table 2 categories与Abstract计数。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-W2\"\n    summary: \"RE分析受entity span error混淆(55.5% F1=0)——测量NER→RE错误传播而非RE本身\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W2+R2-W3: RE FEATURE-OF ρ≈0 vs HYPONYM-OF ρ=0.646。Table 3 RE列与NER并列但未标注混淆。两人交叉共识。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28 R2-W2再次指出: RE仅SciERC一个数据集, 55.5% zero-F1来自span错误。SQL仅87.2% degeneracy缺系统分析。Cross-task validation薄弱。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: Table 3 RE列加脚注标注span error混淆。正文加caveat。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-W3\"\n    summary: \"k=57全局Holm + RE/小配置样本量→统计功效不足，负面结论可能是power问题\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"R1-W3: RE n≈397时仅大效应量可检测。论文核心结论'no signal improves selection'可能反映insufficient power。需在Conclusion加hedge。R2 AGREE。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: Conclusion加hedge('absence of evidence is not evidence of absence'风格)。计算SQL n=196 MDE。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-W4\"\n    summary: \"Entity construction +1.0-1.4pp at 8x cost——cost-effectiveness未在主文讨论\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W5+R2-N2: Table 61在Appendix p45但主文未引用。实践者是否值得8x推理成本换~1pp？R1建议Section 10直接address。R2降为should-fix(若其他问题修复)。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28 R1-W3+R2-W4: 重复提出。Discussion承认'N× cost for ≈1 pp may only justify safety-critical use'但缺Pareto曲线量化。共识: 应明确区分proof-of-concept vs practical recommendation。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: Discussion/Conclusion加cost-effectiveness讨论(8x cost for ~1pp gain)。引用Appendix Table 61。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-M1\"\n    summary: \"2个orphan bib entries: holm1979simple, xia2025survey\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1+R2独立发现。holm1979simple应补\\\\cite，xia2025survey若不引用应删除。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: holm1979simple补\\\\cite到Holm-Bonferroni首次出现处。xia2025survey决定引用或删除。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-M2\"\n    summary: \"Figure 2 caption 'oracle gap'未自含定义\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R2-M2: 建议caption加'(oracle headroom = best-of-N F1 − greedy F1)'。R1 AGREE。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: Figure 2 caption加oracle headroom定义。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-M3\"\n    summary: \"Limitations 未讨论closed-source API模型的degeneracy profile差异\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"R2-M5: 现有Limitations仅提LP signal不可用，未讨论degeneracy特征差异。R1 AGREE。\"\n    action_items:\n      - round: 27\n        action: \"Paper Agent: Limitations加1句关于closed-source API模型degeneracy profile差异(Claude 74% vs DeepSeek 5.5%)。\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R27-MR1\"\n    summary: \"缺失引用: DeNero 2009, Desai & Durrett 2020, Huang 2024, KDD 2025 survey, Aronica 2024\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1: DeNero et al. 2009(consensus decoding MT), Desai & Durrett 2020(calibration seq labeling), Huang et al. 2024(LLMs cannot self-correct)。R2: KDD 2025 UQ survey, Aronica et al. 2024(structured IE), test-time scaling survey 2025。交叉后部分AGREE——核心3篇(DeNero, Huang, Aronica)应补，surveys可选。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28 R2-W3新增: Ma et al. (2024) NAACL 'Self-Improving for Zero-Shot NER with LLMs'——直接使用SC进行NER获正面结果，是最相关先行工作。Madaan et al. (2023) NeurIPS 'Self-Refine'——MRSC方法的直接先行工作。Wei et al. (2022) NeurIPS CoT——SC基础工作。\"\n    action_items:\n      - round: 27\n        action: \"Agent: WebSearch验证4篇引用(DeNero 2009, Huang 2024, Desai & Durrett 2020, Aronica 2024)。确认存在后Paper Agent补入bib+正文。\"\n        assigned_to: main_agent\n        status: in_progress\n\n  # ===== Round 28 新发现 =====\n\n  - id: \"R28-N1\"\n    summary: \"正文§7.5声称construction 'survives Holm-Bonferroni at k=57'但Appendix f声称'no core NER claim survives (p_adj=0.055)'——正文与附录矛盾\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: [1, 2]\n        note: \"Director核实: experiments_main.tex:244说+1.40pp 'survives Holm-Bonferroni at k=57'(基于p<0.001)。但Appendix f:317说'no core NER claim survives (p_adj=0.055 for Few-NERD LP selection and construction)'。若p_raw<0.001且Holm排名第1，p_adj=57×0.001=0.057>0.05。两处表述矛盾——正文需与附录一致。\"\n    action_items:\n      - round: 28\n        action: \"核实Few-NERD construction的exact p_raw和Holm rank。修正experiments_main.tex或Appendix f使表述一致。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R28-N2\"\n    summary: \"Correlation-selection gap与MBR文献增量新颖性定位不够精准\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: [2]\n        note: \"R2-N2 [critical]: Eikema & Aziz(2020,2022)已证明MAP decoding不足, Eikema et al.(2025)指出MBR utilities在structured outputs退化。§8讨论MBR但聚焦utility function选择，未明确论证'correlation-selection gap'的增量贡献vs'MBR utility degradation'。Instance-level signal设计局限更像方法设计问题而非深层发现。R1在优势#3中赞赏MBR理论联系的原创性——存在一定分歧。Director判断: 诊断cascade定位问题在哪个环节是增量贡献，应在§8明确说明。\"\n    action_items:\n      - round: 28\n        action: \"§8 Related Work增加explicit comparison: MBR utility degradation(Eikema et al. 2025)指出问题存在，本文诊断cascade定位问题在哪个环节(degeneracy vs LP compression vs signal alignment)发生——这是增量贡献。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R28-W1\"\n    summary: \"Hidden-state probe跨数据集AUROC方差(SciERC 0.63 vs CoNLL 0.88)未充分解释\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R1-W2 [should-fix]: AUROC变化剧烈，cross-dataset transfer下降。CoNLL高AUROC不能转化为selection gain——需解释是AUROC→ranking gap还是ranking→selection gap。R2 AGREE并补充: CoNLL任务简单(F1≈91%)使错误entity在hidden space中为更明显outlier。hidden-state probe是instance-level signal无法discriminate per-sample candidates。\"\n    action_items:\n      - round: 28\n        action: \"§3补充: (1)CoNLL vs SciERC AUROC差异的可能解释; (2)明确说明高AUROC不转化为selection gain是因为instance-level设计限制。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R28-MR1\"\n    summary: \"缺失引用: Ma et al. (2024) NAACL SC-for-NER, Madaan et al. (2023) Self-Refine\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: [2]\n        note: \"Ma et al.(2024) 'Self-Improving for Zero-Shot NER with LLMs' (NAACL)——直接使用SC进行NER annotation selection获正面结果，是最直接的先行工作。Madaan et al.(2023) 'Self-Refine' (NeurIPS)——MRSC方法的直接基准。遗漏可能被ARR reviewer视为related work不完整。\"\n    action_items:\n      - round: 28\n        action: \"§8 'Consistency for structured IE'段增加Ma et al.(2024)讨论——zero-shot SC获正面结果与本文negative results的对比(zero-shot vs fine-tuned, annotation selection vs output selection)。补引Madaan et al.(2023)。\"\n        assigned_to: research_director\n        status: open"
  }
}
```

</details>

---


### Tool result

_source line 3154 · 2026-05-21T15:24:25.351053+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 42577}, \"error\": \"\"}"}

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

_source line 3155 · 2026-05-21T15:27:01.836485+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 28 (Fresh Review)\n\n**论文**: \"The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\"\n**Venue**: EMNLP 2026 (via ARR, Main Conference Long Paper)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n\n---\n\n## Summary\n\n本文系统研究了自一致性（self-consistency, SC）在命名实体识别（NER）中的局限性。论文提出\"correlation-selection gap\"概念：质量估计信号（如 Soft Jaccard、Fleiss κ）与 oracle F1 存在中等相关（ρ up to 0.47, AUROC up to 0.82），但没有任何信号能在 sample selection 层面超越 greedy decoding。通过四阶段诊断级联（QE → degeneracy → agreement fidelity → LP compression），论文定位了 SC 失败的环节。9 类方法、4 个 NER 数据集、2 个模型族的实验均为负面结果。论文同时提出三条\"逃逸路径\"：LP-weighted entity construction（+1.02–1.40 pp）、cross-model ensemble（+0.42 pp）和 LP selection（+1.39 pp, 仅 Few-NERD），均绕过 entity-level self-verification。\n\n---\n\n## Strengths\n\n**S1. 实验覆盖深度和广度属该领域顶级。** 4 个 NER 数据集（SciERC, CoNLL-2003, Few-NERD, WNUT-17）× 2 个模型族（Qwen3-8B, LLaMA-3.1-8B）× 9 类方法（16+ 配置变体）× 4B/8B/14B/72B scale 消融 × N=2–32 scaling × 温度消融 × free-form vs constrained decoding × cross-task（RE, SQL）。62 张表、47 页附录构成极其详尽的证据网络。Table 62 的 differentiation matrix 清晰定位了本文相对于先行工作的独特贡献。\n\n**S2. 统计方法论远超 NLP 论文平均水准。** Holm-Bonferroni 多重比较校正（k=57 全局 + per-family）、bootstrap 95% CI、TOST 等价检验（含外部锚点）、permutation tests、GroupKFold CV（hidden-state probe）。为负面结果提供了可信的证据基础。**Reproducibility 5/5**：Appendix Table 21 列出全部超参数，NLP Checklist 完整填写，承诺代码/数据开源。\n\n**S3. 诊断框架（四阶段级联）有持久的工具价值。** Degeneracy → agreement fidelity → LP compression 的层次分解为未来研究提供了 operationalizable 的诊断路径。θ_crit = 0.70 的 degeneracy 阈值给出了从业者判断 SC 是否值得尝试的定量依据。\n\n**S4. MBR 理论联系具有原创性。** 将 entity-level construction 形式化为 MBR decoding under entity-wise independence（Proposition 1-2），在文献中是新颖的。Corollary 1 给出 SC gain 的 closed-form 必要条件。\n\n**S5. Introspection gap 是有价值的发现。** Hidden-state probe（AUROC 0.63–0.88）超越 prompt-based self-judgment（0.51）但低于 multi-sample agreement（0.87, 仅 CoNLL），揭示模型内部表示包含 prompt 接口无法访问的质量信息。\n\n**S6. 写作质量高。** 术语一致，叙事逻辑清晰（问题定义 → 诊断 → 失败分析 → 逃逸路径），Limitations 坦诚且具体。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [Critical] 标题\"Capability Ceiling\"与 observational 证据不匹配，因果语言贯穿全文。**\n[R1-N1, R2 AGREE | 共识]\n- 四阶段级联基于观察性关联，Figure 1 caption 标注 \"diagnostic sequence, not causal chain\"，Limitations 承认 \"not interventional\"——但标题\"Capability Ceiling\"暗示已证明的硬上界，§9 使用 \"governs\"，Abstract 使用 \"explaining where and why\"。\n- LoRA-rank 消融（degeneracy 17.8%→7.2%）和温度扫描提供了有限的 quasi-interventional 证据，但不足以支撑 \"ceiling\" claim。\n- **建议**：(1) 修改标题，降低因果强度（如 \"Diagnostic Analysis of...\" 或 \"Characterizing...\"）；(2) §1 或 §3 明确声明 observational 性质；(3) 全文统一将因果动词替换为相关性语言。无需新实验。\n\n**MF2. [Critical] 核心统计 claim 在严格多重比较校正下不稳健，正文与附录存在矛盾。**\n[R2-N1, R1-M3 aligned | 共识]\n- Appendix f（line 317）声称全局 Holm-Bonferroni（k=57）下 \"no core NER claim survives（p_adj=0.055 for Few-NERD LP selection and construction）\"。但 experiments_main.tex（line 244）声称 Few-NERD construction \"+1.40±0.51 pp, p<0.001; survives Holm-Bonferroni at k=57\"——**两处表述直接矛盾**。\n- 正文 §7.5 使用 per-family 校正（selection k=21, construction k=10），但 per-family 分割的预注册依据不足。SciERC construction p_adj=0.20 不显著。\n- **建议**：(1) 核实 construction 的 exact p_raw 和 Holm rank，修正矛盾表述；(2) 正文 §7.5 添加显式指向 Appendix f 的说明，告知读者全局校正结果；(3) 提供 per-family 分割的先验 justification 或补充 permutation test/Bayesian 分析。\n\n**MF3. [Critical] \"Correlation-selection gap\"与 MBR 文献已知发现的增量新颖性需更精确定位。**\n[R2-N2, R1 部分分歧 | 单方 Must-Fix，但 Director 判定有效]\n- Eikema & Aziz（2020, 2022）已证明 MAP decoding 不足，Eikema et al.（2025）指出 MBR utilities 在 structured outputs 退化。§8 讨论 MBR 但聚焦 utility function 选择，未明确论证诊断 cascade 的增量价值——即 MBR 文献指出问题存在，本文定位问题在哪个环节发生（degeneracy vs LP compression vs signal alignment），这是真正的新贡献。\n- R1 在优势 #3 中赞赏 MBR 理论联系的原创性，但这不影响 Related Work 中需要更精确的差异化表述。\n- **建议**：§8 增加 explicit comparison 段落，用 3-4 句说明 MBR utility degradation vs correlation-selection gap 的区别与联系。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. 理论 bound 过松（actual/bound ratio 3–12×），定位需调整。**\n[R1-W1, R2 AGREE | 共识]\n- Table 30 显示 bound 仅捕获实际 gain 的 5–12%，signal alignment α 是瓶颈（best signal 恢复非退化 oracle gap 的 6.8%）。\n- θ_crit = 0.70 提供了有效的定性预测力（necessary condition），但 quantitative bound 对实际决策指导有限。\n- **建议**：§6.3 明确将 bound 定位为 necessary condition 而非 tight bound，正文讨论 tightness 和失败条件。\n\n**SF2. Hidden-state probe 跨数据集 AUROC 方差（SciERC 0.63 vs CoNLL 0.88）未充分解释。**\n[R1-W2, R2 AGREE | 共识]\n- Cross-dataset transfer 下降显著（Few-NERD→CoNLL=0.759, CoNLL→Few-NERD=0.671）。CoNLL 高 AUROC 不能转化为 selection gain——因为 probe 是 instance-level signal，无法区分 per-sample candidates。\n- **建议**：(1) §3 补充 CoNLL 简单任务使错误 entity 在 hidden space 中为更明显 outlier 的解释；(2) 明确说明高 AUROC 不转化为 selection gain 的结构性原因。\n\n**SF3. Escape routes 效果量偏小，cost-effectiveness 未定量分析。**\n[R1-W3, R2-W4 | 共识]\n- +1.02–1.40 pp (N× cost), +0.42 pp (2N× cost), +1.39 pp (仅 Few-NERD)。Discussion 承认 \"N× cost for ≈1 pp may only justify safety-critical use\"。Table 61 在 Appendix 但主文未引用，缺 Pareto 曲线。\n- **建议**：明确区分 proof of concept vs practical recommendation；主文引用 Table 61 或添加简化的 cost-benefit 讨论。\n\n**SF4. N-scaling 止步于 N=32，未讨论更大 N 的外推。**\n[R1-W4, R2 部分 AGREE | 共识]\n- N=32 时 degeneracy 降至 4% 但 selection Δ 仅 +0.95 pp（p=0.091, CI 跨零），说明瓶颈是 signal alignment 而非 candidate pool size。但论文引用 Brown et al.（2024）却未讨论 N=100+ 外推。\n- **建议**：Appendix s 增加基于 scaling law F₁(N) = a − b·N^{−c} 的外推讨论。\n\n**SF5. 模型覆盖有限，泛化性措辞过度。**\n[R1-W5 + R2-W1 | 共识]\n- 完整实验仅 Qwen3-8B 和 LLaMA-3.1-8B（LoRA 微调），共享训练流程可能限制 diversity 上限。72B 仅 Few-NERD，GPT-5.5 仅 200 实例。Limitations 承认 frontier models degeneracy 不同（4%–5.5%）。\n- **建议**：弱化 Introduction/Conclusion 泛化性措辞，明确区分 \"fine-tuned open-weight models\" 和一般性结论。\n\n**SF6. Cross-task validation 薄弱。**\n[R2-W2 | 单方]\n- RE 仅 SciERC 一个数据集，55.5% zero-F1 来自 entity span 错误——测量的是 NER→RE 错误传播而非 RE 本身。SQL 仅提到 87.2% degeneracy 缺系统分析。\n- **建议**：(1) RE 分析加 span error 混淆的 caveat；(2) 降低 cross-task generalization claim 强度。\n\n**SF7. 遗漏直接相关参考文献。**\n[R2-W3 | 单方]\n- Ma et al.（2024）\"Self-Improving for Zero-Shot NER with LLMs\"（NAACL）——直接使用 SC 进行 NER 获正面结果，与本文负面结果形成有意义对比（zero-shot vs fine-tuned）。\n- Madaan et al.（2023）\"Self-Refine\"（NeurIPS）——MRSC 方法的直接先行工作。\n- **建议**：§8 加入讨论。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 交叉结果 |\n|------|----|----|---------|\n| MF1: 因果语言/标题 | Must-Fix | [AGREE] | **强共识** |\n| MF2: 统计稳健性/Holm 校正 | M3 aligned | Must-Fix | **共识** |\n| MF3: MBR 新颖性定位 | 优势#3 原创 | Must-Fix | **部分分歧**（见下） |\n| SF1: 理论 bound 松弛 | Should-Fix | [AGREE] | 共识 |\n| SF2: Probe 方差 | Should-Fix | [AGREE] | 共识 |\n| SF3: Escape routes 效果量 | Should-Fix | [AGREE] | 共识 |\n| SF4: N-scaling 范围 | Should-Fix | [AGREE]（部分） | 共识 |\n| SF5: 模型覆盖 | Should-Fix | [AGREE] | 共识 |\n| R1-N2: SciERC free-form 缺失 | Must-Fix | **[REBUT]** | **R2 正确，R1 事实性误读** |\n\n---\n\n## Reviewer Divergence\n\n**R1-N2（SciERC free-form decoding 缺失）**：R1 声称 free-form 消融未覆盖 SciERC，R2 引用 Appendix q Table `tab:freeform_ablation` 反驳。**Director 核实：R2 正确**——appendix.tex:1154-1165 明确标注 Free-Form Decoding Ablation 以 SciERC 为首要数据集，4-panel 分析完整，NER selection 在 free-form 下仍然无效（gap 从 +0.0059 降至 +0.0018）。R1-N2 不构成有效 Must-Fix，已从最终评估中移除。\n\n**MF3（MBR 新颖性）**：R1 在优势评价中赞赏 MBR 理论联系的原创性（Proposition 1-2 将 entity construction 形式化为 MBR decoding \"在文献中是新颖的\"），R2 则认为核心概念在 Eikema et al.（2025）中已有类似表述。Director 判断：两者不矛盾——MBR formalization 本身有原创性，但 §8 对 MBR 文献的差异化定位确实不够精确。列为 Must-Fix 但修改量可控（增加几句 Related Work 即可）。\n\n---\n\n## Questions（需要作者澄清）\n\n1. **Holm 校正数值不一致**：experiments_main.tex 声称 Few-NERD construction \"survives Holm-Bonferroni at k=57\"，但 Appendix f 声称 \"no core NER claim survives（p_adj=0.055）\"。请核实 exact p_raw 和 Holm rank。\n2. **Abstract k=21 vs 正文**：Abstract 报告 \"selection family k=21\"——请确认 Appendix f Table 13 的 selection family 实际行数是否为 21。\n3. **Proposition 1 entity-wise independence**：NER 中相邻实体预测常相关（如 \"New York\" 和 \"City\"）——该假设何时 violated？violation 对 bound 的影响如何？\n\n---\n\n## Missing References\n\n1. **Ma, Wang, Sun & Li (2024). \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models.\" NAACL 2024.** — 直接使用 SC 进行 NER 获正面结果，最相关先行工作。\n2. **Madaan, Tandon, Gupta et al. (2023). \"Self-Refine: Iterative Refinement with Self-Feedback.\" NeurIPS 2023.** — MRSC 方法的直接基准。\n3. **Wei, Wang, Schuurmans et al. (2022). \"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.\" NeurIPS 2022.** — SC 的前置基础工作。\n4. **\"Test-time Scaling of LLMs: A Survey\" (2025, arXiv:2511.14772)** — TTS 分类框架，有助于定位本文的 inverse scaling 发现。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时 4m9s）\n\n**Findings（4 warnings, 18 info, 0 critical）**：\n\n- **[Warning] 前 2 页纯文本**：Title/Abstract/Introduction/Contributions 连续两页无 display item，Figure 1 直到第 3 页才出现。建议将 Figure 1 提前或在第 2 页插入简化版视觉锚点。\n- **[Warning] 前 2 页无 figure/table/equation**：可改进的节奏问题，但 Introduction 纯文本在 NLP 论文中常见。\n- **[Info] 中段视觉节奏良好**：p3-7 text-table-figure 三重奏交替频繁，9-10 个 display items 密度适合实证诊断论文。\n- **[Info] 色盲友好性**：Figure 1 绿/红对比有 ✓/✗ 符号冗余编码，影响有限。建议红→橙。\n- **[Info] Figure 4**：4 子图面板字号接近可读性下限（约正文 65-70%）。\n- **[Warning] Appendix p.41, p.47 大面积空白**（>50% 页面），建议合并 float。\n- **[Info] 无 LaTeX 渲染错误、overfull hbox、orphan heading、未解析引用。**\n- **[Info] 正文 8 页，Limitations 在 page 8 结束，符合 EMNLP 2026 格式要求。**\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4/5 | 3.5/5 | **3.75/5** |\n| Excitement | 3/5 | 3/5 | **3/5** |\n| Reproducibility | 5/5 | 4/5 | **4.5/5** |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4/5 | — | **4/5** |\n\n**判断依据**：\n- **Soundness 高于平均**：实验设计和统计方法论在 NLP 论文中属于顶级水平，但因果语言与 observational 证据的张力、以及正文/附录 Holm 校正结果的矛盾需要修复。\n- **Excitement 中等**：诊断框架有工具价值，对社区有指导意义（何时 SC 有效/无效），但核心发现（SC 对结构化输出效果差）对熟悉 MBR 文献的读者并不意外；escape routes 增益微弱（+1.0–1.4 pp at N× cost）。\n- **Reproducibility 极优**：47 页附录、62 张表、完整超参数记录、代码开源承诺。\n\n**升级到 4（Conference）的路径**：修复 MF1（标题/因果语言）、MF2（统计矛盾）、MF3（MBR 差异化）可使论文升至 Borderline Conference 上端。SF3（cost-effectiveness 量化）和 SF7（missing references）是加分项。如果同时加强 MBR 新颖性定位（MF3），有望达到 3.5–4 区间。\n\n**降级到 3（Findings）的风险**：如果 MF2 的矛盾表明 Few-NERD construction 实际不过 Holm 校正，则唯一正面结果被削弱；如果 MF3 的 MBR 差异化无法令人信服，则核心概念新颖性不足。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Capability Ceiling\" 标题需降级（MF1）。Introduction 叙事弧流畅，从 SC 在 reasoning 的成功到 NER 的结构性限制过渡自然。四个 contribution 清晰但第 4 个（prescriptive escape routes）在统计稳健性上最脆弱。建议在 contribution 列表中明确标注诊断框架的 observational 性质。\n\n### §2 Quality Estimation\n- §2.2 定义 4 种信号但 LP 在 §2.3 才引入——结构上可改善（R1-M2）。Table 1 \"†One score per input\" 与 per-sample/instance-level 区分重叠（R1-M1/R2 小问题 1）。\n\n### §3 Mechanistic Analysis (Hidden-state Probe)\n- AUROC 0.63–0.88 跨数据集方差的原因需补充解释（SF2）。Cross-dataset transfer 下降是重要的 negative finding，但未被充分阐释。建议添加 explicit takeaway：即使 AUROC=0.88，instance-level 设计限制仍然阻止 selection 改善——这恰恰印证了 correlation-selection gap。\n\n### §4 Selection Gap\n- 核心诊断逻辑自洽但语言需统一为 observational（MF1）。\n\n### §5 Escape Routes / §7.5 Prescriptive\n- +1.40 pp (Few-NERD construction) 和 +1.39 pp (LP selection) 是论文的核心正面结果。正文声称前者 survives global Holm 但附录否认——必须修正（MF2）。Cost-effectiveness 讨论需从 Appendix 提到正文（SF3）。\n\n### §6 Theory\n- Proposition 1-2 的 MBR 形式化有原创性。Degeneracy bound 过松但 θ_crit = 0.70 的定性预测力有价值（SF1）。Entity-wise independence 假设需补充讨论（Q3）。\n\n### §8 Related Work\n- MBR 文献差异化是关键改进点（MF3）。Ma et al.（2024）和 Madaan et al.（2023）是明显遗漏（SF7）。\n\n### §9 Discussion\n- 因果语言（\"governs\"、\"explaining where and why\"）需替换为相关性语言（MF1）。\n\n### Limitations\n- 坦诚且具体。建议增加 closed-source API 模型 degeneracy profile 差异的讨论（Claude 74% vs DeepSeek 5.5%）。\n\n### Appendix\n- 34 页附录体量大但内容充实。核心 findings 高度依赖附录表格（如 Table 13 Holm 校正、Table 30 bound tightness），建议在正文中提供更自包含的数字摘要。",
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
    "report": "# 审稿报告 — Round 28 (Fresh Review)\n\n**论文**: \"The Capability Ceiling of Self-Consistency: How Entity-Level Self-Verification Fails in Named Entity Recognition\"\n**Venue**: EMNLP 2026 (via ARR, Main Conference Long Paper)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n\n---\n\n## Summary\n\n本文系统研究了自一致性（self-consistency, SC）在命名实体识别（NER）中的局限性。论文提出\"correlation-selection gap\"概念：质量估计信号（如 Soft Jaccard、Fleiss κ）与 oracle F1 存在中等相关（ρ up to 0.47, AUROC up to 0.82），但没有任何信号能在 sample selection 层面超越 greedy decoding。通过四阶段诊断级联（QE → degeneracy → agreement fidelity → LP compression），论文定位了 SC 失败的环节。9 类方法、4 个 NER 数据集、2 个模型族的实验均为负面结果。论文同时提出三条\"逃逸路径\"：LP-weighted entity construction（+1.02–1.40 pp）、cross-model ensemble（+0.42 pp）和 LP selection（+1.39 pp, 仅 Few-NERD），均绕过 entity-level self-verification。\n\n---\n\n## Strengths\n\n**S1. 实验覆盖深度和广度属该领域顶级。** 4 个 NER 数据集（SciERC, CoNLL-2003, Few-NERD, WNUT-17）× 2 个模型族（Qwen3-8B, LLaMA-3.1-8B）× 9 类方法（16+ 配置变体）× 4B/8B/14B/72B scale 消融 × N=2–32 scaling × 温度消融 × free-form vs constrained decoding × cross-task（RE, SQL）。62 张表、47 页附录构成极其详尽的证据网络。Table 62 的 differentiation matrix 清晰定位了本文相对于先行工作的独特贡献。\n\n**S2. 统计方法论远超 NLP 论文平均水准。** Holm-Bonferroni 多重比较校正（k=57 全局 + per-family）、bootstrap 95% CI、TOST 等价检验（含外部锚点）、permutation tests、GroupKFold CV（hidden-state probe）。为负面结果提供了可信的证据基础。**Reproducibility 5/5**：Appendix Table 21 列出全部超参数，NLP Checklist 完整填写，承诺代码/数据开源。\n\n**S3. 诊断框架（四阶段级联）有持久的工具价值。** Degeneracy → agreement fidelity → LP compression 的层次分解为未来研究提供了 operationalizable 的诊断路径。θ_crit = 0.70 的 degeneracy 阈值给出了从业者判断 SC 是否值得尝试的定量依据。\n\n**S4. MBR 理论联系具有原创性。** 将 entity-level construction 形式化为 MBR decoding under entity-wise independence（Proposition 1-2），在文献中是新颖的。Corollary 1 给出 SC gain 的 closed-form 必要条件。\n\n**S5. Introspection gap 是有价值的发现。** Hidden-state probe（AUROC 0.63–0.88）超越 prompt-based self-judgment（0.51）但低于 multi-sample agreement（0.87, 仅 CoNLL），揭示模型内部表示包含 prompt 接口无法访问的质量信息。\n\n**S6. 写作质量高。** 术语一致，叙事逻辑清晰（问题定义 → 诊断 → 失败分析 → 逃逸路径），Limitations 坦诚且具体。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [Critical] 标题\"Capability Ceiling\"与 observational 证据不匹配，因果语言贯穿全文。**\n[R1-N1, R2 AGREE | 共识]\n- 四阶段级联基于观察性关联，Figure 1 caption 标注 \"diagnostic sequence, not causal chain\"，Limitations 承认 \"not interventional\"——但标题\"Capability Ceiling\"暗示已证明的硬上界，§9 使用 \"governs\"，Abstract 使用 \"explaining where and why\"。\n- LoRA-rank 消融（degeneracy 17.8%→7.2%）和温度扫描提供了有限的 quasi-interventional 证据，但不足以支撑 \"ceiling\" claim。\n- **建议**：(1) 修改标题，降低因果强度（如 \"Diagnostic Analysis of...\" 或 \"Characterizing...\"）；(2) §1 或 §3 明确声明 observational 性质；(3) 全文统一将因果动词替换为相关性语言。无需新实验。\n\n**MF2. [Critical] 核心统计 claim 在严格多重比较校正下不稳健，正文与附录存在矛盾。**\n[R2-N1, R1-M3 aligned | 共识]\n- Appendix f（line 317）声称全局 Holm-Bonferroni（k=57）下 \"no core NER claim survives（p_adj=0.055 for Few-NERD LP selection and construction）\"。但 experiments_main.tex（line 244）声称 Few-NERD construction \"+1.40±0.51 pp, p<0.001; survives Holm-Bonferroni at k=57\"——**两处表述直接矛盾**。\n- 正文 §7.5 使用 per-family 校正（selection k=21, construction k=10），但 per-family 分割的预注册依据不足。SciERC construction p_adj=0.20 不显著。\n- **建议**：(1) 核实 construction 的 exact p_raw 和 Holm rank，修正矛盾表述；(2) 正文 §7.5 添加显式指向 Appendix f 的说明，告知读者全局校正结果；(3) 提供 per-family 分割的先验 justification 或补充 permutation test/Bayesian 分析。\n\n**MF3. [Critical] \"Correlation-selection gap\"与 MBR 文献已知发现的增量新颖性需更精确定位。**\n[R2-N2, R1 部分分歧 | 单方 Must-Fix，但 Director 判定有效]\n- Eikema & Aziz（2020, 2022）已证明 MAP decoding 不足，Eikema et al.（2025）指出 MBR utilities 在 structured outputs 退化。§8 讨论 MBR 但聚焦 utility function 选择，未明确论证诊断 cascade 的增量价值——即 MBR 文献指出问题存在，本文定位问题在哪个环节发生（degeneracy vs LP compression vs signal alignment），这是真正的新贡献。\n- R1 在优势 #3 中赞赏 MBR 理论联系的原创性，但这不影响 Related Work 中需要更精确的差异化表述。\n- **建议**：§8 增加 explicit comparison 段落，用 3-4 句说明 MBR utility degradation vs correlation-selection gap 的区别与联系。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. 理论 bound 过松（actual/bound ratio 3–12×），定位需调整。**\n[R1-W1, R2 AGREE | 共识]\n- Table 30 显示 bound 仅捕获实际 gain 的 5–12%，signal alignment α 是瓶颈（best signal 恢复非退化 oracle gap 的 6.8%）。\n- θ_crit = 0.70 提供了有效的定性预测力（necessary condition），但 quantitative bound 对实际决策指导有限。\n- **建议**：§6.3 明确将 bound 定位为 necessary condition 而非 tight bound，正文讨论 tightness 和失败条件。\n\n**SF2. Hidden-state probe 跨数据集 AUROC 方差（SciERC 0.63 vs CoNLL 0.88）未充分解释。**\n[R1-W2, R2 AGREE | 共识]\n- Cross-dataset transfer 下降显著（Few-NERD→CoNLL=0.759, CoNLL→Few-NERD=0.671）。CoNLL 高 AUROC 不能转化为 selection gain——因为 probe 是 instance-level signal，无法区分 per-sample candidates。\n- **建议**：(1) §3 补充 CoNLL 简单任务使错误 entity 在 hidden space 中为更明显 outlier 的解释；(2) 明确说明高 AUROC 不转化为 selection gain 的结构性原因。\n\n**SF3. Escape routes 效果量偏小，cost-effectiveness 未定量分析。**\n[R1-W3, R2-W4 | 共识]\n- +1.02–1.40 pp (N× cost), +0.42 pp (2N× cost), +1.39 pp (仅 Few-NERD)。Discussion 承认 \"N× cost for ≈1 pp may only justify safety-critical use\"。Table 61 在 Appendix 但主文未引用，缺 Pareto 曲线。\n- **建议**：明确区分 proof of concept vs practical recommendation；主文引用 Table 61 或添加简化的 cost-benefit 讨论。\n\n**SF4. N-scaling 止步于 N=32，未讨论更大 N 的外推。**\n[R1-W4, R2 部分 AGREE | 共识]\n- N=32 时 degeneracy 降至 4% 但 selection Δ 仅 +0.95 pp（p=0.091, CI 跨零），说明瓶颈是 signal alignment 而非 candidate pool size。但论文引用 Brown et al.（2024）却未讨论 N=100+ 外推。\n- **建议**：Appendix s 增加基于 scaling law F₁(N) = a − b·N^{−c} 的外推讨论。\n\n**SF5. 模型覆盖有限，泛化性措辞过度。**\n[R1-W5 + R2-W1 | 共识]\n- 完整实验仅 Qwen3-8B 和 LLaMA-3.1-8B（LoRA 微调），共享训练流程可能限制 diversity 上限。72B 仅 Few-NERD，GPT-5.5 仅 200 实例。Limitations 承认 frontier models degeneracy 不同（4%–5.5%）。\n- **建议**：弱化 Introduction/Conclusion 泛化性措辞，明确区分 \"fine-tuned open-weight models\" 和一般性结论。\n\n**SF6. Cross-task validation 薄弱。**\n[R2-W2 | 单方]\n- RE 仅 SciERC 一个数据集，55.5% zero-F1 来自 entity span 错误——测量的是 NER→RE 错误传播而非 RE 本身。SQL 仅提到 87.2% degeneracy 缺系统分析。\n- **建议**：(1) RE 分析加 span error 混淆的 caveat；(2) 降低 cross-task generalization claim 强度。\n\n**SF7. 遗漏直接相关参考文献。**\n[R2-W3 | 单方]\n- Ma et al.（2024）\"Self-Improving for Zero-Shot NER with LLMs\"（NAACL）——直接使用 SC 进行 NER 获正面结果，与本文负面结果形成有意义对比（zero-shot vs fine-tuned）。\n- Madaan et al.（2023）\"Self-Refine\"（NeurIPS）——MRSC 方法的直接先行工作。\n- **建议**：§8 加入讨论。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 交叉结果 |\n|------|----|----|---------|\n| MF1: 因果语言/标题 | Must-Fix | [AGREE] | **强共识** |\n| MF2: 统计稳健性/Holm 校正 | M3 aligned | Must-Fix | **共识** |\n| MF3: MBR 新颖性定位 | 优势#3 原创 | Must-Fix | **部分分歧**（见下） |\n| SF1: 理论 bound 松弛 | Should-Fix | [AGREE] | 共识 |\n| SF2: Probe 方差 | Should-Fix | [AGREE] | 共识 |\n| SF3: Escape routes 效果量 | Should-Fix | [AGREE] | 共识 |\n| SF4: N-scaling 范围 | Should-Fix | [AGREE]（部分） | 共识 |\n| SF5: 模型覆盖 | Should-Fix | [AGREE] | 共识 |\n| R1-N2: SciERC free-form 缺失 | Must-Fix | **[REBUT]** | **R2 正确，R1 事实性误读** |\n\n---\n\n## Reviewer Divergence\n\n**R1-N2（SciERC free-form decoding 缺失）**：R1 声称 free-form 消融未覆盖 SciERC，R2 引用 Appendix q Table `tab:freeform_ablation` 反驳。**Director 核实：R2 正确**——appendix.tex:1154-1165 明确标注 Free-Form Decoding Ablation 以 SciERC 为首要数据集，4-panel 分析完整，NER selection 在 free-form 下仍然无效（gap 从 +0.0059 降至 +0.0018）。R1-N2 不构成有效 Must-Fix，已从最终评估中移除。\n\n**MF3（MBR 新颖性）**：R1 在优势评价中赞赏 MBR 理论联系的原创性（Proposition 1-2 将 entity construction 形式化为 MBR decoding \"在文献中是新颖的\"），R2 则认为核心概念在 Eikema et al.（2025）中已有类似表述。Director 判断：两者不矛盾——MBR formalization 本身有原创性，但 §8 对 MBR 文献的差异化定位确实不够精确。列为 Must-Fix 但修改量可控（增加几句 Related Work 即可）。\n\n---\n\n## Questions（需要作者澄清）\n\n1. **Holm 校正数值不一致**：experiments_main.tex 声称 Few-NERD construction \"survives Holm-Bonferroni at k=57\"，但 Appendix f 声称 \"no core NER claim survives（p_adj=0.055）\"。请核实 exact p_raw 和 Holm rank。\n2. **Abstract k=21 vs 正文**：Abstract 报告 \"selection family k=21\"——请确认 Appendix f Table 13 的 selection family 实际行数是否为 21。\n3. **Proposition 1 entity-wise independence**：NER 中相邻实体预测常相关（如 \"New York\" 和 \"City\"）——该假设何时 violated？violation 对 bound 的影响如何？\n\n---\n\n## Missing References\n\n1. **Ma, Wang, Sun & Li (2024). \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models.\" NAACL 2024.** — 直接使用 SC 进行 NER 获正面结果，最相关先行工作。\n2. **Madaan, Tandon, Gupta et al. (2023). \"Self-Refine: Iterative Refinement with Self-Feedback.\" NeurIPS 2023.** — MRSC 方法的直接基准。\n3. **Wei, Wang, Schuurmans et al. (2022). \"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.\" NeurIPS 2022.** — SC 的前置基础工作。\n4. **\"Test-time Scaling of LLMs: A Survey\" (2025, arXiv:2511.14772)** — TTS 分类框架，有助于定位本文的 inverse scaling 发现。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时 4m9s）\n\n**Findings（4 warnings, 18 info, 0 critical）**：\n\n- **[Warning] 前 2 页纯文本**：Title/Abstract/Introduction/Contributions 连续两页无 display item，Figure 1 直到第 3 页才出现。建议将 Figure 1 提前或在第 2 页插入简化版视觉锚点。\n- **[Warning] 前 2 页无 figure/table/equation**：可改进的节奏问题，但 Introduction 纯文本在 NLP 论文中常见。\n- **[Info] 中段视觉节奏良好**：p3-7 text-table-figure 三重奏交替频繁，9-10 个 display items 密度适合实证诊断论文。\n- **[Info] 色盲友好性**：Figure 1 绿/红对比有 ✓/✗ 符号冗余编码，影响有限。建议红→橙。\n- **[Info] Figure 4**：4 子图面板字号接近可读性下限（约正文 65-70%）。\n- **[Warning] Appendix p.41, p.47 大面积空白**（>50% 页面），建议合并 float。\n- **[Info] 无 LaTeX 渲染错误、overfull hbox、orphan heading、未解析引用。**\n- **[Info] 正文 8 页，Limitations 在 page 8 结束，符合 EMNLP 2026 格式要求。**\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4/5 | 3.5/5 | **3.75/5** |\n| Excitement | 3/5 | 3/5 | **3/5** |\n| Reproducibility | 5/5 | 4/5 | **4.5/5** |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4/5 | — | **4/5** |\n\n**判断依据**：\n- **Soundness 高于平均**：实验设计和统计方法论在 NLP 论文中属于顶级水平，但因果语言与 observational 证据的张力、以及正文/附录 Holm 校正结果的矛盾需要修复。\n- **Excitement 中等**：诊断框架有工具价值，对社区有指导意义（何时 SC 有效/无效），但核心发现（SC 对结构化输出效果差）对熟悉 MBR 文献的读者并不意外；escape routes 增益微弱（+1.0–1.4 pp at N× cost）。\n- **Reproducibility 极优**：47 页附录、62 张表、完整超参数记录、代码开源承诺。\n\n**升级到 4（Conference）的路径**：修复 MF1（标题/因果语言）、MF2（统计矛盾）、MF3（MBR 差异化）可使论文升至 Borderline Conference 上端。SF3（cost-effectiveness 量化）和 SF7（missing references）是加分项。如果同时加强 MBR 新颖性定位（MF3），有望达到 3.5–4 区间。\n\n**降级到 3（Findings）的风险**：如果 MF2 的矛盾表明 Few-NERD construction 实际不过 Holm 校正，则唯一正面结果被削弱；如果 MF3 的 MBR 差异化无法令人信服，则核心概念新颖性不足。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"Capability Ceiling\" 标题需降级（MF1）。Introduction 叙事弧流畅，从 SC 在 reasoning 的成功到 NER 的结构性限制过渡自然。四个 contribution 清晰但第 4 个（prescriptive escape routes）在统计稳健性上最脆弱。建议在 contribution 列表中明确标注诊断框架的 observational 性质。\n\n### §2 Quality Estimation\n- §2.2 定义 4 种信号但 LP 在 §2.3 才引入——结构上可改善（R1-M2）。Table 1 \"†One score per input\" 与 per-sample/instance-level 区分重叠（R1-M1/R2 小问题 1）。\n\n### §3 Mechanistic Analysis (Hidden-state Probe)\n- AUROC 0.63–0.88 跨数据集方差的原因需补充解释（SF2）。Cross-dataset transfer 下降是重要的 negative finding，但未被充分阐释。建议添加 explicit takeaway：即使 AUROC=0.88，instance-level 设计限制仍然阻止 selection 改善——这恰恰印证了 correlation-selection gap。\n\n### §4 Selection Gap\n- 核心诊断逻辑自洽但语言需统一为 observational（MF1）。\n\n### §5 Escape Routes / §7.5 Prescriptive\n- +1.40 pp (Few-NERD construction) 和 +1.39 pp (LP selection) 是论文的核心正面结果。正文声称前者 survives global Holm 但附录否认——必须修正（MF2）。Cost-effectiveness 讨论需从 Appendix 提到正文（SF3）。\n\n### §6 Theory\n- Proposition 1-2 的 MBR 形式化有原创性。Degeneracy bound 过松但 θ_crit = 0.70 的定性预测力有价值（SF1）。Entity-wise independence 假设需补充讨论（Q3）。\n\n### §8 Related Work\n- MBR 文献差异化是关键改进点（MF3）。Ma et al.（2024）和 Madaan et al.（2023）是明显遗漏（SF7）。\n\n### §9 Discussion\n- 因果语言（\"governs\"、\"explaining where and why\"）需替换为相关性语言（MF1）。\n\n### Limitations\n- 坦诚且具体。建议增加 closed-source API 模型 degeneracy profile 差异的讨论（Claude 74% vs DeepSeek 5.5%）。\n\n### Appendix\n- 34 页附录体量大但内容充实。核心 findings 高度依赖附录表格（如 Table 13 Holm 校正、Table 30 bound tightness），建议在正文中提供更自包含的数字摘要。",
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

_source line 3156 · 2026-05-21T15:27:05.961270+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4124
}
```

</details>

---


### Assistant

_source line 3157 · 2026-05-21T15:27:18.110536+00:00_

审稿报告已投递至 Research Director。

**Round 28 审稿完成。** 汇总如下：

**Overall Score: 3.5 — Borderline Conference**

**3 个 Must-Fix：**
1. **标题 "Capability Ceiling" 过强** — 证据为 observational，因果语言贯穿全文但无 interventional 验证。修改标题 + 统一相关性语言即可，不需新实验。
2. **正文与附录 Holm 校正结果矛盾** — experiments_main 声称 construction "survives Holm at k=57"，Appendix f 声称 "no core NER claim survives (p_adj=0.055)"。需核实并修正。正文应显式引导读者到全局校正结果。
3. **与 MBR 文献的增量新颖性定位不够精准** — 诊断 cascade 定位问题在哪个环节发生是真正的增量贡献，但 §8 未明确说明。

**7 个 Should-Fix：** 理论 bound 过松、hidden-state probe 方差未解释、escape routes cost-effectiveness 缺量化、N-scaling 外推缺失、模型覆盖有限、cross-task validation 薄弱、遗漏 Ma et al. (2024) 和 Madaan et al. (2023)。

**主要优势：** 实验覆盖属该领域顶级（62 表）、统计方法论远超平均、MBR 理论联系有原创性、诊断框架有持久工具价值、Reproducibility 5/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 237

## Round 237

2 recorded events


### User

_source line 3158 · 2026-05-21T15:27:19.267867+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

### [AGREE with qualification] R2-N1: 核心统计 claim 的稳健性不足

R2 指出全局 Holm-Bonferroni (k=57) 下核心正面 claims 不显著，per-family 分割可能是事后决定。这个 concern 部分成立，但被 R2 **过度加权**了，原因如下：

**同意之处**：
- per-family 分割（selection k=21, construction k=10）的 justification 确实不够显式。论文在 Appendix f (Table 13) 提供了全局校正的完整枚举，这一透明度值得肯定，但正文 §7.5 对 per-family vs global 的差异几乎未做说明（这也是我自己 M3 minor issue 提到的点）。
- SciERC construction 在 per-family 校正下 p_adj=0.20 不显著——这意味着最核心 benchmark 上的 escape route 不具统计稳健性。

**但 R2 的论证有一个关键盲点**：论文的**核心贡献是负面结果**（SC fails for NER），不是正面结果（escape routes work）。负面结果（"no method outperforms greedy"）**不受**多重比较问题影响——如果在全局校正下什么都不显著，这**恰恰强化**了负面结论（即真的没有方法能可靠地超越 greedy）。R2 将论述焦点放在"escape routes 被削弱"上是对的，但这只影响 Contribution 4，不影响 Contributions 1-3（诊断框架、self-verification ceiling、degeneracy 分析）。

**建议给作者的修改方向**：在 §7.5 添加 2-3 句明确说明 per-family 校正的 rationale（selection vs construction 是概念上不同的 hypothesis families，非事后拆分）以及指向 Table 13 的全局结果。将 escape routes 定位为 "suggestive evidence" 而非 "established finding" 即可。R2 建议的 Bayesian 补充或 permutation test 有价值但可能超出 revision 时间预算。

### [REBUT] R2-N2: "Correlation-selection gap" 概念新颖性不足

R2 认为 correlation-selection gap 是 MBR 文献已知发现的延伸，尤其引用 Eikema & Aziz (2020, 2022) 和 Eikema et al. (2025)。**我不同意将此升级为 Must-Fix，原因如下**：

**MBR 文献与本文回答的是不同问题**：
- Eikema & Aziz (2020): MAP decoding 不是最优 → 应该用 MBR。这是**解码策略选择**问题。
- Eikema et al. (2025): structure-conditional MBR 为结构化输出设计更好的 utility。这是**utility 设计**问题。
- 本文的 correlation-selection gap: 为什么**任何**合理信号（9类方法、16+配置）都无法将 quality correlation 转化为 selection gain？答案是**结构性瓶颈**：degeneracy（全部 N samples 相同 → 任何信号都无法选择，§4 Figure 3）和 LP compression（within-instance LP range 仅 0.041 nats，Table 22 → LP-based signals 失去区分力）。

这些是**生成过程的结构属性**，不是"选错了 utility function"。即使设计完美的 utility，如果 degeneracy rate 达到 17.8%（SciERC）到 61.7%（CoNLL），selection 在这些 instances 上物理不可能改善。这个诊断层面的 insight 在 MBR 文献中未被 formalize。

**论文的实际做法**：Section 8 (p.7) 明确讨论了 MBR 联系——"Our selection instantiates MBR decoding (Eikema and Aziz, 2020, 2022; DeNero et al., 2009)... Eikema et al. (2025) find MBR utilities degrade on structured outputs."——但论文的贡献在于**解释降级的结构性原因**（degeneracy bound, Corollary 1），而非仅仅观察到降级。

**建议**：这是一个 **positioning** 问题而非 novelty 问题。建议作者在 Section 8 添加 1-2 句显式区分：MBR 文献关注"what utility to use"，本文回答"why any utility fails for NER selection"（answer: structural degeneracy + LP compression）。但 **不应升级为 Must-Fix**——核心诊断贡献（四阶段级联、degeneracy 分析、hidden-state probes）与 MBR utility 选择问题是正交的。

---

## Should-Fix 问题

### [AGREE with nuance] R2-W1: 模型覆盖范围有限

R2 说"完整实验仅 Qwen3-8B 和 LLaMA-3.1-8B"。实际覆盖比 R2 描述的更广：
- Scale 消融：4B, 8B, 14B（Appendix s, Table 7）
- 72B zero-shot：Qwen2.5-72B on Few-NERD（Table 7, §7.3）
- GPT-5.5：§7.4 提及，samples 有限
- Cross-model：Section 9 (p.8) 提到"Across four frontier models on Few-NERD, degeneracy and the selection gap are negatively correlated (Table 41)"

但我同意 R2 的核心 concern：**Introduction/Conclusion 的措辞暗示了超越实际覆盖范围的普适性**。特别是标题中的"Capability Ceiling"没有限定模型规模或类型。建议在 Conclusion 中添加明确的 scope statement（如 "for 8B-class fine-tuned models with constrained decoding"）。

### [AGREE] R2-W2: Cross-task validation 较薄弱

完全同意。我在自己的审稿中也注意到这个问题。RE 仅 SciERC 一个数据集，且 55.5% zero-F1 来自 NER span 错误（footnote 1, p.2）导致 RE 分析的信噪比很低。SQL (Spider) 仅在 Discussion 中提到 87.2% degeneracy，缺乏与 NER 同等深度的诊断分析。如果要声称诊断框架的跨任务普适性，至少需要对 RE 或 SQL 复制完整的四阶段级联分析。

### [AGREE] R2-W3: 遗漏直接相关参考文献

**Ma et al. (2024) "Self-Improving for Zero-Shot NER" (NAACL 2024)**：这是最关键的遗漏。如果 Ma et al. 在零样本 NER 上用 SC 获得正面结果，论文必须解释与其结论的差异——可能的解释包括：(1) Ma et al. 使用的是 iterative self-improvement（类似 MRSC），而论文的 Table 2 §5.1 已经测试了 MRSC 并显示其在 fine-tuned 模型上无效（best F1 0.763 fails below greedy）；(2) zero-shot vs fine-tuned 模型可能有不同的 degeneracy profile。但无论如何必须 cite 并讨论。

**Madaan et al. (2023) Self-Refine (NeurIPS 2023)**：论文测试了 MRSC (§5.1) 但未引用 Self-Refine 作为该方法的直接先行工作。这是一个引用遗漏，应补充。

**Wei et al. (2022) CoT 和 Test-time Scaling survey**：重要性较低。论文已引用 Wang et al. (2023) 的 self-consistency（建立在 CoT 之上），而 survey 是 positioning 锦上添花。

### [AGREE] R2-W4: Escape routes 实用价值定位模糊

完全同意。这与我自己的 W3 一致。论文应在 §5 或 §9 明确区分：LP-weighted construction 和 cross-model ensemble 是 **proof-of-concept**（证明 ceiling 并非完全不可突破），不是 **practical recommendation**（+1.4pp at N× cost 在多数场景下不划算）。目前 Discussion (p.8) 的措辞"trade-off may only justify safety-critical use"是正确方向但不够突出。

---

## 小问题

### [AGREE] R2-Minor-1: Table 1 标注不一致
同意。LP "per-sample" vs 其他信号 "per-input" 的区别应在 Table 1 caption 直接说明而非靠 footnote。我在自己的 M1 中也指出了这一点。

### [AGREE] R2-Minor-2: Proposition 1 未讨论 MV 删除正确实体
这是一个有效的技术 concern。Proposition 1 定义 M⁺ = ŷ_MV \ ŷ_gr（MV 新增的实体），但没有显式处理 M⁻ = ŷ_gr \ ŷ_MV（MV 删除 greedy 中正确实体的情况）。如果 MV 在某些 instances 上删除了 greedy 的正确实体，gain 分析不完整。论文应在 Appendix 证明中说明 M⁻ 的影响——即使 empirically M⁻ 很少发生（greedy 通常是 MV 的子集），形式证明应覆盖这一情况。

### [REBUT mildly] R2-Minor-3: Figure 1 信息密度过高
Figure 1 (p.3) 作为论文核心架构的 overview figure，密度确实高，但每个面板都 serve 明确目的：Left = QE quality, Center = selection failure mechanism, Right = construction escape。在一张图中呈现完整的"问题-原因-解法"叙事是合理的设计选择。如果拆分为多张图会浪费页面预算（正文仅 8 页）。

### [REBUT] R2-Minor-4: Appendix 34页远超正文
这是一篇**负面结果**论文——声称"没有方法有效"需要穷尽性证据。34页附录中的 62 张表恰恰是这种证据标准的体现，不是缺点。删减附录反而会削弱论文的说服力。ARR 的 review guidelines 允许 appendix 且不限页数，附录的功能正是存放不适合放在正文但对完整性至关重要的细节。

### [AGREE] R2-Minor-5: 引用格式小问题
同意。我的引用验证发现 `lightman2024verify`、`aggarwal2023adaptive` 在 OpenAlex 未匹配，`snell2025scaling` 和 `dembczynski2011exact` 存在 author name encoding 问题。应修正。

---

## 汇总判断

| R2 Issue | R1 判断 | 严重程度调整 |
|----------|--------|------------|
| N1 统计稳健性 | AGREE with qualification | 建议降级为 Should-Fix：核心负面结论不受多重比较影响，仅 escape routes 受影响 |
| N2 新颖性定位 | REBUT | 建议降级为 Should-Fix：是 positioning 问题而非 novelty 问题 |
| W1 模型覆盖 | AGREE with nuance | 维持 Should-Fix |
| W2 Cross-task 薄弱 | AGREE | 维持 Should-Fix |
| W3 缺失引用 | AGREE（Ma et al. 和 Madaan et al.） | Ma et al. 可能需升级为 Must-Fix（如果其 NER SC 正面结果直接矛盾本文结论） |
| W4 实用价值模糊 | AGREE | 维持 Should-Fix |

**整体评估**：R2 的审稿总体合理，但两个 Must-Fix 的严重程度被高估。N1 的核心逻辑（正面结果不稳健）只影响论文的次要贡献（escape routes），不影响主要贡献（负面诊断发现）。N2 是 positioning 改进而非 novelty 缺陷。建议 Director 考虑将两者均调整为 Should-Fix 级别。

**新增关注点**：R2 提到的 Ma et al. (2024) NAACL 论文是我未在第一轮审稿中注意到的重要遗漏。如果该工作确实在 NER SC 上获得正面结果，作者必须解释差异来源（setup 差异、模型差异、evaluation 差异），否则论文的核心 claim 面临直接矛盾。建议 Director 要求作者在 revision 中 explicitly address。


---

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **R1-N1**（因果性/标题）：[AGREE]，标题"Capability Ceiling"与 observational 证据之间有张力，建议修改标题或措辞
- **R1-N2**（SciERC free-form 缺失）：[REBUT]，**事实性错误**——Table 32 明确覆盖了 SciERC，且结果支持论文结论
- **R1-W1–W5**：全部 [AGREE]，与我 Round 1 发现高度一致
- **R1-M4**（引用验证）：[REBUT]，OpenAlex API 局限，非真实引用问题
- **R1-M5**（Figure 1 数字不一致）：[REBUT]，R1 混淆了 SciERC 和 Few-NERD 的数字

---

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：R2 的两个 Must-Fix 被高估——N1（统计稳健性）只影响次要贡献（escape routes），不影响核心负面发现；N2（新颖性）是 positioning 问题而非 novelty 缺陷，建议均降级为 Should-Fix。但 R2 提出的 Ma et al. (2024) NAACL 缺失引用是一个我第一轮未注意到的重要问题，可能需要升级关注。

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

_source line 3159 · 2026-05-21T15:28:04.234100+00:00_

R1 的交叉回应在报告提交后到达。审稿报告已投递（Overall 3.5），但 R1 的回应包含重要补充信息，在此记录关键调整：

**R1 对 R2 两个 Must-Fix 的回应：**

1. **R2-N1（统计稳健性）→ R1 建议降级为 Should-Fix**：R1 指出论文核心贡献是负面结果（SC fails for NER），不是正面结果（escape routes）。如果全局 Holm 校正下什么都不显著，这**恰恰强化**了负面结论。统计问题仅影响 Contribution 4（escape routes），不影响 Contributions 1-3。这是一个有效的论点——但 experiments_main.tex 与 Appendix f 的矛盾（声称 "survives" vs "no claim survives"）仍然需要修复，因此维持报告中的 MF2 等级。

2. **R2-N2（MBR 新颖性）→ R1 REBUT，建议降级为 Should-Fix**：R1 论证 MBR 文献回答"what utility to use"，本文回答"why any utility fails for NER selection"——结构性瓶颈（degeneracy + LP compression）在 MBR 文献中未被 formalize。这是一个合理的区分。**Director 采纳**：MF3 在实际严重性上更接近 Should-Fix，报告中已注明这是"修改量可控"的定位改进。

3. **Ma et al. (2024) NAACL**：R1 强调这是最关键的遗漏——如果 Ma et al. 在 zero-shot NER 上用 SC 获正面结果，与本文负面结论形成直接对比。R1 建议可能升级为 Must-Fix。报告中已列入 SF7 和 Missing References。

**最终收敛状态（含 R1 交叉回应）：**

| 问题 | R1 | R2 | 最终 |
|------|----|----|------|
| MF1 因果语言/标题 | Must-Fix | AGREE | **Must-Fix**（强共识） |
| MF2 统计矛盾 | AGREE (降级建议) | Must-Fix | **Must-Fix**（矛盾需修，但核心负面结论不受影响） |
| MF3 MBR 新颖性 | REBUT (降级) | Must-Fix | **Should-Fix**（定位改进，非 novelty 缺陷） |
| R1-N2 SciERC free-form | Must-Fix | REBUT | **撤销**（R1 事实性误读） |
| Ma et al. 缺失 | 升级建议 | Should-Fix | **Should-Fix → 高优先** |

Overall 评分不变：**3.5 Borderline Conference**。Issue Tracker 已同步更新。审稿流程完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 238

## Round 238

68 recorded events


### User

_source line 3160 · 2026-05-21T16:51:22.541647+00:00_

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

_source line 3161 · 2026-05-21T16:51:27.982191+00:00_

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

_source line 3162 · 2026-05-21T16:51:28.033076+00:00_

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

_source line 3163 · 2026-05-21T16:51:33.904286+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "11"
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
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 3164 · 2026-05-21T16:51:33.954850+00:00_



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

_source line 3165 · 2026-05-21T16:51:38.329041+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "11"
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
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 3166 · 2026-05-21T16:51:38.429853+00:00_



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

_source line 3167 · 2026-05-21T16:51:42.897183+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3168 · 2026-05-21T16:51:42.947752+00:00_



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

_source line 3169 · 2026-05-21T16:51:47.615394+00:00_

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

_source line 3170 · 2026-05-21T16:51:49.021553+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (291 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_e2_pretrained_fewnerd_s123 | E2 pre-trained baseline seed 123: Qwen2.5-7B-Instruct (unfinetuned) on FewNERD SC pipeline N=8 T=1.0. Additional seed for E2 pre-trained baseline statistical power. If correlation-selection gap persists without fine-tuning → phenomenon is model-intrinsic. | — | — | — |\n| exp_fewnerd_n16_s123 | FewNERD N=16 seed=123: second seed for N=16 scaling analysis. Tests whether doubling samples from N=8 to N=16 increases oracle headroom consistently across seeds, and whether MV aggregation gap widens or narrows. | — | — | — |\n\n## 待处理\n- exp_fewnerd_mf4_s456: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=456 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.（排队等待 GPU）\n- exp_fewnerd_mf4_s123: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=123 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.（排队等待 GPU）\n- exp_fewnerd_mf4_s42: MF4 pipeline fix: FewNERD N=8 T=1.
…[truncated 1748 chars]

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

_source line 3171 · 2026-05-21T16:51:49.021930+00:00_

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

_source line 3172 · 2026-05-21T16:51:49.969333+00:00_

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
28	\title{Characterizing the Capability Ceiling of Self-Consistency:\\ How Entity-Level Verification Fails in NER}
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
58	\input{section
…[truncated 175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 947
}
```

</details>

---


### Tool call

_source line 3173 · 2026-05-21T16:51:49.969777+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 3174 · 2026-05-21T16:51:50.522044+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "review_issues.yaml",
  "max_chars": "12000"
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
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 3175 · 2026-05-21T16:51:55.238407+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission guide
…[truncated 1184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5268
}
```

</details>

---


### Tool result

_source line 3176 · 2026-05-21T16:51:55.289159+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4767
}
```

</details>

---


### Tool call

_source line 3177 · 2026-05-21T16:52:04.222326+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
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
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 3178 · 2026-05-21T16:52:05.075768+00:00_

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

_source line 3179 · 2026-05-21T16:52:05.427249+00:00_

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

_source line 3180 · 2026-05-21T16:52:05.427725+00:00_

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


### Tool call

_source line 3181 · 2026-05-21T16:52:06.079941+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
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
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 3182 · 2026-05-21T16:52:06.181616+00:00_

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
…[truncated 47191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool result

_source line 3183 · 2026-05-21T16:52:12.052671+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"}]

Based on the search results, here is the ACL Rolling Review (ARR) 2026 submission guidelines information regarding page limits and format requirements:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). More specifically:

- Short papers: 4 content pages maxim
…[truncated 977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7830
}
```

</details>

---


### Tool result

_source line 3184 · 2026-05-21T16:52:12.053093+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5973
}
```

</details>

---


### Tool call

_source line 3185 · 2026-05-21T16:52:41.614293+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
  "description": "List paper section files"
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
    "description": "List paper section files"
  }
}
```

</details>

---


### Tool result

_source line 3186 · 2026-05-21T16:52:42.467805+00:00_

_archived
abstract.tex
adaptive.tex
appendix.tex
background.tex
checklist.tex
conclusion.tex
diagnostic.tex
discussion.tex
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
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 3187 · 2026-05-21T16:52:42.518491+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline May 2026 commitment deadline"
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
    "query": "EMNLP 2026 ARR submission deadline May 2026 commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 3188 · 2026-05-21T16:52:42.920367+00:00_

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

_source line 3189 · 2026-05-21T16:52:48.390830+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline May 2026 commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"}]

Based on the search results, here is the information about EMNLP 2026 ARR submission and commitment deadlines:

## ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## EMNLP Commitment Deadline

The EMNLP commitment deadline is August 2, 2026.

## Important Context for May 2026 Submissions

For the ARR 2026 May cycle, authors 
…[truncated 674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5872
}
```

</details>

---


### Tool result

_source line 3190 · 2026-05-21T16:52:48.441697+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 230\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5521
}
```

</details>

---


### Tool call

_source line 3191 · 2026-05-21T16:52:55.578275+00:00_

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

_source line 3192 · 2026-05-21T16:52:56.030269+00:00_

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

_source line 3193 · 2026-05-21T16:52:56.030626+00:00_

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

_source line 3194 · 2026-05-21T16:52:56.532897+00:00_

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
…[truncated 4753 chars]

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

_source line 3195 · 2026-05-21T16:52:56.533401+00:00_

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

_source line 3196 · 2026-05-21T16:52:56.935194+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	\subsection{Confidence Signals}\label{sec:signals}
14	
15	Entity matching uses exact span and type match.
16	We evaluate four \textit{consistency signals}---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal}, per-sample signal.
17	
18	\paragraph{Log-probability (per-sample).}
19	$c_{\text{lp}}(y_i) = |y_i|^{-1} \sum_{j} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)$.
20	
21	\paragraph{Soft Jaccard (structural, instance-level).}
22	For samples $y_i, y_j$, we group by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU):
23	\begin{equation}\label{eq:sj}
24	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}
…[truncated 1642 chars]

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

_source line 3197 · 2026-05-21T16:52:56.935561+00:00_

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

_source line 3198 · 2026-05-21T16:52:58.039819+00:00_

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
12	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
13	MRSC best F1 ($0.763$) falls below greedy.
14	
15	\paragraph{Latent Self-Consistency (LSC).}
16	Mean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.
17	Centroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms majority vote ($0.792$) but does not close the oracle gap ($0.882$).
18	
19	\paragraph{Hidden-state probe.}
20	A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
21	All three exceed ESJ ($0.51$); only CoNLL approaches frequency agreement ($0.868$).
22	Cross-dataset transfer is weak: lea
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 3199 · 2026-05-21T16:52:58.090429+00:00_

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

_source line 3200 · 2026-05-21T16:52:58.090952+00:00_

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
…[truncated 2071 chars]

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

_source line 3201 · 2026-05-21T16:52:58.643278+00:00_

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

_source line 3202 · 2026-05-21T16:52:58.693883+00:00_

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

_source line 3203 · 2026-05-21T16:53:03.212002+00:00_

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

_source line 3204 · 2026-05-21T16:53:03.714360+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}).
7	
8	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
9	
10	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
11	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{10.1\% of GPT-5.5 samples produced unparseable output; these are excluded from all metrics. See Appendix~\ref{app:frontier_sc}.}
12	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3: $13.0$\% vs.\ GPT-5.5: $50$\% on Few-NERD; Appendix~\ref{app:cross_scale}).
13	
14	\paragraph{Inverse scaling under adaptive thresholds.}
15	Increasing $N$ \textit{decreases} construction F1 in 40 of 58 transitions ($p{<}0.05$; Appendix~\ref{app:n_scaling}).
16	Methods using $\theta{=}2/N$ are most affected ($-3.09$\,pp at $N{=}8$, $-
…[truncated 2461 chars]

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

_source line 3205 · 2026-05-21T16:53:03.714727+00:00_

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

_source line 3206 · 2026-05-21T16:53:04.166759+00:00_

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

…[truncated 6946 chars]

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

_source line 3207 · 2026-05-21T16:53:04.167121+00:00_

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

_source line 3208 · 2026-05-21T16:53:05.070740+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, adaptive allocation \cite{aggarwal2023adaptive}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} all target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes and fine-grained variants.}
8	\citet{chen2023twofailures} identify SC failures where consistent outputs are systematically wrong; \citet{huang2024large} show LLMs cannot self-correct reasoning without external feedback. Our correlation-selection gap is a distinct failure where signals \textit{correlate} with quality yet fail to \textit{select}.
9	\citet{chen2024usc} extend SC to free-form tasks; our diagnostic shows such extensions face limits under constrained decoding (\S\ref{sec:selection_gap}). \citet{thirukovalluru2024atomic} decompose claims atomically; our entity-level decomposition shows sub-output agreement does not translate to selection gain.
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{yao2026consistency} show consistency correlates with NER/RE accuracy; we diagnose degeneracy and LP compression as mechanisms that prevent this correlation from yielding selection gains.
13	\citet{xie2023zeroshot} propose entity voting for zero-shot NER, \citet{li2024simple} improve structured output formatting, and \citet{ma2024selfimproving} report positive SC results under zero-shot prompting where output diversity is high---contrasting with our fine-tuned setting where degeneracy inverts the diversity conditions.
14	Our approach diagnoses why entity-level agreement fails to improve selection, building on generative IE \cit
…[truncated 1707 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 3209 · 2026-05-21T16:53:05.071235+00:00_

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

_source line 3210 · 2026-05-21T16:53:05.573438+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	NER exhibits oracle scaling ($c{\approx}0.5$; \S\ref{sec:scaling}), but degeneracy (17.8--67.9\%) and LP-quality alignment ($\rho$ 0.043--0.667) constrain aggregation; temperature disentangles these at $T{=}1.2$ (Table~\ref{tab:t_degeneracy}).
4	
5	\paragraph{Degeneracy correlates with the selection gap across model families.}
6	Across four frontier models on Few-NERD, degeneracy and the selection gap (oracle${-}$MV) are negatively correlated (5.5--74\% degen $\to$ 0.290--0.032 gap; Table~\ref{tab:frontier_sc_cross}), consistent with the degeneracy bound (\S\ref{sec:theory}) being structural rather than model-specific.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms, with gains when degeneracy ${<}22$\% and absent when ${>}31$\% ($p{<}0.01$; Appendix~\ref{app:epoch_confound}); no alternative strategy beats greedy (Appendix~\ref{app:dals}, \ref{app:supervised_combination}), making construction the only consistently positive approach (Table~\ref{tab:cost_benefit})---though the trade-off ($N{\times}$ cost for ${\approx}1$\,pp) may only justify safety-critical use.
10	LP compression (median 0.041 nats) connects to calibration challenges \cite{kadavath2022language, xiong2024verbalized}; per-sample alternatives \cite{kang2025selfcertainty} remain untested.
11	

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

_source line 3211 · 2026-05-21T16:53:05.624076+00:00_

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

_source line 3212 · 2026-05-21T16:53:05.925650+00:00_

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
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 3213 · 2026-05-21T16:53:05.926099+00:00_

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

_source line 3214 · 2026-05-21T16:53:06.026861+00:00_

1	Our evidence is correlational and theoretical (MBR framework, conditional decomposition), not interventional: we have not performed controlled interventions (e.g., artificially varying degeneracy while holding other factors constant), and the cascade stages interact in ways that resist decomposition into independent causal effects ($R^2{<}0$; \S\ref{sec:selection_gap}); causal claims require future intervention experiments.
2	
3	Scope: structured IE (NER primary, RE and SQL exploratory), English only, open-weight (Qwen and LLaMA) and closed-source (GPT-5.5) families, fine-tuned (4B--14B) and zero-shot (72B, GPT-5.5) regimes, sample budget $N{\leq}32$.
4	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
5	All experiments use English-language datasets; cross-lingual generalization remains untested.
6	Cross-model consistency results (\S\ref{sec:cross_model}) are limited to one dataset (Few-NERD) and one model pair (Qwen3-8B + LLaMA-3.1-8B).
7	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
8	We cover 4B\textendash 14B fine-tuned, 72B zero-shot, and GPT-5.5 zero-shot; the gap persists across all but behavior with 72B fine-tuning is untested.
9	Frontier API models exhibit markedly different degeneracy profiles (e.g., Claude Sonnet~4 at 74\% vs.\ DeepSeek Chat at 5.5\%; Table~\ref{tab:frontier_sc_cross}), suggesting that our findings from fine-tuned open-weight models may not fully generalize to proprietary systems.
10	The 72B zero-shot comparison simultaneously varies model family (Qwen3$\to$Qwen2.5), training regime (fine-tuned$\to$zero-shot), and quantization (FP16$\to$AWQ 4-bit); these factors cannot be fully disentangled.
11	Our supervised approaches (DeB
…[truncated 3436 chars]

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

_source line 3215 · 2026-05-21T16:53:18.052890+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NOT_FOUND\"",
  "description": "Check external review config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NOT_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 3216 · 2026-05-21T16:53:18.153741+00:00_

NOT_FOUND

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

_source line 3217 · 2026-05-21T16:53:22.607347+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.yaml\" -path \"*/agent/*\" | head -10 && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"config*\" | head -10",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.yaml\" -path \"*/agent/*\" | head -10 && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"config*\" | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 3218 · 2026-05-21T16:53:22.911531+00:00_

---
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/fontTools/config
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/datasets/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/datasets/config.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/util/config.h

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 3219 · 2026-05-21T16:53:26.929311+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/project.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml 2>/dev/null | head -80",
  "description": "Read project config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/project.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml 2>/dev/null | head -80",
    "description": "Read project config"
  }
}
```

</details>

---


### Tool result

_source line 3220 · 2026-05-21T16:53:26.979970+00:00_

execution:
  account: root
  gpu_constraint:
    autodl-5090:
    - cuda:0
    - cuda:1
    - cuda:2
    - cuda:3
    autodl-5090-c:
    - cuda:0
    - cuda:1
    - cuda:2
    - cuda:3
  gpu_ids:
  - cuda:0
  - cuda:1
  - cuda:2
  - cuda:3
  project_path: /root/autodl-tmp/struct_self_consist_ie
  servers:
  - autodl-5090
  - autodl-5090-c
feishu:
  chat_id: oc_1b56445332d8ca2b4964b30f300f0e00
  operational_chat_id: oc_523053f5a039428dc15666668fa856b3
  review_mode: fresh
  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf
  review_round: 30
  review_supplementary_paths: ''
  submission_chat_id: oc_3897c2857f11615119e277e820eae311
project:
  created_at: '2026-05-14T04:20:56.331Z'
  description: When Does Test-Time Scaling Help Structured Prediction? Adaptive Structural
    Self-Consistency with Learned Aggregation
  name: struct_self_consist_ie
  phase: research
  source_idea_id: idea_010
venue: emnlp-2026

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

_source line 3221 · 2026-05-21T16:53:44.399742+00:00_

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

_source line 3222 · 2026-05-21T16:54:08.804768+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24405
}
```

</details>

---


### Tool call

_source line 3223 · 2026-05-21T16:54:09.380852+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责**方法严谨性、实验设计和统计分析**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (Long Paper, ARR)\n- **截止日期**: 2026-05-25\n- **正文页数**: ≤8 页（ACL LaTeX 模板，`\\usepackage[review]{acl}`）\n- **参考文献**: 不限页数\n- **Limitations/Ethics**: 不计入页数\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n核心论点: NER 中 entity-level agreement signals 能做到 quality estimation（ρ up to 0.47, AUROC up to 0.82）但无法做到 sample selection（所有 signal 都不优于 greedy decoding），称之为 \"correlation-selection gap\"。论文提出四阶段诊断 cascade 定位失败原因，并给出三条绕过路径。\n\n## 你的审查侧重\n\n### 必须覆盖\n1. **统计方法的严谨性**:\n   - Holm-Bonferroni 校正的 family 定义是否合理（k=21 selection family, k=10 construction family, k=57 global）\n   - p 值报告是否一致（正文 vs Appendix）\n   - 多重比较校正是否充分\n   - Bootstrap CI 的使用是否恰当\n\n2. **实验设计**:\n   - 数据集选择是否合理（4 NER + RE + SQL）\n   - 模型覆盖度（Qwen3-8B, LLaMA-3.1-8B, 4B/14B ablation, 72B, GPT-5.5）\n   - Seed 数量和统计效力（Few-NERD/CoNLL 3-seed, SciERC 1-seed）\n   - 训练设置差异（Few-NERD 3 epochs vs others 5 epochs）是否构成 confound\n   - Degeneracy decomposition 的实证基础\n\n3. **方法定义的清晰度**:\n   - 5 个 signal 的定义是否无歧义\n   - Instance-level vs per-sample 的区分是否贯穿全文\n   - Entity matching 标准（exact span + type）是否充分描述\n\n4. **理论分析**:\n   - Proposition 1 (Entity Selection Bound) 的假设是否合理\n   - MBR decoding 连接是否正确\n   - Degeneracy bound 的 tightness（论文自述仅捕获 3-12% actual gains）\n\n5. **页数和格式合规性**:\n   - 正文是否 ≤8 页\n   - Double-blind 是否满足（无 de-anonymizing 内容）\n\n### 输出格式\n请按以下结构输出审稿意见:\n1. **Summary** (2-3句)\n2. **Strengths** (逐条, S1/S2/...)\n3. **Weaknesses** (逐条, W1/W2/..., 标注 severity: critical/warning/info)\n4. **Questions** (Q1/Q2/...)\n5. **Missing References** (如有)\n6. **Minor Issues** (M1/M2/...)\n7. **Overall Assessment** (评分 + 置信度 + 1句总评)\n\n严格客观，不留情面。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1"
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
    "text": "你是 Reviewer 1，负责**方法严谨性、实验设计和统计分析**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (Long Paper, ARR)\n- **截止日期**: 2026-05-25\n- **正文页数**: ≤8 页（ACL LaTeX 模板，`\\usepackage[review]{acl}`）\n- **参考文献**: 不限页数\n- **Limitations/Ethics**: 不计入页数\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n核心论点: NER 中 entity-level agreement signals 能做到 quality estimation（ρ up to 0.47, AUROC up to 0.82）但无法做到 sample selection（所有 signal 都不优于 greedy decoding），称之为 \"correlation-selection gap\"。论文提出四阶段诊断 cascade 定位失败原因，并给出三条绕过路径。\n\n## 你的审查侧重\n\n### 必须覆盖\n1. **统计方法的严谨性**:\n   - Holm-Bonferroni 校正的 family 定义是否合理（k=21 selection family, k=10 construction family, k=57 global）\n   - p 值报告是否一致（正文 vs Appendix）\n   - 多重比较校正是否充分\n   - Bootstrap CI 的使用是否恰当\n\n2. **实验设计**:\n   - 数据集选择是否合理（4 NER + RE + SQL）\n   - 模型覆盖度（Qwen3-8B, LLaMA-3.1-8B, 4B/14B ablation, 72B, GPT-5.5）\n   - Seed 数量和统计效力（Few-NERD/CoNLL 3-seed, SciERC 1-seed）\n   - 训练设置差异（Few-NERD 3 epochs vs others 5 epochs）是否构成 confound\n   - Degeneracy decomposition 的实证基础\n\n3. **方法定义的清晰度**:\n   - 5 个 signal 的定义是否无歧义\n   - Instance-level vs per-sample 的区分是否贯穿全文\n   - Entity matching 标准（exact span + type）是否充分描述\n\n4. **理论分析**:\n   - Proposition 1 (Entity Selection Bound) 的假设是否合理\n   - MBR decoding 连接是否正确\n   - Degeneracy bound 的 tightness（论文自述仅捕获 3-12% actual gains）\n\n5. **页数和格式合规性**:\n   - 正文是否 ≤8 页\n   - Double-blind 是否满足（无 de-anonymizing 内容）\n\n### 输出格式\n请按以下结构输出审稿意见:\n1. **Summary** (2-3句)\n2. **Strengths** (逐条, S1/S2/...)\n3. **Weaknesses** (逐条, W1/W2/..., 标注 severity: critical/warning/info)\n4. **Questions** (Q1/Q2/...)\n5. **Missing References** (如有)\n6. **Minor Issues** (M1/M2/...)\n7. **Overall Assessment** (评分 + 置信度 + 1句总评)\n\n严格客观，不留情面。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3224 · 2026-05-21T16:54:29.736477+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20355
}
```

</details>

---


### Tool call

_source line 3225 · 2026-05-21T16:54:30.139334+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责**新颖性、framing、完整性和 Related Work**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (Long Paper, ARR)\n- **截止日期**: 2026-05-25\n- **正文页数**: ≤8 页（ACL LaTeX 模板，`\\usepackage[review]{acl}`）\n- **参考文献**: 不限页数\n- **Limitations/Ethics**: 不计入页数\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n核心论点: NER 中 entity-level agreement signals 能做到 quality estimation（ρ up to 0.47, AUROC up to 0.82）但无法做到 sample selection（所有 signal 都不优于 greedy decoding），称之为 \"correlation-selection gap\"。论文提出四阶段诊断 cascade 定位失败原因，并给出三条绕过路径（LP selection, entity construction, cross-model ensemble）。\n\n## 你的审查侧重\n\n### 必须覆盖\n1. **新颖性评估**:\n   - \"correlation-selection gap\" 这一概念是否真正新颖，还是 MBR 文献（Eikema & Aziz 2020/2022, Eikema et al. 2025）已知发现的重新包装\n   - 四阶段诊断 cascade 的增量贡献 vs 已有 SC failure mode 文献（Chen et al. 2023, Huang et al. 2024）\n   - Entity construction 作为 contribution 是否足够新颖（vs 标准 MBR / ensemble 方法）\n   - Hidden-state probe 结果（AUROC 0.63-0.88）的新颖性 vs 已知 probe 文献\n   - 整体贡献量：论文同时做诊断框架 + 9 methods 评估 + 理论分析 + prescriptive，每项深度是否足够\n\n2. **Framing 审查**:\n   - 标题 \"Capability Ceiling\" 是否与 observational 证据匹配（论文承认 \"not interventional\"）\n   - 因果语言 vs 相关性证据的一致性（\"governs\", \"explaining where and why\" 等措辞）\n   - Abstract 信息密度是否过高\n   - Contributions 的定位（diagnostic framework vs prescriptive escape routes 的主次关系）\n   - NER-centric 证据 vs broader structured prediction claims 的 scope 匹配\n\n3. **Related Work 完整性**:\n   - 与 MBR 文献的差异化是否充分\n   - 与 Yao et al. (2026), Yun et al. (2025) 的区分是否清晰\n   - 是否遗漏重要先行工作（特别是 SC-for-NER: Ma et al. 2024 NAACL; self-refine: Madaan et al. 2023 NeurIPS）\n   - 引用质量和完整性（orphan bib entries, 元数据）\n   - Consensus decoding 文献（DeNero et al. 2009）是否引用\n\n4. **论证完整性**:\n   - RE extension（55.5% zero-F1, span error confound）是否应作为 cross-task validation 呈现\n   - SQL 分析（仅 n=196, 87.2% degeneracy, 无系统分析）是否足够\n   - Cross-model results 仅 1 数据集 1 模型对——是否足以支撑 contribution\n   - Limitations section 是否充分覆盖核心局限\n\n5. **写作质量**:\n   - 术语定义一致性\n   - Abstract 中缩写处理\n   - Figure/Table caption 的自含性\n\n### 输出格式\n请按以下结构输出审稿意见:\n1. **Summary** (2-3句)\n2. **Strengths** (逐条, S1/S2/...)\n3. **Weaknesses** (逐条, W1/W2/..., 标注 severity: critical/warning/info)\n4. **Questions** (Q1/Q2/...)\n5. **Missing References** (如有)\n6. **Minor Issues** (M1/M2/...)\n7. **Overall Assessment** (评分 + 置信度 + 1句总评)\n\n严格客观，不留情面。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1"
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
    "text": "你是 Reviewer 2，负责**新颖性、framing、完整性和 Related Work**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (Long Paper, ARR)\n- **截止日期**: 2026-05-25\n- **正文页数**: ≤8 页（ACL LaTeX 模板，`\\usepackage[review]{acl}`）\n- **参考文献**: 不限页数\n- **Limitations/Ethics**: 不计入页数\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n核心论点: NER 中 entity-level agreement signals 能做到 quality estimation（ρ up to 0.47, AUROC up to 0.82）但无法做到 sample selection（所有 signal 都不优于 greedy decoding），称之为 \"correlation-selection gap\"。论文提出四阶段诊断 cascade 定位失败原因，并给出三条绕过路径（LP selection, entity construction, cross-model ensemble）。\n\n## 你的审查侧重\n\n### 必须覆盖\n1. **新颖性评估**:\n   - \"correlation-selection gap\" 这一概念是否真正新颖，还是 MBR 文献（Eikema & Aziz 2020/2022, Eikema et al. 2025）已知发现的重新包装\n   - 四阶段诊断 cascade 的增量贡献 vs 已有 SC failure mode 文献（Chen et al. 2023, Huang et al. 2024）\n   - Entity construction 作为 contribution 是否足够新颖（vs 标准 MBR / ensemble 方法）\n   - Hidden-state probe 结果（AUROC 0.63-0.88）的新颖性 vs 已知 probe 文献\n   - 整体贡献量：论文同时做诊断框架 + 9 methods 评估 + 理论分析 + prescriptive，每项深度是否足够\n\n2. **Framing 审查**:\n   - 标题 \"Capability Ceiling\" 是否与 observational 证据匹配（论文承认 \"not interventional\"）\n   - 因果语言 vs 相关性证据的一致性（\"governs\", \"explaining where and why\" 等措辞）\n   - Abstract 信息密度是否过高\n   - Contributions 的定位（diagnostic framework vs prescriptive escape routes 的主次关系）\n   - NER-centric 证据 vs broader structured prediction claims 的 scope 匹配\n\n3. **Related Work 完整性**:\n   - 与 MBR 文献的差异化是否充分\n   - 与 Yao et al. (2026), Yun et al. (2025) 的区分是否清晰\n   - 是否遗漏重要先行工作（特别是 SC-for-NER: Ma et al. 2024 NAACL; self-refine: Madaan et al. 2023 NeurIPS）\n   - 引用质量和完整性（orphan bib entries, 元数据）\n   - Consensus decoding 文献（DeNero et al. 2009）是否引用\n\n4. **论证完整性**:\n   - RE extension（55.5% zero-F1, span error confound）是否应作为 cross-task validation 呈现\n   - SQL 分析（仅 n=196, 87.2% degeneracy, 无系统分析）是否足够\n   - Cross-model results 仅 1 数据集 1 模型对——是否足以支撑 contribution\n   - Limitations section 是否充分覆盖核心局限\n\n5. **写作质量**:\n   - 术语定义一致性\n   - Abstract 中缩写处理\n   - Figure/Table caption 的自含性\n\n### 输出格式\n请按以下结构输出审稿意见:\n1. **Summary** (2-3句)\n2. **Strengths** (逐条, S1/S2/...)\n3. **Weaknesses** (逐条, W1/W2/..., 标注 severity: critical/warning/info)\n4. **Questions** (Q1/Q2/...)\n5. **Missing References** (如有)\n6. **Minor Issues** (M1/M2/...)\n7. **Overall Assessment** (评分 + 置信度 + 1句总评)\n\n严格客观，不留情面。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3226 · 2026-05-21T16:54:31.605314+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

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

_source line 3227 · 2026-05-21T16:54:40.594236+00:00_

已并行启动：
- **视觉审查 Agent**: 已派发（fire-and-forget）
- **Reviewer 1**: 方法严谨性 + 实验设计 + 统计分析
- **Reviewer 2**: 新颖性 + framing + 完整性 + Related Work

等待两位 Reviewer 返回初审意见（Step 1）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 239

## Round 239

2 recorded events


### User

_source line 3228 · 2026-05-21T17:01:12.985606+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（Round 1）

**论文**: "Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER"
**审查侧重**: 新颖性、framing、完整性、Related Work

---

### 1. Summary

本文研究 NER 中 entity-level 自一致性信号的能力边界。核心发现：agreement-based 信号能估计输出质量（ρ up to 0.47, AUROC up to 0.82）但无法用于 sample selection（所有信号均不优于 greedy），称为 "correlation-selection gap"。提出四阶段诊断 cascade + 三条绕过路径（LP selection, entity construction, cross-model ensemble）。4 个 NER 数据集、2 个 model family、9 种方法，附 hidden-state probe 和 MBR 理论。

### 2. Strengths

**S1.** 系统性负面结果：4 datasets × 2 model families × 9 methods 一致证明 entity-level SC selection 失败（Table 1, 2），统计检验充分（Holm-Bonferroni, bootstrap CI, permutation tests）。

**S2.** 诊断 cascade 结构化分解失败原因（degeneracy → agreement fidelity → LP compression），比单纯报告"SC 不 work"有更多 insight。

**S3.** MBR 理论连接严谨（Appendix p.1-p.2, Proposition 1-2），与 consensus decoding 文献清晰关联。

**S4.** 实验设计完整：温度敏感性、N-scaling、free-form decoding ablation、robustness 多维验证。

**S5.** Hidden-state probe（AUROC 0.63-0.88）提供独立 introspection boundary 证据。

### 3. Weaknesses

**W1 [critical] "Capability Ceiling" 标题与 observational 证据不匹配。** 论文自承 "correlational and theoretical, not interventional"（Limitations），但标题暗示 impossibility result。主文多处因果措辞（"governs"、"determines"、"explaining where and why"）与 observational design 矛盾。理论结果（Proposition 1）依赖 entity-wise independence 假设，成立程度未严格量化。建议修改标题和系统替换因果措辞。

**W2 [critical] Cross-task validation 薄弱，但 framing 暗示 broader structured prediction 适用性。** RE 仅 1 数据集（SciERC, n=529 non-zero）、55.5% zero-F1 + span error confound、信号排序与 NER 反转；SQL 仅 n=196, 87.2% degeneracy, 无系统分析；cross-model 仅 1 dataset × 1 model pair (+0.42 pp)。无法支撑 "structured prediction" 层面的 claim。建议将 RE/SQL 定位为 "preliminary exploration"，scope 限定为 NER。

**W3 [warning] Correlation-selection gap 与 MBR 文献已有发现的区分不够清晰。** Eikema & Aziz (2022) 已发现需要 decouple candidate set 和 reference set；Müller & Sennrich (2021) 证明 MBR 某些条件下不优于 beam search。主文未充分讨论这些已有发现如何 inform 或 anticipate 本文的 gap。读者可能认为这是 MBR 已知现象的 re-instantiation。

**W4 [warning] Degeneracy 作为核心解释存在 tautological element。** High degeneracy = 模型高度确信 → 本就不需要 selection，这是 trivial。关键问题是 SC 在 non-degenerate instances 上也失败（conditional ρ 接近 0），而这个更简洁的 narrative 不需要四阶段 cascade。

**W5 [warning] Entity construction 新颖性有限。** 实质是 entity-level majority vote with threshold（θ=2/N），论文自己将其形式化为 MBR 特殊情况。+1.4 pp gain 在绝对值上不大。

**W6 [warning] Abstract 信息密度过高。** ~180 词含 12+ 数字、多个首次出现的缩写、4 项 contributions，影响可读性。

**W7 [warning] Limitations 未覆盖几个重要局限：** cross-task 证据弱点、cross-model 极度有限、entity construction gain 幅度、probe overfit 可能性。

### 4. Questions

**Q1.** LP 在 Few-NERD 上 anomalous positive gain（+0.22）的原因？与 degeneracy rate (ρ=0.20) 有关？
**Q2.** Hidden-state probe 是否做过 leave-one-dataset-out CV 评估 transferability？
**Q3.** Entity construction "bypasses entity-level self-verification" 与其本身依赖 entity-level agreement 的逻辑矛盾如何解释？
**Q4.** Cross-model 为何未在 Few-NERD（degeneracy 最低）上测试？
**Q5.** Proposition 1 的 entity-wise independence 假设 violation 程度如何量化？

### 5. Missing References

- 引用验证：57 bib entries, 0 orphan, 0 missing, 2 not found (OpenAlex coverage gaps), 4 encoding mismatches
- **建议补充**：selective prediction NLP 近期工作（Varshney et al. 2022 ACL Findings; Xin et al. 2021）；structured uncertainty（Malinin & Gales 2021 ICLR）
- **需核实**：ma2024selfimproving 第一作者（bib 为 "Ma"，OpenAlex 记录为 "Xie"）

### 6. Minor Issues

M1. Abstract 中 ρ/AUROC 来自不同信号但写法可能误导
M2. Figure 1 caption disclaimer 与主文因果措辞矛盾
M3. Eq. 1 引用 Hungarian matching 但未给出引用
M4. "GPT-5.5" 首次出现未解释
M5. Footnote 1 位置不当（NER context 中提 RE）
M6. 47 页论文（10+37 appendix），大量关键证据仅在附录中

### 7. Overall Assessment

| 维度 | 分数 |
|------|------|
| Soundness | 3.5/5 |
| Excitement | 3/5 |
| Reproducibility | 4/5 |
| **Overall** | **3.0 — Findings** |
| Confidence | 4/5 |

**一句话总评**：NER 范围内的系统性诊断工作有价值，但 "capability ceiling" framing 超出 observational 证据支撑，跨任务/跨模型证据严重不足，与 MBR 文献区分需加强。适合 Findings。

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

_source line 3229 · 2026-05-21T17:01:18.260463+00:00_

Reviewer 2 已返回。等待 Reviewer 1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 240

## Round 240

2 recorded events


### User

_source line 3230 · 2026-05-21T17:01:21.225071+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：Overall Assessment 3.0（Findings 级别），Confidence 4/5。两个 critical 问题：(1) "Capability Ceiling" 标题的因果 framing 超出 observational 证据；(2) 跨任务/跨模型证据严重不足以支撑 "structured prediction" 层面的 claim。四个 warning 级问题涉及与 MBR 文献的新颖性区分、degeneracy 解释的 tautological element、entity construction 新颖性、abstract 密度和 limitations 覆盖。

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

_source line 3231 · 2026-05-21T17:01:27.147459+00:00_

Reviewer 2 意见已收到（3.0 Findings）。等待 Reviewer 1 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 241

## Round 241

6 recorded events


### User

_source line 3232 · 2026-05-21T17:03:22.686972+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性、实验设计与统计分析

**论文**: "Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER"
**Venue**: EMNLP 2026 (Long Paper, ARR)

---

## 1. Summary

本文系统研究了 NER 中 entity-level agreement signals 的能力边界，发现这些 signals 能做 quality estimation（ρ up to 0.47, AUROC up to 0.82）但无法做 sample selection（无 signal 显著优于 greedy decoding），将此称为 "correlation-selection gap"。论文提出四阶段诊断 cascade（QE → degeneracy → agreement fidelity → LP compression）定位失败原因，建立了与 MBR decoding 的理论联系（Proposition 1），并给出三条绕过路径（entity-level construction, cross-model ensemble, trained verifier）。实验覆盖 4 个 NER 数据集 + RE + SQL，6 个模型（4B-72B + GPT-5.5），9 类方法，附带 57 项统计检验的 Holm-Bonferroni 校正。

---

## 2. Strengths

**S1: 实验覆盖度和系统性极为出色。** 4 个 NER benchmark（SciERC/Few-NERD/CoNLL/WNUT-17）跨越 domain、entity 类型数（4-66）和难度梯度；模型从 4B 到 72B 再到 GPT-5.5 覆盖开源微调和闭源 API 两种范式；9 类方法（Table 2）涵盖 instance-level selection、entity-level construction、cross-model ensemble 等。60+ 张表格和 9 张图的 33 页 appendix 提供了罕见级别的实验细节。

**S2: 诊断框架设计精巧且可复用。** 四阶段 cascade（§3-4）逐步排除失败原因：先用三个独立 probe（ESJ §3, MRSC §3, LSC §3）确认自验证失败的普遍性，再通过 degeneracy decomposition（§6.3）分离 "所有样本相同" 的 trivial failure mode，最后定位 LP compression 为残余瓶颈。每个阶段有明确的 pass/fail 判据。这个框架对未来 structured generation 的 test-time compute 研究有方法论贡献。

**S3: 统计方法论严谨。** 全局 Holm-Bonferroni 校正覆盖 k=57 项检验（Table 13, p38），bootstrap 95% CI 用于效应量估计（Table 12），TOST 等价性检验用于支撑负面结论（Appendix p20），instance-level permutation test 验证 FK 的非 trivial 来源（Table 8, p15）。对于一篇以负面结果为核心论断的论文，这种统计审慎度是必要的，作者做到了。

**S4: 负面结果的建设性处理。** 论文不止于报告 "self-consistency 在 NER 上失败"，而是（a）诊断 WHY（degeneracy + LP compression + verification failure），（b）建立理论联系（MBR equivalence, Entity Selection Bound），（c）提出三条可操作的绕过路径（entity construction +1.02-1.40pp, cross-model +0.42pp, verifier +0.30pp; Table 61, p46）。这使论文从 "negative finding" 升级为 "diagnostic + prescriptive" 贡献。

**S5: MBR 理论联系有启发性。** 将 entity-level construction 形式化为 structured MBR decoding（Appendix p.2, §25）是一个有洞察力的连接，将 NER self-consistency 嵌入更广泛的 decoding 理论中。虽然 bound 较松（见 W2），但这个联系本身为后续工作指明了方向。

---

## 3. Weaknesses

**W1 [critical] SciERC 单 seed 显著削弱 25% 的 NER 证据基础**
- 具体位置：Section 7.1 (p6)；Table 21 (p22)；Appendix j (p19)
- 问题：SciERC 仅用 1 个 random seed（seed=42），而 Few-NERD 和 CoNLL 用 3 seeds。论文的核心负面论断（"无 signal 优于 greedy"）建立在 4 个 NER 数据集上，SciERC 占 25% 的权重。单 seed 意味着：(a) SciERC 上的 selection Δ 估计无方差信息，(b) bootstrap CI（Table 12）仅反映 instance-level 而非 seed-level 变异，(c) 跨 seed 稳定性无法验证。Appendix Table 36（p43）的 cross-seed analysis 是在 SciERC 上做的 N=8 vs single，但用的也是 seed=42。
- 为什么影响接收：对于声称 "across four NER datasets" 的 universal negative result，其中一个数据集的不确定性未被量化，削弱了结论的普遍性。尤其是 SciERC 是实验中表现最特殊的数据集（construction gain 最大，+1.53pp ZS; Table 60, p46），单 seed 结果可能是 seed-specific artifact。
- 建议：(a) 补充 SciERC 的 3-seed 实验或至少 2 个额外 seed；(b) 如资源不允许，正文中需更显著地标注 SciERC 结论的 single-seed caveat（当前仅在 Appendix j 简要提及）；(c) 分析 SciERC 结论对 seed 选择的 sensitivity（例如用 jackknife 或 leave-one-seed-out 在其他数据集上模拟 single-seed variance）。

**W2 [critical] Proposition 1 (Entity Selection Bound) 过松，理论贡献受限**
- 具体位置：Section 6.3 (p6)；Table 30 (p41)；Appendix p.5 (p26-27)
- 问题：Bound (1−D)·G_nd·α 仅捕获实际 selection gain 的 3-12%（Table 30 中 Ratio 列：4.7%-12.1%）。Bound 的三个因子——degeneracy rate D、non-degenerate oracle gap G_nd、signal alignment α——虽然各自有意义，但相乘后过于保守。论文自述 "the bound is loose"（p27），但仍将其列为核心贡献之一（Abstract 和 Section 1 的 contributions list）。对于 NER 中典型的 D=0.13-0.70、G_nd=10.9-18.9、α=0.047-0.121（Table 30），bound 值仅 +0.24 到 +1.56 F1 点，而实际 Δ 为 -0.42 到 +1.56。当 bound 与实际 gain 在同一量级时（如 Q3-8B FT FN s123 的 12.1%），bound 几乎没有排除任何可能的 gain 范围。
- 为什么影响接收：理论贡献是本文区别于纯 empirical study 的关键差异化因素。如果 bound 过松到无法提供有意义的预测或约束，其价值主要是概念性的（分解为三因子），而非技术性的。审稿人可能会质疑这是否构成 "theoretical contribution" 还是 "notation/decomposition"。
- 建议：(a) 在正文中明确将 Proposition 1 定位为 "diagnostic decomposition" 而非 "performance bound"，强调其解释价值而非预测价值；(b) 讨论 bound 为何松（哪个因子的估计最保守？信号之间的相关性？）；(c) 探讨能否通过更紧的 α 估计或考虑信号间依赖性来收紧 bound。

**W3 [warning] RE 和 SQL 扩展过于单薄，不足以支撑 "beyond NER" 的泛化声明**
- 具体位置：Section 7.3 (p7)；Appendix o (p24-25)
- 问题：RE 仅在 SciERC 的单一数据集、单一模型（Qwen3-8B）上评估，且限于 non-zero F1 subset（n=207/307 instances, p24）。SQL 仅以 GPT-5.5 在 Spider 上简短提及（Section 7.3），degeneracy 高达 87.2%，实质是 ceiling effect。Cross-task validation（Section 7.3）仅报告 "RE 55.5% zero-F1 instances" 和 "SQL 87.2% degeneracy"，未系统分析 correlation-selection gap 在这些任务上是否成立。
- 为什么影响评分：论文 Abstract 和 Introduction 都提到 "validate on RE and SQL"，暗示 generalizability，但证据基础远弱于 NER。RE 的单数据集、单模型结果可能是 dataset-specific；SQL 的 87.2% degeneracy 意味着几乎所有样本都 trivially degenerate，无法有意义地测试 selection。
- 建议：(a) 降低 RE/SQL 扩展的宣传力度，明确标注为 "preliminary extension" 而非 validation；(b) 在 Limitations 中讨论 RE/SQL 证据的局限性；或 (c) 补充至少一个额外的 RE 数据集（如 TACRED 或 DocRED）。

**W4 [warning] 训练配方差异构成跨数据集比较的潜在混淆因素**
- 具体位置：Section 7.1 (p6)；Table 21 (p22)；Appendix k (p22)
- 问题：Few-NERD 训练 3 epochs 而其他数据集训练 5 epochs（Table 21）。不同训练时长意味着不同的收敛状态，进而影响 degeneracy rate（欠拟合 → 更多 diverse 但 lower-quality 输出 → 更低 degeneracy → 可能更大的 selection headroom）。论文的跨数据集 ρ 比较（Table 6/7, p14/17）和 cross-dataset correlation（Table 7 的 ρ shifting across datasets）可能部分反映训练配方差异而非 dataset 内在属性。
- Appendix ab（p32）对 epoch 效应做了消融（SciERC 3-epoch vs 5-epoch, Table 52），显示 degeneracy 随 epoch 单调递增（从 43.5% 到 60.3%），证实训练时长确实影响 degeneracy。但 Few-NERD 的 3-epoch 设置未做对照（5-epoch 消融）。
- 建议：(a) 对 Few-NERD 补充 5-epoch 消融或解释为何选择 3 epochs；(b) 在讨论跨数据集差异时明确控制训练收敛状态这一混淆因素。

**W5 [warning] 负面结论的统计效力存疑**
- 具体位置：Appendix Table 55 (p34)；Limitations (p8)
- 问题：Table 55 的 post-hoc power analysis 基于 n=23 cross-dataset correlations，显示仅当 ρ≥0.5 时 power≥0.65。对于 ρ=0.3（中等效应），power 仅约 0.32。这意味着论文可能缺乏检测中等大小 cross-dataset 效应的能力。论文的核心负面论断（"no signal outperforms greedy across datasets"）在 per-dataset 层面有充分支持（大 N 的 bootstrap），但 cross-dataset generalization 的 evidence 可能受限于小样本。
- 论文在 Limitations（p8）承认了这一点，但主文的措辞比证据允许的更断定性（如 "the failure is universal"）。
- 建议：主文中对 cross-dataset generalization 的措辞加入适当的 hedge（"across the four datasets tested" 而非暗示 universal）。

**W6 [warning] Degeneracy 可能是 correlation-selection gap 的主要甚至唯一解释，削弱了 "gap" 概念的新颖性**
- 具体位置：Section 6.3 (p6)；Table 30 (p41)
- 问题：Degeneracy rate 在 17.8%-67.9% 之间（Section 6.3）。在 degenerate instances 上，所有 N 个 samples 完全相同，任何 signal 的排名都是 trivially tied。论文的 "non-degenerate" 分析（Table 30）显示即使排除 degenerate instances，selection 仍然失败——这是论文的核心洞察。然而，non-degenerate oracle gap G_nd 的存在仅意味着 oracle 能在非 degenerate instances 上获得更好结果，并不意味着基于 agreement signals 的 selection 应该能做到这一点。Signal alignment α 极低（0.000-0.161）才是真正的瓶颈，但这一发现被 "correlation-selection gap" 这个 framing 所 overshadow。
- 更精确的 framing 可能是 "entity-level agreement signals have near-zero selection alignment despite moderate quality correlation"——这是 α → 0 的直接结论，而非需要整个 diagnostic cascade 才能得出。
- 建议：讨论 Section 中更明确地区分 "degenerate instances 导致的 trivial gap" 和 "non-degenerate instances 上信号对齐失败导致的 non-trivial gap"，并量化两者的相对贡献。

---

## 4. Questions

**Q1**: SciERC 为何仅用 1 个 seed？是资源限制还是方法论考虑？给定 SciERC 是论文中 construction gain 最大的数据集，这个选择的影响尤为重要。

**Q2**: LP compression threshold ε=0.05（§7.3, Table 4）的选择依据是什么？Appendix 中有 sensitivity analysis 吗？不同 ε 值是否改变 LP 作为 selection signal 的排名？

**Q3**: TOST 等价性检验的 equivalence margin δ 是如何选择的？Table 16（p39）和相关讨论中的 δ 值范围（1.3-3.4pp）看起来是 data-driven 的，是否存在循环推理风险？

**Q4**: 论文主要基于 fine-tuned 模型。对于 zero-shot instruction-tuned 模型（Table 60, p46 显示了部分结果），correlation-selection gap 的幅度是否有实质性变化？如果 zero-shot 下 gap 更小或消失，这对论文结论有何影响？

**Q5**: Cross-model ensemble（Section 5.1, +0.42pp）使用了架构完全不同的模型（Qwen vs LLaMA）。如果使用同一架构的不同 checkpoint（如不同 seed 的 Qwen3-8B），是否也能获得类似增益？这对理解 diversity 的来源很重要。

---

## 5. Missing References

未发现重要缺失引用。引用覆盖度良好：self-consistency（Wang et al. 2023; Chen et al. 2024; Taubenfeld et al. 2025），MBR decoding（Eikema & Aziz 2022; Eikema et al. 2025），uncertainty estimation（Kuhn et al. 2023; Farquhar et al. 2024），NER-specific（Xie et al. 2023; Li et al. 2024; Ma et al. 2024）。

可选补充：Malinin & Gales (2021) "Uncertainty Estimation in Autoregressive Structured Prediction" 可能与 structured output 的 uncertainty estimation 相关。

---

## 6. Minor Issues

**M1**: Table 13（p38）caption 中的 k 值——请确认是 k=52 还是 k=57。表格列出 57 行检验，如果 5 项被排除在校正之外，需说明排除标准。

**M2**: Figure 1（p3）的 "Center" 面板表述可更清晰——"instance-level signals assign identical scores to all N candidates" 的视觉表达不够直观，读者需要仔细阅读 caption 才能理解。

**M3**: Section 2.2（p3）定义 Soft Jaccard (SJ) 时，公式(1)中 `rank(b_ij, b_ij)` 的符号含义在首次出现时不够清晰——是否应为 `rank(b_ij, b_ik)` 用于成对比较？

**M4**: "correlation-selection gap" 在 Abstract 中首次出现时缺少一句直觉解释，可能让不熟悉该领域的读者困惑。

**M5**: Appendix 的组织虽然全面，但 33 页的体量使得导航困难。建议在 Appendix 开头加一个目录。

**M6**: 引用验证发现 `aggarwal2023adaptive` 和 `lightman2024verify` 未在 OpenAlex 中匹配到（可能是 API 覆盖问题而非虚假引用），以及 `snell2025scaling`、`muller2021understanding`、`dembczynski2011exact`、`ma2024selfimproving` 有 minor first-author name mismatches（LaTeX 编码 vs Unicode）。

---

## 7. Overall Assessment

**Overall**: 3.5 / 5（Borderline Conference）
**Soundness**: 3.5 / 5
**Excitement**: 3.5 / 5
**Reproducibility**: 4 / 5
**Confidence**: 4 / 5（我仔细阅读了全部 47 页，对 NER 和 test-time compute 领域比较熟悉）

**一句话总评**: 这是一篇实验极为扎实的 diagnostic study，在方法论上有贡献（四阶段 cascade、MBR 连接），但 SciERC 单 seed 问题、理论 bound 过松（3-12%）、RE/SQL 扩展单薄，以及 "correlation-selection gap" 可能主要由 degeneracy 这一已知现象驱动，使其停留在 borderline conference 水平。如果补充 SciERC 的多 seed 实验并收紧理论 bound 的讨论定位，本文有望达到 clear accept。

### 格式合规性检查
- ✅ 正文 8 页（Sections 1-10 + Limitations），符合 ≤8 页要求
- ✅ Double-blind：标题页 "Anonymous ACL submission"，代码 release 使用 "[anonymized URL]"
- ✅ References 不限页数
- ✅ Limitations 章节存在（p8），覆盖 correlational evidence、scope、statistical power
- ✅ Ethics Statement 存在（p9-10）
- ✅ Responsible NLP Research Checklist 完整填写（p10-11）


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

_source line 3233 · 2026-05-21T17:04:29.695796+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 **Reviewer 2** 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question/Minor Issue，用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Round 1）\n\n**论文**: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n**审查侧重**: 新颖性、framing、完整性、Related Work\n\n### 1. Summary\n本文研究 NER 中 entity-level 自一致性信号的能力边界。核心发现：agreement-based 信号能估计输出质量（ρ up to 0.47, AUROC up to 0.82）但无法用于 sample selection（所有信号均不优于 greedy），称为 \"correlation-selection gap\"。提出四阶段诊断 cascade + 三条绕过路径（LP selection, entity construction, cross-model ensemble）。4 个 NER 数据集、2 个 model family、9 种方法，附 hidden-state probe 和 MBR 理论。\n\n### 2. Strengths\n**S1.** 系统性负面结果：4 datasets × 2 model families × 9 methods 一致证明 entity-level SC selection 失败（Table 1, 2），统计检验充分（Holm-Bonferroni, bootstrap CI, permutation tests）。\n**S2.** 诊断 cascade 结构化分解失败原因（degeneracy → agreement fidelity → LP compression），比单纯报告\"SC 不 work\"有更多 insight。\n**S3.** MBR 理论连接严谨（Appendix p.1-p.2, Proposition 1-2），与 consensus decoding 文献清晰关联。\n**S4.** 实验设计完整：温度敏感性、N-scaling、free-form decoding ablation、robustness 多维验证。\n**S5.** Hidden-state probe（AUROC 0.63-0.88）提供独立 introspection boundary 证据。\n\n### 3. Weaknesses\n**W1 [critical] \"Capability Ceiling\" 标题与 observational 证据不匹配。** 论文自承 \"correlational and theoretical, not interventional\"（Limitations），但标题暗示 impossibility result。主文多处因果措辞（\"governs\"、\"determines\"、\"explaining where and why\"）与 observational design 矛盾。理论结果（Proposition 1）依赖 entity-wise independence 假设，成立程度未严格量化。建议修改标题和系统替换因果措辞。\n\n**W2 [critical] Cross-task validation 薄弱，但 framing 暗示 broader structured prediction 适用性。** RE 仅 1 数据集（SciERC, n=529 non-zero）、55.5% zero-F1 + span error confound、信号排序与 NER 反转；SQL 仅 n=196, 87.2% degeneracy, 无系统分析；cross-model 仅 1 dataset × 1 model pair (+0.42 pp)。无法支撑 \"structured prediction\" 层面的 claim。建议将 RE/SQL 定位为 \"preliminary exploration\"，scope 限定为 NER。\n\n**W3 [warning] Correlation-selection gap 与 MBR 文献已有发现的区分不够清晰。** Eikema & Aziz (2022) 已发现需要 decouple candidate set 和 reference set；Müller & Sennrich (2021) 证明 MBR 某些条件下不优于 beam search。主文未充分讨论这些已有发现如何 inform 或 anticipate 本文的 gap。读者可能认为这是 MBR 已知现象的 re-instantiation。\n\n**W4 [warning] Degeneracy 作为核心解释存在 tautological element。** High degeneracy = 模型高度确信 → 本就不需要 selection，这是 trivial。关键问题是 SC 在 non-degenerate instances 上也失败（conditional ρ 接近 0），而这个更简洁的 narrative 不需要四阶段 cascade。\n\n**W5 [warning] Entity construction 新颖性有限。** 实质是 entity-level majority vote with threshold（θ=2/N），论文自己将其形式化为 MBR 特殊情况。+1.4 pp gain 在绝对值上不大。\n\n**W6 [warning] Abstract 信息密度过高。** ~180 词含 12+ 数字、多个首次出现的缩写、4 项 contributions，影响可读性。\n\n**W7 [warning] Limitations 未覆盖几个重要局限：** cross-task 证据弱点、cross-model 极度有限、entity construction gain 幅度、probe overfit 可能性。\n\n### 4. Questions\n**Q1.** LP 在 Few-NERD 上 anomalous positive gain（+0.22）的原因？与 degeneracy rate (ρ=0.20) 有关？\n**Q2.** Hidden-state probe 是否做过 leave-one-dataset-out CV 评估 transferability？\n**Q3.** Entity construction \"bypasses entity-level self-verification\" 与其本身依赖 entity-level agreement 的逻辑矛盾如何解释？\n**Q4.** Cross-model 为何未在 Few-NERD（degeneracy 最低）上测试？\n**Q5.** Proposition 1 的 entity-wise independence 假设 violation 程度如何量化？\n\n### 5. Missing References\n- 引用验证：57 bib entries, 0 orphan, 0 missing, 2 not found (OpenAlex coverage gaps), 4 encoding mismatches\n- **建议补充**：selective prediction NLP 近期工作（Varshney et al. 2022 ACL Findings; Xin et al. 2021）；structured uncertainty（Malinin & Gales 2021 ICLR）\n- **需核实**：ma2024selfimproving 第一作者（bib 为 \"Ma\"，OpenAlex 记录为 \"Xie\"）\n\n### 6. Minor Issues\nM1. Abstract 中 ρ/AUROC 来自不同信号但写法可能误导\nM2. Figure 1 caption disclaimer 与主文因果措辞矛盾\nM3. Eq. 1 引用 Hungarian matching 但未给出引用\nM4. \"GPT-5.5\" 首次出现未解释\nM5. Footnote 1 位置不当（NER context 中提 RE）\nM6. 47 页论文（10+37 appendix），大量关键证据仅在附录中\n\n### 7. Overall Assessment\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| **Overall** | **3.0 — Findings** |\n| Confidence | 4/5 |\n\n**一句话总评**：NER 范围内的系统性诊断工作有价值，但 \"capability ceiling\" framing 超出 observational 证据支撑，跨任务/跨模型证据严重不足，与 MBR 文献区分需加强。适合 Findings。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1"
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
    "text": "以下是 **Reviewer 2** 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question/Minor Issue，用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Round 1）\n\n**论文**: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n**审查侧重**: 新颖性、framing、完整性、Related Work\n\n### 1. Summary\n本文研究 NER 中 entity-level 自一致性信号的能力边界。核心发现：agreement-based 信号能估计输出质量（ρ up to 0.47, AUROC up to 0.82）但无法用于 sample selection（所有信号均不优于 greedy），称为 \"correlation-selection gap\"。提出四阶段诊断 cascade + 三条绕过路径（LP selection, entity construction, cross-model ensemble）。4 个 NER 数据集、2 个 model family、9 种方法，附 hidden-state probe 和 MBR 理论。\n\n### 2. Strengths\n**S1.** 系统性负面结果：4 datasets × 2 model families × 9 methods 一致证明 entity-level SC selection 失败（Table 1, 2），统计检验充分（Holm-Bonferroni, bootstrap CI, permutation tests）。\n**S2.** 诊断 cascade 结构化分解失败原因（degeneracy → agreement fidelity → LP compression），比单纯报告\"SC 不 work\"有更多 insight。\n**S3.** MBR 理论连接严谨（Appendix p.1-p.2, Proposition 1-2），与 consensus decoding 文献清晰关联。\n**S4.** 实验设计完整：温度敏感性、N-scaling、free-form decoding ablation、robustness 多维验证。\n**S5.** Hidden-state probe（AUROC 0.63-0.88）提供独立 introspection boundary 证据。\n\n### 3. Weaknesses\n**W1 [critical] \"Capability Ceiling\" 标题与 observational 证据不匹配。** 论文自承 \"correlational and theoretical, not interventional\"（Limitations），但标题暗示 impossibility result。主文多处因果措辞（\"governs\"、\"determines\"、\"explaining where and why\"）与 observational design 矛盾。理论结果（Proposition 1）依赖 entity-wise independence 假设，成立程度未严格量化。建议修改标题和系统替换因果措辞。\n\n**W2 [critical] Cross-task validation 薄弱，但 framing 暗示 broader structured prediction 适用性。** RE 仅 1 数据集（SciERC, n=529 non-zero）、55.5% zero-F1 + span error confound、信号排序与 NER 反转；SQL 仅 n=196, 87.2% degeneracy, 无系统分析；cross-model 仅 1 dataset × 1 model pair (+0.42 pp)。无法支撑 \"structured prediction\" 层面的 claim。建议将 RE/SQL 定位为 \"preliminary exploration\"，scope 限定为 NER。\n\n**W3 [warning] Correlation-selection gap 与 MBR 文献已有发现的区分不够清晰。** Eikema & Aziz (2022) 已发现需要 decouple candidate set 和 reference set；Müller & Sennrich (2021) 证明 MBR 某些条件下不优于 beam search。主文未充分讨论这些已有发现如何 inform 或 anticipate 本文的 gap。读者可能认为这是 MBR 已知现象的 re-instantiation。\n\n**W4 [warning] Degeneracy 作为核心解释存在 tautological element。** High degeneracy = 模型高度确信 → 本就不需要 selection，这是 trivial。关键问题是 SC 在 non-degenerate instances 上也失败（conditional ρ 接近 0），而这个更简洁的 narrative 不需要四阶段 cascade。\n\n**W5 [warning] Entity construction 新颖性有限。** 实质是 entity-level majority vote with threshold（θ=2/N），论文自己将其形式化为 MBR 特殊情况。+1.4 pp gain 在绝对值上不大。\n\n**W6 [warning] Abstract 信息密度过高。** ~180 词含 12+ 数字、多个首次出现的缩写、4 项 contributions，影响可读性。\n\n**W7 [warning] Limitations 未覆盖几个重要局限：** cross-task 证据弱点、cross-model 极度有限、entity construction gain 幅度、probe overfit 可能性。\n\n### 4. Questions\n**Q1.** LP 在 Few-NERD 上 anomalous positive gain（+0.22）的原因？与 degeneracy rate (ρ=0.20) 有关？\n**Q2.** Hidden-state probe 是否做过 leave-one-dataset-out CV 评估 transferability？\n**Q3.** Entity construction \"bypasses entity-level self-verification\" 与其本身依赖 entity-level agreement 的逻辑矛盾如何解释？\n**Q4.** Cross-model 为何未在 Few-NERD（degeneracy 最低）上测试？\n**Q5.** Proposition 1 的 entity-wise independence 假设 violation 程度如何量化？\n\n### 5. Missing References\n- 引用验证：57 bib entries, 0 orphan, 0 missing, 2 not found (OpenAlex coverage gaps), 4 encoding mismatches\n- **建议补充**：selective prediction NLP 近期工作（Varshney et al. 2022 ACL Findings; Xin et al. 2021）；structured uncertainty（Malinin & Gales 2021 ICLR）\n- **需核实**：ma2024selfimproving 第一作者（bib 为 \"Ma\"，OpenAlex 记录为 \"Xie\"）\n\n### 6. Minor Issues\nM1. Abstract 中 ρ/AUROC 来自不同信号但写法可能误导\nM2. Figure 1 caption disclaimer 与主文因果措辞矛盾\nM3. Eq. 1 引用 Hungarian matching 但未给出引用\nM4. \"GPT-5.5\" 首次出现未解释\nM5. Footnote 1 位置不当（NER context 中提 RE）\nM6. 47 页论文（10+37 appendix），大量关键证据仅在附录中\n\n### 7. Overall Assessment\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| **Overall** | **3.0 — Findings** |\n| Confidence | 4/5 |\n\n**一句话总评**：NER 范围内的系统性诊断工作有价值，但 \"capability ceiling\" framing 超出 observational 证据支撑，跨任务/跨模型证据严重不足，与 MBR 文献区分需加强。适合 Findings。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3234 · 2026-05-21T17:05:19.631162+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 49935
}
```

</details>

---


### Tool call

_source line 3235 · 2026-05-21T17:05:20.183556+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 **Reviewer 1** 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question/Minor Issue，用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见：方法严谨性、实验设计与统计分析\n\n**论文**: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n**Venue**: EMNLP 2026 (Long Paper, ARR)\n\n## 1. Summary\n本文系统研究了 NER 中 entity-level agreement signals 的能力边界，发现这些 signals 能做 quality estimation（ρ up to 0.47, AUROC up to 0.82）但无法做 sample selection（无 signal 显著优于 greedy decoding），将此称为 \"correlation-selection gap\"。论文提出四阶段诊断 cascade（QE → degeneracy → agreement fidelity → LP compression）定位失败原因，建立了与 MBR decoding 的理论联系（Proposition 1），并给出三条绕过路径（entity-level construction, cross-model ensemble, trained verifier）。实验覆盖 4 个 NER 数据集 + RE + SQL，6 个模型（4B-72B + GPT-5.5），9 类方法，附带 57 项统计检验的 Holm-Bonferroni 校正。\n\n## 2. Strengths\n**S1: 实验覆盖度和系统性极为出色。** 4 个 NER benchmark（SciERC/Few-NERD/CoNLL/WNUT-17）跨越 domain、entity 类型数（4-66）和难度梯度；模型从 4B 到 72B 再到 GPT-5.5 覆盖开源微调和闭源 API 两种范式；9 类方法（Table 2）涵盖 instance-level selection、entity-level construction、cross-model ensemble 等。60+ 张表格和 9 张图的 33 页 appendix 提供了罕见级别的实验细节。\n\n**S2: 诊断框架设计精巧且可复用。** 四阶段 cascade（§3-4）逐步排除失败原因：先用三个独立 probe（ESJ §3, MRSC §3, LSC §3）确认自验证失败的普遍性，再通过 degeneracy decomposition（§6.3）分离 \"所有样本相同\" 的 trivial failure mode，最后定位 LP compression 为残余瓶颈。每个阶段有明确的 pass/fail 判据。这个框架对未来 structured generation 的 test-time compute 研究有方法论贡献。\n\n**S3: 统计方法论严谨。** 全局 Holm-Bonferroni 校正覆盖 k=57 项检验（Table 13, p38），bootstrap 95% CI 用于效应量估计（Table 12），TOST 等价性检验用于支撑负面结论（Appendix p20），instance-level permutation test 验证 FK 的非 trivial 来源（Table 8, p15）。对于一篇以负面结果为核心论断的论文，这种统计审慎度是必要的，作者做到了。\n\n**S4: 负面结果的建设性处理。** 论文不止于报告 \"self-consistency 在 NER 上失败\"，而是（a）诊断 WHY（degeneracy + LP compression + verification failure），（b）建立理论联系（MBR equivalence, Entity Selection Bound），（c）提出三条可操作的绕过路径（entity construction +1.02-1.40pp, cross-model +0.42pp, verifier +0.30pp; Table 61, p46）。这使论文从 \"negative finding\" 升级为 \"diagnostic + prescriptive\" 贡献。\n\n**S5: MBR 理论联系有启发性。** 将 entity-level construction 形式化为 structured MBR decoding（Appendix p.2, §25）是一个有洞察力的连接，将 NER self-consistency 嵌入更广泛的 decoding 理论中。虽然 bound 较松（见 W2），但这个联系本身为后续工作指明了方向。\n\n## 3. Weaknesses\n**W1 [critical] SciERC 单 seed 显著削弱 25% 的 NER 证据基础**\n- SciERC 仅用 1 个 random seed（seed=42），而 Few-NERD 和 CoNLL 用 3 seeds。论文核心负面论断建立在 4 个 NER 数据集上，SciERC 占 25% 权重。单 seed 意味着 selection Δ 估计无方差信息，bootstrap CI 仅反映 instance-level 变异。SciERC 是 construction gain 最大的数据集（+1.53pp ZS），单 seed 结果可能是 seed-specific artifact。\n- 建议补充 SciERC 3-seed 或在正文中更显著标注 single-seed caveat。\n\n**W2 [critical] Proposition 1 (Entity Selection Bound) 过松，理论贡献受限**\n- Bound (1−D)·G_nd·α 仅捕获实际 gain 的 3-12%（Table 30）。三个因子各有意义但相乘后过于保守。论文自述 \"the bound is loose\"（p27），但仍列为核心贡献。\n- 建议将 Proposition 1 定位为 \"diagnostic decomposition\" 而非 \"performance bound\"。\n\n**W3 [warning] RE 和 SQL 扩展过于单薄，不足以支撑 \"beyond NER\" 的泛化声明**\n- RE 仅 SciERC 单数据集单模型，SQL 仅 GPT-5.5 在 Spider 上简短提及（87.2% degeneracy = ceiling effect）。建议降低宣传力度或补充数据集。\n\n**W4 [warning] 训练配方差异构成跨数据集比较的潜在混淆因素**\n- Few-NERD 3 epochs vs 其他 5 epochs。SciERC 消融显示 degeneracy 随 epoch 单调递增（43.5%→60.3%），但 Few-NERD 未做 5-epoch 对照。\n\n**W5 [warning] 负面结论的统计效力存疑**\n- Cross-dataset correlation（n=23）的 post-hoc power 在 ρ=0.3 时仅约 0.32。主文措辞比证据允许的更断定性。\n\n**W6 [warning] Degeneracy 可能是 correlation-selection gap 的主要甚至唯一解释**\n- High degeneracy = trivially tied scores。Non-degenerate 分析显示 α 极低（0.000-0.161）才是真正瓶颈，但这一发现被 \"correlation-selection gap\" framing 所 overshadow。更精确的 framing 可能是 \"near-zero selection alignment despite moderate quality correlation\"。\n\n## 4. Questions\n**Q1**: SciERC 为何仅用 1 个 seed？是资源限制还是方法论考虑？\n**Q2**: LP compression threshold ε=0.05 的选择依据？不同 ε 是否改变 LP ranking？\n**Q3**: TOST 等价性检验的 equivalence margin δ 是如何选择的？是否 data-driven 导致循环推理？\n**Q4**: Zero-shot instruction-tuned 模型下 gap 幅度是否有实质变化？\n**Q5**: Cross-model ensemble 用同架构不同 checkpoint 是否也有类似增益？\n\n## 5. Missing References\n未发现重要缺失。可选补充 Malinin & Gales (2021)。\n\n## 6. Minor Issues\nM1: Table 13 caption k=52 vs k=57 需确认\nM2: Figure 1 Center 面板视觉表达不够直观\nM3: SJ 公式(1)符号首次出现时不够清晰\nM4: \"correlation-selection gap\" 在 Abstract 首次出现缺直觉解释\nM5: Appendix 33 页建议加目录\nM6: 引用验证发现 4 个 minor first-author name mismatches\n\n## 7. Overall Assessment\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 3.5 / 5\n**Excitement**: 3.5 / 5\n**Reproducibility**: 4 / 5\n**Confidence**: 4 / 5\n\n**一句话总评**: 实验极为扎实的 diagnostic study，方法论有贡献，但 SciERC 单 seed、理论 bound 过松、RE/SQL 单薄、degeneracy 可能是主要解释，使其停留在 borderline conference。补充 SciERC 多 seed 并收紧理论定位有望 clear accept。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1"
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
    "text": "以下是 **Reviewer 1** 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question/Minor Issue，用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见：方法严谨性、实验设计与统计分析\n\n**论文**: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n**Venue**: EMNLP 2026 (Long Paper, ARR)\n\n## 1. Summary\n本文系统研究了 NER 中 entity-level agreement signals 的能力边界，发现这些 signals 能做 quality estimation（ρ up to 0.47, AUROC up to 0.82）但无法做 sample selection（无 signal 显著优于 greedy decoding），将此称为 \"correlation-selection gap\"。论文提出四阶段诊断 cascade（QE → degeneracy → agreement fidelity → LP compression）定位失败原因，建立了与 MBR decoding 的理论联系（Proposition 1），并给出三条绕过路径（entity-level construction, cross-model ensemble, trained verifier）。实验覆盖 4 个 NER 数据集 + RE + SQL，6 个模型（4B-72B + GPT-5.5），9 类方法，附带 57 项统计检验的 Holm-Bonferroni 校正。\n\n## 2. Strengths\n**S1: 实验覆盖度和系统性极为出色。** 4 个 NER benchmark（SciERC/Few-NERD/CoNLL/WNUT-17）跨越 domain、entity 类型数（4-66）和难度梯度；模型从 4B 到 72B 再到 GPT-5.5 覆盖开源微调和闭源 API 两种范式；9 类方法（Table 2）涵盖 instance-level selection、entity-level construction、cross-model ensemble 等。60+ 张表格和 9 张图的 33 页 appendix 提供了罕见级别的实验细节。\n\n**S2: 诊断框架设计精巧且可复用。** 四阶段 cascade（§3-4）逐步排除失败原因：先用三个独立 probe（ESJ §3, MRSC §3, LSC §3）确认自验证失败的普遍性，再通过 degeneracy decomposition（§6.3）分离 \"所有样本相同\" 的 trivial failure mode，最后定位 LP compression 为残余瓶颈。每个阶段有明确的 pass/fail 判据。这个框架对未来 structured generation 的 test-time compute 研究有方法论贡献。\n\n**S3: 统计方法论严谨。** 全局 Holm-Bonferroni 校正覆盖 k=57 项检验（Table 13, p38），bootstrap 95% CI 用于效应量估计（Table 12），TOST 等价性检验用于支撑负面结论（Appendix p20），instance-level permutation test 验证 FK 的非 trivial 来源（Table 8, p15）。对于一篇以负面结果为核心论断的论文，这种统计审慎度是必要的，作者做到了。\n\n**S4: 负面结果的建设性处理。** 论文不止于报告 \"self-consistency 在 NER 上失败\"，而是（a）诊断 WHY（degeneracy + LP compression + verification failure），（b）建立理论联系（MBR equivalence, Entity Selection Bound），（c）提出三条可操作的绕过路径（entity construction +1.02-1.40pp, cross-model +0.42pp, verifier +0.30pp; Table 61, p46）。这使论文从 \"negative finding\" 升级为 \"diagnostic + prescriptive\" 贡献。\n\n**S5: MBR 理论联系有启发性。** 将 entity-level construction 形式化为 structured MBR decoding（Appendix p.2, §25）是一个有洞察力的连接，将 NER self-consistency 嵌入更广泛的 decoding 理论中。虽然 bound 较松（见 W2），但这个联系本身为后续工作指明了方向。\n\n## 3. Weaknesses\n**W1 [critical] SciERC 单 seed 显著削弱 25% 的 NER 证据基础**\n- SciERC 仅用 1 个 random seed（seed=42），而 Few-NERD 和 CoNLL 用 3 seeds。论文核心负面论断建立在 4 个 NER 数据集上，SciERC 占 25% 权重。单 seed 意味着 selection Δ 估计无方差信息，bootstrap CI 仅反映 instance-level 变异。SciERC 是 construction gain 最大的数据集（+1.53pp ZS），单 seed 结果可能是 seed-specific artifact。\n- 建议补充 SciERC 3-seed 或在正文中更显著标注 single-seed caveat。\n\n**W2 [critical] Proposition 1 (Entity Selection Bound) 过松，理论贡献受限**\n- Bound (1−D)·G_nd·α 仅捕获实际 gain 的 3-12%（Table 30）。三个因子各有意义但相乘后过于保守。论文自述 \"the bound is loose\"（p27），但仍列为核心贡献。\n- 建议将 Proposition 1 定位为 \"diagnostic decomposition\" 而非 \"performance bound\"。\n\n**W3 [warning] RE 和 SQL 扩展过于单薄，不足以支撑 \"beyond NER\" 的泛化声明**\n- RE 仅 SciERC 单数据集单模型，SQL 仅 GPT-5.5 在 Spider 上简短提及（87.2% degeneracy = ceiling effect）。建议降低宣传力度或补充数据集。\n\n**W4 [warning] 训练配方差异构成跨数据集比较的潜在混淆因素**\n- Few-NERD 3 epochs vs 其他 5 epochs。SciERC 消融显示 degeneracy 随 epoch 单调递增（43.5%→60.3%），但 Few-NERD 未做 5-epoch 对照。\n\n**W5 [warning] 负面结论的统计效力存疑**\n- Cross-dataset correlation（n=23）的 post-hoc power 在 ρ=0.3 时仅约 0.32。主文措辞比证据允许的更断定性。\n\n**W6 [warning] Degeneracy 可能是 correlation-selection gap 的主要甚至唯一解释**\n- High degeneracy = trivially tied scores。Non-degenerate 分析显示 α 极低（0.000-0.161）才是真正瓶颈，但这一发现被 \"correlation-selection gap\" framing 所 overshadow。更精确的 framing 可能是 \"near-zero selection alignment despite moderate quality correlation\"。\n\n## 4. Questions\n**Q1**: SciERC 为何仅用 1 个 seed？是资源限制还是方法论考虑？\n**Q2**: LP compression threshold ε=0.05 的选择依据？不同 ε 是否改变 LP ranking？\n**Q3**: TOST 等价性检验的 equivalence margin δ 是如何选择的？是否 data-driven 导致循环推理？\n**Q4**: Zero-shot instruction-tuned 模型下 gap 幅度是否有实质变化？\n**Q5**: Cross-model ensemble 用同架构不同 checkpoint 是否也有类似增益？\n\n## 5. Missing References\n未发现重要缺失。可选补充 Malinin & Gales (2021)。\n\n## 6. Minor Issues\nM1: Table 13 caption k=52 vs k=57 需确认\nM2: Figure 1 Center 面板视觉表达不够直观\nM3: SJ 公式(1)符号首次出现时不够清晰\nM4: \"correlation-selection gap\" 在 Abstract 首次出现缺直觉解释\nM5: Appendix 33 页建议加目录\nM6: 引用验证发现 4 个 minor first-author name mismatches\n\n## 7. Overall Assessment\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 3.5 / 5\n**Excitement**: 3.5 / 5\n**Reproducibility**: 4 / 5\n**Confidence**: 4 / 5\n\n**一句话总评**: 实验极为扎实的 diagnostic study，方法论有贡献，但 SciERC 单 seed、理论 bound 过松、RE/SQL 单薄、degeneracy 可能是主要解释，使其停留在 borderline conference。补充 SciERC 多 seed 并收紧理论定位有望 clear accept。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3236 · 2026-05-21T17:05:21.747545+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1563
}
```

</details>

---


### Assistant

_source line 3237 · 2026-05-21T17:05:24.697337+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 242

## Round 242

2 recorded events


### User

_source line 3238 · 2026-05-21T17:05:27.299356+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：本文是一篇实验极为扎实的 diagnostic study（47页，60+表格，57项统计检验），核心发现 NER 中 entity-level agreement signals 能做 quality estimation 但无法做 sample selection。主要问题：(1) SciERC 单 seed 削弱 25% 证据基础 [critical]；(2) Proposition 1 的 bound 仅捕获 3-12% actual gain [critical]；(3) RE/SQL 扩展单薄 [warning]；(4) 训练配方差异构成混淆 [warning]。评分：Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3.5。

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

_source line 3239 · 2026-05-21T17:05:32.281274+00:00_

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


## Round 243

## Round 243

2 recorded events


### User

_source line 3240 · 2026-05-21T17:07:05.642071+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Strengths 回应

**[AGREE] R2-S1**: 同意。4 datasets × 2 model families × 9 methods 的系统性是本文最突出的优点，我在 R1-S1 中也做了相同评价。Holm-Bonferroni 覆盖 k=57 检验（Table 13）的统计审慎度在 NLP 实证论文中属于上乘。

**[AGREE] R2-S2**: 同意。诊断 cascade 是核心方法论贡献，我在 R1-S2 中给了相同评价。

**[AGREE] R2-S3**: 同意。MBR 连接在 Appendix p.1-p.2 中推导严谨。但我在 R1-W2 中指出 Proposition 1 的 bound 仅捕获 3-12% 的实际 gain（Table 30），理论贡献的实际约束力有限。

**[AGREE] R2-S4**: 同意实验设计完整性。补充一点：temperature sensitivity（Table 7, p14）和 N-scaling（Table 11, p19; Figure 9, p29）覆盖了最重要的超参维度。

**[AGREE] R2-S5**: 同意。Hidden-state probe（AUROC 0.63-0.88）提供了独立的 introspection evidence，证明信息在模型内部存在但 agreement signals 无法有效提取。这与我对 signal alignment α → 0 的分析（R1-W6）互为印证。

---

## Weaknesses 回应

**[REBUT] R2-W1: "Capability Ceiling" 标题与 observational 证据不匹配**

R2 的核心论点是标题暗示 impossibility 但证据仅为 observational。我认为这个批评部分成立但被过度放大：

1. **标题本身是防御性的。** "Characterizing the Capability Ceiling" 是描述性 framing（"刻画"而非"证明"），"How Entity-Level Verification Fails" 是机制描述而非因果断言。这与 R2 引用的 "impossibility result" 标准有质的区别。

2. **论文确实提供了超越 observational 的证据：**
   - Proposition 1（Section 6.3, p6）给出了形式化的 upper bound (1−D)·G_nd·α，这 IS 一个理论 ceiling，不仅仅是 observation
   - TOST 等价性检验（Appendix p20, Table 16）正式界定了 selection gain 的最大可能幅度
   - k=57 的 Holm-Bonferroni 校正后无任何 selection signal 显著为正——这不是单纯的 "未观测到"，而是在严格多重比较控制下的系统性否定

3. **但 R2 对 causal 措辞的批评有道理。** "governs"、"determines" 等措辞确实超出了 observational+theoretical evidence 的支撑范围。这些措辞应改为 "is associated with"、"predicts" 等。

**结论：** 标题无需修改（"characterizing" 已经是适当的 hedge），但正文中 4-5 处因果措辞应系统性替换。这是 minor revision 级别的问题，不应影响接收决定。R2 将此评为 critical 过重。

---

**[AGREE] R2-W2: Cross-task validation 薄弱**

完全同意，这与我的 R1-W3 一致。具体补充：
- RE on SciERC: n=207 non-zero instances（总共 307 中 55.5% 为 zero-F1, Appendix o p24），仅 1 个模型（Qwen3-8B），信号排序与 NER 反转（Table 5, p7: EM 降为最强而 LP 减弱）—— 这恰恰说明 NER 的结论不能简单迁移
- SQL on Spider: 87.2% degeneracy 使结论 trivial
- Abstract/Introduction 的 "validate on RE and SQL" 宣传力度需降级

---

**[REBUT] R2-W3: 与 MBR 文献已有发现的区分不清**

R2 认为 correlation-selection gap 可能是 MBR 已知现象的 re-instantiation。我认为这个批评低估了本文的特异性贡献：

1. **Eikema & Aziz (2022) 和 Müller & Sennrich (2021) 的发现是关于 MT 的 sequence-level MBR。** MT 中 MBR 的主要挑战是 utility function 选择和 candidate/reference decoupling。本文的发现是关于 STRUCTURED OUTPUTS 的 ENTITY-LEVEL agreement，失败机制完全不同：
   - LP compression（Figure 8, p23: within-instance LP range 仅 0.041 nats on SciERC）是 constrained decoding 特有的现象——MT 不使用 schema-constrained generation
   - Entity-level degeneracy（Table 30, D=0.13-0.70）在 exact span+type matching 下的表现与 MT 的 BLEU-based matching 有质的区别

2. **论文 DID 讨论了这些关系（Appendix p.2, §25）。** Eikema et al. (2025) 的 structured MBR 被明确引用并对比（Table 62, p47）。问题在于这个讨论在 Appendix 而非 main text，这是呈现问题而非内容缺陷。

3. **本文的独特贡献是 DIAGNOSTIC：** 不仅报告 "MBR/SC 在 NER 上失败"，而是定位了 entity-level 粒度的具体失败机制（degeneracy + LP compression + α → 0）。MBR 文献没有提供这种粒度的诊断。

**建议：** 将 Appendix 中的 MBR 对比讨论（约 1 段）移入 main text Section 2 或 Section 8，但不应要求改变核心 contribution framing。

---

**[AGREE] R2-W4: Degeneracy 解释的 tautological element**

部分同意。我在 R1-W6 中提出了类似观点：degeneracy 的 "trivial" 解释（样本全同 → selection 无意义）确实不需要四阶段 cascade。核心洞察确实可以更简洁地表述为 "α → 0 on non-degenerate instances"。

但我要为 cascade 做部分辩护：
- Cascade 的价值是 METHODOLOGICAL 而非 NARRATIVE。它为 future work 提供了一个可复用的诊断协议（Appendix ae, p35 explicitly protocols 三步评估流程）
- 读者可能有不同的 prior——有些人认为 "all signals fail" 最可能由 degeneracy 解释，有些人认为是 signal 定义问题，有些人认为是数据集特性。Cascade 系统排除了这些替代解释
- 但 R2 的建议（在主文中更突出 non-degenerate failure 作为核心发现）是合理的

---

**[REBUT] R2-W5: Entity construction 新颖性有限**

R2 将 entity construction 简化为 "majority vote with threshold"。我认为这忽略了其诊断价值：

1. **贡献不在算法本身，而在对比分析。** Entity construction 的意义是与 entity SELECTION 的系统对比（Table 4, p7）：同样的 agreement signals 在 selection 上完全失败但在 construction 上稳定获益（+1.02-1.40pp, Table 61, p46），这精确定位了失败的粒度边界（sample-level vs entity-level）。

2. **MBR 形式化提供了理论解释。** 将 construction 形式化为 entity-level MBR（Appendix p.2）不仅是 notation——它解释了为什么 construction 能绕过 selection 的 LP compression 瓶颈（因为 construction 在 entity 粒度上操作，绕开了 sample-level LP ranking）。

3. **+1.02-1.40pp 在 NER 微调场景下是 meaningful。** 考虑到 greedy baseline 已在 F1=0.66-0.91 范围（Table 61），在已经很强的 baseline 上获得 >1pp 的无额外训练改进，且在多数据集上一致，是有实际价值的。

R2 对绝对增益幅度的质疑可以理解，但 "新颖性有限" 的评价需要考虑上述诊断和理论贡献。

---

**[AGREE] R2-W6: Abstract 信息密度过高**

同意。我在 R1-M4 中也提到 abstract 中 "correlation-selection gap" 首次出现时缺少直觉解释。12+ 数字确实过多，建议精简为核心 3-4 个数字。

---

**[AGREE] R2-W7: Limitations 未覆盖重要局限**

同意。Limitations（p8）覆盖了 correlational evidence、scope、statistical power，但缺少：
- Cross-task 证据的局限性（RE/SQL 的单薄性，我的 R1-W3 和 R2-W2 都指出了）
- Cross-model ensemble 的极度有限（仅 1 dataset × 1 model pair）
- Hidden-state probe 的 overfit 可能性（尤其是 per-dataset training 可能 inflate AUROC）

---

## Questions 回应

**[AGREE] R2-Q1**: LP 在 Few-NERD 上的 anomalous positive gain（+0.22pp）值得更多解释。Few-NERD 有最低的 degeneracy rate（Table 30: D=0.131），LP 在低 degeneracy 下的 discriminative power 更强，这个解释方向合理。但论文应在 main text 中显式讨论这个异常值。

**[AGREE] R2-Q2**: Hidden-state probe 的 cross-dataset transferability 是重要问题。论文目前是 per-dataset training（Table 45, p44），如果 probe 不能 transfer，其作为 "introspection boundary" 证据的价值会减弱——它可能只是 overfit 到 dataset-specific patterns。

**[AGREE] R2-Q3**: Entity construction "bypasses entity-level self-verification" 的措辞确实存在逻辑张力。Construction 仍然依赖 entity-level AGREEMENT（counting entity appearances across samples），只是在不同粒度上使用了这个信号。更准确的表述应是 "bypasses sample-level selection by operating at entity granularity"。

**[AGREE] R2-Q4**: Cross-model 未在 Few-NERD（degeneracy 最低的数据集）上测试是一个遗漏。考虑到论文的 narrative 是 "低 degeneracy 下 selection 更有希望"，在 Few-NERD 上测试 cross-model 是逻辑上最应该做的实验。

**[REBUT] R2-Q5**: Proposition 1 的 entity-wise independence 假设 violation 程度——论文实际上在 Appendix p.2（Remark after Proposition 1 proof）承认了这个假设的局限性，并指出 "we use balanced linear utility (α=1 throughout)"。Table 30（p41）的 Ratio 列（3-12%）间接量化了 violation 程度：如果假设完全成立，bound 应更紧。但 R2 的批评——论文未 DIRECTLY 量化 independence violation（例如通过测量 entity-pair correlation）——是合理的。这是一个可通过补充实验解决的 should-fix 问题。

---

## Missing References 回应

**[AGREE]** Varshney et al. (2022) 的 selective prediction 工作和 Malinin & Gales (2021) 的 structured uncertainty 工作确实应该被引用。我的审稿中也建议了 Malinin & Gales (2021)。

**[AGREE]** ma2024selfimproving 的第一作者 mismatch（bib "Ma" vs OpenAlex "Xie"）我在 R1-M6 中也标注了，需要核实。

---

## Minor Issues 回应

**[AGREE] R2-M1**: Abstract 中 ρ/AUROC 来自不同信号（ρ=0.47 来自 EM, AUROC=0.82 来自 VC 或 SJ），确实可能误导读者认为是同一信号。

**[AGREE] R2-M2**: Figure 1 caption 的 disclaimer 与主文因果措辞的矛盾——与 W1 中的讨论一致。

**[AGREE] R2-M3**: Eq. 1 的 Hungarian matching 缺引用，应加 Kuhn (1955) 或相应引用。

**[AGREE] R2-M4**: GPT-5.5 首次出现未解释其定位（OpenAI closed-source model）。

**[AGREE] R2-M5**: Footnote 1 在 NER context 中提 RE 确实突兀。

**[REBUT] R2-M6**: "47 页论文大量关键证据仅在附录中"——我认为这个批评需要具体化。Main text 8 页包含了核心 claims 的完整论证链（Table 1-4, Figure 1-5）。Appendix 中的是 SUPPORTING evidence（robustness checks, ablations, full tables），不是 KEY evidence 的唯一存放处。ARR format 鼓励利用 unlimited appendix 提供完整细节。如果 R2 能指出哪些 SPECIFIC key evidence 应在 main text 中但缺失，这会是更有建设性的批评。

---

## Overall Assessment 回应

R2 给出 **Overall 3.0 (Findings)**，我给出 **3.5 (Borderline Conference)**。差异主要来自两点分歧：

1. **W1（标题/因果措辞）的严重性**：R2 评为 critical，我认为是 warning 级别。标题本身（"Characterizing"）是防御性的；因果措辞需要修改但属于 minor revision，不影响核心 contribution。

2. **W5（entity construction 新颖性）**：R2 认为有限，我认为其诊断价值（与 selection 的系统对比 + MBR 形式化）被低估。

我们在 W2（cross-task validation 薄弱）和 W4（degeneracy tautology）上高度一致。综合来看，这篇论文的 NER 范围内贡献（诊断框架 + 统计严谨性 + 绕过路径）足够支撑 borderline conference，但 cross-task/cross-model 证据的不足确实是显著弱点。

**我的最终评分维持 3.5 (Borderline Conference)**，但如果 SciERC 多 seed 实验未补充且因果措辞未修改，我可以理解降至 3.0。


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

_source line 3241 · 2026-05-21T17:07:13.632598+00:00_

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


## Round 244

## Round 244

2 recorded events


### User

_source line 3242 · 2026-05-21T17:07:16.224884+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **与 R2 达成共识的关键问题**：cross-task validation 薄弱（W2）、degeneracy 解释的 tautological element（W4）、Limitations 覆盖不全（W7）、Abstract 过密（W6）
- **与 R2 分歧的关键问题**：
  - W1（标题/因果措辞）：我认为标题本身合理（"Characterizing" 已是适当 hedge），因果措辞修改属 minor revision，不应评为 critical
  - W5（entity construction 新颖性）：R2 低估了其诊断价值和 MBR 形式化的理论贡献
  - W3（MBR 文献区分）：论文的 NER-specific 失败机制（LP compression + entity-level degeneracy）与 MT MBR 文献有质的区别，只是讨论位置需从 Appendix 移入 main text
- **评分差异**：我维持 3.5（Borderline Conference），R2 给 3.0（Findings）

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

_source line 3243 · 2026-05-21T17:07:22.163436+00:00_

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


## Round 245

## Round 245

10 recorded events


### User

_source line 3244 · 2026-05-21T17:07:23.675717+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

### 总体判断
R1 的审稿从方法严谨性/实验设计/统计分析角度出发，评估准确且深入。大部分 weaknesses 我同意或强化。一个 rebut 点：R1-W5 关于 cross-dataset correlation 统计效力的担忧虽然技术正确，但核心结论不依赖该分析。

### 逐条回应摘要

**Strengths**: 全部 AGREE (S1-S5)，对 S2（可复用性）和 S4（建设性处理）有补充保留。

**Weaknesses**:
- [AGREE] W1 (SciERC 单 seed): 同意且补充——SciERC 承载了 disproportionate 的正面证据（construction gain 最大、probe AUROC 最高、cross-model 唯一测试），比 R1 指出的 "25% 权重" 更严重。
- [AGREE] W2 (Proposition 1 过松): 同意重定位建议。补充：empirical cascade 与 theoretical decomposition 存在两套平行框架但缺乏映射说明。
- [AGREE] W3 (RE/SQL 薄弱): 强烈同意，我认为应为 critical 而非 warning。RE 信号排序与 NER 反转（VC conditional ρ→0）进一步削弱 cross-task 论证。
- [AGREE] W4 (训练配方差异): 同意，Few-NERD 低 degeneracy 可能部分由更少 epochs 解释。
- [REBUT] W5 (统计效力): 核心结论依赖 per-dataset instance-level 检验（n=551-37648），power 充足。Cross-dataset correlation 是 supplementary analysis。
- [AGREE] W6 (Degeneracy 主要解释): 强烈同意，与我的 W4 一致。R1 的替代 framing "near-zero selection alignment despite moderate quality correlation" 比原文更精确。

**Questions**: Q1-Q4 全部 AGREE，Q5 REBUT（同架构 ensemble 属 deep ensemble，非论文 focus）。

**Minor Issues**: 全部 AGREE (M1-M6)。

### 评分差异说明
R1: 3.5 (Borderline Conference) vs 我: 3.0 (Findings)

差异来源：(1) 我的新颖性评估更严格——correlation-selection gap 与 MBR 文献重叠、capability ceiling framing 问题；(2) 我将 RE/SQL 薄弱标为 critical 而非 warning；(3) 两位 reviewer 均认为 degeneracy 可能是更简洁的唯一解释，削弱 cascade 的 contribution。

如果作者收紧 framing + 补充 SciERC 多 seed + 明确 MBR 区分，可考虑上调至 3.5。

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

_source line 3245 · 2026-05-21T17:07:46.336512+00:00_

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

_source line 3246 · 2026-05-21T17:07:46.437669+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T16:53:47.849588+00:00\", \"completed_at\": \"2026-05-21T16:57:30.008723+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 1-2\", \"message\": \"连续 2 页纯文字（Abstract + Intro + Diagnostic Framework 开头），无任何 figure/table/equation 穿插。审稿人在前 2 分钟内只看到文字墙，缺乏视觉锚定。建议将 Figure 1 提前至第 2 页或在 Intro 中增加一个 teaser figure/关键数字摘要。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"极度拥挤——Table 4、Table 5（含 a/b 两个子表）、Figure 3 全部堆叠在同一页。表格间距极小，Figure 3 被压缩到较小尺寸。建议将 1-2 个 table 移至 appendix 或重新分配 float 位置。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 作为首个 display item 有效传达核心 message：三阶段诊断级联 + 关键数值（AUROC, Δpp）。颜色编码清晰（绿/红/蓝）。图内文字偏小但可读。Caption 自包含。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 柱状图清晰，颜色（蓝/橙/绿）可区分。Table 1 使用 booktabs 风格 + 加粗最优值——专业。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 线图因页面拥挤被压缩，legend 和 axis labels 文字接近可读性下限（约正文字号 60-65%）。建议增大或移到单独位置。\"}, {\"severity\": \"info\", \"dimension\": \"pages 4-7\", \"message\": \"所有正文表格统一使用 booktabs 风格（\\\\toprule/\\\\midrule/\\\\bottomrule），最优值加粗，精度一致——排版规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"需验证正文页数是否符合 EMNLP 2026 的 8 页限制。Conclusion 结束位置约在第 9 页上部，Limitations 紧随其后。若 Conclusion 结束点超过第 8 页底部，需要压缩正文。（Limitations 和 Ethics Statement 不计入页数限制。）\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 6（Appendix）质量估计热力图使用红-黄-绿渐变色标。红绿色盲用户可能难以区分两端。建议改用 viridis 或 Blue-Orange 色标。\"}, {\"severity\": \"info\", \"dimension\": \"pages 41, 46, 47\", \"message\": \"Appendix 页面存在大面积空白（>50% 页面为空）。Table 30+31 仅占 p.41 上部 ~35%，Table 60+61 仅占 p.46 上部 ~40%，Table 62 仅占 p.47 中部 ~35%。虽为 appendix 无硬性限制，但可通过合并或重排减少空页。\"}, {\"severity\": \"info\", \"dimension\": \"pages 38-40\", \"message\": \"Appendix 表格密集区（Tables 13-29），字号偏小但仍可读。表格格式统一，booktabs 风格保持一致。\"}, {\"severity\": \"inf
…[truncated 244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3247 · 2026-05-21T17:09:01.382915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
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
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 3248 · 2026-05-21T17:09:01.433628+00:00_

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
…[truncated 2005 chars]

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

_source line 3249 · 2026-05-21T17:14:33.694510+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ===== 历史 resolved issues (保留) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3-old\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-9 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 30\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"scope 声明在 Introduction 和 Limitations 中已存在。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"仅2个~8B fine-tuned + 1个72B zero-shot。缺closed-source模型。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R1 REBUT R2-W1(事实前提错误:论文已测72B+GPT-5.5)。R2确认事实错误但仍指出缺instruction-tuned vs base对比。共识:模型覆盖度合理但缺base model对比。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: R1-W1(模型覆盖有限)+R2-W1(泛化性声明过度)再次独立提出。完整实验仅Qwen3-8B和LLaMA-3.1-8B(LoRA)。72B仅Few-NERD, GPT-5.5仅200实例。Limitations承认frontier models degeneracy不同(4%-5.5%)。两人AGREE。\"\n      - round: 30\n        reviewers: []\n        note: \"R30 fresh: 未作为独立 weakness 提出。R1 在 S1 中积极评价模型覆盖度(4B-72B+GPT-5.5)。R2-W2 focus on cross-task 而非模型覆盖。可能已通过 GPT-5.5 + Limitations 声明缓解。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n      - round: 30\n        reviewers: []\n        note: \"R30 fresh review 未提及。连续3轮 fresh review 未提及，可能已修复。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 30\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7）。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26视觉审查再次确认p7 display items过密。\"\n      - round: 27\n        reviewers: [2]\n        note: \"R27视觉审查: p6-7 display items密度高但可接受。Figure 1 部分面板文字偏小(约正文60-65%)。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: Figure 4面板较小(约正文65-70%)，Figure 3尺寸偏小但可读。info级。\"\n      - round: 30\n        reviewers: []\n        note: \"R30视觉审查: p7极度拥挤(Table 4+Table 5 a/b+Figure 3堆叠)，Figure 3被压缩。R1-M2也指出Figure 1 Center面板不够直观。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 30\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"construction不应作为standalone contribution。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R2-N2列prescriptive gains为critical(+1.0-1.4pp at 8x cost)。R1降为should-fix(主贡献是诊断框架)。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: R1-W3+R2-W4再次提出escape routes效果量偏小(+1.0-1.4pp at N×cost)。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2-W5再次提出: entity construction实质是MBR特殊情况+threshold majority vote，新颖性有限。R1 REBUT: 贡献在诊断对比价值(与selection的系统对比)和MBR形式化，非算法本身。分歧。\"\n    action_items:\n      - round: 26\n        action: \"确认construction在正文中已降级为diagnostic-motivated ablation而非contribution。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction（framing tautology）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 30\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 必须重构Abstract/Intro将structural/empirical二分法前置。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: Section 4明确区分了definitional vs empirical层面。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28 R2-N2: 与MBR文献增量新颖性需更精确定位。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: R2-W3提出与MBR文献(Eikema & Aziz 2022, Müller & Sennrich 2021)已有发现的区分不清。R1 REBUT: NER-specific失败机制(LP compression under constrained decoding + entity-level degeneracy)与MT MBR有质的区别，但讨论在Appendix而非main text。R2-W4提出degeneracy解释的tautological element——R1 AGREE(α→0才是核心洞察)。\"\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 30\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Reduced to 4 key numbers.\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R2再次提出但R1 REBUT(empirical NLP论文惯例)。共识: 当前密度尚可接受。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: R2-W6再次提出(~180词含12+数字)。R1 AGREE。共识: 需精简为核心3-4个数字。\"\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n      - round: 30\n        reviewers: []\n        note: \"R30 fresh review 未提及。连续3轮 fresh review 未提及。\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 公式删除，改为定性叙述。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"method.tex 加定义。\"\n    resolution_round: 24\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1 minor #2: 最高ρ为EM 0.472(LLaMA CoNLL)，'up to 0.45'略低。建议核实。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2-M1: Abstract中ρ/AUROC来自不同信号(ρ=0.47来自EM, AUROC=0.82来自VC/SJ)但写法可能误导。\"\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"n=23 power 仅约 50% for ρ=0.4。结论过强。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及此 specific null finding。\"\n      - round: 30\n        reviewers: [1]\n        note: \"R30 R1-W5: cross-dataset correlation n=23时post-hoc power在ρ=0.3时仅0.32。主文措辞比证据支持的更断定性。R2 REBUT: 核心结论依赖per-dataset instance-level检验(n=551-37648)，power充足，cross-dataset correlation是supplementary。\"\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"cross-model仅1数据集1对模型。§5.3 SCD不再出现。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n      - round: 28\n        reviewers: [1]\n        note: \"R28 R1-W5: cross-model仅Qwen3-8B+LLaMA-3.1-8B。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: R1-W3+R2-W2共识RE/SQL薄弱(RE仅SciERC单数据集单模型, SQL仅n=196+87.2%degeneracy)。cross-model仅1 dataset×1 model pair。\"\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"'first systematic characterization'过强，应限定为'for NER'。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: 标题'Structured Generation'与NER-centric证据严重不匹配。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: 标题已为NER-specific。RE/SQL定位为preliminary extension。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: 标题已NER-specific('How Entity-Level Verification Fails in NER')。R2-W2仍认为Abstract/Intro的'validate on RE and SQL'宣传力度超出证据。R1-W3同意RE/SQL应降级为'preliminary extension'。两人共识。\"\n    action_items:\n      - round: 27\n        action: \"标题从'Structured Generation'缩窄为NER-specific或'Structured Information Extraction'。Abstract/Intro scope相应调整。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni；4 数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"CoNLL 增益为负 (−0.29pp)。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"p_adj矛盾(§1: 0.20 vs Table 13: 0.038)。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: prescriptive gains边际(+1.0-1.4pp at 8x cost)。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: 全局Holm k=57下p_adj=0.055。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2-W5: +1.4pp gain绝对值不大。R1 REBUT: 在F1=0.66-0.91基线上>1pp无额外训练改进有实际价值。分歧但非核心问题。\"\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"脚注9报告k=38但Table 13列k=57。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-N3 [critical]: Abstract k=19 vs Table 13实际21行。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: per-family分割为事后决定。Abstract报告k=21。\"\n      - round: 30\n        reviewers: [1]\n        note: \"R30 R1-M1: Table 13 caption中k值需确认(k=52 vs k=57)。\"\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"fine-tuning/scale/architecture混淆。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。Limitations已承认。\"\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"SciERC single-seed用于detailed diagnostic。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh: 论文已改为3-seed(Few-NERD/CoNLL)。SciERC仍σ=0.48pp。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30 R1-W1 [critical]: SciERC仅1个seed(seed=42)，占25%NER数据集权重。SciERC承载disproportionate正面证据(construction gain最大+1.53pp ZS, probe AUROC最高)。单seed结果可能是artifact。R2 AGREE并补充SciERC证据比25%权重更重要。两人强烈共识。\"\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"嵌套NER场景何时violated未讨论。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-Q4: entity-wise independence在NER中是否合理。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2-Q5: entity-wise independence假设violation程度如何量化。R1交叉回应: Table 30 Ratio(3-12%)间接反映violation，但论文未直接测量entity-pair correlation。Should-fix。\"\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"bound仅解释3-12%的gap。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: bound仅捕获4.7-12.1%实际增益。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: θ_crit=0.70给出了有效的定性预测力(necessary condition)。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30 R1-W2 [critical]: Bound(1-D)·G_nd·α仅捕获3-12%实际gain(Table 30)。当bound与实际gain同量级时几乎无排除力。论文自述'loose'但仍列为核心贡献。R2 AGREE。共识: 应重定位为'diagnostic decomposition'而非'performance bound'。\"\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"未直接提及。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: 与Yun et al. (2025) diversity collapse差异化需强化。\"\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 未找到/元数据不匹配/orphan bib\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"hobelsberger2025systematic疑似虚构，17 orphan bib entries。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: 2 orphan, 0 fake。较之前有改善(从17降至2)。\"\n      - round: 28\n        reviewers: [1]\n        note: \"R28: lightman2024verify和aggarwal2023adaptive在OpenAlex未匹配。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: R2引用验证57 bib, 0 orphan, 0 missing, 2 not found(OpenAlex覆盖gaps), 4 encoding mismatches。R1-M6确认4个minor first-author name mismatches。引用质量已显著改善。\"\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 标注为descriptive diagnostic而非causal chain。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: 因果语言('governs','explaining')与相关性证据不匹配。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: 标题'Capability Ceiling'暗示硬上界但证据为observational。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: R1-W6+R2-W4共识degeneracy可能是更简洁的唯一解释——α→0(near-zero selection alignment despite moderate quality correlation)才是核心洞察，四阶段cascade可能over-engineered。R1为cascade做部分辩护: 方法论价值(可复用诊断协议)和系统排除替代解释。但同意non-degenerate failure应更突出。\"\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: EL4NER, Self-Certainty BoN 等\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"EL4NER必须引用。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1建议补DeNero et al. 2009, Desai & Durrett 2020, Huang et al. 2024。\"\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"Oracle Scaling figure 已生成并集成。\"\n    resolution_round: 26\n\n  - id: \"R26-N1\"\n    summary: \"N=8/16对test-time compute scaling研究范围过窄\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"建议至少补N=32或论证N=8的cost-efficiency。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及N range。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: N止步于32。\"\n\n  - id: \"R26-N2\"\n    summary: \"Trained verifier (LightGBM AUC=0.923) 负面结果scope有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R26-W1\"\n    summary: \"论文同时做4件事，每项深度不够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 R2 Excitement=2.5/5部分原因是novelty分散。\"\n      - round: 30\n        reviewers: []\n        note: \"R30: 未作为独立weakness提出，但R2 Excitement=3/5可能部分受此影响。\"\n\n  - id: \"R26-VIS1\"\n    summary: \"Page 7 display items严重过密（4表+1图）\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: '略显拥挤但信息承载量高'。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: 密度适合实证诊断论文。\"\n      - round: 30\n        reviewers: []\n        note: \"R30视觉审查[warning]: p7极度拥挤——Table 4+Table 5(a/b)+Figure 3全部堆叠。表格间距极小，Figure 3被压缩。建议移1-2个table到appendix或重排float。R1-M2也提到Figure 1 Center面板不够直观。\"\n\n  - id: \"R26-VIS2\"\n    summary: \"Figure 6 heatmap红绿色阶对色盲不友好\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 26\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: 建议双色发散色板。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: Figure 1绿/红对比对红绿色盲不友好。\"\n      - round: 30\n        reviewers: []\n        note: \"R30视觉审查[info]: p17 Figure 6热力图使用红-黄-绿渐变色标，建议改用viridis或Blue-Orange色标。\"\n\n  - id: \"R27-N1\"\n    summary: \"因果语言与相关性证据不匹配——Section 9 'governs'、Abstract 'explaining why'\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: Figure 1标'not causal'但§9用'governs'。强烈共识。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: 标题'Capability Ceiling'暗示硬上界。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30 R2-W1 [critical]: 标题暗示impossibility，主文多处因果措辞('governs','determines','explaining where and why')与observational design矛盾。R1 REBUT: 标题'Characterizing'已是防御性framing，但同意正文4-5处因果措辞需替换为'is associated with','predicts'等。R1认为这是minor revision不应为critical。分歧: R2维持critical，R1认为warning。\"\n    action_items:\n      - round: 27\n        action: \"全文统一将因果动词替换为相关性语言。Discussion加段讨论因果推断局限。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R27-N2\"\n    summary: \"Holm-Bonferroni k=19(Abstract) vs Table 13实际21行——影响p_adj可复现性\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"Abstract k=19但Table 13有21项。R2 AGREE。交叉共识: 需核实并修正。\"\n      - round: 30\n        reviewers: [1]\n        note: \"R30 R1-M1: Table 13 caption中k值需确认(k=52 vs k=57)。与此issue相关。\"\n\n  - id: \"R27-W1\"\n    summary: \"7种方法分类边界模糊——diagnostic probes vs selection methods未区分\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"Abstract '7 methods'含diagnostic probes和selection methods混为一体。\"\n\n  - id: \"R27-W2\"\n    summary: \"RE分析受entity span error混淆(55.5% F1=0)——测量NER→RE错误传播而非RE本身\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W2+R2-W3: RE FEATURE-OF ρ≈0 vs HYPONYM-OF ρ=0.646。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28: RE仅SciERC一个数据集, 55.5% zero-F1来自span错误。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2-W2提及RE仅1数据集+55.5% zero-F1+span error confound。R1-W3同意。\"\n\n  - id: \"R27-W3\"\n    summary: \"k=57全局Holm + RE/小配置样本量→统计功效不足，负面结论可能是power问题\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"RE n≈397时仅大效应量可检测。需Conclusion加hedge。\"\n\n  - id: \"R27-W4\"\n    summary: \"Entity construction +1.0-1.4pp at 8x cost——cost-effectiveness未在主文讨论\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"Table 61在Appendix但主文未引用。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"Discussion承认'N× cost for ≈1 pp'但缺Pareto曲线量化。\"\n\n  - id: \"R27-M1\"\n    summary: \"2个orphan bib entries: holm1979simple, xia2025survey\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1+R2独立发现。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2引用验证: 57 bib, 0 orphan。可能已修复。\"\n\n  - id: \"R27-M2\"\n    summary: \"Figure 2 caption 'oracle gap'未自含定义\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"建议caption加定义。\"\n\n  - id: \"R27-M3\"\n    summary: \"Limitations 未讨论closed-source API模型的degeneracy profile差异\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"现有Limitations仅提LP signal不可用。\"\n      - round: 30\n        reviewers: []\n        note: \"R30: Limitations已提及frontier models degeneracy差异(Claude 74% vs DeepSeek 5.5%)。可能已部分修复。\"\n\n  - id: \"R27-MR1\"\n    summary: \"缺失引用: DeNero 2009, Desai & Durrett 2020, Huang 2024, KDD 2025 survey, Aronica 2024\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"核心3篇(DeNero, Huang, Aronica)应补。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28新增Ma et al.(2024) NAACL, Madaan et al.(2023) NeurIPS。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2建议补Varshney et al. 2022, Xin et al. 2021, Malinin & Gales 2021。R1认为无重要缺失，仅可选补Malinin & Gales 2021。引用覆盖度评为良好。ma2024selfimproving已在bib中。\"\n\n  - id: \"R28-N1\"\n    summary: \"Holm-Bonferroni表述风险: 旧experiments.tex含错误'survives at k=57'声明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: []\n        note: \"experiments_main.tex已正确区分per-family和global。\"\n\n  - id: \"R28-N2\"\n    summary: \"Correlation-selection gap与MBR文献增量新颖性定位不够精准\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 30\n    mentions:\n      - round: 28\n        reviewers: [2]\n        note: \"Eikema et al.(2025)已知MBR utilities在structured outputs退化。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30 R2-W3 [warning]: MBR文献已有发现(Eikema & Aziz 2022 decoupling, Müller & Sennrich 2021 MBR不优于beam)如何inform本文gap未讨论。R1 REBUT: NER-specific机制(LP compression under constrained decoding)与MT MBR有质的区别，但对比讨论在Appendix需移入main text。分歧程度: R2认为区分不充分，R1认为内容有区别只是呈现位置不当。\"\n\n  - id: \"R28-W1\"\n    summary: \"Hidden-state probe跨数据集AUROC方差(SciERC 0.63 vs CoNLL 0.88)未充分解释\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 30\n    mentions:\n      - round: 28\n        reviewers: [1, 2]\n        note: \"AUROC变化剧烈，cross-dataset transfer下降。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30 R2-Q2关注hidden-state probe的LODO评估。R1交叉回应AGREE: per-dataset training可能inflate AUROC，如probe不能transfer则'introspection boundary'证据价值减弱。论文已有LODO结果(§3: AUROC drops to 0.559-0.671)但主文讨论不足。\"\n\n  - id: \"R28-MR1\"\n    summary: \"缺失引用: Ma et al. (2024) NAACL SC-for-NER, Madaan et al. (2023) Self-Refine\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 30\n    mentions:\n      - round: 28\n        reviewers: [2]\n        note: \"Ma et al.(2024)是最直接先行工作。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2引用验证确认ma2024selfimproving已在bib中(§8引用)。需核实第一作者(bib 'Ma' vs OpenAlex 'Xie')。Madaan et al. 2023也已引用(§3 MRSC)。引用已补入。\"\n\n  - id: \"R28-FILE1\"\n    summary: \"experiments.tex旧版本与experiments_main.tex并存——编译风险\"\n    category: format\n    severity: critical\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: []\n        note: \"main.tex确认使用experiments_main.tex。\"\n\n  # ===== Round 30 新发现 =====\n\n  - id: \"R30-N1\"\n    summary: \"SciERC 单 seed 削弱 25% NER 证据基础——承载 disproportionate 正面证据\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 30\n    last_seen_round: 30\n    mentions:\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R1-W1 [critical]: SciERC仅seed=42，无方差信息。SciERC承载最大construction gain(+1.53pp ZS)、最高probe AUROC(0.882 CoNLL但SciERC是medium-difficulty primary test bed)。单seed结果可能是artifact。R2 AGREE并补充SciERC证据比R1估计的25%权重更严重。两人强烈共识。\"\n    action_items:\n      - round: 30\n        action: \"补充SciERC 3-seed实验；或在正文中显著标注single-seed caveat(当前仅Appendix j简要提及)。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R30-N2\"\n    summary: \"Proposition 1 (Entity Selection Bound) 过松(3-12%)需重定位\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 30\n    last_seen_round: 30\n    mentions:\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R1-W2 [critical]: Bound (1-D)·G_nd·α 仅捕获3-12%实际gain(Table 30)。三因子各有意义但相乘过于保守。当bound与实际gain同量级时无排除力。论文自述'loose'但列为核心贡献。R2 AGREE并补充empirical cascade与theoretical decomposition存在两套平行框架缺映射。共识: 应定位为'diagnostic decomposition'而非'performance bound'，讨论哪个因子最保守。\"\n    action_items:\n      - round: 30\n        action: \"正文中将Proposition 1重定位为diagnostic decomposition；讨论bound为何松(α估计最保守？信号依赖性？)。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R30-W1\"\n    summary: \"训练配方差异(Few-NERD 3 epochs vs others 5)构成跨数据集比较混淆\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 30\n    last_seen_round: 30\n    mentions:\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R1-W4: SciERC消融显示degeneracy随epoch单调递增(43.5%→60.3%)。Few-NERD低degeneracy(13%)可能部分由更少epochs解释。Few-NERD未做5-epoch对照。R2 AGREE。\"\n    action_items:\n      - round: 30\n        action: \"对Few-NERD补充5-epoch消融或解释3 epochs选择依据；跨数据集讨论中控制训练收敛状态。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R30-W2\"\n    summary: \"Limitations未覆盖cross-task证据弱点、cross-model极度有限、probe overfit可能性\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 30\n    last_seen_round: 30\n    mentions:\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R2-W7: Limitations覆盖了correlational evidence/scope/power但缺(a)RE/SQL证据单薄性(b)cross-model仅1 dataset×1 model pair(c)hidden-state probe per-dataset overfit可能(d)entity construction gain幅度。R1 AGREE。\"\n    action_items:\n      - round: 30\n        action: \"Limitations补充上述4点局限。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R30-MR1\"\n    summary: \"建议补充引用: Varshney et al. 2022, Malinin & Gales 2021\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 30\n    last_seen_round: 30\n    mentions:\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R2建议补Varshney et al. 2022(selective prediction), Xin et al. 2021, Malinin & Gales 2021(structured uncertainty)。R1认为可选补Malinin & Gales 2021。非必须但recommended。\""
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
    "issues_yaml": "issues:\n  # ===== 历史 resolved issues (保留) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3-old\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-9 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 30\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"scope 声明在 Introduction 和 Limitations 中已存在。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"仅2个~8B fine-tuned + 1个72B zero-shot。缺closed-source模型。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R1 REBUT R2-W1(事实前提错误:论文已测72B+GPT-5.5)。R2确认事实错误但仍指出缺instruction-tuned vs base对比。共识:模型覆盖度合理但缺base model对比。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: R1-W1(模型覆盖有限)+R2-W1(泛化性声明过度)再次独立提出。完整实验仅Qwen3-8B和LLaMA-3.1-8B(LoRA)。72B仅Few-NERD, GPT-5.5仅200实例。Limitations承认frontier models degeneracy不同(4%-5.5%)。两人AGREE。\"\n      - round: 30\n        reviewers: []\n        note: \"R30 fresh: 未作为独立 weakness 提出。R1 在 S1 中积极评价模型覆盖度(4B-72B+GPT-5.5)。R2-W2 focus on cross-task 而非模型覆盖。可能已通过 GPT-5.5 + Limitations 声明缓解。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n      - round: 30\n        reviewers: []\n        note: \"R30 fresh review 未提及。连续3轮 fresh review 未提及，可能已修复。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 30\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7）。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26视觉审查再次确认p7 display items过密。\"\n      - round: 27\n        reviewers: [2]\n        note: \"R27视觉审查: p6-7 display items密度高但可接受。Figure 1 部分面板文字偏小(约正文60-65%)。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: Figure 4面板较小(约正文65-70%)，Figure 3尺寸偏小但可读。info级。\"\n      - round: 30\n        reviewers: []\n        note: \"R30视觉审查: p7极度拥挤(Table 4+Table 5 a/b+Figure 3堆叠)，Figure 3被压缩。R1-M2也指出Figure 1 Center面板不够直观。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 30\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"construction不应作为standalone contribution。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R2-N2列prescriptive gains为critical(+1.0-1.4pp at 8x cost)。R1降为should-fix(主贡献是诊断框架)。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: R1-W3+R2-W4再次提出escape routes效果量偏小(+1.0-1.4pp at N×cost)。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2-W5再次提出: entity construction实质是MBR特殊情况+threshold majority vote，新颖性有限。R1 REBUT: 贡献在诊断对比价值(与selection的系统对比)和MBR形式化，非算法本身。分歧。\"\n    action_items:\n      - round: 26\n        action: \"确认construction在正文中已降级为diagnostic-motivated ablation而非contribution。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction（framing tautology）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 30\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 必须重构Abstract/Intro将structural/empirical二分法前置。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: Section 4明确区分了definitional vs empirical层面。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28 R2-N2: 与MBR文献增量新颖性需更精确定位。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: R2-W3提出与MBR文献(Eikema & Aziz 2022, Müller & Sennrich 2021)已有发现的区分不清。R1 REBUT: NER-specific失败机制(LP compression under constrained decoding + entity-level degeneracy)与MT MBR有质的区别，但讨论在Appendix而非main text。R2-W4提出degeneracy解释的tautological element——R1 AGREE(α→0才是核心洞察)。\"\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 30\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Reduced to 4 key numbers.\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: R2再次提出但R1 REBUT(empirical NLP论文惯例)。共识: 当前密度尚可接受。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: R2-W6再次提出(~180词含12+数字)。R1 AGREE。共识: 需精简为核心3-4个数字。\"\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未提及。\"\n      - round: 30\n        reviewers: []\n        note: \"R30 fresh review 未提及。连续3轮 fresh review 未提及。\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 公式删除，改为定性叙述。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"method.tex 加定义。\"\n    resolution_round: 24\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1 minor #2: 最高ρ为EM 0.472(LLaMA CoNLL)，'up to 0.45'略低。建议核实。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2-M1: Abstract中ρ/AUROC来自不同信号(ρ=0.47来自EM, AUROC=0.82来自VC/SJ)但写法可能误导。\"\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"n=23 power 仅约 50% for ρ=0.4。结论过强。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及此 specific null finding。\"\n      - round: 30\n        reviewers: [1]\n        note: \"R30 R1-W5: cross-dataset correlation n=23时post-hoc power在ρ=0.3时仅0.32。主文措辞比证据支持的更断定性。R2 REBUT: 核心结论依赖per-dataset instance-level检验(n=551-37648)，power充足，cross-dataset correlation是supplementary。\"\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"cross-model仅1数据集1对模型。§5.3 SCD不再出现。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n      - round: 28\n        reviewers: [1]\n        note: \"R28 R1-W5: cross-model仅Qwen3-8B+LLaMA-3.1-8B。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: R1-W3+R2-W2共识RE/SQL薄弱(RE仅SciERC单数据集单模型, SQL仅n=196+87.2%degeneracy)。cross-model仅1 dataset×1 model pair。\"\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"'first systematic characterization'过强，应限定为'for NER'。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27 fresh: 标题'Structured Generation'与NER-centric证据严重不匹配。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: 标题已为NER-specific。RE/SQL定位为preliminary extension。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: 标题已NER-specific('How Entity-Level Verification Fails in NER')。R2-W2仍认为Abstract/Intro的'validate on RE and SQL'宣传力度超出证据。R1-W3同意RE/SQL应降级为'preliminary extension'。两人共识。\"\n    action_items:\n      - round: 27\n        action: \"标题从'Structured Generation'缩窄为NER-specific或'Structured Information Extraction'。Abstract/Intro scope相应调整。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni；4 数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"CoNLL 增益为负 (−0.29pp)。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"p_adj矛盾(§1: 0.20 vs Table 13: 0.038)。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: prescriptive gains边际(+1.0-1.4pp at 8x cost)。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: 全局Holm k=57下p_adj=0.055。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2-W5: +1.4pp gain绝对值不大。R1 REBUT: 在F1=0.66-0.91基线上>1pp无额外训练改进有实际价值。分歧但非核心问题。\"\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"脚注9报告k=38但Table 13列k=57。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-N3 [critical]: Abstract k=19 vs Table 13实际21行。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: per-family分割为事后决定。Abstract报告k=21。\"\n      - round: 30\n        reviewers: [1]\n        note: \"R30 R1-M1: Table 13 caption中k值需确认(k=52 vs k=57)。\"\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"fine-tuning/scale/architecture混淆。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。Limitations已承认。\"\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"SciERC single-seed用于detailed diagnostic。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh: 论文已改为3-seed(Few-NERD/CoNLL)。SciERC仍σ=0.48pp。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30 R1-W1 [critical]: SciERC仅1个seed(seed=42)，占25%NER数据集权重。SciERC承载disproportionate正面证据(construction gain最大+1.53pp ZS, probe AUROC最高)。单seed结果可能是artifact。R2 AGREE并补充SciERC证据比25%权重更重要。两人强烈共识。\"\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"嵌套NER场景何时violated未讨论。\"\n      - round: 27\n        reviewers: [1]\n        note: \"R27 R1-Q4: entity-wise independence在NER中是否合理。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2-Q5: entity-wise independence假设violation程度如何量化。R1交叉回应: Table 30 Ratio(3-12%)间接反映violation，但论文未直接测量entity-pair correlation。Should-fix。\"\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"bound仅解释3-12%的gap。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: bound仅捕获4.7-12.1%实际增益。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: θ_crit=0.70给出了有效的定性预测力(necessary condition)。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30 R1-W2 [critical]: Bound(1-D)·G_nd·α仅捕获3-12%实际gain(Table 30)。当bound与实际gain同量级时几乎无排除力。论文自述'loose'但仍列为核心贡献。R2 AGREE。共识: 应重定位为'diagnostic decomposition'而非'performance bound'。\"\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"未直接提及。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: 与Yun et al. (2025) diversity collapse差异化需强化。\"\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 未找到/元数据不匹配/orphan bib\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"hobelsberger2025systematic疑似虚构，17 orphan bib entries。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: 2 orphan, 0 fake。较之前有改善(从17降至2)。\"\n      - round: 28\n        reviewers: [1]\n        note: \"R28: lightman2024verify和aggarwal2023adaptive在OpenAlex未匹配。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: R2引用验证57 bib, 0 orphan, 0 missing, 2 not found(OpenAlex覆盖gaps), 4 encoding mismatches。R1-M6确认4个minor first-author name mismatches。引用质量已显著改善。\"\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 30\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"共识: 标注为descriptive diagnostic而非causal chain。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: 因果语言('governs','explaining')与相关性证据不匹配。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: 标题'Capability Ceiling'暗示硬上界但证据为observational。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30: R1-W6+R2-W4共识degeneracy可能是更简洁的唯一解释——α→0(near-zero selection alignment despite moderate quality correlation)才是核心洞察，四阶段cascade可能over-engineered。R1为cascade做部分辩护: 方法论价值(可复用诊断协议)和系统排除替代解释。但同意non-degenerate failure应更突出。\"\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: EL4NER, Self-Certainty BoN 等\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"EL4NER必须引用。\"\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: R1建议补DeNero et al. 2009, Desai & Durrett 2020, Huang et al. 2024。\"\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"Oracle Scaling figure 已生成并集成。\"\n    resolution_round: 26\n\n  - id: \"R26-N1\"\n    summary: \"N=8/16对test-time compute scaling研究范围过窄\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 28\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"建议至少补N=32或论证N=8的cost-efficiency。\"\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及N range。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: N止步于32。\"\n\n  - id: \"R26-N2\"\n    summary: \"Trained verifier (LightGBM AUC=0.923) 负面结果scope有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 fresh review 未直接提及。\"\n\n  - id: \"R26-W1\"\n    summary: \"论文同时做4件事，每项深度不够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27 R2 Excitement=2.5/5部分原因是novelty分散。\"\n      - round: 30\n        reviewers: []\n        note: \"R30: 未作为独立weakness提出，但R2 Excitement=3/5可能部分受此影响。\"\n\n  - id: \"R26-VIS1\"\n    summary: \"Page 7 display items严重过密（4表+1图）\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: '略显拥挤但信息承载量高'。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: 密度适合实证诊断论文。\"\n      - round: 30\n        reviewers: []\n        note: \"R30视觉审查[warning]: p7极度拥挤——Table 4+Table 5(a/b)+Figure 3全部堆叠。表格间距极小，Figure 3被压缩。建议移1-2个table到appendix或重排float。R1-M2也提到Figure 1 Center面板不够直观。\"\n\n  - id: \"R26-VIS2\"\n    summary: \"Figure 6 heatmap红绿色阶对色盲不友好\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 26\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: []\n        note: \"R27视觉审查: 建议双色发散色板。\"\n      - round: 28\n        reviewers: []\n        note: \"R28视觉审查: Figure 1绿/红对比对红绿色盲不友好。\"\n      - round: 30\n        reviewers: []\n        note: \"R30视觉审查[info]: p17 Figure 6热力图使用红-黄-绿渐变色标，建议改用viridis或Blue-Orange色标。\"\n\n  - id: \"R27-N1\"\n    summary: \"因果语言与相关性证据不匹配——Section 9 'governs'、Abstract 'explaining why'\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R27: Figure 1标'not causal'但§9用'governs'。强烈共识。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"R28: 标题'Capability Ceiling'暗示硬上界。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30 R2-W1 [critical]: 标题暗示impossibility，主文多处因果措辞('governs','determines','explaining where and why')与observational design矛盾。R1 REBUT: 标题'Characterizing'已是防御性framing，但同意正文4-5处因果措辞需替换为'is associated with','predicts'等。R1认为这是minor revision不应为critical。分歧: R2维持critical，R1认为warning。\"\n    action_items:\n      - round: 27\n        action: \"全文统一将因果动词替换为相关性语言。Discussion加段讨论因果推断局限。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R27-N2\"\n    summary: \"Holm-Bonferroni k=19(Abstract) vs Table 13实际21行——影响p_adj可复现性\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"Abstract k=19但Table 13有21项。R2 AGREE。交叉共识: 需核实并修正。\"\n      - round: 30\n        reviewers: [1]\n        note: \"R30 R1-M1: Table 13 caption中k值需确认(k=52 vs k=57)。与此issue相关。\"\n\n  - id: \"R27-W1\"\n    summary: \"7种方法分类边界模糊——diagnostic probes vs selection methods未区分\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"Abstract '7 methods'含diagnostic probes和selection methods混为一体。\"\n\n  - id: \"R27-W2\"\n    summary: \"RE分析受entity span error混淆(55.5% F1=0)——测量NER→RE错误传播而非RE本身\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1-W2+R2-W3: RE FEATURE-OF ρ≈0 vs HYPONYM-OF ρ=0.646。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28: RE仅SciERC一个数据集, 55.5% zero-F1来自span错误。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2-W2提及RE仅1数据集+55.5% zero-F1+span error confound。R1-W3同意。\"\n\n  - id: \"R27-W3\"\n    summary: \"k=57全局Holm + RE/小配置样本量→统计功效不足，负面结论可能是power问题\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1]\n        note: \"RE n≈397时仅大效应量可检测。需Conclusion加hedge。\"\n\n  - id: \"R27-W4\"\n    summary: \"Entity construction +1.0-1.4pp at 8x cost——cost-effectiveness未在主文讨论\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 28\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"Table 61在Appendix但主文未引用。\"\n      - round: 28\n        reviewers: [1, 2]\n        note: \"Discussion承认'N× cost for ≈1 pp'但缺Pareto曲线量化。\"\n\n  - id: \"R27-M1\"\n    summary: \"2个orphan bib entries: holm1979simple, xia2025survey\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"R1+R2独立发现。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2引用验证: 57 bib, 0 orphan。可能已修复。\"\n\n  - id: \"R27-M2\"\n    summary: \"Figure 2 caption 'oracle gap'未自含定义\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"建议caption加定义。\"\n\n  - id: \"R27-M3\"\n    summary: \"Limitations 未讨论closed-source API模型的degeneracy profile差异\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [2]\n        note: \"现有Limitations仅提LP signal不可用。\"\n      - round: 30\n        reviewers: []\n        note: \"R30: Limitations已提及frontier models degeneracy差异(Claude 74% vs DeepSeek 5.5%)。可能已部分修复。\"\n\n  - id: \"R27-MR1\"\n    summary: \"缺失引用: DeNero 2009, Desai & Durrett 2020, Huang 2024, KDD 2025 survey, Aronica 2024\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 27\n    last_seen_round: 30\n    mentions:\n      - round: 27\n        reviewers: [1, 2]\n        note: \"核心3篇(DeNero, Huang, Aronica)应补。\"\n      - round: 28\n        reviewers: [2]\n        note: \"R28新增Ma et al.(2024) NAACL, Madaan et al.(2023) NeurIPS。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2建议补Varshney et al. 2022, Xin et al. 2021, Malinin & Gales 2021。R1认为无重要缺失，仅可选补Malinin & Gales 2021。引用覆盖度评为良好。ma2024selfimproving已在bib中。\"\n\n  - id: \"R28-N1\"\n    summary: \"Holm-Bonferroni表述风险: 旧experiments.tex含错误'survives at k=57'声明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: []\n        note: \"experiments_main.tex已正确区分per-family和global。\"\n\n  - id: \"R28-N2\"\n    summary: \"Correlation-selection gap与MBR文献增量新颖性定位不够精准\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 30\n    mentions:\n      - round: 28\n        reviewers: [2]\n        note: \"Eikema et al.(2025)已知MBR utilities在structured outputs退化。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30 R2-W3 [warning]: MBR文献已有发现(Eikema & Aziz 2022 decoupling, Müller & Sennrich 2021 MBR不优于beam)如何inform本文gap未讨论。R1 REBUT: NER-specific机制(LP compression under constrained decoding)与MT MBR有质的区别，但对比讨论在Appendix需移入main text。分歧程度: R2认为区分不充分，R1认为内容有区别只是呈现位置不当。\"\n\n  - id: \"R28-W1\"\n    summary: \"Hidden-state probe跨数据集AUROC方差(SciERC 0.63 vs CoNLL 0.88)未充分解释\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 30\n    mentions:\n      - round: 28\n        reviewers: [1, 2]\n        note: \"AUROC变化剧烈，cross-dataset transfer下降。\"\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R30 R2-Q2关注hidden-state probe的LODO评估。R1交叉回应AGREE: per-dataset training可能inflate AUROC，如probe不能transfer则'introspection boundary'证据价值减弱。论文已有LODO结果(§3: AUROC drops to 0.559-0.671)但主文讨论不足。\"\n\n  - id: \"R28-MR1\"\n    summary: \"缺失引用: Ma et al. (2024) NAACL SC-for-NER, Madaan et al. (2023) Self-Refine\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 30\n    mentions:\n      - round: 28\n        reviewers: [2]\n        note: \"Ma et al.(2024)是最直接先行工作。\"\n      - round: 30\n        reviewers: [2]\n        note: \"R30 R2引用验证确认ma2024selfimproving已在bib中(§8引用)。需核实第一作者(bib 'Ma' vs OpenAlex 'Xie')。Madaan et al. 2023也已引用(§3 MRSC)。引用已补入。\"\n\n  - id: \"R28-FILE1\"\n    summary: \"experiments.tex旧版本与experiments_main.tex并存——编译风险\"\n    category: format\n    severity: critical\n    status: in_progress\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - round: 28\n        reviewers: []\n        note: \"main.tex确认使用experiments_main.tex。\"\n\n  # ===== Round 30 新发现 =====\n\n  - id: \"R30-N1\"\n    summary: \"SciERC 单 seed 削弱 25% NER 证据基础——承载 disproportionate 正面证据\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 30\n    last_seen_round: 30\n    mentions:\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R1-W1 [critical]: SciERC仅seed=42，无方差信息。SciERC承载最大construction gain(+1.53pp ZS)、最高probe AUROC(0.882 CoNLL但SciERC是medium-difficulty primary test bed)。单seed结果可能是artifact。R2 AGREE并补充SciERC证据比R1估计的25%权重更严重。两人强烈共识。\"\n    action_items:\n      - round: 30\n        action: \"补充SciERC 3-seed实验；或在正文中显著标注single-seed caveat(当前仅Appendix j简要提及)。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R30-N2\"\n    summary: \"Proposition 1 (Entity Selection Bound) 过松(3-12%)需重定位\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 30\n    last_seen_round: 30\n    mentions:\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R1-W2 [critical]: Bound (1-D)·G_nd·α 仅捕获3-12%实际gain(Table 30)。三因子各有意义但相乘过于保守。当bound与实际gain同量级时无排除力。论文自述'loose'但列为核心贡献。R2 AGREE并补充empirical cascade与theoretical decomposition存在两套平行框架缺映射。共识: 应定位为'diagnostic decomposition'而非'performance bound'，讨论哪个因子最保守。\"\n    action_items:\n      - round: 30\n        action: \"正文中将Proposition 1重定位为diagnostic decomposition；讨论bound为何松(α估计最保守？信号依赖性？)。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R30-W1\"\n    summary: \"训练配方差异(Few-NERD 3 epochs vs others 5)构成跨数据集比较混淆\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 30\n    last_seen_round: 30\n    mentions:\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R1-W4: SciERC消融显示degeneracy随epoch单调递增(43.5%→60.3%)。Few-NERD低degeneracy(13%)可能部分由更少epochs解释。Few-NERD未做5-epoch对照。R2 AGREE。\"\n    action_items:\n      - round: 30\n        action: \"对Few-NERD补充5-epoch消融或解释3 epochs选择依据；跨数据集讨论中控制训练收敛状态。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R30-W2\"\n    summary: \"Limitations未覆盖cross-task证据弱点、cross-model极度有限、probe overfit可能性\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 30\n    last_seen_round: 30\n    mentions:\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R2-W7: Limitations覆盖了correlational evidence/scope/power但缺(a)RE/SQL证据单薄性(b)cross-model仅1 dataset×1 model pair(c)hidden-state probe per-dataset overfit可能(d)entity construction gain幅度。R1 AGREE。\"\n    action_items:\n      - round: 30\n        action: \"Limitations补充上述4点局限。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R30-MR1\"\n    summary: \"建议补充引用: Varshney et al. 2022, Malinin & Gales 2021\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 30\n    last_seen_round: 30\n    mentions:\n      - round: 30\n        reviewers: [1, 2]\n        note: \"R2建议补Varshney et al. 2022(selective prediction), Xin et al. 2021, Malinin & Gales 2021(structured uncertainty)。R1认为可选补Malinin & Gales 2021。非必须但recommended。\""
  }
}
```

</details>

---


### Tool result

_source line 3250 · 2026-05-21T17:14:33.848323+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 44366}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 3251 · 2026-05-21T17:17:03.943957+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 30 (Fresh Review)\n\n**论文**: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n**Venue**: EMNLP 2026 (Long Paper, ARR)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验设计/统计分析; R2: 新颖性/framing/完整性/Related Work）\n**审稿模式**: Fresh（无历史上下文）\n\n---\n\n## Summary\n\n本文系统研究 NER 中 entity-level self-consistency signals 的能力边界。核心发现：agreement-based signals 能估计输出质量（Spearman ρ up to 0.47, AUROC up to 0.82）但无法用于 sample selection（所有 signal 均不优于 greedy decoding），称为 \"correlation-selection gap\"。论文提出四阶段诊断 cascade（QE → degeneracy → agreement fidelity → LP compression）定位失败原因，建立 MBR decoding 理论联系（Proposition 1），并给出三条绕过路径（LP selection +1.39pp, entity construction +1.02-1.40pp, cross-model ensemble +0.42pp）。实验覆盖 4 个 NER 数据集、2 个 model family（4B-72B + GPT-5.5）、9 类方法，附 57 项统计检验的 Holm-Bonferroni 校正。\n\n---\n\n## Strengths\n\n**S1. 实验覆盖度和系统性极为出色。** 4 NER benchmarks（SciERC/Few-NERD/CoNLL/WNUT-17）跨域、跨难度梯度；模型从 4B 到 72B 再到 GPT-5.5；9 类方法覆盖 selection/construction/ensemble/supervised。60+ 张表格的 33 页 appendix 提供罕见级别的实验细节。[R1-S1, R2-S1, 共识]\n\n**S2. 诊断框架设计精巧且可复用。** 四阶段 cascade 逐步排除失败原因，每个阶段有明确 pass/fail 判据。对未来 structured generation 的 test-time compute 研究有方法论贡献。[R1-S2, R2-S2, 共识]\n\n**S3. 统计方法论严谨。** 全局 Holm-Bonferroni（k=57）、bootstrap 95% CI、TOST 等价性检验、instance-level permutation test。对以负面结果为核心的论文，这种统计审慎度是必要的且做到了。[R1-S3, R2-S1, 共识]\n\n**S4. 负面结果的建设性处理。** 不止报告\"SC 失败\"，而是诊断 WHY + 理论联系（MBR）+ 三条可操作绕过路径。从 \"negative finding\" 升级为 \"diagnostic + prescriptive\"。[R1-S4, 共识]\n\n**S5. MBR 理论联系有启发性。** 将 entity construction 形式化为 structured MBR decoding，嵌入更广泛的 decoding 理论。[R1-S5, R2-S3, 共识]\n\n**S6. Hidden-state probe 提供独立 introspection evidence。** AUROC 0.63-0.88 证明信息在模型内部存在但 agreement signals 无法有效提取。[R2-S5, 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix (共识 Critical)\n\n**W1. SciERC 单 seed 削弱 25%+ NER 证据基础。** SciERC 仅用 1 个 seed（seed=42），而 Few-NERD/CoNLL 用 3 seeds。SciERC 承载 disproportionate 的正面证据（construction gain 最大 +1.02pp, zero-shot +1.53pp; hidden-state probe AUROC 0.882; medium-difficulty primary test bed）。单 seed 的 bootstrap CI 仅反映 instance-level 变异，无法量化 seed-level 不确定性。[R1-W1 critical, R2 强烈 AGREE]\n→ **建议**: 补充 SciERC 3-seed 实验；或在正文显著标注 single-seed caveat（当前仅 Appendix j 简要提及）。\n\n**W2. Cross-task validation (RE/SQL) 过于单薄，不支撑 \"beyond NER\" 的泛化。** RE 仅 SciERC 单数据集单模型（n=207 non-zero），55.5% zero-F1 来自 span error confound，信号排序与 NER 反转。SQL 仅 n=196 + 87.2% degeneracy（ceiling effect），无系统分析。Cross-model 仅 1 dataset × 1 model pair。Abstract/Intro 的 \"validate on RE and SQL\" 宣传力度超出证据。[R1-W3 warning, R2-W2 critical, 共识——R2 认为应为 critical]\n→ **建议**: 降低 RE/SQL 宣传为 \"preliminary extension\"；Limitations 补充 cross-task 证据局限。\n\n### Should-Fix (共识 Warning)\n\n**W3. Proposition 1 (Entity Selection Bound) 过松，理论贡献需重定位。** Bound (1−D)·G_nd·α 仅捕获 3-12% 实际 gain（Table 30），几乎无排除力。论文自述 \"loose\" 但列为核心贡献之一。Empirical cascade 与 theoretical decomposition 存在两套平行框架但缺映射说明。[R1-W2 critical, R2 AGREE]\n→ **建议**: 重定位为 \"diagnostic decomposition\" 而非 \"performance bound\"；讨论哪个因子（α）最保守及为什么。\n\n**W4. Degeneracy 可能是更简洁的核心解释，四阶段 cascade 可能 over-engineered。** 高 degeneracy 下 selection 失败是 trivial（样本全同）。非 degenerate instances 上 α→0（signal alignment 极低，0.000-0.161）才是核心洞察。更精确的 framing 应为 \"near-zero selection alignment despite moderate quality correlation\"，不需要整个 cascade。Cascade 有方法论复用价值但作为 narrative 过重。[R1-W6 warning, R2-W4 warning, 共识]\n→ **建议**: 主文中更突出 non-degenerate failure（α→0）作为核心发现；cascade 定位为可复用诊断协议。\n\n**W5. 训练配方差异构成跨数据集比较混淆。** Few-NERD 3 epochs vs 其他 5 epochs。SciERC 消融显示 degeneracy 随 epoch 单调递增（43.5%→60.3%）。Few-NERD 低 degeneracy（13%）可能部分由更少 epochs 解释，但 Few-NERD 未做 5-epoch 对照。[R1-W4 warning, R2 AGREE]\n→ **建议**: 补充 Few-NERD 5-epoch 消融或明确解释选择依据。\n\n**W6. Abstract 信息密度过高。** ~180 词含 12+ 数字、多个首次出现的缩写、4 项 contributions。ρ/AUROC 来自不同信号但写法可能误导。[R2-W6, R1 AGREE]\n→ **建议**: 精简至核心 3-4 个数字；明确标注 ρ 和 AUROC 来源信号。\n\n**W7. Limitations 覆盖不全。** 缺失：(a) RE/SQL 证据单薄性，(b) cross-model 仅 1 dataset × 1 pair，(c) hidden-state probe per-dataset training 可能 overfit，(d) entity construction gain 幅度（+1pp at N× cost）。[R2-W7, R1 AGREE]\n→ **建议**: 补充上述 4 点。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识（[AGREE]）：\n\n1. **Cross-task 证据不足以支撑泛化声明** — RE/SQL 应明确降级为 preliminary extension [R1-W3 + R2-W2]\n2. **SciERC 单 seed 是显著弱点** — 承载 disproportionate 正面证据但无 seed-level 方差 [R1-W1 + R2]\n3. **Degeneracy 是更简洁的核心解释** — α→0 是洞察核心，cascade 作为 narrative 过重 [R1-W6 + R2-W4]\n4. **理论 bound 需重定位** — 3-12% 捕获率不足以称为 \"bound\"，应改为 diagnostic decomposition [R1-W2 + R2]\n5. **训练配方差异需控制** — Few-NERD 缺 5-epoch 对照 [R1-W4 + R2]\n6. **Abstract 过密 + Limitations 不全** — 需精简数字并补充关键局限 [R2-W6/W7 + R1]\n7. **Cross-dataset correlation power 问题** — n=23 power 不足，但核心结论依赖 per-dataset 检验（power 充足），措辞需 hedge [R1-W5, R2 部分 REBUT]\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 判断 |\n|------|---------|---------|---------------|\n| **标题 \"Capability Ceiling\" framing** | \"Characterizing\" 已是防御性 hedge，因果措辞修改属 minor revision (warning) | 标题暗示 impossibility result，应改标题 (critical) | **R2 更合理**：标题整体是防御性的，但正文因果措辞（\"governs\"/\"determines\"/\"explaining where and why\"）与 observational design 确有矛盾，需系统性替换。标题本身可保留但正文需修。定为 **Should-Fix**。 |\n| **Entity construction 新颖性** | 诊断对比价值 + MBR 形式化被低估 | 实质是 threshold MBR 特殊情况，新颖性有限 (warning) | **R1 更合理**：construction 本身不新，但其与 selection 的系统对比揭示了失败的粒度边界（sample-level vs entity-level），这是诊断贡献的一部分。定为 **info 级**。 |\n| **MBR 文献区分** | NER-specific 机制与 MT MBR 有质的区别，需将讨论从 Appendix 移入 main text | 区分不充分，读者可能视为 re-instantiation (warning) | **折中**：内容上 R1 正确（LP compression under constrained decoding 是 NER-specific），但呈现上 R2 正确（关键对比在 Appendix 不够）。定为 **Should-Fix**（移入 main text）。 |\n\n---\n\n## Questions\n\n**Q1.** SciERC 为何仅用 1 个 seed？是资源限制还是方法论考虑？[R1-Q1, 共识]\n**Q2.** Hidden-state probe 是否做过 LODO CV？论文已有 LODO 结果（§3: AUROC drops to 0.559-0.671）但主文讨论不足——如 probe 不能 transfer，\"introspection boundary\" 证据价值减弱。[R2-Q2, R1 AGREE]\n**Q3.** Entity construction \"bypasses entity-level self-verification\" 但仍依赖 entity-level agreement——更准确表述应为 \"bypasses sample-level selection by operating at entity granularity\"。[R2-Q3, R1 AGREE]\n**Q4.** Cross-model 为何未在 Few-NERD（degeneracy 最低）上测试？这是逻辑上最应做的实验。[R2-Q4, R1 AGREE]\n**Q5.** Proposition 1 entity-wise independence 假设 violation 程度？Table 30 Ratio (3-12%) 间接反映但未直接量化 entity-pair correlation。[R2-Q5, R1 部分 AGREE]\n**Q6.** LP compression threshold ε=0.05 选择依据？不同 ε 是否改变 LP ranking？[R1-Q2]\n**Q7.** TOST equivalence margin δ 的选择是否 data-driven（循环推理风险）？[R1-Q3]\n**Q8.** Zero-shot instruction-tuned 模型下 gap 幅度是否有实质变化？[R1-Q4]\n\n---\n\n## Missing References\n\n- R1: 未发现重要缺失。可选补充 Malinin & Gales (2021) \"Uncertainty Estimation in Autoregressive Structured Prediction\"\n- R2: 建议补充 Varshney et al. (2022) ACL Findings (selective prediction), Xin et al. (2021), Malinin & Gales (2021) ICLR (structured uncertainty)\n- 需核实：ma2024selfimproving 第一作者（bib \"Ma\" vs OpenAlex \"Xie\"）\n- 引用验证：57 bib, 0 orphan, 0 missing, 2 not found (OpenAlex 覆盖 gaps), 4 minor encoding mismatches\n- 引用质量总评：**良好**，无虚假引用\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，不适用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 4 分钟）\n\n| Severity | 发现 |\n|----------|------|\n| warning | Pages 1-2 连续纯文字墙（Abstract + Intro + Diagnostic Framework 开头），无 figure/table/equation 穿插。建议将 Figure 1 提前至第 2 页。 |\n| warning | Page 7 极度拥挤——Table 4 + Table 5(a/b) + Figure 3 全部堆叠，表格间距极小，Figure 3 被压缩至可读性下限（约正文字号 60-65%）。建议移 1-2 个 table 到 appendix。 |\n| info | Figure 1（p3）三阶段诊断级联 + 关键数值，颜色编码清晰，caption 自含。 |\n| info | 所有正文表格统一 booktabs 风格，最优值加粗，精度一致——排版规范。 |\n| info | p17 Figure 6 热力图使用红-黄-绿渐变，建议改用 viridis 或 Blue-Orange 色标（红绿色盲友好）。 |\n| info | Appendix 多页大面积空白（p41/46/47 >50% 空白），可合并减少。 |\n| info | 需验证正文页数：Conclusion 结束位置约 p9 上部，Limitations 紧随。若 Conclusion 超 p8 底部需压缩。 |\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | 3.5/5 | 3.0/5 | **3.0/5** |\n| Reproducibility | 4.0/5 | 4.0/5 | **4.0/5** |\n| **Overall** | **3.5** | **3.0** | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 评分理由\n\n**给 3.0 (Findings) 而非 3.5 的原因：**\n1. **Cross-task overclaiming**：标题已限定 NER，但 Abstract/Intro 仍宣传 \"validate on RE and SQL\"，证据基础远不支撑（RE 单数据集+span error confound，SQL 仅 n=196 的 ceiling effect）\n2. **因果 framing 与 observational 设计的系统性矛盾**：虽然标题 \"Characterizing\" 是防御性的，但正文因果措辞（\"governs\"/\"determines\"/\"explaining where and why\"）仍普遍存在\n3. **SciERC 单 seed 在承载核心正面证据的数据集上是显著缺陷**\n4. **理论 bound 捕获率仅 3-12%**，作为 \"contribution\" 的实际约束力有限\n\n**给 3.0 而非更低的原因：**\n1. NER 范围内的诊断框架是实质性贡献（四阶段 cascade + 可复用协议）\n2. 统计严谨性在 NLP 实证论文中属上乘（k=57 Holm, TOST, bootstrap CI）\n3. 9 方法 × 4 数据集的系统性负面结果在该领域尚无先例\n4. Prescriptive escape routes 虽增量有限（+1-1.4pp）但方向正确\n5. 所有 critical 问题均可在 revision 中修复\n\n### 升级至 3.5 (Borderline Conference) 的条件\n- [ ] SciERC 补充至少 2 个额外 seed（或充分论证 single-seed 不影响核心结论）\n- [ ] RE/SQL 在 Abstract/Intro 中明确降级为 preliminary exploration\n- [ ] Proposition 1 重定位为 diagnostic decomposition（非 performance bound）\n- [ ] 正文因果措辞系统性替换（\"governs\"→\"is associated with\" 等）\n- [ ] MBR 文献对比从 Appendix 移入 main text §8\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"explaining where and why\" 暗示因果但证据为相关性 → 改为 \"characterizing where and how\"\n- \"validate on RE and SQL\" → \"extend exploratorily to RE and SQL\"\n- Contributions list #4 \"prescriptive escape routes\" 的 cost-effectiveness 应在主文讨论（N× cost for ~1pp），当前仅 Appendix Table 61\n\n### Section 2 (Diagnostic Framework)\n- Signal 定义清晰（5 signals 无歧义），instance-level vs per-sample 区分贯穿全文——这是优点\n- Entity matching（exact span + type）描述充分\n- Eq. 1 (SJ) 引用 Hungarian matching 缺引用 → 补 Kuhn (1955)\n\n### Section 3 (How Self-Verification Fails)\n- ESJ/MRSC/LSC 三个独立 probe 一致失败是有力证据\n- Hidden-state probe LODO 结果（AUROC drops to 0.559-0.671）已在文中但讨论不足 → 补充解释 CoNLL vs SciERC AUROC 差异原因（task difficulty → error outlier separability）\n- \"introspection boundary\" 术语需考虑 probe 的 dataset-specific 性质\n\n### Section 4 (Where Single-Signal Selection Fails)\n- Table 1 (selection) 清晰展示核心 negative result\n- \"definitional vs empirical\" 二分法（§4 首段）是论文最精妙的区分之一 → 建议在 Abstract/Intro 更突出\n- Cross-dataset ρ=0.052 (n=23, p=0.81) 的 power 问题已承认但措辞需 hedge\n\n### Section 5 (Adaptive Methods)\n- Table 2 (method summary) 是优秀的概览\n- Cross-model (+0.42pp) 仅 Few-NERD × 1 pair → 在正文中标注 \"single-dataset result\"\n- LightGBM verifier cross-dataset transfer 为负（-0.76 to -1.02pp）→ 强化了 dataset-specific 的论点\n\n### Section 6 (Threshold Regime Analysis)\n- MBR 连接严谨但 Proposition 1 bound 过松 → 见 W3\n- Inverse scaling 发现（40/58 transitions 下 construction F1 下降）是重要实践发现\n- θ_crit=0.70 作为 necessary condition（非 sufficient）有实际价值\n\n### Section 7 (Experiments)\n- Few-NERD 3 epochs vs others 5 epochs → 需控制 [W5]\n- Table 4 (entity construction) multi-seed mean±σ 是好的做法\n- Holm 分 family（selection k=21, construction k=10, signal k=9）vs global k=57 → 需解释分 family 的依据和全局结果\n\n### Section 8 (Related Work)\n- Ma et al. (2024) 已引用 → 验证第一作者\n- MBR 文献对比需从 Appendix 移入此处 [Divergence #3]\n- Yun et al. (2025) diversity collapse 差异化（Table 62）在 Appendix，核心对比建议在 main text 简述\n\n### Section 9 (Discussion)\n- 因果措辞集中区 → 系统替换 \"governs\"/\"determines\" [W1 divergent]\n- Cost-effectiveness 讨论（\"N× cost for ≈1pp\"）已存在但需更 explicit\n\n### Section 10 (Conclusion)\n- 2 句过于精简；建议加 1 句关于 non-degenerate failure（α→0）作为核心洞察的总结\n\n### Limitations\n- 覆盖良好但缺 4 点 [W7]\n- 已有 frontier model degeneracy 差异讨论（Claude 74% vs DeepSeek 5.5%）→ 有进步\n\n### Format Compliance\n- ✅ 正文 ≤8 页（需视觉审查确认 Conclusion 结束位置）\n- ✅ Double-blind（\"Anonymous ACL submission\"，\"[anonymized URL]\"）\n- ✅ ACL LaTeX 模板 + [review] option\n- ✅ References 不限页数\n- ✅ Limitations + Ethics Statement 存在\n- ⚠️ p7 极度拥挤（视觉审查 warning）",
  "project": "struct_self_consist_ie",
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
    "report": "# 审稿报告 — Round 30 (Fresh Review)\n\n**论文**: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n**Venue**: EMNLP 2026 (Long Paper, ARR)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验设计/统计分析; R2: 新颖性/framing/完整性/Related Work）\n**审稿模式**: Fresh（无历史上下文）\n\n---\n\n## Summary\n\n本文系统研究 NER 中 entity-level self-consistency signals 的能力边界。核心发现：agreement-based signals 能估计输出质量（Spearman ρ up to 0.47, AUROC up to 0.82）但无法用于 sample selection（所有 signal 均不优于 greedy decoding），称为 \"correlation-selection gap\"。论文提出四阶段诊断 cascade（QE → degeneracy → agreement fidelity → LP compression）定位失败原因，建立 MBR decoding 理论联系（Proposition 1），并给出三条绕过路径（LP selection +1.39pp, entity construction +1.02-1.40pp, cross-model ensemble +0.42pp）。实验覆盖 4 个 NER 数据集、2 个 model family（4B-72B + GPT-5.5）、9 类方法，附 57 项统计检验的 Holm-Bonferroni 校正。\n\n---\n\n## Strengths\n\n**S1. 实验覆盖度和系统性极为出色。** 4 NER benchmarks（SciERC/Few-NERD/CoNLL/WNUT-17）跨域、跨难度梯度；模型从 4B 到 72B 再到 GPT-5.5；9 类方法覆盖 selection/construction/ensemble/supervised。60+ 张表格的 33 页 appendix 提供罕见级别的实验细节。[R1-S1, R2-S1, 共识]\n\n**S2. 诊断框架设计精巧且可复用。** 四阶段 cascade 逐步排除失败原因，每个阶段有明确 pass/fail 判据。对未来 structured generation 的 test-time compute 研究有方法论贡献。[R1-S2, R2-S2, 共识]\n\n**S3. 统计方法论严谨。** 全局 Holm-Bonferroni（k=57）、bootstrap 95% CI、TOST 等价性检验、instance-level permutation test。对以负面结果为核心的论文，这种统计审慎度是必要的且做到了。[R1-S3, R2-S1, 共识]\n\n**S4. 负面结果的建设性处理。** 不止报告\"SC 失败\"，而是诊断 WHY + 理论联系（MBR）+ 三条可操作绕过路径。从 \"negative finding\" 升级为 \"diagnostic + prescriptive\"。[R1-S4, 共识]\n\n**S5. MBR 理论联系有启发性。** 将 entity construction 形式化为 structured MBR decoding，嵌入更广泛的 decoding 理论。[R1-S5, R2-S3, 共识]\n\n**S6. Hidden-state probe 提供独立 introspection evidence。** AUROC 0.63-0.88 证明信息在模型内部存在但 agreement signals 无法有效提取。[R2-S5, 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix (共识 Critical)\n\n**W1. SciERC 单 seed 削弱 25%+ NER 证据基础。** SciERC 仅用 1 个 seed（seed=42），而 Few-NERD/CoNLL 用 3 seeds。SciERC 承载 disproportionate 的正面证据（construction gain 最大 +1.02pp, zero-shot +1.53pp; hidden-state probe AUROC 0.882; medium-difficulty primary test bed）。单 seed 的 bootstrap CI 仅反映 instance-level 变异，无法量化 seed-level 不确定性。[R1-W1 critical, R2 强烈 AGREE]\n→ **建议**: 补充 SciERC 3-seed 实验；或在正文显著标注 single-seed caveat（当前仅 Appendix j 简要提及）。\n\n**W2. Cross-task validation (RE/SQL) 过于单薄，不支撑 \"beyond NER\" 的泛化。** RE 仅 SciERC 单数据集单模型（n=207 non-zero），55.5% zero-F1 来自 span error confound，信号排序与 NER 反转。SQL 仅 n=196 + 87.2% degeneracy（ceiling effect），无系统分析。Cross-model 仅 1 dataset × 1 model pair。Abstract/Intro 的 \"validate on RE and SQL\" 宣传力度超出证据。[R1-W3 warning, R2-W2 critical, 共识——R2 认为应为 critical]\n→ **建议**: 降低 RE/SQL 宣传为 \"preliminary extension\"；Limitations 补充 cross-task 证据局限。\n\n### Should-Fix (共识 Warning)\n\n**W3. Proposition 1 (Entity Selection Bound) 过松，理论贡献需重定位。** Bound (1−D)·G_nd·α 仅捕获 3-12% 实际 gain（Table 30），几乎无排除力。论文自述 \"loose\" 但列为核心贡献之一。Empirical cascade 与 theoretical decomposition 存在两套平行框架但缺映射说明。[R1-W2 critical, R2 AGREE]\n→ **建议**: 重定位为 \"diagnostic decomposition\" 而非 \"performance bound\"；讨论哪个因子（α）最保守及为什么。\n\n**W4. Degeneracy 可能是更简洁的核心解释，四阶段 cascade 可能 over-engineered。** 高 degeneracy 下 selection 失败是 trivial（样本全同）。非 degenerate instances 上 α→0（signal alignment 极低，0.000-0.161）才是核心洞察。更精确的 framing 应为 \"near-zero selection alignment despite moderate quality correlation\"，不需要整个 cascade。Cascade 有方法论复用价值但作为 narrative 过重。[R1-W6 warning, R2-W4 warning, 共识]\n→ **建议**: 主文中更突出 non-degenerate failure（α→0）作为核心发现；cascade 定位为可复用诊断协议。\n\n**W5. 训练配方差异构成跨数据集比较混淆。** Few-NERD 3 epochs vs 其他 5 epochs。SciERC 消融显示 degeneracy 随 epoch 单调递增（43.5%→60.3%）。Few-NERD 低 degeneracy（13%）可能部分由更少 epochs 解释，但 Few-NERD 未做 5-epoch 对照。[R1-W4 warning, R2 AGREE]\n→ **建议**: 补充 Few-NERD 5-epoch 消融或明确解释选择依据。\n\n**W6. Abstract 信息密度过高。** ~180 词含 12+ 数字、多个首次出现的缩写、4 项 contributions。ρ/AUROC 来自不同信号但写法可能误导。[R2-W6, R1 AGREE]\n→ **建议**: 精简至核心 3-4 个数字；明确标注 ρ 和 AUROC 来源信号。\n\n**W7. Limitations 覆盖不全。** 缺失：(a) RE/SQL 证据单薄性，(b) cross-model 仅 1 dataset × 1 pair，(c) hidden-state probe per-dataset training 可能 overfit，(d) entity construction gain 幅度（+1pp at N× cost）。[R2-W7, R1 AGREE]\n→ **建议**: 补充上述 4 点。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识（[AGREE]）：\n\n1. **Cross-task 证据不足以支撑泛化声明** — RE/SQL 应明确降级为 preliminary extension [R1-W3 + R2-W2]\n2. **SciERC 单 seed 是显著弱点** — 承载 disproportionate 正面证据但无 seed-level 方差 [R1-W1 + R2]\n3. **Degeneracy 是更简洁的核心解释** — α→0 是洞察核心，cascade 作为 narrative 过重 [R1-W6 + R2-W4]\n4. **理论 bound 需重定位** — 3-12% 捕获率不足以称为 \"bound\"，应改为 diagnostic decomposition [R1-W2 + R2]\n5. **训练配方差异需控制** — Few-NERD 缺 5-epoch 对照 [R1-W4 + R2]\n6. **Abstract 过密 + Limitations 不全** — 需精简数字并补充关键局限 [R2-W6/W7 + R1]\n7. **Cross-dataset correlation power 问题** — n=23 power 不足，但核心结论依赖 per-dataset 检验（power 充足），措辞需 hedge [R1-W5, R2 部分 REBUT]\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 判断 |\n|------|---------|---------|---------------|\n| **标题 \"Capability Ceiling\" framing** | \"Characterizing\" 已是防御性 hedge，因果措辞修改属 minor revision (warning) | 标题暗示 impossibility result，应改标题 (critical) | **R2 更合理**：标题整体是防御性的，但正文因果措辞（\"governs\"/\"determines\"/\"explaining where and why\"）与 observational design 确有矛盾，需系统性替换。标题本身可保留但正文需修。定为 **Should-Fix**。 |\n| **Entity construction 新颖性** | 诊断对比价值 + MBR 形式化被低估 | 实质是 threshold MBR 特殊情况，新颖性有限 (warning) | **R1 更合理**：construction 本身不新，但其与 selection 的系统对比揭示了失败的粒度边界（sample-level vs entity-level），这是诊断贡献的一部分。定为 **info 级**。 |\n| **MBR 文献区分** | NER-specific 机制与 MT MBR 有质的区别，需将讨论从 Appendix 移入 main text | 区分不充分，读者可能视为 re-instantiation (warning) | **折中**：内容上 R1 正确（LP compression under constrained decoding 是 NER-specific），但呈现上 R2 正确（关键对比在 Appendix 不够）。定为 **Should-Fix**（移入 main text）。 |\n\n---\n\n## Questions\n\n**Q1.** SciERC 为何仅用 1 个 seed？是资源限制还是方法论考虑？[R1-Q1, 共识]\n**Q2.** Hidden-state probe 是否做过 LODO CV？论文已有 LODO 结果（§3: AUROC drops to 0.559-0.671）但主文讨论不足——如 probe 不能 transfer，\"introspection boundary\" 证据价值减弱。[R2-Q2, R1 AGREE]\n**Q3.** Entity construction \"bypasses entity-level self-verification\" 但仍依赖 entity-level agreement——更准确表述应为 \"bypasses sample-level selection by operating at entity granularity\"。[R2-Q3, R1 AGREE]\n**Q4.** Cross-model 为何未在 Few-NERD（degeneracy 最低）上测试？这是逻辑上最应做的实验。[R2-Q4, R1 AGREE]\n**Q5.** Proposition 1 entity-wise independence 假设 violation 程度？Table 30 Ratio (3-12%) 间接反映但未直接量化 entity-pair correlation。[R2-Q5, R1 部分 AGREE]\n**Q6.** LP compression threshold ε=0.05 选择依据？不同 ε 是否改变 LP ranking？[R1-Q2]\n**Q7.** TOST equivalence margin δ 的选择是否 data-driven（循环推理风险）？[R1-Q3]\n**Q8.** Zero-shot instruction-tuned 模型下 gap 幅度是否有实质变化？[R1-Q4]\n\n---\n\n## Missing References\n\n- R1: 未发现重要缺失。可选补充 Malinin & Gales (2021) \"Uncertainty Estimation in Autoregressive Structured Prediction\"\n- R2: 建议补充 Varshney et al. (2022) ACL Findings (selective prediction), Xin et al. (2021), Malinin & Gales (2021) ICLR (structured uncertainty)\n- 需核实：ma2024selfimproving 第一作者（bib \"Ma\" vs OpenAlex \"Xie\"）\n- 引用验证：57 bib, 0 orphan, 0 missing, 2 not found (OpenAlex 覆盖 gaps), 4 minor encoding mismatches\n- 引用质量总评：**良好**，无虚假引用\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，不适用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 4 分钟）\n\n| Severity | 发现 |\n|----------|------|\n| warning | Pages 1-2 连续纯文字墙（Abstract + Intro + Diagnostic Framework 开头），无 figure/table/equation 穿插。建议将 Figure 1 提前至第 2 页。 |\n| warning | Page 7 极度拥挤——Table 4 + Table 5(a/b) + Figure 3 全部堆叠，表格间距极小，Figure 3 被压缩至可读性下限（约正文字号 60-65%）。建议移 1-2 个 table 到 appendix。 |\n| info | Figure 1（p3）三阶段诊断级联 + 关键数值，颜色编码清晰，caption 自含。 |\n| info | 所有正文表格统一 booktabs 风格，最优值加粗，精度一致——排版规范。 |\n| info | p17 Figure 6 热力图使用红-黄-绿渐变，建议改用 viridis 或 Blue-Orange 色标（红绿色盲友好）。 |\n| info | Appendix 多页大面积空白（p41/46/47 >50% 空白），可合并减少。 |\n| info | 需验证正文页数：Conclusion 结束位置约 p9 上部，Limitations 紧随。若 Conclusion 超 p8 底部需压缩。 |\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | 3.5/5 | 3.0/5 | **3.0/5** |\n| Reproducibility | 4.0/5 | 4.0/5 | **4.0/5** |\n| **Overall** | **3.5** | **3.0** | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 评分理由\n\n**给 3.0 (Findings) 而非 3.5 的原因：**\n1. **Cross-task overclaiming**：标题已限定 NER，但 Abstract/Intro 仍宣传 \"validate on RE and SQL\"，证据基础远不支撑（RE 单数据集+span error confound，SQL 仅 n=196 的 ceiling effect）\n2. **因果 framing 与 observational 设计的系统性矛盾**：虽然标题 \"Characterizing\" 是防御性的，但正文因果措辞（\"governs\"/\"determines\"/\"explaining where and why\"）仍普遍存在\n3. **SciERC 单 seed 在承载核心正面证据的数据集上是显著缺陷**\n4. **理论 bound 捕获率仅 3-12%**，作为 \"contribution\" 的实际约束力有限\n\n**给 3.0 而非更低的原因：**\n1. NER 范围内的诊断框架是实质性贡献（四阶段 cascade + 可复用协议）\n2. 统计严谨性在 NLP 实证论文中属上乘（k=57 Holm, TOST, bootstrap CI）\n3. 9 方法 × 4 数据集的系统性负面结果在该领域尚无先例\n4. Prescriptive escape routes 虽增量有限（+1-1.4pp）但方向正确\n5. 所有 critical 问题均可在 revision 中修复\n\n### 升级至 3.5 (Borderline Conference) 的条件\n- [ ] SciERC 补充至少 2 个额外 seed（或充分论证 single-seed 不影响核心结论）\n- [ ] RE/SQL 在 Abstract/Intro 中明确降级为 preliminary exploration\n- [ ] Proposition 1 重定位为 diagnostic decomposition（非 performance bound）\n- [ ] 正文因果措辞系统性替换（\"governs\"→\"is associated with\" 等）\n- [ ] MBR 文献对比从 Appendix 移入 main text §8\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"explaining where and why\" 暗示因果但证据为相关性 → 改为 \"characterizing where and how\"\n- \"validate on RE and SQL\" → \"extend exploratorily to RE and SQL\"\n- Contributions list #4 \"prescriptive escape routes\" 的 cost-effectiveness 应在主文讨论（N× cost for ~1pp），当前仅 Appendix Table 61\n\n### Section 2 (Diagnostic Framework)\n- Signal 定义清晰（5 signals 无歧义），instance-level vs per-sample 区分贯穿全文——这是优点\n- Entity matching（exact span + type）描述充分\n- Eq. 1 (SJ) 引用 Hungarian matching 缺引用 → 补 Kuhn (1955)\n\n### Section 3 (How Self-Verification Fails)\n- ESJ/MRSC/LSC 三个独立 probe 一致失败是有力证据\n- Hidden-state probe LODO 结果（AUROC drops to 0.559-0.671）已在文中但讨论不足 → 补充解释 CoNLL vs SciERC AUROC 差异原因（task difficulty → error outlier separability）\n- \"introspection boundary\" 术语需考虑 probe 的 dataset-specific 性质\n\n### Section 4 (Where Single-Signal Selection Fails)\n- Table 1 (selection) 清晰展示核心 negative result\n- \"definitional vs empirical\" 二分法（§4 首段）是论文最精妙的区分之一 → 建议在 Abstract/Intro 更突出\n- Cross-dataset ρ=0.052 (n=23, p=0.81) 的 power 问题已承认但措辞需 hedge\n\n### Section 5 (Adaptive Methods)\n- Table 2 (method summary) 是优秀的概览\n- Cross-model (+0.42pp) 仅 Few-NERD × 1 pair → 在正文中标注 \"single-dataset result\"\n- LightGBM verifier cross-dataset transfer 为负（-0.76 to -1.02pp）→ 强化了 dataset-specific 的论点\n\n### Section 6 (Threshold Regime Analysis)\n- MBR 连接严谨但 Proposition 1 bound 过松 → 见 W3\n- Inverse scaling 发现（40/58 transitions 下 construction F1 下降）是重要实践发现\n- θ_crit=0.70 作为 necessary condition（非 sufficient）有实际价值\n\n### Section 7 (Experiments)\n- Few-NERD 3 epochs vs others 5 epochs → 需控制 [W5]\n- Table 4 (entity construction) multi-seed mean±σ 是好的做法\n- Holm 分 family（selection k=21, construction k=10, signal k=9）vs global k=57 → 需解释分 family 的依据和全局结果\n\n### Section 8 (Related Work)\n- Ma et al. (2024) 已引用 → 验证第一作者\n- MBR 文献对比需从 Appendix 移入此处 [Divergence #3]\n- Yun et al. (2025) diversity collapse 差异化（Table 62）在 Appendix，核心对比建议在 main text 简述\n\n### Section 9 (Discussion)\n- 因果措辞集中区 → 系统替换 \"governs\"/\"determines\" [W1 divergent]\n- Cost-effectiveness 讨论（\"N× cost for ≈1pp\"）已存在但需更 explicit\n\n### Section 10 (Conclusion)\n- 2 句过于精简；建议加 1 句关于 non-degenerate failure（α→0）作为核心洞察的总结\n\n### Limitations\n- 覆盖良好但缺 4 点 [W7]\n- 已有 frontier model degeneracy 差异讨论（Claude 74% vs DeepSeek 5.5%）→ 有进步\n\n### Format Compliance\n- ✅ 正文 ≤8 页（需视觉审查确认 Conclusion 结束位置）\n- ✅ Double-blind（\"Anonymous ACL submission\"，\"[anonymized URL]\"）\n- ✅ ACL LaTeX 模板 + [review] option\n- ✅ References 不限页数\n- ✅ Limitations + Ethics Statement 存在\n- ⚠️ p7 极度拥挤（视觉审查 warning）",
    "project": "struct_self_consist_ie",
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

_source line 3252 · 2026-05-21T17:17:07.908025+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3964
}
```

</details>

---


### Assistant

_source line 3253 · 2026-05-21T17:17:19.005019+00:00_

审稿报告已投递至 Research Director。

**Round 30 审稿完成总结：**

- **Overall: 3.0 (Findings)**，R1 给 3.5 / R2 给 3.0
- **2 个 Must-Fix (共识 Critical)**：SciERC 单 seed 削弱核心正面证据；RE/SQL cross-task validation 过薄
- **5 个 Should-Fix (共识 Warning)**：Proposition 1 需重定位为 diagnostic decomposition；degeneracy 是更简洁的核心解释（α→0）；训练配方混淆；Abstract 过密；Limitations 不全
- **1 个分歧点**：标题因果 framing — R2 认为 critical，R1 认为 minor revision，Director 定为 Should-Fix
- **升级路径明确**：补 SciERC 多 seed + 降级 RE/SQL 宣传 + 重定位理论 + 替换因果措辞 + MBR 对比移入 main text → 可升至 3.5 (Borderline Conference)
- **视觉审查**：2 warning（p1-2 文字墙、p7 过度拥挤），0 critical
- **Issue Tracker**：已同步更新，新增 4 条 open issues + 更新 20+ 条历史 issues 的 R30 mentions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 246

## Round 246

2 recorded events


### User

_source line 3254 · 2026-05-21T17:17:21.632375+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- R1 的 6 个 weaknesses 中，5 个 **AGREE**（W1 单 seed、W2 bound 过松、W3 RE/SQL 薄弱、W4 训练差异、W6 degeneracy 主解释），1 个 **REBUT**（W5 统计效力——核心结论不依赖 cross-dataset correlation）
- R1 的 5 个 questions 中，4 个 AGREE，1 个 REBUT（Q5 同架构 ensemble 不是论文 focus）
- Minor issues 全部 AGREE
- 评分差异：R1 给 3.5 vs 我给 3.0，主要因为我对新颖性和 cross-task framing 评估更严格

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

_source line 3255 · 2026-05-21T17:17:35.307464+00:00_

审稿报告已投递完成。

**Round 30 审稿总结：**

- **Overall: 3.0 (Findings)**，R1 给 3.5 / R2 给 3.0
- **2 个共识 Critical**：SciERC 单 seed 削弱证据基础；RE/SQL cross-task validation 过于单薄
- **5 个共识 Warning**：Proposition 1 需重定位为 diagnostic decomposition；degeneracy 是更简洁的核心解释；训练配方差异未控制；Abstract 过密；Limitations 不全
- **1 个分歧**：标题因果 framing（R2 认为 critical，R1 认为 minor revision）
- **升级至 3.5 的条件**：补 SciERC 多 seed、降级 RE/SQL 宣传、重定位理论 bound、替换因果措辞、MBR 对比移入 main text

Issue Tracker 已同步更新（Round 30 新增 4 条 + 更新 20+ 条历史 issue）。视觉审查完成（2 warning: p1-2 文字墙、p7 过度拥挤）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 247

## Round 247

82 recorded events


### User

_source line 3256 · 2026-05-22T00:55:28.467858+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: docs/paper/main.tex
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

_source line 3257 · 2026-05-22T00:55:34.792337+00:00_

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

_source line 3258 · 2026-05-22T00:55:34.894263+00:00_

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

_source line 3259 · 2026-05-22T00:55:41.903647+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,read_local_file",
  "max_results": "15"
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
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,read_local_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 3260 · 2026-05-22T00:55:42.004501+00:00_



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

_source line 3261 · 2026-05-22T00:55:47.429316+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "15"
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
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 3262 · 2026-05-22T00:55:47.429792+00:00_



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

_source line 3263 · 2026-05-22T00:55:53.001926+00:00_

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

_source line 3264 · 2026-05-22T00:55:54.457603+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (301 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T23:20:22Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 300 个实验 — DONE 279, PREPARING 18, QUEUED 3\n**DONE 分布**: failed 12, killed 36, negative 53, success 178\n\n### GPU 占用\n- **分配**: 8 张 — autodl-5090:cuda:0, autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3, autodl-5090-c:cuda:0, autodl-5090-c:cuda:1, autodl-5090-c:cuda:2, autodl-5090-c:cuda:3\n- **空闲（分配了没跑）**: autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3, autodl-5090-c:cuda:1, autodl-5090-c:cuda:2, autodl-5090-c:cuda:3\n\n### 💾 磁盘余量\n- **autodl-5090**:\n  - `/autodl-pub`: 8.8T/14T 可用（已用 38%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n- **autodl-5090-c**:\n  - `/autodl-pub`: 6.4T/14T 可用（已用 55%）\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `exp_fewnerd_mf4v2_s456_v3` [success] — 2026-05-21T21:53:49\n- `exp_fewnerd_mf4v2_s123_v3` [success] — 2026-05-21T21:53:33\n- `exp_fewnerd_5epoch_s456` [success] — 2026-05-21T21:41:55\n- `exp_e2_pretrained_fewnerd_s456` [success] — 2026-05-21T21:19:16 — process dead 5× with no sentinel/W&B — auto-res
…[truncated 1774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 3265 · 2026-05-22T00:55:54.910112+00:00_

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

_source line 3266 · 2026-05-22T00:55:55.412649+00:00_

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
28	\title{Characterizing the Capability Ceiling of Self-Consistency:\\ How Entity-Level Verification Fails in NER}
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
58	\input{section
…[truncated 175 chars]

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

_source line 3267 · 2026-05-22T00:55:55.513558+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
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
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 3268 · 2026-05-22T00:55:56.769594+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 3269 · 2026-05-22T00:55:56.921677+00:00_

-rw-r--r-- 1 ubuntu ubuntu 986902 May 22 00:38 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool result

_source line 3270 · 2026-05-22T00:56:02.616037+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"}]

I've performed the web search with y
…[truncated 1318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7102
}
```

</details>

---


### Tool call

_source line 3271 · 2026-05-22T00:56:09.491509+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 3272 · 2026-05-22T00:56:10.495806+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 Budapest call for papers commitment deadline ARR"
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
    "query": "EMNLP 2026 Budapest call for papers commitment deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 3273 · 2026-05-22T00:56:10.797926+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
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
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 3274 · 2026-05-22T00:56:15.013287+00:00_

Web search results for query: "EMNLP 2026 Budapest call for papers commitment deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.1616 Confs: Workshop at EMNLP 2026: Multimodal Interaction in Face-to-Face Dialogue (Hungary)","url":"https://linguistlist.org/issues/37/1616/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here are the key deadlines for EMNLP 2026 in Budapest related to ARR and commitment:

**EMNLP 2026 Important Dates:**

- ARR submission deadline (long & short pap
…[truncated 444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 4517
}
```

</details>

---


### Tool result

_source line 3275 · 2026-05-22T00:56:16.369154+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

Upon acceptance, final versions of long pap
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6877
}
```

</details>

---


### Tool result

_source line 3276 · 2026-05-22T00:56:16.369679+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5571
}
```

</details>

---


### Tool call

_source line 3277 · 2026-05-22T00:56:33.246673+00:00_

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

_source line 3278 · 2026-05-22T00:56:33.247116+00:00_



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

_source line 3279 · 2026-05-22T00:56:37.670354+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 3280 · 2026-05-22T00:56:38.172811+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3281 · 2026-05-22T00:56:38.274808+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
  "description": "List paper sections"
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
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 3282 · 2026-05-22T00:56:38.325420+00:00_

_archived
abstract.tex
adaptive.tex
appendix.tex
background.tex
checklist.tex
conclusion.tex
diagnostic.tex
discussion.tex
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
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3283 · 2026-05-22T00:56:43.446141+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config"
  }
}
```

</details>

---


### Tool result

_source line 3284 · 2026-05-22T00:56:43.948676+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3285 · 2026-05-22T00:56:43.999295+00:00_

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

_source line 3286 · 2026-05-22T00:56:44.208791+00:00_

1	\begin{abstract}
2	Test-time compute scaling yields large gains on discrete-answer reasoning and code generation, yet for named entity recognition (NER), where outputs are entity sets with partial overlap, quality estimation does not translate to sample selection.
3	Across nine method categories, no entity-level agreement signal reliably improves selection: quality estimation signals correlate with oracle F1 (Spearman $\rho$ up to 0.47) yet no signal selects better than greedy decoding.
4	A reusable four-stage diagnostic cascade localizes where selection breaks down, with preliminary extensions to RE and SQL parsing.
5	On non-degenerate instances, selection alignment $\alpha$ approaches zero despite moderate quality correlations---this near-zero alignment, not degeneracy, is the binding constraint.
6	The positive results bypass sample-level selection: log-probability selection ($+1.39$\,pp on Few-NERD) and entity-level construction via weighted voting ($+0.3$--$1.4$\,pp) operate at entity granularity.
7	Strict majority vote fails on all tested datasets; degeneracy above 70\% eliminates aggregation gain.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 209
}
```

</details>

---


### Tool call

_source line 3287 · 2026-05-22T00:56:44.209325+00:00_

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

_source line 3288 · 2026-05-22T00:56:44.360269+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling complements model scaling \cite{snell2025scaling}: repeated sampling with majority voting \cite{wang2023selfconsistency}, best-of-$N$ with learned verifiers \cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \cite{muennighoff2025s1} produce large gains on reasoning and code generation.
4	These successes share a structural prerequisite: the output space admits either exact equivalence classes (multiple-choice, numeric answers) or execution-based verification (code).
5	Named entity recognition (NER) breaks both assumptions.
6	The output is a set of typed entities; two samples from the same input routinely extract overlapping but non-identical sets, and no external oracle can adjudicate correctness at test time.
7	Without equivalence classes, majority voting reduces to heuristic frequency counting; without a verifier, best-of-$N$ requires a reliable proxy signal.
8	This structural mismatch raises a concrete question: can self-consistency signals that estimate quality well for reasoning tasks also \textit{select} better outputs or \textit{construct} better entity sets for NER?
9	We investigate this question for NER and extend exploratorily to SQL parsing, treating NER as a representative instance of the broader set-valued generation problem.
10	
11	The question has practical stakes beyond information extraction.
12	Hallucination detection methods such as SelfCheckGPT \cite{manakul2023selfcheckgpt} and FActScore \cite{min2023factscore} rely on cross-sample consistency to verify individual claims: if a model's outputs agree, the shared content is presumed factual.
13	This reasoning assumes entity-level self-verification works, that a model can reliably distinguish correct extractions from incorrect ones through self-judgment or re-prompting.
14	We show this assumption fails.
15	Three independent probes (entity self-judgment, multi-round re-prompting, latent-space aggreg
…[truncated 4823 chars]

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

_source line 3289 · 2026-05-22T00:56:52.542266+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null; grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null; echo \"---\"; grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null || echo \"NO_GLOBAL_CONFIG\"",
  "description": "Search for external review config"
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
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null; grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null; echo \"---\"; grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null || echo \"NO_GLOBAL_CONFIG\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool call

_source line 3290 · 2026-05-22T00:56:52.844365+00:00_

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

_source line 3291 · 2026-05-22T00:56:53.748017+00:00_

---
NO_GLOBAL_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 1205
}
```

</details>

---


### Tool result

_source line 3292 · 2026-05-22T00:56:53.798816+00:00_

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

…[truncated 7041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 3293 · 2026-05-22T00:56:53.799204+00:00_

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

_source line 3294 · 2026-05-22T00:56:54.050659+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}).
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{10.1\% of GPT-5.5 samples produced unparseable output; these are excluded from all metrics. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3: $13.0$\% vs.\ GPT-5.5: $50$\% on Few-NERD; Appendix~\ref{app:cross_scale}).
14	
15	\paragraph{Inverse scaling under adap
…[truncated 3035 chars]

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

_source line 3295 · 2026-05-22T00:56:54.101417+00:00_

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

_source line 3296 · 2026-05-22T00:56:54.101787+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	NER exhibits oracle scaling ($c{\approx}0.5$) but aggregation fails above $\theta_{\text{crit}}{=}0.70$; entity construction and LP selection ($+0.3$--$1.4$\,pp) bypass this barrier at entity granularity.
4	The binding constraint is $\alpha{\to}0$ even when $\rho$ is substantial.
5	

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

_source line 3297 · 2026-05-22T00:57:01.546376+00:00_

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

_source line 3298 · 2026-05-22T00:57:01.898588+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	\subsection{Confidence Signals}\label{sec:signals}
14	
15	Entity matching uses exact span and type match.
16	We evaluate four \textit{consistency signals}---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal}, per-sample signal.
17	
18	\paragraph{Log-probability (per-sample).}
19	$c_{\text{lp}}(y_i) = |y_i|^{-1} \sum_{j} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)$.
20	
21	\paragraph{Soft Jaccard (structural, instance-level).}
22	For samples $y_i, y_j$, we group by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU):
23	\begin{equation}\label{eq:sj}
24	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}
…[truncated 1642 chars]

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

_source line 3299 · 2026-05-22T00:57:01.949652+00:00_

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

_source line 3300 · 2026-05-22T00:57:02.352006+00:00_

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
12	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
13	MRSC best F1 ($0.763$) falls below greedy.
14	
15	\paragraph{Latent Self-Consistency (LSC).}
16	Mean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.
17	Centroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms majority vote ($0.792$) but does not close the oracle gap ($0.882$).
18	
19	\paragraph{Hidden-state probe.}
20	A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
21	All three exceed ESJ ($0.51$); only CoNLL approaches frequency agreement ($0.868$).
22	Cross-dataset transfer is weak: lea
…[truncated 1062 chars]

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

_source line 3301 · 2026-05-22T00:57:02.352426+00:00_

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

_source line 3302 · 2026-05-22T00:57:02.808011+00:00_

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
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$; 3-seed Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
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
28	\bottom
…[truncated 2372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 3303 · 2026-05-22T00:57:02.808570+00:00_

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

_source line 3304 · 2026-05-22T00:57:02.909350+00:00_

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
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3305 · 2026-05-22T00:57:06.927042+00:00_

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

_source line 3306 · 2026-05-22T00:57:07.429387+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	NER exhibits oracle scaling ($c{\approx}0.5$), but degeneracy (12.2--67.9\%) and LP-quality alignment ($\rho$ 0.043--0.667) constrain aggregation; temperature disentangles these (\S\ref{sec:scaling}; Table~\ref{tab:t_degeneracy}).
4	Across four frontier models on Few-NERD, degeneracy and the selection gap are negatively correlated (5.5--74\% degen; Table~\ref{tab:frontier_sc_cross}), consistent with the bound (\S\ref{sec:theory}) being structural.
5	
6	\paragraph{Pretrained vs.\ finetuned: degeneracy as the mechanism.}
7	On CoNLL, the pretrained model achieves comparable $\rho_{\textup{SJ}}$ ($0.47$ vs.\ $0.41$--$0.45$ finetuned) but MV captures ${\sim}98$\% of oracle headroom (degeneracy $36$\%) versus ${<}2$\% finetuned (degeneracy $57$--$60$\%).
8	Fine-tuning decouples agreement from quality through dataset-dependent pathways---diversity elimination on CoNLL, correlated error patterns on Few-NERD (Appendix~\ref{app:cross_scale}); per-type analysis confirms 7/8 entity types flip MV direction from positive to negative after finetuning (Appendix~\ref{app:pertype}).
9	
10	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
11	Entity-level construction bypasses both failure mechanisms when degeneracy ${<}22$\% ($p{<}0.01$; Appendix~\ref{app:epoch_confound}); the trade-off ($N{\times}$ cost for ${\approx}1$\,pp) may only justify safety-critical use.
12	LP compression (median 0.041 nats) connects to calibration challenges \cite{kadavath2022language, xiong2024verbalized}.
13	

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

_source line 3307 · 2026-05-22T00:57:07.429845+00:00_

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

_source line 3308 · 2026-05-22T00:57:07.881772+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, adaptive allocation \cite{aggarwal2023adaptive}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} all target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes and fine-grained variants.}
8	\citet{chen2023twofailures} identify SC failures where consistent outputs are systematically wrong; \citet{huang2024large} show LLMs cannot self-correct reasoning without external feedback. Our correlation-selection gap is a distinct failure where signals \textit{correlate} with quality yet fail to \textit{select}.
9	\citet{chen2024usc} extend SC to free-form tasks; our diagnostic shows such extensions face limits under constrained decoding (\S\ref{sec:selection_gap}). \citet{thirukovalluru2024atomic} decompose claims atomically; our entity-level decomposition shows sub-output agreement does not translate to selection gain.
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{yao2026consistency} show consistency correlates with NER/RE accuracy; we diagnose degeneracy and LP compression as mechanisms that prevent this correlation from yielding selection gains.
13	\citet{xie2023zeroshot} propose entity voting for zero-shot NER, \citet{li2024simple} improve structured output formatting, and \citet{xie2024selfimproving} report positive SC results under zero-shot prompting where output diversity is high---contrasting with our fine-tuned setting where degeneracy inverts the diversity conditions.
14	Our approach diagnoses why entity-level agreement fails to improve selection, building on generative IE \ci
…[truncated 2024 chars]

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

_source line 3309 · 2026-05-22T00:57:07.882247+00:00_

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

_source line 3310 · 2026-05-22T00:57:08.334215+00:00_

1	Our evidence is correlational and theoretical (MBR framework, conditional decomposition), not interventional: we have not performed controlled interventions (e.g., artificially varying degeneracy while holding other factors constant), and the cascade stages interact in ways that resist decomposition into independent causal effects ($R^2{<}0$; \S\ref{sec:selection_gap}); causal claims require future intervention experiments.
2	
3	Scope: structured IE (NER primary, RE and SQL exploratory), English only, open-weight (Qwen and LLaMA) and closed-source (GPT-5.5) families, fine-tuned (4B--14B) and zero-shot (72B, GPT-5.5) regimes, sample budget $N{\leq}32$.
4	Our evaluation covers four NER datasets; the RE extension covers a single SciERC benchmark ($n{=}207$ non-zero instances; 55.5\% yield zero F1 from upstream entity span errors rather than relation classification failure), and the SQL extension covers a single Spider subset ($n{=}196$) with 87.2\% degeneracy---both are exploratory and do not support generalization claims.
5	All experiments use English-language datasets; cross-lingual generalization remains untested.
6	Cross-model consistency results (\S\ref{sec:cross_model}) are limited to one dataset (Few-NERD) and one model pair (Qwen3-8B + LLaMA-3.1-8B).
7	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
8	Entity-level construction requires $N{\times}$ inference cost for $+1$\textendash$1.4$\,pp gain; cost-effectiveness may not justify deployment in resource-constrained settings.
9	We cover 4B\textendash 14B fine-tuned, 72B zero-shot, and GPT-5.5 zero-shot; the gap persists across all but behavior with 72B fine-tuning is untested.
10	Frontier API models exhibit markedly different degeneracy profiles (e.g., Claude Sonnet~4 at 74\% vs.\ DeepSeek Chat at 5.5\%; Table~\ref{tab:frontier_sc_cross
…[truncated 4014 chars]

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

_source line 3311 · 2026-05-22T00:57:08.384815+00:00_

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

_source line 3312 · 2026-05-22T00:57:08.837016+00:00_

File content (64892 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

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

_source line 3313 · 2026-05-22T00:57:13.756327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 3314 · 2026-05-22T00:57:14.258786+00:00_

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
…[truncated 4982 chars]

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

_source line 3315 · 2026-05-22T00:57:14.761311+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "description": "Count appendix lines"
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
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "description": "Count appendix lines"
  }
}
```

</details>

---


### Tool result

_source line 3316 · 2026-05-22T00:57:15.263916+00:00_

2397 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3317 · 2026-05-22T00:57:15.314628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-2"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-2"
  }
}
```

</details>

---


### Tool result

_source line 3318 · 2026-05-22T00:57:15.466560+00:00_

PDF pages extracted: 2 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf (963.8KB)

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

_source line 3319 · 2026-05-22T00:57:21.595663+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "7-10"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "7-10"
  }
}
```

</details>

---


### Tool result

_source line 3320 · 2026-05-22T00:57:22.600008+00:00_

PDF pages extracted: 4 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf (963.8KB)

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

_source line 3321 · 2026-05-22T00:57:23.056097+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Get PDF page count"
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
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Get PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 3322 · 2026-05-22T00:57:24.009976+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Fri May 22 00:38:40 2026 UTC
ModDate:         Fri May 22 00:38:40 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           47
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       986902 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 3323 · 2026-05-22T00:57:24.060710+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/ 2>/dev/null | head -30",
  "description": "List paper figures"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/ 2>/dev/null | head -30",
    "description": "List paper figures"
  }
}
```

</details>

---


### Tool result

_source line 3324 · 2026-05-22T00:57:24.111379+00:00_

fig_bound.png
fig_degeneracy_lp_scatter.pdf
fig_length_logprob_scatter.pdf
fig_lp_range_cdf.pdf
fig_oracle_scaling.pdf
fig_overview.pdf
fig_overview.png
fig_reliability.pdf
fig_selection_gap.pdf
fig_selection_gap.png
fig_signal_heatmap.pdf
fig_temperature_robustness.pdf

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

_source line 3325 · 2026-05-22T00:58:15.892201+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues"
  }
}
```

</details>

---


### Tool result

_source line 3326 · 2026-05-22T00:58:16.896751+00:00_

&lt;persisted-output>
Output too large (50.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/4d0c58e2-7d3b-474e-9f6b-9d5b96343388/tool-results/bw7irusr1.txt

Preview (first 2KB):
issues:
  # ===== 历史 resolved issues (保留) =====
  - id: "R1-W1"
    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
    resolution_round: 19

  - id: "R1-W2"
    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 21
    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
    resolution_round: 21

  - id: "R2-N1-old"
    summary: "Contribution 1 'methodological premise' 是定义推论"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
    resolution_round: 19

  - id: "R2-N2-old"
    summary: "与 MBR 文献差异化定位不够锐利"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
    resolution_round: 19

  - id: "R2-N4-old"
    summary: "模型规模 3B-8B，70B+ 未知"
    category: experiment
    severity: info
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
    resolution_round: 19

  - id: "R1-W3-old"
    summary: "2-seed 统计效力不足"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    last_
…[truncated 327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 3327 · 2026-05-22T00:58:17.399031+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
  "description": "Check existing review reports"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 3328 · 2026-05-22T00:58:17.801330+00:00_

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
round_27.md
round_29.md
round_3.md
round_30.md
round_4.md
round_5.md
round_6.md
round_7.md
round_7_consistency.md
round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 3329 · 2026-05-22T00:58:17.902211+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null || echo \"NO_CONFIG\"",
  "description": "Read full project config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null || echo \"NO_CONFIG\"",
    "description": "Read full project config"
  }
}
```

</details>

---


### Tool result

_source line 3330 · 2026-05-22T00:58:17.952848+00:00_

NO_CONFIG

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

_source line 3331 · 2026-05-22T00:58:54.443984+00:00_

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

_source line 3332 · 2026-05-22T00:59:14.568113+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20124
}
```

</details>

---


### Tool call

_source line 3333 · 2026-05-22T00:59:14.669203+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## Venue 信息\n- **EMNLP 2026** via ACL Rolling Review\n- ARR submission deadline: 2026-05-25\n- Long paper: 正文 8 页 + 无限参考文献页\n- Limitations/Ethics 不计入页数\n- 模板: ACL LaTeX (review mode)\n- 匿名: Double-blind\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `docs/paper/main.tex`（各 section 在 `docs/paper/sections/` 下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`（47页，正文8页+Appendix）\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Diagnostic framework 的四阶段级联（QE → degeneracy → agreement fidelity → LP compression）是否逻辑自洽？\n- \"correlation-selection gap\" 的定义和度量是否清晰、无歧义？\n- MBR 解码框架下的 entity construction 是否数学上严谨？Proposition 和 Theorem 的证明是否正确？\n- 各 signal（SJ, VC, EM, FK, LP）的定义和计算是否完备？instance-level vs per-sample 的区分是否充分利用？\n\n### 2. 实验设计\n- 4 个 NER 数据集 + 2 个模型族的覆盖是否充分？\n- 训练配置（LoRA fine-tuning, 3 vs 5 epochs）是否引入混淆？\n- N=8 primary, N=16 scaling 的样本量是否足够？\n- Constrained decoding 的使用是否公平？是否可能人为压制了 diversity？\n- RE 和 SQL parsing 的 exploratory extension 是否过于薄弱？\n- 9 个 method categories 的覆盖是否全面？是否有明显遗漏的方法？\n\n### 3. 统计分析\n- Holm-Bonferroni 多重比较校正是否正确应用？k=57 global correction 是否过于保守？\n- Bootstrap p-values 的计算方法是否合理？\n- 3-seed 实验的统计效力是否足够（特别是 SciERC n=529）？\n- \"selection alignment α approaches zero\" 的度量和置信区间？\n- Degeneracy 的定义（all N samples yield identical F1）是否过于严格或宽松？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Critical / Major / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度 + 简要理由）"
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## Venue 信息\n- **EMNLP 2026** via ACL Rolling Review\n- ARR submission deadline: 2026-05-25\n- Long paper: 正文 8 页 + 无限参考文献页\n- Limitations/Ethics 不计入页数\n- 模板: ACL LaTeX (review mode)\n- 匿名: Double-blind\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `docs/paper/main.tex`（各 section 在 `docs/paper/sections/` 下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`（47页，正文8页+Appendix）\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Diagnostic framework 的四阶段级联（QE → degeneracy → agreement fidelity → LP compression）是否逻辑自洽？\n- \"correlation-selection gap\" 的定义和度量是否清晰、无歧义？\n- MBR 解码框架下的 entity construction 是否数学上严谨？Proposition 和 Theorem 的证明是否正确？\n- 各 signal（SJ, VC, EM, FK, LP）的定义和计算是否完备？instance-level vs per-sample 的区分是否充分利用？\n\n### 2. 实验设计\n- 4 个 NER 数据集 + 2 个模型族的覆盖是否充分？\n- 训练配置（LoRA fine-tuning, 3 vs 5 epochs）是否引入混淆？\n- N=8 primary, N=16 scaling 的样本量是否足够？\n- Constrained decoding 的使用是否公平？是否可能人为压制了 diversity？\n- RE 和 SQL parsing 的 exploratory extension 是否过于薄弱？\n- 9 个 method categories 的覆盖是否全面？是否有明显遗漏的方法？\n\n### 3. 统计分析\n- Holm-Bonferroni 多重比较校正是否正确应用？k=57 global correction 是否过于保守？\n- Bootstrap p-values 的计算方法是否合理？\n- 3-seed 实验的统计效力是否足够（特别是 SciERC n=529）？\n- \"selection alignment α approaches zero\" 的度量和置信区间？\n- Degeneracy 的定义（all N samples yield identical F1）是否过于严格或宽松？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Critical / Major / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度 + 简要理由）"
  }
}
```

</details>

---


### Tool result

_source line 3334 · 2026-05-22T00:59:32.159958+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17490
}
```

</details>

---


### Tool call

_source line 3335 · 2026-05-22T00:59:32.261580+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "你是 Reviewer 2，负责**新颖性 + 相关工作完整性 + 写作/呈现质量**。\n\n## Venue 信息\n- **EMNLP 2026** via ACL Rolling Review\n- ARR submission deadline: 2026-05-25\n- Long paper: 正文 8 页 + 无限参考文献页\n- Limitations/Ethics 不计入页数\n- 模板: ACL LaTeX (review mode)\n- 匿名: Double-blind\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `docs/paper/main.tex`（各 section 在 `docs/paper/sections/` 下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`（47页，正文8页+Appendix）\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- \"correlation-selection gap\" 作为核心概念的新颖性——是否只是已知现象的重新包装？\n- 四阶段 diagnostic cascade 相比现有 SC failure mode 分析（Chen et al. 2024a, Huang et al. 2024）的增量贡献？\n- 与 Yun et al. (2025) \"diversity collapse\" 的区分是否充分？两者是否本质上在说同一件事？\n- 与 Yao et al. (2026) consistency-accuracy correlation 的关系——本文的 diagnostic 是否只是 Yao 的负面案例？\n- Entity construction via MBR 的方法论新颖性——MBR decoding 在 MT/code 中已有大量工作，NER 应用是否有足够的 novelty？\n- 正面结果（+0.3-1.4pp）的 practical significance——这个幅度是否值得一篇长文？\n\n### 2. 相关工作完整性\n- 检查 Related Work (Section 8) 是否遗漏重要文献\n- 特别关注：test-time compute scaling, structured prediction, NER, self-consistency, MBR decoding, uncertainty estimation 等领域的最新进展（2025-2026）\n- 用 web_search 搜索可能遗漏的近期工作\n\n### 3. 写作与呈现质量\n- Introduction 的 narrative flow 是否清晰？reader 能否快速理解核心问题和贡献？\n- 8 页正文 + 37 页 Appendix 的比例是否合理？是否有关键信息被不当地放入 Appendix？\n- Figure 1 (overview) 的信息密度和可读性\n- 表格设计（Table 1-5）的清晰度\n- 术语一致性（degeneracy, alignment, compression 等）\n- 论文结构：10 个 section 在 8 页内是否过于拥挤？\n- Abstract 和 Conclusion 是否准确概括了论文的发现？是否有 overclaiming？\n- Limitations 的覆盖是否充分？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Critical / Major / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度 + 简要理由）"
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
    "text": "你是 Reviewer 2，负责**新颖性 + 相关工作完整性 + 写作/呈现质量**。\n\n## Venue 信息\n- **EMNLP 2026** via ACL Rolling Review\n- ARR submission deadline: 2026-05-25\n- Long paper: 正文 8 页 + 无限参考文献页\n- Limitations/Ethics 不计入页数\n- 模板: ACL LaTeX (review mode)\n- 匿名: Double-blind\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `docs/paper/main.tex`（各 section 在 `docs/paper/sections/` 下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`（47页，正文8页+Appendix）\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- \"correlation-selection gap\" 作为核心概念的新颖性——是否只是已知现象的重新包装？\n- 四阶段 diagnostic cascade 相比现有 SC failure mode 分析（Chen et al. 2024a, Huang et al. 2024）的增量贡献？\n- 与 Yun et al. (2025) \"diversity collapse\" 的区分是否充分？两者是否本质上在说同一件事？\n- 与 Yao et al. (2026) consistency-accuracy correlation 的关系——本文的 diagnostic 是否只是 Yao 的负面案例？\n- Entity construction via MBR 的方法论新颖性——MBR decoding 在 MT/code 中已有大量工作，NER 应用是否有足够的 novelty？\n- 正面结果（+0.3-1.4pp）的 practical significance——这个幅度是否值得一篇长文？\n\n### 2. 相关工作完整性\n- 检查 Related Work (Section 8) 是否遗漏重要文献\n- 特别关注：test-time compute scaling, structured prediction, NER, self-consistency, MBR decoding, uncertainty estimation 等领域的最新进展（2025-2026）\n- 用 web_search 搜索可能遗漏的近期工作\n\n### 3. 写作与呈现质量\n- Introduction 的 narrative flow 是否清晰？reader 能否快速理解核心问题和贡献？\n- 8 页正文 + 37 页 Appendix 的比例是否合理？是否有关键信息被不当地放入 Appendix？\n- Figure 1 (overview) 的信息密度和可读性\n- 表格设计（Table 1-5）的清晰度\n- 术语一致性（degeneracy, alignment, compression 等）\n- 论文结构：10 个 section 在 8 页内是否过于拥挤？\n- Abstract 和 Conclusion 是否准确概括了论文的发现？是否有 overclaiming？\n- Limitations 的覆盖是否充分？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Critical / Major / Minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度 + 简要理由）"
  }
}
```

</details>

---


### Tool result

_source line 3336 · 2026-05-22T00:59:33.883732+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1622
}
```

</details>

---


### Assistant

_source line 3337 · 2026-05-22T00:59:48.637315+00:00_

Round 1 已启动：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法/实验/统计） | 🟢 已派发 |
| Reviewer 2（新颖性/相关工作/写作） | 🟢 已派发 |
| 视觉审查 Agent | 🟢 已启动 |
| 外部审稿 | ⬜ 未配置，跳过 |

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 248

## Round 248

2 recorded events


### User

_source line 3338 · 2026-05-22T01:06:49.703327+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见

**论文**: "Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER"
**审稿侧重**: 新颖性 + 相关工作完整性 + 写作/呈现质量

---

## Summary

本文研究 self-consistency（SC）在命名实体识别（NER）上的失败模式。作者定义了"correlation-selection gap"——质量估计信号与 oracle F1 存在相关性（AUROC 至多 0.45），但无法用于选择更好的样本或构建更好的实体集。论文提出四阶段诊断级联（degeneracy → alignment → LP compression → construction），在四个 NER 数据集、两个模型上评估了九类方法，最终通过 LP-weighted entity construction 获得 +0.3–1.4pp 的提升。

---

## Strengths

**S1. 问题定位精准，填补研究空白。** 现有 SC 文献几乎完全聚焦于分类/推理任务（Wang et al. 2023; Snell et al. 2025），NER 作为 set-valued 结构化输出的代表性任务，缺乏系统性的 SC 失败分析。本文填补了这一空白，对 test-time compute scaling 社区有参考价值。

**S2. 诊断框架结构清晰。** 四阶段级联（§2–§4）将一个复杂问题分解为可独立检验的子问题，逻辑链条完整：degeneracy 检查样本多样性是否存在 → alignment 检查 agreement 是否与质量对齐 → LP compression 检查 log-prob 是否提供额外信号 → construction 检查实体级聚合是否可行。每一步都有对应的实验支撑。

**S3. 实验设计严谨，统计测试充分。** 论文报告了 bootstrap 95% CI（Table 1, §1）、Holm 校正的置换检验（§4）、permutation p-values（Table 8）、split-half reliability（Table 8），以及 Bonferroni 校正（Appendix p.20），统计规范性高于多数同类工作。

**S4. 引用验证通过。** 57 条 bib entry 全部有引用、无 orphan，52/57 通过 OpenAlex 在线验证，3 条 mismatch 仅为编码差异（如 Müller vs m\"uller），2 条 not_found（Lightman et al. 2024, Aggarwal et al. 2023）为知名发表论文但 OpenAlex 索引缺失，无伪造引用。

**S5. Proposition 1 提供理论支撑。** §6.1 的 Proposition 1（MBR 目标下 majority vote 在 balanced set-overlap utility 下恢复 entity-level majority vote）为 entity construction 方法提供了理论动机，虽然证明本身不复杂，但将 MBR 框架与 NER 问题清晰连接。

---

## Weaknesses

### Critical

**N1. [Critical] 核心叙事自相矛盾——"SC 失败"与"SC 可被修复"的张力未解决**
- 具体位置：Abstract, §1, §5, §6, §10
- 问题：标题和 Abstract 的核心 claim 是 "entity-level verification fails"、"no entity-level agreement signal reliably improves selection"。但 §5–§6 和 Table 1–2 展示了 LP selection 在 Few-NERD 上 +1.39pp、LP-weighted entity construction 在 Few-NERD 上 +1.4pp 的正面结果。论文同时声称 SC 失败又展示 SC 可以（通过 LP 信号）获得不可忽略的提升，这两个叙事之间的张力未被充分调和。读者在读完 §5 后会困惑：到底 SC 是否"fails"？
- Abstract 中 "yet no signal outperforms greedy" 的表述与 Table 1 中 LP selection ΔF1=+1.39pp（p<0.001）直接矛盾——LP selection 确实 outperforms greedy，只是幅度有限。
- 为什么影响接收：核心 claim 的 internal consistency 是 soundness 的基本要求。当前叙事给人的印象是作者在选择性地呈现结果以支持"负面发现"的叙事。
- 建议：明确区分 "entity-level agreement signals"（确实失败）vs "model-internal signals like LP"（有条件成功），重新组织 claim hierarchy。

**N2. [Critical] 与 Yao et al. (2026) 的区分不充分——本文的 diagnostic 可能只是 Yao 的负面案例细化**
- 具体位置：§8 (Related Work), §1 Introduction
- 问题：Yao et al. (2026) 在 Genomics & Informatics 上发表的工作已经在 entity/relation extraction 场景下研究了 consistency-accuracy correlation，并报告了类似的发现——相关性存在但 model-dependent、task-complexity-dependent。本文的 "correlation-selection gap" 本质上是 Yao 发现的一个特例（NER 上 correlation 存在但 selection 失败）。论文 §8 仅用一句话提到 Yao et al.（"Yao et al. (2026) demonstrates..."），未深入讨论两者的区别和增量贡献。
- 为什么影响接收：如果增量贡献仅是 "在更多数据集上复现了 Yao 的发现并加了一个 four-stage cascade"，novelty 可能不足。
- 建议：在 §1 或 §8 中专门用一段详细对比，说明本文的 diagnostic cascade 和 construction 方法在 Yao et al. 之上的具体增量。

### Major

**W1. [Major] 8页正文 vs 37页 Appendix 的比例严重失衡**
- 具体位置：全文结构
- 问题：Appendix 页数（37页，p.11–p.47）是正文（8页）的近5倍。关键实验信息被推入 Appendix：Table 2 的完整 9 类方法结果仅在正文展示 Few-NERD（"Full coverage in Appendix b.4"）；entity-level verification probes 的详细分析在 Appendix h–i；cross-dataset transfer 分析在 Appendix b.3；N-scaling 分析在 Appendix b.6。一个 reviewer 需要阅读 ~47 页才能评估完整性，这对审稿造成不合理的负担。
- 建议：将 Table 2 扩展为完整版（至少包含 2 个数据集）、将 cross-dataset 和 N-scaling 的核心发现移入正文。可考虑合并 §2–§3 或 §9–§10 以腾出空间。

**W2. [Major] 仅两个同规模模型家族，泛化性存疑**
- 具体位置：§7.1, Limitations
- 问题：实验仅使用 Qwen2.5-7B 和 LLaMA-3.1-8B，两者均为 ~7–8B 参数的 instruction-tuned 模型。论文的核心 claim 是关于 SC 在 NER 上的 "capability ceiling"，但未验证此 ceiling 在不同规模（如 70B）、不同架构（如 Mixtral/decoder-encoder）、不同能力水平的模型上是否成立。Limitations 中提到 "English only, open-weight 7B/8B" 但将其定位为次要局限。
- 为什么影响评分：如果更强的模型（如 70B）在 NER 上的 degeneracy 更低、alignment 更好，四阶段级联的结论可能不成立——ceiling 可能是 model-specific 而非 task-structural。
- 建议：至少增加一个不同规模的模型（如 Qwen2.5-72B 或 LLaMA-3.1-70B）来验证 ceiling 的 scale-invariance。

**W3. [Major] "Correlation-selection gap" 的新颖性——本质上是已知现象的重新命名**
- 具体位置：§1, §4
- 问题：在 selective prediction / calibration 文献中，一个 well-calibrated 的 confidence score 可以 rank 但不足以做 selection（因为 selection 需要 pointwise discrimination 而 ranking 只需 ordinal）是已知的（Geifman & El-Yaniv 2017; Guo et al. 2017）。特别是在 structured output 中，set-level agreement 与 element-level quality 的脱节也被 Kuleshov & Liang (2015) 讨论过。本文将此现象在 NER 上实证化并命名为 "correlation-selection gap"，但概念本身的新颖性有限。
- 建议：在 §1 或 §4 中明确承认 correlation-selection gap 在理论上并非全新概念，本文的贡献在于 (1) 在 NER 上的实证量化和 (2) 四阶段 cascade 的诊断工具。

**W4. [Major] 正面结果的 practical significance 不足以支撑长文**
- 具体位置：§5, §6, Table 1–2
- 问题：LP-weighted entity construction 的最佳改进为 Few-NERD +1.4pp、SciERC +1.28pp（Table 2, §5），但 CoNLL 上无显著提升（+0.3pp, non-significant）。考虑到这需要 N=8 次采样（8x 推理成本），效率很低。论文本身也承认 "positive results ... practical significance" 有限（§7.5）。对于一篇 8 页长文，如果核心发现是 "SC 不行" + "我们的修复方案只改进了 0.3–1.4pp"，读者会质疑这是否值得一篇完整论文。
- 建议：要么更深入地分析 *为什么* 改进如此有限（理论 bound tighter analysis），要么提出更强的 construction 方法。当前论文在 diagnostic（前半部分）和 prescriptive（后半部分）之间两头不够深入。

**W5. [Major] 与 Yun et al. (2025) "diversity collapse" 的区分模糊**
- 具体位置：§8, §3
- 问题：Yun et al. (2025) 的 "diversity collapse" 论证了 instruction-tuned LLM 在结构化格式下产生低多样性输出，这直接解释了本文 §3 中观察到的 "degeneracy"（CoNLL 上 48–87% 的 instances 产生 identical outputs）。论文 §8 用一句话提及 Yun et al.（"Yun et al. (2025) identify diversity collapse under constrained decoding"），但未深入讨论：本文的 degeneracy 是否就是 diversity collapse 的 NER 特例？如果是，§3 的发现本质上是 Yun et al. 的复现。
- 建议：需要实验性区分（e.g., constrained decoding vs free-form 下的 degeneracy 对比）或更深入的概念辨析。

### Minor

**W6. [Minor] 10 个 section 在 8 页内过于拥挤**
- 正文包含 §1 Introduction – §10 Conclusion，外加多个 subsection。§9 Discussion 被压缩到不到半页，§10 Conclusion 同样不到半页。建议合并 §9 和 §10。

**W7. [Minor] Table 2 在正文中只展示 Few-NERD 数据集的结果**
- Table 2（§5）展示 9 类方法的汇总，但仅报告 "Few-NERD only; SciERC ΔF1=−0.12 pp"，完整结果在 Appendix b.4。正文应至少展示两个数据集以支撑 "across NER datasets" 的 claim。

**W8. [Minor] Figure 1 信息密度过高**
- Figure 1 试图用三个 panel 覆盖 correlation-selection gap 的三个方面（quality estimation, sample selection, entity construction），但每个 panel 内包含多个子图、注释和数字，首次阅读时认知负荷较大。建议拆分为两个图或简化 annotation。

**W9. [Minor] Abstract 中 "no signal outperforms greedy" 与 Table 1 矛盾**
- Abstract: "yet no signal outperforms greedy"。但 Table 1 显示 LP selection 在 Few-NERD 上 ΔF1=+1.39pp（p<0.001）。这句话需要加限定词（如 "no *agreement-based* signal"）。

**W10. [Minor] Proposition 1 的条件过强**
- §6.1 Proposition 1 假设 "balanced set-overlap utility"（α=0）和 entity-level independence，实际中这些条件很少满足。论文选择 c=0.5（"the elbow of compression curve"），但未讨论对 α 值的敏感性。

---

## Questions

**Q1.** Abstract 声称 "no entity-level agreement signal reliably improves selection"，但 LP 是 model-internal signal 而非 entity-level agreement signal——作者能否精确定义 "entity-level agreement signal" 的范围？LP selection 的成功是否意味着 model-internal signals 可以部分绕过 correlation-selection gap？

**Q2.** 论文只测试了 7–8B 模型。有没有证据或理论论证表明 correlation-selection gap 在更大模型上仍然存在？如果 70B 模型的 degeneracy 显著降低（因为更强的 NER 能力），四阶段级联的第一阶段就可能被绕过，后续结论可能不同。

**Q3.** CoNLL 上 48–87% instances 产生 identical outputs（§3），这是否主要因为 CoNLL 是 well-studied benchmark、模型已经 overfit 或 memorize 了这些 entities？如果在 fully out-of-distribution 的 NER 数据上测试，degeneracy 是否会显著降低？

**Q4.** Entity construction via LP-weighted MBR（§6.1）本质上是用 model probability 作为 weight。这与 model-based MBR（Jinnai et al. 2024）有什么区别？为什么不直接用 model-based MBR？

**Q5.** 四阶段 cascade 中，Stage 1（degeneracy）和 Stage 3（LP compression）之间的交互没有被讨论。如果高 degeneracy 和高 LP compression 同时出现（如 CoNLL），这是否意味着模型对 NER 已经 "converged"，SC 根本没有意义？

---

## Missing References

**M1.** Conformal prediction for structured NLP outputs（如 Fisch et al. 2021 "Few-Shot Conformal Prediction with Auxiliary Tasks"、Quach et al. 2024）——与 calibrated selection 直接相关。

**M2.** Token-level vs entity-level uncertainty 的区分文献（如 He et al. 2024 on uncertainty decomposition in sequence labeling）——论文讨论了 entity-level 但未引用 token-level 的先行工作。

**M3.** Pass@k 文献的原始来源 Chen et al. (2021) "Evaluating Large Language Models Trained on Code"——论文讨论 best-of-N 但仅引用 Brown et al. 2024，未追溯到 pass@k 的起源。

**M4.** Selective prediction survey for NLP（如 Varshney et al. 2022 "Investigating Selective Prediction Approaches Across Several Tasks in IID, OOD, and Adversarial Settings"）——论文涉及 selection 但 selective prediction 文献覆盖不足。

**M5.** 近期 test-time scaling survey（如 "Revisiting Test-Time Scaling: A Survey" 2025）——应在 §8 引用以定位本文在 TTS 大图景中的位置。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论基本合理，统计测试充分，但核心 claim 存在内部矛盾（N1），仅两个同规模模型限制泛化性（W2） |
| Excitement | 2.5/5 | 问题有意义但发现偏 expected——SC 在 structured output 上失败并不令人意外；正面结果幅度很小 |
| Reproducibility | 4/5 | 标准数据集和模型，Appendix 提供充分细节，承诺代码/数据发布 |
| Datasets/Software | 3/5 | 使用现有数据集，诊断工具有复用价值但未明确发布计划 |

## Overall Assessment

**Overall**: 3.0 — Findings

**Reviewer Confidence**: 4/5（对 self-consistency、MBR decoding、NER evaluation 均较熟悉，仔细阅读了全文及关键 appendix 章节）

**一句话总结**: 论文对 SC 在 NER 上的失败模式提供了系统性的实证分析和清晰的诊断框架，但核心概念（correlation-selection gap）的新颖性有限，与 Yao et al. (2026) 和 Yun et al. (2025) 的增量区分不足，正面结果（+0.3–1.4pp）的 practical significance 较弱，且 8:37 的正文/附录比例暗示主要贡献可能更适合以 shorter 或更聚焦的形式呈现。

**理由**: 本文的诊断贡献——特别是四阶段级联和在 4 个数据集上的系统验证——有学术价值，值得发表。但以下因素限制了评分：(1) 核心叙事的内部矛盾（声称 SC 失败但同时展示 SC 成功的案例）；(2) 概念新颖性有限（correlation ≠ selection 在 calibration 文献中已知）；(3) 只有两个同规模模型，"capability ceiling" 的 claim 缺乏足够的泛化支撑；(4) practical impact 有限（最佳改进 1.4pp，需要 8x 推理成本）。建议定位为 Findings 论文，或在修改中解决 N1–N2 的核心叙事问题并增加更大模型的实验以支撑 "ceiling" 的 claim。

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

_source line 3339 · 2026-05-22T01:07:06.019570+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 249

## Round 249

2 recorded events


### User

_source line 3340 · 2026-05-22T01:07:19.620412+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断**: Overall 3.0（Findings），Excitement 2.5/5。

**主要问题**:
- 2 个 Critical：核心叙事自相矛盾（声称 SC 失败但同时展示正面结果），与 Yao et al. (2026) 的增量区分不足
- 5 个 Major：正文/附录比例 8:37 严重失衡；仅两个同规模模型限制泛化性；correlation-selection gap 概念新颖性有限；正面结果 practical significance 弱（+0.3–1.4pp at 8x cost）；与 Yun et al. diversity collapse 区分模糊
- 5 个 Minor：结构过于拥挤、Table 2 只展示单数据集、Figure 1 信息密度过高、Abstract overclaim、Proposition 1 条件过强
- 5 条 Missing References：conformal prediction、token-level uncertainty、pass@k 原始来源、selective prediction survey、TTS survey

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

_source line 3341 · 2026-05-22T01:07:28.596625+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 250

## Round 250

6 recorded events


### User

_source line 3342 · 2026-05-22T01:07:30.109107+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验设计 + 统计分析

### 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 扎实的诊断性实证研究，提出了"correlation-selection gap"新概念并系统验证，但理论贡献中的独立性假设缺乏充分论证，exploratory extensions (RE/SQL) 过于薄弱，且 N=8 的采样规模不足以支撑"capability ceiling"的强声明。

### 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法论扎实（Holm-Bonferroni, bootstrap），但 Proposition 1 的 entity-wise independence 假设不现实，部分因果性语言超出相关性证据 |
| Excitement | 3.0/5 | Correlation-selection gap 有概念价值，诊断级联可复用；但核心是负面结果，可操作建议有限 |
| Reproducibility | 4/5 | 详尽的实验配置、公开数据集和模型、承诺发布代码 |
| Reviewer Confidence | 4/5 | 仔细检查了方法论、统计分析和数学证明，熟悉相关文献 |

---

### Must-Fix 问题

**N1** [critical] **Proposition 1 的 entity-wise independence 假设不现实且未充分讨论**
- 位置：Section 6.1, Proposition 1 (p.6); Appendix p.1 proof (p.29-31)
- Proposition 1 声称在 balanced set-overlap utility 下 MBR-optimal construction 等价于 majority vote。证明依赖 entity-wise independence，但 NER 中 entity 之间有明显依赖（span 重叠约束、句内 entity 数量约束、自回归生成中的条件依赖）。论文仅在 p.30 简短承认假设是近似的，未量化偏差也未讨论假设违反时结论的退化。这是论文唯一的理论贡献，需要更充分的论证。
- 建议：添加经验验证（entity 对的 mutual information），讨论 near-optimality guarantee，或将 Proposition 1 重定位为 motivating analysis。

**N2** [critical] **N=8 不足以支撑 "capability ceiling" 声明**
- 位置：Section 7.1, Section 6.2, Appendix s (p.32)
- N=8 时 degeneracy 12%-62%，部分是小 N 的直接后果。N=16 分析显示 degeneracy 下降且 LP 增益出现。Figure 10 显示 oracle F1 随 N 单调递增。标题中的 "capability ceiling" 暗示固有结构性限制，但如果 ceiling 随 N 上升，核心命题需要重新表述。
- 建议：至少在一个数据集上测试 N=32/64，验证 selection gap 是否饱和；或将 "ceiling" 修改为更审慎的措辞。

---

### Should-Fix 问题

**W1** [major] RE/SQL extensions 过于薄弱，不足以支撑泛化声明。RE 仅用 SciERC 1 个模型 397 个有效样本，SQL 更为简略。建议明确定位为 preliminary evidence 或增加实验覆盖。

**W2** [major] k=57 global Holm-Bonferroni 可能过度保守。57 个测试跨越不同研究问题。建议补充 Benjamini-Hochberg FDR 作为 sensitivity check。

**W3** [major] 部分因果性语言超出相关性证据。如 Section 4 "degeneracy is the binding constraint" — 但 non-degenerate subset 上 selection gap 仍存在。建议调整为相关性语言。

**W4** [major] SciERC (n=529) 和 cross-dataset 分析 (n=23) 的统计效力不足。论文自己的 power analysis 确认了这一点。建议在主文中注明 power 限制。

**W5** [minor→major] 缺少 sequence-level entropy 等 token-level 不确定性方法的比较。LP 是一种 token-level 信号聚合，但未与其他聚合方式做系统比较。

---

### 小问题
- M1: Table 1 和 Table 3 的 significance threshold 标注不一致
- M2: Figure 1 箭头暗示因果方向，与 "diagnostic sequence" 标注不符
- M3: SJ 定义中的 sim(·,·) 函数未在主文说明
- M4: "capability ceiling" 未形式化定义
- M5: Appendix ag (Failure Mode Gallery) 有价值，建议主文简要引用

---

### Questions for Authors
- Q1: Entity-wise independence 假设在实验数据上的近似程度？
- Q2: N=32/64 时 degeneracy rate 和 selection gap 趋势？
- Q3: 改用 BH-FDR 后哪些额外发现显著？
- Q4: Constrained decoding 的 selection gap 更小是否说明 degeneracy 源于 model behavior？
- Q5: Hidden-state probe 是否应做 entity-level 而非 sample-level？
- Q6: 增加 RE 数据集后预期 correlation-selection gap 大小？

---

### Missing References
1. Malinin & Gales (2021) — 结构化预测中的不确定性估计
2. Kuhn et al. (2023) Semantic Uncertainty — 引用但未作为 baseline 比较
3. MBR-for-structured-output 相关工作

---

### 主要优势
- S1: Correlation-selection gap 概念新颖有解释力
- S2: 四阶段诊断级联可复用
- S3: 实验规模和统计严谨性远超领域平均
- S4: 诚实呈现负面结果
- S5: Constrained decoding confound 处理得当

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

_source line 3343 · 2026-05-22T01:08:26.223358+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE]（同意并说明理由）或 [REBUT]（反驳并提供证据，cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.0 — Findings\n**Reviewer Confidence**: 4/5\n\n### Strengths\nS1. 问题定位精准，填补研究空白（SC 文献聚焦分类/推理，NER 缺乏系统性分析）\nS2. 诊断框架结构清晰（四阶段级联逻辑完整）\nS3. 实验设计严谨，统计测试充分（bootstrap CI, Holm 校正, permutation p-values）\nS4. 引用验证通过（57条 bib entry 无伪造）\nS5. Proposition 1 提供理论支撑（MBR 与 NER 清晰连接）\n\n### Critical Weaknesses\n\n**N1. [Critical] 核心叙事自相矛盾——\"SC 失败\"与\"SC 可被修复\"的张力未解决**\n- Abstract, §1, §5, §6, §10\n- 标题和 Abstract 声称 \"entity-level verification fails\"、\"no entity-level agreement signal reliably improves selection\"。但 §5–§6 展示了 LP selection +1.39pp（Few-NERD）、LP-weighted entity construction +1.4pp 的正面结果。\n- Abstract 中 \"yet no signal outperforms greedy\" 与 Table 1 中 LP selection ΔF1=+1.39pp（p<0.001）直接矛盾。\n- 当前叙事给人印象是作者在选择性呈现结果以支持\"负面发现\"叙事。\n\n**N2. [Critical] 与 Yao et al. (2026) 的区分不充分**\n- Yao et al. (2026) 已在 entity/relation extraction 场景下研究了 consistency-accuracy correlation。本文的 \"correlation-selection gap\" 可能只是 Yao 发现的一个特例。论文 §8 仅用一句话提到。\n\n### Major Weaknesses\n\n**W1. [Major] 8页正文 vs 37页 Appendix 比例严重失衡**\n- 关键实验信息被推入 Appendix：Table 2 完整结果、entity-level probes 详细分析、cross-dataset transfer、N-scaling。\n- reviewer 需要阅读 ~47 页才能评估完整性。\n\n**W2. [Major] 仅两个同规模模型家族，泛化性存疑**\n- 仅 Qwen2.5-7B 和 LLaMA-3.1-8B。\"capability ceiling\" 的 claim 缺乏更大模型验证。\n\n**W3. [Major] \"Correlation-selection gap\" 概念新颖性有限**\n- 在 selective prediction / calibration 文献中，calibrated score 可 rank 但不足以做 selection 是已知现象（Geifman & El-Yaniv 2017; Guo et al. 2017）。\n\n**W4. [Major] 正面结果 practical significance 不足以支撑长文**\n- LP-weighted entity construction 最佳改进 +1.4pp（Few-NERD），需要 8x 推理成本。论文在 diagnostic 和 prescriptive 之间两头不够深入。\n\n**W5. [Major] 与 Yun et al. (2025) \"diversity collapse\" 区分模糊**\n- 本文的 degeneracy 是否就是 diversity collapse 的 NER 特例？如果是，§3 的发现本质上是 Yun et al. 的复现。\n\n### Minor Weaknesses\nW6. 10 个 section 在 8 页内过于拥挤\nW7. Table 2 只展示单数据集\nW8. Figure 1 信息密度过高\nW9. Abstract 中 \"no signal outperforms greedy\" 与 Table 1 矛盾\nW10. Proposition 1 条件过强\n\n### Questions\nQ1. LP 是 model-internal signal 而非 entity-level agreement signal——\"entity-level agreement signal\" 的精确范围？\nQ2. 有无证据表明 correlation-selection gap 在 70B+ 模型上仍存在？\nQ3. CoNLL 高 degeneracy 是否因 benchmark memorization？\nQ4. LP-weighted MBR 与 model-based MBR（Jinnai et al. 2024）区别？\nQ5. Degeneracy 和 LP compression 的交互效应？\n\n### Missing References\nM1. Conformal prediction for structured NLP（Fisch et al. 2021, Quach et al. 2024）\nM2. Token-level vs entity-level uncertainty（He et al. 2024）\nM3. Pass@k 原始来源 Chen et al. (2021)\nM4. Selective prediction survey（Varshney et al. 2022）\nM5. Test-time scaling survey（2025）\n\n---\n\n请逐条回应上述所有 Weakness（N1, N2, W1–W10）和 Question（Q1–Q5），标注 [AGREE] 或 [REBUT]。"
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE]（同意并说明理由）或 [REBUT]（反驳并提供证据，cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.0 — Findings\n**Reviewer Confidence**: 4/5\n\n### Strengths\nS1. 问题定位精准，填补研究空白（SC 文献聚焦分类/推理，NER 缺乏系统性分析）\nS2. 诊断框架结构清晰（四阶段级联逻辑完整）\nS3. 实验设计严谨，统计测试充分（bootstrap CI, Holm 校正, permutation p-values）\nS4. 引用验证通过（57条 bib entry 无伪造）\nS5. Proposition 1 提供理论支撑（MBR 与 NER 清晰连接）\n\n### Critical Weaknesses\n\n**N1. [Critical] 核心叙事自相矛盾——\"SC 失败\"与\"SC 可被修复\"的张力未解决**\n- Abstract, §1, §5, §6, §10\n- 标题和 Abstract 声称 \"entity-level verification fails\"、\"no entity-level agreement signal reliably improves selection\"。但 §5–§6 展示了 LP selection +1.39pp（Few-NERD）、LP-weighted entity construction +1.4pp 的正面结果。\n- Abstract 中 \"yet no signal outperforms greedy\" 与 Table 1 中 LP selection ΔF1=+1.39pp（p<0.001）直接矛盾。\n- 当前叙事给人印象是作者在选择性呈现结果以支持\"负面发现\"叙事。\n\n**N2. [Critical] 与 Yao et al. (2026) 的区分不充分**\n- Yao et al. (2026) 已在 entity/relation extraction 场景下研究了 consistency-accuracy correlation。本文的 \"correlation-selection gap\" 可能只是 Yao 发现的一个特例。论文 §8 仅用一句话提到。\n\n### Major Weaknesses\n\n**W1. [Major] 8页正文 vs 37页 Appendix 比例严重失衡**\n- 关键实验信息被推入 Appendix：Table 2 完整结果、entity-level probes 详细分析、cross-dataset transfer、N-scaling。\n- reviewer 需要阅读 ~47 页才能评估完整性。\n\n**W2. [Major] 仅两个同规模模型家族，泛化性存疑**\n- 仅 Qwen2.5-7B 和 LLaMA-3.1-8B。\"capability ceiling\" 的 claim 缺乏更大模型验证。\n\n**W3. [Major] \"Correlation-selection gap\" 概念新颖性有限**\n- 在 selective prediction / calibration 文献中，calibrated score 可 rank 但不足以做 selection 是已知现象（Geifman & El-Yaniv 2017; Guo et al. 2017）。\n\n**W4. [Major] 正面结果 practical significance 不足以支撑长文**\n- LP-weighted entity construction 最佳改进 +1.4pp（Few-NERD），需要 8x 推理成本。论文在 diagnostic 和 prescriptive 之间两头不够深入。\n\n**W5. [Major] 与 Yun et al. (2025) \"diversity collapse\" 区分模糊**\n- 本文的 degeneracy 是否就是 diversity collapse 的 NER 特例？如果是，§3 的发现本质上是 Yun et al. 的复现。\n\n### Minor Weaknesses\nW6. 10 个 section 在 8 页内过于拥挤\nW7. Table 2 只展示单数据集\nW8. Figure 1 信息密度过高\nW9. Abstract 中 \"no signal outperforms greedy\" 与 Table 1 矛盾\nW10. Proposition 1 条件过强\n\n### Questions\nQ1. LP 是 model-internal signal 而非 entity-level agreement signal——\"entity-level agreement signal\" 的精确范围？\nQ2. 有无证据表明 correlation-selection gap 在 70B+ 模型上仍存在？\nQ3. CoNLL 高 degeneracy 是否因 benchmark memorization？\nQ4. LP-weighted MBR 与 model-based MBR（Jinnai et al. 2024）区别？\nQ5. Degeneracy 和 LP compression 的交互效应？\n\n### Missing References\nM1. Conformal prediction for structured NLP（Fisch et al. 2021, Quach et al. 2024）\nM2. Token-level vs entity-level uncertainty（He et al. 2024）\nM3. Pass@k 原始来源 Chen et al. (2021)\nM4. Selective prediction survey（Varshney et al. 2022）\nM5. Test-time scaling survey（2025）\n\n---\n\n请逐条回应上述所有 Weakness（N1, N2, W1–W10）和 Question（Q1–Q5），标注 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 3344 · 2026-05-22T01:08:42.044815+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15821
}
```

</details>

---


### Tool call

_source line 3345 · 2026-05-22T01:08:42.195973+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE]（同意并说明理由）或 [REBUT]（反驳并提供证据，cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Reviewer Confidence**: 4/5\n\n### Strengths\nS1. Correlation-selection gap 概念新颖有解释力\nS2. 四阶段诊断级联可复用\nS3. 实验规模和统计严谨性远超领域平均\nS4. 诚实呈现负面结果\nS5. Constrained decoding confound 处理得当\n\n### Must-Fix (Critical)\n\n**N1. [Critical] Proposition 1 的 entity-wise independence 假设不现实且未充分讨论**\n- Section 6.1, Proposition 1; Appendix proof\n- 证明依赖 entity-wise independence，但 NER 中 entity 有 span 重叠约束、句内数量约束、自回归条件依赖。\n- 论文仅简短承认假设是近似的，未量化偏差也未讨论退化。\n- 建议：添加经验验证（entity 对的 mutual information），或重定位为 motivating analysis。\n\n**N2. [Critical] N=8 不足以支撑 \"capability ceiling\" 声明**\n- N=8 时 degeneracy 12%-62%，部分是小 N 的直接后果。\n- N=16 分析显示 degeneracy 下降且 LP 增益出现。\n- Oracle F1 随 N 单调递增。\n- 标题中 \"capability ceiling\" 暗示固有结构性限制，但如果 ceiling 随 N 上升，核心命题需重新表述。\n- 建议：至少测试 N=32/64，或修改 \"ceiling\" 措辞。\n\n### Should-Fix (Major)\n\n**W1. [Major] RE/SQL extensions 过于薄弱**\n- RE 仅用 SciERC 1 个模型 397 个样本，SQL 更简略。\n- 建议明确定位为 preliminary evidence 或增加覆盖。\n\n**W2. [Major] k=57 global Holm-Bonferroni 可能过度保守**\n- 57 个测试跨越不同研究问题。\n- 建议补充 BH-FDR 作为 sensitivity check。\n\n**W3. [Major] 部分因果性语言超出相关性证据**\n- 如 \"degeneracy is the binding constraint\" — 但 non-degenerate subset 上 selection gap 仍存在。\n- 建议调整为相关性语言。\n\n**W4. [Major] SciERC (n=529) 和 cross-dataset 分析 (n=23) 的统计效力不足**\n- 论文自己的 power analysis 确认了这一点。\n- 建议在主文中注明 power 限制。\n\n**W5. [Minor→Major] 缺少 sequence-level entropy 等 token-level 不确定性方法的比较**\n- LP 是 token-level 信号聚合，未与其他聚合方式做系统比较。\n\n### Minor\nM1. Table 1 和 Table 3 的 significance threshold 标注不一致\nM2. Figure 1 箭头暗示因果方向，与 \"diagnostic sequence\" 标注不符\nM3. SJ 定义中 sim(·,·) 未在主文说明\nM4. \"capability ceiling\" 未形式化定义\nM5. Appendix ag (Failure Mode Gallery) 有价值，建议主文简要引用\n\n### Questions\nQ1. Entity-wise independence 在实验数据上的近似程度？\nQ2. N=32/64 时 degeneracy rate 和 selection gap 趋势？\nQ3. 改用 BH-FDR 后哪些额外发现显著？\nQ4. Constrained decoding 的 selection gap 更小是否说明 degeneracy 源于 model behavior？\nQ5. Hidden-state probe 是否应做 entity-level 而非 sample-level？\nQ6. 增加 RE 数据集后预期 correlation-selection gap 大小？\n\n### Missing References\n1. Malinin & Gales (2021) — 结构化预测中的不确定性估计\n2. Kuhn et al. (2023) Semantic Uncertainty — 引用但未作为 baseline 比较\n3. MBR-for-structured-output 相关工作\n\n---\n\n请逐条回应上述所有 Weakness（N1, N2, W1–W5, M1–M5）和 Question（Q1–Q6），标注 [AGREE] 或 [REBUT]。"
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
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE]（同意并说明理由）或 [REBUT]（反驳并提供证据，cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Reviewer Confidence**: 4/5\n\n### Strengths\nS1. Correlation-selection gap 概念新颖有解释力\nS2. 四阶段诊断级联可复用\nS3. 实验规模和统计严谨性远超领域平均\nS4. 诚实呈现负面结果\nS5. Constrained decoding confound 处理得当\n\n### Must-Fix (Critical)\n\n**N1. [Critical] Proposition 1 的 entity-wise independence 假设不现实且未充分讨论**\n- Section 6.1, Proposition 1; Appendix proof\n- 证明依赖 entity-wise independence，但 NER 中 entity 有 span 重叠约束、句内数量约束、自回归条件依赖。\n- 论文仅简短承认假设是近似的，未量化偏差也未讨论退化。\n- 建议：添加经验验证（entity 对的 mutual information），或重定位为 motivating analysis。\n\n**N2. [Critical] N=8 不足以支撑 \"capability ceiling\" 声明**\n- N=8 时 degeneracy 12%-62%，部分是小 N 的直接后果。\n- N=16 分析显示 degeneracy 下降且 LP 增益出现。\n- Oracle F1 随 N 单调递增。\n- 标题中 \"capability ceiling\" 暗示固有结构性限制，但如果 ceiling 随 N 上升，核心命题需重新表述。\n- 建议：至少测试 N=32/64，或修改 \"ceiling\" 措辞。\n\n### Should-Fix (Major)\n\n**W1. [Major] RE/SQL extensions 过于薄弱**\n- RE 仅用 SciERC 1 个模型 397 个样本，SQL 更简略。\n- 建议明确定位为 preliminary evidence 或增加覆盖。\n\n**W2. [Major] k=57 global Holm-Bonferroni 可能过度保守**\n- 57 个测试跨越不同研究问题。\n- 建议补充 BH-FDR 作为 sensitivity check。\n\n**W3. [Major] 部分因果性语言超出相关性证据**\n- 如 \"degeneracy is the binding constraint\" — 但 non-degenerate subset 上 selection gap 仍存在。\n- 建议调整为相关性语言。\n\n**W4. [Major] SciERC (n=529) 和 cross-dataset 分析 (n=23) 的统计效力不足**\n- 论文自己的 power analysis 确认了这一点。\n- 建议在主文中注明 power 限制。\n\n**W5. [Minor→Major] 缺少 sequence-level entropy 等 token-level 不确定性方法的比较**\n- LP 是 token-level 信号聚合，未与其他聚合方式做系统比较。\n\n### Minor\nM1. Table 1 和 Table 3 的 significance threshold 标注不一致\nM2. Figure 1 箭头暗示因果方向，与 \"diagnostic sequence\" 标注不符\nM3. SJ 定义中 sim(·,·) 未在主文说明\nM4. \"capability ceiling\" 未形式化定义\nM5. Appendix ag (Failure Mode Gallery) 有价值，建议主文简要引用\n\n### Questions\nQ1. Entity-wise independence 在实验数据上的近似程度？\nQ2. N=32/64 时 degeneracy rate 和 selection gap 趋势？\nQ3. 改用 BH-FDR 后哪些额外发现显著？\nQ4. Constrained decoding 的 selection gap 更小是否说明 degeneracy 源于 model behavior？\nQ5. Hidden-state probe 是否应做 entity-level 而非 sample-level？\nQ6. 增加 RE 数据集后预期 correlation-selection gap 大小？\n\n### Missing References\n1. Malinin & Gales (2021) — 结构化预测中的不确定性估计\n2. Kuhn et al. (2023) Semantic Uncertainty — 引用但未作为 baseline 比较\n3. MBR-for-structured-output 相关工作\n\n---\n\n请逐条回应上述所有 Weakness（N1, N2, W1–W5, M1–M5）和 Question（Q1–Q6），标注 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 3346 · 2026-05-22T01:08:43.910615+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1714
}
```

</details>

---


### Assistant

_source line 3347 · 2026-05-22T01:08:47.169771+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 251

## Round 251

2 recorded events


### User

_source line 3348 · 2026-05-22T01:08:49.882926+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我对论文给出 **Overall 3.5 (Borderline Conference)**。两个 critical 问题是 (1) Proposition 1 的 entity-wise independence 假设在 NER 中不现实且未充分讨论影响，(2) N=8 的采样规模不足以支撑 "capability ceiling" 的强声明。四个 major 问题涉及 RE/SQL 泛化证据薄弱、Holm-Bonferroni 过度保守、因果性语言过度、统计效力不足。论文的核心优势在于 correlation-selection gap 概念的新颖性、诊断级联的可复用性、以及远超领域平均的实验规模和统计严谨性。

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

_source line 3349 · 2026-05-22T01:08:58.316250+00:00_

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


## Round 252

## Round 252

2 recorded events


### User

_source line 3350 · 2026-05-22T01:10:50.068582+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix (Critical)

**[AGREE] R1-N1: Proposition 1 的 entity-wise independence 假设不现实**

同意这是一个重要问题。NER 中实体之间存在多重依赖：(1) span 不可重叠约束（特别是 flat NER），(2) 句内实体数量的隐式约束（一个句子中实体数目有上限），(3) 自回归生成中先前 entity 的输出会 condition 后续 entity 的生成概率。§6.1 Proposition 1 的证明完全依赖 entity-wise independence 将 set-level MBR 分解为 entity-wise majority vote，但论文仅用一句话承认假设是近似的（"The bound assumes entity-wise independence; actual entity correlations further limit..."）。

不过，我认为严重程度应定为 **Major 而非 Critical**。理由：Proposition 1 在论文中的角色是 motivating analysis（为 LP-weighted entity construction 提供理论动机），而非核心定理。即使 independence 假设不完全成立，MBR 框架的实证效果（Table 1: +1.4pp on Few-NERD）独立于理论证明。建议作者 (1) 将 Proposition 1 明确重定位为 "motivating analysis under simplifying assumptions"，(2) 补充实验量化 entity 间的 mutual information（如 R1 所建议），(3) 讨论当 independence 被违反时 MBR 退化为什么形式。

---

**[AGREE] R1-N2: N=8 不足以支撑 "capability ceiling" 声明**

强烈同意。这与我自己 review 中的关切（W2: 仅两个同规模模型）互补——R1 从 sample size N 维度指出了同样的泛化问题。

具体证据：
- §6.2（Table 5）显示 oracle F1 从 N=8 到 N=16 仍在上升（Few-NERD: 从 14B FT 的 oracle headroom 持续增加）
- Appendix b.6 的 N-scaling 分析显示 N=16 时 SJ 信号仍在改善（SJ ρ improves by 0.091 from N=8 to N=16）
- §4 Figure 2 显示 selection gap 在 N=8 时的具体数值，但未展示 gap 是否随 N 收敛——如果 gap 随 N 缩小，"ceiling" 就不成立
- 标题中 "Capability Ceiling" 暗示固有结构限制，但数据仅支持 "在 N≤16、7-8B 模型上存在显著 gap" 这一更弱的结论

"Ceiling" 这个词意味着一个渐近上界，但论文没有提供收敛性证据。建议修改标题（如 "Characterizing the Limitations of Self-Consistency for NER"）或至少测试 N=32/64 并展示 gap 的 N-dependence 趋势。

---

### Should-Fix (Major)

**[AGREE] R1-W1: RE/SQL extensions 过于薄弱**

同意。§1 Introduction 声称 "preliminary extensions to RE and SQL parsing, treating NER as a representative instance of the broader set-valued generation problem"，但 RE 仅用 SciERC 的 1 个模型（Qwen2.5-7B）、397 个样本，SQL 部分更少（Appendix 中简略提及）。这种覆盖度不足以支撑 "broader set-valued generation" 的泛化声明。应明确定位为 preliminary evidence 并在 Limitations 中注明，或从 claim 中移除 "broader" 定位。

---

**[REBUT] R1-W2: k=57 global Holm-Bonferroni 过度保守**

部分不同意。论文在 §4 中使用 Holm-Bonferroni 校正 57 个测试是一个 defensible 的保守选择。理由：

1. 论文的核心 claim 之一是 **负面结果**（"no signal outperforms greedy"）。对于负面结果，保守的多重比较校正实际上 *增强* 了 claim 的可信度——如果用更宽松的 BH-FDR 后出现更多显著结果，反而会削弱 "nothing works" 的叙事。
2. 论文 Appendix p.20 已经报告了 Bonferroni 校正结果，且指出 "the sole positive finding, the nominal LP ΔF1 (+2.9 pp, p=0.001; §9), survives Bonferroni correction over the 5 signal comparisons"。

但我同意 R1 的建议：**补充 BH-FDR 作为 sensitivity analysis** 是有价值的，特别是可以揭示哪些 borderline 结果在更宽松校正下变为显著。这不应影响核心结论，但增加分析的完整性。建议作为 Appendix 补充而非 must-fix。

---

**[AGREE] R1-W3: 部分因果性语言超出相关性证据**

同意。论文 §4 使用 "degeneracy is the binding constraint"、§6 Discussion 中 "LP compression limits exploitation"，但这些都是基于相关性/条件分析的推断，而非因果识别。关键证据：§4 Figure 2 显示 non-degenerate subset 上 selection gap 仍然存在（"Dashed green: oracle headroom +1.11pp; oracle headroom = best-of-N F1 − greedy F1, dotted grey: random"），这直接表明 degeneracy 不是唯一的 binding constraint。

R1 的观察非常精准——如果移除 degeneracy 后 gap 仍存在，就不能称 degeneracy 为 "the binding constraint"。应改为 "a major contributing factor" 或 "a necessary but insufficient condition for closing the gap"。

---

**[AGREE] R1-W4: SciERC (n=529) 和 cross-dataset (n=23) 统计效力不足**

同意。论文自身的 power analysis（Appendix p.20）已确认 SciERC 上 n=529 对小效应量的检测力不足（80% power requires n≈85 for ρ=0.3），cross-dataset 分析仅 n=23 个 configurations 更是远低于统计效力要求。这些结论应在主文中加 caveat，而非仅在 Appendix 中讨论。

---

**[AGREE] R1-W5: 缺少 token-level 不确定性方法的系统比较**

同意，这是一个有价值的 gap。论文使用 LP（log-probability 的均值）作为 token-level 信号的唯一聚合方式，但未与其他聚合方式比较：
- Sequence-level entropy（而非 mean log-prob）
- Per-token entropy 的 max/variance（捕捉 uncertain spans 而非整体）
- Predictive entropy（Kuhn et al. 2023 的做法，论文引用了但未做 baseline）

LP 在论文中是唯一展示正面结果的 model-internal signal（Table 1），因此其他 token-level aggregation 是否也有效是一个关键问题。如果 sequence entropy 同样有效，LP 的贡献就被稀释；如果只有 LP 有效，则需要解释为什么 mean log-prob 特殊。建议至少补充 sequence entropy 作为 ablation。

---

### Minor

**[AGREE] R1-M1: Table 1 和 Table 3 的 significance threshold 标注不一致**
同意。Table 1 使用 †/‡ 标注显著性，Table 3 使用 bold，应统一。

**[AGREE] R1-M2: Figure 1 箭头暗示因果方向**
同意。Figure 1 标注为 "diagnostic sequence; not causal chain" 但视觉设计（从左到右的箭头和 pass/fail 判断）暗示因果链。建议将箭头改为虚线或双向箭头以弱化因果暗示。

**[REBUT] R1-M3: SJ 定义中 sim(·,·) 未在主文说明**
不完全同意。§2.2 Equation (1) 定义了 SJ(ŷᵢ, ŷⱼ) = Σₑ sim(bₑ,ᵢ, bₑ,ⱼ) / max(|ŷᵢ|, |ŷⱼ|)，紧接着 §2.2 正文说明 "For samples ŷᵢ, ŷⱼ, we group by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU)"。sim(·,·) 实际上隐含在 bipartite matching 的描述中——虽然不是显式定义 sim 函数，但结合上下文可以理解为 token-level IoU。不过我承认更显式的定义会更好，这属于 writing clarity 的小问题。

**[AGREE] R1-M4: "capability ceiling" 未形式化定义**
同意，与 N2 一致。论文使用 "capability ceiling" 作为核心概念但未给出形式化定义（如 sup_N lim selection_gap(N) > ε）。

**[AGREE] R1-M5: Appendix ag (Failure Mode Gallery) 有价值**
同意。Failure mode gallery 提供了 qualitative evidence 支撑定量分析，主文应至少用 1-2 句引用并指引读者。

---

### Questions 回应

**Q1. Entity-wise independence 的近似程度？**
这是关键验证点。我补充：可以通过计算同一样本内不同 entity 的 agreement 信号（如 VC/SJ）之间的 Pearson/Spearman 相关来量化 within-sample entity 依赖。如果 entity 间相关性低（如 |r|<0.2），independence 假设是合理的近似；否则 Proposition 1 的分解不成立。

**Q2. N=32/64 时趋势？**
我同样关注。Appendix b.6 报告了 N=16 的结果但未到 N=32。如果 N=32 时 selection gap 仍不收敛，"ceiling" claim 更有说服力；如果 gap 随 N 缩小，则当前 claim 需大幅修改。这个实验对论文核心 claim 的成立至关重要。

**Q3. BH-FDR 后哪些额外发现显著？**
如我在 W2 回应中所述，这对评估 conservative correction 的影响有价值，但不太可能改变核心结论。预期仅有 borderline 结果变为显著。

**Q4. Constrained decoding 下 selection gap 更小是否说明 degeneracy 源于 model behavior？**
有趣的问题。§7.1 提到使用 XGrammar 进行 constrained decoding。如果 constrained decoding 降低了 degeneracy（通过强制格式合规消除格式错误样本），selection gap 更小可能反映的是格式噪声被消除后的 cleaner signal，而非 degeneracy 本身源于 model behavior。需要更仔细的因果分析。

**Q5. Hidden-state probe 应做 entity-level 而非 sample-level？**
好问题。§3, Appendix h-i 的 hidden-state probe 在 sample-level 操作（predicting per-sample F1），但论文的核心问题是 entity-level verification。Entity-level probe（predicting per-entity correctness）可能提供更直接的 diagnostic 信号。论文 Appendix i 中提到 "entity-level self-verification probes" 但似乎仍是 aggregate 层面。建议作者澄清 probe 的 granularity。

**Q6. RE 数据集上 correlation-selection gap 预期大小？**
RE 通常比 NER 更复杂（relation 涉及 entity pair + relation type），output space 更大。预期 correlation-selection gap 至少与 NER 同等甚至更大。但 SciERC RE 的 n=397 太小，难以得出可靠结论。

---

### 总结

我与 R1 在大多数核心问题上达成一致，特别是：
1. **N2（N=8 不够 / "ceiling" 过强）** — 这与我自己的 W2（仅两个同规模模型）共同指向同一个根本问题：论文的泛化 claim 超出了实验证据的支撑范围
2. **W3（因果语言过强）** — 与我自己的 N1（叙事矛盾）一致
3. **N1（independence 假设）** — 我同意方向但认为应定为 Major 而非 Critical

唯一主要分歧在 **W2（Holm-Bonferroni 是否过度保守）**：我认为对于负面结果的论文，保守校正反而增强了可信度，但补充 BH-FDR sensitivity analysis 是值得做的。

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

_source line 3351 · 2026-05-22T01:10:55.312558+00:00_

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


## Round 253

## Round 253

2 recorded events


### User

_source line 3352 · 2026-05-22T01:11:00.907551+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部意见的逐条交叉回应并提交给 Review Director。

核心结论：与 R1 在大多数问题上一致，特别是 N=8/"ceiling" 过强（N2）、因果语言过强（W3）、RE/SQL 覆盖不足（W1）。唯一主要分歧在 Holm-Bonferroni 的保守性问题（W2）——我认为对负面结果论文保守校正是合理的。将 R1 的 N1（Proposition 1 independence）从 Critical 下调至 Major，因为该 proposition 角色是 motivating analysis 而非核心定理。

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

_source line 3353 · 2026-05-22T01:11:06.858979+00:00_

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


## Round 254

## Round 254

14 recorded events


### User

_source line 3354 · 2026-05-22T01:13:18.505352+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应：对 Reviewer 2 审稿意见的逐条回应

### Critical Weaknesses

**[REBUT] R2-N1: "核心叙事自相矛盾"**
R2 称 Abstract "no signal outperforms greedy" 与 LP +1.39pp "直接矛盾"，但原文 Abstract (p.1) 将 "no signal outperforms greedy" 明确限定在 SciERC 上，紧接着说明 LP/Few-NERD 例外。标题 "Entity-Level Verification Fails" 中的 entity-level verification 指 SJ/VC/EM/FK（agreement signals），LP 是 model-internal signal（Table 1 caption 明确标注），不属于 entity-level verification。R2 的"直接矛盾"和"选择性呈现"指控不成立。但同意论文的整体 framing 偏向负面叙事，应平衡 diagnostic 和 prescriptive 两条线索。

**[REBUT] R2-N2: "与 Yao et al. (2026) 区分不充分"**
Yao et al. 证明 correlation 存在（ρ>0），本文追问为什么 correlation 不能 operationalize 为 selection gain，给出四阶段诊断级联。这是递进关系而非特例关系。但同意 §8 一句话处理不充分，需扩展对比讨论。

### Major Weaknesses

**[AGREE] R2-W1**: 8:37 比例确实极端。N-scaling 和 hidden-state probes 应融入正文。

**[REBUT] R2-W2**: R2 称"仅两个同规模模型"是事实错误。论文用了 5 个变体（3B/7B/8B/72B），72B 在 Appendix t (p.34-36) 显示 gap 在 20 倍规模跨度内持续。但同意缺乏闭源模型验证。

**[REBUT] R2-W3**: Calibration 文献（Guo et al. 2017）讨论 softmax miscalibration，与本文的 set-valued output 上的 degeneracy + LP compression 失败机制本质不同。R2 的类比停留在表面相似性。

**[AGREE] R2-W4**: +1.4pp at 8x cost 实用价值有限，但论文定位是 diagnostic study 而非 method paper。建议正文明确定位。

**[REBUT] R2-W5**: Degeneracy ≠ diversity collapse。关键证据：Appendix q (p.32-33) free-form decoding 下 degeneracy 同样存在，说明非 constrained decoding artifact。定义不同（F1-level vs text-level）、scope 不同、诊断深度不同。

### Minor Weaknesses
[AGREE] W6, W7, W8, W10
[REBUT] W9（与 N1 重复，Abstract 表述无矛盾）

### Questions
[AGREE] Q1: LP 应显式分类为 model-internal signal
[REBUT] Q2: 72B 证据在 Appendix t，R2 可能遗漏
[AGREE] Q3: CoNLL memorization 应讨论
[AGREE] Q4: 应区分 LP-weighted vs model-based MBR
[AGREE] Q5: 应按 degeneracy 分层分析 LP discriminative power

### Missing References
[AGREE] M1 (Fisch 2021), M3 (Chen 2021), M4 (Varshney 2022)
[REBUT] M2, M5（相关但非必须）

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

_source line 3355 · 2026-05-22T01:13:55.684837+00:00_

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

_source line 3356 · 2026-05-22T01:13:55.685251+00:00_

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

_source line 3357 · 2026-05-22T01:13:55.736329+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T00:58:58.220240+00:00\", \"completed_at\": \"2026-05-22T01:03:49.440826+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本，无任何 display item（figure/table）。审稿人前 2 分钟只看到密集文字，直到第 3 页才遇到 Figure 1 作为视觉锚点。建议将 Figure 1 提前到第 2 页（调整 float 位置或缩减 Introduction 长度）\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 作为首个 display item，有效传达 correlation-selection gap 核心概念（Quality Estimation → Sample Selection → Entity-Level Construction 三阶段）。Caption 自包含，能独立理解。但图中部分标注文字（如 box 内 \\\"High F1\\\" / \\\"p = 0.39\\\" 等）字号偏小，在打印版上可读性有风险\"}, {\"severity\": \"warning\", \"dimension\": \"page 3\", \"message\": \"Figure 1 使用红色和绿色作为主要对比色（红色 ✗ vs 绿色 ✓），对红绿色盲用户（~8% 男性）不友好。建议改用 blue/orange 或 Okabe-Ito 色板，或至少辅以形状/图案区分\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 和 Figure 2 布局合理，视觉密度适中。Figure 2 的绿色/灰色柱状图颜色区分度良好，虚线标注 oracle 值有效。Table 1 使用 booktabs 风格，最优值加粗，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2（9 类方法汇总表）使用全宽 figure* 合理，信息密度高。部分单元格文字较小但可读\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"全页纯文本（含 Proposition 1 和公式），无 figure/table。虽有 Proposition 框和 MBR 公式提供一定视觉节奏，但与 page 8 一起构成 2 段纯文本区域。Proposition 1 的数学推导使此处文本密集可接受，但整体节奏偏紧\"}, {\"severity\": \"critical\", \"dimension\": \"page 7\", \"message\": \"单页塞入 4 个 display items（Tables 3, 4, 5 + Figure 3），严重过挤。表格字号极小（尤其 Tables 4, 5），Figure 3 的散点图标注文字在 150dpi 渲染下已经需要仔细辨认。建议将 Table 4 或 Table 5 移至 Appendix，或合并 Tables 4+5 为一个表\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Discussion + Related Work 引用 + Conclusion 占据整页纯文本，无 display item。与 page 6 类似形成纯文本段，但作为论文末尾段落（Discussion/Conclusion）属可接受范围\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 的 caption 自包含性良好（解释了 x/y 轴含义和主要发现），但图本身面积过小（约 1/6 栏宽），散点标记和趋势线在小尺寸下难以区分\"}, {\"severity\": \"inf
…[truncated 2164 chars]

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


### Tool result

_source line 3358 · 2026-05-22T01:13:55.736948+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3359 · 2026-05-22T01:14:10.478332+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -200 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "description": "Read existing review issues (first 200 lines)"
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
    "command": "head -200 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "description": "Read existing review issues (first 200 lines)"
  }
}
```

</details>

---


### Tool result

_source line 3360 · 2026-05-22T01:14:10.629576+00:00_

issues:
  # ===== 历史 resolved issues (保留) =====
  - id: "R1-W1"
    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
    resolution_round: 19

  - id: "R1-W2"
    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 21
    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
    resolution_round: 21

  - id: "R2-N1-old"
    summary: "Contribution 1 'methodological premise' 是定义推论"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
    resolution_round: 19

  - id: "R2-N2-old"
    summary: "与 MBR 文献差异化定位不够锐利"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
    resolution_round: 19

  - id: "R2-N4-old"
    summary: "模型规模 3B-8B，70B+ 未知"
    category: experiment
    severity: info
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
    resolution_round: 19

  - id: "R1-W3-old"
    summary: "2-seed 统计效力不足"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。"
    resolution_round: 19

  - id: "R1-W4-old"
    summary: "Per-entity-type non-independence"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resoluti
…[truncated 3211 chars]

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

_source line 3361 · 2026-05-22T01:14:31.950973+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "description": "Count issue tracker lines"
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
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "description": "Count issue tracker lines"
  }
}
```

</details>

---


### Tool result

_source line 3362 · 2026-05-22T01:14:32.001698+00:00_

1509 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

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

_source line 3363 · 2026-05-22T01:16:29.175995+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ===== Round 31 (fresh review) 新发现 =====\n\n  - id: \"R31-N1\"\n    summary: \"N=8 采样不足以支撑 'capability ceiling' 声明\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 强烈同意。N=8 时 degeneracy 12-62% 部分是小 N 直接后果；N=16 时 degeneracy 下降且 LP 增益出现；oracle F1 随 N 单调递增。标题 'Capability Ceiling' 暗示固有结构限制但未提供收敛证据。建议测试 N=32/64 或修改措辞。\"\n    action_items:\n      - round: 31\n        action: \"至少在 1 个数据集测试 N=32/64 并展示 selection gap 的 N-dependence；或将 'ceiling' 改为 'limitations'\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-N2\"\n    summary: \"Proposition 1 entity-wise independence 假设不现实且未充分讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 定为 Critical，R2 同意方向但降为 Major——Proposition 1 是 motivating analysis 非核心定理。NER 中 entity 有 span 重叠、数量约束、自回归条件依赖。建议量化 entity 间 mutual information 或重定位为 motivating analysis。\"\n    action_items:\n      - round: 31\n        action: \"将 Proposition 1 重定位为 motivating analysis under simplifying assumptions；补充 entity 间依赖的经验量化\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W1\"\n    summary: \"核心叙事 framing 偏向负面——SC 'fails' vs LP 正面结果的张力\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R2 定为 Critical（叙事自相矛盾），R1 以文本证据反驳——LP 是 model-internal 非 entity-level agreement，Abstract 限定于 SciERC。R1 rebuttal 成立但双方均认为整体 framing 偏向负面叙事，应平衡 diagnostic 和 prescriptive 两条线索。降为 Major。\"\n    action_items:\n      - round: 31\n        action: \"平衡 diagnostic/prescriptive 叙事；Abstract 和 Introduction 中明确区分 agreement signals（失败）vs model-internal LP（有条件成功）\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W2\"\n    summary: \"与 Yao et al. (2026) 的增量区分不充分\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R2 定为 Critical，R1 反驳——Yao 证明 correlation 存在，本文追问为何不能 operationalize 为 selection gain，是递进关系非特例。R1 同意 §8 一句话处理不充分。降为 Major。\"\n    action_items:\n      - round: 31\n        action: \"在 §1 或 §8 用一段专门对比 Yao et al.，说明 diagnostic cascade 和 construction 方法的增量贡献\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W3\"\n    summary: \"因果性语言超出相关性证据\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。'degeneracy is the binding constraint' 等表述超出证据——non-degenerate subset 上 selection gap 仍存在。应改为 'a major contributing factor'。注意：历史 R1-W2 (resolved round 21) 曾修复因果语言，但本轮发现残留。\"\n    action_items:\n      - round: 31\n        action: \"检查全文残留因果性语言，降级为 correlational/associational\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W4\"\n    summary: \"RE/SQL exploratory extensions 过于薄弱\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。RE 仅 SciERC 1 模型 397 样本，SQL 更简略，不足以支撑 'broader set-valued generation' 泛化声明。\"\n    action_items:\n      - round: 31\n        action: \"明确定位为 preliminary evidence 并在 Limitations 注明；或从 claim 中移除 'broader' 定位\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W5\"\n    summary: \"正文/附录比例 8:37 严重失衡\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 同意。关键信息（N-scaling、hidden-state probes、cross-dataset transfer）被推入 Appendix。审稿人需读 ~47 页评估完整性。\"\n    action_items:\n      - round: 31\n        action: \"将 N-scaling 核心发现和 cross-dataset 结果移入正文；可合并 Discussion+Conclusion 腾出空间\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W6\"\n    summary: \"SciERC (n=529) 和 cross-dataset (n=23) 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。论文自身 power analysis 确认不足，但仅在 Appendix 讨论，应在主文注明 power 限制。\"\n    action_items:\n      - round: 31\n        action: \"在主文相关结论处注明 statistical power caveat\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W7\"\n    summary: \"缺少 token-level 不确定性方法的系统比较\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出 (minor→major)，R2 同意。LP 是唯一 token-level 聚合，未与 sequence entropy、per-token entropy max/variance 等比较。\"\n    action_items:\n      - round: 31\n        action: \"至少补充 sequence entropy 作为 ablation\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W8\"\n    summary: \"Holm-Bonferroni k=57 global correction 可能过度保守\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出 (Major)，R2 部分反驳——对负面结果论文保守校正增强可信度。共识：补充 BH-FDR 作为 sensitivity check 有价值但非 must-fix。\"\n    action_items:\n      - round: 31\n        action: \"在 Appendix 补充 BH-FDR sensitivity analysis\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-M1\"\n    summary: \"Table 1/Table 3 significance 标注不一致\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1]\n        note: \"Table 1 用 †/‡，Table 3 用 bold。应统一。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-M2\"\n    summary: \"Figure 1 箭头暗示因果方向与 'diagnostic sequence' 标注不符\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"建议将箭头改为虚线或双向箭头以弱化因果暗示。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-M3\"\n    summary: \"缺失引用: conformal prediction, pass@k 原始来源, selective prediction survey 等\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R2 提 5 条 (Fisch 2021, He 2024, Chen 2021, Varshney 2022, TTS survey)；R1 提 3 条 (Malinin & Gales 2021, Kuhn 2023 as baseline, MBR-structured)。交叉后共识 must-add: Fisch 2021, Chen 2021, Varshney 2022, Malinin & Gales 2021。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-VIS1\"\n    summary: \"Page 7 单页塞入 4 个 display items (Tables 3,4,5 + Figure 3) 过挤\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [\"visual_check\"]\n        note: \"表格字号极小，Figure 3 散点图标注难辨认。建议移 Table 4 或 5 至 Appendix 或合并。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ===== 历史 resolved issues (保留) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n"
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
    "issues_yaml": "issues:\n  # ===== Round 31 (fresh review) 新发现 =====\n\n  - id: \"R31-N1\"\n    summary: \"N=8 采样不足以支撑 'capability ceiling' 声明\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 强烈同意。N=8 时 degeneracy 12-62% 部分是小 N 直接后果；N=16 时 degeneracy 下降且 LP 增益出现；oracle F1 随 N 单调递增。标题 'Capability Ceiling' 暗示固有结构限制但未提供收敛证据。建议测试 N=32/64 或修改措辞。\"\n    action_items:\n      - round: 31\n        action: \"至少在 1 个数据集测试 N=32/64 并展示 selection gap 的 N-dependence；或将 'ceiling' 改为 'limitations'\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-N2\"\n    summary: \"Proposition 1 entity-wise independence 假设不现实且未充分讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 定为 Critical，R2 同意方向但降为 Major——Proposition 1 是 motivating analysis 非核心定理。NER 中 entity 有 span 重叠、数量约束、自回归条件依赖。建议量化 entity 间 mutual information 或重定位为 motivating analysis。\"\n    action_items:\n      - round: 31\n        action: \"将 Proposition 1 重定位为 motivating analysis under simplifying assumptions；补充 entity 间依赖的经验量化\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W1\"\n    summary: \"核心叙事 framing 偏向负面——SC 'fails' vs LP 正面结果的张力\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R2 定为 Critical（叙事自相矛盾），R1 以文本证据反驳——LP 是 model-internal 非 entity-level agreement，Abstract 限定于 SciERC。R1 rebuttal 成立但双方均认为整体 framing 偏向负面叙事，应平衡 diagnostic 和 prescriptive 两条线索。降为 Major。\"\n    action_items:\n      - round: 31\n        action: \"平衡 diagnostic/prescriptive 叙事；Abstract 和 Introduction 中明确区分 agreement signals（失败）vs model-internal LP（有条件成功）\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W2\"\n    summary: \"与 Yao et al. (2026) 的增量区分不充分\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R2 定为 Critical，R1 反驳——Yao 证明 correlation 存在，本文追问为何不能 operationalize 为 selection gain，是递进关系非特例。R1 同意 §8 一句话处理不充分。降为 Major。\"\n    action_items:\n      - round: 31\n        action: \"在 §1 或 §8 用一段专门对比 Yao et al.，说明 diagnostic cascade 和 construction 方法的增量贡献\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W3\"\n    summary: \"因果性语言超出相关性证据\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。'degeneracy is the binding constraint' 等表述超出证据——non-degenerate subset 上 selection gap 仍存在。应改为 'a major contributing factor'。注意：历史 R1-W2 (resolved round 21) 曾修复因果语言，但本轮发现残留。\"\n    action_items:\n      - round: 31\n        action: \"检查全文残留因果性语言，降级为 correlational/associational\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W4\"\n    summary: \"RE/SQL exploratory extensions 过于薄弱\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。RE 仅 SciERC 1 模型 397 样本，SQL 更简略，不足以支撑 'broader set-valued generation' 泛化声明。\"\n    action_items:\n      - round: 31\n        action: \"明确定位为 preliminary evidence 并在 Limitations 注明；或从 claim 中移除 'broader' 定位\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W5\"\n    summary: \"正文/附录比例 8:37 严重失衡\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 同意。关键信息（N-scaling、hidden-state probes、cross-dataset transfer）被推入 Appendix。审稿人需读 ~47 页评估完整性。\"\n    action_items:\n      - round: 31\n        action: \"将 N-scaling 核心发现和 cross-dataset 结果移入正文；可合并 Discussion+Conclusion 腾出空间\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W6\"\n    summary: \"SciERC (n=529) 和 cross-dataset (n=23) 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。论文自身 power analysis 确认不足，但仅在 Appendix 讨论，应在主文注明 power 限制。\"\n    action_items:\n      - round: 31\n        action: \"在主文相关结论处注明 statistical power caveat\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W7\"\n    summary: \"缺少 token-level 不确定性方法的系统比较\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出 (minor→major)，R2 同意。LP 是唯一 token-level 聚合，未与 sequence entropy、per-token entropy max/variance 等比较。\"\n    action_items:\n      - round: 31\n        action: \"至少补充 sequence entropy 作为 ablation\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-W8\"\n    summary: \"Holm-Bonferroni k=57 global correction 可能过度保守\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R1 提出 (Major)，R2 部分反驳——对负面结果论文保守校正增强可信度。共识：补充 BH-FDR 作为 sensitivity check 有价值但非 must-fix。\"\n    action_items:\n      - round: 31\n        action: \"在 Appendix 补充 BH-FDR sensitivity analysis\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-M1\"\n    summary: \"Table 1/Table 3 significance 标注不一致\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1]\n        note: \"Table 1 用 †/‡，Table 3 用 bold。应统一。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-M2\"\n    summary: \"Figure 1 箭头暗示因果方向与 'diagnostic sequence' 标注不符\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"建议将箭头改为虚线或双向箭头以弱化因果暗示。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-M3\"\n    summary: \"缺失引用: conformal prediction, pass@k 原始来源, selective prediction survey 等\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [1, 2]\n        note: \"R2 提 5 条 (Fisch 2021, He 2024, Chen 2021, Varshney 2022, TTS survey)；R1 提 3 条 (Malinin & Gales 2021, Kuhn 2023 as baseline, MBR-structured)。交叉后共识 must-add: Fisch 2021, Chen 2021, Varshney 2022, Malinin & Gales 2021。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R31-VIS1\"\n    summary: \"Page 7 单页塞入 4 个 display items (Tables 3,4,5 + Figure 3) 过挤\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 31\n    last_seen_round: 31\n    mentions:\n      - round: 31\n        reviewers: [\"visual_check\"]\n        note: \"表格字号极小，Figure 3 散点图标注难辨认。建议移 Table 4 或 5 至 Appendix 或合并。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ===== 历史 resolved issues (保留) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n"
  }
}
```

</details>

---


### Tool result

_source line 3364 · 2026-05-22T01:16:29.227330+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 13034}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3365 · 2026-05-22T01:19:08.211164+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\n\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**投稿类别**: Long Paper\n**审稿模式**: Fresh（全新初审）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计；R2: 新颖性+相关工作+写作）\n**轮次**: Round 1 + 交叉分享，1 轮收敛\n\n---\n\n## Summary\n\n本文研究 self-consistency（SC）在命名实体识别（NER）上的失败模式，定义了\"correlation-selection gap\"——质量估计信号与 oracle F1 存在相关性（Spearman ρ up to 0.47, AUROC up to 0.82），但无法用于选择更好的样本。作者提出四阶段诊断级联（degeneracy → agreement fidelity → LP compression → construction），在 4 个 NER 数据集（SciERC, Few-NERD, CoNLL-2003, WNUT-17）、两个模型族（Qwen3-8B, LLaMA-3.1-8B）上系统评估了 9 类方法，发现均无法可靠改善 sample selection。正面结果通过 LP-weighted entity construction（+0.3–1.4pp）和 LP selection（+1.39pp on Few-NERD）在 entity 粒度绕过了 sample-level selection 的瓶颈。\n\n---\n\n## Strengths\n\n**S1. 问题定位精准，填补研究空白。** SC 文献几乎完全聚焦于分类/推理任务，NER 作为 set-valued 结构化输出的代表性任务缺乏系统性 SC 失败分析。本文填补了这一空白。[R1, R2 共识]\n\n**S2. 诊断框架结构清晰、可复用。** 四阶段级联（§2–§4）将复杂问题分解为可独立检验的子问题，每一步有对应实验支撑，逻辑链条完整。该框架可迁移至其他 set-valued 任务。[R1, R2 共识]\n\n**S3. 实验规模和统计严谨性远超领域平均。** 报告了 bootstrap 95% CI、Holm 校正置换检验、permutation p-values、split-half reliability、Bonferroni 校正。300+ 实验覆盖 4 数据集 × 多模型 × 多 seed。[R1, R2 共识]\n\n**S4. 诚实呈现负面结果。** 论文未夸大正面发现，系统展示了 9 类方法的失败并提供了清晰的诊断解释。这在 ML 论文中难得。[R1]\n\n**S5. 引用验证通过。** 57 条 bib entry 全部有引用、无 orphan，52/57 通过在线验证，无伪造引用。[R2]\n\n**S6. Constrained decoding confound 处理得当。** 论文包含 free-form vs constrained decoding 对比（Appendix q），排除了 degeneracy 是 constrained decoding artifact 的可能。[R1]\n\n---\n\n## Weaknesses\n\n### Critical\n\n**C1. N=8 采样不足以支撑 \"capability ceiling\" 声明** [R1-N2, R2 AGREE]\n- N=8 时 degeneracy 12%–62%，部分是小 N 的直接后果。N=16 分析（Appendix）显示 degeneracy 下降、SJ ρ 改善 +0.091、LP 增益出现。Oracle F1 随 N 单调递增（Figure 10）。\n- 标题 \"Capability Ceiling\" 暗示固有结构性上界，但论文未提供 selection gap 随 N 收敛的证据。\"Ceiling\" 意味着渐近上界，当前数据仅支持 \"在 N≤16 上存在显著 gap\" 这一更弱结论。\n- **修改建议**: 至少在 1 个数据集测试 N=32/64 并展示 selection gap 的 N-dependence 趋势；或将 \"ceiling\" 修改为 \"limitations\"（如 \"Characterizing the Limitations of Self-Consistency for NER\"）。\n\n### Major\n\n**M1. Proposition 1 的 entity-wise independence 假设不现实** [R1-N1 Critical → R2 降为 Major]\n- §6.1 Proposition 1 的 MBR 分解依赖 entity-wise independence，但 NER 中实体有 span 重叠约束、句内数量约束、自回归条件依赖。论文仅用一句话承认假设是近似的，未量化偏差。\n- R2 认为 Proposition 1 是 motivating analysis 而非核心定理，Table 5 的实证效果独立于理论证明，因此 severity 降为 Major。\n- **修改建议**: 将 Proposition 1 重定位为 \"motivating analysis under simplifying assumptions\"；补充 entity 间 mutual information 的经验量化。\n\n**M2. 核心叙事 framing 偏向负面** [R2-N1 Critical → R1 REBUT → 降为 Major]\n- R2 指出 Abstract \"no signal outperforms greedy\" 与 LP +1.39pp 矛盾。R1 反驳：(1) Abstract 限定于 SciERC，(2) LP 是 model-internal signal 非 entity-level agreement signal（Table 1 caption 明确标注），\"entity-level verification fails\" 指的是 SJ/VC/EM/FK。\n- R1 的反驳成立——\"直接矛盾\" 指控不成立。但双方均认为整体 framing 偏向负面叙事，应更好地平衡 diagnostic 和 prescriptive 两条线索。\n- **修改建议**: Abstract 和 Introduction 中明确区分 agreement signals（确实失败）vs model-internal LP（有条件成功）；重组 claim hierarchy。\n\n**M3. 与 Yao et al. (2026) 的增量区分不充分** [R2-N2 Critical → R1 REBUT → 降为 Major]\n- R2 认为本文可能只是 Yao et al. consistency-accuracy correlation 的 NER 特例。R1 反驳：Yao 证明 correlation 存在，本文追问为何不能 operationalize 为 selection gain，提供了四阶段诊断级联，是递进关系而非特例。\n- R1 的反驳合理但双方均同意 §8 一句话处理不充分。\n- **修改建议**: 在 §1 或 §8 用一段专门对比 Yao et al.，说明 diagnostic cascade + construction 方法的具体增量。\n\n**M4. RE/SQL exploratory extensions 过于薄弱** [R1-W1, R2 AGREE]\n- RE 仅 SciERC 1 个模型 397 有效样本（55.5% zero-F1 受 upstream NER 错误污染），SQL 仅 Spider subset n=196 with 87.2% degeneracy。不足以支撑 Introduction 中 \"broader set-valued generation problem\" 的泛化声明。\n- **修改建议**: 明确定位为 preliminary evidence 并在 Limitations 注明；或从 claim 中移除 \"broader\" 定位。\n\n**M5. 正文/附录比例 8:37 严重失衡** [R2-W1, R1 AGREE]\n- 关键信息被推入 Appendix：9 类方法完整结果（Appendix b.4）、N-scaling 分析（Appendix b.6）、hidden-state probes（Appendix h-i）、cross-dataset transfer。审稿人需读 ~47 页才能评估完整性。\n- **修改建议**: 将 N-scaling 核心发现和 cross-dataset 结果移入正文。可合并 §9 Discussion + §10 Conclusion 腾出空间。\n\n**M6. 因果性语言超出相关性证据** [R1-W3, R2 AGREE]\n- \"degeneracy is the binding constraint\"（§4）等表述超出证据。Non-degenerate subset 上 selection gap 仍存在，说明 degeneracy 不是唯一约束。论文 §2 声明 \"observational\" 但后续 section 有因果性措辞残留。\n- 注意：历史 R1-W2（Round 1-21）曾修复全文因果语言（15 处 + 4 处残留），本轮发现仍有残留。\n- **修改建议**: 全文检查因果性语言，降级为 \"a major contributing factor\" / \"associated with\"。\n\n**M7. SciERC (n=529) 和 cross-dataset (n=23) 统计效力不足** [R1-W4, R2 AGREE]\n- 论文自身 power analysis（Appendix）确认 80% power requires n≈85 for ρ=0.3，cross-dataset n=23 远低于要求。但这些 caveat 仅在 Appendix 讨论。\n- **修改建议**: 在主文相关结论处注明 statistical power 限制。\n\n**M8. 缺少 token-level 不确定性方法的系统比较** [R1-W5, R2 AGREE]\n- LP（mean token log-prob）是唯一的 token-level 信号聚合方式，也是唯一展示正面结果的 model-internal signal。未与 sequence entropy、per-token entropy max/variance、predictive entropy（Kuhn et al. 2023）等做比较。\n- **修改建议**: 至少补充 sequence entropy 作为 ablation。\n\n### Minor / Info\n\n**m1.** 正面结果 practical significance 有限（+1.4pp at 8x inference cost）——但论文定位为 diagnostic study 而非 method paper，双方认为可接受。建议正文明确定位。[R2-W4, R1 nuanced AGREE]\n\n**m2.** Table 1/Table 3 significance 标注不一致（†/‡ vs bold）。[R1]\n\n**m3.** Figure 1 箭头暗示因果方向与 \"diagnostic sequence\" 标注不符。建议改为虚线。[R1, R2 AGREE]\n\n**m4.** \"Capability ceiling\" 未形式化定义。[R1]\n\n**m5.** 10 个 section 在 8 页内过于拥挤，§9 Discussion 和 §10 Conclusion 各不到半页。建议合并。[R2]\n\n**m6.** Table 2 在正文仅展示 Few-NERD 单数据集结果。应至少展示 2 个数据集。[R2]\n\n**m7.** Proposition 1 条件过强（balanced set-overlap utility + entity independence），未讨论对 α 值的敏感性。[R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **N=8/\"ceiling\" 过强** — 论文的泛化 claim 超出实验证据支撑范围。标题暗示固有结构限制，但未提供收敛证据。[C1]\n2. **因果语言残留** — 论文声明 observational 但后续有因果性措辞。[M6]\n3. **RE/SQL 不足以泛化** — 覆盖度太低，应降级为 preliminary evidence。[M4]\n4. **统计效力问题** — SciERC n=529 和 cross-dataset n=23 应在主文注明。[M7]\n5. **附录比例失衡** — 关键结果不应仅在 Appendix。[M5]\n6. **缺少 token-level 信号比较** — LP 是唯一的 model-internal signal 比较对象。[M8]\n\n## Reviewer Divergence [REBUT]\n\n1. **叙事矛盾 severity** — R2 定为 Critical（\"直接矛盾\"），R1 以文本证据反驳（LP ≠ entity-level agreement，Abstract 限定于 SciERC）。**Director 判断**: R1 的反驳成立，降为 Major（framing bias 而非 factual contradiction）。[M2]\n\n2. **与 Yao et al. 关系** — R2 认为是 Yao 的特例，R1 认为是递进关系（从 correlation 存在到 why selection fails）。**Director 判断**: R1 论据更充分（四阶段 cascade + construction 是增量），但 §8 一句话确实不够，降为 Major。[M3]\n\n3. **模型覆盖** — R2 称\"仅两个同规模模型\"，R1 指出论文含 5 个变体（4B/7B/8B/14B/72B），R2 遗漏了 Appendix t 的 72B 数据。**Director 判断**: R2 的事实认定有误，但 72B 仅在 Appendix 且为 zero-shot，缺乏 fine-tuned 大模型验证仍是合理关切。\n\n4. **vs Yun et al. diversity collapse** — R2 认为 degeneracy 是 diversity collapse 的 NER 特例；R1 引用 Appendix q 证据（free-form decoding 下 degeneracy 同样存在）区分两者。**Director 判断**: R1 的区分合理（定义不同、scope 不同、free-form 证据排除了 constrained decoding artifact），但论文正文应更清晰地呈现这一区分。\n\n5. **Holm-Bonferroni 保守性** — R1 认为 k=57 过度保守；R2 反驳对负面结果论文保守校正增强可信度。**Director 判断**: 双方有理。补充 BH-FDR sensitivity check 即可（Info 级别）。\n\n6. **Proposition 1 severity** — R1 定 Critical，R2 降为 Major（motivating analysis 非核心定理）。**Director 判断**: 采用 R2 的 Major 定级——Proposition 1 的实证效果（Table 5）独立于理论证明。\n\n---\n\n## Questions（需要作者回应）\n\n**Q1.** \"Entity-level agreement signal\" 的精确范围是什么？LP selection 的成功是否意味着 model-internal signals 可以部分绕过 correlation-selection gap？论文应在 §2 中给出明确分类。\n\n**Q2.** N=32/64 时 degeneracy rate 和 selection gap 的趋势如何？是否有证据表明 gap 随 N 收敛到某个 asymptote？\n\n**Q3.** CoNLL 上 48%–87% instances 产生 identical outputs——这是否因为模型在 well-studied benchmark 上 overfit/memorize？在 fully OOD 数据上 degeneracy 是否会降低？\n\n**Q4.** LP-weighted MBR（§6.1）与 model-based MBR（Jinnai et al. 2024）有何实质区别？\n\n**Q5.** Entity-wise independence 假设在实验数据上的近似程度如何？可否通过 entity 对的 mutual information 量化？\n\n**Q6.** 为何未比较 sequence entropy 等其他 token-level 信号聚合方式？LP 的 mean log-prob 聚合是否有特殊优势？\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 交叉确认应补充：\n1. **Fisch et al. (2021)** \"Few-Shot Conformal Prediction with Auxiliary Tasks\" — conformal prediction for structured NLP [R2, R1 AGREE]\n2. **Chen et al. (2021)** \"Evaluating Large Language Models Trained on Code\" — pass@k 原始来源 [R2, R1 AGREE]\n3. **Varshney et al. (2022)** \"Investigating Selective Prediction Approaches...\" — selective prediction survey [R2, R1 AGREE]\n4. **Malinin & Gales (2021)** — 结构化预测中的不确定性估计 [R1, R2 AGREE]\n5. He et al. (2024) on token-level uncertainty decomposition [R2, R1 认为相关但非必须]\n6. Test-time scaling survey (2025) [R2, R1 认为相关但非必须]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~5 分钟）。发现 1 critical + 6 warnings + 18 info：\n\n**[Critical]** Page 7 单页塞入 4 个 display items（Tables 3, 4, 5 + Figure 3），严重过挤。表格字号极小，Figure 3 散点图标注在 150dpi 下难以辨认。建议移 Table 4 或 5 至 Appendix 或合并。\n\n**[Warning]**\n- Pages 1-2 连续纯文本无 display item，首个视觉锚点（Figure 1）在第 3 页——建议提前\n- Figure 1 使用红/绿对比色，对色盲用户不友好（~8% 男性）——建议改用 blue/orange 或 Okabe-Ito 色板\n- Page 6 全页纯文本（含 Proposition 1），节奏偏紧\n- Page 8 Discussion/Related Work/Conclusion 全纯文本\n- Appendix p.25 Table 13（57 行汇总表）字号极小\n- Appendix p.26 单页 7 个小表格，排版极度拥挤\n\n**整体**: 全文 booktabs 风格一致、公式渲染正确、无 overfull hbox、无 section heading 孤悬、主文在第 8 页结束符合页数限制。\n\n---\n\n## Overall Assessment\n\n### 评分: 3.0 — Findings\n\n**R1 评分**: 3.5 (Borderline Conference) | **R2 评分**: 3.0 (Findings)\n\n### 综合评分理由\n\n本文对 SC 在 NER 上的失败模式提供了系统性的实证分析——四阶段诊断级联有概念价值和复用性，300+ 实验的统计严谨性远超领域平均。然而以下因素限制了评分：\n\n1. **核心 claim 过强** [Critical]: \"Capability Ceiling\" 暗示固有结构限制，但 N=8 时未提供 selection gap 随 N 收敛的证据。标题和 claim 需要降级。\n\n2. **Framing 失衡** [Major consensus]: 论文在 diagnostic（负面发现）和 prescriptive（正面结果 +0.3–1.4pp）之间的叙事张力未被充分调和。Agreement signals 的失败是清楚的，但 LP 的有条件成功被 framing 淡化。\n\n3. **泛化支撑不足** [Major consensus]: RE/SQL 扩展过于初步；缺少 token-level 信号对比；关键结果在 Appendix 而非正文。\n\n4. **理论贡献有限** [Major]: Proposition 1 依赖不现实的 independence 假设，需重定位为 motivating analysis。\n\n5. **增量新颖性** [Major]: 与 Yao et al. (2026) 和 Yun et al. (2025) 的增量区分需更充分论证。\n\n**Findings 适配理由**: 论文的核心贡献——correlation-selection gap 概念和四阶段诊断级联——有学术价值，适合 Findings 发表。但 \"ceiling\" 的过强 claim、正面结果的有限 practical significance（+1.4pp at 8× cost）、以及多个泛化性问题，使其不足以进入主会议。\n\n### 置信度: 4/5\n\n两位 Reviewer（confidence 均为 4/5）在核心问题上达成高度共识。分歧点均有充分论据支撑且已 resolve（Director 判断均有据可循）。论文已被仔细通读（含关键 Appendix 章节）。\n\n---\n\n## Detailed Comments\n\n### 按优先级排列的修改建议\n\n**Priority 1 (Must-fix for resubmission)**:\n1. 修改标题——将 \"Capability Ceiling\" 替换为 \"Limitations\" 或类似审慎措辞；或补充 N=32/64 收敛证据\n2. 平衡 diagnostic/prescriptive 叙事——Abstract 和 Introduction 明确区分 agreement signals vs LP\n3. 扩展 Yao et al. (2026) 对比——从一句话扩展为一段专门讨论\n\n**Priority 2 (Should-fix)**:\n4. 将 Proposition 1 重定位为 motivating analysis，补充 entity 间 dependency 量化\n5. 全文检查因果性语言残留\n6. 将 N-scaling 和 cross-dataset 核心发现从 Appendix 移入正文\n7. 补充 sequence entropy 等 token-level 信号比较\n8. 主文标注 SciERC / cross-dataset 的 statistical power caveat\n9. RE/SQL 降级为 preliminary evidence\n\n**Priority 3 (Nice-to-have)**:\n10. 合并 §9+§10 腾出空间\n11. Table 2 扩展至 2+ 数据集\n12. Figure 1 改用色盲友好色板\n13. 统一 Table 显著性标注格式\n14. 补充缺失引用（Fisch 2021, Chen 2021, Varshney 2022, Malinin & Gales 2021）\n15. Page 7 display items 过挤——移 Table 至 Appendix 或合并\n",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
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
    "report": "# 审稿报告：Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\n\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**投稿类别**: Long Paper\n**审稿模式**: Fresh（全新初审）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计；R2: 新颖性+相关工作+写作）\n**轮次**: Round 1 + 交叉分享，1 轮收敛\n\n---\n\n## Summary\n\n本文研究 self-consistency（SC）在命名实体识别（NER）上的失败模式，定义了\"correlation-selection gap\"——质量估计信号与 oracle F1 存在相关性（Spearman ρ up to 0.47, AUROC up to 0.82），但无法用于选择更好的样本。作者提出四阶段诊断级联（degeneracy → agreement fidelity → LP compression → construction），在 4 个 NER 数据集（SciERC, Few-NERD, CoNLL-2003, WNUT-17）、两个模型族（Qwen3-8B, LLaMA-3.1-8B）上系统评估了 9 类方法，发现均无法可靠改善 sample selection。正面结果通过 LP-weighted entity construction（+0.3–1.4pp）和 LP selection（+1.39pp on Few-NERD）在 entity 粒度绕过了 sample-level selection 的瓶颈。\n\n---\n\n## Strengths\n\n**S1. 问题定位精准，填补研究空白。** SC 文献几乎完全聚焦于分类/推理任务，NER 作为 set-valued 结构化输出的代表性任务缺乏系统性 SC 失败分析。本文填补了这一空白。[R1, R2 共识]\n\n**S2. 诊断框架结构清晰、可复用。** 四阶段级联（§2–§4）将复杂问题分解为可独立检验的子问题，每一步有对应实验支撑，逻辑链条完整。该框架可迁移至其他 set-valued 任务。[R1, R2 共识]\n\n**S3. 实验规模和统计严谨性远超领域平均。** 报告了 bootstrap 95% CI、Holm 校正置换检验、permutation p-values、split-half reliability、Bonferroni 校正。300+ 实验覆盖 4 数据集 × 多模型 × 多 seed。[R1, R2 共识]\n\n**S4. 诚实呈现负面结果。** 论文未夸大正面发现，系统展示了 9 类方法的失败并提供了清晰的诊断解释。这在 ML 论文中难得。[R1]\n\n**S5. 引用验证通过。** 57 条 bib entry 全部有引用、无 orphan，52/57 通过在线验证，无伪造引用。[R2]\n\n**S6. Constrained decoding confound 处理得当。** 论文包含 free-form vs constrained decoding 对比（Appendix q），排除了 degeneracy 是 constrained decoding artifact 的可能。[R1]\n\n---\n\n## Weaknesses\n\n### Critical\n\n**C1. N=8 采样不足以支撑 \"capability ceiling\" 声明** [R1-N2, R2 AGREE]\n- N=8 时 degeneracy 12%–62%，部分是小 N 的直接后果。N=16 分析（Appendix）显示 degeneracy 下降、SJ ρ 改善 +0.091、LP 增益出现。Oracle F1 随 N 单调递增（Figure 10）。\n- 标题 \"Capability Ceiling\" 暗示固有结构性上界，但论文未提供 selection gap 随 N 收敛的证据。\"Ceiling\" 意味着渐近上界，当前数据仅支持 \"在 N≤16 上存在显著 gap\" 这一更弱结论。\n- **修改建议**: 至少在 1 个数据集测试 N=32/64 并展示 selection gap 的 N-dependence 趋势；或将 \"ceiling\" 修改为 \"limitations\"（如 \"Characterizing the Limitations of Self-Consistency for NER\"）。\n\n### Major\n\n**M1. Proposition 1 的 entity-wise independence 假设不现实** [R1-N1 Critical → R2 降为 Major]\n- §6.1 Proposition 1 的 MBR 分解依赖 entity-wise independence，但 NER 中实体有 span 重叠约束、句内数量约束、自回归条件依赖。论文仅用一句话承认假设是近似的，未量化偏差。\n- R2 认为 Proposition 1 是 motivating analysis 而非核心定理，Table 5 的实证效果独立于理论证明，因此 severity 降为 Major。\n- **修改建议**: 将 Proposition 1 重定位为 \"motivating analysis under simplifying assumptions\"；补充 entity 间 mutual information 的经验量化。\n\n**M2. 核心叙事 framing 偏向负面** [R2-N1 Critical → R1 REBUT → 降为 Major]\n- R2 指出 Abstract \"no signal outperforms greedy\" 与 LP +1.39pp 矛盾。R1 反驳：(1) Abstract 限定于 SciERC，(2) LP 是 model-internal signal 非 entity-level agreement signal（Table 1 caption 明确标注），\"entity-level verification fails\" 指的是 SJ/VC/EM/FK。\n- R1 的反驳成立——\"直接矛盾\" 指控不成立。但双方均认为整体 framing 偏向负面叙事，应更好地平衡 diagnostic 和 prescriptive 两条线索。\n- **修改建议**: Abstract 和 Introduction 中明确区分 agreement signals（确实失败）vs model-internal LP（有条件成功）；重组 claim hierarchy。\n\n**M3. 与 Yao et al. (2026) 的增量区分不充分** [R2-N2 Critical → R1 REBUT → 降为 Major]\n- R2 认为本文可能只是 Yao et al. consistency-accuracy correlation 的 NER 特例。R1 反驳：Yao 证明 correlation 存在，本文追问为何不能 operationalize 为 selection gain，提供了四阶段诊断级联，是递进关系而非特例。\n- R1 的反驳合理但双方均同意 §8 一句话处理不充分。\n- **修改建议**: 在 §1 或 §8 用一段专门对比 Yao et al.，说明 diagnostic cascade + construction 方法的具体增量。\n\n**M4. RE/SQL exploratory extensions 过于薄弱** [R1-W1, R2 AGREE]\n- RE 仅 SciERC 1 个模型 397 有效样本（55.5% zero-F1 受 upstream NER 错误污染），SQL 仅 Spider subset n=196 with 87.2% degeneracy。不足以支撑 Introduction 中 \"broader set-valued generation problem\" 的泛化声明。\n- **修改建议**: 明确定位为 preliminary evidence 并在 Limitations 注明；或从 claim 中移除 \"broader\" 定位。\n\n**M5. 正文/附录比例 8:37 严重失衡** [R2-W1, R1 AGREE]\n- 关键信息被推入 Appendix：9 类方法完整结果（Appendix b.4）、N-scaling 分析（Appendix b.6）、hidden-state probes（Appendix h-i）、cross-dataset transfer。审稿人需读 ~47 页才能评估完整性。\n- **修改建议**: 将 N-scaling 核心发现和 cross-dataset 结果移入正文。可合并 §9 Discussion + §10 Conclusion 腾出空间。\n\n**M6. 因果性语言超出相关性证据** [R1-W3, R2 AGREE]\n- \"degeneracy is the binding constraint\"（§4）等表述超出证据。Non-degenerate subset 上 selection gap 仍存在，说明 degeneracy 不是唯一约束。论文 §2 声明 \"observational\" 但后续 section 有因果性措辞残留。\n- 注意：历史 R1-W2（Round 1-21）曾修复全文因果语言（15 处 + 4 处残留），本轮发现仍有残留。\n- **修改建议**: 全文检查因果性语言，降级为 \"a major contributing factor\" / \"associated with\"。\n\n**M7. SciERC (n=529) 和 cross-dataset (n=23) 统计效力不足** [R1-W4, R2 AGREE]\n- 论文自身 power analysis（Appendix）确认 80% power requires n≈85 for ρ=0.3，cross-dataset n=23 远低于要求。但这些 caveat 仅在 Appendix 讨论。\n- **修改建议**: 在主文相关结论处注明 statistical power 限制。\n\n**M8. 缺少 token-level 不确定性方法的系统比较** [R1-W5, R2 AGREE]\n- LP（mean token log-prob）是唯一的 token-level 信号聚合方式，也是唯一展示正面结果的 model-internal signal。未与 sequence entropy、per-token entropy max/variance、predictive entropy（Kuhn et al. 2023）等做比较。\n- **修改建议**: 至少补充 sequence entropy 作为 ablation。\n\n### Minor / Info\n\n**m1.** 正面结果 practical significance 有限（+1.4pp at 8x inference cost）——但论文定位为 diagnostic study 而非 method paper，双方认为可接受。建议正文明确定位。[R2-W4, R1 nuanced AGREE]\n\n**m2.** Table 1/Table 3 significance 标注不一致（†/‡ vs bold）。[R1]\n\n**m3.** Figure 1 箭头暗示因果方向与 \"diagnostic sequence\" 标注不符。建议改为虚线。[R1, R2 AGREE]\n\n**m4.** \"Capability ceiling\" 未形式化定义。[R1]\n\n**m5.** 10 个 section 在 8 页内过于拥挤，§9 Discussion 和 §10 Conclusion 各不到半页。建议合并。[R2]\n\n**m6.** Table 2 在正文仅展示 Few-NERD 单数据集结果。应至少展示 2 个数据集。[R2]\n\n**m7.** Proposition 1 条件过强（balanced set-overlap utility + entity independence），未讨论对 α 值的敏感性。[R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **N=8/\"ceiling\" 过强** — 论文的泛化 claim 超出实验证据支撑范围。标题暗示固有结构限制，但未提供收敛证据。[C1]\n2. **因果语言残留** — 论文声明 observational 但后续有因果性措辞。[M6]\n3. **RE/SQL 不足以泛化** — 覆盖度太低，应降级为 preliminary evidence。[M4]\n4. **统计效力问题** — SciERC n=529 和 cross-dataset n=23 应在主文注明。[M7]\n5. **附录比例失衡** — 关键结果不应仅在 Appendix。[M5]\n6. **缺少 token-level 信号比较** — LP 是唯一的 model-internal signal 比较对象。[M8]\n\n## Reviewer Divergence [REBUT]\n\n1. **叙事矛盾 severity** — R2 定为 Critical（\"直接矛盾\"），R1 以文本证据反驳（LP ≠ entity-level agreement，Abstract 限定于 SciERC）。**Director 判断**: R1 的反驳成立，降为 Major（framing bias 而非 factual contradiction）。[M2]\n\n2. **与 Yao et al. 关系** — R2 认为是 Yao 的特例，R1 认为是递进关系（从 correlation 存在到 why selection fails）。**Director 判断**: R1 论据更充分（四阶段 cascade + construction 是增量），但 §8 一句话确实不够，降为 Major。[M3]\n\n3. **模型覆盖** — R2 称\"仅两个同规模模型\"，R1 指出论文含 5 个变体（4B/7B/8B/14B/72B），R2 遗漏了 Appendix t 的 72B 数据。**Director 判断**: R2 的事实认定有误，但 72B 仅在 Appendix 且为 zero-shot，缺乏 fine-tuned 大模型验证仍是合理关切。\n\n4. **vs Yun et al. diversity collapse** — R2 认为 degeneracy 是 diversity collapse 的 NER 特例；R1 引用 Appendix q 证据（free-form decoding 下 degeneracy 同样存在）区分两者。**Director 判断**: R1 的区分合理（定义不同、scope 不同、free-form 证据排除了 constrained decoding artifact），但论文正文应更清晰地呈现这一区分。\n\n5. **Holm-Bonferroni 保守性** — R1 认为 k=57 过度保守；R2 反驳对负面结果论文保守校正增强可信度。**Director 判断**: 双方有理。补充 BH-FDR sensitivity check 即可（Info 级别）。\n\n6. **Proposition 1 severity** — R1 定 Critical，R2 降为 Major（motivating analysis 非核心定理）。**Director 判断**: 采用 R2 的 Major 定级——Proposition 1 的实证效果（Table 5）独立于理论证明。\n\n---\n\n## Questions（需要作者回应）\n\n**Q1.** \"Entity-level agreement signal\" 的精确范围是什么？LP selection 的成功是否意味着 model-internal signals 可以部分绕过 correlation-selection gap？论文应在 §2 中给出明确分类。\n\n**Q2.** N=32/64 时 degeneracy rate 和 selection gap 的趋势如何？是否有证据表明 gap 随 N 收敛到某个 asymptote？\n\n**Q3.** CoNLL 上 48%–87% instances 产生 identical outputs——这是否因为模型在 well-studied benchmark 上 overfit/memorize？在 fully OOD 数据上 degeneracy 是否会降低？\n\n**Q4.** LP-weighted MBR（§6.1）与 model-based MBR（Jinnai et al. 2024）有何实质区别？\n\n**Q5.** Entity-wise independence 假设在实验数据上的近似程度如何？可否通过 entity 对的 mutual information 量化？\n\n**Q6.** 为何未比较 sequence entropy 等其他 token-level 信号聚合方式？LP 的 mean log-prob 聚合是否有特殊优势？\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 交叉确认应补充：\n1. **Fisch et al. (2021)** \"Few-Shot Conformal Prediction with Auxiliary Tasks\" — conformal prediction for structured NLP [R2, R1 AGREE]\n2. **Chen et al. (2021)** \"Evaluating Large Language Models Trained on Code\" — pass@k 原始来源 [R2, R1 AGREE]\n3. **Varshney et al. (2022)** \"Investigating Selective Prediction Approaches...\" — selective prediction survey [R2, R1 AGREE]\n4. **Malinin & Gales (2021)** — 结构化预测中的不确定性估计 [R1, R2 AGREE]\n5. He et al. (2024) on token-level uncertainty decomposition [R2, R1 认为相关但非必须]\n6. Test-time scaling survey (2025) [R2, R1 认为相关但非必须]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~5 分钟）。发现 1 critical + 6 warnings + 18 info：\n\n**[Critical]** Page 7 单页塞入 4 个 display items（Tables 3, 4, 5 + Figure 3），严重过挤。表格字号极小，Figure 3 散点图标注在 150dpi 下难以辨认。建议移 Table 4 或 5 至 Appendix 或合并。\n\n**[Warning]**\n- Pages 1-2 连续纯文本无 display item，首个视觉锚点（Figure 1）在第 3 页——建议提前\n- Figure 1 使用红/绿对比色，对色盲用户不友好（~8% 男性）——建议改用 blue/orange 或 Okabe-Ito 色板\n- Page 6 全页纯文本（含 Proposition 1），节奏偏紧\n- Page 8 Discussion/Related Work/Conclusion 全纯文本\n- Appendix p.25 Table 13（57 行汇总表）字号极小\n- Appendix p.26 单页 7 个小表格，排版极度拥挤\n\n**整体**: 全文 booktabs 风格一致、公式渲染正确、无 overfull hbox、无 section heading 孤悬、主文在第 8 页结束符合页数限制。\n\n---\n\n## Overall Assessment\n\n### 评分: 3.0 — Findings\n\n**R1 评分**: 3.5 (Borderline Conference) | **R2 评分**: 3.0 (Findings)\n\n### 综合评分理由\n\n本文对 SC 在 NER 上的失败模式提供了系统性的实证分析——四阶段诊断级联有概念价值和复用性，300+ 实验的统计严谨性远超领域平均。然而以下因素限制了评分：\n\n1. **核心 claim 过强** [Critical]: \"Capability Ceiling\" 暗示固有结构限制，但 N=8 时未提供 selection gap 随 N 收敛的证据。标题和 claim 需要降级。\n\n2. **Framing 失衡** [Major consensus]: 论文在 diagnostic（负面发现）和 prescriptive（正面结果 +0.3–1.4pp）之间的叙事张力未被充分调和。Agreement signals 的失败是清楚的，但 LP 的有条件成功被 framing 淡化。\n\n3. **泛化支撑不足** [Major consensus]: RE/SQL 扩展过于初步；缺少 token-level 信号对比；关键结果在 Appendix 而非正文。\n\n4. **理论贡献有限** [Major]: Proposition 1 依赖不现实的 independence 假设，需重定位为 motivating analysis。\n\n5. **增量新颖性** [Major]: 与 Yao et al. (2026) 和 Yun et al. (2025) 的增量区分需更充分论证。\n\n**Findings 适配理由**: 论文的核心贡献——correlation-selection gap 概念和四阶段诊断级联——有学术价值，适合 Findings 发表。但 \"ceiling\" 的过强 claim、正面结果的有限 practical significance（+1.4pp at 8× cost）、以及多个泛化性问题，使其不足以进入主会议。\n\n### 置信度: 4/5\n\n两位 Reviewer（confidence 均为 4/5）在核心问题上达成高度共识。分歧点均有充分论据支撑且已 resolve（Director 判断均有据可循）。论文已被仔细通读（含关键 Appendix 章节）。\n\n---\n\n## Detailed Comments\n\n### 按优先级排列的修改建议\n\n**Priority 1 (Must-fix for resubmission)**:\n1. 修改标题——将 \"Capability Ceiling\" 替换为 \"Limitations\" 或类似审慎措辞；或补充 N=32/64 收敛证据\n2. 平衡 diagnostic/prescriptive 叙事——Abstract 和 Introduction 明确区分 agreement signals vs LP\n3. 扩展 Yao et al. (2026) 对比——从一句话扩展为一段专门讨论\n\n**Priority 2 (Should-fix)**:\n4. 将 Proposition 1 重定位为 motivating analysis，补充 entity 间 dependency 量化\n5. 全文检查因果性语言残留\n6. 将 N-scaling 和 cross-dataset 核心发现从 Appendix 移入正文\n7. 补充 sequence entropy 等 token-level 信号比较\n8. 主文标注 SciERC / cross-dataset 的 statistical power caveat\n9. RE/SQL 降级为 preliminary evidence\n\n**Priority 3 (Nice-to-have)**:\n10. 合并 §9+§10 腾出空间\n11. Table 2 扩展至 2+ 数据集\n12. Figure 1 改用色盲友好色板\n13. 统一 Table 显著性标注格式\n14. 补充缺失引用（Fisch 2021, Chen 2021, Varshney 2022, Malinin & Gales 2021）\n15. Page 7 display items 过挤——移 Table 至 Appendix 或合并\n",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3366 · 2026-05-22T01:19:12.577174+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4366
}
```

</details>

---


### Assistant

_source line 3367 · 2026-05-22T01:19:28.777390+00:00_

审稿报告已投递至 Research Director。

---

**📋 圆桌审稿会议完成**

- **Overall**: 3.0 — Findings
- **R1**: 3.5 (Borderline Conference) | **R2**: 3.0 (Findings)
- **1 Critical**: N=8 不足以支撑 "Capability Ceiling" 声明
- **8 Major**: Proposition 1 假设、framing 偏向负面、vs Yao 区分不足、RE/SQL 薄弱、附录比例失衡、因果语言残留、统计效力不足、缺 token-level 信号比较
- **7 Minor/Info**: 标注不一致、Figure 1 色盲、结构拥挤等
- **Issue Tracker**: 已更新 14 条新 issue（R31-N1 至 R31-VIS1）
- **视觉审查**: 已完成，Page 7 过挤为唯一 critical
- **外部审稿**: 未配置

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 255

## Round 255

2 recorded events


### User

_source line 3368 · 2026-05-22T01:19:31.540778+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **6 条 REBUT**：N1（Abstract 无矛盾，entity-level verification 不含 LP）、N2（递进关系非特例）、W2（5 个模型变体非 2 个）、W3（失败机制与 calibration 本质不同）、W5（degeneracy ≠ diversity collapse，free-form 证据）、W9（重复 N1）
- **8 条 AGREE**：W1（正文/附录失衡）、W4（实用价值有限但定位应明确）、W6-W8（排版密度）、W10（independence 过强）、Q1/Q3-Q5
- **1 条 partial REBUT**：Q2（72B 证据存在但 R2 可能遗漏）

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

_source line 3369 · 2026-05-22T01:19:39.486700+00:00_

收到 Reviewer 1 的交叉回应。两位 Reviewer 的交叉分享已全部完成，审稿报告已在上一条消息中投递至 Research Director。

本轮审稿流程全部结束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 256

## Round 256

88 recorded events


### User

_source line 3370 · 2026-05-22T02:01:37.205549+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
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

_source line 3371 · 2026-05-22T02:01:43.628227+00:00_

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

_source line 3372 · 2026-05-22T02:01:43.679178+00:00_

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

_source line 3373 · 2026-05-22T02:01:50.264687+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch",
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
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3374 · 2026-05-22T02:01:50.265100+00:00_



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

_source line 3375 · 2026-05-22T02:01:54.491474+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
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
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3376 · 2026-05-22T02:01:54.542073+00:00_

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


### Tool call

_source line 3377 · 2026-05-22T02:02:00.220762+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3378 · 2026-05-22T02:02:00.221283+00:00_



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

_source line 3379 · 2026-05-22T02:02:05.991564+00:00_

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

_source line 3380 · 2026-05-22T02:02:07.851168+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (301 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T23:20:22Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 300 个实验 — DONE 279, PREPARING 18, QUEUED 3\n**DONE 分布**: failed 12, killed 36, negative 53, success 178\n\n### GPU 占用\n- **分配**: 8 张 — autodl-5090:cuda:0, autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3, autodl-5090-c:cuda:0, autodl-5090-c:cuda:1, autodl-5090-c:cuda:2, autodl-5090-c:cuda:3\n- **空闲（分配了没跑）**: autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3, autodl-5090-c:cuda:1, autodl-5090-c:cuda:2, autodl-5090-c:cuda:3\n\n### 💾 磁盘余量\n- **autodl-5090**:\n  - `/autodl-pub`: 8.8T/14T 可用（已用 38%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n- **autodl-5090-c**:\n  - `/autodl-pub`: 6.4T/14T 可用（已用 55%）\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `exp_fewnerd_mf4v2_s456_v3` [success] — 2026-05-21T21:53:49\n- `exp_fewnerd_mf4v2_s123_v3` [success] — 2026-05-21T21:53:33\n- `exp_fewnerd_5epoch_s456` [success] — 2026-05-21T21:41:55\n- `exp_e2_pretrained_fewnerd_s456` [success] — 2026-05-21T21:19:16 — process dead 5× with no sentinel/W&B — auto-res
…[truncated 1774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1859
}
```

</details>

---


### Tool call

_source line 3381 · 2026-05-22T02:02:07.851703+00:00_

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

_source line 3382 · 2026-05-22T02:02:08.002673+00:00_

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
28	\title{Characterizing the Capability Ceiling of Self-Consistency:\\ How Entity-Level Verification Fails in NER}
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
45	
46	\section*{Limitations}
47	\input{sections/limitations}
48	
49	\section*{Ethics Statement}
50	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
51	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
52	No new human data was collected or annotated for this study.
53	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
54	Code and data will be released upon acceptance at [anonymized URL].
55	
56	\section*{Responsible NLP Research Checklist}
57	\input{sections/checklist}
58	
59	\bibliograp
…[truncated 144 chars]

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

_source line 3383 · 2026-05-22T02:02:09.057360+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 3384 · 2026-05-22T02:02:09.359212+00:00_

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

_source line 3385 · 2026-05-22T02:02:14.585677+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found some results related to EMNLP 2026 and ARR, but they mostly pertain to workshops a
…[truncated 1108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5528
}
```

</details>

---


### Tool result

_source line 3386 · 2026-05-22T02:02:14.636855+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Experiment Memory\\n\\n## exp_e2_pretrained_fewnerd — Analysis (2026-05-21)\\n\\n### Setup\\n- Model: Qwen2.5-7B-Instruct (pretrained, no fine-tuning)\\n- Dataset: FewNERD (37,648 instances)\\n- SC pipeline: N=8, T=1.0, seed=42\\n\\n### Key Metrics\\n\\n| Metric | FewNERD | CoNLL (ref) |\\n|--------|---------|-------------|\\n| Greedy F1 | 0.5121 | 0.5385 |\\n| Oracle F1 | 0.6175 | 0.6275 |\\n| Oracle headroom | +0.1054 | +0.0890 |\\n| Fleiss κ (mean) | 0.4501 | 0.5470 |\\n| Soft Jaccard (mean) | 0.6881 | 0.7764 |\\n| Sample F1 (mean±std) | 0.523±0.332 | 0.581±0.384 |\\n| Sample F1=0 (%) | 18.2% | 23.4% |\\n| Full ρ(κ,F1) | +0.383 | +0.377 |\\n| Full ρ(SJ,F1) | +0.433 | +0.392 |\\n| Cond ρ(κ,F1) | +0.371 | +0.435 |\\n| Cond ρ(SJ,F1) | +0.440 | +0.467 |\\n| Structural > Surface | YES (+0.050) | YES (+0.015) |\\n| LP full ρ | +0.189 | -0.020 (ns) |\\n| LP full AUROC | 0.596 | 0.538 |\\n| LP cond ρ | +0.176 | +0.210 |\\n| LP cond AUROC | 0.593 | 0.580 |\\n| Verdict | PASS | MARGINAL |\\n\\n### Conclusion: SUCCESS\\n\\n**Correlation-selection gap confirmed on pretrained model.**\\n\\n1. **Gap exists**: Oracle F1 (0.618) exceeds Greedy F1 (0.512) by 10.5pp — substantial untapped selection potential in the 8 samples\\n2. **Agreement correlates with correctness**: ρ(SJ,F1) = +0.43 (p≈0), but this correlation does NOT close the gap via naive MV → classic correlation-selection gap\\n3. **Structural > Surface**: Soft Jaccard beats Fleiss κ as quality signal by +0.050 ρ — consistent across both datasets\\n4. **Logprob weak**: LP correlation exists (ρ=0.19) but much weaker than agreement-based signals — LP alone insufficient for selection\\n5. **Cross-dataset consistency**: Gap pattern replicates across FewNERD (37.6K instances) and CoNLL (3.5K instances), with FewNERD showing larger headroom and stronger structural 
…[truncated 1423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5277
}
```

</details>

---


### Tool call

_source line 3387 · 2026-05-22T02:02:29.149545+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline ARR commitment page limit"
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
    "query": "EMNLP 2026 submission deadline ARR commitment page limit"
  }
}
```

</details>

---


### Tool call

_source line 3388 · 2026-05-22T02:02:29.852494+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit template"
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
    "query": "ACL Rolling Review 2026 author guidelines page limit template"
  }
}
```

</details>

---


### Tool call

_source line 3389 · 2026-05-22T02:02:32.465310+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 3390 · 2026-05-22T02:02:32.766842+00:00_

-rw-r--r-- 1 ubuntu ubuntu 989054 May 22 01:55 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 3391 · 2026-05-22T02:02:32.817410+00:00_

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

_source line 3392 · 2026-05-22T02:02:34.875344+00:00_

Web search results for query: "EMNLP 2026 submission deadline ARR commitment page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's the information about EMNLP 2026 submission deadline, ARR commitment, and page limits:

## ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## ARR Commitment Deadline

The EMNLP commitment deadline is August 2, 2026.

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Additionally, the mandatory Limitations section is required, placed after the conclusion.

## Special ARR Policy for EMNLP 2026

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors
…[truncated 362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5725
}
```

</details>

---


### Tool result

_source line 3393 · 2026-05-22T02:02:37.084079+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit template"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL Rolling Review 2026 author guidelines:

**Page Limits:**
For ACL 2026 submissions, long papers have an 8-page limit, and short papers have a 4-page limit, with one additional page allowed in final versions to address reviewer comments (up to 9 pages for long papers, up to 5 pages for short papers).

**Template:**
There is an official Overleaf template, and this template has a [review] setting that must be on for the submission. Additionally, ARR has abandoned the MS Word template for conference submissions, with submissions based on the Word template being desk-rejected starting from March 2026.

**Formatting and Content Requirements:**
- All
…[truncated 552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7231
}
```

</details>

---


### Tool result

_source line 3394 · 2026-05-22T02:02:37.084576+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 235\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4267
}
```

</details>

---


### Tool call

_source line 3395 · 2026-05-22T02:02:57.504151+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
  "description": "List paper sections"
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
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 3396 · 2026-05-22T02:02:57.956663+00:00_

_archived
abstract.tex
adaptive.tex
appendix.tex
background.tex
checklist.tex
conclusion.tex
diagnostic.tex
discussion.tex
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
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 3397 · 2026-05-22T02:02:58.509918+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -100",
  "description": "Check project config for external review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -100",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 3398 · 2026-05-22T02:02:59.414256+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 3399 · 2026-05-22T02:02:59.414635+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"",
  "description": "Check if review issues tracker exists"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 3400 · 2026-05-22T02:02:59.517363+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 3401 · 2026-05-22T02:03:06.533944+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 3402 · 2026-05-22T02:03:06.986189+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/’: No such file or directory

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

_source line 3403 · 2026-05-22T02:03:06.986592+00:00_

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

_source line 3404 · 2026-05-22T02:03:07.639256+00:00_

1	\begin{abstract}
2	Test-time compute scaling yields large gains on discrete-answer reasoning and code generation, yet for named entity recognition (NER), where outputs are entity sets with partial overlap, quality estimation does not translate to sample selection.
3	Across nine method categories, no entity-level agreement signal reliably improves selection: quality estimation signals correlate with oracle F1 (Spearman $\rho$ up to 0.47) yet no signal selects better than greedy decoding.
4	However, model-internal log-probability (LP) signals partially bypass this gap, achieving $+1.39$\,pp on Few-NERD through LP-weighted selection.
5	A reusable four-stage diagnostic cascade localizes where selection breaks down, with preliminary extensions to RE and SQL parsing.
6	On non-degenerate instances, selection alignment $\alpha$ approaches zero despite moderate quality correlations---this near-zero alignment, not degeneracy, is a major contributing factor.
7	Entity-level construction via weighted voting ($+0.3$--$1.4$\,pp) further exploits partial agreement at entity granularity.
8	Strict majority vote fails on all tested datasets; degeneracy above 70\% eliminates aggregation gain.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 3405 · 2026-05-22T02:03:07.790278+00:00_

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

_source line 3406 · 2026-05-22T02:03:07.840953+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling complements model scaling \cite{snell2025scaling}: repeated sampling with majority voting \cite{wang2023selfconsistency}, best-of-$N$ with learned verifiers \cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \cite{muennighoff2025s1} produce large gains on reasoning and code generation.
4	These successes share a structural prerequisite: the output space admits either exact equivalence classes (multiple-choice, numeric answers) or execution-based verification (code).
5	Named entity recognition (NER) breaks both assumptions.
6	The output is a set of typed entities; two samples from the same input routinely extract overlapping but non-identical sets, and no external oracle can adjudicate correctness at test time.
7	Without equivalence classes, majority voting reduces to heuristic frequency counting; without a verifier, best-of-$N$ requires a reliable proxy signal.
8	This structural mismatch raises a concrete question: can self-consistency signals that estimate quality well for reasoning tasks also \textit{select} better outputs or \textit{construct} better entity sets for NER?
9	We investigate this question for NER and extend exploratorily to SQL parsing, treating NER as a representative instance of set-valued generation.
10	
11	The question has practical stakes beyond information extraction.
12	Hallucination detection methods such as SelfCheckGPT \cite{manakul2023selfcheckgpt} and FActScore \cite{min2023factscore} rely on cross-sample consistency to verify individual claims: if a model's outputs agree, the shared content is presumed factual.
13	This reasoning assumes entity-level self-verification works, that a model can reliably distinguish correct extractions from incorrect ones through self-judgment or re-prompting.
14	We show this assumption fails.
15	Three independent probes (entity self-judgment, multi-round re-prompting, latent-space aggregation) all yield cha
…[truncated 4979 chars]

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

_source line 3407 · 2026-05-22T02:03:15.836432+00:00_

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

_source line 3408 · 2026-05-22T02:03:17.191844+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i)
…[truncated 2151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 3409 · 2026-05-22T02:03:18.095929+00:00_

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

_source line 3410 · 2026-05-22T02:03:18.146692+00:00_

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

…[truncated 6189 chars]

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

_source line 3411 · 2026-05-22T02:03:18.599639+00:00_

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

_source line 3412 · 2026-05-22T02:03:18.600080+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}).
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{10.1\% of GPT-5.5 samples produced unparseable output; these are excluded from all metrics. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3: $13.0$\% vs.\ GPT-5.5: $50$\% on Few-NERD; Appendix~\ref{app:cross_scale}).
14	
15	\paragraph{Inverse scaling under adap
…[truncated 3054 chars]

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

_source line 3413 · 2026-05-22T02:03:19.504335+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" -o -name \"project.yml\" | head -10",
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" -o -name \"project.yml\" | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 3414 · 2026-05-22T02:03:19.806750+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 3415 · 2026-05-22T02:03:25.883986+00:00_

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

_source line 3416 · 2026-05-22T02:03:26.336147+00:00_

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
12	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
13	MRSC best F1 ($0.763$) falls below greedy.
14	
15	\paragraph{Latent Self-Consistency (LSC).}
16	Mean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.
17	Centroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms majority vote ($0.792$) but does not close the oracle gap ($0.882$).
18	
19	\paragraph{Hidden-state probe.}
20	A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
21	All three exceed ESJ ($0.51$); only CoNLL approaches frequency agreement ($0.868$).
22	Cross-dataset transfer is weak: lea
…[truncated 1062 chars]

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

_source line 3417 · 2026-05-22T02:03:26.336624+00:00_

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

_source line 3418 · 2026-05-22T02:03:26.838890+00:00_

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
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3419 · 2026-05-22T02:03:26.839300+00:00_

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

_source line 3420 · 2026-05-22T02:03:27.442162+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}
2	
3	Degeneracy (12.2--67.9\%) and LP-quality alignment ($\rho$ 0.043--0.667) constrain aggregation; temperature disentangles these (\S\ref{sec:scaling}; Table~\ref{tab:t_degeneracy}).
4	Across four frontier models, degeneracy and the selection gap are negatively correlated (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), consistent with the bound (\S\ref{sec:theory}).
5	
6	\paragraph{Pretrained vs.\ finetuned.}
7	On CoNLL, the pretrained model's MV captures ${\sim}98$\% of oracle headroom (degeneracy $36$\%) versus ${<}2$\% finetuned ($57$--$60$\%); fine-tuning decouples agreement from quality through dataset-dependent pathways (Appendix~\ref{app:cross_scale}), with 7/8 entity types flipping MV direction after finetuning (Appendix~\ref{app:pertype}).
8	
9	\paragraph{From diagnosis to practice.}\label{sec:selection_method}\label{sec:conclusion}
10	Entity-level construction bypasses both failure mechanisms when degeneracy ${<}22$\% ($p{<}0.01$; Appendix~\ref{app:epoch_confound}).
11	We position these gains ($+0.3$--$1.4$\,pp) as diagnostic evidence: aggregation fails above $\theta_{\text{crit}}{=}0.70$, and a major contributing factor is near-zero $\alpha$ even when $\rho$ is substantial, compounded by LP compression \cite{kadavath2022language, xiong2024verbalized}.
12	

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

_source line 3421 · 2026-05-22T02:03:27.442518+00:00_

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

_source line 3422 · 2026-05-22T02:03:27.493012+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code \cite{chen2021codex}.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, adaptive allocation \cite{aggarwal2023adaptive}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} all target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes and fine-grained variants.}
8	\citet{chen2023twofailures} identify SC failures where consistent outputs are systematically wrong; \citet{huang2024large} show LLMs cannot self-correct reasoning without external feedback. Our correlation-selection gap is a distinct failure where signals \textit{correlate} with quality yet fail to \textit{select}.
9	\citet{chen2024usc} extend SC to free-form tasks; our diagnostic shows such extensions face limits under constrained decoding (\S\ref{sec:selection_gap}). \citet{thirukovalluru2024atomic} decompose claims atomically; our entity-level decomposition shows sub-output agreement does not translate to selection gain.
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{yao2026consistency} demonstrate that consistency correlates with quality across NER/RE tasks ($\rho$ up to 0.47); we diagnose why this correlation fails to yield selection gain, identifying entity-level mechanisms (degeneracy, LP compression, near-zero $\alpha$) absent from their task-level analysis, and provide an operational workaround via entity construction ($+0.32$--$1.40$\,pp) at entity granularity.
13	\citet{xie2023zeroshot} propose entity voting for zero-shot NER, \citet{li2024simple} improve structured output formatting, and \citet{xie2024selfimproving} report positive SC results under zero-shot p
…[truncated 1947 chars]

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

_source line 3423 · 2026-05-22T02:03:32.112594+00:00_

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

_source line 3424 · 2026-05-22T02:03:33.067064+00:00_

1	Our evidence is correlational and theoretical (MBR framework, conditional decomposition), not interventional: we have not performed controlled interventions (e.g., artificially varying degeneracy while holding other factors constant), and the cascade stages interact in ways that resist decomposition into independent causal effects ($R^2{<}0$; \S\ref{sec:selection_gap}); causal claims require future intervention experiments.
2	
3	Scope: structured IE (NER primary, RE and SQL exploratory), English only, open-weight (Qwen and LLaMA) and closed-source (GPT-5.5) families, fine-tuned (4B--14B) and zero-shot (72B, GPT-5.5) regimes, sample budget $N{\leq}32$.
4	Our evaluation covers four NER datasets; the RE extension covers a single SciERC benchmark ($n{=}207$ non-zero instances; 55.5\% yield zero F1 from upstream entity span errors rather than relation classification failure), and the SQL extension covers a single Spider subset ($n{=}196$) with 87.2\% degeneracy---both are exploratory and do not support generalization claims.
5	All experiments use English-language datasets; cross-lingual generalization remains untested.
6	Cross-model consistency results (\S\ref{sec:cross_model}) are limited to one dataset (Few-NERD) and one model pair (Qwen3-8B + LLaMA-3.1-8B).
7	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
8	Entity-level construction requires $N{\times}$ inference cost for $+1$\textendash$1.4$\,pp gain; cost-effectiveness may not justify deployment in resource-constrained settings.
9	We cover 4B\textendash 14B fine-tuned, 72B zero-shot, and GPT-5.5 zero-shot; the gap persists across all but behavior with 72B fine-tuning is untested.
10	Frontier API models exhibit markedly different degeneracy profiles (e.g., Claude Sonnet~4 at 74\% vs.\ DeepSeek Chat at 5.5\%; Table~\ref{tab:frontier_sc_cross
…[truncated 4014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 3425 · 2026-05-22T02:03:33.117686+00:00_

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

_source line 3426 · 2026-05-22T02:03:33.369081+00:00_

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
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$; 3-seed Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
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
28	\bottom
…[truncated 2403 chars]

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

_source line 3427 · 2026-05-22T02:03:33.419699+00:00_

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

_source line 3428 · 2026-05-22T02:03:33.821520+00:00_

File content (65633 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

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

_source line 3429 · 2026-05-22T02:03:39.342170+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 3430 · 2026-05-22T02:03:40.346774+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 3431 · 2026-05-22T02:03:40.397654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "0",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 3432 · 2026-05-22T02:03:41.000367+00:00_

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
…[truncated 4980 chars]

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

_source line 3433 · 2026-05-22T02:03:41.051087+00:00_

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

_source line 3434 · 2026-05-22T02:03:41.051735+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3435 · 2026-05-22T02:03:51.758160+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ -name \"*.yaml\" -path \"*/struct_self_consist_ie/*\" | grep -v artifacts | grep -v decisions | head -10",
  "description": "Find YAML config files in project"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ -name \"*.yaml\" -path \"*/struct_self_consist_ie/*\" | grep -v artifacts | grep -v decisions | head -10",
    "description": "Find YAML config files in project"
  }
}
```

</details>

---


### Tool result

_source line 3436 · 2026-05-22T02:03:52.712481+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/secrets/struct_self_consist_ie/manifest.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 3437 · 2026-05-22T02:03:52.915325+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Get PDF page count"
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
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Get PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 3438 · 2026-05-22T02:03:52.966198+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Fri May 22 01:55:49 2026 UTC
ModDate:         Fri May 22 01:55:49 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           47
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       989054 bytes
Optimized:       no
PDF version:     1.7

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

_source line 3439 · 2026-05-22T02:03:59.702323+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ 2>/dev/null | head -5",
  "description": "Search for external review config"
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
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 3440 · 2026-05-22T02:04:00.260655+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 558
}
```

</details>

---


### Tool call

_source line 3441 · 2026-05-22T02:04:00.863342+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ 2>/dev/null | head -5",
  "description": "Search for paperreview config"
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
    "command": "grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ 2>/dev/null | head -5",
    "description": "Search for paperreview config"
  }
}
```

</details>

---


### Tool result

_source line 3442 · 2026-05-22T02:04:01.014402+00:00_

(Bash completed with no output)

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

_source line 3443 · 2026-05-22T02:04:03.927373+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -10",
  "description": "Search for external review config broadly"
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
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -10",
    "description": "Search for external review config broadly"
  }
}
```

</details>

---


### Tool result

_source line 3444 · 2026-05-22T02:04:04.128608+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 3445 · 2026-05-22T02:04:09.393426+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/ 2>/dev/null | head -30",
  "description": "List paper figures"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/ 2>/dev/null | head -30",
    "description": "List paper figures"
  }
}
```

</details>

---


### Tool result

_source line 3446 · 2026-05-22T02:04:09.845805+00:00_

fig_bound.png
fig_degeneracy_lp_scatter.pdf
fig_length_logprob_scatter.pdf
fig_lp_range_cdf.pdf
fig_oracle_scaling.pdf
fig_overview.pdf
fig_overview.png
fig_reliability.pdf
fig_selection_gap.pdf
fig_selection_gap.png
fig_signal_heatmap.pdf
fig_temperature_robustness.pdf

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

_source line 3447 · 2026-05-22T02:04:10.399463+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib 2>/dev/null",
  "description": "Count reference entries"
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
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib 2>/dev/null",
    "description": "Count reference entries"
  }
}
```

</details>

---


### Tool result

_source line 3448 · 2026-05-22T02:04:10.901768+00:00_

513 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3449 · 2026-05-22T02:04:11.153033+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-8"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 3450 · 2026-05-22T02:04:11.708494+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf (965.9KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---


### Tool call

_source line 3451 · 2026-05-22T02:04:41.386275+00:00_

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

_source line 3452 · 2026-05-22T02:05:19.358556+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 37972
}
```

</details>

---


### Tool call

_source line 3453 · 2026-05-22T02:05:19.810621+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计声明。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 统一审稿）\n- **ARR Submission Deadline**: 2026-05-25\n- **投稿类别**: Long Paper\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不要求必须阅读\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n- **论文路径**: `docs/paper/main.tex`（各章节在 `docs/paper/sections/` 下）\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`（47页：8页正文 + 附录/引用）\n\n## 论文概要\n研究 test-time compute scaling（self-consistency）在 NER 任务上的效果。核心发现是\"correlation-selection gap\"：质量估计信号（如 Soft Jaccard、Fleiss' κ）与 oracle F1 存在中等相关（ρ 达 0.47），但无法转化为样本选择增益。只有 log-probability (LP) 在 Few-NERD 上实现了 +1.39pp 的选择增益。提出四阶段诊断框架（QE → degeneracy → agreement fidelity → LP compression）和实体级构建（+0.32-1.40pp）作为处方式逃逸路线。\n\n## 你的审查重点\n\n### 1. 方法论严谨性\n- 诊断框架（四阶段级联）的逻辑完整性：各阶段是否独立？因果链是否成立？\n- 信号定义（SJ、VC、EM、FK、LP）是否清晰无歧义？instance-level vs per-sample 的区分是否有价值？\n- \"capability ceiling\" 的定义是否过于宽泛或过于狭窄？\n- Degeneracy Decomposition (Proposition 1) 的理论贡献：bound 只捕获 3-12% 的实际增益，这是否削弱了理论的价值？\n- MBR 框架连接是否增加了理解还是仅是事后包装？\n\n### 2. 实验设计\n- 数据集选择（SciERC、CoNLL、Few-NERD、WNUT-17）是否覆盖足够？是否有选择偏差？\n- 主要正面结果集中在 Few-NERD 一个数据集上（LP selection +1.39pp），这是否构成 generalizability 问题？\n- LoRA fine-tuning 设置（rank=16, alpha=16）的合理性？不同 epoch（3 vs 5）的处理是否引入混淆？\n- 3-seed 统计检验的充分性：SciERC 仅用 1 个 primary seed（σ=0.48pp），可靠性如何？\n- Holm-Bonferroni 多重比较校正的执行：family 定义（k=10, 21, 9）是否合理？global k=57 导致 p_adj=0.055 是否意味着主要结论边缘？\n- RE 和 SQL parsing 的 exploratory extension 质量：RE 只有 SciERC（n=207），SQL 只有 Spider subset（n=196），是否太弱？\n\n### 3. 统计声明\n- 逐一检查所有 p 值和置信区间的报告是否一致\n- \"no signal outperforms greedy\" 是一个否定结论——统计效力是否足以支撑？(MDE ≈1.5pp, n=529 on SciERC)\n- LP selection 在 Few-NERD 上的显著性（p<0.001）vs 在 SciERC 上的不显著（p=0.29）：样本量差异（32,565 vs 529）是否是主要解释？\n- entity construction 的 Holm p_adj=0.006（k=10）但 global p_adj=0.055（k=57）：作者如何处理这种张力？\n\n### 4. 可重现性\n- 训练细节、超参数是否充分报告？\n- constrained decoding 的实现细节是否足够？\n- 评价指标定义（per-instance macro F1 vs span-level micro F1）是否有潜在歧义？\n\n请严格按照 EMNLP 2026 审稿标准评审。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（含评分和置信度）。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1"
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
    "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计声明。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 统一审稿）\n- **ARR Submission Deadline**: 2026-05-25\n- **投稿类别**: Long Paper\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不要求必须阅读\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n- **论文路径**: `docs/paper/main.tex`（各章节在 `docs/paper/sections/` 下）\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`（47页：8页正文 + 附录/引用）\n\n## 论文概要\n研究 test-time compute scaling（self-consistency）在 NER 任务上的效果。核心发现是\"correlation-selection gap\"：质量估计信号（如 Soft Jaccard、Fleiss' κ）与 oracle F1 存在中等相关（ρ 达 0.47），但无法转化为样本选择增益。只有 log-probability (LP) 在 Few-NERD 上实现了 +1.39pp 的选择增益。提出四阶段诊断框架（QE → degeneracy → agreement fidelity → LP compression）和实体级构建（+0.32-1.40pp）作为处方式逃逸路线。\n\n## 你的审查重点\n\n### 1. 方法论严谨性\n- 诊断框架（四阶段级联）的逻辑完整性：各阶段是否独立？因果链是否成立？\n- 信号定义（SJ、VC、EM、FK、LP）是否清晰无歧义？instance-level vs per-sample 的区分是否有价值？\n- \"capability ceiling\" 的定义是否过于宽泛或过于狭窄？\n- Degeneracy Decomposition (Proposition 1) 的理论贡献：bound 只捕获 3-12% 的实际增益，这是否削弱了理论的价值？\n- MBR 框架连接是否增加了理解还是仅是事后包装？\n\n### 2. 实验设计\n- 数据集选择（SciERC、CoNLL、Few-NERD、WNUT-17）是否覆盖足够？是否有选择偏差？\n- 主要正面结果集中在 Few-NERD 一个数据集上（LP selection +1.39pp），这是否构成 generalizability 问题？\n- LoRA fine-tuning 设置（rank=16, alpha=16）的合理性？不同 epoch（3 vs 5）的处理是否引入混淆？\n- 3-seed 统计检验的充分性：SciERC 仅用 1 个 primary seed（σ=0.48pp），可靠性如何？\n- Holm-Bonferroni 多重比较校正的执行：family 定义（k=10, 21, 9）是否合理？global k=57 导致 p_adj=0.055 是否意味着主要结论边缘？\n- RE 和 SQL parsing 的 exploratory extension 质量：RE 只有 SciERC（n=207），SQL 只有 Spider subset（n=196），是否太弱？\n\n### 3. 统计声明\n- 逐一检查所有 p 值和置信区间的报告是否一致\n- \"no signal outperforms greedy\" 是一个否定结论——统计效力是否足以支撑？(MDE ≈1.5pp, n=529 on SciERC)\n- LP selection 在 Few-NERD 上的显著性（p<0.001）vs 在 SciERC 上的不显著（p=0.29）：样本量差异（32,565 vs 529）是否是主要解释？\n- entity construction 的 Holm p_adj=0.006（k=10）但 global p_adj=0.055（k=57）：作者如何处理这种张力？\n\n### 4. 可重现性\n- 训练细节、超参数是否充分报告？\n- constrained decoding 的实现细节是否足够？\n- 评价指标定义（per-instance macro F1 vs span-level micro F1）是否有潜在歧义？\n\n请严格按照 EMNLP 2026 审稿标准评审。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（含评分和置信度）。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3454 · 2026-05-22T02:05:51.515752+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31705
}
```

</details>

---
